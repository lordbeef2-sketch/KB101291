# NI DOCUMENT BUNDLE: ni-spml-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-spml-labview-api-ref start=1 end=60 -->
<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=menus/categories/measurement/nispml/spml-calibration-mnu.html language=enus -->
## TOPIC 00001: Calibration

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `menus/categories/measurement/nispml/spml-calibration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/menus/categories/measurement/nispml/spml-calibration-mnu.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Calibration VIs to perform a s-parameter calibration on your device. icon

### Calibration

Use the Calibration VIs to perform a s-parameter calibration on your device.

[IMAGE alt='icon' src='spml-calibration-mnu.png']

- [Configure Calibration Method VI](../../../../vi-lib/nispml/configure-calibration-method-vi.html) Sets the calibration method to use for the S-parameter measurement.
- [Get Calibration Status VI](../../../../vi-lib/nispml/get-calibration-status-vi.html) Fetches the calibration status of S-Parameter measurements, including whether calibration was performed on the measurement, and the timestamp when calibration was performed.
- [Get Calibration Actions VI](../../../../vi-lib/nispml/get-calibration-actions-vi.html) Fetches all the calibration actions to perform. Use this VI before executing the calibration actions using the Calibrate S-Parameters VI.
- [Calibrate S-Parameters VI](../../../../vi-lib/nispml/calibrate-s-parameters-vi.html) Performs calibration on the measurement system. Before using this VI, use the Get Calibration Actions VI to get all the steps required for your measurement topology and execute each action.
- [Get Calibration Measurement VI](../../../../vi-lib/nispml/get-calibration-measurement-vi.html) Fetches the raw calibration measurements for various calibration methods. Refer to the SOLT Measurements output and TRL Measurements output for details.
- [Save Calibration Parameters VI](../../../../vi-lib/nispml/save-calibration-parameters-vi.html) Saves the calibration parameters in a .tdms file.
- [Load Calibration Parameters VI](../../../../vi-lib/nispml/load-calibration-parameters-vi.html) Configures the S-parameter measurement session to retrieve parameters from a particular calibration file. You can define and write to this file location using the Save Calibration Parameters VI.
- [Configure Calibration Standards File Paths VI](../../../../vi-lib/nispml/configure-calibration-standards-file-paths-vi.html) Configures the locations of the short, open, and load standard characterization files that are used in the system-wide calibration.
- [Configure Calibration Through File Path VI](../../../../vi-lib/nispml/configure-calibration-through-file-path-vi.html) Configures the location of the through adapter calibration file that is used in the system-wide calibration.
- [Configure TRL Calibration VI](../../../../vi-lib/nispml/configure-trl-calibration-vi.html) Configures configuration options for TRL calibration.

Parent topic:

S-Parameter Measurement

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=menus/categories/measurement/nispml/spml-configuration-mnu.html language=enus -->
## TOPIC 00002: Configuration

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `menus/categories/measurement/nispml/spml-configuration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/menus/categories/measurement/nispml/spml-configuration-mnu.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Configuration VIs to configure the s-parameter measurement. icon

### Configuration

Use the Configuration VIs to configure the s-parameter measurement.

[IMAGE alt='icon' src='spml-configuration-mnu.png']

- [Configure Averaging VI](../../../../vi-lib/nispml/configure-averaging-vi.html) Configures the averaging technique used to calculate the S-parameter for the instrument.
- [Configure External Gain VI](../../../../vi-lib/nispml/configure-external-gain-vi.html) Configures the maximum gain of all the paths from VST RFout to RFin so you can set the appropriate reference level for the measurements.
- [Configure Frequency Range VI](../../../../vi-lib/nispml/configure-frequency-range-vi.html) Configures the frequency range used for S-parameter measurements.
- [Configure IF Bandwidth VI](../../../../vi-lib/nispml/configure-if-bandwidth-vi.html) Configures the IF bandwidth of the measurement.
- [Configure Stimulus VI](../../../../vi-lib/nispml/configure-stimulus-vi.html) Defines the type of RF signal used to stimulate the DUT.
- [Configure Topology VI](../../../../vi-lib/nispml/configure-topology-vi.html) Configures the type of NI and third party hardware configuration used to calculate S-parameters.
- [Configure RFSG Power Level VI](../../../../vi-lib/nispml/configure-rfsg-power-level-vi.html) Configures the power level used to calculate the S-parameter measurement.
- [Configure RFSG Attenuation VI](../../../../vi-lib/nispml/configure-rfsg-attenuation-vi.html) Configures the RFSG attenuation type so that the power level at the DUT port is corrected to match the same power level set by the Configure RFSG Power Level VI.
- [Configure Start Trigger Input VI](../../../../vi-lib/nispml/configure-start-trigger-input-vi.html) Configures the trigger to start the S-parameter measurement. The measurement is complete when there is a rising edge on the assigned trigger. This configuration only supports the 2 couplers per port 1 VST with solid state switch setup. If the trigger is not configured or configured for an unsupported setup the measurement is performed immediately after initiated.
- [Configure RFSG Export Trigger VI](../../../../vi-lib/nispml/configure-rfsg-export-trigger-vi.html) Configures the type and source of the trigger to export for each pulse. This configuration supports the 2 couplers per port 1 VST with solid state switch setup. If the trigger is not configured, or configured for an unsupported setup, no trigger is exported.

Parent topic:

S-Parameter Measurement

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=menus/categories/measurement/nispml/spml-util-mnu.html language=enus -->
## TOPIC 00003: Utility

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `menus/categories/measurement/nispml/spml-util-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/menus/categories/measurement/nispml/spml-util-mnu.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Utility VIs to access additional features of the S-Parameter Measurement Library. icon

### Utility

Use the Utility VIs to access additional features of the S-Parameter Measurement Library.

[IMAGE alt='icon' src='spml-util-mnu.png']

- [Save S-Parameters VI](../../../../vi-lib/nispml/save-s-parameters-vi.html) Saves measurement results in an .s2p file.
- [Get Topology References VI](../../../../vi-lib/nispml/get-topology-references-vi.html) Fetches the RFmx and RFSG references of the current S-parameter measurement session.

Parent topic:

S-Parameter Measurement

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=menus/categories/measurement/spml-mnu.html language=enus -->
## TOPIC 00004: S-Parameter Measurement

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `menus/categories/measurement/spml-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/menus/categories/measurement/spml-mnu.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the S-Parameter Measurement Library VIs to program NI VST devices with external coupler networks to perform s-parameter measurements. icon

### S-Parameter Measurement

Use the S-Parameter Measurement Library VIs to program NI VST devices with external coupler networks to perform s-parameter measurements.

[IMAGE alt='icon' src='spml-mnu.png']

