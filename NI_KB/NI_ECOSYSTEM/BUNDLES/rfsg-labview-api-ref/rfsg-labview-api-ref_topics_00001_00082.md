# NI DOCUMENT BUNDLE: rfsg-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfsg-labview-api-ref start=1 end=82 -->
<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/dir-mnu.html language=enus -->
## TOPIC 00001: NI-RFSG

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/dir-mnu.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This help file contains technical and programming support for using the NI-RFSG LabVIEW API. This help file provides reference material for the NI-RFSG VIs. Use the NI-RFSG VIs to program RF signal generators using the NI-RFSG instrument driver. © 2004–2025 National Instruments Corporation. All righ

### NI-RFSG

This help file contains technical and programming support for using the NI-RFSG LabVIEW API. This help file provides reference material for the NI-RFSG VIs.

Use the NI-RFSG VIs to program RF signal generators using the NI-RFSG instrument driver.

© 2004–2025 National Instruments Corporation. All rights reserved.

[IMAGE alt='icon' src='dir-mnu.png']

- [niRFSG Initialize VI](../../instr-lib/nirfsg/nirfsg-initialize-vi.html) Opens a session to the device you specify as the resource name and returns an instrument handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG VIs.
- [niRFSG Configure RF VI](../../instr-lib/nirfsg/nirfsg-configure-rf-vi.html) Configures the frequency and power level of the RF output signal. The PXI-5670/5671, PXIe-5672, and PXIe-5860 device must be in the Configuration state before you call this VI. The PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 device can be in the Configuration state or Generation state when you call this VI.
- [niRFSG Initiate VI](../../instr-lib/nirfsg/nirfsg-initiate-vi.html) Initiates signal generation, causing the NI-RFSG device to leave the Configuration state or Committed state and enter the Generation state. If settings have not been committed to the device before you use this VI, they are committed by this VI. The operation returns when the RF output signal settles. To return to the Configuration state, use the niRFSG Abort VI.
- [niRFSG Check Generation Status VI](../../instr-lib/nirfsg/nirfsg-check-generation-status-vi.html) Checks the status of the generation. Use this VI to check for any errors that may occur during signal generation or to check whether the device has finished generating.
- [niRFSG Close VI](../../instr-lib/nirfsg/nirfsg-close-vi.html) Aborts any signal generation in progress and destroys the instrument driver session.
- [niRFSG Property Node VI](../../instr-lib/nirfsg/nirfsg-property-node-vi.html) Gets (reads), sets (writes), or resets (sets to default value) NI-RFSG properties. When you read a property, NI-RFSG analyzes the current configuration in order to return the coerced value for that property. NI-RFSG verifies many properties upon reading, thereby either transitioning the session to the verified state or alerting you of an invalid configuration. Setting or resetting a property transitions the session to an unverified state.
- [Generation Configuration](../../instr-lib/nirfsg/nirfsg-config-mnu.html) Use the Configuration VIs to configure the signal generation.
- [niRFSG Abort VI](../../instr-lib/nirfsg/nirfsg-abort-vi.html) Stops signal generation.
- [Utility](../../instr-lib/nirfsg/nirfsg-utility-mnu.html) Use the utility VIs to access additional features of the NI-RFSG instrument driver.
- [Calibration](../../instr-lib/nirfsg/nirfsg-calibration-mnu.html) Use the Calibration VIs to calibrate your device. Refer to the calibration procedure for your device for more information about device calibration.

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-5611-initialize-impairment-calibration-vi.html language=enus -->
## TOPIC 00002: niRFSG 5611 Initialize Impairment Calibration VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-5611-initialize-impairment-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-5611-initialize-impairment-calibration-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an impairment calibration section. Supported Devices: PXIe-5611, PXIe-5673/5673E Related Topics Impairment Calibration icon Inputs/Outputs civrn.png instrument handle instrument handle identifies your instrument calibration session. instrument handle is obtained from the niRFSG Initializ

### niRFSG 5611 Initialize Impairment Calibration VI

Initializes an impairment calibration section.

**Supported Devices**: PXIe-5611, PXIe-5673/5673E

**Related Topics**

[Impairment Calibration](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=impairment-calibration)

