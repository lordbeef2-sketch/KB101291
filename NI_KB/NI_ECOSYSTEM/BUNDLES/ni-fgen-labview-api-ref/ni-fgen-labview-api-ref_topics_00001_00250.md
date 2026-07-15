# NI DOCUMENT BUNDLE: ni-fgen-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-fgen-labview-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=api-reference.html language=enus -->
## TOPIC 00001: NI-FGEN LabVIEW API Reference

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `api-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/api-reference.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This API reference provides information about the programmatic elements available for this product. Looking for Something Else? For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse R

### NI-FGEN LabVIEW API Reference

This API reference provides information about the programmatic elements available for this product.

#### Looking for Something Else?

For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse *Related Information*.

Related information:

- NI-FGEN Driver Downloads
- NI-FGEN Release Notes
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/dir-mnu.html language=enus -->
## TOPIC 00002: NI-FGEN

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/dir-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN VIs to develop applications for your NI signal generator.

### NI-FGEN

Use the NI-FGEN VIs to develop applications for your NI signal generator.

- [niFgen Initialize VI](../../instr-lib/nifgen/nifgen-llb/nifgen-initialize-vi.html) Performs the following initialization actions:
- [Configuration](../../instr-lib/nifgen/nifgen-config-mnu.html) Use the NI-FGEN Configuration VIs to configure the analog and digital output, clocking, triggering and synchronization, and onboard signal processing of your signal generator.
- [Waveform Control](../../instr-lib/nifgen/nifgen-generate-waveforms-mnu.html) Use the NI-FGEN Waveform Control VIs to configure and control the generation of standard functions, arbitrary waveforms, arbitrary sequences, frequency lists, and scripts on your signal generator.
- [niFgen Close VI](../../instr-lib/nifgen/nifgen-llb/nifgen-close-vi.html) Performs the following operations:
- [niFgen Initialize With Options VI](../../instr-lib/nifgen/nifgen-llb/nifgen-initialize-with-options-vi.html) Performs the following initialization actions:
- [Utility](../../instr-lib/nifgen/nifgen-utility-mnu.html) Use the NI-FGEN Utility VIs to control common instrument operations. These operations include many that VXIplug&play require, such as reset, self-test, revision query, and error message. This palette also contains VIs that create waveform data.
- [niFgen Property Node VI](../../instr-lib/nifgen/nifgen-llb/nifgen-property-node-vi.html) Sets or gets properties of instruments or channels. For multi-channel sessions in which you want to configure subsets of channels differently, you must wire an Active Channel of an NI-FGEN property node. The Active Channel is listed first in the property node.
- [Calibration](../../instr-lib/nifgen/nifgen-calibration-mnu.html) Use the NI-FGEN Calibration VIs to calibrate NI signal generators. Different signal generators use different calibration VIs. Refer to your signal generator calibration procedure for more information.
- [niFgen Initialize With Channels VI](../../instr-lib/nifgen/nifgen-llb/nifgen-initialize-with-channels-vi.html) Creates and returns a new NI-FGEN session to the specified channel of a waveform generator that is used in all subsequent NI-FGEN VI calls.

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/adc-cal-adjust-vi.html language=enus -->
## TOPIC 00003: ADC Cal Adjust VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/adc-cal-adjust-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/adc-cal-adjust-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measures the generated voltage of a PXIe-5413/5423/5433 with the onboard calibration ADC and compares it to the actual voltage measured by the external DMM, performs any required adjustments to the ADC, and computes any calibration coefficients that will be stored in the onboard memory when the cali

### ADC Cal Adjust VI

Measures the generated voltage of a PXIe-5413/5423/5433 with the onboard calibration ADC and compares it to the actual voltage measured by the
external DMM, performs any required adjustments to the ADC, and computes any calibration coefficients that will be stored in the onboard memory when the calibration session is committed.

This VI also indicates if ADC calibration is complete. You must repeat the ADC calibration adjustment procedure steps until this VI returns TRUE for ADC cal complete.

[IMAGE alt='icon' src='adc-cal-adjust-vi.png']

#### Inputs/Outputs

| external cal session in — External Cal Session In identifies an external calibration session. measured voltage — Measured Voltage specifies the voltage of the analog output signal generated at a specified channel of the waveform generator as measured by the DMM connected to the channel being calibrated. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. external cal session out — External Cal Session Out returns a reference to your external calibration session to wire to the next VI. ADC cal complete — ADC Cal Complete returns TRUE if ADC calibration is complete. If this parameter returns FALSE, you must repeat calls to the ADC Cal Configure and ADC Cal Adjust VIs until ADC calibration is complete. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/adc-cal-configure-vi.html language=enus -->
## TOPIC 00004: ADC Cal Configure VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/adc-cal-configure-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/adc-cal-configure-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the channel of the PXIe-5413/5423/5433 specified with the ADC Cal Initialize VI and then returns a value for approximate voltage generated, which is used to program the range of a DMM connected to the previously specified channel. icon Inputs/Outputs cni5433_Ext_Cal_APIlvclass.png externa

### ADC Cal Configure VI

Configures the channel of the PXIe-5413/5423/5433 specified with the [ADC Cal Initialize](/csh?topicname=adc-cal-initialize-vi.html) VI and then returns a value for approximate voltage generated, which is used to program the range of a DMM connected to the previously specified channel.

[IMAGE alt='icon' src='adc-cal-configure-vi.png']

#### Inputs/Outputs

| external cal session in — External Cal Session In identifies an external calibration session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. external cal session out — External Cal Session Out returns a reference to your external calibration session to wire to the next VI. approximate voltage generated — Approximate Voltage Generated returns a value for the approximate voltage of the analog output signal generated at a specified channel of the waveform generator to be used to program the range of the DMM connected to the channel being calibrated. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/adc-cal-initialize-vi.html language=enus -->
## TOPIC 00005: ADC Cal Initialize VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/adc-cal-initialize-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/adc-cal-initialize-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an external calibration session for ADC calibration on a specified channel or channels of a PXIe-5413/5423/5433. icon Inputs/Outputs cni5433_Ext_Cal_APIlvclass.png external cal session in External Cal Session In identifies an external calibration session. cu32.png channel Channel identif

### ADC Cal Initialize VI

Initializes an external calibration session for ADC calibration on a specified channel or channels of a PXIe-5413/5423/5433.

[IMAGE alt='icon' src='adc-cal-initialize-vi.png']

#### Inputs/Outputs

| external cal session in — External Cal Session In identifies an external calibration session. channel — Channel identifies the channel of the previously specified waveform generator to use for calibration. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. external cal session out — External Cal Session Out returns a reference to your external calibration session to wire to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/close-ext-cal-session-vi.html language=enus -->
## TOPIC 00006: Close Ext Cal Session VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/close-ext-cal-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/close-ext-cal-session-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an NI-FGEN external calibration session to PXIe-5413/5423/5433 waveform generators. If specified, this VI stores the new calibration constants and calibration data, such as time and temperature, in the onboard memory. icon Inputs/Outputs cni5433_Ext_Cal_APIlvclass.png external cal session Ext

### Close Ext Cal Session VI

Closes an NI-FGEN external calibration session to PXIe-5413/5423/5433 waveform generators. If specified, this VI stores the new calibration constants and calibration data, such as time and temperature, in the onboard memory.

[IMAGE alt='icon' src='close-ext-cal-session-vi.png']

#### Inputs/Outputs

| external cal session — External Cal Session identifies an external calibration session. action — Action specifies the action to perform upon closing. Input Description Abort Disregards the new calibration constants before closing Commit Stores the new calibration constants on the device before closing error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input | Description |
| Abort | Disregards the new calibration constants before closing |
| Commit | Stores the new calibration constants on the device before closing |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/flatness-cal-adjust-vi.html language=enus -->
## TOPIC 00007: Flatness Cal Adjust VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/flatness-cal-adjust-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/flatness-cal-adjust-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the externally measured power of a signal generated by a PXIe-5413/5423/5433, performs any required adjustments, and computes any calibration constants in the onboard memory. This VI also indicates if flatness calibration is complete. You must repeat the flatness calibration adjustment procedu

### Flatness Cal Adjust VI

Saves the externally measured power of a signal generated by a PXIe-5413/5423/5433, performs any required adjustments, and computes any calibration constants in the onboard memory.

This VI also indicates if flatness calibration is complete. You must repeat the flatness calibration adjustment procedure steps until this VI returns TRUE for flatness cal complete.

[IMAGE alt='icon' src='flatness-cal-adjust-vi.png']

#### Inputs/Outputs

| external cal session in — External Cal Session In identifies an external calibration session. measured power (dBm) — Measured Power (dBm) specifies the power in dBM of the analog output signal generated by the waveform generator as measured by the power sensor connected to the waveform generator. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. external cal session out — External Cal Session Out returns a reference to your external calibration session to wire to the next VI. flatness cal complete — Flatness Cal Complete returns TRUE if flatness calibration is complete. If this parameter returns FALSE, you must repeat calls to the Flatness Cal Configure and Flatness Cal Adjust VIs until flatness calibration is complete. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/flatness-cal-configure-vi.html language=enus -->
## TOPIC 00008: Flatness Cal Configure VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/flatness-cal-configure-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/flatness-cal-configure-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the PXIe-5413/5423/5433 for an iteration of the flatness calibration step. icon Inputs/Outputs cni5433_Ext_Cal_APIlvclass.png external cal session in External Cal Session In identifies an external calibration session. cerrcodeclst.png error in error in describes error conditions that occu

### Flatness Cal Configure VI

Configures the PXIe-5413/5423/5433 for an iteration of the flatness calibration step.

[IMAGE alt='icon' src='flatness-cal-configure-vi.png']

#### Inputs/Outputs

| external cal session in — External Cal Session In identifies an external calibration session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. external cal session out — External Cal Session Out returns a reference to your external calibration session to wire to the next VI. current configuration — Current Configuration returns the current configuration of the waveform generator, including the channel being calibrated, the expected voltage range (Vpk-pk), the expected frequency, and whether the configuration is valid in the current iteration of the flatness calibration step. Use this information to configure the DMM to measure the voltage range and frequency of the signal on the specified channel. channel — expected vpp — frequency — valid — next configuration — Next Configuration returns the next expected configuration of the waveform generator, including the channel being calibrated, the expected voltage range (Vpk-pk), the expected frequency, and whether the configuration will be valid in the next iteration of the flatness calibration step. Use this information to determine if the next configuration is within the limits of the DMM. channel — expected vpp — frequency — valid — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| channel — expected vpp — frequency — valid — |
| channel — expected vpp — frequency — valid — |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/flatness-cal-initialize-vi.html language=enus -->
## TOPIC 00009: Flatness Cal Initialize VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/flatness-cal-initialize-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/flatness-cal-initialize-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an external calibration session for flatness calibration on all available channels of a PXIe-5413/5423/5433. icon Inputs/Outputs cni5433_Ext_Cal_APIlvclass.png external cal session in External Cal Session In identifies an external calibration session. cerrcodeclst.png error in error in d

### Flatness Cal Initialize VI

Initializes an external calibration session for flatness calibration on all available channels of a PXIe-5413/5423/5433.

[IMAGE alt='icon' src='flatness-cal-initialize-vi.png']

#### Inputs/Outputs

| external cal session in — External Cal Session In identifies an external calibration session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. external cal session out — External Cal Session Out returns a reference to your external calibration session to wire to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/get-user-info-vi.html language=enus -->
## TOPIC 00010: Get User Info VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/get-user-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/get-user-info-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves user-defined information previously set by the Set User Info VI from the onboard memory. icon Inputs/Outputs cni5433_Ext_Cal_APIlvclass.png external cal session in External Cal Session In identifies an external calibration session. cerrcodeclst.png error in error in describes error conditi

### Get User Info VI

Retrieves user-defined information previously set by the [Set User Info](/csh?topicname=set-user-info-vi.html) VI from the onboard memory.

[IMAGE alt='icon' src='get-user-info-vi.png']

#### Inputs/Outputs

| external cal session in — External Cal Session In identifies an external calibration session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. external cal session out — External Cal Session Out returns a reference to your external calibration session to wire to the next VI. user info — User Info is a string containing the user information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/ni5433-ext-cal-api-mnu.html language=enus -->
## TOPIC 00011: PXIe-5433 Ext Cal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/ni5433-ext-cal-api-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/ni5433-ext-cal-api-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN ni5433 Ext Cal VIs to perform external ADC, timebase, and flatness calibration on PXIe-5413/5423/5433 waveform generators. icon

### PXIe-5433 Ext Cal

Use the NI-FGEN ni5433 Ext Cal VIs to perform external ADC, timebase, and flatness calibration on PXIe-5413/5423/5433 waveform generators.

[IMAGE alt='icon' src='ni5433-ext-cal-api-mnu.png']

- [Open Ext Cal Session VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/open-ext-cal-session-vi.html) Opens an external calibration session for a PXIe-5413, PXIe-5423, or PXIe-5433 waveform generator. This VI resets the device and downloads the calibration bitstream to the device if it is not already present.
- [Close Ext Cal Session VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/close-ext-cal-session-vi.html) Closes an NI-FGEN external calibration session to PXIe-5413/5423/5433 waveform generators. If specified, this VI stores the new calibration constants and calibration data, such as time and temperature, in the onboard memory.
- [ADC Cal Initialize VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/adc-cal-initialize-vi.html) Initializes an external calibration session for ADC calibration on a specified channel or channels of a PXIe-5413/5423/5433.
- [ADC Cal Configure VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/adc-cal-configure-vi.html) Configures the channel of the PXIe-5413/5423/5433 specified with the ADC Cal Initialize VI and then returns a value for approximate voltage generated, which is used to program the range of a DMM connected to the previously specified channel.
- [ADC Cal Adjust VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/adc-cal-adjust-vi.html) Measures the generated voltage of a PXIe-5413/5423/5433 with the onboard calibration ADC and compares it to the actual voltage measured by the external DMM, performs any required adjustments to the ADC, and computes any calibration coefficients that will be stored in the onboard memory when the calibration session is committed.
- [Timebase Cal Initialize VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/timebase-cal-initialize-vi.html) Initializes an external calibration session for timebase calibration on a specified channel of a PXIe-5413/5423/5433.
- [Timebase Cal Configure VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/timebase-cal-configure-vi.html) Configures the channel of the PXIe-5413/5423/5433 specified with the Timebase Cal Initialize VI and then returns a value for approximate frequency generated, which is used to program an oscilloscope (external timebase calibration source) that can measure a 5.5 V pk-pk sine wave of the returned frequency.
- [Timebase Cal Adjust VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/timebase-cal-adjust-vi.html) Measures the generated frequency of a PXIe-5413/5423/5433 and compares it to the actual frequency measured by the oscilloscope, performs any required adjustments to the internal TCXO, and computes any calibration constants in the onboard memory.
- [Flatness Cal Initialize VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/flatness-cal-initialize-vi.html) Initializes an external calibration session for flatness calibration on all available channels of a PXIe-5413/5423/5433.
- [Flatness Cal Configure VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/flatness-cal-configure-vi.html) Configures the PXIe-5413/5423/5433 for an iteration of the flatness calibration step.
- [Flatness Cal Adjust VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/flatness-cal-adjust-vi.html) Saves the externally measured power of a signal generated by a PXIe-5413/5423/5433, performs any required adjustments, and computes any calibration constants in the onboard memory.
- [Set User Info VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/set-user-info-vi.html) Stores user-defined information in the onboard memory.
- [Get User Info VI](../../../../instr-lib/nifgen/ni5433/external-cal-api/get-user-info-vi.html) Retrieves user-defined information previously set by the Set User Info VI from the onboard memory.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/open-ext-cal-session-vi.html language=enus -->
## TOPIC 00012: Open Ext Cal Session VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/open-ext-cal-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/open-ext-cal-session-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens an external calibration session for a PXIe-5413, PXIe-5423, or PXIe-5433 waveform generator. This VI resets the device and downloads the calibration bitstream to the device if it is not already present. icon Inputs/Outputs cstr.png calibration password Calibration Password specifies the passwo

### Open Ext Cal Session VI

Opens an external calibration session for a PXIe-5413, PXIe-5423, or PXIe-5433 waveform generator. This VI resets the device and downloads the calibration bitstream to the device if it is not already present.

[IMAGE alt='icon' src='open-ext-cal-session-vi.png']

#### Inputs/Outputs

| calibration password — Calibration Password specifies the password used to write calibration constants to onboard memory when the Action parameter of the Close Ext Cal Session VI is set to Commit. Calibration Password must be correct to commit calibration constants to onboard memory and overwrite calibration constants from a previous calibration session. device in — Device In identifies the waveform generator to open an external calibation session to. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. external cal session — External Cal Session is a reference to your external calibration session to wire to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/set-user-info-vi.html language=enus -->
## TOPIC 00013: Set User Info VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/set-user-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/set-user-info-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores user-defined information in the onboard memory. You can retrieve information stored by this VI using the Get User Info VI. icon Inputs/Outputs cni5433_Ext_Cal_APIlvclass.png external cal session in External Cal Session In identifies an external calibration session. cstr.png user info User Inf

### Set User Info VI

Stores user-defined information in the onboard memory.

You can retrieve information stored by this VI using the [Get User Info](get-user-info-vi.html) VI.

[IMAGE alt='icon' src='set-user-info-vi.png']

#### Inputs/Outputs

| external cal session in — External Cal Session In identifies an external calibration session. user info — User Info specifies the information string to be stored in the onboard memory. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. external cal session out — External Cal Session Out returns a reference to your external calibration session to wire to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/timebase-cal-adjust-vi.html language=enus -->
## TOPIC 00014: Timebase Cal Adjust VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/timebase-cal-adjust-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/timebase-cal-adjust-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measures the generated frequency of a PXIe-5413/5423/5433 and compares it to the actual frequency measured by the oscilloscope, performs any required adjustments to the internal TCXO, and computes any calibration constants in the onboard memory. This VI also indicates if timebase calibration is comp

### Timebase Cal Adjust VI

Measures the generated frequency of a PXIe-5413/5423/5433 and compares it to the actual frequency measured by the oscilloscope, performs any required adjustments to the internal TCXO, and computes any calibration constants in the onboard memory.

This VI also indicates if timebase calibration is complete. You must repeat the timebase calibration adjustment procedure steps until this VI returns TRUE for timebase cal complete.

[IMAGE alt='icon' src='timebase-cal-adjust-vi.png']

#### Inputs/Outputs

| external cal session in — External Cal Session In identifies an external calibration session. measured frequency — Measured Frequency specifies the frequency of the analog output signal generated at a specified channel of the waveform generator as measured by the oscilloscope connected to the channel being calibrated. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. external cal session out — External Cal Session Out returns a reference to your external calibration session to wire to the next VI. timebase cal complete — Timebase Cal Complete returns TRUE if timebase calibration is complete. If this parameter returns FALSE, you must repeat calls to the Timebase Cal Configure and Timebase Cal Adjust VIs until timebase calibration is complete. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/timebase-cal-configure-vi.html language=enus -->
## TOPIC 00015: Timebase Cal Configure VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/timebase-cal-configure-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/timebase-cal-configure-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the channel of the PXIe-5413/5423/5433 specified with the Timebase Cal Initialize VI and then returns a value for approximate frequency generated, which is used to program an oscilloscope (external timebase calibration source) that can measure a 5.5 V[pk-pk] sine wave of the returned freq

### Timebase Cal Configure VI

Configures the channel of the PXIe-5413/5423/5433 specified with the [Timebase Cal Initialize](/csh?topicname=timebase-cal-initialize-vi.html) VI and then returns a value for approximate frequency generated, which is used to program an oscilloscope (external timebase calibration source) that can measure a 5.5 V<sub>pk-pk</sub> sine wave of the returned frequency.

[IMAGE alt='icon' src='timebase-cal-configure-vi.png']

#### Inputs/Outputs

| external cal session in — External Cal Session In identifies an external calibration session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. external cal session out — External Cal Session Out returns a reference to your external calibration session to wire to the next VI. approximate frequency generated — Approximate Frequency Generated returns a value for the approximate frequency of the analog output signal generated at a specified channel of the waveform generator to be used to program an oscilloscope connected to the channel being calibrated that can measure a 5.5 Vpk-pk sine wave of the returned frequency. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/ni5433/external-cal-api/timebase-cal-initialize-vi.html language=enus -->
## TOPIC 00016: Timebase Cal Initialize VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/ni5433/external-cal-api/timebase-cal-initialize-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/ni5433/external-cal-api/timebase-cal-initialize-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an external calibration session for timebase calibration on a specified channel of a PXIe-5413/5423/5433. icon Inputs/Outputs cni5433_Ext_Cal_APIlvclass.png external cal session in External Cal Session In identifies an external calibration session. cu32.png channel Channel identifies the

### Timebase Cal Initialize VI

Initializes an external calibration session for timebase calibration on a specified channel of a PXIe-5413/5423/5433.

[IMAGE alt='icon' src='timebase-cal-initialize-vi.png']

#### Inputs/Outputs

| external cal session in — External Cal Session In identifies an external calibration session. channel — Channel identifies the channel of the previously specified waveform generator to use for calibration. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. external cal session out — External Cal Session Out returns a reference to your external calibration session to wire to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PXIe-5433 Ext Cal

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-5404-routing-mnu.html language=enus -->
## TOPIC 00017: 5404 Routing

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-5404-routing-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-5404-routing-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this VI to configure the routing of signals in the NI 5404 signal generator to RTSI lines and front panel connectors. icon

### 5404 Routing

Use this VI to configure the routing of signals in the NI 5404 signal generator to RTSI lines and front panel connectors.

[IMAGE alt='icon' src='nifgen-5404-routing-mnu.png']

- [niFgen Route Signal Out VI](../../instr-lib/nifgen/nifgen-llb/nifgen-route-signal-out-vi.html) Routes various signals in the signal generator to the RTSI lines or front panel terminals.

Parent topic:

Configure Clock

Parent topic:

Configure Trigger & Synchronization

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-arbsequence-mnu.html language=enus -->
## TOPIC 00018: Arbitrary Sequence

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-arbsequence-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-arbsequence-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Arbitrary Sequence VIs to configure, define, and clear an arbitrary sequence. icon

### Arbitrary Sequence

Use the NI-FGEN Arbitrary Sequence VIs to configure, define, and clear an arbitrary sequence.

[IMAGE alt='icon' src='nifgen-arbsequence-mnu.png']

- [niFgen Query Arb Sequence Capabilities VI](../../instr-lib/nifgen/nifgen-llb/nifgen-query-arb-sequence-capabilities-vi.html) Returns the attributes of the signal generator that are related to creating arbitrary sequences. These attributes are the Maximum Number of Sequences , Minimum Sequence Length , Maximum Sequence Length , and Maximum Loop Count .
- [niFgen Create Arbitrary Sequence VI](../../instr-lib/nifgen/nifgen-llb/nifgen-create-arbitrary-sequence-vi.html) Creates an arbitrary sequence from an array of waveform handles and an array of corresponding loop counts. This VI returns a handle that identifies the sequence. You pass this handle to the niFgen Configure Arbitrary Sequence VI to specify what arbitrary sequence you want the signal generator to produce.
- [niFgen Create Advanced Arb Sequence VI](../../instr-lib/nifgen/nifgen-llb/nifgen-create-advanced-arb-sequence-vi.html) Creates an arbitrary sequence from an array of waveform handles and an array of corresponding loop counts. This VI returns a handle that identifies the sequence. You pass this handle to the niFgen Configure Arbitrary Sequence VI to specify what arbitrary sequence you want the signal generator to produce.
- [niFgen Configure Arbitrary Sequence VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-arbitrary-sequence-vi.html) Configures the signal generator properties that affect arbitrary sequence generation. This VI selects the arbitrary sequence to produce and sets the gain and offset.
- [niFgen Clear Arbitrary Sequence VI](../../instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-sequence-vi.html) Removes a previously created arbitrary sequence from the signal generator memory and invalidates the sequence handle.
- [niFgen Query Arb Waveform Capabilities VI](../../instr-lib/nifgen/nifgen-llb/nifgen-query-arb-waveform-capabilities-vi.html) Returns the attributes of the signal generator that are related to creating arbitrary waveforms. These properties are the maximum number of waveforms, waveform quantum, minimum waveform size, and maximum waveform size.
- [niFgen Clear Arbitrary Memory VI](../../instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-memory-vi.html) Removes all previously created arbitrary waveforms, sequences, and scripts from the signal generator memory, and invalidates all waveform handles, sequence handles, and waveform names.
- [niFgen Allocate Waveform VI](../../instr-lib/nifgen/nifgen-llb/nifgen-allocate-waveform-vi.html) Specifies the size of a waveform up front so that it can be allocated in onboard memory before loading the associated data. Data can then be loaded in smaller blocks with the niFgen Write Waveform (poly) VI.
- [niFgen Set Waveform Next Write Position VI](../../instr-lib/nifgen/nifgen-llb/nifgen-set-waveform-next-write-position-vi.html) Sets the position in the waveform at which data is written during the next write. This VI allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the Waveform Handle parameter. Subsequent writes to that waveform begin where the last write left off, unless this VI is called again. The Waveform Handle passed in must have been created by a call to the niFgen Allocate Waveform VI or the niFgen Clear Arbitrary Waveform VI.
- [niFgen Create Waveform (poly) VI](../../instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-poly-vi.html) Takes the data provided and creates an onboard waveform of the same size for use in Arbitrary Waveform or Arbitrary Sequence output mode.
- [niFgen Write Waveform (poly) VI](../../instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-poly-vi.html) Writes data to the waveform in onboard memory.

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-arbwaveform-mnu.html language=enus -->
## TOPIC 00019: Arbitrary Waveform

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-arbwaveform-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-arbwaveform-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Arbitrary Waveform VIs to configure, define, and clear an arbitrary waveform. icon

### Arbitrary Waveform

Use the NI-FGEN Arbitrary Waveform VIs to configure, define, and clear an arbitrary waveform.

[IMAGE alt='icon' src='nifgen-arbwaveform-mnu.png']

- [niFgen Query Arb Waveform Capabilities VI](../../instr-lib/nifgen/nifgen-llb/nifgen-query-arb-waveform-capabilities-vi.html) Returns the attributes of the signal generator that are related to creating arbitrary waveforms. These properties are the maximum number of waveforms, waveform quantum, minimum waveform size, and maximum waveform size.
- [niFgen Create Waveform (poly) VI](../../instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-poly-vi.html) Takes the data provided and creates an onboard waveform of the same size for use in Arbitrary Waveform or Arbitrary Sequence output mode.
- [niFgen Configure Arbitrary Waveform VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-arbitrary-waveform-vi.html) Configures the properties of the signal generator that affect arbitrary waveform generation. Selects the arbitrary waveform to produce and sets the gain and offset.
- [niFgen Clear Arbitrary Waveform VI](../../instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-waveform-vi.html) Removes a previously created arbitrary waveform from the signal generator memory and invalidates the waveform handle.
- [niFgen Clear Arbitrary Memory VI](../../instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-memory-vi.html) Removes all previously created arbitrary waveforms, sequences, and scripts from the signal generator memory, and invalidates all waveform handles, sequence handles, and waveform names.
- [niFgen Allocate Waveform VI](../../instr-lib/nifgen/nifgen-llb/nifgen-allocate-waveform-vi.html) Specifies the size of a waveform up front so that it can be allocated in onboard memory before loading the associated data. Data can then be loaded in smaller blocks with the niFgen Write Waveform (poly) VI.
- [niFgen Set Waveform Next Write Position VI](../../instr-lib/nifgen/nifgen-llb/nifgen-set-waveform-next-write-position-vi.html) Sets the position in the waveform at which data is written during the next write. This VI allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the Waveform Handle parameter. Subsequent writes to that waveform begin where the last write left off, unless this VI is called again. The Waveform Handle passed in must have been created by a call to the niFgen Allocate Waveform VI or the niFgen Clear Arbitrary Waveform VI.
- [niFgen Write Waveform (poly) VI](../../instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-poly-vi.html) Writes data to the waveform in onboard memory.

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-cal-adc-control-mnu.html language=enus -->
## TOPIC 00020: ADC Control

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-cal-adc-control-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-cal-adc-control-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN ADC Control VIs only when following the calibration procedure of the signal generator. icon

### ADC Control

Use the NI-FGEN ADC Control VIs only when following the calibration procedure of the signal generator.

[IMAGE alt='icon' src='nifgen-cal-adc-control-mnu.png']

- [niFgen Initialize Cal ADC Calibration VI](../../instr-lib/nifgen/nifgen-llb/nifgen-initialize-cal-adc-calibration-vi.html) Initializes an external calibration session for ADC calibration. For the NI 5421/5422/5441, ADC calibration involves characterizing the gain and offset of the onboard ADC.
- [niFgen Write Binary 16 Analog Static Value VI](../../instr-lib/nifgen/nifgen-llb/nifgen-write-binary-16-analog-static-value-vi.html) Writes a 16-bit value to the DAC, which could be output as a DC voltage.
- [niFgen Read CAL ADC VI](../../instr-lib/nifgen/nifgen-llb/nifgen-read-cal-adc-vi.html) Takes one or more voltage measurements from the onboard calibration ADC and returns their average value. The signal that the ADC actually measures can be specified using the Cal ADC Input property. The ADC has some inherent gain and offset. These values can be determined during an external calibration session and stored in the calibration EEPROM.
- [niFgen Cal Adjust Cal ADC VI](../../instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-cal-adc-vi.html) Calculates calibration constants pertaining to the gain and offset of the onboard calibration ADC. During external calibration, you can generate voltages and measure them both externally and with the calibration ADC. The measured voltages are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.

Parent topic:

Cal Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-cal-analog-output-control-mnu.html language=enus -->
## TOPIC 00021: Analog Output Control

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-cal-analog-output-control-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-cal-analog-output-control-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Analog Output Control VIs only when following the calibration DC gain and offset portion of the signal generator calibration procedure. icon

### Analog Output Control

Use the NI-FGEN Analog Output Control VIs only when following the calibration DC gain and offset portion of the signal generator calibration procedure.

[IMAGE alt='icon' src='nifgen-cal-analog-output-control-mnu.png']

- [niFgen Initialize Analog Output Calibration VI](../../instr-lib/nifgen/nifgen-llb/nifgen-initialize-analog-output-calibration-vi.html) Sets up the device to start the analog output calibration.
- [niFgen Cal Adjust Main Path Output Impedance VI](../../instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-output-impedance-vi.html) Calculates calibration constants pertaining to main analog path output impedance. During external calibration, you can put the device in different configurations and take measurements of the resulting output voltage across different loads. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.
- [niFgen Cal Adjust Main Path Pre Amp Gain VI](../../instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-pre-amp-gain-vi.html) Calculates calibration constants pertaining to the preamplifier gain of the main analog path. During external calibration, you can put the device in different configurations; program different gain, offset, and main DAC values; and take measurements of the resulting output voltages. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.
- [niFgen Cal Adjust Main Path Post Amp Gain And Offset VI](../../instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-post-amp-gain-and-offset-vi.html) Calculates calibration constants pertaining to the post-amplifier gain and offset of the main analog path. During external calibration, you can put the device in different configurations; program different gain, offset, and main DAC values; and take measurements of the resulting output voltage. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.
- [niFgen Cal Adjust Main Path Pre Amp Offset VI](../../instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-pre-amp-offset-vi.html) Calculates calibration constants pertaining to the pre-amplifier offset of the main analog path. During external calibration, you can put the device in different configurations; program different gain, offset, and main DAC values; and take measurements of the resulting output voltages. The configuration data as well as the measurements, are passed to this VI so that, NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.
- [niFgen Cal Adjust Direct Path Output Impedance VI](../../instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-direct-path-output-impedance-vi.html) Calculates calibration constants pertaining to direct analog path output impedance. During external calibration, you can put the device in different configurations and take measurements of the resulting output voltage across different loads. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.
- [niFgen Cal Adjust Direct Path Gain VI](../../instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-direct-path-gain-vi.html) Calculates calibration constants pertaining to the gain of the direct analog path. During external calibration, you can put the device in different configurations; program different gain and main DAC values; and take measurements of the resulting output voltages. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.
- [niFgen Write Binary 16 Analog Static Value VI](../../instr-lib/nifgen/nifgen-llb/nifgen-write-binary-16-analog-static-value-vi.html) Writes a 16-bit value to the DAC, which could be output as a DC voltage.

Parent topic:

Cal Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-cal-control-functions-mnu.html language=enus -->
## TOPIC 00022: Cal Control

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-cal-control-functions-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-cal-control-functions-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Cal Control VIs only when following the analog output portion the calibration procedure of the signal generator. Navigate to Start»All Programs»National Instruments»NI-FGEN»Documentation»Calibration to find Calibration Procedures for your signal generator. icon

### Cal Control

Use the NI-FGEN Cal Control VIs only when following the analog output portion the calibration procedure of the signal generator. Navigate to **Start»All Programs»National Instruments»NI-FGEN»Documentation»Calibration** to find Calibration Procedures for your signal generator.

[IMAGE alt='icon' src='nifgen-cal-control-functions-mnu.png']

- [ADC Control](../../instr-lib/nifgen/nifgen-cal-adc-control-mnu.html) Use the NI-FGEN ADC Control VIs only when following the calibration procedure of the signal generator.
- [Oscillator Control](../../instr-lib/nifgen/nifgen-cal-vcxo-control-mnu.html) Use the NI-FGEN Oscillator Control VIs only when following the oscillator frequency calibration portion of the signal generator calibration procedure.
- [Analog Output Control](../../instr-lib/nifgen/nifgen-cal-analog-output-control-mnu.html) Use the NI-FGEN Analog Output Control VIs only when following the calibration DC gain and offset portion of the signal generator calibration procedure.
- [Flatness Control](../../instr-lib/nifgen/nifgen-cal-flatness-mnu.html) Use the NI-FGEN Flatness Control VIs only when following the flatness calibration section of the signal generator calibration procedure.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-cal-flatness-mnu.html language=enus -->
## TOPIC 00023: Flatness Control

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-cal-flatness-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-cal-flatness-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Flatness Control VIs only when following the flatness calibration section of the signal generator calibration procedure. icon

### Flatness Control

Use the NI-FGEN Flatness Control VIs only when following the flatness calibration section of the signal generator calibration procedure.

[IMAGE alt='icon' src='nifgen-cal-flatness-mnu.png']

- [niFgen Initialize Flatness Calibration VI](../../instr-lib/nifgen/nifgen-llb/nifgen-initialize-flatness-calibration-vi.html) Initializes an external calibration session to calibrate flatness.
- [niFgen Cal Adjust Flatness VI](../../instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-flatness-vi.html) During external calibration, the device is configured with the different analog settings. Measurements are taken of the resulting output voltage across different frequencies. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.

Parent topic:

Cal Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-cal-utility-mnu.html language=enus -->
## TOPIC 00024: Utility

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-cal-utility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-cal-utility-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Cal Utility VIs to get information about previous calibrations, store information, or password protect the external calibration data on your board. icon

### Utility

Use the NI-FGEN Cal Utility VIs to get information about previous calibrations, store information, or password protect the external calibration data on your board.

[IMAGE alt='icon' src='nifgen-cal-utility-mnu.png']

- [niFgen Get Self Cal Supported VI](../../instr-lib/nifgen/nifgen-llb/nifgen-get-self-cal-supported-vi.html) Returns whether the device supports self-calibration.
- [niFgen Restore Last Ext Cal Constants VI](../../instr-lib/nifgen/nifgen-llb/nifgen-restore-last-ext-cal-constants-vi.html) Overwrites the current calibration constants with those from the last successful external calibration. This action effectively undoes any self-calibrations performed since the last time an external calibration was performed.
- [niFgen Get Ext Cal Recommended Interval VI](../../instr-lib/nifgen/nifgen-llb/nifgen-get-ext-cal-recommended-interval-vi.html) Returns the recommended interval between external calibrations in months.
- [niFgen Get Self Cal Last Date And Time VI](../../instr-lib/nifgen/nifgen-llb/nifgen-get-self-cal-last-date-and-time-vi.html) Returns the date and time of the last successful self-calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this VI returns 14 for the hours parameter and 30 for the minutes parameter.
- [niFgen Get Self Cal Last Temp VI](../../instr-lib/nifgen/nifgen-llb/nifgen-get-self-cal-last-temp-vi.html) Returns the temperature at the last successful self-calibration. The temperature is returned in degrees Celsius.
- [niFgen Read Current Temperature VI](../../instr-lib/nifgen/nifgen-llb/nifgen-read-current-temperature-vi.html) Reads the current onboard temperature of the device. The temperature is returned in degrees Celsius.
- [niFgen Get Ext Cal Last Date And Time VI](../../instr-lib/nifgen/nifgen-llb/nifgen-get-ext-cal-last-date-and-time-vi.html) Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this VI returns 14 for the Hour parameter and 30 for the Minute parameter.
- [niFgen Get Ext Cal Last Temp VI](../../instr-lib/nifgen/nifgen-llb/nifgen-get-ext-cal-last-temp-vi.html) Returns the temperature at the last successful external calibration. The temperature is returned in degrees Celsius.
- [niFgen Get Cal User Defined Info VI](../../instr-lib/nifgen/nifgen-llb/nifgen-get-cal-user-defined-info-vi.html) Retrieves user-defined information from the onboard EEPROM.
- [niFgen Set Cal User Defined Info VI](../../instr-lib/nifgen/nifgen-llb/nifgen-set-cal-user-defined-info-vi.html) Stores user-defined information in the onboard EEPROM.
- [niFgen Change Ext Cal Password VI](../../instr-lib/nifgen/nifgen-llb/nifgen-change-ext-cal-password-vi.html) Changes the password that is required to initialize an external calibration session. The password may be up to four characters long.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-cal-vcxo-control-mnu.html language=enus -->
## TOPIC 00025: Oscillator Control

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-cal-vcxo-control-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-cal-vcxo-control-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Oscillator Control VIs only when following the oscillator frequency calibration portion of the signal generator calibration procedure. icon

### Oscillator Control

Use the NI-FGEN Oscillator Control VIs only when following the oscillator frequency calibration portion of the signal generator calibration procedure.

[IMAGE alt='icon' src='nifgen-cal-vcxo-control-mnu.png']

- [niFgen Initialize Oscillator Frequency Calibration VI](../../instr-lib/nifgen/nifgen-llb/nifgen-initialize-oscillator-frequency-calibration-vi.html) Sets up the device to start the oscillator calibration.
- [niFgen Cal Adjust Oscillator Frequency VI](../../instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-oscillator-frequency-vi.html) Calculates calibration constants pertaining to the oscillator. During external calibration, you can generate sine waves and take measurements of the resulting output frequencies. The desired and measured frequencies are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.

Parent topic:

Cal Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-calibration-mnu.html language=enus -->
## TOPIC 00026: Calibration

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-calibration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-calibration-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Calibration VIs to calibrate NI signal generators. Different signal generators use different calibration VIs. Refer to your signal generator calibration procedure for more information. icon

### Calibration

Use the NI-FGEN Calibration VIs to calibrate NI signal generators. Different signal generators use different calibration VIs. Refer to your signal generator calibration procedure for more information.

[IMAGE alt='icon' src='nifgen-calibration-mnu.png']

- [niFgen Self Cal VI](../../instr-lib/nifgen/nifgen-llb/nifgen-self-cal-vi.html) Performs a full internal (self-) calibration on the device. If the calibration is successful, new calibration data and constants are stored in the onboard EEPROM. Refer to the calibration procedure of the signal generator for more information.
- [PXIe-5433 Ext Cal](../../instr-lib/nifgen/ni5433/external-cal-api/ni5433-ext-cal-api-mnu.html) Use the NI-FGEN ni5433 Ext Cal VIs to perform external ADC, timebase, and flatness calibration on PXIe-5413/5423/5433 waveform generators.
- [niFgen Init Ext Cal VI](../../instr-lib/nifgen/nifgen-llb/nifgen-init-ext-cal-vi.html) Creates and initializes a special NI-FGEN external calibration session. The ViSession returned is an NI-FGEN session that can be used to configure the device using normal attributes and functions. However, flags have been set that allow you to program an external calibration procedure using the special calibration properties and VIs. The NI 5404 and PXIe-5413/5423/5433 have different calibration VIs. Refer to the calibration procedure of the signal generator for more information.
- [Cal Control](../../instr-lib/nifgen/nifgen-cal-control-functions-mnu.html) Use the NI-FGEN Cal Control VIs only when following the analog output portion the calibration procedure of the signal generator. Navigate to Start»All Programs»National Instruments»NI-FGEN»Documentation»Calibration to find Calibration Procedures for your signal generator.
- [niFgen Close Ext Cal VI](../../instr-lib/nifgen/nifgen-llb/nifgen-close-ext-cal-vi.html) Closes an NI-FGEN external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM.
- [Utility](../../instr-lib/nifgen/nifgen-cal-utility-mnu.html) Use the NI-FGEN Cal Utility VIs to get information about previous calibrations, store information, or password protect the external calibration data on your board.
- [niFgen Property Node VI](../../instr-lib/nifgen/nifgen-llb/nifgen-property-node-vi.html) Sets or gets properties of instruments or channels. For multi-channel sessions in which you want to configure subsets of channels differently, you must wire an Active Channel of an NI-FGEN property node. The Active Channel is listed first in the property node.

Parent topic:

NI-FGEN

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-config-mnu.html language=enus -->
## TOPIC 00027: Configuration

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-config-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-config-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Configuration VIs to configure the analog and digital output, clocking, triggering and synchronization, and onboard signal processing of your signal generator. icon

### Configuration

Use the NI-FGEN Configuration VIs to configure the analog and digital output, clocking, triggering and synchronization, and onboard signal processing of your signal generator.

[IMAGE alt='icon' src='nifgen-config-mnu.png']

- [Configure Output](../../instr-lib/nifgen/nifgen-configure-output-mnu.html) Use the NI-FGEN Configure Output VIs to enable signal generation and configure the analog output, analog and digital filtering, and digital pattern of your signal generator.
- [Configure Clock](../../instr-lib/nifgen/nifgen-configure-clock-mnu.html) Use the NI-FGEN Configure Clock VIs to configure signal generator clocking and data generation speed.
- [Configure Trigger & Synchronization](../../instr-lib/nifgen/nifgen-configure-trigger-mnu.html) Use the NI-FGEN Configure Trigger & Synchronization VIs to configure signal generator triggering and synchronization and to route signals from the signal generator to other devices.
- [Configure Onboard Signal Processing](../../instr-lib/nifgen/nifgen-configure-osp-mnu.html) Use the NI-FGEN Configure Onboard Signal Processing VIs to configure the filters used with the onboard signal processing (OSP) block.
- [Configure Peer-to-Peer (P2P)](../../instr-lib/nifgen/nifgen-configure-p2p-mnu.html) Use the NI-FGEN Peer-to-Peer VIs to configure the signal generator endpoint for peer-to-peer streaming.
- [niFgen Import Attribute Configuration(poly) VI](../../instr-lib/nifgen/nifgen-llb/nifgen-import-attribute-configuration-poly-vi.html) Imports a configuration to the session from either a file or a buffer.
- [niFgen Export Attribute Configuration(poly) VI](../../instr-lib/nifgen/nifgen-llb/nifgen-export-attribute-configuration-poly-vi.html) Exports a session configuration to either a file or a buffer.

Parent topic:

NI-FGEN

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-configure-clock-mnu.html language=enus -->
## TOPIC 00028: Configure Clock

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-configure-clock-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-configure-clock-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Configure Clock VIs to configure signal generator clocking and data generation speed. icon

### Configure Clock

Use the NI-FGEN Configure Clock VIs to configure signal generator clocking and data generation speed.

[IMAGE alt='icon' src='nifgen-configure-clock-mnu.png']

- [niFgen Configure Sample Clock Source VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-sample-clock-source-vi.html) Sets the source of the Sample clock (update clock) of the signal generator.
- [niFgen Configure Clock Mode VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-clock-mode-vi.html) Selects the clock mode for the signal generator.
- [niFgen Set Sample Rate VI](../../instr-lib/nifgen/nifgen-llb/nifgen-set-sample-rate-vi.html) Configures the sample rate, which determines the rate at which the signal generator produces arbitrary waveforms. When you configure the signal generator to produce an arbitrary sequence, this is the sample rate for all arbitrary waveforms in the sequence. If the update clock (Sample clock) source is external, setting the sample rate informs NI-FGEN of the external rate.
- [niFgen Configure Reference Clock VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-reference-clock-vi.html) Configures the signal generator Reference clock source and frequency. The signal generator uses the Reference clock to tune the Sample clock timebase of the signal generator so that the frequency stability and accuracy of the Sample clock timebase matches that of the Reference clock.
- [niFgen Adjust Sample Clock Relative Delay VI](../../instr-lib/nifgen/nifgen-llb/nifgen-adjust-sample-clock-relative-delay-vi.html) Delays (or phase shifts) the Sample clock, which delays the output of the module. Adjustment time can be positive or negative, but it must be less than or equal to the Sample clock period. The delay takes effect immediately after this VI is called.
- [niFgen Export Signal VI](../../instr-lib/nifgen/nifgen-llb/nifgen-export-signal-vi.html) Routes signals (clocks, triggers, and events) to the output terminal you specify.
- [5404 Routing](../../instr-lib/nifgen/nifgen-5404-routing-mnu.html) Use this VI to configure the routing of signals in the NI 5404 signal generator to RTSI lines and front panel connectors.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-configure-osp-mnu.html language=enus -->
## TOPIC 00029: Configure Onboard Signal Processing

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-configure-osp-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-configure-osp-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Configure Onboard Signal Processing VIs to configure the filters used with the onboard signal processing (OSP) block. icon

### Configure Onboard Signal Processing

Use the NI-FGEN Configure Onboard Signal Processing VIs to configure the filters used with the onboard signal processing (OSP) block.

[IMAGE alt='icon' src='nifgen-configure-osp-mnu.png']

- [niFgen Configure Custom FIR Filter Coefficients VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-custom-fir-filter-coefficients-vi.html) Sets the FIR filter coefficients used by the onboard signal processing block. The values are coerced to the closest settings achievable by the signal generator.
- [niFgen Get FIR Filter Coefficients VI](../../instr-lib/nifgen/nifgen-llb/nifgen-get-fir-filter-coefficients-vi.html) Returns the FIR filter coefficients used by the onboard signal processing block. These coefficients are determined by NI-FGEN and based on the FIR filter type and corresponding property (Alpha, Passband, BT) unless you are using the custom filter. If you are using a custom filter, the coefficients returned are those set with the niFgen Configure Custom FIR Filter Coefficients VI coerced to the quantized values used by the device.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-configure-output-mnu.html language=enus -->
## TOPIC 00030: Configure Output

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-configure-output-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-configure-output-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Configure Output VIs to enable signal generation and configure the analog output, analog and digital filtering, and digital pattern of your signal generator. icon

### Configure Output

Use the NI-FGEN Configure Output VIs to enable signal generation and configure the analog output, analog and digital filtering, and digital pattern of your signal generator.

[IMAGE alt='icon' src='nifgen-configure-output-mnu.png']

- [niFgen Output Enable VI](../../instr-lib/nifgen/nifgen-llb/nifgen-output-enable-vi.html) Configures the signal generator to generate a signal at the channel output connector.
- [niFgen Configure Output Impedance VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-output-impedance-vi.html) Configures the output impedance for the channel that you specify.
- [niFgen Configure Analog Filter VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-analog-filter-vi.html) Configures the analog filter for the device. You can apply the analog filter setting in Arbitrary Waveform, Arbitrary Sequence, or Script output mode, or in Frequency List or Standard Function output mode when used with user-defined functions.
- [niFgen Configure Digital Filter VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-filter-vi.html) Configures the digital filter for the device. You can apply the digital filter setting in Arbitrary Waveform, Arbitrary Sequence, or Script output mode, or in Frequency List or Standard Function output mode when used with user-defined functions.
- [niFgen Configure Digital Patterning VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-patterning-vi.html) Configures the state of the DIGITAL DATA & CONTROL/DIGITAL PATTERN connector.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-configure-p2p-mnu.html language=enus -->
## TOPIC 00031: Configure Peer-to-Peer (P2P)

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-configure-p2p-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-configure-p2p-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Peer-to-Peer VIs to configure the signal generator endpoint for peer-to-peer streaming. icon

### Configure Peer-to-Peer (P2P)

Use the NI-FGEN Peer-to-Peer VIs to configure the signal generator endpoint for peer-to-peer streaming.

[IMAGE alt='icon' src='nifgen-configure-p2p-mnu.png']

- [niFgen Get Stream Endpoint Handle VI](../../instr-lib/nifgen/nifgen-llb/nifgen-get-stream-endpoint-handle-vi.html) Returns a reader endpoint handle that can be used with NI-P2P to configure a peer-to-peer stream with a signal generator endpoint.
- [niFgen Write P2P Endpoint I16 VI](../../instr-lib/nifgen/nifgen-llb/nifgen-write-p2p-endpoint-i16-vi.html) Writes I16 data to the peer-to-peer endpoint. Use this VI to write initial data from the host to the endpoint before starting generation to avoid underflow at the beginning of the generation.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-configure-trigger-mnu.html language=enus -->
## TOPIC 00032: Configure Trigger & Synchronization

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-configure-trigger-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-configure-trigger-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Configure Trigger & Synchronization VIs to configure signal generator triggering and synchronization and to route signals from the signal generator to other devices. icon

### Configure Trigger & Synchronization

Use the NI-FGEN Configure Trigger & Synchronization VIs to configure signal generator triggering and synchronization and to route signals from the signal generator to other devices.

[IMAGE alt='icon' src='nifgen-configure-trigger-mnu.png']

- [niFgen Configure Trigger Mode VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-trigger-mode-vi.html) Sets the trigger mode for your device.
- [niFgen Configure Trigger (poly) VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-trigger-poly-vi.html) Configures the trigger source. The signal generator responds to a trigger according to the current trigger mode.
- [niFgen Configure Synchronization VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-synchronization-vi.html) Sets the signal generator to receive a synchronization signal to synchronize two or more signal generators. One signal generator should route a SYNC signal to a RTSI line using the niFgen Export Signal VI ( niFgen Route Signal Out VI for the NI 5404), and other signal generators should receive the signal using this VI.
- [niFgen Send Software Edge Trigger VI](../../instr-lib/nifgen/nifgen-llb/nifgen-send-software-edge-trigger-vi.html) Sends a command to trigger the signal generator. This VI can act as an override for an external edge trigger.
- [niFgen Export Signal VI](../../instr-lib/nifgen/nifgen-llb/nifgen-export-signal-vi.html) Routes signals (clocks, triggers, and events) to the output terminal you specify.
- [5404 Routing](../../instr-lib/nifgen/nifgen-5404-routing-mnu.html) Use this VI to configure the routing of signals in the NI 5404 signal generator to RTSI lines and front panel connectors.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-freqlist-mnu.html language=enus -->
## TOPIC 00033: Frequency List

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-freqlist-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-freqlist-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Frequency List VIs to configure, define, and clear a frequency list. icon

### Frequency List

Use the NI-FGEN Frequency List VIs to configure, define, and clear a frequency list.

[IMAGE alt='icon' src='nifgen-freqlist-mnu.png']

- [niFgen Query Freq List Capabilities VI](../../instr-lib/nifgen/nifgen-llb/nifgen-query-freq-list-capabilities-vi.html) Returns the properties of the signal generator that are related to creating frequency lists. These properties are the Maximum Number of Freq Lists , Minimum Frequency List Length , Maximum Frequency List Length , Minimum Frequency List Duration , Maximum Frequency List Duration , and Frequency List Duration Quantum .
- [niFgen Create Frequency List VI](../../instr-lib/nifgen/nifgen-llb/nifgen-create-frequency-list-vi.html) Creates a frequency list from an array of frequencies and an array of durations. The two arrays should have the same number of elements. The VI returns a handle that identifies the frequency list. You can pass this handle to the niFgen Configure Frequency List VI to specify what frequency list you want the signal generator to produce.
- [niFgen Configure Frequency List VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-frequency-list-vi.html) Configures the properties of the signal generator that affect frequency list generation. Selects the frequency list to produce and sets the amplitude, DC offset, and start phase.
- [niFgen Clear Frequency List VI](../../instr-lib/nifgen/nifgen-llb/nifgen-clear-frequency-list-vi.html) Removes a previously created frequency list from the signal generator memory and invalidates the Frequency List Handle .
- [niFgen Define User Standard Waveform VI](../../instr-lib/nifgen/nifgen-llb/nifgen-define-user-standard-waveform-vi.html) Defines a user waveform for either Standard Function or Frequency List output mode.
- [niFgen Clear User Standard Waveform VI](../../instr-lib/nifgen/nifgen-llb/nifgen-clear-user-standard-waveform-vi.html) Clears the user-defined waveform created by the niFgen Define User Standard Waveform VI.

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-generate-waveforms-mnu.html language=enus -->
## TOPIC 00034: Waveform Control

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-generate-waveforms-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-generate-waveforms-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN Waveform Control VIs to configure and control the generation of standard functions, arbitrary waveforms, arbitrary sequences, frequency lists, and scripts on your signal generator. icon

### Waveform Control

Use the NI-FGEN Waveform Control VIs to configure and control the generation of standard functions, arbitrary waveforms, arbitrary sequences, frequency lists, and scripts on your signal generator.

[IMAGE alt='icon' src='nifgen-generate-waveforms-mnu.png']

- [niFgen Configure Output Mode VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-output-mode-vi.html) Configures the output mode of the signal generator. The output mode determines how the signal generator produces waveforms. For example, you can select to generate a standard waveform, an arbitrary waveform, or a sequence of arbitrary waveforms.
- [Standard Waveform](../../instr-lib/nifgen/nifgen-standard-waveform-mnu.html) Use the NI-FGEN Standard Waveform VIs to configure, define, and clear a standard waveform.
- [Frequency List](../../instr-lib/nifgen/nifgen-freqlist-mnu.html) Use the NI-FGEN Frequency List VIs to configure, define, and clear a frequency list.
- [niFgen Commit VI](../../instr-lib/nifgen/nifgen-llb/nifgen-commit-vi.html) Causes a transition to the Committed state. This VI verifies property values, reserves the device, and commits the property values to the device. If the property values are all valid, NI-FGEN sets the device hardware configuration to match the session configuration.
- [niFgen Initiate Generation VI](../../instr-lib/nifgen/nifgen-llb/nifgen-initiate-generation-vi.html) Initiates signal generation. If you want to abort signal output, call the niFgen Abort Generation VI. Call this VI to cause the signal generator to produce a signal again.
- [niFgen Abort Generation VI](../../instr-lib/nifgen/nifgen-llb/nifgen-abort-generation-vi.html) Aborts any previously initiated signal generation. Call the niFgen Initiate Generation VI to initiate signal generation.
- [niFgen Configure Channels VI](../../instr-lib/nifgen/nifgen-llb/nifgen-configure-channels-vi.html) Configures the channels that are used with the instrument specified in Instrument Handle . If you call this VI, you must call it immediately after initializing your session and before configuring any properties or writing data.
- [Arbitrary Waveform](../../instr-lib/nifgen/nifgen-arbwaveform-mnu.html) Use the NI-FGEN Arbitrary Waveform VIs to configure, define, and clear an arbitrary waveform.
- [Arbitrary Sequence](../../instr-lib/nifgen/nifgen-arbsequence-mnu.html) Use the NI-FGEN Arbitrary Sequence VIs to configure, define, and clear an arbitrary sequence.
- [Script](../../instr-lib/nifgen/nifgen-script-mnu.html) Use the NI-FGEN Script VIs to create, configure, and clear scripts.
- [niFgen Is Done VI](../../instr-lib/nifgen/nifgen-llb/nifgen-is-done-vi.html) Determines whether the current generation has completed. This VI sets the Done parameter to be TRUE if the session is in the Idle or Committed states.
- [niFgen Wait Until Done VI](../../instr-lib/nifgen/nifgen-llb/nifgen-wait-until-done-vi.html) Waits until the device is done generating or until the maximum time has expired.

Parent topic:

NI-FGEN

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-abort-generation-vi.html language=enus -->
## TOPIC 00035: niFgen Abort Generation VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-abort-generation-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-abort-generation-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts any previously initiated signal generation. Call the niFgen Initiate Generation VI to initiate signal generation. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen I

### niFgen Abort Generation VI

Aborts any previously initiated signal generation. Call the [niFgen Initiate Generation](/csh?topicname=nifgen-initiate-generation-vi.html) VI to initiate signal generation.

[IMAGE alt='icon' src='nifgen-abort-generation-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-adjust-sample-clock-relative-delay-vi.html language=enus -->
## TOPIC 00036: niFgen Adjust Sample Clock Relative Delay VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-adjust-sample-clock-relative-delay-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-adjust-sample-clock-relative-delay-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Delays (or phase shifts) the Sample clock, which delays the output of the module. Adjustment time can be positive or negative, but it must be less than or equal to the Sample clock period. The delay takes effect immediately after this VI is called. To delay an external Sample clock, set the Sample C

### niFgen Adjust Sample Clock Relative Delay VI

Delays (or phase shifts) the Sample clock, which delays the output of the module. Adjustment time can be positive or negative, but it must be less than or equal to the Sample clock period. The delay takes effect immediately after this VI is called.

To delay an external Sample clock, set the [Sample Clock Absolute Delay](/csh?context=nifgen_nifgenpropref_pnifgen_sampleclockabsolutedelay) property. Delaying the Sample clock can be useful when lining up the output of multiple modules or when intentionally phase shifting the output relative to a fixed reference such as the PLL Reference clock.

Note

NI-TClk Synchronize

[IMAGE alt='icon' src='nifgen-adjust-sample-clock-relative-delay-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Adjustment Time — Adjustment Time specifies the amount of time to adjust the Sample clock delay. Units: Seconds (s) error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Clock

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-allocate-named-waveform-vi.html language=enus -->
## TOPIC 00037: niFgen Allocate Named Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-allocate-named-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-allocate-named-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial size of a named waveform so that it can be allocated in onboard memory before loading the associated data. Data can then be loaded in smaller blocks with the niFgen Write Waveform (poly) VI. icon Inputs/Outputs cu32.png Waveform Size Waveform Size specifies the size of the wave

### niFgen Allocate Named Waveform VI

Specifies the initial size of a named waveform so that it can be allocated in onboard memory before loading the associated data. Data can then be loaded in smaller blocks with the [niFgen Write Waveform (poly)](/csh?topicname=nifgen-write-waveform-poly-vi.html) VI.

[IMAGE alt='icon' src='nifgen-allocate-named-waveform-vi.png']

#### Inputs/Outputs

| Waveform Size — Waveform Size specifies the size of the waveform in samples. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Name — Waveform Name specifies the name of the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Name Out — Waveform Name Out passes the name of the named waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Script

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-allocate-waveform-vi.html language=enus -->
## TOPIC 00038: niFgen Allocate Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-allocate-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-allocate-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the size of a waveform up front so that it can be allocated in onboard memory before loading the associated data. Data can then be loaded in smaller blocks with the niFgen Write Waveform (poly) VI. The signal generator must not be in the Generating state when you call this VI. You must set

### niFgen Allocate Waveform VI

Specifies the size of a waveform up front so that it can be allocated in onboard memory before loading the associated data. Data can then be loaded in smaller blocks with the [niFgen Write Waveform (poly)](/csh?topicname=nifgen-write-waveform-poly-vi.html) VI.

Note

Note

Output Mode

Arbitrary Waveform

Arbitrary Sequence

niFgen Configure Output Mode

[IMAGE alt='icon' src='nifgen-allocate-waveform-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Size — Waveform Size specifies the size of the waveform in samples. This value must be an integer multiple of the waveform quantum. Use the Waveform Quantum property or the niFgen Query Arb Waveform Capabilities VI to determine the waveform quantum. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle Out — Waveform Handle Out returns the handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Arbitrary Waveform

Parent topic:

Arbitrary Sequence

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-attach-grpc-session-vi.html language=enus -->
## TOPIC 00039: niFgen Attach gRPC Session VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-attach-grpc-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-attach-grpc-session-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Attaches to an existing NI-FGEN session with the specified Session Name on the specified NI gRPC Device Server. Returns a session handle to be used in all subsequent NI-FGEN VI calls. If you do not specify a session name for the server, or if the specified session name did not previously exist on th

### niFgen Attach gRPC Session VI

Attaches to an existing NI-FGEN session with the specified Session Name on the specified NI gRPC Device Server. Returns a session handle to be used in all subsequent NI-FGEN VI calls.

Note

This VI creates a new session in LabVIEW that corresponds to the Session Name specified in the server. If a session with the specified name did not previously exist on the server, then NI-FGEN will return an error.

The resulting session in LabVIEW forwards driver calls to the corresponding session on the server.

[IMAGE alt='icon' src='nifgen-attach-grpc-session-vi.png']

#### Inputs/Outputs

| gRPC Options — gRPC Options specifies the information used to connect to the server. Session Name — Session Name specifies the name of the MeasurementLink gRPC session. Address (localhost) — Address (localhost) specifies the address of the NI gRPC Device Server. Port (31763) — Port (31763) specifies the port that the NI gRPC Device Server monitors for connections. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Session Name — Session Name specifies the name of the MeasurementLink gRPC session. Address (localhost) — Address (localhost) specifies the address of the NI gRPC Device Server. Port (31763) — Port (31763) specifies the port that the NI gRPC Device Server monitors for connections. |

Parent topic:

MeasurementLink

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-cal-adc-vi.html language=enus -->
## TOPIC 00040: niFgen Cal Adjust Cal ADC VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-cal-adc-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-cal-adc-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration constants pertaining to the gain and offset of the onboard calibration ADC. During external calibration, you can generate voltages and measure them both externally and with the calibration ADC. The measured voltages are passed to this VI so that NI-FGEN can calculate the appro

### niFgen Cal Adjust Cal ADC VI

Calculates calibration constants pertaining to the gain and offset of the onboard calibration ADC. During external calibration, you can generate voltages and measure them both externally and with the calibration ADC. The measured voltages are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.

[IMAGE alt='icon' src='nifgen-cal-adjust-cal-adc-vi.png']

#### Inputs/Outputs

| Channel Name — Channel Name specifies the channel that this VI uses. Configuration — Configuration specifies the configuration of the device for this stage of calibration. Input Value Configuration Setting -1 NIFGEN_VAL_CAL_CONFIG_GLOBAL 10 NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH 11 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. Voltages Measured Externally — Voltages Measured Externally is an array of analog output voltages measured with an external instrument. Voltages Measured with Cal ADC — Voltages Measured with Cal ADC is an array of analog output voltages measured with the onboard calibration ADC. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input Value | Configuration Setting |
| -1 | NIFGEN_VAL_CAL_CONFIG_GLOBAL |
| 10 | NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH |
| 11 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH |

Parent topic:

ADC Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-direct-path-gain-vi.html language=enus -->
## TOPIC 00041: niFgen Cal Adjust Direct Path Gain VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-direct-path-gain-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-direct-path-gain-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration constants pertaining to the gain of the direct analog path. During external calibration, you can put the device in different configurations; program different gain and main DAC values; and take measurements of the resulting output voltages. The configuration data, as well as t

### niFgen Cal Adjust Direct Path Gain VI

Calculates calibration constants pertaining to the gain of the direct analog path. During external calibration, you can put the device in different configurations; program different gain and main DAC values; and take measurements of the resulting output voltages. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.

[IMAGE alt='icon' src='nifgen-cal-adjust-direct-path-gain-vi.png']

#### Inputs/Outputs

| MainDACValues — MainDACValues specifies an array of the values programmed to the main output DAC during this calibration stage. Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. Channel Name — Channel Name specifies the channel that this VI uses. GainDACValues — GainDACValues specifies an array of the values programmed to the gain calibration DAC during this calibration stage. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error MeasuredOutputs — MeasuredOutputs specifies an array of the analog output voltages measured during this calibration stage. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Analog Output Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-direct-path-output-impedance-vi.html language=enus -->
## TOPIC 00042: niFgen Cal Adjust Direct Path Output Impedance VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-direct-path-output-impedance-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-direct-path-output-impedance-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration constants pertaining to direct analog path output impedance. During external calibration, you can put the device in different configurations and take measurements of the resulting output voltage across different loads. The configuration data, as well as the measurements, are p

### niFgen Cal Adjust Direct Path Output Impedance VI

Calculates calibration constants pertaining to direct analog path output impedance. During external calibration, you can put the device in different configurations and take measurements of the resulting output voltage across different loads. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.

[IMAGE alt='icon' src='nifgen-cal-adjust-direct-path-output-impedance-vi.png']

#### Inputs/Outputs

| Load Impedance — Load Impedance specifies the impedance of the load across which the measurement passed in as Measured Voltage Across Load is taken. Configuration — Configuration specifies the configuration of the device for this stage of calibration. Input Value Configuration Setting 0 NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH_50OHMS 1 NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH_75OHMS 2 NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH_DIFFERENTIAL Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. Channel Name — Channel Name specifies the channel that this VI uses. Measured Source Voltage — Measured Source Voltage specifies the analog output voltage measured across a very high-impedance load. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Measured Voltage Across Load — Measured Voltage Across Load specifies the analog output voltage measured across the load impedance specified in Load Impedance. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input Value | Configuration Setting |
| 0 | NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH_50OHMS |
| 1 | NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH_75OHMS |
| 2 | NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH_DIFFERENTIAL |

Parent topic:

Analog Output Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-flatness-vi.html language=enus -->
## TOPIC 00043: niFgen Cal Adjust Flatness VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-flatness-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-flatness-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: During external calibration, the device is configured with the different analog settings. Measurements are taken of the resulting output voltage across different frequencies. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate cali

### niFgen Cal Adjust Flatness VI

During external calibration, the device is configured with the different analog settings. Measurements are taken of the resulting output voltage across different frequencies. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.

[IMAGE alt='icon' src='nifgen-cal-adjust-flatness-vi.png']

#### Inputs/Outputs

| Frequencies Array — Frequencies Array specifies the frequencies at which different sine tones were generated, in Hertz. Configuration — Configuration specifies the configuration of the device for this stage of calibration. Input Value Configuration Setting 0 NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_0DB 1 NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_3DB 2 NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_6DB 3 NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_9DB 4 NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_12DB 5 NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_0DB 6 NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_3DB 7 NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_6DB 8 NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_9DB 9 NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_12DB 10 NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH 12 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_0DB 13 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_9DB 14 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_33DB Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. Channel Name — Channel Name specifies the channel that this VI uses. Requested Amplitude — Requested Amplitude specifies the Amplitude, in volts, that was used to configure NI-FGEN in order to generate the sine tones at different frequencies. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Measured Amplitudes Array — Measured Amplitudes Array specifies the amplitudes measured for each corresponding frequency in the Frequencies Array, in volts. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input Value | Configuration Setting |
| 0 | NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_0DB |
| 1 | NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_3DB |
| 2 | NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_6DB |
| 3 | NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_9DB |
| 4 | NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_12DB |
| 5 | NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_0DB |
| 6 | NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_3DB |
| 7 | NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_6DB |
| 8 | NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_9DB |
| 9 | NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_12DB |
| 10 | NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH |
| 12 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_0DB |
| 13 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_9DB |
| 14 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_33DB |

Parent topic:

Flatness Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-output-impedance-vi.html language=enus -->
## TOPIC 00044: niFgen Cal Adjust Main Path Output Impedance VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-output-impedance-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-output-impedance-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration constants pertaining to main analog path output impedance. During external calibration, you can put the device in different configurations and take measurements of the resulting output voltage across different loads. The configuration data, as well as the measurements, are pas

### niFgen Cal Adjust Main Path Output Impedance VI

Calculates calibration constants pertaining to main analog path output impedance. During external calibration, you can put the device in different configurations and take measurements of the resulting output voltage across different loads. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.

[IMAGE alt='icon' src='nifgen-cal-adjust-main-path-output-impedance-vi.png']

#### Inputs/Outputs

| Load Impedance — Load Impedance specifies the impedance of the load across which the measurement passed in as Measured Voltage Across Load is taken. Configuration — Configuration specifies the configuration of the device for this stage of calibration. Input Value Configuration Setting -1 NIFGEN_VAL_CAL_CONFIG_GLOBAL 10 NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH 11 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. Channel Name — Channel Name specifies the channel that this VI uses. Measured Source Voltage — Measured Source Voltage specifies the analog output voltage measured across a very high-impedance load. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Measured Voltage Across Load — Measured Voltage Across Load specifies the analog output voltage measured across the load impedance specified in Load Impedance. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input Value | Configuration Setting |
| -1 | NIFGEN_VAL_CAL_CONFIG_GLOBAL |
| 10 | NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH |
| 11 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH |

Parent topic:

Analog Output Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-post-amp-gain-and-offset-vi.html language=enus -->
## TOPIC 00045: niFgen Cal Adjust Main Path Post Amp Gain And Offset VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-post-amp-gain-and-offset-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-post-amp-gain-and-offset-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration constants pertaining to the post-amplifier gain and offset of the main analog path. During external calibration, you can put the device in different configurations; program different gain, offset, and main DAC values; and take measurements of the resulting output voltage. The

### niFgen Cal Adjust Main Path Post Amp Gain And Offset VI

Calculates calibration constants pertaining to the post-amplifier gain and offset of the main analog path. During external calibration, you can put the device in different configurations; program different gain, offset, and main DAC values; and take measurements of the resulting output voltage. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.

[IMAGE alt='icon' src='nifgen-cal-adjust-main-path-post-amp-gain-and-offset-vi.png']

#### Inputs/Outputs

| MainDACValues — MainDACValues specifies an array of the values programmed to the main output DAC during this calibration stage. Configuration — Configuration specifies the configuration of the device for this stage of calibration. Input Value Configuration Setting 0 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_0DB 1 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_12DB 2 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_24DB 3 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_36DB 4 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_0DB 5 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_12DB 6 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_24DB 7 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_36DB Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. Channel Name — Channel Name specifies the channel that this VI uses. GainDACValues — GainDACValues specifies an array of the values programmed to the gain calibration DAC during this calibration stage. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error MeasuredOutputs — MeasuredOutputs specifies an array of the analog output voltages measured during this calibration stage. OffsetDACValues — OffsetDACValues specifies an array of the values programmed to the offset calibration DAC during this calibration stage. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input Value | Configuration Setting |
| 0 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_0DB |
| 1 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_12DB |
| 2 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_24DB |
| 3 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_LOW_GAIN_36DB |
| 4 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_0DB |
| 5 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_12DB |
| 6 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_24DB |
| 7 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_HIGH_GAIN_36DB |

Parent topic:

Analog Output Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-pre-amp-gain-vi.html language=enus -->
## TOPIC 00046: niFgen Cal Adjust Main Path Pre Amp Gain VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-pre-amp-gain-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-pre-amp-gain-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration constants pertaining to the preamplifier gain of the main analog path. During external calibration, you can put the device in different configurations; program different gain, offset, and main DAC values; and take measurements of the resulting output voltages. The configuratio

### niFgen Cal Adjust Main Path Pre Amp Gain VI

Calculates calibration constants pertaining to the preamplifier gain of the main analog path. During external calibration, you can put the device in different configurations; program different gain, offset, and main DAC values; and take measurements of the resulting output voltages. The configuration data, as well as the measurements, are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.

[IMAGE alt='icon' src='nifgen-cal-adjust-main-path-pre-amp-gain-vi.png']

#### Inputs/Outputs

| MainDACValues — MainDACValues specifies an array of the values programmed to the main output DAC during this calibration stage. Configuration — Configuration specifies the configuration of the device for this stage of calibration. Input Value Configuration Setting 0 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_0DB 1 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_3DB 2 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_6DB 3 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_9DB 4 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_12DB 5 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_0DB 6 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_3DB 7 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_6DB 8 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_9DB 9 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_12DB Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. Channel Name — Channel Name specifies the channel that this VI uses. GainDACValues — GainDACValues specifies an array of the values programmed to the gain calibration DAC during this calibration stage. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error MeasuredOutputs — MeasuredOutputs specifies an array of the analog output voltages measured during this calibration stage. OffsetDACValues — OffsetDACValues specifies an array of the values programmed to the offset calibration DAC during this calibration stage. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input Value | Configuration Setting |
| 0 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_0DB |
| 1 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_3DB |
| 2 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_6DB |
| 3 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_9DB |
| 4 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_12DB |
| 5 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_0DB |
| 6 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_3DB |
| 7 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_6DB |
| 8 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_9DB |
| 9 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_12DB |

Parent topic:

Analog Output Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-pre-amp-offset-vi.html language=enus -->
## TOPIC 00047: niFgen Cal Adjust Main Path Pre Amp Offset VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-pre-amp-offset-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-main-path-pre-amp-offset-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration constants pertaining to the pre-amplifier offset of the main analog path. During external calibration, you can put the device in different configurations; program different gain, offset, and main DAC values; and take measurements of the resulting output voltages. The configura

### niFgen Cal Adjust Main Path Pre Amp Offset VI

Calculates calibration constants pertaining to the pre-amplifier offset of the main analog path. During external calibration, you can put the device in different configurations; program different gain, offset, and main DAC values; and take measurements of the resulting output voltages. The configuration data as well as the measurements, are passed to this VI so that, NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.

[IMAGE alt='icon' src='nifgen-cal-adjust-main-path-pre-amp-offset-vi.png']

#### Inputs/Outputs

| Configuration — Configuration specifies the configuration of the device for this stage of calibration. Input Value Configuration Setting 0 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_0DB 1 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_3DB 2 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_6DB 3 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_9DB 4 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_12DB 5 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_0DB 6 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_3DB 7 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_6DB 8 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_9DB 9 NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_12DB Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. Channel Name — Channel Name specifies the channel that this VI uses. GainDACValues — GainDACValues specifies an array of the values programmed to the gain calibration DAC during this calibration stage. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error MeasuredOutputs — MeasuredOutputs specifies an array of the analog output voltages measured during this calibration stage. OffsetDACValues — OffsetDACValues specifies an array of the values programmed to the offset calibration DAC during this calibration stage. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input Value | Configuration Setting |
| 0 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_0DB |
| 1 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_3DB |
| 2 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_6DB |
| 3 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_9DB |
| 4 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_12DB |
| 5 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_0DB |
| 6 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_3DB |
| 7 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_6DB |
| 8 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_9DB |
| 9 | NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_12DB |

Parent topic:

Analog Output Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-oscillator-frequency-vi.html language=enus -->
## TOPIC 00048: niFgen Cal Adjust Oscillator Frequency VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-oscillator-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-cal-adjust-oscillator-frequency-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration constants pertaining to the oscillator. During external calibration, you can generate sine waves and take measurements of the resulting output frequencies. The desired and measured frequencies are passed to this VI so that NI-FGEN can calculate the appropriate calibration cons

### niFgen Cal Adjust Oscillator Frequency VI

Calculates calibration constants pertaining to the oscillator. During external calibration, you can generate sine waves and take measurements of the resulting output frequencies. The desired and measured frequencies are passed to this VI so that NI-FGEN can calculate the appropriate calibration constants and, when the calibration session is committed, store them in the onboard EEPROM.

[IMAGE alt='icon' src='nifgen-cal-adjust-oscillator-frequency-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. Desired Frequency In Hz — Desired Frequency In Hz specifies the expected frequency of the output waveform. Measured Frequency In Hz — Measured Frequency In Hz specifies the actual (measured) frequency of the output waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Oscillator Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-change-ext-cal-password-vi.html language=enus -->
## TOPIC 00049: niFgen Change Ext Cal Password VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-change-ext-cal-password-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-change-ext-cal-password-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the password that is required to initialize an external calibration session. The password may be up to four characters long. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. cstr.png Old Password Old Password is the old (current) e

### niFgen Change Ext Cal Password VI

Changes the password that is required to initialize an external calibration session. The password may be up to four characters long.

[IMAGE alt='icon' src='nifgen-change-ext-cal-password-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Old Password — Old Password is the old (current) external calibration password. New Password — New Password is the new (desired) external calibration password. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-memory-vi.html language=enus -->
## TOPIC 00050: niFgen Clear Arbitrary Memory VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-memory-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-memory-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes all previously created arbitrary waveforms, sequences, and scripts from the signal generator memory, and invalidates all waveform handles, sequence handles, and waveform names. The signal generator must not be in the Generating state when you call this VI. icon Inputs/Outputs civrn.png Instr

### niFgen Clear Arbitrary Memory VI

Removes all previously created arbitrary waveforms, sequences, and scripts from the signal generator memory, and invalidates all waveform handles, sequence handles, and waveform names.

Note

[IMAGE alt='icon' src='nifgen-clear-arbitrary-memory-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Arbitrary Waveform

Parent topic:

Arbitrary Sequence

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-sequence-vi.html language=enus -->
## TOPIC 00051: niFgen Clear Arbitrary Sequence VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-sequence-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-sequence-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a previously created arbitrary sequence from the signal generator memory and invalidates the sequence handle. The signal generator must not be in the Generating state when you call this VI. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument s

### niFgen Clear Arbitrary Sequence VI

Removes a previously created arbitrary sequence from the signal generator memory and invalidates the sequence handle.

Note

[IMAGE alt='icon' src='nifgen-clear-arbitrary-sequence-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Sequence Handle — Sequence Handle specifies the handle of the arbitrary sequence to produce. You can create multiple arbitrary sequences using the niFgen Create Arbitrary Sequence VI or the niFgen Create Advanced Arb Sequence VI. These VIs return a handle that you use to identify each sequence. Specify a value of -1 to clear all sequences. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Arbitrary Sequence

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-waveform-vi.html language=enus -->
## TOPIC 00052: niFgen Clear Arbitrary Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-clear-arbitrary-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a previously created arbitrary waveform from the signal generator memory and invalidates the waveform handle. The signal generator must not be in the Generating state when you call this VI. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument s

### niFgen Clear Arbitrary Waveform VI

Removes a previously created arbitrary waveform from the signal generator memory and invalidates the waveform handle.

Note

[IMAGE alt='icon' src='nifgen-clear-arbitrary-waveform-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Waveform Handle — Waveform Handle selects the arbitrary waveform to clear. You can create multiple arbitrary waveforms using the niFgen Create Waveform (poly) VI. niFgen Create Waveform (poly) VI returns a handle that you use to identify each waveform. Specify a value of -1 to clear all waveforms. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Arbitrary Waveform

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-clear-frequency-list-vi.html language=enus -->
## TOPIC 00053: niFgen Clear Frequency List VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-clear-frequency-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-clear-frequency-list-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a previously created frequency list from the signal generator memory and invalidates the Frequency List Handle. The signal generator must not be in the Generating state when you call this VI. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument

### niFgen Clear Frequency List VI

Removes a previously created frequency list from the signal generator memory and invalidates the **Frequency List Handle**.

Note

[IMAGE alt='icon' src='nifgen-clear-frequency-list-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Frequency List Handle — Frequency List Handle specifies the handle of the frequency list you want the signal generator to remove. You can create multiple frequency lists using the niFgen Create Frequency List VI, which returns a handle that you use to identify each list. Specify a value of -1 to clear all frequency lists. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Frequency List

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-clear-user-standard-waveform-vi.html language=enus -->
## TOPIC 00054: niFgen Clear User Standard Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-clear-user-standard-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-clear-user-standard-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the user-defined waveform created by the niFgen Define User Standard Waveform VI. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or th

### niFgen Clear User Standard Waveform VI

Clears the user-defined waveform created by the [niFgen Define User Standard Waveform](/csh?topicname=nifgen-define-user-standard-waveform-vi.html) VI.

[IMAGE alt='icon' src='nifgen-clear-user-standard-waveform-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Standard Waveform

Parent topic:

Frequency List

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-close-ext-cal-vi.html language=enus -->
## TOPIC 00055: niFgen Close Ext Cal VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-close-ext-cal-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-close-ext-cal-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an NI-FGEN external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies your instrument session. Instrument Handle is

### niFgen Close Ext Cal VI

Closes an NI-FGEN external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM.

[IMAGE alt='icon' src='nifgen-close-ext-cal-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. Action — Action specifies the action to perform upon closing. Input Description Abort Disregards the new calibration constants before closing Commit Stores the new calibration constants on the device before closing error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input | Description |
| Abort | Disregards the new calibration constants before closing |
| Commit | Stores the new calibration constants on the device before closing |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-close-vi.html language=enus -->
## TOPIC 00056: niFgen Close VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-close-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-close-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the following operations: - Closes the instrument I/O session. - Destroys the NI-FGEN session and all of its properties. - Deallocates any memory resources NI-FGEN uses. After calling niFgen Close, you cannot use NI-FGEN again until you call the niFgen Initialize VI or the niFgen Initialize

### niFgen Close VI

Performs the following operations:

- Closes the instrument I/O session.

- Destroys the NI-FGEN session and all of its properties.

- Deallocates any memory resources NI-FGEN uses.

Note

niFgen Initialize

niFgen Initialize With Options

Not all signal routes established by calling the [niFgen Export Signal](nifgen-export-signal-vi.html) VI and the [niFgen Route Signal Out](nifgen-route-signal-out-vi.html) VIs are released when the NI-FGEN session is closed.

| Routes To | Status |
| --- | --- |
| Front Panel | Remains connected |
| RTSI/PXI Backplane | Disconnected |

[IMAGE alt='icon' src='nifgen-close-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-FGEN

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-commit-vi.html language=enus -->
## TOPIC 00057: niFgen Commit VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-commit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-commit-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Causes a transition to the Committed state. This VI verifies property values, reserves the device, and commits the property values to the device. If the property values are all valid, NI-FGEN sets the device hardware configuration to match the session configuration. In the Committed state, waveforms

### niFgen Commit VI

Causes a transition to the Committed state. This VI verifies property values, reserves the device, and commits the property values to the device. If the property values are all valid, NI-FGEN sets the device hardware configuration to match the session configuration.

In the Committed state, waveforms, scripts, and sequences can be loaded into memory. If any properties are changed, NI-FGEN implicitly transitions back to the Idle state. This VI has no effect if the device is already in the Committed or Generating states, and returns a successful status value.

Calling this VI before the [niFgen Initiate Generation](nifgen-initiate-generation-vi.html) VI is optional but has several benefits:

- Routes are committed, so signals are exported or imported.
- Any reference clock and external clock circuits are phase-locked.
- A subsequent niFgen Initiate Generation can run faster because the device is already configured.

[IMAGE alt='icon' src='nifgen-commit-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-analog-filter-vi.html language=enus -->
## TOPIC 00058: niFgen Configure Analog Filter VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-analog-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-analog-filter-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the analog filter for the device. You can apply the analog filter setting in Arbitrary Waveform, Arbitrary Sequence, or Script output mode, or in Frequency List or Standard Function output mode when used with user-defined functions. icon Inputs/Outputs cdbl.png Filter Correction Frequency

### niFgen Configure Analog Filter VI

Configures the analog filter for the device. You can apply the analog filter setting in Arbitrary Waveform, Arbitrary Sequence, or Script output mode, or in Frequency List or Standard Function output mode when used with user-defined functions.

[IMAGE alt='icon' src='nifgen-configure-analog-filter-vi.png']

#### Inputs/Outputs

| Filter Correction Frequency — Filter Correction Frequency specifies the filter correction frequency of the analog filter. For Standard Waveform Output, Filter Correction Frequency should typically be set to be the same as the frequency of the standard waveform. Units: hertz (Hz) Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Analog Filter Enable (default: True) — Analog Filter Enable specifies whether to enable the analog filter. Set Analog Filter Enable to TRUE to enable the analog filter. Default value: True error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Output

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-arbitrary-sequence-vi.html language=enus -->
## TOPIC 00059: niFgen Configure Arbitrary Sequence VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-arbitrary-sequence-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-arbitrary-sequence-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the signal generator properties that affect arbitrary sequence generation. This VI selects the arbitrary sequence to produce and sets the gain and offset. The signal generator must not be in the Generating state when you call this VI. You must set Output Mode to Arbitrary Sequence using

### niFgen Configure Arbitrary Sequence VI

Configures the signal generator properties that affect arbitrary sequence generation. This VI selects the arbitrary sequence to produce and sets the gain and offset.

Note

Note

Output Mode

Arbitrary Sequence

niFgen Configure Output Mode

[IMAGE alt='icon' src='nifgen-configure-arbitrary-sequence-vi.png']

#### Inputs/Outputs

| Offset — Offset specifies the value the signal generator adds to the arbitrary waveform. When you create an arbitrary waveform, you must first normalize the data points to a range of -1.00 to +1.00. You can use this parameter to shift the range of the arbitrary waveform. For example, to configure the output signal to range from 0.00 V to 2.00 V instead of -1.00 V to 1.00 V, set Offset to 1.00. Units: volts (V) Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Sequence Handle — Sequence Handle specifies the handle of the arbitrary sequence to produce. You can create multiple arbitrary sequences using the niFgen Create Arbitrary Sequence VI or the niFgen Create Advanced Arb Sequence VI. These VIs return a handle that you use to identify each sequence. Specify a value of -1 to clear all sequences. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Gain — Gain specifies the factor by which the signal generator scales the arbitrary waveforms in the sequence. When you create an arbitrary waveform, you must first normalize the data points to a range of -1.00 to +1.00. You can use this parameter to scale the waveform to other ranges. The gain is applied before the offset is added. For example, to configure the output signal to range from -2.00 V to +2.00 V, set Gain to 2.00. Units: unitless Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Arbitrary Sequence

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-arbitrary-waveform-vi.html language=enus -->
## TOPIC 00060: niFgen Configure Arbitrary Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-arbitrary-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-arbitrary-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the properties of the signal generator that affect arbitrary waveform generation. Selects the arbitrary waveform to produce and sets the gain and offset. The signal generator must not be in the Generating state when you call this VI. You must set Output Mode parameter of the niFgen Config

### niFgen Configure Arbitrary Waveform VI

Configures the properties of the signal generator that affect arbitrary waveform generation. Selects the arbitrary waveform to produce and sets the gain and offset.

Note

Note

Output Mode

niFgen Configure Output Mode

Arbitrary Waveform

[IMAGE alt='icon' src='nifgen-configure-arbitrary-waveform-vi.png']

#### Inputs/Outputs

| Offset — Offset specifies the value the signal generator adds to the arbitrary waveform. When you create an arbitrary waveform, you must first normalize the data points to a range of -1.00 to +1.00. You can use this parameter to shift the range of the arbitrary waveform. For example, to configure the output signal to range from 0.00 V to 2.00 V instead of -1.00 V to 1.00 V, set Offset to 1.00. Units: volts (V) Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Handle — Waveform Handle selects the arbitrary waveform to produce. You can create multiple arbitrary waveforms using the niFgen Create Waveform (poly) VI, which returns a handle that you use to identify each waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Gain — Gain specifies the factor by which the signal generator scales the arbitrary waveforms in the sequence. When you create an arbitrary waveform, you must first normalize the data points to a range of -1.00 to +1.00. You can use this parameter to scale the waveform to other ranges. The gain is applied before the offset is added. For example, to configure the output signal to range from -2.00 V to +2.00 V, set Gain to 2.00. Units: unitless Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Arbitrary Waveform

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-channels-vi.html language=enus -->
## TOPIC 00061: niFgen Configure Channels VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-channels-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the channels that are used with the instrument specified in Instrument Handle. If you call this VI, you must call it immediately after initializing your session and before configuring any properties or writing data. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identif

### niFgen Configure Channels VI

Configures the channels that are used with the instrument specified in **Instrument Handle**. If you call this VI, you must call it immediately after initializing your session and before configuring any properties or writing data.

[IMAGE alt='icon' src='nifgen-configure-channels-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channels — Channels specifies the channel or channels that all subsequent channel-based properties in the session set. Valid values are non-negative integers. For example, 0 is the only valid value on devices with one channel, while devices with two channels support values of 0 and 1. You can specify more than one channel by inserting commas between values (for example, "0,1"). error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-clock-mode-vi.html language=enus -->
## TOPIC 00062: niFgen Configure Clock Mode VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-clock-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-clock-mode-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the clock mode for the signal generator. Some signal generators allow you to switch the Sample clock to High-Resolution or Automatic Sampling mode with this VI. When you select Divide-Down Sampling, NI-FGEN rounds the sample rate to a frequency that can be achieved by dividing down the board

### niFgen Configure Clock Mode VI

Selects the clock mode for the signal generator.

Some signal generators allow you to switch the Sample clock to High-Resolution or Automatic Sampling mode with this VI.

When you select **Divide-Down Sampling**, NI-FGEN rounds the sample rate to a frequency that can be achieved by dividing down the board clock (Sample clock timebase). However, if you select **High-Resolution Sampling**, you can set the sample rate to any value. If you select **Automatic**, NI-FGEN selects the clock mode based on the sample rate, using divide-down sampling when possible.

Note

Note

Output Mode

Arbitrary Waveform

Arbitrary Sequence

niFgen Configure Output Mode

[IMAGE alt='icon' src='nifgen-configure-clock-mode-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Clock Mode (default: 1=divide down) — Clock Mode sets the clock mode of the signal generator. Default value: 1=divide down Hi Resolution Sampling Sample rate is generated by a high-resolution clock source. Divide Down Sampling Sample rate is generated by dividing the source frequency. Automatic NI-FGEN selects between the divide-down and high-resolution modes error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Hi Resolution Sampling | Sample rate is generated by a high-resolution clock source. |
| Divide Down Sampling | Sample rate is generated by dividing the source frequency. |
| Automatic | NI-FGEN selects between the divide-down and high-resolution modes |

Parent topic:

Configure Clock

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-custom-fir-filter-coefficients-vi.html language=enus -->
## TOPIC 00063: niFgen Configure Custom FIR Filter Coefficients VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-custom-fir-filter-coefficients-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-custom-fir-filter-coefficients-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the FIR filter coefficients used by the onboard signal processing block. The values are coerced to the closest settings achievable by the signal generator. Refer to the FIR Filter topic for your device in the NI Signal Generators Help for more information about FIR filter coefficients. This VI

### niFgen Configure Custom FIR Filter Coefficients VI

Sets the FIR filter coefficients used by the onboard signal processing block. The values are coerced to the closest settings achievable by the signal generator.

Refer to the *FIR Filter* topic for your device in the *NI Signal Generators Help* for more information about FIR filter coefficients. This VI is supported only for the NI 5441.

Note

[IMAGE alt='icon' src='nifgen-configure-custom-fir-filter-coefficients-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. FIR Filter Coefficients — FIR Filter Coefficients specifies the array of data the onboard signal processor uses for the FIR filter coefficients. For the NI 5441, you must wire a symmetric array of 95 coefficients to this parameter. The coefficients should range between -1.00 and +1.00. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Onboard Signal Processing

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-edge-script-trigger-vi.html language=enus -->
## TOPIC 00064: niFgen Configure Digital Edge Script Trigger VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-edge-script-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-edge-script-trigger-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Script trigger for edge triggering. icon Inputs/Outputs ci32.png Edge (Rising) Edge specifies the edge to detect. You can choose Rising Edge or Falling Edge. Default value: Rising civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle

### niFgen Configure Digital Edge Script Trigger VI

Configures a Script trigger for edge triggering.

[IMAGE alt='icon' src='nifgen-configure-digital-edge-script-trigger-vi.png']

#### Inputs/Outputs

| Edge (Rising) — Edge specifies the edge to detect. You can choose Rising Edge or Falling Edge. Default value: Rising Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Trigger ID (Script Trigger 0) — Trigger ID specifies the Script trigger used for triggering. Default value: Script Trigger 0 Source — Source specifies which trigger source the signal generator uses. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-edge-start-trigger-vi.html language=enus -->
## TOPIC 00065: niFgen Configure Digital Edge Start Trigger VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-edge-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-edge-start-trigger-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start trigger for edge triggering. icon Inputs/Outputs ci32.png Edge (Rising) Edge specifies the edge to detect. You can choose Rising Edge or Falling Edge. Default value: Rising civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handl

### niFgen Configure Digital Edge Start Trigger VI

Configures the Start trigger for edge triggering.

[IMAGE alt='icon' src='nifgen-configure-digital-edge-start-trigger-vi.png']

#### Inputs/Outputs

| Edge (Rising) — Edge specifies the edge to detect. You can choose Rising Edge or Falling Edge. Default value: Rising Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Source — Source specifies which trigger source the signal generator uses. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-filter-vi.html language=enus -->
## TOPIC 00066: niFgen Configure Digital Filter VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-filter-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the digital filter for the device. You can apply the digital filter setting in Arbitrary Waveform, Arbitrary Sequence, or Script output mode, or in Frequency List or Standard Function output mode when used with user-defined functions. icon Inputs/Outputs civrn.png Instrument Handle Instru

### niFgen Configure Digital Filter VI

Configures the digital filter for the device. You can apply the digital filter setting in Arbitrary Waveform, Arbitrary Sequence, or Script output mode, or in Frequency List or Standard Function output mode when used with user-defined functions.

[IMAGE alt='icon' src='nifgen-configure-digital-filter-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Digital Filter Enable (default: True) — Digital Filter Enable specifies whether to enable the digital filter. Set Digital Filter Enable to TRUE to enable the digital filter. Default value: True error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Output

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-level-script-trigger-vi.html language=enus -->
## TOPIC 00067: niFgen Configure Digital Level Script Trigger VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-level-script-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-level-script-trigger-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Script trigger for level triggering. icon Inputs/Outputs ci32.png Trigger When (High) Trigger When specifies the active level for the desired trigger. You can select High or Low. Default value: High civrn.png Instrument Handle Instrument Handle identifies a particular instrument session

### niFgen Configure Digital Level Script Trigger VI

Configures a Script trigger for level triggering.

[IMAGE alt='icon' src='nifgen-configure-digital-level-script-trigger-vi.png']

#### Inputs/Outputs

| Trigger When (High) — Trigger When specifies the active level for the desired trigger. You can select High or Low. Default value: High Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Trigger ID (Script Trigger 0) — Trigger ID specifies the Script trigger used for triggering. Default value: Script Trigger 0 Source — Source specifies which trigger source the signal generator uses. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-patterning-vi.html language=enus -->
## TOPIC 00068: niFgen Configure Digital Patterning VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-patterning-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-patterning-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the state of the DIGITAL DATA & CONTROL/DIGITAL PATTERN connector. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen In

### niFgen Configure Digital Patterning VI

Configures the state of the DIGITAL DATA & CONTROL/DIGITAL PATTERN connector.

[IMAGE alt='icon' src='nifgen-configure-digital-patterning-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Digital Patterning Enable (default: True) — Digital Patterning Enable specifies whether pattern signals are present on the DIGITAL DATA & CONTROL/DIGITAL PATTERN connector. Set Digital Patterning Enable to TRUE to specify that pattern signals are present. Default value: True error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Output

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-frequency-list-vi.html language=enus -->
## TOPIC 00069: niFgen Configure Frequency List VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-frequency-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-frequency-list-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the properties of the signal generator that affect frequency list generation. Selects the frequency list to produce and sets the amplitude, DC offset, and start phase. The signal generator must not be in the Generating state when you call this VI. You must set the Output Mode parameter to

### niFgen Configure Frequency List VI

Configures the properties of the signal generator that affect frequency list generation. Selects the frequency list to produce and sets the amplitude, DC offset, and start phase.

Note

Note

Output Mode

Frequency List

niFgen Configure Output Mode

[IMAGE alt='icon' src='nifgen-configure-frequency-list-vi.png']

#### Inputs/Outputs

| DC Offset — DC Offset specifies the DC offset of the standard waveform that you want the signal generator to produce. NI-FGEN sets the DC Offset property to this value. This value is the offset at the output terminal. The value is the offset from ground to the center of the waveform you specify with the Waveform parameter. For example, to configure a waveform with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the DC Offset to 5.00 V. Units: volts (V) Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Frequency List Handle — Frequency List Handle specifies the handle of the frequency list you want the signal generator to produce. You can create multiple frequency lists using the niFgen Create Frequency List VI, which returns a handle that you use to identify each list. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Amplitude — Amplitude specifies the amplitude of the standard waveform that you want the signal generator to produce. NI-FGEN sets the Amplitude property to this value. This value is the amplitude at the output terminal. For example, to produce a waveform ranging from -5.00 V to +5.00 V, set Amplitude to 10.00 V. Units: Vpk-pk Note This parameter does not affect signal generator behavior when you set Waveform Type to DC. Start Phase — Start Phase specifies the horizontal offset of the standard waveform that you want the signal generator to produce. Specify this parameter in degrees of one waveform cycle. NI-FGEN sets the Start Phase property to this value (measured in degrees of one cycle). A start phase of 180 degrees means output generation begins halfway through the waveform. A start phase of 360 degrees offsets the output by an entire waveform cycle and is therefore identical to a start phase of 0 degrees. Note This parameter does not affect signal generator behavior when you set the Waveform parameter to DC Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Frequency List

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-output-impedance-vi.html language=enus -->
## TOPIC 00070: niFgen Configure Output Impedance VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-output-impedance-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-output-impedance-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the output impedance for the channel that you specify. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize Wit

### niFgen Configure Output Impedance VI

Configures the output impedance for the channel that you specify.

[IMAGE alt='icon' src='nifgen-configure-output-impedance-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Impedance (default: 0=50 ohms) — Impedance specifies the impedance value that you want the signal generator to use. NI-FGEN sets the Output Impedance property to this value. Units: ohms Default value: 50 Ω 0 50 Ω 1 75 Ω error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | 50 Ω |
| 1 | 75 Ω |

Parent topic:

Configure Output

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-output-mode-vi.html language=enus -->
## TOPIC 00071: niFgen Configure Output Mode VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-output-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-output-mode-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the output mode of the signal generator. The output mode determines how the signal generator produces waveforms. For example, you can select to generate a standard waveform, an arbitrary waveform, or a sequence of arbitrary waveforms. The signal generator must not be in the Generating sta

### niFgen Configure Output Mode VI

Configures the output mode of the signal generator. The output mode determines how the signal generator produces waveforms. For example, you can select to generate a standard waveform, an arbitrary waveform, or a sequence of arbitrary waveforms.

Note

[IMAGE alt='icon' src='nifgen-configure-output-mode-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Output Mode (default: 0=Standard Function) — Output Mode specifies the output mode that you want the signal generator to use. The value you specify determines which VIs and properties you can use to configure the waveform the signal generator produces. Default value: 0=Standard Function Standard Function Standard Function mode. Frequency List Frequency List mode - Generates a standard function using a list of frequencies you define. Arbitrary Waveform Arbitrary Waveform mode - Generates waveforms from user-created/provided waveform arrays of numeric data. Arbitrary Sequence Arbitrary Sequence mode - Generates downloaded waveforms in the order your specify. Script Script mode - Allows you to use scripting to link and loop multiple waveforms in complex combinations. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Standard Function | Standard Function mode. |
| Frequency List | Frequency List mode - Generates a standard function using a list of frequencies you define. |
| Arbitrary Waveform | Arbitrary Waveform mode - Generates waveforms from user-created/provided waveform arrays of numeric data. |
| Arbitrary Sequence | Arbitrary Sequence mode - Generates downloaded waveforms in the order your specify. |
| Script | Script mode - Allows you to use scripting to link and loop multiple waveforms in complex combinations. |

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-p2p-endpoint-fullness-start-trigger-vi.html language=enus -->
## TOPIC 00072: niFgen Configure P2P Endpoint Fullness Start Trigger VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-p2p-endpoint-fullness-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-p2p-endpoint-fullness-start-trigger-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start trigger for to detect peer-to-peer endpoint fullness. Generation begins when the number of samples in the peer-to-peer endpoint reaches the threshold indicated by the Fullness Level parameter. Because of an additional internal FIFO in the signal generator, the writer peer must a

### niFgen Configure P2P Endpoint Fullness Start Trigger VI

Configures the Start trigger for to detect peer-to-peer endpoint fullness. Generation begins when the number of samples in the peer-to-peer endpoint reaches the threshold indicated by the **Fullness Level** parameter.

Note

[IMAGE alt='icon' src='nifgen-configure-p2p-endpoint-fullness-start-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Fullness Level — Fullness Level specifies the quantity of data in the FIFO endpoint that asserts the trigger. Units: samples per channel error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-reference-clock-vi.html language=enus -->
## TOPIC 00073: niFgen Configure Reference Clock VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-reference-clock-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-reference-clock-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the signal generator Reference clock source and frequency. The signal generator uses the Reference clock to tune the Sample clock timebase of the signal generator so that the frequency stability and accuracy of the Sample clock timebase matches that of the Reference clock. icon Inputs/Out

### niFgen Configure Reference Clock VI

Configures the signal generator Reference clock source and frequency. The signal generator uses the Reference clock to tune the Sample clock timebase of the signal generator so that the frequency stability and accuracy of the Sample clock timebase matches that of the Reference clock.

[IMAGE alt='icon' src='nifgen-configure-reference-clock-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Source — Source specifies the Reference clock source that you want the signal generator to use. For example, when you set this parameter to Clock In, the signal generator uses the signal it receives at the CLK IN front panel connector as the Reference clock. The Reference clock phase-locks with the signal generator Sample clock timebase to allow the frequency stability and accuracy of the Sample clock timebase to match that of the Reference clock. None (0) Specifies that a Reference clock is not used. PXI Clock (1) Specifies the PXI clock is used as the Reference clock source. Clock In (2) Specifies that the CLK IN input signal from the front panel connector is used as the Reference clock source. Onboard Reference Clock (3) Specifies that the onboard reference clock is used as the Reference clock source. RTSI 7 (4) Specifies that the RTSI line 7 is used as the Reference clock source. Ref In (5) Specifies that the REF IN input signal from the front panel connector is used as the Reference clock source. Reference Clock Frequency — Reference Clock Frequency specifies the Reference clock frequency. Units: hertz (Hz) error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| None (0) | Specifies that a Reference clock is not used. |
| PXI Clock (1) | Specifies the PXI clock is used as the Reference clock source. |
| Clock In (2) | Specifies that the CLK IN input signal from the front panel connector is used as the Reference clock source. |
| Onboard Reference Clock (3) | Specifies that the onboard reference clock is used as the Reference clock source. |
| RTSI 7 (4) | Specifies that the RTSI line 7 is used as the Reference clock source. |
| Ref In (5) | Specifies that the REF IN input signal from the front panel connector is used as the Reference clock source. |

Parent topic:

Configure Clock

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-sample-clock-source-vi.html language=enus -->
## TOPIC 00074: niFgen Configure Sample Clock Source VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-sample-clock-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-sample-clock-source-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source of the Sample clock (update clock) of the signal generator. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Init

### niFgen Configure Sample Clock Source VI

Sets the source of the Sample clock (update clock) of the signal generator.

[IMAGE alt='icon' src='nifgen-configure-sample-clock-source-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Source (Onboard Clock) — Source specifies the Sample clock source that you want the signal generator to use. Default value: Onboard Clock For a complete list of the sample clock sources available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. Refer to the Sample Clock Source property for more information about setting this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Clock

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-software-edge-script-trigger-vi.html language=enus -->
## TOPIC 00075: niFgen Configure Software Edge Script Trigger VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-software-edge-script-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-software-edge-script-trigger-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Script trigger for software triggering. Use the niFgen Send Software Edge Trigger VI to assert the trigger condition. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI

### niFgen Configure Software Edge Script Trigger VI

Configures a Script trigger for software triggering. Use the [niFgen Send Software Edge Trigger](/csh?topicname=nifgen-send-software-edge-trigger-vi.html) VI to assert the trigger condition.

[IMAGE alt='icon' src='nifgen-configure-software-edge-script-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Trigger ID (Script Trigger 0) — Trigger ID specifies the Script trigger used for triggering. Default value: Script Trigger 0 error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-software-edge-start-trigger-vi.html language=enus -->
## TOPIC 00076: niFgen Configure Software Edge Start Trigger VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-software-edge-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-software-edge-start-trigger-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start trigger for software triggering. Use the niFgen Send Software Edge Trigger VI to assert the trigger condition. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize V

### niFgen Configure Software Edge Start Trigger VI

Configures the Start trigger for software triggering. Use the [niFgen Send Software Edge Trigger](/csh?topicname=nifgen-send-software-edge-trigger-vi.html) VI to assert the trigger condition.

[IMAGE alt='icon' src='nifgen-configure-software-edge-start-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-standard-waveform-vi.html language=enus -->
## TOPIC 00077: niFgen Configure Standard Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-standard-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-standard-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the properties of the signal generator that affect standard waveform generation. These settings are the waveform, amplitude, DC offset, frequency, and start phase. You must set Output Mode to Standard Function using the niFgen Configure Output Mode VI before calling this VI. icon Inputs/O

### niFgen Configure Standard Waveform VI

Configures the properties of the signal generator that affect standard waveform generation. These settings are the waveform, amplitude, DC offset, frequency, and start phase.

Note

Output Mode

Standard Function

niFgen Configure Output Mode

[IMAGE alt='icon' src='nifgen-configure-standard-waveform-vi.png']

#### Inputs/Outputs

| Channel Name — Channel Name specifies the channel that this VI uses. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Waveform — Waveform specifies the standard waveform that you want the signal generator to produce. NI-FGEN sets the Waveform property to this value. Input Value Waveform Type 0 Sine 1 Square 2 Triangle 3 Ramp Up 4 Ramp Down 5 DC 6 Noise 7 User Frequency — Frequency specifies the frequency of the standard waveform that you want the signal generator to produce. NI-FGEN sets the Frequency property to this value, in hertz (Hz). Note This parameter does not affect signal generator behavior when you set Waveform to DC. Frequency ranges vary by device. Amplitude — Amplitude specifies the amplitude of the standard waveform that you want the signal generator to produce. NI-FGEN sets the Amplitude property to this value. This value is the amplitude at the output terminal. For example, to produce a waveform ranging from -5.00 V to +5.00 V, set Amplitude to 10.00 V. Units: Vpk-pk Note This parameter does not affect signal generator behavior when you set Waveform Type to DC. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Start Phase — Start Phase specifies the horizontal offset of the standard waveform that you want the signal generator to produce. Specify this parameter in degrees of one waveform cycle. NI-FGEN sets the Start Phase property to this value (measured in degrees of one cycle). A start phase of 180 degrees means output generation begins halfway through the waveform. A start phase of 360 degrees offsets the output by an entire waveform cycle and is therefore identical to a start phase of 0 degrees. Note This parameter does not affect signal generator behavior when you set the Waveform parameter to DC DC Offset — DC Offset specifies the DC offset of the standard waveform that you want the signal generator to produce. NI-FGEN sets the DC Offset property to this value. This value is the offset at the output terminal. The value is the offset from ground to the center of the waveform you specify with the Waveform parameter. For example, to configure a waveform with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the DC Offset to 5.00 V. Units: volts (V) Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input Value | Waveform Type |
| 0 | Sine |
| 1 | Square |
| 2 | Triangle |
| 3 | Ramp Up |
| 4 | Ramp Down |
| 5 | DC |
| 6 | Noise |
| 7 | User |

Parent topic:

Standard Waveform

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-synchronization-vi.html language=enus -->
## TOPIC 00078: niFgen Configure Synchronization VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-synchronization-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-synchronization-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the signal generator to receive a synchronization signal to synchronize two or more signal generators. One signal generator should route a SYNC signal to a RTSI line using the niFgen Export Signal VI (niFgen Route Signal Out VI for the NI 5404), and other signal generators should receive the si

### niFgen Configure Synchronization VI

Sets the signal generator to receive a synchronization signal to synchronize two or more signal generators. One signal generator should route a SYNC signal to a RTSI line using the [niFgen Export Signal](/csh?topicname=nifgen-export-signal-vi.html) VI ([niFgen Route Signal Out](/csh?topicname=nifgen-route-signal-out-vi.html) VI for the NI 5404), and other signal generators should receive the signal using this VI.

Note

Note

[IMAGE alt='icon' src='nifgen-configure-synchronization-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Synchronization Source (default: 0=none) — Synchronization Source specifies the source of the synchronization signal you want to use. Default value: 0=none Input Value Synchronization Source 0 NONE 1 TTL0 2 TTL1 3 TTL2 4 TTL3 5 TTL4 6 TTL5 7 TTL6 8 RTSI 0 9 RTSI 1 10 RTSI 2 11 RTSI 3 12 RTSI 4 13 RTSI 5 14 RTSI 6 error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input Value | Synchronization Source |
| 0 | NONE |
| 1 | TTL0 |
| 2 | TTL1 |
| 3 | TTL2 |
| 4 | TTL3 |
| 5 | TTL4 |
| 6 | TTL5 |
| 7 | TTL6 |
| 8 | RTSI 0 |
| 9 | RTSI 1 |
| 10 | RTSI 2 |
| 11 | RTSI 3 |
| 12 | RTSI 4 |
| 13 | RTSI 5 |
| 14 | RTSI 6 |

Parent topic:

Configure Trigger & Synchronization

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-trigger-mode-vi.html language=enus -->
## TOPIC 00079: niFgen Configure Trigger Mode VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-trigger-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-trigger-mode-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the trigger mode for your device. Refer to the Trigger Modes topic for your device in the NI Signal Generators Help for descriptions of the specific behavior for supported trigger modes. The signal generator must be in the Generating state when you call this VI. In Frequency List output mode, S

### niFgen Configure Trigger Mode VI

Sets the trigger mode for your device.

Refer to the Trigger Modes topic for your device in the *NI Signal Generators Help* for descriptions of the specific behavior for supported trigger modes.

Note

Note

[IMAGE alt='icon' src='nifgen-configure-trigger-mode-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Trigger Mode (default: 1=continuous) — Trigger Mode specifies the trigger mode. Default value: 1=continuous Single The signal generator uses Single trigger mode. Continuous The signal generator uses Continuous trigger mode. Burst The signal generator uses Burst trigger mode. Stepped The signal generator uses Stepped trigger mode. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Single | The signal generator uses Single trigger mode. |
| Continuous | The signal generator uses Continuous trigger mode. |
| Burst | The signal generator uses Burst trigger mode. |
| Stepped | The signal generator uses Stepped trigger mode. |

Parent topic:

Configure Trigger & Synchronization

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-configure-trigger-poly-vi.html language=enus -->
## TOPIC 00080: niFgen Configure Trigger (poly) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-configure-trigger-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-configure-trigger-poly-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the trigger source. The signal generator responds to a trigger according to the current trigger mode. The signal generator must not be in the Generating state when you call this VI. icon

### niFgen Configure Trigger (poly) VI

Configures the trigger source. The signal generator responds to a trigger according to the current trigger mode.

Note

[IMAGE alt='icon' src='nifgen-configure-trigger-poly-vi.png']

- [niFgen Configure Digital Edge Start Trigger VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-edge-start-trigger-vi.html) Configures the Start trigger for edge triggering.
- [niFgen Configure Software Edge Start Trigger VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-configure-software-edge-start-trigger-vi.html) Configures the Start trigger for software triggering. Use the niFgen Send Software Edge Trigger VI to assert the trigger condition.
- [niFgen Configure P2P Endpoint Fullness Start Trigger VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-configure-p2p-endpoint-fullness-start-trigger-vi.html) Configures the Start trigger for to detect peer-to-peer endpoint fullness. Generation begins when the number of samples in the peer-to-peer endpoint reaches the threshold indicated by the Fullness Level parameter.
- [niFgen Disable Start Trigger VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-disable-start-trigger-vi.html) Disables the Start trigger.
- [niFgen Configure Digital Edge Script Trigger VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-edge-script-trigger-vi.html) Configures a Script trigger for edge triggering.
- [niFgen Configure Digital Level Script Trigger VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-configure-digital-level-script-trigger-vi.html) Configures a Script trigger for level triggering.
- [niFgen Configure Software Edge Script Trigger VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-configure-software-edge-script-trigger-vi.html) Configures a Script trigger for software triggering. Use the niFgen Send Software Edge Trigger VI to assert the trigger condition.
- [niFgen Disable Script Trigger VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-disable-script-trigger-vi.html) Disables the Script trigger.

Parent topic:

Configure Trigger & Synchronization

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-create-advanced-arb-sequence-vi.html language=enus -->
## TOPIC 00081: niFgen Create Advanced Arb Sequence VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-create-advanced-arb-sequence-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-create-advanced-arb-sequence-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an arbitrary sequence from an array of waveform handles and an array of corresponding loop counts. This VI returns a handle that identifies the sequence. You pass this handle to the niFgen Configure Arbitrary Sequence VI to specify what arbitrary sequence you want the signal generator to pro

### niFgen Create Advanced Arb Sequence VI

Creates an arbitrary sequence from an array of waveform handles and an array of corresponding loop counts. This VI returns a handle that identifies the sequence. You pass this handle to the [niFgen Configure Arbitrary Sequence](/csh?topicname=nifgen-configure-arbitrary-sequence-vi.html) VI to specify what arbitrary sequence you want the signal generator to produce.

Note

Note

Output Mode

niFgen Configure Output Mode

Arbitrary Sequence

An arbitrary sequence consists of multiple waveforms. For each waveform, you specify the number of times the signal generator produces the waveform before proceeding to the next waveform. The number of times to repeat a specific waveform is called the loop count.

niFgen Create Advanced Arb Sequence VI extends the [niFgen Create Arbitrary Sequence](nifgen-create-arbitrary-sequence-vi.html) VI by adding the ability to set the number of samples in each sequence step and to set marker locations.

[IMAGE alt='icon' src='nifgen-create-advanced-arb-sequence-vi.png']

#### Inputs/Outputs

| Marker Location Array — Marker Location Array specifies the array of marker locations where you want a marker to be generated in the sequence. Each Marker Location Array element corresponds to a Waveform Handles Array element and indicates where in the waveform a marker is to occur. The marker location must be less than the size of the waveform the marker is in. If you do not want a marker generated for a particular sequence stage, set the marker location to -1 (no marker). Loop Counts Array — Loop Counts Array specifies the array of loop counts that you want to use to create a new arbitrary sequence. Each Loop Counts Array element corresponds to a Waveform Handles Array element and indicates how many times to repeat that waveform. Each element of the Loop Count Array must be less than or equal to the maximum loop count the signal generator allows. You can obtain the maximum loop count from the Maximum Loop Count parameter of the niFgen Query Arb Sequence Capabilities VI. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Sequence Length — Sequence Length specifies the number of waveforms in the new arbitrary sequence that you want to create. The value you pass must be between the minimum and maximum sequence lengths the signal generator allows, which on some signal generators depend on the remaining unallocated memory. You can obtain the minimum and maximum sequence lengths from the Minimum Sequence Length and Maximum Sequence Length parameters in the niFgen Query Arb Sequence Capabilities VI. Waveform Handles Array — Waveform Handles Array specifies the array of waveform handles from which you want to create a new arbitrary sequence. Each Waveform Handles Array element has a corresponding Loop Counts Array element that indicates how many times that waveform is repeated. You obtain waveform handles when you create arbitrary waveforms with the niFgen Create Waveform (poly) VI or the niFgen Allocate Waveform VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Sample Counts Array — Sample Counts Array specifies the array of sample counts that you want to use to create a new arbitrary sequence. Sample Counts Array element corresponds to a Waveform Handles Array element and indicates the subset, in samples, of the given waveform to generate. Each element of the Sample Count Array must be larger than the minimum waveform size, a multiple of the waveform quantum and no larger than the number of samples in the corresponding waveform. You can obtain these values by calling the niFgen Query Arb Waveform Capabilities VI. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Coerced Markers Array — Coerced Markers Array returns an array of all given markers that are coerced (rounded) to the nearest marker quantum. Not all devices coerce markers. Sequence Handle — Sequence Handle returns a handle that identifies the new sequence. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Arbitrary Sequence

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-create-arbitrary-sequence-vi.html language=enus -->
## TOPIC 00082: niFgen Create Arbitrary Sequence VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-create-arbitrary-sequence-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-create-arbitrary-sequence-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an arbitrary sequence from an array of waveform handles and an array of corresponding loop counts. This VI returns a handle that identifies the sequence. You pass this handle to the niFgen Configure Arbitrary Sequence VI to specify what arbitrary sequence you want the signal generator to pro

### niFgen Create Arbitrary Sequence VI

Creates an arbitrary sequence from an array of waveform handles and an array of corresponding loop counts. This VI returns a handle that identifies the sequence. You pass this handle to the [niFgen Configure Arbitrary Sequence](/csh?topicname=nifgen-configure-arbitrary-sequence-vi.html) VI to specify what arbitrary sequence you want the signal generator to produce.

Note

Note

Output Mode

Arbitrary Sequence

niFgen Configure Output Mode

An arbitrary sequence consists of multiple waveforms. For each waveform, you can specify the number of times that the signal generator produces the waveform before proceeding to the next waveform. The number of times to repeat a specific waveform is called the *loop count*.

[IMAGE alt='icon' src='nifgen-create-arbitrary-sequence-vi.png']

#### Inputs/Outputs

| Loop Counts Array — Loop Counts Array specifies the array of loop counts that you want to use to create a new arbitrary sequence. Each Loop Counts Array element corresponds to a Waveform Handles Array element and indicates how many times to repeat that waveform. Each element of the Loop Count Array must be less than or equal to the maximum loop count the signal generator allows. You can obtain the maximum loop count from the Maximum Loop Count parameter of the niFgen Query Arb Sequence Capabilities VI. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Sequence Length — Sequence Length specifies the number of waveforms in the new arbitrary sequence that you want to create. The value you pass must be between the minimum and maximum sequence lengths the signal generator allows, which on some signal generators depend on the remaining unallocated memory. You can obtain the minimum and maximum sequence lengths from the Minimum Sequence Length and Maximum Sequence Length parameters in the niFgen Query Arb Sequence Capabilities VI. Waveform Handles Array — Waveform Handles Array specifies the array of waveform handles from which you want to create a new arbitrary sequence. Each Waveform Handles Array element has a corresponding Loop Counts Array element that indicates how many times that waveform is repeated. You obtain waveform handles when you create arbitrary waveforms with the niFgen Create Waveform (poly) VI or the niFgen Allocate Waveform VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Sequence Handle — Sequence Handle returns a handle that identifies the new sequence. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Arbitrary Sequence

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-create-frequency-list-vi.html language=enus -->
## TOPIC 00083: niFgen Create Frequency List VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-create-frequency-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-create-frequency-list-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a frequency list from an array of frequencies and an array of durations. The two arrays should have the same number of elements. The VI returns a handle that identifies the frequency list. You can pass this handle to the niFgen Configure Frequency List VI to specify what frequency list you w

### niFgen Create Frequency List VI

Creates a frequency list from an array of frequencies and an array of durations. The two arrays should have the same number of elements. The VI returns a handle that identifies the frequency list. You can pass this handle to the [niFgen Configure Frequency List](/csh?topicname=nifgen-configure-frequency-list-vi.html) VI to specify what frequency list you want the signal generator to produce.

Note

Note

Output Mode

Frequency List

niFgen Configure Output Mode

A frequency list consists of a list of frequencies and durations. The signal generator generates each frequency for the given amount of time and then moves on to the next frequency. When the end of the list is reached, the signal generator starts over at the beginning of the list.

[IMAGE alt='icon' src='nifgen-create-frequency-list-vi.png']

#### Inputs/Outputs

| Frequency Array — Frequency Array specifies the array of frequencies to form the frequency list. The array must have at least as many elements as the value you specify in the Frequency List Length parameter. Each Frequency Array element has a corresponding Duration Array element that indicates how long that frequency is repeated. Units: hertz (Hz) Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Frequency List Length — Frequency List Length if specified, controls the number of steps in the frequency list. The value must be between the minimum and maximum frequency list lengths that the signal generator allows. You can obtain the minimum and maximum frequency list lengths from the Minimum Frequency List Length and Maximum Frequency List Length parameters in the niFgen Query Freq List Capabilities VI. The Frequency Array and the Duration Array parameters must each be at least as long as the frequency list length if one is specified. Waveform — Waveform specifies the standard waveform that you want the signal generator to produce. NI-FGEN sets the Waveform property to this value. Input Value Waveform Type 0 Sine 1 Square 2 Triangle 3 Ramp Up 4 Ramp Down 5 DC 6 Noise 7 User error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Duration Array — Duration Array specifies the array of durations to form the frequency list. The array must have at least as many elements as the value that you specify in the Frequency List Length parameter. Each Duration Array element has a corresponding Frequency Array element and indicates how long in seconds to generate the corresponding frequency. Units: seconds Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Frequency List Handle — Frequency List Handle specifies the handle of the frequency list you want the signal generator to produce. You can create multiple frequency lists using the niFgen Create Frequency List VI. niFgen Create Frequency List returns a handle that you use to identify each list. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input Value | Waveform Type |
| 0 | Sine |
| 1 | Square |
| 2 | Triangle |
| 3 | Ramp Up |
| 4 | Ramp Down |
| 5 | DC |
| 6 | Noise |
| 7 | User |

Parent topic:

Frequency List

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-complex-dbl-vi.html language=enus -->
## TOPIC 00084: niFgen Create Waveform (Complex DBL) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-complex-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-complex-dbl-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an onboard waveform from complex double-precision floating-point data for use in Arbitrary Waveform or Arbitrary Sequence output mode on devices with the OSP Enabled property set to TRUE and the Data Processing Mode property set to Complex. The Waveform Handle returned by the VI can be used

### niFgen Create Waveform (Complex DBL) VI

Creates an onboard waveform from complex double-precision floating-point data for use in Arbitrary Waveform or Arbitrary Sequence output mode on devices with the [OSP Enabled](/csh?context=nifgen_nifgenpropref_pnifgen_ospenabled) property set to TRUE and the [Data Processing Mode](/csh?context=nifgen_nifgenpropref_pnifgen_dataprocessingmode) property set to **Complex**. The **Waveform Handle** returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.

[IMAGE alt='icon' src='nifgen-create-waveform-complex-dbl-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Data Array — Waveform Data Array specifies the array of data you want to load into the new waveform. The array must have at least as many elements as the value that you specify in the Waveform Size parameter. You must normalize the data points in the array to be between -1.00 and +1.00. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle — Waveform Handle returns a handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Create Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-complex-wdt-vi.html language=enus -->
## TOPIC 00085: niFgen Create Waveform (Complex WDT) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-complex-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-complex-wdt-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an onboard waveform from WDT data for use in Arbitrary Waveform or Arbitrary Sequence output mode. The Waveform Handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is

### niFgen Create Waveform (Complex WDT) VI

Creates an onboard waveform from WDT data for use in Arbitrary Waveform or Arbitrary Sequence output mode. The **Waveform Handle** returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.

[IMAGE alt='icon' src='nifgen-create-waveform-complex-wdt-vi.png']

#### Inputs/Outputs

| Use Waveform dT for IQ Rate — Use Waveform dT for IQ Rate specifies whether the I/Q rate should be set to match the sampling information contained in the Waveform parameter. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform — Waveform specifies the data you want to use for the arbitrary waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle — Waveform Handle returns a handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Create Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-dbl-vi.html language=enus -->
## TOPIC 00086: niFgen Create Waveform (DBL) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-dbl-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an onboard waveform from double-precision floating-point data for use in Arbitrary Waveform or Arbitrary Sequence output mode. The waveform handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or dele

### niFgen Create Waveform (DBL) VI

Creates an onboard waveform from double-precision floating-point data for use in Arbitrary Waveform or Arbitrary Sequence output mode. The waveform handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.

[IMAGE alt='icon' src='nifgen-create-waveform-dbl-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Data Array — Waveform Data Array specifies the array of data you want to load into the new waveform. You must normalize the data points in the array to be between -1.00 and +1.00. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle — Waveform Handle returns a handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Create Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-from-file-dbl-vi.html language=enus -->
## TOPIC 00087: niFgen Create Waveform From File (DBL) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-from-file-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-from-file-dbl-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Takes waveform data from a specified file of double-precision floating-point data and creates an onboard waveform for use in Arbitrary Waveform or Arbitrary Sequence output mode. The Waveform Handle returned can be used later for setting the active waveform, changing the data in the waveform, buildi

### niFgen Create Waveform From File (DBL) VI

Takes waveform data from a specified file of double-precision floating-point data and creates an onboard waveform for use in Arbitrary Waveform or Arbitrary Sequence output mode. The **Waveform Handle** returned can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.

Note

Gain

niFgen Configure Arbitrary Waveform

niFgen Configure Arbitrary Sequence

[IMAGE alt='icon' src='nifgen-create-waveform-from-file-dbl-vi.png']

#### Inputs/Outputs

| Byte Order — Byte Order specifies the byte order of the data in the file: Big Endian or Little Endian Note Data written by most applications in Windows (including LabWindows™/CVI™) is in Little Endian format. Data written to a file from LabVIEW is in Big Endian format by default on all platforms. (Big Endian and Little Endian refer to the way data is stored in memory, which can differ on different processors.) Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. File Name — File Name specifies the full path and name of the file where the waveform data resides. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle — Waveform Handle returns a handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Create Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-from-file-i16-vi.html language=enus -->
## TOPIC 00088: niFgen Create Waveform From File (I16) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-from-file-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-from-file-i16-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Takes binary data from a specified file of 16-bit integers and creates an onboard waveform for use in Arbitrary Waveform or Arbitrary Sequence output mode. The Waveform Handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences

### niFgen Create Waveform From File (I16) VI

Takes binary data from a specified file of 16-bit integers and creates an onboard waveform for use in Arbitrary Waveform or Arbitrary Sequence output mode. The **Waveform Handle** returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.

This VI can also create an onboard waveform from complex data for use on devices with the [OSP Enabled](/csh?context=nifgen_nifgenpropref_pnifgen_ospenabled) property set to **TRUE** and the [Data Processing Mode](/csh?context=nifgen_nifgenpropref_pnifgen_dataprocessingmode) property set to **Complex**. To write complex data, you must interleave the I and Q value pairs.

[IMAGE alt='icon' src='nifgen-create-waveform-from-file-i16-vi.png']

#### Inputs/Outputs

| Byte Order — Byte Order specifies the byte order of the data in the file: Big Endian or Little Endian. Note Data written by most applications in Windows (including LabWindows/CVI) is in Little Endian format. Data written to a file from LabVIEW is in Big Endian format by default on all platforms. (Big Endian and Little Endian refer to the way data is stored in memory, which can differ on different processors.) The 16-bit integer, or I16, data (values between -32768 and +32767) is assumed to represent -1 to +1 volts. Use the Gain parameter of the niFgen Configure Arbitrary Waveform VI or niFgen Configure Arbitrary Sequence VI to generate different voltages. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. File Name — File Name specifies the full path and name of the file where the waveform data resides. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle — Waveform Handle returns a handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Create Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-i16-vi.html language=enus -->
## TOPIC 00089: niFgen Create Waveform (I16) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-i16-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an onboard waveform from I16 data for use in Arbitrary Waveform or Arbitrary Sequence output mode. The Waveform Handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is

### niFgen Create Waveform (I16) VI

Creates an onboard waveform from I16 data for use in Arbitrary Waveform or Arbitrary Sequence output mode. The **Waveform Handle** returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.

This VI can also create an onboard waveform from complex data for use on devices with the[OSP Enabled](/csh?context=nifgen_nifgenpropref_pnifgen_ospenabled) property set to **TRUE** and the [Data Processing Mode](/csh?context=nifgen_nifgenpropref_pnifgen_dataprocessingmode) property set to **Complex**. To write complex data, you must interleave the I and Q value pairs.

[IMAGE alt='icon' src='nifgen-create-waveform-i16-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Data Array — Waveform Data Array specifies the array of data you want to use for the new arbitrary waveform. You must normalize the data points in the array to be between -32768 and 32767 inclusive. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle — Waveform Handle returns a handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Create Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-poly-vi.html language=enus -->
## TOPIC 00090: niFgen Create Waveform (poly) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-poly-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Takes the data provided and creates an onboard waveform of the same size for use in Arbitrary Waveform or Arbitrary Sequence output mode. The Waveform Handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or d

### niFgen Create Waveform (poly) VI

Takes the data provided and creates an onboard waveform of the same size for use in Arbitrary Waveform or Arbitrary Sequence output mode.

The **Waveform Handle** returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.

Note

Note

Output Mode

Arbitrary Waveform

Arbitrary Sequence

niFgen Configure Output Mode

[IMAGE alt='icon' src='nifgen-create-waveform-poly-vi.png']

- [niFgen Create Waveform (DBL) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-dbl-vi.html) Creates an onboard waveform from double-precision floating-point data for use in Arbitrary Waveform or Arbitrary Sequence output mode. The waveform handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.
- [niFgen Create Waveform (I16) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-i16-vi.html) Creates an onboard waveform from I16 data for use in Arbitrary Waveform or Arbitrary Sequence output mode. The Waveform Handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.
- [niFgen Create Waveform (WDT) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-wdt-vi.html) Creates an onboard waveform from WDT data for use in Arbitrary Waveform or Arbitrary Sequence output mode. The Waveform Handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.
- [niFgen Create Waveform (Complex DBL) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-complex-dbl-vi.html) Creates an onboard waveform from complex double-precision floating-point data for use in Arbitrary Waveform or Arbitrary Sequence output mode on devices with the OSP Enabled property set to TRUE and the Data Processing Mode property set to Complex . The Waveform Handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.
- [niFgen Create Waveform (Complex WDT) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-complex-wdt-vi.html) Creates an onboard waveform from WDT data for use in Arbitrary Waveform or Arbitrary Sequence output mode. The Waveform Handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.
- [niFgen Create Waveform From File (DBL) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-from-file-dbl-vi.html) Takes waveform data from a specified file of double-precision floating-point data and creates an onboard waveform for use in Arbitrary Waveform or Arbitrary Sequence output mode. The Waveform Handle returned can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.
- [niFgen Create Waveform From File (I16) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-from-file-i16-vi.html) Takes binary data from a specified file of 16-bit integers and creates an onboard waveform for use in Arbitrary Waveform or Arbitrary Sequence output mode. The Waveform Handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.

Parent topic:

Arbitrary Waveform

Parent topic:

Arbitrary Sequence

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-wdt-vi.html language=enus -->
## TOPIC 00091: niFgen Create Waveform (WDT) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-create-waveform-wdt-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an onboard waveform from WDT data for use in Arbitrary Waveform or Arbitrary Sequence output mode. The Waveform Handle returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is

### niFgen Create Waveform (WDT) VI

Creates an onboard waveform from WDT data for use in Arbitrary Waveform or Arbitrary Sequence output mode. The **Waveform Handle** returned by the VI can be used later for setting the active waveform, changing the data in the waveform, building sequences of waveforms, or deleting the waveform when it is no longer needed.

Note

Gain

niFgen Configure Arbitrary Waveform

niFgen Configure Arbitrary Sequence

Note

Use Waveform dT for Sample Rate

Use Waveform dT for Rate

niFgen Set Sample Rate

Sample Rate

[IMAGE alt='icon' src='nifgen-create-waveform-wdt-vi.png']

#### Inputs/Outputs

| Use Waveform dT for Sample Rate — Use Waveform dT for Sample Rate specifies whether the sample rate should be set to match the sampling information contained in the Waveform parameter. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform — Waveform specifies the data you want to use for the arbitrary waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle — Waveform Handle returns a handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Create Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-define-user-standard-waveform-vi.html language=enus -->
## TOPIC 00092: niFgen Define User Standard Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-define-user-standard-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-define-user-standard-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a user waveform for either Standard Function or Frequency List output mode. To select the waveform, set the Waveform parameter of the niFgen Configure Standard Waveform VI or niFgen Create Frequency List VI to User. The waveform data must be scaled between -1.0 and 1.0. Use the Amplitude par

### niFgen Define User Standard Waveform VI

Defines a user waveform for either Standard Function or Frequency List output mode.

To select the waveform, set the **Waveform** parameter of the [niFgen Configure Standard Waveform](nifgen-configure-standard-waveform-vi.html) VI or [niFgen Create Frequency List](nifgen-create-frequency-list-vi.html) VI to **User**.

The waveform data must be scaled between -1.0 and 1.0. Use the **Amplitude** parameter of the [niFgen Configure Standard Waveform](nifgen-configure-standard-waveform-vi.html) VI to generate different output voltages.

Note

Output Mode

Standard Function

Frequency List

niFgen Configure Output Mode

[IMAGE alt='icon' src='nifgen-define-user-standard-waveform-vi.png']

#### Inputs/Outputs

| Channel Name — Channel Name specifies the channel that this VI uses. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Waveform Size — Waveform Size specifies the size of the waveform in samples. Waveform Data Array — Waveform Data Array specifies the array of data you want to load into the new waveform. You must normalize the data points in the array to be between -1.00 and +1.00. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Standard Waveform

Parent topic:

Frequency List

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-delete-named-waveform-vi.html language=enus -->
## TOPIC 00093: niFgen Delete Named Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-delete-named-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-delete-named-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the specified named waveform from onboard memory. The signal generator must not be in the Generating state when you call this VI. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initia

### niFgen Delete Named Waveform VI

Deletes the specified named waveform from onboard memory.

Note

[IMAGE alt='icon' src='nifgen-delete-named-waveform-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Name — Waveform Name specifies the name of the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Script

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-delete-script-vi.html language=enus -->
## TOPIC 00094: niFgen Delete Script VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-delete-script-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-delete-script-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the specified script from onboard memory. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. c

### niFgen Delete Script VI

Deletes the specified script from onboard memory.

[IMAGE alt='icon' src='nifgen-delete-script-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Script Name — Script Name specifies the name of the script you want to delete. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Script

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-detach-grpc-session-vi.html language=enus -->
## TOPIC 00095: niFgen Detach gRPC Session VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-detach-grpc-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-detach-grpc-session-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session specified in instrument handle but leaves the session open on the NI gRPC Device Server. NI-FGEN returns an error unless an open session at instrument handle exists and was created using the niFgen Initialize With Channels for gRPC session VI or the niFgen Attach gRPC Session VI.

### niFgen Detach gRPC Session VI

Closes the session specified in **instrument handle** but leaves the session open on the NI gRPC Device Server.

NI-FGEN returns an error unless an open session at **instrument handle** exists and was created using the [niFgen Initialize With Channels for gRPC session](/csh?context=nifgen_nifgenlv_nifgenlv.chm::nifgen_initialize_with_channels_for_grpc_session) VI or the [niFgen Attach gRPC Session](/csh?context=nifgen_nifgenlv_nifgenlv.chm::nifgen_attach_grpc_session) VI.

[IMAGE alt='icon' src='nifgen-detach-grpc-session-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize With Channels for gRPC session VI or the niFgen Attach gRPC Session VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

MeasurementLink

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-disable-script-trigger-vi.html language=enus -->
## TOPIC 00096: niFgen Disable Script Trigger VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-disable-script-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-disable-script-trigger-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the Script trigger. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. cstr.png Trigger ID (S

### niFgen Disable Script Trigger VI

Disables the Script trigger.

[IMAGE alt='icon' src='nifgen-disable-script-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Trigger ID (Script Trigger 0) — Trigger ID specifies the Script trigger used for triggering. Default value: Script Trigger 0 error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-disable-start-trigger-vi.html language=enus -->
## TOPIC 00097: niFgen Disable Start Trigger VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-disable-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-disable-start-trigger-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the Start trigger. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. cerrcodeclst.png error

### niFgen Disable Start Trigger VI

Disables the Start trigger.

[IMAGE alt='icon' src='nifgen-disable-start-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-disable-vi.html language=enus -->
## TOPIC 00098: niFgen Disable VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-disable-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-disable-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected. The analog output and all exported signals are disabled. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handl

### niFgen Disable VI

Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected. The analog output and all exported signals are disabled.

[IMAGE alt='icon' src='nifgen-disable-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-error-message-vi.html language=enus -->
## TOPIC 00099: niFgen Error Message VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-error-message-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-error-message-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a status code returned by an NI-FGEN VI into a user-readable string. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen In

### niFgen Error Message VI

Converts a status code returned by an NI-FGEN VI into a user-readable string.

[IMAGE alt='icon' src='nifgen-error-message-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Message Box (default: don't show) — Message Box specifies whether or not a dialog message is shown. Default value: Don't show Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Error Code — Error Code specifies the code parameter that is returned from any of the NI-FGEN VIs. Error Message — Error Message returns the user-readable message string that corresponds to the status code you specify. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-export-attribute-configuration-buffer-vi.html language=enus -->
## TOPIC 00100: niFgen Export Attribute Configuration Buffer VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-export-attribute-configuration-buffer-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-export-attribute-configuration-buffer-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a session configuration to a buffer. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. cerrco

### niFgen Export Attribute Configuration Buffer VI

Exports a session configuration to a buffer.

[IMAGE alt='icon' src='nifgen-export-attribute-configuration-buffer-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. buffer — buffer is a byte array that contains the exported configuration. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Requirements for Exporting and Importing Arbitrary Waveforms**

Arbitrary waveforms you export and import between sessions using this VI must meet the following criteria:

- All waveforms in the exporting session are created from files using the niFgen Create Waveform (poly) VI
- The full file path of the file containing the arbitrary waveform still exists upon import
- All waveforms are defined using handles rather than names
- All waveforms are completenone are streamed or incrementally written

You can set the device mode with the [niFgen Configure Output Mode](nifgen-configure-output-mode-vi.html) VI. For more information on arbitrary waveform mode, refer to [Arbitrary Waveform Output Mode](/csh?context=nifgen_siggenhelp_arb_mode) and [Configure Arbitrary Waveform Mode](/csh?context=nifgen_siggenhelp_programming_arb_waveform).

**Channel Mapping Behavior**

When exporting and importing configurations between NI‑FGEN sessions that were initialized with different channels using the **channel name** input to the [niFgen Initialize With Channels](nifgen-initialize-with-channels-vi.html) VI, the configuration of the exporting channel is mapped to the importing channel.

For example, if your entry for **channel name** is 0 for the exporting session and 1 for the importing session, the configuration exported from channel 0 is imported into channel 1.

Note

Parent topic:

niFgen Export Attribute Configuration(poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-export-attribute-configuration-file-vi.html language=enus -->
## TOPIC 00101: niFgen Export Attribute Configuration File VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-export-attribute-configuration-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-export-attribute-configuration-file-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a session configuration to the specified file. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels

### niFgen Export Attribute Configuration File VI

Exports a session configuration to the specified file.

[IMAGE alt='icon' src='nifgen-export-attribute-configuration-file-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. file path — file path is the absolute path to a placeholder file you must create to contain the configuration you want to export. If you specify an empty or relative path, this VI returns an error. Default file extension: .nifgenconfig error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Requirements for Exporting and Importing Arbitrary Waveforms**

Arbitrary waveforms you export and import between sessions using this VI must meet the following criteria:

- All waveforms in the exporting session are created from files using the niFgen Create Waveform (poly) VI
- The full file path of the file containing the arbitrary waveform still exists upon import
- All waveforms are defined using handles rather than names
- All waveforms are completenone are streamed or incrementally written

You can set the device mode with the [niFgen Configure Output Mode](nifgen-configure-output-mode-vi.html) VI. For more information on arbitrary waveform mode, refer to [Arbitrary Waveform Output Mode](/csh?context=nifgen_siggenhelp_arb_mode) and [Configure Arbitrary Waveform Mode](/csh?context=nifgen_siggenhelp_programming_arb_waveform).

**Channel Mapping Behavior**

When exporting and importing configurations between NI‑FGEN sessions that were initialized with different channels using the **channel name** input to the [niFgen Initialize With Channels](nifgen-initialize-with-channels-vi.html) VI, the configuration of the exporting channel is mapped to the importing channel.

For example, if your entry for **channel name** is 0 for the exporting session and 1 for the importing session, the configuration exported from channel 0 is imported into channel 1.

Note

Parent topic:

niFgen Export Attribute Configuration(poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-export-attribute-configuration-poly-vi.html language=enus -->
## TOPIC 00102: niFgen Export Attribute Configuration(poly) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-export-attribute-configuration-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-export-attribute-configuration-poly-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a session configuration to either a file or a buffer. You can export and import supported configurations only between NI‑FGEN devices with identical bus types, model numbers, and channel counts, as well as the same number of initialized channels. This VI verifies that the attributes you have

### niFgen Export Attribute Configuration(poly) VI

Exports a session configuration to either a file or a buffer.

You can export and import supported configurations only between NI‑FGEN devices with identical bus types, model numbers, and channel counts, as well as the same number of initialized channels.

This VI verifies that the attributes you have configured for the session are valid. If the configuration is invalid, NI‑FGEN returns an error.

**Supported Configurations**

You can export and import the following between NI‑FGEN sessions:

- Attribute configurations
- Arbitrary waveforms

**Related topics:**

[Setting Attributes Before Reading Attributes](/csh?context=nifgen_siggenhelp_setting_before_reading_attributes)

[Output Modes](/csh?context=nifgen_siggenhelp_output_arb_freq_script_seq)

[IMAGE alt='icon' src='nifgen-export-attribute-configuration-poly-vi.png']

#### Details

**Requirements for Exporting and Importing Arbitrary Waveforms**

Arbitrary waveforms you export and import between sessions using this VI must meet the following criteria:

- All waveforms in the exporting session are created from files using the niFgen Create Waveform (poly) VI
- The full file path of the file containing the arbitrary waveform still exists upon import
- All waveforms are defined using handles rather than names
- All waveforms are completenone are streamed or incrementally written

You can set the device mode with the [niFgen Configure Output Mode](nifgen-configure-output-mode-vi.html) VI. For more information on arbitrary waveform mode, refer to [Arbitrary Waveform Output Mode](/csh?context=nifgen_siggenhelp_arb_mode) and [Configure Arbitrary Waveform Mode](/csh?context=nifgen_siggenhelp_programming_arb_waveform).

**Channel Mapping Behavior**

When exporting and importing configurations between NI‑FGEN sessions that were initialized with different channels using the **channel name** input to the [niFgen Initialize With Channels](nifgen-initialize-with-channels-vi.html) VI, the configuration of the exporting channel is mapped to the importing channel.

For example, if your entry for **channel name** is 0 for the exporting session and 1 for the importing session, the configuration exported from channel 0 is imported into channel 1.

Note

- [niFgen Export Attribute Configuration File VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-export-attribute-configuration-file-vi.html) Exports a session configuration to the specified file.
- [niFgen Export Attribute Configuration Buffer VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-export-attribute-configuration-buffer-vi.html) Exports a session configuration to a buffer.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-export-signal-vi.html language=enus -->
## TOPIC 00103: niFgen Export Signal VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-export-signal-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-export-signal-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes signals (clocks, triggers, and events) to the output terminal you specify. Any routes created within a session persist after the session closes to prevent signal glitching. To unconfigure signal routes created in previous sessions, set Reset Device in niFgen Initialize to TRUE or use niFgen R

### niFgen Export Signal VI

Routes signals (clocks, triggers, and events) to the output terminal you specify.

Any routes created within a session persist after the session closes to prevent signal glitching. To unconfigure signal routes created in previous sessions, set **Reset Device** in [niFgen Initialize](nifgen-initialize-vi.html) to TRUE or use [niFgen Reset Device](nifgen-reset-device-vi.html).

If you export a signal with this VI and commit the session, the signal is routed to the output terminal you specify.

[IMAGE alt='icon' src='nifgen-export-signal-vi.png']

#### Inputs/Outputs

| Output Terminal (do not export) — Output Terminal specifies the terminal to export the signal (clock, trigger, or event). Default Value: do not export Note The following defined values are examples of possible output terminals. For a complete list of the output terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. Do not export signal The signal is not exported. PFI 0 The signal is exported on PFI 0. PFI 1 The signal is exported on PFI 1. PFI 4 The signal is exported on PFI 4. PFI 5 The signal is exported on PFI 5. PXI_TRIG_0 The signal is exported on PXI or RTSI line 0. PXI_TRIG_1 The signal is exported on PXI or RTSI line 1. PXI_TRIG_2 The signal is exported on PXI or RTSI line 2. PXI_TRIG_3 The signal is exported on PXI or RTSI line 3. PXI_TRIG_4 The signal is exported on PXI or RTSI line 4. PXI_TRIG_5 The signal is exported on PXI or RTSI line 5. PXI_TRIG_6 The signal is exported on PXI or RTSI line 6. PXI_TRIG_7 The signal is exported on PXI or RTSI line 7. DDC_ClkOut The signal is exported on the CLK OUT line on the DDC connector. PXI_STAR The signal is exported on the PXI star line. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Signal Identifier (None) — Signal Identifier specifies which instance of the selected signals to export. Default value: None None Default (for non instance-based signals) ScriptTrigger0 Script trigger 0 ScriptTrigger1 Script trigger 1 ScriptTrigger2 Script trigger 2 ScriptTrigger3 Script trigger 3 Marker0 Marker 0 Marker1 Marker 1 Marker2 Marker 2 Marker3 Marker 3 DataMarker0 Data Marker 0 * DataMarker1 Data Marker 1 * DataMarker2 Data Marker 2 * DataMarker3 Data Marker 3 * *These Data Marker values apply only to single-channel devices or to multichannel devices that are configured for single-channel operation. When using a device that is configured for multichannel operation, specify the channel number along with the signal identifier. For example, to export Data Marker 0 on channel 1 of a device configured for multichannel operation, use the value 1/ DataMarker0. If you do not specify a channel when using a device configured for multichannel generation, the Data Marker generates on all channels. Signal — Signal specifies the signal to export. Sample Clock The Sample clock is exported. Sample Clock Timebase The Sample clock timebase is exported. Reference Clock The Reference clock is exported. Onboard Reference Clock The onboard 10 MHz synchronization clock. (PCI only) Start Trigger The Start trigger is exported. Script Trigger The Script trigger is exported. Marker Event The Marker event is exported. Data Marker Event The Data Marker event is exported. Ready For Start Event The Ready For Start event is exported. Started Event The Started event is exported. Done Event The Done event is exported. Synchronization Pulse The synchronization pulse is exported. This signal is a synchronization strobe that is used to guarantee absolute synchronization between two or more signal generators. (NI 5404 only) Sync Out The SYNC OUT signal is exported. This signal is normally exported on the SYNC_OUT front panel connector. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Do not export signal | The signal is not exported. |
| PFI 0 | The signal is exported on PFI 0. |
| PFI 1 | The signal is exported on PFI 1. |
| PFI 4 | The signal is exported on PFI 4. |
| PFI 5 | The signal is exported on PFI 5. |
| PXI_TRIG_0 | The signal is exported on PXI or RTSI line 0. |
| PXI_TRIG_1 | The signal is exported on PXI or RTSI line 1. |
| PXI_TRIG_2 | The signal is exported on PXI or RTSI line 2. |
| PXI_TRIG_3 | The signal is exported on PXI or RTSI line 3. |
| PXI_TRIG_4 | The signal is exported on PXI or RTSI line 4. |
| PXI_TRIG_5 | The signal is exported on PXI or RTSI line 5. |
| PXI_TRIG_6 | The signal is exported on PXI or RTSI line 6. |
| PXI_TRIG_7 | The signal is exported on PXI or RTSI line 7. |
| DDC_ClkOut | The signal is exported on the CLK OUT line on the DDC connector. |
| PXI_STAR | The signal is exported on the PXI star line. |
| None | Default (for non instance-based signals) |
| ScriptTrigger0 | Script trigger 0 |
| ScriptTrigger1 | Script trigger 1 |
| ScriptTrigger2 | Script trigger 2 |
| ScriptTrigger3 | Script trigger 3 |
| Marker0 | Marker 0 |
| Marker1 | Marker 1 |
| Marker2 | Marker 2 |
| Marker3 | Marker 3 |
| DataMarker0 | Data Marker 0 * |
| DataMarker1 | Data Marker 1 * |
| DataMarker2 | Data Marker 2 * |
| DataMarker3 | Data Marker 3 * |
| *These Data Marker values apply only to single-channel devices or to multichannel devices that are configured for single-channel operation. When using a device that is configured for multichannel operation, specify the channel number along with the signal identifier. For example, to export Data Marker 0 on channel 1 of a device configured for multichannel operation, use the value 1/ DataMarker0. If you do not specify a channel when using a device configured for multichannel generation, the Data Marker generates on all channels. |  |
| Sample Clock | The Sample clock is exported. |
| Sample Clock Timebase | The Sample clock timebase is exported. |
| Reference Clock | The Reference clock is exported. |
| Onboard Reference Clock | The onboard 10 MHz synchronization clock. (PCI only) |
| Start Trigger | The Start trigger is exported. |
| Script Trigger | The Script trigger is exported. |
| Marker Event | The Marker event is exported. |
| Data Marker Event | The Data Marker event is exported. |
| Ready For Start Event | The Ready For Start event is exported. |
| Started Event | The Started event is exported. |
| Done Event | The Done event is exported. |
| Synchronization Pulse | The synchronization pulse is exported. This signal is a synchronization strobe that is used to guarantee absolute synchronization between two or more signal generators. (NI 5404 only) |
| Sync Out | The SYNC OUT signal is exported. This signal is normally exported on the SYNC_OUT front panel connector. |

Parent topic:

Configure Clock

Parent topic:

Configure Trigger & Synchronization

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-get-cal-user-defined-info-vi.html language=enus -->
## TOPIC 00104: niFgen Get Cal User Defined Info VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-get-cal-user-defined-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-get-cal-user-defined-info-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves user-defined information from the onboard EEPROM. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides sta

### niFgen Get Cal User Defined Info VI

Retrieves user-defined information from the onboard EEPROM.

[IMAGE alt='icon' src='nifgen-get-cal-user-defined-info-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. UserDefinedInfo — UserDefinedInfo is a string containing the user information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-get-ext-cal-last-date-and-time-vi.html language=enus -->
## TOPIC 00105: niFgen Get Ext Cal Last Date And Time VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-get-ext-cal-last-date-and-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-get-ext-cal-last-date-and-time-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this VI returns 14 for the Hour parameter and 30 for the Minute parameter. icon Inputs/Outputs civrn.png Instrument Handle

### niFgen Get Ext Cal Last Date And Time VI

Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this VI returns **14** for the **Hour** parameter and **30** for the **Minute** parameter.

[IMAGE alt='icon' src='nifgen-get-ext-cal-last-date-and-time-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Year — Year is expressed as an integer. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Month — Month is expressed as an integer. For example, December is represented as 12. Day — Day is expressed as an integer. error out — error out contains error information. This output provides standard error out functionality. Minute — Minute is expressed as an integer. Hour — Hour is expressed as an integer. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-get-ext-cal-last-temp-vi.html language=enus -->
## TOPIC 00106: niFgen Get Ext Cal Last Temp VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-get-ext-cal-last-temp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-get-ext-cal-last-temp-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature at the last successful external calibration. The temperature is returned in degrees Celsius. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. cerrcodeclst.png error in (no error) error in describes error conditions

### niFgen Get Ext Cal Last Temp VI

Returns the temperature at the last successful external calibration. The temperature is returned in degrees Celsius.

[IMAGE alt='icon' src='nifgen-get-ext-cal-last-temp-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Temperature — Temperature is expressed in degrees Celsius. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-get-ext-cal-recommended-interval-vi.html language=enus -->
## TOPIC 00107: niFgen Get Ext Cal Recommended Interval VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-get-ext-cal-recommended-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-get-ext-cal-recommended-interval-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended interval between external calibrations in months. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This inpu

### niFgen Get Ext Cal Recommended Interval VI

Returns the recommended interval between external calibrations in months.

[IMAGE alt='icon' src='nifgen-get-ext-cal-recommended-interval-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Months — Months returns the recommended maximum interval between external calibrations in months. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-get-fir-filter-coefficients-vi.html language=enus -->
## TOPIC 00108: niFgen Get FIR Filter Coefficients VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-get-fir-filter-coefficients-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-get-fir-filter-coefficients-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the FIR filter coefficients used by the onboard signal processing block. These coefficients are determined by NI-FGEN and based on the FIR filter type and corresponding property (Alpha, Passband, BT) unless you are using the custom filter. If you are using a custom filter, the coefficients r

### niFgen Get FIR Filter Coefficients VI

Returns the FIR filter coefficients used by the onboard signal processing block. These coefficients are determined by NI-FGEN and based on the FIR filter type and corresponding property (Alpha, Passband, BT) unless you are using the custom filter. If you are using a custom filter, the coefficients returned are those set with the [niFgen Configure Custom FIR Filter Coefficients](/csh?topicname=nifgen-configure-custom-fir-filter-coefficients-vi.html) VI coerced to the quantized values used by the device.

Refer to the *FIR Filter* topic for your device in the *NI Signal Generators Help* for more information about FIR filter coefficients. This VI is supported only for the NI 5441.

[IMAGE alt='icon' src='nifgen-get-fir-filter-coefficients-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. FIR Filter Coefficients — FIR Filter Coefficients returns the FIR filter coefficients that the onboard signal processor is using as an array of data. For the NI 5441, the array contains 95 coefficients coerced to the quantized values used by the device. The coefficients range between -1.00 and +1.00. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Onboard Signal Processing

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-get-self-cal-last-date-and-time-vi.html language=enus -->
## TOPIC 00109: niFgen Get Self Cal Last Date And Time VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-get-self-cal-last-date-and-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-get-self-cal-last-date-and-time-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful self-calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this VI returns 14 for the hours parameter and 30 for the minutes parameter. icon Inputs/Outputs civrn.png Instrument Handle In

### niFgen Get Self Cal Last Date And Time VI

Returns the date and time of the last successful self-calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this VI returns 14 for the hours parameter and 30 for the minutes parameter.

[IMAGE alt='icon' src='nifgen-get-self-cal-last-date-and-time-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Year — Year is expressed as an integer. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Month — Month is expressed as an integer. For example, December is represented as 12. Day — Day is expressed as an integer. error out — error out contains error information. This output provides standard error out functionality. Minute — Minute is expressed as an integer. Hour — Hour is expressed as an integer. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-get-self-cal-last-temp-vi.html language=enus -->
## TOPIC 00110: niFgen Get Self Cal Last Temp VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-get-self-cal-last-temp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-get-self-cal-last-temp-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature at the last successful self-calibration. The temperature is returned in degrees Celsius. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. cerrcodeclst.png error in (no error) error in describes error conditions that

### niFgen Get Self Cal Last Temp VI

Returns the temperature at the last successful self-calibration. The temperature is returned in degrees Celsius.

[IMAGE alt='icon' src='nifgen-get-self-cal-last-temp-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Temperature — Temperature is expressed in degrees Celsius. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-get-self-cal-supported-vi.html language=enus -->
## TOPIC 00111: niFgen Get Self Cal Supported VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-get-self-cal-supported-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-get-self-cal-supported-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the device supports self-calibration. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels V

### niFgen Get Self Cal Supported VI

Returns whether the device supports self-calibration.

[IMAGE alt='icon' src='nifgen-get-self-cal-supported-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. SelfCalSupported — SelfCalSupported returns TRUE if self-calibration is supported, FALSE otherwise. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-get-session-reference-vi.html language=enus -->
## TOPIC 00112: niFgen Get Session Reference VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-get-session-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-get-session-reference-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts a session that can be passed to NI-TClk VIs. Session references are of generic type, which means that the corresponding wires are blue-green, unlike the wires for regular instrument driver sessions. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular in

### niFgen Get Session Reference VI

Extracts a session that can be passed to NI-TClk VIs. Session references are of generic type, which means that the corresponding wires are blue-green, unlike the wires for regular instrument driver sessions.

[IMAGE alt='icon' src='nifgen-get-session-reference-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Session Reference — Session Reference references the device session that can be passed to NI-TClk VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-get-stream-endpoint-handle-vi.html language=enus -->
## TOPIC 00113: niFgen Get Stream Endpoint Handle VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-get-stream-endpoint-handle-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-get-stream-endpoint-handle-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a reader endpoint handle that can be used with NI-P2P to configure a peer-to-peer stream with a signal generator endpoint. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI

### niFgen Get Stream Endpoint Handle VI

Returns a reader endpoint handle that can be used with NI-P2P to configure a peer-to-peer stream with a signal generator endpoint.

[IMAGE alt='icon' src='nifgen-get-stream-endpoint-handle-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Stream Endpoint — Stream Endpoint is the stream endpoint FIFO to configure. Refer to the peer-to-peer streaming topic for your device in the NI Signal Generators Help for more information. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Reader Handle — Reader Handle specifies the reader endpoint handle that is used with NI-P2P to create a stream with the signal generator as an endpoint. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Peer-to-Peer (P2P)

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-import-attribute-configuration-buffer-vi.html language=enus -->
## TOPIC 00114: niFgen Import Attribute Configuration Buffer VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-import-attribute-configuration-buffer-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-import-attribute-configuration-buffer-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports a configuration to the session from the specified buffer. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize Wit

### niFgen Import Attribute Configuration Buffer VI

Imports a configuration to the session from the specified buffer.

[IMAGE alt='icon' src='nifgen-import-attribute-configuration-buffer-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. buffer — buffer is a byte array that contains the configuration to import. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Requirements for Exporting and Importing Arbitrary Waveforms**

Arbitrary waveforms you export and import between sessions using this VI must meet the following criteria:

- All waveforms in the exporting session are created from files using the niFgen Create Waveform (poly) VI
- The full file path of the file containing the arbitrary waveform still exists upon import
- All waveforms are defined using handles rather than names
- All waveforms are completenone are streamed or incrementally written

You can set the device mode with the [niFgen Configure Output Mode](nifgen-configure-output-mode-vi.html) VI. For more information on arbitrary waveform mode, refer to [Arbitrary Waveform Output Mode](/csh?context=nifgen_siggenhelp_arb_mode) and [Configure Arbitrary Waveform Mode](/csh?context=nifgen_siggenhelp_programming_arb_waveform).

**Channel Mapping Behavior**

When exporting and importing configurations between NI‑FGEN sessions that were initialized with different channels using the **channel name** input to the [niFgen Initialize With Channels](nifgen-initialize-with-channels-vi.html) VI, the configuration of the exporting channel is mapped to the importing channel.

For example, if your entry for **channel name** is 0 for the exporting session and 1 for the importing session, the configuration exported from channel 0 is imported into channel 1.

Note

Parent topic:

niFgen Import Attribute Configuration(poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-import-attribute-configuration-file-vi.html language=enus -->
## TOPIC 00115: niFgen Import Attribute Configuration File VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-import-attribute-configuration-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-import-attribute-configuration-file-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports a configuration to the session from the specified file. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With

### niFgen Import Attribute Configuration File VI

Imports a configuration to the session from the specified file.

[IMAGE alt='icon' src='nifgen-import-attribute-configuration-file-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. file path — file path is the absolute path to the file that contains the configuration to import. If you specify an empty or relative path, this VI returns an error. Default file extension: .nifgenconfig error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Requirements for Exporting and Importing Arbitrary Waveforms**

Arbitrary waveforms you export and import between sessions using this VI must meet the following criteria:

- All waveforms in the exporting session are created from files using the niFgen Create Waveform (poly) VI
- The full file path of the file containing the arbitrary waveform still exists upon import
- All waveforms are defined using handles rather than names
- All waveforms are completenone are streamed or incrementally written

You can set the device mode with the [niFgen Configure Output Mode](nifgen-configure-output-mode-vi.html) VI. For more information on arbitrary waveform mode, refer to [Arbitrary Waveform Output Mode](/csh?context=nifgen_siggenhelp_arb_mode) and [Configure Arbitrary Waveform Mode](/csh?context=nifgen_siggenhelp_programming_arb_waveform).

**Channel Mapping Behavior**

When exporting and importing configurations between NI‑FGEN sessions that were initialized with different channels using the **channel name** input to the [niFgen Initialize With Channels](nifgen-initialize-with-channels-vi.html) VI, the configuration of the exporting channel is mapped to the importing channel.

For example, if your entry for **channel name** is 0 for the exporting session and 1 for the importing session, the configuration exported from channel 0 is imported into channel 1.

Note

Parent topic:

niFgen Import Attribute Configuration(poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-import-attribute-configuration-poly-vi.html language=enus -->
## TOPIC 00116: niFgen Import Attribute Configuration(poly) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-import-attribute-configuration-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-import-attribute-configuration-poly-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports a configuration to the session from either a file or a buffer. You can export and import supported configurations only between NI‑FGEN devices with identical bus types, model numbers, and channel counts, as well as the same number of initialized channels. You cannot call this VI while the se

### niFgen Import Attribute Configuration(poly) VI

Imports a configuration to the session from either a file or a buffer.

You can export and import supported configurations only between NI‑FGEN devices with identical bus types, model numbers, and channel counts, as well as the same number of initialized channels.

Note

Running/Generating

**Supported Configurations**

You can export and import the following between NI‑FGEN sessions:

- Attribute configurations
- Arbitrary waveforms

**Related topics:**

[Programming State Model](/csh?context=nifgen_siggenhelp_prog_nifgen_state_model)

[Setting Attributes Before Reading Attributes](/csh?context=nifgen_siggenhelp_setting_before_reading_attributes)

[Output Modes](/csh?context=nifgen_siggenhelp_output_arb_freq_script_seq)

[IMAGE alt='icon' src='nifgen-import-attribute-configuration-poly-vi.png']

#### Details

**Requirements for Exporting and Importing Arbitrary Waveforms**

Arbitrary waveforms you export and import between sessions using this VI must meet the following criteria:

- All waveforms in the exporting session are created from files using the niFgen Create Waveform (poly) VI
- The full file path of the file containing the arbitrary waveform still exists upon import
- All waveforms are defined using handles rather than names
- All waveforms are completenone are streamed or incrementally written

You can set the device mode with the [niFgen Configure Output Mode](nifgen-configure-output-mode-vi.html) VI. For more information on arbitrary waveform mode, refer to [Arbitrary Waveform Output Mode](/csh?context=nifgen_siggenhelp_arb_mode) and [Configure Arbitrary Waveform Mode](/csh?context=nifgen_siggenhelp_programming_arb_waveform).

**Channel Mapping Behavior**

When exporting and importing configurations between NI‑FGEN sessions that were initialized with different channels using the **channel name** input to the [niFgen Initialize With Channels](nifgen-initialize-with-channels-vi.html) VI, the configuration of the exporting channel is mapped to the importing channel.

For example, if your entry for **channel name** is 0 for the exporting session and 1 for the importing session, the configuration exported from channel 0 is imported into channel 1.

Note

- [niFgen Import Attribute Configuration File VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-import-attribute-configuration-file-vi.html) Imports a configuration to the session from the specified file.
- [niFgen Import Attribute Configuration Buffer VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-import-attribute-configuration-buffer-vi.html) Imports a configuration to the session from the specified buffer.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-init-ext-cal-vi.html language=enus -->
## TOPIC 00117: niFgen Init Ext Cal VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-init-ext-cal-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-init-ext-cal-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates and initializes a special NI-FGEN external calibration session. The ViSession returned is an NI-FGEN session that can be used to configure the device using normal attributes and functions. However, flags have been set that allow you to program an external calibration procedure using the spec

### niFgen Init Ext Cal VI

Creates and initializes a special NI-FGEN external calibration session. The ViSession returned is an NI-FGEN session that can be used to configure the device using normal attributes and functions. However, flags have been set that allow you to program an external calibration procedure using the special calibration properties and VIs. The NI 5404 and PXIe-5413/5423/5433 have different calibration VIs. Refer to the calibration procedure of the signal generator for more information.

[IMAGE alt='icon' src='nifgen-init-ext-cal-vi.png']

#### Inputs/Outputs

| Resource Name — Resource Name specifies the instrument name, for example "PXI1Slot3" where "PXI1Slot3" is an instrument name assigned by Measurement & Automation Explorer (MAX). Syntax: Example # Device Type Syntax Variable 1 NI-DAQmx device myDAQmxDevice (myDAQmxDevice = device name) 2 NI-DAQmx device DAQ::myDAQmxDevice (myDAQmxDevice = device name) 3 NI-DAQmx device DAQ::2 (2 = device name) 4 IVI logical name or IVI virtual name myLogicalName (myLogicalName = name) For NI-DAQmx devices, the syntax is just the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by right-clicking on the name in MAX and entering a new name. An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx device name, as shown in Example 2. This naming convention allows for the use of an NI-DAQmx device in an application that was originally designed for a Traditional NI-DAQ device. For example, if the application expects DAQ::1 (Traditional NI-DAQ syntax), you can rename the NI-DAQmx device to 1 in MAX and pass in DAQ::1 for the resource name, as shown in Example 3. If you use the DAQ::n syntax and an NI-DAQmx device name already exists with that same name, the NI-DAQmx device is matched first. You can also pass in the name of an IVI logical name or an IVI virtual name configured with the IVI Configuration utility, as shown in Example 4. A logical name identifies a particular virtual instrument. A virtual name identifies a specific device and specifies the initial settings for the session. Caution NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must ensure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. Password — Password specifies calibration password required to open an external calibration session to the device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |  |  |
| --- | --- | --- | --- |
| Example # | Device Type | Syntax | Variable |
| 1 | NI-DAQmx device | myDAQmxDevice | (myDAQmxDevice = device name) |
| 2 | NI-DAQmx device | DAQ::myDAQmxDevice | (myDAQmxDevice = device name) |
| 3 | NI-DAQmx device | DAQ::2 | (2 = device name) |
| 4 | IVI logical name or IVI virtual name | myLogicalName | (myLogicalName = name) |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-initialize-analog-output-calibration-vi.html language=enus -->
## TOPIC 00118: niFgen Initialize Analog Output Calibration VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-initialize-analog-output-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-initialize-analog-output-calibration-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets up the device to start the analog output calibration. The session handle should be the handle returned by the niFgen Init Ext Cal VI. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal

### niFgen Initialize Analog Output Calibration VI

Sets up the device to start the analog output calibration.

The session handle should be the handle returned by the [niFgen Init Ext Cal](nifgen-init-ext-cal-vi.html) VI.

[IMAGE alt='icon' src='nifgen-initialize-analog-output-calibration-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Analog Output Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-initialize-cal-adc-calibration-vi.html language=enus -->
## TOPIC 00119: niFgen Initialize Cal ADC Calibration VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-initialize-cal-adc-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-initialize-cal-adc-calibration-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an external calibration session for ADC calibration. For the NI 5421/5422/5441, ADC calibration involves characterizing the gain and offset of the onboard ADC. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies your instrument session. Instrument Handle is obtai

### niFgen Initialize Cal ADC Calibration VI

Initializes an external calibration session for ADC calibration. For the NI 5421/5422/5441, ADC calibration involves characterizing the gain and offset of the onboard ADC.

[IMAGE alt='icon' src='nifgen-initialize-cal-adc-calibration-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

ADC Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-initialize-flatness-calibration-vi.html language=enus -->
## TOPIC 00120: niFgen Initialize Flatness Calibration VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-initialize-flatness-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-initialize-flatness-calibration-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an external calibration session to calibrate flatness. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. cerrcodeclst.png error in (no error) error in describes error condit

### niFgen Initialize Flatness Calibration VI

Initializes an external calibration session to calibrate flatness.

[IMAGE alt='icon' src='nifgen-initialize-flatness-calibration-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Flatness Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-initialize-oscillator-frequency-calibration-vi.html language=enus -->
## TOPIC 00121: niFgen Initialize Oscillator Frequency Calibration VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-initialize-oscillator-frequency-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-initialize-oscillator-frequency-calibration-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets up the device to start the oscillator calibration. The session handle should be the handle returned by the niFgen Init Ext Cal VI. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI.

### niFgen Initialize Oscillator Frequency Calibration VI

Sets up the device to start the oscillator calibration.

The session handle should be the handle returned by the [niFgen Init Ext Cal](nifgen-init-ext-cal-vi.html) VI.

[IMAGE alt='icon' src='nifgen-initialize-oscillator-frequency-calibration-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Oscillator Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-initialize-vi.html language=enus -->
## TOPIC 00122: niFgen Initialize VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-initialize-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-initialize-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the following initialization actions: - Creates a new IVI instrument driver session. - Opens a session to the specified device using the interface and address that you specify for Resource Name. - If ID Query is set to TRUE, this VI queries the device ID and checks that the ID is valid for

### niFgen Initialize VI

Performs the following initialization actions:

- Creates a new IVI instrument driver session.

- Opens a session to the specified device using the interface and address that you specify for **Resource Name**.

- If **ID Query** is set to TRUE, this VI queries the device ID and checks that the ID is valid for NI-FGEN.

- If **Reset Device** is set to TRUE, this VI resets the device to a known state.

- Sends initialization commands to set the device to the state necessary for the operation of NI-FGEN.

- Returns a session handle that you can use to identify the device in all subsequent NI-FGEN VI calls.

[IMAGE alt='icon' src='nifgen-initialize-vi.png']

#### Inputs/Outputs

| Resource Name — Resource Name specifies the instrument name, for example "PXI1Slot3" where "PXI1Slot3" is an instrument name assigned by Measurement & Automation Explorer (MAX). Syntax: Example # Device Type Syntax Variable 1 NI-DAQmx device myDAQmxDevice (myDAQmxDevice = device name) 2 NI-DAQmx device DAQ::myDAQmxDevice (myDAQmxDevice = device name) 3 NI-DAQmx device DAQ::2 (2 = device name) 4 IVI logical name or IVI virtual name myLogicalName (myLogicalName = name) For NI-DAQmx devices, the syntax is just the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by right-clicking on the name in MAX and entering a new name. An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx device name, as shown in Example 2. This naming convention allows for the use of an NI-DAQmx device in an application that was originally designed for a Traditional NI-DAQ device. For example, if the application expects DAQ::1 (Traditional NI-DAQ syntax), you can rename the NI-DAQmx device to 1 in MAX and pass in DAQ::1 for the resource name, as shown in Example 3. If you use the DAQ::n syntax and an NI-DAQmx device name already exists with that same name, the NI-DAQmx device is matched first. You can also pass in the name of an IVI logical name or an IVI virtual name configured with the IVI Configuration utility, as shown in Example 4. A logical name identifies a particular virtual instrument. A virtual name identifies a specific device and specifies the initial settings for the session. Caution NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must ensure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. Id Query (default: True) — Id Query specifies whether to verify that NI-FGEN supports the device you initialize. Circumstances can arise where sending an ID query to the device is undesirable. When you set this parameter to FALSE, the VI initializes the device without performing an ID query. Default value: True Reset Device (default: True) — Reset Device specifies whether you want to reset the device during the initialization procedure. Set Reset Device to TRUE to reset the device. Reset Device performs the same function as the niFgen Reset VI. Default value: True error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |  |  |
| --- | --- | --- | --- |
| Example # | Device Type | Syntax | Variable |
| 1 | NI-DAQmx device | myDAQmxDevice | (myDAQmxDevice = device name) |
| 2 | NI-DAQmx device | DAQ::myDAQmxDevice | (myDAQmxDevice = device name) |
| 3 | NI-DAQmx device | DAQ::2 | (2 = device name) |
| 4 | IVI logical name or IVI virtual name | myLogicalName | (myLogicalName = name) |

Parent topic:

NI-FGEN

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-initialize-with-channels-for-grpc-session-vi.html language=enus -->
## TOPIC 00123: niFgen Initialize With Channels for gRPC Session VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-initialize-with-channels-for-grpc-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-initialize-with-channels-for-grpc-session-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new NI-FGEN session on the specified NI gRPC Device Server using the specified instrument(s) and channel(s). This VI initializes a NI-FGEN session on the specified NI gRPC Device Server and attaches to it from LabVIEW. If the Session Name is specified in the gRPC Options and the same s

### niFgen Initialize With Channels for gRPC Session VI

Initializes a new NI-FGEN session on the specified NI gRPC Device Server using the specified instrument(s) and channel(s).

This VI initializes a NI-FGEN session on the specified NI gRPC Device Server and attaches to it from LabVIEW. If the Session Name is specified in the gRPC Options and the same session name previously exists on the server, then NI-FGEN will return an error. If the Session Name in the gRPC Options is empty, the resource name will be used as a session name.

The resulting session in LabVIEW forwards driver calls to the corresponding session on the server.

[IMAGE alt='icon' src='nifgen-initialize-with-channels-for-grpc-session-vi.png']

#### Inputs/Outputs

| gRPC Options — gRPC Options specifies the information used to connect to the server. Session Name — Session Name specifies the name of the MeasurementLink gRPC session. Address (localhost) — Address (localhost) specifies the address of the NI gRPC Device Server. Port (31763) — Port (31763) specifies the port that the NI gRPC Device Server monitors for connections. Option String — Option String specifies the initial values of certain session properties. Default Values: "Simulate=0,RangeCheck=1,Cache=1, QueryInstrStatus=1" The syntax for Option String is attributeName=value where: attributeName = the name of the attribute value = the value to which the attribute is set. To set multiple properties, separate them with a comma. If you do not wire this input or pass in an empty string, the session uses the default values for these properties. You can override the default values by assigning a value explicitly in a string that you pass for this input. You do not have to specify all of the properties and may leave any of them out. If you do not specify one of the properties, its default value is used. Property Name Property Defined Constant Default Value RangeCheck niFgen >> Inherent IVI Attributes >> User Options >> Range Check 1 (True) Cache niFgen >> Inherent IVI Attributes >> User Options >> Cache 1 (True) Simulate niFgen >> Inherent IVI Attributes >> User Options >> Simulate 0 (False) QueryInstrStatus niFgen >> Inherent IVI Attributes >> User Options >> Query Instrument Status 1 (True) If simulation is enabled (Simulate=1), you may specify the device that you want to simulate. To specify a device, enter the following syntax in Option String. DriverSetup=Model:< driver model number >;BoardType:< module type >;MemorySize:< size of onboard memory in bytes > Option String Examples: Device Option String Syntax NI PXI-5404 Simulate=1,DriverSetup=Model:5404;BoardType:PXI NI PCI-5421 Simulate=1,DriverSetup=Model:5421;BoardType:PCI;MemorySize:268435456 NI PXIe-5450 Simulate=1,DriverSetup=Model:5450;Channels:0-1;BoardType:PXIe;MemorySize:268435456 Note When you configure multichannel devices, the Option String Channels parameter specifies which channels to initialize. Valid values include channel ranges (for example, "Channels:0-1") and individual channels (for example, "Channels:1"). Resource Name — Resource Name specifies the instrument name, for example "PXI1Slot3" where "PXI1Slot3" is an instrument name assigned by Measurement & Automation Explorer (MAX). Syntax: Example # Device Type Syntax Variable 1 NI-DAQmx device myDAQmxDevice (myDAQmxDevice = device name) 2 NI-DAQmx device DAQ::myDAQmxDevice (myDAQmxDevice = device name) 3 NI-DAQmx device DAQ::2 (2 = device name) 4 IVI logical name or IVI virtual name myLogicalName (myLogicalName = name) For NI-DAQmx devices, the syntax is just the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by right-clicking on the name in MAX and entering a new name. An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx device name, as shown in Example 2. This naming convention allows for the use of an NI-DAQmx device in an application that was originally designed for a Traditional NI-DAQ device. For example, if the application expects DAQ::1 (Traditional NI-DAQ syntax), you can rename the NI-DAQmx device to 1 in MAX and pass in DAQ::1 for the resource name, as shown in Example 3. If you use the DAQ::n syntax and an NI-DAQmx device name already exists with that same name, the NI-DAQmx device is matched first. You can also pass in the name of an IVI logical name or an IVI virtual name configured with the IVI Configuration utility, as shown in Example 4. A logical name identifies a particular virtual instrument. A virtual name identifies a specific device and specifies the initial settings for the session. Caution NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must ensure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. Channel Name — Channel Name specifies the channel that this VI uses. Reset Device (default: False) — Reset Device specifies whether you want to reset the device during the initialization procedure. Set Reset Device to TRUE to reset the device. Reset Device performs the same function as the niFgen Reset VI. Resetting a device is not supported when configured for multiple channel-based sessions. Default value: False error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |  |  |
| --- | --- | --- | --- |
| Session Name — Session Name specifies the name of the MeasurementLink gRPC session. Address (localhost) — Address (localhost) specifies the address of the NI gRPC Device Server. Port (31763) — Port (31763) specifies the port that the NI gRPC Device Server monitors for connections. |  |  |  |
| Property Name | Property Defined Constant | Default Value |  |
| RangeCheck | niFgen >> Inherent IVI Attributes >> User Options >> Range Check | 1 (True) |  |
| Cache | niFgen >> Inherent IVI Attributes >> User Options >> Cache | 1 (True) |  |
| Simulate | niFgen >> Inherent IVI Attributes >> User Options >> Simulate | 0 (False) |  |
| QueryInstrStatus | niFgen >> Inherent IVI Attributes >> User Options >> Query Instrument Status | 1 (True) |  |
| Device | Option String Syntax |  |  |
| NI PXI-5404 | Simulate=1,DriverSetup=Model:5404;BoardType:PXI |  |  |
| NI PCI-5421 | Simulate=1,DriverSetup=Model:5421;BoardType:PCI;MemorySize:268435456 |  |  |
| NI PXIe-5450 | Simulate=1,DriverSetup=Model:5450;Channels:0-1;BoardType:PXIe;MemorySize:268435456 |  |  |
| Example # | Device Type | Syntax | Variable |
| 1 | NI-DAQmx device | myDAQmxDevice | (myDAQmxDevice = device name) |
| 2 | NI-DAQmx device | DAQ::myDAQmxDevice | (myDAQmxDevice = device name) |
| 3 | NI-DAQmx device | DAQ::2 | (2 = device name) |
| 4 | IVI logical name or IVI virtual name | myLogicalName | (myLogicalName = name) |

Parent topic:

MeasurementLink

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-initialize-with-channels-vi.html language=enus -->
## TOPIC 00124: niFgen Initialize With Channels VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-initialize-with-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-initialize-with-channels-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates and returns a new NI-FGEN session to the specified channel of a waveform generator that is used in all subsequent NI-FGEN VI calls. icon Inputs/Outputs cstr.png Option String Option String specifies the initial values of certain session properties. Default Values: "Simulate=0,RangeCheck=1,Ca

### niFgen Initialize With Channels VI

Creates and returns a new NI-FGEN session to the specified channel of a waveform generator that is used in all subsequent NI-FGEN VI calls.

[IMAGE alt='icon' src='nifgen-initialize-with-channels-vi.png']

#### Inputs/Outputs

| Option String — Option String specifies the initial values of certain session properties. Default Values: "Simulate=0,RangeCheck=1,Cache=1, QueryInstrStatus=1" The syntax for Option String is attributeName=value where: attributeName = the name of the attribute value = the value to which the attribute is set. To set multiple properties, separate them with a comma. If you do not wire this input or pass in an empty string, the session uses the default values for these properties. You can override the default values by assigning a value explicitly in a string that you pass for this input. You do not have to specify all of the properties and may leave any of them out. If you do not specify one of the properties, its default value is used. Property Name Property Defined Constant Default Value RangeCheck niFgen >> Inherent IVI Attributes >> User Options >> Range Check 1 (True) Cache niFgen >> Inherent IVI Attributes >> User Options >> Cache 1 (True) Simulate niFgen >> Inherent IVI Attributes >> User Options >> Simulate 0 (False) QueryInstrStatus niFgen >> Inherent IVI Attributes >> User Options >> Query Instrument Status 1 (True) If simulation is enabled (Simulate=1), you may specify the device that you want to simulate. To specify a device, enter the following syntax in Option String. DriverSetup=Model:< driver model number >;BoardType:< module type >;MemorySize:< size of onboard memory in bytes > Option String Examples: Device Option String Syntax NI PXI-5404 Simulate=1,DriverSetup=Model:5404;BoardType:PXI NI PCI-5421 Simulate=1,DriverSetup=Model:5421;BoardType:PCI;MemorySize:268435456 NI PXIe-5450 Simulate=1,DriverSetup=Model:5450;Channels:0-1;BoardType:PXIe;MemorySize:268435456 Note When you configure multichannel devices, the Option String Channels parameter specifies which channels to initialize. Valid values include channel ranges (for example, "Channels:0-1") and individual channels (for example, "Channels:1"). Resource Name — Resource Name specifies the instrument name, for example "PXI1Slot3" where "PXI1Slot3" is an instrument name assigned by Measurement & Automation Explorer (MAX). Syntax: Example # Device Type Syntax Variable 1 NI-DAQmx device myDAQmxDevice (myDAQmxDevice = device name) 2 NI-DAQmx device DAQ::myDAQmxDevice (myDAQmxDevice = device name) 3 NI-DAQmx device DAQ::2 (2 = device name) 4 IVI logical name or IVI virtual name myLogicalName (myLogicalName = name) For NI-DAQmx devices, the syntax is just the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by right-clicking on the name in MAX and entering a new name. An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx device name, as shown in Example 2. This naming convention allows for the use of an NI-DAQmx device in an application that was originally designed for a Traditional NI-DAQ device. For example, if the application expects DAQ::1 (Traditional NI-DAQ syntax), you can rename the NI-DAQmx device to 1 in MAX and pass in DAQ::1 for the resource name, as shown in Example 3. If you use the DAQ::n syntax and an NI-DAQmx device name already exists with that same name, the NI-DAQmx device is matched first. You can also pass in the name of an IVI logical name or an IVI virtual name configured with the IVI Configuration utility, as shown in Example 4. A logical name identifies a particular virtual instrument. A virtual name identifies a specific device and specifies the initial settings for the session. Caution NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must ensure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. Channel Name — Channel Name specifies the channel that this VI uses. Reset Device (default: False) — Reset Device specifies whether you want to reset the device during the initialization procedure. Set Reset Device to TRUE to reset the device. Reset Device performs the same function as the niFgen Reset VI. Resetting a device is not supported when configured for multiple channel-based sessions. Default value: False error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |  |  |
| --- | --- | --- | --- |
| Property Name | Property Defined Constant | Default Value |  |
| RangeCheck | niFgen >> Inherent IVI Attributes >> User Options >> Range Check | 1 (True) |  |
| Cache | niFgen >> Inherent IVI Attributes >> User Options >> Cache | 1 (True) |  |
| Simulate | niFgen >> Inherent IVI Attributes >> User Options >> Simulate | 0 (False) |  |
| QueryInstrStatus | niFgen >> Inherent IVI Attributes >> User Options >> Query Instrument Status | 1 (True) |  |
| Device | Option String Syntax |  |  |
| NI PXI-5404 | Simulate=1,DriverSetup=Model:5404;BoardType:PXI |  |  |
| NI PCI-5421 | Simulate=1,DriverSetup=Model:5421;BoardType:PCI;MemorySize:268435456 |  |  |
| NI PXIe-5450 | Simulate=1,DriverSetup=Model:5450;Channels:0-1;BoardType:PXIe;MemorySize:268435456 |  |  |
| Example # | Device Type | Syntax | Variable |
| 1 | NI-DAQmx device | myDAQmxDevice | (myDAQmxDevice = device name) |
| 2 | NI-DAQmx device | DAQ::myDAQmxDevice | (myDAQmxDevice = device name) |
| 3 | NI-DAQmx device | DAQ::2 | (2 = device name) |
| 4 | IVI logical name or IVI virtual name | myLogicalName | (myLogicalName = name) |

Parent topic:

NI-FGEN

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-initialize-with-options-vi.html language=enus -->
## TOPIC 00125: niFgen Initialize With Options VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-initialize-with-options-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-initialize-with-options-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the following initialization actions: - Creates a new IVI instrument session and optionally sets the initial state of the following session properties: Range Check, Cache, Simulate, and Record Coercions. - Opens a session to the specified device using the interface and address that you spec

### niFgen Initialize With Options VI

Performs the following initialization actions:

- Creates a new IVI instrument session and optionally sets the initial state of the following session properties: [Range Check](/csh?context=nifgen_nifgenpropref_pnifgen_rangecheck), [Cache](/csh?context=nifgen_nifgenpropref_pnifgen_cache), [Simulate](/csh?context=nifgen_nifgenpropref_pnifgen_simulate), and [Record Coercions](/csh?context=nifgen_nifgenpropref_pnifgen_recordvaluecoercions).

- Opens a session to the specified device using the interface and address that you specify for **Resource Name**.

- If **Reset Device** is set to TRUE, this VI resets the device to a known state.

- Sends initialization commands to set the instrument to the state necessary for NI-FGEN operation.

- Returns a session handle that you can use to identify the device in all subsequent NI-FGEN VI calls.

[IMAGE alt='icon' src='nifgen-initialize-with-options-vi.png']

#### Inputs/Outputs

| Option String — Option String specifies the initial values of certain session properties. Default Values: "Simulate=0,RangeCheck=1,Cache=1, QueryInstrStatus=1" The syntax for Option String is attributeName=value where: attributeName = the name of the attribute value = the value to which the attribute is set. To set multiple properties, separate them with a comma. If you do not wire this input or pass in an empty string, the session uses the default values for these properties. You can override the default values by assigning a value explicitly in a string that you pass for this input. You do not have to specify all of the properties and may leave any of them out. If you do not specify one of the properties, its default value is used. Property Name Property Defined Constant Default Value RangeCheck niFgen >> Inherent IVI Attributes >> User Options >> Range Check 1 (True) Cache niFgen >> Inherent IVI Attributes >> User Options >> Cache 1 (True) Simulate niFgen >> Inherent IVI Attributes >> User Options >> Simulate 0 (False) QueryInstrStatus niFgen >> Inherent IVI Attributes >> User Options >> Query Instrument Status 1 (True) If simulation is enabled (Simulate=1), you may specify the device that you want to simulate. To specify a device, enter the following syntax in Option String. DriverSetup=Model:< driver model number >;BoardType:< module type >;MemorySize:< size of onboard memory in bytes > Option String Examples: Device Option String Syntax NI PXI-5404 Simulate=1,DriverSetup=Model:5404;BoardType:PXI NI PCI-5421 Simulate=1,DriverSetup=Model:5421;BoardType:PCI;MemorySize:268435456 NI PXIe-5450 Simulate=1,DriverSetup=Model:5450;Channels:0-1;BoardType:PXIe;MemorySize:268435456 Note When you configure multichannel devices, the Option String Channels parameter specifies which channels to initialize. Valid values include channel ranges (for example, "Channels:0-1") and individual channels (for example, "Channels:1"). Resource Name — Resource Name specifies the instrument name, for example "PXI1Slot3" where "PXI1Slot3" is an instrument name assigned by Measurement & Automation Explorer (MAX). Syntax: Example # Device Type Syntax Variable 1 NI-DAQmx device myDAQmxDevice (myDAQmxDevice = device name) 2 NI-DAQmx device DAQ::myDAQmxDevice (myDAQmxDevice = device name) 3 NI-DAQmx device DAQ::2 (2 = device name) 4 IVI logical name or IVI virtual name myLogicalName (myLogicalName = name) For NI-DAQmx devices, the syntax is just the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by right-clicking on the name in MAX and entering a new name. An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx device name, as shown in Example 2. This naming convention allows for the use of an NI-DAQmx device in an application that was originally designed for a Traditional NI-DAQ device. For example, if the application expects DAQ::1 (Traditional NI-DAQ syntax), you can rename the NI-DAQmx device to 1 in MAX and pass in DAQ::1 for the resource name, as shown in Example 3. If you use the DAQ::n syntax and an NI-DAQmx device name already exists with that same name, the NI-DAQmx device is matched first. You can also pass in the name of an IVI logical name or an IVI virtual name configured with the IVI Configuration utility, as shown in Example 4. A logical name identifies a particular virtual instrument. A virtual name identifies a specific device and specifies the initial settings for the session. Caution NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must ensure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. Id Query (default: True) — Id Query specifies whether to verify that NI-FGEN supports the device you initialize. Circumstances can arise where sending an ID query to the device is undesirable. When you set this parameter to FALSE, the VI initializes the device without performing an ID query. Default value: True Reset Device (default: True) — Reset Device specifies whether you want to reset the device during the initialization procedure. Set Reset Device to TRUE to reset the device. Reset Device performs the same function as the niFgen Reset VI. Default value: True error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |  |  |
| --- | --- | --- | --- |
| Property Name | Property Defined Constant | Default Value |  |
| RangeCheck | niFgen >> Inherent IVI Attributes >> User Options >> Range Check | 1 (True) |  |
| Cache | niFgen >> Inherent IVI Attributes >> User Options >> Cache | 1 (True) |  |
| Simulate | niFgen >> Inherent IVI Attributes >> User Options >> Simulate | 0 (False) |  |
| QueryInstrStatus | niFgen >> Inherent IVI Attributes >> User Options >> Query Instrument Status | 1 (True) |  |
| Device | Option String Syntax |  |  |
| NI PXI-5404 | Simulate=1,DriverSetup=Model:5404;BoardType:PXI |  |  |
| NI PCI-5421 | Simulate=1,DriverSetup=Model:5421;BoardType:PCI;MemorySize:268435456 |  |  |
| NI PXIe-5450 | Simulate=1,DriverSetup=Model:5450;Channels:0-1;BoardType:PXIe;MemorySize:268435456 |  |  |
| Example # | Device Type | Syntax | Variable |
| 1 | NI-DAQmx device | myDAQmxDevice | (myDAQmxDevice = device name) |
| 2 | NI-DAQmx device | DAQ::myDAQmxDevice | (myDAQmxDevice = device name) |
| 3 | NI-DAQmx device | DAQ::2 | (2 = device name) |
| 4 | IVI logical name or IVI virtual name | myLogicalName | (myLogicalName = name) |

Parent topic:

NI-FGEN

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-initiate-generation-vi.html language=enus -->
## TOPIC 00126: niFgen Initiate Generation VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-initiate-generation-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-initiate-generation-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates signal generation. If you want to abort signal output, call the niFgen Abort Generation VI. Call this VI to cause the signal generator to produce a signal again. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle

### niFgen Initiate Generation VI

Initiates signal generation. If you want to abort signal output, call the [niFgen Abort Generation](/csh?topicname=nifgen-abort-generation-vi.html) VI. Call this VI to cause the signal generator to produce a signal again.

[IMAGE alt='icon' src='nifgen-initiate-generation-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-is-done-vi.html language=enus -->
## TOPIC 00127: niFgen Is Done VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-is-done-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-is-done-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current generation has completed. This VI sets the Done parameter to be TRUE if the session is in the Idle or Committed states. NI-FGEN reports Done as TRUE only after the current generation is complete in Single trigger mode. icon Inputs/Outputs civrn.png Instrument Handle In

### niFgen Is Done VI

Determines whether the current generation has completed. This VI sets the **Done** parameter to be TRUE if the session is in the Idle or Committed states.

Note

Done

[IMAGE alt='icon' src='nifgen-is-done-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Done — Done returns TRUE if the generation has completed. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-output-enable-vi.html language=enus -->
## TOPIC 00128: niFgen Output Enable VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-output-enable-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-output-enable-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the signal generator to generate a signal at the channel output connector. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the n

### niFgen Output Enable VI

Configures the signal generator to generate a signal at the channel output connector.

[IMAGE alt='icon' src='nifgen-output-enable-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Output Enable (default: True) — Output Enable specifies the state of the output enable relay. Set Output Enable to TRUE to enable the relay. Default value: True error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Output

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-property-node-vi.html language=enus -->
## TOPIC 00129: niFgen Property Node VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-property-node-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets or gets properties of instruments or channels. For multi-channel sessions in which you want to configure subsets of channels differently, you must wire an Active Channel of an NI-FGEN property node. The Active Channel is listed first in the property node. Channel Based Properties Some NI-FGEN p

### niFgen Property Node VI

Sets or gets properties of instruments or channels. For multi-channel sessions in which you want to configure subsets of channels differently, you must wire an Active Channel of an NI-FGEN property node. The Active Channel is listed first in the property node.

[IMAGE alt='image' src='loc_nifgenpropertynode_base.gif']

**Channel Based Properties**

Some NI-FGEN properties are channel based or apply to a specific channel. When a property is channel based, you must specify an active channel before setting or getting properties. In the following example, ch0 is configured to operate in Single Trigger mode and ch1 is configured to operate in Continuous Trigger mode. Both properties are channel based.

[IMAGE alt='image' src='loc_nifgenpropertynode_channel.gif']

**Non-Channel Based Properties**

To set or get NI-FGEN properties that are not channel based, you must not specify an active channel or must specify an active channel of "". The following example shows a property node used to get the value of the [Driver Vendor](/csh?context=nifgen_nifgenpropref_pnifgen_drivervendor) property.

[IMAGE alt='image' src='loc_nifgenpropertynode_nonchannel.gif']

**Related Topics:**

- niFgen Properties

[IMAGE alt='icon' src='nifgen-property-node-vi.png']

#### Inputs/Outputs

| reference — reference is the refnum associated with the object for which you want to set or get properties. If the Property Node class is Application or VI, you do not have to wire a refnum to this input. For the Application class, the default is the current application instance. For the VI class, the default is the VI containing the Property Node. You also can wire a LabVIEW class to the reference input to access the private data of the LabVIEW class. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error reference out — reference out returns reference unchanged. error out — error out contains error information. This output provides standard error out functionality. Property — property are examples of properties you want to set (write) or get (read). |
| --- |

Parent topic:

NI-FGEN

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-query-arb-sequence-capabilities-vi.html language=enus -->
## TOPIC 00130: niFgen Query Arb Sequence Capabilities VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-query-arb-sequence-capabilities-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-query-arb-sequence-capabilities-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the attributes of the signal generator that are related to creating arbitrary sequences. These attributes are the Maximum Number of Sequences, Minimum Sequence Length, Maximum Sequence Length, and Maximum Loop Count. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifie

### niFgen Query Arb Sequence Capabilities VI

Returns the attributes of the signal generator that are related to creating arbitrary sequences. These attributes are the **Maximum Number of Sequences**, **Minimum Sequence Length**, **Maximum Sequence Length**, and **Maximum Loop Count**.

[IMAGE alt='icon' src='nifgen-query-arb-sequence-capabilities-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Maximum Sequence Length — Maximum Sequence Length returns the maximum number of arbitrary waveforms the signal generator allows in a sequence. On some signal generators this may vary with remaining onboard memory. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Minimum Sequence Length — Minimum Sequence Length returns the minimum number of arbitrary waveforms the signal generator allows in a sequence. Maximum Number of Sequences — Maximum Number of Sequences returns the maximum number of arbitrary waveform sequences that the signal generator allows. On some signal generators this may vary with remaining onboard memory. error out — error out contains error information. This output provides standard error out functionality. Maximum Loop Count — Maximum Loop Count returns the maximum number of times the signal generator can repeat an arbitrary waveform in a sequence. |
| --- |

Parent topic:

Arbitrary Sequence

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-query-arb-waveform-capabilities-vi.html language=enus -->
## TOPIC 00131: niFgen Query Arb Waveform Capabilities VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-query-arb-waveform-capabilities-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-query-arb-waveform-capabilities-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the attributes of the signal generator that are related to creating arbitrary waveforms. These properties are the maximum number of waveforms, waveform quantum, minimum waveform size, and maximum waveform size. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a pa

### niFgen Query Arb Waveform Capabilities VI

Returns the attributes of the signal generator that are related to creating arbitrary waveforms. These properties are the maximum number of waveforms, waveform quantum, minimum waveform size, and maximum waveform size.

[IMAGE alt='icon' src='nifgen-query-arb-waveform-capabilities-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Minimum Waveform Size — Minimum Waveform Size returns the minimum number of points that the signal generator allows in a waveform. For some signal generators, you may need to supply a larger waveform than the value specified by this parameter. Refer to the "Features Supported" topic for your device in the NI Signal Generators Help for a table of minimum waveform sizes. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Quantum — Waveform Quantum returns the size (number of points) of each waveform must be a multiple of a constant quantum value. This parameter obtains the quantum value that the signal generator uses. For example, if this output returns a value of 8, all waveform sizes must be a multiple of 8. Maximum Number of Waveforms — Maximum Number of Waveforms returns the maximum number of arbitrary waveforms that the signal generator allows. On some signal generators this may vary with remaining onboard memory. error out — error out contains error information. This output provides standard error out functionality. Maximum Waveform Size — Maximum Waveform Size returns the maximum number of points that the signal generator allows in a waveform. On some signal generators this may vary with remaining onboard memory. |
| --- |

Parent topic:

Arbitrary Waveform

Parent topic:

Arbitrary Sequence

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-query-freq-list-capabilities-vi.html language=enus -->
## TOPIC 00132: niFgen Query Freq List Capabilities VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-query-freq-list-capabilities-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-query-freq-list-capabilities-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the properties of the signal generator that are related to creating frequency lists. These properties are the Maximum Number of Freq Lists, Minimum Frequency List Length, Maximum Frequency List Length, Minimum Frequency List Duration, Maximum Frequency List Duration, and Frequency List Durat

### niFgen Query Freq List Capabilities VI

Returns the properties of the signal generator that are related to creating frequency lists. These properties are the **Maximum Number of Freq Lists**, **Minimum Frequency List Length**, **Maximum Frequency List Length**, **Minimum Frequency List Duration**, **Maximum Frequency List Duration**, and **Frequency List Duration Quantum**.

[IMAGE alt='icon' src='nifgen-query-freq-list-capabilities-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Minimum Frequency List Duration — Minimum Frequency List Duration returns the minimum duration that the signal generator allows in a step of a frequency list. Maximum Frequency List Duration — Maximum Frequency List Duration returns the maximum duration that the signal generator allows in a step of a frequency list. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Maximum Number of Freq Lists — Maximum Number of Freq Lists returns the maximum number of frequency lists that the signal generator allows. Frequency List Duration Quantum — Frequency List Duration Quantum returns the quantum that all durations must be a multiple of. This parameter returns the quantum in a frequency list. error out — error out contains error information. This output provides standard error out functionality. Maximum Frequency List Length — Maximum Frequency List Length returns the maximum number of steps that the signal generator allows in a frequency list. Minimum Frequency List Length — Minimum Frequency List Length returns the minimum number of steps that the signal generator allows in a frequency list. |
| --- |

Parent topic:

Frequency List

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-read-cal-adc-vi.html language=enus -->
## TOPIC 00133: niFgen Read CAL ADC VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-read-cal-adc-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-read-cal-adc-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Takes one or more voltage measurements from the onboard calibration ADC and returns their average value. The signal that the ADC actually measures can be specified using the Cal ADC Input property. The ADC has some inherent gain and offset. These values can be determined during an external calibrati

### niFgen Read CAL ADC VI

Takes one or more voltage measurements from the onboard calibration ADC and returns their average value. The signal that the ADC actually measures can be specified using the [Cal ADC Input](/csh?context=nifgen_nifgenpropref_pnifgen_caladcinput) property. The ADC has some inherent gain and offset. These values can be determined during an external calibration session and stored in the calibration EEPROM.

If the **Return Calibrated Value?** is TRUE, NI-FGEN adjusts the value that is returned to account for the gain and offset of the ADC. Otherwise, the raw voltage value reported by the ADC is returned.

[IMAGE alt='icon' src='nifgen-read-cal-adc-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Number of Reads to Average — Number of Reads to Average specifies the number of measurements to be taken and averaged to determine the return value. Return Calibrated Value? — Return Calibrated Value? specifies whether the voltage returned from the ADC should be adjusted to account for the gain and offset of the ADC. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Calibration ADC Value — Calibration ADC Value returns the average of the voltage measurements taken from the onboard calibration ADC. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

ADC Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-read-current-temperature-vi.html language=enus -->
## TOPIC 00134: niFgen Read Current Temperature VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-read-current-temperature-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-read-current-temperature-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the current onboard temperature of the device. The temperature is returned in degrees Celsius. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. cerrcodeclst.png error in (no error) error in describes error conditions that occur befor

### niFgen Read Current Temperature VI

Reads the current onboard temperature of the device. The temperature is returned in degrees Celsius.

[IMAGE alt='icon' src='nifgen-read-current-temperature-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Temperature — Temperature is expressed in degrees Celsius. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-reset-device-vi.html language=enus -->
## TOPIC 00135: niFgen Reset Device VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-reset-device-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-reset-device-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a hard reset on the device. Generation is stopped, all routes are released, external bidirectional terminals are tri-stated, FPGAs are reset, hardware is configured to its default state, and all session properties are reset to their default states. icon Inputs/Outputs civrn.png Instrument H

### niFgen Reset Device VI

Performs a hard reset on the device. Generation is stopped, all routes are released, external bidirectional terminals are tri-stated, FPGAs are reset, hardware is configured to its default state, and all session properties are reset to their default states.

[IMAGE alt='icon' src='nifgen-reset-device-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-reset-vi.html language=enus -->
## TOPIC 00136: niFgen Reset VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-reset-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-reset-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the instrument to a known state. This VI aborts the generation, clears all routes, and resets session properties to the default values. This VI does not, however, commit the session properties or configure the device hardware to its default state. For the NI 5404, this VI exhibits the same be

### niFgen Reset VI

Resets the instrument to a known state. This VI aborts the generation, clears all routes, and resets session properties to the default values. This VI does not, however, commit the session properties or configure the device hardware to its default state.

Note

niFgen Reset Device

[IMAGE alt='icon' src='nifgen-reset-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-restore-last-ext-cal-constants-vi.html language=enus -->
## TOPIC 00137: niFgen Restore Last Ext Cal Constants VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-restore-last-ext-cal-constants-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-restore-last-ext-cal-constants-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Overwrites the current calibration constants with those from the last successful external calibration. This action effectively undoes any self-calibrations performed since the last time an external calibration was performed. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifie

### niFgen Restore Last Ext Cal Constants VI

Overwrites the current calibration constants with those from the last successful external calibration. This action effectively undoes any self-calibrations performed since the last time an external calibration was performed.

[IMAGE alt='icon' src='nifgen-restore-last-ext-cal-constants-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-revision-query-vi.html language=enus -->
## TOPIC 00138: niFgen Revision Query VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-revision-query-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-revision-query-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision numbers of NI-FGEN and the instrument firmware. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize

### niFgen Revision Query VI

Returns the revision numbers of NI-FGEN and the instrument firmware.

[IMAGE alt='icon' src='nifgen-revision-query-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Size of Instrument Driver Revision — Size of Instrument Driver Revision specifies the maximum size of the instrument driver revision string and must be set to a minimum of 2,048. Size of Firmware Revision — Size of Firmware Revision specifies the maximum size of the firmware revision string. This parameter must be set to a minimum of 2,048. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Instrument Driver Revision — Instrument Driver Revision returns the NI-FGEN software revision numbers in the form of a string. Firmware Revision — Firmware Revision returns the instrument firmware revision numbers in the form of a string. Not all devices have firmware information available. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-route-signal-out-vi.html language=enus -->
## TOPIC 00139: niFgen Route Signal Out VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-route-signal-out-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-route-signal-out-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes various signals in the signal generator to the RTSI lines or front panel terminals. The signal generator must not be in the Generating state when you call this VI. You can clear a previously routed signal by routing NONE to the destination terminal. Not all signal routes established by callin

### niFgen Route Signal Out VI

Routes various signals in the signal generator to the RTSI lines or front panel terminals.

Note

Note

Not all signal routes established by calling this VI are released when the NI-FGEN session is closed by the [niFgen Close](nifgen-close-vi.html) VI.

| Routes To | Status |
| --- | --- |
| Front Panel | Remains connected |
| RTSI/PXI Backplane | Disconnected |

[IMAGE alt='icon' src='nifgen-route-signal-out-vi.png']

#### Inputs/Outputs

| Route Signal From — Route Signal From specifies the source of the signal to route. Input Value Source 0 NONE 1 MARKER 2 SYNC OUT 3 OUT START TRIGGER 4 BOARD CLOCK 5 SYNCHRONIZATION 6 SOFTWARE TRIGGER 7 REF IN 8 PXI_CLK10 9 PXI_STAR 10 PFI 0 11 RTSI 0 12 RTSI 1 13 RTSI 2 14 RTSI 3 15 RTSI 4 16 RTSI 5 17 RTSI 6 18 RTSI 7 19 RTSI CLOCK 20 CLOCK OUT 21 PLL REF SOURCE 22 UPDATE CLOCK 23 ONBOARD REF CLOCK Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Route Signal To — Route Signal To specifies the destination of the signal to route. Input Value Destination 0 RTSI 0 1 RTSI 1 2 RTSI 2 3 RTSI 3 4 RTSI 4 5 RTSI 5 6 RTSI 6 7 RTSI CLOCK 8 REF OUT 9 PFI 0 10 RTSI 7 11 PFI 1 12 PFI 4 13 PFI 5 14 PXI STAR Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Input Value | Source |
| 0 | NONE |
| 1 | MARKER |
| 2 | SYNC OUT |
| 3 | OUT START TRIGGER |
| 4 | BOARD CLOCK |
| 5 | SYNCHRONIZATION |
| 6 | SOFTWARE TRIGGER |
| 7 | REF IN |
| 8 | PXI_CLK10 |
| 9 | PXI_STAR |
| 10 | PFI 0 |
| 11 | RTSI 0 |
| 12 | RTSI 1 |
| 13 | RTSI 2 |
| 14 | RTSI 3 |
| 15 | RTSI 4 |
| 16 | RTSI 5 |
| 17 | RTSI 6 |
| 18 | RTSI 7 |
| 19 | RTSI CLOCK |
| 20 | CLOCK OUT |
| 21 | PLL REF SOURCE |
| 22 | UPDATE CLOCK |
| 23 | ONBOARD REF CLOCK |
| Input Value | Destination |
| 0 | RTSI 0 |
| 1 | RTSI 1 |
| 2 | RTSI 2 |
| 3 | RTSI 3 |
| 4 | RTSI 4 |
| 5 | RTSI 5 |
| 6 | RTSI 6 |
| 7 | RTSI CLOCK |
| 8 | REF OUT |
| 9 | PFI 0 |
| 10 | RTSI 7 |
| 11 | PFI 1 |
| 12 | PFI 4 |
| 13 | PFI 5 |
| 14 | PXI STAR |

Parent topic:

5404 Routing

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-self-cal-vi.html language=enus -->
## TOPIC 00140: niFgen Self Cal VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-self-cal-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-self-cal-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a full internal (self-) calibration on the device. If the calibration is successful, new calibration data and constants are stored in the onboard EEPROM. Refer to the calibration procedure of the signal generator for more information. This VI does not apply to the NI 5404, which uses differ

### niFgen Self Cal VI

Performs a full internal (self-) calibration on the device. If the calibration is successful, new calibration data and constants are stored in the onboard EEPROM. Refer to the calibration procedure of the signal generator for more information.

Note

[IMAGE alt='icon' src='nifgen-self-cal-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-self-test-vi.html language=enus -->
## TOPIC 00141: niFgen Self-Test VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-self-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-self-test-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs the instrument self-test routine and returns the test results. When used on some signal generators, the device is reset after the niFgen Self-Test VI runs. If you use the niFgen Self-Test VI, your device may not be in its previously configured state after the VI runs. icon Inputs/Outputs civrn.

### niFgen Self-Test VI

Runs the instrument self-test routine and returns the test results.

Note

[IMAGE alt='icon' src='nifgen-self-test-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Size of Self-Test Message — Size of Self-Test Message specifies the maximum size of the Self-Test Message string. Set Size of Self-Test Message to a minimum of 2,048. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Self-Test Message — Self-Test Message returns the self-test response string from the instrument. Self-Test Result — Self-Test Result returns the value returned from the instrument self-test. Zero means success. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-send-software-edge-trigger-vi.html language=enus -->
## TOPIC 00142: niFgen Send Software Edge Trigger VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-send-software-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-send-software-edge-trigger-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to trigger the signal generator. This VI can act as an override for an external edge trigger. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize W

### niFgen Send Software Edge Trigger VI

Sends a command to trigger the signal generator. This VI can act as an override for an external edge trigger.

[IMAGE alt='icon' src='nifgen-send-software-edge-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Trigger (Start Trigger) — Trigger specifies the type of software trigger to send. You can select Start Trigger or Script Trigger. Default value: Start Trigger Trigger ID (None) — Trigger ID specifies the Script Trigger to use for triggering. Default value: None error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Trigger & Synchronization

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-set-cal-user-defined-info-vi.html language=enus -->
## TOPIC 00143: niFgen Set Cal User Defined Info VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-set-cal-user-defined-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-set-cal-user-defined-info-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores user-defined information in the onboard EEPROM. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. cstr.png UserDefinedInfo UserDefinedInfo specifies the information string to be stored in the EEPROM. cerrcodeclst.png error in (no err

### niFgen Set Cal User Defined Info VI

Stores user-defined information in the onboard EEPROM.

[IMAGE alt='icon' src='nifgen-set-cal-user-defined-info-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. UserDefinedInfo — UserDefinedInfo specifies the information string to be stored in the EEPROM. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-set-named-waveform-next-write-position-vi.html language=enus -->
## TOPIC 00144: niFgen Set Named Waveform Next Write Position VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-set-named-waveform-next-write-position-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-set-named-waveform-next-write-position-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the position in the named waveform to which data is written at the next write. This VI allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the Waveform Name parameter. Subsequent writes to that waveform begin w

### niFgen Set Named Waveform Next Write Position VI

Sets the position in the named waveform to which data is written at the next write. This VI allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the **Waveform Name** parameter. Subsequent writes to that waveform begin where the last write ended, unless this VI is called again. The **Waveform Name** passed in must have been created by a call to the [niFgen Allocate Waveform](/csh?topicname=nifgen-allocate-waveform-vi.html) VI or the [niFgen Clear Arbitrary Waveform](/csh?topicname=nifgen-clear-arbitrary-waveform-vi.html) VI.

[IMAGE alt='icon' src='nifgen-set-named-waveform-next-write-position-vi.png']

#### Inputs/Outputs

| Relative To — Relative To specifies the reference position in the waveform. This position and Offset together determine where to start loading data into the waveform. Input Value Input Name Description 0 NIFGEN_VAL_WAVEFORM_POSITION_CURRENT The reference position is relative to the current position. 1 NIFGEN_VAL_WAVEFORM_POSITION_START The reference position is relative to the start of the waveform. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Name — Waveform Name specifies the name of the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Offset — Offset specifies the offset from the Relative To parameter at which to start loading the data into the waveform. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Name Out — Waveform Name Out passes the name of the named waveform. error out — error out contains error information. This output provides standard error out functionality. |  |  |
| --- | --- | --- |
| Input Value | Input Name | Description |
| 0 | NIFGEN_VAL_WAVEFORM_POSITION_CURRENT | The reference position is relative to the current position. |
| 1 | NIFGEN_VAL_WAVEFORM_POSITION_START | The reference position is relative to the start of the waveform. |

Parent topic:

Script

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-set-sample-rate-vi.html language=enus -->
## TOPIC 00145: niFgen Set Sample Rate VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-set-sample-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-set-sample-rate-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sample rate, which determines the rate at which the signal generator produces arbitrary waveforms. When you configure the signal generator to produce an arbitrary sequence, this is the sample rate for all arbitrary waveforms in the sequence. If the update clock (Sample clock) source i

### niFgen Set Sample Rate VI

Configures the sample rate, which determines the rate at which the signal generator produces arbitrary waveforms. When you configure the signal generator to produce an arbitrary sequence, this is the sample rate for all arbitrary waveforms in the sequence. If the update clock (Sample clock) source is external, setting the sample rate informs NI-FGEN of the external rate.

Note

Note

Output Mode

Arbitrary Waveform

Arbitrary Sequence

niFgen Configure Output Mode

[IMAGE alt='icon' src='nifgen-set-sample-rate-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Sample Rate (Samp/s) — Sample Rate specifies the sample rate at which you want the signal generator to generate arbitrary waveforms. If you are using an external update clock (Sample clock), this is the frequency of the external update clock. Units: Samples per second (S/s) error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Clock

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-set-waveform-next-write-position-vi.html language=enus -->
## TOPIC 00146: niFgen Set Waveform Next Write Position VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-set-waveform-next-write-position-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-set-waveform-next-write-position-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the position in the waveform at which data is written during the next write. This VI allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the Waveform Handle parameter. Subsequent writes to that waveform begin w

### niFgen Set Waveform Next Write Position VI

Sets the position in the waveform at which data is written during the next write. This VI allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the **Waveform Handle** parameter. Subsequent writes to that waveform begin where the last write left off, unless this VI is called again. The **Waveform Handle** passed in must have been created by a call to the [niFgen Allocate Waveform](/csh?topicname=nifgen-allocate-waveform-vi.html) VI or the [niFgen Clear Arbitrary Waveform](/csh?topicname=nifgen-clear-arbitrary-waveform-vi.html) VI.

[IMAGE alt='icon' src='nifgen-set-waveform-next-write-position-vi.png']

#### Inputs/Outputs

| Relative To — Relative To specifies the reference position in the waveform. This position and Offset together determine where to start loading data into the waveform. Input Value Input Name Description 0 NIFGEN_VAL_WAVEFORM_POSITION_CURRENT The reference position is relative to the current position. 1 NIFGEN_VAL_WAVEFORM_POSITION_START The reference position is relative to the start of the waveform. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Handle — Waveform Handle specifies the handle of the arbitrary waveform previously allocated with the niFgen Allocate Waveform VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Offset — Offset specifies the offset from the Relative To parameter at which to start loading the data into the waveform. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle Out — Waveform Handle Out returns the handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |  |  |
| --- | --- | --- |
| Input Value | Input Name | Description |
| 0 | NIFGEN_VAL_WAVEFORM_POSITION_CURRENT | The reference position is relative to the current position. |
| 1 | NIFGEN_VAL_WAVEFORM_POSITION_START | The reference position is relative to the start of the waveform. |

Parent topic:

Arbitrary Waveform

Parent topic:

Arbitrary Sequence

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-util-create-bin16-waveform-data-vi.html language=enus -->
## TOPIC 00147: niFgen Util Create Bin16 Waveform Data VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-util-create-bin16-waveform-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-util-create-bin16-waveform-data-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an array of 16-bit integers (I16) corresponding to the selected waveform. The number 1.0 is scaled to full range of 32,767. icon Inputs/Outputs cnclst.png Waveform Waveform specifies waveform information that is used to generate the waveform data. cu16.png Waveform Type Waveform Type selects

### niFgen Util Create Bin16 Waveform Data VI

Creates an array of 16-bit integers (I16) corresponding to the selected waveform. The number 1.0 is scaled to full range of 32,767.

[IMAGE alt='icon' src='nifgen-util-create-bin16-waveform-data-vi.png']

#### Inputs/Outputs

| Waveform — Waveform specifies waveform information that is used to generate the waveform data. Waveform Type — Waveform Type selects the type of waveform. Amplitude — Amplitude specifies the amplitude of the waveform that you want the signal generator to produce. This value is the amplitude at the output terminal. For example, to produce a waveform ranging from -5.00 V to +5.00 V, set Amplitude to 5.00 V. Units: peak voltage Note This parameter does not affect signal generator behavior when you set Waveform Type to DC. # of Points — # of Points specifies the number of points in the waveform. Waveform Data — Waveform Data returns the waveform output. |
| --- |
| Waveform Type — Waveform Type selects the type of waveform. Amplitude — Amplitude specifies the amplitude of the waveform that you want the signal generator to produce. This value is the amplitude at the output terminal. For example, to produce a waveform ranging from -5.00 V to +5.00 V, set Amplitude to 5.00 V. Units: peak voltage Note This parameter does not affect signal generator behavior when you set Waveform Type to DC. # of Points — # of Points specifies the number of points in the waveform. |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-util-create-frequency-sweep-data-vi.html language=enus -->
## TOPIC 00148: niFgen Util Create Frequency Sweep Data VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-util-create-frequency-sweep-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-util-create-frequency-sweep-data-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an array of doubles filled with the frequencies specified. The frequencies are created in a logarithmic progression from Start Frequency to Stop Frequency. icon Inputs/Outputs cdbl.png Start Frequency Start Frequency specifies the first frequency of the sweep to be generated. cdbl.png Stop F

### niFgen Util Create Frequency Sweep Data VI

Creates an array of doubles filled with the frequencies specified. The frequencies are created in a logarithmic progression from **Start Frequency** to **Stop Frequency**.

[IMAGE alt='icon' src='nifgen-util-create-frequency-sweep-data-vi.png']

#### Inputs/Outputs

| Start Frequency — Start Frequency specifies the first frequency of the sweep to be generated. Stop Frequency — Stop Frequency specifies the last frequency of the sweep to be generated. # Frequency Steps — # Frequency Steps specifies the number of frequencies in the frequency sweep. Frequency Sweep Array — Frequency Sweep Array returns the array of double-precision floating-point data filled with the frequencies specified. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-util-create-waveform-data-vi.html language=enus -->
## TOPIC 00149: niFgen Util Create Waveform Data VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-util-create-waveform-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-util-create-waveform-data-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an array of doubles filled with the specified waveform. icon Inputs/Outputs cnclst.png Waveform Waveform specifies waveform information that is used to generate the waveform data. cu16.png Waveform Type Waveform Type selects the type of waveform. cdbl.png Amplitude Amplitude specifies the am

### niFgen Util Create Waveform Data VI

Creates an array of doubles filled with the specified waveform.

[IMAGE alt='icon' src='nifgen-util-create-waveform-data-vi.png']

#### Inputs/Outputs

| Waveform — Waveform specifies waveform information that is used to generate the waveform data. Waveform Type — Waveform Type selects the type of waveform. Amplitude — Amplitude specifies the amplitude of the waveform that you want the signal generator to produce. This value is the amplitude at the output terminal. For example, to produce a waveform ranging from -5.00 V to +5.00 V, set Amplitude to 5.00 V. Units: peak voltage Note This parameter does not affect signal generator behavior when you set Waveform Type to DC. # of Points — # of Points specifies the number of points in the waveform. Waveform Data — Waveform Data returns the waveform output. |
| --- |
| Waveform Type — Waveform Type selects the type of waveform. Amplitude — Amplitude specifies the amplitude of the waveform that you want the signal generator to produce. This value is the amplitude at the output terminal. For example, to produce a waveform ranging from -5.00 V to +5.00 V, set Amplitude to 5.00 V. Units: peak voltage Note This parameter does not affect signal generator behavior when you set Waveform Type to DC. # of Points — # of Points specifies the number of points in the waveform. |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-wait-until-done-vi.html language=enus -->
## TOPIC 00150: niFgen Wait Until Done VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-wait-until-done-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-wait-until-done-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the device is done generating or until the maximum time has expired. This VI reports Instrument Handle Out to the next VI only after the current generation is complete in Single Trigger mode. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instru

### niFgen Wait Until Done VI

Waits until the device is done generating or until the maximum time has expired.

Note

Instrument Handle Out

[IMAGE alt='icon' src='nifgen-wait-until-done-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. MaxTime (msec) — MaxTime (msec) specifies the timeout value in milliseconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-binary-16-analog-static-value-vi.html language=enus -->
## TOPIC 00151: niFgen Write Binary 16 Analog Static Value VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-binary-16-analog-static-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-binary-16-analog-static-value-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a 16-bit value to the DAC, which could be output as a DC voltage. This VI writes to the DAC only when used in an external calibration session. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen In

### niFgen Write Binary 16 Analog Static Value VI

Writes a 16-bit value to the DAC, which could be output as a DC voltage.

This VI writes to the DAC only when used in an external calibration session.

[IMAGE alt='icon' src='nifgen-write-binary-16-analog-static-value-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies your instrument session. Instrument Handle is obtained from the niFgen Init Ext Cal VI. Channel Name — Channel Name specifies the channel that this VI uses. Value — Value specifies the value to write. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

ADC Control

Parent topic:

Analog Output Control

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-binary-16-waveform-vi.html language=enus -->
## TOPIC 00152: niFgen Write Binary 16 Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-binary-16-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-binary-16-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes binary data to a waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data. This instance can also write complex data to a waveform in onboard memory o

### niFgen Write Binary 16 Waveform VI

Writes binary data to a waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

This instance can also write complex data to a waveform in onboard memory on devices with the [OSP Enabled](/csh?context=nifgen_nifgenpropref_pnifgen_ospenabled) property set to TRUE and the [Data Processing Mode](/csh?context=nifgen_nifgenpropref_pnifgen_dataprocessingmode) property set to **Complex**. To write complex data, you must interleave the I/Q pairs or use the Complex DBL or Complex WDT instances of this VI.

[IMAGE alt='icon' src='nifgen-write-binary-16-waveform-vi.png']

#### Inputs/Outputs

| Waveform Data — Waveform Data specifies the array of data you want to load into the waveform. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Handle — Waveform Handle specifies the handle of the arbitrary waveform previously allocated with the niFgen Allocate Waveform VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle Out — Waveform Handle Out returns the handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Write Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-complex-wdt-waveform-vi.html language=enus -->
## TOPIC 00153: niFgen Write Complex WDT Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-complex-wdt-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-complex-wdt-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex WDT data to a waveform in the device onboard memory. Use this instance when the OSP Enabled property is set to True and the Data Processing Mode property is set to Complex. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to th

### niFgen Write Complex WDT Waveform VI

Writes complex WDT data to a waveform in the device onboard memory. Use this instance when the [OSP Enabled](/csh?context=nifgen_nifgenpropref_pnifgen_ospenabled) property is set to **True** and the [Data Processing Mode](/csh?context=nifgen_nifgenpropref_pnifgen_dataprocessingmode) property is set to **Complex**. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

[IMAGE alt='icon' src='nifgen-write-complex-wdt-waveform-vi.png']

#### Inputs/Outputs

| Use Waveform dT for IQ Rate — Use Waveform dT for IQ Rate specifies whether the I/Q rate should be set to match the sampling information contained in the Waveform parameter. Waveform — Waveform specifies the data you want to use for the arbitrary waveform. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Handle — Waveform Handle specifies the handle of the arbitrary waveform previously allocated with the niFgen Allocate Waveform VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle Out — Waveform Handle Out returns the handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Write Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-complex-dbl-vi.html language=enus -->
## TOPIC 00154: niFgen Write Named Waveform (Complex DBL) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-complex-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-complex-dbl-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex data to the named waveform in onboard memory on devices with the OSP Enabled property set to TRUE and the Data Processing Mode property set to Complex. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for

### niFgen Write Named Waveform (Complex DBL) VI

Writes complex data to the named waveform in onboard memory on devices with the [OSP Enabled](/csh?context=nifgen_nifgenpropref_pnifgen_ospenabled) property set to TRUE and the [Data Processing Mode](/csh?context=nifgen_nifgenpropref_pnifgen_dataprocessingmode) property set to **Complex**. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

[IMAGE alt='icon' src='nifgen-write-named-waveform-complex-dbl-vi.png']

#### Inputs/Outputs

| Waveform Data — Waveform Data specifies the array of data you want to load into the waveform. You must normalize the data points in the array to be between -1.00 and +1.00. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Name — Waveform Name specifies the name of the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Name Out — Waveform Name Out passes the name of the named waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Write Named Waveform VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-complex-wdt-vi.html language=enus -->
## TOPIC 00155: niFgen Write Named Waveform (Complex WDT) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-complex-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-complex-wdt-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex WDT data to the waveform in the device onboard memory. Use this instance when the OSP Enabled property set to TRUE and the Data Processing Mode property set to Complex. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the St

### niFgen Write Named Waveform (Complex WDT) VI

Writes complex WDT data to the waveform in the device onboard memory. Use this instance when the [OSP Enabled](/csh?context=nifgen_nifgenpropref_pnifgen_ospenabled) property set to TRUE and the [Data Processing Mode](/csh?context=nifgen_nifgenpropref_pnifgen_dataprocessingmode) property set to **Complex**. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

[IMAGE alt='icon' src='nifgen-write-named-waveform-complex-wdt-vi.png']

#### Inputs/Outputs

| Use Waveform dT for IQ Rate — Use Waveform dT for IQ Rate specifies whether the I/Q rate should be set to match the sampling information contained in the Waveform parameter. Waveform — Waveform specifies the data you want to use for the arbitrary waveform. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Name — Waveform Name specifies the name of the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Name Out — Waveform Name Out passes the name of the named waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Write Named Waveform VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-dbl-vi.html language=enus -->
## TOPIC 00156: niFgen Write Named Waveform (DBL) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-dbl-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes floating-point data to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data. icon Inputs/Outputs c1ddbl.png Waveform Data Waveform Data

### niFgen Write Named Waveform (DBL) VI

Writes floating-point data to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

[IMAGE alt='icon' src='nifgen-write-named-waveform-dbl-vi.png']

#### Inputs/Outputs

| Waveform Data — Waveform Data specifies the array of data you want to load into the waveform. You must normalize the data points in the array to be between -1.00 and +1.00. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Name — Waveform Name specifies the name of the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Name Out — Waveform Name Out passes the name of the named waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Write Named Waveform VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-direct-dma-i16-vi.html language=enus -->
## TOPIC 00157: niFgen Write Named Waveform Direct DMA (I16) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-direct-dma-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-direct-dma-i16-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a specified amount of data from a Direct DMA-compatible device to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data. icon Inputs/Outp

### niFgen Write Named Waveform Direct DMA (I16) VI

Writes a specified amount of data from a Direct DMA-compatible device to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

[IMAGE alt='icon' src='nifgen-write-named-waveform-direct-dma-i16-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Name — Waveform Name specifies the name of the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Window Address — Window Address specifies the windows address of the Direct DMA-compatible data source. Samples to Write — Samples to Write specifies the number of samples to write from the Direct DMA-compatible data source. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Name Out — Waveform Name Out passes the name of the named waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Write Named Waveform VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-i16-vi.html language=enus -->
## TOPIC 00158: niFgen Write Named Waveform (I16) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-i16-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes binary data to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data. This instance can also write complex data to the named waveform in

### niFgen Write Named Waveform (I16) VI

Writes binary data to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

This instance can also write complex data to the named waveform in onboard memory on devices with the [OSP Enabled](/csh?context=nifgen_nifgenpropref_pnifgen_ospenabled) property set to TRUE and the [Data Processing Mode](/csh?context=nifgen_nifgenpropref_pnifgen_dataprocessingmode) property set to **Complex**. To write complex data, you must interleave the I/Q pairs or use the Complex DBL or Complex WDT instances of this VI.

[IMAGE alt='icon' src='nifgen-write-named-waveform-i16-vi.png']

#### Inputs/Outputs

| Waveform Data — Waveform Data specifies the array of data you want to load into the waveform. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Name — Waveform Name specifies the name of the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Name Out — Waveform Name Out passes the name of the named waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Write Named Waveform VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-vi.html language=enus -->
## TOPIC 00159: niFgen Write Named Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: By default, the subsequent call to the niFgen Write Named Waveform (poly) VI continues writing data from the position of the last sample written. The write position and offset can be set using the niFgen Set Named Waveform Next Write Position VI. If streaming is enabled, you can write more data than

### niFgen Write Named Waveform VI

By default, the subsequent call to the niFgen Write Named Waveform (poly) VI continues writing data from the position of the last sample written. The write position and offset can be set using the [niFgen Set Named Waveform Next Write Position](/csh?topicname=nifgen-set-named-waveform-next-write-position-vi.html) VI. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

[IMAGE alt='icon' src='nifgen-write-named-waveform-vi.png']

- [niFgen Write Named Waveform (DBL) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-dbl-vi.html) Writes floating-point data to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.
- [niFgen Write Named Waveform (I16) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-i16-vi.html) Writes binary data to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.
- [niFgen Write Named Waveform (WDT) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-wdt-vi.html) Writes WDT data to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.
- [niFgen Write Named Waveform (Complex DBL) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-complex-dbl-vi.html) Writes complex data to the named waveform in onboard memory on devices with the OSP Enabled property set to TRUE and the Data Processing Mode property set to Complex . If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.
- [niFgen Write Named Waveform Direct DMA (I16) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-direct-dma-i16-vi.html) Writes a specified amount of data from a Direct DMA-compatible device to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.
- [niFgen Write Named Waveform (Complex WDT) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-complex-wdt-vi.html) Writes complex WDT data to the waveform in the device onboard memory. Use this instance when the OSP Enabled property set to TRUE and the Data Processing Mode property set to Complex . If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.

Parent topic:

Script

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-wdt-vi.html language=enus -->
## TOPIC 00160: niFgen Write Named Waveform (WDT) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-named-waveform-wdt-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes WDT data to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data. icon Inputs/Outputs cbool.png Use Waveform dT for Sample Rate Use Wave

### niFgen Write Named Waveform (WDT) VI

Writes WDT data to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

[IMAGE alt='icon' src='nifgen-write-named-waveform-wdt-vi.png']

#### Inputs/Outputs

| Use Waveform dT for Sample Rate — Use Waveform dT for Sample Rate specifies whether the sample rate should be set to match the sampling information contained in the Waveform parameter. Waveform — Waveform specifies the data you want to use for the arbitrary waveform. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Name — Waveform Name specifies the name of the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Name Out — Waveform Name Out passes the name of the named waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Write Named Waveform VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-p2p-endpoint-i16-vi.html language=enus -->
## TOPIC 00161: niFgen Write P2P Endpoint I16 VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-p2p-endpoint-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-p2p-endpoint-i16-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes I16 data to the peer-to-peer endpoint. Use this VI to write initial data from the host to the endpoint before starting generation to avoid underflow at the beginning of the generation. icon Inputs/Outputs c1di16.png Endpoint Data Endpoint Data specifies the array of data to write into the end

### niFgen Write P2P Endpoint I16 VI

Writes I16 data to the peer-to-peer endpoint. Use this VI to write initial data from the host to the endpoint before starting generation to avoid underflow at the beginning of the generation.

[IMAGE alt='icon' src='nifgen-write-p2p-endpoint-i16-vi.png']

#### Inputs/Outputs

| Endpoint Data — Endpoint Data specifies the array of data to write into the endpoint FIFO. The binary data is left-justified. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Endpoint Name — Endpoint Name specifies the name of the FIFO endpoint. Data is written to the endpoint FIFO. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Endpoint Name Out — Endpoint Name Out passes a reference to the FIFO endpoint to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Peer-to-Peer (P2P)

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-script-vi.html language=enus -->
## TOPIC 00162: niFgen Write Script VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-script-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-script-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a string containing one or more scripts that govern the generation of waveforms. icon Inputs/Outputs civrn.png Instrument Handle Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the

### niFgen Write Script VI

Writes a string containing one or more scripts that govern the generation of waveforms.

[IMAGE alt='icon' src='nifgen-write-script-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Script — Script contains the text of the script you want to use for your generation operation. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Script

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-complex-dbl-vi.html language=enus -->
## TOPIC 00163: niFgen Write Waveform (Complex DBL) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-complex-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-complex-dbl-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex data to the waveform in onboard memory on devices with the OSP Enabled property set to TRUE and the Data Processing Mode property set to Complex. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more

### niFgen Write Waveform (Complex DBL) VI

Writes complex data to the waveform in onboard memory on devices with the [OSP Enabled](/csh?context=nifgen_nifgenpropref_pnifgen_ospenabled) property set to TRUE and the [Data Processing Mode](/csh?context=nifgen_nifgenpropref_pnifgen_dataprocessingmode) property set to **Complex**. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

[IMAGE alt='icon' src='nifgen-write-waveform-complex-dbl-vi.png']

#### Inputs/Outputs

| Waveform Data — Waveform Data specifies the array of data you want to load into the waveform. You must normalize the data points in the array to be between -1.00 and +1.00. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Handle — Waveform Handle specifies the handle of the arbitrary waveform previously allocated with the niFgen Allocate Waveform VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle Out — Waveform Handle Out returns the handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Write Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-i16-direct-dma-vi.html language=enus -->
## TOPIC 00164: niFgen Write Waveform I16 Direct DMA VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-i16-direct-dma-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-i16-direct-dma-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a specified amount of data from a Direct DMA-compatible device to the waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data. icon Inputs/Outputs ci

### niFgen Write Waveform I16 Direct DMA VI

Writes a specified amount of data from a Direct DMA-compatible device to the waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

[IMAGE alt='icon' src='nifgen-write-waveform-i16-direct-dma-vi.png']

#### Inputs/Outputs

| Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Handle — Waveform Handle specifies the handle of the arbitrary waveform previously allocated with the niFgen Allocate Waveform VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Window Address — Window Address specifies the windows address of the Direct DMA-compatible data source. Samples to Write — Samples to Write specifies the number of samples to write from the Direct DMA-compatible data source. Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle Out — Waveform Handle Out returns the handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Write Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-poly-vi.html language=enus -->
## TOPIC 00165: niFgen Write Waveform (poly) VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-poly-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to the waveform in onboard memory. The Waveform Handle passed in must have been created by a call to the niFgen Allocate Waveform VI or the niFgen Create Waveform (poly) VI. By default, the subsequent call to the niFgen Write Waveform (poly) VI continues writing data from the position of

### niFgen Write Waveform (poly) VI

Writes data to the waveform in onboard memory.

The **Waveform Handle** passed in must have been created by a call to the [niFgen Allocate Waveform](nifgen-allocate-waveform-vi.html) VI or the [niFgen Create Waveform (poly)](nifgen-create-waveform-poly-vi.html) VI. By default, the subsequent call to the niFgen Write Waveform (poly) VI continues writing data from the position of the last sample written. You can change the write position and offset using the [niFgen Set Waveform Next Write Position](nifgen-set-waveform-next-write-position-vi.html) VI. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

[IMAGE alt='icon' src='nifgen-write-waveform-poly-vi.png']

- [niFgen Write Waveform VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-vi.html) Writes data to a waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.
- [niFgen Write Binary 16 Waveform VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-write-binary-16-waveform-vi.html) Writes binary data to a waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.
- [niFgen Write WDT Waveform VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-write-wdt-waveform-vi.html) Writes WDT data to the waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.
- [niFgen Write Waveform (Complex DBL) VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-complex-dbl-vi.html) Writes complex data to the waveform in onboard memory on devices with the OSP Enabled property set to TRUE and the Data Processing Mode property set to Complex . If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.
- [niFgen Write Waveform I16 Direct DMA VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-i16-direct-dma-vi.html) Writes a specified amount of data from a Direct DMA-compatible device to the waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.
- [niFgen Write Complex WDT Waveform VI](../../../instr-lib/nifgen/nifgen-llb/nifgen-write-complex-wdt-waveform-vi.html) Writes complex WDT data to a waveform in the device onboard memory. Use this instance when the OSP Enabled property is set to True and the Data Processing Mode property is set to Complex . If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data.

Parent topic:

Arbitrary Waveform

Parent topic:

Arbitrary Sequence

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-vi.html language=enus -->
## TOPIC 00166: niFgen Write Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to a waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data. icon Inputs/Outputs c1ddbl.png Waveform Data Waveform Data specifies the array of

### niFgen Write Waveform VI

Writes data to a waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

[IMAGE alt='icon' src='nifgen-write-waveform-vi.png']

#### Inputs/Outputs

| Waveform Data — Waveform Data specifies the array of data you want to load into the waveform. You must normalize the data points in the array to be between -1.00 and +1.00. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Handle — Waveform Handle specifies the handle of the arbitrary waveform previously allocated with the niFgen Allocate Waveform VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle Out — Waveform Handle Out returns the handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Write Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/nifgen-write-wdt-waveform-vi.html language=enus -->
## TOPIC 00167: niFgen Write WDT Waveform VI

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/nifgen-write-wdt-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/nifgen-write-wdt-waveform-vi.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes WDT data to the waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the Streaming topic for more information about streaming data. icon Inputs/Outputs cbool.png Use Waveform dT for Sample Rate Use Waveform d

### niFgen Write WDT Waveform VI

Writes WDT data to the waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. Refer to the [Streaming](/csh?context=nifgen_siggenhelp_streaming) topic for more information about streaming data.

[IMAGE alt='icon' src='nifgen-write-wdt-waveform-vi.png']

#### Inputs/Outputs

| Use Waveform dT for Sample Rate — Use Waveform dT for Sample Rate specifies whether the sample rate should be set to match the sampling information contained in the Waveform parameter. Waveform — Waveform specifies the data you want to use for the arbitrary waveform. Instrument Handle — Instrument Handle identifies a particular instrument session. Instrument Handle is obtained from the niFgen Initialize VI, niFgen Initialize With Options VI, or the niFgen Initialize With Channels VI. Channel Name — Channel Name specifies the channel that this VI uses. Waveform Handle — Waveform Handle specifies the handle of the arbitrary waveform previously allocated with the niFgen Allocate Waveform VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Default value: no error Instrument Handle Out — Instrument Handle Out passes a reference to your instrument session to the next VI. Waveform Handle Out — Waveform Handle Out returns the handle that identifies the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niFgen Write Waveform (poly) VI

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00168: Using the Standard Functionality for error in Parameters

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/standard-functionality-for-error-in-parameters.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error

### Using the Standard Functionality for error in Parameters

Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error in behavior is as follows

Note

error in

error in

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-llb/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00169: Using the Standard Functionality for error out Parameters

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-llb/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-llb/standard-functionality-for-error-out-parameters.html
- document_id: `ni-fgen-labview-api-ref`
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

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-measurementlink-mnu.html language=enus -->
## TOPIC 00170: MeasurementLink

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-measurementlink-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-measurementlink-mnu.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette in conjunction with MeasurementLink Session Management. icon

### MeasurementLink

Use the VIs on this palette in conjunction with MeasurementLink Session Management.

[IMAGE alt='icon' src='nifgen-measurementlink-mnu.png']

- [niFgen Initialize With Channels for gRPC Session VI](../../instr-lib/nifgen/nifgen-llb/nifgen-initialize-with-channels-for-grpc-session-vi.html) Initializes a new NI-FGEN session on the specified NI gRPC Device Server using the specified instrument(s) and channel(s).
- [niFgen Attach gRPC Session VI](../../instr-lib/nifgen/nifgen-llb/nifgen-attach-grpc-session-vi.html) Attaches to an existing NI-FGEN session with the specified Session Name on the specified NI gRPC Device Server. Returns a session handle to be used in all subsequent NI-FGEN VI calls.
- [niFgen Detach gRPC Session VI](../../instr-lib/nifgen/nifgen-llb/nifgen-detach-grpc-session-vi.html) Closes the session specified in instrument handle but leaves the session open on the NI gRPC Device Server.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen-p.html language=enus -->
## TOPIC 00171: niFgen Properties

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen-p.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN properties to access advanced configuration options for signal generator applications. © 2008–2019 National Instruments. All rights reserved.

### niFgen Properties

Use the NI-FGEN properties to access advanced configuration options for signal generator applications.

© 2008–2019 National Instruments. All rights reserved.

- [Active Channel](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-activechannel.html) Specifies the channel used to access all subsequent channel-based properties. You must set this property before setting any channel-based properties. Pass a name that the instrument driver defines or a virtual channel name defined in MAX.
- [Output:Output Mode](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-outputmode.html) Specifies the output mode the signal generator uses. The output mode you specify determines which VIs and properties you use to configure the waveform the signal generator produces.
- [Output:Output Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-outputenabled.html) Specifies whether the signal that the signal generator produces appears at the output connector.
- [Output:Digital Gain](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalgain.html) Specifies a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the DAC. For a digital gain greater than 1.0, the product of digital gain times the generated data must be inside the range ±1.0, assuming floating point data. If the product exceeds these limits, the signal generator clips the output signal, and an error results.
- [Output:Analog Path](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogpath.html) Specifies the analog signal path. The main path allows the user to configure gain, offset, analog filter status, output impedance, and output enable.
- [Output:Load Impedance](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-loadimpedance.html) Specifies the load impedance connected to the analog output of the channel.
- [Output:Output Impedance](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-outputimpedance.html) Specifies the output impedance of the signal generator at the output connector. NI signal generators have an output impedance of 50 ohms and an optional 75 ohms on select modules.
- [Output:Terminal Configuration](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-terminalconfiguration.html) Specifies whether to analyze gain and offset values based on single-ended or differential operation.
- [Output:Common Mode Offset](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-commonmodeoffset.html) Specifies the value the signal generator adds to or subtracts from the arbitrary waveform data. This property applies only when set the Terminal Configuration property to Differential . Common-mode offset is applied to the signals generated at each differential output terminal.
- [Output:Channel Delay](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-channeldelay.html) Specifies the delay to apply to the analog output of the channel specified by the Active Channel property.
- [Output:Absolute Delay](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-absolutedelay.html) Specifies the sub-Sample Clock delay, in seconds, to apply to the waveform. Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurement to the current session.
- [Output:Filters:Analog Filter Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogfilterenabled.html) Specifies whether the signal generator applies an analog filter to the output signal. Set this property to TRUE to enable the filter. This property is valid in Arbitrary Waveform, Arbitrary Sequence, and Script output modes. You also can use this property in Standard Function and Frequency List output modes for user-defined waveforms.
- [Output:Filters:Digital Filter Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalfilterenabled.html) Specifies whether the signal generator applies a digital filter to the output signal. Set this property to TRUE to use a digital filter. This property is valid in Arbitrary Waveform, Arbitrary Sequence, and Script output modes. You also can use this property in Standard Function and Frequency List output modes for user-defined waveforms.
- [Output:Filters:Digital Filter Interpolation Factor](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalfilterinterpolationfactor.html) Specifies the interpolation factor when the Digital Filter Enabled property is set to TRUE.
- [Output:Filters:Flatness Correction Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-flatnesscorrectionenabled.html) Specify a value of TRUE to enable flatness correction. When flatness correction is enabled, the signal generator applies a flatness correction factor to the generated sine wave to ensure the same output power level at all frequencies.
- [Output:Data Mask:Analog Data Mask](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogdatamask.html) Specifies the mask to apply to the analog output data. The masked data is replaced with the data in the Analog Static Value property.
- [Output:Data Mask:Analog Static Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogstaticvalue.html) Specifies the static value that replaces data masked by the Analog Data Mask property.
- [Output:Data Mask:Digital Data Mask](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitaldatamask.html) Specifies the mask to apply to the output on the digital connector. The masked data is replaced with the data in the Digital Static Value property.
- [Output:Data Mask:Digital Static Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalstaticvalue.html) Specifies the static value that replaces data masked by the Digital Data Mask property.
- [Output:Advanced:Digital Pattern Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalpatternenabled.html) Specifies whether the signal generator generates a digital pattern corresponding to the output signal. Set this property to TRUE to generate a digital pattern.
- [Output:Advanced:AUX Power Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-auxpowerenabled.html) Controls the specified auxiliary power pin. Setting this property to TRUE energizes the auxiliary power when the session is committed. When this property is FALSE, the power pin of the connector outputs no power.
- [Output:Advanced:Idle Behavior](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-idlebehavior.html) Specifies the behavior of the output during the Idle state.
- [Output:Advanced:Idle Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-idlevalue.html) Specifies the value to generate in the Idle state. You must set the Idle Behavior property to Jump To Value to use this property.
- [Output:Advanced:Wait Behavior](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-waitbehavior.html) Specifies the behavior of the output while waiting for a Script Trigger or during a wait instruction.
- [Output:Advanced:Wait Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-waitvalue.html) Specifies the value to generate while waiting. You must set the Wait Behavior property to Jump To Value to use this property.
- [Arbitrary Waveform:Gain](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarywaveformgain.html) Specifies the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to scale the arbitrary waveform to other ranges.
- [Arbitrary Waveform:Offset](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarywaveformoffset.html) Specifies the value the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to shift the arbitrary waveform range.
- [Arbitrary Waveform:Arbitrary Waveform Mode:Arbitrary Waveform Handle](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarywaveformhandle.html) Selects which arbitrary waveform the signal generator produces. You can create multiple arbitrary waveforms using the niFgen Create Waveform VI.
- [Arbitrary Waveform:Arbitrary Waveform Mode:Marker Position](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbwfm-markerpos.html) Specifies the position for a marker to be asserted in the arbitrary waveform.
- [Arbitrary Waveform:Arbitrary Waveform Mode:Repeat Count](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbwfm-repeatcount.html) Specifies the number of times to repeat the arbitrary waveform when the Trigger Mode parameter in the niFgen Configure Trigger Mode VI is set to Single or Stepped .
- [Arbitrary Waveform:Arbitrary Sequence Mode:Arbitrary Sequence Handle](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarysequencehandle.html) Selects which sequence the signal generator produces. You can create multiple sequences using the niFgen Create Arbitrary Sequence VI.
- [Arbitrary Waveform:Arbitrary Sequence Mode:Max Number of Sequences](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxnumberofsequences.html) Returns the maximum number of arbitrary sequences the signal generator allows.
- [Arbitrary Waveform:Arbitrary Sequence Mode:Max Sequence Length](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxsequencelength.html) Returns the maximum number of arbitrary waveforms the signal generator allows in a sequence.
- [Arbitrary Waveform:Arbitrary Sequence Mode:Min Sequence Length](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minsequencelength.html) Returns the minimum number of arbitrary waveforms the signal generator allows in a sequence. Typically, this value is constant for the signal generator.
- [Arbitrary Waveform:Arbitrary Sequence Mode:Max Loop Count](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxloopcount.html) Returns the maximum number of times the signal generator can repeat a waveform in a sequence. Typically, this value is constant for the signal generator.
- [Arbitrary Waveform:Script Mode:Script to Generate](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttogenerate.html) Specifies which script the signal generator uses. To configure the signal generator to run a particular script, set this property to the name of the script.
- [Arbitrary Waveform:Capabilities:Waveform Quantum](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-quantum.html) Returns the quantum value the signal generator allows. The size of each arbitrary waveform must be a multiple of this quantum value.
- [Arbitrary Waveform:Capabilities:Max Number of Waveforms](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxnumberofwaveforms.html) Returns the maximum number of arbitrary waveforms that the signal generator allows. On some signal generators, this value may vary with remaining onboard memory.
- [Arbitrary Waveform:Capabilities:Min Waveform Size](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minwaveformsize.html) Returns the minimum number of points the signal generator allows in an arbitrary waveform. Typically, this value is constant for the signal generator.
- [Arbitrary Waveform:Capabilities:Max Waveform Size](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maxwaveformsize.html) Returns the maximum number of points the signal generator allows in an arbitrary waveform. On some signal generators, this value may vary with remaining onboard memory.
- [Arbitrary Waveform:Data Transfer:Data Transfer Block Size](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferblocksize.html) Specifies the number of samples at a time to download to onboard memory. This property is useful when the total data to be transferred to onboard memory is large.
- [Arbitrary Waveform:Data Transfer:File Transfer Block Size](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-filetransferblocksize.html) Specifies the maximum number of samples to transfer at one time from the device to host memory. This property is used in conjunction with the niFgen Create Waveform From File VI and the niFgen Write Waveform From File VI.
- [Arbitrary Waveform:Data Transfer:Maximum Bandwidth](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumbandwidth.html) Specifies the maximum amount of bus bandwidth to use for data transfers.
- [Arbitrary Waveform:Data Transfer:Direct DMA:Direct DMA Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-directdmaenabled.html) Enables the device for Direct DMA writes.
- [Arbitrary Waveform:Data Transfer:Direct DMA:Window Address](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-directdmawindowaddress.html) Specifies the window address (beginning of window) of the waveform data source. This window address is specified by your Direct DMA-compatible data source.
- [Arbitrary Waveform:Data Transfer:Direct DMA:Window Size in Bytes](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-directdmawindowsize.html) Specifies the size of the memory window provided by your Direct DMA-compatible data source.
- [Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Handle](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-streamingwaveformhandle.html) Specifies the waveform handle of the waveform used to continuously stream data during generation.
- [Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Name](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-streamingwaveformname.html) Specifies the name of the waveform used to continuously stream data during generation. This property defaults to an empty string when no streaming waveform is specified.
- [Arbitrary Waveform:Data Transfer:Streaming:Space Available in Streaming Waveform](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-spaceavailinstreamingwfm.html) Returns the space available in the streaming waveform for writing new data.
- [Arbitrary Waveform:Data Transfer:Streaming:Streaming Write Timeout](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-streamingwritetimeout.html) Specifies the maximum amount of time allowed to complete a streaming write operation.
- [Arbitrary Waveform:Data Transfer:Advanced:Maximum In-Flight Read Requests](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumin-flightreadrequests.html) Specifies the maximum number of concurrent PCI Express read requests the signal generator can issue.
- [Arbitrary Waveform:Data Transfer:Advanced:PCI DMA Optimizations Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pcidmaoptimizationsenabled.html) Controls whether NI-FGEN allows performance optimizations for DMA transfers. This property is only valid for PCI and PXI SMC-based devices. This property is enabled (TRUE) by default, and NI recommends leaving it enabled.
- [Arbitrary Waveform:Data Transfer:Advanced:Preferred Packet Size](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-preferredpacketsize.html) Specifies the preferred size of the data field in a PCI Express read request packet.
- [Arbitrary Waveform:Onboard Signal Processing:OSP Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospenabled.html) Enables (TRUE) or disables (FALSE) the OSP block of the signal generator. When the OSP block is disabled, all OSP-related properties are disabled and have no effect on the generated signal.
- [Arbitrary Waveform:Onboard Signal Processing:IQ Rate](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-iqrate.html) Specifies the rate at which the user-provided waveform data is generated when the OSP Enabled property is set to TRUE.
- [Arbitrary Waveform:Onboard Signal Processing:Data Processing Mode](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-dataprocessingmode.html) Controls the way that data is processed by the OSP block.
- [Arbitrary Waveform:Onboard Signal Processing:OSP Mode](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospmode.html) Specifies the generation mode of the OSP, which determines the type of data contained in the output signal.
- [Arbitrary Waveform:Onboard Signal Processing:Carrier Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierenabled.html) Enables (TRUE) or disables (FALSE) generation of the carrier.
- [Arbitrary Waveform:Onboard Signal Processing:Carrier Frequency](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierfrequency.html) Specifies the frequency of the generated carrier.
- [Arbitrary Waveform:Onboard Signal Processing:Frequency Shift](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequencyshift.html) Specifies the amount of frequency shift applied to the baseband signal.
- [Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Filter Type](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-filtertype.html) Specifies the pulse-shaping filter type for the FIR filter.
- [Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Flat:Passband](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-flatfilterpassband.html) Specifies the passband value to use when calculating the FIR filter coefficients. The FIR filter is designed to be flat to passband × I/Q rate. This property is used only when the Filter Type property is set to Flat .
- [Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Raised Cosine:Alpha](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-raisedcosinefilteralpha.html) Specifies the alpha value to use when calculating the pulse-shaping FIR filter coefficients. This property is used only when the Filter Type property is set to Raised Cosine .
- [Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Root Raised Cosine:Alpha](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-rootraisedcosinefilteralpha.html) Specifies the alpha value to use when calculating the pulse-shaping FIR filter coefficients. This property is used only when the Filter Type property is set to Root Raised Cosine .
- [Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Gaussian:BT](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-gaussianfilterbt.html) Specifies the BT value to use when calculating the pulse-shaping FIR filter coefficients. The BT value is the product of the -3 dB bandwidth and the symbol period. This property is used only when the Filter Type property is set to Gaussian .
- [Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Carrier Phase:Carrier Phase I](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierphasei.html) Specifies the I carrier phase, in degrees, at the first point of the generated signal.
- [Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Carrier Phase:Carrier Phase Q](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierphaseq.html) Specifies the Q carrier phase, in degrees, at the first point of the generated signal. This property is used only when the Data Processing Mode property is set to Complex .
- [Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Gain:Pre-filter Gain I](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filtergaini.html) Specifies the digital gain to apply to the I data stream before any filtering by the OSP block.
- [Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Gain:Pre-filter Gain Q](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filtergainq.html) Specifies the digital gain to apply to the Q data stream before any filtering by the OSP block. This property is used only when the Data Processing Mode property is set to Complex .
- [Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Offset:Pre-filter Offset I](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filteroffseti.html) Specifies the digital offset to apply to the I data stream. This offset is applied after the prefilter gain and before any filtering.
- [Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Offset:Pre-filter Offset Q](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-filteroffsetq.html) Specifies the digital offset to apply to the Q data stream. This offset is applied after the prefilter gain and before any filtering. This property is only used when the Data Processing Mode property is set to Complex .
- [Arbitrary Waveform:Onboard Signal Processing:Advanced:FIR Filter Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-firfilterenabled.html) Specify TRUE to enables the FIR filter. Specify FALSE to disable the FIR filter.
- [Arbitrary Waveform:Onboard Signal Processing:Advanced:FIR Interpolation Factor](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-firinterpolation.html) Specifies the interpolation factor for the FIR filter. If you do not set this value, NI-FGEN calculates the appropriate value based on the value of the IQ Rate property.
- [Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Filter Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cicfilterenabled.html) Enables (TRUE) or disables (FALSE) the CIC filter.
- [Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Filter Gain](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cicfiltergain.html) Specifies the gain applied at the final stage of the CIC filter. This property is commonly used to compensate for attenuation in the FIR filter. If you set the FIR Filter Type to a value other than Custom , NI-FGEN calculates the CIC gain to achieve unity gain between the FIR and CIC filters. Setting this property overrides the value set by NI-FGEN.
- [Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Interpolation Factor](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cicinterpolation.html) Specifies the interpolation factor for the CIC filter. If you do not set this value, NI-FGEN calculates the appropriate value based on the value of the IQ Rate property.
- [Arbitrary Waveform:Onboard Signal Processing:Advanced:Compensate for Filter Group Delay](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-compensatefiltergroupdelay.html) Adjusts for OSP filter group delay when aligning analog outputs and events in OSP mode. If you set this property to TRUE, event outputs align more closely with the analog output. The analog output also aligns more closely between two devices synchronized using NI-TClk.
- [Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Error Reporting](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospoverflowerrorreporting.html) Configures error reporting when the OSP block detects an overflow in any of its stages. Overflows lead to waveform clipping.
- [Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Status](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-ospoverflowstatus.html) Returns a bit field of the overflow status in any stage of the OSP block. This property is functional regardless of the value for the OSP Overflow Error Reporting property.
- [Arbitrary Waveform:Peer-to-Peer:P2P Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-p2penabled.html) Specifies whether the signal generator reads data from the peer-to-peer endpoint (TRUE) instead of reading it from the onboard memory. This property is endpoint based .
- [Arbitrary Waveform:Peer-to-Peer:Destination Channels](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-destinationchannels.html) Specifies which channels are written to by a peer-to-peer endpoint. If multiple channels are specified, data is deinterleaved to each channel. Channels are configured using the niFgen Configure Channels VI. This property is endpoint based .
- [Arbitrary Waveform:Peer-to-Peer:Endpoint Size](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointsize.html) Returns the size, in samples per channel, of the peer-to-peer endpoint. This property is endpoint-based .
- [Arbitrary Waveform:Peer-to-Peer:Space Available In Endpoint](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-spaceavailableinendpoint.html) Returns the current space available in the endpoint in samples per channel. You can use this property when priming the endpoint with initial data through the niFgen Write P2P Endpoint I16 VI to determine how many samples you can write. You also can use this property to characterize the performance and measure the latency of the peer-to-peer stream as data moves across the bus. This property is endpoint-based .
- [Arbitrary Waveform:Peer-to-Peer:Most Space Available In Endpoint](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-mostspaceavailableinendpoint.html) Returns the largest number of samples per channel available in the endpoint since this property was last read. This property can be used to determine how much endpoint space to use as a buffer against PCI Express bus traffic latencies by reading the property and keeping track of the largest value returned. This property is endpoint-based .
- [Arbitrary Waveform:Peer-to-Peer:Endpoint Count](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointcount.html) Returns the number of peer-to-peer FIFO endpoints supported by the device.
- [Arbitrary Waveform:Peer-to-Peer:Data Transfer Permission Interval](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissioninterval.html) Specifies the interval, in samples per channel, at which the signal generator issues credits to allow the writer peer to transfer data over the bus into the configured endpoint. Refer to the Flow Control topic in the NI Signal Generators Help for more information. This property is coerced up by NI-FGEN to the nearest 128-byte boundary. This property is endpoint-based .
- [Arbitrary Waveform:Peer-to-Peer:Data Transfer Permission Initial Credits](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissioninitialcredits.html) Specifies the initial amount of data, in samples per channel, that the writer peer is allowed to transfer over the bus into the configured endpoint when the peer-to-peer data stream is enabled. If you do not set this property and the endpoint is empty, credits equal to the full size of the endpoint are issued to the writer peer. If data has been written to the endpoint using the niFgen Write P2P Endpoint I16 VI prior to enabling the stream, credits equal to the remaining space available in the endpoint are issued to the writer peer. This property is coerced up by NI-FGEN to 8-byte boundaries.
- [Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Manual Configuration Enabled](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-manualconfigurationenabled.html) Enables (TRUE) or disables (FALSE) manual configuration for a peer-to-peer endpoint. Enabling this property disables automatic NI-P2P stream manager flow control and Done Notifications.
- [Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Data Transfer Permission Address](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissionaddress.html) Indicates the address in the writer peer to which the signal generator sends data transfer permission credits. This property is endpoint-based .
- [Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Data Transfer Permission Address Type](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissionaddresstype.html) Specifies the type of address for the Data Transfer Permission Address property. This property is endpoint-based .
- [Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Endpoint Window Address](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointwindowaddress.html) Returns the signal generator address where endpoint data is sent by the writer peer. The type of this address is specified by the Endpoint Window Address Type property. This property is endpoint-based .
- [Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Endpoint Window Address Type](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointwindowaddresstype.html) Specifies the type of the Endpoint Window Address property. This property is endpoint-based .
- [Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Endpoint Window Size](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointwindowsize.html) Returns the size, in bytes, of the endpoint window. The endpoint window is also described by the Endpoint Window Address property and the Endpoint Window Address Type property. This property is endpoint-based .
- [Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Notification:Done Notification Address](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-donenotificationaddress.html) Returns the signal generator address to which the writer peer sends the Done Notification Value . This property is endpoint-based . Refer to the Stopping a Peer-to-Peer Generation topic in the NI Signal Generators Help for more information about using Done Notifications.
- [Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Notification:Done Notification Address Type](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-donenotificationaddresstype.html) Specifies the address type of the Done Notification Address property. This property is endpoint-based . Refer to the Stopping a Peer-to-Peer Generation topic in the NI Signal Generators Help for more information about using Done Notifications.
- [Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Notification:Done Notification Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-donenotificationvalue.html) Returns the value the writer peer writes to the address specified by the Done Notification Address property. This property is endpoint-based . Refer to the Stopping a Peer-to-Peer Generation topic in the NI Signal Generators Help for more information about using Done Notifications.
- [Standard Function:Waveform](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-waveform.html) Specifies which standard waveform the signal generator produces. Use this property only when the Output Mode property is set to NIFGEN_VAL_OUTPUT_FUNC .
- [Standard Function:Amplitude](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-amplitude.html) Controls the amplitude of the standard waveform that the signal generator produces. This value is the amplitude at the output terminal.
- [Standard Function:DC Offset](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-dcoffset.html) Controls the DC offset of the standard waveform that the signal generator produces.
- [Standard Function:Start Phase](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startphase.html) Controls horizontal offset of the standard waveform the signal generator produces. Specify this property in degrees of one waveform cycle.
- [Standard Function:Duty Cycle High](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-dutycyclehigh.html) Specifies the duty cycle of the square wave the signal generator is producing. Specify this property as a percentage of the time the square wave is high in a cycle.
- [Standard Function:Sync Duty Cycle High](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-syncdutycyclehigh.html) Specifies the duty cycle of the square wave the signal generator produces on the SYNC OUT connector. Specify this property as a percentage of the time the square wave is high in each cycle.
- [Standard Function:Sync Out Output Terminal](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-syncoutoutputterminal.html) Specifies the terminal at which to export the SYNC OUT signal. This property is not supported for all devices. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX.
- [Standard Function:Standard Function Mode:Frequency](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequency.html) Controls the frequency of the standard waveform that the signal generator produces.
- [Standard Function:Standard Function Mode:Buffer Size](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-buffersize.html) Contains the number of samples used in the standard function waveform buffer.
- [Standard Function:Standard Function Mode:Maximum Buffer Size](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumbuffersize.html) Sets the maximum number of samples that can be used in the standard function waveform buffer. Increasing this value may increase the quality of the waveform but may also increase the amount of time required to change the waveform while running.
- [Standard Function:Frequency List Mode:Frequency List Handle](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequencylisthandle.html) Sets which frequency list the signal generator produces. You create a frequency list using the niFgen Create Frequency List VI. The niFgen Create Frequency List VI returns a handle that you use to identify the list.
- [Standard Function:Frequency List Mode:Maximum Number Of Frequency Lists](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumnumberoffrequencylists.html) Returns the maximum number of frequency lists that the signal generator allows.
- [Standard Function:Frequency List Mode:Maximum Frequency List Length](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumfrequencylistlength.html) Returns the maximum number of steps that can be in a frequency list.
- [Standard Function:Frequency List Mode:Minimum Frequency List Length](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minimumfrequencylistlength.html) Returns the minimum number of frequency lists that the signal generator allows.
- [Standard Function:Frequency List Mode:Frequency List Duration Quantum](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-frequencylistdurationquantum.html) Returns the quantum that all durations must be a multiple of in a frequency list.
- [Standard Function:Frequency List Mode:Maximum Frequency List Duration](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-maximumfrequencylistduration.html) Returns the maximum duration, in seconds, of any one step in the frequency list.
- [Standard Function:Frequency List Mode:Minimum Frequency List Duration](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minimumfrequencylistduration.html) Returns the minimum duration, in seconds, of any one step in a frequency list.
- [Clocks:Reference Clock:Source](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-referenceclocksource.html) Specifies the Reference Clock source used by the signal generator.
- [Clocks:Reference Clock:Frequency](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-referenceclockfrequency.html) Specifies the Reference Clock frequency. The signal generator uses the Reference Clock to derive frequencies and sample rates when generating output.
- [Clocks:Reference Clock:Export Output Terminal](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedreferenceclockoutputterminal.html) Specifies the terminal at which to export the Reference Clock.
- [Clocks:Reference Clock:Onboard Reference Clock:Export Output Terminal](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedonboardreferenceclockoutputterminal.html) Specifies the terminal at which to export the onboard Reference Clock.
- [Clocks:Sample Clock:Rate](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-samplerate.html) Specifies the rate, in samples per second, at which the signal generator generates the points in arbitrary waveforms.
- [Clocks:Sample Clock:Mode](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-clockmode.html) Specifies the Sample Clock mode for the signal generator.
- [Clocks:Sample Clock:Source](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclocksource.html) Specifies the Sample Clock source.
- [Clocks:Sample Clock:Export Output Terminal](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclockoutputterminal.html) Specifies the terminal at which to export the Sample Clock. If you specify a divisor with the Exported Sample Clock Divisor property, the Sample Clock exported with this property is the value of the Sample Clock after it is divided-down.
- [Clocks:Sample Clock:Exported Sample Clock Divisor](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclockdivisor.html) Specifies the factor by which to divide the update (Sample) Clock before it is exported.
- [Clocks:Sample Clock Timebase:Rate](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclocktimebaserate.html) Specifies the Sample Clock Timebase rate. This property applies only to external Sample Clock timebases.
- [Clocks:Sample Clock Timebase:Source](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclocktimebasesource.html) Specifies the Sample Clock Timebase source.
- [Clocks:Sample Clock Timebase:Export Output Terminal](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclocktimebaseoutputterminal.html) Specifies the terminal at which to export the Sample Clock Timebase.
- [Clocks:Sample Clock Timebase:Exported Sample Clock Timebase Divisor](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedsampleclocktimebasedivisor.html) Specifies the factor by which to divide the device clock (Sample Clock timebase) before it is exported.
- [Clocks:Advanced:External Sample Clock Multiplier](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-externalsampleclockmultiplier.html) Specifies a multiplication factor to use to obtain a desired sample rate from an external Sample Clock.
- [Clocks:Advanced:Sample Clock Absolute Delay](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-sampleclockabsolutedelay.html) Specifies the delay in seconds to apply to an external Sample Clock. This property is useful when trying to align the output of two devices.
- [Clocks:Advanced:External Clock Delay Binary Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-externalclockdelaybinaryvalue.html) Specifies the external clock delay binary value.
- [Clocks:Advanced:Oscillator Phase DAC Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-oscillatorphasedacvalue.html) Specifies the oscillator phase DAC value.
- [Events:Marker:Output Terminal](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventoutputterminal.html) Specifies the destination terminal for the Marker Event.
- [Events:Marker:Output Behavior](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventoutputbehavior.html) Specifies the output behavior for the Marker Event.
- [Events:Marker:Pulse:Polarity](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventpulsepolarity.html) Specifies the output polarity of the Marker Event.
- [Events:Marker:Pulse:Width Units](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventpulsewidthunits.html) Specifies the pulse width units of the Marker Event.
- [Events:Marker:Pulse:Width Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventpulsewidthvalue.html) Specifies the pulse width value of the Marker Event. Set the units for the values with the Marker Event Pulse Width Units property.
- [Events:Marker:Toggle:Initial State](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventtoggleinitialstate.html) Specifies the initial state of the Marker Event.
- [Events:Marker:Advanced:Delay Units](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventdelayunits.html) Specifies the units used for the Marker Event Delay Value property.
- [Events:Marker:Advanced:Delay Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventdelayvalue.html) Specifies the amount of delay applied to a Marker Event with respect to the analog output of the signal generator.
- [Events:Marker:Advanced:Latched Status](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventlatchedstatus.html) Specifies the latched status of the specified Marker Event. Set this property to FALSE to clear the latched status of the Marker Event.
- [Events:Marker:Advanced:All Marker Events Latched Status](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-allmarkereventslatchedstatus.html) Returns a bit field of the latched status of all Marker Events. Set this property to 0 to clear the latched status of all Marker Events.
- [Events:Marker:Advanced:Live Status](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markereventlivestatus.html) Returns TRUE if the status of the specified Marker Event is live, and FALSE otherwise.
- [Events:Marker:Advanced:All Marker Events Live Status](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-allmarkereventslivestatus.html) Returns a bit field of the live status of all Marker Events.
- [Events:Data Marker:Output Terminal](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkereventoutputterminal.html) Specifies the destination terminal for the Data Marker Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX.
- [Events:Data Marker:Data Bit Number](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkereventbitnumber.html) Specifies the bit number to assign to the Data Marker Event.
- [Events:Data Marker:Level:Active Level](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkereventlevelpolarity.html) Specifies the output polarity of the Data Marker Event. Refer to Data Marker Events topic for more information about Data Marker Event polarity.
- [Events:Ready For Start:Output Terminal](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-readyforstarteventoutputterminal.html) Specifies the destination terminal for the Ready for Start Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX.
- [Events:Ready For Start:Level:Active Level](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-readyforstarteventactivelevel.html) Specifies the output polarity of the Ready for Start Event.
- [Events:Ready For Start:Advanced:Live Status](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-readyforstarteventlivestatus.html) Returns TRUE if the status of the specified Ready for Start Event is live, and FALSE otherwise.
- [Events:Started:Output Terminal](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventoutputterminal.html) Specifies the destination terminal for the Started Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX.
- [Events:Started:Output Behavior](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventoutputbehavior.html) Specifies the output behavior for the Started Event.
- [Events:Started:Pulse:Polarity](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventpulsepolarity.html) Specifies the output polarity of the Started Event.
- [Events:Started:Pulse:Width Units](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventpulsewidthunits.html) Specifies the pulse width units for the Started Event.
- [Events:Started:Pulse:Width Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventpulsewidthvalue.html) Specifies the pulse width value for the Started Event.
- [Events:Started:Level:Active Level](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventactivelevel.html) Specifies the output polarity of the Started Event.
- [Events:Started:Advanced:Delay Units](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventdelayunits.html) Specifies the units used for the Started Event Delay Value property.
- [Events:Started:Advanced:Delay Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventdelayvalue.html) Specifies the amount of delay applied to a Started Event with respect to the analog output of the signal generator.
- [Events:Started:Advanced:Latched Status](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-startedeventlatchedstatus.html) Returns the latched status of the specified Started Event.
- [Events:Done:Output Terminal](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventoutputterminal.html) Specifies the destination terminal for the Done Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX.
- [Events:Done:Output Behavior](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventoutputbehavior.html) Specifies the output behavior for the Done Event.
- [Events:Done:Pulse:Polarity](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventpulsepolarity.html) Specifies the output polarity of the Done Event.
- [Events:Done:Pulse:Width Units](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventpulsewidthunits.html) Specifies the pulse width units for the Done Event.
- [Events:Done:Pulse:Width Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventpulsewidthvalue.html) Specifies the pulse width for the Done Event.
- [Events:Done:Level:Active Level](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventactivelevel.html) Specifies the output polarity of the Done Event.
- [Events:Done:Advanced:Delay Units](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventdelayunits.html) Specifies the units used for the Done Event Delay Value property.
- [Events:Done:Advanced:Delay Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventdelayvalue.html) Specifies the amount of delay applied to a Done Event with respect to the analog output of the signal generator.
- [Events:Done:Advanced:Latched Status](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventlatchedstatus.html) Returns the latched status of the specified Done Event.
- [Triggers:Trigger Mode](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-triggermode.html) Controls the trigger mode.
- [Triggers:Start:Trigger Type](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-starttriggertype.html) Specifies the type of Start Trigger you want to use.
- [Triggers:Start:Output Terminal](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedstarttriggeroutputterminal.html) Specifies the destination terminal for exporting the Start Trigger.
- [Triggers:Start:Digital Edge:Source](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-starttriggerdigitaledge-source.html) Specifies the source terminal for the Start Trigger. This property is used only when the Start Trigger Type property is set to Digital Edge .
- [Triggers:Start:Digital Edge:Edge](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-starttriggerdigitaledge-edge.html) Specifies the active edge for the Start Trigger. This property is used only when the Start Trigger Type property is set to Digital Edge .
- [Triggers:Start:P2P Endpoint Fullness:Level](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-p2pendpointfullnessstarttriggerlevel.html) Specifies the number of samples the endpoint needs to receive before the signal generator starts generation. This property applies only when the Start Trigger Type property is set to P2P Endpoint Fullness . Refer to the Flow Control topic in the NI Signal Generators Help for more information about peer-to-peer operations. This property is coerced down to 8-byte boundaries.
- [Triggers:Script:Trigger Type](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggertype.html) Specifies the Script trigger type. Depending upon the value of this property, additional properties may be needed to fully configure the trigger.
- [Triggers:Script:Output Terminal](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-exportedscripttriggeroutputterminal.html) Specifies the output terminal for the exported Script Trigger.
- [Triggers:Script:Digital Edge:Source](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitaledge-source.html) Specifies the source terminal for the Script Trigger. This property is used when the Script Trigger Type property is set to Digital Edge .
- [Triggers:Script:Digital Edge:Edge](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitaledge-edge.html) Specifies the active edge for the Script Trigger. This property is used when the Script Trigger Type property is set to Digital Edge .
- [Triggers:Script:Digital Level:Source](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitallevel-source.html) Specifies the source terminal for the Script Trigger. This property is used when the Script Trigger Type property is set to Digital Level .
- [Triggers:Script:Digital Level:Active Level](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerdigitallevel-activelevel.html) Specifies the active level for the Script Trigger. This property is used when the Script Trigger Type property is set to Digital Level .
- [Instrument:Bus Type](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-bustype.html) Returns the bus type of the signal generator.
- [Instrument:Memory Size](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-memorysize.html) Returns the amount of memory in bytes on the signal generator.
- [Instrument:Serial Number](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-serialnumber.html) Returns the serial number of the signal generator.
- [Instrument:Marker Events Count](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-markerscount.html) Returns the number of markers supported by the device. Use this property when the Output Mode property is set to NIFGEN_VAL_OUTPUT_SCRIPT .
- [Instrument:Data Marker Events Count](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkerscount.html) Returns the number of Data Marker Events supported by the device.
- [Instrument:Script Triggers Count](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-scripttriggerscount.html) Returns the number of Script Triggers supported by the device. Use this property when the Output Mode property is set to NIFGEN_VAL_OUTPUT_SCRIPT .
- [Instrument:FPGA Bitfile Path](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-fpgabitfilepath.html) Gets the absolute file path to the bitfile loaded on the FPGA.
- [Instrument:Calibration:Cal ADC Input](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-caladcinput.html) Specifies the input of the calibration ADC. The ADC can take a reading from several inputs: the analog output, a 2.5 V reference, and ground. The latter two inputs are used to calibrate the ADC itself.
- [Instrument:Calibration:Gain DAC Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-gaindacvalue.html) Specifies the value programmed to the Gain DAC. The value should be treated as an unsigned, right-justified number.
- [Instrument:Calibration:Offset DAC Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-offsetdacvalue.html) Specifies the value programmed to the Offset DAC. The value should be treated as an unsigned, right-justified number.
- [Instrument:Calibration:Oscillator Freq DAC Value](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-oscillatorfreqdacvalue.html) Specifies the value programmed to the Oscillator DAC. The value should be treated as an unsigned, right-justified number.
- [Instrument:Calibration:Pre-Amplifier Attenuation](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-pre-amplifierattenuation.html) Specifies the amount of preamplifier attenuation to apply to the signal, in dB.
- [Instrument:Calibration:Post-Amplifier Attenuation](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-post-amplifierattenuation.html) Specifies the amount of post-amplifier attenuation to apply to the signal, in dB.
- [Instrument:Inherent IVI Attributes:User Options:Range Check](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-rangecheck.html) Specifies whether to validate property values and VI parameters. Set this property to TRUE to enable range-checking.
- [Instrument:Inherent IVI Attributes:User Options:Query Instrument Status](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-queryinstrumentstatus.html) Specifies whether NI-FGEN retains instrument status after each operation. Set this property to TRUE to query the instrument status.
- [Instrument:Inherent IVI Attributes:User Options:Cache](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cache.html) Specifies whether to cache the value of properties.
- [Instrument:Inherent IVI Attributes:User Options:Simulate](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-simulate.html) Specifies whether or not to simulate NI-FGEN I/O operations. Set this property to TRUE to enable simulation.
- [Instrument:Inherent IVI Attributes:User Options:Record Value Coercions](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-recordvaluecoercions.html) Specifies whether the IVI engine keeps a list of the value coercions it makes for ViInt32 and ViReal64 properties. Set this property to TRUE to record the coercions. Use the niFgen Initialize With Options VI to override this value.
- [Instrument:Inherent IVI Attributes:User Options:Interchange Check](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-interchangecheck.html) Specifies whether to perform interchangeability checking and log interchangeability warnings when you call VIs. Set this property to TRUE to enable interchangeability checking.
- [Instrument:Inherent IVI Attributes:Driver Identification:Description](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-description.html) Contains a brief description of the specific driver.
- [Instrument:Inherent IVI Attributes:Driver Identification:Driver Prefix](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-driverprefix.html) Contains the prefix for NI-FGEN. The name of each user-callable VI in NI-FGEN starts with this prefix.
- [Instrument:Inherent IVI Attributes:Driver Identification:Driver Vendor](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-drivervendor.html) Contains the name of the vendor that supplies NI-FGEN.
- [Instrument:Inherent IVI Attributes:Driver Identification:Revision](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-revision.html) Contains additional version information about NI-FGEN.
- [Instrument:Inherent IVI Attributes:Driver Identification:Class Specification Major Version](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-classspecificationmajorversion.html) Returns the major version number of the class specification with which NI-FGEN is compliant.
- [Instrument:Inherent IVI Attributes:Driver Identification:Class Specification Minor Version](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-classspecificationminorversion.html) Returns the minor version number of the class specification with which NI-FGEN is compliant.
- [Instrument:Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-supportedinstrumentmodels.html) Returns a model code of the instrument. For drivers that support more than one device, this property contains a comma-separated list of supported instrument models.
- [Instrument:Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-classgroupcapabilities.html) Returns a comma-separated list of class-extension groups that NI-FGEN implements.
- [Instrument:Inherent IVI Attributes:Driver Capabilities:Channel Count](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-channelcount.html) Returns the number of channels that NI-FGEN supports. For each property for which IVI_VAL_MULTI_CHANNEL is set, the IVI engine maintains a separate cache value for each channel.
- [Instrument:Inherent IVI Attributes:Instrument Identification:Manufacturer](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-manufacturer.html) Returns the name of the instrument manufacturer you are currently using.
- [Instrument:Inherent IVI Attributes:Instrument Identification:Model](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-model.html) Returns the model number or name of the instrument that you are currently using.
- [Instrument:Inherent IVI Attributes:Instrument Identification:Firmware Revision](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-firmwarerevision.html) Returns the firmware revision information for the instrument you are currently using.
- [Instrument:Inherent IVI Attributes:Instrument Identification:Module Revision](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-modulerevision.html) Returns the revision letter of the module you are using.
- [Instrument:Inherent IVI Attributes:Advanced Session Information:Logical Name](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-logicalname.html) Returns the logical name you specified when opening the current IVI session.
- [Instrument:Inherent IVI Attributes:Advanced Session Information:Resource Descriptor](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-resourcedescriptor.html) Returns the resource descriptor NI-FGEN uses to identify the physical device.
- [Instrument:5401/5411/5431:Filter Correction Frequency](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-filtercorrectionfrequency.html) Specifies the filter correction frequency of the analog filter. This property can correct for the ripples in the analog filter frequency response at the frequency specified.
- [Instrument:5401/5411/5431:Trigger Source](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-triggersource.html) Specifies which trigger source the signal generator uses.
- [Instrument:5401/5411/5431:Synchronization Source](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-synchronizationsource.html) Specifies the source of the synchronization signal to use.
- [Instrument:5401/5411/5431:Video Waveform Type](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-videowaveformtype.html) Specifies the waveform type the NI 5431 generates. Setting this property ensures the oscillator crystal is set to the proper frequency.
- [Instrument:Obsolete:Major Version](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-majorversion.html) Returns the major version number of NI-FGEN.
- [Instrument:Obsolete:Minor Version](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-minorversion.html) Returns the minor version number of NI-FGEN.
- [Instrument:Obsolete:Error Elaboration](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-errorelaboration.html) Contains an optional string with additional information concerning the primary error condition.
- [Instrument:Obsolete:Primary Error](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-primaryerror.html) Describes the first error that occurred since the last call to the niFgen Error Message VI on the session.
- [Instrument:Obsolete:Secondary Error](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-secondaryerror.html) Provides an optional code with additional information concerning the primary error condition. The error and warning values can be status codes defined by IVI, VISA, class drivers, or specific drivers. Zero indicates no additional information.
- [Instrument:Obsolete:Operation Mode](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-operationmode.html) Specifies how the signal generator produces waveforms. NI signal generators currently support only one value: NIFGEN_VAL_OPERATE_CONTINUOUS . To control trigger mode, set the Trigger Mode property.
- [Instrument:Obsolete:Ref Clock Source](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-refclocksource.html) Controls the Reference Clock source the signal generator uses.
- [Instrument:Obsolete:Update Clock Source](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-updateclocksource.html) Controls the Update Clock source.
- [Instrument:Obsolete:Actual Arb Sample Rate](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-actualarbsamplerate.html) Returns the actual sample rate value of the signal generator after any coercion or rounding.
- [Instrument:Obsolete:DAQmx Task](../../../instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-daqmxtask.html) Returns the NI-DAQmx task pointer.

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-absolutedelay.html language=enus -->
## TOPIC 00172: Output:Absolute Delay

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-absolutedelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-absolutedelay.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sub-Sample Clock delay, in seconds, to apply to the waveform. Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing the absolute delay value of a previous measuremen

### Output:Absolute Delay

Specifies the sub-Sample Clock delay, in seconds, to apply to the waveform. Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurement to the current session.

To set this property, the waveform generator must be in the Idle (Configuration) state.

Note

**Units**: seconds (s)

**Valid Values**: Plus or minus half of one Sample Clock period

**Default Value**: 0.0

**Supported Waveform Generators**: PXIe-5413/5423/5433

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Absolute Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-activechannel.html language=enus -->
## TOPIC 00173: Active Channel

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-activechannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-activechannel.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel used to access all subsequent channel-based properties. You must set this property before setting any channel-based properties. Pass a name that the instrument driver defines or a virtual channel name defined in MAX. Remarks The following table lists the characteristics of this

### Active Channel

Specifies the channel used to access all subsequent channel-based properties. You must set this property before setting any channel-based properties. Pass a name that the instrument driver defines or a virtual channel name defined in MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Channel |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-actualarbsamplerate.html language=enus -->
## TOPIC 00174: Instrument:Obsolete:Actual Arb Sample Rate

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-actualarbsamplerate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-actualarbsamplerate.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the actual sample rate value of the signal generator after any coercion or rounding. Remarks The following table lists the characteristics of this property. Short Name Actual Arb Sample Rate Data type cdbl.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Obsolete:Actual Arb Sample Rate

Returns the actual sample rate value of the signal generator after any coercion or rounding.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Actual Arb Sample Rate |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-allmarkereventslatchedstatus.html language=enus -->
## TOPIC 00175: Events:Marker:Advanced:All Marker Events Latched Status

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-allmarkereventslatchedstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-allmarkereventslatchedstatus.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a bit field of the latched status of all Marker Events. Set this property to 0 to clear the latched status of all Marker Events. Remarks The following table lists the characteristics of this property. Short Name All Marker Events Latched Status Data type ci32.png Permissions Read/Write High-

### Events:Marker:Advanced:All Marker Events Latched Status

Returns a bit field of the latched status of all Marker Events. Set this property to 0 to clear the latched status of all Marker Events.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | All Marker Events Latched Status |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-allmarkereventslivestatus.html language=enus -->
## TOPIC 00176: Events:Marker:Advanced:All Marker Events Live Status

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-allmarkereventslivestatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-allmarkereventslivestatus.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a bit field of the live status of all Marker Events. Remarks The following table lists the characteristics of this property. Short Name All Marker Events Live Status Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Events:Marker:Advanced:All Marker Events Live Status

Returns a bit field of the live status of all Marker Events.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | All Marker Events Live Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-amplitude.html language=enus -->
## TOPIC 00177: Standard Function:Amplitude

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-amplitude.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-amplitude.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the amplitude of the standard waveform that the signal generator produces. This value is the amplitude at the output terminal. For example, to produce a waveform ranging from -5.00 V to +5.00 V, set Amplitude property to 10.00 V. Units: volts peak-to-peak (V[pk-pk]) Default Value: None This

### Standard Function:Amplitude

Controls the amplitude of the standard waveform that the signal generator produces. This value is the amplitude at the output terminal.

For example, to produce a waveform ranging from -5.00 V to +5.00 V, set Amplitude property to 10.00 V.

**Units**: volts peak-to-peak (V<sub>pk-pk</sub>)

**Default Value**: None

Note

Waveform

NIFGEN_VAL_WFM_DC

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Amplitude |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Frequency List, niFgen Configure Standard Waveform |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogdatamask.html language=enus -->
## TOPIC 00178: Output:Data Mask:Analog Data Mask

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogdatamask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogdatamask.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mask to apply to the analog output data. The masked data is replaced with the data in the Analog Static Value property. Remarks The following table lists the characteristics of this property. Short Name Analog Data Mask Data type ci32.png Permissions Read/Write High-level VIs N/A Chann

### Output:Data Mask:Analog Data Mask

Specifies the mask to apply to the analog output data. The masked data is replaced with the data in the [Analog Static Value](/csh?topicname=pnifgen-analogstaticvalue.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Analog Data Mask |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogfilterenabled.html language=enus -->
## TOPIC 00179: Output:Filters:Analog Filter Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogfilterenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal generator applies an analog filter to the output signal. Set this property to TRUE to enable the filter. This property is valid in Arbitrary Waveform, Arbitrary Sequence, and Script output modes. You also can use this property in Standard Function and Frequency List outp

### Output:Filters:Analog Filter Enabled

Specifies whether the signal generator applies an analog filter to the output signal. Set this property to TRUE to enable the filter. This property is valid in Arbitrary Waveform, Arbitrary Sequence, and Script output modes. You also can use this property in Standard Function and Frequency List output modes for user-defined waveforms.

**Default Value**: FALSE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Analog Filter Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Analog Filter |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogpath.html language=enus -->
## TOPIC 00180: Output:Analog Path

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogpath.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogpath.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the analog signal path. The main path allows the user to configure gain, offset, analog filter status, output impedance, and output enable. The direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The direct path provides a smaller output range

### Output:Analog Path

Specifies the analog signal path. The main path allows the user to configure gain, offset, analog filter status, output impedance, and output enable.

The direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The direct path provides a smaller output range but lower distortion. The main path has two amplifier options, high and low gain. Setting this value to **NIFGEN_VAL_MAIN_ANALOG_PATH** allows NI-FGEN to choose the amplifier based on the user-specified gain.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Analog Path |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| NIFGEN_VAL_MAIN_ANALOG_PATH | 0 | Specifies the main path. |
| --- | --- | --- |
| NIFGEN_VAL_DIRECT_ANALOG_PATH | 1 | Specifies the direct path. |
| NIFGEN_VAL_FIXED_LOW_GAIN_ANALOG_PATH | 2 | Specifies the main path with low gain amplifier. |
| NIFGEN_VAL_FIXED_HIGH_GAIN_ANALOG_PATH | 3 | Specifies the main path with high gain amplifier. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogstaticvalue.html language=enus -->
## TOPIC 00181: Output:Data Mask:Analog Static Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogstaticvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-analogstaticvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the static value that replaces data masked by the Analog Data Mask property. Remarks The following table lists the characteristics of this property. Short Name Analog Static Value Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes

### Output:Data Mask:Analog Static Value

Specifies the static value that replaces data masked by the [Analog Data Mask](/csh?topicname=pnifgen-analogdatamask.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Analog Static Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarysequencehandle.html language=enus -->
## TOPIC 00182: Arbitrary Waveform:Arbitrary Sequence Mode:Arbitrary Sequence Handle

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarysequencehandle.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarysequencehandle.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects which sequence the signal generator produces. You can create multiple sequences using the niFgen Create Arbitrary Sequence VI. The niFgen Create Arbitrary Sequence VI returns a Sequence Handle that you use to identify the particular sequence. To configure the signal generator to produce a pa

### Arbitrary Waveform:Arbitrary Sequence Mode:Arbitrary Sequence Handle

Selects which sequence the signal generator produces. You can create multiple sequences using the [niFgen Create Arbitrary Sequence](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI.

The niFgen Create Arbitrary Sequence VI returns a **Sequence Handle** that you use to identify the particular sequence. To configure the signal generator to produce a particular sequence, set this property to the **Sequence Handle** value. Use this property when the [Output Mode](pnifgen-outputmode.html) property is set to **NIFGEN_VAL_OUTPUT_SEQ**.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Arbitrary Sequence Handle |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Arbitrary Sequence |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarywaveformgain.html language=enus -->
## TOPIC 00183: Arbitrary Waveform:Gain

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarywaveformgain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarywaveformgain.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to scale the arbitrary waveform to other ranges. For example, when you set this property t

### Arbitrary Waveform:Gain

Specifies the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to scale the arbitrary waveform to other ranges.

For example, when you set this property to 2.0, the output signal ranges from -2.0 V to +2.0 V.

Use this property when the [Output Mode](pnifgen-outputmode.html) property is set to **NIFGEN_VAL_OUTPUT_ARB** or **NIFGEN_VAL_OUTPUT_SEQ**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Gain |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Arbitrary Sequence, niFgen Configure Arbitrary Waveform |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarywaveformhandle.html language=enus -->
## TOPIC 00184: Arbitrary Waveform:Arbitrary Waveform Mode:Arbitrary Waveform Handle

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarywaveformhandle.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarywaveformhandle.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects which arbitrary waveform the signal generator produces. You can create multiple arbitrary waveforms using the niFgen Create Waveform VI. The niFgen Create Waveform VI, niFgen Allocate Waveform VI, and similar VIs return a Waveform Handle that you use to identify the particular waveform. To c

### Arbitrary Waveform:Arbitrary Waveform Mode:Arbitrary Waveform Handle

Selects which arbitrary waveform the signal generator produces. You can create multiple arbitrary waveforms using the [niFgen Create Waveform](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI.

The [niFgen Create Waveform](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI, [niFgen Allocate Waveform](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI, and similar VIs return a **Waveform Handle** that you use to identify the particular waveform. To configure the signal generator to produce a particular waveform, set this property to the **Waveform Handle** value.

Use this property only when the [Output Mode](pnifgen-outputmode.html) property is set to **NIFGEN_VAL_OUTPUT_ARB**.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Arbitrary Waveform Handle |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Arbitrary Waveform |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarywaveformoffset.html language=enus -->
## TOPIC 00185: Arbitrary Waveform:Offset

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarywaveformoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbitrarywaveformoffset.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to shift the arbitrary waveform range. For example, when you set this property to 1.0, the output s

### Arbitrary Waveform:Offset

Specifies the value the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to shift the arbitrary waveform range.

For example, when you set this property to 1.0, the output signal ranges from 0.0 V to 2.0 V.

Use this property when the [Output Mode](pnifgen-outputmode.html) property is set to **NIFGEN_VAL_OUTPUT_ARB** or **NIFGEN_VAL_OUTPUT_SEQ**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Arbitrary Sequence, niFgen Configure Arbitrary Waveform |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbwfm-markerpos.html language=enus -->
## TOPIC 00186: Arbitrary Waveform:Arbitrary Waveform Mode:Marker Position

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbwfm-markerpos.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbwfm-markerpos.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the position for a marker to be asserted in the arbitrary waveform. Use this property when the Output Mode property is set to NIFGEN_VAL_OUTPUT_ARB. Use the niFgen Export Signal VI to export the marker signal. Default Value: -1 Remarks The following table lists the characteristics of this

### Arbitrary Waveform:Arbitrary Waveform Mode:Marker Position

Specifies the position for a marker to be asserted in the arbitrary waveform.

Use this property when the [Output Mode](pnifgen-outputmode.html) property is set to **NIFGEN_VAL_OUTPUT_ARB**. Use the [niFgen Export Signal](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI to export the marker signal.

**Default Value**: -1

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Marker Position |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbwfm-repeatcount.html language=enus -->
## TOPIC 00187: Arbitrary Waveform:Arbitrary Waveform Mode:Repeat Count

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbwfm-repeatcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-arbwfm-repeatcount.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of times to repeat the arbitrary waveform when the Trigger Mode parameter in the niFgen Configure Trigger Mode VI is set to Single or Stepped. This property is ignored if the Trigger Mode parameter is set to Continuous or Burst. Use this property when the Output Mode property is

### Arbitrary Waveform:Arbitrary Waveform Mode:Repeat Count

Specifies the number of times to repeat the arbitrary waveform when the **Trigger Mode** parameter in the [niFgen Configure Trigger Mode](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI is set to **Single** or **Stepped**.

This property is ignored if the **Trigger Mode** parameter is set to **Continuous** or **Burst**. Use this property when the [Output Mode](pnifgen-outputmode.html) property is set to **NIFGEN_VAL_OUTPUT_ARB**.

When used during [streaming](/csh?context=nifgen_siggenhelp_streaming) operations, this property specifies the number of times to repeat the streaming waveform (the onboard memory allocated for streaming).

**Default Value**: 1

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Repeat Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-auxpowerenabled.html language=enus -->
## TOPIC 00188: Output:Advanced:AUX Power Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-auxpowerenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-auxpowerenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the specified auxiliary power pin. Setting this property to TRUE energizes the auxiliary power when the session is committed. When this property is FALSE, the power pin of the connector outputs no power. Default Value: FALSE Remarks The following table lists the characteristics of this prop

### Output:Advanced:AUX Power Enabled

Controls the specified auxiliary power pin. Setting this property to TRUE energizes the auxiliary power when the session is committed. When this property is FALSE, the power pin of the connector outputs no power.

**Default Value**: FALSE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AUX Power Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-buffersize.html language=enus -->
## TOPIC 00189: Standard Function:Standard Function Mode:Buffer Size

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-buffersize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-buffersize.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the number of samples used in the standard function waveform buffer. This property is valid only on devices that implement Standard Function output mode in software, and it is read-only for all other devices. Refer to the Standard Function Mode topic in the NI Signal Generators Help for mor

### Standard Function:Standard Function Mode:Buffer Size

Contains the number of samples used in the standard function waveform buffer.

This property is valid only on devices that implement Standard Function output mode in software, and it is read-only for all other devices.

Note

Standard Function Mode

NI Signal Generators Help

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Buffer Size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-bustype.html language=enus -->
## TOPIC 00190: Instrument:Bus Type

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-bustype.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-bustype.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bus type of the signal generator. Remarks The following table lists the characteristics of this property. Short Name Bus Type Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No NIFGEN_VAL_BUS_INVALID 0 Indicates an invalid bus type. NIFGEN_VAL_BUS_

### Instrument:Bus Type

Returns the bus type of the signal generator.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Bus Type |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

| NIFGEN_VAL_BUS_INVALID | 0 | Indicates an invalid bus type. |
| --- | --- | --- |
| NIFGEN_VAL_BUS_AT | 1 | Indicates the signal generator is the AT bus type. |
| NIFGEN_VAL_BUS_PCI | 2 | Indicates the signal generator is the PCI bus type. |
| NIFGEN_VAL_BUS_PXI | 3 | Indicates the signal generator is the PXI bus type. |
| NIFGEN_VAL_BUS_VXI | 4 | Indicates the signal generator is the VXI bus type. |
| NIFGEN_VAL_BUS_PCMCIA | 5 | Indicates the signal generator is the PCMCIA bus type. |
| NIFGEN_VAL_BUS_PXIE | 6 | Indicates the signal generator is the PXI Express bus type. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cache.html language=enus -->
## TOPIC 00191: Instrument:Inherent IVI Attributes:User Options:Cache

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cache.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cache.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to cache the value of properties. When caching is enabled (TRUE), NI-FGEN keeps track of the current instrument settings and avoids sending redundant commands to the instrument. Thus, you can significantly increase execution speed. NI-FGEN can choose always to cache or never to cac

### Instrument:Inherent IVI Attributes:User Options:Cache

Specifies whether to cache the value of properties.

When caching is enabled (TRUE), NI-FGEN keeps track of the current instrument settings and avoids sending redundant commands to the instrument. Thus, you can significantly increase execution speed. NI-FGEN can choose always to cache or never to cache particular properties regardless of the setting of this property. Use the [niFgen Initialize With Options](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI to override this value.

**Default Value**: TRUE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cache |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Initialize With Options |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-caladcinput.html language=enus -->
## TOPIC 00192: Instrument:Calibration:Cal ADC Input

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-caladcinput.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-caladcinput.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input of the calibration ADC. The ADC can take a reading from several inputs: the analog output, a 2.5 V reference, and ground. The latter two inputs are used to calibrate the ADC itself. You cannot change this property while the device is generating a waveform. If you want to change t

### Instrument:Calibration:Cal ADC Input

Specifies the input of the calibration ADC. The ADC can take a reading from several inputs: the analog output, a 2.5 V reference, and ground. 
The latter two inputs are used to calibrate the ADC itself.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cal ADC Input |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| NIFGEN_VAL_ANALOG_OUTPUT | 0 | Specifies that the ADC measures the analog output. |
| --- | --- | --- |
| NIFGEN_VAL_INTERNAL_VOLTAGE_REFERENCE | 1 | Specifies that the ADC measures the internal voltage reference. |
| NIFGEN_VAL_GROUND | 2 | Specifies that the ADC measures the ground voltage. |
| NIFGEN_VAL_ANALOG_OUTPUT_DIFFERENTIAL | 3 | Specifies that the ADC measures the differential analog output. |
| NIFGEN_VAL_ANALOG_OUTPUT_PLUS | 4 | Specifies that the ADC measures the positive differential analog output. |
| NIFGEN_VAL_ANALOG_OUTPUT_MINUS | 5 | Specifies that the ADC measures the negative differential analog output. |
| NIFGEN_VAL_ANALOG_OUTPUT_IDLE | 6 | Specifies that the ADC measures the idle analog output. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierenabled.html language=enus -->
## TOPIC 00193: Arbitrary Waveform:Onboard Signal Processing:Carrier Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables (TRUE) or disables (FALSE) generation of the carrier. Remarks The following table lists the characteristics of this property. Short Name Carrier Enabled Data type cbool.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes

### Arbitrary Waveform:Onboard Signal Processing:Carrier Enabled

Enables (TRUE) or disables (FALSE) generation of the carrier.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Carrier Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierfrequency.html language=enus -->
## TOPIC 00194: Arbitrary Waveform:Onboard Signal Processing:Carrier Frequency

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierfrequency.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency of the generated carrier. Remarks The following table lists the characteristics of this property. Short Name Carrier Frequency Data type cdbl.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes

### Arbitrary Waveform:Onboard Signal Processing:Carrier Frequency

Specifies the frequency of the generated carrier.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Carrier Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierphasei.html language=enus -->
## TOPIC 00195: Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Carrier Phase:Carrier Phase I

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierphasei.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierphasei.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the I carrier phase, in degrees, at the first point of the generated signal. Default Value: 0.0 Remarks The following table lists the characteristics of this property. Short Name Carrier Phase I Data type cdbl.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes

### Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Carrier Phase:Carrier Phase I

Specifies the I carrier phase, in degrees, at the first point of the generated signal.

**Default Value**: 0.0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Carrier Phase I |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierphaseq.html language=enus -->
## TOPIC 00196: Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Carrier Phase:Carrier Phase Q

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierphaseq.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-carrierphaseq.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Q carrier phase, in degrees, at the first point of the generated signal. This property is used only when the Data Processing Mode property is set to Complex. Default Value: -90.0 Remarks The following table lists the characteristics of this property. Short Name Carrier Phase Q Data typ

### Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Carrier Phase:Carrier Phase Q

Specifies the Q carrier phase, in degrees, at the first point of the generated signal. This property is used only when the [Data Processing Mode](/csh?topicname=pnifgen-dataprocessingmode.html) property is set to **Complex**.

**Default Value**: -90.0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Carrier Phase Q |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-channelcount.html language=enus -->
## TOPIC 00197: Instrument:Inherent IVI Attributes:Driver Capabilities:Channel Count

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-channelcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-channelcount.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of channels that NI-FGEN supports. For each property for which IVI_VAL_MULTI_CHANNEL is set, the IVI engine maintains a separate cache value for each channel. Remarks The following table lists the characteristics of this property. Short Name Channel Count Data type ci32.png Permis

### Instrument:Inherent IVI Attributes:Driver Capabilities:Channel Count

Returns the number of channels that NI-FGEN supports. 
 For each property for which IVI_VAL_MULTI_CHANNEL is set, the IVI engine maintains a separate cache value for each channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Channel Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-channeldelay.html language=enus -->
## TOPIC 00198: Output:Channel Delay

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-channeldelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-channeldelay.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the delay to apply to the analog output of the channel specified by the Active Channel property. You can use the output delay to configure the timing relationship between channels on a multichannel device. Values for this property can be zero or positive. A value of zero indicates that the

### Output:Channel Delay

Specifies the delay to apply to the analog output of the channel specified by the [Active Channel](/csh?topicname=pnifgen-activechannel.html) property.

You can use the output delay to configure the timing relationship between channels on a multichannel device. Values for this property can be zero or positive. A value of zero indicates that the channels are aligned. A positive value delays the analog output by the specified number of seconds.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Channel Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cicfilterenabled.html language=enus -->
## TOPIC 00199: Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Filter Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cicfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cicfilterenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables (TRUE) or disables (FALSE) the CIC filter. You must set the CIC Filter Enabled and FIR Filter Enabled properties to the same value. Remarks The following table lists the characteristics of this property. Short Name CIC Filter Enabled Data type cbool.png Permissions Read/Write High-level VIs

### Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Filter Enabled

Enables (TRUE) or disables (FALSE) the CIC filter.

Note

FIR Filter Enabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CIC Filter Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cicfiltergain.html language=enus -->
## TOPIC 00200: Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Filter Gain

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cicfiltergain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cicfiltergain.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the gain applied at the final stage of the CIC filter. This property is commonly used to compensate for attenuation in the FIR filter. If you set the FIR Filter Type to a value other than Custom, NI-FGEN calculates the CIC gain to achieve unity gain between the FIR and CIC filters. Setting

### Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Filter Gain

Specifies the gain applied at the final stage of the CIC filter. This property is commonly used to compensate for attenuation in the FIR filter. If you set the [FIR Filter Type](/csh?topicname=pnifgen-filtertype.html) to a value other than **Custom**, NI-FGEN calculates the CIC gain to achieve unity gain between the FIR and CIC filters. Setting this property overrides the value set by NI-FGEN.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CIC Filter Gain |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cicinterpolation.html language=enus -->
## TOPIC 00201: Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Interpolation Factor

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cicinterpolation.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-cicinterpolation.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the interpolation factor for the CIC filter. If you do not set this value, NI-FGEN calculates the appropriate value based on the value of the IQ Rate property. Remarks The following table lists the characteristics of this property. Short Name CIC Interpolation Data type cdbl.png Permission

### Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Interpolation Factor

Specifies the interpolation factor for the CIC filter. If you do not set this value, NI-FGEN calculates the appropriate value based on the value of the [IQ Rate](/csh?topicname=pnifgen-iqrate.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CIC Interpolation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-classgroupcapabilities.html language=enus -->
## TOPIC 00202: Instrument:Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-classgroupcapabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-classgroupcapabilities.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a comma-separated list of class-extension groups that NI-FGEN implements. Remarks The following table lists the characteristics of this property. Short Name Class Group Capabilities Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities

Returns a comma-separated list of class-extension groups that NI-FGEN implements.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Class Group Capabilities |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-classspecificationmajorversion.html language=enus -->
## TOPIC 00203: Instrument:Inherent IVI Attributes:Driver Identification:Class Specification Major Version

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-classspecificationmajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-classspecificationmajorversion.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the major version number of the class specification with which NI-FGEN is compliant. Remarks The following table lists the characteristics of this property. Short Name Class Specification Major Version Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Inherent IVI Attributes:Driver Identification:Class Specification Major Version

Returns the major version number of the class specification with which NI-FGEN is compliant.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Class Specification Major Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-classspecificationminorversion.html language=enus -->
## TOPIC 00204: Instrument:Inherent IVI Attributes:Driver Identification:Class Specification Minor Version

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-classspecificationminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-classspecificationminorversion.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minor version number of the class specification with which NI-FGEN is compliant. Remarks The following table lists the characteristics of this property. Short Name Class Specification Minor Version Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Inherent IVI Attributes:Driver Identification:Class Specification Minor Version

Returns the minor version number of the class specification with which NI-FGEN is compliant.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Class Specification Minor Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-clockmode.html language=enus -->
## TOPIC 00205: Clocks:Sample Clock:Mode

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-clockmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-clockmode.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Sample Clock mode for the signal generator. For signal generators that support it, this property allows switching the Sample Clock to a high-resolution clocking mode. When in divide-down sampling mode, the sample rate can be set only to certain frequencies, based on dividing down the S

### Clocks:Sample Clock:Mode

Specifies the Sample Clock mode for the signal generator.

For signal generators that support it, this property allows switching the Sample Clock to a high-resolution clocking mode. When in divide-down sampling mode, the sample rate can be set only to certain frequencies, based on dividing down the Sample Clock. However, in high-resolution mode, the sample rate may be set to any value.

Note

niFgen Abort Generation

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Clock Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Clock Mode |
| Channel-based | No |
| Resettable | Yes |

| NIFGEN_VAL_DIVIDE_DOWN | 1 | Divide down sampling—Sample rate is generated by dividing the source frequency. |
| --- | --- | --- |
| NIFGEN_VAL_HIGH_RESOLUTION | 0 | High resolution sampling—Sample rate is generated by a high resolution clock source. |
| NIFGEN_VAL_AUTOMATIC | 2 | Automatic Selection—NI-FGEN selects between the divide-down and high-resolution modes. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-commonmodeoffset.html language=enus -->
## TOPIC 00206: Output:Common Mode Offset

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-commonmodeoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-commonmodeoffset.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value the signal generator adds to or subtracts from the arbitrary waveform data. This property applies only when set the Terminal Configuration property to Differential. Common-mode offset is applied to the signals generated at each differential output terminal. Remarks The following

### Output:Common Mode Offset

Specifies the value the signal generator adds to or subtracts from the arbitrary waveform data. This property applies only when set the [Terminal Configuration](/csh?topicname=pnifgen-terminalconfiguration.html) property to **Differential**. Common-mode offset is applied to the signals generated at each differential output terminal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Common Mode Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-compensatefiltergroupdelay.html language=enus -->
## TOPIC 00207: Arbitrary Waveform:Onboard Signal Processing:Advanced:Compensate for Filter Group Delay

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-compensatefiltergroupdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-compensatefiltergroupdelay.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts for OSP filter group delay when aligning analog outputs and events in OSP mode. If you set this property to TRUE, event outputs align more closely with the analog output. The analog output also aligns more closely between two devices synchronized using NI-TClk. Group delay is the delay that

### Arbitrary Waveform:Onboard Signal Processing:Advanced:Compensate for Filter Group Delay

Adjusts for OSP filter group delay when aligning analog outputs and events in OSP mode. If you set this property to TRUE, event outputs align more closely with the analog output. The analog output also aligns more closely between two devices synchronized using NI-TClk.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Compensate for Filter Group Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-daqmxtask.html language=enus -->
## TOPIC 00208: Instrument:Obsolete:DAQmx Task

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-daqmxtask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-daqmxtask.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DAQmx task pointer. Remarks The following table lists the characteristics of this property. Short Name DAQmx Task Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Obsolete:DAQmx Task

Returns the NI-DAQmx task pointer.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DAQmx Task |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkereventbitnumber.html language=enus -->
## TOPIC 00209: Events:Data Marker:Data Bit Number

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkereventbitnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkereventbitnumber.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bit number to assign to the Data Marker Event. Remarks The following table lists the characteristics of this property. Short Name Data Marker Event Bit Number Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes

### Events:Data Marker:Data Bit Number

Specifies the bit number to assign to the Data Marker Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Marker Event Bit Number |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkereventlevelpolarity.html language=enus -->
## TOPIC 00210: Events:Data Marker:Level:Active Level

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkereventlevelpolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkereventlevelpolarity.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output polarity of the Data Marker Event. Refer to Data Marker Events topic for more information about Data Marker Event polarity. Remarks The following table lists the characteristics of this property. Short Name Data Marker Event Level Polarity Data type ci32.png Permissions Read/Wri

### Events:Data Marker:Level:Active Level

Specifies the output polarity of the Data Marker Event. Refer to [Data Marker Events](/csh?context=nifgen_siggenhelp_events_data_markers) topic for more information about Data Marker Event polarity.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Marker Event Level Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Active High | 101 | When the data bit is 1 (high), the Data Marker Event level is high. |
| --- | --- | --- |
| Active Low | 102 | When the data bit is 1 (high), the Data Marker Event level is low. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkereventoutputterminal.html language=enus -->
## TOPIC 00211: Events:Data Marker:Output Terminal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkereventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkereventoutputterminal.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Data Marker Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. NI recommends using a data sample rate of less than 200 MS/s for data markers routed to RTSI. Faster sample r

### Events:Data Marker:Output Terminal

Specifies the destination terminal for the Data Marker Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Marker Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkerscount.html language=enus -->
## TOPIC 00212: Instrument:Data Marker Events Count

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkerscount.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datamarkerscount.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of Data Marker Events supported by the device. Remarks The following table lists the characteristics of this property. Short Name Data Markers Count Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Data Marker Events Count

Returns the number of Data Marker Events supported by the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Markers Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-dataprocessingmode.html language=enus -->
## TOPIC 00213: Arbitrary Waveform:Onboard Signal Processing:Data Processing Mode

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-dataprocessingmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-dataprocessingmode.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the way that data is processed by the OSP block. When using the NI 5450/5451 with I/Q rates higher than 200 MS/s, NI-FGEN restricts this property value to Complex. Remarks The following table lists the characteristics of this property. Short Name Data Processing Mode Data type ci32.png Perm

### Arbitrary Waveform:Onboard Signal Processing:Data Processing Mode

Controls the way that data is processed by the OSP block.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Processing Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Real | 0 | Specifies that the waveform data points are real numbers (I data). |
| --- | --- | --- |
| Complex | 1 | Specifies that the waveform data points are complex numbers (I/Q data). |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferblocksize.html language=enus -->
## TOPIC 00214: Arbitrary Waveform:Data Transfer:Data Transfer Block Size

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferblocksize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferblocksize.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples at a time to download to onboard memory. This property is useful when the total data to be transferred to onboard memory is large. Remarks The following table lists the characteristics of this property. Short Name Data Transfer Block Size Data type ci32.png Permission

### Arbitrary Waveform:Data Transfer:Data Transfer Block Size

Specifies the number of samples at a time to download to onboard memory. This property is useful when the total data to be transferred to onboard memory is large.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Transfer Block Size |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissionaddress.html language=enus -->
## TOPIC 00215: Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Data Transfer Permission Address

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissionaddress.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissionaddress.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the address in the writer peer to which the signal generator sends data transfer permission credits. This property is endpoint-based. You can use this property only when the Manual Configuration Enabled property is set to TRUE. Remarks The following table lists the characteristics of this

### Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Data Transfer Permission Address

Indicates the address in the writer peer to which the signal generator sends data transfer permission credits. This property is [endpoint-based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint).

Note

Manual Configuration Enabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Transfer Permission Address |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissionaddresstype.html language=enus -->
## TOPIC 00216: Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Data Transfer Permission Address Type

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissionaddresstype.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissionaddresstype.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of address for the Data Transfer Permission Address property. This property is endpoint-based. You can only use this property when the Manual Configuration Enabled property is set to TRUE. Default Value: Virtual Remarks The following table lists the characteristics of this propert

### Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Data Transfer Permission Address Type

Specifies the type of address for the [Data Transfer Permission Address](/csh?topicname=pnifgen-datatransferpermissionaddress.html) property. This property is [endpoint-based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint).

Note

Manual Configuration Enabled

**Default Value**: **Virtual**

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Transfer Permission Address Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

| Physical | 0 | Specifies a physical memory address. |
| --- | --- | --- |
| Virtual | 1 | Specifies a virtual memory address. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissioninitialcredits.html language=enus -->
## TOPIC 00217: Arbitrary Waveform:Peer-to-Peer:Data Transfer Permission Initial Credits

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissioninitialcredits.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissioninitialcredits.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial amount of data, in samples per channel, that the writer peer is allowed to transfer over the bus into the configured endpoint when the peer-to-peer data stream is enabled. If you do not set this property and the endpoint is empty, credits equal to the full size of the endpoint

### Arbitrary Waveform:Peer-to-Peer:Data Transfer Permission Initial Credits

Specifies the initial amount of data, in samples per channel, that the writer peer is allowed to transfer over the bus into the configured endpoint when the peer-to-peer data stream is enabled. If you do not set this property and the endpoint is empty, credits equal to the full size of the endpoint are issued to the writer peer. If data has been written to the endpoint using the [niFgen Write P2P Endpoint I16](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI prior to enabling the stream, credits equal to the remaining space available in the endpoint are issued to the writer peer. This property is coerced up by NI-FGEN to 8-byte boundaries.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Transfer Permission Initial Credits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissioninterval.html language=enus -->
## TOPIC 00218: Arbitrary Waveform:Peer-to-Peer:Data Transfer Permission Interval

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissioninterval.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-datatransferpermissioninterval.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the interval, in samples per channel, at which the signal generator issues credits to allow the writer peer to transfer data over the bus into the configured endpoint. Refer to the Flow Control topic in the NI Signal Generators Help for more information. This property is coerced up by NI-F

### Arbitrary Waveform:Peer-to-Peer:Data Transfer Permission Interval

Specifies the interval, in samples per channel, at which the signal generator issues credits to allow the writer peer to transfer data over the bus into the configured endpoint. Refer to the [Flow Control](/csh?context=nifgen_siggenhelp_p2p_flow_control) topic in the *NI Signal Generators Help* for more information. This property is coerced up by NI-FGEN to the nearest 128-byte boundary. This property is [endpoint-based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint).

**Default Value**: 1,024

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Transfer Permission Interval |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-dcoffset.html language=enus -->
## TOPIC 00219: Standard Function:DC Offset

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-dcoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-dcoffset.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the DC offset of the standard waveform that the signal generator produces. This value is the offset at the output terminal. The value is the offset from ground to the center of the waveform you specify with the Waveform property. For example, to configure a waveform with an amplitude of 10.

### Standard Function:DC Offset

Controls the DC offset of the standard waveform that the signal generator produces.

This value is the offset at the output terminal. The value is the offset from ground to the center of the waveform you specify with the [Waveform](pnifgen-waveform.html) property.

For example, to configure a waveform with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set this property to 5.00 V.

**Units**: volts (V)

**Default Value**: None

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DC Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Frequency List, niFgen Configure Standard Waveform |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-description.html language=enus -->
## TOPIC 00220: Instrument:Inherent IVI Attributes:Driver Identification:Description

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-description.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-description.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains a brief description of the specific driver. Remarks The following table lists the characteristics of this property. Short Name Description Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Inherent IVI Attributes:Driver Identification:Description

Contains a brief description of the specific driver.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Description |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-destinationchannels.html language=enus -->
## TOPIC 00221: Arbitrary Waveform:Peer-to-Peer:Destination Channels

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-destinationchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-destinationchannels.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which channels are written to by a peer-to-peer endpoint. If multiple channels are specified, data is deinterleaved to each channel. Channels are configured using the niFgen Configure Channels VI. This property is endpoint based. Default Value: "" (empty string), all channels are configure

### Arbitrary Waveform:Peer-to-Peer:Destination Channels

Specifies which channels are written to by a peer-to-peer endpoint. If multiple channels are specified, data is deinterleaved to each channel. Channels are configured using the [niFgen Configure Channels](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI. This property is [endpoint based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint).

**Default Value**: "" (empty string), all channels are configured

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Destination Channels |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitaldatamask.html language=enus -->
## TOPIC 00222: Output:Data Mask:Digital Data Mask

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitaldatamask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitaldatamask.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mask to apply to the output on the digital connector. The masked data is replaced with the data in the Digital Static Value property. Remarks The following table lists the characteristics of this property. Short Name Digital Data Mask Data type ci32.png Permissions Read/Write High-leve

### Output:Data Mask:Digital Data Mask

Specifies the mask to apply to the output on the digital connector. The masked data is replaced with the data in the [Digital Static Value](/csh?topicname=pnifgen-digitalstaticvalue.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Data Mask |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalfilterenabled.html language=enus -->
## TOPIC 00223: Output:Filters:Digital Filter Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalfilterenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal generator applies a digital filter to the output signal. Set this property to TRUE to use a digital filter. This property is valid in Arbitrary Waveform, Arbitrary Sequence, and Script output modes. You also can use this property in Standard Function and Frequency List o

### Output:Filters:Digital Filter Enabled

Specifies whether the signal generator applies a digital filter to the output signal. Set this property to TRUE to use a digital filter. This property is valid in Arbitrary Waveform, Arbitrary Sequence, and Script output modes. You also can use this property in Standard Function and Frequency List output modes for user-defined waveforms.

**Default Value**: FALSE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Filter Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Digital Filter |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalfilterinterpolationfactor.html language=enus -->
## TOPIC 00224: Output:Filters:Digital Filter Interpolation Factor

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalfilterinterpolationfactor.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalfilterinterpolationfactor.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the interpolation factor when the Digital Filter Enabled property is set to TRUE. You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. Valid Val

### Output:Filters:Digital Filter Interpolation Factor

Specifies the interpolation factor when the [Digital Filter Enabled](/csh?topicname=pnifgen-digitalfilterenabled.html) property is set to TRUE.

Note

niFgen Abort Generation

**Valid Values**: 2, 4, and 8

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Filter Interpolation Factor |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalgain.html language=enus -->
## TOPIC 00225: Output:Digital Gain

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalgain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalgain.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the DAC. For a digital gain greater than 1.0, the product of digital gain times the generated data must be inside the range ±1.0, assuming floating point data. If the prod

### Output:Digital Gain

Specifies a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the DAC. For a digital gain greater than 1.0, the product of digital gain times the generated data must be inside the range ±1.0, assuming floating point data. If the product exceeds these limits, the signal generator clips the output signal, and an error results.

Some signal generators support both digital gain and analog gain, specified with the [Amplitude](pnifgen-amplitude.html) property or [Arbitrary Waveform Gain](pnifgen-arbitrarywaveformgain.html) property. Digital gain can be changed during generation without the glitches that may occur when changing analog gains, because of relay switching. However, the DAC output resolution is a function of analog gain, so only analog gain makes full use of the resolution of the DAC.

**Default Value**: 1

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Gain |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalpatternenabled.html language=enus -->
## TOPIC 00226: Output:Advanced:Digital Pattern Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalpatternenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalpatternenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal generator generates a digital pattern corresponding to the output signal. Set this property to TRUE to generate a digital pattern. Remarks The following table lists the characteristics of this property. Short Name Digital Pattern Enabled Data type cbool.png Permissions R

### Output:Advanced:Digital Pattern Enabled

Specifies whether the signal generator generates a digital pattern corresponding to the output signal. Set this property to TRUE to generate a digital pattern.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Pattern Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Digital Patterning |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalstaticvalue.html language=enus -->
## TOPIC 00227: Output:Data Mask:Digital Static Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalstaticvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-digitalstaticvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the static value that replaces data masked by the Digital Data Mask property. Remarks The following table lists the characteristics of this property. Short Name Digital Static Value Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes

### Output:Data Mask:Digital Static Value

Specifies the static value that replaces data masked by the [Digital Data Mask](/csh?topicname=pnifgen-digitaldatamask.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Static Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-directdmaenabled.html language=enus -->
## TOPIC 00228: Arbitrary Waveform:Data Transfer:Direct DMA:Direct DMA Enabled

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-directdmaenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-directdmaenabled.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the device for Direct DMA writes. When enabled, all niFgen Create Waveform VI and niFgen Write Waveform VI calls that are given a data address in the Direct DMA window download data residing on the Direct DMA device to the instrument onboard memory. Remarks The following table lists the char

### Arbitrary Waveform:Data Transfer:Direct DMA:Direct DMA Enabled

Enables the device for Direct DMA writes.

When enabled, all [niFgen Create Waveform](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI and [niFgen Write Waveform](/csh?context=nifgen_siggenhelp_javascript:launchmergedhelp() VI calls that are given a data address in the Direct DMA window download data residing on the Direct DMA device to the instrument onboard memory.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Direct DMA Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-directdmawindowaddress.html language=enus -->
## TOPIC 00229: Arbitrary Waveform:Data Transfer:Direct DMA:Window Address

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-directdmawindowaddress.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-directdmawindowaddress.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the window address (beginning of window) of the waveform data source. This window address is specified by your Direct DMA-compatible data source. Remarks The following table lists the characteristics of this property. Short Name Direct DMA Window Address Data type ci32.png Permissions Read

### Arbitrary Waveform:Data Transfer:Direct DMA:Window Address

Specifies the window address (beginning of window) of the waveform data source. This window address is specified by your Direct DMA-compatible data source.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Direct DMA Window Address |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-directdmawindowsize.html language=enus -->
## TOPIC 00230: Arbitrary Waveform:Data Transfer:Direct DMA:Window Size in Bytes

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-directdmawindowsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-directdmawindowsize.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the size of the memory window provided by your Direct DMA-compatible data source. Remarks The following table lists the characteristics of this property. Short Name Direct DMA Window Size Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes

### Arbitrary Waveform:Data Transfer:Direct DMA:Window Size in Bytes

Specifies the size of the memory window provided by your Direct DMA-compatible data source.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Direct DMA Window Size |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventactivelevel.html language=enus -->
## TOPIC 00231: Events:Done:Level:Active Level

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventactivelevel.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output polarity of the Done Event. Remarks The following table lists the characteristics of this property. Short Name Done Event Active Level Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Active High 101 When the operation is complete, the

### Events:Done:Level:Active Level

Specifies the output polarity of the Done Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Active Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Active High | 101 | When the operation is complete, the Done Event level is high. |
| --- | --- | --- |
| Active Low | 102 | When the operation is complete, the Done Event level is low. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventdelayunits.html language=enus -->
## TOPIC 00232: Events:Done:Advanced:Delay Units

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventdelayunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventdelayunits.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units used for the Done Event Delay Value property. Remarks The following table lists the characteristics of this property. Short Name Done Event Delay Units Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Sample Clock Periods 101 The delay

### Events:Done:Advanced:Delay Units

Specifies the units used for the [Done Event Delay Value](/csh?topicname=pnifgen-doneeventdelayvalue.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Delay Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Sample Clock Periods | 101 | The delay is specified in Sample Clock periods and then coerced up by NI-FGEN to the nearest Sample Clock period. |
| --- | --- | --- |
| Seconds | 102 | The delay is specified in seconds and then coerced up by NI-FGEN to the nearest Sample Clock period. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventdelayvalue.html language=enus -->
## TOPIC 00233: Events:Done:Advanced:Delay Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventdelayvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventdelayvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of delay applied to a Done Event with respect to the analog output of the signal generator. A positive delay value indicates that the Done Event occurs after the analog data, while a negative delay value indicates that the Done Event occurs before the analog data. A value of zer

### Events:Done:Advanced:Delay Value

Specifies the amount of delay applied to a Done Event with respect to the analog output of the signal generator.

A positive delay value indicates that the Done Event occurs after the analog data, while a negative delay value indicates that the Done Event occurs before the analog data. A value of zero aligns the Done Event with the analog output.

You can specify the units of the delay value by setting the [Delay Units](pnifgen-doneeventdelayunits.html) property.

**Default Value**: 0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Delay Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventlatchedstatus.html language=enus -->
## TOPIC 00234: Events:Done:Advanced:Latched Status

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventlatchedstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventlatchedstatus.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the latched status of the specified Done Event. Remarks The following table lists the characteristics of this property. Short Name Done Event Latched Status Data type cbool.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Events:Done:Advanced:Latched Status

Returns the latched status of the specified Done Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Latched Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventoutputbehavior.html language=enus -->
## TOPIC 00235: Events:Done:Output Behavior

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventoutputbehavior.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output behavior for the Done Event. Remarks The following table lists the characteristics of this property. Short Name Done Event Output Behavior Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Pulse 101 Triggers a pulse for a specified peri

### Events:Done:Output Behavior

Specifies the output behavior for the Done Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Output Behavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Pulse | 101 | Triggers a pulse for a specified period of time. |
| --- | --- | --- |
| Level | 102 | Changes to high or low while the event is active, depending on the active state you specify. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventoutputterminal.html language=enus -->
## TOPIC 00236: Events:Done:Output Terminal

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventoutputterminal.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Done Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the Device Routes tab in MAX. Remarks The following table lists the characteristics of this property. Short Name Done Event Output Terminal Data t

### Events:Done:Output Terminal

Specifies the destination terminal for the Done Event. For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventpulsepolarity.html language=enus -->
## TOPIC 00237: Events:Done:Pulse:Polarity

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventpulsepolarity.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output polarity of the Done Event. Remarks The following table lists the characteristics of this property. Short Name Done Event Pulse Polarity Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Active High 101 When the operation is done, the D

### Events:Done:Pulse:Polarity

Specifies the output polarity of the Done Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Pulse Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Active High | 101 | When the operation is done, the Done Event polarity is high. |
| --- | --- | --- |
| Active Low | 102 | When the operation is done, the Done Event polarity is low. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventpulsewidthunits.html language=enus -->
## TOPIC 00238: Events:Done:Pulse:Width Units

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventpulsewidthunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventpulsewidthunits.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse width units for the Done Event. Remarks The following table lists the characteristics of this property. Short Name Done Event Pulse Width Units Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Sample Clock Periods 101 Specifies the puls

### Events:Done:Pulse:Width Units

Specifies the pulse width units for the Done Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Pulse Width Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Sample Clock Periods | 101 | Specifies the pulse width in Sample Clock periods. |
| --- | --- | --- |
| Seconds | 102 | Specifies the pulse width in seconds. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventpulsewidthvalue.html language=enus -->
## TOPIC 00239: Events:Done:Pulse:Width Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventpulsewidthvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-doneeventpulsewidthvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse width for the Done Event. Remarks The following table lists the characteristics of this property. Short Name Done Event Pulse Width Value Data type cdbl.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes

### Events:Done:Pulse:Width Value

Specifies the pulse width for the Done Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Pulse Width Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-donenotificationaddress.html language=enus -->
## TOPIC 00240: Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Notification:Done Notification Address

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-donenotificationaddress.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-donenotificationaddress.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the signal generator address to which the writer peer sends the Done Notification Value. This property is endpoint-based. Refer to the Stopping a Peer-to-Peer Generation topic in the NI Signal Generators Help for more information about using Done Notifications. You can only use this property

### Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Notification:Done Notification Address

Returns the signal generator address to which the writer peer sends the [Done Notification Value](/csh?topicname=pnifgen-donenotificationvalue.html). This property is [endpoint-based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint). Refer to the [Stopping a Peer-to-Peer Generation](/csh?context=nifgen_siggenhelp_p2p_stopping_generation) topic in the *NI Signal Generators Help* for more information about using Done Notifications.

Note

Manual Configuration Enabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Notification Address |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-donenotificationaddresstype.html language=enus -->
## TOPIC 00241: Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Notification:Done Notification Address Type

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-donenotificationaddresstype.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-donenotificationaddresstype.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the address type of the Done Notification Address property. This property is endpoint-based. Refer to the Stopping a Peer-to-Peer Generation topic in the NI Signal Generators Help for more information about using Done Notifications. You can only use this property when the Manual Configurat

### Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Notification:Done Notification Address Type

Specifies the address type of the [Done Notification Address](/csh?topicname=pnifgen-donenotificationaddress.html) property. This property is [endpoint-based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint). Refer to the [Stopping a Peer-to-Peer Generation](/csh?context=nifgen_siggenhelp_p2p_stopping_generation) topic in the *NI Signal Generators Help* for more information about using Done Notifications.

Note

Manual Configuration Enabled

Default Value: **Virtual**

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Notification Address Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

| Physical | 0 | Specifies a physical memory address. |
| --- | --- | --- |
| Virtual | 1 | Specifies a virtual memory address. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-donenotificationvalue.html language=enus -->
## TOPIC 00242: Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Notification:Done Notification Value

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-donenotificationvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-donenotificationvalue.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value the writer peer writes to the address specified by the Done Notification Address property. This property is endpoint-based. Refer to the Stopping a Peer-to-Peer Generation topic in the NI Signal Generators Help for more information about using Done Notifications. You can only use t

### Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Notification:Done Notification Value

Returns the value the writer peer writes to the address specified by the [Done Notification Address](/csh?topicname=pnifgen-donenotificationaddress.html) property. This property is [endpoint-based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint). Refer to the [Stopping a Peer-to-Peer Generation](/csh?context=nifgen_siggenhelp_p2p_stopping_generation) topic in the *NI Signal Generators Help* for more information about using Done Notifications.

Note

Manual Configuration Enabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Notification Value |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-driverprefix.html language=enus -->
## TOPIC 00243: Instrument:Inherent IVI Attributes:Driver Identification:Driver Prefix

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-driverprefix.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-driverprefix.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the prefix for NI-FGEN. The name of each user-callable VI in NI-FGEN starts with this prefix. Remarks The following table lists the characteristics of this property. Short Name Driver Prefix Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Inherent IVI Attributes:Driver Identification:Driver Prefix

Contains the prefix for NI-FGEN. The name of each user-callable VI in NI-FGEN starts with this prefix.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Driver Prefix |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-drivervendor.html language=enus -->
## TOPIC 00244: Instrument:Inherent IVI Attributes:Driver Identification:Driver Vendor

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-drivervendor.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-drivervendor.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains the name of the vendor that supplies NI-FGEN. Remarks The following table lists the characteristics of this property. Short Name Driver Vendor Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Instrument:Inherent IVI Attributes:Driver Identification:Driver Vendor

Contains the name of the vendor that supplies NI-FGEN.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Driver Vendor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-dutycyclehigh.html language=enus -->
## TOPIC 00245: Standard Function:Duty Cycle High

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-dutycyclehigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-dutycyclehigh.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duty cycle of the square wave the signal generator is producing. Specify this property as a percentage of the time the square wave is high in a cycle. Units: Percentage of time the waveform is high Default Value: 50% This parameter only affects signal generator behavior when you set th

### Standard Function:Duty Cycle High

Specifies the duty cycle of the square wave the signal generator is producing. Specify this property as a percentage of the time the square wave is high in a cycle.

**Units**: Percentage of time the waveform is high

**Default Value**: 50%

Note

Waveform

NIFGEN_VAL_WFM_SQUARE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Duty Cycle High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointcount.html language=enus -->
## TOPIC 00246: Arbitrary Waveform:Peer-to-Peer:Endpoint Count

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointcount.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of peer-to-peer FIFO endpoints supported by the device. Remarks The following table lists the characteristics of this property. Short Name Endpoint Count Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Arbitrary Waveform:Peer-to-Peer:Endpoint Count

Returns the number of peer-to-peer FIFO endpoints supported by the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Endpoint Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointsize.html language=enus -->
## TOPIC 00247: Arbitrary Waveform:Peer-to-Peer:Endpoint Size

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointsize.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size, in samples per channel, of the peer-to-peer endpoint. This property is endpoint-based. Remarks The following table lists the characteristics of this property. Short Name Endpoint Size Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based Yes Resettable No

### Arbitrary Waveform:Peer-to-Peer:Endpoint Size

Returns the size, in samples per channel, of the peer-to-peer endpoint. This property is [endpoint-based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Endpoint Size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointwindowaddress.html language=enus -->
## TOPIC 00248: Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Endpoint Window Address

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointwindowaddress.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointwindowaddress.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the signal generator address where endpoint data is sent by the writer peer. The type of this address is specified by the Endpoint Window Address Type property. This property is endpoint-based. You can only use this property when the Manual Configuration Enabled property is set to TRUE. Rema

### Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Endpoint Window Address

Returns the signal generator address where endpoint data is sent by the writer peer. The type of this address is specified by the [Endpoint Window Address Type](/csh?topicname=pnifgen-endpointwindowaddresstype.html) property. This property is [endpoint-based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint).

Note

Manual Configuration Enabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Endpoint Window Address |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointwindowaddresstype.html language=enus -->
## TOPIC 00249: Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Endpoint Window Address Type

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointwindowaddresstype.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointwindowaddresstype.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of the Endpoint Window Address property. This property is endpoint-based. You can only use this property when the Manual Configuration Enabled property is set to TRUE. Default Value: Virtual Remarks The following table lists the characteristics of this property. Short Name Endpoin

### Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Endpoint Window Address Type

Specifies the type of the [Endpoint Window Address](/csh?topicname=pnifgen-endpointwindowaddress.html) property. This property is [endpoint-based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint).

Note

Manual Configuration Enabled

**Default Value**: **Virtual**

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Endpoint Window Address Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

| Physical | 0 | Specifies a physical memory address. |
| --- | --- | --- |
| Virtual | 1 | Specifies a virtual memory address. |

Parent topic:

niFgen Properties

<!--NI_TOPIC bundle=ni-fgen-labview-api-ref path=instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointwindowsize.html language=enus -->
## TOPIC 00250: Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Endpoint Window Size

- bundle_id: `ni-fgen-labview-api-ref`
- source_path: `instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointwindowsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-labview-api-ref/raw/resource/enus/instr-lib/nifgen/nifgen-rc/nifgen/pnifgen-endpointwindowsize.html
- document_id: `ni-fgen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size, in bytes, of the endpoint window. The endpoint window is also described by the Endpoint Window Address property and the Endpoint Window Address Type property. This property is endpoint-based. You can only use this property when the Manual Configuration Enabled property is set to TR

### Arbitrary Waveform:Peer-to-Peer:Obsolete:Manual:Configuration:Endpoint Window Size

Returns the size, in bytes, of the endpoint window. The endpoint window is also described by the [Endpoint Window Address](/csh?topicname=pnifgen-endpointwindowaddress.html) property and the [Endpoint Window Address Type](/csh?topicname=pnifgen-endpointwindowaddresstype.html) property. This property is [endpoint-based](/csh?context=nifgen_siggenhelp_p2p_configuring_an_endpoint).

Note

Manual Configuration Enabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Endpoint Window Size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niFgen Properties