- [Initialize VI](../../../vi-lib/nispml/initialize-vi.html) Initializes a S-parameter session for the session name that you specify in the Session Name parameter and returns a session reference handle that identifies the session in all subsequent S-Parameter VIs.
- [Configuration](../../../menus/categories/measurement/nispml/spml-configuration-mnu.html) Use the Configuration VIs to configure the s-parameter measurement.
- [Commit VI](../../../vi-lib/nispml/commit-vi.html) Commits the configured parameters to the hardware. Call this VI after all configuration VIs and before the Load Calibration VI for proper operation.
- [Initiate VI](../../../vi-lib/nispml/initiate-vi.html) Begins the S-parameter measurement.
- [Fetch S-Parameters VI](../../../vi-lib/nispml/fetch-s-parameters-vi.html) Fetches the calculated S-parameter measurement.
- [Close VI](../../../vi-lib/nispml/close-vi.html) Closes the S-parameter measurement session.
- [Utility](../../../menus/categories/measurement/nispml/spml-util-mnu.html) Use the Utility VIs to access additional features of the S-Parameter Measurement Library.
- [Calibration](../../../menus/categories/measurement/nispml/spml-calibration-mnu.html) Use the Calibration VIs to perform a s-parameter calibration on your device.

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=S-Par-1-Coupler-Per-Port-1-VST-Switching-Class.html language=enus -->
## TOPIC 00005: S-Par 1 Coupler Per Port 1 VST Switching Class

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `S-Par-1-Coupler-Per-Port-1-VST-Switching-Class.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/S-Par-1-Coupler-Per-Port-1-VST-Switching-Class.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class is the base class for 1 coupler per port 1 VST setup. To implement your own switching class, inherit from this class and override the following two functions. Connect.vi This member VI is used to make the connection based on the direction of the incident and the coupler selection. Port 1

### S-Par 1 Coupler Per Port 1 VST Switching Class

This class is the base class for 1 coupler per port 1 VST setup. To implement your own
 switching class, inherit from this class and override the following two
 functions.

#### Connect.vi

This member VI is used to make the connection based on the
 direction of the incident and the coupler selection.

[IMAGE alt='image' src='S-par-1-Coupler-Per-Port-1-VST-Switching-(Connect).gif']

[IMAGE alt='image' src='terminals/cbool.png']
 Port 1 incident

Specifies the direction of the stimulus.

| TRUE | The stimulus comes from Port 1. |
| --- | --- |
| FALSE | The stimulus comes from Port 2. |

[IMAGE alt='image' src='terminals/cbool.png']
 Reflection

| TRUE | Reflection measurement. |
| --- | --- |
| FALSE | Transmission measurement. |

#### Close Object.vi

This member VI is used to close all the sessions opened for the
 switches or DIO modules to control external switches.

[IMAGE alt='image' src='S-par-1-Coupler-Per-Port-1-VST-Switching-(Close-Object).gif']

#### Initialize

Other than these two functions, you may also need to create an
 initialize function to create a new switching object, as shown in the following
 example. You will need to open the sessions for all the modules used for switching,
 check if the configuration is valid, and create a data value reference for the class
 object so that it can be used in the S-parameter Measurement
 API.

[IMAGE alt='image' src='S-par-1-Coupler-Per-Port-1-VST-Switching-(Init).gif']

Parent topic:

S-Parameter Switching Configuration Class

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=S-Par-2-Couplers-Per-Port-1-VST-Switching-(Scan-Mode)-Class.html language=enus -->
## TOPIC 00006: S-Par 2 Couplers Per Port 1 VST Switching (Scan Mode) Class

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `S-Par-2-Couplers-Per-Port-1-VST-Switching-(Scan-Mode)-Class.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/S-Par-2-Couplers-Per-Port-1-VST-Switching-(Scan-Mode)-Class.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class is the base class for 2 couplers per port 1 VST, solid state switch setup. To implement your own switching class, inherit from this class and override the following two functions. This switching configuration should enable scanning of the switches automatically with a trigger input so tha

### S-Par 2 Couplers Per Port 1 VST
 Switching (Scan Mode) Class

This class is the base class for 2 couplers per port 1 VST, solid state switch setup.
 To implement your own switching class, inherit from this class and override the
 following two functions. This switching configuration should enable scanning of the
 switches automatically with a trigger input so that the switching path can be updated as
 needed.

#### Update Scan Status.vi

This member VI is used to make the connection based on the
 direction of the incident and the coupler selection.

[IMAGE alt='image' src='S-Par-2-Couplers-Per-Port-1-VST-Switching-(Scan-Mode)-(Update-Scan-Status).gif']

[IMAGE alt='image' src='terminals/cenum.png']
 Scanning Status

Specifies the status to set on the switches. Select from the following
 options.

| Idle | Specifies that no switching is needed. The internal status should be initialized as Idle. |
| --- | --- |
| Port 1 SOL | Scans the two couplers on Port 1, mainly for SOL calibration of Port 1. |
| Port 2 SOL | Scans the two couplers on Port 2, mainly for SOL calibration of Port 2. |
| Through/DUT | Scans the 2 port measurements for through calibration or DUT measurements. |

[IMAGE alt='image' src='terminals/cbool.png']
 Status Changed

Returns TRUE when a change in the scanning status occurs after this VI is
 called. Returns FALSE when the scanning status is unchanged
 after this VI is called.

#### Close
 Object.vi

This member VI is used to close all the sessions opened for the
 switches or DIO modules to control external switches.

[IMAGE alt='image' src='S-Par-2-Couplers-Per-Port-1-VST-Switching-(Close-Object).gif']

#### Initialize

Other than these two functions, you may also need to create an
 initialize function to create a new switching object, as shown in the following
 example. You will need to open the sessions for all the modules used for switching,
 check if the configuration is valid, and create a data value reference for the class
 object so that it can be used in the S-parameter Measurement
 API.

[IMAGE alt='image' src='S-Par-2-Couplers-Per-Port-1-VST-Switching-(Scan-Mode)-(Init).gif']

Parent topic:

S-Parameter Switching Configuration Class

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=S-Par-2-Couplers-Per-Port-1-VST-Switching-Class.html language=enus -->
## TOPIC 00007: S-Par 2 Couplers Per Port 1 VST Switching Class

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `S-Par-2-Couplers-Per-Port-1-VST-Switching-Class.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/S-Par-2-Couplers-Per-Port-1-VST-Switching-Class.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class is the base class for 2 couplers per port 1 VST setup. To implement your own switching class, inherit from this class and override the following two functions. Connect.vi This member VI is used to make the connection based on the direction of the incident and the coupler selection. Incide

### S-Par 2 Couplers Per Port 1 VST Switching Class

This class is the base class for 2 couplers per port 1 VST setup. To implement your own
 switching class, inherit from this class and override the following two
 functions.

#### Connect.vi

This member VI is used to make the connection based on the
 direction of the incident and the coupler selection.

[IMAGE alt='image' src='S-Par-2-Couplers-Per-Port-1-VST-Switching-(Connect).gif']

[IMAGE alt='image' src='terminals/cenum.png']
 Incident Selection

[IMAGE alt='image' src='terminals/cenum.png']
 Coupler Selection

Specifies the coupler to measure.

#### Close
 Object.vi

This member VI is used to close all the sessions opened for the
 switches or DIO modules to control external switches.

[IMAGE alt='image' src='S-Par-2-Couplers-Per-Port-1-VST-Switching-(Close-Object).gif']

#### Initialize

Other than these two functions, you may also need to create an
 initialize function to create a new switching object, as shown in the following
 example. You will need to open the sessions for all the modules used for switching,
 check if the configuration is valid, and create a data value reference for the class
 object so that it can be used in the S-parameter Measurement
 API.

[IMAGE alt='image' src='S-Par-2-Couplers-Per-Port-1-VST-Switching-(Init).gif']

Parent topic:

S-Parameter Switching Configuration Class

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=S-Par-S11-2-Couplers-Switching-Class.html language=enus -->
## TOPIC 00008: S-Par S11 2 Couplers Switching Class

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `S-Par-S11-2-Couplers-Switching-Class.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/S-Par-S11-2-Couplers-Switching-Class.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class is the base class for the S11 2 couplers setup. To implement your own switching class, inherit from this class and override the following two functions. Connect.vi This member VI is used to make the connection based on the direction of the incident and the coupler selection. Coupler Selec

### S-Par S11 2 Couplers Switching Class

This class is the base class for the S11 2 couplers setup. To implement your own
 switching class, inherit from this class and override the following two
 functions.

#### Connect.vi

This member VI is used to make the connection based on the
 direction of the incident and the coupler selection.

[IMAGE alt='image' src='S-Par-S11-2-Couplers-(Connect).gif']

[IMAGE alt='image' src='terminals/cenum.png']
 Coupler Selection

Specifies the coupler to measure.

#### Close Object.vi

This member VI is used to close all the sessions opened for the
 switches or DIO modules to control external switches.

[IMAGE alt='image' src='S-Par-2-Couplers-Per-Port-1-VST-Switching-(Close-Object).gif']

#### Initialize

Other than these two functions, you may also need to create an
 initialize function to create a new switching object, as shown in the following
 example. You will need to open the sessions for all the modules used for switching,
 check if the configuration is valid, and create a data value reference for the class
 object so that it can be used in the S-parameter Measurement
 API.

[IMAGE alt='image' src='S-Par-S11-2-Couplers-(Init).gif']

Parent topic:

