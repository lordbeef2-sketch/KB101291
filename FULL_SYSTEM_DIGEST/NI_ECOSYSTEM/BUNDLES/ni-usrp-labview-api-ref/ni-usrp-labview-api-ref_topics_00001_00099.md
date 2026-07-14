# NI DOCUMENT BUNDLE: ni-usrp-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-usrp-labview-api-ref start=1 end=99 -->
<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/dir-mnu.html language=enus -->
## TOPIC 00001: NI-USRP VIs

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/dir-mnu.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-USRP VIs to develop applications for USRP devices. These VIs cannot be used with USRP RIO VIs. icon Palette Object Description Rx Use the niUSRP Rx VIs to develop receiver applications for USRP devices. Tx Use the niUSRP Tx VIs to develop transmitter applications for USRP devices. niUSRP

### NI-USRP VIs

Use the NI-USRP VIs to develop applications for USRP devices. These VIs cannot be used with USRP RIO VIs.

[IMAGE alt='icon' src='dir-mnu.png']

| Palette Object | Description |
| --- | --- |
| Rx | Use the niUSRP Rx VIs to develop receiver applications for USRP devices. |
| Tx | Use the niUSRP Tx VIs to develop transmitter applications for USRP devices. |
| niUSRP Property Node VI | Gets (reads) or sets (writes) NI-USRP properties. When you read a property, NI-USRP analyzes the current configuration and returns the coerced value for that property. Setting a property may transition the session to the Initialized state. |
| Synchronization | Use the niUSRP Synchronization VIs to synchronize timing in applications for USRP devices. |
| Utility | Use the niUSRP Utility VIs to access utility features of NI-USRP. |

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-abort-vi.html language=enus -->
## TOPIC 00002: niUSRP Abort VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-abort-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-abort-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops an acquisition previously started. For finite acquisitions, calling this VI is optional unless you want to stop the acquisition before it completes. If the acquisition aborts successfully, the driver transitions to the Done state. icon Inputs/Outputs civrn.png session handle session handle ide

### niUSRP Abort VI

Stops an acquisition previously started.

For finite acquisitions, calling this VI is optional unless you want to stop the acquisition before it completes. If the acquisition aborts successfully, the driver transitions to the Done state.

[IMAGE alt='icon' src='niusrp-abort-vi.png']

#### Inputs/Outputs

| session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Rx

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-clear-command-time-vi.html language=enus -->
## TOPIC 00003: niUSRP Clear Command Time VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-clear-command-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-clear-command-time-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears command times, causing future control commands to take effect immediately. Previous control commands will still occur at their associated command times. icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) on which to set the configuration civrn.png session handle s

### niUSRP Clear Command Time VI

Clears command times, causing future control commands to take effect immediately. Previous control commands will still occur at their associated command times.

