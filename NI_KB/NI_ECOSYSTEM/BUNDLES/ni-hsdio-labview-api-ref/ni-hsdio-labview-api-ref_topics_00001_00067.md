# NI DOCUMENT BUNDLE: ni-hsdio-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-hsdio-labview-api-ref start=1 end=67 -->
<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/acquisition_configuration_pal.html language=enus -->
## TOPIC 00001: Acquisition Configuration

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/acquisition_configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/acquisition_configuration_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Acquisition Configuration

Owning Palette:

Dynamic & Static Acquisition

Installed With:

Use the Acquisition Configuration VIs to configure triggers, voltage levels, data position, and other properties for your acquisition operation.

| Palette Object | Description |
| --- | --- |
| niHSDIO Configure Data Interpretation | Use this VI to select between acquiring high/low data or valid/invalid data during a static or dynamic acquisition operation. |
| niHSDIO Configure Data Position Delay | Configures the data position delay with respect to the Sample clock. |
| niHSDIO Configure Data Position | Configures the various ways the data is clocked relative to the Sample clock. |
| niHSDIO Configure Trigger | Configures the specified trigger. |
| niHSDIO Configure Voltage | Configures the voltage levels for the data, trigger, and event channels. You can use either predefined logic families or custom voltage levels. |
| niHSDIO Export Signal | Use this VI to route signals (clocks, triggers, and events) to the output terminal you specify. Refer to your device documentation for valid signal destinations. |
| niHSDIO Tristate Channels | Forces a channel into a high-impedance state. The effect is immediate; it does not require the session be committed. The channel remains tristated regardless of what other software commands are called. Call this VI again and wire FALSE to the tristate terminal to allow other software commands to control the channel normally. |

| Subpalette | Description |
| --- | --- |
| Adv Timing | Use the Adv Timing VIs to configure advanced timing features. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/adv_pmu_pal.html language=enus -->
## TOPIC 00002: Advanced stPMU

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/adv_pmu_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/adv_pmu_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Advanced stPMU

Owning Palette:

Software-Timed PMU

Installed With:

Use the Advanced stPMU VIs to force and sense external signals in your system.

| Palette Object | Description |
| --- | --- |
| niHSDIO stPMU External Force Control | Connects or disconnects the channels specified in the channel list parameter to or from the EXTERNAL FORCE terminal (either on the AUX I/O connector or the REMOTE SENSE connector on the device front panel, depending on the value of the connectors parameter). This VI does not force a voltage or current by itself; it only connects NI-HSDIO to an external device. |
| niHSDIO stPMU External Sense Control | Connects or disconnects the channel specified in the channel parameter to or from the EXTERNAL SENSE terminal (either on the AUX I/O connector or the REMOTE SENSE connector on the device front panel, depending on the value of the connector parameter). Note You can conduct an external sense operation on only one channel at a time with this VI. |
|  | Note You can conduct an external sense operation on only one channel at a time with this VI. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/adv_timing_pal.html language=enus -->
## TOPIC 00003: Adv Timing

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/adv_timing_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/adv_timing_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Adv Timing

Owning Palette:

Generation Configuration

Installed With:

Use the Adv Timing VIs to configure advanced timing features.

| Palette Object | Description |
| --- | --- |
| niHSDIO Adjust Sample Clock Relative Delay | Delays the Sample clock relative to the Reference clock. Use this VI to align the Sample clock of your device with the Sample clock of another device in your system. The adjustment takes effect immediately. Call this VI only after your session is committed. |
| niHSDIO Configure Ref Clock | Configures the Reference clock. Use this VI when you are using the On Board Clock as a Sample clock and you want the Sample clock to be phase-locked to a reference signal. Phase-locking the Sample clock to a Reference clock prevents the Sample clock from losing alignment with the Reference clock. The driver ignores the Reference clock rate input when the Reference clock source is PXI Clock. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/advanced_acquisition_control_pal.html language=enus -->
## TOPIC 00004: Advanced Acquisition Control

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/advanced_acquisition_control_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/advanced_acquisition_control_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Advanced Acquisition Control

Owning Palette:

Dynamic & Static Acquisition

Installed With:

Use the Advanced Acquisition Control VIs to control advanced acquisition features.

| Palette Object | Description |
| --- | --- |
| niHSDIO Abort | Stops a running dynamic session. This VI is generally not required on finite data operations, as these operations complete after the last data point is generated or acquired. This VI is generally required only for continuous operations or if you want to interrupt an incomplete finite operation. |
| niHSDIO Fetch Waveform | Transfers acquired waveform data from device memory to PC memory. This data was previously written to onboard memory by the hardware after the hardware was initiated. |
| niHSDIO HWC Fetch Sample Errors (U32) | Returns the sample error information from a hardware comparison operation. |
| niHSDIO Initiate | Commits any pending attributes to hardware and starts the dynamic operation. |
| niHSDIO Wait Until Done | Pauses execution of your program until the dynamic data operation is completed or the VI returns a timeout error. The niHSDIO Wait Until Done VI periodically checks the operation status and returns control to the calling program if the operation completes successfully or if an error occurs (including a timeout error). |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/calibration_pal.html language=enus -->
## TOPIC 00005: Calibration

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/calibration_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/calibration_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Calibration

Owning Palette:

Utility

Installed With:

Use the Calibration VIs to access calibration operations.

| Palette Object | Description |
| --- | --- |
| niHSDIO Self Cal | Self-calibrates the device. During self-calibration of NI 6541/6542, NI 6551/6552, and NI 6561/6562 devices, the voltage-controlled crystal oscillator (VCXO) phase D/A converters are recalibrated. During self-calibration of NI 6555/6556 devices, the device conducts an analog voltage calibration and a digital timing calibration. Note NI 6544/6545/6547/6548 devices do not require calibration. For these devices, calling this VI or function just resets the device. Note On NI 6555/6556 devices, self-calibration may take between 15 and 20 minutes. Do not disable the device or LabVIEW during this time. You cannot self-calibrate your NI 6555/6556 in Measurement & Automation Explorer (MAX). You must use this VI to self-calibrate your NI 6555/6556. |
|  | Note NI 6544/6545/6547/6548 devices do not require calibration. For these devices, calling this VI or function just resets the device. |
|  | Note On NI 6555/6556 devices, self-calibration may take between 15 and 20 minutes. Do not disable the device or LabVIEW during this time. You cannot self-calibrate your NI 6555/6556 in Measurement & Automation Explorer (MAX). You must use this VI to self-calibrate your NI 6555/6556. |

| Subpalette | Description |
| --- | --- |
| External Calibration | Use the External Calibration VIs to perform external calibration operations. |
| Calibration Utility | Use the Calibration Utility VIs to access calibration utility operations. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/calibration_utility_pal.html language=enus -->
## TOPIC 00006: Calibration Utility

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/calibration_utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/calibration_utility_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Calibration Utility

Owning Palette:

Calibration

Installed With:

Use the Calibration Utility VIs to access calibration utility operations.

| Palette Object | Description |
| --- | --- |
| niHSDIO Change Ext Cal Password | Changes the password that is required to initialize an external calibration session. password may be up to four characters long. |
| niHSDIO Get Cal User Defined Info | Returns the user-defined information in the device onboard EEPROM. |
| niHSDIO Set Cal User Defined Info | Stores a user-defined string of characters in the device onboard EEPROM. If the string is longer than the maximum allowable size, it is truncated. |
| niHSDIO Get Cal User Defined Info Max Size | Returns the maximum number of characters that can be used to store user-defined information in the device onboard EEPROM. |
| niHSDIO Get Ext Cal Last Date And Time | Returns the date and time of the most recent successful external calibration. |
| niHSDIO Get Ext Cal Last Temp | Returns the onboard temperature of the device in degrees Celsius during the last successful external calibration. |
| niHSDIO Read Current Temperature | Returns the current onboard temperature of the device in degrees Celsius. |
| niHSDIO Get Self Cal Last Date And Time | Returns the date and time of the most recent successful self-calibration. |
| niHSDIO Get Self Cal Last Temp | Returns the onboard temperature of the device in degrees Celsius during the last successful self-calibration. |
| niHSDIO Get Ext Cal Recommended Interval | Returns the recommended number of months between external calibrations. |
| niHSDIO Close Ext Cal | Closes an NI-HSDIO external calibration session and, if specified, stores the new calibration constants and calibration data in the onboard EEPROM. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/dynamic___static_acquisition_pal.html language=enus -->
## TOPIC 00007: Dynamic & Static Acquisition

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/dynamic___static_acquisition_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/dynamic___static_acquisition_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Dynamic & Static Acquisition

Owning Palette:

NI-HSDIO VIs

Installed With:

Use Dynamic & Static Acquisition VIs to program dynamic and static acquisition operations.

| Palette Object | Description |
| --- | --- |
| niHSDIO Init Acquisition Session | Creates a new acquisition session. You can perform static and dynamic acquisition operations with this session. |
| niHSDIO Assign Dynamic Channels | Configures channels for dynamic acquisition (if instrument handle is an acquisition session) or dynamic generation (if instrument handle is a generation session). |
| niHSDIO Configure Sample Clock | Configures the Sample clock. This VI allows you to specify the Sample clock source and rate. |
| niHSDIO Configure Acquisition Size | Configures the size of the acquisition, including how many records are acquired and the minimum record size. |
| niHSDIO Read Waveform | Initiates a waveform acquisition on channels enabled for dynamic acquisition, waits to acquire the number of samples specified in samples to read, and returns the acquired data. |
| niHSDIO Close | Closes the specified session and frees reserved resources. If the session is running, it is first aborted. |
| niHSDIO Property Node | The niHSDIO Property Node is used to set, get, or check properties. |

| Subpalette | Description |
| --- | --- |
| Acquisition Configuration | Use the Acquisition Configuration VIs to configure triggers, voltage levels, data position, and other properties for your acquisition operation. |
| Advanced Acquisition Control | Use the Advanced Acquisition Control VIs to control advanced acquisition features. |
| Static Acquisition | Use the Static Acquisition VIs to program static acquisition operations. |
| Utility | Use the Utility VIs to access utility features of NI-HSDIO. |
| Software-Timed PMU | Use the Software-Timed PMU VIs to measure and source voltages and currents in your system. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_config_volt.html language=enus -->
## TOPIC 00008: niHSDIO Configure Voltage VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_config_volt.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_config_volt.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Configure Voltage VI

Installed With:

Configures the voltage levels for the data, trigger, and event channels. You can use either predefined logic families or custom voltage levels.

For more information about the voltage options available with your device, refer to [Voltage Levels](/csh?topicname=hsdio/fv_levels_revised.html) and [Logic Families](/csh?topicname=hsdio/flogicfams.html).

|  | Note NI-HSDIO returns an error if you use this VI with an NI 656x device. |
| --- | --- |

**Related Topics**

- Single-Ended Voltage Levels

#### Data Voltage Logic Family

This instance of niHSDIO Configure Voltage configures the voltage levels for the data channels using a logic family. Refer to the device documentation for descriptions of logic families and possible voltage restrictions.

|  | Note The default logic level for all supported devices in acquisition and generation sessions is 3.3V. |
| --- | --- |