[IMAGE alt='icon' src='nirfsg-5611-initialize-impairment-calibration-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument calibration session. instrument handle is obtained from the niRFSG Initialize External Calibration VI. modulator to calibrate — modulator to calibrate specifies which modulator to calibrate. Lower Frequency Modulator Specifies the lower frequency modulator to calibrate. Higher Frequency Modulator Specifies the higher frequency modulator to calibrate. Both Modulators (default) Specifies the lower frequency and higher frequency modulator to calibrate. If you do not calibrate both modulators, you must repeat the entire adjustment procedure for each modulator to complete a full calibration. error in (no error) — error in(no error) describes error conditions that occur before this node runs. The default is no error. This node does not pass the error in(no error) input to the error out output. Regardless of whether an error occurred before this node runs, the node returns no error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Lower Frequency Modulator | Specifies the lower frequency modulator to calibrate. |
| Higher Frequency Modulator | Specifies the higher frequency modulator to calibrate. |
| Both Modulators (default) | Specifies the lower frequency and higher frequency modulator to calibrate. |

Parent topic:

NI PXIe-5611 Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-5611-initialize-lo-filter-calibration-vi.html language=enus -->
## TOPIC 00003: niRFSG 5611 Initialize LO Filter Calibration VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-5611-initialize-lo-filter-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-5611-initialize-lo-filter-calibration-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates external calibration constants for calibrating the LO filter DAC. Supported Devices: PXIe-5611, PXIe-5673/5673E icon Inputs/Outputs civrn.png instrument handle instrument handle identifies your instrument calibration session. instrument handle is obtained from the niRFSG Initialize Externa

### niRFSG 5611 Initialize LO Filter Calibration VI

Generates external calibration constants for calibrating the LO filter DAC.

**Supported Devices**: PXIe-5611, PXIe-5673/5673E

[IMAGE alt='icon' src='nirfsg-5611-initialize-lo-filter-calibration-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument calibration session. instrument handle is obtained from the niRFSG Initialize External Calibration VI. filter to calibrate — filter to calibrate specifies which filter to calibrate. The default value is All Filters. If you choose not to calibrate all filters, you must repeat the entire adjustment procedure on all filters to complete a full calibration. All Filters Specifies all filters. Filter166 Specifies the Filter166 filter. Filter630 Specifies the Filter630 filter. Filter323 Specifies the Filter323 filter. Filter1147 Specifies the Filter1147 filter. Filter2088 Specifies the Filter2088 filter. error in (no error) — error in(no error) describes error conditions that occur before this node runs. The default is no error. This node does not pass the error in(no error) input to the error out output. Regardless of whether an error occurred before this node runs, the node returns no error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| All Filters | Specifies all filters. |
| Filter166 | Specifies the Filter166 filter. |
| Filter630 | Specifies the Filter630 filter. |
| Filter323 | Specifies the Filter323 filter. |
| Filter1147 | Specifies the Filter1147 filter. |
| Filter2088 | Specifies the Filter2088 filter. |

Parent topic:

NI PXIe-5611 Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-5652-adjust-reference-clock-calibration-vi.html language=enus -->
## TOPIC 00004: niRFSG 5652 Adjust Reference Clock Calibration VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-5652-adjust-reference-clock-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-5652-adjust-reference-clock-calibration-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration information pertaining to the 10 MHz OCXO reference of the PXI/PXIe-5650/5651/5652. This calculation is based on user-supplied measurements. The calibration information is stored in the driver session, and you can later write this information to the device. Supported Devices:

### niRFSG 5652 Adjust Reference Clock Calibration VI

Calculates calibration information pertaining to the 10 MHz OCXO reference of the PXI/PXIe-5650/5651/5652. This calculation is based on user-supplied measurements. The calibration information is stored in the driver session, and you can later write this information to the device.

**Supported Devices**: PXI/PXIe-5650/5651/5652

[IMAGE alt='icon' src='nirfsg-5652-adjust-reference-clock-calibration-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument calibration session. measured REF OUT frequency (Hz) — measured REF OUT frequency specifies the frequency measured at the REF OUT front panel connector. measured REF OUT power (dBm) — measured REF OUT power specifies the power measured at the frequency indicated by the measured REF OUT frequency input. error in (no error) — error in(no error) describes error conditions that occur before this node runs. The default is no error. This node does not pass the error in(no error) input to the error out output. Regardless of whether an error occurred before this node runs, the node returns no error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. reference clock calibration complete — reference clock calibration complete indicates whether the Reference Clock calibration is complete. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI 5652 Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-5652-configure-alc-calibration-vi.html language=enus -->
## TOPIC 00005: niRFSG 5652 Configure ALC Calibration VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-5652-configure-alc-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-5652-configure-alc-calibration-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the PXI/PXIe-5650/5651/5652 for the next automatic leveling control (ALC) calibration point and waits for the output signal to settle. Supported Devices: PXI/PXIe-5650/5651/5652 icon Inputs/Outputs civrn.png instrument handle instrument handle identifies your instrument calibration sessio

### niRFSG 5652 Configure ALC Calibration VI

Configures the PXI/PXIe-5650/5651/5652 for the next automatic leveling control (ALC) calibration point and waits for the output signal to settle.

**Supported Devices**: PXI/PXIe-5650/5651/5652

[IMAGE alt='icon' src='nirfsg-5652-configure-alc-calibration-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument calibration session. error in (no error) — error in(no error) describes error conditions that occur before this node runs. The default is no error. This node does not pass the error in(no error) input to the error out output. Regardless of whether an error occurred before this node runs, the node returns no error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. frequency to measure (Hz) — frequency to measure indicates the frequency of the generated signal. This value is expressed in hertz. The power of the generated signal should be measured. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI 5652 Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-5652-configure-attenuator-calibration-vi.html language=enus -->
## TOPIC 00006: niRFSG 5652 Configure Attenuator Calibration VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-5652-configure-attenuator-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-5652-configure-attenuator-calibration-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the PXI/PXIe-5650/5651/5652 for the next attenuator calibration point and waits for the output signal to settle. Supported Devices: PXI/PXIe-5650/5651/5652 icon Inputs/Outputs civrn.png instrument handle instrument handle identifies your instrument calibration session. cerrcodeclst.png er

### niRFSG 5652 Configure Attenuator Calibration VI

Configures the PXI/PXIe-5650/5651/5652 for the next attenuator calibration point and waits for the output signal to settle.

**Supported Devices**: PXI/PXIe-5650/5651/5652

[IMAGE alt='icon' src='nirfsg-5652-configure-attenuator-calibration-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument calibration session. error in (no error) — error in(no error) describes error conditions that occur before this node runs. The default is no error. This node does not pass the error in(no error) input to the error out output. Regardless of whether an error occurred before this node runs, the node returns no error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. frequency to measure (Hz) — frequency to measure indicates the frequency of the generated signal. This value is expressed in hertz. The power of the generated signal should be measured. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI 5652 Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-5652-configure-reference-clock-calibration-vi.html language=enus -->
## TOPIC 00007: niRFSG 5652 Configure Reference Clock Calibration VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-5652-configure-reference-clock-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-5652-configure-reference-clock-calibration-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the PXI/PXIe-5650/5651/5652 with specific settings for calibrating the 10 MHz OCXO reference. Supported Devices: PXI/PXIe-5650/5651/5652 icon Inputs/Outputs civrn.png instrument handle instrument handle identifies your instrument calibration session. cerrcodeclst.png error in (no error) e

### niRFSG 5652 Configure Reference Clock Calibration VI

Configures the PXI/PXIe-5650/5651/5652 with specific settings for calibrating the 10 MHz OCXO reference.

**Supported Devices**: PXI/PXIe-5650/5651/5652

[IMAGE alt='icon' src='nirfsg-5652-configure-reference-clock-calibration-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument calibration session. error in (no error) — error in(no error) describes error conditions that occur before this node runs. The default is no error. This node does not pass the error in(no error) input to the error out output. Regardless of whether an error occurred before this node runs, the node returns no error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. center frequency (Hz) — center frequency returns the value at which to set the spectrum analyzer center frequency. frequency span (Hz) — frequency span returns the value at which to set the spectrum analyzer frequency span. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI 5652 Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-5696-attenuator-path-cal-adjust-vi.html language=enus -->
## TOPIC 00008: niRFSG 5696 Attenuator Path Cal Adjust VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-5696-attenuator-path-cal-adjust-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-5696-attenuator-path-cal-adjust-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration information pertaining to the attenuator path on the PXIe-5696. This calculation is based on user-supplied measurements. The calibration information is stored in the driver session, and you can later write this information to the device. Supported Devices: PXIe-5696 icon Input

### niRFSG 5696 Attenuator Path Cal Adjust VI

Calculates calibration information pertaining to the attenuator path on the PXIe-5696. This calculation is based on user-supplied measurements. The calibration information is stored in the driver session, and you can later write this information to the device.

**Supported Devices**: PXIe-5696

[IMAGE alt='icon' src='nirfsg-5696-attenuator-path-cal-adjust-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument calibration session. measured power (dBm) — measured power specifies the power measured at the frequency indicated by the niRFSG 5696 Attenuator Path Cal Configure VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. attenuator calibration complete — attenuator calibration complete indicates whether the attenuator calibration is complete. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI PXIe-5696 Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-calibration-mnu.html language=enus -->
## TOPIC 00009: Calibration

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-calibration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-calibration-mnu.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Calibration VIs to calibrate your device. Refer to the calibration procedure for your device for more information about device calibration. icon

### Calibration

Use the Calibration VIs to calibrate your device. Refer to the [calibration procedure](/csh?context=nirfsg_rfsg_related) for your device for more information about device calibration.

[IMAGE alt='icon' src='nirfsg-calibration-mnu.png']

- [Self Calibration](../../instr-lib/nirfsg/nirfsg-self-calibration-mnu.html) Use the Self Calibration VIs to perform self-calibration and to obtain information about previous calibrations.
- [External Calibration](../../instr-lib/nirfsg/nirfsg-external-calibration-mnu.html) Use the External Calibration VIs to calibrate your device. Refer to the calibration procedure for your device for more information about device calibration.

Parent topic:

NI-RFSG

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-calibration-ni-5652-mnu.html language=enus -->
## TOPIC 00010: NI 5652 Calibration

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-calibration-ni-5652-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-calibration-ni-5652-mnu.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI 5652 Calibration VIs to calibrate your PXI/PXIe-5650/5651/5652 device. Refer to the calibration procedure for your device for more information about device calibration. icon

### NI 5652 Calibration

Use the NI 5652 Calibration VIs to calibrate your PXI/PXIe-5650/5651/5652 device. Refer to the [calibration procedure](/csh?context=nirfsg_rfsg_related) for your device for more information about device calibration.

[IMAGE alt='icon' src='nirfsg-calibration-ni-5652-mnu.png']

- [niRFSG 5652 Initialize ALC Calibration VI](../../instr-lib/nirfsg/nirfsg-5652-initialize-alc-calibration-vi.html) Generates external calibration constants for calibrating the automatic leveling control (ALC).
- [niRFSG 5652 Configure ALC Calibration VI](../../instr-lib/nirfsg/nirfsg-5652-configure-alc-calibration-vi.html) Configures the PXI/PXIe-5650/5651/5652 for the next automatic leveling control (ALC) calibration point and waits for the output signal to settle.
- [niRFSG 5652 Adjust ALC Calibration VI](../../instr-lib/nirfsg/nirfsg-5652-adjust-alc-calibration-vi.html) Calculates calibration information pertaining to the ALC of the PXI/PXIe-5650/5651/5652. This calculation is based on user-supplied measurements. The calibration information is stored in the driver session, and you can later write this information to the device.
- [niRFSG 5652 Initialize Attenuator Calibration VI](../../instr-lib/nirfsg/nirfsg-5652-initialize-attenuator-calibration-vi.html) Generates external calibration constants for calibrating the attenuator.
- [niRFSG 5652 Configure Attenuator Calibration VI](../../instr-lib/nirfsg/nirfsg-5652-configure-attenuator-calibration-vi.html) Configures the PXI/PXIe-5650/5651/5652 for the next attenuator calibration point and waits for the output signal to settle.
- [niRFSG 5652 Adjust Attenuator Calibration VI](../../instr-lib/nirfsg/nirfsg-5652-adjust-attenuator-calibration-vi.html) Calculates calibration information pertaining to the selected attenuator on the PXI/PXIe-5650/5651/5652. This calculation is based on user-supplied measurements. The calibration information is stored in the driver session, and you can later write this information to the device.
- [niRFSG 5652 Validate ALC Limits Table VI](../../instr-lib/nirfsg/nirfsg-5652-validate-alc-limits-table-vi.html) Validates the PXI/PXIe-5650/5651/5652 ALC limits table, which determines the attenuator and path NI-RFSG uses for each frequency and power combination.
- [niRFSG 5652 Initialize Reference Clock Calibration VI](../../instr-lib/nirfsg/nirfsg-5652-initialize-reference-clock-calibration-vi.html) Generates external calibration constants for calibrating the 10 MHz reference.
- [niRFSG 5652 Configure Reference Clock Calibration VI](../../instr-lib/nirfsg/nirfsg-5652-configure-reference-clock-calibration-vi.html) Configures the PXI/PXIe-5650/5651/5652 with specific settings for calibrating the 10 MHz OCXO reference.
- [niRFSG 5652 Adjust Reference Clock Calibration VI](../../instr-lib/nirfsg/nirfsg-5652-adjust-reference-clock-calibration-vi.html) Calculates calibration information pertaining to the 10 MHz OCXO reference of the PXI/PXIe-5650/5651/5652. This calculation is based on user-supplied measurements. The calibration information is stored in the driver session, and you can later write this information to the device.

Parent topic:

External Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-calibration-ni-pxie-5611-mnu.html language=enus -->
## TOPIC 00011: NI PXIe-5611 Calibration

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-calibration-ni-pxie-5611-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-calibration-ni-pxie-5611-mnu.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI PXIe-5611 Calibration VIs to calibrate your PXIe-5611 device. Refer to the calibration procedure for your device for more information about device calibration. icon

### NI PXIe-5611 Calibration

Use the NI PXIe-5611 Calibration VIs to calibrate your PXIe-5611 device. Refer to the [calibration procedure](/csh?context=nirfsg_rfsg_related) for your device for more information about device calibration.

[IMAGE alt='icon' src='nirfsg-calibration-ni-pxie-5611-mnu.png']

- [niRFSG 5611 Initialize LO Filter Calibration VI](../../instr-lib/nirfsg/nirfsg-5611-initialize-lo-filter-calibration-vi.html) Generates external calibration constants for calibrating the LO filter DAC.
- [niRFSG 5611 Configure LO Filter Calibration VI](../../instr-lib/nirfsg/nirfsg-5611-configure-lo-filter-calibration-vi.html) Configures the device for the next LO filter DAC calibration point and waits for the output signal to settle.
- [niRFSG 5611 Adjust LO Filter Calibration VI](../../instr-lib/nirfsg/nirfsg-5611-adjust-lo-filter-calibration-vi.html) Calculates calibration information pertaining to the LO filter DAC. This information is based on user-supplied measurements. The calibration information is stored in driver session, and you can later write this information to the device.
- [niRFSG 5611 Initialize LO Gain Calibration VI](../../instr-lib/nirfsg/nirfsg-5611-initialize-lo-gain-calibration-vi.html) Generates external calibration constants for calibrating the LO gain.
- [niRFSG 5611 Configure LO Gain Calibration VI](../../instr-lib/nirfsg/nirfsg-5611-configure-lo-gain-calibration-vi.html) Configures the device for the next LO gain calibration point and waits for the output signal to settle.
- [niRFSG 5611 Adjust LO Gain Calibration VI](../../instr-lib/nirfsg/nirfsg-5611-adjust-lo-gain-calibration-vi.html) Calculates calibration information pertaining to the LO gain of the device based on user-supplied measurements. The calibration information is stored in the driver session and can later be written to the device.
- [niRFSG 5611 Initialize Impairment Calibration VI](../../instr-lib/nirfsg/nirfsg-5611-initialize-impairment-calibration-vi.html) Initializes an impairment calibration section.
- [niRFSG 5611 Configure Impairment Calibration VI](../../instr-lib/nirfsg/nirfsg-5611-configure-impairment-calibration-vi.html) Configures the device for the next impairment calibration point and waits for the output signal to settle.
- [niRFSG 5611 Adjust Impairment Calibration VI](../../instr-lib/nirfsg/nirfsg-5611-adjust-impairment-calibration-vi.html) Calculates calibration information pertaining to the impairments of the device based on user-supplied measurements. The calibration information is stored in the driver session and can later be written to the device.
- [niRFSG 5611 Initialize RF Gain Calibration VI](../../instr-lib/nirfsg/nirfsg-5611-initialize-rf-gain-calibration-vi.html) Generates external calibration constants for calibrating the RF gain.
- [niRFSG 5611 Configure RF Gain Calibration VI](../../instr-lib/nirfsg/nirfsg-5611-configure-rf-gain-calibration-vi.html) Configures the device for the next RF gain calibration point and waits for the output signal to settle.
- [niRFSG 5611 Adjust RF Gain Calibration VI](../../instr-lib/nirfsg/nirfsg-5611-adjust-rf-gain-calibration-vi.html) Calculates calibration information pertaining to the RF gain of the device based on user-supplied measurements. The calibration information is stored in the driver session and can later be written to the device.

Parent topic:

External Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-check-generation-status-vi.html language=enus -->
## TOPIC 00012: niRFSG Check Generation Status VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-check-generation-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-check-generation-status-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the generation. Use this VI to check for any errors that may occur during signal generation or to check whether the device has finished generating. Supported Devices: PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe

### niRFSG Check Generation Status VI

Checks the status of the generation. Use this VI to check for any errors that may occur during signal generation or to check whether the device has finished generating.

**Supported Devices**: PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[NI-RFSG Instrument Driver Programming Flow](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=ni-rfsg-instrument-driver-programming-flow)

[Stopping Pear-to-Peer Generation](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=stopping-peer-to-peer-generation)

[IMAGE alt='icon' src='nirfsg-check-generation-status-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. done? — done? returns TRUE when signal generation has completed. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-RFSG

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-clear-all-arb-waveforms-vi.html language=enus -->
## TOPIC 00013: niRFSG Clear All Arb Waveforms VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-clear-all-arb-waveforms-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-clear-all-arb-waveforms-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes all currently defined waveforms and scripts. The NI-RFSG device must be in the Configuration state before you call this VI. Supported Devices: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs civrn.png instrument handl

### niRFSG Clear All Arb Waveforms VI

Deletes all currently defined waveforms and scripts. The NI-RFSG device must be in the Configuration state before you call this VI.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-clear-all-arb-waveforms-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Waveform

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-clear-self-calibrate-range-vi.html language=enus -->
## TOPIC 00014: niRFSG Clear Self Calibrate Range VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-clear-self-calibrate-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-clear-self-calibrate-range-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the data obtained from the niRFSG Self Calibrate Range VI. Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842 icon Inputs/Outputs civrn.png instrument handle instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG

### niRFSG Clear Self Calibrate Range VI

Clears the data obtained from the [niRFSG Self Calibrate Range](/csh?topicname=nirfsg-self-calibrate-range-vi.html) VI.

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

[IMAGE alt='icon' src='nirfsg-clear-self-calibrate-range-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Self Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-close-vi.html language=enus -->
## TOPIC 00015: niRFSG Close VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-close-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-close-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts any signal generation in progress and destroys the instrument driver session. Supported Devices: PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Related Top

### niRFSG Close VI

Aborts any signal generation in progress and destroys the instrument driver session.

**Supported Devices**: PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[NI-RFSG Instrument Driver Programming Flow](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=ni-rfsg-instrument-driver-programming-flow)

[NI-RFSG Programming State Model](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=ni-rfsg-programming-state-model)

[IMAGE alt='icon' src='nirfsg-close-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. The default is no error. This node passes the error in input to the error out output. This node will run regardless of whether an error occurred before it. This input contains status, code, and source, which provide standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-RFSG

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-config-mnu.html language=enus -->
## TOPIC 00016: Generation Configuration

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-config-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-config-mnu.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Configuration VIs to configure the signal generation. icon

### Generation Configuration

Use the Configuration VIs to configure the signal generation.

[IMAGE alt='icon' src='nirfsg-config-mnu.png']

- [Configure Waveform](../../instr-lib/nirfsg/nirfsg-configure-waveform-mnu.html) Use the Waveform Configuration VIs to configure a waveform.
- [Configuration List](../../instr-lib/nirfsg/nirfsg-configuration-list-mnu.html) Use the configuration list VIs to use RF list mode.
- [Configure Trigger](../../instr-lib/nirfsg/nirfsg-configure-trigger-mnu.html) Use the Trigger Configuration VIs to configure NI-RFSG triggers.
- [Configure Clock](../../instr-lib/nirfsg/nirfsg-configure-clock-mnu.html) Use the Clock Configuration VIs to configure the clocks.
- [Peer To Peer](../../instr-lib/nirfsg/nirfsg-configure-p2p-mnu.html) Use the peer-to-peer VIs to configure peer-to-peer streaming.
- [De-embedding](../../instr-lib/nirfsg/nirfsg-deembedding-mnu.html) Use the NI-RFSG De-embedding VIs to de-embed measurements.

Parent topic:

NI-RFSG

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-configure-de-embedding-table-interpolation-nearest-vi.html language=enus -->
## TOPIC 00017: niRFSG Configure De-embedding Table Interpolation (Nearest) VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-configure-de-embedding-table-interpolation-nearest-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-configure-de-embedding-table-interpolation-nearest-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the nearest interpolation method. The parameters of the table nearest to the carrier frequency are used for de-embedding. Supported Devices: PXIe-5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs civrn.png instrument handle instrument handle identifies your instrument session. instrumen

### niRFSG Configure De-embedding Table Interpolation (Nearest) VI

Selects the nearest interpolation method.

The parameters of the table nearest to the carrier frequency are used for de-embedding.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-configure-de-embedding-table-interpolation-nearest-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. port — port specifies the name of the port. The only valid value for the PXIe-5840/5841 is "" (empty string). table name — table name specifies the name of the table. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSG Configure De-embedding Table Interpolation VI

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-configure-ref-clock-vi.html language=enus -->
## TOPIC 00018: niRFSG Configure Ref Clock VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-configure-ref-clock-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-configure-ref-clock-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the NI-RFSG device Reference Clock. The Reference Clock ensures that the NI-RFSG devices are operating from a common timebase. The NI-RFSG device must be in the Configuration state before you call this VI. Supported Devices: PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/565

### niRFSG Configure Ref Clock VI

Configures the NI-RFSG device Reference Clock. The Reference Clock ensures that the NI-RFSG devices are operating from a common timebase. The NI-RFSG device must be in the Configuration state before you call this VI.

**Supported Devices**: PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[PXIe-5672 Timing Configurations](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=timing-configurations)

[PXIe-5673 Timing Configurations](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=timing-configurations-for-pxie-5673-modules)

[PXIe-5673E Timing Configurations](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=timing-configurations-for-pxie-5673e-modules)

[PXIe-5830 Timing Configurations](https://ni.com/docs/en-US/csh?pubname=pxie-5830-feature&topicname=timing-configurations)

[PXIe-5831/5832 Timing Configurations](https://ni.com/docs/en-US/csh?pubname=pxie-5831&topicname=timing-configurations)

[IMAGE alt='icon' src='nirfsg-configure-ref-clock-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. ref clock source — ref clock source specifies the source of the Reference Clock signal. Onboard Clock (default) Uses the onboard Reference Clock as the clock source. PXIe-5830/5831/5832â€”For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5841 with PXIe-5655â€”Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. PXIe-5842â€”Lock to the associated PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. RefIn Uses the clock signal present at the front panel REF IN connector as the clock source. PXIe-5830/5831/5832â€”For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe- 3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For the PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5841 with PXIe-5655â€”Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. PXIe-5842â€”Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXI Clock Uses the PXI_CLK signal, which is present on the PXI backplane, as the clock source. PXI_ClkMaster This value is valid on only the PXIe-5831 with PXIe-5653 and the PXIe-5832 with PXIe-5653. PXIe-5831 with PXIe-5653â€”NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653â€”NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. ref clock rate (Hz) — ref clock rate specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. This parameter is only valid when the ref clock source parameter is set to RefIn. The default value is Auto (-1.0), which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. Refer to the Reference Clock Rate property for possible values. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Onboard Clock (default) | Uses the onboard Reference Clock as the clock source. PXIe-5830/5831/5832â€”For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5841 with PXIe-5655â€”Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. PXIe-5842â€”Lock to the associated PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
| RefIn | Uses the clock signal present at the front panel REF IN connector as the clock source. PXIe-5830/5831/5832â€”For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe- 3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For the PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5841 with PXIe-5655â€”Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. PXIe-5842â€”Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
| PXI Clock | Uses the PXI_CLK signal, which is present on the PXI backplane, as the clock source. |
| PXI_ClkMaster | This value is valid on only the PXIe-5831 with PXIe-5653 and the PXIe-5832 with PXIe-5653. PXIe-5831 with PXIe-5653â€”NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653â€”NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. |

Parent topic:

Configure Clock

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-configure-script-trigger-digital-edge-vi.html language=enus -->
## TOPIC 00019: niRFSG Configure Script Trigger Digital Edge VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-configure-script-trigger-digital-edge-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-configure-script-trigger-digital-edge-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a specified Script Trigger for digital edge triggering. Supported Devices: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs cstr.png trigger id trigger id specifies the Script Trigger to configure. civrn.png instrum

### niRFSG Configure Script Trigger Digital Edge VI

Configures a specified Script Trigger for digital edge triggering.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-configure-script-trigger-digital-edge-vi.png']

#### Inputs/Outputs

| trigger id — trigger id specifies the Script Trigger to configure. instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. source — source specifies the trigger source terminal for the digital edge Script Trigger. NI-RFSG sets the Digital Edge Script Trigger Source property to this value. Refer to this property for possible values. edge — edge specifies the active edge for the digital edge Script Trigger. NI-RFSG sets the Digital Edge Script Trigger Edge property to this value. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSG Configure Trigger VI

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-configure-script-trigger-digital-level-vi.html language=enus -->
## TOPIC 00020: niRFSG Configure Script Trigger Digital Level VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-configure-script-trigger-digital-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-configure-script-trigger-digital-level-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a specified Script Trigger for digital level triggering. Supported Devices: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs cstr.png trigger id trigger id specifies the Script Trigger to configure. civrn.png instru

### niRFSG Configure Script Trigger Digital Level VI

Configures a specified Script Trigger for digital level triggering.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-configure-script-trigger-digital-level-vi.png']

#### Inputs/Outputs

| trigger id — trigger id specifies the Script Trigger to configure. instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. source — source specifies the trigger source terminal for the digital level Script Trigger. NI-RFSG sets the Digital Level Script Trigger Source property to this value. Refer to this property for possible values. level — level specifies the active level for the digital level Script Trigger. NI-RFSG sets the Digital Level Script Trigger Active Level property to this value. Refer to this property for possible values. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSG Configure Trigger VI

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-configure-script-trigger-software-vi.html language=enus -->
## TOPIC 00021: niRFSG Configure Script Trigger Software VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-configure-script-trigger-software-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-configure-script-trigger-software-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a specified Script Trigger for software triggering. Supported Devices: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs cstr.png trigger id trigger id specifies the Script Trigger to configure. civrn.png instrument

### niRFSG Configure Script Trigger Software VI

Configures a specified Script Trigger for software triggering.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-configure-script-trigger-software-vi.png']

#### Inputs/Outputs

| trigger id — trigger id specifies the Script Trigger to configure. instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSG Configure Trigger VI

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-configure-signal-bandwidth-vi.html language=enus -->
## TOPIC 00022: niRFSG Configure Signal Bandwidth VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-configure-signal-bandwidth-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-configure-signal-bandwidth-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the signal bandwidth of the arbitrary waveform. The NI-RFSG device must be in the Configuration state before you call this VI. Supported Devices: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs civrn.png instrument

### niRFSG Configure Signal Bandwidth VI

Configures the signal bandwidth of the arbitrary waveform. The NI-RFSG device must be in the Configuration state before you call this VI.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-configure-signal-bandwidth-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. signal bandwidth (Hz) — signal bandwidth specifies the signal bandwidth used by NI-RFSG for generating an RF output signal. NI-RFSG sets the Signal Bandwidth (Hz) property to this value. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

NI-RFSG defines *signal bandwidth* as twice the maximum baseband signal
 deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such
 cases, the signal bandwidth is simply the baseband signal's minimum frequency subtracted
 from its maximum frequency, or *f*
<sub>max</sub> - *f*
<sub>min</sub>. NI-RFSG uses this value to optimally configure
 the center frequency of the upconverter to help minimize phase noise.
 The generated signal is not filtered to achieve the set bandwidth. However, specifying
 a bandwidth smaller than the actual bandwidth of the signal could potentially result in spectral
 distortion.

Note

Parent topic:

Configure Waveform

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-configure-start-trigger-digital-edge-vi.html language=enus -->
## TOPIC 00023: niRFSG Configure Start Trigger Digital Edge VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-configure-start-trigger-digital-edge-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-configure-start-trigger-digital-edge-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start Trigger for digital edge triggering. For the PXIe-5654/5654 with PXIe-5696, the Start Trigger is valid only with a timer-based list when RF list mode is enabled. Supported Devices: PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820

### niRFSG Configure Start Trigger Digital Edge VI

Configures the Start Trigger for digital edge triggering.

Note

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-configure-start-trigger-digital-edge-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. source — source specifies the trigger source terminal for the digital edge Start Trigger. NI-RFSG sets the Digital Edge Start Trigger Source property to this value. Refer to this property for possible values. edge — edge specifies the active edge for the digital edge Start Trigger. NI-RFSG sets the Digital Edge Start Trigger Edge property to this value. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSG Configure Trigger VI

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-configure-waveform-burstlocation-mnu.html language=enus -->
## TOPIC 00024: Burst Location

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-configure-waveform-burstlocation-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-configure-waveform-burstlocation-mnu.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the waveform burst VIs on this palette to configure NI-RFSG waveform burst locations. icon

### Burst Location

Use the waveform burst VIs on this palette to configure NI-RFSG waveform burst locations.

[IMAGE alt='icon' src='nirfsg-configure-waveform-burstlocation-mnu.png']

- [niRFSG Set Waveform Burst Start Locations VI](../../instr-lib/nirfsg/nirfsg-set-waveform-burst-start-locations-vi.html) Configures the start location of the burst in samples where the burst refers to the active portion of a waveform.
- [niRFSG Set Waveform Burst Stop Locations VI](../../instr-lib/nirfsg/nirfsg-set-waveform-burst-stop-locations-vi.html) Configures the stop location of the burst in samples where the burst refers to the active portion of a waveform.
- [niRFSG Get Waveform Burst Start Locations VI](../../instr-lib/nirfsg/nirfsg-get-waveform-burst-start-locations-vi.html) Returns the burst start locations of the waveform stored in the NI-RFSG session.
- [niRFSG Get Waveform Burst Stop Locations VI](../../instr-lib/nirfsg/nirfsg-get-waveform-burst-stop-locations-vi.html) Returns the burst stop locations of the waveforms stored in the NI-RFSG session.

Parent topic:

Configure Waveform

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-create-configuration-list-vi.html language=enus -->
## TOPIC 00025: niRFSG Create Configuration List VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-create-configuration-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-create-configuration-list-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an empty configuration list. Use the Active Configuration List property to enable a configuration list created by this VI. Call the niRFSG Create Configuration List Step VI to add steps to the configuration list. Supported Devices: PXIe-5644/5645/5646, PXIe-5650/5651/5652/5653/5654/5654 with

### niRFSG Create Configuration List VI

Creates an empty configuration list. Use the [Active Configuration List](/csh?context=nirfsg_rfsgproperties_pnirfsg_activeconfigurationlist) property to enable a configuration list created by this VI. Call the [niRFSG Create Configuration List Step](/csh?topicname=nirfsg-create-configuration-list-step-vi.html) VI to add steps to the configuration list.

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5650/5651/5652/5653/5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters

**Related Topics**

[RF List Mode](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=rf-list-mode)

[Using RF List Mode](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=using-rf-list-mode)

[IMAGE alt='icon' src='nirfsg-create-configuration-list-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. list name — list name specifies the name of the configuration list. This string is case-insensitive and alphanumeric, and it cannot contain spaces or use reserved words. configuration list properties — configuration list properties specifies the properties that you intend to change between configuration list steps. Calling the niRFSG Create Configuration List VI allocates space for each of the configuration list properties. When you use the niRFSG Property Node to set one of the configuration list properties, that property is set as one of the configuration list steps. Use the Active Configuration List Step property to specify which configuration list step to configure. You can include the following properties in your configuration list based on your device: Property PXIe-5644/5646 PXIe-5645 PXIe-5650/5651/5652 PXIe-5653 PXIe-5654 PXIe-5654 with PXIe-5696 PXIe-5673E PXIe-5820 PXIe-5830/5831/5832 PXIe-5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters PXIe-5841 with PXIe-5655 PXIe-5860 ALC Control ✓ Amp Path ✓ Amplitude Settling ✓ ✓ ✓ ✓ ✓ ✓ Attenuator Setting (dB) ✓ Automatic Power Search ✓ Digital Gain (dB) ✓ ✓ ✓ ✓ ✓ ✓ External Gain ✓ ✓ ✓ ✓ Frequency (Hz) ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Frequency Settling ✓ ✓ ✓ ✓ ✓ ✓ ✓ IQ Out Port Carrier Frequency ✓ ✓ IQ Out Port Common Mode Offset ✓ ✓ IQ Out Port Level ✓ ✓ IQ Out Port Offset ✓ ✓ LO Source ✓ ✓ Output Enabled ✓ ✓ Phase Offset (Degrees) ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Power Level (dBm) ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Pre-filter Gain (dB) ✓ ✓ ✓ ✓ ✓ Pulse Modulation Enabled ✓ ✓ ✓ RF In LO Export Enabled ✓ Selected Ports ✓ Signal Bandwidth (Hz) ✓ ✓ ✓ Timer Event Interval (s) ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Upconverter Center Frequency (Hz) ✓ ✓ ✓ ✓ Upconverter Frequency Offset (Hz) ✓ Upconverter Frequency Offset Mode ✓ ✓ ✓ set as active list — set as active list sets this list as the active configuration list when this parameter is enabled. NI recommends that you set this parameter to TRUE when creating the list. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Property | PXIe-5644/5646 | PXIe-5645 | PXIe-5650/5651/5652 | PXIe-5653 | PXIe-5654 | PXIe-5654 with PXIe-5696 | PXIe-5673E | PXIe-5820 | PXIe-5830/5831/5832 | PXIe-5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters | PXIe-5841 with PXIe-5655 | PXIe-5860 |
| ALC Control |  |  |  |  |  | ✓ |  |  |  |  |  |  |
| Amp Path |  |  |  |  |  | ✓ |  |  |  |  |  |  |
| Amplitude Settling |  |  |  |  | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ |
| Attenuator Setting (dB) |  |  |  |  |  | ✓ |  |  |  |  |  |  |
| Automatic Power Search |  |  |  |  |  | ✓ |  |  |  |  |  |  |
| Digital Gain (dB) | ✓ | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ |  | ✓ |
| External Gain |  |  |  |  |  |  |  | ✓ | ✓ | ✓ |  | ✓ |
| Frequency (Hz) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  | ✓ |
| Frequency Settling |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  | ✓ |
| IQ Out Port Carrier Frequency |  | ✓ |  |  |  |  |  | ✓ |  |  |  |  |
| IQ Out Port Common Mode Offset |  | ✓ |  |  |  |  |  | ✓ |  |  |  |  |
| IQ Out Port Level |  | ✓ |  |  |  |  |  | ✓ |  |  |  |  |
| IQ Out Port Offset |  | ✓ |  |  |  |  |  | ✓ |  |  |  |  |
| LO Source |  |  |  |  |  |  |  |  |  | ✓ | ✓ |  |
| Output Enabled |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |
| Phase Offset (Degrees) | ✓ | ✓ | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  | ✓ |
| Power Level (dBm) | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ | ✓ |  | ✓ |
| Pre-filter Gain (dB) |  |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ |  | ✓ |
| Pulse Modulation Enabled |  |  |  |  | ✓ | ✓ | ✓ |  |  |  |  |  |
| RF In LO Export Enabled |  |  |  |  |  |  |  |  |  | ✓ |  |  |
| Selected Ports |  |  |  |  |  |  |  |  | ✓ |  |  |  |
| Signal Bandwidth (Hz) |  |  |  |  |  |  |  | ✓ |  | ✓ |  | ✓ |
| Timer Event Interval (s) | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |
| Upconverter Center Frequency (Hz) | ✓ | ✓ |  |  |  |  | ✓ |  |  | ✓ |  |  |
| Upconverter Frequency Offset (Hz) |  |  |  |  |  |  |  |  |  | ✓ |  |  |
| Upconverter Frequency Offset Mode |  |  |  |  |  |  |  |  |  | ✓ | ✓ | ✓ |

Parent topic:

Configuration List

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-get-external-calibration-last-date-and-time-vi.html language=enus -->
## TOPIC 00026: niRFSG Get External Calibration Last Date and Time VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-get-external-calibration-last-date-and-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-get-external-calibration-last-date-and-time-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time. For example, if the device was calibrated at 2:30 PM, this VI returns 14 for the hours and 30 for the minutes. Supported Devices: PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/P

### niRFSG Get External Calibration Last Date and Time VI

Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time. For example, if the device was calibrated at 2:30 PM, this VI returns **14** for the hours and **30** for the minutes.

**Supported Devices**: PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-get-external-calibration-last-date-and-time-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI, the niRFSG Initialize With Options VI, or the niRFSG Initialize External Calibration VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from either the niRFSG Initialize VI, the niRFSG Initialize With Options VI, or the niRFSG Initialize External Calibration VI. last external calibration date and time — last external calibration date and time specifies the date and time of the last successful external calibration. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-get-waveform-burst-start-locations-vi.html language=enus -->
## TOPIC 00027: niRFSG Get Waveform Burst Start Locations VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-get-waveform-burst-start-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-get-waveform-burst-start-locations-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the burst start locations of the waveform stored in the NI-RFSG session. Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842 icon Inputs/Outputs cstr.png channel name channel name specifies the waveform name and the marker name. Example: "waveform::waveform0/marker0" civrn.png instrum

### niRFSG Get Waveform Burst Start Locations VI

Returns the burst start locations of the waveform stored in the NI-RFSG session.

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842

[IMAGE alt='icon' src='nirfsg-get-waveform-burst-start-locations-vi.png']

#### Inputs/Outputs

| channel name — channel name specifies the waveform name and the marker name. Example: "waveform::waveform0/marker0" instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. locations — locations returns the burst start locations stored in the NI-RFSG session for the waveform you specified in the channel name parameter. This value is expressed in samples. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Burst Location

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-get-waveform-marker-event-locations-vi.html language=enus -->
## TOPIC 00028: niRFSG Get Waveform Marker Event Locations VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-get-waveform-marker-event-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-get-waveform-marker-event-locations-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the marker locations associated with the waveform and the marker stored in the NI-RFSG session. Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842 icon Inputs/Outputs cstr.png channel name channel name specifies the waveform name and the marker name. Example: "waveform::waveform0/mar

### niRFSG Get Waveform Marker Event Locations VI

Returns the marker locations associated with the waveform and the marker stored in the NI-RFSG session.

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842

[IMAGE alt='icon' src='nirfsg-get-waveform-marker-event-locations-vi.png']

#### Inputs/Outputs

| channel name — channel name specifies the waveform name and the marker name. Example: "waveform::waveform0/marker0" instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. locations — locations returns the marker locations stored in the NI-RFSG session for the channel you specified in the channel name parameter. This value is expressed in samples. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Marker Event

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-initialize-external-calibration-vi.html language=enus -->
## TOPIC 00029: niRFSG Initialize External Calibration VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-initialize-external-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-initialize-external-calibration-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates and initializes an NI-RFSG external calibration session. Supported Devices: PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654, PXIe-5673/5673E, PXIe-5696 icon Inputs/Outputs civrn.png resource name resource name specifies the resource name of the device to initialize. cstr.png password pass

### niRFSG Initialize External Calibration VI

Creates and initializes an NI-RFSG external calibration session.

**Supported Devices**: PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654, PXIe-5673/5673E, PXIe-5696

[IMAGE alt='icon' src='nirfsg-initialize-external-calibration-vi.png']

#### Inputs/Outputs

| resource name — resource name specifies the resource name of the device to initialize. password — password specifies the calibration password required to open an external calibration session to the device. Refer to the calibration procedure for your device for more information about the default password. option string — option string sets the initial value of certain properties for the session. You can set the following properties using this parameter: Range Check Query Instrument Status Cache Coercions Simulate Driver Setup error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle — instrument handle passes a reference to your instrument session to the next VI. instrument handle is obtained from this VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-load-configurations-from-file-vi.html language=enus -->
## TOPIC 00030: niRFSG Load Configurations From File VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-load-configurations-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-load-configurations-from-file-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the configurations from the specified file to the NI-RFSG driver session. The VI does an implicit reset before loading the configurations from the file. Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs civrn.png instrument handle instrument handle identifies

### niRFSG Load Configurations From File VI

Loads the configurations from the specified file to the NI-RFSG driver session. The VI does an implicit reset before loading the configurations from the file.

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-load-configurations-from-file-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. channel name — channel name specifies the name of the channel. This string is case-insensitive and alphanumeric, and it cannot use reserved words. file path — file path specifies the absolute path of the file from which the NI-RFSG loads the configurations. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-p.html language=enus -->
## TOPIC 00031: niRFSG Properties

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-p.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-p.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the niRFSG Property Node to get (read) or set (write) NI-RFSG properties. When you read a property, NI-RFSG analyzes the current configuration to return the coerced value for that property. NI-RFSG verifies many properties upon reading, thereby either transitioning the session to the verified st

### niRFSG Properties

Use the niRFSG Property Node to get (read) or set (write) NI-RFSG properties. When you read a property, NI-RFSG analyzes the current configuration to return the coerced value for that property. NI-RFSG verifies many properties upon reading, thereby either transitioning the session to the verified state or alerting you of an invalid configuration. Setting a property transitions the session to an unverified state.

© 2004–2025 National Instruments Corporation. All rights reserved.

- [Active Channel](../../instr-lib/nirfsg/pnirfsg-activechannel.html) Specifies the channel name used to access all subsequent channel-based properties in this property node. Set the channel before setting channel-based properties.
- [Arb:Advanced:Compensate for Filter Group Delay](../../instr-lib/nirfsg/pnirfsg-compensateforfiltergroupdelay.html) Enables or disables compensation for filter group delay on the AWG module. This property also accounts for the upconverter group delay and aligns the RF output with the Started Event, Done Event, and Marker Events.
- [Arb:Advanced:Digital Gain (dB)](../../instr-lib/nirfsg/pnirfsg-digitalgain-db.html) Specifies the digital gain, in decibels. The digital gain is applied to the waveform data after filtering. Use this property to adjust the output power of the device while keeping the analog path fixed. This may cause clipping, overflows, or quantization noise if used improperly.
- [Arb:Advanced:Overflow Error Reporting](../../instr-lib/nirfsg/pnirfsg-overflowerrorreporting.html) Configures error reporting for onboard signal processing (OSP) overflows. Overflows lead to clipping of the waveform.
- [Arb:Arb Carrier Frequency (Hz)](../../instr-lib/nirfsg/pnirfsg-carrierfrequency-hz.html) Indicates the carrier frequency generated by the AWG module.
- [Arb:Arb Power (dBm)](../../instr-lib/nirfsg/pnirfsg-power-dbm.html) Indicates the average output power from the PXI-5421, PXI-5441, PXIe-5442, and PXIe-5450 AWG modules. If an arbitrary waveform is being generated, this property specifies either the average power or the peak power of the signal, depending on the Power Level Type property setting.
- [Arb:Data Transfer:Advanced:Host DMA Buffer Size](../../instr-lib/nirfsg/pnirfsg-hostdmabuffersize.html) Specifies the size of the DMA buffer in computer memory, in bytes. To set this property, the NI-RFSG device must be in the Configuration state.
- [Arb:Data Transfer:Advanced:Maximum In-Flight Read Requests](../../instr-lib/nirfsg/pnirfsg-maximumin-flightreadrequests.html) Specifies the maximum number of concurrent PCI Express read requests the RF signal generator can issue.
- [Arb:Data Transfer:Advanced:Preferred Packet Size](../../instr-lib/nirfsg/pnirfsg-preferredpacketsize.html) Specifies the preferred size of the data field in a PCI Express read request packet.
- [Arb:Data Transfer:Data Transfer Block Size](../../instr-lib/nirfsg/pnirfsg-datatransferblocksize.html) Indicates the number of samples at a time to download to onboard memory. This property is useful when the total data to be transferred to onboard memory is large.
- [Arb:Data Transfer:Direct Download](../../instr-lib/nirfsg/pnirfsg-directdownload.html) Specifies whether the niRFSG Write Arb Waveform VI immediately writes waveforms to the device or copies the waveform to host memory for later download. NI-RFSG reads and validates this property when an arbitrary waveform is first allocated.
- [Arb:Data Transfer:Maximum Bandwidth](../../instr-lib/nirfsg/pnirfsg-maximumbandwidth.html) Specifies the maximum amount of bus bandwidth to use for data transfers.
- [Arb:Data Transfer:Streaming:Space Available In Streaming Waveform (Samples)](../../instr-lib/nirfsg/pnirfsg-spaceavailinstreamingwfm.html) Indicates the space available, in samples, in the streaming waveform for writing new data. For optimal performance, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform. This waveform size ensures that writes do not have to wrap around from the end to the beginning of the waveform buffer.
- [Arb:Data Transfer:Streaming:Streaming Enabled](../../instr-lib/nirfsg/pnirfsg-streamingenabled.html) Enables or disables continuous streaming of waveform data.
- [Arb:Data Transfer:Streaming:Streaming Waveform Name](../../instr-lib/nirfsg/pnirfsg-streamingwaveformname.html) Specifies the name of the waveform used to continuously stream data during generation.
- [Arb:Data Transfer:Streaming:Streaming Write Timeout](../../instr-lib/nirfsg/pnirfsg-streamingwritetimeout.html) Indicates the maximum amount of time allowed to complete a streaming write operation.
- [Arb:Device Instantaneous Bandwidth (Hz)](../../instr-lib/nirfsg/pnirfsg-deviceinstantaneousbandwidth.html) Specifies the instantaneous bandwidth of the device. The instantaneous bandwidth is the effective real-time bandwidth of the signal path for your configuration.
- [Arb:Digital Equalization Enabled](../../instr-lib/nirfsg/pnirfsg-digitalequalizationenabled.html) When this property is enabled, NI-RFSG equalizes the waveform data to correct for variations in the response of the NI-RFSG device. Enabling digital equalization improves the modulation error ratio (MER) and error vector magnitude (EVM) for signals with large bandwidths (>500 kHz), but it increases tuning times.
- [Arb:Digital Pattern](../../instr-lib/nirfsg/pnirfsg-digitalpattern.html) Enables or disables digital pattern on the PXI-5421/5441 AWG module. This property must be set to TRUE to enable signal routing to and from the Digital Data & Control connector.
- [Arb:Generation Mode](../../instr-lib/nirfsg/pnirfsg-generationmode.html) Specifies whether to generate a continuous wave (CW) signal, the arbitrary waveform specified by the Selected Waveform property, or the script specified by the Selected Script property, upon calling the niRFSG Initiate VI.
- [Arb:IQ Rate (S/s)](../../instr-lib/nirfsg/pnirfsg-iqrate-ss.html) This property specifies the I/Q rate of the arbitrary waveform. The I/Q rate is coerced to a value the hardware can achieve. Read this value back after setting it to see the actual I/Q rate. NI-RFSG internally uses an FIR filter with flat response up to (0.4 Ã— IQ rate). Given a desired signal with the maximum frequency content f , sample the signal at an I/Q rate greater than or equal to ( f /0.4).
- [Arb:IQ Swap Enabled](../../instr-lib/nirfsg/pnirfsg-iqswapenabled.html) Enables or disables the inverse phase rotation of the I/Q signal by swapping the I and Q inputs.
- [Arb:Memory Size](../../instr-lib/nirfsg/pnirfsg-memorysize.html) The total amount of memory on the RF signal generator in bytes.
- [Arb:Phase Continuity Enabled](../../instr-lib/nirfsg/pnirfsg-phasecontinuityenabled.html) Specifies whether the driver maintains phase continuity in the arbitrary waveforms. When this property is set to Enable, NI-RFSG may increase the waveform size, and the Frequency Tolerance (Hz) property specifies the maximum allowable frequency error that can be introduced when keeping the signal phase-continuous. To set the Phase Continuity Enabled property, the NI-RFSG device must be in the Configuration state. This property only applies when the Generation Mode property is set to Arb Waveform or Script.
- [Arb:Pre-filter Gain (dB)](../../instr-lib/nirfsg/pnirfsg-pre-filtergain-db.html) Specifies the AWG prefilter gain. The prefilter gain is applied to the waveform data before any other signal processing. Reduce this value to prevent overflow in the AWG interpolation filters. Other gains on the NI-RFSG device are automatically adjusted to compensate for nonunity AWG prefilter gain. The PXI-5671, PXIe-5672, and PXIe-5860 must be in the Configuration state to use this property. However, the PXIe-5644/5645/5646, PXIe-5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842 can be in either the Configuration or the Generation state to use this property.
- [Arb:Pulse Shaping:Filter Type](../../instr-lib/nirfsg/pnirfsg-filtertype.html) Specifies the pulse-shaping filter type for the FIR filter. You can use this property only with signal generators that support onboard signal processing (OSP). NI-RFSG returns an error if you use this property with a device that does not support OSP.
- [Arb:Pulse Shaping:Raised Cosine Alpha](../../instr-lib/nirfsg/pnirfsg-raisedcosinefilteralpha.html) Specifies the alpha value to use when calculating the pulse-shaping FIR filter coefficients. You can use this property only when the Filter Type property is set to Raised Cosine and with signal generators that support onboard signal processing (OSP). NI-RFSG returns an error if you use this property with a device that does not support OSP.
- [Arb:Pulse Shaping:Root Raised Cosine Alpha](../../instr-lib/nirfsg/pnirfsg-rootraisedcosinefilteralpha.html) Specifies the alpha value to use when calculating the pulse-shaping FIR filter coefficients. You can use this property only when the Filter Type property is set to Root Raised Cosine and with signal generators that support onboard signal processing (OSP). NI-RFSG returns an error if you use this property with a device that does not support OSP.
- [Arb:Selected Script](../../instr-lib/nirfsg/pnirfsg-selectedscript.html) Specifies the script in onboard memory to generate upon calling the niRFSG Initiate VI when the Generation Mode property is set to Script. The Selected Script property is ignored when the Generation Mode property is set to Arb Waveform or CW.
- [Arb:Signal Bandwidth (Hz)](../../instr-lib/nirfsg/pnirfsg-signalbandwidth-hz.html) Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8 Ã— I/Q rate).
- [Arb:Software Scaling Factor](../../instr-lib/nirfsg/pnirfsg-softwarescalingfactor.html) Specifies how much to scale the data before writing it with the niRFSG Write Arb Waveform VI. The resulting waveform must be smaller than 1.0 in complex magnitude. This property is supported only if you set the Power Level Type property to Peak Power.
- [Arb:Waveform Attributes:Waveform IQ Rate (S/s)](../../instr-lib/nirfsg/pnirfsg-waveformiqrate.html) Specifies the I/Q rate of the waveform. To set this property, the NI-RFSG device must be in the Configuration state.
- [Arb:Waveform Attributes:Waveform PAPR (dB)](../../instr-lib/nirfsg/pnirfsg-waveformpapr.html) Specifies the peak-to-average power ratio (PAPR).
- [Arb:Waveform Attributes:Waveform RF Blanking](../../instr-lib/nirfsg/pnirfsg-rfblanking.html) Enables or disables RF blanking.
- [Arb:Waveform Attributes:Waveform Runtime Scaling](../../instr-lib/nirfsg/pnirfsg-waveformruntimescaling.html) Specifies the waveform runtime scaling. The waveform runtime scaling is applied to the waveform data before any other signal processing.
- [Arb:Waveform Attributes:Waveform Signal Bandwidth (Hz)](../../instr-lib/nirfsg/pnirfsg-waveformsignalbandwidth-hz.html) Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8 Ã— I/Q rate ).
- [Arb:Waveform Attributes:Waveform Size](../../instr-lib/nirfsg/pnirfsg-waveformsize.html) Specifies the size of the waveform specified by active channel
- [Arb:Waveform Capabilities:Max Number Waveforms](../../instr-lib/nirfsg/pnirfsg-maxnumberwaveforms.html) Specifies the maximum number of waveforms the NI-RFSG device can hold in memory.
- [Arb:Waveform Capabilities:Max Waveform Size](../../instr-lib/nirfsg/pnirfsg-maxwaveformsize.html) Specifies the size of the largest waveform that is allowed.
- [Arb:Waveform Capabilities:Min Waveform Size](../../instr-lib/nirfsg/pnirfsg-minwaveformsize.html) Specifies the smallest allowable waveform size.
- [Arb:Waveform Capabilities:Selected Waveform](../../instr-lib/nirfsg/pnirfsg-selectedwaveform.html) Specifies the waveform in onboard memory to generate upon calling the niRFSG Initiate VI when the Generation Mode property is set to Arb Waveform. The Selected Waveform property is ignored when the Generation Mode property is set to Script or CW. To set the Selected Waveform property, the NI-RFSG device must be in the Configuration state.
- [Arb:Waveform Capabilities:Waveform Quantum](../../instr-lib/nirfsg/pnirfsg-waveformquantum.html) Returns the waveform quantum for the device. The number of samples in a waveform must be an integer multiple of the waveform quantum. The other restrictions on the length of the waveform are the minimum and maximum arbitrary waveform sizes.
- [Arb:Waveform Repeat Count](../../instr-lib/nirfsg/pnirfsg-arbwaveformrepeatcount.html) Specifies the repeat count of a waveform when you set the Waveform Repeat Count Is Finite property to TRUE. This property is valid only when you set the Generation Mode property to Arb Waveform . To set this property, the NI-RFSG device must be in the Configuration state.
- [Arb:Waveform Repeat Count Is Finite](../../instr-lib/nirfsg/pnirfsg-arbwaveformrepeatcountisfinite.html) Specifies the repetition mode of a waveform when you set the Generation Mode property to Arb Waveform . If you set this property to TRUE, the number of repetitions is determined by the Waveform Repeat Count property. To set this property, the NI-RFSG device must be in the Configuration state.
- [Arb:Write Waveform Burst Detection:Enabled](../../instr-lib/nirfsg/pnirfsg-writewaveformburstdetection.html) Enables the detection of burst start and burst stop locations in the waveform. Set this property to Enable before writing a waveform to NI-RFSG memory for detecting bursts. You can read the detected burst start and burst stop locations using niRFSG Get Waveform Burst Start Locations and niRFSG Get Waveform Burst Stop Locations VIs respectively.
- [Arb:Write Waveform Burst Detection:Mode](../../instr-lib/nirfsg/pnirfsg-writewaveformburstdetectionmode.html) Specifies the algorithm that NI-RFSG uses to detect the burst start and burst stop locations in the waveform when burst detection is enabled using the Write Waveform Burst Detection property. When you set Write Waveform Burst Detection Mode to Auto , NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform. To fine-tune the burst detection process parameters yourself, you can set this property to Manual and specify the burst detection parameters using the Minimum Quiet Time , Power Threshold , and Minimum Burst Time properties.
- [Arb:Write Waveform Burst Detection:Power Threshold](../../instr-lib/nirfsg/pnirfsg-powerthreshold.html) Specifies the relative power level at which burst start or stop locations are detected. The threshold is relative to the peak power in the waveform. NI-RFSG detects burst start (or burst stop) locations when the signal exceeds (or falls below) the level specified by this property. This property is ignored when you disable the Write Waveform Burst Detection property or when you set the Write Waveform Burst Detection Mode property to Auto .
- [Arb:Write Waveform Normalization](../../instr-lib/nirfsg/pnirfsg-writewaveformnormalization.html) Specifies whether to perform the normalization on a waveform.
- [Clock:Advanced:Arb Oscillator Phase DAC Value](../../instr-lib/nirfsg/pnirfsg-oscillatorphasevalue.html) Specifies the oscillator phase digital-to-analog converter (DAC) value on the arbitrary waveform generator (AWG). Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing a previous measurement's phase DAC value to the current session. This property is applicable only when the Arb Sample Clock Source property is set to ClkIn.
- [Clock:Arb Onboard Sample Clock Mode](../../instr-lib/nirfsg/pnirfsg-arbonboardsampleclockmode.html) Specifies the Sample Clock mode on the device. To set this property, the NI-RFSG device must be in the Configuration state.
- [Clock:Arb Sample Clock Rate (Hz)](../../instr-lib/nirfsg/pnirfsg-arbsampleclockrate-hz.html) Returns the rate of the Sample Clock on the device.
- [Clock:Arb Sample Clock Source](../../instr-lib/nirfsg/pnirfsg-arbsampleclocksource.html) Specifies the Sample Clock source for the device. To set this property, the NI-RFSG device must be in the Configuration state.
- [Clock:PXI Chassis Clk 10 Source](../../instr-lib/nirfsg/pnirfsg-pxichassisclk10source.html) Specifies the clock source for driving the PXI 10 MHz backplane Reference Clock. This property is configurable if the PXI-5610 upconverter module is installed in only Slot 2 of a PXI chassis. To set this property, the NI-RFSG device must be in the Configuration state.
- [Clock:Reference Clock Export Output Terminal](../../instr-lib/nirfsg/pnirfsg-referenceclockexportoutputterminal.html) Specifies the destination terminal for exporting the Reference Clock on the RF signal generators. To set this property, the NI-RFSG device must be in the Configuration state.
- [Clock:Reference Clock Exported Rate (Hz)](../../instr-lib/nirfsg/pnirfsg-referenceclockexportedrate-hz.html) Specifies the Reference Clock Rate, in Hz, of the signal sent to the Reference Clock Export Output Terminal . To set this attribute, the NI-RFSG device must be in the Configuration state.
- [Clock:Reference Clock Rate (Hz)](../../instr-lib/nirfsg/pnirfsg-referenceclockrate-hz.html) Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector. This property is only valid when the Reference Clock Source property is set to ClkIn , or RefIn .
- [Clock:Reference Clock Source](../../instr-lib/nirfsg/pnirfsg-referenceclocksource.html) Specifies the Reference Clock source. To set this property, the NI-RFSG device must be in the Configuration state.
- [Configuration List:Active List](../../instr-lib/nirfsg/pnirfsg-activeconfigurationlist.html) Specifies the name of the configuration list to make active. When a property is get or set and that property is in the configuration list properties of the active list, the property is set to or get from the active list step of the active list. If the Active Configuration List property is set to "" (empty string), no list is active.
- [Configuration List:Active Step](../../instr-lib/nirfsg/pnirfsg-activeconfigurationliststep.html) Specifies the active step of the list defined by the Active Configuration List property.
- [Configuration List:Configuration List Is Done](../../instr-lib/nirfsg/pnirfsg-configurationlistisdone.html) Returns whether the configuration list is still running or done. To read this property, the device must be in the Generation state.
- [Configuration List:Configuration List Repeat](../../instr-lib/nirfsg/pnirfsg-configurationlistrepeat.html) Specifies whether the configuration list runs only once or continuously.
- [Configuration List:Step In Progress](../../instr-lib/nirfsg/pnirfsg-configurationliststepinprogress.html) Returns the configuration list step that is currently programmed to the hardware. The list is zero-indexed. You can query this property only when a list is executed.
- [De-embedding:Compensation Gain](../../instr-lib/nirfsg/pnirfsg-deembeddingcompensationgain.html) Returns the de-embedding gain applied to compensate for the mismatch on the specified port. Use the Active Channel property to specify the name of the port to configure for de-embedding.
- [De-embedding:Selected Table](../../instr-lib/nirfsg/pnirfsg-deembeddingselectedtable.html) Selects the de-embedding table to apply to the generations on the specified port. Use the Active Channel property to specify the name of the port to configure for de-embedding.
- [De-embedding:Type](../../instr-lib/nirfsg/pnirfsg-deembeddingtype.html) Specifies the type of de-embedding to apply to generations on the specified port. Use the Active Channel property to specify the name of the port to configure for de-embedding.
- [Device Characteristics:AE Temperature (Degrees C)](../../instr-lib/nirfsg/pnirfsg-aetemperature-degreesc.html) Returns the amplitude extender module temperature in degrees Celsius.
- [Device Characteristics:AWG Temperature (Degrees C)](../../instr-lib/nirfsg/pnirfsg-awgtemperature-degreesc.html) Returns the AWG module temperature in degrees Celsius.
- [Device Characteristics:Device Temperature (Degrees C)](../../instr-lib/nirfsg/pnirfsg-devicetemperature-degreesc.html) Returns the device temperature. If the NI-RFSG session is controlling multiple devices, this property returns the temperature of the primary RF device. The NI-RFSG session is opened using the primary RF device name.
- [Device Characteristics:FPGA Target Name](../../instr-lib/nirfsg/pnirfsg-fpgatargetname.html) Returns a string containing the name of the FPGA target being used. This name can be used with the RIO open session to open a reference to the FPGA.
- [Device Characteristics:FPGA Temperature (Degrees C)](../../instr-lib/nirfsg/pnirfsg-fpgatemperature-degreesc.html) Returns the FPGA temperature in degrees Celsius.
- [Device Characteristics:LO Temperature (Degrees C)](../../instr-lib/nirfsg/pnirfsg-lotemperature-degreesc.html) Returns the LO module temperature in degrees Celsius.
- [Device Characteristics:Module Power Consumption (W)](../../instr-lib/nirfsg/pnirfsg-modulepowerconsumption.html) Returns the total power consumption of the device, in watts.
- [Device Characteristics:Module Revision](../../instr-lib/nirfsg/pnirfsg-modulerevision.html) Returns the module revision letter. If the NI-RFSG session is controlling multiple modules, this property returns the revision letter of the primary RF module. The NI-RFSG session is opened using the primary RF module name.
- [Device Characteristics:Options:Fast Tuning Option](../../instr-lib/nirfsg/pnirfsg-fasttuning.html) Returns whether the RF signal generator has the fast tuning option available.
- [Device Characteristics:Serial Number](../../instr-lib/nirfsg/pnirfsg-serialnumber.html) Returns the serial number of the RF module. If the NI-RFSG session is controlling multiple modules, this property returns the serial number of the primary RF module.
- [Device Characteristics:Temperature Read Interval](../../instr-lib/nirfsg/pnirfsg-temperaturereadinterval.html) Specifies the minimum time, in seconds, between temperature sensor readings.
- [Device Specific:Vector Signal Transceiver:Device Characteristics:FPGA Bitfile Path](../../instr-lib/nirfsg/pnirfsg-fpgabitfilepath.html) Returns a string containing the path to the location of the current NI-RFSG instrument driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device. You can specify the bitfile location using the Driver Setup string in the options string input of the niRFSG Initialize With Options VI.
- [Device Specific:Vector Signal Transceiver:Events:Events Delay](../../instr-lib/nirfsg/pnirfsg-eventsdelay.html) Specifies the delay, in seconds, applied to the Started Event, Done Event, and all Marker Events with respect to the analog output of the RF signal generator. To set this property, the NI-RFSG device must be in the Configuration or Generation state.
- [Device Specific:Vector Signal Transceiver:IQ Out Port:Carrier Frequency](../../instr-lib/nirfsg/pnirfsg-iqoutportcarrierfrequency.html) Specifies the frequency, in Hz, of the I/Q OUT port signal. The onboard signal processing (OSP) applies the specified frequency shift to the I/Q data before the data is sent to the digital-to-analog converter (DAC). To set this property, the NI-RFSG device must be in the Configuration state.
- [Device Specific:Vector Signal Transceiver:IQ Out Port:Common Mode Offset](../../instr-lib/nirfsg/pnirfsg-iqoutportcommonmodeoffset.html) Specifies the common-mode offset, in volts, applied to the signals generated at each differential output terminal. This property is valid only when you set the IQ Out Port Terminal Configuration property to Differential . Common-mode offset shifts both positive and negative terminals in the same direction.
- [Device Specific:Vector Signal Transceiver:IQ Out Port:Level](../../instr-lib/nirfsg/pnirfsg-iqoutportlevel.html) Specifies the amplitude of the generated signal in volts, peak-to-peak (V pk-pk ). For example, if you set this property to 1.0, the output signal ranges from -0.5 volts to 0.5 volts.
- [Device Specific:Vector Signal Transceiver:IQ Out Port:Load Impedance](../../instr-lib/nirfsg/pnirfsg-iqoutportloadimpedance.html) Specifies the load impedance, in ohms, connected to the I/Q OUT port. To set this property, the NI-RFSG device must be in the Configuration state.
- [Device Specific:Vector Signal Transceiver:IQ Out Port:Offset](../../instr-lib/nirfsg/pnirfsg-iqoutportoffset.html) Specifies the value, in volts, that the signal generator adds to the I and Q signals. To set this property, the NI-RFSG device must be in the Configuration state.
- [Device Specific:Vector Signal Transceiver:IQ Out Port:Temperature (Degrees C)](../../instr-lib/nirfsg/pnirfsg-iqoutporttemperature-degreesc.html) Returns the temperature, in degrees Celsius, of the I/Q Out circuitry on the device.
- [Device Specific:Vector Signal Transceiver:IQ Out Port:Terminal Configuration](../../instr-lib/nirfsg/pnirfsg-iqoutporttermcfg.html) Specifies whether to use the I/Q OUT port for Differential configuration or Single-Ended configuration. If you set this property to Single-Ended , you must terminate the negative I and Q output connectors with a 50 Ohm termination.
- [Device Specific:Vector Signal Transceiver:Signal Path:Absolute Delay](../../instr-lib/nirfsg/pnirfsg-absolutedelay.html) Specifies the sub-Sample Clock delay, in seconds, to apply to the I/Q waveform. Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurement to the current session.
- [Device Specific:Vector Signal Transceiver:Signal Path:Available Paths:Available Paths](../../instr-lib/nirfsg/pnirfsg-availablepaths.html) Returns a comma separated list of the configurable paths available for use based on your instrument configuration.
- [Device Specific:Vector Signal Transceiver:Signal Path:Available Ports](../../instr-lib/nirfsg/pnirfsg-availableports.html) Returns a CSV of the available ports for your hardware configuration.
- [Device Specific:Vector Signal Transceiver:Signal Path:Fixed Group Delay Across Ports](../../instr-lib/nirfsg/pnirfsg-fixedgroupdelayacrossports.html) Specifies a comma-separated list of ports for which to fix the group delay.
- [Device Specific:Vector Signal Transceiver:Signal Path:Interpolation Delay](../../instr-lib/nirfsg/pnirfsg-interpolationdelay.html) Specifies the delay, in seconds, to apply to the I/Q waveform. To set this property, the NI-RFSG device must be in the Configuration state.
- [Device Specific:Vector Signal Transceiver:Signal Path:LO Frequency Step Size (Hz)](../../instr-lib/nirfsg/pnirfsg-lofrequencystepsize-hz.html) Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL).
- [Device Specific:Vector Signal Transceiver:Signal Path:LO PLL Fractional Mode Enabled](../../instr-lib/nirfsg/pnirfsg-lopllfractionalmodeenabled.html) Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL). This property enables or disables fractional frequency tuning in the LO. Fractional mode provides a finer frequency step resolution and allows smaller values for the LO Frequency Step Size property. However, fractional mode may introduce non-harmonic spurs.
- [Device Specific:Vector Signal Transceiver:Signal Path:LO Source](../../instr-lib/nirfsg/pnirfsg-losource.html) Specifies whether to use the internal or external local oscillator (LO) source. If this property is set to "" (empty string), NI-RFSG uses the internal LO source. To set this property, the NI-RFSG device must be in the Configuration state.
- [Device Specific:Vector Signal Transceiver:Signal Path:LO VCO Frequency Step Size (Hz)](../../instr-lib/nirfsg/pnirfsg-lovcofrequencystepsize-hz.html) Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal.
- [Device Specific:Vector Signal Transceiver:Signal Path:Output Port](../../instr-lib/nirfsg/pnirfsg-outputport.html) Specifies the connector(s) to use to generate the signal. To set this property, the NI-RFSG device must be in the Configuration state.
- [Device Specific:Vector Signal Transceiver:Signal Path:RF Blanking Source](../../instr-lib/nirfsg/pnirfsg-rfblankingsource.html) Specifies the Marker Event at which RF blanking occurs. RF blanking quickly attenuates the RF OUT signal. Use Marker Events to toggle the state of RF blanking. The RF Output always starts in the unblanked state.
- [Device Specific:Vector Signal Transceiver:Signal Path:Relative Delay](../../instr-lib/nirfsg/pnirfsg-relativedelay.html) Specifies the delay, in seconds, to apply to the I/Q waveform.
- [Device Specific:Vector Signal Transceiver:Signal Path:Selected Path:Selected Path](../../instr-lib/nirfsg/pnirfsg-selectedpath.html) Specifies which path to configure to generate a signal.
- [Device Specific:Vector Signal Transceiver:Signal Path:Selected Ports](../../instr-lib/nirfsg/pnirfsg-selectedports.html) Specifies the port to configure.
- [Device Specific:Vector Signal Transceiver:Triggers:Sync Sample Clock Dist Line](../../instr-lib/nirfsg/pnirfsg-syncsampleclockdistline.html) Specifies which external trigger line distributes the Sample Clock sync signal. When synchronizing the Sample Clock between multiple devices, configure all devices to use the same Sample Clock sync distribution line.
- [Device Specific:Vector Signal Transceiver:Triggers:Sync Sample Clock Master](../../instr-lib/nirfsg/pnirfsg-syncsampleclockmaster.html) Specifies whether the device is the master device when synchronizing the Sample Clock between multiple devices. The master device distributes the Sample Clock sync signal to all devices in the system through the Sample Clock sync distribution line.
- [Device Specific:Vector Signal Transceiver:Triggers:Sync Script Trigger Dist Line](../../instr-lib/nirfsg/pnirfsg-syncscripttriggerdistline.html) Specifies which external trigger line distributes the synchronized Script Trigger signal. Use the Active Channel property to specify the name of the Script Trigger you are configuring. When synchronizing the Script Trigger, configure all devices to use the same Script Trigger distribution line.
- [Device Specific:Vector Signal Transceiver:Triggers:Sync Script Trigger Master](../../instr-lib/nirfsg/pnirfsg-syncscripttriggermaster.html) Specifies whether the device is the master device when synchronizing the Script Trigger between multiple devices. Use the Active Channel property to specify the name of the Script Trigger you are configuring.
- [Device Specific:Vector Signal Transceiver:Triggers:Sync Start Trigger Dist Line](../../instr-lib/nirfsg/pnirfsg-starttriggerdistline.html) Specifies which external trigger line distributes the synchronized Start Trigger signal. When synchronizing the Start Trigger, configure all devices to use the same Start Trigger distribution line.
- [Device Specific:Vector Signal Transceiver:Triggers:Sync Start Trigger Master](../../instr-lib/nirfsg/pnirfsg-syncstarttriggermaster.html) Specifies whether the device is the master device when synchronizing the Start Trigger between multiple devices. The master device distributes the synchronized Start Trigger to all devices in the system through the Start Trigger distribution line.
- [Device Specific:Vector Signal Transceiver:Upconverter:Frequency Offset (Hz)](../../instr-lib/nirfsg/pnirfsg-upconverterfrequencyoffset-hz.html) This property offsets the Upconverter Center Frequency (Hz) from the RF frequency. Use this property to keep the local oscillator (LO) leakage at a determined offset from the RF signal.
- [Events:Configuration Settled Event Export Output Terminal](../../instr-lib/nirfsg/pnirfsg-configurationsettledevent-exportoutputterm.html) Specifies the destination terminal for exporting the Configuration Settled event. To set this property, the NI-RFSG device must be in the Configuration state.
- [Events:Configuration Settled Event Terminal Name](../../instr-lib/nirfsg/pnirfsg-configurationsettledevent-terminalname.html) Returns the fully qualified signal name as a string.
- [Events:Done Event Export Output Terminal](../../instr-lib/nirfsg/pnirfsg-doneevent-exportoutputterm.html) Specifies the destination terminal for exporting the Done event. To set this property, the NI-RFSG device must be in the Configuration state.
- [Events:Done Event Terminal Name](../../instr-lib/nirfsg/pnirfsg-doneevent-terminalname.html) Returns the fully qualified signal name as a string.
- [Events:Marker:Output Behavior](../../instr-lib/nirfsg/pnirfsg-markerevent-outputbehavior.html) Specifies the output behavior for the Marker Event. To set this property, the NI-RFSG device must be in the Configuration state.
- [Events:Marker:Output Terminal](../../instr-lib/nirfsg/pnirfsg-markerevent-exportoutputterm.html) Specifies the destination terminal for exporting the Marker Event. To set this property, the NI-RFSG device must be in the Configuration state.
- [Events:Marker:Pulse:Width Units](../../instr-lib/nirfsg/pnirfsg-markerevent-pulse-widthunits.html) Specifies the pulse width units for the Marker Event. This property is valid only when the Marker Event Output Behavior property is set to Pulse .
- [Events:Marker:Pulse:Width Value](../../instr-lib/nirfsg/pnirfsg-markerevent-pulse-widthvalue.html) Specifies the pulse width value for the Marker Event. Use the Marker Event Pulse Width Units property to set the units for the pulse width value. This property is valid only when the Marker Event Output Behavior property is set to Pulse .
- [Events:Marker:Terminal Name](../../instr-lib/nirfsg/pnirfsg-markerevent-terminalname.html) Returns the fully qualified signal name as a string.
- [Events:Marker:Toggle:Initial State](../../instr-lib/nirfsg/pnirfsg-markerevent-toggle-initialstate.html) Specifies the initial state for the Marker Event when the Marker Event Output Behavior property is set to Toggle .
- [Events:Pulse Modulation:Exported Pulse Modulation Event Active Level](../../instr-lib/nirfsg/pnirfsg-exportedpulsemodulationeventactivelevel.html) Specifies the active level of the exported Pulse Modulation Event. When `NIRFSG_ATTR_PULSE_MODULATION_ENABLED` is Enabled, `NIRFSG_ATTR_PULSE_MODULATION_ACTIVE_LEVEL` is `NIRFSG_VAL_ACTIVE_HIGH`, `NIRFSG_ATTR_EXPORTED_PULSE_MODULATION_EVENT_OUTPUT_TERMINAL` is `PulseOut`, and this property is `NIRFSG_VAL_ACTIVE_HIGH`, then the Pulse Modulation Event will transition from Low to High after the the Pulse In signal is set to logic high, and the RF Output has settled. To set this property, the NI-RFSG device must be in the Configuration state.
- [Events:Pulse Modulation:Exported Pulse Modulation Event Output Terminal](../../instr-lib/nirfsg/pnirfsg-exportedpulsemodulationeventoutputterminal.html) Specifies the destination terminal for exporting the Pulse Modulation Event. The Pulse Modulation Event tracks the RF Envelope when Pulse Modulation is Enabled. If this property is set to a value other than `NIRFSG_VAL_DO_NOT_EXPORT_STR`, calling NI-RFSG Commit will cause the output terminal to be pulled to the logic level that is the inverse of `NIRFSG_ATTR_EXPORTED_PULSE_MODULATION_EVENT_ACTIVE_LEVEL`. You can tri-state this terminal by setting this property to `NIRFSG_VAL_DO_NOT_EXPORT_STR` or by calling `niRFSG Reset`. To set this property, the NI-RFSG device must be in the Configuration state.
- [Events:Started Event Export Output Terminal](../../instr-lib/nirfsg/pnirfsg-startedevent-exportoutputterm.html) Specifies the destination terminal for exporting the Started Event. To set this property, the NI-RFSG device must be in the Configuration state.
- [Events:Started Event Terminal Name](../../instr-lib/nirfsg/pnirfsg-startedevent-terminalname.html) Returns the fully qualified signal name as a string.
- [Events:Timer:Interval](../../instr-lib/nirfsg/pnirfsg-timereventinterval.html) Specifies the time, in seconds, before the timer emits an event after the task is started and specifies the time interval between timer events after the first event.
- [External Calibration:Last External Calibration Temperature](../../instr-lib/nirfsg/pnirfsg-lastextcaltemp.html) Indicates the temperature, in degrees Celsius, of the device at the time of the last external calibration.
- [External Calibration:Recommended Interval](../../instr-lib/nirfsg/pnirfsg-recommendedinterval.html) Indicates, in months, the recommended interval between each external calibration of the device.
- [IQ Impairment:Enabled](../../instr-lib/nirfsg/pnirfsg-impairmentenabled.html) Enables or disables I/Q impairment. The I Offset , Q Offset , and IQ Skew properties are ignored when the Impairment Enabled property is disabled.
- [IQ Impairment:Gain Imbalance (dB)](../../instr-lib/nirfsg/pnirfsg-gainimbalance-db.html) Specifies the gain imbalance of the I/Q modulator (I versus Q).
- [IQ Impairment:I Offset](../../instr-lib/nirfsg/pnirfsg-ioffset.html) When using an NI AWG module or vector signal transceiver (VST) device, this property specifies the I-signal DC offset. Units are either percent (%) or volts (V), depending on the Offset Units property setting.
- [IQ Impairment:IQ Skew (Degrees)](../../instr-lib/nirfsg/pnirfsg-iqskew-degrees.html) Specifies the adjustment of the phase angle between the I and Q vectors. If this skew is zero, the phase angle is 90 degrees.
- [IQ Impairment:Offset Units](../../instr-lib/nirfsg/pnirfsg-offsetunits.html) Specifies the units of the I Offset property and the Q Offset property. Offset units are either percent (%) or volts (V).
- [IQ Impairment:Q Offset](../../instr-lib/nirfsg/pnirfsg-qoffset.html) When using a NI AWG module or VST device, this property specifies the Q-signal DC offset. Units are either percent (%) or volts (V), depending on the Offset Units property setting.
- [Inherent IVI Attributes:Advanced Session Information:Logical Name](../../instr-lib/nirfsg/pnirfsg-logicalname.html) Returns a string that contains the logical name you specified when opening the current IVI session.
- [Inherent IVI Attributes:Advanced Session Information:Resource Descriptor](../../instr-lib/nirfsg/pnirfsg-resourcedescriptor.html) Returns a string that contains the resource descriptor NI-RFSG uses to identify the physical device. If you initialize NI-RFSG with a logical name, this property contains the resource name that corresponds to the entry in the IVI Configuration Utility. If you initialize NI-RFSG with the resource name, this property contains that value.
- [Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities](../../instr-lib/nirfsg/pnirfsg-classgroupcapabilities.html) Returns a string that contains a comma-separated list of class-extension groups that NI-RFSG implements.
- [Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models](../../instr-lib/nirfsg/pnirfsg-supportedinstrumentmodels.html) Returns a string that contains a model code of the NI-RFSG device. For drivers that support more than one device, this property contains a comma-separated list of supported devices.
- [Inherent IVI Attributes:Driver Identification:Class Specification Major Version](../../instr-lib/nirfsg/pnirfsg-classspecificationmajorversion.html) Returns the major version number of the class specification with which NI-RFSG is compliant.
- [Inherent IVI Attributes:Driver Identification:Class Specification Minor Version](../../instr-lib/nirfsg/pnirfsg-classspecificationminorversion.html) Returns the minor version number of the class specification with which NI-RFSG is compliant.
- [Inherent IVI Attributes:Driver Identification:Description](../../instr-lib/nirfsg/pnirfsg-description.html) Returns a string that contains a brief description of NI-RFSG. This property returns National Instruments RF Signal Generator Instrument Driver .
- [Inherent IVI Attributes:Driver Identification:Driver Prefix](../../instr-lib/nirfsg/pnirfsg-driverprefix.html) Returns a string that contains the prefix for NI-RFSG. The name of each user-callable VI in NI-RFSG starts with this prefix. This property returns niRFSG .
- [Inherent IVI Attributes:Driver Identification:Driver Vendor](../../instr-lib/nirfsg/pnirfsg-drivervendor.html) Returns a string that contains the name of the vendor that supplies NI-RFSG. This property returns National Instruments .
- [Inherent IVI Attributes:Driver Identification:Revision](../../instr-lib/nirfsg/pnirfsg-revision.html) Returns a string that contains additional version information about NI-RFSG. For example, NI-RFSG can return Driver: NI-RFSG 14.5.0, Compiler: MSVC 9.00, Components: IVI Engine 4.00, VISA-Spec 4.00 as the value of this property.
- [Inherent IVI Attributes:Instrument Identification:Firmware Revision](../../instr-lib/nirfsg/pnirfsg-firmwarerevision.html) Returns a string that contains the firmware revision information for the NI-RFSG device you are currently using.
- [Inherent IVI Attributes:Instrument Identification:Manufacturer](../../instr-lib/nirfsg/pnirfsg-manufacturer.html) Returns a string that contains the name of the manufacturer for the NI-RFSG device you are currently using.
- [Inherent IVI Attributes:Instrument Identification:Model](../../instr-lib/nirfsg/pnirfsg-model.html) Returns a string that contains the model number or name of the NI-RFSG device you are currently using.
- [Inherent IVI Attributes:User Options:Cache](../../instr-lib/nirfsg/pnirfsg-cache.html) Specifies whether to cache the value of properties. When caching is enabled, NI-RFSG tracks the current NI-RFSG device settings and avoids sending redundant commands to the device. NI-RFSG can always cache or never cache particular properties, regardless of the setting of this property. Call the niRFSG Initialize With Options VI to override the default value.
- [Inherent IVI Attributes:User Options:Interchange Check](../../instr-lib/nirfsg/pnirfsg-interchangecheck.html) Specifies whether to perform interchangeability checking and retrieve interchangeability warnings.
- [Inherent IVI Attributes:User Options:Query Instrument Status](../../instr-lib/nirfsg/pnirfsg-queryinstrumentstatus.html) Specifies whether the NI-RFSG instrument driver queries the device status after each operation. Querying the device status is useful for debugging. After you validate your program, you can set this property to FALSE to disable status checking and maximize performance. NI-RFSG can choose to ignore status checking for particular properties, regardless of the setting of this property. Call the niRFSG Initialize With Options VI to override the default value.
- [Inherent IVI Attributes:User Options:Range Check](../../instr-lib/nirfsg/pnirfsg-rangecheck.html) Specifies whether to validate property values and VI parameters. Range-checking parameters is very useful for debugging. After you validate your program, you can set this property to FALSE to disable range checking and maximize performance. NI-RFSG can choose to ignore range checking for particular properties, regardless of the setting of this property. Call the niRFSG Initialize With Options VI to override the default value.
- [Inherent IVI Attributes:User Options:Record Value Coercions](../../instr-lib/nirfsg/pnirfsg-recordvaluecoercions.html) Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties.
- [Inherent IVI Attributes:User Options:Simulate](../../instr-lib/nirfsg/pnirfsg-simulate.html) Specifies whether NI-RFSG simulates I/O operations. This property is useful for debugging applications without using hardware. After a session is opened, you cannot change the simulation state. Call the niRFSG Initialize With Options VI to enable simulation.
- [Load Configurations:Load Options](../../instr-lib/nirfsg/pnirfsg-loadoptions.html) Specifies the configurations to skip while loading from a file.
- [Load Configurations:Reset Options](../../instr-lib/nirfsg/pnirfsg-resetoptions.html) Specifies the configurations to skip to reset while loading configurations from a file.
- [Modulation:Analog:AM Sensitivity](../../instr-lib/nirfsg/pnirfsg-anlgmod-amsensitivity.html) Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.
- [Modulation:Analog:FM Band](../../instr-lib/nirfsg/pnirfsg-anlgmod-fmband.html) Specifies the analog modulation frequency modulation (FM) band to use. Wideband FM allows for modulating signals higher than 100 kHz. Narrowband FM allows for modulating lower frequency signals.
- [Modulation:Analog:FM Deviation (Hz)](../../instr-lib/nirfsg/pnirfsg-anlgmod-fmdev-hz.html) Specifies the deviation to use in frequency modulation.
- [Modulation:Analog:FM Narrowband Integrator](../../instr-lib/nirfsg/pnirfsg-anlgmod-fmnarrowbandintegrator.html) Specifies the narrowband frequency modulation (FM) range to apply by sending the signal through an integrator.
- [Modulation:Analog:FM Sensitivity](../../instr-lib/nirfsg/pnirfsg-anlgmod-fmsensitivity.html) Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.
- [Modulation:Analog:Modulation Type](../../instr-lib/nirfsg/pnirfsg-anlgmod-type.html) Specifies the analog modulation format to use.
- [Modulation:Analog:PM Deviation (Degrees)](../../instr-lib/nirfsg/pnirfsg-anlgmod-pmdev-degrees.html) Specifies the deviation to use in phase modulation, in degrees.
- [Modulation:Analog:PM Mode](../../instr-lib/nirfsg/pnirfsg-anlgmod-pmmode.html) Specifies the phase modulation (PM) mode to use.
- [Modulation:Analog:PM Sensitivity](../../instr-lib/nirfsg/pnirfsg-anlgmod-pmsensitivity.html) Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.
- [Modulation:Analog:Waveform Frequency (Hz)](../../instr-lib/nirfsg/pnirfsg-anlgmod-wfmfreq-hz.html) Specifies the frequency of the waveform to use as the message signal in analog modulation.
- [Modulation:Analog:Waveform Type](../../instr-lib/nirfsg/pnirfsg-anlgmod-wfmtype.html) Specifies the type of waveform to use as the message signal for analog modulation.
- [Modulation:Digital:FSK Deviation (Hz)](../../instr-lib/nirfsg/pnirfsg-digmod-fskdev-hz.html) Specifies the deviation to use in FSK modulation.
- [Modulation:Digital:Modulation Type](../../instr-lib/nirfsg/pnirfsg-digmod-type.html) Specifies the digital modulation format to use.
- [Modulation:Digital:PRBS Order](../../instr-lib/nirfsg/pnirfsg-digmod-prbsorder.html) Specifies the order of the pseudorandom bit sequence ( PRBS ) internally generated by hardware and used as the message signal in digital modulation.
- [Modulation:Digital:PRBS Seed](../../instr-lib/nirfsg/pnirfsg-digmod-prbsseed.html) Specifies the seed of the internally generated pseudorandom bit sequence (PRBS).
- [Modulation:Digital:Symbol Rate](../../instr-lib/nirfsg/pnirfsg-digmod-symbolrate.html) Specifies the symbol rate of the bit stream for digital modulation.
- [Modulation:Digital:Waveform Type](../../instr-lib/nirfsg/pnirfsg-digmod-wfmtype.html) Specifies the type of waveform to use as the message signal in digital modulation.
- [Modulation:Pulse:Pulse Modulation Active Level](../../instr-lib/nirfsg/pnirfsg-pulsemodulationactivelevel.html) Specifies the active level of the pulse modulation signal when pulse modulation is enabled. To set this property, the NI-RFSG device must be in the Configuration state.
- [Modulation:Pulse:Pulse Modulation Enabled](../../instr-lib/nirfsg/pnirfsg-pulsemodulationenabled.html) Enables or disables pulse modulation.
- [Modulation:Pulse:Pulse Modulation Mode](../../instr-lib/nirfsg/pnirfsg-pulsemodulationmode.html) This property allows you to choose a tradeoff between switching speed and On/Off Ratio when using pulse modulation. Refer to the product specifications document for the switching characteristics of each mode. This property is settable while the device is generating, but some output pulses may be dropped.
- [Modulation:Pulse:Pulse Modulation Source](../../instr-lib/nirfsg/pnirfsg-pulsemodulationsource.html) Specifies the source of the pulse modulation signal. When Pulse In in used, the pulse modulation is applied with the lowest latency and jitter, but is not aligned to any particular waveform sample. When a marker is used, the RF pulse is aligned to a specific sample in the arbitrary waveform. To set this property, the NI-RFSG device must be in the Configuration state.
- [Peer-to-Peer:Data Transfer Permission Initial Credits](../../instr-lib/nirfsg/pnirfsg-datatransferpermissioninitialcredits.html) Specifies the initial amount of data, in samples per channel, that the writer peer is allowed to transfer over the bus into the configured endpoint when the peer-to-peer data stream is enabled. If this property is not set and the endpoint is empty, credits equal to the full size of the endpoint are issued to the writer peer. If data has been written to the endpoint using the niRFSG Write P2P Endpoint (I16) VI prior to enabling the stream, credits equal to the remaining space available in the endpoint are issued to the writer peer. This property is coerced up by NI-RFSG to 8 byte boundaries. This property is endpoint-based.
- [Peer-to-Peer:Data Transfer Permission Interval](../../instr-lib/nirfsg/pnirfsg-datatransferpermissioninterval.html) Specifies the interval, in samples per channel, at which the RF signal generator issues credits to allow the writer peer to transfer data over the bus into the configured endpoint. This property is coerced up by NI-RFSG to the nearest 128 byte boundary. This property is endpoint-based.
- [Peer-to-Peer:Enabled](../../instr-lib/nirfsg/pnirfsg-p2penabled.html) Specifies whether the device reads data from the peer-to-peer endpoint. This property is endpoint-based.
- [Peer-to-Peer:Endpoint Count](../../instr-lib/nirfsg/pnirfsg-p2pendpointcount.html) Returns the number of peer-to-peer FIFO endpoints supported by the device.
- [Peer-to-Peer:Endpoint Size](../../instr-lib/nirfsg/pnirfsg-p2pendpointsize.html) Returns the size, in samples, of the device's endpoint. This property is endpoint-based.
- [Peer-to-Peer:Generation FIFO Sample Quantum](../../instr-lib/nirfsg/pnirfsg-p2pgenerationfifosamplequantum.html) Returns how many samples NI-RFSG pulls from the peer-to-peer FIFO per read. You can use this property to determine how many samples to send across the peer-to-peer bus to ensure that no samples are ignored. If you send a number of samples that is not a multiple of this value, the remaining samples are not read from the FIFO during generation. This property is endpoint-based.
- [Peer-to-Peer:Is Finite Generation](../../instr-lib/nirfsg/pnirfsg-p2pisfinitegeneration.html) Specifies whether peer-to-peer should continuously generate data from the peer-to-peer stream or from only a finite number of samples, according to the Number Of Samples To Generate property. To use this property, peer-to-peer must be enabled. This property is endpoint-based.
- [Peer-to-Peer:Most Space Available in Endpoint](../../instr-lib/nirfsg/pnirfsg-p2pmostspaceavailableinendpoint.html) Returns the largest number of samples per channel available in the endpoint since this property was last read. You can use this property to determine how much endpoint space to use as a buffer against bus traffic latencies by reading the property and keeping track of the largest value returned. This property is endpoint-based.
- [Peer-to-Peer:Number Of Samples To Generate](../../instr-lib/nirfsg/pnirfsg-p2pnumberofsamplestogenerate.html) Specifies how many samples are generated from the peer-to-peer subsystem when it is enabled. To use this property, peer-to-peer must be enabled and set to finite generation. This property is endpoint-based.
- [Peer-to-Peer:Space Available In Endpoint](../../instr-lib/nirfsg/pnirfsg-p2pspaceavailableinendpoint.html) Returns the current space available in the endpoint in samples per channel. You can use this property when priming the endpoint with initial data through the niRFSG Write P2P Endpoint (I16) VI to determine how many samples you can write. You can also use this property to characterize the performance and measure the latency of the peer-to-peer stream as data moves across the bus. This property is endpoint-based.
- [RF:ALC Control](../../instr-lib/nirfsg/pnirfsg-automaticlevelcontrol.html) Enables or disables the automatic leveling control (ALC).
- [RF:Advanced:Amp Path](../../instr-lib/nirfsg/pnirfsg-amppath.html) Specifies the amplification path to use. The low harmonic path provides greater second and third harmonic spurious response, and the high power path provides higher output power.
- [RF:Advanced:Correction Temperature](../../instr-lib/nirfsg/pnirfsg-correctiontemperature.html) Specifies the temperature, in degrees Celsius, to use for adjusting the device settings to correct for temperature changes. If you set this property, NI-RFSG uses the value you specify and therefore no longer uses the actual device temperature as the correction temperature. If you do not set this property, NI-RFSG checks the current device temperature in the Committed state and automatically sets the value of this property.
- [RF:Advanced:Ref PLL Bandwidth](../../instr-lib/nirfsg/pnirfsg-refpllbandwidth.html) Configures the loop bandwidth of the reference PLL.
- [RF:Advanced:Thermal Correction Headroom Range (Degrees C)](../../instr-lib/nirfsg/pnirfsg-thermalcorrectionheadroomrange.html) Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the Device Temperature property.
- [RF:Advanced:Thermal Correction Temperature Resolution (Degrees C)](../../instr-lib/nirfsg/pnirfsg-thermalcorrectiontemperatureresolution.html) Specifies the temperature change, in degrees Celsius, that is required before NI-RFSG recalculates the thermal correction settings when entering the Generation state.
- [RF:Advanced:YIG Main Coil Drive](../../instr-lib/nirfsg/pnirfsg-yigmaincoildrive.html) Adjusts the dynamics of the current driving the YIG main coil.
- [RF:Allow Out Of Specification User Settings](../../instr-lib/nirfsg/pnirfsg-allowoutofspecificationusersettings.html) Enables or disables warnings or errors when you set frequency, power, and bandwidth values beyond the limits of the NI-RFSG device specifications. When you enable this property, the driver does not report out-of-specification warnings or errors.
- [RF:Amplitude Settling](../../instr-lib/nirfsg/pnirfsg-amplitudesettling.html) Configures the amplitude settling accuracy in decibels. NI-RFSG waits until the RF power settles within the specified accuracy level after calling the niRFSG Initiate VI or niRFSG Wait Until Settled VI or prior to advancing to next step if using RF list mode.
- [RF:Attenuator Hold Enabled](../../instr-lib/nirfsg/pnirfsg-attenuatorholdenabled.html) Enables or disables attenuator hold. While this property is set to TRUE, changing the power level causes NI-RFSG to scale the digital data sent to the AWG instead of adjusting the attenuators. Changing power levels in this manner allows the device to increase or decrease the power level in more accurate increments but may affect signal-to-noise ratios (noise density).
- [RF:Attenuator Hold Max Power (dBm)](../../instr-lib/nirfsg/pnirfsg-attenuatorholdmaxpower-dbm.html) Specifies the maximum power level of the RF output signal when the Attenuator Hold Enabled property is set to TRUE.
- [RF:Attenuator Setting (dB)](../../instr-lib/nirfsg/pnirfsg-attenuatorsetting.html) Specifies the level of attenuation in the attenuator path. Setting this property overrides the value chosen by NI-RFSG. Not all power levels are achievable if you set this property.
- [RF:Automatic Power Search](../../instr-lib/nirfsg/pnirfsg-automaticpowersearch.html) Enables or disables automatic power search. When this property is enabled, a power search performs after the device is initiated, after output power is enabled, or when the frequency or power level changes while the device is generating. When this property is disabled, NI-RFSG does not perform a power search unless you call the niRFSG Perform Power Search VI.
- [RF:Automatic Thermal Correction](../../instr-lib/nirfsg/pnirfsg-automaticthermalcorrection.html) Enables or disables automatic thermal correction. When this property is enabled, changes to settings cause NI-RFSG to check whether the device temperature has changed and adjust the settings as needed. When this property is disabled, you must explicitly call the niRFSG Perform Thermal Correction VI to adjust the device for temperature changes.
- [RF:External Gain (dB)](../../instr-lib/nirfsg/pnirfsg-externalgain.html) Specifies the external amplification or attenuation, if any, between the RF signal generator and the device under test.
- [RF:Frequency (Hz)](../../instr-lib/nirfsg/pnirfsg-frequency-hz.html) Specifies the frequency of the generated RF signal. For arbitrary waveform generation, this property specifies the center frequency of the signal.
- [RF:Frequency Settling](../../instr-lib/nirfsg/pnirfsg-frequencysettling.html) Configures the frequency settling time. Interpretation of this value depends on the Frequency Settling Units property.
- [RF:Frequency Settling Units](../../instr-lib/nirfsg/pnirfsg-frequencysettlingunits.html) Determines the interpretation of the value passed to the Frequency Settling property.
- [RF:Frequency Tolerance (Hz)](../../instr-lib/nirfsg/pnirfsg-frequencytolerance-hz.html) Specifies the allowable frequency error introduced during the software upconversion process. NI-RFSG may introduce a frequency error up to the specified amount to optimize computational speed and onboard memory usage while upconverting phase-continuous signals.
- [RF:LO Frequency (Hz)](../../instr-lib/nirfsg/pnirfsg-lofrequency-hz.html) Specifies the frequency of the LO source.
- [RF:LO In Power (dBm)](../../instr-lib/nirfsg/pnirfsg-loinpower-dbm.html) Specifies the power level of the signal at the LO IN front panel connector.
- [RF:LO Out Enabled](../../instr-lib/nirfsg/pnirfsg-looutenabled.html) Specifies whether the local oscillator signal is present at the LO OUT front panel connector. The local oscillator signal remains at the LO OUT front panel connector until this property is set to FALSE even if the Output Enabled property is set to FALSE, the niRFSG Abort VI is called, or the NI-RFSG session is closed.
- [RF:LO Out Export Configure From RFSA](../../instr-lib/nirfsg/pnirfsg-looutexportconfigurefromrfsa.html) Specifies whether to allow NI-RFSA to control the NI-RFSG LO out export.
- [RF:LO Out Power (dBm)](../../instr-lib/nirfsg/pnirfsg-looutpower-dbm.html) Specifies the power level of the signal at the LO OUT front panel connector.
- [RF:Loop Bandwidth](../../instr-lib/nirfsg/pnirfsg-upconverterloopbandwidth.html) Configures the loop bandwidth of the tuning PLLs. This property is ignored on the PXI-5610, PXI-5670/5671, and PXIe-5672 for signal bandwidths greater than or equal to 10 MHz. This property is ignored on the PXI/PXIe-5650/5651/5652 for RF frequencies less than 50 MHz.
- [RF:Output Enabled](../../instr-lib/nirfsg/pnirfsg-outputenabled.html) Enables or disables signal output. Setting the Output Enabled property to FALSE while in the Generation state stops signal output although generation continues internally. For the PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653, PXI-5670/5671, and PXIe-5672/5673/5673E, setting the Output Enabled property while in the Committed state does not transition the device to the Configuration state, but output changes immediately.
- [RF:Peak Envelope Power (dBm)](../../instr-lib/nirfsg/pnirfsg-peakenvelopepower-dbm.html) Specifies the maximum instantaneous power of the RF output signal.
- [RF:Peak Power Adjustment (dB)](../../instr-lib/nirfsg/pnirfsg-peakpoweradjustment-db.html) Adjusts the Power Level (dBm) property. This property is valid only when you set the Power Level Type property to Peak Power . The value of the Peak Power Adjustment (dB) property adds to the Power Level (dBm) property. The Peak Power Adjustment (dB) property typically specifies the peak-to-average power ratio (PAPR) of a waveform. If the PAPR is specified, the specified power level becomes the average power level of the waveform, even if the Power Level Type property is set to Peak Power.
- [RF:Peak Power Adjustment Inheritance](../../instr-lib/nirfsg/pnirfsg-ppainheritancebehavior.html) Determines the inheritance behavior of the Peak Power Adjustment property when a script inherits values from specified waveforms.
- [RF:Phase Offset (Degrees)](../../instr-lib/nirfsg/pnirfsg-phaseoffset-degrees.html) Changes the phase of the RF output signal. Use this property to align the phase of the RF output with the phase of the RF output of another device as long as the two devices are phase-coherent.
- [RF:Power Level (dBm)](../../instr-lib/nirfsg/pnirfsg-powerlevel-dbm.html) Specifies either the average power level or peak power level of the generated RF signal, depending on the Power Level Type property setting.
- [RF:Power Level Type](../../instr-lib/nirfsg/pnirfsg-powerleveltype.html) Specifies the way the driver interprets the value of the Power Level property. The Power Level Type property also affects how waveforms are scaled.
- [RF:RF In LO Export Enabled](../../instr-lib/nirfsg/pnirfsg-rfinloexportenabled.html) Specifies whether to enable the RF IN LO OUT terminal on the PXIe-5840/5841.
- [RF:Upconverter:Center Frequency (Hz)](../../instr-lib/nirfsg/pnirfsg-upconvertercenterfrequency-hz.html) Indicates the center frequency of the passband containing the upconverted RF signal. Writing a value to this property while using the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, or PXIe-5820/5840/5841/5842 enables in-band retuning. In-band retuning increases the speed of frequency sweeps by reducing the amount of upconverter retunes.
- [RF:Upconverter:Frequency Offset Mode](../../instr-lib/nirfsg/pnirfsg-upconverterfrequencyoffsetmode.html) Specifies whether to allow NI-RFSG to select the upconverter frequency offset. You can either set an offset yourself or let NI-RFSG select one for you.
- [RF:Upconverter:Gain (dB)](../../instr-lib/nirfsg/pnirfsg-upconvertergain-db.html) Indicates the gain that the upconverter applies to the signal.
- [Self Calibration:Last Self Calibration Temperature](../../instr-lib/nirfsg/pnirfsg-lastselfcaltemp.html) Indicates, in degrees Celsius, the temperature of the device at the time of the last self calibration.
- [Triggers:Configuration List Step:Digital Edge:Edge](../../instr-lib/nirfsg/pnirfsg-configlisttrig-digedge-edge.html) Specifies the active edge for the Configuration List Step Trigger. This property is valid only when the Configuration List Step Trigger Type property is set to Digital Edge. To set this property, the NI-RFSG device must be in the Configuration state.
- [Triggers:Configuration List Step:Digital Edge:Source](../../instr-lib/nirfsg/pnirfsg-configlisttrig-digedge-source.html) Specifies the source terminal for the Configuration List Step Trigger. This property is valid only when the Configuration List Step Trigger Type property is set to Digital Edge.
- [Triggers:Configuration List Step:Export Output Terminal](../../instr-lib/nirfsg/pnirfsg-configlisttrig-exportoutputterm.html) Specifies the destination terminal for exporting the Configuration List Step Trigger. To set this property, the NI-RFSG device must be in the Configuration state.
- [Triggers:Configuration List Step:Terminal Name](../../instr-lib/nirfsg/pnirfsg-configlisttrig-terminalname.html) Returns the fully qualified signal name as a string.
- [Triggers:Configuration List Step:Type](../../instr-lib/nirfsg/pnirfsg-configlisttrig-type.html) Specifies the type of trigger to use as the Configuration List Step Trigger.
- [Triggers:Script:Digital Edge:Edge](../../instr-lib/nirfsg/pnirfsg-scripttrig-digedge-edge.html) Specifies the active edge for the Script Trigger. This property requires that you use the Active Channel property to specify the name of the Script Trigger you are configuring. This property is used when Script Trigger Type property is set to Digital Edge.
- [Triggers:Script:Digital Edge:Source](../../instr-lib/nirfsg/pnirfsg-scripttrig-digedge-source.html) Specifies the source terminal for the Script Trigger. This property requires that you use the Active Channel property to specify the name of the Script Trigger you are configuring. This property is used only when the Script Trigger Type property is set to Digital Edge.
- [Triggers:Script:Digital Level:Active Level](../../instr-lib/nirfsg/pnirfsg-scripttrig-diglevel-activelevel.html) Specifies the active level for the Script Trigger. This property is used when the Script Trigger Type property is set to Digital Level.
- [Triggers:Script:Digital Level:Source](../../instr-lib/nirfsg/pnirfsg-scripttrig-diglevel-source.html) Specifies the source terminal for the Script Trigger. This property is used when the Script Trigger Type property is set to Digital Level.
- [Triggers:Script:Export Output Terminal](../../instr-lib/nirfsg/pnirfsg-scripttrig-exportoutputterm.html) Specifies the destination terminal for exporting the Script Trigger. This property requires that you use the Active Channel property to specify the name of the Script Trigger you are configuring. To set this property, the NI-RFSG device must be in the Configuration state.
- [Triggers:Script:Terminal Name](../../instr-lib/nirfsg/pnirfsg-scripttrig-terminalname.html) Returns the fully qualified signal name as a string.
- [Triggers:Script:Type](../../instr-lib/nirfsg/pnirfsg-scripttrig-type.html) Specifies the type of trigger to use as the Script Trigger. This property requires that you use the Active Channel property to specify the name of the Script Trigger you are configuring. To set this property, the NI-RFSG device must be in the Configuration state.
- [Triggers:Start:Digital Edge:Edge](../../instr-lib/nirfsg/pnirfsg-starttrig-digedge-edge.html) Specifies the active edge for the Start Trigger. This property is used when the Start Trigger Type property is set to Digital Edge. To set this property, the NI-RFSG device must be in the Configuration state.
- [Triggers:Start:Digital Edge:Source](../../instr-lib/nirfsg/pnirfsg-starttrig-digedge-source.html) Specifies the source terminal for the Start Trigger. This property is used when the Start Trigger Type property is set to Digital Edge. To set the Start Trigger Digital Edge Source property, the NI-RFSG device must be in the Configuration state.
- [Triggers:Start:Export Output Terminal](../../instr-lib/nirfsg/pnirfsg-starttrig-exportoutputterm.html) Specifies the destination terminal for exporting the Start trigger. To set this property, the NI-RFSG device must be in the Configuration state.
- [Triggers:Start:P2P Endpoint Fullness:Level](../../instr-lib/nirfsg/pnirfsg-p2pendpointfullnessstarttriggerlevel.html) Specifies the number of samples needed to be received by the endpoint before the device starts generation. This property applies only when the Start Trigger Type property is set to P2P Endpoint Fullness.
- [Triggers:Start:Terminal Name](../../instr-lib/nirfsg/pnirfsg-starttrig-terminalname.html) Returns the fully qualified signal name as a string.
- [Triggers:Start:Type](../../instr-lib/nirfsg/pnirfsg-starttrig-type.html) Specifies the Start Trigger type. Depending upon the value of this property, more properties may be needed to fully configure the trigger. To set this property, the NI-RFSG device must be in the Configuration state.

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-perform-power-search-vi.html language=enus -->
## TOPIC 00032: niRFSG Perform Power Search VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-perform-power-search-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-perform-power-search-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a power search if the ALC Control property is disabled. Calling this VI disables modulation for a short time while the device levels the output signal. Power search temporarily enables the ALC, so ensure the appropriate included cable is connected between the PXIe-5654 ALC IN connector and

### niRFSG Perform Power Search VI

Performs a power search if the [ALC Control](/csh?context=nirfsg_rfsgproperties_pnirfsg_automaticlevelcontrol) property is disabled. Calling this VI disables modulation for a short time while the device levels the output signal.

Note

**Supported Devices**:PXIe-5654 with PXIe-5696

**Related Topics**

[Power Search](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=5654-power-search)

[IMAGE alt='icon' src='nirfsg-perform-power-search-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-property-node-vi.html language=enus -->
## TOPIC 00033: niRFSG Property Node VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-property-node-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads), sets (writes), or resets (sets to default value) NI-RFSG properties. When you read a property, NI-RFSG analyzes the current configuration in order to return the coerced value for that property. NI-RFSG verifies many properties upon reading, thereby either transitioning the session to t

### niRFSG Property Node VI

Gets (reads), sets (writes), or resets (sets to default value) NI-RFSG properties. When you read a property, NI-RFSG analyzes the current configuration in order to return the coerced value for that property. NI-RFSG verifies many properties upon reading, thereby either transitioning the session to the verified state or alerting you of an invalid configuration. Setting or resetting a property transitions the session to an unverified state.

**Related Topics**

[niRFSG Properties](/csh?context=nirfsg_rfsgproperties_cnirfsg)—Refer to this topic for more information about using the NI-RFSG properties.

[IMAGE alt='icon' src='nirfsg-property-node-vi.png']

#### Inputs/Outputs

| reference — reference identifies your instrument session. reference is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in (no error) — error in(no error) describes error conditions that occur before this node runs. The default is no error. This node does not pass the error in(no error) input to the error out output. Regardless of whether an error occurred before this node runs, the node returns no error. This input contains status, code, and source, which provide standard error in functionality. Property — Property Node is used to get (read), set (write), or reset (set to default value) RFSG properties. reference out — reference out passes a reference to your instrument session to the next VI. reference out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-RFSG

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-query-arb-waveform-capabilities-vi.html language=enus -->
## TOPIC 00034: niRFSG Query Arb Waveform Capabilities VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-query-arb-waveform-capabilities-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-query-arb-waveform-capabilities-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries and returns the arbitrary waveform capabilities of the NI-RFSG device. These capabilities are related to the current device configuration. The NI-RFSG device must be in the Configuration or Generation state before you call this VI. Supported Devices: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-

### niRFSG Query Arb Waveform Capabilities VI

Queries and returns the arbitrary waveform capabilities of the NI-RFSG device. These capabilities are related to the current device configuration. The NI-RFSG device must be in the Configuration or Generation state before you call this VI.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-query-arb-waveform-capabilities-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. maximum number of waveforms — maximum number of waveforms returns the maximum number of arbitrary waveforms, as specified in the Max. Number Waveforms property, that you can write. maximum waveform size (samples) — maximum waveform size returns the value of the Max. Waveform Size property. The number of samples that you write must be less than or equal to this value. minimum waveform size (samples) — minimum waveform size returns the value of the Min. Waveform Size property. The number of samples that you write must be greater than or equal to this value. error out — error out contains error information. This output provides standard error out functionality. waveform quantum — waveform quantum returns the quantum value the signal generator uses. The value of the Waveform Quantum property is returned. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-read-and-download-waveform-from-file-tdms-vi.html language=enus -->
## TOPIC 00035: niRFSG Read and Download Waveform From File (TDMS) VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-read-and-download-waveform-from-file-tdms-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-read-and-download-waveform-from-file-tdms-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms from a TDMS file and downloads one waveform into each of the NI RF vector signal generators. Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs cstr.png waveform name waveform name specifies the name used to store the waveform. This string is case

### niRFSG Read and Download Waveform From File (TDMS) VI

Reads the waveforms from a TDMS file and downloads one waveform into each of the NI RF vector signal generators.

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-read-and-download-waveform-from-file-tdms-vi.png']

#### Inputs/Outputs

| waveform name — waveform name specifies the name used to store the waveform. This string is case-insensitive. Example: "waveform::waveform0" instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. file path — file path specifies the absolute path to the TDMS file from which the NI-RFSG reads the waveforms. waveform index — waveform index specifies the index of the waveform to be read from the TDMS file. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

This VI reads the following information from the TDMS file and writes it into the NI-RFSG session:

- Sample Rate
- PAPR
- Runtime Scaling
- RF Blanking Marker Locations
- RF Blanking Enabled
- Burst Start Locations
- Burst Stop Locations
- RF Blanking Marker Source
- Signal Bandwidth
- Waveform Size

If RF blanking marker locations are present in the file but burst locations are not present, burst locations are calculated from RF blanking marker locations and stored in the NI-RFSG session.

Parent topic:

Configure Waveform

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-reset-device-vi.html language=enus -->
## TOPIC 00036: niRFSG Reset Device VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-reset-device-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-reset-device-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a hard reset on the device, which consists of the following actions: - Signal generation is stopped. - All routes are released. - External bidirectional terminals are tristated. - FPGAs are reset. - Hardware is configured to its default state. - All session properties are reset to their def

### niRFSG Reset Device VI

Performs a hard reset on the device, which consists of the following actions:

- Signal generation is stopped.

- All routes are released.

- External bidirectional terminals are tristated.

- FPGAs are reset.

- Hardware is configured to its default state.

- All session properties are reset to their default states.

**Supported Devices**:PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E

**Related Topics**

[Thermal Shutdown](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=thermal-shutdown)

[IMAGE alt='icon' src='nirfsg-reset-device-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

During a device reset, routes of signals between this and other devices are released,
 regardless of which device created the route. For example, a trigger signal exported to
 a PXI trigger line that is used by another device is no longer exported.

- PXI-5610, PXI-5670/5671, PXIe-5672: After calling this VI, the device requires 25 seconds before returning to full functionality. NI-RFSG enforces this condition by adding a wait, if needed, the next time you try to access the device.

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-reset-vi.html language=enus -->
## TOPIC 00037: niRFSG Reset VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-reset-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-reset-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all properties to their default values and moves the NI-RFSG device to the Configuration state. This VI aborts the signal generation, clears all routes, deletes all de-embedding tables, and resets session properties to their initial values. During a reset, routes of signals between this and o

### niRFSG Reset VI

Resets all properties to their default values and moves the NI-RFSG device to the Configuration state. This VI aborts the signal generation, clears all routes, deletes all de-embedding tables, and resets session properties to their initial values. During a reset, routes of signals between this and other devices are released, regardless of which device created the route.

Note

niRFSG Reset With Options

steps to omit

Routes

**Supported Devices**: PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-reset-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-set-waveform-burst-start-locations-vi.html language=enus -->
## TOPIC 00038: niRFSG Set Waveform Burst Start Locations VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-set-waveform-burst-start-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-set-waveform-burst-start-locations-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start location of the burst in samples where the burst refers to the active portion of a waveform. Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842 icon Inputs/Outputs cstr.png channel name channel name specifies the waveform name and the marker name. Example: "waveform::wav

### niRFSG Set Waveform Burst Start Locations VI

Configures the start location of the burst in samples where the burst refers to the active portion of a waveform.

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842

[IMAGE alt='icon' src='nirfsg-set-waveform-burst-start-locations-vi.png']

#### Inputs/Outputs

| channel name — channel name specifies the waveform name and the marker name. Example: "waveform::waveform0/marker0" instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. locations — locations specifies the burst start locations, in samples, to store in the NI-RFSG session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Burst Location

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-set-waveform-marker-event-locations-vi.html language=enus -->
## TOPIC 00039: niRFSG Set Waveform Marker Event Locations VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-set-waveform-marker-event-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-set-waveform-marker-event-locations-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the marker locations associated with waveform and marker in the NI-RFSG session. Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842 icon Inputs/Outputs cstr.png channel name channel name specifies the waveform name and the marker name. Example: "waveform::waveform0/marker0" civrn.

### niRFSG Set Waveform Marker Event Locations VI

Configures the marker locations associated with waveform and marker in the NI-RFSG session.

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842

[IMAGE alt='icon' src='nirfsg-set-waveform-marker-event-locations-vi.png']

#### Inputs/Outputs

| channel name — channel name specifies the waveform name and the marker name. Example: "waveform::waveform0/marker0" instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. locations — locations specifies the marker location, in samples, to store in the NI-RFSG session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Marker Event

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-update-external-calibration-temperature-vi.html language=enus -->
## TOPIC 00040: niRFSG Update External Calibration Temperature VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-update-external-calibration-temperature-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-update-external-calibration-temperature-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates the temperature of the last external calibration to the current temperature. Supported Devices: PXIe-5653/5654, PXIe-5696 icon Inputs/Outputs civrn.png instrument handle instrument handle identifies your instrument calibration session. instrument handle is obtained from the niRFSG Initialize

### niRFSG Update External Calibration Temperature VI

Updates the temperature of the last external calibration to the current temperature.

**Supported Devices**: PXIe-5653/5654, PXIe-5696

[IMAGE alt='icon' src='nirfsg-update-external-calibration-temperature-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument calibration session. instrument handle is obtained from the niRFSG Initialize External Calibration VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-utility-mnu.html language=enus -->
## TOPIC 00041: Utility

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-utility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-utility-mnu.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the utility VIs to access additional features of the NI-RFSG instrument driver. icon

### Utility

Use the utility VIs to access additional features of the NI-RFSG instrument driver.

[IMAGE alt='icon' src='nirfsg-utility-mnu.png']

- [niRFSG Initialize With Options VI](../../instr-lib/nirfsg/nirfsg-initialize-with-options-vi.html) Opens a session to the device you specify as the resource name and returns an instrument handle that you use to identify the instrument in all subsequent NI-RFSG VIs. This VI also configures the device using the option string input.
- [niRFSG Commit VI](../../instr-lib/nirfsg/nirfsg-commit-vi.html) Programs the device with the correct settings. Calling this VI moves the NI-RFSG device from the Configuration state to the Committed state. After this VI executes, a change to any property reverts the NI-RFSG device to the Configuration state.
- [niRFSG Wait Until Settled VI](../../instr-lib/nirfsg/nirfsg-wait-until-settled-vi.html) Waits until the RF output signal settles. This VI is useful for devices that support changes while in the Generation state. Call this VI after making a dynamic change to wait for the output signal to settle. You can also call this VI after calling the niRFSG Commit VI to wait for changes to settle. The niRFSG Wait Until Settled VI is not required after calling the niRFSG Initiate VI because the niRFSG Initiate VI automatically waits for the output to settle.
- [niRFSG Configure Output Enabled VI](../../instr-lib/nirfsg/nirfsg-configure-output-enabled-vi.html) Enables or disables signal output. Setting output enabled to FALSE while in the Generation state attenuates the generated signal so that no signal is output.
- [niRFSG Self Test VI](../../instr-lib/nirfsg/nirfsg-self-test-vi.html) Performs a self-test on the NI-RFSG device and returns the test results. This VI performs a simple series of tests to determine whether the NI-RFSG device is powered up and responding. This VI does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this VI. The NI-RFSG device must be in the Configuration state before you call this VI.
- [niRFSG Reset VI](../../instr-lib/nirfsg/nirfsg-reset-vi.html) Resets all properties to their default values and moves the NI-RFSG device to the Configuration state. This VI aborts the signal generation, clears all routes, deletes all de-embedding tables, and resets session properties to their initial values. During a reset, routes of signals between this and other devices are released, regardless of which device created the route.
- [niRFSG Reset With Options VI](../../instr-lib/nirfsg/nirfsg-reset-with-options-vi.html) Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes.
- [niRFSG Reset Device VI](../../instr-lib/nirfsg/nirfsg-reset-device-vi.html) Performs a hard reset on the device, which consists of the following actions:
- [niRFSG Save Configurations To File VI](../../instr-lib/nirfsg/nirfsg-save-configurations-to-file-vi.html) Saves the configurations of the session to the specified file.
- [niRFSG Load Configurations From File VI](../../instr-lib/nirfsg/nirfsg-load-configurations-from-file-vi.html) Loads the configurations from the specified file to the NI-RFSG driver session. The VI does an implicit reset before loading the configurations from the file.
- [niRFSG Perform Power Search VI](../../instr-lib/nirfsg/nirfsg-perform-power-search-vi.html) Performs a power search if the ALC Control property is disabled. Calling this VI disables modulation for a short time while the device levels the output signal.
- [niRFSG Get Session Reference VI](../../instr-lib/nirfsg/nirfsg-get-session-reference-vi.html) Extracts a session that can be passed to NI-TClk VIs. Session References are of generic data type, which means that the corresponding wires are blue-green, unlike the wires for regular instrument driver sessions.
- [niRFSG Revision Query VI](../../instr-lib/nirfsg/nirfsg-revision-query-vi.html) Returns the revision numbers of the NI-RFSG driver and the instrument firmware.
- [niRFSG Query Arb Waveform Capabilities VI](../../instr-lib/nirfsg/nirfsg-query-arb-waveform-capabilities-vi.html) Queries and returns the arbitrary waveform capabilities of the NI-RFSG device. These capabilities are related to the current device configuration. The NI-RFSG device must be in the Configuration or Generation state before you call this VI.
- [niRFSG Perform Thermal Correction VI](../../instr-lib/nirfsg/nirfsg-perform-thermal-correction-vi.html) Corrects for any signal drift due to temperature variation when generating the same signal for extended periods of time without a parameter change. Under normal circumstances of short-term signal generation, NI-RFSG performs thermal correction automatically by ensuring stable power levels, and you do not need to call this VI. Use this VI when generating the same signal for a long period of time in a temperature-fluctuating environment. The NI-RFSG device must be in the Generation state before you call this VI.
- [niRFSG Error Message VI](../../instr-lib/nirfsg/nirfsg-error-message-vi.html) Converts a error code returned by an NI-RFSG VI into a user-readable string. Instead of using this VI, most applications will use an Error Out control or the Simple Error Handler in LabVIEW to display error information.
- [niRFSG Get Max Settable Power VI](../../instr-lib/nirfsg/nirfsg-get-max-settable-power-vi.html) Returns the maximum settable output power level for the current configuration.

Parent topic:

NI-RFSG

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-wait-until-settled-vi.html language=enus -->
## TOPIC 00042: niRFSG Wait Until Settled VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-wait-until-settled-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-wait-until-settled-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the RF output signal settles. This VI is useful for devices that support changes while in the Generation state. Call this VI after making a dynamic change to wait for the output signal to settle. You can also call this VI after calling the niRFSG Commit VI to wait for changes to settle.

### niRFSG Wait Until Settled VI

Waits until the RF output signal settles. This VI is useful for devices that support changes while in the Generation state. Call this VI after making a dynamic change to wait for the output signal to settle. You can also call this VI after calling the [niRFSG Commit](/csh?topicname=nirfsg-commit-vi.html) VI to wait for changes to settle. The niRFSG Wait Until Settled VI is not required after calling the [niRFSG Initiate](/csh?topicname=nirfsg-initiate-vi.html) VI because the niRFSG Initiate VI automatically waits for the output to settle.

**Supported Devices**: PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-wait-until-settled-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. Max. time (ms) — Max. time specifies the maximum time the VI waits for the output to settle. If the maximum time is exceeded, this VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-write-arb-waveform-complex-input-sgl-vi.html language=enus -->
## TOPIC 00043: niRFSG Write Arb Waveform (Complex Input SGL) VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-write-arb-waveform-complex-input-sgl-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-write-arb-waveform-complex-input-sgl-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This VI accepts complex baseband signal data in the form of a complex cluster. Supported Devices: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs cstr.png name name specifie

### niRFSG Write Arb Waveform (Complex Input SGL) VI

Writes an arbitrary waveform to the NI-RFSG device. This VI accepts complex baseband signal data in the form of a complex cluster.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-write-arb-waveform-complex-input-sgl-vi.png']

#### Inputs/Outputs

| name — name specifies the name used to store the waveform. This string is case-insensitive and alphanumeric, and it cannot use reserved words. instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. IQ waveform — IQ waveform specifies the complex baseband signal to write to the NI-RFSG device. t0 — t0 specifies the trigger (start) time of the acquired Y array. dt — dt specifies the time interval between the samples in the acquired Y array. dt is the reciprocal of the I/Q rate. Y — Y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. use waveform dt for IQ rate? — use waveform dt for IQ rate? specifies TRUE if the VI uses the waveform dt to configure the I/Q rate and FALSE if it does not configure the I/Q rate. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. more data pending? — more data pending? specifies whether the data block contains the end of the waveform. Set more data pending? to TRUE to allow data to be appended to the waveform later. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. You can append data to a previously written waveform by using the saved waveform name. Set this parameter to FALSE to indicate that this data block contains the end of the waveform. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 specifies the trigger (start) time of the acquired Y array. dt — dt specifies the time interval between the samples in the acquired Y array. dt is the reciprocal of the I/Q rate. Y — Y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

niRFSG Write Arb Waveform VI

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-write-arb-waveform-complex-input-vi.html language=enus -->
## TOPIC 00044: niRFSG Write Arb Waveform (Complex Input) VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-write-arb-waveform-complex-input-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-write-arb-waveform-complex-input-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This VI accepts complex baseband signal data in the form of a complex cluster. Supported Devices: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs cstr.png name name specifie

### niRFSG Write Arb Waveform (Complex Input) VI

Writes an arbitrary waveform to the NI-RFSG device. This VI accepts complex baseband signal data in the form of a complex cluster.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-write-arb-waveform-complex-input-vi.png']

#### Inputs/Outputs

| name — name specifies the name used to store the waveform. This string is case-insensitive and alphanumeric, and it cannot use reserved words. instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. IQ waveform — IQ waveform specifies the complex baseband signal to write to the NI-RFSG device. t0 — t0 specifies the trigger (start) time of the acquired Y array. dt — dt specifies the time interval between the samples in the acquired Y array. dt is the reciprocal of the I/Q rate. Y — Y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. use waveform dt for IQ rate? — use waveform dt for IQ rate? specifies TRUE if the VI uses the waveform dt to configure the I/Q rate and FALSE if it does not configure the I/Q rate. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. more data pending? — more data pending? specifies whether the data block contains the end of the waveform. Set more data pending? to TRUE to allow data to be appended to the waveform later. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. You can append data to a previously written waveform by using the saved waveform name. Set this parameter to FALSE to indicate that this data block contains the end of the waveform. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 specifies the trigger (start) time of the acquired Y array. dt — dt specifies the time interval between the samples in the acquired Y array. dt is the reciprocal of the I/Q rate. Y — Y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

niRFSG Write Arb Waveform VI

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-write-arb-waveform-cwdt-vi.html language=enus -->
## TOPIC 00045: niRFSG Write Arb Waveform (CWDT) VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-write-arb-waveform-cwdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-write-arb-waveform-cwdt-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This VI accepts the complex baseband signal data in the form of a complex waveform datatype. Supported Devices: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs cstr.png name

### niRFSG Write Arb Waveform (CWDT) VI

Writes an arbitrary waveform to the NI-RFSG device. This VI accepts the complex baseband signal data in the form of a complex waveform datatype.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsg-write-arb-waveform-cwdt-vi.png']

#### Inputs/Outputs

| name — name specifies the name used to store the waveform. This string is case-insensitive and alphanumeric, and it cannot use reserved words. instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. IQ Waveform — IQ Waveform specifies the complex waveform to write to the NI-RFSG device. use waveform dt for IQ rate? — use waveform dt for IQ rate? specifies TRUE if the VI uses the waveform dt to configure the I/Q rate and FALSE if it does not configure the I/Q rate. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. more data pending? — more data pending? specifies whether the data block contains the end of the waveform. Set more data pending? to TRUE to allow data to be appended to the waveform later. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. You can append data to a previously written waveform by using the saved waveform name. Set this parameter to FALSE to indicate that this data block contains the end of the waveform. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSG Write Arb Waveform VI

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/nirfsg-write-arb-waveform-direct-dma-vi.html language=enus -->
## TOPIC 00046: niRFSG Write Arb Waveform (Direct DMA) VI

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/nirfsg-write-arb-waveform-direct-dma-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/nirfsg-write-arb-waveform-direct-dma-vi.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG device. This VI inputs the I and Q vectors of a complex baseband signal. The NI-RFSG device must be in the Configuration state before calling this VI. Related Topics Streaming Assigning Properties or Attributes to a Waveform icon Inputs/Outputs cstr.png na

### niRFSG Write Arb Waveform (Direct DMA) VI

Writes an arbitrary waveform to the NI-RFSG device. This VI inputs the I and Q vectors of a complex baseband signal. The NI-RFSG device must be in the Configuration state before calling this VI.

**Related Topics**

[Streaming](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=streaming)

[Assigning Properties or Attributes to a Waveform](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=assigning-properties-or-attributes-to-a-wavef)

[IMAGE alt='icon' src='nirfsg-write-arb-waveform-direct-dma-vi.png']

#### Inputs/Outputs

| name — name specifies the name used to store the waveform. This is a case-insensitive alphanumeric string that does not use reserved words. instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from either the niRFSG Initialize VI or the niRFSG Initialize With Options VI. direct DMA address — samples to write — error in — error in can accept error information wired from VIs previously called. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle out is obtained from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error out — error out passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

niRFSG Write Arb Waveform VI

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-activeconfigurationlist.html language=enus -->
## TOPIC 00047: Configuration List:Active List

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-activeconfigurationlist.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-activeconfigurationlist.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of the configuration list to make active. When a property is get or set and that property is in the configuration list properties of the active list, the property is set to or get from the active list step of the active list. If the Active Configuration List property is set to ""

### Configuration List:Active List

Specifies the name of the configuration list to make active. When a property is get or set and that property is in the configuration list properties of the active list, the property is set to or get from the active list step of the active list. If the Active Configuration List property is set to "" (empty string), no list is active.

Note

Frequency Settling Units

Seconds After I/O

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters

**Default Value**: "" (empty string)

**Related Topics**

[RF List Mode](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=rf-list-mode)

[Using RF List Mode](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=using-rf-list-mode)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Configuration List |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSG Create Configuration List |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-activeconfigurationliststep.html language=enus -->
## TOPIC 00048: Configuration List:Active Step

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-activeconfigurationliststep.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-activeconfigurationliststep.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active step of the list defined by the Active Configuration List property. Supported Devices: PXIe-5644/5645/5646, PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Freque

### Configuration List:Active Step

Specifies the active step of the list defined by the [Active Configuration List](/csh?topicname=pnirfsg-activeconfigurationlist.html) property.

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters

**Default Value**: 0

**Related Topics**

[RF List Mode](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=rf-list-mode)

[Using RF List Mode](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=using-rf-list-mode)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Configuration List Step |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSG Create Configuration List |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-aetemperature-degreesc.html language=enus -->
## TOPIC 00049: Device Characteristics:AE Temperature (Degrees C)

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-aetemperature-degreesc.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-aetemperature-degreesc.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the amplitude extender module temperature in degrees Celsius. Supported Devices: PXIe-5654 with PXIe-5696 Remarks The following table lists the characteristics of this property. Short Name AE Temperature (Degrees C) Data type cdbl.png Permissions Read Only High-level VIs N/A Channel-based No

### Device Characteristics:AE Temperature (Degrees C)

Returns the amplitude extender module temperature in degrees Celsius.

**Supported Devices**: PXIe-5654 with PXIe-5696

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AE Temperature (Degrees C) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-allowoutofspecificationusersettings.html language=enus -->
## TOPIC 00050: RF:Allow Out Of Specification User Settings

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-allowoutofspecificationusersettings.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-allowoutofspecificationusersettings.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables warnings or errors when you set frequency, power, and bandwidth values beyond the limits of the NI-RFSG device specifications. When you enable this property, the driver does not report out-of-specification warnings or errors. To set this property, the NI-RFSG device must be in th

### RF:Allow Out Of Specification User Settings

Enables or disables warnings or errors when you set frequency, power, and bandwidth values beyond the limits of the NI-RFSG device specifications. When you enable this property, the driver does not report out-of-specification warnings or errors.

To set this property, the NI-RFSG device must be in the Configuration state.

Note

**Supported Devices**: PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841

**Default Value**: Disable

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Allow Out Of Specification User Settings |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Disable | 0 | Disables out of specification user settings. |
| --- | --- | --- |
| Enable | 1 | Enables out of specification user settings. |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-amplitudesettling.html language=enus -->
## TOPIC 00051: RF:Amplitude Settling

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-amplitudesettling.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-amplitudesettling.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the amplitude settling accuracy in decibels. NI-RFSG waits until the RF power settles within the specified accuracy level after calling the niRFSG Initiate VI or niRFSG Wait Until Settled VI or prior to advancing to next step if using RF list mode. Any specified amplitude settling value t

### RF:Amplitude Settling

Configures the amplitude settling accuracy in decibels. NI-RFSG waits until the RF power settles within the specified accuracy level after calling the [niRFSG Initiate](/csh?context=nirfsg_lvrfsg_nirfsg_initiate) VI or [niRFSG Wait Until Settled](/csh?context=nirfsg_lvrfsg_nirfsg_wait_until_settled) VI or prior to advancing to next step if using RF list mode.

Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.

PXI/PXIe-5650/5651/5652: This property is for NI internal use only.

**Supported Devices**: PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Default Values**:

PXIe-5654: 4

PXIe-5654 with PXIe-5696 (ALC disabled): 4

PXIe-5654 with PXIe-5696 (ALC enabled): 0.2

PXIe-5820/5830/5831/5832/5840/5841/5842/5860: 0.5

**Valid Values**:

PXIe-5654: 1.5, 2, 4

PXIe-5654 with PXIe-5696 (ALC disabled): 1.5, 2, 4

PXIe-5654 with PXIe-5696 (ALC enabled): 0.2, 0.5

PXIe-5820/5830/5831/5832/5840/5841/5842/5860: 0.01 to 1

**Related Topics**

[Amplitude Settling Times](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=amplitude-settling-times)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Amplitude Settling |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-anlgmod-amsensitivity.html language=enus -->
## TOPIC 00052: Modulation:Analog:AM Sensitivity

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-anlgmod-amsensitivity.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-anlgmod-amsensitivity.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator. When using the PXIe-5654with PXIe-5696, NI-RFSG may

### Modulation:Analog:AM Sensitivity

Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.

When using the PXIe-5654with PXIe-5696, NI-RFSG may coerce AM sensitivity. Coercing the AM sensitivity prevents overpower conditions at the PXIe-5696 input. Read this property to determine the coerced value.

**Supported Devices**: PXIe-5654/5654 with PXIe-5696

**Default Value**: 100

**Valid Values**: 0 to 100

**Related Topics**

[Amplitude Modulation](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=amplitude-modulation-am)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AnlgMod.AM Sensitivity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-anlgmod-fmband.html language=enus -->
## TOPIC 00053: Modulation:Analog:FM Band

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-anlgmod-fmband.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-anlgmod-fmband.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the analog modulation frequency modulation (FM) band to use. Wideband FM allows for modulating signals higher than 100 kHz. Narrowband FM allows for modulating lower frequency signals. Supported Devices: PXIe-5654/5654 with PXIe-5696 Default Value: Wideband Related Topics Frequency Modulat

### Modulation:Analog:FM Band

Specifies the analog modulation frequency modulation (FM) band to use. Wideband FM allows for modulating signals higher than 100 kHz. Narrowband FM allows for modulating lower frequency signals.

**Supported Devices**: PXIe-5654/5654 with PXIe-5696

**Default Value**: Wideband

**Related Topics**

[Frequency Modulation](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=frequency-modulation-fm)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AnlgMod.FM Band |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Narrowband | 17000 | Specifies narrowband frequency modulation. |
| --- | --- | --- |
| Wideband | 17001 | Specifies wideband frequency modulation. |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-anlgmod-fmdev-hz.html language=enus -->
## TOPIC 00054: Modulation:Analog:FM Deviation (Hz)

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-anlgmod-fmdev-hz.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-anlgmod-fmdev-hz.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the deviation to use in frequency modulation. Supported Devices: PXI/PXIe-5650/5651/5652 Default Value: 1 kHz Related Topics Modulation Schemes Remarks The following table lists the characteristics of this property. Short Name AnlgMod.FMDev (Hz) Data type cdbl.png Permissions Read/Write Hi

### Modulation:Analog:FM Deviation (Hz)

Specifies the deviation to use in frequency modulation.

**Supported Devices**: PXI/PXIe-5650/5651/5652

**Default Value**: 1 kHz

**Related Topics**

[Modulation Schemes](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=modulation-schemes)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AnlgMod.FMDev (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-anlgmod-fmnarrowbandintegrator.html language=enus -->
## TOPIC 00055: Modulation:Analog:FM Narrowband Integrator

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-anlgmod-fmnarrowbandintegrator.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-anlgmod-fmnarrowbandintegrator.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the narrowband frequency modulation (FM) range to apply by sending the signal through an integrator. This property is valid only when you set the Modulation Type property to FM and the FM Band property to Narrowband. Supported Devices: PXIe-5654/5654 with PXIe-5696 Default Value: 100 Hz to

### Modulation:Analog:FM Narrowband Integrator

Specifies the narrowband frequency modulation (FM) range to apply by sending the signal through an integrator.

This property is valid only when you set the [Modulation Type](pnirfsg-anlgmod-type.html) property to **FM** and the [FM Band](pnirfsg-anlgmod-fmband.html) property to **Narrowband**.

**Supported Devices**: PXIe-5654/5654 with PXIe-5696

**Default Value**: 100 Hz to 1 kHz

**Related Topics**

[Frequency Modulation](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=frequency-modulation-fm)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AnlgMod.FM Narrowband Integrator |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| 100Hz to 1kHz | 18000 | Specifies a range from 100 Hz to 1 kHz |
| --- | --- | --- |
| 1kHz to 10kHz | 18001 | Specifies a range from 1 kHz to 10 kHz |
| 10kHz to 100kHz | 18002 | Specifies a range from 10 kHz to 100 kHz |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-anlgmod-fmsensitivity.html language=enus -->
## TOPIC 00056: Modulation:Analog:FM Sensitivity

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-anlgmod-fmsensitivity.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-anlgmod-fmsensitivity.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator. Supported Devices: PXIe-5654/5654 with PXIe-5696 De

### Modulation:Analog:FM Sensitivity

Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.

**Supported Devices**: PXIe-5654/5654 with PXIe-5696

**Default Value**: 100

**Valid Values**: 0 to 100

**Related Topics**

[Frequency Modulation](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=frequency-modulation-fm)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AnlgMod.FM Sensitivity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-anlgmod-pmdev-degrees.html language=enus -->
## TOPIC 00057: Modulation:Analog:PM Deviation (Degrees)

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-anlgmod-pmdev-degrees.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-anlgmod-pmdev-degrees.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the deviation to use in phase modulation, in degrees. Supported Devices: PXI/PXIe-5650/5651/5652, PXIe-5653 Default Value: 90 degrees Related Topics Modulation Schemes Remarks The following table lists the characteristics of this property. Short Name AnlgMod.PMDev (Degrees) Data type cdbl.

### Modulation:Analog:PM Deviation (Degrees)

Specifies the deviation to use in phase modulation, in degrees.

**Supported Devices**: PXI/PXIe-5650/5651/5652, PXIe-5653

**Default Value**: 90 degrees

**Related Topics**

[Modulation Schemes](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=modulation-schemes)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AnlgMod.PMDev (Degrees) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-iqoutporttermcfg.html language=enus -->
## TOPIC 00058: Device Specific:Vector Signal Transceiver:IQ Out Port:Terminal Configuration

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-iqoutporttermcfg.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-iqoutporttermcfg.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use the I/Q OUT port for Differential configuration or Single-Ended configuration. If you set this property to Single-Ended, you must terminate the negative I and Q output connectors with a 50 Ohm termination. If you set this property to Single-Ended, the positive I and Q connec

### Device Specific:Vector Signal Transceiver:IQ Out Port:Terminal Configuration

Specifies whether to use the I/Q OUT port for **Differential** configuration or **Single-Ended** configuration. If you set this property to **Single-Ended**, you must terminate the negative I and Q output connectors with a 50 Ohm termination.

If you set this property to **Single-Ended**, the positive I and Q connectors generate the resulting waveform. If you set this property to **Differential**, both the positive and negative I and Q connectors generate the resulting waveform.

To use this property, you must use the [Active Channel](pnirfsg-activechannel.html) property to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

Note

To set this property, the NI-RFSG device must be in the Configuration state.

PXIe-5820: The only valid value for this property is **Differential**.

**Supported Devices**: PXIe-5645, PXIe-5820

**Default Value**: Differential

**Related Topics**

[Differential and Single-Ended Operation (I/Q Interface)](https://ni.com/docs/en-US/csh?pubname=pxie-5645-feature&topicname=differential-single-ended-operation)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Out Port Terminal Configuration |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Differential | 15000 | Sets the terminal configuration to differential. |
| --- | --- | --- |
| Single-Ended | 15001 | Sets the terminal configuration to single-ended. |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-iqrate-ss.html language=enus -->
## TOPIC 00059: Arb:IQ Rate (S/s)

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-iqrate-ss.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-iqrate-ss.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property specifies the I/Q rate of the arbitrary waveform. The I/Q rate is coerced to a value the hardware can achieve. Read this value back after setting it to see the actual I/Q rate. NI-RFSG internally uses an FIR filter with flat response up to (0.4 Ã— IQ rate). Given a desired signal with

### Arb:IQ Rate (S/s)

This property specifies the I/Q rate of the arbitrary waveform. The I/Q rate is coerced to a value the hardware can achieve. Read this value back after setting it to see the actual I/Q rate. NI-RFSG internally uses an FIR filter with flat response up to (0.4 Ã— IQ rate). Given a desired signal with the maximum frequency content *f*, sample the signal at an I/Q rate greater than or equal to (*f*/0.4).

This property only applies when the [Generation Mode](pnirfsg-generationmode.html) property is set to Arb Waveform or Script.

To set this property, the NI-RFSG device must be in the Configuration state.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

The following table lists available I/Q rates.

| Device | Available Rates |
| --- | --- |
| PXIe-5644/5645 | Up to 120 MS/s. |
| PXIe-5646 | Up to 250 MS/s. |
| PXI-5670 | 50 MS/s, 100 MS/s |
| PXI-5671 | 50 MS/s, 100 MS/s, and (100 MS/s)/n, where n is divisible by 2 between 12 to 512, and divisible by 4 between 512 to 1,024 (n = 12,14,16, ...,512, 516, 520, ...,1024). Setting the I/Q rate to one of these values enables the DUC. |
| PXIe-5672 | Up to 100 MS/s. |
| PXIe-5673/5673E | Up to 200 MS/s. Note If an PXIe-5450 with module revisions A or B is used as part of your PXIe-5673/5673E, the NI-FGEN Compensate for Filter Group Delay property is disabled if the requested I/Q rate is less than 1.5 MS/s. |
| PXIe-5820/5830/5831/5832/5840/5841/5860 | Up to 1.25 GS/s. |
| PXI-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options) | Up to 2.5 GS/s. |
| PXIe-5842 (4 GHz bandwidth option) using the Standard personality | Up to 2.5 GS/s. |
| PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality | 5 GS/s only. |

Setting this property to 50 MS/s on the PXI-5670/5671, PXIe-5672 has the following implications:

- The NI-RFSG driver is forced to place the carrier frequency at 18 MHz Â± 1 MHz to avoid aliasing. Forcing the carrier frequency to that point implies that NI-RFSG does not have the freedom to pick a carrier frequency that could optimize the waveform size if phase continuity is enabled.
- Output signal bandwidth must be less than 5 MHz to avoid aliasing.
- Close-in phase noise is higher.

Note

**Related Topics**

[Streaming](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=streaming)

[Assigning Properties or Attributes to a Waveform](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=assigning-properties-or-attributes-to-a-wavef)—Refer to this topic for more information about using this property to associate an I/Q rate with a waveform.

[Digital Upconverter](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=digital-upconverter)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Rate (S/s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSG Write Arb Waveform |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-iqskew-degrees.html language=enus -->
## TOPIC 00060: IQ Impairment:IQ Skew (Degrees)

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-iqskew-degrees.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-iqskew-degrees.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the adjustment of the phase angle between the I and Q vectors. If this skew is zero, the phase angle is 90 degrees. Supported Devices: PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842 Valid Values: -30 degrees to 30 degrees Related Topics Impairment Calibration

### IQ Impairment:IQ Skew (Degrees)

Specifies the adjustment of the phase angle between the I and Q vectors. If this skew is zero, the phase angle is 90 degrees.

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

**Valid Values**: -30 degrees to 30 degrees

**Related Topics**

[Impairment Calibration](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=impairment-calibration)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Skew (Degrees) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-iqswapenabled.html language=enus -->
## TOPIC 00061: Arb:IQ Swap Enabled

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-iqswapenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-iqswapenabled.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables the inverse phase rotation of the I/Q signal by swapping the I and Q inputs. To set this property, the NI-RFSG device must be in the Configuration state. Supported Devices: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842 Default V

### Arb:IQ Swap Enabled

Enables or disables the inverse phase rotation of the I/Q signal by swapping the I and Q inputs.

To set this property, the NI-RFSG device must be in the Configuration state.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

**Default Value**: FALSE

| TRUE | Applies noninverse phase rotation of the I/Q signal. |
| --- | --- |
| FALSE | Applies inverse phase rotation of the I/Q signal. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Swap Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-lastselfcaltemp.html language=enus -->
## TOPIC 00062: Self Calibration:Last Self Calibration Temperature

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-lastselfcaltemp.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-lastselfcaltemp.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates, in degrees Celsius, the temperature of the device at the time of the last self calibration. Supported Devices: PXIe-5644/5645/5646 Remarks The following table lists the characteristics of this property. Short Name Last Self Cal Temp Data type cdbl.png Permissions Read Only High-level VIs

### Self Calibration:Last Self Calibration Temperature

Indicates, in degrees Celsius, the temperature of the device at the time of the last self calibration.

**Supported Devices**: PXIe-5644/5645/5646

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Last Self Cal Temp |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-loadoptions.html language=enus -->
## TOPIC 00063: Load Configurations:Load Options

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-loadoptions.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-loadoptions.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the configurations to skip while loading from a file. Default Values: Skip None Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Remarks The following table lists the characteristics of this property. Short Name Load Options Data type ci32.png Permissions Read/Write High-lev

### Load Configurations:Load Options

Specifies the configurations to skip while loading from a file.

**Default Values**: Skip None

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Load Options |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Skip None | 0 | NI-RFSG loads all the configurations to the session. |
| --- | --- | --- |
| Skip Waveforms | 1 | NI-RFSG skips loading the waveform configurations to the session. |
| Skip Scripts | 2 | NI-RFSG skips loading the scripts to the session. |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-lofrequencystepsize-hz.html language=enus -->
## TOPIC 00064: Device Specific:Vector Signal Transceiver:Signal Path:LO Frequency Step Size (Hz)

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-lofrequencystepsize-hz.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-lofrequencystepsize-hz.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL). When the LO PLL Fractional Mode Enabled property is set to Enabled, the specified step size affects the fractional spur performance of the device. When the LO PLL Fractional Mode Enabled property is set to Disabled

### Device Specific:Vector Signal Transceiver:Signal Path:LO Frequency Step Size (Hz)

Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL).

When the [LO PLL Fractional Mode Enabled](pnirfsg-lopllfractionalmodeenabled.html) property is set to **Enabled**, the specified step size affects the fractional spur performance of the device. When the LO PLL Fractional Mode Enabled property is set to **Disabled**, the specified step size affects the phase noise performance of the device.

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

**Default Values**:

PXIe-5644/5645/5646: 200 kHz

PXIe-5830: 2 MHz

PXIe-5831/5832 (RF port): 8 MHz

PXIe-5831/5832 (IF port): 2 MHz, 4 MHz

PXIe-5840/5841:

- Fractional mode: 500 kHz
- Integer mode: 10 MHz for frequencies less than or equal to 4 GHz. 20 MHz for frequencies greater than 4 GHz.

PXIe-5841 with PXIe-5655: 500 kHz

PXIe-5842: 1 Hz

**Valid Values**:

The valid values for this property depend on the LO PLL Fractional Mode Enabled property.

**PXIe-5644/5645/5646**—If you set the LO PLL Fractional Mode Enabled property to **Disabled**, the specified value is coerced to the nearest valid value.

**PXIe-5840/5841**—If you set the LO PLL Fractional Mode Enabled property to **Disabled**, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.

To use this property for the PXIe-5830/5831/5832 and PXIe-5842 VST with 54 GHz Frequency Extension, you must first use the [Active Channel](pnirfsg-activechannel.html) property to specify the name of the channel you are configuring. You can configure LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

Note

| LO PLL Fractional Mode Enabled Property Setting | LO Frequency Step Size Property Valid Values on PXIe-5644/5645 | LO Frequency Step Size Property Valid Values on PXIe-5646 | LO Frequency Step Size Property Valid Values on PXIe-5840/5841 | LO Frequency Step Size Property Valid Values on PXIe-5830/5831/5832 | LO Frequency Step Size Property Valid Values on PXIe-5841 with PXIe-5655, PXIe-5842* |
| --- | --- | --- | --- | --- | --- |
| Enabled | 50 kHz to 24 MHz | 50 kHz to 25 MHz | 50 kHz to 100 MHz | LO1: 8 Hz to 400 MHz LO2: 4 kHz to 400 MHz | 1 nHz to 50 MHz |
| Disabled | 4 MHz, 5 MHz, 6 MHz, 12 MHz, 24 MHz | 2 MHz, 5 MHz, 10 MHz, 25 MHz | 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, 100 MHz | LO1: -- LO2: -- | 1 nHz to 50 MHz |

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Frequency Step Size (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-logicalname.html language=enus -->
## TOPIC 00065: Inherent IVI Attributes:Advanced Session Information:Logical Name

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-logicalname.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-logicalname.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the logical name you specified when opening the current IVI session. You can pass a logical name to the niRFSG Initialize VI or the niRFSG Initialize with Options VI. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refer

### Inherent IVI Attributes:Advanced Session Information:Logical Name

Returns a string that contains the logical name you specified when opening the current IVI session.

You can pass a logical name to the [niRFSG Initialize](/csh?context=nirfsg_lvrfsg_nirfsg_initialize) VI or the
[niRFSG Initialize with Options](/csh?context=nirfsg_lvrfsg_nirfsg_initialize_with_options) VI. The
IVI Configuration Utility must contain an entry for the logical name. The logical name entry
refers to a driver session section in the IVI Configuration file. The driver session section
specifies a physical device and initial user options.

**Supported Devices**: PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logical Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-looutpower-dbm.html language=enus -->
## TOPIC 00066: RF:LO Out Power (dBm)

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-looutpower-dbm.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-looutpower-dbm.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level of the signal at the LO OUT front panel connector. For the PXIe-5644/5645/5646 and PXIe-5673/5673E, this property is always read-only. To use this property for the PXIe-5830/5831/5832 and PXIe-5842 VST with 54 GHz Frequency Extension, you must first use the Active Channel p

### RF:LO Out Power (dBm)

Specifies the power level of the signal at the LO OUT front panel connector.

Note

To use this property for the PXIe-5830/5831/5832 and PXIe-5842 VST with 54 GHz Frequency Extension, you must first use the [Active Channel](pnirfsg-activechannel.html) property to specify the name of the channel you are configuring. You can configure LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

**Related Topics**

[LO OUT](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=GUID-B94B8CEE-C212-4F12-9A4E-FBCEFE951708)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Out Power (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-oscillatorphasevalue.html language=enus -->
## TOPIC 00067: Clock:Advanced:Arb Oscillator Phase DAC Value

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-oscillatorphasevalue.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-oscillatorphasevalue.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the oscillator phase digital-to-analog converter (DAC) value on the arbitrary waveform generator (AWG). Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing a previous

### Clock:Advanced:Arb Oscillator Phase DAC Value

Specifies the oscillator phase digital-to-analog converter (DAC) value on the arbitrary waveform generator (AWG). Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing a previous measurement's phase DAC value to the current session. This property is applicable only when the [Arb Sample Clock Source](/csh?topicname=pnirfsg-arbsampleclocksource.html) property is set to ClkIn.

**Supported Devices**: PXIe-5673/5673E

**Related Topics**

[NI-TClk Overview](https://ni.com/docs/en-US/csh?pubname=ni-tclk&topicname=ni-tclk-overview)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Arb Oscillator Phase DAC Value |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-p2pendpointfullnessstarttriggerlevel.html language=enus -->
## TOPIC 00068: Triggers:Start:P2P Endpoint Fullness:Level

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-p2pendpointfullnessstarttriggerlevel.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-p2pendpointfullnessstarttriggerlevel.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples needed to be received by the endpoint before the device starts generation. This property applies only when the Start Trigger Type property is set to P2P Endpoint Fullness. Supported Devices: PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842 Default Value: -1, which

### Triggers:Start:P2P Endpoint Fullness:Level

Specifies the number of samples needed to be received by the endpoint before the device starts generation. This property applies only when the [Start Trigger Type](/csh?topicname=pnirfsg-starttrig-type.html) property is set to P2P Endpoint Fullness.

**Supported Devices**: PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

**Default Value**: -1, which allows NI-RFSG to select the appropriate fullness level.

**Related Topics**

[Start Trigger](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=ni-rfsg-start-trigger)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | StartTrig.P2PEndpointFullness.Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSG Configure Start Trigger P2P Endpoint Fullness |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-p2pspaceavailableinendpoint.html language=enus -->
## TOPIC 00069: Peer-to-Peer:Space Available In Endpoint

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-p2pspaceavailableinendpoint.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-p2pspaceavailableinendpoint.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current space available in the endpoint in samples per channel. You can use this property when priming the endpoint with initial data through the niRFSG Write P2P Endpoint (I16) VI to determine how many samples you can write. You can also use this property to characterize the performance

### Peer-to-Peer:Space Available In Endpoint

Returns the current space available in the endpoint in samples per channel. You can use this property when priming the endpoint with initial data through the [niRFSG Write P2P Endpoint (I16)](/csh?context=nirfsg_lvrfsg_nirfsg_write_p2p_endpoint_(i16)) VI to determine how many samples you can write. You can also use this property to characterize the performance and measure the latency of the peer-to-peer stream as data moves across the bus. This property is endpoint-based.

**Supported Devices**: PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

**Related Topics**

[Configuring a Peer-to-Peer Endpoint](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=configuring-a-peer-to-peer-endpoint)

[Starting Peer-to-Peer Generation](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=starting-peer-to-peer-generation)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | P2P Space Available In Endpoint |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-scripttrig-diglevel-source.html language=enus -->
## TOPIC 00070: Triggers:Script:Digital Level:Source

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-scripttrig-diglevel-source.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-scripttrig-diglevel-source.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the Script Trigger. This property is used when the Script Trigger Type property is set to Digital Level. Supported Devices: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Related Topics Script Trigger PFI Lines

### Triggers:Script:Digital Level:Source

Specifies the source terminal for the Script Trigger. This property is used when the [Script Trigger Type](/csh?topicname=pnirfsg-scripttrig-type.html) property is set to Digital Level.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Script Trigger](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=ni-rfsg-script-trigger)

[PFI Lines](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=pfi-lines)

[PXI Trigger Lines](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=pxi-trigger-lines)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ScriptTrig.DigLevel.Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSG Configure Trigger |
| Channel-based | Yes |
| Resettable | Yes |

| PFI0 | PFI0 | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0. |
| --- | --- | --- |
| PFI1 | PFI1 | The trigger is received on PFI 1. |
| PFI2 | PFI2 | The trigger is received on PFI 2. |
| PFI3 | PFI3 | The trigger is received on PFI 3. |
| PXI_Trig0 | PXI_Trig0 | The trigger is received on PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | The trigger is received on PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | The trigger is received on PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | The trigger is received on PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | The trigger is received on PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | The trigger is received on PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | The trigger is received on PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | The trigger is received on PXI trigger line 7. |
| PXI_Star | PXI_Star | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. |
| PXIe_DStarB | PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| PulseIn | PulseIn | The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842. |
| DIO/PFI0 | DIO/PFI0 | The signal is exported to the PFI 0 on the DIO front panel connector |
| DIO/PFI1 | DIO/PFI1 | The signal is exported to the PFI 1 on the DIO front panel connector |
| DIO/PFI2 | DIO/PFI2 | The signal is exported to the PFI 2 on the DIO front panel connector |
| DIO/PFI3 | DIO/PFI3 | The signal is exported to the PFI 3 on the DIO front panel connector |
| DIO/PFI4 | DIO/PFI4 | The signal is exported to the PFI 4 on the DIO front panel connector |
| DIO/PFI5 | DIO/PFI5 | The signal is exported to the PFI 5 on the DIO front panel connector |
| DIO/PFI6 | DIO/PFI6 | The signal is exported to the PFI 6 on the DIO front panel connector |
| DIO/PFI7 | DIO/PFI7 | The signal is exported to the PFI 7 on the DIO front panel connector |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-selectedpath.html language=enus -->
## TOPIC 00071: Device Specific:Vector Signal Transceiver:Signal Path:Selected Path:Selected Path

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-selectedpath.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-selectedpath.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which path to configure to generate a signal. Related Topics Available Paths property Remarks The following table lists the characteristics of this property. Short Name Selected Path Data type cstr.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes

### Device Specific:Vector Signal Transceiver:Signal Path:Selected Path:Selected Path

Specifies which path to configure to generate a signal.

**Related Topics**

[Available Paths](pnirfsg-availablepaths.html) property

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Selected Path |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-selectedports.html language=enus -->
## TOPIC 00072: Device Specific:Vector Signal Transceiver:Signal Path:Selected Ports

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-selectedports.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-selectedports.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the port to configure. When using RF list mode, ports cannot be shared with NI-RFSA. Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Default Value: PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: "" (empty string) PXIe-5830/5831/5832: if0 PXIe-5842

### Device Specific:Vector Signal Transceiver:Signal Path:Selected Ports

Specifies the port to configure.

Note

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Default Value**:

PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: "" (empty string)

PXIe-5830/5831/5832: if0

PXIe-5842 VST with 54 GHz Frequency Extension: rmm0/port0

**Valid Values**:

PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: "" (empty string)

PXIe-5830: if0, if1

PXIe-5831/5832: if0, if1, rf*<0-1>*/port*<x>*, where *0-1* indicates one (*0*) or two (*1*) mmRH-5582 connections and *x* is the port number on the mmRH-5582 front panel.

PXIe-5842 VST with 54 GHz Frequency Extension: rfinout0, rfinout1, rmm0/port0, rmm0/port1

**Related Topics**

[Available Ports](pnirfsg-availableports.html) property

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Selected Ports |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-selectedscript.html language=enus -->
## TOPIC 00073: Arb:Selected Script

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-selectedscript.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-selectedscript.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the script in onboard memory to generate upon calling the niRFSG Initiate VI when the Generation Mode property is set to Script. The Selected Script property is ignored when the Generation Mode property is set to Arb Waveform or CW. To set the Selected Script property, the NI-RFSG device m

### Arb:Selected Script

Specifies the script in onboard memory to generate upon calling the [niRFSG Initiate](/csh?context=nirfsg_lvrfsg_nirfsg_initiate) VI when the [Generation Mode](/csh?topicname=pnirfsg-generationmode.html) property is set to Script. The Selected Script property is ignored when the Generation Mode property is set to Arb Waveform or CW.

To set the Selected Script property, the NI-RFSG device must be in the Configuration state.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Assigning Properties or Attributes to a Waveform](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=assigning-properties-or-attributes-to-a-wavef)

[Scripting Instructions](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=scripting-instructions)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Selected Script |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-serialnumber.html language=enus -->
## TOPIC 00074: Device Characteristics:Serial Number

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-serialnumber.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-serialnumber.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the serial number of the RF module. If the NI-RFSG session is controlling multiple modules, this property returns the serial number of the primary RF module. Supported Devices: PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/567

### Device Characteristics:Serial Number

Returns the serial number of the RF module. If the NI-RFSG session is controlling multiple modules, this property returns the serial number of the primary RF module.

**Supported Devices**: PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Serial Number |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-signalbandwidth-hz.html language=enus -->
## TOPIC 00075: Arb:Signal Bandwidth (Hz)

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-signalbandwidth-hz.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-signalbandwidth-hz.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8 Ã— I/Q rate). NI-RFSG defines signal bandwidth as twice the maximum I/Q signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the bandwidth is simply the I/Q sig

### Arb:Signal Bandwidth (Hz)

Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8 Ã— I/Q rate).

NI-RFSG defines *signal bandwidth* as twice the maximum I/Q signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the bandwidth is simply the I/Q signal's minimum frequency subtracted from its maximum frequency or *f*
<sub>max</sub> - *f*
<sub>min</sub>.

This property applies only when the [Generation Mode](pnirfsg-generationmode.html) property is set to Arb Waveform or Script, except for when using the PXIe-5830/5831/5832/5840/5841/5842/5860, which supports setting this property in all supported generation modes. To set the Signal Bandwidth property, the NI-RFSG device must be in the Configuration state.

PXI-5670/5671, PXIe-5672: Based on your signal bandwidth, NI-RFSG decides whether to configure the upconverter center frequency in increments of 1 MHz or 5 MHz. Failure to configure this property may result in the signal being placed outside the upconverter passband.

PXIe-5644/5645/5646, PXIe-5673/5673E: This property is used only for error checking purposes. Otherwise, this property is ignored.

PXIe-5820/5830/5831/5832/5840/5841/5842/5860: Based on your signal bandwidth, NI-RFSG decides the equalized bandwidth. If this property is not set, NI-RFSG uses the maximum available signal bandwidth. For the PXIe-5840/5841/5842/5860, the maximum allowed signal bandwidth depends on the upconverter center frequency. Refer to the specifications document for your device for more information about signal bandwidth. The device specifications depend on the signal bandwidth.

**Supported Devices**: PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Phase-Locked Loop Bandwidth](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=phase-locked-loop-bandwidth)

[Frequency Tuning Times](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=frequency-tuning-times)

[PXIe-5830 Frequency and Bandwidth Selection](https://ni.com/docs/en-US/csh?pubname=pxie-5830-feature&topicname=frequency-and-bandwidth-selection)

[PXIe-5831/5832 Frequency and Bandwidth Selection](https://ni.com/docs/en-US/csh?pubname=pxie-5831&topicname=frequency-and-bandwidth-selection)

[PXIe-5841 Frequency and Bandwidth Selection](https://ni.com/docs/en-US/csh?pubname=pxie-5841&topicname=frequency-and-bandwidth-selection)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Signal Bandwidth (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-simulate.html language=enus -->
## TOPIC 00076: Inherent IVI Attributes:User Options:Simulate

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-simulate.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-simulate.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether NI-RFSG simulates I/O operations. This property is useful for debugging applications without using hardware. After a session is opened, you cannot change the simulation state. Call the niRFSG Initialize With Options VI to enable simulation. Supported Devices: PXI-5610, PXIe-5611, P

### Inherent IVI Attributes:User Options:Simulate

Specifies whether NI-RFSG simulates I/O operations. This property is useful for debugging applications without using hardware. After a session is opened, you cannot change the simulation state. Call the [niRFSG Initialize With Options](/csh?context=nirfsg_lvrfsg_nirfsg_initialize_with_options) VI to enable simulation.

**Supported Devices**: PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

| TRUE | Simulation is enabled. |
| --- | --- |
| FALSE | Simulation is disabled. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Simulate |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-spaceavailinstreamingwfm.html language=enus -->
## TOPIC 00077: Arb:Data Transfer:Streaming:Space Available In Streaming Waveform (Samples)

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-spaceavailinstreamingwfm.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-spaceavailinstreamingwfm.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the space available, in samples, in the streaming waveform for writing new data. For optimal performance, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform. This waveform size ensures that writes do not have to wrap around

### Arb:Data Transfer:Streaming:Space Available In Streaming Waveform (Samples)

Indicates the space available, in samples, in the streaming waveform for writing new data. For optimal performance, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform. This waveform size ensures that writes do not have to wrap around from the end to the beginning of the waveform buffer.

To read this property, the NI-RFSG device must be in the Committed state.

**Supported Devices**: PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Streaming](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=streaming)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SpaceAvailInStreamingWfm |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-streamingenabled.html language=enus -->
## TOPIC 00078: Arb:Data Transfer:Streaming:Streaming Enabled

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-streamingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-streamingenabled.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables continuous streaming of waveform data. Supported Devices: PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Default Value: Disabled Enabled Enables streaming. Disabled Disables streaming. Related Topics Streaming Remarks The following table lists the characterist

### Arb:Data Transfer:Streaming:Streaming Enabled

Enables or disables continuous streaming of waveform data.

**Supported Devices**: PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Default Value**: Disabled

| Enabled | Enables streaming. |
| --- | --- |
| Disabled | Disables streaming. |

**Related Topics**

[Streaming](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=streaming)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Streaming Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-syncsampleclockmaster.html language=enus -->
## TOPIC 00079: Device Specific:Vector Signal Transceiver:Triggers:Sync Sample Clock Master

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-syncsampleclockmaster.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-syncsampleclockmaster.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device is the master device when synchronizing the Sample Clock between multiple devices. The master device distributes the Sample Clock sync signal to all devices in the system through the Sample Clock sync distribution line. When synchronizing the Sample Clock, one device mus

### Device Specific:Vector Signal Transceiver:Triggers:Sync Sample Clock Master

Specifies whether the device is the master device when synchronizing the Sample Clock between multiple devices. The master device distributes the Sample Clock sync signal to all devices in the system through the Sample Clock sync distribution line.

When synchronizing the Sample Clock, one device must always be designated as the master. The master device actively drives the Sample Clock sync distribution line.

To set this property, the NI-RFSG device must be in the Configuration state.

**Supported Devices**: PXIe-5646

**Default Value**: FALSE

| TRUE | The device is the master device for synchronizing the Sample Clock. |
| --- | --- |
| FALSE | The device is not the master device for synchronizing the Sample Clock. |

**Related Topics**

[Synchronization Using NI-RFSA and NI-RFSG](https://ni.com/docs/en-US/csh?pubname=pxie-5644-feature&topicname=synchronization-rfsa-g)—Refer to this topic for more information about PXIe-5646 device synchronization.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sync Sample Clock Master |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-syncscripttriggerdistline.html language=enus -->
## TOPIC 00080: Device Specific:Vector Signal Transceiver:Triggers:Sync Script Trigger Dist Line

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-syncscripttriggerdistline.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-syncscripttriggerdistline.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which external trigger line distributes the synchronized Script Trigger signal. Use the Active Channel property to specify the name of the Script Trigger you are configuring. When synchronizing the Script Trigger, configure all devices to use the same Script Trigger distribution line. To s

### Device Specific:Vector Signal Transceiver:Triggers:Sync Script Trigger Dist Line

Specifies which external trigger line distributes the synchronized Script Trigger signal. Use the [Active Channel](/csh?topicname=pnirfsg-activechannel.html) property to specify the name of the Script Trigger you are configuring. When synchronizing the Script Trigger, configure all devices to use the same Script Trigger distribution line.

To set this property, the NI-RFSG device must be in the Configuration state.

**Supported Devices**: PXIe-5644/5645/5646

**Default Value**: "" (empty string)

**Valid Values**: PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

**Related Topics**

[Script Trigger](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=ni-rfsg-script-trigger)

[Synchronizing Sample Clock and Sampled Reference Clock Signals](https://ni.com/docs/en-US/csh?pubname=pxie-5644-feature&topicname=sample-clock-sync)

Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sync Script Trigger Dist Line |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-syncscripttriggermaster.html language=enus -->
## TOPIC 00081: Device Specific:Vector Signal Transceiver:Triggers:Sync Script Trigger Master

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-syncscripttriggermaster.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-syncscripttriggermaster.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device is the master device when synchronizing the Script Trigger between multiple devices. Use the Active Channel property to specify the name of the Script Trigger you are configuring. The master device distributes the synchronized Script Trigger to all devices in the system

### Device Specific:Vector Signal Transceiver:Triggers:Sync Script Trigger Master

Specifies whether the device is the master device when synchronizing the Script Trigger between multiple devices. Use the [Active Channel](/csh?topicname=pnirfsg-activechannel.html) property to specify the name of the Script Trigger you are configuring.

The master device distributes the synchronized Script Trigger to all devices in the system through the Script Trigger distribution line.

When synchronizing the Script Trigger, one device must always be designated as the master. The master device actively drives the Script Trigger distribution line. For slave devices, set the [Script Trigger Type](pnirfsg-scripttrig-type.html) property to **Digital Edge**, and set the [Script Trigger Digital Edge Source](pnirfsg-starttrig-digedge-source.html) property to sync_script.

To set this property, the NI-RFSG device must be in the Configuration state.

**Supported Devices**: PXIe-5644/5645/5646

**Default Value**: FALSE

| TRUE | The device is the master device for synchronizing the Script Trigger. |
| --- | --- |
| FALSE | The device is not the master device for synchronizing the Script Trigger. |

**Related Topics**

[Script Trigger](https://ni.com/docs/en-US/csh?pubname=ni-rfsg&topicname=ni-rfsg-script-trigger)

[Synchronizing Sample Clock and Sampled Reference Clock Signals](https://ni.com/docs/en-US/csh?pubname=pxie-5644-feature&topicname=sample-clock-sync)

Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sync Script Trigger Master |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niRFSG Properties

<!--NI_TOPIC bundle=rfsg-labview-api-ref path=instr-lib/nirfsg/pnirfsg-upconverterfrequencyoffset-hz.html language=enus -->
## TOPIC 00082: Device Specific:Vector Signal Transceiver:Upconverter:Frequency Offset (Hz)

- bundle_id: `rfsg-labview-api-ref`
- source_path: `instr-lib/nirfsg/pnirfsg-upconverterfrequencyoffset-hz.html`
- source_url: https://docs-be.ni.com/bundle/rfsg-labview-api-ref/raw/resource/enus/instr-lib/nirfsg/pnirfsg-upconverterfrequencyoffset-hz.html
- document_id: `rfsg-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property offsets the Upconverter Center Frequency (Hz) from the RF frequency. Use this property to keep the local oscillator (LO) leakage at a determined offset from the RF signal. You cannot set the Upconverter Center Frequency (Hz) property or the Arb Carrier Frequency (Hz) property at the sa

### Device Specific:Vector Signal Transceiver:Upconverter:Frequency Offset (Hz)

This property offsets the [Upconverter Center Frequency (Hz)](/csh?topicname=pnirfsg-upconvertercenterfrequency-hz.html) from the RF frequency. Use this property to keep the local oscillator (LO) leakage at a determined offset from the RF signal.

Note

Arb Carrier Frequency (Hz)

Note

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

**Valid Values**:

PXIe-5644/5645: -42 MHz to +42 MHz

PXIe-5646: -100 MHz to +100 MHz

PXIe-5830/5831/5832/5840: -500 MHz to +500 MHz

PXIe-5841 (200 MHz bandwidth option): -100 MHz to +100 MHz

PXIe-5841 (1 GHz bandwidth option): -500 MHz to +500 MHz

PXI-5842 (500 MHz bandwidth option): -250 MHz to +250 MHz

PXI-5842 (1 GHz bandwidth option): -500 MHz to +500 MHz

PXI-5842 (2 GHz bandwidth option): -1 GHz to +1 GHz

PXI-5842 (4 GHz bandwidth option) using the Standard personality: -1 GHz to +1 GHz

PXI-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality: -2 GHz to +2 GHz

**Related Topics**

[PXIe-5830 Frequency and Bandwidth Selection](https://ni.com/docs/en-US/csh?pubname=pxie-5830-feature&topicname=frequency-and-bandwidth-selection)

[PXIe-5831/5832 Frequency and Bandwidth Selection](https://ni.com/docs/en-US/csh?pubname=pxie-5831&topicname=frequency-and-bandwidth-selection)

[PXIe-5841 Frequency and Bandwidth Selection](https://ni.com/docs/en-US/csh?pubname=pxie-5841&topicname=frequency-and-bandwidth-selection)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Upconverter Frequency Offset (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSG Properties