[IMAGE alt='icon' src='niusrp-clear-command-time-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) on which to set the configuration session handle — session handle identifies your instrument session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Synchronization

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-clear-error-vi.html language=enus -->
## TOPIC 00004: niUSRP Clear Error VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-clear-error-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-clear-error-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the last error code. icon Inputs/Outputs civrn.png session handle session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. cerrcodeclst.p

### niUSRP Clear Error VI

Clears the last error code.

[IMAGE alt='icon' src='niusrp-clear-error-vi.png']

#### Inputs/Outputs

| session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-close-session-vi.html language=enus -->
## TOPIC 00005: niUSRP Close Session VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-close-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-close-session-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session handle to the device. icon Inputs/Outputs civrn.png session handle session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. c

### niUSRP Close Session VI

Closes the session handle to the device.

[IMAGE alt='icon' src='niusrp-close-session-vi.png']

#### Inputs/Outputs

| session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Rx

Parent topic:

Tx

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-commit-vi.html language=enus -->
## TOPIC 00006: niUSRP Commit VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-commit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-commit-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Validates any changed properties and commits the settings to the device. This VI also starts the process of locking to a reference frequency if you specify a source using the Reference Frequency Source property. If the commit operation is successful, the driver transitions to the Committed state. ic

### niUSRP Commit VI

Validates any changed properties and commits the settings to the device.

This VI also starts the process of locking to a reference frequency if you specify a source using the [Reference Frequency Source](/csh?context=niusrp_usrppropref_pniusrp_referencefrequencysource) property. If the commit operation is successful, the driver transitions to the Committed state.

[IMAGE alt='icon' src='niusrp-commit-vi.png']

#### Inputs/Outputs

| session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-configure-gpio-pins-vi.html language=enus -->
## TOPIC 00007: niUSRP Configure GPIO Pins VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-configure-gpio-pins-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-configure-gpio-pins-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the X410 GPIO signal properties such as direction (I/O), voltage level, and master for multiple pins on a selected 'bank' and a 12-bit binary 'mask' to indicate which pins to configure. Please see the GPIO API for more help, https://files.ettus.com/manual/page_x400_gpio_api.html icon Inpu

### niUSRP Configure GPIO Pins VI

Configures the X410 GPIO signal properties such as direction (I/O), voltage level, and master for multiple pins on a selected 'bank' and a 12-bit binary 'mask' to indicate which pins to configure. Please see the GPIO API for more help, https://files.ettus.com/manual/page_x400_gpio_api.html

[IMAGE alt='icon' src='niusrp-configure-gpio-pins-vi.png']

#### Inputs/Outputs

| bank — the string name of which bank's pins to configure (GPIO0/GPIO1) channel list — channel list specifies the channel(s) to configure. session handle — session handle out passes a reference to your instrument session to the next VI. mask — 12-bit binary bitmask to signify which pins on the selected bank to configure (1 means configure, 0 means do not change). The port mapping should be set to DIO mapping so the 0 bit of mask will correspond to the 0 pin on the GPIO, the 1 bit will correspond to the 1 pin, and so on. direction — unsigned integer for the direction of the pins being configured (1 is output, 0 is input) voltage level — Voltage level not currently supported by UHD. Need to change voltage through MPM call. Unsigned integer for the voltage level to set the pins being configured error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. master — string for what master drives the pins being configured session handle out — session handle out passes a reference to your instrument session to the next VI. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-configure-number-of-samples-vi.html language=enus -->
## TOPIC 00008: niUSRP Configure Number of Samples VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-configure-number-of-samples-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-configure-number-of-samples-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device operation is finite or continuous and the number of samples to acquire. icon Inputs/Outputs civrn.png session handle session handle identifies your instrument session. session handle is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx)

### niUSRP Configure Number of Samples VI

Specifies whether the device operation is finite or continuous and the number of samples to acquire.

[IMAGE alt='icon' src='niusrp-configure-number-of-samples-vi.png']

#### Inputs/Outputs

| session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. number of samples is finite — number of samples is finite specifies whether the device acquires a finite number of samples or acquires samples continuously. The default value is FALSE. TRUE The device acquires a finite number of samples. FALSE The device acquires samples continuously. number of samples — number of samples specifies the number of samples to acquire from the device. This value is ignored if number of samples is finite is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE | The device acquires a finite number of samples. |
| FALSE | The device acquires samples continuously. |

Parent topic:

Rx

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-configure-signal-vi.html language=enus -->
## TOPIC 00009: niUSRP Configure Signal VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-configure-signal-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-configure-signal-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures properties of the transmit (Tx) or receive (Rx) signal. The USRP devices are not calibrated. The gain value does not represent an absolute gain and does not have linear behavior. Different devices exhibit different gain curves for different carrier frequencies. You may need to experiment

### niUSRP Configure Signal VI

Configures properties of the transmit (Tx) or receive (Rx) signal.

Note

[IMAGE alt='icon' src='niusrp-configure-signal-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) to configure. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. IQ rate — IQ rate specifies the rate of the baseband I/Q data in samples per second (S/s). carrier frequency — carrier frequency specifies the carrier frequency, in Hz, of the RF signal. gain — gain specifies the aggregate gain, in dB, applied to the RF signal. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. active antenna — active antenna specifies the antenna port to use for this channel. Refer to the antenna names topic for your device for a list of antenna names that active antenna accepts. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. coerced IQ rate — coerced IQ rate returns the actual I/Q rate, in samples per second (S/s), for this session, coerced to a value supported by the device. coerced carrier frequency — coerced carrier frequency returns the actual carrier frequency, in Hz, for this session, coerced to a value supported by the device. coerced gain — coerced gain returns the actual gain, in dB, for this session, coerced to a value supported by the device. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Rx

Parent topic:

Tx

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-configure-trigger-vi.html language=enus -->
## TOPIC 00010: niUSRP Configure Trigger VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-configure-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-configure-trigger-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the trigger generated by the onboard device timer. The trigger specifies the time to acquire or generate the first sample. icon

### niUSRP Configure Trigger VI

Configures the trigger generated by the onboard device timer. The trigger specifies the time to acquire or generate the first sample.

[IMAGE alt='icon' src='niusrp-configure-trigger-vi.png']

Parent topic:

Synchronization

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-convert-from-gain-to-power-vi.html language=enus -->
## TOPIC 00011: niUSRP Convert From Gain To Power VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-convert-from-gain-to-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-convert-from-gain-to-power-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a dB gain value to an approximate dBm power level. Supported Devices: Ettus USRP X410 icon Inputs/Outputs cstr.png channel channel indicates channels on which to run the operation. civrn.png session handle session handle identifies your instrument session. session handle is obtained from th

### niUSRP Convert From Gain To Power VI

Converts a dB gain value to an approximate dBm power level.

**Supported Devices**: Ettus USRP X410

[IMAGE alt='icon' src='niusrp-convert-from-gain-to-power-vi.png']

#### Inputs/Outputs

| channel — channel indicates channels on which to run the operation. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. carrier frequency — carrier frequency specifies the carrier frequency, in Hz, of the RF signal. gain — gain specifies the aggregate gain, in dB, applied to the RF signal. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from this VI and identifies this receive (Rx) session. power — power outputs the converted power value. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-convert-from-power-to-gain-vi.html language=enus -->
## TOPIC 00012: niUSRP Convert From Power To Gain VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-convert-from-power-to-gain-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-convert-from-power-to-gain-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an approximate dBm power level to a dB gain value. Supported Devices: Ettus USRP X410 icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) to configure. civrn.png session handle session handle identifies your instrument session. session handle is obtained from the

### niUSRP Convert From Power To Gain VI

Converts an approximate dBm power level to a dB gain value.

**Supported Devices**: Ettus USRP X410

[IMAGE alt='icon' src='niusrp-convert-from-power-to-gain-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) to configure. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. carrier frequency — carrier frequency specifies the carrier frequency, in Hz, of the RF signal. power — error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from this VI and identifies this receive (Rx) session. gain — error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-disable-start-trigger-vi.html language=enus -->
## TOPIC 00013: niUSRP Disable Start Trigger VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-disable-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-disable-start-trigger-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the Start Trigger. When the Start Trigger is disabled, acquisitions and generations begin immediately when data is available. icon Inputs/Outputs civrn.png session handle session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the

### niUSRP Disable Start Trigger VI

Disables the Start Trigger. When the Start Trigger is disabled, acquisitions and generations begin immediately when data is available.

[IMAGE alt='icon' src='niusrp-disable-start-trigger-vi.png']

#### Inputs/Outputs

| session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Synchronization

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-export-signal-vi.html language=enus -->
## TOPIC 00014: niUSRP Export Signal VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-export-signal-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-export-signal-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a route to export the specified signal to the specified output terminal. Valid mapping is one-to-one such that Reference Frequency maps to REF OUT, Timebase Clock maps to PPS TRIG OUT, and LO maps to LO OUT. icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) to c

### niUSRP Export Signal VI

Creates a route to export the specified signal to the specified output terminal. Valid mapping is one-to-one such that Reference Frequency maps to REF OUT, Timebase Clock maps to PPS TRIG OUT, and LO maps to LO OUT.

[IMAGE alt='icon' src='niusrp-export-signal-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) to configure. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. signal — signal specifies the signal to route out of the device output terminal — error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Synchronization

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-fetch-rx-data-2d-cdb-vi.html language=enus -->
## TOPIC 00015: niUSRP Fetch Rx Data (2D CDB) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-fetch-rx-data-2d-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-fetch-rx-data-2d-cdb-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches complex, double-precision floating-point data from the specified channels. icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) from which to fetch the data. civrn.png session handle session handle identifies your instrument session. session handle is obtained from

### niUSRP Fetch Rx Data (2D CDB) VI

Fetches complex, double-precision floating-point data from the specified channels.

[IMAGE alt='icon' src='niusrp-fetch-rx-data-2d-cdb-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) from which to fetch the data. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. number of samples — number of samples specifies the number of samples to fetch from the acquisition channel. For finite acquisitions, if you specify a value of -1, NI-USRP returns all the remaining samples. NI-USRP returns the samples when the requested number of samples is retrieved from the device or when the timeout is exceeded, whichever happens first. timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been acquired. A negative value indicates to the driver to wait indefinitely. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. data — data returns the received baseband samples as an array of complex, double-precision floating-point data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. The total number of elements returned in the array equals the value of the number of samples input x the number of channels. Each row of the 2D array corresponds to a separate channel. The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of the Configure Signal VI. timestamp — timestamp returns the timestamp of the first receive (Rx) sample returned and indicates the time associated with the first sample of the waveform, according to the onboard device timer. timestamp is the time of the clock in seconds, interpreted as whole seconds.fractional seconds. whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. |

Parent topic:

niUSRP Fetch Rx Data (poly) VI

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-fetch-rx-data-2d-i16-vi.html language=enus -->
## TOPIC 00016: niUSRP Fetch Rx Data (2D I16) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-fetch-rx-data-2d-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-fetch-rx-data-2d-i16-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches complex, 16-bit signed integer data from the specified channels. To use the niUSRP Fetch Rx Data (2D I16) VI, you must set the Host Data Type property to I16. data returns binary values that range from 32,767 to -32,768. The corresponding floating-point values range from 1.0 to ‑1.0. Use the

### niUSRP Fetch Rx Data (2D I16) VI

Fetches complex, 16-bit signed integer data from the specified channels. To use the niUSRP Fetch Rx Data (2D I16) VI, you must set the [Host Data Type](/csh?context=niusrp_usrppropref_pniusrp_hostdatatype) property to I16.

**data** returns binary values that range from 32,767 to -32,768. The corresponding floating-point values range from 1.0 to ‑1.0. Use the following equations to convert values from binary to floating-point or from floating-point to binary:

*floating-point value* = *binary value*/32,768

*binary value* = *floating-point value* x 32,767

[IMAGE alt='icon' src='niusrp-fetch-rx-data-2d-i16-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) from which to fetch the data. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. number of samples — number of samples specifies the number of samples to fetch from the acquisition channel. For finite acquisitions, if you specify a value of -1, NI-USRP returns all the remaining samples. NI-USRP returns the samples when the requested number of samples is retrieved from the device or when the timeout is exceeded, whichever happens first. timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been acquired. A negative value indicates to the driver to wait indefinitely. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. data — data returns the received baseband samples as an array of complex, 16-bit signed integer data. The real and imaginary components of the data correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. I and Q are interleaved [I, Q, I, Q, ...] in the array. The total number of elements returned in the array equals (the value of the number of samples input x 2) x the number of channels. Each row of the 2D array corresponds to a separate channel. The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of the Configure Signal VI. timestamp — timestamp returns the timestamp of the first receive (Rx) sample returned and indicates the time associated with the first sample of the waveform, according to the onboard device timer. timestamp is the time of the clock in seconds, interpreted as whole seconds.fractional seconds. whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. |

Parent topic:

niUSRP Fetch Rx Data (poly) VI

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-fetch-rx-data-cdb-cluster-vi.html language=enus -->
## TOPIC 00017: niUSRP Fetch Rx Data (CDB Cluster) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-fetch-rx-data-cdb-cluster-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-fetch-rx-data-cdb-cluster-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches a cluster of complex, double-precision floating-point data from the specified channel. Modulation Toolkit VIs use the complex, double-precision floating-point cluster data type. Use this VI in applications that use Modulation Toolkit VIs. icon Inputs/Outputs cstr.png channel list channel lis

### niUSRP Fetch Rx Data (CDB Cluster) VI

Fetches a cluster of complex, double-precision floating-point data from the specified channel. Modulation Toolkit VIs use the complex, double-precision floating-point cluster data type. Use this VI in applications that use Modulation Toolkit VIs.

[IMAGE alt='icon' src='niusrp-fetch-rx-data-cdb-cluster-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) from which to fetch the data. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. number of samples — number of samples specifies the number of samples to fetch from the acquisition channel. For finite acquisitions, if you specify a value of -1, NI-USRP returns all the remaining samples. NI-USRP returns the samples when the requested number of samples is retrieved from the device or when the timeout is exceeded, whichever happens first. timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been acquired. A negative value indicates to the driver to wait indefinitely. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. data — data returns the received baseband samples as complex, double-precision floating-point data in a cluster, which also includes sampling information. t0 — t0 specifies the trigger (start) time of the acquired Y array. dt — dt specifies the time between values in the Y array. Y — Y specifies the complex-valued baseband waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. timestamp — timestamp returns the timestamp of the first receive (Rx) sample returned and indicates the time associated with the first sample of the waveform, according to the onboard device timer. timestamp is the time of the clock in seconds, interpreted as whole seconds.fractional seconds. whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 specifies the trigger (start) time of the acquired Y array. dt — dt specifies the time between values in the Y array. Y — Y specifies the complex-valued baseband waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
| whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. |

Parent topic:

niUSRP Fetch Rx Data (poly) VI

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-fetch-rx-data-cdb-vi.html language=enus -->
## TOPIC 00018: niUSRP Fetch Rx Data (CDB) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-fetch-rx-data-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-fetch-rx-data-cdb-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches complex, double-precision floating-point data from the specified channel. icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) from which to fetch the data. civrn.png session handle session handle identifies your instrument session. session handle is obtained from

### niUSRP Fetch Rx Data (CDB) VI

Fetches complex, double-precision floating-point data from the specified channel.

[IMAGE alt='icon' src='niusrp-fetch-rx-data-cdb-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) from which to fetch the data. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. number of samples — number of samples specifies the number of samples to fetch from the acquisition channel. For finite acquisitions, if you specify a value of -1, NI-USRP returns all the remaining samples. NI-USRP returns the samples when the requested number of samples is retrieved from the device or when the timeout is exceeded, whichever happens first. timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been acquired. A negative value indicates to the driver to wait indefinitely. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. data — data returns the received baseband samples as an array of complex, double-precision floating-point data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. Because the USRP is not a calibrated device, the units returned by data do not correspond to volts or dB. The Power Spectrum VI used in many of the example VIs returns the magnitude spectrum in Vrms^2 or dB relative to 1 Vrms/1 _. If you set the Power Spectrum input to return the spectrum in Vrms^2, you can convert Vrms^2 to volts. The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of the Configure Signal VI. timestamp — timestamp returns the timestamp of the first receive (Rx) sample returned and indicates the time associated with the first sample of the waveform, according to the onboard device timer. timestamp is the time of the clock in seconds, interpreted as whole seconds.fractional seconds. whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. |

Parent topic:

niUSRP Fetch Rx Data (poly) VI

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-fetch-rx-data-cdb-wdt-vi.html language=enus -->
## TOPIC 00019: niUSRP Fetch Rx Data (CDB WDT) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-fetch-rx-data-cdb-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-fetch-rx-data-cdb-wdt-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches complex, double-precision floating-point data in a waveform data type from the specified channel. icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) from which to fetch the data. civrn.png session handle session handle identifies your instrument session. session

### niUSRP Fetch Rx Data (CDB WDT) VI

Fetches complex, double-precision floating-point data in a waveform data type from the specified channel.

[IMAGE alt='icon' src='niusrp-fetch-rx-data-cdb-wdt-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) from which to fetch the data. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. number of samples — number of samples specifies the number of samples to fetch from the acquisition channel. For finite acquisitions, if you specify a value of -1, NI-USRP returns all the remaining samples. NI-USRP returns the samples when the requested number of samples is retrieved from the device or when the timeout is exceeded, whichever happens first. timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been acquired. A negative value indicates to the driver to wait indefinitely. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. data — data returns the received baseband samples as complex, double-precision floating-point data in a waveform data type, which also includes sampling information. timestamp — timestamp returns the timestamp of the first receive (Rx) sample returned and indicates the time associated with the first sample of the waveform, according to the onboard device timer. timestamp is the time of the clock in seconds, interpreted as whole seconds.fractional seconds. whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. |

Parent topic:

niUSRP Fetch Rx Data (poly) VI

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-fetch-rx-data-i16-vi.html language=enus -->
## TOPIC 00020: niUSRP Fetch Rx Data (I16) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-fetch-rx-data-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-fetch-rx-data-i16-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches complex, 16-bit signed integer data from the specified channel. To use the niUSRP Fetch Rx Data (I16) VI, you must set the Host Data Type property to I16. data returns binary values that range from 32,767 to -32,768. The corresponding floating point-values range from 1.0 to ‑1.0. Use the fol

### niUSRP Fetch Rx Data (I16) VI

Fetches complex, 16-bit signed integer data from the specified channel. To use the niUSRP Fetch Rx Data (I16) VI, you must set the [Host Data Type](/csh?context=niusrp_usrppropref_pniusrp_hostdatatype) property to I16.

**data** returns binary values that range from 32,767 to -32,768. The corresponding floating point-values range from 1.0 to ‑1.0. Use the following equations to convert values from binary to floating-point or from floating-point to binary:

*floating-point value* = *binary value*/32,768

*binary value* = *floating-point value* x 32,767

[IMAGE alt='icon' src='niusrp-fetch-rx-data-i16-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) from which to fetch the data. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. number of samples — number of samples specifies the number of samples to fetch from the acquisition channel. For finite acquisitions, if you specify a value of -1, NI-USRP returns all the remaining samples. NI-USRP returns the samples when the requested number of samples is retrieved from the device or when the timeout is exceeded, whichever happens first. timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been acquired. A negative value indicates to the driver to wait indefinitely. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. data — data returns the received baseband samples as an array of complex, 16-bit signed integer data. The real and imaginary components of the data correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. I and Q are interleaved [I, Q, I, Q, ...] in the array. The total number of elements returned in the array equals the value of the number of samples parameter x 2. The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of the Configure Signal VI. timestamp — timestamp returns the timestamp of the first receive (Rx) sample returned and indicates the time associated with the first sample of the waveform, according to the onboard device timer. timestamp is the time of the clock in seconds, interpreted as whole seconds.fractional seconds. whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. |

Parent topic:

niUSRP Fetch Rx Data (poly) VI

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-fetch-rx-data-poly-vi.html language=enus -->
## TOPIC 00021: niUSRP Fetch Rx Data (poly) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-fetch-rx-data-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-fetch-rx-data-poly-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches data from the specified channel list. icon

### niUSRP Fetch Rx Data (poly) VI

Fetches data from the specified channel list.

[IMAGE alt='icon' src='niusrp-fetch-rx-data-poly-vi.png']

- [niUSRP Fetch Rx Data (CDB Cluster) VI](../../instr-lib/niusrp/niusrp-fetch-rx-data-cdb-cluster-vi.html) Fetches a cluster of complex, double-precision floating-point data from the specified channel. Modulation Toolkit VIs use the complex, double-precision floating-point cluster data type. Use this VI in applications that use Modulation Toolkit VIs.
- [niUSRP Fetch Rx Data (CDB WDT) VI](../../instr-lib/niusrp/niusrp-fetch-rx-data-cdb-wdt-vi.html) Fetches complex, double-precision floating-point data in a waveform data type from the specified channel.
- [niUSRP Fetch Rx Data (CDB) VI](../../instr-lib/niusrp/niusrp-fetch-rx-data-cdb-vi.html) Fetches complex, double-precision floating-point data from the specified channel.
- [niUSRP Fetch Rx Data (I16) VI](../../instr-lib/niusrp/niusrp-fetch-rx-data-i16-vi.html) Fetches complex, 16-bit signed integer data from the specified channel. To use the niUSRP Fetch Rx Data (I16) VI, you must set the Host Data Type property to I16.
- [niUSRP Fetch Rx Data (2D CDB) VI](../../instr-lib/niusrp/niusrp-fetch-rx-data-2d-cdb-vi.html) Fetches complex, double-precision floating-point data from the specified channels.
- [niUSRP Fetch Rx Data (2D I16) VI](../../instr-lib/niusrp/niusrp-fetch-rx-data-2d-i16-vi.html) Fetches complex, 16-bit signed integer data from the specified channels. To use the niUSRP Fetch Rx Data (2D I16) VI, you must set the Host Data Type property to I16.

Parent topic:

Rx

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-find-devices-vi.html language=enus -->
## TOPIC 00022: niUSRP Find Devices VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-find-devices-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-find-devices-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of USRP devices discovered in the system. icon Inputs/Outputs cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standard error in functionality. i1dcclst.png niUSRP devices niUSRP devices returns an array of

### niUSRP Find Devices VI

Returns a list of USRP devices discovered in the system.

[IMAGE alt='icon' src='niusrp-find-devices-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niUSRP devices — niUSRP devices returns an array of niUSRP device clusters, where each niUSRP device cluster represents a device discovered in the system. Each niUSRP device cluster contains the following elements. address — address returns a string containing the IP address of the device. You can wire the address element to the device names input for the niUSRP Open Rx Session and the niUSRP Open Tx Session VIs. serial number — serial number returns a string containing the serial number of the device. model — model returns a string containing the model name of the device. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| address — address returns a string containing the IP address of the device. You can wire the address element to the device names input for the niUSRP Open Rx Session and the niUSRP Open Tx Session VIs. serial number — serial number returns a string containing the serial number of the device. model — model returns a string containing the model name of the device. |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-get-error-vi.html language=enus -->
## TOPIC 00023: niUSRP Get Error VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-get-error-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-get-error-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the error code and description for the last error that occurred. This VI is generally not needed because the error out outputs return fully formatted error information from each VI or Property Node. If you did not use error handling or if you lost an error, you can use this VI to retrieve th

### niUSRP Get Error VI

Returns the error code and description for the last error that occurred.

This VI is generally not needed because the **error out** outputs return fully formatted error information from each VI or Property Node. If you did not use error handling or if you lost an error, you can use this VI to retrieve the error information.

[IMAGE alt='icon' src='niusrp-get-error-vi.png']

#### Inputs/Outputs

| session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error code — error code returns the status error code for the last error that occurred. error description — error description returns the error message string for the last error that occurred. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-get-power-range-vi.html language=enus -->
## TOPIC 00024: niUSRP Get Power Range VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-get-power-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-get-power-range-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the approximate minimum and maximum dBm power levels for a given frequency. Supported Devices: Ettus USRP X410 icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) to configure. civrn.png session handle session handle identifies your instrument session. session handle

### niUSRP Get Power Range VI

Gets the approximate minimum and maximum dBm power levels for a given frequency.

**Supported Devices**: Ettus USRP X410

[IMAGE alt='icon' src='niusrp-get-power-range-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) to configure. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. carrier frequency — carrier frequency specifies the carrier frequency, in Hz, of the RF signal. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from this VI and identifies this receive (Rx) session. max reference level — max reference level defines the maximum power level the device can reach for a given frequency. If no frequency is supplied, the current configured frequency is chosen. If a power level greater than this range is selected, it will be clipped to the maximum. min reference level — min reference level defines the minimum power level the device can reach for a given frequency. If no frequency is supplied, the current configured frequency is chosen. If a power level less than this range is selected, it will be clipped to the minimum. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-get-time-vi.html language=enus -->
## TOPIC 00025: niUSRP Get Time VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-get-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-get-time-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the time value of the onboard device timer. icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) to configure. civrn.png session handle session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Op

### niUSRP Get Time VI

Returns the time value of the onboard device timer.

[IMAGE alt='icon' src='niusrp-get-time-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) to configure. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. when — when specifies when to get the timestamp from the onboard device timer. The default value is now. now (0) Gets the onboard device timer from the specified timestamp immediately. next timebase edge (1) Gets the onboard device timer from the specified timestamp at the next edge of the timebase clock. previous timebase edge (2) Gets the onboard device timer from the specified timestamp at the previous edge of the timebase clock. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. USRP Timestamp — USRP timestamp is a timestamp in the format used by USRP. USRP timestamp is the time of the clock in seconds, interpreted as whole seconds.fractional seconds. whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| now (0) | Gets the onboard device timer from the specified timestamp immediately. |
| next timebase edge (1) | Gets the onboard device timer from the specified timestamp at the next edge of the timebase clock. |
| previous timebase edge (2) | Gets the onboard device timer from the specified timestamp at the previous edge of the timebase clock. |
| whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. |  |

Parent topic:

Synchronization

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-initiate-vi.html language=enus -->
## TOPIC 00026: niUSRP Initiate VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-initiate-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-initiate-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts the Rx acquisition. The niUSRP Initiate VI starts the waveform acquisition in a receive (Rx) session. You must initiate the Rx session before you use a niUSRP Fetch Rx Data (poly) VI to retrieve waveform data. You do not need to call the niUSRP Initiate VI for transmit (Tx) sessions; you init

### niUSRP Initiate VI

Starts the Rx acquisition.

The niUSRP Initiate VI starts the waveform acquisition in a receive (Rx) session. You must initiate the Rx session before you use a [niUSRP Fetch Rx Data (poly)](niusrp-fetch-rx-data-poly-vi.html) VI to retrieve waveform data. You do not need to call the niUSRP Initiate VI for transmit (Tx) sessions; you initiate waveform generation when you provide data using the [niUSRP Write Tx Data (poly)](niusrp-write-tx-data-poly-vi.html) VI.

[IMAGE alt='icon' src='niusrp-initiate-vi.png']

#### Inputs/Outputs

| session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Rx Session VI and identifies a particular receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

If acquisition begins successfully, NI-USRP transitions to the Running state. If you configured a Start Trigger, the device begins waiting for the specified trigger. Use the niUSRP Initiate VI in conjunction with one of the [niUSRP Fetch Rx Data (poly)](niusrp-fetch-rx-data-poly-vi.html) VIs to retrieve the acquired data.

Parent topic:

Rx

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-lv-timestamp-to-usrp-timestamp-vi.html language=enus -->
## TOPIC 00027: niUSRP LV Timestamp to USRP Timestamp VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-lv-timestamp-to-usrp-timestamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-lv-timestamp-to-usrp-timestamp-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Translates a LabVIEW timestamp to a USRP timestamp. icon Inputs/Outputs catrn.png LabVIEW Timestamp LabVIEW timestamp is a timestamp with the format used in LabVIEW. The timestamp data is displayed in hours, minutes, seconds, and milliseconds, as well as the month, day, and year. cerrcodeclst.png Th

### niUSRP LV Timestamp to USRP Timestamp VI

Translates a LabVIEW timestamp to a USRP timestamp.

[IMAGE alt='icon' src='niusrp-lv-timestamp-to-usrp-timestamp-vi.png']

#### Inputs/Outputs

| LabVIEW Timestamp — LabVIEW timestamp is a timestamp with the format used in LabVIEW. The timestamp data is displayed in hours, minutes, seconds, and milliseconds, as well as the month, day, and year. — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. USRP Timestamp — USRP timestamp is a timestamp in the format used by USRP. USRP timestamp is the time of the clock in seconds, interpreted as whole seconds.fractional seconds. whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. — error out contains error information. This output provides standard error out functionality. |
| --- |
| whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-open-rx-session-vi.html language=enus -->
## TOPIC 00028: niUSRP Open Rx Session VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-open-rx-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-open-rx-session-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a receive (Rx) session to the device(s) you specify in the device names input and returns session handle out, which you use to identify this instrument session in all subsequent NI-USRP VIs. icon Inputs/Outputs civrn.png device names device names specifies the name(s) or IP address(es) of the

### niUSRP Open Rx Session VI

Opens a receive (Rx) session to the device(s) you specify in the **device names** input and returns **session handle out**, which you use to identify this instrument session in all subsequent NI-USRP VIs.

[IMAGE alt='icon' src='niusrp-open-rx-session-vi.png']

#### Inputs/Outputs

| device names — device names specifies the name(s) or IP address(es) of the device(s). reset — reset specifies whether to reset the device(s) to a known initialization state. Note reset has no effect in NI-USRP. All properties are set to their default values when a session is created. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from this VI and identifies this receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Rx

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-open-rx-session-with-custom-bitfile-vi.html language=enus -->
## TOPIC 00029: niUSRP Open Rx Session with Custom Bitfile VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-open-rx-session-with-custom-bitfile-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-open-rx-session-with-custom-bitfile-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a receive (Rx) session with a custom bitfile. The config and streaming parameters define the type of subsystems used and device functionality available. For most Ettus USRP X410 applications, set streaming as RIO and config as UHD. For Ettus USRP X410 applications with a custom FPGA, set strea

### niUSRP Open Rx Session with Custom Bitfile VI

Opens a receive (Rx) session with a custom bitfile.

The **config** and **streaming** parameters define the type of subsystems used and device functionality available.

For most Ettus USRP X410 applications, set **streaming** as RIO and **config** as UHD. For Ettus USRP X410 applications with a custom FPGA, set **streaming** as none and **config** as UHD. For Ettus USRP X410 applications using the FPGA as a co-processor and not transmitting or receiving an RF signal, set **streaming** as none and config as none.

For most other USRP applications, set **streaming** as UHD and **config** as UHD.

[IMAGE alt='icon' src='niusrp-open-rx-session-with-custom-bitfile-vi.png']

#### Inputs/Outputs

| device names — device names specifies the name(s) or IP address(es) of the device(s). reset — reset specifies whether to reset the device(s) to a known initialization state. Note reset has no effect in NI-USRP. All properties are set to their default values when a session is created. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. config — config defines the type of configuration subsystem being used. streaming — streaming defines the type of the streaming subsystem being used. bitfile path — bitfile path locates the custom bitfile to load. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from this VI and identifies this receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Rx

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-open-tx-session-vi.html language=enus -->
## TOPIC 00030: niUSRP Open Tx Session VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-open-tx-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-open-tx-session-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a transmit (Tx) session to the device(s) you specify in the device names input and returns session handle out, which you use to identify this instrument session in all subsequent NI-USRP VIs. icon Inputs/Outputs civrn.png device names device names specifies the name(s) or IP address(es) of the

### niUSRP Open Tx Session VI

Opens a transmit (Tx) session to the device(s) you specify in the **device names** input and returns **session handle out**, which you use to identify this instrument session in all subsequent NI-USRP VIs.

[IMAGE alt='icon' src='niusrp-open-tx-session-vi.png']

#### Inputs/Outputs

| device names — device names specifies the name(s) or IP address(es) of the device(s). reset — reset specifies whether to reset the device(s) to a known initialization state. Note reset has no effect in NI-USRP. All properties are set to their default values when a session is created. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from this VI and identifies this transmit (Tx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Tx

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-open-tx-session-with-custom-bitfile-vi.html language=enus -->
## TOPIC 00031: niUSRP Open Tx Session with Custom Bitfile VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-open-tx-session-with-custom-bitfile-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-open-tx-session-with-custom-bitfile-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a transmit (Tx) session with a custom bitfile. The config and streaming parameters define the type of subsystems used and device functionality available. For most Ettus USRP X410 applications, set streaming as RIO and config as UHD. For Ettus USRP X410 applications with a custom FPGA, set stre

### niUSRP Open Tx Session with Custom Bitfile VI

Opens a transmit (Tx) session with a custom bitfile.

The **config** and **streaming** parameters define the type of subsystems used and device functionality available.

For most Ettus USRP X410 applications, set **streaming** as RIO and **config** as UHD. For Ettus USRP X410 applications with a custom FPGA, set **streaming** as none and **config** as UHD. For Ettus USRP X410 applications using the FPGA as a co-processor and not transmitting or receiving an RF signal, set **streaming** as none and config as none.

For most other USRP applications, set **streaming** as UHD and **config** as UHD.

[IMAGE alt='icon' src='niusrp-open-tx-session-with-custom-bitfile-vi.png']

#### Inputs/Outputs

| device names — device names specifies the name(s) or IP address(es) of the device(s). reset — reset specifies whether to reset the device(s) to a known initialization state. Note reset has no effect in NI-USRP. All properties are set to their default values when a session is created. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. config — config defines the type of configuration subsystem being used. streaming — streaming defines the type of the streaming subsystem being used. bitfile path — bitfile path locates the custom bitfile to load. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from this VI and identifies this transmit (Tx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Tx

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-property-node-vi.html language=enus -->
## TOPIC 00032: niUSRP Property Node VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-property-node-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads) or sets (writes) NI-USRP properties. When you read a property, NI-USRP analyzes the current configuration and returns the coerced value for that property. Setting a property may transition the session to the Initialized state. Refer to niUSRP Properties for more information about using

### niUSRP Property Node VI

Gets (reads) or sets (writes) NI-USRP properties. When you read a property, NI-USRP analyzes the current configuration and returns the coerced value for that property. Setting a property may transition the session to the Initialized state.

Refer to [niUSRP Properties](/csh?context=niusrp_niusrp_p) for more information about using the NI-USRP properties.

[IMAGE alt='icon' src='niusrp-property-node-vi.png']

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp-p.html language=enus -->
## TOPIC 00033: niUSRP Properties

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp-p.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the niUSRP properties to access advanced configuration options for NI-USRP driver applications.

### niUSRP Properties

Use the niUSRP properties to access advanced configuration options for NI-USRP driver applications.

- [Active Channel](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-activechannel.html) Specifies the channel name used to access all subsequent properties in this instance of the property node. If the property you want to use is channel-based, you must first select this property and then pass the name of the specific channel. If the property you specify is not channel-based, or you want to set the property on all channels, pass an empty string or omit setting this property.
- [Clocking and Synchronization:Start Trigger Type](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-starttriggertype.html) Specifies the type of start trigger, which controls how the device generates or acquires signals. Use this property to choose whether to generate or acquire data immediately or to synchronize generations and acquisitions to the timestamp specified by the Start Trigger Time properties.
- [Clocking and Synchronization:Start Trigger Time (whole seconds)](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-starttriggertimefull.html) Specifies the whole seconds part of the trigger start time.
- [Clocking and Synchronization:Start Trigger Time (fractional seconds)](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-starttriggertimefractional.html) Specifies the fractional seconds part of the trigger start time.
- [Configuration:Enabled Channels](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-enabledchannels.html) Specifies the list of channels enabled for acquisition/generation for this session.
- [Clocking and Synchronization:Reference Frequency Source](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-referencefrequencysource.html) Specifies the source of the signal used as a frequency reference for the local oscillator (LO).
- [Clocking and Synchronization:Exported Reference Frequency Output Terminal](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-exportedreferencefrequencyoutputterminal.html) Specifies the output terminal of the exported reference frequency signal.
- [Clocking and Synchronization:Timebase Clock Source](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-timebaseclocksource.html) Specifies the source of the signal used as the timebase clock if you set the Start Trigger Type property to Time .
- [Clocking and Synchronization:Exported Timebase Clock Output Terminal](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-exportedtimebaseclockoutputterminal.html) Specifies the output terminal of the exported timebase clock (PPS) signal.
- [Clocking and Synchronization:Timebase Clock Polarity](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-timebaseclockpolarity.html) Specifies the polarity of the signal used as the timebase clock if you set the Start Trigger Type property to Time .
- [Clocking and Synchronization:Local Oscillator:LO Source](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-losource.html) Specifies the LO source for the selected channel.
- [Clocking and Synchronization:Local Oscillator:LO Export Enabled](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loexportenabled.html) Specifies whether or not to export the LO of the selected channel.
- [Clocking and Synchronization:Local Oscillator:LO IF1 Frequency](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif1frequency.html) Specifies the frequency, in Hz, of the IF1 LO.
- [Clocking and Synchronization:Local Oscillator:LO IF2 Frequency](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif2frequency.html) Specifies the frequency, in Hz, of the IF2 LO.
- [Clocking and Synchronization:Local Oscillator:Coerced LO IF1 Frequency](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif1frequencycoerced.html) Reads back the frequency, in Hz, of the IF1 LO.
- [Clocking and Synchronization:Local Oscillator:Coerced LO IF2 Frequency](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif2frequencycoerced.html) Reads back the frequency, in Hz, of the IF2 LO.
- [Configuration:Number of Samples Is Finite](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-numberofsamplesisfinite.html) Specifies whether the device acquires a finite number of samples or acquires samples continuously.
- [Configuration:Number of Samples](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-numberofsamples.html) Specifies the finite number of samples to acquire. This value is ignored if you set the Number of Samples is Finite property to FALSE .
- [Configuration:IQ Rate](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-iqrate.html) Specifies the sample rate of the baseband I/Q data for transmit (Tx) or receive (Rx) signals in samples per second (S/s).
- [Configuration:Carrier Frequency](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-carrierfrequency.html) Specifies the carrier frequency, in Hz, of the RF signal.
- [Configuration:Bandwidth](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-bandwidth.html) Specifies the bandwidth, in Hz, of the analog filter used in the RF front-end.
- [Configuration:Gain](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gain.html) Specifies the gain, in dB, applied to the RF signal for receive (Rx) and transmit (Tx) signals.
- [Configuration:Active Antenna](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-activeantenna.html) Specifies the antenna port to use for this channel.
- [Configuration:Power Reference](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-power.html) Specifies the power, in dBm, of a full-scale RF signal for receive (Rx) and transmit (Tx) signals.
- [Clocking and Synchronization:Local Oscillator:LO Distribution](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-lodistribution.html) Specifies the LO distribution for the selected channel. Only supported for N321
- [Configuration:Number of Channels in Session](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-numberofchannelsinsession.html) Returns the number of separate transmit (Tx) or receive (Rx) channels contained in the current driver session.
- [Configuration:Trig I/O Mode](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-trigiomode.html) Specifies the mode of the Trig In/Out terminal.
- [Configuration:Advanced:Host Data Type](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-hostdatatype.html) Specifies the data type to fetch from or write to the driver.
- [Configuration:Advanced:Sample Width](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-samplewidth.html) Specifies the width, in bits, of the binary data sample transferred across the bus between the host and the device.
- [Configuration:Advanced:Expected Peak](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-expectedpeak.html) Specifies the expected peak signal, as a fraction of the full-scale signal to acquire or generate. 1.0 = 100%, 0.5 = 50%. NI-USRP uses this value to scale 8-bit data transferred over the bus.
- [Configuration:Advanced:LO Frequency](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-lofrequency.html) Specifies the local oscillator (LO) frequency, in Hz.
- [Configuration:Advanced:Coerced LO Frequency](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-lofrequencycoerced.html) Reads back the coerced local oscillator (LO) frequency, in Hz.
- [Configuration:Advanced:ADC Self Calibration Mode](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-adcselfcalibrationmode.html) Specifies the operating mode for the ADC self-calibration blocks.
- [Configuration:Advanced:Warning Policy](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-warningpolicy.html) Specifies whether NI-USRP returns an error, returns a warning, or ignores overflow, underflow, or timeout conditions during data transfer.
- [Meta Information:Driver Identification:Current Driver Version](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-currentdriverversion.html) Returns a string that contains the current version information for the NI-USRP driver. For example, NI-USRP can return 1.3.0 .
- [Meta Information:Instrument Identification:Model](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-model.html) Returns a string that contains the model number or name of the device that you are currently using.
- [Meta Information:Instrument Identification:Current Firmware Version](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-currentfirmwareversion.html) Returns a string containing the current version of the firmware for the device you are currently using.
- [Meta Information:Instrument Identification:Oldest Compatible Firmware Version](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-oldestcompatiblefirmwareversion.html) Returns a string containing the oldest compatible version of the firmware for the device you are currently using.
- [Meta Information:Instrument Identification:Current FPGA Version](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-currentfpgaversion.html) Returns a string containing the current version of the FPGA image for the device you are currently using.
- [Meta Information:Instrument Identification:Oldest Compatible FPGA Version](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-oldestcompatiblefpgaversion.html) Returns a string containing the oldest compatible version of the FPGA image for the device you are currently using.
- [Clocking and Synchronization:GPS Disciplined Clock:Has GPS Disciplined Clock?](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-hasgpsdo.html) Returns TRUE if the device has a GPS-disciplined clock. This property allows the device to use a GPS clock reference and GPS timestamps.
- [Clocking and Synchronization:GPS Disciplined Clock:GPS Time (seconds)](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpstime.html) Returns the time that the GPS reports. Time is measured in seconds since 00:00:00 January 1, 1970 (UTC).
- [Clocking and Synchronization:GPS Disciplined Clock:GPS Lock Status](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpslockstatus.html) Returns True if the GPS has a satellite fix.
- [Clocking and Synchronization:GPS Disciplined Clock:GPS Sentence GGA](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpssentencegga.html) Returns the GPS fix data.
- [Clocking and Synchronization:GPS Disciplined Clock:GPS Sentence RMC](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpssentencermc.html) Returns the recommended minimum specific GPS and transit data.
- [Clocking and Synchronization:Data Clock Rate](../../../instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-dataclockrate.html) Specifies the data rate of samples coming from the analog-to-digital converters (ADCs) to the DSP or going to the digital-to-analog converters (DACs) from the DSP. Only the USRP-2900/2901 supports changing the data clock rate.

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-activeantenna.html language=enus -->
## TOPIC 00034: Configuration:Active Antenna

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-activeantenna.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-activeantenna.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the antenna port to use for this channel. Refer to the antenna names topic of your USRP device for a list of antenna names that this property accepts. Remarks The following table lists the characteristics of this property. Short Name Active Antenna Data type cstr.png Permissions Read/Write

### Configuration:Active Antenna

Specifies the antenna port to use for this channel.

Refer to the *antenna names* topic of your USRP device for a list of antenna names that this property accepts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Antenna |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-activechannel.html language=enus -->
## TOPIC 00035: Active Channel

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-activechannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-activechannel.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel name used to access all subsequent properties in this instance of the property node. If the property you want to use is channel-based, you must first select this property and then pass the name of the specific channel. If the property you specify is not channel-based, or you wa

### Active Channel

Specifies the channel name used to access all subsequent properties in this instance of the property node. If the property you want to use is channel-based, you must first select this property and then pass the name of the specific channel. If the property you specify is not channel-based, or you want to set the property on all channels, pass an empty string or omit setting this property.

Enter 0 for the first channel and 1 for the second channel. The order of the IP addresses sets the channel order.

**Default Value**: "" (empty string)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Channel |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-adcselfcalibrationmode.html language=enus -->
## TOPIC 00036: Configuration:Advanced:ADC Self Calibration Mode

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-adcselfcalibrationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-adcselfcalibrationmode.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the operating mode for the ADC self-calibration blocks. Remarks The following table lists the characteristics of this property. Short Name ADC Self Calibration Mode Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Disabled 0 ADC calibration block

### Configuration:Advanced:ADC Self Calibration Mode

Specifies the operating mode for the ADC self-calibration blocks.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ADC Self Calibration Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Disabled | 0 | ADC calibration blocks are "frozen" and not currently running. |
| --- | --- | --- |
| Running | 1 | ADC calibration blocks are actively self-adjusting. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-bandwidth.html language=enus -->
## TOPIC 00037: Configuration:Bandwidth

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-bandwidth.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth, in Hz, of the analog filter used in the RF front-end. This property sets an upper limit to the maximum bandwidth that the device can acquire or generate. Refer to your device specifications for more information about available bandwidth options. The range of available values

### Configuration:Bandwidth

Specifies the bandwidth, in Hz, of the analog filter used in the RF front-end.

This property sets an upper limit to the maximum bandwidth that the device can acquire or generate. Refer to your device specifications for more information about available bandwidth options.

The range of available values is hardware dependent. If you specify a value outside the range supported by your device, NI-USRP coerces the value to the nearest supported value. Writing to this property specifies the value you want to use. Reading from this property returns the actual value, which may have been coerced to the capabilities of the device. NI recommends that you read the value after you write to this property to determine the actual setting for the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Bandwidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niUSRP Configure Signal |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-carrierfrequency.html language=enus -->
## TOPIC 00038: Configuration:Carrier Frequency

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-carrierfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-carrierfrequency.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the carrier frequency, in Hz, of the RF signal. The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and additional frequency translation implemented in the digital signal processing on the FPGA. To set the LO to a spe

### Configuration:Carrier Frequency

Specifies the carrier frequency, in Hz, of the RF signal.

The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and additional frequency translation implemented in the digital signal processing on the FPGA. To set the LO to a specific frequency, set the [LO Frequency](pniusrp-lofrequency.html) property.

The range of available values is hardware dependent. If you specify a value outside the range supported by your device, NI-USRP coerces the value to the nearest supported value. Writing to this property specifies the value you want to use. Reading from this property returns the actual value, which may have been coerced to the capabilities of the device. NI recommends that you read the value after you write to this property to determine the actual setting for the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Carrier Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niUSRP Configure Signal |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-currentdriverversion.html language=enus -->
## TOPIC 00039: Meta Information:Driver Identification:Current Driver Version

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-currentdriverversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-currentdriverversion.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the current version information for the NI-USRP driver. For example, NI-USRP can return 1.3.0. Remarks The following table lists the characteristics of this property. Short Name Current Driver Version Data type cstr.png Permissions Read Only High-level VIs N/A Channel-

### Meta Information:Driver Identification:Current Driver Version

Returns a string that contains the current version information for the NI-USRP driver. For example, NI-USRP can return 1.3.0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Driver Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-currentfirmwareversion.html language=enus -->
## TOPIC 00040: Meta Information:Instrument Identification:Current Firmware Version

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-currentfirmwareversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-currentfirmwareversion.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the current version of the firmware for the device you are currently using. Remarks The following table lists the characteristics of this property. Short Name Current Firmware Version Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based Yes Resettable

### Meta Information:Instrument Identification:Current Firmware Version

Returns a string containing the current version of the firmware for the device you are currently using.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current Firmware Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-currentfpgaversion.html language=enus -->
## TOPIC 00041: Meta Information:Instrument Identification:Current FPGA Version

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-currentfpgaversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-currentfpgaversion.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the current version of the FPGA image for the device you are currently using. Remarks The following table lists the characteristics of this property. Short Name Current FPGA Version Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based Yes Resettable N

### Meta Information:Instrument Identification:Current FPGA Version

Returns a string containing the current version of the FPGA image for the device you are currently using.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Current FPGA Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-dataclockrate.html language=enus -->
## TOPIC 00042: Clocking and Synchronization:Data Clock Rate

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-dataclockrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-dataclockrate.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data rate of samples coming from the analog-to-digital converters (ADCs) to the DSP or going to the digital-to-analog converters (DACs) from the DSP. Only the USRP-2900/2901 supports changing the data clock rate. Remarks The following table lists the characteristics of this property. S

### Clocking and Synchronization:Data Clock Rate

Specifies the data rate of samples coming from the analog-to-digital converters (ADCs) to the DSP or going to the digital-to-analog converters (DACs) from the DSP. Only the USRP-2900/2901 supports changing the data clock rate.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Clock Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-enabledchannels.html language=enus -->
## TOPIC 00043: Configuration:Enabled Channels

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-enabledchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-enabledchannels.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the list of channels enabled for acquisition/generation for this session. Valid Values: "0","1","0,1",etc. Default Value: all channels Remarks The following table lists the characteristics of this property. Short Name Enabled Channels Data type cstr.png Permissions Read/Write High-level VI

### Configuration:Enabled Channels

Specifies the list of channels enabled for acquisition/generation for this session.

**Valid Values**: "0","1","0,1",etc.

**Default Value**: all channels

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enabled Channels |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-expectedpeak.html language=enus -->
## TOPIC 00044: Configuration:Advanced:Expected Peak

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-expectedpeak.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-expectedpeak.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the expected peak signal, as a fraction of the full-scale signal to acquire or generate. 1.0 = 100%, 0.5 = 50%. NI-USRP uses this value to scale 8-bit data transferred over the bus. USRP devices support 16-bit values, which allow a full-scale binary data range from -32,768 to 32,767. When

### Configuration:Advanced:Expected Peak

Specifies the expected peak signal, as a fraction of the full-scale signal to acquire or generate. 1.0 = 100%, 0.5 = 50%. NI-USRP uses this value to scale 8-bit data transferred over the bus.

USRP devices support 16-bit values, which allow a full-scale binary data range from -32,768 to 32,767. When using an 8-bit sample width, transfer the 8-bit samples that contain the significant values of your signal. Use the Expected Peak property to specify the fraction of the full-scale range you expect your signal to occupy so that you transfer the most significant bits.

Use the following equation to determine the value for the Expected Peak property:

*Expected Actual Signal Range*/*Full-Scale Range* = *Expected Peak Property Value*

For example, if your input signal range is -128 to 127, the expected peak, as a fraction of full-scale, is 0.00390625. If you set the Expected Peak property to 0.00390625 and the [Sample Width](pniusrp-samplewidth.html) property to **8-bit**, NI-USRP transfers the lower 8-bits of data across the bus, which preserves the full dynamic range of the signal. If you set the Expected Peak property to the default value (1.0), only the upper 8-bits are transferred across the bus, which results in a signal loss.

**Default Value**: 1.0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Expected Peak |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-exportedreferencefrequencyoutputterminal.html language=enus -->
## TOPIC 00045: Clocking and Synchronization:Exported Reference Frequency Output Terminal

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-exportedreferencefrequencyoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-exportedreferencefrequencyoutputterminal.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal of the exported reference frequency signal. Valid Values: None, RefOut Remarks The following table lists the characteristics of this property. Short Name Exported Reference Frequency Output Terminal Data type cstr.png Permissions Read/Write High-level VIs N/A Channel-ba

### Clocking and Synchronization:Exported Reference Frequency Output Terminal

Specifies the output terminal of the exported reference frequency signal.

**Valid Values**: None, RefOut

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Reference Frequency Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| None |  | Indicates the signal should not be exported. |
| --- | --- | --- |
| PpsTrigOut | PpsTrigOut | Exports the signal to the PPS TRIG OUT front panel terminal. |
| RefOut | RefOut | Exports the signal to the REF OUT front panel terminal. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-exportedtimebaseclockoutputterminal.html language=enus -->
## TOPIC 00046: Clocking and Synchronization:Exported Timebase Clock Output Terminal

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-exportedtimebaseclockoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-exportedtimebaseclockoutputterminal.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output terminal of the exported timebase clock (PPS) signal. Valid Values: None, PpsTrigOut Remarks The following table lists the characteristics of this property. Short Name Exported Timebase Clock Output Terminal Data type cstr.png Permissions Read/Write High-level VIs N/A Channel-ba

### Clocking and Synchronization:Exported Timebase Clock Output Terminal

Specifies the output terminal of the exported timebase clock (PPS) signal.

**Valid Values**: None, PpsTrigOut

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Timebase Clock Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| None |  | Indicates the signal should not be exported. |
| --- | --- | --- |
| PpsTrigOut | PpsTrigOut | Exports the signal to the PPS TRIG OUT front panel terminal. |
| RefOut | RefOut | Exports the signal to the REF OUT front panel terminal. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gain.html language=enus -->
## TOPIC 00047: Configuration:Gain

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gain.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the gain, in dB, applied to the RF signal for receive (Rx) and transmit (Tx) signals. Gain represents the total aggregate gain applied to the signal throughout the signal path. The USRP devices are not calibrated. The gain value does not represent an absolute gain and does not have linear

### Configuration:Gain

Specifies the gain, in dB, applied to the RF signal for receive (Rx) and transmit (Tx) signals.

Gain represents the total aggregate gain applied to the signal throughout the signal path.

Note

The range of available values is hardware dependent. If you specify a value outside the range supported by your device, NI-USRP coerces the value to the nearest supported value. Writing to this property specifies the value you want to use. Reading from this property returns the actual value, which may have been coerced to the capabilities of the device. NI recommends that you read the value after you write to this property to determine the actual setting for the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Gain |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niUSRP Configure Signal |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpslockstatus.html language=enus -->
## TOPIC 00048: Clocking and Synchronization:GPS Disciplined Clock:GPS Lock Status

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpslockstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpslockstatus.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if the GPS has a satellite fix. Remarks The following table lists the characteristics of this property. Short Name GPS Lock Status Data type cbool.png Permissions Read Only High-level VIs N/A Channel-based Yes Resettable No

### Clocking and Synchronization:GPS Disciplined Clock:GPS Lock Status

Returns True if the GPS has a satellite fix.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | GPS Lock Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpssentencegga.html language=enus -->
## TOPIC 00049: Clocking and Synchronization:GPS Disciplined Clock:GPS Sentence GGA

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpssentencegga.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpssentencegga.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the GPS fix data. Remarks The following table lists the characteristics of this property. Short Name GPS Sentence GGA Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based Yes Resettable No

### Clocking and Synchronization:GPS Disciplined Clock:GPS Sentence GGA

Returns the GPS fix data.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | GPS Sentence GGA |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpssentencermc.html language=enus -->
## TOPIC 00050: Clocking and Synchronization:GPS Disciplined Clock:GPS Sentence RMC

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpssentencermc.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpssentencermc.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended minimum specific GPS and transit data. Remarks The following table lists the characteristics of this property. Short Name GPS Sentence RMC Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based Yes Resettable No

### Clocking and Synchronization:GPS Disciplined Clock:GPS Sentence RMC

Returns the recommended minimum specific GPS and transit data.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | GPS Sentence RMC |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpstime.html language=enus -->
## TOPIC 00051: Clocking and Synchronization:GPS Disciplined Clock:GPS Time (seconds)

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpstime.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-gpstime.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the time that the GPS reports. Time is measured in seconds since 00:00:00 January 1, 1970 (UTC). Remarks The following table lists the characteristics of this property. Short Name GPS Time (seconds) Data type ci64.png Permissions Read Only High-level VIs N/A Channel-based Yes Resettable No

### Clocking and Synchronization:GPS Disciplined Clock:GPS Time (seconds)

Returns the time that the GPS reports. Time is measured in seconds since 00:00:00 January 1, 1970 (UTC).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | GPS Time (seconds) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-hasgpsdo.html language=enus -->
## TOPIC 00052: Clocking and Synchronization:GPS Disciplined Clock:Has GPS Disciplined Clock?

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-hasgpsdo.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-hasgpsdo.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns TRUE if the device has a GPS-disciplined clock. This property allows the device to use a GPS clock reference and GPS timestamps. Remarks The following table lists the characteristics of this property. Short Name Has GPS Disciplined Clock? Data type cbool.png Permissions Read Only High-level

### Clocking and Synchronization:GPS Disciplined Clock:Has GPS Disciplined Clock?

Returns TRUE if the device has a GPS-disciplined clock. This property allows the device to use a GPS clock reference and GPS timestamps.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Has GPS Disciplined Clock? |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-hostdatatype.html language=enus -->
## TOPIC 00053: Configuration:Advanced:Host Data Type

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-hostdatatype.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-hostdatatype.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data type to fetch from or write to the driver. Default Value: CDB Remarks The following table lists the characteristics of this property. Short Name Host Data Type Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes CDB 0 Write or fetch data as

### Configuration:Advanced:Host Data Type

Specifies the data type to fetch from or write to the driver.

**Default Value**: CDB

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Host Data Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| CDB | 0 | Write or fetch data as complex, double-precision floating-point (CDB) samples. |
| --- | --- | --- |
| I16 | 1 | Write or fetch data as signed 16-bit integer (I16) samples. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-iqrate.html language=enus -->
## TOPIC 00054: Configuration:IQ Rate

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-iqrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-iqrate.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sample rate of the baseband I/Q data for transmit (Tx) or receive (Rx) signals in samples per second (S/s). The range of available values is hardware dependent. If you specify a value outside the range supported by your device, NI-USRP coerces the value to the nearest supported value.

### Configuration:IQ Rate

Specifies the sample rate of the baseband I/Q data for transmit (Tx) or receive (Rx) signals in samples per second (S/s).

The range of available values is hardware dependent. If you specify a value outside the range supported by your device, NI-USRP coerces the value to the nearest supported value. Writing to this property specifies the value you want to use. Reading from this property returns the actual value, which may have been coerced to the capabilities of the device. NI recommends that you read the value after you write to this property to determine the actual setting for the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niUSRP Configure Signal |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-lodistribution.html language=enus -->
## TOPIC 00055: Clocking and Synchronization:Local Oscillator:LO Distribution

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-lodistribution.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-lodistribution.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LO distribution for the selected channel. Only supported for N321 Default Value: LO OUT0-3 Disabled Remarks The following table lists the characteristics of this property. Short Name LO Distribution Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettabl

### Clocking and Synchronization:Local Oscillator:LO Distribution

Specifies the LO distribution for the selected channel. Only supported for N321

**Default Value**: LO OUT0-3 Disabled

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Distribution |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| LO OUT0-3 Disabled | 0 | Disable LO distribution output 0-3. |
| --- | --- | --- |
| LO OUT0 Enabled | 1 | Enable LO distribution output 0. |
| LO OUT1 Enabled | 2 | Enable LO distribution output 1. |
| LO OUT2 Enabled | 4 | Enable LO distribution output 2. |
| LO OUT3 Enabled | 8 | Enable LO distribution output 3. |
| LO OUT0-3 Enabled | 15 | Enable LO distribution output 0-3. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loexportenabled.html language=enus -->
## TOPIC 00056: Clocking and Synchronization:Local Oscillator:LO Export Enabled

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loexportenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loexportenabled.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether or not to export the LO of the selected channel. Default Value: FALSE Remarks The following table lists the characteristics of this property. Short Name LO Export Enabled Data type cbool.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes

### Clocking and Synchronization:Local Oscillator:LO Export Enabled

Specifies whether or not to export the LO of the selected channel.

**Default Value**: FALSE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Export Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-lofrequency.html language=enus -->
## TOPIC 00057: Configuration:Advanced:LO Frequency

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-lofrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-lofrequency.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the local oscillator (LO) frequency, in Hz. The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP t

### Configuration:Advanced:LO Frequency

Specifies the local oscillator (LO) frequency, in Hz.

The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to automatically calculate the value for the LO frequency, or you can specify it with the LO Frequency property.

If you only specify a value for the [Carrier Frequency](pniusrp-carrierfrequency.html) property, NI-USRP sets the LO frequency as close to the carrier frequency as possible and implements the remainder of the frequency translation using digital signal processing. Any time the carrier frequency changes, NI-USRP adjusts the LO frequency. However, each time the LO frequency changes, NI-USRP must wait for the LO frequency to settle before it adjusts, which causes a delay.

When changing carrier frequencies within a narrow range, you can minimize retuning time by locking the LO frequency to one value using the LO Frequency property. In this case, changes to the carrier frequency do not affect the specified LO frequency, and NI-USRP only changes the digital signal processing frequency to account for the difference between the carrier frequency and LO frequency. To unlock the LO frequency and allow NI-USRP to automatically calculate it, set the LO Frequency property to -1. Specifying the LO frequency allows you to offset the LO from the carrier frequency, which avoids LO feedthrough that can distort your signal.

The range of available values is hardware dependent. If you specify a value outside the range supported by your device, NI-USRP coerces the value to the nearest supported value. Writing to this property specifies the value you want to use. Reading from this property returns the actual value, which may have been coerced to the capabilities of the device. NI recommends that you read the value after you write to this property to determine the actual setting for the device.

Note

*Carrier frequency* = *LO frequency* - *DSP frequency*

For example, if you want to sweep through a 25 MHz band starting at 2.4375 GHz, set the LO Frequency property to a value halfway through the band using the following equation:

2.4375 GHz + (25 MHz / 2) = 2.45 GHz.

When you set the LO Frequency property to 2.45 GHz, as the carrier frequency changes, NI-USRP only changes the DSP frequency as it sweeps through the bandwidth. The following figure illustrates how NI-USRP sets the frequency values on the first step of the sweep.

[IMAGE alt='image' src='LO-frequency.gif']

**Default Value**: -1

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-lofrequencycoerced.html language=enus -->
## TOPIC 00058: Configuration:Advanced:Coerced LO Frequency

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-lofrequencycoerced.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-lofrequencycoerced.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads back the coerced local oscillator (LO) frequency, in Hz. The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow

### Configuration:Advanced:Coerced LO Frequency

Reads back the coerced local oscillator (LO) frequency, in Hz.

The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to automatically calculate the value for the LO frequency, or you can specify it with the LO Frequency property.

If you only specify a value for the [Carrier Frequency](pniusrp-carrierfrequency.html) property, NI-USRP sets the LO frequency as close to the carrier frequency as possible and implements the remainder of the frequency translation using digital signal processing. Any time the carrier frequency changes, NI-USRP adjusts the LO frequency. However, each time the LO frequency changes, NI-USRP must wait for the LO frequency to settle before it adjusts, which causes a delay.

When changing carrier frequencies within a narrow range, you can minimize retuning time by locking the LO frequency to one value using the LO Frequency property. In this case, changes to the carrier frequency do not affect the specified LO frequency, and NI-USRP only changes the digital signal processing frequency to account for the difference between the carrier frequency and LO frequency. To unlock the LO frequency and allow NI-USRP to automatically calculate it, set the LO Frequency property to -1. Specifying the LO frequency allows you to offset the LO from the carrier frequency, which avoids LO feedthrough that can distort your signal.

The range of available values is hardware dependent. If you specify a value outside the range supported by your device, NI-USRP coerces the value to the nearest supported value. Writing to this property specifies the value you want to use. Reading from this property returns the actual value, which may have been coerced to the capabilities of the device. NI recommends that you read the value after you write to this property to determine the actual setting for the device.

Note

*Carrier frequency* = *LO frequency* - *DSP frequency*

For example, if you want to sweep through a 25 MHz band starting at 2.4375 GHz, set the LO Frequency property to a value halfway through the band using the following equation:

2.4375 GHz + (25 MHz / 2) = 2.45 GHz.

When you set the LO Frequency property to 2.45 GHz, as the carrier frequency changes, NI-USRP only changes the DSP frequency as it sweeps through the bandwidth. The following figure illustrates how NI-USRP sets the frequency values on the first step of the sweep.

[IMAGE alt='image' src='LO-frequency.gif']

**Default Value**: -1

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Coerced LO Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif1frequency.html language=enus -->
## TOPIC 00059: Clocking and Synchronization:Local Oscillator:LO IF1 Frequency

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif1frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif1frequency.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency, in Hz, of the IF1 LO. The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to autom

### Clocking and Synchronization:Local Oscillator:LO IF1 Frequency

Specifies the frequency, in Hz, of the IF1 LO.

The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to automatically calculate the value for the LO frequency, or you can specify it with the [LO Frequency](pniusrp-lofrequency.html) property. For the USRP-2945/2955 device, you can manually configure the separate LO stage frequencies by specifying both LO IF1 Frequency and LO IF2 Frequency to avoid the automatic tuning used in either [Carrier Frequency](pniusrp-carrierfrequency.html) or [LO Frequency](pniusrp-lofrequency.html) properties. When LO IF1 Frequency is configured, NI-USRP adjusts the DSP frequency translation to maintain the same overall carrier frequency if possible.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO IF1 Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif1frequencycoerced.html language=enus -->
## TOPIC 00060: Clocking and Synchronization:Local Oscillator:Coerced LO IF1 Frequency

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif1frequencycoerced.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif1frequencycoerced.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads back the frequency, in Hz, of the IF1 LO. The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to auto

### Clocking and Synchronization:Local Oscillator:Coerced LO IF1 Frequency

Reads back the frequency, in Hz, of the IF1 LO.

The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to automatically calculate the value for the LO frequency, or you can specify it with the [LO Frequency](pniusrp-lofrequency.html) property. For the USRP-2945/2955 device, you can manually configure the separate LO stage frequencies by specifying both LO IF1 Frequency and LO IF2 Frequency to avoid the automatic tuning used in either [Carrier Frequency](pniusrp-carrierfrequency.html) or [LO Frequency](pniusrp-lofrequency.html) properties. When LO IF1 Frequency is configured, NI-USRP adjusts the DSP frequency translation to maintain the same overall carrier frequency if possible.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Coerced LO IF1 Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif2frequency.html language=enus -->
## TOPIC 00061: Clocking and Synchronization:Local Oscillator:LO IF2 Frequency

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif2frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif2frequency.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency, in Hz, of the IF2 LO. The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to autom

### Clocking and Synchronization:Local Oscillator:LO IF2 Frequency

Specifies the frequency, in Hz, of the IF2 LO.

The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to automatically calculate the value for the LO frequency, or you can specify it with the [LO Frequency](pniusrp-lofrequency.html) property. For the USRP-2945/2955 device, you can manually configure the separate LO stage frequencies by specifying both LO IF1 Frequency and LO IF2 Frequency to avoid the automatic tuning used in either [Carrier Frequency](pniusrp-carrierfrequency.html) or [LO Frequency](pniusrp-lofrequency.html) properties. When LO IF2 Frequency is configured, NI-USRP adjusts the DSP frequency translation to maintain the same overall carrier frequency if possible.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO IF2 Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif2frequencycoerced.html language=enus -->
## TOPIC 00062: Clocking and Synchronization:Local Oscillator:Coerced LO IF2 Frequency

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif2frequencycoerced.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-loif2frequencycoerced.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads back the frequency, in Hz, of the IF2 LO. The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to auto

### Clocking and Synchronization:Local Oscillator:Coerced LO IF2 Frequency

Reads back the frequency, in Hz, of the IF2 LO.

The overall carrier frequency is realized in hardware as a combination of frequency translation in the local oscillator (LO) and an additional frequency translation implemented in the digital signal processing on the FPGA. You can allow NI-USRP to automatically calculate the value for the LO frequency, or you can specify it with the [LO Frequency](pniusrp-lofrequency.html) property. For the USRP-2945/2955 device, you can manually configure the separate LO stage frequencies by specifying both LO IF1 Frequency and LO IF2 Frequency to avoid the automatic tuning used in either [Carrier Frequency](pniusrp-carrierfrequency.html) or [LO Frequency](pniusrp-lofrequency.html) properties. When LO IF2 Frequency is configured, NI-USRP adjusts the DSP frequency translation to maintain the same overall carrier frequency if possible.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Coerced LO IF2 Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-losource.html language=enus -->
## TOPIC 00063: Clocking and Synchronization:Local Oscillator:LO Source

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-losource.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-losource.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LO source for the selected channel. Default Value: Internal Remarks The following table lists the characteristics of this property. Short Name LO Source Data type cstr.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Internal internal Uses internal channel

### Clocking and Synchronization:Local Oscillator:LO Source

Specifies the LO source for the selected channel.

**Default Value**: Internal

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Internal | internal | Uses internal channel LO source. |
| --- | --- | --- |
| Companion | companion | Uses internal LO source of the other channel on the shared daughterboard. |
| External/LO IN | external | Uses external LO source. |
| Reimport | reimport | Uses an LO source that originates internally, is exported, and is then imported through the external LO terminal. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-model.html language=enus -->
## TOPIC 00064: Meta Information:Instrument Identification:Model

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-model.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-model.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the model number or name of the device that you are currently using. Remarks The following table lists the characteristics of this property. Short Name Model Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based Yes Resettable No

### Meta Information:Instrument Identification:Model

Returns a string that contains the model number or name of the device that you are currently using.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Model |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-numberofchannelsinsession.html language=enus -->
## TOPIC 00065: Configuration:Number of Channels in Session

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-numberofchannelsinsession.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-numberofchannelsinsession.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of separate transmit (Tx) or receive (Rx) channels contained in the current driver session. Remarks The following table lists the characteristics of this property. Short Name Number of Channels in Session Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No

### Configuration:Number of Channels in Session

Returns the number of separate transmit (Tx) or receive (Rx) channels contained in the current driver session.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Channels in Session |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-numberofsamples.html language=enus -->
## TOPIC 00066: Configuration:Number of Samples

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-numberofsamples.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-numberofsamples.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the finite number of samples to acquire. This value is ignored if you set the Number of Samples is Finite property to FALSE. Remarks The following table lists the characteristics of this property. Short Name Number of Samples Data type ci64.png Permissions Read/Write High-level VIs niUSRP

### Configuration:Number of Samples

Specifies the finite number of samples to acquire. This value is ignored if you set the [Number of Samples is Finite](/csh?topicname=pniusrp-numberofsamplesisfinite.html) property to **FALSE**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Samples |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niUSRP Configure Number of Samples |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-numberofsamplesisfinite.html language=enus -->
## TOPIC 00067: Configuration:Number of Samples Is Finite

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-numberofsamplesisfinite.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-numberofsamplesisfinite.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device acquires a finite number of samples or acquires samples continuously. Default Value: FALSE Remarks The following table lists the characteristics of this property. Short Name Number of Samples Is Finite Data type cbool.png Permissions Read/Write High-level VIs niUSRP Conf

### Configuration:Number of Samples Is Finite

Specifies whether the device acquires a finite number of samples or acquires samples continuously.

**Default Value**: FALSE

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Samples Is Finite |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niUSRP Configure Number of Samples |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-oldestcompatiblefirmwareversion.html language=enus -->
## TOPIC 00068: Meta Information:Instrument Identification:Oldest Compatible Firmware Version

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-oldestcompatiblefirmwareversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-oldestcompatiblefirmwareversion.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the oldest compatible version of the firmware for the device you are currently using. Remarks The following table lists the characteristics of this property. Short Name Oldest Compatible Firmware Version Data type cstr.png Permissions Read Only High-level VIs N/A Channel-

### Meta Information:Instrument Identification:Oldest Compatible Firmware Version

Returns a string containing the oldest compatible version of the firmware for the device you are currently using.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Oldest Compatible Firmware Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-oldestcompatiblefpgaversion.html language=enus -->
## TOPIC 00069: Meta Information:Instrument Identification:Oldest Compatible FPGA Version

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-oldestcompatiblefpgaversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-oldestcompatiblefpgaversion.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the oldest compatible version of the FPGA image for the device you are currently using. Remarks The following table lists the characteristics of this property. Short Name Oldest Compatible FPGA Version Data type cstr.png Permissions Read Only High-level VIs N/A Channel-ba

### Meta Information:Instrument Identification:Oldest Compatible FPGA Version

Returns a string containing the oldest compatible version of the FPGA image for the device you are currently using.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Oldest Compatible FPGA Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-power.html language=enus -->
## TOPIC 00070: Configuration:Power Reference

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-power.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-power.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power, in dBm, of a full-scale RF signal for receive (Rx) and transmit (Tx) signals. Power represents the total power at the output/input of the USRP. For Rx, power reference represents the power that would measured at the input RF port if the digital baseband were full-scale. For Tx,

### Configuration:Power Reference

Specifies the power, in dBm, of a full-scale RF signal for receive (Rx) and transmit (Tx) signals.

Power represents the total power at the output/input of the USRP.

For Rx, power reference represents the power that would measured at the input RF port if the digital baseband were full-scale. For Tx, power reference represents the power that would be output at the RF port if the digital baseband data were full-scale.

Note

The range of available values is hardware dependent. If you specify a value outside the range supported by your device, NI-USRP coerces the value to the nearest supported value. Writing to this property specifies the value you want to use. Reading from this property returns the actual value, which may have been coerced to the capabilities of the device. NI recommends that you read the value after you write to this property to determine the actual setting for the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Power Reference |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-referencefrequencysource.html language=enus -->
## TOPIC 00071: Clocking and Synchronization:Reference Frequency Source

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-referencefrequencysource.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-referencefrequencysource.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the signal used as a frequency reference for the local oscillator (LO). Valid Values: Internal, RefIn, Mimo, GPS Default Value: Internal Remarks The following table lists the characteristics of this property. Short Name Reference Frequency Source Data type cstr.png Permission

### Clocking and Synchronization:Reference Frequency Source

Specifies the source of the signal used as a frequency reference for the local oscillator (LO).

**Valid Values**: Internal, RefIn, Mimo, GPS

**Default Value**: Internal

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference Frequency Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Internal | Internal | Specifies the onboard reference signal as the source for the frequency reference signal. |
| --- | --- | --- |
| RefIn | RefIn | Specifies the reference signal received from the REF IN connector on the device front panel as the source for the frequency reference signal. |
| Mimo | Mimo | Specifies the reference signal received from the MIMO EXPANSION connector on the device front panel as the source for the frequency reference signal. |
| GPS | GPS | Specifies the reference signal received from the GPS. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-samplewidth.html language=enus -->
## TOPIC 00072: Configuration:Advanced:Sample Width

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-samplewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-samplewidth.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width, in bits, of the binary data sample transferred across the bus between the host and the device. Default Value: 16-bit Remarks The following table lists the characteristics of this property. Short Name Sample Width Data type ci32.png Permissions Read/Write High-level VIs N/A Chann

### Configuration:Advanced:Sample Width

Specifies the width, in bits, of the binary data sample transferred across the bus between the host and the device.

**Default Value**: 16-bit

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| 16-bit | 16 | Each component of each complex sample uses 16 bits, for a total of 32 bits per sample. |
| --- | --- | --- |
| 8-bit | 8 | Each component of each complex sample uses 8 bits, for a total of 16 bits per sample. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-starttriggertimefractional.html language=enus -->
## TOPIC 00073: Clocking and Synchronization:Start Trigger Time (fractional seconds)

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-starttriggertimefractional.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-starttriggertimefractional.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the fractional seconds part of the trigger start time. Remarks The following table lists the characteristics of this property. Short Name Start Trigger Time (fractional seconds) Data type cdbl.png Permissions Read/Write High-level VIs niUSRP Configure Trigger Channel-based No Resettable Ye

### Clocking and Synchronization:Start Trigger Time (fractional seconds)

Specifies the fractional seconds part of the trigger start time.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Time (fractional seconds) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niUSRP Configure Trigger |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-starttriggertimefull.html language=enus -->
## TOPIC 00074: Clocking and Synchronization:Start Trigger Time (whole seconds)

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-starttriggertimefull.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-starttriggertimefull.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the whole seconds part of the trigger start time. Remarks The following table lists the characteristics of this property. Short Name Start Trigger Time (whole seconds) Data type ci64.png Permissions Read/Write High-level VIs niUSRP Configure Trigger Channel-based No Resettable Yes

### Clocking and Synchronization:Start Trigger Time (whole seconds)

Specifies the whole seconds part of the trigger start time.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Time (whole seconds) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niUSRP Configure Trigger |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-starttriggertype.html language=enus -->
## TOPIC 00075: Clocking and Synchronization:Start Trigger Type

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-starttriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-starttriggertype.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of start trigger, which controls how the device generates or acquires signals. Use this property to choose whether to generate or acquire data immediately or to synchronize generations and acquisitions to the timestamp specified by the Start Trigger Time properties. Default Value:

### Clocking and Synchronization:Start Trigger Type

Specifies the type of start trigger, which controls how the device generates or acquires signals. Use this property to choose whether to generate or acquire data immediately or to synchronize generations and acquisitions to the timestamp specified by the Start Trigger Time properties.

**Default Value**: None

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niUSRP Configure Trigger |
| Channel-based | No |
| Resettable | Yes |

| None | 0 | For Rx, acquires data immediately (as soon as the acquisition starts). For Tx, generates data as soon as it writes to the device. |
| --- | --- | --- |
| Time | 1 | Acquires or generates data synchronous to a timestamp. The Start Trigger occurs when the onboard device timer reaches the timestamp specified by the Start Trigger Time properties. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-timebaseclockpolarity.html language=enus -->
## TOPIC 00076: Clocking and Synchronization:Timebase Clock Polarity

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-timebaseclockpolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-timebaseclockpolarity.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the signal used as the timebase clock if you set the Start Trigger Type property to Time. Default Value: Rising Remarks The following table lists the characteristics of this property. Short Name Timebase Clock Polarity Data type ci32.png Permissions Read/Write High-level VI

### Clocking and Synchronization:Timebase Clock Polarity

Specifies the polarity of the signal used as the timebase clock if you set the [Start Trigger Type](/csh?topicname=pniusrp-starttriggertype.html) property to **Time**.

**Default Value**: Rising

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Timebase Clock Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Rising | 0 | Data latches on the clock rising edge. |
| --- | --- | --- |
| Falling | 1 | Data latches on the clock falling edge. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-timebaseclocksource.html language=enus -->
## TOPIC 00077: Clocking and Synchronization:Timebase Clock Source

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-timebaseclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-timebaseclocksource.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the signal used as the timebase clock if you set the Start Trigger Type property to Time. Valid Values: Internal, PpsIn, Mimo, GPS Default Value: Internal Remarks The following table lists the characteristics of this property. Short Name Timebase Clock Source Data type cstr.p

### Clocking and Synchronization:Timebase Clock Source

Specifies the source of the signal used as the timebase clock if you set the [Start Trigger Type](/csh?topicname=pniusrp-starttriggertype.html) property to **Time**.

**Valid Values**: Internal, PpsIn, Mimo, GPS

**Default Value**: Internal

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Timebase Clock Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Internal | Internal | Specifies the onboard device timer as the source for the timebase clock. |
| --- | --- | --- |
| PpsIn | PpsIn | Specifies the signal received from the PPS IN connector on the device front panel as the source for the timebase clock. |
| Mimo | Mimo | Specifies the signal received from the MIMO EXPANSION connector on the device front panel as the source for the timebase clock. |
| GPS | GPS | Specifies the reference signal received from the GPS. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-trigiomode.html language=enus -->
## TOPIC 00078: Configuration:Trig I/O Mode

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-trigiomode.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-trigiomode.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mode of the Trig In/Out terminal. Valid Values: Input, Output, Off Default Value: Off Remarks The following table lists the characteristics of this property. Short Name Trig I/O Mode Data type cstr.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes Input Inpu

### Configuration:Trig I/O Mode

Specifies the mode of the Trig In/Out terminal.

**Valid Values**: Input, Output, Off

**Default Value**: Off

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trig I/O Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Input | Input | Sets the Trig In/Out terminal to input. |
| --- | --- | --- |
| Output | Output | Sets the Trig In/Out terminal to output. |
| Off | Off | Turns off the Trig In/Out terminal. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-warningpolicy.html language=enus -->
## TOPIC 00079: Configuration:Advanced:Warning Policy

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-warningpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rc/niusrp/pniusrp-warningpolicy.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether NI-USRP returns an error, returns a warning, or ignores overflow, underflow, or timeout conditions during data transfer. Default Value: Return Errors Remarks The following table lists the characteristics of this property. Short Name Warning Policy Data type ci32.png Permissions Rea

### Configuration:Advanced:Warning Policy

Specifies whether NI-USRP returns an error, returns a warning, or ignores overflow, underflow, or timeout conditions during data transfer.

**Default Value**: Return Errors

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Warning Policy |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Return Warnings | 0 | Returns a warning when an overflow, underflow, or timeout condition occurs during a data transfer. |
| --- | --- | --- |
| Return Errors | 1 | Returns an error when an overflow, underflow, or timeout condition occurs during a data transfer. |
| Return Success | 2 | Ignores overflow, underflow, or timeout conditions during a data transfer. |

Parent topic:

niUSRP Properties

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-reset-vi.html language=enus -->
## TOPIC 00080: niUSRP Reset VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-reset-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-reset-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the device to a known initialization state. This VI aborts any existing acquisitions or generations and restores the device properties to their default states. icon Inputs/Outputs civrn.png session handle session handle identifies your instrument session. session handle is obtained from the n

### niUSRP Reset VI

Resets the device to a known initialization state. This VI aborts any existing acquisitions or generations and restores the device properties to their default states.

[IMAGE alt='icon' src='niusrp-reset-vi.png']

#### Inputs/Outputs

| session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-run-adc-self-calibration-vi.html language=enus -->
## TOPIC 00081: niUSRP Run ADC Self Calibration VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-run-adc-self-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-run-adc-self-calibration-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a receive (Rx) session to the device(s) you specify in the device names input and returns session handle out, which you use to identify this instrument session in all subsequent NI-USRP VIs. Supported Devices: Ettus USRP X410/X440 icon Inputs/Outputs civrn.png session handle session handle ide

### niUSRP Run ADC Self Calibration VI

Opens a receive (Rx) session to the device(s) you specify in the **device names** input and returns **session handle out**, which you use to identify this instrument session in all subsequent NI-USRP VIs.

**Supported Devices**: Ettus USRP X410/X440

[IMAGE alt='icon' src='niusrp-run-adc-self-calibration-vi.png']

#### Inputs/Outputs

| session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. channels — channels indicates channels on which to run the operation. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from this VI and identifies this receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-rx-mnu.html language=enus -->
## TOPIC 00082: Rx

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-rx-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-rx-mnu.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the niUSRP Rx VIs to develop receiver (Rx) applications for USRP devices. icon

### Rx

Use the niUSRP Rx VIs to develop receiver (Rx) applications for USRP devices.

[IMAGE alt='icon' src='niusrp-rx-mnu.png']

- [niUSRP Open Rx Session VI](../../instr-lib/niusrp/niusrp-open-rx-session-vi.html) Opens a receive (Rx) session to the device(s) you specify in the device names input and returns session handle out , which you use to identify this instrument session in all subsequent NI-USRP VIs.
- [niUSRP Open Rx Session with Custom Bitfile VI](../../instr-lib/niusrp/niusrp-open-rx-session-with-custom-bitfile-vi.html) Opens a receive (Rx) session with a custom bitfile.
- [niUSRP Configure Number of Samples VI](../../instr-lib/niusrp/niusrp-configure-number-of-samples-vi.html) Specifies whether the device operation is finite or continuous and the number of samples to acquire.
- [niUSRP Configure Signal VI](../../instr-lib/niusrp/niusrp-configure-signal-vi.html) Configures properties of the transmit (Tx) or receive (Rx) signal.
- [niUSRP Initiate VI](../../instr-lib/niusrp/niusrp-initiate-vi.html) Starts the Rx acquisition.
- [niUSRP Fetch Rx Data (poly) VI](../../instr-lib/niusrp/niusrp-fetch-rx-data-poly-vi.html) Fetches data from the specified channel list.
- [niUSRP Abort VI](../../instr-lib/niusrp/niusrp-abort-vi.html) Stops an acquisition previously started.
- [niUSRP Close Session VI](../../instr-lib/niusrp/niusrp-close-session-vi.html) Closes the session handle to the device.

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-self-test-vi.html language=enus -->
## TOPIC 00083: niUSRP Self Test VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-self-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-self-test-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a self-test of the device. icon Inputs/Outputs civrn.png session handle session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. cerrco

### niUSRP Self Test VI

Performs a self-test of the device.

[IMAGE alt='icon' src='niusrp-self-test-vi.png']

#### Inputs/Outputs

| session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. test result — test result returns the result of the self-test. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-set-command-time-vi.html language=enus -->
## TOPIC 00084: niUSRP Set Command Time VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-set-command-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-set-command-time-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Tells the device to execute the next hardware configuration setting at the specified timestamp. This should only be used after niUSRP Initiate VI is called on the session. icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) on which to set the configuration civrn.png sess

### niUSRP Set Command Time VI

Tells the device to execute the next hardware configuration setting at the specified timestamp. This should only be used after niUSRP Initiate VI is called on the session.

[IMAGE alt='icon' src='niusrp-set-command-time-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) on which to set the configuration session handle — session handle identifies your instrument session. command time — command time specifies the time at which the next command will activate in seconds, interpreted as whole seconds.fractional seconds. whole seconds — whole seconds is the integer number of seconds for the time of the start trigger, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision floating-point value representing the remaining fraction of a second for the time of the start trigger, according to the onboard device timer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| whole seconds — whole seconds is the integer number of seconds for the time of the start trigger, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision floating-point value representing the remaining fraction of a second for the time of the start trigger, according to the onboard device timer. |

Parent topic:

Synchronization

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-set-time-vi.html language=enus -->
## TOPIC 00085: niUSRP Set Time VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-set-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-set-time-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time value of the onboard device timer. icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) on which to set the time. civrn.png session handle session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the

### niUSRP Set Time VI

Sets the time value of the onboard device timer.

[IMAGE alt='icon' src='niusrp-set-time-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) on which to set the time. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. apply timestamp — apply timestamp specifies when to apply the timestamp to the onboard device timer. The default value is now. now (0) Sets the onboard device timer to the specified timestamp immediately. next timebase edge (1) Sets the onboard device timer to the specified timestamp at the next edge of the timebase clock. timestamp — timestamp specifies the time to set on the onboard device timer. whole seconds — whole seconds is the integer number of seconds for the time to set on the onboard device timer. fractional seconds — fractional seconds is the double-precision floating-point value representing the remaining fraction of a second for the time to set on the onboard device timer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| now (0) | Sets the onboard device timer to the specified timestamp immediately. |
| next timebase edge (1) | Sets the onboard device timer to the specified timestamp at the next edge of the timebase clock. |
| whole seconds — whole seconds is the integer number of seconds for the time to set on the onboard device timer. fractional seconds — fractional seconds is the double-precision floating-point value representing the remaining fraction of a second for the time to set on the onboard device timer. |  |

Parent topic:

Synchronization

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-sync-mnu.html language=enus -->
## TOPIC 00086: Synchronization

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-sync-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-sync-mnu.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the niUSRP Synchronization VIs to synchronize timing in applications for USRP devices. icon

### Synchronization

Use the niUSRP Synchronization VIs to synchronize timing in applications for USRP devices.

[IMAGE alt='icon' src='niusrp-sync-mnu.png']

- [niUSRP Configure Trigger VI](../../instr-lib/niusrp/niusrp-configure-trigger-vi.html) Configures the trigger generated by the onboard device timer. The trigger specifies the time to acquire or generate the first sample.
- [niUSRP Set Time VI](../../instr-lib/niusrp/niusrp-set-time-vi.html) Sets the time value of the onboard device timer.
- [niUSRP Disable Start Trigger VI](../../instr-lib/niusrp/niusrp-disable-start-trigger-vi.html) Disables the Start Trigger. When the Start Trigger is disabled, acquisitions and generations begin immediately when data is available.
- [niUSRP Get Time VI](../../instr-lib/niusrp/niusrp-get-time-vi.html) Returns the time value of the onboard device timer.
- [niUSRP Wait For Lock VI](../../instr-lib/niusrp/niusrp-wait-for-lock-vi.html) Configures the device to wait for the GPS to lock. GPSDO may take up to 10 minutes to lock to a satellite the first time.
- [niUSRP Export Signal VI](../../instr-lib/niusrp/niusrp-export-signal-vi.html) Creates a route to export the specified signal to the specified output terminal. Valid mapping is one-to-one such that Reference Frequency maps to REF OUT, Timebase Clock maps to PPS TRIG OUT, and LO maps to LO OUT.
- [niUSRP Set Command Time VI](../../instr-lib/niusrp/niusrp-set-command-time-vi.html) Tells the device to execute the next hardware configuration setting at the specified timestamp. This should only be used after niUSRP Initiate VI is called on the session.
- [niUSRP Clear Command Time VI](../../instr-lib/niusrp/niusrp-clear-command-time-vi.html) Clears command times, causing future control commands to take effect immediately. Previous control commands will still occur at their associated command times.

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-tx-mnu.html language=enus -->
## TOPIC 00087: Tx

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-tx-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-tx-mnu.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the niUSRP Tx VIs to develop transmitter (Tx) applications for USRP devices. icon

### Tx

Use the niUSRP Tx VIs to develop transmitter (Tx) applications for USRP devices.

[IMAGE alt='icon' src='niusrp-tx-mnu.png']

- [niUSRP Open Tx Session VI](../../instr-lib/niusrp/niusrp-open-tx-session-vi.html) Opens a transmit (Tx) session to the device(s) you specify in the device names input and returns session handle out , which you use to identify this instrument session in all subsequent NI-USRP VIs.
- [niUSRP Open Tx Session with Custom Bitfile VI](../../instr-lib/niusrp/niusrp-open-tx-session-with-custom-bitfile-vi.html) Opens a transmit (Tx) session with a custom bitfile.
- [niUSRP Configure Signal VI](../../instr-lib/niusrp/niusrp-configure-signal-vi.html) Configures properties of the transmit (Tx) or receive (Rx) signal.
- [niUSRP Write Tx Data (poly) VI](../../instr-lib/niusrp/niusrp-write-tx-data-poly-vi.html) Writes data to the specified channel list.
- [niUSRP Close Session VI](../../instr-lib/niusrp/niusrp-close-session-vi.html) Closes the session handle to the device.

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-usrp-timestamp-to-lv-timestamp-vi.html language=enus -->
## TOPIC 00088: niUSRP USRP Timestamp to LV Timestamp VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-usrp-timestamp-to-lv-timestamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-usrp-timestamp-to-lv-timestamp-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a USRP timestamp to a LabVIEW timestamp. icon Inputs/Outputs cnclst.png USRP Timestamp USRP timestamp is a timestamp in the format used by USRP. USRP timestamp is the time of the clock in seconds, interpreted as whole seconds.fractional seconds. cu64.png whole seconds whole seconds is the i

### niUSRP USRP Timestamp to LV Timestamp VI

Converts a USRP timestamp to a LabVIEW timestamp.

[IMAGE alt='icon' src='niusrp-usrp-timestamp-to-lv-timestamp-vi.png']

#### Inputs/Outputs

| USRP Timestamp — USRP timestamp is a timestamp in the format used by USRP. USRP timestamp is the time of the clock in seconds, interpreted as whole seconds.fractional seconds. whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. — LV Timestamp is a timestamp in the format used by LabVIEW. The timestamp is displayed in hours, minutes, seconds, and milliseconds, as well as the month, day, and year. — error out contains error information. This output provides standard error out functionality. |
| --- |
| whole seconds — whole seconds is the integer number of seconds for the time associated with the first sample of the waveform, according to the onboard device timer. fractional seconds — fractional seconds is the double-precision, floating-point value representing the remaining fraction of a second for the time associated with the first sample of the waveform, according to the onboard device timer. |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-utilities-mnu.html language=enus -->
## TOPIC 00089: Utility

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-utilities-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-utilities-mnu.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the niUSRP Utility VIs to access utility features of NI-USRP. icon

### Utility

Use the niUSRP Utility VIs to access utility features of NI-USRP.

[IMAGE alt='icon' src='niusrp-utilities-mnu.png']

- [niUSRP Commit VI](../../instr-lib/niusrp/niusrp-commit-vi.html) Validates any changed properties and commits the settings to the device.
- [niUSRP Reset VI](../../instr-lib/niusrp/niusrp-reset-vi.html) Resets the device to a known initialization state. This VI aborts any existing acquisitions or generations and restores the device properties to their default states.
- [niUSRP Self Test VI](../../instr-lib/niusrp/niusrp-self-test-vi.html) Performs a self-test of the device.
- [niUSRP Get Error VI](../../instr-lib/niusrp/niusrp-get-error-vi.html) Returns the error code and description for the last error that occurred.
- [niUSRP Clear Error VI](../../instr-lib/niusrp/niusrp-clear-error-vi.html) Clears the last error code.
- [niUSRP Find Devices VI](../../instr-lib/niusrp/niusrp-find-devices-vi.html) Returns a list of USRP devices discovered in the system.
- [niUSRP LV Timestamp to USRP Timestamp VI](../../instr-lib/niusrp/niusrp-lv-timestamp-to-usrp-timestamp-vi.html) Translates a LabVIEW timestamp to a USRP timestamp.
- [niUSRP USRP Timestamp to LV Timestamp VI](../../instr-lib/niusrp/niusrp-usrp-timestamp-to-lv-timestamp-vi.html) Converts a USRP timestamp to a LabVIEW timestamp.
- [niUSRP Run ADC Self Calibration VI](../../instr-lib/niusrp/niusrp-run-adc-self-calibration-vi.html) Opens a receive (Rx) session to the device(s) you specify in the device names input and returns session handle out , which you use to identify this instrument session in all subsequent NI-USRP VIs.
- [niUSRP Convert From Gain To Power VI](../../instr-lib/niusrp/niusrp-convert-from-gain-to-power-vi.html) Converts a dB gain value to an approximate dBm power level.
- [niUSRP Convert From Power To Gain VI](../../instr-lib/niusrp/niusrp-convert-from-power-to-gain-vi.html) Converts an approximate dBm power level to a dB gain value.
- [niUSRP Get Power Range VI](../../instr-lib/niusrp/niusrp-get-power-range-vi.html) Gets the approximate minimum and maximum dBm power levels for a given frequency.
- [niUSRP Configure GPIO Pins VI](../../instr-lib/niusrp/niusrp-configure-gpio-pins-vi.html) Configures the X410 GPIO signal properties such as direction (I/O), voltage level, and master for multiple pins on a selected 'bank' and a 12-bit binary 'mask' to indicate which pins to configure. Please see the GPIO API for more help, https://files.ettus.com/manual/page_x400_gpio_api.html

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-wait-for-lock-vi.html language=enus -->
## TOPIC 00090: niUSRP Wait For Lock VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-wait-for-lock-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-wait-for-lock-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the GPS to lock. GPSDO may take up to 10 minutes to lock to a satellite the first time. icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) to configure. civrn.png session handle session handle identifies your instrument session. session

### niUSRP Wait For Lock VI

Configures the device to wait for the GPS to lock. GPSDO may take up to 10 minutes to lock to a satellite the first time.

[IMAGE alt='icon' src='niusrp-wait-for-lock-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) to configure. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. device — device specifies the lock signal to wait for. Leave device set to the default value, GPS. timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been generated. A negative value indicates to the driver to wait indefinitely. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI or the niUSRP Open Rx Session VI and identifies a particular transmit (Tx) or receive (Rx) session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Synchronization

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-write-tx-data-2d-cdb-vi.html language=enus -->
## TOPIC 00091: niUSRP Write Tx Data (2D CDB) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-write-tx-data-2d-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-write-tx-data-2d-cdb-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex, double-precision floating-point data to the specified channels. icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) to which to write the data. civrn.png session handle session handle identifies your instrument session. session handle is obtained from the

### niUSRP Write Tx Data (2D CDB) VI

Writes complex, double-precision floating-point data to the specified channels.

[IMAGE alt='icon' src='niusrp-write-tx-data-2d-cdb-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) to which to write the data. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI and identifies a particular transmit (Tx) session. data — data specifies the baseband samples to transmit as an array of complex, double-precision floating-point data. The real and imaginary components of the data correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. Each row of the 2D array corresponds to a separate channel. The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of the Configure Signal VI. data accepts complex, double-precision floating-point values whose real and imaginary components range from 1.0 to -1.0. Maintain the maximum complex magnitude to a value less than 1.0 to prevent DSP overflow. Because the DSP frequency response varies over frequency and over I/Q rates, some tones with a complex magnitude less than but close to 1 may cause DSP overflow. Consider reducing the amplitude if you observe unexpected spurs in the spectrum of your generated signal. Use the following equation to determine the complex magnitude of the signal: timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been generated. A negative value indicates to the driver to wait indefinitely. end of data? — end of data? specifies whether this is the last call to the niUSRP Write Tx Data VI for the current contiguous transmit operation. The default value is FALSE. TRUE Specifies that data contains the end of the data transmission. The transmission aborts when the last data sample generates. FALSE Specifies that you will provide more data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI and identifies a particular transmit (Tx) session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE | Specifies that data contains the end of the data transmission. The transmission aborts when the last data sample generates. |
| FALSE | Specifies that you will provide more data. |

Parent topic:

niUSRP Write Tx Data (poly) VI

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-write-tx-data-2d-i16-vi.html language=enus -->
## TOPIC 00092: niUSRP Write Tx Data (2D I16) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-write-tx-data-2d-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-write-tx-data-2d-i16-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex, 16-bit signed integer data to the specified channels. To use the niUSRP Write Tx Data (2D I16) VI, you must set the Host Data Type property to I16. data accepts binary values that range from 32,767 to -32,768. The corresponding floating-point values range from 1.0 to ‑1.0. Use the fo

### niUSRP Write Tx Data (2D I16) VI

Writes complex, 16-bit signed integer data to the specified channels. To use the niUSRP Write Tx Data (2D I16) VI, you must set the [Host Data Type](/csh?context=niusrp_usrppropref_pniusrp_hostdatatype) property to I16.

**data** accepts binary values that range from 32,767 to -32,768. The corresponding floating-point values range from 1.0 to ‑1.0. Use the following equations to convert values from binary to floating-point or from floating-point to binary:

*floating-point value* = *binary value*/32,768

*binary value* = *floating-point value* x 32,767

[IMAGE alt='icon' src='niusrp-write-tx-data-2d-i16-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) to which to write the data. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI and identifies a particular transmit (Tx) session. data — data specifies the baseband samples to transmit as an array of complex, 16-bit signed integer data. The real and imaginary components of the data correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. I and Q are interleaved [I, Q, I, Q, ...] in the array. Each row of the 2D array corresponds to a separate channel. The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of the Configure Signal VI. data accepts signed, 16-bit integer values that range from 32,767 to -32,768. The maximum complex magnitude is 32,767. However, because the DSP frequency response varies over frequency and over I/Q rates, some tones with a complex magnitude less than but close to 32,767 may cause DSP overflow. Consider reducing the amplitude if you observe unexpected spurs in the spectrum of your generated signal. Use the following equation to determine the complex magnitude of the signal: timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been generated. A negative value indicates to the driver to wait indefinitely. end of data? — end of data? specifies whether this is the last call to the niUSRP Write Tx Data VI for the current contiguous transmit operation. The default value is FALSE. TRUE Specifies that data contains the end of the data transmission. The transmission aborts when the last data sample generates. FALSE Specifies that you will provide more data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI and identifies a particular transmit (Tx) session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE | Specifies that data contains the end of the data transmission. The transmission aborts when the last data sample generates. |
| FALSE | Specifies that you will provide more data. |

Parent topic:

niUSRP Write Tx Data (poly) VI

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-write-tx-data-cdb-cluster-vi.html language=enus -->
## TOPIC 00093: niUSRP Write Tx Data (CDB Cluster) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-write-tx-data-cdb-cluster-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-write-tx-data-cdb-cluster-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a cluster of complex, double-precision floating-point data to the specified channel. Modulation Toolkit VIs use the complex, double-precision floating-point cluster data type. Use this VI in applications that use Modulation Toolkit VIs. icon Inputs/Outputs cstr.png channel list channel list s

### niUSRP Write Tx Data (CDB Cluster) VI

Writes a cluster of complex, double-precision floating-point data to the specified channel. Modulation Toolkit VIs use the complex, double-precision floating-point cluster data type. Use this VI in applications that use Modulation Toolkit VIs.

[IMAGE alt='icon' src='niusrp-write-tx-data-cdb-cluster-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) to which to write the data. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI and identifies a particular transmit (Tx) session. — data specifies the baseband samples to transmit as complex, double-precision floating-point data in a cluster, which also includes sampling information. data accepts complex, double-precision floating-point values whose real and imaginary components range from 1.0 to -1.0. Maintain the maximum complex magnitude to a value less than 1.0 to prevent DSP overflow. Because the DSP frequency response varies over frequency and over I/Q rates, some tones with a complex magnitude less than but close to 1 may cause DSP overflow. Consider reducing the amplitude if you observe unexpected spurs in the spectrum of your generated signal. Use the following equation to determine the complex magnitude of the signal: t0 — t0 NI-USRP ignores this value. dt — dt specifies the time between values in the Y array. Y — Y specifies the complex-valued baseband waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been generated. A negative value indicates to the driver to wait indefinitely. end of data? — end of data? specifies whether this is the last call to the niUSRP Write Tx Data VI for the current contiguous transmit operation. The default value is FALSE. TRUE Specifies that data contains the end of the data transmission. The transmission aborts when the last data sample generates. FALSE Specifies that you will provide more data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. use waveform dt for IQ rate? — use waveform dt for IQ rate? specifies whether the dt element of the data waveform overrides the I/Q rate. The default value is FALSE. TRUE Specifies that the waveform dt overrides the I/Q rate. FALSE Specifies that the waveform dt does not override the I/Q rate. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI and identifies a particular transmit (Tx) session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| t0 — t0 NI-USRP ignores this value. dt — dt specifies the time between values in the Y array. Y — Y specifies the complex-valued baseband waveform. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |  |
| TRUE | Specifies that data contains the end of the data transmission. The transmission aborts when the last data sample generates. |
| FALSE | Specifies that you will provide more data. |
| TRUE | Specifies that the waveform dt overrides the I/Q rate. |
| FALSE | Specifies that the waveform dt does not override the I/Q rate. |

Parent topic:

niUSRP Write Tx Data (poly) VI

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-write-tx-data-cdb-vi.html language=enus -->
## TOPIC 00094: niUSRP Write Tx Data (CDB) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-write-tx-data-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-write-tx-data-cdb-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex, double-precision floating-point data to the specified channel. icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) to which to write the data. civrn.png session handle session handle identifies your instrument session. session handle is obtained from the n

### niUSRP Write Tx Data (CDB) VI

Writes complex, double-precision floating-point data to the specified channel.

[IMAGE alt='icon' src='niusrp-write-tx-data-cdb-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) to which to write the data. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI and identifies a particular transmit (Tx) session. data — data specifies the baseband samples to transmit as an array of complex, double-precision floating-point data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of the Configure Signal VI. data accepts complex, double-precision floating-point values whose real and imaginary components range from 1.0 to -1.0. Maintain the maximum complex magnitude to a value less than 1.0 to prevent DSP overflow. Because the DSP frequency response varies over frequency and over I/Q rates, some tones with a complex magnitude less than but close to 1 may cause DSP overflow. Consider reducing the amplitude if you observe unexpected spurs in the spectrum of your generated signal. Use the following equation to determine the complex magnitude of the signal: timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been generated. A negative value indicates to the driver to wait indefinitely. end of data? — end of data? specifies whether this is the last call to the niUSRP Write Tx Data VI for the current contiguous transmit operation. The default value is FALSE. TRUE Specifies that data contains the end of the data transmission. The transmission aborts when the last data sample generates. FALSE Specifies that you will provide more data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI and identifies a particular transmit (Tx) session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE | Specifies that data contains the end of the data transmission. The transmission aborts when the last data sample generates. |
| FALSE | Specifies that you will provide more data. |

Parent topic:

niUSRP Write Tx Data (poly) VI

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-write-tx-data-cdb-wdt-vi.html language=enus -->
## TOPIC 00095: niUSRP Write Tx Data (CDB WDT) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-write-tx-data-cdb-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-write-tx-data-cdb-wdt-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex, double-precision floating-point data in a waveform data type to the specified channel. icon Inputs/Outputs cstr.png channel list channel list specifies the channel(s) to which to write the data. civrn.png session handle session handle identifies your instrument session. session handl

### niUSRP Write Tx Data (CDB WDT) VI

Writes complex, double-precision floating-point data in a waveform data type to the specified channel.

[IMAGE alt='icon' src='niusrp-write-tx-data-cdb-wdt-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) to which to write the data. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI and identifies a particular transmit (Tx) session. data — data specifies the baseband samples to transmit as complex, double-precision floating-point data in a waveform data type, which also includes sampling information. data accepts complex, double-precision floating-point values whose real and imaginary components range from 1.0 to -1.0. Maintain the maximum complex magnitude to a value less than 1.0 to prevent DSP overflow. Because the DSP frequency response varies over frequency and over I/Q rates, some tones with a complex magnitude less than but close to 1 may cause DSP overflow. Consider reducing the amplitude if you observe unexpected spurs in the spectrum of your generated signal. Use the following equation to determine the complex magnitude of the signal: timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been generated. A negative value indicates to the driver to wait indefinitely. end of data? — end of data? specifies whether this is the last call to the niUSRP Write Tx Data VI for the current contiguous transmit operation. The default value is FALSE. TRUE Specifies that data contains the end of the data transmission. The transmission aborts when the last data sample generates. FALSE Specifies that you will provide more data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. use waveform dt for IQ rate? — use waveform dt for IQ rate? specifies whether the dt element of the data waveform overrides the I/Q rate. The default value is FALSE. TRUE Specifies that the waveform dt overrides the I/Q rate. FALSE Specifies that the waveform dt does not override the I/Q rate. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI and identifies a particular transmit (Tx) session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE | Specifies that data contains the end of the data transmission. The transmission aborts when the last data sample generates. |
| FALSE | Specifies that you will provide more data. |
| TRUE | Specifies that the waveform dt overrides the I/Q rate. |
| FALSE | Specifies that the waveform dt does not override the I/Q rate. |

Parent topic:

niUSRP Write Tx Data (poly) VI

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-write-tx-data-i16-vi.html language=enus -->
## TOPIC 00096: niUSRP Write Tx Data (I16) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-write-tx-data-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-write-tx-data-i16-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes complex, 16-bit signed integer data to the specified channel. To use the niUSRP Write Tx Data (I16) VI, you must set the Host Data Type property to I16. data accepts binary values that range from 32,767 to -32,768. The corresponding floating-point values range from 1.0 to ‑1.0. Use the follow

### niUSRP Write Tx Data (I16) VI

Writes complex, 16-bit signed integer data to the specified channel. To use the niUSRP Write Tx Data (I16) VI, you must set the [Host Data Type](/csh?context=niusrp_usrppropref_pniusrp_hostdatatype) property to I16.

**data** accepts binary values that range from 32,767 to -32,768. The corresponding floating-point values range from 1.0 to ‑1.0. Use the following equations to convert values from binary to floating-point or from floating-point to binary:

*floating-point value* = *binary value*/32,768

*binary value* = *floating-point value* x 32,767

[IMAGE alt='icon' src='niusrp-write-tx-data-i16-vi.png']

#### Inputs/Outputs

| channel list — channel list specifies the channel(s) to which to write the data. session handle — session handle identifies your instrument session. session handle is obtained from the niUSRP Open Tx Session VI and identifies a particular transmit (Tx) session. data — data specifies the baseband samples to transmit as an array of complex, 16-bit signed integer data. The real and imaginary components of the data correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. I and Q are interleaved [I, Q, I, Q, ...] in the array. The time between samples in the waveform (the sample period) equals 1 divided by the coerced I/Q rate. Determine the coerced I/Q rate by reading the IQ Rate property after you set it or by reading the coerced IQ rate output of the Configure Signal VI. data accepts signed, 16-bit integer values that range from 32,767 to -32,768. The maximum complex magnitude is 32,767. However, because the DSP frequency response varies over frequency and over I/Q rates, some tones with a complex magnitude less than but close to 32,767 may cause DSP overflow. Consider reducing the amplitude if you observe unexpected spurs in the spectrum of your generated signal. Use the following equation to determine the complex magnitude of the signal: timeout — timeout specifies the time to wait, in seconds, before returning an error if the requested number of samples have not been generated. A negative value indicates to the driver to wait indefinitely. end of data? — end of data? specifies whether this is the last call to the niUSRP Write Tx Data VI for the current contiguous transmit operation. The default value is FALSE. TRUE Specifies that data contains the end of the data transmission. The transmission aborts when the last data sample generates. FALSE Specifies that you will provide more data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. session handle out — session handle out passes a reference to your instrument session to the next VI. session handle out is obtained from the niUSRP Open Tx Session VI and identifies a particular transmit (Tx) session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE | Specifies that data contains the end of the data transmission. The transmission aborts when the last data sample generates. |
| FALSE | Specifies that you will provide more data. |

Parent topic:

niUSRP Write Tx Data (poly) VI

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/niusrp-write-tx-data-poly-vi.html language=enus -->
## TOPIC 00097: niUSRP Write Tx Data (poly) VI

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/niusrp-write-tx-data-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/niusrp-write-tx-data-poly-vi.html
- document_id: `ni-usrp-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to the specified channel list. icon

### niUSRP Write Tx Data (poly) VI

Writes data to the specified channel list.

[IMAGE alt='icon' src='niusrp-write-tx-data-poly-vi.png']

- [niUSRP Write Tx Data (CDB Cluster) VI](../../instr-lib/niusrp/niusrp-write-tx-data-cdb-cluster-vi.html) Writes a cluster of complex, double-precision floating-point data to the specified channel. Modulation Toolkit VIs use the complex, double-precision floating-point cluster data type. Use this VI in applications that use Modulation Toolkit VIs.
- [niUSRP Write Tx Data (CDB WDT) VI](../../instr-lib/niusrp/niusrp-write-tx-data-cdb-wdt-vi.html) Writes complex, double-precision floating-point data in a waveform data type to the specified channel.
- [niUSRP Write Tx Data (CDB) VI](../../instr-lib/niusrp/niusrp-write-tx-data-cdb-vi.html) Writes complex, double-precision floating-point data to the specified channel.
- [niUSRP Write Tx Data (I16) VI](../../instr-lib/niusrp/niusrp-write-tx-data-i16-vi.html) Writes complex, 16-bit signed integer data to the specified channel. To use the niUSRP Write Tx Data (I16) VI, you must set the Host Data Type property to I16.
- [niUSRP Write Tx Data (2D CDB) VI](../../instr-lib/niusrp/niusrp-write-tx-data-2d-cdb-vi.html) Writes complex, double-precision floating-point data to the specified channels.
- [niUSRP Write Tx Data (2D I16) VI](../../instr-lib/niusrp/niusrp-write-tx-data-2d-i16-vi.html) Writes complex, 16-bit signed integer data to the specified channels. To use the niUSRP Write Tx Data (2D I16) VI, you must set the Host Data Type property to I16.

Parent topic:

Tx

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/standard-error-in-parameters.html language=enus -->
## TOPIC 00098: Using the Standard Functionality for error in Parameters

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/standard-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/standard-error-in-parameters.html
- document_id: `ni-usrp-labview-api-ref`
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

<!--NI_TOPIC bundle=ni-usrp-labview-api-ref path=instr-lib/niusrp/standard-error-out-parameters.html language=enus -->
## TOPIC 00099: Using the Standard Functionality for error out Parameters

- bundle_id: `ni-usrp-labview-api-ref`
- source_path: `instr-lib/niusrp/standard-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/ni-usrp-labview-api-ref/raw/resource/enus/instr-lib/niusrp/standard-error-out-parameters.html
- document_id: `ni-usrp-labview-api-ref`
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