[IMAGE alt='niHSDIO Configure Data Voltage Logic Family' src='nihsdio_configure_data_voltage_logic_family.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel list specifies which channels to apply settings to. Leave channel list blank to apply to all channels. |
|  | logic family specifies the settings for the instrument generation and acquisition operations. Note All of the following values may not be supported by your device. To view all valid logic families for your device, refer to the specifications document for your device. 5.0V Logic (5) Uses 5.0 V logic family. 3.3V Logic (6) Uses 3.3 V logic family. 2.5V Logic (7) Uses 2.5 V logic family. 1.8V Logic (8) Uses 1.8 V logic family. 1.5V Logic (80) Uses 1.5 V logic family. 1.2V Logic (81) Uses 1.2 V logic family. |
|  | Note All of the following values may not be supported by your device. To view all valid logic families for your device, refer to the specifications document for your device. |
| 5.0V Logic (5) | Uses 5.0 V logic family. |
| 3.3V Logic (6) | Uses 3.3 V logic family. |
| 2.5V Logic (7) | Uses 2.5 V logic family. |
| 1.8V Logic (8) | Uses 1.8 V logic family. |
| 1.5V Logic (80) | Uses 1.5 V logic family. |
| 1.2V Logic (81) | Uses 1.2 V logic family. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Data Voltage Custom Levels

This instance of niHSDIO Configure Voltage configures the voltage levels of the data channels using the specified high and low levels. Refer to the device documentation for possible voltage restrictions.

|  | Note If you are using an NI 6541/6542 device for generation sessions, you must set high level to the appropriate logic family value, and you must set low level to 0. For acquisition sessions with the NI 6541/6542, select the same value for high level and low level from the following list: 0.9 V, 1.25 V, or 1.65 V. |
| --- | --- |

|  | Note If you are using an NI 6544/6545/6547/6548 device for generation sessions, you must set low level to 0. For acquisition sessions with the NI 6544/6545/6547/6548, you must select the same value for high level and low level. |
| --- | --- |

When you use this VI, NI-HSDIO coerces the values you specify according to the voltage levels supported by your device. Refer to your device specifications for more information about the supported voltage levels. After you commit the session, you can read the Data High or Data Low properties to get the actual value of the configured custom levels.

[IMAGE alt='niHSDIO Configure Data Voltage Custom Levels' src='nihsdio_configure_data_voltage_custom_levels.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel list specifies which channels to apply settings to. Leave channel list blank to apply to all channels. |
|  | high level specifies what voltage identifies high level. |
|  | low level specifies what voltage identifies low level. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Trigger Voltage Logic Family

This instance of niHSDIO Configure Voltage configures the voltage levels for the trigger channels using a logic family. Refer to the device documentation for descriptions of logic families and possible voltage restrictions.

|  | Note The default logic level for all supported devices in acquisition and generation sessions is 3.3V. |
| --- | --- |

[IMAGE alt='niHSDIO Configure Trigger Voltage Logic Family' src='nihsdio_configure_trigger_voltage_logic_family.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | logic family specifies the settings for the instrument generation and acquisition operations. Note All of the following values may not be supported by your device. To view all valid logic families for your device, refer to the specifications document for your device. 5.0V Logic (5) Uses 5.0 V logic family. 3.3V Logic (6) Uses 3.3 V logic family. 2.5V Logic (7) Uses 2.5 V logic family. 1.8V Logic (8) Uses 1.8 V logic family. 1.5V Logic (80) Uses 1.5 V logic family. 1.2V Logic (81) Uses 1.2 V logic family. |
|  | Note All of the following values may not be supported by your device. To view all valid logic families for your device, refer to the specifications document for your device. |
| 5.0V Logic (5) | Uses 5.0 V logic family. |
| 3.3V Logic (6) | Uses 3.3 V logic family. |
| 2.5V Logic (7) | Uses 2.5 V logic family. |
| 1.8V Logic (8) | Uses 1.8 V logic family. |
| 1.5V Logic (80) | Uses 1.5 V logic family. |
| 1.2V Logic (81) | Uses 1.2 V logic family. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Trigger Voltage Custom Levels

This instance of niHSDIO Configure Voltage configures the voltage levels of the trigger channels using user-defined high and low levels. Refer to the device documentation for possible voltage restrictions.

|  | Note If you are using an NI 6541/6542 device for generation sessions, you must set high level to the appropriate logic family value, and you must set low level to 0. For acquisition sessions with the NI 6541/6542, select the same value for high level and low level from the following list: 0.9 V, 1.25 V, or 1.65 V. |
| --- | --- |

|  | Note If you are using an NI 6544/6545/6547/6548 device for generation sessions, you must set low level to 0. For acquisition sessions with the NI 6544/6545/6547/6548, you must select the same value for high level and low level. |
| --- | --- |

When you use this VI, NI-HSDIO coerces the values you specify according to the voltage levels supported by your device. Refer to your device specifications for more information about the supported voltage levels. After you commit the session, you can read the Trigger High or Trigger Low properties to get the actual value of the configured custom levels.

[IMAGE alt='niHSDIO Configure Trigger Voltage Custom Levels' src='nihsdio_configure_trigger_voltage_custom_levels.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | high level specifies what voltage identifies high level. |
|  | low level specifies what voltage identifies low level. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Event Voltage Logic Family

This instance of niHSDIO Configure Voltage configures the voltage levels for the event channels using a logic family. Refer to the device documentation for descriptions of logic families and possible voltage restrictions.

|  | Note The default logic level for all supported devices in acquisition and generation sessions is 3.3V. |
| --- | --- |

[IMAGE alt='niHSDIO Configure Event Voltage Logic Family' src='nihsdio_configure_event_voltage_logic_family.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | logic family specifies the settings for the instrument generation and acquisition operations. Note All of the following values may not be supported by your device. To view all valid logic families for your device, refer to the specifications document for your device. 5.0V Logic (5) Uses 5.0 V logic family. 3.3V Logic (6) Uses 3.3 V logic family. 2.5V Logic (7) Uses 2.5 V logic family. 1.8V Logic (8) Uses 1.8 V logic family. 1.5V Logic (80) Uses 1.5 V logic family. 1.2V Logic (81) Uses 1.2 V logic family. |
|  | Note All of the following values may not be supported by your device. To view all valid logic families for your device, refer to the specifications document for your device. |
| 5.0V Logic (5) | Uses 5.0 V logic family. |
| 3.3V Logic (6) | Uses 3.3 V logic family. |
| 2.5V Logic (7) | Uses 2.5 V logic family. |
| 1.8V Logic (8) | Uses 1.8 V logic family. |
| 1.5V Logic (80) | Uses 1.5 V logic family. |
| 1.2V Logic (81) | Uses 1.2 V logic family. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Event Voltage Custom Levels

This instance of niHSDIO Configure Voltage configures the voltage levels of the event channels using user-defined high and low levels. Refer to the device documentation for possible voltage restrictions.

|  | Note If you are using an NI 6541/6542 device for generation sessions, you must set high level to the appropriate logic family value, and you must set low level to 0. For acquisition sessions with the NI 6541/6542, select the same value for high level and low level from the following list: 0.9 V, 1.25 V, or 1.65 V. |
| --- | --- |

|  | Note If you are using an NI 6544/6545/6547/6548 device for generation sessions, you must set low level to 0. For acquisition sessions with the NI 6544/6545/6547/6548, you must select the same value for high level and low level. |
| --- | --- |

When you use this VI, NI-HSDIO coerces the values you specify according to the voltage levels supported by your device. Refer to your device specifications for more information about the supported voltage levels. After you commit the session, you can read the Event High or Event Low properties to get the actual value of the configured custom levels.

[IMAGE alt='niHSDIO Configure Event Voltage Custom Levels' src='nihsdio_configure_event_voltage_custom_levels.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | high level specifies what voltage identifies high level. |
|  | low level specifies what voltage identifies low level. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_convert_binary.html language=enus -->
## TOPIC 00009: niHSDIO Convert Binary To WDT VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_convert_binary.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_convert_binary.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Convert Binary To WDT VI

Installed With:

Converts unsigned binary data into the digital waveform data type (WDT). Use this VI to easily create extended state (0, 1, H, L, X, Z) digital waveforms from binary data.

**Related Topics**

- File I/O and Digital Waveform Data
- Digital Waveform Data Represenstation in LabVIEW

#### Stimulus Data

Converts binary data to drive low (0) or drive high (1) digital waveform data types. You can specify a bitmask to create tristate (Z) data.

[IMAGE alt='niHSDIO Convert Binary To WDT Stimulus Data (U32)' src='nihsdio_convert_binary_to_wdt_stimulus_data_(u32).gif']

|  | data specifies the high and low values for the digital waveform. |
| --- | --- |
|  | dt specifies the time between values in digital waveform. |
|  | signal list specifies which bits from data to include in the digital waveform. |
|  | drive enable specifies the bitmask that selects between tristating and driving the value selected in the data. Bits set to 0 translate to Z (tristate), and bits set to 1 translate to the value of the corresponding bit in data. If drive enable is empty, all the values in the array translate to 0 and 1. |
|  | compress data specifies whether the digital waveform data is compressed. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | digital waveform returns the converted data for the waveform. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Response Data

Converts binary data to expect low (L) or expect high (H) digital waveform data types. A bitmask may be specified to create don't care (X) data.

[IMAGE alt='niHSDIO Convert Binary To WDT Response Data (U32)' src='nihsdio_convert_binary_to_wdt_response_data_(u32).gif']

|  | data specifies the high and low values for the digital waveform. |
| --- | --- |
|  | dt specifies the time between values in digital waveform. |
|  | signal list specifies which bits from data to include in the digital waveform. |
|  | compare enable specifies the bitmask that selects between X (ignore) and a compare value determined by the data array. Bits set to 0 translate to X, and bits set to 1 translate to L (compare low) or H (compare high) depending on the value of the corresponding bit in the data array. If this array is empty, all the values in the data array translate to L and H. |
|  | compress data specifies whether the digital waveform data is compressed. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | digital waveform returns the converted data for the waveform. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Stimulus and Response Data

Compiles binary data to bidirectional drive (0, 1, Z) and compare (H, L, X) data.

|  | Note A bit cannot be set to 1 in both the drive enable and compare enable arrays. Comparing values (H, L, and X) always causes the channel to be set to tristate. |
| --- | --- |

[IMAGE alt='niHSDIO Convert Binary To WDT Stimulus And Response Data (U32)' src='nihsdio_convert_binary_to_wdt_stimulus_and_response_data_(u32).gif']

|  | data specifies the high and low values for driving or comparing data in the digital waveform. |
| --- | --- |
|  | dt specifies the time between values in digital waveform. |
|  | signal list specifies which bits from data to include in the digital waveform. |
|  | drive enable specifies the bitmask that selects between tristating and driving the value selected in the data. Bits set to 0 translate to Z (tristate), and bits set to 1 translate to the value of the corresponding bit in data. |
|  | compare enable specifies the bitmask that selects between X (ignore) and a compare value determined by the data array. Bits set to 0 translate to X, and bits set to 1 translate to L (compare low) or H (compare high) depending on the value of the corresponding bit in the data array. If this array is empty, all the values in the data array translate to L and H. |
|  | compress data specifies whether the digital waveform data is compressed. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | digital waveform returns the converted data for the waveform. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_delete_wvfm.html language=enus -->
## TOPIC 00010: niHSDIO Delete Named Waveform VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_delete_wvfm.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_delete_wvfm.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Delete Named Waveform VI

Installed With:

Frees waveform space in onboard memory.

The niHSDIO Delete Named Waveform VI releases [onboard memory](/csh?topicname=hsdio/fonboard_memory.html) space previously allocated by either the [niHSDIO Allocate Named Waveform](hsdio_allocate_named_wvfm.html) or the [niHSDIO Write Named Waveform](hsdio_write_nm.html) VI. Any future references to the deleted waveform result in an error. However, previously written scripts that still reference the deleted waveform do not generate an error at initiation.

**Related Topics**

- Generation Onboard Memory

[IMAGE alt='niHSDIO Delete Named Waveform' src='nihsdio_delete_named_waveform.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | waveform name specifies the name of the waveform to delete. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_error.html language=enus -->
## TOPIC 00011: niHSDIO Error Message VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_error.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_error.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Error Message VI

Installed With:

Takes the error code returned by the NI-HSDIO VIs, interprets it, and returns it as a readable string.

[IMAGE alt='niHSDIO Error Message' src='nihsdio_error_message.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error code is the error code returned by the device. The default value is 0, which means no errors occurred. |
|  | error in accepts error information wired from previously called VIs. This VI executes regardless of incoming errors. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error message returns a user-readable message string that corresponds to the status code you specify. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_export.html language=enus -->
## TOPIC 00012: niHSDIO Export Signal VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_export.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_export.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Export Signal VI

Installed With:

Use this VI to route signals (clocks, triggers, and events) to the **output terminal** you specify. Refer to your device documentation for valid signal destinations.

Any routes created within a session persist after the session closes to prevent signal glitching. To unconfigure signal routes created in previous sessions, set the **reset instrument** parameter in the [niHSDIO Init Generation Session](hsdio_init_gen_sess.html) VI or the [niHSDIO Init Acquisition Session](hsdio_init_acq_sess.html) VI to TRUE or use the [niHSDIO Reset Device](hsdio_reset_device.html) VI.

If you export a signal with this VI and commit the session, the signal is routed to the output terminal you specify. If you then reconfigure the signal to have a different output terminal, the previous output terminal is tristated after the session is committed. If you change **output terminal** to **Do Not Export** when you commit the session, the previous output terminal is tristated.

**Related Topics**

- Configuring and Exporting Events

[IMAGE alt='niHSDIO Export Signal' src='nihsdio_export_signal.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | signal identifier describes the signal being exported. You can select Script Trigger 0, Script Trigger 1, Script Trigger 2, Script Trigger 3, Marker 0, Marker 1, Marker 2, Marker 3, or None. Note When using the NI 6544/6545/6547/6548, Script Trigger 3 and Marker 3 are unavailable. |
|  | Note When using the NI 6544/6545/6547/6548, Script Trigger 3 and Marker 3 are unavailable. |
|  | signal specifies the signal to export. Sample Clock Device Sample clock. Reference Clock Device Reference clock. Start Trigger Device Start trigger. Reference Trigger Device Reference trigger (dynamic acquisition only). Advance Trigger Device Advance trigger (dynamic acquisition only) Pause Trigger Device Pause trigger (dynamic generation only). Script Trigger Device Script trigger (dynamic generation only—requires signal identifier to describe a particular Script trigger). Stop Trigger Device Stop trigger (dynamic generation only). Data Active Event Data Active event (dynamic generation only). Ready for Start Event Ready for Start event. Ready for Advance Event Ready for Advance event (dynamic acquisition only). Marker Event Marker event (dynamic generation only—requires signal identifier to describe a particular marker). End of Record Event End of Record event (dynamic acquisition only). Onboard Ref Clock Device onboard Reference clock (PCI devices only). Selecting Script Trigger or Marker Event requires a signal identifier to describe the particular signal. |
| Sample Clock | Device Sample clock. |
| Reference Clock | Device Reference clock. |
| Start Trigger | Device Start trigger. |
| Reference Trigger | Device Reference trigger (dynamic acquisition only). |
| Advance Trigger | Device Advance trigger (dynamic acquisition only) |
| Pause Trigger | Device Pause trigger (dynamic generation only). |
| Script Trigger | Device Script trigger (dynamic generation only—requires signal identifier to describe a particular Script trigger). |
| Stop Trigger | Device Stop trigger (dynamic generation only). |
| Data Active Event | Data Active event (dynamic generation only). |
| Ready for Start Event | Ready for Start event. |
| Ready for Advance Event | Ready for Advance event (dynamic acquisition only). |
| Marker Event | Marker event (dynamic generation only—requires signal identifier to describe a particular marker). |
| End of Record Event | End of Record event (dynamic acquisition only). |
| Onboard Ref Clock | Device onboard Reference clock (PCI devices only). |
|  | output terminal specifies the terminal where the signal is exported. Do not export signal The signal is not exported. PFI 0 The signal is exported to the PFI 0 front panel connector. PFI <1..3> The signal is exported to PFI <1..3> on the DDC front panel connector. PXI Trigger Line/RTSI <0..7> The signal is exported to PXI trigger line or RTSI trigger line. CLK OUT The signal is exported to the front panel CLK OUT connector. DDC CLK OUT The signal is exported to the DDC CLK OUT pin on the DDC front panel connector. |
| Do not export signal | The signal is not exported. |
| PFI 0 | The signal is exported to the PFI 0 front panel connector. |
| PFI <1..3> | The signal is exported to PFI <1..3> on the DDC front panel connector. |
| PXI Trigger Line/RTSI <0..7> | The signal is exported to PXI trigger line or RTSI trigger line. |
| CLK OUT | The signal is exported to the front panel CLK OUT connector. |
| DDC CLK OUT | The signal is exported to the DDC CLK OUT pin on the DDC front panel connector. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_fetch.html language=enus -->
## TOPIC 00013: niHSDIO Fetch Waveform VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_fetch.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_fetch.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Fetch Waveform VI

Installed With:

Transfers acquired waveform data from device memory to PC memory. This data was previously written to [onboard memory](/csh?topicname=hsdio/fonboard_memory.html) by the hardware after the hardware was initiated.

If the number of samples specified in **samples to read** is not available after the time duration specified in **max time milliseconds**, this VI returns no data with a timeout error.

The fetch position can be modified by selecting the appropriate Fetch Relative To and Fetch Offset properties in the [niHSDIO Property Node](ppropertynode.html). The default Fetch Relative To value is **Current Read Position**. The default Fetch Offset value is 0.

The niHSDIO Fetch Waveform VI is not necessary if you use the [niHSDIO Read Waveform](hsdio_read_wvfm.html) VI, as the fetch is performed as part of that function.

#### 1D U32

This instance of niHSDIO Fetch Waveform fetches the data as an array of unsigned 32-bit integers and returns the number of samples read.

[IMAGE alt='niHSDIO Fetch Waveform (1D U32)' src='nihsdio_fetch_waveform_(1d_u32).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | record to fetch specifies which record you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the acquired waveform. |
|  | number of samples read returns the number of samples that were successfully acquired and transferred into data. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 1D U16

This instance of niHSDIO Fetch Waveform fetches the data as an array of unsigned 16-bit integers and returns the number of samples read.

[IMAGE alt='niHSDIO Fetch Waveform (1D U16)' src='nihsdio_fetch_waveform_(1d_u16).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | record to fetch specifies which record you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the data for the waveform. |
|  | number of samples read returns the number of samples that were successfully acquired and transferred into data. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 1D U8

This instance of niHSDIO Fetch Waveform fetches the data as an array of unsigned 8-bit integers and returns the number of samples read.

[IMAGE alt='niHSDIO Fetch Waveform (1D U8)' src='nihsdio_fetch_waveform_(1d_u8).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | record to fetch specifies which record you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the data for the waveform. |
|  | number of samples read returns the number of samples that were successfully acquired and transferred into data. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### WDT

This instance of niHSDIO Fetch Waveform fetches the data from the subset of channels listed in the **channel list** parameter using the waveform data type and returns the number of samples read. The waveform only contains data from the subset of channels specified in the **channel list** parameter, not from all of the channels listed in the [niHSDIO Assign Dynamic Channels](hsdio_assign_dyn_chan.html) VI, unless you leave the **channel list** parameter blank.

[IMAGE alt='niHSDIO Fetch Waveform (WDT)' src='nihsdio_fetch_waveform_(wdt).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | timestamp type specifies whether the timestamp for the waveform data is relative or absolute. |
|  | channel list specifies the channels from which to fetch waveform data. You must assign all channels that you want to fetch using the niHSDIO Assign Dynamic Channels VI before selecting those channels with this parameter. NI-HSDIO fetches waveform data in the order that you list channels in this parameter, not in the order that those channels are listed in the niHSDIO Assign Dynamic Channels VI. If you leave this parameter blank, NI-HSDIO fetches all channels. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | record to fetch specifies which record you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the acquired waveform. |
|  | number of samples read returns the number of samples that were successfully acquired and transferred into data. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Multi Bus 1D WDT

This instance of niHSDIO Fetch Bus Waveform fetches an array of data using the waveform data type and returns an array of waveforms, one for each element in the **channel list** array. 
 This VI allows you to fetch data in any order or subset that you desire without the need to manipulate the data after fetching it.

[IMAGE alt='niHSDIO Fetch Bus Waveform (WDT)' src='nihsdio_fetch_bus_waveform_(wdt).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch per waveform. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | channel list specifies the channels from which to fetch waveform data. You must assign all channels that you want to fetch using the niHSDIO Assign Dynamic Channels VI before selecting those channels with this parameter. NI-HSDIO fetches waveform data in the order that you list channels in this parameter, not in the order that those channels are listed in the niHSDIO Assign Dynamic Channels VI. If you leave this parameter blank, NI-HSDIO fetches all channels. Each element in this array, consisting of its specified channels, is output as a single waveform in the data parameter. Specify multiple channels in each element by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies a waveform showing channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies a waveform showing channels 0, 1, and 2). You can include the same channel in multiple elements of this array. For example, if you choose 0:2 as the first element, 0, 2 as the second element, and 0 as the third element, the data parameter returns three waveforms: the first depicting channels 0 through 2, the second depicting channels 0 and 2, and the third depicting just channel 0. |
|  | timestamp type specifies whether the timestamp for the waveform data is relative or absolute. |
|  | starting record specifies the record at which you want to start fetching data. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the acquired data as an array of waveforms, one for each element in the channel list parameter. |
|  | number of samples read returns the number of samples that were successfully acquired and transferred into data. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 2D U32

This instance of niHSDIO Fetch Waveform fetches the data as a two-dimensional array of unsigned 32-bit integers and returns the number of samples read.

[IMAGE alt='niHSDIO Fetch Multi Record (2D U32)' src='nihsdio_fetch_multi_record_(2d_u32).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | starting record specifies the record at which you want to start fetching data. |
|  | records to fetch specifies how many records you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the data for the waveform. |
|  | wfm info returns the absolute and relative timestamp for the operation, the dt, and the actual number of samples read. absolute timestamp returns the absolute timestamp for the operation. relative timestamp returns the relative timestamp for the operation. dt returns the time between values in the waveform. actual samples read returns the number of samples read. reserved 1 is reserved for future use. reserved 2 is reserved for future use. |
|  | absolute timestamp returns the absolute timestamp for the operation. |
|  | relative timestamp returns the relative timestamp for the operation. |
|  | dt returns the time between values in the waveform. |
|  | actual samples read returns the number of samples read. |
|  | reserved 1 is reserved for future use. |
|  | reserved 2 is reserved for future use. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 2D U16

This instance of niHSDIO Fetch Waveform fetches the data as a two-dimensional array of unsigned 16-bit integers and returns the number of samples read.

[IMAGE alt='niHSDIO Fetch Multi Record (2D U16)' src='nihsdio_fetch_multi_record_(2d_u16).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | starting record specifies the record at which you want to start fetching data. |
|  | records to fetch specifies how many records you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the data for the waveform. |
|  | wfm info returns the absolute and relative timestamp for the operation, the dt, and the actual number of samples read. absolute timestamp returns the absolute timestamp for the operation. relative timestamp returns the relative timestamp for the operation. dt returns the time between values in the waveform. actual samples read returns the number of samples read. reserved 1 is reserved for future use. reserved 2 is reserved for future use. |
|  | absolute timestamp returns the absolute timestamp for the operation. |
|  | relative timestamp returns the relative timestamp for the operation. |
|  | dt returns the time between values in the waveform. |
|  | actual samples read returns the number of samples read. |
|  | reserved 1 is reserved for future use. |
|  | reserved 2 is reserved for future use. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 2D U8

This instance of niHSDIO Fetch Waveform fetches the data as a two-dimensional array of unsigned 8-bit integers and returns the number of samples read.

[IMAGE alt='niHSDIO Fetch Multi Record (2D U8)' src='nihsdio_fetch_multi_record_(2d_u8).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | starting record specifies the record at which you want to start fetching data. |
|  | records to fetch specifies how many records you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the data for the waveform. |
|  | wfm info returns the absolute and relative timestamp for the operation, the dt, and the actual number of samples read. absolute timestamp returns the absolute timestamp for the operation. relative timestamp returns the relative timestamp for the operation. dt returns the time between values in the waveform. actual samples read returns the number of samples read. reserved 1 is reserved for future use. reserved 2 is reserved for future use. |
|  | absolute timestamp returns the absolute timestamp for the operation. |
|  | relative timestamp returns the relative timestamp for the operation. |
|  | dt returns the time between values in the waveform. |
|  | actual samples read returns the number of samples read. |
|  | reserved 1 is reserved for future use. |
|  | reserved 2 is reserved for future use. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 1D WDT

This instance of niHSDIO Fetch Waveform fetches the data from the subset of channels listed in the **channel list** parameter as an array of waveform data type data and returns the number of samples read. Each waveform only contains data from the subset of channels specified in the **channel list** parameter, not from all of the channels listed in the [niHSDIO Assign Dynamic Channels](hsdio_assign_dyn_chan.html) VI, unless you leave the **channel list** parameter blank.

[IMAGE alt='niHSDIO Fetch Multi Record (WDT)' src='nihsdio_fetch_multi_record_(wdt).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | channel list specifies the channels from which to fetch waveform data. You must assign all channels that you want to fetch using the niHSDIO Assign Dynamic Channels VI before selecting those channels with this parameter. NI-HSDIO fetches waveform data in the order that you list channels in this parameter, not in the order that those channels are listed in the niHSDIO Assign Dynamic Channels VI. If you leave this parameter blank, NI-HSDIO fetches all channels. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). |
|  | timestamp type specifies whether the timestamp for the waveform data is relative or absolute. |
|  | starting record specifies the record at which you want to start fetching data. |
|  | records to fetch specifies how many records you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the data for the waveform. |
|  | actual samples read returns the number of samples read. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Direct DMA

This instance of niHSDIO Fetch Waveform transfers acquired waveform data from device memory directly to PC memory allocated by a Direct DMA-compatible device.

[IMAGE alt='niHSDIO Fetch Waveform (Direct DMA)' src='nihsdio_fetch_waveform_(direct_dma).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | buffer address specifies the location for the buffer in memory at which to transfer acquired data. |
|  | buffer size specifies the size (in bytes) of the buffer in memory at which to transfer acquired data. |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | record to fetch specifies which record you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | offset to first sample specifies the offset of the first sample acquired within the specified buffer. Data transferred from device memory in 128 byte increments, so the first sample of the acquired data typically occurs at some offset from the start of the buffer when using a Reference trigger. |
|  | wfm info returns the absolute and relative timestamp for the operation, the dt, and the actual number of samples read. absolute timestamp returns the absolute timestamp for the operation. relative timestamp returns the relative timestamp for the operation. dt returns the time between values in the waveform. actual samples read returns the number of samples read. reserved 1 is reserved for future use. reserved 2 is reserved for future use. |
|  | absolute timestamp returns the absolute timestamp for the operation. |
|  | relative timestamp returns the relative timestamp for the operation. |
|  | dt returns the time between values in the waveform. |
|  | actual samples read returns the number of samples read. |
|  | reserved 1 is reserved for future use. |
|  | reserved 2 is reserved for future use. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_gen_express.html language=enus -->
## TOPIC 00014: NI-HSDIO Express (Generation) VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_gen_express.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_gen_express.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-HSDIO Express (Generation) VI (Deprecated)

This VI is deprecated. NI recommends that you use the Dynamic Generate.vi example instead of this VI as a starting point for new applications you create.

This VI will execute in code created with versions of NI-HSDIO earlier than 19.0, but it cannot be reconfigured from a dialog box with NI-HSDIO 19.0 or later. To reconfigure this VI, right-click the Express VI and select **Open Front Panel**»**Convert**. This will convert the Express VI to code that you can configure on the block diagram.

Generates a digital waveform using a National Instruments digital 
waveform generator/analyzer.

|  | Note NI 6555/6556 devices are not supported by NI-HSDIO Express VIs. |
| --- | --- |

|  |
| --- |
| Block Diagram Inputs |
| Block Diagram Outputs |

| Parameter | Description |
| --- | --- |
| Configuration | Contains the following options: Device—Specifies the device to use for the generation. This ring control lists all devices installed on this computer which can be used by this Express VI. If you reopen the NI-HSDIO Express (Generation) configuration page and the current device is dimmed, the device name has changed or the device is no longer in the system. Generation Mode—You can select one of the following modes: Finite—Configures the device to generate a single waveform once. In this generation mode, the Express VI waits until the waveform generation is complete or Max time expires before exiting. Start continuous—Configures the device to generate the same waveform continuously until it is stopped or a new waveform is downloaded. In this generation mode, the Express VI returns without waiting for the waveform generation to complete. Stop continuous—Configures the Express VI to stop a generation previously started by an instance of this Express VI configured in Start continuous generation mode. This VI stops the device and releases all device resources used by the generation. Double Data Rate—Specifies whether or not to process data in double data rate (DDR) mode. This feature is not supported on all devices. Checked: Configures device for DDR mode. Unchecked: Disables DDR mode. Channels—Displays the channels currently configured to generate data. Modify—Click Modify to launch the Select Channels dialog box. Timing—Contains the following options: Extract rate from waveform—Specifies whether this Express VI configures the device sample rate using the value specified by the rate control or the value in the waveform at the data input terminal or the sample rate stored in the waveform file. Checked: Uses the sample rate stored in the waveform at the data input terminal or from the waveform file on disk. Unchecked: Uses the sample rate specified in rate. Rate (Hz)—Specifies the Sample clock frequency for the generation. Generation Data—Contains the following options: Data Source—Specifies whether the Express VI retrieves the data to generate from an .hws (Hierarchical Waveform Storage) file. Otherwise, data must be wired to the data input terminal. Path—If Read from file is checked, use this control to specify the .hws file containing the data to generate. |
| Voltage | Contains the following options: Data Voltage—Contains the following options: Logic family—Specifies the voltage levels for the generated data to use one of the predefined logic families. Custom levels—Specifies that the generation data use custom-defined voltage levels. High—Specifies the high voltage level for the generation. This feature is not supported on all devices. Low—Specifies the low voltage level for the generation. This feature is not supported on all devices. Trigger Line Voltage—Contains the following options: Logic family—Specifies whether you configure the voltage levels for the trigger channel using one of the predefined voltage families for this device. Custom levels—Specifies whether you configure custom high and low voltage levels for the trigger channel. This feature is not supported on all devices. High—Specifies the high voltage threshold for the trigger. This feature is not supported on all devices. Low—Specifies the low voltage threshold for the trigger. This feature is not supported on all devices. |
| Trigger | Contains the following options: Trigger—Specifies which trigger is configured. Note Not all triggers are supported by all devices. Trigger type—Specifies the Start trigger type for the generation. If this control is set to None, the trigger is disabled. If this control is set to Digital edge, the following options are visible: Trigger source—Specifies the input terminal for the trigger signal. Digital edge—Specifies whether to trigger on a rising or falling edge of the trigger signal. Max time (s)—Specifies how long to allow the VI to complete the finite generation before returning a timeout error. This control is only available in the Finite generation mode. Units: Seconds (s) |
|  | Note Not all triggers are supported by all devices. |
| Advanced Timing | Configures options used less frequently for timing. Contains the following: Clock configuration—Contains the following options: Sample clock source—Specifies the Sample clock source. Note When On Board Clock is not selected and the clock rate is inaccurate, the driver may return an error. All external clocks must have accurate values for the clock rate input, including STROBE and the PXI_STAR line. Reference clock source—Specifies the PLL reference clock source. The device phase-locks the Sample clock to the Reference clock signal to prevent the Sample clock from drifting relative to the Reference clock. Exported signals—Contains the following options: Sample clock output terminal—Specifies which terminal, if any, the device should use to export the Sample clock signal. Data active output terminal—Specifies which terminal, if any, the device should use to export the Data Active event. The Data Active event is asserted when device is generating data. If the device is waiting for a trigger or stopped, it is deasserted. Data active level—Specifies the output polarity of the Data Active event. If the event is active high, the exported signal is low level while the event is deasserted. A high pulse occurs when the event asserts. If the event is active low, the exported signal is high level while the event is deasserted. A low pulse occurs when the event asserts. Data position—Specifies which Sample clock edge generates a sample. You can also configure the device to generate data at a configurable delay past each rising edge of the Sample clock. Data delay—Specifies the delay after the Sample clock rising edge when the device generates a new data sample. Data delay is expressed as a fraction of the clock period. Initial state—Specifies the state of the data channels between the time the device is configured and the first data sample is generated. This configuration option is only useful if you configure a Start trigger for the generation. Set this control to Hold last value if you are not using a Start trigger. Idle state—Specifies the state of the data channels at the end of the generation or after you stop the generation. |
|  | Note When On Board Clock is not selected and the clock rate is inaccurate, the driver may return an error. All external clocks must have accurate values for the clock rate input, including STROBE and the PXI_STAR line. |

#### Block Diagram Inputs

| Parameter | Description |
| --- | --- |
| data | Contains the digital waveform to generate. data does not exist when you select the Read from File option in the NI-HSDIO Express (Generation) configuration page. |
| close | Determines whether the instrument session remains open when the Express VI finishes execution. Use this parameter for loop optimization by setting it to FALSE on all iterations other than the last iteration. close is TRUE by default. Note This input is not intended to be used to share the session between Express VIs. If you have a loop containing multiple Express VIs that use the same device, you must wire in TRUE for this input. |
|  | Note This input is not intended to be used to share the session between Express VIs. If you have a loop containing multiple Express VIs that use the same device, you must wire in TRUE for this input. |
| max time | Specifies the timeout value for the generation. |
| error in | Describes error conditions that occur before this Express VI runs. |

#### Block Diagram Outputs

| Parameter | Description |
| --- | --- |
| error out | Contains error information. If error in indicates that an error occurred before this Express VI ran, error out contains the same error information. Otherwise, it describes the error status that this Express VI produces. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_get_session_ref.html language=enus -->
## TOPIC 00015: niHSDIO Get Session Reference VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_get_session_ref.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_get_session_ref.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Get Session Reference VI

Installed With:

Returns a session reference you can pass to NI-TClk VIs. Session references are of generic type, which means that the corresponding wires are blue-green, unlike the wires for regular instrument driver sessions.

[IMAGE alt='niHSDIO Get Session Reference' src='nihsdio_get_session_reference.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | session reference references the device session. session reference is a generic Session reference that can be passed to NI-TClk VIs. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_init_acq_sess.html language=enus -->
## TOPIC 00016: niHSDIO Init Acquisition Session VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_init_acq_sess.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_init_acq_sess.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Init Acquisition Session VI

Installed With:

Creates a new acquisition session. You can perform static and dynamic acquisition operations with this session.

Creating a new session does not automatically tristate your front panel terminals or channels possibly driving voltages from previous sessions. Refer to the [niHSDIO Close](hsdio_close.html) VI for more information about leaving lines driving after closing a session.

Set **reset instrument** to TRUE to place your device in a known start-up state when creating a new session. This action is equivalent to using the [niHSDIO Reset](hsdio_reset.html) VI, and it tristates the front panel terminals and channels.

**Related Topics**

- Dynamic Acquisition
- Initialize Your Session

[IMAGE alt='niHSDIO Init Acquisition Session' src='nihsdio_init_acquisition_session.gif']

|  | resource name specifies the device name, for example PXI1Slot3, where PXI1Slot3 is a device name assigned by Measurement & Automation Explorer. |
| --- | --- |
|  | option string is currently unused. Leave this parameter unwired. |
|  | id query specifies whether the driver performs an ID query on the instrument. When id query is set to TRUE, the driver ensures compatibility between the instrument and the driver. When id query is set to FALSE, the driver skips the ID query. |
|  | reset instrument specifies whether the driver resets the device during initialization of the session. TRUE means that the device is reset; FALSE means that the device is not reset. Refer to niHSDIO Reset for more information about what happens during an instrument reset. Note Resetting your device resets the entire device. Acquisition or generation operations in progress are aborted and cleared. |
|  | Note Resetting your device resets the entire device. Acquisition or generation operations in progress are aborted and cleared. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_init_ext_cal.html language=enus -->
## TOPIC 00017: niHSDIO Init Ext Cal VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_init_ext_cal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_init_ext_cal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Init Ext Cal VI

Installed With:

Creates and initializes a special NI-HSDIO external calibration session. **instrument handle out** is an NI-HSDIO session that can be used during the calibration session.

|  | Note For information about sequencing the external calibration functions to successfully calibrate your NI-HSDIO device, refer to the calibration procedure for that device. |
| --- | --- |

The default password for all NI products is 'NI'.

Multiple calls to this function return the same session ID. Calibration sessions are mutually exclusive with acquisition and generation sessions.

**Related Topics**

- Initialize Your Session

[IMAGE alt='niHSDIO Init Ext Cal' src='nihsdio_init_ext_cal.gif']

|  | resource name specifies the device name, for example PXI1Slot3, where PXI1Slot3 is a device name assigned by Measurement & Automation Explorer. |
| --- | --- |
|  | password is the current calibration password for the device. This password is case sensitive. The default password for all NI products is NI. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_init_gen_sess.html language=enus -->
## TOPIC 00018: niHSDIO Init Generation Session VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_init_gen_sess.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_init_gen_sess.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Init Generation Session VI

Installed With:

Creates a new generation session. You can perform static and dynamic generation operations with this session.

Creating a new session does not automatically tristate your front panel terminals or channels that might have been left driving voltages from previous sessions. Refer to the [niHSDIO Close](hsdio_close.html) VI for more information about leaving lines driving after closing a session.

Set **reset instrument** to TRUE to place your device in a known start-up state when creating a new session. This action is equivalent to using the [niHSDIO Reset](hsdio_reset.html) VI, and it tristates the front panel terminals and channels.

**Related Topics**

- Initialize Your Session

[IMAGE alt='niHSDIO Init Generation Session' src='nihsdio_init_generation_session.gif']

|  | resource name specifies the device name, for example PXI1Slot3, where PXI1Slot3 is a device name assigned by Measurement & Automation Explorer. |
| --- | --- |
|  | option string is currently unused. Leave this parameter unwired. |
|  | id query specifies whether the driver performs an ID query on the instrument. When id query is set to TRUE, the driver ensures compatibility between the instrument and the driver. When id query is set to FALSE, the driver skips the ID query. |
|  | reset instrument specifies whether the driver resets the device during initialization of the session. TRUE means that the device is reset; FALSE means that the device is not reset. Refer to niHSDIO Reset for more information about what happens during an instrument reset. Note Resetting your device resets the entire device. Acquisition or generation operations in progress are aborted and cleared. |
|  | Note Resetting your device resets the entire device. Acquisition or generation operations in progress are aborted and cleared. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_initiate.html language=enus -->
## TOPIC 00019: niHSDIO Initiate VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_initiate.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_initiate.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Initiate VI

Installed With:

Commits any pending attributes to hardware and starts the dynamic operation.

Refer to the [niHSDIO Commit](hsdio_commit.html) VI for more information about committing.

For a generation operation with a configured [Start trigger](/csh?topicname=hsdio/ftriggers_hsdi.html), the niHSDIO Initiate VI causes the channels to go to their [Initial states](/csh?topicname=hsdio/falternatevectors.html). Refer to the [niHSDIO Configure Initial State](hsdio_config_initial.html) VI for more information about Initial states.

This VI is valid for only dynamic operations (acquisition or generation). It is not valid for static operations.

**Related Topics**

- Initialize Your Session

[IMAGE alt='niHSDIO Initiate' src='nihsdio_initiate.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_is_done.html language=enus -->
## TOPIC 00020: niHSDIO Is Done VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_is_done.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_is_done.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Is Done VI

Installed With:

Checks the hardware to determine if the device completed the dynamic data operation or if any errors have occurred. You can also use this VI for continuous dynamic data operations to poll for error conditions.

[IMAGE alt='niHSDIO Is Done' src='nihsdio_is_done.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | done returns the state of the completed data operation. The VI returns TRUE if the data operation is complete or an error has occurred. The VI returns FALSE if the data operation has not completed. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_pmu_disable.html language=enus -->
## TOPIC 00021: niHSDIO stPMU Disable PMU VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_pmu_disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_pmu_disable.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO stPMU Disable PMU VI

Installed With:

Disables the PMU source operations on the channels specified in the **channel list** parameter. Use the **return state (tristate)** parameter to tristate or return each channel to its previous digital [state](/csh?topicname=hsdio/ppmu_state_diagram_6556.html).

|  | Note When you use the PMU VIs to source a voltage or current on your system, the voltage or current continues to be sourced on the selected channels until you reset your device or call this VI. The niHSDIO Abort and niHSDIO Close VIs do not stop sourcing the voltage or current. |
| --- | --- |

If you have not yet committed your session, calling this VI implicitly commits your session. If you have already committed your session by calling a VI such as the [niHSDIO Commit](hsdio_commit.html) VI, the [niHSDIO Initiate](hsdio_initiate.html) VI, the [niHSDIO Read Waveform](hsdio_read_wvfm.html) VI, the [niHSDIO Write Named Waveform](hsdio_write_nm.html) VI, or the other [Software-Timed PMU](stpmu_pal.html) VIs, this VI will *not* commit your session again.

|  | Note Even after using this VI to disable the PMU source operations, you can still use the PMU measure voltage operations. |
| --- | --- |

|  | Note Only NI 6555/6556 devices support this VI. |
| --- | --- |

**Related Topics**

- DCL with PPMU and Deskew

[IMAGE alt='niHSDIO stPMU Disable PMU' src='nihsdio_stpmu_disable_pmu.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel list specifies the channels being configured. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). Use PFI1 or PFI2 to specify a valid PFI channel. Use DDC_CLKOUT or STROBE to specify a valid clocking terminal. If you configure multiple channels with this parameter, all those channels have the same settings. Selecting no channels for this parameter returns an error. |
|  | return state (tristate) selects, after disabling, whether to tristate the channel or to return it to its previous digital state. Note PFI 1, PFI 2, DDC CLK OUT, and STROBE support only previous digital state. If you try to tristate a PFI channel, NI-HSDIO returns an error. Tristate (90) Tristates the channel. This value is the default. Previous digital state (91) Returns the channel to its previous digital state. |
|  | Note PFI 1, PFI 2, DDC CLK OUT, and STROBE support only previous digital state. If you try to tristate a PFI channel, NI-HSDIO returns an error. |
| Tristate (90) | Tristates the channel. This value is the default. |
| Previous digital state (91) | Returns the channel to its previous digital state. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_pmu_ext_force.html language=enus -->
## TOPIC 00022: niHSDIO stPMU External Force Control VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_pmu_ext_force.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_pmu_ext_force.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO stPMU External Force Control VI

Installed With:

Connects or disconnects the channels specified in the **channel list** parameter to or from the EXTERNAL FORCE terminal (either on the AUX I/O connector or the REMOTE SENSE connector on the device front panel, depending on the value of the **connectors** parameter). This VI does not force a voltage or current by itself; it only connects NI-HSDIO to an external device.

If you have not yet committed your session, calling this VI implicitly commits your session. If you have already committed your session by calling a VI such as the [niHSDIO Commit](hsdio_commit.html) VI, the [niHSDIO Initiate](hsdio_initiate.html) VI, the [niHSDIO Read Waveform](hsdio_read_wvfm.html) VI, the [niHSDIO Write Named Waveform](hsdio_write_nm.html) VI, or the other [Software-Timed PMU](stpmu_pal.html) VIs, this VI will *not* commit your session again.

|  | Note Only NI 6555/6556 devices support this VI. |
| --- | --- |

**Related Topics**

- DCL with PPMU and Deskew
- External Force and Sense

[IMAGE alt='niHSDIO stPMU External Force Control' src='nihsdio_stpmu_external_force_control.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel list specifies the channels being configured. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). Use PFI1 or PFI2 to specify a valid PFI channel. Use DDC_CLKOUT or STROBE to specify a valid clocking terminal. If you configure multiple channels with this parameter, all those channels have the same settings. Selecting no channels for this parameter returns an error. |
|  | action selects whether to connect or disconnect a channel or channels from the EXTERNAL FORCE pin. Note On the NI 6556, selecting Disconnect disconnects both the AUX I/O and Remote Sense connectors regardless of which is connected currently. Connect (92) Connects the channel to the EXTERNAL FORCE pin. Disconnect (93) Disconnects the channel from the EXTERNAL FORCE pin. |
|  | Note On the NI 6556, selecting Disconnect disconnects both the AUX I/O and Remote Sense connectors regardless of which is connected currently. |
| Connect (92) | Connects the channel to the EXTERNAL FORCE pin. |
| Disconnect (93) | Disconnects the channel from the EXTERNAL FORCE pin. |
|  | connector selects whether to access the PMU pins on the AUX I/O connector or the REMOTE SENSE connector. Note This parameter is valid only on the NI 6556, which has both the AUX I/O and REMOTE SENSE connectors. If you are operating an NI 6555, you must select Remote Sense because the NI 6555 does not have an AUX I/O connector. If you select AUX I/O while using an NI 6555, NI-HSDIO returns an error. AUX I/O (94) Accesses the PMU pins on the AUX I/O connector. This is the default value. Remote Sense (95) Accesses the PMU pins on the REMOTE SENSE connector. |
|  | Note This parameter is valid only on the NI 6556, which has both the AUX I/O and REMOTE SENSE connectors. If you are operating an NI 6555, you must select Remote Sense because the NI 6555 does not have an AUX I/O connector. If you select AUX I/O while using an NI 6555, NI-HSDIO returns an error. |
| AUX I/O (94) | Accesses the PMU pins on the AUX I/O connector. This is the default value. |
| Remote Sense (95) | Accesses the PMU pins on the REMOTE SENSE connector. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_pmu_ext_sense.html language=enus -->
## TOPIC 00023: niHSDIO stPMU External Sense Control VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_pmu_ext_sense.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_pmu_ext_sense.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO stPMU External Sense Control VI

Installed With:

Connects or disconnects the channel specified in the **channel** parameter to or from the EXTERNAL SENSE terminal (either on the AUX I/O connector or the REMOTE SENSE connector on the device front panel, depending on the value of the **connector** parameter).

|  | Note You can conduct an external sense operation on only one channel at a time with this VI. |
| --- | --- |

If you have not yet committed your session, calling this VI implicitly commits your session. If you have already committed your session by calling a VI such as the [niHSDIO Commit](hsdio_commit.html) VI, the [niHSDIO Initiate](hsdio_initiate.html) VI, the [niHSDIO Read Waveform](hsdio_read_wvfm.html) VI, the [niHSDIO Write Named Waveform](hsdio_write_nm.html) VI, or the other [Software-Timed PMU](stpmu_pal.html) VIs, this VI will *not* commit your session again.

|  | Note Only NI 6555/6556 devices support this VI. |
| --- | --- |

**Related Topics**

- DCL with PPMU and Deskew
- External Force and Sense

[IMAGE alt='niHSDIO stPMU External Sense Control' src='nihsdio_stpmu_external_sense_control.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel specifies the channel on which to conduct the external sense. You can specify only one channel at a time with this parameter. Use PFI1 or PFI2 to specify a valid PFI channel. |
|  | action selects whether to connect or disconnect the channel from the EXTERNAL SENSE terminal. Note On the NI 6556, selecting Disconnect disconnects both the AUX I/O and Remote Sense connectors regardless of which is connected currently. Connect (92) Connects the channel to the EXTERNAL SENSE terminal. This value is the default. Disconnect (93) Disconnects the channel from the EXTERNAL SENSE terminal. |
|  | Note On the NI 6556, selecting Disconnect disconnects both the AUX I/O and Remote Sense connectors regardless of which is connected currently. |
| Connect (92) | Connects the channel to the EXTERNAL SENSE terminal. This value is the default. |
| Disconnect (93) | Disconnects the channel from the EXTERNAL SENSE terminal. |
|  | connector selects whether to access the PMU pins on the AUX I/O connector or the REMOTE SENSE connector. Note This parameter is valid only on the NI 6556, which has both the AUX I/O and REMOTE SENSE connectors. If you are operating an NI 6555, you must select Remote Sense because the NI 6555 does not have an AUX I/O connector. If you select AUX I/O while using an NI 6555, NI-HSDIO returns an error. AUX I/O (94) Accesses the PMU pins on the AUX I/O connector. This is the default value. Remote Sense (95) Accesses the PMU pins on the REMOTE SENSE connector. |
|  | Note This parameter is valid only on the NI 6556, which has both the AUX I/O and REMOTE SENSE connectors. If you are operating an NI 6555, you must select Remote Sense because the NI 6555 does not have an AUX I/O connector. If you select AUX I/O while using an NI 6555, NI-HSDIO returns an error. |
| AUX I/O (94) | Accesses the PMU pins on the AUX I/O connector. This is the default value. |
| Remote Sense (95) | Accesses the PMU pins on the REMOTE SENSE connector. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_pmu_measure_current.html language=enus -->
## TOPIC 00024: niHSDIO stPMU Measure Current VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_pmu_measure_current.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_pmu_measure_current.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO stPMU Measure Current VI

Installed With:

Measures the current on the channels specified in the **channel list** parameter. You must call the [niHSDIO stPMU Source Current](hsdio_pmu_source_current.html) or the [niHSDIO stPMU Source Voltage](hsdio_pmu_source_voltage.html) VI before measuring current with this VI, or NI-HSDIO returns an error.

If you have not yet committed your session, calling this VI implicitly commits your session. If you have already committed your session by calling a VI such as the [niHSDIO Commit](hsdio_commit.html) VI, the [niHSDIO Initiate](hsdio_initiate.html) VI, the [niHSDIO Read Waveform](hsdio_read_wvfm.html) VI, the [niHSDIO Write Named Waveform](hsdio_write_nm.html) VI, or the other [Software-Timed PMU](stpmu_pal.html) VIs, this VI will *not* commit your session again.

|  | Note Only NI 6555/6556 devices support this VI. |
| --- | --- |

**Related Topics**

- DCL with PPMU and Deskew
- External Force and Sense

[IMAGE alt='niHSDIO stPMU Measure Current' src='nihsdio_stpmu_measure_current.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel list specifies the channels being configured. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). Use PFI1 or PFI2 to specify a valid PFI channel. Use DDC_CLKOUT or STROBE to specify a valid clocking terminal. If you configure multiple channels with this parameter, all those channels have the same settings. Selecting no channels for this parameter returns an error. |
|  | aperture time (4E-6) configures the amount of time, in seconds, to measure each channel. The aperture time determines the number of hardware averages per measurement. The larger the aperture time, the greater the number of hardware averages. The default value for this control is 4E-6 (0.000004) seconds. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | current measurements returns an array of double-precision numbers representing the averaged measured currents, per channel, in amps (A), over time. The order of the returned currents directly corresponds with the order in which the channels are configured in the channel list parameter. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_pmu_measure_voltage.html language=enus -->
## TOPIC 00025: niHSDIO stPMU Measure Voltage VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_pmu_measure_voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_pmu_measure_voltage.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO stPMU Measure Voltage VI

Installed With:

Measures the voltage on the channels specified in the **channel list** parameter. You can call this VI at any time, including while in a digital state or a PMU state.

If you have not yet committed your session, calling this VI implicitly commits your session. If you have already committed your session by calling a VI such as the [niHSDIO Commit](hsdio_commit.html) VI, the [niHSDIO Initiate](hsdio_initiate.html) VI, the [niHSDIO Read Waveform](hsdio_read_wvfm.html) VI, the [niHSDIO Write Named Waveform](hsdio_write_nm.html) VI, or the other [Software-Timed PMU](stpmu_pal.html) VIs, this VI will *not* commit your session again.

|  | Note Only NI 6555/6556 devices support this VI. |
| --- | --- |

**Related Topics**

- DCL with PPMU and Deskew

[IMAGE alt='niHSDIO stPMU Measure Voltage' src='nihsdio_stpmu_measure_voltage.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel list specifies the channels being configured. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). Use PFI1 or PFI2 to specify a valid PFI channel. Use DDC_CLKOUT or STROBE to specify a valid clocking terminal. If you configure multiple channels with this parameter, all those channels have the same settings. Selecting no channels for this parameter returns an error. |
|  | aperture time (4E-6) configures the amount of time, in seconds, to measure each channel. The aperture time determines the number of hardware averages per measurement. The larger the aperture time, the greater the number of hardware averages. The default value for this control is 4E-6 (0.000004) seconds. |
|  | sense (local) selects between local or remote sensing on the specified channel(s). local (88) Local sensing of voltages. This value is measured on the DDC connector. This value is the default. remote (89) Remote sensing of voltages. This value is measured on the REMOTE SENSE connector. |
| local (88) | Local sensing of voltages. This value is measured on the DDC connector. This value is the default. |
| remote (89) | Remote sensing of voltages. This value is measured on the REMOTE SENSE connector. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | voltage measurements returns an array of double-precision numbers representing the averaged measured voltages, per channel, in volts (V), over time. The order of the returned voltages directly corresponds with the order in which the channels are configured in the channel list parameter. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_pmu_source_current.html language=enus -->
## TOPIC 00026: niHSDIO stPMU Source Current VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_pmu_source_current.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_pmu_source_current.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO stPMU Source Current VI

Installed With:

Enables the PMU capabilities on the channels specified in the **channel list** parameter and sources the current specified in the **current level** parameter while maintaining the voltage within the specified limits.

If you have not yet committed your session, calling this VI implicitly commits your session. If you have already committed your session by calling a VI such as the [niHSDIO Commit](hsdio_commit.html) VI, the [niHSDIO Initiate](hsdio_initiate.html) VI, the [niHSDIO Read Waveform](hsdio_read_wvfm.html) VI, the [niHSDIO Write Named Waveform](hsdio_write_nm.html) VI, or the other [Software-Timed PMU](stpmu_pal.html) VIs, this VI will *not* commit your session again.

|  | Note Only NI 6555/6556 devices support this VI. |
| --- | --- |

**Related Topics**

- DCL with PPMU and Deskew
- Force Current
- Force Current Voltage Clamps

[IMAGE alt='niHSDIO stPMU Source Current' src='nihsdio_stpmu_source_current.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel list specifies the channels being configured. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). Use PFI1 or PFI2 to specify a valid PFI channel. Use DDC_CLKOUT or STROBE to specify a valid clocking terminal. If you configure multiple channels with this parameter, all those channels have the same settings. Selecting no channels for this parameter returns an error. |
|  | current level specifies the current level, in amps (A), to source on the specified channel(s). |
|  | upper voltage limit specifies the maximum voltage limit, in volts (V), on the specified channel(s). |
|  | lower voltage limit specifies the minimum voltage limit, in volts (V), on the specified channel(s). |
|  | current range specifies the current range, in amps (A), that is used in the ensuing current measurement on the specified channel(s). The NI 6555/6556 supports the following eight current range options: 32 mA, 8 mA, 2 mA, 512 μA, 128 μA, 32 μA, 8 μA, or 2 μA. If you choose a range other than one of these options, NI-HSDIO coerces the value up to the nearest range. NI-HSDIO also returns an error if you enter a value above 32 mA. The default value for this parameter is 0, but NI-HSDIO returns an error if you select a value less than or equal to 0. Note Tightening your current range increases your accuracy. |
|  | Note Tightening your current range increases your accuracy. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_pmu_source_voltage.html language=enus -->
## TOPIC 00027: niHSDIO stPMU Source Voltage VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_pmu_source_voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_pmu_source_voltage.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO stPMU Source Voltage VI

Installed With:

Enables the PMU capabilities on the channels specified in the **channel list** parameter and sources the voltage specified in the **voltage level** parameter.

If you have not yet committed your session, calling this VI implicitly commits your session. If you have already committed your session by calling a VI such as the [niHSDIO Commit](hsdio_commit.html) VI, the [niHSDIO Initiate](hsdio_initiate.html) VI, the [niHSDIO Read Waveform](hsdio_read_wvfm.html) VI, the [niHSDIO Write Named Waveform](hsdio_write_nm.html) VI, or the other [Software-Timed PMU](stpmu_pal.html) VIs, this VI will *not* commit your session again.

|  | Note Only NI 6555/6556 devices support this VI. |
| --- | --- |

**Related Topics**

- DCL with PPMU and Deskew
- Voltage Ranges and Settings
- Force Voltage

[IMAGE alt='niHSDIO stPMU Source Voltage' src='nihsdio_stpmu_source_voltage.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel list specifies the channels being configured. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). Use PFI1 or PFI2 to specify a valid PFI channel. Use DDC_CLKOUT or STROBE to specify a valid clocking terminal. If you configure multiple channels with this parameter, all those channels have the same settings. Selecting no channels for this parameter returns an error. |
|  | voltage level specifies the voltage level, in volts (V), for the output generation channel(s). Valid values range from -2 V to +7 V. Refer to the NI 6555/6556 Specifications for more information about accuracy. |
|  | sense (local) selects between local or remote sensing on the specified channel(s). local (88) Local sensing of voltages. This value is measured on the DDC connector. This value is the default. remote (89) Remote sensing of voltages. This value is measured on the REMOTE SENSE connector. |
| local (88) | Local sensing of voltages. This value is measured on the DDC connector. This value is the default. |
| remote (89) | Remote sensing of voltages. This value is measured on the REMOTE SENSE connector. |
|  | current range specifies the current range, in amps (A), that is used in the ensuing current measurement on the specified channel(s). The NI 6555/6556 supports the following eight current range options: 32 mA, 8 mA, 2 mA, 512 μA, 128 μA, 32 μA, 8 μA, or 2 μA. If you choose a range other than one of these options, NI-HSDIO coerces the value up to the nearest range. NI-HSDIO also returns an error if you enter a value above 32 mA. The default value for this parameter is 0, but NI-HSDIO returns an error if you select a value less than or equal to 0. Note Tightening your current range increases your accuracy. |
|  | Note Tightening your current range increases your accuracy. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_read_static_pfi.html language=enus -->
## TOPIC 00028: niHSDIO Read Static PFI (U32) VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_read_static_pfi.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_read_static_pfi.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Read Static PFI (U32) VI

Installed With:

Immediately reads all PFI channels configured for static acquisition. The least significant bit of **read data** corresponds to the lowest physical PFI channel number.

You can configure a channel for [static acquisition](/csh?topicname=hsdio/fstaticacq.html) using the [niHSDIO Assign Static Channels](hsdio_assign_stat_chan.html) VI. 
 Channels not configured for static acquisition return a zero. Channels that do not exist on the hardware also return a zero.

Values obtained from static read operations are affected by the **data interpretation** parameter of the [niHSDIO Configure Data Interpretation](hsdio_config_data_int.html) VI.

**Related Topics**

- Acquiring or Generating Static Data

[IMAGE alt='niHSDIO Read Static PFI (U32)' src='nihsdio_read_static_pfi_(u32).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | read data returns the bit value of data read from PFI channels configured for static acquisition. The least significant bit of read data corresponds to the lowest physical channel number. For example, bit 0 corresponds to PFI0, and bit 31 corresponds to PFI31, if that channel exists on the hardware. If read data returns a value of 0x000F, channels PFI0 to PFI3 are logic one and the remaining channels are logic zero or are not configured for static acquisition. If read data returns a value of 0xFFF0, channels PFI4 to PFI15 are logic one and the remaining channels are logic zero or are not configured for static acquisition. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_read_staticu32.html language=enus -->
## TOPIC 00029: niHSDIO Read Static (U32) VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_read_staticu32.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_read_staticu32.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Read Static (U32) VI

Installed With:

Immediately reads the digital value on channels configured for static acquisition.

You can configure a channel for [static acquisition](/csh?topicname=hsdio/fstaticacq.html) using the [niHSDIO Assign Static Channels](hsdio_assign_stat_chan.html) VI. Channels not configured for static acquisition return a zero.

Values obtained from static read operations are affected by the **data interpretation** parameter of the [niHSDIO Configure Data Interpretation](hsdio_config_data_int.html) VI.

**Related Topics**

- Acquiring or Generating Static Data

[IMAGE alt='niHSDIO Read Static (U32)' src='nihsdio_read_static_(u32).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | read data returns the bit value of data read from channels configured for static acquisition. The least significant bit of read data corresponds to the lowest physical channel number. For example, if read data returns a value of 0x00F0, channels 4 to 7 are logic one and the remaining channels are logic zero or are not configured for static acquisition. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_read_wvfm.html language=enus -->
## TOPIC 00030: niHSDIO Read Waveform VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_read_wvfm.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_read_wvfm.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Read Waveform VI

Installed With:

Initiates a waveform acquisition on channels enabled for dynamic acquisition, waits to acquire the number of samples specified in **samples to read**, and returns the acquired data.

**Related Topics**

- Records

#### 1D U32

This instance of niHSDIO Read Waveform returns the data as an array of unsigned 32-bit integers.

[IMAGE alt='niHSDIO Read Waveform (1D U32)' src='nihsdio_read_waveform_(1d_u32).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | record to fetch specifies which record you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the acquired waveform. |
|  | number of samples read returns the number of samples that were successfully acquired and transferred into data. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 1D U16

This instance of niHSDIO Read Waveform returns the acquired waveform as an array of unsigned 16-bit integers.

[IMAGE alt='niHSDIO Read Waveform (1D U16)' src='nihsdio_read_waveform_(1d_u16).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | record to fetch specifies which record you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the data for the waveform. |
|  | number of samples read returns the number of samples that were successfully acquired and transferred into data. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 1D U8

This instance of niHSDIO Read Waveform returns the acquired waveform as an array of unsigned 8-bit integers.

[IMAGE alt='niHSDIO Read Waveform (1D U8)' src='nihsdio_read_waveform_(1d_u8).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | record to fetch specifies which record you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the data for the waveform. |
|  | number of samples read returns the number of samples that were successfully acquired and transferred into data. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### WDT

This instance of niHSDIO Read Waveform returns the acquired waveform data from the subset of channels listed in the **channel list** parameter as a waveform data type. The waveform only contains data from the subset of channels specified in the **channel list** parameter, not from all of the channels listed in the [niHSDIO Assign Dynamic Channels](hsdio_assign_dyn_chan.html) VI, unless you leave the **channel list** parameter blank.

[IMAGE alt='niHSDIO Read Waveform (WDT)' src='nihsdio_read_waveform_(wdt).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | timestamp type specifies whether the timestamp for the waveform data is relative or absolute. |
|  | channel list specifies the channels from which to read waveform data. You must assign all channels that you want to read using the niHSDIO Assign Dynamic Channels VI before selecting those channels with this parameter. NI-HSDIO reads waveform data in the order that you list channels in this parameter, not in the order that those channels are listed in the niHSDIO Assign Dynamic Channels VI. If you leave this parameter blank, NI-HSDIO reads all channels that were set using the niHSDIO Assign Dynamic Channels VI. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | record to fetch specifies which record you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the acquired waveform. |
|  | number of samples read returns the number of samples that were successfully acquired and transferred into data. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Multi Bus 1D WDT

This instance of niHSDIO Read Bus Waveform returns the acquired waveform data as an array of waveforms, one for each element in the **channel list** array. 
 This VI allows you to read data in any order or subset that you desire without the need to manipulate the data after reading it.

[IMAGE alt='niHSDIO Read Bus Waveform (WDT)' src='nihsdio_read_bus_waveform_(wdt).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch per waveform. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | channel list specifies the channels from which to read waveform data. You must assign all channels that you want to read using the niHSDIO Assign Dynamic Channels VI before selecting those channels with this parameter. NI-HSDIO reads waveform data in the order that you list channels in this parameter, not in the order that those channels are listed in the niHSDIO Assign Dynamic Channels VI. If you leave this parameter blank, NI-HSDIO reads all channels. Each element in this array, consisting of its specified channels, is output as a single waveform in the data parameter. Specify multiple channels in each element by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies a waveform showing channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies a waveform showing channels 0, 1, and 2). You can include the same channel in multiple elements of this array. For example, if you choose 0:2 as the first element, 0, 2 as the second element, and 0 as the third element, the data parameter returns three waveforms: the first depicting channels 0 through 2, the second depicting channels 0 and 2, and the third depicting just channel 0. |
|  | timestamp type specifies whether the timestamp for the waveform data is relative or absolute. |
|  | starting record specifies the record at which you want to start fetching data. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the acquired data as an array of waveforms, one for each element in the channel list parameter. |
|  | number of samples read returns the number of samples that were successfully acquired and transferred into data. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 2D U32

This instance of niHSDIO Read Waveform returns the acquired waveform as a two-dimensional array of unsigned 32-bit integers.

[IMAGE alt='niHSDIO Read Multi Record (2D U32)' src='nihsdio_read_multi_record_(2d_u32).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | starting record specifies the record at which you want to start fetching data. |
|  | records to fetch specifies how many records you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the data for the waveform. |
|  | wfm info returns the absolute and relative timestamp for the operation, the dt, and the actual number of samples read. absolute timestamp returns the absolute timestamp for the operation. relative timestamp returns the relative timestamp for the operation. dt returns the time between values in the waveform. actual samples read returns the number of samples read. reserved 1 is reserved for future use. reserved 2 is reserved for future use. |
|  | absolute timestamp returns the absolute timestamp for the operation. |
|  | relative timestamp returns the relative timestamp for the operation. |
|  | dt returns the time between values in the waveform. |
|  | actual samples read returns the number of samples read. |
|  | reserved 1 is reserved for future use. |
|  | reserved 2 is reserved for future use. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 2D U16

This instance of niHSDIO Read Waveform returns the acquired waveform as a two-dimensional array of unsigned 16-bit integers.

[IMAGE alt='niHSDIO Read Multi Record (2D U16)' src='nihsdio_read_multi_record_(2d_u16).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | starting record specifies the record at which you want to start fetching data. |
|  | records to fetch specifies how many records you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the data for the waveform. |
|  | wfm info returns the absolute and relative timestamp for the operation, the dt, and the actual number of samples read. absolute timestamp returns the absolute timestamp for the operation. relative timestamp returns the relative timestamp for the operation. dt returns the time between values in the waveform. actual samples read returns the number of samples read. reserved 1 is reserved for future use. reserved 2 is reserved for future use. |
|  | absolute timestamp returns the absolute timestamp for the operation. |
|  | relative timestamp returns the relative timestamp for the operation. |
|  | dt returns the time between values in the waveform. |
|  | actual samples read returns the number of samples read. |
|  | reserved 1 is reserved for future use. |
|  | reserved 2 is reserved for future use. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 2D U8

This instance of niHSDIO Read Waveform returns the acquired waveform as a two-dimensional array of unsigned 8-bit integers.

[IMAGE alt='niHSDIO Read Multi Record (2D U8)' src='nihsdio_read_multi_record_(2d_u8).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | starting record specifies the record at which you want to start fetching data. |
|  | records to fetch specifies how many records you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the data for the waveform. |
|  | wfm info returns the absolute and relative timestamp for the operation, the dt, and the actual number of samples read. absolute timestamp returns the absolute timestamp for the operation. relative timestamp returns the relative timestamp for the operation. dt returns the time between values in the waveform. actual samples read returns the number of samples read. reserved 1 is reserved for future use. reserved 2 is reserved for future use. |
|  | absolute timestamp returns the absolute timestamp for the operation. |
|  | relative timestamp returns the relative timestamp for the operation. |
|  | dt returns the time between values in the waveform. |
|  | actual samples read returns the number of samples read. |
|  | reserved 1 is reserved for future use. |
|  | reserved 2 is reserved for future use. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 1D WDT

This instance of niHSDIO Read Waveform returns the acquired waveforms from the subset of channels listed in the **channel list** parameter as an array of waveform data type data. Each waveform only contains data from the subset of channels specified in the **channel list** parameter, not from all of the channels listed in the [niHSDIO Assign Dynamic Channels](hsdio_assign_dyn_chan.html) VI, unless you leave the **channel list** parameter blank.

[IMAGE alt='niHSDIO Read Multi Record (WDT)' src='nihsdio_read_multi_record_(wdt).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
| --- | --- |
|  | samples to read specifies the number of samples to fetch. If you specify a value for samples to read that is greater than the number of samples in the device memory, NI-HSDIO returns the samples that are acquired after max time milliseconds. Setting this parameter to -1 acquires the samples per record specified in the niHSDIO Configure Acquisition Size VI. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | channel list specifies the channels from which to read waveform data. You must assign all channels that you want to read using the niHSDIO Assign Dynamic Channels VI before selecting those channels with this parameter. NI-HSDIO reads waveform data in the order that you list channels in this parameter, not in the order that those channels are listed in the niHSDIO Assign Dynamic Channels VI. If you leave this parameter blank, NI-HSDIO reads all channels that were set using the niHSDIO Assign Dynamic Channels VI. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). |
|  | timestamp type specifies whether the timestamp for the waveform data is relative or absolute. |
|  | starting record specifies the record at which you want to start fetching data. |
|  | records to fetch specifies how many records you want to fetch from onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI. |
|  | data returns the data for the waveform. |
|  | actual samples read returns the number of samples read. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_reset.html language=enus -->
## TOPIC 00031: niHSDIO Reset VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_reset.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Reset VI

Installed With:

Resets the session to its initial state. All channels and front panel terminals are put into a high-impedance state. All software attributes are reset to their initial values. During a reset, signal routes between this and other devices are released, regardless of which device created the route. For instance, a trigger signal being exported to a PXI trigger line and used by another device is no longer exported.

The niHSDIO Reset VI is applied to the *entire* device. If you have both a generation and an acquisition session active, the niHSDIO Reset VI resets the current session, including attributes, and invalidates the other session if it is committed or running. The other session must be closed.

[IMAGE alt='niHSDIO Reset' src='nihsdio_reset.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_reset_device.html language=enus -->
## TOPIC 00032: niHSDIO Reset Device VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_reset_device.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_reset_device.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Reset Device VI

Installed With:

Resets the device to its initial state and reloads the FPGA. All channels and front panel terminals are put into a high-impedance state. All software attributes are reset to their initial values. The entire contents of the FPGA and EEPROM files are reloaded. Use this VI to re-enable your device if it has disabled itself because the device temperature has risen above its optimal operating temperature.

During a device reset, signal routes between this and other devices are released, regardless of which device created the route. For instance, a trigger signal being exported to a PXI trigger line and used by another device is no longer exported.

The niHSDIO Reset Device VI is applied to the *entire* device. If you have both a generation and an acquisition session active, the niHSDIO Reset Device VI resets the current session, including attributes, and invalidates the other session if it is committed or running. The other session must be closed.

Generally, using the [niHSDIO Reset](hsdio_reset.html) VI is acceptable in place of the niHSDIO Reset Device VI. The [niHSDIO Reset](hsdio_reset.html) VI executes more quickly.

[IMAGE alt='niHSDIO Reset Device' src='nihsdio_reset_device.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_self_calibrate.html language=enus -->
## TOPIC 00033: niHSDIO Self Cal VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_self_calibrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_self_calibrate.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Self Cal VI

Installed With:

Self-calibrates the device. During self-calibration of NI 6541/6542, NI 6551/6552, and NI 6561/6562 devices, the voltage-controlled crystal oscillator (VCXO) phase D/A converters are recalibrated. During self-calibration of NI 6555/6556 devices, the device conducts an analog voltage calibration and a digital timing calibration.

|  | Note NI 6544/6545/6547/6548 devices do not require calibration. For these devices, calling this VI or function just resets the device. |
| --- | --- |

|  | Note On NI 6555/6556 devices, self-calibration may take between 15 and 20 minutes. Do not disable the device or LabVIEW during this time. You cannot self-calibrate your NI 6555/6556 in Measurement & Automation Explorer (MAX). You must use this VI to self-calibrate your NI 6555/6556. |
| --- | --- |

[IMAGE alt='niHSDIO Self Cal' src='nihsdio_self_cal.gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_self_test.html language=enus -->
## TOPIC 00034: niHSDIO Self Test VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_self_test.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_self_test.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Self Test VI

Installed With:

Performs a self-test on the instrument and returns the test results. The niHSDIO Self Test VI performs a simple series of tests that ensure the instrument is powered up and responding. Complete functional testing and calibration are not performed by this function.

This function is internal and does not affect external I/O connections or connections between devices.

**Related Topics**

- Thermal Shutdown
- LED Indicators (NI 6551/6552)
- LED Indicators (NI 6544/6545/6547/6548)
- LED Indicators (NI PXI-6541/6542 )
- LED Indicators (NI PXI-656x)
- LED Indicators (NI 6555/6556)

[IMAGE alt='niHSDIO Self Test' src='nihsdio_self_test.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | self test result returns the value returned from the device self-test. A 0 means the self-test passed; anything else means the test failed. |
|  | self test message returns the self-test response string from the device. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_send_sw_trig.html language=enus -->
## TOPIC 00035: niHSDIO Send Software Edge Trigger VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_send_sw_trig.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_send_sw_trig.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Send Software Edge Trigger VI

Installed With:

Forces a particular edge, pattern match, or software trigger to occur.

This VI applies only to the triggers listed below, and it is valid only if the particular trigger has been configured for edge, pattern match, or software triggering:

- Start Trigger
- Reference Trigger
- Advance Trigger
- Script Trigger
- Stop Trigger

For edge or pattern match triggers, you can use this VI as a software override.

**Related Topics**

- Triggers Summary

[IMAGE alt='niHSDIO Send Software Edge Trigger' src='nihsdio_send_software_edge_trigger.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | trigger specifies the trigger to assert. You can select Start Trigger, Reference Trigger, Advance Trigger, Script Trigger, or Stop Trigger as the value for this control. |
|  | trigger identifier specifies the details of the script trigger. trigger identifier can be ScriptTrigger0, ScriptTrigger1, ScriptTrigger2, or ScriptTrigger3; or you can leave this parameter blank for the Start, Reference, Advance, and Stop triggers. Note NI 6544/6545/6547/6548 devices do not support ScriptTrigger 3. |
|  | Note NI 6544/6545/6547/6548 devices do not support ScriptTrigger 3. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_set_act_script.html language=enus -->
## TOPIC 00036: niHSDIO Configure Script To Generate VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_set_act_script.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_set_act_script.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Configure Script To Generate VI

Installed With:

Sets the script that is generated after you call the [niHSDIO Initiate](hsdio_initiate.html) VI when the **generation mode** parameter of the [niHSDIO Configure Generation Mode](hsdio_config_md.html) VI is set to **Scripted**. If multiple scripts load when the [niHSDIO Initiate](hsdio_initiate.html) VI is called, one script must be designated the script to generate or you receive an error.

This VI is only required if multiple [scripts](/csh?topicname=hsdio/fscripts.html) are present in the [onboard memory](/csh?topicname=hsdio/fonboard_memory.html).

**Related Topics**

- Generation Onboard Memory

[IMAGE alt='niHSDIO Configure Script To Generate' src='nihsdio_configure_script_to_generate.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | script name specifies a string containing a syntactically correct script that is written to the onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_set_act_wvfm.html language=enus -->
## TOPIC 00037: niHSDIO Configure Waveform To Generate VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_set_act_wvfm.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_set_act_wvfm.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Configure Waveform To Generate VI

Installed With:

Sets the waveform to be generated after a call to the [niHSDIO Initiate](hsdio_initiate.html) VI when the **generation mode** parameter of the [niHSDIO Configure Generation Mode](hsdio_config_md.html) VI is set to **Waveform**. **Waveform** is the default value for the **generation mode**.

If this VI is not called and you have multiple waveforms in onboard memory, NI-HSDIO generates an error at initiate.

**Related Topics**

- Generation Onboard Memory

[IMAGE alt='niHSDIO Configure Waveform To Generate' src='nihsdio_configure_waveform_to_generate.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | waveform name specifies the name of a previously allocated or written waveform to be generated at initiate. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_tristate.html language=enus -->
## TOPIC 00038: niHSDIO Tristate Channels VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_tristate.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_tristate.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Tristate Channels VI

Installed With:

Forces a channel into a high-impedance state. The effect is immediate; it does not require the session be committed. The channel remains tristated regardless of what other software commands are called. Call this VI again and wire FALSE to the **tristate** terminal to allow other software commands to control the channel normally.

Channels stay tristated while the session remains open. Closing the session does not affect the high-impedance state of the channel, but future sessions can now control it.

You must assign channels for static use with the [niHSDIO Assign Static Channels](hsdio_assign_stat_chan.html) VI before sending those channels into a high-impedance state with this VI, otherwise NI-HSDIO returns an error.

**Related Topics**

- Per Cycle Tristate
- Open Collector

[IMAGE alt='niHSDIO Tristate Channels' src='nihsdio_tristate_channels.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel list specifies which channels are tristated. Channels not specified in this list are unaffected. The following strings are examples of valid channel list syntax: 0-3, 5, 8-15 or 0, 3, 10. On supported devices, you can select the following clocks using these strings: STROBE and DDC_CLKOUT. On supported devices, you also can select all supported PFI channels using strings such as PFI1, PFI26, and so on. The clock and PFI strings are not case sensitive and can be grouped with the standard input strings separated by commas. The following are examples of valid string syntax: 0, 4, 6, PFI1, 7 or 0-12, STROBE, DDC_CLKOUT. |
|  | tristate specifies whether the channels specified in channel list remain tristated. If tristate is TRUE, the channels specified in channel list remain tristated, ignoring future software commands. If tristate is FALSE, the channels specified in channel list become untristated by future software commands. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_wait_done.html language=enus -->
## TOPIC 00039: niHSDIO Wait Until Done VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_wait_done.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_wait_done.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Wait Until Done VI

Installed With:

Pauses execution of your program until the dynamic data operation is completed or the VI returns a timeout error. The niHSDIO Wait Until Done VI periodically checks the operation status and returns control to the calling program if the operation completes successfully or if an error occurs (including a timeout error).

Use this VI for finite data operations that you expect to complete within a certain time.

[IMAGE alt='niHSDIO Wait Until Done' src='nihsdio_wait_until_done.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | max time milliseconds specifies the number of milliseconds to allow the function to complete before returning. If the specified time elapses before the data operation has completed, the function returns a timeout error. Setting a value of 0 causes the VI to return immediately. This setting can be useful to manually poll for hardware errors after a data operation has been initiated. If no other error has occurred and the data operation is still not complete, the VI returns a timeout error. Setting a value of -1 causes the VI to never timeout. Be careful not to use this value during a continuous operation, as it never returns unless a hardware error occurs. Perform a manual device reset from Measurement & Automation Explorer if you cannot exit this state or use the niHSDIO Reset or niHSDIO Reset Device VI from the other session of the device. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_write_nm.html language=enus -->
## TOPIC 00040: niHSDIO Write Named Waveform VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_write_nm.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_write_nm.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Write Named Waveform VI

Installed With:

Transfers waveform data from PC memory to onboard memory. If you specify a **waveform name** not already being used on the instrument, the appropriate amount of onboard memory is allocated (if available) and the data is stored in that new location. For binary data, choose the appropriate instance of this VI or function based on your data width. For data other than binary data, choose the appropriate instance of this VI or function based on your cycle-cycle-tristate or hardware compare needs.

**Related Topics**

- Writing Waveforms to Your Device
- File I/O and Digital Waveform Data
- Generation Onboard Memory

[Details](#details)

#### 1D U32

This instance of niHSDIO Write Named Waveform writes the waveform to onboard memory from a one-dimensional array of unsigned 32-bit data.

[IMAGE alt='niHSDIO Write Named Waveform (1D U32)' src='nihsdio_write_named_waveform_(1d_u32).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | waveform name specifies the name of the waveform to configure position. You should name waveforms using this VI under either of the following conditions: You are using scripts. You want to download multiple waveforms into the hardware. |
|  | data specifies the samples to write. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 1D U16

This instance of niHSDIO Write Named Waveform writes the waveform to onboard memory from a one-dimensional array of unsigned 16-bit data.

[IMAGE alt='niHSDIO Write Named Waveform (1D U16)' src='nihsdio_write_named_waveform_(1d_u16).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | waveform name specifies the name of the waveform to configure position. You should name waveforms using this VI under either of the following conditions: You are using scripts. You want to download multiple waveforms into the hardware. |
|  | data specifies the data to be written. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 1D U8

This instance of niHSDIO Write Named Waveform writes the waveform to onboard memory from a one-dimensional array of unsigned 8-bit data.

[IMAGE alt='niHSDIO Write Named Waveform (1D U8)' src='nihsdio_write_named_waveform_(1d_u8).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | waveform name specifies the name of the waveform to configure position. You should name waveforms using this VI under either of the following conditions: You are using scripts. You want to download multiple waveforms into the hardware. |
|  | data specifies the data for the waveform to be written. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### WDT

This instance of niHSDIO Write Named Waveform writes the waveform to onboard memory as waveform data type data.

[IMAGE alt='niHSDIO Write Named Waveform (WDT)' src='nihsdio_write_named_waveform_(wdt).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | waveform name specifies the name of the waveform to configure position. You should name waveforms using this VI under either of the following conditions: You are using scripts. You want to download multiple waveforms into the hardware. |
|  | data provides a waveform to generate. |
|  | Use rate from waveform specifies how the sample rate is computed. Setting this value to TRUE computes the sample rate from the WDT value. If the sample rate has been configured using the niHSDIO Configure Sample Clock, Use rate from waveform overrides the sample rate. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### HWS

This instance of niHSDIO Write Named Waveform writes the waveform to onboard memory from a .hws (Hierarchical Waveform Storage) file.

[IMAGE alt='niHSDIO Write Named Waveform From File (HWS)' src='nihsdio_write_named_waveform_from_file_(hws).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | waveform name specifies the name of the waveform to configure position. You should name waveforms using this VI under either of the following conditions: You are using scripts. You want to download multiple waveforms into the hardware. |
|  | file path specifies the path and file name of the HWS file to open. The .hws extension is typically used for HWS files, although using this extension is optional. |
|  | Use rate from waveform specifies how the sample rate is computed. Setting this value to TRUE computes the sample rate from the WDT value. If the sample rate has been configured using the niHSDIO Configure Sample Clock, Use rate from waveform overrides the sample rate. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | waveform size returns the number of samples contained in the waveform. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Direct DMA

This instance of niHSDIO Write Named Waveform writes a specified amount of data from a Direct DMA-compatible device to the waveform in onboard memory.

The sample size of the data you write is shown by the following table.

| Device | Sample Size in Bytes |
| --- | --- |
| NI 6541/6542 | 4 |
| NI 6544/6545 | 4 |
| NI 6547/6548 | 4 in SDR mode; 2 in DDR mode |
| NI 655x | 4 |
| NI 656x | 2 in SDR mode; 1 in DDR mode |

[IMAGE alt='niHSDIO Write Named Waveform (Direct DMA)' src='nihsdio_write_named_waveform_(direct_dma).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | waveform name specifies the name to associate with the allocated waveform memory. |
|  | window address specifies the window address from the Direct DMA-compatible data source. |
|  | samples to write specifies the number of samples to write from the Direct DMA-compatible data source. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Details

Data is always written to memory starting at the waveform write position. The initial write position for a new waveform is the start of the allocated memory. This VI moves the next write position to the end of the data just written, so subsequent uses of this VI appends data to the end of previously written data. You may also manually change the write position with the [niHSDIO Set Named Waveform Next Write Position](set_named_wvfm.html) VI. If you try to write past the end of the allocated space, the VI returns an error.

Waveforms are stored contiguously in onboard memory. You cannot resize an existing named waveform. Instead, delete the existing waveform using the [niHSDIO Delete Named Waveform](hsdio_delete_wvfm.html) VI and then re-create it with the new size using the same name.

This VI also calls the Dynamic instance of the [niHSDIO Commit](hsdio_commit.html) VI.

When you explicitly call the [niHSDIO Allocate Named Waveform](hsdio_allocate_named_wvfm.html) VI and write waveforms using multiple niHSDIO Write Named Waveform VIs, each waveform block written must be a multiple of 32 samples for the NI 654*x*/655*x* devices (64 samples for the NI 6547/6548 in DDR mode) or a multiple of 64 samples for the NI 656*x* devices (128 samples in DDR mode).

|  | Note If the waveform was allocated 10 KB, but this VI has only written a 5 KB waveform, the remaining 5 KB contain invalid data. |
| --- | --- |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_write_script.html language=enus -->
## TOPIC 00041: niHSDIO Write Script VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_write_script.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_write_script.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Write Script VI

Installed With:

Writes a string to the onboard memory containing scripts that govern the waveform generation.

If this VI is called repeatedly, previously written [scripts](/csh?topicname=hsdio/fscripts.html) with unique names remain loaded. Previously written scripts with identical names to those being written are replaced. If multiple scripts load when the [niHSDIO Initiate](hsdio_initiate.html) VI is called, one script must be designated as the script to generate. If only one script exists in memory, you do not need to designate the script to generate.

This VI returns an error if the script uses incorrect syntax. This VI calls the Dynamic instance of the [niHSDIO Commit](hsdio_commit.html) VI. All pending attributes are committed to hardware.

**Related Topics**

- Generation Onboard Memory

[IMAGE alt='niHSDIO Write Script' src='nihsdio_write_script.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | script specifies the text of the script you want to use for your generation operation. For more information about scripting syntax, refer to Scripting Instructions in the Script Editor Help. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_write_static.html language=enus -->
## TOPIC 00042: niHSDIO Write Static (U32) VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_write_static.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_write_static.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Write Static (U32) VI

Installed With:

Writes to channels configured for static generation. You can configure a channel for static generation using the [niHSDIO Assign Static Channels](hsdio_assign_stat_chan.html) VI.

**Related Topics**

- Acquiring or Generating Static Data

[IMAGE alt='niHSDIO Write Static (U32)' src='nihsdio_write_static_(u32).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | write data specifies the bit value of data to drive on channels configured for static generation. 1 corresponds to logic high level, 0 corresponds to logic low level. The least significant bit of write data corresponds to the lowest physical channel number. For example, a write data value of 0xFF00 sets the lower 8 channels to a logic low level and sets channels 8 to 15 to a logic high level. Data values in write data corresponding to channels not configured for static generation are ignored. Static channels explicitly disabled with the niHSDIO Tristate Channels VI remain disabled, but the channel data value changes internally. Re-enabling a channel with niHSDIO Tristate Channels VI causes the channel to drive any value that you have written to it, even while the channel was disabled. |
|  | channel mask (no masking:-1) specifies the bit-value of channels to leave unchanged. 1 means to change the channel to whatever is reflected by write data. 0 means do not alter the channel, regardless of write data. The least significant bit of channel mask corresponds to the lowest physical channel number. For example, a write data value of 0xFFFF and channel mask of 0x00FF means set only channels 0-7 to 1; all other channels remain unchanged. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/hsdio_write_static_pfi.html language=enus -->
## TOPIC 00043: niHSDIO Write Static PFI (U32) VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/hsdio_write_static_pfi.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/hsdio_write_static_pfi.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Write Static PFI (U32) VI

Installed With:

Writes data to PFI channels configured for static generation. You can configure a channel for static generation using the [niHSDIO Assign Static Channels](hsdio_assign_stat_chan.html) VI.

|  | Note NI-HSDIO returns an error if an event is already routed to a PFI channel and you try to reserve that same channel for static use with this VI. |
| --- | --- |

[IMAGE alt='niHSDIO Write Static PFI (U32)' src='nihsdio_write_static_pfi_(u32).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | write data (0x0000) specifies the bit value of data to drive on PFI channels configured for static generation. 1 corresponds to logic high level, 0 corresponds to logic low level. The least significant bit of write data corresponds to the lowest physical PFI channel number. For example, a write data value of 0xFF00 sets PFI0 through PFI7 to logic 0 and sets PFI8 through PFI 15 to logic 1. Data values in write data corresponding to channels not configured for static generation are ignored. Static channels explicitly disabled with the niHSDIO Tristate Channels VI remain disabled, but the channel data value changes internally. Re-enabling a channel with niHSDIO Tristate Channels VI causes the channel to drive any value that you have written to it, even while the channel was disabled. |
|  | channel mask (no masking:-1) specifies the bit-value of the PFI channels to leave unchanged. 1 means to change the PFI channel to whatever is reflected by write data. 0 means do not alter the PFI channel, regardless of write data. The least significant bit of channel mask corresponds to the lowest physical PFI channel number. For example, a write data value of 0xFFFF and channel mask of 0x00FF means set only PFI0 through PFI7 to logic 1; all other PFI channels remain unchanged. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_cal_adjust.html language=enus -->
## TOPIC 00044: niHSDIO Cal Adjust VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_cal_adjust.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_cal_adjust.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Cal Adjust VI

Installed With:

This VI performs internal calculations and saves the resulting values until the end of the External Calibration session. These values will be stored on the device when [niHSDIO Close Ext Cal](hsdio_close_ext_cal.html) is executed with the **action** configured to Commit, or discarded if the **action** is configured as Cancel.

#### DBL

This VI takes a single floating point value as input and performs internal calculations based on this value, previous inputs, the **calibration reference**, and the **calibration type**.

[IMAGE alt='niHSDIO Cal Adjust (DBL)' src='nihsdio_cal_adjust_(dbl).gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel specifies channel to adjust. |
|  | calibration reference specifies which internal routing path to configure based on the calibration type. Refer to the calibration procedure document for your device for the correct value to use. |
|  | calibration type specifies which section of the external calibration pocedure you are trying to execute. Refer to the calibration procedure document for your device for the correct value to use. |
|  | value specifies the floating point value used to perform internal calculations. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### 1D DBL

This VI takes an array of raw DBL values and performs internal calculations based on these values, previous inputs, the **calibration reference**, and the **calibration type**.

[IMAGE alt='niHSDIO Cal Adjust (1D DBL)' src='nihsdio_cal_adjust_(1d_dbl).gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel specifies channel to adjust. |
|  | calibration reference specifies which internal routing path to configure based on the calibration type. Refer to the calibration procedure document for your device for the correct value to use. |
|  | calibration type specifies which section of the external calibration pocedure you are trying to execute. Refer to the calibration procedure document for your device for the correct value to use. |
|  | values specifies the floating point values used to perform internal calculations. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_cal_clear_state.html language=enus -->
## TOPIC 00045: niHSDIO Cal Clear State VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_cal_clear_state.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_cal_clear_state.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Cal Clear State VI

Installed With:

Restores the internal routing of the device to the default, unconfigured state.

[IMAGE alt='niHSDIO Cal Clear State' src='nihsdio_cal_clear_state.gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_cal_close_child_session.html language=enus -->
## TOPIC 00046: niHSDIO Cal Close Child Session VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_cal_close_child_session.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_cal_close_child_session.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Cal Close Child Session VI

Installed With:

Closes the child session of the open External Calibration session, similar to [niHSDIO Close](hsdio_close.html) VI. If any open child sessions have not been closed when [niHSDIO Close Ext Cal](hsdio_close_ext_cal.html) VI is called, they are closed implicitly.

[IMAGE alt='niHSDIO Cal Close Child Session' src='nihsdio_cal_close_child_session.gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | child session instrument handle identifies the niHSDIO Acquisition or Generation session that is created by the calibration session for the purpose of measurement. You can create one acquisition and/or one generation session at a time within the calibration session. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_cal_configure_state.html language=enus -->
## TOPIC 00047: niHSDIO Cal Configure State VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_cal_configure_state.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_cal_configure_state.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Cal Configure State VI

Installed With:

Configures the internal routing of the device or the channel so that you can perform specific calibration steps.

#### Device

Configures the internal routing of the device so that you can perform specific calibration steps.

[IMAGE alt='niHSDIO Cal Configure Device State' src='nihsdio_cal_configure_device_state.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | calibration reference specifies which internal routing path to configure based on the calibration type. Refer to the calibration procedure document for your device for the correct value to use. |
|  | calibration type specifies which section of the external calibration pocedure you are trying to execute. Refer to the calibration procedure document for your device for the correct value to use. |
|  | connector selects whether to access the PMU pins on the AUX I/O connector or the REMOTE SENSE connector. Note This parameter is valid only on the NI 6556, which has both the AUX I/O and REMOTE SENSE connectors. If you are operating an NI 6555, you must select Remote Sense because the NI 6555 does not have an AUX I/O connector. If you select AUX I/O while using an NI 6555, NI-HSDIO returns an error. AUX I/O (94) Accesses the PMU pins on the AUX I/O connector. This is the default value. Remote Sense (95) Accesses the PMU pins on the REMOTE SENSE connector. |
|  | Note This parameter is valid only on the NI 6556, which has both the AUX I/O and REMOTE SENSE connectors. If you are operating an NI 6555, you must select Remote Sense because the NI 6555 does not have an AUX I/O connector. If you select AUX I/O while using an NI 6555, NI-HSDIO returns an error. |
| AUX I/O (94) | Accesses the PMU pins on the AUX I/O connector. This is the default value. |
| Remote Sense (95) | Accesses the PMU pins on the REMOTE SENSE connector. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Channel

Configures the internal routing of the channel so that you can perform specific calibration steps.

[IMAGE alt='niHSDIO Cal Configure Channel State' src='nihsdio_cal_configure_channel_state.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | channel specifies channels on which to modify the internal routing. |
|  | calibration reference specifies which internal routing path to configure based on the calibration type. Refer to the calibration procedure document for your device for the correct value to use. |
|  | calibration type specifies which section of the external calibration pocedure you are trying to execute. Refer to the calibration procedure document for your device for the correct value to use. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_cal_init_child_session.html language=enus -->
## TOPIC 00048: niHSDIO Cal Init Child Session VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_cal_init_child_session.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_cal_init_child_session.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Cal Init Child Session VI

Installed With:

Creates a new acquisition or generation session within an existing External Calibration session, based on the specified **session type** . This VI returns a handle to the new child session.

|  | Note An error occurs if another child session of the same type is already open. |
| --- | --- |

[IMAGE alt='niHSDIO Cal Init Child Session' src='nihsdio_cal_init_child_session.gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | session type specifies the type of session, either Acquisition or Generation. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | child session instrument handle out identifies the niHSDIO Acquisition or Generation session that is created by the calibration session for the purpose of measurement. You can create one acquisition and/or one generation session at a time within the calibration session. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_get_cal_user_defined_info.html language=enus -->
## TOPIC 00049: niHSDIO Get Cal User Defined Info VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_get_cal_user_defined_info.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_get_cal_user_defined_info.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Get Cal User Defined Info VI

Installed With:

Returns the user-defined information in the device onboard EEPROM.

[IMAGE alt='niHSDIO Get Cal User Defined Info' src='nihsdio_get_cal_user_defined_info.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | info returns the user-defined information stored in the onboard EEPROM. specifies the string to store in the onboard EEPROM. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_get_cal_user_defined_info_max_size.html language=enus -->
## TOPIC 00050: niHSDIO Get Cal User Defined Info Max Size VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_get_cal_user_defined_info_max_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_get_cal_user_defined_info_max_size.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Get Cal User Defined Info Max Size VI

Installed With:

Returns the maximum number of characters that can be used to store user-defined information in the device onboard EEPROM.

[IMAGE alt='niHSDIO Get Cal User Defined Info Max Size' src='nihsdio_get_cal_user_defined_info_max_size.gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | info size returns the number of characters that can be stored in the device onboard EEPROM. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_get_ext_cal_last_date_and_time.html language=enus -->
## TOPIC 00051: niHSDIO Get Ext Cal Last Date And Time VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_get_ext_cal_last_date_and_time.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_get_ext_cal_last_date_and_time.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Get Ext Cal Last Date And Time VI

Installed With:

Returns the date and time of the most recent successful external calibration.

The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this VI returns 14 for the hours parameter and 30 for the minutes parameter.

[IMAGE alt='niHSDIO Get Ext Cal Last Date And Time' src='nihsdio_get_ext_cal_last_date_and_time.gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | year returns the year in which the device was last calibrated. |
|  | month returns the month in which the device was last calibrated. |
|  | day returns the day on which the device was last calibrated. |
|  | hour returns the hour (in 24-hour time) in which the device was last calibrated. |
|  | minute returns the minute in which the device was last calibrated. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_get_ext_cal_last_temp.html language=enus -->
## TOPIC 00052: niHSDIO Get Ext Cal Last Temp VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_get_ext_cal_last_temp.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_get_ext_cal_last_temp.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Get Ext Cal Last Temp VI

Installed With:

Returns the onboard temperature of the device in degrees Celsius during the last successful external calibration.

[IMAGE alt='niHSDIO Get Ext Cal Last Temp' src='nihsdio_get_ext_cal_last_temp.gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | temperature returns the onboard temperature of the device (in degrees Celsius) during the last successful external calibration. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_get_ext_cal_recommended_interval.html language=enus -->
## TOPIC 00053: niHSDIO Get Ext Cal Recommended Interval VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_get_ext_cal_recommended_interval.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_get_ext_cal_recommended_interval.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Get Ext Cal Recommended Interval VI

Installed With:

Returns the recommended number of months between external calibrations.

[IMAGE alt='niHSDIO Get Ext Cal Recommended Interval' src='nihsdio_get_ext_cal_recommended_interval.gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | months specifies the recommended maximum interval, in months, between external calibrations. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_get_self_cal_last_date_and_time.html language=enus -->
## TOPIC 00054: niHSDIO Get Self Cal Last Date And Time VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_get_self_cal_last_date_and_time.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_get_self_cal_last_date_and_time.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Get Self Cal Last Date And Time VI

Installed With:

Returns the date and time of the most recent successful self-calibration.

The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this VI returns 14 for the hours parameter and 30 for the minutes parameter.

[IMAGE alt='niHSDIO Get Self Cal Last Date And Time' src='nihsdio_get_self_cal_last_date_and_time.gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | year returns the year in which the device was last calibrated. |
|  | month returns the month in which the device was last calibrated. |
|  | day returns the day on which the device was last calibrated. |
|  | hour returns the hour (in 24-hour time) in which the device was last calibrated. |
|  | minute returns the minute in which the device was last calibrated. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_get_self_cal_last_temp.html language=enus -->
## TOPIC 00055: niHSDIO Get Self Cal Last Temp VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_get_self_cal_last_temp.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_get_self_cal_last_temp.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Get Self Cal Last Temp VI

Installed With:

Returns the onboard temperature of the device in degrees Celsius during the last successful self-calibration.

[IMAGE alt='niHSDIO Get Self Cal Last Temp' src='nihsdio_get_self_cal_last_temp.gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | temperature returns the onboard temperature of the device (in degrees Celsius) during the last successful self-calibration. |
|  | instrument handle out passes a reference to your calibration session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_hwc_fetch_sample_errors_u32.html language=enus -->
## TOPIC 00056: niHSDIO HWC Fetch Sample Errors (U32) VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_hwc_fetch_sample_errors_u32.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_hwc_fetch_sample_errors_u32.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO HWC Fetch Sample Errors (U32) VI

Installed With:

Returns the sample error information from a hardware comparison operation.

**Related Topics**

- Hardware Comparison

[IMAGE alt='niHSDIO HWC Fetch Sample Errors (U32)' src='nihsdio_hwc_fetch_sample_errors_(u32).gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | sample errors to read specifies the number of sample errors to read. |
|  | max time milliseconds specifies, in milliseconds, the time allotted for the VI to complete before NI-HSDIO returns a timeout error. If you set the value to -1, the VI never times out. If you set this parameter to 0, the VI returns immediately with up to the number of samples specified in samples to read. If samples to read is greater than the number of samples in the device memory and all the available samples are acquired before a timeout, NI-HSDIO returns the available samples. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | number of sample errors read returns the total number of sample errors read from device memory. |
|  | sample numbers returns the array of sample indexes in which an error occurred. |
|  | error bits returns an array containing the channels, or bits, in which an error occured for each sample with an error. 1 indicates an error. 0 indicates no error. |
|  | repeat count returns the number of times the error was repeated. This parameter only yields data when the Filter Repeated Sample Errors property is set to True. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_pal.html language=enus -->
## TOPIC 00057: NI-HSDIO VIs

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-HSDIO VIs

Installed With:

June 2013, 372527F-01

Use the NI-HSDIO VIs to create a high-speed digital I/O application for your NI digital waveform generator/analyzer.

| Subpalette | Description |
| --- | --- |
| Dynamic & Static Acquisition | Use Dynamic & Static Acquisition VIs to program dynamic and static acquisition operations. |
| Dynamic & Static Generation | Use the Dynamic & Static Generation VIs to create applications that generate static or dynamic digital data. |

© 2003–2013 National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_read_current_temperature.html language=enus -->
## TOPIC 00058: niHSDIO Read Current Temperature VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_read_current_temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_read_current_temperature.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Read Current Temperature VI

Installed With:

Returns the current onboard temperature of the device in degrees Celsius.

[IMAGE alt='niHSDIO Read Current Temperature' src='nihsdio_read_current_temperature.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | temperature returns the onboard temperature of the device in degrees Celsius. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/nihsdio_set_cal_user_defined_info.html language=enus -->
## TOPIC 00059: niHSDIO Set Cal User Defined Info VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/nihsdio_set_cal_user_defined_info.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/nihsdio_set_cal_user_defined_info.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Set Cal User Defined Info VI

Installed With:

Stores a user-defined string of characters in the device onboard EEPROM. If the string is longer than the maximum allowable size, it is truncated.

This VI overwrites any existing user-defined information. If you call this VI in a session, information is immediately changed. If you call this VI in an external calibration session, information is changed only after you close the session using the [niHSDIO Close Ext Cal](hsdio_close_ext_cal.html) VI with calibration close action set to **Commit**.

[IMAGE alt='niHSDIO Set Cal User Defined Info' src='nihsdio_set_cal_user_defined_info.gif']

|  | instrument handle identifies your calibration session. instrument handle is obtained from the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | info specifies the string to store in the onboard EEPROM. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/ppropertynode.html language=enus -->
## TOPIC 00060: niHSDIO Property Node VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/ppropertynode.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/ppropertynode.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Property Node VI

Installed With:

The niHSDIO Property Node is used to set, get, or check properties.

Some NI-HSDIO properties are channel based. When a property is channel based, you must specify an active channel before setting, getting, or checking properties.

[IMAGE alt='niHSDIO Property Node' src='nihsdio_property_node.gif']

|  | reference passes a reference to your instrument session to the next VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | reference out passes a reference to your instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/scripting_pal.html language=enus -->
## TOPIC 00061: Scripting

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/scripting_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/scripting_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Scripting

Owning Palette:

Generation Configuration

Installed With:

Use the Scripting VIs to create and configure scripts for your generation operation.

| Palette Object | Description |
| --- | --- |
| niHSDIO Configure Generation Mode | Specifies whether to initiate the waveform generation based on a specified script or based on a waveform. |
| niHSDIO Write Script | Writes a string to the onboard memory containing scripts that govern the waveform generation. |
| niHSDIO Configure Script To Generate | Sets the script that is generated after you call the niHSDIO Initiate VI when the generation mode parameter of the niHSDIO Configure Generation Mode VI is set to Scripted. If multiple scripts load when the niHSDIO Initiate VI is called, one script must be designated the script to generate or you receive an error. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/set_named_wvfm.html language=enus -->
## TOPIC 00062: niHSDIO Set Named Waveform Next Write Position VI

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/set_named_wvfm.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/set_named_wvfm.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO Set Named Waveform Next Write Position VI

Installed With:

Modifies where to next write within a named waveform.

The [niHSDIO Write Named Waveform](hsdio_write_nm.html) VI always begins writing at the current write position. Existing data in the waveform is overwritten.

**Related Topics**

- Generation Onboard Memory

[Details](#details)

[IMAGE alt='niHSDIO Set Named Waveform Next Write Position' src='nihsdio_set_named_waveform_next_write_position.gif']

|  | instrument handle identifies your instrument session. instrument handle is obtained from the niHSDIO Init Acquisition Session VI, the niHSDIO Init Generation Session VI, or the niHSDIO Init Ext Cal VI. |
| --- | --- |
|  | waveform name specifies the name to associate with the allocated waveform memory. |
|  | position specifies where to place the write position, in conjunction with offset. Current Write Position (45) The offset is relative to the current write position in the waveform. Start of Waveform (44) The offset is relative to the beginning of the waveform. |
| Current Write Position (45) | The offset is relative to the current write position in the waveform. |
| Start of Waveform (44) | The offset is relative to the beginning of the waveform. |
|  | offset specifies an offset for the write position within the named waveform. offset is in samples. Before issuing a write waveform command, the offset relative to the start of the waveform must be a multiple of 32 samples for NI 654x/655x devices (64 samples for the NI 6547/6548 in DDR mode) and a multiple of 64 samples for NI 656x devices (128 samples for the NI 656x is in DDR mode). |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niHSDIO Init Acquisition Session VI or the niHSDIO Init Generation Session VI. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Details

**position** and **offset** are used together to determine the next write position. **position** describes an absolute or relative move. **offset** is the number of samples to shift the next write position. You must always set the write position at a position that is a multiple of 32 samples for NI 654*x*/655*x* devices (64 samples for the NI 6547/6548 in DDR mode) or a multiple of 64 samples for NI 656*x* devices (128 samples for the NI 656*x* in DDR mode).

The following table shows examples of combinations of **position** and **offset**.

| Position | Offset | Next Write Position |
| --- | --- | --- |
| Start of Waveform | 0 | Start of waveform |
| Start of Waveform | 5 | Sixth sample of waveform |
| Start of Waveform | -1 | ERROR. These settings would try to place write position before start of waveform. |
| Current Write Position | 0 | No effect. These settings leave the next write position unchanged. |
| Current Write Position | 10 | Shift write position 10 samples ahead from current location. This position setting is valid only if the current write position plus this offset is in the waveform. |
| Current Write Position | -10 | Shift write position 10 samples back from current location. This position setting is valid only if the current write position is greater than 10. |

The write position is moved to the end of the most recently written data after each use of the [niHSDIO Write Named Waveform](hsdio_write_nm.html) VI. Thus you do not need to explicitly use the niHSDIO Set Named Waveform Next Write Position VI.

Setting the **position** beyond the bounds of the allocated space produces an error.

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/static_acquisition_pal.html language=enus -->
## TOPIC 00063: Static Acquisition

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/static_acquisition_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/static_acquisition_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Static Acquisition

Owning Palette:

Dynamic & Static Acquisition

Installed With:

Use the Static Acquisition VIs to program static acquisition operations.

| Palette Object | Description |
| --- | --- |
| niHSDIO Assign Static Channels | Configures DIO and PFI channels for static acquisition (if instrument handle is an acquisition session) or for static generation (if instrument handle is a generation session). |
| niHSDIO Read Static (U32) | Immediately reads the digital value on channels configured for static acquisition. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/static_generation_pal.html language=enus -->
## TOPIC 00064: Static Generation

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/static_generation_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/static_generation_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Static Generation

Owning Palette:

Dynamic & Static Generation

Installed With:

Use the Static Generation VIs to program static generation operations.

| Palette Object | Description |
| --- | --- |
| niHSDIO Assign Static Channels | Configures DIO and PFI channels for static acquisition (if instrument handle is an acquisition session) or for static generation (if instrument handle is a generation session). |
| niHSDIO Write Static (U32) | Writes to channels configured for static generation. You can configure a channel for static generation using the niHSDIO Assign Static Channels VI. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/stpmu_pal.html language=enus -->
## TOPIC 00065: Software-Timed PMU

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/stpmu_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/stpmu_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Software-Timed PMU

Owning Palette:

Dynamic & Static Generation

Installed With:

Use the Software-Timed PMU VIs to measure and source voltages and currents in your system.

| Palette Object | Description |
| --- | --- |
| niHSDIO stPMU Source Voltage | Enables the PMU capabilities on the channels specified in the channel list parameter and sources the voltage specified in the voltage level parameter. |
| niHSDIO stPMU Source Current | Enables the PMU capabilities on the channels specified in the channel list parameter and sources the current specified in the current level parameter while maintaining the voltage within the specified limits. |
| niHSDIO stPMU Measure Voltage | Measures the voltage on the channels specified in the channel list parameter. You can call this VI at any time, including while in a digital state or a PMU state. |
| niHSDIO stPMU Measure Current | Measures the current on the channels specified in the channel list parameter. You must call the niHSDIO stPMU Source Current or the niHSDIO stPMU Source Voltage VI before measuring current with this VI, or NI-HSDIO returns an error. |
| niHSDIO stPMU Disable PMU | Disables the PMU source operations on the channels specified in the channel list parameter. Use the return state (tristate) parameter to tristate or return each channel to its previous digital state. |

| Subpalette | Description |
| --- | --- |
| Advanced stPMU | Use the Advanced stPMU VIs to force and sense external signals in your system. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/utility_pal.html language=enus -->
## TOPIC 00066: Utility

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/utility_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Utility

Owning Palette:

Dynamic & Static Generation

Installed With:

Use the Utility VIs to access utility features of NI-HSDIO.

| Palette Object | Description |
| --- | --- |
| niHSDIO Commit | Programs the hardware for the data operation using the properties you select. Before entering the committed state, most property values are stored in software only; these values have not yet been programmed to the hardware. After the session is committed, the hardware is configured. |
| niHSDIO Convert Binary To WDT | Converts unsigned binary data into the digital waveform data type (WDT). Use this VI to easily create extended state (0, 1, H, L, X, Z) digital waveforms from binary data. |
| niHSDIO Error Message | Takes the error code returned by the NI-HSDIO VIs, interprets it, and returns it as a readable string. |
| niHSDIO Get Session Reference | Returns a session reference you can pass to NI-TClk VIs. Session references are of generic type, which means that the corresponding wires are blue-green, unlike the wires for regular instrument driver sessions. |
| niHSDIO Is Done | Checks the hardware to determine if the device completed the dynamic data operation or if any errors have occurred. You can also use this VI for continuous dynamic data operations to poll for error conditions. |
| niHSDIO Reset | Resets the session to its initial state. All channels and front panel terminals are put into a high-impedance state. All software attributes are reset to their initial values. During a reset, signal routes between this and other devices are released, regardless of which device created the route. For instance, a trigger signal being exported to a PXI trigger line and used by another device is no longer exported. |
| niHSDIO Reset Device | Resets the device to its initial state and reloads the FPGA. All channels and front panel terminals are put into a high-impedance state. All software attributes are reset to their initial values. The entire contents of the FPGA and EEPROM files are reloaded. Use this VI to re-enable your device if it has disabled itself because the device temperature has risen above its optimal operating temperature. |
| niHSDIO Self Test | Performs a self-test on the instrument and returns the test results. The niHSDIO Self Test VI performs a simple series of tests that ensure the instrument is powered up and responding. Complete functional testing and calibration are not performed by this function. |
| niHSDIO Send Software Edge Trigger | Forces a particular edge, pattern match, or software trigger to occur. |

| Subpalette | Description |
| --- | --- |
| Calibration | Use the Calibration VIs to access calibration operations. |

<!--NI_TOPIC bundle=ni-hsdio-labview-api-ref path=hsdioviref/waveform_control_pal.html language=enus -->
## TOPIC 00067: Waveform Control

- bundle_id: `ni-hsdio-labview-api-ref`
- source_path: `hsdioviref/waveform_control_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-labview-api-ref/raw/resource/enus/hsdioviref/waveform_control_pal.html
- document_id: `ni-hsdio-labview-api-ref`
- page_type: `leaf`
- content_type: ``

### Waveform Control

Owning Palette:

Generation Configuration

Installed With:

Use the Waveform Control VIs to configure the waveforms in your generation operation.

| Palette Object | Description |
| --- | --- |
| niHSDIO Configure Waveform To Generate | Sets the waveform to be generated after a call to the niHSDIO Initiate VI when the generation mode parameter of the niHSDIO Configure Generation Mode VI is set to Waveform. Waveform is the default value for the generation mode. |
| niHSDIO Allocate Named Waveform | Reserves waveform space in onboard memory and associates a waveform name with it. Individual waveforms are stored contiguously in onboard memory. |
| niHSDIO Delete Named Waveform | Frees waveform space in onboard memory. |
| niHSDIO Set Named Waveform Next Write Position | Modifies where to next write within a named waveform. |