S-Parameter Switching Configuration Class

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=S-Parameter-Switching-Configuration-Class.html language=enus -->
## TOPIC 00009: S-Parameter Switching Configuration Class

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `S-Parameter-Switching-Configuration-Class.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/S-Parameter-Switching-Configuration-Class.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `concept`
- source_description: The S-Parameter Switching Configuration class is a plugin that includes one base class for each setup which require switches. The S-Parameter Switching Configuration class is located in the labview\vi.lib\niSPML\Switching directory for LabVIEW 2023 and older. The S-Parameter Switching Configuration

### S-Parameter Switching Configuration Class

The S-Parameter Switching Configuration class is a plugin that includes one base
 class for each setup which require switches. The S-Parameter Switching Configuration
 class is located in the
 labview\vi.lib\niSPML\Switching
 directory for LabVIEW 2023 and older. The S-Parameter Switching Configuration
 class is located in the
 c:\program files\NI\LVAddons\niSPML\1\vi.lib\niSPML\Switching directory for LabVIEW 2024 and newer.
 directory for LabVIEW 2024 and later.

S-Par Switching.lvlib includes base classes for
 one-coupler-per-port, single VST setups, two-couplers-per-port, single VST setups, S11
 two couplers setups, and two-couplers-per-port, single VST (solid state switch)
 setups.

By inheriting the corresponding base class, you can create a switching configuration class
 that uses your own switches for S-parameter measurements. Refer to the
 labview\examples\niSPML\SubVIs\Switching for S-Parameters
 directory for example VIs that demonstrate how to implement the switching configuration
 classes in LabVIEW 2023 and older. Refer to the
 c:\program files\NI\LVAddons\niSPML\1\examples\niSPML\SubVIs\Switching for S-Parameters
 directory for example VIs that demonstrate how to implement the switching configuration
 classes in LabVIEW 2024 and later.

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/calibrate-s-parameters-vi.html language=enus -->
## TOPIC 00010: Calibrate S-Parameters VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/calibrate-s-parameters-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/calibrate-s-parameters-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs calibration on the measurement system. Before using this VI, use the Get Calibration Actions VI to get all the steps required for your measurement topology and execute each action. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-paramet

### Calibrate S-Parameters VI

Performs calibration on the measurement system. Before using this VI, use the **Get Calibration Actions** VI to get all the steps required for your measurement topology and execute each action.

[IMAGE alt='icon' src='calibrate-s-parameters-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Calibration Action — Specifies the calibration action to perform. Obtain this string using the Get Calibration Actions VI. The default value is an empty string. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/close-vi.html language=enus -->
## TOPIC 00011: Close VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/close-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/close-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the S-parameter measurement session. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Error conditions that occur before this node runs. This input provides standard error in functio

### Close VI

Closes the S-parameter measurement session.

[IMAGE alt='icon' src='close-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

S-Parameter Measurement

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/commit-vi.html language=enus -->
## TOPIC 00012: Commit VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/commit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/commit-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits the configured parameters to the hardware. Call this VI after all configuration VIs and before the Load Calibration VI for proper operation. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png

### Commit VI

Commits the configured parameters to the hardware. Call this VI after all configuration VIs and before the **Load Calibration** VI for proper operation.

[IMAGE alt='icon' src='commit-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

S-Parameter Measurement

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-averaging-vi.html language=enus -->
## TOPIC 00013: Configure Averaging VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-averaging-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the averaging technique used to calculate the S-parameter for the instrument. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. ci32.png Averaging Enabled Specifies whether averaging is enabled or disabled

### Configure Averaging VI

Configures the averaging technique used to calculate the S-parameter for the instrument.

[IMAGE alt='icon' src='configure-averaging-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Averaging Enabled — Specifies whether averaging is enabled or disabled. The default value is FALSE. Averaging Count — Specifies the averaging count. When you set the Averaging Type parameter to Per Sweep, this value defines the number of sweeps. When you set the Averaging Type parameter to Per Point, this value defines the number of records collected at each frequency step. Averaging Type — Specifies the type of averaging to perform. The default value is Per Sweep. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-calibration-method-vi.html language=enus -->
## TOPIC 00014: Configure Calibration Method VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-calibration-method-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-calibration-method-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the calibration method to use for the S-parameter measurement. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. ci32.png Calibration Method Specifies the supported calibration method based on the measurement to

### Configure Calibration Method VI

Sets the calibration method to use for the S-parameter measurement.

[IMAGE alt='icon' src='configure-calibration-method-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Calibration Method — Specifies the supported calibration method based on the measurement topology. The default value is None. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-calibration-standards-file-paths-vi.html language=enus -->
## TOPIC 00015: Configure Calibration Standards File Paths VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-calibration-standards-file-paths-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-calibration-standards-file-paths-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the locations of the short, open, and load standard characterization files that are used in the system-wide calibration. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cpath.png Short s1p File Path Spec

### Configure Calibration Standards File Paths VI

Configures the locations of the short, open, and load standard characterization files that are used in the system-wide calibration.

[IMAGE alt='icon' src='configure-calibration-standards-file-paths-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Short s1p File Path — Specifies the location of the short s1p file used for calibration. The default value is empty. Open s1p File Path — Specifies the location of the open s1p file used for calibration. The default value is empty. Load s1p File Path — Specifies the location of the load s1p file used for calibration. The default value is empty. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-calibration-through-file-path-vi.html language=enus -->
## TOPIC 00016: Configure Calibration Through File Path VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-calibration-through-file-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-calibration-through-file-path-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the location of the through adapter calibration file that is used in the system-wide calibration. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cpath.png Through s2p File Path Specifies the location of

### Configure Calibration Through File Path VI

Configures the location of the through adapter calibration file that is used in the system-wide calibration.

[IMAGE alt='icon' src='configure-calibration-through-file-path-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Through s2p File Path — Specifies the location of the through s2p file used for calibration. The default value is empty. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-external-gain-vi.html language=enus -->
## TOPIC 00017: Configure External Gain VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-external-gain-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-external-gain-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the maximum gain of all the paths from VST RFout to RFin so you can set the appropriate reference level for the measurements. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cdbl.png External Gain (dB) S

### Configure External Gain VI

Configures the maximum gain of all the paths from VST RFout to RFin so you can set the appropriate reference level for the measurements.

[IMAGE alt='icon' src='configure-external-gain-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. External Gain (dB) — Specifies the expected gain between the generation and analysis ports of the VST(s). This value should include attenuation in cabling, couplers, and other signal conditioning between the transmission and analysis ports of the VST. The default value is -30 dB. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-frequency-range-vi.html language=enus -->
## TOPIC 00018: Configure Frequency Range VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-frequency-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-frequency-range-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency range used for S-parameter measurements. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cdbl.png Start Frequency (Hz) Specifies the beginning frequency of the stimulus to be applied to the

### Configure Frequency Range VI

Configures the frequency range used for S-parameter measurements.

[IMAGE alt='icon' src='configure-frequency-range-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Start Frequency (Hz) — Specifies the beginning frequency of the stimulus to be applied to the DUT. The default value is 5 GHz. Frequency Step (Hz) — Specifies the frequency step size of the stimulus to be applied to the DUT. The default value is 50 MHz. Stop Frequency (Hz) — Specifies the ending frequency of the stimulus to be applied to the DUT. The default value is 5.5 GHz. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-if-bandwidth-vi.html language=enus -->
## TOPIC 00019: Configure IF Bandwidth VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-if-bandwidth-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-if-bandwidth-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the IF bandwidth of the measurement. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cdbl.png IF Bandwidth (Hz) Specifies the IF bandwidth of the measurement. When the IF bandwidth is reduced, noise take

### Configure IF Bandwidth VI

Configures the IF bandwidth of the measurement.

[IMAGE alt='icon' src='configure-if-bandwidth-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. IF Bandwidth (Hz) — Specifies the IF bandwidth of the measurement. When the IF bandwidth is reduced, noise taken into the measurement decreases and the measurement time increases. The default value is 1 kHz. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-rfsg-attenuation-constant-vi.html language=enus -->
## TOPIC 00020: Configure RFSG Attenuation (Constant) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-rfsg-attenuation-constant-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-rfsg-attenuation-constant-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a single value to compensate for the attenuation on the signal path from VST RF out to the ports connected to the DUT. icon Inputs/Outputs cenum.png Path Selection Specifies the path to apply the attenuation setting. cdatavalref.png S-Par Reference In Specifies the session reference handle

### Configure RFSG Attenuation (Constant) VI

Specifies a single value to compensate for the attenuation on the signal path from VST RF out to the ports connected to the DUT.

[IMAGE alt='icon' src='configure-rfsg-attenuation-constant-vi.png']

#### Inputs/Outputs

| Path Selection — Specifies the path to apply the attenuation setting. S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Tx Constant Attenuation (dB) — Specifies the constant attenuation value applied to the RFSG session. For example, if the attenuation is set to 1 dB and the Configure RFSG Power Level VI Power Level (dBm) input is set to 0 dBm, the actual power level at the VST RFout port is 1 dBm to compensate for the attenuation on the signal path. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure RFSG Attenuation VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-rfsg-attenuation-vi.html language=enus -->
## TOPIC 00021: Configure RFSG Attenuation VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-rfsg-attenuation-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-rfsg-attenuation-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RFSG attenuation type so that the power level at the DUT port is corrected to match the same power level set by the Configure RFSG Power Level VI. icon

### Configure RFSG Attenuation VI

Configures the RFSG attenuation type so that the power level at the DUT port is corrected to match the same power level set by the **Configure RFSG Power Level** VI.

[IMAGE alt='icon' src='configure-rfsg-attenuation-vi.png']

- [Configure RFSG Attenuation (Constant) VI](../../vi-lib/nispml/configure-rfsg-attenuation-constant-vi.html) Specifies a single value to compensate for the attenuation on the signal path from VST RF out to the ports connected to the DUT.
- [Configure RFSG Attenuation (XML File) VI](../../vi-lib/nispml/configure-rfsg-attenuation-xml-file-vi.html) Specifies the attenuation to the RFSG session for the path from VST RF out to the ports connected to the DUT. The path is based on the RFSG system calibration XML file created using the RF System Calibration Assistant. Use the RF System Calibration Assistant to save multiple generator path calibrations in a single XML file. Specify the path to use with the RFSG Attenuation Path Name input. Although the RF System Calibration Assistant allows you to calibrate one path at multiple power levels for the same frequency, this API only supports calibrations done at one power level for each frequency. This function returns an error if you do not wire the RFSG XML File Path input or specify an empty or relative path.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-rfsg-attenuation-xml-file-vi.html language=enus -->
## TOPIC 00022: Configure RFSG Attenuation (XML File) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-rfsg-attenuation-xml-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-rfsg-attenuation-xml-file-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation to the RFSG session for the path from VST RF out to the ports connected to the DUT. The path is based on the RFSG system calibration XML file created using the RF System Calibration Assistant. Use the RF System Calibration Assistant to save multiple generator path calibrati

### Configure RFSG Attenuation (XML File) VI

Specifies the attenuation to the RFSG session for the path from VST RF out to the ports connected to the DUT. The path is based on the RFSG system calibration XML file created using the RF System Calibration Assistant. Use the RF System Calibration Assistant to save multiple generator path calibrations in a single XML file. Specify the path to use with the **RFSG Attenuation Path Name** input. Although the RF System Calibration Assistant allows you to calibrate one path at multiple power levels for the same frequency, this API only supports calibrations done at one power level for each frequency. This function returns an error if you do not wire the **RFSG XML File Path** input or specify an empty or relative path.

[IMAGE alt='icon' src='configure-rfsg-attenuation-xml-file-vi.png']

#### Inputs/Outputs

| Path Selection — Specifies the path to apply the attenuation setting. S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. RFSG XML File Path — Specifies the absolute path to the XML file generated by the RF System Calibration Assistant. The default value is empty. RFSG Attenuation Path Name — Specifies the name of the generator path to use. This path is specified by the XML file created with the RF System Calibration Assistant. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure RFSG Attenuation VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-rfsg-export-trigger-gate-vi.html language=enus -->
## TOPIC 00023: Configure RFSG Export Trigger (Gate) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-rfsg-export-trigger-gate-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-rfsg-export-trigger-gate-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures RFSG to export a gated trigger, and configures the parameters for the trigger. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cstr.png Trigger Output Specifies the terminal on which to export a trigger.

### Configure RFSG Export Trigger (Gate) VI

Configures RFSG to export a gated trigger, and configures the parameters for the trigger.

[IMAGE alt='icon' src='configure-rfsg-export-trigger-gate-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Trigger Output — Specifies the terminal on which to export a trigger. Enter a valid terminal (PFI0,1,2,3, PXI_Trig0-7, PXI_STAR, PXIe_DStarC, or TrigIN) or leave empty. The default value is Do not export signal (not set). Pre-trigger Time (s) — Specifies the time, in seconds, to wait before the rising edge of the pulse to toggle the gated trigger as high. Post-trigger Time (s) — Specifies the time, in seconds, to wait after the falling edge of the pulse to toggle the gated trigger as low. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure RFSG Export Trigger VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-rfsg-export-trigger-none-vi.html language=enus -->
## TOPIC 00024: Configure RFSG Export Trigger (None) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-rfsg-export-trigger-none-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-rfsg-export-trigger-none-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures RFSG to not export a trigger. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Error conditions that occur before this node runs. This input provides standard error in functional

### Configure RFSG Export Trigger (None) VI

Configures RFSG to not export a trigger.

[IMAGE alt='icon' src='configure-rfsg-export-trigger-none-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure RFSG Export Trigger VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-rfsg-export-trigger-pulse-vi.html language=enus -->
## TOPIC 00025: Configure RFSG Export Trigger (Pulse) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-rfsg-export-trigger-pulse-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-rfsg-export-trigger-pulse-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures RFSG to export a pulse trigger and specifies the terminal on which RFSG exports the trigger. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cstr.png Trigger Output Specifies the terminal on which to exp

### Configure RFSG Export Trigger (Pulse) VI

Configures RFSG to export a pulse trigger and specifies the terminal on which RFSG exports the trigger.

[IMAGE alt='icon' src='configure-rfsg-export-trigger-pulse-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Trigger Output — Specifies the terminal on which to export a trigger. Enter a valid terminal (PFI0,1,2,3, PXI_Trig0-7, PXI_STAR, PXIe_DStarC, or TrigIN) or leave empty. The default value is Do not export signal (not set). error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure RFSG Export Trigger VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-rfsg-export-trigger-vi.html language=enus -->
## TOPIC 00026: Configure RFSG Export Trigger VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-rfsg-export-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-rfsg-export-trigger-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type and source of the trigger to export for each pulse. This configuration supports the 2 couplers per port 1 VST with solid state switch setup. If the trigger is not configured, or configured for an unsupported setup, no trigger is exported. icon

### Configure RFSG Export Trigger VI

Configures the type and source of the trigger to export for each pulse. This configuration supports the 2 couplers per port 1 VST with solid state switch setup. If the trigger is not configured, or configured for an unsupported setup, no trigger is exported.

[IMAGE alt='icon' src='configure-rfsg-export-trigger-vi.png']

- [Configure RFSG Export Trigger (Pulse) VI](../../vi-lib/nispml/configure-rfsg-export-trigger-pulse-vi.html) Configures RFSG to export a pulse trigger and specifies the terminal on which RFSG exports the trigger.
- [Configure RFSG Export Trigger (Gate) VI](../../vi-lib/nispml/configure-rfsg-export-trigger-gate-vi.html) Configures RFSG to export a gated trigger, and configures the parameters for the trigger.
- [Configure RFSG Export Trigger (None) VI](../../vi-lib/nispml/configure-rfsg-export-trigger-none-vi.html) Configures RFSG to not export a trigger.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-rfsg-power-level-vi.html language=enus -->
## TOPIC 00027: Configure RFSG Power Level VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-rfsg-power-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-rfsg-power-level-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power level used to calculate the S-parameter measurement. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cdbl.png Power Level (dBm) Specifies the power level of the RF signal to generate. The defau

### Configure RFSG Power Level VI

Configures the power level used to calculate the S-parameter measurement.

[IMAGE alt='icon' src='configure-rfsg-power-level-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Power Level (dBm) — Specifies the power level of the RF signal to generate. The default value is 0 dBm. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-start-trigger-input-vi.html language=enus -->
## TOPIC 00028: Configure Start Trigger Input VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-start-trigger-input-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-start-trigger-input-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the trigger to start the S-parameter measurement. The measurement is complete when there is a rising edge on the assigned trigger. This configuration only supports the 2 couplers per port 1 VST with solid state switch setup. If the trigger is not configured or configured for an unsupporte

### Configure Start Trigger Input VI

Configures the trigger to start the S-parameter measurement. The measurement is complete when there is a rising edge on the assigned trigger. This configuration only supports the 2 couplers per port 1 VST with solid state switch setup. If the trigger is not configured or configured for an unsupported setup the measurement is performed immediately after initiated.

[IMAGE alt='icon' src='configure-start-trigger-input-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Start Trigger Input — Specifies the terminal on which the S-parameter session looks for a start trigger. The default value is None. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-stimulus-cw-vi.html language=enus -->
## TOPIC 00029: Configure Stimulus (CW) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-stimulus-cw-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-stimulus-cw-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the stimulus as a continuous wave. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Error conditions that occur before this node runs. This input provides standard error in function

### Configure Stimulus (CW) VI

Defines the stimulus as a continuous wave.

[IMAGE alt='icon' src='configure-stimulus-cw-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Stimulus VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-stimulus-pulsed-cw-vi.html language=enus -->
## TOPIC 00030: Configure Stimulus (Pulsed CW) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-stimulus-pulsed-cw-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-stimulus-pulsed-cw-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the stimulus as a pulsed continuous wave and configures the wave. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cdbl.png Pulse Width (s) Specifies the pulse width. The default value is 10 us. cdbl.png PRI

### Configure Stimulus (Pulsed CW) VI

Defines the stimulus as a pulsed continuous wave and configures the wave.

[IMAGE alt='icon' src='configure-stimulus-pulsed-cw-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Pulse Width (s) — Specifies the pulse width. The default value is 10 us. PRI (s) — Specifies the pulse repetition interval (PRI). The default value is 1 ms. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Stimulus VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-stimulus-vi.html language=enus -->
## TOPIC 00031: Configure Stimulus VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-stimulus-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-stimulus-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the type of RF signal used to stimulate the DUT. icon

### Configure Stimulus VI

Defines the type of RF signal used to stimulate the DUT.

[IMAGE alt='icon' src='configure-stimulus-vi.png']

- [Configure Stimulus (CW) VI](../../vi-lib/nispml/configure-stimulus-cw-vi.html) Defines the stimulus as a continuous wave.
- [Configure Stimulus (Pulsed CW) VI](../../vi-lib/nispml/configure-stimulus-pulsed-cw-vi.html) Defines the stimulus as a pulsed continuous wave and configures the wave.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-topology-1cperport1vst-vi.html language=enus -->
## TOPIC 00032: Configure Topology (1CperPort1VST) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-topology-1cperport1vst-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-topology-1cperport1vst-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the S-parameter measurement to use one VST with one coupler per port. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. civrn.png NI RFSG Session Specifies the name of the NI-RFSG session being used. The d

### Configure Topology (1CperPort1VST) VI

Configures the S-parameter measurement to use one VST with one coupler per port.

[IMAGE alt='icon' src='configure-topology-1cperport1vst-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. NI RFSG Session — Specifies the name of the NI-RFSG session being used. The default value is empty. NI RFmx Session — Specifies the name of the NI-RFmx session being used. The default value is empty. Switch Reference — Specifies the class instance of the switch. Refer to S-Parameter Switching Configuration Class for more information. The default value is empty. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Topology VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-topology-1cperport1vsts21-vi.html language=enus -->
## TOPIC 00033: Configure Topology (1CperPort1VSTS21) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-topology-1cperport1vsts21-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-topology-1cperport1vsts21-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the S21 measurement to use one VST. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. civrn.png NI RFSG Session Specifies the name of the NI-RFSG session being used. The default value is empty. cpoly.png N

### Configure Topology (1CperPort1VSTS21) VI

Configures the S21 measurement to use one VST.

[IMAGE alt='icon' src='configure-topology-1cperport1vsts21-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. NI RFSG Session — Specifies the name of the NI-RFSG session being used. The default value is empty. NI RFmx Session — Specifies the name of the NI-RFmx session being used. The default value is empty. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Topology VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-topology-1cperport2vst-vi.html language=enus -->
## TOPIC 00034: Configure Topology (1CperPort2VST) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-topology-1cperport2vst-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-topology-1cperport2vst-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the S-parameter measurement to use two VSTs with one coupler per port. icon Inputs/Outputs cpoly.png NI RFmx Session Instr 2 Specifies the NI-RFmx session name associated with the VST connected to Port 2 of the DUT. The default value is empty. civrn.png NI RFSG Session Instr 2 Specifies t

### Configure Topology (1CperPort2VST) VI

Configures the S-parameter measurement to use two VSTs with one coupler per port.

[IMAGE alt='icon' src='configure-topology-1cperport2vst-vi.png']

#### Inputs/Outputs

| NI RFmx Session Instr 2 — Specifies the NI-RFmx session name associated with the VST connected to Port 2 of the DUT. The default value is empty. NI RFSG Session Instr 2 — Specifies the NI-RFSG session name associated with the VST connected to Port 2 of the DUT. The default value is empty. S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. NI RFSG Session Instr 1 — Specifies the NI-RFSG session name associated with the VST connected to Port 1 of the DUT. The default value is empty. NI RFmx Session Instr 1 — Specifies the NI-RFmx session name associated with the VST connected to Port 1 of the DUT. The default value is empty. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Topology VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-topology-2cperport1vst-solid-state-switch-vi.html language=enus -->
## TOPIC 00035: Configure Topology (2CperPort1VST, Solid State Switch) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-topology-2cperport1vst-solid-state-switch-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-topology-2cperport1vst-solid-state-switch-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the S-parameter measurement to use one 1 VST solid state switch with two couplers per port. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. civrn.png NI RFSG Session Specifies the name of the NI-RFSG ses

### Configure Topology (2CperPort1VST, Solid State Switch) VI

Configures the S-parameter measurement to use one 1 VST solid state switch with two couplers per port.

[IMAGE alt='icon' src='configure-topology-2cperport1vst-solid-state-switch-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. NI RFSG Session — Specifies the name of the NI-RFSG session being used. The default value is empty. NI RFmx Session — Specifies the name of the NI-RFmx session being used. The default value is empty. Switch Reference — Specifies the class instance of the switch. Refer to S-Parameter Switching Configuration Class for more information. The default value is empty. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Topology VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-topology-2cperport1vst-vi.html language=enus -->
## TOPIC 00036: Configure Topology (2CperPort1VST) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-topology-2cperport1vst-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-topology-2cperport1vst-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the S-parameter measurement to use one VST with two couplers per port. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. civrn.png NI RFSG Session Specifies the name of the NI-RFSG session being used. The

### Configure Topology (2CperPort1VST) VI

Configures the S-parameter measurement to use one VST with two couplers per port.

[IMAGE alt='icon' src='configure-topology-2cperport1vst-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. NI RFSG Session — Specifies the name of the NI-RFSG session being used. The default value is empty. NI RFmx Session — Specifies the name of the NI-RFmx session being used. The default value is empty. Switch Reference — Specifies the class instance of the switch. Refer to S-Parameter Switching Configuration Class for more information. The default value is empty. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Topology VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-topology-s11-1coupler-vi.html language=enus -->
## TOPIC 00037: Configure Topology (S11_1Coupler) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-topology-s11-1coupler-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-topology-s11-1coupler-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the S-parameter measurement to use S11 with one coupler. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. civrn.png NI RFSG Session Specifies the name of the NI-RFSG session being used. The default value

### Configure Topology (S11_1Coupler) VI

Configures the S-parameter measurement to use S11 with one coupler.

[IMAGE alt='icon' src='configure-topology-s11-1coupler-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. NI RFSG Session — Specifies the name of the NI-RFSG session being used. The default value is empty. NI RFmx Session — Specifies the name of the NI-RFmx session being used. The default value is empty. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Topology VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-topology-s11-2couplers-vi.html language=enus -->
## TOPIC 00038: Configure Topology (S11_2Couplers) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-topology-s11-2couplers-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-topology-s11-2couplers-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the S-parameter measurement to use S11 with two couplers. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. civrn.png NI RFSG Session Specifies the name of the NI-RFSG session being used. The default value

### Configure Topology (S11_2Couplers) VI

Configures the S-parameter measurement to use S11 with two couplers.

[IMAGE alt='icon' src='configure-topology-s11-2couplers-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. NI RFSG Session — Specifies the name of the NI-RFSG session being used. The default value is empty. NI RFmx Session — Specifies the name of the NI-RFmx session being used. The default value is empty. Switch Reference — Specifies the class instance of the switch. Refer to S-Parameter Switching Configuration Class for more information. The default value is empty. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Topology VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-topology-vi.html language=enus -->
## TOPIC 00039: Configure Topology VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-topology-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-topology-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type of NI and third party hardware configuration used to calculate S-parameters. Refer to the S-Parameter Measurement Library User Manual for details about each topology. icon

### Configure Topology VI

Configures the type of NI and third party hardware configuration used to calculate S-parameters.

Refer to the [S-Parameter Measurement Library User
Manual](https://www.ni.com/docs/en-US/bundle/s-parameter-measurement-library/page/user-manual-welcome) for details about each topology.

[IMAGE alt='icon' src='configure-topology-vi.png']

- [Configure Topology (1CperPort1VST) VI](../../vi-lib/nispml/configure-topology-1cperport1vst-vi.html) Configures the S-parameter measurement to use one VST with one coupler per port.
- [Configure Topology (2CperPort1VST) VI](../../vi-lib/nispml/configure-topology-2cperport1vst-vi.html) Configures the S-parameter measurement to use one VST with two couplers per port.
- [Configure Topology (2CperPort1VST, Solid State Switch) VI](../../vi-lib/nispml/configure-topology-2cperport1vst-solid-state-switch-vi.html) Configures the S-parameter measurement to use one 1 VST solid state switch with two couplers per port.
- [Configure Topology (1CperPort2VST) VI](../../vi-lib/nispml/configure-topology-1cperport2vst-vi.html) Configures the S-parameter measurement to use two VSTs with one coupler per port.
- [Configure Topology (1CperPort1VSTS21) VI](../../vi-lib/nispml/configure-topology-1cperport1vsts21-vi.html) Configures the S21 measurement to use one VST.
- [Configure Topology (S11_1Coupler) VI](../../vi-lib/nispml/configure-topology-s11-1coupler-vi.html) Configures the S-parameter measurement to use S11 with one coupler.
- [Configure Topology (S11_2Couplers) VI](../../vi-lib/nispml/configure-topology-s11-2couplers-vi.html) Configures the S-parameter measurement to use S11 with two couplers.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/configure-trl-calibration-vi.html language=enus -->
## TOPIC 00040: Configure TRL Calibration VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/configure-trl-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/configure-trl-calibration-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures configuration options for TRL calibration. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. ccclst.png TRL Calibration Configuration Specifies configuration options for TRL calibration. cenum.png Reflecti

### Configure TRL Calibration VI

Configures configuration options for TRL calibration.

[IMAGE alt='icon' src='configure-trl-calibration-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. TRL Calibration Configuration — Specifies configuration options for TRL calibration. Reflection Type — Specifies the type of reflection to use for the reflection step. Short: Performs the reflection step with a short standard. Open: Performs the reflection step with an open standard. Line Delays (ps) — Specifies the delay of the lines used for the calibration, in ps. Up to 2 delay lines are supported. If more than 2 delays are specified the calibration errors out. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |
| Reflection Type — Specifies the type of reflection to use for the reflection step. Short: Performs the reflection step with a short standard. Open: Performs the reflection step with an open standard. Line Delays (ps) — Specifies the delay of the lines used for the calibration, in ps. Up to 2 delay lines are supported. If more than 2 delays are specified the calibration errors out. |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/fetch-s-parameters-all-complex-vi.html language=enus -->
## TOPIC 00041: Fetch S-Parameters (All Complex) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/fetch-s-parameters-all-complex-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/fetch-s-parameters-all-complex-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches all S-parameters in a measurement. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Error conditions that occur before this node runs. This input provides standard error in function

### Fetch S-Parameters (All Complex) VI

Fetches all S-parameters in a measurement.

[IMAGE alt='icon' src='fetch-s-parameters-all-complex-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. S-Parameters — Returns all four S-parameter measurements, expressed as a 2D array of complex numbers. Each row of the 2D array is the S-parameter at a frequency point, corresponding to the element at the same array index of the Frequency (Hz) output. The columns of the 2D array are ordered as S11, S21, S12 and S22. Frequency (Hz) — Returns the frequency of the specified S-parameter. This value is expressed in Hz. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Fetch S-Parameters VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/fetch-s-parameters-complex-vi.html language=enus -->
## TOPIC 00042: Fetch S-parameters (Complex) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/fetch-s-parameters-complex-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/fetch-s-parameters-complex-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the frequency and the complex number of a single S-parameter measurement. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cenum.png S-Parameter Selection Specifies which S-parameter measurement the VI fetch

### Fetch S-parameters (Complex) VI

Fetches the frequency and the complex number of a single S-parameter measurement.

[IMAGE alt='icon' src='fetch-s-parameters-complex-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. S-Parameter Selection — Specifies which S-parameter measurement the VI fetches. The default value is S11. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. S-Parameters — Returns a single S-parameter measurement. This value is expressed as a complex number. Frequency (Hz) — Returns the frequency of the specified S-parameter. This value is expressed in Hz. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Fetch S-Parameters VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/fetch-s-parameters-mag-phase-vi.html language=enus -->
## TOPIC 00043: Fetch S-Parameters (Mag-Phase) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/fetch-s-parameters-mag-phase-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/fetch-s-parameters-mag-phase-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the frequency, magnitude, and phase of a single S-parameter measurement. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cenum.png S-Parameter Selection Specifies which S-parameter measurement the VI fetche

### Fetch S-Parameters (Mag-Phase) VI

Fetches the frequency, magnitude, and phase of a single S-parameter measurement.

[IMAGE alt='icon' src='fetch-s-parameters-mag-phase-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. S-Parameter Selection — Specifies which S-parameter measurement the VI fetches. The default value is S11. Magnitude Format — Specifies the format of the magnitude for the given S-parameter measurement. The default value is Log Magnitude (dB). error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. Magnitude — Returns the magnitude of the specified S-parameter. This value is expressed in units as defined by the Magnitude Format input. Phase — Returns the phase of the specified S-parameter. This value is expressed in degrees. Frequency (Hz) — Returns the frequency of the specified S-parameter. This value is expressed in Hz. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Fetch S-Parameters VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/fetch-s-parameters-vi.html language=enus -->
## TOPIC 00044: Fetch S-Parameters VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/fetch-s-parameters-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/fetch-s-parameters-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the calculated S-parameter measurement. icon

### Fetch S-Parameters VI

Fetches the calculated S-parameter measurement.

[IMAGE alt='icon' src='fetch-s-parameters-vi.png']

- [Fetch S-Parameters (Mag-Phase) VI](../../vi-lib/nispml/fetch-s-parameters-mag-phase-vi.html) Fetches the frequency, magnitude, and phase of a single S-parameter measurement.
- [Fetch S-parameters (Complex) VI](../../vi-lib/nispml/fetch-s-parameters-complex-vi.html) Fetches the frequency and the complex number of a single S-parameter measurement.
- [Fetch S-Parameters (All Complex) VI](../../vi-lib/nispml/fetch-s-parameters-all-complex-vi.html) Fetches all S-parameters in a measurement.

Parent topic:

S-Parameter Measurement

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/get-calibration-actions-vi.html language=enus -->
## TOPIC 00045: Get Calibration Actions VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/get-calibration-actions-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/get-calibration-actions-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches all the calibration actions to perform. Use this VI before executing the calibration actions using the Calibrate S-Parameters VI. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Er

### Get Calibration Actions VI

Fetches all the calibration actions to perform. Use this VI before executing the calibration actions using the **Calibrate S-Parameters** VI.

[IMAGE alt='icon' src='get-calibration-actions-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. Calibration Actions — Returns the calibration actions, expressed as an array of strings to perform. Wire this output to the Calibrate S-Parameters VI. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/get-calibration-measurement-vi.html language=enus -->
## TOPIC 00046: Get Calibration Measurement VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/get-calibration-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/get-calibration-measurement-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the raw calibration measurements for various calibration methods. Refer to the SOLT Measurements output and TRL Measurements output for details. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.

### Get Calibration Measurement VI

Fetches the raw calibration measurements for various calibration methods. Refer to the **SOLT Measurements** output and **TRL Measurements** output for details.

[IMAGE alt='icon' src='get-calibration-measurement-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. SOLT Measurements — Returns raw calibration measurements for SOLT, SOLR, and QSOLT calibration. Each element in the array is one point out of averaging count points as configured in the Configure Averaging VI. Port 1 SOL — Short, open, and load measurements from port 1 as a 2D array of complex doubles. The first index of the array selects the measurement and the second index selects the point in the frequency sweep. The order of the measurements are reference receiver short, test receiver short, reference receiver open, test receiver open, reference receiver load, and test receiver load. Port 2 SOL — Short, open, and load measurements from port 2 as a 2D array of complex doubles. The first index of the array selects the measurement and the second index selects the point in the frequency sweep. The order of the measurements are reference receiver short, test receiver short, reference receiver open, test receiver open, reference receiver load, and test receiver load. Through — The through measurement from a calibration. forward — The measurement when port 1 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. reverse — The measurement when port 2 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. TRL Measurements — Returns raw calibration measurements for TRL calibration. Each element in the array is one point out of averaging count points as configured in the Configure Averaging VI. Port 1 Reflection — Reflection measurements from port 1 as a 2D array of complex doubles. The first index of the array selects the measurement and the second index selects the point in the frequency sweep. The order of the measurements are reference receiver reflection and test receiver reflection. Port 2 Reflection — Reflection measurements from port 2 as a 2D array of complex doubles. The first index of the array selects the measurement and the second index selects the point in the frequency sweep. The order of the measurements are reference receiver reflection and test receiver reflection. Through — The through measurement from a calibration. forward — The measurement when port 1 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. reverse — The measurement when port 2 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. Lines — Line measurements as a 1D array. Each element of the array contains the measurements for one of the lines in a TRL calibration. forward — The measurement when port 1 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. reverse — The measurement when port 2 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. error out — Error information. This output provides standard error out functionality. |
| --- |
| Port 1 SOL — Short, open, and load measurements from port 1 as a 2D array of complex doubles. The first index of the array selects the measurement and the second index selects the point in the frequency sweep. The order of the measurements are reference receiver short, test receiver short, reference receiver open, test receiver open, reference receiver load, and test receiver load. Port 2 SOL — Short, open, and load measurements from port 2 as a 2D array of complex doubles. The first index of the array selects the measurement and the second index selects the point in the frequency sweep. The order of the measurements are reference receiver short, test receiver short, reference receiver open, test receiver open, reference receiver load, and test receiver load. Through — The through measurement from a calibration. forward — The measurement when port 1 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. reverse — The measurement when port 2 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. |
| forward — The measurement when port 1 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. reverse — The measurement when port 2 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. |
| In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. |
| In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. |
| Port 1 Reflection — Reflection measurements from port 1 as a 2D array of complex doubles. The first index of the array selects the measurement and the second index selects the point in the frequency sweep. The order of the measurements are reference receiver reflection and test receiver reflection. Port 2 Reflection — Reflection measurements from port 2 as a 2D array of complex doubles. The first index of the array selects the measurement and the second index selects the point in the frequency sweep. The order of the measurements are reference receiver reflection and test receiver reflection. Through — The through measurement from a calibration. forward — The measurement when port 1 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. reverse — The measurement when port 2 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. Lines — Line measurements as a 1D array. Each element of the array contains the measurements for one of the lines in a TRL calibration. forward — The measurement when port 1 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. reverse — The measurement when port 2 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. |
| forward — The measurement when port 1 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. reverse — The measurement when port 2 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. |
| In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. |
| In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. |
| forward — The measurement when port 1 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. reverse — The measurement when port 2 is generating. In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. |
| In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. |
| In Port Reference — The measurement of the reference receiver at the receiving port. In Port Test — The measurement of the test receiver at the receiving port. Out Port Reference — The measurement of the reference receiver at the generating port. Out Port Test — The measurement of the test receiver at the generating port. |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/get-calibration-status-vi.html language=enus -->
## TOPIC 00047: Get Calibration Status VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/get-calibration-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/get-calibration-status-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the calibration status of S-Parameter measurements, including whether calibration was performed on the measurement, and the timestamp when calibration was performed. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement s

### Get Calibration Status VI

Fetches the calibration status of S-Parameter measurements, including whether calibration was performed on the measurement, and the timestamp when calibration was performed.

[IMAGE alt='icon' src='get-calibration-status-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. Calibrated — Returns whether calibration was performed on the measurement. Calibration Timestamp — Returns the timestamp of the last calibration date. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/get-topology-references-1cperport1vst-vi.html language=enus -->
## TOPIC 00048: Get Topology References (1CperPort1VST) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/get-topology-references-1cperport1vst-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/get-topology-references-1cperport1vst-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the references of a 1 Coupler per Port, 1 VST measurement session. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Error conditions that occur before this node runs. This input pro

### Get Topology References (1CperPort1VST) VI

Fetches the references of a 1 Coupler per Port, 1 VST measurement session.

[IMAGE alt='icon' src='get-topology-references-1cperport1vst-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. NI RFSG Session — Returns the name of the NI-RFSG session that was used. NI RFmx Session — Returns the name of the NI-RFmx session that was used. Switch Reference — Returns the class instance of the switch. Refer to S-Parameter Switching Configuration Class for more information. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Topology References VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/get-topology-references-1cperport1vsts21-vi.html language=enus -->
## TOPIC 00049: Get Topology References (1CperPort1VSTS21) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/get-topology-references-1cperport1vsts21-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/get-topology-references-1cperport1vsts21-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the references of a 1 VST measurement session that was used for an S21 measurement only. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Error conditions that occur before this nod

### Get Topology References (1CperPort1VSTS21) VI

Fetches the references of a 1 VST measurement session that was used for an S21 measurement only.

[IMAGE alt='icon' src='get-topology-references-1cperport1vsts21-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. NI RFSG Session — Returns the name of the NI-RFSG session that was used. NI RFmx Session — Returns the name of the NI-RFmx session that was used. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Topology References VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/get-topology-references-1cperport2vst-vi.html language=enus -->
## TOPIC 00050: Get Topology References (1CperPort2VST) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/get-topology-references-1cperport2vst-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/get-topology-references-1cperport2vst-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the references of a 1 Coupler per Port, 2 VST measurement session. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Error conditions that occur before this node runs. This input pro

### Get Topology References (1CperPort2VST) VI

Fetches the references of a 1 Coupler per Port, 2 VST measurement session.

[IMAGE alt='icon' src='get-topology-references-1cperport2vst-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. NI RFSG Session Instr 2 — Returns the NI-RFSG session name associated with the VST connected to Port 2 of the DUT. NI RFmx Session Instr 2 — Returns the NI-RFmx session name associated with the VST connected to Port 2 of the DUT. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. NI RFSG Session Instr 1 — Returns the NI-RFSG session name associated with the VST connected to Port 1 of the DUT. NI RFmx Session Instr 1 — Returns the NI-RFmx session name associated with the VST connected to Port 1 of the DUT. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Topology References VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/get-topology-references-2cperport1vst-solid-state-switch-vi.html language=enus -->
## TOPIC 00051: Get Topology References (2CperPort1VST, Solid State Switch) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/get-topology-references-2cperport1vst-solid-state-switch-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/get-topology-references-2cperport1vst-solid-state-switch-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the references of a 2 Coupler per Port, 1 VST solid state switch measurement session. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Error conditions that occur before this node r

### Get Topology References (2CperPort1VST, Solid State Switch) VI

Fetches the references of a 2 Coupler per Port, 1 VST solid state switch measurement session.

[IMAGE alt='icon' src='get-topology-references-2cperport1vst-solid-state-switch-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. NI RFSG Session — Returns the name of the NI-RFSG session that was used. NI RFmx Session — Returns the name of the NI-RFmx session that was used. Switch Reference — Returns the class instance of the switch. Refer to S-Parameter Switching Configuration Class for more information. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Topology References VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/get-topology-references-2cperport1vst-vi.html language=enus -->
## TOPIC 00052: Get Topology References (2CperPort1VST) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/get-topology-references-2cperport1vst-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/get-topology-references-2cperport1vst-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the references of a 2 Coupler per Port, 1 VST measurement session. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Error conditions that occur before this node runs. This input pro

### Get Topology References (2CperPort1VST) VI

Fetches the references of a 2 Coupler per Port, 1 VST measurement session.

[IMAGE alt='icon' src='get-topology-references-2cperport1vst-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. NI RFSG Session — Returns the name of the NI-RFSG session that was used. NI RFmx Session — Returns the name of the NI-RFmx session that was used. Switch Reference — Returns the class instance of the switch. Refer to S-Parameter Switching Configuration Class for more information. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Topology References VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/get-topology-references-s11-1coupler-vi.html language=enus -->
## TOPIC 00053: Get Topology References (S11_1Coupler) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/get-topology-references-s11-1coupler-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/get-topology-references-s11-1coupler-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the references of an S11, 1 Coupler measurement session. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Error conditions that occur before this node runs. This input provides stan

### Get Topology References (S11_1Coupler) VI

Fetches the references of an S11, 1 Coupler measurement session.

[IMAGE alt='icon' src='get-topology-references-s11-1coupler-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. NI RFSG Session — Returns the name of the NI-RFSG session that was used. NI RFmx Session — Returns the name of the NI-RFmx session that was used. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Topology References VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/get-topology-references-s11-2couplers-vi.html language=enus -->
## TOPIC 00054: Get Topology References (S11_2Couplers) VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/get-topology-references-s11-2couplers-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/get-topology-references-s11-2couplers-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the references of an S11, 2 Couplers measurement session. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Error conditions that occur before this node runs. This input provides sta

### Get Topology References (S11_2Couplers) VI

Fetches the references of an S11, 2 Couplers measurement session.

[IMAGE alt='icon' src='get-topology-references-s11-2couplers-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. NI RFSG Session — Returns the name of the NI-RFSG session that was used. NI RFmx Session — Returns the name of the NI-RFmx session that was used. Switch Reference — Returns the class instance of the switch. Refer to S-Parameter Switching Configuration Class for more information. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Topology References VI

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/get-topology-references-vi.html language=enus -->
## TOPIC 00055: Get Topology References VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/get-topology-references-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/get-topology-references-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the RFmx and RFSG references of the current S-parameter measurement session. Refer to the S-Parameter Measurement Library User Manual for details about each topology. icon

### Get Topology References VI

Fetches the RFmx and RFSG references of the current S-parameter measurement session.

Refer to the [S-Parameter Measurement Library User
Manual](https://www.ni.com/docs/en-US/bundle/s-parameter-measurement-library/page/user-manual-welcome) for details about each topology.

[IMAGE alt='icon' src='get-topology-references-vi.png']

- [Get Topology References (1CperPort1VST) VI](../../vi-lib/nispml/get-topology-references-1cperport1vst-vi.html) Fetches the references of a 1 Coupler per Port, 1 VST measurement session.
- [Get Topology References (2CperPort1VST) VI](../../vi-lib/nispml/get-topology-references-2cperport1vst-vi.html) Fetches the references of a 2 Coupler per Port, 1 VST measurement session.
- [Get Topology References (1CperPort2VST) VI](../../vi-lib/nispml/get-topology-references-1cperport2vst-vi.html) Fetches the references of a 1 Coupler per Port, 2 VST measurement session.
- [Get Topology References (1CperPort1VSTS21) VI](../../vi-lib/nispml/get-topology-references-1cperport1vsts21-vi.html) Fetches the references of a 1 VST measurement session that was used for an S21 measurement only.
- [Get Topology References (S11_1Coupler) VI](../../vi-lib/nispml/get-topology-references-s11-1coupler-vi.html) Fetches the references of an S11, 1 Coupler measurement session.
- [Get Topology References (S11_2Couplers) VI](../../vi-lib/nispml/get-topology-references-s11-2couplers-vi.html) Fetches the references of an S11, 2 Couplers measurement session.
- [Get Topology References (2CperPort1VST, Solid State Switch) VI](../../vi-lib/nispml/get-topology-references-2cperport1vst-solid-state-switch-vi.html) Fetches the references of a 2 Coupler per Port, 1 VST solid state switch measurement session.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/initialize-vi.html language=enus -->
## TOPIC 00056: Initialize VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/initialize-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/initialize-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a S-parameter session for the session name that you specify in the Session Name parameter and returns a session reference handle that identifies the session in all subsequent S-Parameter VIs. icon Inputs/Outputs cstr.png Session Name Specifies a unique measurement name. For multiple meas

### Initialize VI

Initializes a S-parameter session for the session name that you specify in the Session Name parameter and returns a session reference handle that identifies the session in all subsequent S-Parameter VIs.

[IMAGE alt='icon' src='initialize-vi.png']

#### Inputs/Outputs

| Session Name — Specifies a unique measurement name. For multiple measurements within the same process, the name must be unique. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session created by this VI. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

S-Parameter Measurement

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/initiate-vi.html language=enus -->
## TOPIC 00057: Initiate VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/initiate-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/initiate-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins the S-parameter measurement. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cerrcodeclst.png error in Error conditions that occur before this node runs. This input provides standard error in functionality.

### Initiate VI

Begins the S-parameter measurement.

[IMAGE alt='icon' src='initiate-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

S-Parameter Measurement

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/load-calibration-parameters-vi.html language=enus -->
## TOPIC 00058: Load Calibration Parameters VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/load-calibration-parameters-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/load-calibration-parameters-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the S-parameter measurement session to retrieve parameters from a particular calibration file. You can define and write to this file location using the Save Calibration Parameters VI. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-pa

### Load Calibration Parameters VI

Configures the S-parameter measurement session to retrieve parameters from a particular calibration file. You can define and write to this file location using the **Save Calibration Parameters** VI.

[IMAGE alt='icon' src='load-calibration-parameters-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Calibration Parameters File Path — Specifies the location of the calibration parameters file. The default value is empty. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/save-calibration-parameters-vi.html language=enus -->
## TOPIC 00059: Save Calibration Parameters VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/save-calibration-parameters-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/save-calibration-parameters-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the calibration parameters in a .tdms file. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cpath.png Calibration Parameters File Path Specifies the location of the calibration parameters file. The default va

### Save Calibration Parameters VI

Saves the calibration parameters in a .tdms file.

[IMAGE alt='icon' src='save-calibration-parameters-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. Calibration Parameters File Path — Specifies the location of the calibration parameters file. The default value is empty. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-spml-labview-api-ref path=vi-lib/nispml/save-s-parameters-vi.html language=enus -->
## TOPIC 00060: Save S-Parameters VI

- bundle_id: `ni-spml-labview-api-ref`
- source_path: `vi-lib/nispml/save-s-parameters-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-spml-labview-api-ref/raw/resource/enus/vi-lib/nispml/save-s-parameters-vi.html
- document_id: `ni-spml-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves measurement results in an .s2p file. icon Inputs/Outputs cdatavalref.png S-Par Reference In Specifies the session reference handle of the S-parameter measurement session. cpath.png S-Parameters File Path Specifies the location of the S-parameters measurement data. cerrcodeclst.png error in Err

### Save S-Parameters VI

Saves measurement results in an .s2p file.

[IMAGE alt='icon' src='save-s-parameters-vi.png']

#### Inputs/Outputs

| S-Par Reference In — Specifies the session reference handle of the S-parameter measurement session. S-Parameters File Path — Specifies the location of the S-parameters measurement data. error in — Error conditions that occur before this node runs. This input provides standard error in functionality. S-Par Reference Out — Returns the session reference handle of the S-parameter measurement session. error out — Error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility
