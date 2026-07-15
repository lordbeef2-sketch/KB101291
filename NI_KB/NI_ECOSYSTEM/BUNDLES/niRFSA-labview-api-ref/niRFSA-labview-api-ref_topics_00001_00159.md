# NI DOCUMENT BUNDLE: niRFSA-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=niRFSA-labview-api-ref start=1 end=159 -->
<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/acquisition-mnu.html language=enus -->
## TOPIC 00001: Acquisition

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/acquisition-mnu.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/acquisition-mnu.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-RFSA Acquisition VIs to control acquisition operations with your vector signal analyzer. icon

### Acquisition

Use the NI-RFSA Acquisition VIs to control acquisition operations with your vector signal analyzer.

[IMAGE alt='icon' src='acquisition-mnu.png']

- [niRFSA Read Power Spectrum (Cluster) VI](../../instr-lib/nirfsa/nirfsa-llb/nirfsa-read-power-spectrum-cluster-vi.html) Initiates a spectrum acquisition and returns power spectrum data.
- [niRFSA Read IQ VI](../../instr-lib/nirfsa/nirfsa-llb/nirfsa-read-iq-vi.html) Initiates an acquisition and fetches a single I/Q data record. Do not use this VI if you have configured the device to continuously acquire data samples or to acquire multiple records.
- [niRFSA Initiate VI](../../instr-lib/nirfsa/nirfsa-llb/nirfsa-initiate-vi.html) Commits settings to hardware, waits for hardware settling, and starts an acquisition. You can use this VI in conjunction with the niRFSA Fetch IQ VI to retrieve acquired I/Q data, or you can use the niRFSA Read IQ VI to both initiate the acquisition and retrieve I/Q data at one time.
- [niRFSA Fetch IQ VI](../../instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-vi.html) Transfers acquired waveform data from device memory to computer memory; this process is also known as fetching. The data transferred was acquired to onboard memory previously by the hardware after the acquisition was initiated.
- [niRFSA Abort VI](../../instr-lib/nirfsa/nirfsa-llb/nirfsa-abort-vi.html) Stops an acquisition previously started with the niRFSA Initiate VI or the niRFSA Read Power Spectrum (Cluster) VI. You can also use the niRFSA Abort VI to stop a self calibration. Calling this VI is optional, unless you want to stop an acquisition before it is complete or you are continuously acquiring data.

Parent topic:

NI-RFSA

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/calibration-control-5601-mnu.html language=enus -->
## TOPIC 00002: NI 5601

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/calibration-control-5601-mnu.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/calibration-control-5601-mnu.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI 5601 VIs to access PXIe-5601-specific calibration features of NI-RFSA. Supported Devices: PXIe-5601 icon

### NI 5601

Use the NI 5601 VIs to access PXIe-5601-specific calibration features of NI-RFSA.

**Supported Devices**: PXIe-5601

[IMAGE alt='icon' src='calibration-control-5601-mnu.png']

- [niRFSA Cal Adjust Reference Level Calibration VI](../../instr-lib/nirfsa/nirfsa-llb/nirfsa-cal-adjust-reference-level-calibration-vi.html) Writes the reference level calibration data settings to the driver.
- [niRFSA Cal Adjust IF Response Calibration VI](../../instr-lib/nirfsa/nirfsa-llb/nirfsa-cal-adjust-if-response-calibration-vi.html) Specifies the IF response settings.
- [niRFSA Cal Adjust IF Attenuation Calibration VI](../../instr-lib/nirfsa/nirfsa-llb/nirfsa-cal-adjust-if-attenuation-calibration-vi.html) Specifies the IF attenuation settings.
- [niRFSA Cal Set Temperature VI](../../instr-lib/nirfsa/nirfsa-llb/nirfsa-cal-set-temperature-vi.html) Writes the calibration temperature to the driver.

Parent topic:

Calibration Control

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/calibration-control-5698-mnu.html language=enus -->
## TOPIC 00003: NI 5698

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/calibration-control-5698-mnu.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/calibration-control-5698-mnu.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI 5698 VI to access PXIe-5698-specific calibration features of NI-RFSA. Supported Devices: PXIe-5698 icon

### NI 5698

Use the NI 5698 VI to access PXIe-5698-specific calibration features of NI-RFSA.

**Supported Devices**: PXIe-5698

[IMAGE alt='icon' src='calibration-control-5698-mnu.png']

- [niRFSA Cal Adjust Device Gain VI](../../instr-lib/nirfsa/nirfsa-llb/nirfsa-cal-adjust-device-gain-vi.html) Records measured gain information that is gathered during the Reference Level Calibration step and IF Attenuation Calibration step.

Parent topic:

Calibration Control

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-close-ext-cal-vi.html language=enus -->
## TOPIC 00004: niRFSA Close Ext Cal VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-close-ext-cal-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-close-ext-cal-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an NI-RFSA external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM. Supported Devices: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/

### niRFSA Close Ext Cal VI

Closes an NI-RFSA external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM.

**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-close-ext-cal-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your calibration instrument session. instrument handle is obtained from the niRFSA Init Ext Cal VI. action — action specifies how to use the calibration values from this session as the session is closed. Abort (1500) The old calibration constants are kept, and the new ones are discarded. This is the default behavior. Commit (1501) The new calibration constants are stored in the EEPROM. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. So if an error was contained in error in and this VI also produces an error, error out contains the same information as error in. For all other cases, this output provides standard error out functionality. |  |
| --- | --- |
| Abort (1500) | The old calibration constants are kept, and the new ones are discarded. This is the default behavior. |
| Commit (1501) | The new calibration constants are stored in the EEPROM. |

Parent topic:

Calibration

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-close-external-alignment-step-vi.html language=enus -->
## TOPIC 00005: niRFSA Close External Alignment Step VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-close-external-alignment-step-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-close-external-alignment-step-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an EEPROM-specific external alignment step opened by the niRFSA Initialize External Alignment Step VI. Supported Devices: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only) icon Inputs/Outputs civrn.png instrument handle instrument handle identifies your external alignment session. instru

### niRFSA Close External Alignment Step VI

Closes an EEPROM-specific external alignment step opened by the [niRFSA Initialize External Alignment Step](/csh?topicname=nirfsa-initialize-external-alignment-step-vi.html) VI.

**Supported Devices**: PXIe-5605 (PXIe-5665 only), PXIe-5606 (PXIe-5668 only)

[IMAGE alt='icon' src='nirfsa-close-external-alignment-step-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your external alignment session. instrument handle is obtained from the niRFSA Initialize External Alignment VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize External Alignment VI. error out — error out contains error information. So if an error was contained in error in and this VI also produces an error, error out contains the same information as error in. For all other cases, this output provides standard error out functionality. |
| --- |

Parent topic:

Calibration Control

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-de-embedding-table-interpolation-spline-vi.html language=enus -->
## TOPIC 00006: niRFSA Configure De-embedding Table Interpolation (Spline) VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-de-embedding-table-interpolation-spline-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-de-embedding-table-interpolation-spline-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the spline interpolation method. If the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a spline interpolation based on the entries in the de-embedding table to determine the parameters used for de-embedding. Supported Devices: PXIe-5830/5831/5832/5840/5841

### niRFSA Configure De-embedding Table Interpolation (Spline) VI

Selects the spline interpolation method.

If the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a spline interpolation based on the entries in the de-embedding table to determine the parameters used for de-embedding.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-configure-de-embedding-table-interpolation-spline-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. port — port specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string). table name — table name specifies the name of the table. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSA Configure De-embedding Table Interpolation VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-de-embedding-table-interpolation-vi.html language=enus -->
## TOPIC 00007: niRFSA Configure De-embedding Table Interpolation VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-de-embedding-table-interpolation-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-de-embedding-table-interpolation-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the interpolation method to use when interpolating parameters from the de-embedding table. Linear interpolation is the default. Supported Devices: PXIe-5830/5831/5832/5840/5841/5842/5860 icon

### niRFSA Configure De-embedding Table Interpolation VI

Specifies the interpolation method to use when interpolating parameters from the de-embedding table. Linear interpolation is the default.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-configure-de-embedding-table-interpolation-vi.png']

- [niRFSA Configure De-embedding Table Interpolation (Nearest) VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-de-embedding-table-interpolation-nearest-vi.html) Selects the nearest interpolation method.
- [niRFSA Configure De-embedding Table Interpolation (Linear) VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-de-embedding-table-interpolation-linear-vi.html) Selects the linear interpolation method.
- [niRFSA Configure De-embedding Table Interpolation (Spline) VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-de-embedding-table-interpolation-spline-vi.html) Selects the spline interpolation method.

Parent topic:

De-embedding

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-number-of-samples-vi.html language=enus -->
## TOPIC 00008: niRFSA Configure Number of Samples VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-number-of-samples-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-number-of-samples-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of samples in a finite acquisition or configures the device to continuously acquire samples. Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Related Topics I/Q Modulation icon Inputs/Outputs civrn.pn

### niRFSA Configure Number of Samples VI

Configures the number of samples in a finite acquisition or configures the device to
 continuously acquire samples.

**Supported Devices**: PXIe-5644/5645/5646, 
 PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[I/Q Modulation](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=iq-modulation)

[IMAGE alt='icon' src='nirfsa-configure-number-of-samples-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. number of samples is finite — number of samples is finite specifies whether to configure the device to acquire a finite number of samples or to acquire samples continuously. The default value is TRUE. TRUE The NI-RFSA device acquires a finite number of samples. FALSE The NI-RFSA device continuously acquires samples until you call the niRFSA Abort VI to abort the acquisition. samples per record — samples per record specifies the number of samples per record if number of samples is finite is set to TRUE. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE | The NI-RFSA device acquires a finite number of samples. |
| FALSE | The NI-RFSA device continuously acquires samples until you call the niRFSA Abort VI to abort the acquisition. |

#### Details

If you configure the device for finite acquisition, it acquires the specified number
 of samples and then stops the acquisition. You can configure the device to acquire multiple records using the [niRFSA Configure Number of Records](nirfsa-configure-number-of-records-vi.html) VI. Each
 record contains the number of samples specified in this VI. The default number of records to acquire is 1.

If you configure the device to continuously acquire samples, it continues acquiring
 data until you call the [niRFSA Abort](nirfsa-abort-vi.html) VI to abort the acquisition. The device stores
 data in onboard memory in a circular fashion. After the device fills the memory, it
 starts overwriting previously acquired data from the beginning of the memory buffer.
 Retrieve the samples as they are being acquired using the [niRFSA Fetch IQ](nirfsa-fetch-iq-vi.html) VI to avoid overwriting data before you retrieve it.

Parent topic:

IQ

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-pxi-chassis-clk10-vi.html language=enus -->
## TOPIC 00009: niRFSA Configure PXI Chassis Clk10 VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-pxi-chassis-clk10-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-pxi-chassis-clk10-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. This option can be configured only when the PXI-5600 is installed in the Star Trigger Controller Slot, also known as the System Timing Slot, of the PXI chassis. Supported Devices: PXI-5600 (external digitizer mode), PXI-5

### niRFSA Configure PXI Chassis Clk10 VI

Specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. This
 option can be configured only when the PXI-5600 is installed in the Star Trigger Controller Slot, also known as the System Timing Slot, of the PXI chassis.

**Supported Devices**: PXI-5600 (external digitizer mode), PXI-5661

**Related Topics**

[System Reference Clock](/csh?context=nirfsa_nirfsa_system-reference-clock)

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

[Events](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=events)

[IMAGE alt='icon' src='nirfsa-configure-pxi-chassis-clk10-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. PXI Clk10 source — PXI Clk10 source specifies the signal to drive the 10 MHz Reference Clock on the PXI backplane. This option can only be configured when the PXI-5600 is in Slot 2 of the PXI chassis. None The device does not drive the PXI 10 MHz backplane Reference clock. OnboardClock The device drives the PXI 10 MHz backplane Reference Clock with the PXI-5600 onboard clock. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O on the PXI-5600 front panel to use this option. RefIn The device drives the PXI 10 MHz backplane Reference Clock with the reference source attached to the PXI-5600 REF IN connector. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O on the PXI-5600 front panel to use this option. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| None | The device does not drive the PXI 10 MHz backplane Reference clock. |
| OnboardClock | The device drives the PXI 10 MHz backplane Reference Clock with the PXI-5600 onboard clock. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O on the PXI-5600 front panel to use this option. |
| RefIn | The device drives the PXI 10 MHz backplane Reference Clock with the reference source attached to the PXI-5600 REF IN connector. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O on the PXI-5600 front panel to use this option. |

Parent topic:

Clock

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-ref-clock-vi.html language=enus -->
## TOPIC 00010: niRFSA Configure Ref Clock VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-ref-clock-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-ref-clock-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the NI-RFSA device Reference Clock. Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Related Topics PXI-5661 Reference Clocking PXIe-5663

### niRFSA Configure Ref Clock VI

Configures the NI-RFSA device Reference Clock.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[PXI-5661 Reference Clocking](https://ni.com/docs/en-US/csh?pubname=pxi-5661-feature&topicname=reference-clock)

[PXIe-5663 Timing Configurations](https://ni.com/docs/en-US/csh?pubname=pxie-5663-5663e-feature&topicname=timing-configurations)

[PXIe-5665 Timing Configurations](https://ni.com/docs/en-US/csh?pubname=pxie-5665-feature&topicname=timing-configurations)

[PXIe-5667 Timing Configurations](https://ni.com/docs/en-US/csh?pubname=pxie-5667-feature&topicname=timing-configurations)

[PXIe-5668 Timing Configurations](https://ni.com/docs/en-US/csh?pubname=pxie-5668-feature&topicname=timing-configurations)

[PXIe-5830 Timing Configurations](https://ni.com/docs/en-US/csh?pubname=pxie-5830-feature&topicname=timing-configurations)

[PXIe-5831/5832 Timing Configurations](https://ni.com/docs/en-US/csh?pubname=pxie-5831&topicname=timing-configurations)

[IMAGE alt='icon' src='nirfsa-configure-ref-clock-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. clock source — clock source specifies the Reference Clock source. OnboardClock PXI-5661â€”Lock the NI-RFSA device to the PXI-5600 RF downconverter onboard clock. PXIe-5663/5663Eâ€”Lock the PXIe-5663/5663E to the PXI/PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN connector on the PXIe-5622. If the REF OUT2 connector does not exist, connect the REF IN/OUT connector on the PXI/PXIe-5652 to the CLK IN connector on the PXIe-5622. PXIe-5665â€”Lock the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622. PXIe-5667â€”Lock the PXIe-5667 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. PXIe-5668â€”Lock the PXIe-5668 to the PXIe-5653 LO source onboard clock. Connect the LO2 OUT terminal on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841â€”Lock the NI-RFSA device to its onboard clock. PXIe-5830/5831/5832â€”For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5841 with PXIe-5655â€”Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. PXIe-5842â€”Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860â€”Lock to the PXIe-5860 onboard clock. RefIn PXI-5661â€”Lock the NI-RFSA device to the signal at the external FREQ REF IN connector on the PXI-5600. PXIe-5663/5663Eâ€”Connect the external signal to the PXI/PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN connector on the PXIe-5622. On versions of the 5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, this configuration can only be used in external digitizer mode. PXIe-5665â€”Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the clock rate parameter according to the frequency of your external clock signal. PXIe-5667â€”Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. If your external clock signal frequency is set to a frequency other than 10 MHz, set the clock rate parameter according to the frequency of your external clock signal. PXIe-5668â€”Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT terminal on the PXIe-5606 to the CLK IN connector on the PXIe-5624. If your external clock signal frequency is set to a frequency other than 10 MHz, set the clock rate parameter according to the frequency of your external clock signal. PXIe-5694—Connect the Reference Clock signal to the REF/LO IN connector on the PXIe-5694 front panel. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841â€”Lock the NI-RFSA device to the signal at the external REF IN connector. PXIe-5830/5831/5832â€”For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For the PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5841 with PXIe-5655â€”Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. PXIe-5842â€”Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860â€”Lock to the signal at the REF IN connector on the PXIe-5860. ClkIn PXIe-5663/5663Eâ€”Lock the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXI/PXIe-5652. PXIe-5665â€”Lock the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the clock rate parameter to 100 MHz. PXIe-5667â€”Lock the PXIe-5667 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Connect the 10 MHZ REF OUT connector on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. Set the clock rate parameter to 100 MHz. PXIe-5668â€”Lock the PXIe-5668 to an external 10 MHz or 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the clock rate parameter to 10 MHz or 100 MHz, as appropriate. PXIe-5644/5645/5646, PXI-5661, PXIe-5820/5830/5831/5832/5840/5840 with PXIe-5653/5841/5841 with PXIe-5655/5842/5860â€”This configuration does not apply. PXI_Clk PXI-5661â€”Lock the NI-RFSA device to the PXI backplane clock using the PXI-5600. You must connect the PXI 10 MHz connector to the REF IN connector on the PXI-5600 front panel to use this option. PXIe-5668â€”Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 Out connector to the CLK IN connector on the PXIe-5624. PXIe-5830/5831/5832/5841 with PXIe-5655/5842â€”Lock LO module to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667, PXIe-5694, PXIe-5820/5840/5841/5842/5860â€”Lock the NI-RFSA device to the PXI backplane clock. RefIn2 PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5841 with PXIe-5655/5842/5860â€”This configuration does not apply. PXI_ClkMaster PXIe-5831 with PXIe-5653â€”NI-RFSA configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653â€”NI-RFSA configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5841 with PXIe-5655/5842/5860â€”This configuration does not apply. clock rate — clock rate specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. This parameter is only valid when the clock source parameter is set to ClkIn, RefIn, or RefIn2. The default value is 10 MHz. For the PXIe-5644/5645/5646, PXIe-5601/5663, PXIe-5694, and the PXIe-5820/5830/5831/5832/5840/5841, 10 MHz is the only supported value. For the PXIe-5665/5667/5668, you can specify values between 5 MHz and 100 MHz, in increments of 1 MHz. For the PXIe-5841 with PXIe-5655, and the PXIe-5842, you can specify the following values: 10 MHz, 100 MHz, 270 MHz, and 3.84 MHz * y, where y is 4, 8, 16, 24, 25, or 32. For the PXIe-5860, you can specify the following values: 10 MHz, 100 MHz error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| OnboardClock | PXI-5661â€”Lock the NI-RFSA device to the PXI-5600 RF downconverter onboard clock. PXIe-5663/5663Eâ€”Lock the PXIe-5663/5663E to the PXI/PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN connector on the PXIe-5622. If the REF OUT2 connector does not exist, connect the REF IN/OUT connector on the PXI/PXIe-5652 to the CLK IN connector on the PXIe-5622. PXIe-5665â€”Lock the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622. PXIe-5667â€”Lock the PXIe-5667 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. PXIe-5668â€”Lock the PXIe-5668 to the PXIe-5653 LO source onboard clock. Connect the LO2 OUT terminal on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841â€”Lock the NI-RFSA device to its onboard clock. PXIe-5830/5831/5832â€”For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5841 with PXIe-5655â€”Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. PXIe-5842â€”Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860â€”Lock to the PXIe-5860 onboard clock. |
| RefIn | PXI-5661â€”Lock the NI-RFSA device to the signal at the external FREQ REF IN connector on the PXI-5600. PXIe-5663/5663Eâ€”Connect the external signal to the PXI/PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN connector on the PXIe-5622. On versions of the 5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, this configuration can only be used in external digitizer mode. PXIe-5665â€”Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the clock rate parameter according to the frequency of your external clock signal. PXIe-5667â€”Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. If your external clock signal frequency is set to a frequency other than 10 MHz, set the clock rate parameter according to the frequency of your external clock signal. PXIe-5668â€”Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT terminal on the PXIe-5606 to the CLK IN connector on the PXIe-5624. If your external clock signal frequency is set to a frequency other than 10 MHz, set the clock rate parameter according to the frequency of your external clock signal. PXIe-5694—Connect the Reference Clock signal to the REF/LO IN connector on the PXIe-5694 front panel. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841â€”Lock the NI-RFSA device to the signal at the external REF IN connector. PXIe-5830/5831/5832â€”For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For the PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653â€”Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5841 with PXIe-5655â€”Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. PXIe-5842â€”Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860â€”Lock to the signal at the REF IN connector on the PXIe-5860. |
| ClkIn | PXIe-5663/5663Eâ€”Lock the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXI/PXIe-5652. PXIe-5665â€”Lock the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the clock rate parameter to 100 MHz. PXIe-5667â€”Lock the PXIe-5667 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Connect the 10 MHZ REF OUT connector on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. Set the clock rate parameter to 100 MHz. PXIe-5668â€”Lock the PXIe-5668 to an external 10 MHz or 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the clock rate parameter to 10 MHz or 100 MHz, as appropriate. PXIe-5644/5645/5646, PXI-5661, PXIe-5820/5830/5831/5832/5840/5840 with PXIe-5653/5841/5841 with PXIe-5655/5842/5860â€”This configuration does not apply. |
| PXI_Clk | PXI-5661â€”Lock the NI-RFSA device to the PXI backplane clock using the PXI-5600. You must connect the PXI 10 MHz connector to the REF IN connector on the PXI-5600 front panel to use this option. PXIe-5668â€”Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 Out connector to the CLK IN connector on the PXIe-5624. PXIe-5830/5831/5832/5841 with PXIe-5655/5842â€”Lock LO module to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667, PXIe-5694, PXIe-5820/5840/5841/5842/5860â€”Lock the NI-RFSA device to the PXI backplane clock. |
| RefIn2 | PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5841 with PXIe-5655/5842/5860â€”This configuration does not apply. |
| PXI_ClkMaster | PXIe-5831 with PXIe-5653â€”NI-RFSA configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653â€”NI-RFSA configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5841 with PXIe-5655/5842/5860â€”This configuration does not apply. |

Parent topic:

Clock

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-reference-level-vi.html language=enus -->
## TOPIC 00011: niRFSA Configure Reference Level VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-reference-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-reference-level-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level. The reference level represents the maximum expected power of an input RF signal. Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860 Rel

### niRFSA Configure Reference Level VI

Configures the reference level. The reference level represents the maximum expected power of an input RF signal.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Improving Your Measurements](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=improving-your-measurements)

[Programming Attenuation-Related Properties and Attributes Using NI-RFSA](https://ni.com/docs/en-US/csh?pubname=pxie-5665-feature&topicname=programming-attenuation)

[IMAGE alt='icon' src='nirfsa-configure-reference-level-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. reference level (dBm) — reference level specifies the expected total power, in dBm, of the RF input signal. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-spectrum-frequency-center-span-vi.html language=enus -->
## TOPIC 00012: niRFSA Configure Spectrum Frequency Center Span VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-spectrum-frequency-center-span-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-spectrum-frequency-center-span-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the span and center frequency of the spectrum read by NI-RFSA. A spectrum acquisition consists of data surrounding the center frequency. Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-582

### niRFSA Configure Spectrum Frequency Center Span VI

Configures the span and center frequency of the spectrum read by NI-RFSA. A spectrum acquisition consists of data surrounding the center frequency.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-configure-spectrum-frequency-center-span-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. frequency — frequency specifies the center frequency in a spectrum acquisition. The value is expressed in hertz (Hz). The NI-RFSA device you use determines the valid range. Refer to the specifications document for your device for more information about frequency range. span — span specifies the span of a spectrum acquisition. The value is expressed in hertz (Hz). Note For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect measurements. Refer to the Digitizer Dither Enabled property for more information about dithering. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

Note

stop frequency

start frequency

Note

Parent topic:

niRFSA Configure Spectrum Frequency VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-spectrum-frequency-start-stop-vi.html language=enus -->
## TOPIC 00013: niRFSA Configure Spectrum Frequency Start Stop VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-spectrum-frequency-start-stop-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-spectrum-frequency-start-stop-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start and stop frequencies of a spectrum read by NI-RFSA. Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs civrn.png instrume

### niRFSA Configure Spectrum Frequency Start Stop VI

Configures the start and stop frequencies of a spectrum read by NI-RFSA.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-configure-spectrum-frequency-start-stop-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. start frequency — start frequency specifies the lower limit of a span of frequencies, in hertz (Hz). stop frequency — stop frequency specifies the upper limit of a span of frequencies, in hertz (Hz). error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

Note

stop frequency

start frequency

Note

Parent topic:

niRFSA Configure Spectrum Frequency VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-spectrum-frequency-vi.html language=enus -->
## TOPIC 00014: niRFSA Configure Spectrum Frequency VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-spectrum-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-spectrum-frequency-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency range of the spectrum read by NI-RFSA. Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 You can configure a spectrum in one of two ways

### niRFSA Configure Spectrum Frequency VI

Configures the frequency range of the spectrum read by NI-RFSA.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

You can configure a spectrum in one of two ways:

- As a span of data surrounding the center frequency.
- As a span of data between a start frequency and a stop frequency.

Each of these methods corresponds to an instance of this polymorphic VI.

[IMAGE alt='icon' src='nirfsa-configure-spectrum-frequency-vi.png']

#### Details

Note

stop frequency

start frequency

Note

- [niRFSA Configure Spectrum Frequency Center Span VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-spectrum-frequency-center-span-vi.html) Configures the span and center frequency of the spectrum read by NI-RFSA. A spectrum acquisition consists of data surrounding the center frequency.
- [niRFSA Configure Spectrum Frequency Start Stop VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-spectrum-frequency-start-stop-vi.html) Configures the start and stop frequencies of a spectrum read by NI-RFSA.

Parent topic:

Spectrum

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-trigger-vi.html language=enus -->
## TOPIC 00015: niRFSA Configure Trigger VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-trigger-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start, Reference, and Advance Triggers. Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Related Topics Triggers PXI Trigger Lines icon

### niRFSA Configure Trigger VI

Configures the Start, Reference, and Advance Triggers.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

[PXI Trigger Lines](/csh?context=nirfsa_nirfsa_pxi-trigger-lines)

[IMAGE alt='icon' src='nirfsa-configure-trigger-vi.png']

- [niRFSA Disable Ref Trigger VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-disable-ref-trigger-vi.html) Configures the device to not wait for a Reference Trigger to mark a reference point within a record. This VI is necessary only if you previously configured a Reference Trigger and now want to disable it.
- [niRFSA Configure Digital Edge Ref Trigger VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-digital-edge-ref-trigger-vi.html) Configures the device to wait for a digital edge Reference Trigger to mark a reference point within the record.
- [niRFSA Configure Software Edge Ref Trigger VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-software-edge-ref-trigger-vi.html) Configures the device to wait for a software Reference Trigger to mark a reference point within the record. The device waits until you call the niRFSA Send Software Edge Trigger VI to assert the trigger.
- [niRFSA Configure IQ Power Edge Ref Trigger VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-iq-power-edge-ref-trigger-vi.html) Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.
- [niRFSA Disable Start Trigger VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-disable-start-trigger-vi.html) Configures the device to not wait for a Start Trigger at the beginning of the acquisition. This VI is necessary only if you previously configured a Start Trigger and now want to disable it.
- [niRFSA Configure Digital Edge Start Trigger VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-digital-edge-start-trigger-vi.html) Configures the device to wait for a digital edge Start Trigger at the beginning of the acquisition.
- [niRFSA Configure Software Edge Start Trigger VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-software-edge-start-trigger-vi.html) Configures the device to wait for a software Start Trigger at the beginning of the acquisition. The device waits until you call the niRFSA Send Software Edge Trigger VI to assert the trigger.
- [niRFSA Disable Advance Trigger VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-disable-advance-trigger-vi.html) Configures the device to not use an Advance Trigger. This VI is necessary only if you configured an Advance Trigger in the past and now want to disable it.
- [niRFSA Configure Digital Edge Advance Trigger VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-digital-edge-advance-trigger-vi.html) Configures the device to wait for a digital edge Advance Trigger. The Advance Trigger indicates where a new record begins.
- [niRFSA Configure Software Edge Advance Trigger VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-configure-software-edge-advance-trigger-vi.html) Configures the device to wait for a software Advance Trigger. The Advance Trigger indicates where a new record begins. The device waits until you call the niRFSA Send Software Edge Trigger VI to assert the trigger.

Parent topic:

Trigger

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-create-configuration-list-vi.html language=enus -->
## TOPIC 00016: niRFSA Create Configuration List VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-create-configuration-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-create-configuration-list-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an empty configuration list for RF list mode. After a configuration list is created, enable the list using the set as active list input. Call the niRFSA Create Configuration List Step VI to add steps to the active configuration list. Supported Devices: PXIe-5644/5645/5646, PXIe-5663E/5665/56

### niRFSA Create Configuration List VI

Creates an empty configuration list for [RF list mode](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=rf-list-mode). After a configuration list is created, enable the list using the **set as active list** input. Call the [niRFSA Create Configuration List Step](/csh?topicname=nirfsa-create-configuration-list-step-vi.html) VI to add steps to the active configuration list.

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters

**Related Topics**

[RF List Mode](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=rf-list-mode)

[IMAGE alt='icon' src='nirfsa-create-configuration-list-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. list name — list name specifies the name of the configuration list. This string may not contain spaces, special characters, or punctuation marks. configuration list properties — configuration list properties specifies the properties that you intend to change between configuration list steps. Calling the niRFSA Create Configuration List VI allocates space for each of the configuration list properties. When you use the NI-RFSA property node to set one of the configuration list properties, that property is set as one of the configuration list steps. Specify which configuration list step is being configured using the Active Configuration List property. You can include the following properties in your configuration list based on your device: Property PXIe-5663E PXIe-5665 PXIe-5667 PXIe-5644/5646 PXIe-5645 PXIe-5820 PXIe-5830/5831/5832 PXIe-5840/5841 PXIe-5841 with PXIe-5655 PXIe-5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters PXIe-5860 Channel Coupling ✓ Device Instantaneous Bandwidth ✓ ✓ ✓ ✓ ✓ ✓ ✓ Downconverter Center Frequency ✓ ✓ ✓ ✓ ✓ ✓ ✓ Downconverter Frequency Offset ✓ ✓ Downconverter Frequency Offset Mode ✓ ✓ ✓ Downconverter Preselector Enabled ✓ (PXIe-5665 (14 GHz) only) ✓ (PXIe-5667 (7 GHz) only) ✓ External Gain ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Frequency Settling ✓ ✓ ✓ ✓ ✓ ✓ IF Filter Bandwidth ✓ ✓ ✓ IF Output Power Level ✓ ✓ ✓ IF Output Power Level Offset ✓ ✓ ✓ IQ Carrier Frequency ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ IQ In Port Carrier Frequency ✓ ✓ IQ In Port Vertical Range ✓ ✓ IQ Power Edge Trigger Level ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ LO Source ✓ ✓ ✓ Low Frequency Bypass Enabled ✓ Mechanical Attenuation ✓ ✓ ✓ Mechanical Attenuator Enabled ✓ Minimum ACPR ✓ Notch Filter Enabled ✓ Number of Samples ✓ ✓ ✓ ✓ ✓ OSP Data Scaling Factor ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Reference Level ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ RF Attenuation ✓ ✓ ✓ RF Out LO Export Enabled ✓ ✓ RF Preamp Enabled ✓ ✓ ✓ ✓ RF Preselector Filter ✓ Timer Event Interval ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ set as active list — set as active list sets this list as the active configuration list when this parameter is set to TRUE. The default value is TRUE. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Property | PXIe-5663E | PXIe-5665 | PXIe-5667 | PXIe-5644/5646 | PXIe-5645 | PXIe-5820 | PXIe-5830/5831/5832 | PXIe-5840/5841 | PXIe-5841 with PXIe-5655 | PXIe-5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters | PXIe-5860 |
| Channel Coupling |  |  | ✓ |  |  |  |  |  |  |  |  |
| Device Instantaneous Bandwidth | ✓ | ✓ | ✓ |  |  | ✓ |  | ✓ |  | ✓ | ✓ |
| Downconverter Center Frequency | ✓ | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  | ✓ |  |
| Downconverter Frequency Offset |  |  |  |  |  |  |  | ✓ |  | ✓ |  |
| Downconverter Frequency Offset Mode |  |  |  |  |  |  |  | ✓ | ✓ | ✓ |  |
| Downconverter Preselector Enabled |  | ✓ (PXIe-5665 (14 GHz) only) | ✓ (PXIe-5667 (7 GHz) only) |  |  |  |  | ✓ |  |  |  |
| External Gain | ✓ | ✓ | ✓ |  |  | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| Frequency Settling | ✓ | ✓ | ✓ |  |  |  |  | ✓ |  | ✓ | ✓ |
| IF Filter Bandwidth | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |
| IF Output Power Level | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |
| IF Output Power Level Offset | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |
| IQ Carrier Frequency | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  | ✓ | ✓ |
| IQ In Port Carrier Frequency |  |  |  |  | ✓ | ✓ |  |  |  |  |  |
| IQ In Port Vertical Range |  |  |  |  | ✓ | ✓ |  |  |  |  |  |
| IQ Power Edge Trigger Level | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| LO Source |  |  |  |  |  |  |  | ✓ | ✓ | ✓ |  |
| Low Frequency Bypass Enabled |  |  | ✓ |  |  |  |  |  |  |  |  |
| Mechanical Attenuation | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |
| Mechanical Attenuator Enabled | ✓ |  |  |  |  |  |  |  |  |  |  |
| Minimum ACPR |  | ✓ |  |  |  |  |  |  |  |  |  |
| Notch Filter Enabled |  |  | ✓ |  |  |  |  |  |  |  |  |
| Number of Samples |  |  |  |  |  | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| OSP Data Scaling Factor | ✓ | ✓ | ✓ |  |  | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| Reference Level | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |  | ✓ | ✓ |
| RF Attenuation | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |
| RF Out LO Export Enabled |  |  |  |  |  |  |  | ✓ | ✓ |  |  |
| RF Preamp Enabled | ✓ | ✓ | ✓ |  |  |  |  | ✓ |  |  |  |
| RF Preselector Filter |  |  | ✓ |  |  |  |  |  |  |  |  |
| Timer Event Interval | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |

Parent topic:

Configuration List

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-create-de-embedding-s-parameter-table-array-vi.html language=enus -->
## TOPIC 00017: niRFSA Create De-embedding S-parameter Table (array) VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-create-de-embedding-s-parameter-table-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-create-de-embedding-s-parameter-table-array-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an s-parameter de-embedding table for the port from the input data. If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement. Supported Devices: PXIe-5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs c3dcdb.png S-parameter table S-par

### niRFSA Create De-embedding S-parameter Table (array) VI

Creates an s-parameter de-embedding table for the port from the input data.

If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-create-de-embedding-s-parameter-table-array-vi.png']

#### Inputs/Outputs

| S-parameter table — S-parameter table specifies the S-parameters for each frequency. The first index indicates which frequency the entry is for. The second index is the target port for the S-parameter and the third index is the the source port. For example, to index the s21 parameter for the fourth frequency in the table, you would use {3, 1, 0} as the indexes since they are zero-based. instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. port — port specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string). table name — table name specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced. frequencies — frequencies specifies the frequencies for the S-parameter table rows. Frequencies must be unique and in ascending order. error in — error in describes error conditions that occur before this node runs. The default is no error. This node runs regardless of whether an error occurred before it executed. This input contains status, code, and source, which provide standard error in functionality. S-parameters orientation — S-parameters orientation specifies the orientation of the data in the S2P file relative to the DUT port. The default value is Port2 Towards DUT. Port1 Towards DUT (24000) Port 1 of the S2P is oriented towards the DUT port. Port2 Towards DUT (24001) Port 2 of the S2P is oriented towards the DUT port. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Port1 Towards DUT (24000) | Port 1 of the S2P is oriented towards the DUT port. |
| Port2 Towards DUT (24001) | Port 2 of the S2P is oriented towards the DUT port. |

Parent topic:

niRFSA Create De-embedding S-parameter Table VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-create-de-embedding-s-parameter-table-s2p-file-vi.html language=enus -->
## TOPIC 00018: niRFSA Create De-embedding S-parameter Table (S2P file) VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-create-de-embedding-s-parameter-table-s2p-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-create-de-embedding-s-parameter-table-s2p-file-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an S-parameter de-embedding table for the port based on the specified S2P file. If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement. Supported Devices: PXIe-5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs civrn.png instrument h

### niRFSA Create De-embedding S-parameter Table (S2P file) VI

Creates an S-parameter de-embedding table for the port based on the specified S2P file.

If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-create-de-embedding-s-parameter-table-s2p-file-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. port — port specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string). table name — table name specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced. S2P file path — S2P file path specifies the path to the S2P file that contains de-embedding information for the specified port. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. S-parameters orientation — S-parameters orientation specifies the orientation of the data in the S2P file relative to the DUT port. The default value is Port2 Towards DUT. Port1 Towards DUT (24000) Port 1 of the S2P is oriented towards the DUT port. Port2 Towards DUT (24001) Port 2 of the S2P is oriented towards the DUT port. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Port1 Towards DUT (24000) | Port 1 of the S2P is oriented towards the DUT port. |
| Port2 Towards DUT (24001) | Port 2 of the S2P is oriented towards the DUT port. |

Parent topic:

niRFSA Create De-embedding S-parameter Table VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-delete-de-embedding-table-vi.html language=enus -->
## TOPIC 00019: niRFSA Delete De-embedding Table VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-delete-de-embedding-table-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-delete-de-embedding-table-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the selected de-embedding table for a given port. Supported Devices: PXIe-5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs civrn.png instrument handle instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initial

### niRFSA Delete De-embedding Table VI

Deletes the selected de-embedding table for a given port.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-delete-de-embedding-table-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. port — port specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string). table name — table name specifies the name of the table. error in — error in describes error conditions that occur before this node runs. The default is no error. This node runs regardless of whether an error occurred before it executed. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

De-embedding

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-disable-advance-trigger-vi.html language=enus -->
## TOPIC 00020: niRFSA Disable Advance Trigger VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-disable-advance-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-disable-advance-trigger-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not use an Advance Trigger. This VI is necessary only if you configured an Advance Trigger in the past and now want to disable it. Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outpu

### niRFSA Disable Advance Trigger VI

Configures the device to not use an Advance Trigger. This VI is necessary only if you configured an Advance Trigger in the past and now want to disable it.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-disable-advance-trigger-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSA Configure Trigger VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-disable-ref-trigger-vi.html language=enus -->
## TOPIC 00021: niRFSA Disable Ref Trigger VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-disable-ref-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-disable-ref-trigger-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a Reference Trigger to mark a reference point within a record. This VI is necessary only if you previously configured a Reference Trigger and now want to disable it. Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831

### niRFSA Disable Ref Trigger VI

Configures the device to not wait for a Reference Trigger to mark a reference point
 within a record. This VI is necessary only if you previously configured a Reference Trigger and now want to disable it.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-disable-ref-trigger-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSA Configure Trigger VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-disable-start-trigger-vi.html language=enus -->
## TOPIC 00022: niRFSA Disable Start Trigger VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-disable-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-disable-start-trigger-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a Start Trigger at the beginning of the acquisition. This VI is necessary only if you previously configured a Start Trigger and now want to disable it. Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/584

### niRFSA Disable Start Trigger VI

Configures the device to not wait for a Start Trigger at the beginning of the acquisition. This VI is necessary only if you previously configured a Start Trigger and now want to disable it.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-disable-start-trigger-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niRFSA Configure Trigger VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-enable-session-access-vi.html language=enus -->
## TOPIC 00023: niRFSA Enable Session Access VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-enable-session-access-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-enable-session-access-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables SFP session access for the specified instrument. SFP session access allows the NI-RFSA Soft Front Panel (SFP) to access a device with an existing open session and can help you debug your code. To enable session access, specify an instrument handle and wire TRUE to the session acc

### niRFSA Enable Session Access VI

Enables or disables SFP session access for the specified instrument.

SFP session access allows the NI-RFSA Soft Front Panel (SFP) to access a device with an existing open session and can help you debug your code. To enable session access, specify an **instrument handle** and wire TRUE to the **session access enabled** parameter. To disable session access wire FALSE to the **session access enabled** parameter.

Refer to [Debugging Your Application Using SFP Session Access](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=debugging-your-application-using-sfp-session) for more information about SFP session access.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842/5860

Note

[IMAGE alt='icon' src='nirfsa-enable-session-access-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. session access enabled — session access enabled enables or disables SFP session access for the specified device. The default value is FALSE. TRUE Enables SFP session access. FALSE Disables SFP session access. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE | Enables SFP session access. |
| FALSE | Disables SFP session access. |

Parent topic:

Utility

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-export-signal-vi.html language=enus -->
## TOPIC 00024: niRFSA Export Signal VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-export-signal-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-export-signal-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes signals (triggers, clocks, and events) to the specified output terminal. Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Related Topics Triggers Events Signal Routing icon Inputs/Outputs civrn.png instru

### niRFSA Export Signal VI

Routes signals (triggers, clocks, and events) to the specified output terminal.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

[Events](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=events)

[Signal Routing](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=signal-routing)

[IMAGE alt='icon' src='nirfsa-export-signal-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. signal — signal specifies the type of signal to route. Start Trigger NI-RFSA routes a Start Trigger. Ref Trigger NI-RFSA routes a Reference Trigger. Advance Trigger NI-RFSA routes an Advance Trigger. Ready for Start Event NI-RFSA routes a Ready for Start Event. Ready for Advance Event NI-RFSA routes a Ready for Advance Event. Ready for Ref Event NI-RFSA routes a Ready for Reference Event. End of Record Event NI-RFSA routes an End of Record Event. Done Event NI-RFSA routes a Done Event. Ref Clock NI-RFSA routes a Reference Clock signal. User NI-RFSA routes a user-defined signal, specified using the signal identifier parameter. signal identifier — signal identifier specifies the user-defined signal to route. Specify the signal you have implemented using FPGA extensions. output terminal — output terminal specifies the terminal where the signal is exported. You can also choose not to export any signal. For the PXIe-5841 with PXIe-5655, the signal is exported to the terminal on the PXIe-5841. Do not export signal The signal is not exported. ClkOut The signal is exported to the CLK OUT connector on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. RefOut The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. RefOut2 The signal is exported to the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. PFI0 The signal is exported to the PFI 0 connector. PFI1 The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622. PXI_Trig0 The signal is exported to the PXI trigger line 0. PXI_Trig1 The signal is exported to the PXI trigger line 1. PXI_Trig2 The signal is exported to the PXI trigger line 2. PXI_Trig3 The signal is exported to the PXI trigger line 3. PXI_Trig4 The signal is exported to the PXI trigger line 4. PXI_Trig5 The signal is exported to the PXI trigger line 5. PXI_Trig6 The signal is exported to the PXI trigger line 6. PXIe_DStarC The signal is exported to the PXI DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Start Trigger | NI-RFSA routes a Start Trigger. |
| Ref Trigger | NI-RFSA routes a Reference Trigger. |
| Advance Trigger | NI-RFSA routes an Advance Trigger. |
| Ready for Start Event | NI-RFSA routes a Ready for Start Event. |
| Ready for Advance Event | NI-RFSA routes a Ready for Advance Event. |
| Ready for Ref Event | NI-RFSA routes a Ready for Reference Event. |
| End of Record Event | NI-RFSA routes an End of Record Event. |
| Done Event | NI-RFSA routes a Done Event. |
| Ref Clock | NI-RFSA routes a Reference Clock signal. |
| User | NI-RFSA routes a user-defined signal, specified using the signal identifier parameter. |
| Do not export signal | The signal is not exported. |
| ClkOut | The signal is exported to the CLK OUT connector on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut2 | The signal is exported to the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. |
| PFI0 | The signal is exported to the PFI 0 connector. |
| PFI1 | The signal is exported to the PFI 1 connector on the PXI-5142 and PXIe-5622. |
| PXI_Trig0 | The signal is exported to the PXI trigger line 0. |
| PXI_Trig1 | The signal is exported to the PXI trigger line 1. |
| PXI_Trig2 | The signal is exported to the PXI trigger line 2. |
| PXI_Trig3 | The signal is exported to the PXI trigger line 3. |
| PXI_Trig4 | The signal is exported to the PXI trigger line 4. |
| PXI_Trig5 | The signal is exported to the PXI trigger line 5. |
| PXI_Trig6 | The signal is exported to the PXI trigger line 6. |
| PXIe_DStarC | The signal is exported to the PXI DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |

#### Details

If you export a signal with this VI and [commit](nirfsa-commit-vi.html) the
 session, the signal is routed to the output terminal you specify. If you then
 reconfigure the signal to have a different output terminal, the previous output terminal
 is tristated when the session is next committed. If you set the **output terminal** parameter to **Do Not Export** and [commit](nirfsa-commit-vi.html), the previous output terminal is tri-stated.

Any signals, except for those exported over PXI trigger lines, that are exported within a session persist after the session closes to prevent signal glitches between sessions. PXI trigger lines are always set to tristate when a session is closed. If you wish to have the output terminal tristated when the session closes, change the **output terminal** for the exported signal to **Do Not
 Export**, and [commit](nirfsa-commit-vi.html) the session again before
 closing it.

You can also tristate all PFI lines by setting the **reset**
 input in the [niRFSA Initialize](nirfsa-initialize-vi.html) VI to TRUE or
 by using the [niRFSA Reset](nirfsa-reset-vi.html) VI.

Parent topic:

Trigger

Parent topic:

Clock

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-ext-cal-store-baseline-for-self-cal-vi.html language=enus -->
## TOPIC 00025: niRFSA Ext Cal Store Baseline For Self Cal VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-ext-cal-store-baseline-for-self-cal-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-ext-cal-store-baseline-for-self-cal-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the external calibration step to run and stores the associated constants in the device memory so that they can be compared with the computed constants at run time. A password is required to run the VI. Supported Devices: PXIe-5603/5605/5606, PXIe-5665/5668 icon Inputs/Outputs civrn.png ins

### niRFSA Ext Cal Store Baseline For Self Cal VI

Specifies the external calibration step to run and stores the associated constants in the device memory so that they can be compared with the computed constants at run time. A password is required to run the VI.

**Supported Devices**: PXIe-5603/5605/5606, PXIe-5665/5668

[IMAGE alt='icon' src='nirfsa-ext-cal-store-baseline-for-self-cal-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI. password — password specifies the password for the calibration session. The initial password is factory configured to NI. password can be a maximum of ten alphanumeric characters. step to run — step to run specifies the step for which constants are computed. Gain Reference Measures the changes in gain since the last external calibration was run. IF Flatness Measures the IF response of the entire system for each of the supported IF filters. Digitizer Self Cal Calls for digitizer self-calibration, if the digitizer is associated with the RF downconverter. LO Self Cal Calls for LO self-calibration, if the LO source module is associated with the RF downconverter. Preselector Alignment Calls for preselector alignment. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Gain Reference | Measures the changes in gain since the last external calibration was run. |
| IF Flatness | Measures the IF response of the entire system for each of the supported IF filters. |
| Digitizer Self Cal | Calls for digitizer self-calibration, if the digitizer is associated with the RF downconverter. |
| LO Self Cal | Calls for LO self-calibration, if the LO source module is associated with the RF downconverter. |
| Preselector Alignment | Calls for preselector alignment. |

Parent topic:

NI 5665

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-1d-complex-wdt-nrec-1chan-vi.html language=enus -->
## TOPIC 00026: niRFSA Fetch IQ (1D Complex WDT NRec 1Chan) VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-1d-complex-wdt-nrec-1chan-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-1d-complex-wdt-nrec-1chan-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q data from multiple records in an acquisition. Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs cu16.png timestamp type timestamp type specifies the time format of the data output. The defaul

### niRFSA Fetch IQ (1D Complex WDT NRec 1Chan) VI

Fetches I/Q data from multiple records in an acquisition.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-fetch-iq-1d-complex-wdt-nrec-1chan-vi.png']

#### Inputs/Outputs

| timestamp type — timestamp type specifies the time format of the data output. The default value is Relative. Relative The timestamp corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred. Absolute The timestamp corresponds to the date and time of the acquisition of the first sample returned. Note The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. number of records (-1) — number of records specifies the number of records to fetch. A value of -1 specifies that NI-RFSA fetches all records in an acquisition. Record numbers are zero-based. The default value is -1. If starting record is set to a value greater than 0, setting number of records to –1 returns an error. If you set starting record to a value greater than 0, set number of records to the exact number of records to fetch. Note If you set number of records to 0, this VI returns an error. starting record — starting record specifies the first record to retrieve. Record numbers are zero-based. The default value is 0. instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. samples to read (-1) — samples to read specifies the number of samples to fetch. A value of -1 specifies that NI-RFSA fetches all samples. The default value is -1. Note Setting samples to read to –1 fetches all remaining samples currently available depending on the Fetch Relative To property and the Fetch Offset property settings. timeout (10 sec) — timeout specifies the time, in seconds, allotted for the VI to complete before returning a timeout error for the PXI-5661, PXIe-5663/5665/5667. Specifies the time, in seconds, allotted to receive the reference trigger for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. Note A value of -1 specifies that the VI waits until all data is available. A value of 0 specifies the VI immediately returns available data. The default value is 10. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. data — data returns the acquired waveform. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Relative | The timestamp corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred. |
| Absolute | The timestamp corresponds to the date and time of the acquisition of the first sample returned. |

Parent topic:

niRFSA Fetch IQ VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-1d-i16-data-ref-vi.html language=enus -->
## TOPIC 00027: niRFSA Fetch IQ (1D I16 Data Ref) VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-1d-i16-data-ref-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-1d-i16-data-ref-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches binary I/Q data inside a data value reference from a single record in an acquisition. You must call Delete Data Value Reference on any outstanding data value references before calling niRFSA Fetch IQ, niRFSA Close, niRFSA Initialize, or niRFSA Reset. Refer to the LabVIEW Help for more inform

### niRFSA Fetch IQ (1D I16 Data Ref) VI

Fetches binary I/Q data inside a data value reference from a single record in an acquisition.

Note

niRFSA Close

niRFSA Initialize

niRFSA Reset

LabVIEW Help

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-fetch-iq-1d-i16-data-ref-vi.png']

#### Inputs/Outputs

| record to fetch — record to fetch specifies the record to retrieve. Record numbers are zero-based. The default value is 0. instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. samples to read (-1) — samples to read specifies the number of samples to fetch. A value of -1 specifies that NI-RFSA fetches all samples. The default value is -1. Note Setting samples to read to –1 fetches all remaining samples currently available depending on the Fetch Relative To property and the Fetch Offset property settings. timeout (10 sec) — timeout specifies the time, in seconds, allotted for the VI to complete before returning a timeout error. A value of -1 specifies that the VI waits until all data is available. The default value is 10 seconds. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. data value reference — returns the external data value reference containing the acquired unscaled, complex waveform. The array is composed of interleaved I and Q samples, where the order of the array is as follows: Array[0] = I(0) Array[1] = Q(0) Array[2] = I(1) Array[3] = Q(1) wfm info — wfm info contains the absolute and relative timestamps for the operation, the time interval, and the actual number of samples read. absolute timestamp — absolute timestamp returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions. Note The value of the absolute timestamp returned is always 0 for the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. relative timestamp — relative timestamp returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred. dt — dt returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. actual samples read — actual samples read returns an integer representing the number of samples in the waveform. offset — offset returns the offset to scale data, (b), in mx + b form. gain — gain returns the gain to scale data, (m), in mx + b form. reserved1 — reserved2 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| absolute timestamp — absolute timestamp returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions. Note The value of the absolute timestamp returned is always 0 for the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. relative timestamp — relative timestamp returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred. dt — dt returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. actual samples read — actual samples read returns an integer representing the number of samples in the waveform. offset — offset returns the offset to scale data, (b), in mx + b form. gain — gain returns the gain to scale data, (m), in mx + b form. reserved1 — reserved2 — |

#### Details

Use the In Place Element structure Data Value Reference Read/Write Element to read data and operate on the data within place. Refer to the *LabVIEW Help* for more information on the Data Value Reference Read/Write Element.

To improve streaming performance, consider the following recommendations:

- Use LabVIEW (64-bit).
- Set the Host DMA Buffer Size property to at least 512 MB.
- Use the TDMS Advanced Asynchronous Write (Data Ref) function to optimize performance when writing data to disk. Refer to the LabVIEW Help for more information about this function.

Parent topic:

niRFSA Fetch IQ VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-1d-i16-vi.html language=enus -->
## TOPIC 00028: niRFSA Fetch IQ (1D I16) VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-1d-i16-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-1d-i16-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches binary I/Q data from a single record in an acquisition. Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs ci64.png record to fetch record to fetch specifies the record to retrieve. Record numbers

### niRFSA Fetch IQ (1D I16) VI

Fetches binary I/Q data from a single record in an acquisition.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-fetch-iq-1d-i16-vi.png']

#### Inputs/Outputs

| record to fetch — record to fetch specifies the record to retrieve. Record numbers are zero-based. The default value is 0. instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. samples to read (-1) — samples to read specifies the number of samples to fetch. A value of -1 specifies that NI-RFSA fetches all samples. The default value is -1. Note Setting samples to read to –1 fetches all remaining samples currently available depending on the Fetch Relative To property and the Fetch Offset property settings. timeout (10 sec) — timeout specifies the time, in seconds, allotted for the VI to complete before returning a timeout error for the PXI-5661, PXIe-5663/5665/5667. Specifies the time, in seconds, allotted to receive the reference trigger for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. Note A value of -1 specifies that the VI waits until all data is available. A value of 0 specifies the VI immediately returns available data. The default value is 10. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. data — data returns the acquired unscaled, complex waveform. The array is composed of interleaved I and Q samples, where the order of the array is as follows: Array[0] = I(0) Array[1] = Q(0) Array[2] = I(1) Array[3] = Q(1) wfm info — wfm info contains the absolute and relative timestamps for the operation, the time interval, and the actual number of samples read. absolute timestamp — absolute timestamp returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions. Note The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. relative timestamp — relative timestamp returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred. Note The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646. dt — dt returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. actual samples read — actual samples read returns an integer representing the number of samples in the waveform. offset — offset returns the offset to scale data, (b), in mx + b form. gain — gain returns the gain to scale data, (m), in mx + b form. reserved1 — reserved2 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| absolute timestamp — absolute timestamp returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions. Note The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. relative timestamp — relative timestamp returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred. Note The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646. dt — dt returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. actual samples read — actual samples read returns an integer representing the number of samples in the waveform. offset — offset returns the offset to scale data, (b), in mx + b form. gain — gain returns the gain to scale data, (m), in mx + b form. reserved1 — reserved2 — |

Parent topic:

niRFSA Fetch IQ VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-complex-cluster-1rec-1chan-vi.html language=enus -->
## TOPIC 00029: niRFSA Fetch IQ (Complex Cluster 1Rec 1Chan) VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-complex-cluster-1rec-1chan-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-fetch-iq-complex-cluster-1rec-1chan-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q data from a single record in an acquisition. Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs ci64.png record to fetch record to fetch specifies the record to retrieve. Record numbers are ze

### niRFSA Fetch IQ (Complex Cluster 1Rec 1Chan) VI

Fetches I/Q data from a single record in an acquisition.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-fetch-iq-complex-cluster-1rec-1chan-vi.png']

#### Inputs/Outputs

| record to fetch — record to fetch specifies the record to retrieve. Record numbers are zero-based. The default value is 0. instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. samples to read (-1) — samples to read specifies the number of samples to fetch. A value of -1 specifies that NI-RFSA fetches all samples. The default value is -1. Note Setting samples to read to –1 fetches all remaining samples currently available depending on the Fetch Relative To property and the Fetch Offset property settings. timeout (10 sec) — timeout specifies the time, in seconds, allotted for the VI to complete before returning a timeout error for the PXI-5661, PXIe-5663/5665/5667. Specifies the time, in seconds, allotted to receive the reference trigger for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. Note A value of -1 specifies that the VI waits until all data is available. A value of 0 specifies the VI immediately returns available data. The default value is 10. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. data — data returns the acquired data as a cluster. t0 — t0 returns the start time of the first sample returned. The timestamp corresponds to the difference in seconds between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred. Note The value of t0 returned in data is always 0 for the PXIe-5644/5645/5646. dt — dt returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. Y — Y returns the complex-value time domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. To calculate the instantaneous power of a sampled I/Q point, use the equation (I2 + Q2)/2R, where R is the input impedance in ohms (Ω). For vector signal analyzers, R=50 Ω. Note The size of the array can vary per record if the Number of Samples property changes per step during RF list mode. wfm info — wfm info contains the absolute and relative timestamps for the operation, the time interval, and the actual number of samples read. absolute timestamp — absolute timestamp returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions. NOTE: The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841. relative timestamp — relative timestamp returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred. NOTE: The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646. dt — dt returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. actual samples read — actual samples read returns an integer representing the number of samples in the waveform. offset — offset returns the offset to scale data, (b), in mx + b form. gain — gain returns the gain to scale data, (m), in mx + b form. reserved1 — reserved2 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 returns the start time of the first sample returned. The timestamp corresponds to the difference in seconds between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred. Note The value of t0 returned in data is always 0 for the PXIe-5644/5645/5646. dt — dt returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. Y — Y returns the complex-value time domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. To calculate the instantaneous power of a sampled I/Q point, use the equation (I2 + Q2)/2R, where R is the input impedance in ohms (Ω). For vector signal analyzers, R=50 Ω. Note The size of the array can vary per record if the Number of Samples property changes per step during RF list mode. |
| absolute timestamp — absolute timestamp returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions. NOTE: The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841. relative timestamp — relative timestamp returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred. NOTE: The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646. dt — dt returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. actual samples read — actual samples read returns an integer representing the number of samples in the waveform. offset — offset returns the offset to scale data, (b), in mx + b form. gain — gain returns the gain to scale data, (m), in mx + b form. reserved1 — reserved2 — |

Parent topic:

niRFSA Fetch IQ VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-get-de-embedding-s-parameters-vi.html language=enus -->
## TOPIC 00030: niRFSA Get De-embedding S-parameters VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-get-de-embedding-s-parameters-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-get-de-embedding-s-parameters-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the S-parameters used for de-embedding a measurement on the selected port. This includes interpolation of the parameters based on the configured carrier frequency. This VI returns an empty array if no de-embedding is completed. The port orientation for the returned S-parameters is normalized

### niRFSA Get De-embedding S-parameters VI

Returns the S-parameters used for de-embedding a measurement on the selected port. This includes interpolation of the parameters based on the configured carrier frequency.
This VI returns an empty array if no de-embedding is completed.

Note

Port2 Towards DUT

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-get-de-embedding-s-parameters-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. S-parameters — S-parameters returns an array of S-parameters. The first index indicates the target port for the S-parameter and the second index is the source port. For example, to index the s21 parameter, use {1, 0} for the indexes since they are zero-based. number of ports — number of ports returns the number of S-parameter ports. The S-parameter array is always n x n, where n is the number of ports. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

De-embedding

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-get-ext-cal-last-date-and-time-vi.html language=enus -->
## TOPIC 00031: niRFSA Get Ext Cal Last Date And Time VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-get-ext-cal-last-date-and-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-get-ext-cal-last-date-and-time-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful external calibration. The time returned is 24-hour local time and the date is returned as integer values; for example, if the device was calibrated at 2:30 PM on December 31, 2010, this VI returns 14 for the hour output, 30 for the minute output, 12 f

### niRFSA Get Ext Cal Last Date And Time VI

Returns the date and time of the last successful external calibration.

The time returned is 24-hour local time and the date is returned as integer values; for example, if the device was calibrated at 2:30 PM on December 31, 2010, this VI returns **14** for the **hour** output, **30** for the **minute** output, **12** for the **month** output, **31** for the **day** output, and **2010** for the **year** output.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-get-ext-cal-last-date-and-time-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your calibration instrument session. instrument handle is obtained from the niRFSA Initialize VI, niRFSA Initialize With Options VI, or niRFSA Init Ext Cal VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. year — year returns the year of the last external calibration. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI, niRFSA Initialize With Options VI, or niRFSA Init Ext Cal VI. month — month returns the month of the last external calibration. day — day returns the day of the last external calibration. error out — error out contains error information. This output provides standard error out functionality. minute — minute returns the minute of the last external calibration. hour — hour returns the hour of the last external calibration. |
| --- |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-get-scaling-coefficients-vi.html language=enus -->
## TOPIC 00032: niRFSA Get Scaling Coefficients VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-get-scaling-coefficients-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-get-scaling-coefficients-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns coefficients you can use to convert unscaled data to scaled I/Q data. Acquired data may be unscaled when sent by a peer-to-peer stream or when fetched as unscaled data. Use this VI to scale such I/Q values. The coefficient info array returns one cluster that contains gain and offset elements

### niRFSA Get Scaling Coefficients VI

Returns coefficients you can use to convert unscaled data to scaled I/Q data.

Acquired data may be unscaled when sent by a peer-to-peer stream or when fetched as unscaled data. Use this VI to scale such I/Q values.

The **coefficient info** array returns one cluster that contains **gain** and **offset** elements. To obtain scaled I/Q values, multiply the unscaled data by the **gain** value of the cluster, then add the **offset**.

Note

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-get-scaling-coefficients-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. coefficient info — coefficient info returns the array with coefficient information. Offset — offset returns the number to add to the data from a peer-to-peer stream after the gain has been applied in order to scale unscaled data. Gain — gain returns the multiplier to use to scale data obtained from a peer-to-peer stream. Reserved1 — Reserved2 — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Offset — offset returns the number to add to the data from a peer-to-peer stream after the gain has been applied in order to scale unscaled data. Gain — gain returns the multiplier to use to scale data obtained from a peer-to-peer stream. Reserved1 — Reserved2 — |

Parent topic:

Utility

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-get-self-cal-last-date-and-time-vi.html language=enus -->
## TOPIC 00033: niRFSA Get Self Cal Last Date And Time VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-get-self-cal-last-date-and-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-get-self-cal-last-date-and-time-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful self-calibration. The time returned is 24-hour local time and the date is returned as integer values. For example, if the device was calibrated at 2:30 PM on December 31, 2010, this VI returns 14 for the hour output, 30 for the minute output, 12 for t

### niRFSA Get Self Cal Last Date And Time VI

Returns the date and time of the last successful self-calibration.

The time returned is 24-hour local time and the date is returned as integer values. For example, if the device was calibrated at 2:30 PM on December 31, 2010, this VI returns **14** for the **hour** output, **30** for the **minute** output, **12** for the **month** output, **31** for the **day** output, and **2010** for the **year** output.

Note

Image Suppression

self cal step

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-get-self-cal-last-date-and-time-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your calibration instrument session. instrument handle is obtained from the niRFSA Initialize VI, niRFSA Initialize With Options VI, or niRFSA Init Ext Cal VI. self cal step — self cal step specifies the self-calibration step to query for the last successful self-calibration date and time data. Preselector Alignment Selects the Preselector Alignment self-calibration step. Gain Reference Selects the Gain Reference self-calibration step. IF Flatness Selects the IF Flatness self-calibration step. Digitizer Self Cal Selects the Digitizer Self Cal self-calibration step. LO Self Cal Selects the LO Self Cal self-calibration step. Amplitude Accuracy Selects the Amplitude Accuracy self-calibration step. Residual LO Power Selects the Residual LO Power self-calibration step. Image Suppression Selects the Image Suppression self-calibration step. Synthesizer Alignment Selects the Synthesizer Alignment self-calibration step. DC Offset Selects the DC Offset self-calibration step. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. year — year returns the year of the last self-calibration. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. month — month returns the month of the last self-calibration. day — day returns the day of the last self-calibration. minute — minute returns the minute of the last self-calibration. error out — error out contains error information. This output provides standard error out functionality. hour — hour returns the hour of the last self-calibration. |  |
| --- | --- |
| Preselector Alignment | Selects the Preselector Alignment self-calibration step. |
| Gain Reference | Selects the Gain Reference self-calibration step. |
| IF Flatness | Selects the IF Flatness self-calibration step. |
| Digitizer Self Cal | Selects the Digitizer Self Cal self-calibration step. |
| LO Self Cal | Selects the LO Self Cal self-calibration step. |
| Amplitude Accuracy | Selects the Amplitude Accuracy self-calibration step. |
| Residual LO Power | Selects the Residual LO Power self-calibration step. |
| Image Suppression | Selects the Image Suppression self-calibration step. |
| Synthesizer Alignment | Selects the Synthesizer Alignment self-calibration step. |
| DC Offset | Selects the DC Offset self-calibration step. |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-get-self-cal-last-temp-vi.html language=enus -->
## TOPIC 00034: niRFSA Get Self Cal Last Temp VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-get-self-cal-last-temp-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-get-self-cal-last-temp-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature, in degrees Celsius, at the last successful self-calibration. For the PXIe-5644/5645/5646, you must select Image Suppression for the self cal step input. Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/

### niRFSA Get Self Cal Last Temp VI

Returns the temperature, in degrees Celsius, at the last successful self-calibration.

Note

Image Suppression

self cal step

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-get-self-cal-last-temp-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your calibration instrument session. instrument handle is obtained from the niRFSA Initialize VI, niRFSA Initialize With Options VI, or niRFSA Init Ext Cal VI. self cal step — self cal step specifies the self-calibration step to query for the last successful self-calibration temperature data. Preselector Alignment Selects the Preselector Alignment self-calibration step. Gain Reference Selects the Gain Reference self-calibration step. IF Flatness Selects the IF Flatness self-calibration step. Digitizer Self Cal Selects the Digitizer Self Cal self-calibration step. LO Self Cal Selects the LO Self Cal self-calibration step. Amplitude Accuracy Selects the Amplitude Accuracy self-calibration step. Residual LO Power Selects the Residual LO Power self-calibration step. Image Suppression Selects the Image Suppression self-calibration step. Synthesizer Alignment Selects the Synthesizer Alignment self-calibration step. DC Offset Selects the DC Offset self-calibration step. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. temperature — temperature returns the temperature, in degrees Celsius, at the last self-calibration. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Preselector Alignment | Selects the Preselector Alignment self-calibration step. |
| Gain Reference | Selects the Gain Reference self-calibration step. |
| IF Flatness | Selects the IF Flatness self-calibration step. |
| Digitizer Self Cal | Selects the Digitizer Self Cal self-calibration step. |
| LO Self Cal | Selects the LO Self Cal self-calibration step. |
| Amplitude Accuracy | Selects the Amplitude Accuracy self-calibration step. |
| Residual LO Power | Selects the Residual LO Power self-calibration step. |
| Image Suppression | Selects the Image Suppression self-calibration step. |
| Synthesizer Alignment | Selects the Synthesizer Alignment self-calibration step. |
| DC Offset | Selects the DC Offset self-calibration step. |

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-get-session-reference-vi.html language=enus -->
## TOPIC 00035: niRFSA Get Session Reference VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-get-session-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-get-session-reference-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts a session that can be passed to NI-TClk VIs. Session references are of generic type, which means that the corresponding wires are blue-green, unlike the wires for regular instrument driver sessions. Supported Devices: PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 N

### niRFSA Get Session Reference VI

Extracts a session that can be passed to NI-TClk VIs. Session references are of
 generic type, which means that the corresponding wires are blue-green, unlike the wires
 for regular instrument driver sessions.

**Supported Devices**: PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Note

[IMAGE alt='icon' src='nirfsa-get-session-reference-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. session reference — session reference references the device session that can be passed to NI-TClk VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-get-spectral-info-for-smt-vi.html language=enus -->
## TOPIC 00036: niRFSA Get Spectral Info for SMT VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-get-spectral-info-for-smt-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-get-spectral-info-for-smt-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a cluster containing information about the power spectrum NI-RFSA computes. The NI Spectral Measurements Toolkit (SMT) requires this information. Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs

### niRFSA Get Spectral Info for SMT VI

Returns a cluster containing information about the power spectrum NI-RFSA computes.

Note

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-get-spectral-info-for-smt-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. spectral info — spectral info returns properties of the computed spectrum such as spectrum type, spectrum scale (linear or logarithmic), the window type the VI used to compute the spectrum, window size, and FFT size. Connect this parameter to subsequent VIs that contain the spectral info input. Do not modify the values. spectrum type — spectrum type returns the type of spectrum. linear/dB — linear/dB returns whether the spectrum scale is linear or logarithmic. window — window returns the time-domain window that the VI uses. window size — window size returns the window size used in window. FFT size — FFT size returns the FFT size. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| spectrum type — spectrum type returns the type of spectrum. linear/dB — linear/dB returns whether the spectrum scale is linear or logarithmic. window — window returns the time-domain window that the VI uses. window size — window size returns the window size used in window. FFT size — FFT size returns the FFT size. |

Parent topic:

Utility

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-get-stream-endpoint-handle-vi.html language=enus -->
## TOPIC 00037: niRFSA Get Stream Endpoint Handle VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-get-stream-endpoint-handle-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-get-stream-endpoint-handle-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a writer endpoint handle that you can use with NI-P2P to configure a peer-to-peer stream with the digitizer as an endpoint. Supported Devices: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Related Topics Peer-to-Peer Streaming Configuring an Endpoint Configurin

### niRFSA Get Stream Endpoint Handle VI

Returns a writer endpoint handle that you can use with NI-P2P to configure a peer-to-peer stream with the digitizer as an endpoint.

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Peer-to-Peer Streaming](https://ni.com/docs/en-US/csh?pubname=ni-rf-vst&topicname=p2p-streaming)

[Configuring an Endpoint](https://ni.com/docs/en-US/csh?pubname=pxie-5842&topicname=configuring-peer-to-peer-endpoint)

[Configuring a Peer-to-Peer Stream](https://ni.com/docs/en-US/csh?pubname=pxie-5842&topicname=configuring-peer-to-peer-stream)

[IMAGE alt='icon' src='nirfsa-get-stream-endpoint-handle-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. stream endpoint — stream endpoint specifies the name of the stream resources you want to use. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. writer handle — writer handle returns the writer endpoint handle which you use with NI-P2P to create a stream with the digitizer as an endpoint. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-get-terminal-name-vi.html language=enus -->
## TOPIC 00038: niRFSA Get Terminal Name VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-get-terminal-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-get-terminal-name-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified name of the signal being queried. Signals can be triggers, clocks, or events. You can pass the terminal name output to the source input of the niRFSA Configure Trigger VI. Supported Devices: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Rela

### niRFSA Get Terminal Name VI

Returns the fully qualified name of the signal being queried. Signals can be triggers, clocks, or events.

You can pass the **terminal name** output to the **source** input of the [niRFSA Configure Trigger](nirfsa-configure-trigger-vi.html) VI.

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Events](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=events)

[IMAGE alt='icon' src='nirfsa-get-terminal-name-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. signal — signal specifies the signal for which you want to query the terminal. Start Trigger NI-RFSA returns the terminal name for the Start Trigger. Ref Trigger NI-RFSA returns the terminal name for the Reference Trigger. Advance Trigger NI-RFSA returns the terminal name for the Advance Trigger. Ready for Start Event NI-RFSA returns the terminal name for the Ready for Start Event. Ready for Ref Event NI-RFSA returns the terminal name for the Ready for Reference Event. Ready for Advance Event NI-RFSA returns the terminal name for the Ready for Advance Event. End of Record Event NI-RFSA returns the terminal name for the End of Record Event. Done Event NI-RFSA returns the terminal name for the Done Event. Reference Clock NI-RFSA does not support this option for the niRFSA Get Terminal Name VI. User NI-RFSA routes a user-defined signal. signal identifier — signal identifier specifies the user-defined signal to route. Specify the signal you have implemented using FPGA extensions. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. terminal name — terminal name returns the fully qualified name of the signal being queried. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Start Trigger | NI-RFSA returns the terminal name for the Start Trigger. |
| Ref Trigger | NI-RFSA returns the terminal name for the Reference Trigger. |
| Advance Trigger | NI-RFSA returns the terminal name for the Advance Trigger. |
| Ready for Start Event | NI-RFSA returns the terminal name for the Ready for Start Event. |
| Ready for Ref Event | NI-RFSA returns the terminal name for the Ready for Reference Event. |
| Ready for Advance Event | NI-RFSA returns the terminal name for the Ready for Advance Event. |
| End of Record Event | NI-RFSA returns the terminal name for the End of Record Event. |
| Done Event | NI-RFSA returns the terminal name for the Done Event. |
| Reference Clock | NI-RFSA does not support this option for the niRFSA Get Terminal Name VI. |
| User | NI-RFSA routes a user-defined signal. |

Parent topic:

Trigger

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-property-node-vi.html language=enus -->
## TOPIC 00039: niRFSA Property Node VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-property-node-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads), sets (writes), or resets (sets to default value) NI-RFSA properties. When you read a property, NI-RFSA analyzes the current configuration to return the coerced value for that property. NI-RFSA verifies many properties upon reading, thereby either transitioning the session to the verifi

### niRFSA Property Node VI

Gets (reads), sets (writes), or resets (sets to default value) NI-RFSA properties. When you read a property, NI-RFSA analyzes the current configuration to return the coerced value for that property. NI-RFSA verifies many properties upon reading, thereby either transitioning the session to the verified state or alerting you of an invalid configuration. Setting or resetting a property transitions the session to an unverified state.

Refer to the [NI-RFSA Properties](/csh?context=nirfsa_rfsapropref_cnirfsa) for more information about using the NI-RFSA properties.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5600, PXIe-5601/5603/5605/5606, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-property-node-vi.png']

#### Inputs/Outputs

| reference — reference identifies your instrument session. reference refers to the instrument handle obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error in (no error) — error in describes error conditions that occur before this node runs. The default is no error. This node runs regardless of whether an error occurred before it executed. This input contains status, code, and source, which provide standard error in functionality. Property — reference out — reference out passes a reference to your instrument session to the next VI. reference out refers to the instrument handle that is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

Note

Mechanical Attenuation

Reference Level

Parent topic:

NI-RFSA

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-read-iq-vi.html language=enus -->
## TOPIC 00040: niRFSA Read IQ VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-read-iq-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-read-iq-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates an acquisition and fetches a single I/Q data record. Do not use this VI if you have configured the device to continuously acquire data samples or to acquire multiple records. Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/584

### niRFSA Read IQ VI

Initiates an acquisition and fetches a single [I/Q data](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=iq-modulation) record. Do not use this VI if
 you have configured the device to continuously acquire data samples or to acquire
 multiple records.

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[I/Q Modulation](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=iq-modulation)

[IMAGE alt='icon' src='nirfsa-read-iq-vi.png']

- [niRFSA Read IQ (Complex Cluster 1Rec 1Chan) VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-read-iq-complex-cluster-1rec-1chan-vi.html) Returns the I/Q data as a complex cluster.
- [niRFSA Read IQ (Complex WDT 1Rec 1Chan) VI](../../../instr-lib/nirfsa/nirfsa-llb/nirfsa-read-iq-complex-wdt-1rec-1chan-vi.html) Returns the I/Q data as a complex waveform data type (WDT).

Parent topic:

Acquisition

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-read-power-spectrum-dbl-vi.html language=enus -->
## TOPIC 00041: niRFSA Read Power Spectrum (DBL) VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-read-power-spectrum-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-read-power-spectrum-dbl-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates a spectrum acquisition and returns double precision power spectrum data. Under certain configurations, negative infinity is returned from this VI. If the Reference Level is very high and if the Signal Bandwidth is comparatively less, the ADC returns zero, which equates to negative infinity

### niRFSA Read Power Spectrum (DBL) VI

Initiates a spectrum acquisition and returns double precision power spectrum data.

Note

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='nirfsa-read-power-spectrum-dbl-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. timeout (10 sec) — timeout specifies the time, in seconds, allotted for the VI to complete before returning a timeout error. A value of -1 specifies that the VI waits until all data is available. The default value is 10. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. power spectrum — power spectrum returns power spectrum data. f0 — f0 returns the center frequency, in Hz, of the first bin of the power spectrum data. df — df returns the frequency interval, in Hz, between data points in the spectrum. data — data returns the acquired waveform as an array. If averaging is enabled, data returns the averaged power spectrum. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| f0 — f0 returns the center frequency, in Hz, of the first bin of the power spectrum data. df — df returns the frequency interval, in Hz, between data points in the spectrum. data — data returns the acquired waveform as an array. If averaging is enabled, data returns the averaged power spectrum. |

Parent topic:

niRFSA Read Power Spectrum (Cluster) VI

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-reset-with-options-vi.html language=enus -->
## TOPIC 00042: niRFSA Reset With Options VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-reset-with-options-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-reset-with-options-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes. For the PXI-5600, this VI does not reset the PXI Clock signal that is driven by devices installed in the Star Trigger Controller Slot, also known as the System Timing Slot. To avoid r

### niRFSA Reset With Options VI

Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes.

For the PXI-5600, this VI does not reset the PXI Clock signal that is driven by devices installed in the Star Trigger Controller Slot, also known as the System Timing Slot.

To avoid resetting routes on PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSG sessions, NI recommends using this VI instead of the [niRFSA Reset](nirfsa-reset-vi.html) VI, with the **steps to omit** parameter set to **Routes**.

By default, this VI resets all properties to their default values, deletes all de-embedding tables, aborts generation, clears all routes, and resets session properties to initial values. You can specify steps to omit using the **steps to omit** parameter. For example, if you set the **steps to omit** parameter to **Routes**, this VI does not release signal routes during the reset process.

When routes of signals between two devices are released, they are released regardless of which device created the route.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

[Events](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=events)

[IMAGE alt='icon' src='nirfsa-reset-with-options-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. steps to omit — steps to omit specifies a list of steps to skip during reset process. The default value is an empty array, which specifies that no steps are omitted during reset. Routes Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after reset. De-embedding Table Omits deleting de-embedding tables. Note Routes is not supported in external calibration or alignment sessions. Note Routes is not supported for the PXI-5600/5661. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Routes | Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after reset. |
| De-embedding Table | Omits deleting de-embedding tables. |

Parent topic:

Utility

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-llb/nirfsa-self-test-vi.html language=enus -->
## TOPIC 00043: niRFSA Self Test VI

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-llb/nirfsa-self-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-llb/nirfsa-self-test-vi.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a self-test on the NI-RFSA device and returns the test result. This VI performs a simple series of tests verifying that the NI-RFSA device is powered on and responding. This VI calls the niRFSA Reset VI, which resets the software state. Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606

### niRFSA Self Test VI

Performs a self-test on the NI-RFSA device and returns the test result. This VI
 performs a simple series of tests verifying that the NI-RFSA device is powered on and
 responding.

Note

niRFSA Reset

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Running a Self-Test on an NI-RFSA Device](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=running-a-self-test-on-an-ni-rfsa-device)

[IMAGE alt='icon' src='nirfsa-self-test-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies your instrument session. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference to your instrument session to the next VI. instrument handle is obtained from the niRFSA Initialize VI or the niRFSA Initialize With Options VI and identifies a particular instrument session. self test result — self-test result returns the value from the device self-test. A value of 0 means success. All other values indicate failure. self test message — self-test message returns the self-test response string from the NI-RFSA device. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-acpr-5603.html language=enus -->
## TOPIC 00044: Vertical:Advanced:Minimum Adjacent Channel Power Ratio (dB)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-acpr-5603.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-acpr-5603.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum adjacent channel power ratio (ACPR), in decibels, relative to the main channel reference level. This property configures NI-RFSA to optimize downconverter gain to measure a lower-power adjacent channel, adding gain only after filtering the main channel. The gain NI-RFSA applies

### Vertical:Advanced:Minimum Adjacent Channel Power Ratio (dB)

Specifies the minimum adjacent channel power ratio (ACPR), in decibels, relative to the main channel reference level. This property configures NI-RFSA to optimize downconverter gain to measure a lower-power adjacent channel, adding gain only after filtering the main channel. The gain NI-RFSA applies is always less than or equal to the ACPR value you specify.

Note

Device Instantaneous Bandwidth

Span

IF Filter Bandwidth

Device Instantaneous Bandwidth

Span

IF Filter Bandwidth

Note

Note

IF Output Power Level

Reference Level

**Default Value**: 0

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Minimum ACPR |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-advancetrig-type.html language=enus -->
## TOPIC 00045: Triggers:Advance:Type

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-advancetrig-type.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-advancetrig-type.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether you want the Advance Trigger to be a digital edge or software trigger. Set this property to None if you set the Acquisition Type property to Spectrum or if you set the acquisition type parameter to Spectrum using the niRFSA Configure Acquisition Type VI. Default Value: None Support

### Triggers:Advance:Type

Specifies whether you want the Advance Trigger to be a digital edge or software trigger.

Note

None

Acquisition Type

Spectrum

acquisition type

Spectrum

niRFSA Configure Acquisition Type

**Default Value**: None

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

[PXI Trigger Lines](/csh?context=nirfsa_nirfsa_pxi-trigger-lines)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Advance Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSA Configure Trigger |
| Channel-based | No |
| Resettable | Yes |

| None | 600 | No Advance Trigger is configured. |
| --- | --- | --- |
| Digital Edge | 601 | The Advance Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the Digital Edge Advance Trigger Source property. |
| Software | 604 | The Advance Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the niRFSA Send Software Edge Trigger VI and setting the trigger input to Advance Trigger. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-advancetriggerterminalname.html language=enus -->
## TOPIC 00046: Triggers:Advance:Terminal Name

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-advancetriggerterminalname.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-advancetriggerterminalname.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. Default Values: PXIe-5830/5831/5832: /BasebandModule/ai/0/AdvanceTrigger, where BasebandModule is the name of the baseband module for your device in MAX. PXIe-5820/5840/5841/5842: /ModuleName/ai/0/AdvanceTrigger, where ModuleName is the name of yo

### Triggers:Advance:Terminal Name

Returns the fully qualified signal name as a string.

**Default Values**:

**PXIe-5830/5831/5832**: /*BasebandModule*/ai/0/AdvanceTrigger, where *BasebandModule* is the name of the baseband module for your device in MAX.

**PXIe-5820/5840/5841/5842**: /*ModuleName*/ai/0/AdvanceTrigger, where *ModuleName* is the name of your device in MAX.

**PXIe-5860**: /*ModuleName*/ai/*ChannelNumber*/AdvanceTrigger, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

**All other devices**: /*DigitizerName*/AdvanceTrigger, where *DigitizerName* is the name of your associated digitizer module in MAX.

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Events](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=events)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Advance Trigger Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niRFSA Get Terminal Name |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-allowoutofspecificationusersettings.html language=enus -->
## TOPIC 00047: Acquisition:Advanced:Allow Out Of Specification User Settings

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-allowoutofspecificationusersettings.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-allowoutofspecificationusersettings.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables warnings and errors when you set frequency, power, or bandwidth values beyond the limits of the NI-RFSA device specifications. When you enable this property, the driver does not report out-of-specification warnings and errors. Default Value: Disabled Supported Devices: PXIe-5820/

### Acquisition:Advanced:Allow Out Of Specification User Settings

Enables or disables warnings and errors when you set frequency, power, or bandwidth values beyond the limits of the NI-RFSA device specifications. When you enable this property, the driver does not report out-of-specification warnings and errors.

**Default Value**: Disabled

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Allow Out Of Specification User Settings |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Disabled | 1900 | The property is disabled. |
| --- | --- | --- |
| Enabled | 1901 | The property is enabled. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrection300mhzfilter.html language=enus -->
## TOPIC 00048: Self Calibration:NI 5665/5668R:Calibration Correction for 300 kHz Filter

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrection300mhzfilter.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrection300mhzfilter.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the internal gain self-calibration correction, in decibels, for the 300 kHz IF filter path. The value you set for this property overrides any previously-set value. Default Value: 0 Supported Devices: PXIe-5603/5605/5606 Remarks The following table lists the characteristics of this property. Sho

### Self Calibration:NI 5665/5668R:Calibration Correction for 300 kHz Filter

Sets the internal gain self-calibration correction, in decibels, for the 300 kHz IF filter path. The value you set for this property overrides any previously-set value.

**Default Value**: 0

**Supported Devices**: PXIe-5603/5605/5606

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Calibration Correction for 300 kHz Filter |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrection320mhzfilter.html language=enus -->
## TOPIC 00049: Self Calibration:NI 5665/5668R:Calibration Correction for 320 MHz Filter

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrection320mhzfilter.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrection320mhzfilter.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the internal gain self-calibration correction, decibels, for the 320 MHz IF filter path. The value you set for this property overrides any previously-set value. Default Value: 0 Supported Devices: PXIe-5606 Remarks The following table lists the characteristics of this property. Short Name Calib

### Self Calibration:NI 5665/5668R:Calibration Correction for 320 MHz Filter

Sets the internal gain self-calibration correction, decibels, for the 320 MHz IF filter path. The value you set for this property overrides any previously-set value.

**Default Value**: 0

**Supported Devices**: PXIe-5606

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Calibration Correction for 320 MHz Filter |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrection5mhzfilter.html language=enus -->
## TOPIC 00050: Self Calibration:NI 5665/5668R:Calibration Correction for 5 MHz Filter

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrection5mhzfilter.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrection5mhzfilter.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the internal gain self-calibration correction, in decibels, for the 5 MHz IF filter path. The value you set for this property overrides any previously-set value. Default Value: 0 Supported Devices: PXIe-5603/5605/5606 Remarks The following table lists the characteristics of this property. Short

### Self Calibration:NI 5665/5668R:Calibration Correction for 5 MHz Filter

Sets the internal gain self-calibration correction, in decibels, for the 5 MHz IF filter path. The value you set for this property overrides any previously-set value.

**Default Value**: 0

**Supported Devices**: PXIe-5603/5605/5606

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Calibration Correction for 5 MHz Filter |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrection765mhzfilter.html language=enus -->
## TOPIC 00051: Self Calibration:NI 5665/5668R:Calibration Correction for 765 MHz Filter

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrection765mhzfilter.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrection765mhzfilter.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the internal gain self-calibration correction, in decibels, for the 765 MHz IF filter path. The value you set for this property overrides any previously-set value. Default Value: 0 Supported Devices: PXIe-5606 Remarks The following table lists the characteristics of this property. Short Name Ca

### Self Calibration:NI 5665/5668R:Calibration Correction for 765 MHz Filter

Sets the internal gain self-calibration correction, in decibels, for the 765 MHz IF filter path. The value you set for this property overrides any previously-set value.

**Default Value**: 0

**Supported Devices**: PXIe-5606

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Calibration Correction for 765 MHz Filter |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrectionthroughfilter.html language=enus -->
## TOPIC 00052: Self Calibration:NI 5665/5668R:Calibration Correction for Through Filter

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrectionthroughfilter.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-calcorrectionthroughfilter.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the internal gain self-calibration correction, in decibels, for the IF filter through path. The value you set for this property overrides any previously-set value. Default Value: 0 Supported Devices: PXIe-5603/5605 Remarks The following table lists the characteristics of this property. Short Na

### Self Calibration:NI 5665/5668R:Calibration Correction for Through Filter

Sets the internal gain self-calibration correction, in decibels, for the IF filter through path. The value you set for this property overrides any previously-set value.

**Default Value**: 0

**Supported Devices**: PXIe-5603/5605

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Calibration Correction for Through Filter |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-caltonepowerreferredtorfin.html language=enus -->
## TOPIC 00053: Vertical:Advanced:NI 5693:Cal Tone Power Referred to RF IN

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-caltonepowerreferredtorfin.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-caltonepowerreferredtorfin.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power, in dBm, of a virtual signal connected to the RF IN connector on the PXIe-5693 front panel when the calibration tone is enabled. You can enable a calibration tone for the PXIe-5693 by setting the RF Conditioning Cal Tone Mode property to Low Band RF or High Band RF. Default Value:

### Vertical:Advanced:NI 5693:Cal Tone Power Referred to RF IN

Returns the power, in dBm, of a virtual signal connected to the RF IN connector on the PXIe-5693 front panel when the calibration tone is enabled.

You can enable a calibration tone for the PXIe-5693 by setting the [RF Conditioning Cal Tone Mode](pnirfsa-conditioningcaltonemode.html) property to **Low Band RF** or **High Band RF**.

**Default Value**: N/A

**Supported Devices**: PXIe-5693

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cal Tone Power |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-caltonestepattenuation.html language=enus -->
## TOPIC 00054: Factory Calibration:NI 5665/5668R:Cal Tone Step Attenuation

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-caltonestepattenuation.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-caltonestepattenuation.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the step attenuator, in decibels, to engage in the calibration tone path. This property is valid only during a calibration session. Valid Values: PXIe-5606: 0 to 31 PXIe-5693: 2.00, 10.00 Default Values: PXIe-5606: 0 dB PXIe-5693: 2.00 dB Supported Devices: PXIe-5606, PXIe-5693 Remarks The

### Factory Calibration:NI 5665/5668R:Cal Tone Step Attenuation

Specifies the step attenuator, in decibels, to engage in the calibration tone path. This property is valid only during a calibration session.

**Valid Values:**

**PXIe-5606**: 0 to 31

**PXIe-5693**: 2.00, 10.00

**Default Values:**

**PXIe-5606**: 0 dB

**PXIe-5693**: 2.00 dB

**Supported Devices**: PXIe-5606, PXIe-5693

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cal Tone Step Attenuation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-channelcoupling.html language=enus -->
## TOPIC 00055: Vertical:Advanced:NI 5665/5667/5668R:Channel Coupling

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-channelcoupling.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-channelcoupling.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter. For the PXIe-5605/5606/5665/5667/5668, this property must be set to AC Coupled when the DC block is present and set to DC Coupled when the DC block is not present to ensure device specifications are met and proper calib

### Vertical:Advanced:NI 5665/5667/5668R:Channel Coupling

Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter.

Note

AC Coupled

DC Coupled

PXIe-5665 Block Diagram

PXIe-5605 Front Panel and LEDs

PXIe-5667 Block Diagram

PXIe-5668 Block Diagram

**Valid Values**:

**PXIe-5603/5665 (3.6 GHz)**—AC Coupled, DC Coupled

**PXIe-5605/5665 (14 GHz)**—AC Coupled, DC Coupled

**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low-frequency bypass path**—AC Coupled, DC Coupled

**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**—AC Coupled

**PXIe-5667 (7 GHz)**—AC Coupled

**PXIe-5606/5668**—AC Coupled, DC Coupled

**Default Value**: AC Coupled

**Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Channel Coupling |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| AC Coupled | 3001 | Specifies that the RF input channel is AC-coupled. For low frequencies (<10 MHz), accuracy decreases because NI-RFSA does not calibrate the configuration. |
| --- | --- | --- |
| DC Coupled | 3002 | Specifies that the RF input channel is DC-coupled. NI-RFSA enforces a minimum RF attenuation for device protection. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-decimationdelay.html language=enus -->
## TOPIC 00056: Device Specific:Vector Signal Transceiver:Signal Path:Decimation Delay

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-decimationdelay.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-decimationdelay.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sub-sample delay, in seconds, to apply to the acquired signal. To set this property, the NI-RFSA device must be in the Configuration state. Valid Values: -4.16 ns to +4.16 ns Default Value: 0 Supported Devices: PXIe-5644/5645/5646 Remarks The following table lists the characteristics o

### Device Specific:Vector Signal Transceiver:Signal Path:Decimation Delay

Specifies the sub-sample delay, in seconds, to apply to the acquired signal. To set this property, the NI-RFSA device must be in the Configuration state.

**Valid Values**: -4.16 ns to +4.16 ns

**Default Value**: 0

**Supported Devices**: PXIe-5644/5645/5646

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Decimation Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-deembeddingcompensationgain.html language=enus -->
## TOPIC 00057: De-embedding:Compensation Gain

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-deembeddingcompensationgain.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-deembeddingcompensationgain.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the de-embedding gain applied to compensate for the mismatch on the specified port. Use the Active Channel property to specify the name of the port to configure for de-embedding. If de-embedding is enabled, NI-RFSA uses the returned compensation gain to remove the effects of the external net

### De-embedding:Compensation Gain

Returns the de-embedding gain applied to compensate for the mismatch on the specified port. Use the [Active Channel](/csh?topicname=pnirfsa-activechannel.html) property to specify the name of the port to configure for de-embedding.

If de-embedding is enabled, NI-RFSA uses the returned compensation gain to remove the effects of the external network between the instrument and the DUT.

**Supported Devices**: PXIe-5830/5831/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | De-embedding Compensation Gain |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-deembeddingselectedtable.html language=enus -->
## TOPIC 00058: De-embedding:Selected Table

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-deembeddingselectedtable.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-deembeddingselectedtable.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the de-embedding table to apply to the measurements on the specified port. Use the Active Channel property to specify the name of the port to configure for de-embedding. If de-embedding is enabled, NI-RFSA uses the specified table to remove the effects of the external network between the ins

### De-embedding:Selected Table

Selects the de-embedding table to apply to the measurements on the specified port. Use the [Active Channel](/csh?topicname=pnirfsa-activechannel.html) property to specify the name of the port to configure for de-embedding.

If de-embedding is enabled, NI-RFSA uses the specified table to remove the effects of the external network between the instrument and the DUT.

Use the [niRFSA Create S-parameter Table](/csh?context=nirfsa_rfsaviref_nirfsa_create_deembedding_sparameter_table) VI to create tables.

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | De-embedding Selected Table |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-deviceinstantaneousbandwidth.html language=enus -->
## TOPIC 00059: Acquisition:Device Instantaneous Bandwidth (Hz)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-deviceinstantaneousbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-deviceinstantaneousbandwidth.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the instantaneous bandwidth of the device in Hz. The instantaneous bandwidth is the effective real-time bandwidth of the signal path for your configuration. Specify the maximum instantaneous bandwidth needed for your measurement. NI-RFSA coerces the actual IF filter to use based on other m

### Acquisition:Device Instantaneous Bandwidth (Hz)

Specifies the instantaneous bandwidth of the device in Hz. The instantaneous bandwidth is the effective real-time bandwidth of the signal path for your configuration.

Specify the maximum instantaneous bandwidth needed for your measurement. NI-RFSA coerces the actual IF filter to use based on other measurement constraints such as the [IF Filter Bandwidth](pnirfsa-iffilterbandwidth.html) property and the [Digital IF Equalization Enabled](pnirfsa-digitalifequalizationenabled.html) property.

To change the value that NI-RFSA uses for the maximum size of multispan acquisition subspans, use the [FFT Width](pnirfsa-fftwidth.html) property.

The [Signal Bandwidth](pnirfsa-signalbandwidth.html), centered at the [IQ Carrier Frequency](pnirfsa-iqcarrierfrequency.html), must fit within the Device Instantaneous Bandwidth, which is centered at the [Downconverter Center Frequency](pnirfsa-downconvertercenterfrequency.html).

Note

**PXI-5661**ï¿½The PXI-5600 RF downconverter instantaneous bandwidth is 20 MHz.

**PXIe-5663/5663E**ï¿½Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the [PXIe-5601 RF downconverter overview](https://ni.com/docs/en-US/csh?pubname=pxie-5663-5663e-feature&topicname=overview) for more information about instantaneous bandwidth.

Note

**PXIe-5665**ï¿½Your maximum allowed instantaneous bandwidth is independent of the downconverter center frequency. Refer to the *NI PXIe-5665 Specifications* for more information about instantaneous bandwidth.

**PXIe-5665 (14 GHz), PXIe-5668**—If you have enabled the preselector for the PXIe-5605/5606, the device instantaneous bandwidth value is only a typical specification. For multispan acquisitions, NI-RFSA uses this typical specification as the maximum size for the acquisition subspans.

Note

Note

**PXIe-5693**—This property is read-only for the PXIe-5693. The value for the device instantaneous bandwidth depends on the value for the RF preselector filter.

**PXIe-5694/PXIe-5667**—If your application uses the PXIe-5694 as part of an PXIe-5667 spectrum monitoring receiver or the PXIe-5694 as a stand-alone device, NI-RFSA determines the appropriate IF filter to use based on the value that you set for this property.

Note

Signal Conditioning Enabled

Bypassed

| Device Instantaneous Bandwidth Property Value Frequency Range | IF Filter |
| --- | --- |
| ≤30 kHz (IF Conditioning Downconversion Enabled property set to Enabled) | 30 kHz |
| >30 kHz and ≤400 kHz | 400 kHz |
| >400 kHz and ≤1.4 MHz | 1.4 MHz |
| >1.4 MHz and ≤5 MHz | 5 MHz |
| >5 MHz and ≤20 MHz | 20 MHz |
| >20 MHz (Signal Conditioning Enabled property set to Bypassed) | Bypass |

**PXIe-5644/5645/5646**—This property is read-only for the PXIe-5644/5645/5646. Refer to the specifications document for your device for more information about instantaneous bandwidth.

**PXIe-5840/5841/5860**—Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the *NI PXIe-5840/5841/5842/5860 Specifications* for more information about instantaneous bandwidth. Set this property to select different device instantaneous bandwidths for a given downconverter center frequency. The device instantaneous bandwidth that you select is greater than or equal to the requested instantaneous bandwidth. If this property is not set, NI-RFSA uses the maximum allowed instantaneous bandwidth.

**PXIe-5842**—Your maximum allowed instantaneous bandwidth depends on the device's hardware options, configured device personality, and the downconverter center frequency you use. Refer to the *NI PXIe-5842 Specifications* for more information about instantaneous bandwidth and device personality. Set this property to select different device instantaneous bandwidths for a given downconverter center frequency. The device instantaneous bandwidth that you select is greater than or equal to the requested instantaneous bandwidth. If this property is not set, NI-RFSA uses the maximum allowed instantaneous bandwidth.

**Default Value**: N/A

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[PXIe-5830 Frequency and Bandwidth Selection](https://ni.com/docs/en-US/csh?pubname=pxie-5830-feature&topicname=frequency-and-bandwidth-selection)

[PXIe-5831/5832 Frequency and Bandwidth Selection](https://ni.com/docs/en-US/csh?pubname=pxie-5831&topicname=frequency-and-bandwidth-selection)

[PXIe-5841 Frequency and Bandwidth Selection](https://ni.com/docs/en-US/csh?pubname=pxie-5841&topicname=frequency-and-bandwidth-selection)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Device Instantaneous Bandwidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-devicetemp.html language=enus -->
## TOPIC 00060: Device Characteristics:Device Temperature (Degrees C)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-devicetemp.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-devicetemp.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current temperature, in degrees Celsius, of the module. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters—If you query this property during RF list mode, list steps may take longer to com

### Device Characteristics:Device Temperature (Degrees C)

Returns the current temperature, in degrees Celsius, of the module.

**PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters**—If you query this property during RF list mode, list steps may take longer to complete during list execution.

**PXIe-5830/5831/5832**—To use this property, you must first set the [Active Channel](pnirfsa-activechannel.html) property using the appropriate string for your instrument configuration. Setting the Active Channel property is not required for the PXIe-3621/3622/3623. Refer to the following table to determine which strings are valid for your configuration.

| Hardware Module | TRX Port Type | Active Channel String |
| --- | --- | --- |
| PXIe-3621/3622/3623 | — | if or "" (empty string) |
| PXIe-5820 | — | fpga |
| First connected mmRH-5582 | DIRECT TRX PORTS Only | rf0 |
| SWITCHED TRX PORTS [0-7] | rf0switch0 |  |
| SWITCHED TRX PORTS [8-15] | rf0switch1 |  |
| Second connected mmRH-5582 | DIRECT TRX PORTS Only | rf1 |
| SWITCHED TRX PORTS [0-7] | rf1switch0 |  |
| SWITCHED TRX PORTS [8-15] | rf1switch1 |  |

**Default Value**: N/A

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Device Temperature |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitalgain.html language=enus -->
## TOPIC 00061: Vertical:Advanced:Digital Gain (dB)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitalgain.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitalgain.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the scaling factor, in decibels, applied to the time-domain voltage data in the digitizer. NI-RFSA does not compensate for the specified digital gain. You can use this property to account for external gain changes without changing the analog signal path. The PXIe-5644/5645/5646 applies thi

### Vertical:Advanced:Digital Gain (dB)

Specifies the scaling factor, in decibels, applied to the time-domain voltage data in the digitizer. NI-RFSA does not compensate for the specified digital gain.

You can use this property to account for external gain changes without changing the analog signal path.

Note

**Default Value**: 0 dB

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Gain |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitalifequalizationenabled.html language=enus -->
## TOPIC 00062: Signal Path:Digital IF Equalization Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitalifequalizationenabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitalifequalizationenabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables use of the digital equalization filter for the RF downconverter. PXIe-5820/5830/5831/5832/5840/5841/5842/5860—The only valid value for this property is TRUE. For PXIe-5665/5667 devices, digital IF equalization is supported only with a 150 MHz clock. You cannot set this property to TRUE if th

### Signal Path:Digital IF Equalization Enabled

Enables use of the digital equalization filter for the RF downconverter.

**PXIe-5820/5830/5831/5832/5840/5841/5842/5860**—The only valid value for this property is TRUE.

Note

Digitizer Sample Clock Timebase Source

LORefClk

Note

**Default Value**: TRUE, if the device configuration is supported.

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

| TRUE | Enables digital IF equalization on the RF downconverter. |
| --- | --- |
| FALSE | Disables digital IF equalization on the RF downconverter. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital IF Equalization Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizersampclkexportedterm.html language=enus -->
## TOPIC 00063: Clocking:Digitizer Sample Clock Exported Terminal

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizersampclkexportedterm.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizersampclkexportedterm.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal at which to export the Digitizer Sample Clock. Default Value: "" (empty string) Supported Devices: PXIe-5668 Remarks The following table lists the characteristics of this property. Short Name Digitizer Sample Clock Exported Terminal Data type cstr.png Permissions Read/Write Hi

### Clocking:Digitizer Sample Clock Exported Terminal

Specifies the terminal at which to export the Digitizer Sample Clock.

**Default Value**: "" (empty string)

**Supported Devices**: PXIe-5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digitizer Sample Clock Exported Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| None | None | The Sample Clock is not exported from the Digitizer. |
| --- | --- | --- |
| ClkOut | ClkOut | Export the Sample Clock on the CLK OUT terminal on the Digitizer. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizersampclkrate.html language=enus -->
## TOPIC 00064: Clocking:Digitizer Sample Clock Rate

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizersampclkrate.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizersampclkrate.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency, in Hz, of the Sample Clock on the digitizer. Supported Devices: PXIe-5668 Remarks The following table lists the characteristics of this property. Short Name Digitizer Sample Clock Rate Data type cdbl.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Clocking:Digitizer Sample Clock Rate

Specifies the frequency, in Hz, of the Sample Clock on the digitizer.

**Supported Devices**: PXIe-5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digitizer Sample Clock Rate |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizersampclktimebaserate.html language=enus -->
## TOPIC 00065: Clocking:Digitizer Sample Clock Timebase Rate

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizersampclktimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizersampclktimebaserate.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency, in Hz, of the external clock used as the timebase source if you set the Digitizer Sample Clock Timebase Source property to an external source, such as ClkIn or LORefClk. PXI-5661—If this property is set to a value less than 60 MHz, signals at frequencies just above the 20 MH

### Clocking:Digitizer Sample Clock Timebase Rate

Specifies the frequency, in Hz, of the external clock used as the timebase source if you set the [Digitizer Sample Clock Timebase Source](/csh?topicname=pnirfsa-digitizersampclktimebasesrc.html) property to an external source, such as **ClkIn** or **LORefClk**.

**PXI-5661**—If this property is set to a value less than 60 MHz, signals at frequencies just above the 20 MHz passband of the downconverter may be aliased back into the passband. This aliasing occurs because the IF frequency of the downconverter is at 15 MHz, and the upper end of the passband is at 25 MHz. At sampling rates below 60 MHz, the Nyquist frequency is close to the end of the passband and creates aliases that are not filtered effectively by the downconverter.

**PXIe-5663/5663E/5665/5667**—The PXIe-5663/5663E/5665/5667 supports only a 150 MHz external clock.

**PXIe-5668**—The PXIe-5668 supports only a 2 GHz external clock.

**Default Value**: 150 MHz

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digitizer Sample Clock Timebase Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizersampclktimebasesrc.html language=enus -->
## TOPIC 00066: Clocking:Digitizer Sample Clock Timebase Source

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizersampclktimebasesrc.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizersampclktimebasesrc.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the Sample Clock timebase, which is the timebase used to control waveform sampling. Default Value: OnboardClock Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668 Remarks The following table lists the characteristics of this property. Short Name Digitizer Sample Cloc

### Clocking:Digitizer Sample Clock Timebase Source

Specifies the source of the Sample Clock timebase, which is the timebase used to control waveform sampling.

**Default Value**: OnboardClock

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digitizer Sample Clock Timebase Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| OnboardClock | OnboardClock | The digitizer uses its onboard clock as the Sample Clock timebase. |
| --- | --- | --- |
| ClkIn | ClkIn | The digitizer uses the signal present on the CLK IN connector as the Sample Clock timebase. |
| LORefClk | LORefClk | The digitizer uses the signal generated on the 100 MHz REF OUT terminal on the PXIe-5653 as the Sample Clock timebase. This value is supported only for the PXIe-5665. |
| PXI_STAR | PXI_STAR | The digitizer uses the signal present at the PXI star trigger line as the Sample Clock timebase. |
| DownconverterLO2Out | DownconverterLO2Out | The digitizer uses the signal exported from the LO2 OUT terminal on the PXIe-5606 as the Sample Clock timebase. This value is supported only for the PXIe-5668. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizertemp.html language=enus -->
## TOPIC 00067: Device Characteristics:Digitizer Temperature (Degrees C)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizertemp.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizertemp.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current temperature, in degrees Celsius, of the digitizer module. PXIe-5820/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters—If you query this property during RF list mode, list steps may take longer to complete durin

### Device Characteristics:Digitizer Temperature (Degrees C)

Returns the current temperature, in degrees Celsius, of the digitizer module.

**PXIe-5820/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters**—If you query this property during RF list mode, list steps may take longer to complete during list execution.

**Default Value**: N/A

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860, PXIe-5842 with S-parameters, PXIe-5842 with 54GHz Frequency Extension, PXIe-5860 with S-parameters

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digitizer Temperature |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizerverticalrange.html language=enus -->
## TOPIC 00068: Vertical:Digitizer Vertical Range

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizerverticalrange.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-digitizerverticalrange.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the vertical range of the digitizer. The vertical range is defined as the absolute value of the input range for a channel. The default vertical range works for all device configurations, but you can use this property to optimize performance if you know that the signal level at the digitize

### Vertical:Digitizer Vertical Range

Specifies the vertical range of the digitizer. The vertical range is defined as the absolute value of the input range for a channel. The default vertical range works for all device configurations, but you can use this property to optimize performance if you know that the signal level at the digitizer input terminal is low.

Note

This property is expressed in volts. For example, to acquire a sine wave that spans between –0.5 and +0.5 V, set this property to 1.0.

**PXIe-5840/5841/5842/5860**—This property is read-only.

**Default Value**: 1.0

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digitizer Vertical Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-doneevent-outputterm.html language=enus -->
## TOPIC 00069: Events:Done:Output Terminal

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-doneevent-outputterm.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-doneevent-outputterm.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Done Event. Default Value: "" (empty string) Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Remarks The following table lists the characteristics of this property. Short Name Do

### Events:Done:Output Terminal

Specifies the destination terminal for the Done Event.

**Default Value**: "" (empty string)

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Do not export signal |  | The signal is not exported. |
| --- | --- | --- |
| ClkOut | ClkOut | The signal is exported to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut | RefOut | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut2 | RefOut2 | The signal is exported to the REF OUT2 terminal on the LO. This connector exists on only the PXIe-5652. |
| PFI0 | PFI0 | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| PFI1 | PFI1 | The signal is exported to the PFI 1 connector on the PXIe-5142 and PXIe-5622. |
| PXI_Trig0 | PXI_Trig0 | The signal is exported to the PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | The signal is exported to the PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | The signal is exported to the PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | The signal is exported to the PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | The signal is exported to the PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | The signal is exported to the PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | The signal is exported to the PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | The signal is exported to the PXI trigger line 7. |
| PXI_STAR | PXI_STAR | The signal is exported to the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. |
| PXIe_DStarC | PXIe_DStarC | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| DIO/PFI0 | DIO/PFI0 | The signal is exported to the PFI 0 on the DIO front panel connector |
| DIO/PFI1 | DIO/PFI1 | The signal is exported to the PFI 1 on the DIO front panel connector |
| DIO/PFI2 | DIO/PFI2 | The signal is exported to the PFI 2 on the DIO front panel connector |
| DIO/PFI3 | DIO/PFI3 | The signal is exported to the PFI 3 on the DIO front panel connector |
| DIO/PFI4 | DIO/PFI4 | The signal is exported to the PFI 4 on the DIO front panel connector |
| DIO/PFI5 | DIO/PFI5 | The signal is exported to the PFI 5 on the DIO front panel connector |
| DIO/PFI6 | DIO/PFI6 | The signal is exported to the PFI 6 on the DIO front panel connector |
| DIO/PFI7 | DIO/PFI7 | The signal is exported to the PFI 7 on the DIO front panel connector |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-doneevent-terminalname.html language=enus -->
## TOPIC 00070: Events:Done:Terminal Name

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-doneevent-terminalname.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-doneevent-terminalname.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. Default Values: PXIe-5830/5831/5832: /BasebandModule/ai/0/DoneEvent, where BasebandModule is the name of the baseband module for your device in MAX. PXIe-5820/5840/5841/5842: /ModuleName/ai/0/DoneEvent, where ModuleName is the name of your device

### Events:Done:Terminal Name

Returns the fully qualified signal name as a string.

**Default Values**:

**PXIe-5830/5831/5832**: /*BasebandModule*/ai/0/DoneEvent, where *BasebandModule* is the name of the baseband module for your device in MAX.

**PXIe-5820/5840/5841/5842**: /*ModuleName*/ai/0/DoneEvent, where *ModuleName* is the name of your device in MAX.

**PXIe-5860**: /*ModuleName*/ai/*ChannelNumber*/DoneEvent, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

**All other devices**: /*DigitizerName*/DoneEvent, where *DigitizerName* is the name of your associated digitizer module in MAX.

**Supported Devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-downconversionenabled.html language=enus -->
## TOPIC 00071: Signal Path:Advanced:IF Conditioning Downconversion Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-downconversionenabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-downconversionenabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether downconversion to 21.4 MHz is enabled for the IF conditioning module. The IF output frequency is 21.4 MHz when you enable this property, and it is 193.6 MHz when you disable this property. If you set the Signal Conditioning Enabled property to Bypassed, you cannot set the IF Condit

### Signal Path:Advanced:IF Conditioning Downconversion Enabled

Specifies whether downconversion to 21.4 MHz is enabled for the IF conditioning module. The IF output frequency is 21.4 MHz when you enable this property, and it is 193.6 MHz when you disable this property.

Note

Signal Conditioning Enabled

Bypassed

Enabled

Note

Disabled

**Default Value**: Disabled

**Supported Devices**: PXIe-5667, PXIe-5694

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IF Conditioning Downconversion Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Disabled | 1900 | The property is disabled. |
| --- | --- | --- |
| Enabled | 1901 | The property is enabled. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-externalgain-5601.html language=enus -->
## TOPIC 00072: Vertical:Advanced:External Gain (dB)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-externalgain-5601.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-externalgain-5601.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the gain, in decibels, of a switch (or cable) connected before the RF IN connector of an NI-RFSA system. When you set this property, NI-RFSA calculates appropriate attenuator settings based on the value of this property and the value of the Reference Level property. In this case, NI-RFSA i

### Vertical:Advanced:External Gain (dB)

Specifies the gain, in decibels, of a switch (or cable) connected before the RF IN connector of an NI-RFSA system. When you set this property, NI-RFSA calculates appropriate attenuator settings based on the value of this property and the value of the [Reference Level](/csh?topicname=pnirfsa-referencelevel.html) property. In this case, NI-RFSA interprets the reference level as the maximum expected power level of the signal at the input of the external gain device. For more information about attenuation, refer to the *Attenuation and Signal Levels* topic for your device in the *NI RF Vector Signal Analyzers Help*.

Note

Note

With this property set, NI-RFSA reads the [IQ Power Edge Trigger Level](pnirfsa-reftrig-iqpwredge-lvl.html) property value as the power level at the input of the external gain device at which the NI-RFSA device should trigger.

Negative values indicate attenuation.

**Default Value**: 0

**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | External Gain |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fetchoffset.html language=enus -->
## TOPIC 00073: Acquisition:Fetch:Fetch Offset

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fetchoffset.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fetchoffset.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset relative to the position specified by the Fetch Relative To property from which to start fetching data. Offset can be a positive or negative value. Default Value: 0 Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/58

### Acquisition:Fetch:Fetch Offset

Specifies the offset relative to the position specified by the [Fetch Relative To](/csh?topicname=pnirfsa-fetchrelativeto.html) property from which to start fetching data. Offset can be a positive or negative value.

**Default Value**: 0

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fetch Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fftwidth.html language=enus -->
## TOPIC 00074: Acquisition:Spectrum:FFT Width

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fftwidth.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fftwidth.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition. The maximum FFT width when using the PXIe-5622 is constrained to 50 MHz or 25 MHz, depending on the digitizer option you purchased. The maximum FFT width when using the

### Acquisition:Spectrum:FFT Width

Specifies the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition.

Note

Note

Downconverter Center Frequency

NI-RFSA treats the *device instantaneous bandwidth* as the effective real-time bandwidth of the signal path. The *span* specifies the frequency range of the computed spectrum. A vector signal analyzer can acquire a bandwidth only within the device instantaneous bandwidth frequency. If the span you choose is greater than the device instantaneous bandwidth, NI-RFSA obtains multiple acquisitions and combines them into a single spectrum. By specifying the FFT width, you can control the specific bandwidth obtained in each signal acquisition. If you read the FFT Width property without setting it, NI-RFSA returns the value of the [Device Instantaneous Bandwidth](pnirfsa-deviceinstantaneousbandwidth.html) property.

Note

Smooth Spectrum Enabled

enabled

**Valid Values**:

The lower limit for all FFT width supported devices using the PXIe-5622 digitizer is 7.325 kHz. The lower limit for all FFT width supported devices using the PXIe-5624 digitizer is 400 MHz or 800 MHz, depending on the FPGA image that is downloaded upon opening the session to the PXIe-5624 digitizer.

**PXIe-5663/5663E**—The FFT width upper limit for the PXIe-5663/5663E depends on the RF frequency and on the module revision of the PXIe-5601 as illustrated in the following table. Refer to the [Identifying Module Revision](https://ni.com/docs/en-US/csh?pubname=pxie-5663-5663e-feature&topicname=identifying-module-revision) topic for more information about determining which revision of the PXIe-5601 RF downconverter you have installed.

| RF Frequency | PXIe-5601 Instantaneous Bandwidth | FFT Width Upper Limit |
| --- | --- | --- |
| 10 MHz to <120 MHz | 10 MHz | 10 MHz (Revision E), 20 MHz* (Revision G or later) |
| 120 MHz to <330 MHz | 20 MHz | 20 MHz (Revision E), 30 MHz* (Revision G or later) |
| 330 MHz to <6.6 GHz | 50 MHz | 50 MHz |
| *National Instruments does not guarantee device specifications if you set the FFT Width property greater than the warranted instantaneous bandwidth specification. |  |  |

**PXIe-5665/5667/5668**—The upper limit of the FFT width is the maximum device instantaneous bandwidth.

If you do not set the [Device Instantaneous Bandwidth](pnirfsa-deviceinstantaneousbandwidth.html) property for the PXIe-5665/5667/5668, NI-RFSA determines the appropriate IF filter to use based on the value that you set for the FFT width and your specific device. Refer to the following tables to determine which IF filter corresponds to each FFT width frequency range for your device.

If you set the Device Instantaneous Bandwidth property, NI-RFSA selects the appropriate IF filter based on the Device Instantaneous Bandwidth property and the FFT Width property determines how much filter bandwidth is used during acquisition. Refer to the Device Instantaneous Bandwidth property to determine which IF filter corresponds to the Device Instantaneous Bandwidth property setting.

| Device | FFT Width Property Value Frequency Range | IF Filter |
| --- | --- | --- |
| PXIe-5603/5665 (3.6 GHz) | ≤300 kHz | 300 kHz IF filter |
| >300 kHz and ≤5 MHz | Through IF filter |  |
| >5 MHz | Through IF filter |  |
| PXIe-5605/5665 (14 GHz) | ≤300 kHz | 300 kHz IF filter |
| >300 kHz and ≤5 MHz | 5 MHz IF filter |  |
| >5 MHz | Through IF filter |  |
| PXIe-5667 | ≤30 kHz (IF Conditioning Downconversion Enabled property set to Enabled) | 30 kHz |
| >30 kHz and ≤400 kHz | 400 kHz |  |
| ≤400 kHz (IF Conditioning Downconversion Enabled property set to Disabled) | 400 kHz |  |
| >400 kHz and ≤1.4 MHz | 1.4 MHz |  |
| >1.4 MHz and ≤5 MHz | 5 MHz |  |
| >5 MHz and ≤20 MHz | 20 MHz |  |
| >20 MHz and 50 MHz (Signal Conditioning Enabled property set to Bypassed) | Bypass |  |
| PXIe-5668 | ≤300 KHz | 300 KHz |
| >300 KHz and ≤5 MHz | 5 MHz |  |
| >5 MHz and ≤100 MHz | 100 MHz |  |
| >100 MHz and ≤320 MHz | 320 MHz |  |
| >320 MHz and ≤400 MHz | (high band) 765 MHz |  |
| (low band) 320 MHz |  |  |

Note

Note

**Default Value**: N/A

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FFT Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-firmwarerevision.html language=enus -->
## TOPIC 00075: Inherent IVI Attributes:Instrument Identification:Firmware Revision

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-firmwarerevision.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-firmwarerevision.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the firmware revision information for the NI-RFSA downconverter for the composite device you are currently using. PXIe-5820/5830/5831/5832/5840/5841/5842/5860 devices will return "No revision information available." To retrieve the firmware revision, use MAX, Hardware Con

### Inherent IVI Attributes:Instrument Identification:Firmware Revision

Returns a string containing the firmware revision information for the NI-RFSA downconverter for the composite device you are currently using.

Note

**Default Value**: N/A

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Firmware Revision |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fixedgroupdelayacrossports.html language=enus -->
## TOPIC 00076: Signal Path:Advanced:Fixed Group Delay Across Ports

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fixedgroupdelayacrossports.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fixedgroupdelayacrossports.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a comma-separated list of ports for which to fix the group delay. Valid Values: PXIe-5831/5832: rf<0-1>/port<x> , where 0-1 indicates one (0 ) or two (1 ) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel. Default Value: PXIe-5831/5832: "" (empty string), which sp

### Signal Path:Advanced:Fixed Group Delay Across Ports

Specifies a comma-separated list of ports for which to fix the group delay.

**Valid Values**:

PXIe-5831/5832: rf*<0-1>*/port*<x>*, where *0-1* indicates one (*0*) or two (*1*) mmRH-5582 connections and *x* is the port number on the mmRH-5582 front panel.

**Default Value**:

PXIe-5831/5832: "" (empty string), which specifies that the group delay will not be fixed for any port.

**Supported Devices**: PXIe-5831/5832

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fixed Group Delay Across Ports |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fpgabitfilepath.html language=enus -->
## TOPIC 00077: Device Characteristics:FPGA Bitfile Path

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fpgabitfilepath.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fpgabitfilepath.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the path to the location of the current NI-RFSA instrument driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device. You can specify the bitfile location using the Driver Setup string in the option string property of the niRFSA Initialize With Opti

### Device Characteristics:FPGA Bitfile Path

Returns a string containing the path to the location of the current NI-RFSA instrument driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device. You can specify the bitfile location using the Driver Setup string in the **option string** property of the [niRFSA Initialize With Options](/csh?context=nirfsa_rfsaviref_nirfsa_initialize_with_options) VI.

NI-RFSA instrument driver FPGA extensions enable you to use pre-compiled FPGA bitfiles to customize the behavior of the device FPGA while maintaining the functionality of the NI-RFSA instrument driver.

Refer to [NI-RFSA Instrument Driver FPGA Extensions](https://ni.com/docs/en-US/csh?pubname=ni-rf-vst&topicname=rfsa-rfsg-instrument-driver-fpga-extensions) for more information about using NI-RFSA instrument driver FPGA extensions for NI devices.

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FPGA Bitfile Path |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fpgatargetname.html language=enus -->
## TOPIC 00078: Device Characteristics:FPGA Target Name

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fpgatargetname.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fpgatargetname.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the name of the FPGA target being used. This name can be used with the RIO open session to open a reference to the FPGA. This property is channel dependent if multiple targets are supported. Supported Devices: PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Remark

### Device Characteristics:FPGA Target Name

Returns a string containing the name of the FPGA target being used. This name can be used with the RIO open session to open a reference to the FPGA.

This property is channel dependent if multiple targets are supported.

**Supported Devices**: PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FPGA Target Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fractionalresampleenabled.html language=enus -->
## TOPIC 00079: Signal Path:Fractional Resample Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fractionalresampleenabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-fractionalresampleenabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether fractional resampling is enabled on the digitizer. Fractional resampling allows the digitizer to achieve very fine resolution on the I/Q rate value. Setting this property to FALSE improves spectral performance. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: The

### Signal Path:Fractional Resample Enabled

Specifies whether fractional resampling is enabled on the digitizer. Fractional resampling allows the digitizer to achieve very fine resolution on the I/Q rate value. Setting this property to FALSE improves spectral performance.

**PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: The only valid value for this property is **TRUE**.

**PXIe-5668**: When using a 400 MHz FPGA image, the only valid value for this property is **TRUE**. When using a 800 MHz FPGA image, the only valid value for this property is **FALSE**. Refer to [NI-RFSA Instrument Driver FPGA Extensions](https://ni.com/docs/en-US/csh?pubname=ni-rf-vst&topicname=rfsa-rfsg-instrument-driver-fpga-extensions) for more information about FPGA images.

**Default Value**: TRUE

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

| TRUE | Enables fractional resampling. |
| --- | --- |
| FALSE | Disables fractional resampling. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fractional Resample Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-frequencysettling-5601.html language=enus -->
## TOPIC 00080: Signal Path:Advanced:Frequency Settling

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-frequencysettling-5601.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-frequencysettling-5601.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value used for local oscillator (LO) frequency settling. The units and interpretation for this scalar value are specified using the Frequency Settling Units property. This property is not supported if you are using an external LO. Valid Values: Frequency Settling Units Property Value P

### Signal Path:Advanced:Frequency Settling

Specifies the value used for local oscillator (LO) frequency settling. The units and interpretation for this scalar value are specified using the [Frequency Settling Units](/csh?topicname=pnirfsa-frequencysettlingunits-5601.html) property. This property is not supported if you are using an external LO.

**Valid Values**:

| Frequency Settling Units Property Value | PXIe-5663/5663E | PXIe-5665/5668 | PXIe-5644/5645/5646 | PXIe-5830/5831/5832/5840/5841/5842, PXIe-5831 with PXIe-5653 (using PXIe-3622 LO)3 | PXIe-5831 with PXIe-5653 (using PXIe-5653 LO) and PXIe-5832 with PXIe-5653 (using PXIe-5653 LO)3 |
| --- | --- | --- | --- | --- | --- |
| Seconds After Lock | 2 microseconds1 to 80 milliseconds, resolution of approximately 2 microseconds | 4 microseconds to 80 milliseconds, resolution of approximately 4 microseconds | 1 microsecond1 to 65 milliseconds, resolution of 1 microsecond | 1 microsecond1 to 10 seconds, resolution of 1 microsecond | 4 microseconds to 80 milliseconds, resolution of approximately 4 microseconds |
| Seconds After I/O | 0 microseconds to 80 milliseconds2, resolution of 1 microsecond | 0 microseconds to 80 milliseconds2, resolution of 1 microsecond | 1 microsecond to 65 milliseconds, resolution of 1 microsecond | 0 microseconds to 10 seconds, resolution of 1 microsecond | 0 microseconds to 80 milliseconds2, resolution of 1 microsecond |
| PPM | 1.0, 0.1, 0.01 | 1.0, 0.1, 0.01, 0.001 | 1.0, 0.1, 0.01 | 1.0 to 0.01 | 1.0 to 0.01 |

| 1If the Frequency Settling Units property is set to Seconds After Lock and the Downconverter Loop Bandwidth property is set to Narrow, NI recommends a minimum settling time of 128 microseconds to ensure that the phase-locked loop (PLL) lock stabilizes. If the Downconverter Loop Bandwidth property is set to Wide, NI recommends a minimum settling time of 16 microseconds. 2When in RF list mode, the valid values for Seconds After I/O are 0 microseconds to 50 milliseconds. 3The valid values for this configuration depend on the module used as the LO source. Refer to the LO Source property for more information. |
| --- |

**Default Value**: 0.1

**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frequency Settling |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-frequencysettlingunits-5601.html language=enus -->
## TOPIC 00081: Signal Path:Advanced:Frequency Settling Units

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-frequencysettlingunits-5601.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-frequencysettlingunits-5601.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the delay duration units and interpretation for LO settling. Specify the actual settling value using the Frequency Settling property. This property is not supported if you are using an external LO. Default Value: PPM Supported Devices: PXIe-5601/5603/5605/5606 (external digitizer mode), PX

### Signal Path:Advanced:Frequency Settling Units

Specifies the delay duration units and interpretation for LO settling. Specify the actual settling value using the [Frequency Settling](/csh?topicname=pnirfsa-frequencysettling-5601.html) property. This property is not supported if you are using an external LO.

**Default Value**: PPM

**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frequency Settling Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| PPM | 2000 | Specifies the frequency settling in parts per million (PPM). |
| --- | --- | --- |
| Seconds After Lock | 2001 | Specifies the frequency settling in time after lock (seconds). |
| Seconds After I/O | 2002 | Specifies the frequency settling in time after I/O (seconds). |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-if1-attenuation.html language=enus -->
## TOPIC 00082: Signal Path:Advanced:NI 5663:IF1 Attenuation (dB)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-if1-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-if1-attenuation.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF1 attenuation, in decibels. The device IF1 attenuator is set to this nominal value. Use this property, along with the IF2 Attenuation property, when you set the IF Filter property to Bypass. Valid Values: 0 to 15 Default Value: N/A Supported Devices: PXIe-5601 (external digitizer mod

### Signal Path:Advanced:NI 5663:IF1 Attenuation (dB)

Specifies the IF1 attenuation, in decibels. The device IF1 attenuator is set to this nominal value. Use this property, along with the [IF2 Attenuation](/csh?topicname=pnirfsa-if2-attenuation.html) property, when you set the [IF Filter](/csh?topicname=pnirfsa-iffilter.html) property to **Bypass**.

**Valid Values**: 0 to 15

**Default Value**: N/A

**Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IF1 Attenuation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-if2-attenuation.html language=enus -->
## TOPIC 00083: Signal Path:Advanced:NI 5663:IF2 Attenuation (dB)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-if2-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-if2-attenuation.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF2 attenuation, in decibels. The device IF2 attenuator is set to this nominal value. Use this property, along with the IF1 Attenuation property, when you set the IF Filter property to Bypass. Valid Values: 0 to 15 Default Value: N/A Supported Devices: PXIe-5601 (external digitizer mod

### Signal Path:Advanced:NI 5663:IF2 Attenuation (dB)

Specifies the IF2 attenuation, in decibels. The device IF2 attenuator is set to this nominal value. Use this property, along with the [IF1 Attenuation](/csh?topicname=pnirfsa-if1-attenuation.html) property, when you set the [IF Filter](/csh?topicname=pnirfsa-iffilter.html) property to **Bypass**.

**Valid Values**: 0 to 15

**Default Value**: N/A

**Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IF2 Attenuation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ifattentableselect-5603.html language=enus -->
## TOPIC 00084: Factory Calibration:NI 5665/5668R:IF Attenuation Table Selection

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ifattentableselect-5603.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ifattentableselect-5603.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF attenuation table to use for external calibration. This property is valid only in a calibration session. Default Value: Standard IF Attenuation Table Supported Devices: PXIe-5603/5605 Remarks The following table lists the characteristics of this property. Short Name IF Attenuation T

### Factory Calibration:NI 5665/5668R:IF Attenuation Table Selection

Specifies the IF attenuation table to use for external calibration. This property is valid only in a calibration session.

**Default Value**: Standard IF Attenuation Table

**Supported Devices**: PXIe-5603/5605

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IF Attenuation Table Selection |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Standard IF Attenuation Table | 2900 | Specifies that the standard IF attenuation table is used for the external calibration. |
| --- | --- | --- |
| ACPR IF Attenuation Table | 2901 | Specifies that the adjacent channel power ratio (ACPR) IF attenuation table is used for the external calibration. You can only select this value if you set the IF Filter Selection property to 5 MHz or 300 kHz. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ifattenuation.html language=enus -->
## TOPIC 00085: Signal Path:Advanced:NI 5663:IF Attenuation (dB)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ifattenuation.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ifattenuation.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device attenuation to a value that has the actual calibrated IF attenuation closest to the desired value. Valid Values: 0 to 30 Default Value: N/A Supported Devices: PXIe-5601/5603/5605 (external digitizer mode), PXIe-5663/5663E/5665/5667 Remarks The following table lists the characte

### Signal Path:Advanced:NI 5663:IF Attenuation (dB)

Configures the device attenuation to a value that has the actual calibrated IF attenuation closest to the desired value.

**Valid Values**: 0 to 30

**Default Value**: N/A

**Supported Devices**: PXIe-5601/5603/5605 (external digitizer mode), PXIe-5663/5663E/5665/5667

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IF Attenuation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ifattenuationtableindex.html language=enus -->
## TOPIC 00086: Factory Calibration:NI 5665/5668R:IF Attenuation Table Index

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ifattenuationtableindex.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ifattenuationtableindex.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF attenuation index from a table of valid settings. This property is valid only during a calibration session. PXIe-5603/5605/5606: To select a correct attenuation table, set this property in conjunction with the IF Filter Selection and IF Attenuation Table Selection properties. PXIe-5

### Factory Calibration:NI 5665/5668R:IF Attenuation Table Index

Specifies the IF attenuation index from a table of valid settings. This property is valid only during a calibration session.

**PXIe-5603/5605/5606**: To select a correct attenuation table, set this property in conjunction with the [IF Filter Selection](pnirfsa-iffilterselection.html) and [IF Attenuation Table Selection](pnirfsa-ifattentableselect-5603.html) properties.

**PXIe-5694**: To select correct attenuation settings, set this property in conjunction with the PXIe-5694 [IF Filter Selection](pnirfsa-iffilterselection.html) property.

**Valid Values**:

**PXIe-5603/5605/5606**: 0 to 57

**PXIe-5694**: 0 to 25

**Default Values**:

**PXIe-5603/5605/5606**: N/A

**PXIe-5694**: 0

**Supported Devices**: PXIe-5603/5605/5606, PXIe-5694

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IF Attenuation Table Index |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ifconditioningtemp.html language=enus -->
## TOPIC 00087: Device Characteristics:IF Conditioning Temperature (Degrees C)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ifconditioningtemp.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ifconditioningtemp.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current temperature, in degrees Celsius, of the IF conditioning module associated with the NI-RFSA device. Default Value: N/A Supported Devices: PXIe-5667 Remarks The following table lists the characteristics of this property. Short Name IF Conditioning Temperature Data type cdbl.png Per

### Device Characteristics:IF Conditioning Temperature (Degrees C)

Returns the current temperature, in degrees Celsius, of the IF conditioning module associated with the NI-RFSA device.

**Default Value**: N/A

**Supported Devices**: PXIe-5667

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IF Conditioning Temperature |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iffilter.html language=enus -->
## TOPIC 00088: Signal Path:Advanced:NI 5663:IF Filter

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iffilter.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iffilter.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the desired IF filter path, regardless of the RF band chosen by NI-RFSA. Default Value: N/A Supported Devices: PXIe-5601 Remarks The following table lists the characteristics of this property. Short Name IF Filter Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based N

### Signal Path:Advanced:NI 5663:IF Filter

Specifies the desired IF filter path, regardless of the RF band chosen by NI-RFSA.

**Default Value**: N/A

**Supported Devices**: PXIe-5601

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IF Filter |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| 187.5 MHz Wide | 1400 | The device uses the 187.5 MHz wide bandwidth filter. |
| --- | --- | --- |
| 187.5 MHz Narrow | 1401 | The device uses the 187.5 MHz narrow bandwidth filter. |
| 53 MHz | 1402 | The device uses the 53 MHz filter. |
| Bypass | 1403 | The device bypasses the IF filter. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iffilterselection.html language=enus -->
## TOPIC 00089: Factory Calibration:NI 5665/5668R:IF Filter Selection

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iffilterselection.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iffilterselection.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF filter path used during calibration. The property is valid only during a calibration session. Default Values: PXIe-5603/5605: Through PXIe-5606: 100 MHz PXIe-5694: 20 MHz Supported Devices: PXIe-5603/5605/5606, PXIe-5694 Remarks The following table lists the characteristics of this

### Factory Calibration:NI 5665/5668R:IF Filter Selection

Specifies the IF filter path used during calibration. The property is valid only during a calibration session.

**Default Values**:

**PXIe-5603/5605**: Through

**PXIe-5606**: 100 MHz

**PXIe-5694**: 20 MHz

**Supported Devices**: PXIe-5603/5605/5606, PXIe-5694

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IF Filter Selection |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| 5 MHz | 2100 | Specifies that the 5 MHz filter path is used during calibration. |
| --- | --- | --- |
| 300 kHz | 2101 | Specifies that the 300 kHz filter path is used during calibration. Not supported for the PXIe-5694. |
| Through | 2102 | None of the IF filter paths are used during calibration. Not supported for the PXIe-5606. |
| 20 MHz | 2103 | Specifies that the 20 MHz filter path is used during calibration. Not supported for the PXIe-5603/5605/5606. |
| 1.4 MHz | 2104 | Specifies that the 1.4 MHz filter path is used during calibration. Not supported for the PXIe-5603/5605/5606. |
| 400kHz | 2105 | Specifies that the 400 kHz filter path is used during calibration. Not supported for the PXIe-5603/5605/5606. |
| 110 kHz | 2106 | Specifies that the 110 kHz filter path is used during calibration. Not supported for the PXIe-5603/5605/5606. |
| 30 kHz | 2107 | Specifies that the 30 kHz filter path is used during calibration. Not supported for the PXIe-5603/5605/5606. |
| 100 MHz | 2108 | Specifies that the 100 MHz filter path is used during calibration. Not supported for the PXIe-5603/5605/5694. |
| 320 MHz | 2109 | Specifies that the 320 MHz filter path is used during calibration. Not supported for the PXIe-5603/5605/5694. |
| 765 MHz | 2110 | Specifies that the 765 MHz filter path is used during calibration. Not supported for the PXIe-5603/5605/5694. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-inputisolation.html language=enus -->
## TOPIC 00090: Signal Path:Advanced:Input Isolation Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-inputisolation.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-inputisolation.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether input isolation is enabled. Enabling this property isolates the input signal at the RF IN connector on the RF downconverter from the rest of the RF downconverter signal path. Disabling this property reintegrates the input signal into the RF downconverter signal path. If you enable

### Signal Path:Advanced:Input Isolation Enabled

Specifies whether input isolation is enabled.

Enabling this property isolates the input signal at the RF IN connector on the RF downconverter from the rest of the RF downconverter signal path. Disabling this property reintegrates the input signal into the
RF downconverter signal path.

Note

For the PXIe-5830/5831/5832, input isolation is supported for all available ports for your hardware configuration.

**Default Value**: Disabled

**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5693, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Input Isolation Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Disabled | 1900 | The property is disabled. |
| --- | --- | --- |
| Enabled | 1901 | The property is enabled. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-interchangecheck.html language=enus -->
## TOPIC 00091: Inherent IVI Attributes:User Options:Interchange Check

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-interchangecheck.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-interchangecheck.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to perform interchangeability checking and retrieve interchangeability warnings. Interchangeability check is unsupported. Default Value: FALSE Supported Devices: None TRUE NI-RFSA performs interchangeability-checking and retrieves warnings. FALSE NI-RFSA does not perform interchang

### Inherent IVI Attributes:User Options:Interchange Check

Specifies whether to perform interchangeability checking and retrieve interchangeability warnings.

Note

**Default Value**: FALSE

**Supported Devices**: None

| TRUE | NI-RFSA performs interchangeability-checking and retrieves warnings. |
| --- | --- |
| FALSE | NI-RFSA does not perform interchangeability-checking or retrieve warnings. This value is the default. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Interchange Check |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iq-allowmorerecords.html language=enus -->
## TOPIC 00092: Acquisition:IQ:Allow More Records Than Memory

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iq-allowmorerecords.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iq-allowmorerecords.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to allow the device to acquire more records than will fit in the device memory of the PXIe-5622/5624. If you set the property to FALSE and attempt to acquire more records than fit into the device memory of the PXIe-5622/5624, NI-RFSA returns an error. If this property is set to TRU

### Acquisition:IQ:Allow More Records Than Memory

Specifies whether to allow the device to acquire more records than will fit in the device memory of the PXIe-5622/5624.

Note

Note

TRUE

**Default Value**: FALSE

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

| TRUE | Allows acquisition of more records than fit in device memory. |
| --- | --- |
| FALSE | Does not allow acquisitions of more records than fit in device memory. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Allow More Records Than Memory |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iq-numrecords.html language=enus -->
## TOPIC 00093: Acquisition:IQ:Number Of Records

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iq-numrecords.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iq-numrecords.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of records to acquire if the Number of Records Is Finite property is set to TRUE. Default Value: 1 Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Related Topics I/Q Modulation Remarks The following t

### Acquisition:IQ:Number Of Records

Specifies the number of records to acquire if the [Number of Records Is Finite](/csh?topicname=pnirfsa-iq-numrecordsisfinite.html) property is set to TRUE.

**Default Value**: 1

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[I/Q Modulation](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=iq-modulation)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Records |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSA Configure Number of Records |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iq-numsampsisfinite.html language=enus -->
## TOPIC 00094: Acquisition:IQ:Number Of Samples Is Finite

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iq-numsampsisfinite.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iq-numsampsisfinite.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device acquires a finite number of samples or acquires continuously. Default Value: TRUE Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 TRUE Acquire a finite number of samples. FALSE Acquire samples

### Acquisition:IQ:Number Of Samples Is Finite

Specifies whether the device acquires a finite number of samples or acquires continuously.

**Default Value**: TRUE

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

| TRUE | Acquire a finite number of samples. |
| --- | --- |
| FALSE | Acquire samples continuously until you abort the acquisition. |

**Related Topics**

[I/Q Modulation](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=iq-modulation)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Samples Is Finite |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSA Configure Number of Samples |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iqcarrierfrequency.html language=enus -->
## TOPIC 00095: Acquisition:IQ:IQ Carrier Frequency

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iqcarrierfrequency.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iqcarrierfrequency.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the expected carrier frequency of the incoming signal for demodulation, in Hz. The NI-RFSA device tunes to this frequency. NI-RFSA may coerce this value based on hardware settings and the RF downconverter specifications. For the PXIe-5645, this property is ignored if you are using the I/Q

### Acquisition:IQ:IQ Carrier Frequency

Specifies the expected carrier frequency of the incoming signal for demodulation, in Hz. The NI-RFSA device tunes to this frequency. NI-RFSA may coerce this value based on hardware settings and the RF downconverter specifications.

Note

**Default Values**:

**PXIe-5644/5645/5646, PXIe-5840/5841/5860, PXIe-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options)**: 1 GHz

**PXIe-5842 (4 GHz bandwidth option) using the Standard personality**: 1 GHz

**PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality**: 6.5 GHz

**PXIe-5820**: 0 Hz

**PXIe-5830/5831/5832**: 6.5 GHz

**All other devices**: 100 MHz

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Carrier Wave](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=fund-carrierwave)

[I/Q Modulation](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=iq-modulation)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Carrier Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSA Configure IQ Carrier Frequency |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iqinporttemperature.html language=enus -->
## TOPIC 00096: Device Specific:Vector Signal Transceiver:IQ In Port:Temperature (Degrees C)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iqinporttemperature.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iqinporttemperature.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature, in degrees Celsius, of the I/Q IN circuitry on the device. Supported Devices: PXIe-5645, PXIe-5820 Remarks The following table lists the characteristics of this property. Short Name IQ In Port Temperature Data type cdbl.png Permissions Read Only High-level VIs N/A Channel-ba

### Device Specific:Vector Signal Transceiver:IQ In Port:Temperature (Degrees C)

Returns the temperature, in degrees Celsius, of the I/Q IN circuitry on the device.

**Supported Devices**: PXIe-5645, PXIe-5820

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ In Port Temperature |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iqinportterminalconfiguration.html language=enus -->
## TOPIC 00097: Device Specific:Vector Signal Transceiver:IQ In Port:Terminal Configuration

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iqinportterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-iqinportterminalconfiguration.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the terminal configuration of the I/Q IN port. To use this property, you must use the Active Channel property to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string

### Device Specific:Vector Signal Transceiver:IQ In Port:Terminal Configuration

Configures the terminal configuration of the I/Q IN port.

To use this property, you must use the [Active Channel](pnirfsa-activechannel.html) property to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

Note

**PXIe-5820**—The only valid value for this property is differential.

**Default Value**: differential

**Supported Devices**: PXIe-5645, PXIe-5820

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ In Port Term Cfg |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Differential | 2100 | Sets the terminal configuration to differential. |
| --- | --- | --- |
| Single-Ended | 2101 | Sets the terminal configuration to single-ended. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-lo3attenuation-5603.html language=enus -->
## TOPIC 00098: Factory Calibration:NI 5665/5668R:LO3 Attenuation

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-lo3attenuation-5603.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-lo3attenuation-5603.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LO3 attenuation, in decibels, during a calibration session. This property is valid only during a calibration session. Valid and Default Values: Device Valid Values Default Value PXIe-5603/5605 0 to 15.5 15.5 PXIe-5606 0 to 31 31 Supported Devices: PXIe-5603/5605/5606 Remarks The follow

### Factory Calibration:NI 5665/5668R:LO3 Attenuation

Specifies the LO3 attenuation, in decibels, during a calibration session. This property is valid only during a calibration session.

**Valid and Default Values**:

| Device | Valid Values | Default Value |
| --- | --- | --- |
| PXIe-5603/5605 | 0 to 15.5 | 15.5 |
| PXIe-5606 | 0 to 31 | 31 |

**Supported Devices**: PXIe-5603/5605/5606

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO3 Attenuation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-loexportenabled.html language=enus -->
## TOPIC 00099: Signal Path:LO Export Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-loexportenabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-loexportenabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the LO OUT terminals on the installed devices. PXIe-5601—The only valid value for this property is TRUE. PXIe-5603/5605/5606—If you want to daisy-chain multiple devices together using the same LO source, set this property to TRUE to export the LO input signals on the LO1

### Signal Path:LO Export Enabled

Specifies whether to enable the LO OUT terminals on the installed devices.

**PXIe-5601**—The only valid value for this property is **TRUE**.

**PXIe-5603/5605/5606**—If you want to daisy-chain multiple devices together using the same LO source, set this property to TRUE to export the LO input signals on the LO1 IN, LO2 IN, and LO3 IN terminals to LO1 OUT, LO2 OUT, and LO3 OUT, respectively.

**PXIe-5694**—You can enable this property only if you set the [LO Source](pnirfsa-losource.html) property to **LO In** or if you set the LO Source property to **Onboard** and the [IF Conditioning Downconversion Enabled](pnirfsa-downconversionenabled.html) property to **Enabled**.

**PXIe-5830/5831, PXIe-5842 VST with 54 GHz Frequency Extension**—To use this property for the PXIe-5830/5831/5832 or PXIe-5842 VST with 54 GHz Frequency Extension, you must first use the [Active Channel](pnirfsa-activechannel.html) property to specify the name of the channel you are configuring. You can configure LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

Note

Note

Note

**Default Values**:

**PXIe-5601, PXIe-5663/5663E**—TRUE

**PXIe-5603/5605/5606, PXIe-5644/5645/5646, PXIe-5665/5667/5668, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842**—FALSE

**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842

| TRUE | Enables the LO OUT terminals. |
| --- | --- |
| FALSE | Disables the LO OUT terminals. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Export Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-losource.html language=enus -->
## TOPIC 00100: Signal Path:LO Source

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-losource.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-losource.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LO signal source used to downconvert the RF input signal. If this property is set to "" (empty string), NI-RFSA uses the internal LO source. To use this property for the PXIe-5830/5831/5832 and PXIe-5842 VST with 54 GHz Frequency Extension, you must first use the Active Channel propert

### Signal Path:LO Source

Specifies the LO signal source used to downconvert the RF input signal. If this property is set to "" (empty string), NI-RFSA uses the internal LO source.

To use this property for the PXIe-5830/5831/5832 and PXIe-5842 VST with 54 GHz Frequency Extension, you must first use the [Active Channel](pnirfsa-activechannel.html) property to specify the name of the channel you are configuring. You can configure LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

Note

SG SA Shared

Note

If no signal downconversion is required, this property is ignored.

**Default Value**: Onboard

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842

**Related Topics**

[PXIe-5830 LO Sharing Using NI-RFSA and NI-RFSG](https://ni.com/docs/en-US/csh?pubname=pxie-5830-feature&topicname=lo-sharing-using-rfsa-rfsg)

[PXIe-5831/5832 LO Sharing Using NI-RFSA and NI-RFSG](https://ni.com/docs/en-US/csh?pubname=pxie-5831&topicname=lo-sharing-using-rfsa-rfsg)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| None | None | Specifies that no LO source is required to downconvert the RF input signal. |
| --- | --- | --- |
| Onboard | Onboard | Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal. PXIe-5831—This configuration uses the onboard LO of the PXIe-3622, using the LO2 stage. PXIe-5832—This configuration uses the onboard LO of the PXIe-3623, using the LO2 stage. PXIe-5831 with PXIe-5653—This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3622. PXIe-5832 with PXIe-5653—This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3623. PXIe-5841 with PXIe-5655—This configuration uses the onboard LO of the PXIe-5655. PXIe-5842—This configuration uses the onboard LO of the PXIe-5655. |
| LO In | LO_In | Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel. |
| Secondary | Secondary | Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid on only the PXIe-5831/5832 with PXIe-5653 (LO1 stage only). |
| SG SA Shared | SG_SA_Shared | Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSA selects an internal synthesizer and the synthesizer signal is switched to both the RF Out and RF In mixers. This value is valid on only the PXIe-5830/5831/5832/5841 with PXIe-5655, PXIe-5842. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-mechanicalattenuation.html language=enus -->
## TOPIC 00101: Vertical:Advanced:Mechanical Attenuation (dB)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-mechanicalattenuation.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-mechanicalattenuation.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the level of mechanical attenuation for the RF path, in decibels. PXIe-5667— This property is read-only when the Low Frequency Bypass Enabled property is set to Disabled. PXIe-5668 with PXIe-5698— This property is read-only when the Preamp Enabled property is set to Enabled. Valid Values:

### Vertical:Advanced:Mechanical Attenuation (dB)

Specifies the level of mechanical attenuation for the RF path, in decibels.

**PXIe-5667**— This property is read-only when the [Low Frequency Bypass Enabled](pnirfsa-lowfrequencybypassenabled.html) property is set to **Disabled**.

**PXIe-5668 with PXIe-5698**— This property is read-only when the [Preamp Enabled](pnirfsa-preampenabled.html) property is set to **Enabled**.

**Valid Values**:

**PXIe-5601/5663/5663E**—0, 16

**PXIe-5603/5665 (3.6 GHz)**—0, 10, 20, 30

**PXIe-5605/5665 (14 GHz), PXIe-5606/5668**—0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75

**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low frequency bypass path**—0, 10, 20, 30

**PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**—0

**PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector low frequency bypass path**—0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75

**PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector filter path**—0

**PXIe-5668 with PXIe-5698 with the Preamp Enabled property set to Enabled**—5

**Default Value**: N/A

**Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mechanical Attenuation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-mechanicalattenuationenabled.html language=enus -->
## TOPIC 00102: Vertical:Advanced:NI 5663:Mechanical Attenuator Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-mechanicalattenuationenabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-mechanicalattenuationenabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the mechanical attenuator is enabled. Set this property to Enabled to allow NI-RFSA to use the mechanical attenuator. Disabling this attenuator can improve device performance. Refer to PXIe-5663/5663E RF Attenuation and Signal Levels for more information about the attenuators. Defa

### Vertical:Advanced:NI 5663:Mechanical Attenuator Enabled

Specifies whether the mechanical attenuator is enabled. Set this property to **Enabled** to allow NI-RFSA to use the mechanical attenuator.

Disabling this attenuator can improve device performance. Refer to [PXIe-5663/5663E RF Attenuation and Signal Levels](https://ni.com/docs/en-US/csh?pubname=pxie-5663-5663e-feature&topicname=programming-attenuation) for more information about the attenuators.

**Default Value**: Enabled

**Supported Devices**: PXIe-5601 (external digitizer mode), PXIe-5663/5663E

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mechanical Attenuator Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Disabled | 1900 | The property is disabled. |
| --- | --- | --- |
| Enabled | 1901 | The property is enabled. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-memorysize.html language=enus -->
## TOPIC 00103: Device Characteristics:Memory Size

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-memorysize.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-memorysize.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the digitizer onboard memory size, in bytes. Default Value: N/A Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Remarks The following table lists the characteristics of this property. Short Name Memory Size Data t

### Device Characteristics:Memory Size

Returns the digitizer onboard memory size, in bytes.

**Default Value**: N/A

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Memory Size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-minreconfigtime.html language=enus -->
## TOPIC 00104: Configuration List:Advanced:Minimum Reconfiguration Time

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-minreconfigtime.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-minreconfigtime.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property is not for customer use. Remarks The following table lists the characteristics of this property. Short Name Minimum Reconfiguration Time Data type cdbl.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes

### Configuration List:Advanced:Minimum Reconfiguration Time

This property is not for customer use.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Minimum Reconfiguration Time |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-mixerlevel.html language=enus -->
## TOPIC 00105: Vertical:Mixer Level (dBm)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-mixerlevel.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-mixerlevel.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mixer level, in dBm. The mixer level represents the attenuation value to apply to the input RF signal as it reaches the first mixer in the signal chain. If you do not set this property, NI-RFSA automatically selects an optimal mixer level value based on the reference level. The valid v

### Vertical:Mixer Level (dBm)

Specifies the mixer level, in dBm. The mixer level represents the attenuation value to apply to the input RF signal as it reaches the first mixer in the signal chain. If you do not set this property, NI-RFSA automatically selects an optimal mixer level value based on the reference level. The valid values for this property depend on your device configuration.

If you set the Mixer Level and [Mixer Level Offset](pnirfsa-mixerleveloffset.html) properties at the same time, NI-RFSA returns an error.

**PXIe-5601/5663/5663E**—This property is read-only.

**PXIe-5667**—This property is read-only when the [Low Frequency Bypass Enabled](pnirfsa-lowfrequencybypassenabled.html) property is set to **Disabled**.

**Default Values**:

**PXI-5600/5661**: –30

**PXIe-5603/5605/5665/5667/5668**: –10

**All other devices**: N/A

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mixer Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-mixerleveloffset.html language=enus -->
## TOPIC 00106: Vertical:Mixer Level Offset (dB)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-mixerleveloffset.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-mixerleveloffset.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of decibels by which to adjust the device mixer level. The default value is 0, which specifies device settings that are the best compromise between distortion and noise. Specifying a positive value for this property configures the device for moderate distortion and low noise, an

### Vertical:Mixer Level Offset (dB)

Specifies the number of decibels by which to adjust the device mixer level. The default value is 0, which specifies device settings that are the best compromise between distortion and noise. Specifying a positive value for this property configures the device for moderate distortion and low noise, and specifying a negative value results in low distortion and higher noise.

You cannot set the Mixer Level Offset and [Mixer Level](pnirfsa-mixerlevel.html) properties at the same time.

**PXIe-5667**—This property is read-only when the [Low Frequency Bypass Enabled](pnirfsa-lowfrequencybypassenabled.html) property is set to **Disabled**.

**Default Value**: 0

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mixer Level Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-model.html language=enus -->
## TOPIC 00107: Inherent IVI Attributes:Instrument Identification:Model

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-model.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-model.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the model number or name of the NI-RFSA device that you are currently using. Default Value: N/A Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-582

### Inherent IVI Attributes:Instrument Identification:Model

Returns a string that contains the model number or name of the NI-RFSA device that you are currently using.

**Default Value**: N/A

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Model |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-notchfilterenabled.html language=enus -->
## TOPIC 00108: Signal Path:Advanced:Notch Filter Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-notchfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-notchfilterenabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the notch filter is enabled on the RF conditioning module. The PXI-5661, and PXIe-5663/5663E/5665 only support setting this property to Disabled. Default Value: Disabled Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5693 Remarks The following table lists the characte

### Signal Path:Advanced:Notch Filter Enabled

Specifies whether the notch filter is enabled on the RF conditioning module.

Note

Disabled

**Default Value**: Disabled

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5693

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Notch Filter Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Disabled | 3400 | Disables the notch filter. |
| --- | --- | --- |
| Enabled when in Signal Path | 3401 | The notch filter is automatically enabled when it is in the signal path and automatically disabled when it is not in the signal path. |
| Enabled | 3402 | Enables the notch filter. If the notch filter is not in the signal path or if the notch filter is not supported on the device, NI-RFSA returns an error. Select Enable when in Signal Path whenever possible to avoid an error. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ospdatascalingfactor.html language=enus -->
## TOPIC 00109: Vertical:Advanced:OSP Data Scaling Factor

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ospdatascalingfactor.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ospdatascalingfactor.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the scaling factor applied to the time-domain voltage data in the IF digitizer. Use this property to maximize the dynamic range of the digitizer by increasing the maximum IF power the digitizer can measure without creating OSP overflows. Because of the device amplitude response, some wide-

### Vertical:Advanced:OSP Data Scaling Factor

Specifies the scaling factor applied to the time-domain voltage data in the IF digitizer. Use this property to maximize the dynamic range of the digitizer by increasing the maximum IF power the digitizer can measure without creating OSP overflows.

Because of the device amplitude response, some wide-band signals normally attenuated by the downconverter go through the IF digitizer without causing an ADC overflow. During IF equalization, these wide-band digitizer input signals may become amplified. These amplified input signal values overflow the available numeric range used in the signal processing algorithm.

You can use this property when OSP calculations would generate an overflow while applying digital filters to the data. The OSP module in the digitizer multiplies the time-domain signal amplitude, in volts, by the specified property value before further onboard processing. Set this property to a value less than 1 to avoid OSP overflow for near full-scale IF signals and to use the maximum dynamic range of the digitizer. NI-RFSA compensates for the specified OSP data scaling factor to ensure that the correct scaled data, in absolute levels, is always returned regardless of the value of this property.

**Valid Values:** 0.25 to 1.0

**Default Values:**

**PXI-5661, PXIe-5663/5663E/5665 (3.6 GHz)/5667 (3.6 GHz)/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: 1.0

**PXIe-5665 (14 GHz)/5667 (7 GHz)**: 0.8

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OSP Data Scaling Factor |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-overflowerrorreporting.html language=enus -->
## TOPIC 00110: Vertical:Advanced:Overflow Error Reporting

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-overflowerrorreporting.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-overflowerrorreporting.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures error reporting for ADC and onboard signal processing overflows. Overflows lead to clipping of the waveform. Default Value: Warning Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Remarks The following table lists the characteristics of this property.

### Vertical:Advanced:Overflow Error Reporting

Configures error reporting for ADC and onboard signal processing overflows. Overflows lead to clipping of the waveform.

**Default Value**: Warning

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Overflow Error Reporting |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Warning | 1301 | NI-RFSA returns a warning when an ADC or onboard signal processing (OSP) overflow occurs. |
| --- | --- | --- |
| Disabled | 1302 | NI-RFSA does not return an error or a warning when an ADC or OSP overflow occurs. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2penabled.html language=enus -->
## TOPIC 00111: Peer-to-Peer:Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2penabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2penabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether peer-to-peer streaming is enabled for the active stream endpoint. This property is endpoint-based. Default Value: FALSE Supported Devices: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 TRUE Enables streaming. FALSE Disables streaming. Remarks The following

### Peer-to-Peer:Enabled

Specifies whether peer-to-peer streaming is enabled for the active stream endpoint.

This property is [endpoint-based](https://ni.com/docs/en-US/csh?pubname=pxie-5842&topicname=configuring-peer-to-peer-endpoint).

**Default Value**: FALSE

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| TRUE | Enables streaming. |
| --- | --- |
| FALSE | Disables streaming. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | P2P Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2pendpointoverflow.html language=enus -->
## TOPIC 00112: Peer-to-Peer:Endpoint Overflow

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2pendpointoverflow.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2pendpointoverflow.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the endpoint has overflowed. An overflow condition occurs when data is written to the endpoint faster than it can be streamed from it. During an overflow, data in the endpoint begins to be overwritten. Reset the device or close the session to reset the overflow condition. Default V

### Peer-to-Peer:Endpoint Overflow

Indicates whether the endpoint has overflowed. An overflow condition occurs when data is written to the endpoint faster than it can be streamed from it. During an overflow, data in the endpoint begins to be overwritten. Reset the device or close the session to reset the overflow condition.

**Default Value**: FALSE

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| TRUE | The endpoint has overflowed. |
| --- | --- |
| FALSE | You can write additional data to the endpoint. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | P2P Endpoint Overflow |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2pendpointsize.html language=enus -->
## TOPIC 00113: Peer-to-Peer:Endpoint Size

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2pendpointsize.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2pendpointsize.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size, in samples, of the peer-to-peer endpoint. Default Value: 0 Supported Devices: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Remarks The following table lists the characteristics of this property. Short Name P2P Endpoint Size Data type ci64.png Permissions

### Peer-to-Peer:Endpoint Size

Returns the size, in samples, of the peer-to-peer endpoint.

**Default Value**: 0

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | P2P Endpoint Size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2pfifoendpointcount.html language=enus -->
## TOPIC 00114: Peer-to-Peer:FIFO Endpoint Count

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2pfifoendpointcount.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2pfifoendpointcount.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of peer-to-peer streams supported by the device. Default Value: 0 Supported Devices: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Remarks The following table lists the characteristics of this property. Short Name P2P FIFO Endpoint Count Data type ci64.pn

### Peer-to-Peer:FIFO Endpoint Count

Returns the number of peer-to-peer streams supported by the device.

**Default Value**: 0

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | P2P FIFO Endpoint Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2ponboardmemoryenabled.html language=enus -->
## TOPIC 00115: Peer-to-Peer:Onboard Memory Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2ponboardmemoryenabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2ponboardmemoryenabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether a limit is placed on the number of records and the size of the records by the size of the device onboard memory. When a peer-to-peer stream is enabled and onboard memory is disabled, any fetch calls result in an error. Default Value: FALSE Supported Devices: PXIe-5663/5663E/5665/56

### Peer-to-Peer:Onboard Memory Enabled

Specifies whether a limit is placed on the number of records and the size of the records by the size of the device onboard memory. When a peer-to-peer stream is enabled and onboard memory is disabled, any fetch calls result in an error.

**Default Value**: FALSE

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | P2P Onboard Memory Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2psamplestransferred.html language=enus -->
## TOPIC 00116: Peer-to-Peer:Samples Transferred

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2psamplestransferred.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-p2psamplestransferred.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of complex samples transferred through the peer-to-peer stream endpoint since the endpoint was last reset. Default Value: 0 Supported Devices: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Remarks The following table lists the characteristics of this property.

### Peer-to-Peer:Samples Transferred

Returns the number of complex samples transferred through the peer-to-peer stream endpoint since the endpoint was last reset.

**Default Value**: 0

**Supported Devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | P2P Samples Transferred |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-phaseoffset.html language=enus -->
## TOPIC 00117: Acquisition:IQ:Phase Offset

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-phaseoffset.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-phaseoffset.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset to apply to the initial I and Q phases. Valid Values: –180 to 180 Default Value: 0 Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 Remarks The following table lists the characteristics of this property. Sh

### Acquisition:IQ:Phase Offset

Specifies the offset to apply to the initial I and Q phases.

**Valid Values**: –180 to 180

**Default Value**: 0

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Phase Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-preampenabled.html language=enus -->
## TOPIC 00118: Vertical:Advanced:Preamp Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-preampenabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-preampenabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RF preamplifier is enabled in the system. PXIe-5667, PXIe-5644/5645/5646, PXIe-5830/5831/5840/5841/5842—Automatic enables the RF preamplifier based on the value of the Reference Level property and the center frequency. Except on the PXIe-5830/5831/5832, NI-RFSA coerces this pro

### Vertical:Advanced:Preamp Enabled

Specifies whether the RF preamplifier is enabled in the system.

**PXIe-5667, PXIe-5644/5645/5646, PXIe-5830/5831/5840/5841/5842**—**Automatic** enables the RF preamplifier based on the value of the [Reference Level](pnirfsa-referencelevel.html) property and the center frequency. Except on the PXIe-5830/5831/5832, NI-RFSA coerces this property from **Automatic** to the selected value.

Note

Enabled

Disabled

**PXIe-5667**—**Automatic** is supported only when the [Low Frequency Bypass Enabled](pnirfsa-lowfrequencybypassenabled.html) property is set to **Enabled**. If the reference level is greater than -25 dBm, NI-RFSA disables the preamplifier. If the reference level is less than or equal to -25 dBm, NI-RFSA sets the Preamp Enabled property to **Enabled when in Signal Path**.

**PXIe-5668 with PXIe-5698**—If you set this property to **Enabled**, only the preamplifier on PXIe-5698 is used, and the preamplifier on PXIe-5668 remains disabled.

**Default Value**:

**PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842**: Automatic

**All other devices**: Disabled

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5698, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Preamp Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Disabled | 2500 | Disables the RF preamplifier. |
| --- | --- | --- |
| Enabled when in Signal Path | 2501 | Enables the RF preamplifier when it is in the signal path and disables it when it is not in the signal path. Only devices with an RF preamplifier on the downconverter and an RF preselector support this option. Use the RF Preamp Present property to determine whether the downconverter has a preamplifier. |
| Enabled | 2502 | Enables the RF preamplifier. If the RF preamplifier is not in a signal path, NI-RFSA returns an error. Select the Enabled when in Signal Path option whenever possible to avoid an error. |
| Automatic | 2503 | Automatically enables the RF preamplifier based on the value of the Reference Level property. This value is valid only for the PXIe-5644/5645/5646, PXIe-5667, and PXIe-5830/5831/5832/5840/5841/5842/5860. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-preselectorenabled.html language=enus -->
## TOPIC 00119: Signal Path:Advanced:Downconverter Preselector Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-preselectorenabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-preselectorenabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the tunable preselector is enabled on the downconverter. All devices support setting this property to Disabled or Enabled when in Signal Path. Only devices with a preselector on the downconverter support setting this property to Enabled. Default Value: Disabled if the device has no

### Signal Path:Advanced:Downconverter Preselector Enabled

Specifies whether the tunable preselector is enabled on the downconverter.

Note

Disabled

Enabled when in Signal Path

Enabled

**Default Value**: Disabled if the device has no preselector, Enabled when in Signal Path if the device has a preselector.

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Preselector Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Disabled | 2600 | Disables the preselector. |
| --- | --- | --- |
| Enabled when in Signal Path | 2601 | The preselector is automatically enabled when it is in the signal path and is automatically disabled when it is not in the signal path. Use the Preselector Present property to determine if the downconverter has a preselector. |
| Enabled | 2602 | Enables the preselector. If the preselector is not in the signal path or if the preselector is not supported on the device, NI-RFSA returns an error. Select the Enabled when in Signal Path whenever possible to avoid an error. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-preselectorpresent.html language=enus -->
## TOPIC 00120: Device Characteristics:Preselector Present

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-preselectorpresent.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-preselectorpresent.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether a preselector is available on the RF downconverter module. Default Value: N/A Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 TRUE A preselector is

### Device Characteristics:Preselector Present

Returns whether a preselector is available on the RF downconverter module.

**Default Value**: N/A

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| TRUE | A preselector is available on the downconverter. |
| --- | --- |
| FALSE | No preselector is available on the downconverter. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Preselector Present |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-rdyforstartevent-outputterm.html language=enus -->
## TOPIC 00121: Events:Ready For Start:Output Terminal

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-rdyforstartevent-outputterm.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-rdyforstartevent-outputterm.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Ready for Start Event. Default Value: "" (empty string) Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Remarks The following table lists the characteristics of this property. Sh

### Events:Ready For Start:Output Terminal

Specifies the destination terminal for the Ready for Start Event.

**Default Value**: "" (empty string)

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Start Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Do not export signal |  | The signal is not exported. |
| --- | --- | --- |
| ClkOut | ClkOut | The signal is exported to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut | RefOut | The signal is exported to the REF IN/OUT terminal on the PXI/PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut2 | RefOut2 | The signal is exported to the REF OUT2 terminal on the LO. This connector exists on only the PXIe-5652. |
| PFI0 | PFI0 | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| PFI1 | PFI1 | The signal is exported to the PFI 1 connector on the PXIe-5142 and PXIe-5622. |
| PXI_Trig0 | PXI_Trig0 | The signal is exported to the PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | The signal is exported to the PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | The signal is exported to the PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | The signal is exported to the PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | The signal is exported to the PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | The signal is exported to the PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | The signal is exported to the PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | The signal is exported to the PXI trigger line 7. |
| PXI_STAR | PXI_STAR | The signal is exported to the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. |
| PXIe_DStarC | PXIe_DStarC | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| DIO/PFI0 | DIO/PFI0 | The signal is exported to the PFI 0 on the DIO front panel connector |
| DIO/PFI1 | DIO/PFI1 | The signal is exported to the PFI 1 on the DIO front panel connector |
| DIO/PFI2 | DIO/PFI2 | The signal is exported to the PFI 2 on the DIO front panel connector |
| DIO/PFI3 | DIO/PFI3 | The signal is exported to the PFI 3 on the DIO front panel connector |
| DIO/PFI4 | DIO/PFI4 | The signal is exported to the PFI 4 on the DIO front panel connector |
| DIO/PFI5 | DIO/PFI5 | The signal is exported to the PFI 5 on the DIO front panel connector |
| DIO/PFI6 | DIO/PFI6 | The signal is exported to the PFI 6 on the DIO front panel connector |
| DIO/PFI7 | DIO/PFI7 | The signal is exported to the PFI 7 on the DIO front panel connector |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-readyforadvanceeventterminalname.html language=enus -->
## TOPIC 00122: Events:Ready For Advance:Terminal Name

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-readyforadvanceeventterminalname.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-readyforadvanceeventterminalname.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. Default Values: PXIe-5830/5831/5832: /BasebandModule/ai/0/ReadyForAdvanceEvent, where BasebandModule is the name of the baseband module for your device in MAX. PXIe-5820/5840/5841/5842: /ModuleName/ai/0/ReadyForAdvanceEvent, where ModuleName is th

### Events:Ready For Advance:Terminal Name

Returns the fully qualified signal name as a string.

**Default Values**:

**PXIe-5830/5831/5832**: /*BasebandModule*/ai/0/ReadyForAdvanceEvent, where *BasebandModule* is the name of the baseband module for your device in MAX.

**PXIe-5820/5840/5841/5842**: /*ModuleName*/ai/0/ReadyForAdvanceEvent, where *ModuleName* is the name of your device in MAX.

**PXIe-5860**: /*ModuleName*/ai/*ChannelNumber*/ReadyForAdvanceEvent, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

**All other devices**: /*DigitizerName*/ReadyForAdvanceEvent, where *DigitizerName* is the name of your associated digitizer module in MAX.

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Events](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=events)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Advance Event Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niRFSA Get Terminal Name |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-recordsdone.html language=enus -->
## TOPIC 00123: Acquisition:Fetch:Records Done

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-recordsdone.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-recordsdone.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of records the RF vector signal analyzer has acquired. Default Value: N/A Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Remarks The following table lists the characteristics of this property. Short Na

### Acquisition:Fetch:Records Done

Returns the number of records the RF vector signal analyzer has acquired.

**Default Value**: N/A

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Records Done |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-recordvaluecoercions.html language=enus -->
## TOPIC 00124: Inherent IVI Attributes:User Options:Record Value Coercions

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-recordvaluecoercions.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-recordvaluecoercions.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties. This property is currently not supported. Default Value: FALSE Supported Devices: None TRUE The IVI engine keeps a list of the value coercions. FALSE The IVI engine does not keep a lis

### Inherent IVI Attributes:User Options:Record Value Coercions

Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties.

Note

**Default Value**: FALSE

**Supported Devices**: None

| TRUE | The IVI engine keeps a list of the value coercions. |
| --- | --- |
| FALSE | The IVI engine does not keep a list of the value coercions. This value is the default. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Record Value Coercions |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ref-trigger-osp-delay.html language=enus -->
## TOPIC 00125: Triggers:Ref:Advanced:OSP Delay Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ref-trigger-osp-delay.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-ref-trigger-osp-delay.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block. If you set this property to Disabled, the Reference Triggers bypass the OSP block and are processed immediately. Enabling this property requires the following e

### Triggers:Ref:Advanced:OSP Delay Enabled

Specifies whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block. If you set this property to **Disabled**, the Reference Triggers bypass the OSP block and are processed immediately.

Enabling this property requires the following equipment configurations:

- All digitizers being used must be the same model and hardware revision.
- All digitizers must use the same firmware.
- All digitizers must be configured with the same I/Q rate.
- All devices must use the same signal path.

**PXIe-5663/5663E**—Read the value of the [IF Filter](pnirfsa-iffilter.html) property to determine the IF filters used by the PXIe-5663/5663E.

**PXIe-5665/5667/5668**—Refer to the device-specific information in the [Device Instantaneous Bandwidth](pnirfsa-deviceinstantaneousbandwidth.html) property to determine the IF filters used by the PXIe-5665/5667/5668. If you set the [FFT Width](pnirfsa-fftwidth.html) property, refer to the device-specific information for this property and the Device Instantaneous Bandwidth property to determine the IF filters used. For frequencies less than 3.6 GHz, set the [Preamp Enabled](pnirfsa-preampenabled.html) property to the same value for all devices.

**PXIe-5665 14 GHz**—Set the [Downconverter Preselector Enabled](pnirfsa-preselectorenabled.html) property to the same value for all devices.

If the I/Q rate is set programmatically for I/Q acquisitions, the following properties should be identical for the best device synchronization:

- Digital IF Equalization Enabled
- OSP Sampling Ratio

For spectrum acquisitions, the following properties should be identical for the best device synchronization:

- Span
- Resolution Bandwidth
- Digital IF
- OSP Sampling Ratio

For more information about the digitizer OSP block and Reference Triggers, refer to the following topics in the *NI High-Speed Digitizers Help*:

- NI-5622 Onboard Signal Processing (OSP)
- NI-5142 Onboard Signal Processing (OSP)
- NI PXIe-5622 Trigger Sources
- NI PXI-5142 Trigger Sources
- NI PXIe-5622 Block Diagram
- NI PXI-5142 Block Diagram

**Default Value**: Enabled

**Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference Trigger OSP Delay Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Disabled | 1900 | The property is disabled. |
| --- | --- | --- |
| Enabled | 1901 | The property is enabled. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-refclkexportedterm.html language=enus -->
## TOPIC 00126: Clocking:Ref Clock Exported Terminal

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-refclkexportedterm.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-refclkexportedterm.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a comma-separated list of the terminals at which to export the Reference Clock. Default Value: "" (empty string) Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Related Topics Triggers Events Signal R

### Clocking:Ref Clock Exported Terminal

Specifies a comma-separated list of the terminals at which to export the Reference Clock.

**Default Value**: "" (empty string)

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

[Events](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=events)

[Signal Routing](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=signal-routing)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref Clock Exported Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSA Export Signal |
| Channel-based | No |
| Resettable | Yes |

| None | None | The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646. |
| --- | --- | --- |
| RefOut | RefOut | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut2 | RefOut2 | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. |
| ClkOut | ClkOut | Export the Reference Clock on the CLK OUT terminal on the Digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| IFCondRefOut | IFCondRefOut | Export the clock on the REF OUT terminal on the PXIe-5694. This value is valid only for the PXIe-5667. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-refclockexportedrate.html language=enus -->
## TOPIC 00127: Clocking:Ref Clock Exported Rate:Ref Clock Exported Rate

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-refclockexportedrate.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-refclockexportedrate.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Reference Clock Rate, in Hz, of the signal sent to the Ref Clock Exported Terminal. Default Value: 10 MHz Valid Values: PXIe-5820/5830/5831/5832/5840/5841: 10 MHz PXIe-5842: 10 MHz, 100 MHz, 1 GHz PXIe-5860: 10 MHz, 100 MHz Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/586

### Clocking:Ref Clock Exported Rate:Ref Clock Exported Rate

Specifies the Reference Clock Rate, in Hz, of the signal sent to the [Ref Clock Exported Terminal](/csh?topicname=pnirfsa-refclkexportedterm.html).

**Default Value**: 10 MHz

**Valid Values**:

PXIe-5820/5830/5831/5832/5840/5841: 10 MHz

PXIe-5842: 10 MHz, 100 MHz, 1 GHz

PXIe-5860: 10 MHz, 100 MHz

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref Clock Exported Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| 10MHz | 10000000 | Exports a 10 MHz Reference Clock. |
| --- | --- | --- |
| 100MHz | 100000000 | Exports a 100 MHz Reference Clock. |
| 1GHz | 1000000000 | Exports a 1 GHz Reference Clock. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-refclockrate.html language=enus -->
## TOPIC 00128: Clocking:Ref Clock Rate

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-refclockrate.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-refclockrate.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector. This property is only valid when the Ref Clock Source property is set to ClkIn or RefIn. Valid Values: PXIe-5644/5645/5646, PXIe-5601/5663/5663E, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841—10 MHz P

### Clocking:Ref Clock Rate

Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector. This property is only valid when the [Ref Clock Source](/csh?topicname=pnirfsa-refclocksrc.html) property is set to **ClkIn** or **RefIn**.

**Valid Values**:

**PXIe-5644/5645/5646, PXIe-5601/5663/5663E, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841**—10 MHz

**PXIe-5603/5605/5665/5667/5668**—5 MHz to 100 MHz, in increments of 1 MHz

**PXIe-5841 with PXIe-5655, PXIe-5842**—10 MHz, 100 MHz, 270 MHz, and 3.84 MHz * *y*, where *y* is 4, 8, 16, 24, 25, or 32.

**PXIe-5860**—10 MHz, 100 MHz

**Default Value**: 10 MHz

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref Clock Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSA Configure Ref Clock |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-refclocksrc.html language=enus -->
## TOPIC 00129: Clocking:Ref Clock Source

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-refclocksrc.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-refclocksrc.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Reference Clock source. For the PXIe-5694, if your application requires an external LO source, set this property to None. Default Values: PXIe-5694: RefIn All other devices: OnboardClock Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/564

### Clocking:Ref Clock Source

Specifies the Reference Clock source.

Note

None

**Default Values**:

**PXIe-5694**: RefIn

**All other devices**: OnboardClock

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ref Clock Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSA Configure Ref Clock |
| Channel-based | No |
| Resettable | Yes |

| None | None | No Reference Clock is required for the current device configuration. This value is valid only for the PXIe-5694 and for the PXIe-5668 to indicate no Reference Clock should be used when an External LO is used with the VSA and the Digitizer will use an External Clock as the Sample Clock Timebase |
| --- | --- | --- |
| OnboardClock | OnboardClock | PXI-5661ï¿½NI-RFSA locks the NI-RFSA device to the PXI-5600 RF downconverter onboard clock. PXIe-5663/5663Eï¿½NI-RFSA locks the PXIe-5663/5663E to the PXI/PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, connect the REF IN/OUT connector on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. PXIe-5665ï¿½NI-RFSA locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622. PXIe-5667ï¿½NI-RFSA locks the PXIe-5667 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. PXIe-5668ï¿½Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860ï¿½Lock the NI-RFSA device to its onboard clock. PXIe-5830/5831/5832ï¿½For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653ï¿½Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653ï¿½Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5841 with PXIe-5655ï¿½Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. PXIe-5842ï¿½Lock to the associated PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860ï¿½Lock to the PXIe-5860 onboard clock. |
| RefIn | RefIn | PXI-5661ï¿½NI-RFSA locks the NI-RFSA device to the signal at the external FREQ REF IN connector on the PXI-5600. PXIe-5663/5663Eï¿½Connect the external signal to the PXI/PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, this configuration can only be used in external digitizer mode. PXIe-5665ï¿½Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Ref Clock Rate property according to the frequency of your external clock signal. PXIe-5667ï¿½Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN connector on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Ref Clock Rate property according to the frequency of your external clock signal. PXIe-5668ï¿½Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the clock rate parameter according to the frequency of your external clock signal. PXIe-5694—Connect the Reference Clock signal to the REF/LO IN connector on the PXIe-5694 front panel. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860ï¿½Lock the NI-RFSA device to the signal at the external REF IN connector. PXIe-5830/5831/5832ï¿½For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For the PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653ï¿½Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653ï¿½Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5841 with PXIe-5655ï¿½Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. PXIe-5842ï¿½Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860ï¿½Lock to the signal at the REF IN connector on the PXIe-5860. |
| PXI_Clk | PXI_Clk | PXI-5661ï¿½NI-RFSA locks the NI-RFSA device to the PXI backplane clock using the PXI-5600. You must connect the PXI 10 MHz connector to the REF IN connector on the PXI-5600 front panel to use this option. PXIe-5668ï¿½Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667, PXIe-5694, PXIe-5820/5840/5841/5860ï¿½NI-RFSA locks the device to the PXI backplane clock. PXIe-5830/5831/5832/5841 with PXIe-5655, PXIe-5842, PXIe-5860ï¿½NI-RFSA locks the device to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
| ClkIn | ClkIn | PXI-5661ï¿½This configuration does not apply to the PXI-5661. PXIe-5663/5663Eï¿½NI-RFSA locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXI/PXIe-5652. PXIe-5665ï¿½NI-RFSA locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Ref Clock Rate property to 100 MHz. PXIe-5667ï¿½NI-RFSA locks the PXIe-5667 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Connect the 10 MHZ REF OUT connector on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. Set the Ref Clock Rate property to 100 MHz. PXIe-5668ï¿½Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the clock rate parameter to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860ï¿½This configuration does not apply. |
| PXI_ClkMaster | PXI_ClkMaster | PXIe-5831 with PXIe-5653ï¿½NI-RFSA configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653ï¿½NI-RFSA configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860ï¿½This configuration does not apply. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-referencelevel.html language=enus -->
## TOPIC 00130: Vertical:Reference Level (dBm)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-referencelevel.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-referencelevel.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference level, in dBm. The reference level represents the maximum expected power of an RF input signal. For the PXIe-5645, this property is ignored if you are using the I/Q ports. Refer to the External Gain property for more information about how configuring an external gain and a re

### Vertical:Reference Level (dBm)

Specifies the reference level, in dBm. The reference level represents the maximum expected power of an RF input signal.

Note

Refer to the [External Gain](pnirfsa-externalgain-5601.html) property for more information about how configuring an external gain and a reference level affect attenuation.

**Default Value**: 0

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Improving Your Measurements](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=improving-your-measurements)

[Programming Attenuation-Related Properties and Attributes Using NI-RFSA](https://ni.com/docs/en-US/csh?pubname=pxie-5665-feature&topicname=programming-attenuation)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSA Configure Reference Level |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-referencelevelheadroom.html language=enus -->
## TOPIC 00131: Vertical:Advanced:Reference Level Headroom (dB)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-referencelevelheadroom.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-referencelevelheadroom.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the margin NI-RFSA adds to the Reference Level property. The margin helps to avoid clipping and overflow warnings if the input signal exceeds the configured reference level. NI-RFSA configures the input gain to avoid clipping and associated overflow warnings as long as the instantaneous po

### Vertical:Advanced:Reference Level Headroom (dB)

Specifies the margin NI-RFSA adds to the [Reference Level](/csh?topicname=pnirfsa-referencelevel.html) property. The margin helps to avoid clipping and overflow warnings if the input signal exceeds the configured reference level.

NI-RFSA configures the input gain to avoid clipping and associated overflow warnings as long as the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or have already included margin in the reference level, you may be able to improve the signal-to-noise ratio by reducing the reference level headroom.

**Default Values**:

**PXIe-5830/5831/5832/5841/5842/5860**: 1.0 dB

**PXIe-5840**: 0.0 dB

**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference Level Headroom |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-reftorefholdoff.html language=enus -->
## TOPIC 00132: Triggers:Ref:Advanced:Ref To Ref Trigger Holdoff (s)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-reftorefholdoff.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-reftorefholdoff.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum time, in seconds, that must elapse between Reference Triggers of two records. The device does not recognize the Reference Trigger of the next record before this minimum time elapses. Default Value: 0 Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/58

### Triggers:Ref:Advanced:Ref To Ref Trigger Holdoff (s)

Specifies the minimum time, in seconds, that must elapse between Reference Triggers of two records. The device does not recognize the Reference Trigger of the next record before this minimum time elapses.

**Default Value**: 0

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference To Reference Holdoff |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-reftrig-digedge-edge.html language=enus -->
## TOPIC 00133: Triggers:Ref:Digital Edge:Edge

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-reftrig-digedge-edge.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-reftrig-digedge-edge.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the Reference Trigger. This property is used only when the Ref Trigger Type property is set to Digital Edge. Default Value: Rising Edge Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Related

### Triggers:Ref:Digital Edge:Edge

Specifies the active edge for the Reference Trigger. This property is used only when the [Ref Trigger Type](/csh?topicname=pnirfsa-reftrig-type.html) property is set to **Digital Edge**.

**Default Value**: Rising Edge

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

[PXI Trigger Lines](/csh?context=nirfsa_nirfsa_pxi-trigger-lines)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference Trigger Digital Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSA Configure Trigger |
| Channel-based | No |
| Resettable | Yes |

| Rising Edge | 900 | The trigger asserts on the rising edge of the signal. |
| --- | --- | --- |
| Falling Edge | 901 | The trigger asserts on the falling edge of the signal. This value is only valid for the PXIe-5668. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-reftrig-iqpwredge-lvl.html language=enus -->
## TOPIC 00134: Triggers:Ref:IQ Power Edge:Level

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-reftrig-iqpwredge-lvl.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-reftrig-iqpwredge-lvl.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level, in dBm, at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. If you are using external gain with your device, refer to the External Gain proper

### Triggers:Ref:IQ Power Edge:Level

Specifies the power level, in dBm, at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. If you are using external gain with your device, refer to the [External Gain](/csh?topicname=pnirfsa-externalgain-5601.html) property for more information about how this property affects the I/Q power edge trigger level.

**Default Value**: 0

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

[PXI Trigger Lines](/csh?context=nirfsa_nirfsa_pxi-trigger-lines)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Power Edge Trigger Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSA Configure Trigger |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-resourcedescriptor.html language=enus -->
## TOPIC 00135: Inherent IVI Attributes:Advanced Session Information:Resource Descriptor

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-resourcedescriptor.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-resourcedescriptor.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the resource descriptor NI-RFSA uses to identify the physical device. If you initialize NI-RFSA with a logical name, this property contains the resource name that corresponds to the entry in the IVI Configuration Utility. If you initialize NI-RFSA with the resource name, this property cont

### Inherent IVI Attributes:Advanced Session Information:Resource Descriptor

Indicates the resource descriptor NI-RFSA uses to identify the physical device. If you initialize NI-RFSA with a logical name, this property contains the resource name that corresponds to the entry in the IVI Configuration Utility.

If you initialize NI-RFSA with the resource name, this property contains that value.

**Default Value**: N/A

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Resource Descriptor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-rfelectronicattentableindex-5603.html language=enus -->
## TOPIC 00136: Factory Calibration:NI 5665/5668R:RF Electronic Attenuation Table Index

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-rfelectronicattentableindex-5603.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-rfelectronicattentableindex-5603.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the value of the RF electronic attenuation from a table of valid configurations. This property is valid only during a calibration session and when you set the RF Path Selection property to RF band 1. Default Value: N/A Supported Devices: PXIe-5603/5605/5606 Remarks The following table lists

### Factory Calibration:NI 5665/5668R:RF Electronic Attenuation Table Index

Selects the value of the RF electronic attenuation from a table of valid configurations. This property is valid only during a calibration session and when you set the [RF Path Selection](/csh?topicname=pnirfsa-rfpathselection.html) property to **RF band 1**.

**Default Value**: N/A

**Supported Devices**: PXIe-5603/5605/5606

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RF Electronic Attenuation Table Index |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-rfpreselectorfilter.html language=enus -->
## TOPIC 00137: Signal Path:Advanced:RF Preselector Filter

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-rfpreselectorfilter.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-rfpreselectorfilter.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RF preselector filter to use. You can write to this property when using only the PXIe-5693 as a stand-alone device. Default Values: PXIe-5667, PXIe-5693: RF Preselector 9 PXIe-5665: RF Preselector Filter None Supported Devices: PXIe-5665/5667, PXIe-5693 Remarks The following table list

### Signal Path:Advanced:RF Preselector Filter

Specifies the RF preselector filter to use.

Note

**Default Values**:

**PXIe-5667, PXIe-5693**: RF Preselector 9

**PXIe-5665**: RF Preselector Filter None

**Supported Devices**: PXIe-5665/5667, PXIe-5693

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RF Preselector Filter |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| RF Preselector Filter None | 3300 | Specifies that no preselector filter is used. |
| --- | --- | --- |
| RF Preselector Filter 1 | 3301 | Specifies that the 19 MHz to 35 MHz preselector filter is used. |
| RF Preselector Filter 2 | 3302 | Specifies that the 33 MHz to 61 MHz preselector filter is used. |
| RF Preselector Filter 3 | 3303 | Specifies that the 59 MHz to 110 MHz preselector filter is used. |
| RF Preselector Filter 4 | 3304 | Specifies that the 90 MHz to 170 MHz preselector filter is used. |
| RF Preselector Filter 5 | 3305 | Specifies that the 140 MHz to 245 MHz preselector filter is used. |
| RF Preselector Filter 6 | 3306 | Specifies that the 205 MHz to 370 MHz preselector filter is used. |
| RF Preselector Filter 7 | 3307 | Specifies that the 330 MHz to 575 MHz preselector filter is used. |
| RF Preselector Filter 8 | 3308 | Specifies that the 530 MHz to 975 MHz preselector filter is used. |
| RF Preselector Filter 9 | 3309 | Specifies that the 910 MHz to 1,640 MHz preselector filter is used. |
| RF Preselector Filter 10 | 3310 | Specifies that the 1,560 MHz to 2,040 MHz preselector filter is used. |
| RF Preselector Filter 11 | 3311 | Specifies that the 1,960 MHz to 2,540 MHz preselector filter is used. |
| RF Preselector Filter 12 | 3312 | Specifies that the 2,460 MHz to 3,040 MHz preselector filter is used. |
| RF Preselector Filter 13 | 3313 | Specifies that the 2,960 MHz to 3,840 MHz preselector filter is used. |
| RF Preselector Filter 14 | 3314 | Specifies that the 3,760 MHz to 4,640 MHz preselector filter is used. |
| RF Preselector Filter 15 | 3315 | Specifies that the 4,560 MHz to 5,840 MHz preselector filter is used. |
| RF Preselector Filter 16 | 3316 | Specifies that the 5,760 MHz to 7,040 MHz preselector filter is used. |
| RF Preselector Filter External Filter | 3317 | Specifies that the 20 MHz to 3.04 GHz external filter filter path is used. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-selectedports.html language=enus -->
## TOPIC 00138: Signal Path:Advanced:Selected Ports

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-selectedports.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-selectedports.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which port to configure to acquire a signal. When using RF list mode, ports cannot be shared with NI-RFSG. Valid Values: PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: "" (empty string) PXIe-5830: if0, if1 PXIe-5831/5832: if0, if1, rf<0-1>/port<x> , where 0-1 indicates one (0 ) or two

### Signal Path:Advanced:Selected Ports

Specifies which port to configure to acquire a signal.

Note

**Valid Values**:

PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: "" (empty string)

PXIe-5830: if0, if1

PXIe-5831/5832: if0, if1, rf*<0-1>*/port*<x>*, where *0-1* indicates one (*0*) or two (*1*) mmRH-5582 connections and *x* is the port number on the mmRH-5582 front panel.

PXIe-5842 VST with 54 GHz Frequency Extension: rfinout0, rfinout1, rmm0/port0, rmm0/port1

**Default Value**:

PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: "" (empty string)

PXIe-5830/5831/5832: if1

PXIe-5842 VST with 54 GHz Frequency Extension: rmm0/port1

**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Available Ports](pnirfsa-availableports.html) property

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

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-serialnum.html language=enus -->
## TOPIC 00139: Device Characteristics:Serial Number

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-serialnum.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-serialnum.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the serial number of the RF downconverter module. For the PXIe-5644/5645/5646 and PXIe-5820/5840/5841/5842/5860, this property returns the serial number of the VST module. For the PXIe-5830/5831/5832, this property returns the serial number of the PXIe-3621/3622/3623. Default Value: N/A Supp

### Device Characteristics:Serial Number

Returns the serial number of the RF downconverter module.

Note

**Default Value**: N/A

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-signalbandwidth.html language=enus -->
## TOPIC 00140: Acquisition:IQ:Signal Bandwidth (Hz)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-signalbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-signalbandwidth.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the input signal around the I/Q carrier frequency. This value must be less than or equal to (0.8 x I/Q rate). NI-RFSA defines signal bandwidth as twice the maximum I/Q signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the ban

### Acquisition:IQ:Signal Bandwidth (Hz)

Specifies the bandwidth of the input signal around the [I/Q carrier frequency](/csh?topicname=pnirfsa-iqcarrierfrequency.html). This value must be less than or equal to (0.8 x [I/Q rate](/csh?topicname=pnirfsa-iq-rate.html)).

NI-RFSA defines *signal bandwidth* as twice the maximum I/Q signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the bandwidth is simply the I/Q signal's minimum frequency subtracted from its maximum frequency or *f*
<sub>max</sub> - *f*
<sub>min</sub>.

If you do not set this property, NI-RFSA uses the maximum available signal bandwidth. Depending on your device settings, setting this property enables certain optimizations. Based on the specified signal bandwidth, NI-RFSA decides the minimum equalized bandwidth and equalizer gain.

Note

Downconverter Frequency Offset Mode

Ensure you set the signal bandwidth wide enough to encompass all significant anticipated input power. In cases where NI-RFSA optimizes the input gain based on the signal bandwidth, significant input power outside the signal bandwidth can lead to clipping and associated overflow warnings if you do not have much margin in your [reference level](pnirfsa-referencelevel.html).

**Default Value**: 0 Hz

**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[PXIe-5830 Frequency and Bandwidth Selection](https://ni.com/docs/en-US/csh?pubname=pxie-5830-feature&topicname=frequency-and-bandwidth-selection)

[PXIe-5831/5832 Frequency and Bandwidth Selection](https://ni.com/docs/en-US/csh?pubname=pxie-5831&topicname=frequency-and-bandwidth-selection)

[PXIe-5841 Frequency and Bandwidth Selection](https://ni.com/docs/en-US/csh?pubname=pxie-5841&topicname=frequency-and-bandwidth-selection)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Signal Bandwidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-signalconditioningenabled.html language=enus -->
## TOPIC 00141: Signal Path:Advanced:NI 5694:Signal Conditioning Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-signalconditioningenabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-signalconditioningenabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether all signal conditioning is enabled on the PXIe-5694. If you set this property to Bypassed, NI-RFSA bypasses all signal conditioning, prevents any signal downconversion, and fixes the values for the Downconverter Gain property, Device Instantaneous Bandwidth property, and the IF Fil

### Signal Path:Advanced:NI 5694:Signal Conditioning Enabled

Specifies whether all signal conditioning is enabled on the PXIe-5694.

Note

Bypassed

Downconverter Gain

Device Instantaneous Bandwidth

IF Filter Bandwidth

**Default Value**: Enabled

**Supported Devices**: PXIe-5694

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Signal Conditioning Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Enabled | 3600 | Enables signal conditioning. |
| --- | --- | --- |
| Bypassed | 3601 | Bypasses all signal conditioning. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-smoothspectrumenabled.html language=enus -->
## TOPIC 00142: Acquisition:Spectrum:Smooth Spectrum Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-smoothspectrumenabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-smoothspectrumenabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies that an optimized IF filtering selection is made at different spectrum frequency ranges during spectrum acquisition. The IF filter used depends on the configured RF center frequency, as shown in the following table. Center Frequency IF Filter ≥20 Hz and <80 MHz 300 kHz ≥80 MHz 50 MHz Setti

### Acquisition:Spectrum:Smooth Spectrum Enabled

Specifies that an optimized IF filtering selection is made at different spectrum frequency ranges during spectrum acquisition.

The IF filter used depends on the configured RF center frequency, as shown in the following table.

| Center Frequency | IF Filter |
| --- | --- |
| ≥20 Hz and <80 MHz | 300 kHz |
| ≥80 MHz | 50 MHz |

Note

Enabled

IF Filter Bandwidth

Device Instantaneous Bandwidth

**Default Value**: Disabled

**Supported Devices**: PXIe-5665/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Smooth Spectrum Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Disabled | 1900 | The property is disabled. |
| --- | --- | --- |
| Enabled | 1901 | The property is enabled. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-fftsize.html language=enus -->
## TOPIC 00143: Acquisition:Spectrum:FFT Size

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-fftsize.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-fftsize.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size of the fast Fourier transform (FFT). Default Value: N/A Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Remarks The following table lists the characteristics of this property. Short Name FFT Size Data typ

### Acquisition:Spectrum:FFT Size

Returns the size of the fast Fourier transform (FFT).

**Default Value**: N/A

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FFT Size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-fftwindowshapefactor.html language=enus -->
## TOPIC 00144: Acquisition:Spectrum:FFT Window Shape Factor

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-fftwindowshapefactor.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-fftwindowshapefactor.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the shape factor of the window used in the fast Fourier transform (FFT). The window shape factor is defined as the ratio of the 60 dB to 6 dB bandwidths. The following table shows the shape factor for each NI-RFSA FFT window type. Window Type Shape Factor Uniform 1.57:1 Hanning 1.94:1 Hammin

### Acquisition:Spectrum:FFT Window Shape Factor

Returns the shape factor of the window used in the fast Fourier transform (FFT).
 The window shape factor is defined as the ratio of the 60 dB to 6 dB bandwidths.

The following table shows the shape factor for each NI-RFSA FFT window type.

| Window Type | Shape Factor |
| --- | --- |
| Uniform | 1.57:1 |
| Hanning | 1.94:1 |
| Hamming | 2.13:1 |
| Exact Blackman | 2.52:1 |
| Flat Top | 2.0:1 |
| 4-term Blackman-Harris | 2.5:1 |
| 7-term Blackman-Harris | 4.1:1 |
| Low Side Lobe | 2.78:1 |
| Gaussian | 2.3:1 |
| Kaiser Bessel | 2.55:1 |

**Default Value**: N/A

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FFT Window Shape Factor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-fftwindowtype.html language=enus -->
## TOPIC 00145: Acquisition:Spectrum:FFT Window Type

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-fftwindowtype.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-fftwindowtype.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time-domain window type. Default Value: PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: 7-term Blackman-Harris PXIe-5667: 4-term Blackman-Harris Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXI

### Acquisition:Spectrum:FFT Window Type

Specifies the time-domain window type.

**Default Value**:

**PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: 7-term Blackman-Harris

**PXIe-5667**: 4-term Blackman-Harris

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Resolution Bandwidth](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=resolution-bandwidth)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FFT Window Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Uniform | 500 | No window is applied. |
| --- | --- | --- |
| Hanning | 501 | The Hanning window is useful for analyzing transients longer than the time duration of the window, and also for general-purpose applications. A Hanning window is applied to the waveform using the following equation: y[i] = 0.5 ï¿½ x[i] ï¿½ [1ï¿½cos(w)] where w = (2)i/n and n = waveform size. |
| Hamming | 502 | A Hamming window is applied to the waveform using the following equation: y[i] = x[i] ï¿½ [0.54 ï¿½ 0.46cos(w)] where w = (2)i/n and n = the waveform size. Note Hanning and Hamming windows are somewhat similar. However, in the time domain, the Hamming window does not get as close to zero near the edges as does the Hanning window. |
| Blackman-Harris | 503 | A Blackman-Harris window is applied to the waveform using the following equation: y[i] = x[i] ï¿½ [0.42323 ï¿½ 0.49755cos(w) + 0.07922cos(2w)] where w = (2)i/n and n = the waveform size. |
| Exact Blackman | 504 | An Exact Blackman window is applied to the waveform using the following equation: y[i] = x[i] ï¿½ [a 0 ï¿½ a 1cos(w) + a 2cos(2w)] where w = (2)i/n n = the waveform size a 0 = 7,938/18,608 a 1 = 9,240/18,608 a 2 = 1,430/18,608 |
| Blackman | 505 | A Blackman window is useful for analyzing transient signals, and provides similar windowing to Hanning and Hamming windows but adds one additional cosine term to reduce ripple. A Blackman window is applied to the waveform using the following equation: y[i] = x[i] ï¿½ [0.42 ï¿½ 0.50cos(w) + 0.08cos(2w)] where w = (2)i/n and n = the waveform size. |
| Flat Top | 506 | The fifth-order Flat Top window has the best amplitude accuracy of all the window functions. The increased amplitude accuracy (ï¿½0.02 dB for signals exactly between integral cycles) is at the expense of frequency selectivity. The Flat Top window is most useful in accurately measuring the amplitude of single frequency components with little nearby spectral energy in the signal. A fifth-order Flat Top window is applied to the waveform using the following equation: y[i] = x[i] ï¿½ [a 0 ï¿½ a 1cos(w) + a 2cos(2w) ï¿½ a 3cos(3w) + a 4cos(4w)] where w = (2)i/n n is the waveform size a 0 = 0.215578948 a 1 = 0.41663158 a 2 = 0.277263158 a 3 = 0.083578947 a 4 = 0.006947368. |
| 4-term Blackman-Harris | 507 | A four-term Blackman-Harris window is a general-purpose window; it has side-lobe rejection in the upper 90 dB, with moderately wide side lobe. A 4-term Blackman Harris window is applied to the waveform using the following equation: w[i] = x[i] ï¿½ [a 0 ï¿½ a 1cos(w) + a 2cos(2w) ï¿½ a 3cos(3w)] where w = (2)i/N N is the waveform size a 0 = 0.35875 a 1 = 0.48829 a 2 = 0.14128 a 3 = 0.01168 |
| 7-term Blackman-Harris | 508 | A 7-term Blackman-Harris window has the highest dynamic range; it is ideal for signal-to-noise ratio applications. A 7-term Blackman Harris window is applied to the waveform using the following equation: y[i] = x[i] ï¿½ [a 0 ï¿½ a 1cos(w) + a 2cos(2w) ï¿½ a 3cos(3w) + a 4cos(4w) ï¿½ a 5cos(5w) + a 6cos(6w)] where w = (2)i/n n is the waveform size a 0 = 0.27105140069342 a 1 = 0.43329793923448 a 2 = 0.21812299954311 a 3 = 0.06592544638803 a 4 = 0.01081174209837 a 5 = 0.00077658482522 a 6 = 0.00001388721735. |
| Low Side Lobe | 509 | The Low Side Lobe window further reduces the size of the main lobe. The following equation defines the Low Side Lobe window. where N is the length of window w = (2 n)/N a 0 = 0.323215218 a 1 = 0.471492057 a 2 = 0.17553428 a 3 = 0.028497078 a 4 = 0.001261367 |
| Gaussian | 510 | A Gaussian window is applied to the waveform using the following equation: y[i] = x[i] ï¿½ e ((-0.5(i - (N-1)/0.5) / (σ(N-1)/0.5)) where N is the length of the window and σ ≤ 0.5 |
| Kaiser Bessel | 511 | A Kaiser-Bessel window is applied to the waveform using the following equation: y[i] = x[i] ï¿½ I0 ï¿½ (π ï¿½ α(1 - (2i/ (N-1)-1)2)0.5) / (I0 ï¿½ π ï¿½ α) where i ≥ 0 and i ≤ N-1 N is the length of the window α determines the shape of the window I0 is the zeroth order Modified Bessel function of the first kind |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-numaverages.html language=enus -->
## TOPIC 00146: Acquisition:Spectrum:Number Of Averages

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-numaverages.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-numaverages.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions to average. The averaging process returns the final result after the number of averages is complete. Default Value: 10 Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Remarks The follo

### Acquisition:Spectrum:Number Of Averages

Specifies the number of acquisitions to average. The averaging process returns the final result after the number of averages is complete.

**Default Value**: 10

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Averages |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-resolutionbandwidthtype.html language=enus -->
## TOPIC 00147: Acquisition:Spectrum:Resolution Bandwidth Type

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-resolutionbandwidthtype.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-spectrum-resolutionbandwidthtype.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the Resolution Bandwidth property is expressed. Default Value: 3 dB Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Remarks The following table lists the characteristics of this property. Short Name Resoluti

### Acquisition:Spectrum:Resolution Bandwidth Type

Specifies how the [Resolution Bandwidth](/csh?topicname=pnirfsa-spectrum-resolutionbandwidth.html) property is expressed.

**Default Value**: 3 dB

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Resolution Bandwidth Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| 3dB | 300 | Defines the resolution bandwidth (RBW) in terms of the 3 dB bandwidth of the window specified by the FFT Window Type property. |
| --- | --- | --- |
| 6dB | 301 | Defines the RBW in terms of the 6 dB bandwidth of the window specified by the FFT Window Type property. |
| Bin Width | 302 | Defines the RBW in terms of the display resolution, which is the ratio of the sample rate to the number of samples that you acquire. |
| ENBW | 303 | Defines the RBW in terms of the equivalent noise bandwidth (ENBW) of the window specified by the FFT Window Type property. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-starttorefholdoff.html language=enus -->
## TOPIC 00148: Triggers:Ref:Advanced:Start To Ref Trigger Holdoff (s)

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-starttorefholdoff.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-starttorefholdoff.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum time, in seconds, that must elapse after the Start Trigger is received before the device recognizes a Reference Trigger. Default Value: 0 Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Related Topics Triggers Remarks Th

### Triggers:Ref:Advanced:Start To Ref Trigger Holdoff (s)

Specifies the minimum time, in seconds, that must elapse after the Start Trigger is received before the device recognizes a Reference Trigger.

**Default Value**: 0

**Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start To Reference Holdoff |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-starttrig-digedge-edge.html language=enus -->
## TOPIC 00149: Triggers:Start:Digital Edge:Edge

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-starttrig-digedge-edge.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-starttrig-digedge-edge.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the Start Trigger. This property is used only when the Start Trigger Type property is set to Digital Edge. Default Value: Rising Edge Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Related T

### Triggers:Start:Digital Edge:Edge

Specifies the active edge for the Start Trigger. This property is used only when the [Start Trigger Type](/csh?topicname=pnirfsa-starttrig-type.html) property is set to **Digital Edge**.

**Default Value**: Rising Edge

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

[PXI Trigger Lines](/csh?context=nirfsa_nirfsa_pxi-trigger-lines)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Digital Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSA Configure Trigger |
| Channel-based | No |
| Resettable | Yes |

| Rising Edge | 900 | The trigger asserts on the rising edge of the signal. |
| --- | --- | --- |
| Falling Edge | 901 | The trigger asserts on the falling edge of the signal. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-starttrig-digedge-src.html language=enus -->
## TOPIC 00150: Triggers:Start:Digital Edge:Source

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-starttrig-digedge-src.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-starttrig-digedge-src.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the Start Trigger. This property is used only when the Start Trigger Type property is set to Digital Edge. Default Value: "" (empty string) Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

### Triggers:Start:Digital Edge:Source

Specifies the source terminal for the Start Trigger. This property is used only when the [Start Trigger Type](/csh?topicname=pnirfsa-starttrig-type.html) property is set to **Digital Edge**.

**Default Value**: "" (empty string)

**Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

| PFI0 | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0. |
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
| PXI_STAR | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. |
| PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| TimerEvent | The trigger is received from the Timer Event. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5663E/5665. |
| DIO/PFI0 | The trigger is received on PFI 0 of the DIO front panel connector. |
| DIO/PFI1 | The trigger is received on PFI 1 of the DIO front panel connector. |
| DIO/PFI2 | The trigger is received on PFI 2 of the DIO front panel connector. |
| DIO/PFI3 | The trigger is received on PFI 3 of the DIO front panel connector. |
| DIO/PFI4 | The trigger is received on PFI 4 of the DIO front panel connector. |
| DIO/PFI5 | The trigger is received on PFI 5 of the DIO front panel connector. |
| DIO/PFI6 | The trigger is received on PFI 6 of the DIO front panel connector. |
| DIO/PFI7 | The trigger is received on PFI 7 of the DIO front panel connector. |

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

[PXI Trigger Lines](/csh?context=nirfsa_nirfsa_pxi-trigger-lines)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Digital Edge Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niRFSA Configure Trigger |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-stepgainenabled.html language=enus -->
## TOPIC 00151: Vertical:Advanced:NI 5694:Step Gain Enabled

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-stepgainenabled.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-stepgainenabled.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the step gain amplifier. Default Value: Disabled Supported Devices: PXIe-5694 Remarks The following table lists the characteristics of this property. Short Name Step Gain Enabled Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes

### Vertical:Advanced:NI 5694:Step Gain Enabled

Specifies whether to enable the step gain amplifier.

**Default Value**: Disabled

**Supported Devices**: PXIe-5694

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Step Gain Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Disabled | 3200 | Disables the step gain amplifier. |
| --- | --- | --- |
| Enabled | 3201 | Enables the step gain amplifier. |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-steptriggersource.html language=enus -->
## TOPIC 00152: Triggers:Configuration List Step:Digital Edge:Source

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-steptriggersource.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-steptriggersource.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the list trigger source. The default value is the End Of Record Event. When the value is End Of Record Event, this will signal the instrument to reconfigure from configuration N to configuration N + 1 after the End Of Record Event, and before the Ready For Advance Event. If you configure

### Triggers:Configuration List Step:Digital Edge:Source

Configures the list trigger source. The default value is the **End Of Record Event**. When the value is **End Of Record Event**, this will signal the instrument to reconfigure from configuration N to configuration N + 1 after the End Of Record Event, and before the Ready For Advance Event. If you configure this property to any other value, the instrument reconfiguration will occur whenever the specified trigger is asserted, which may be decoupled from the acquisition state machine. Therefore, if you trigger a reconfiguration during a record acquisition, you may see transient data in the record, which should be discarded by the application. NI recommends you to use this property only in case of streaming.

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Configuration List Step Trigger Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-supportedinstrumentmodels.html language=enus -->
## TOPIC 00153: Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-supportedinstrumentmodels.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-supportedinstrumentmodels.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a comma-separated list of supported devices. Default Value: N/A Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860 Remarks The follow

### Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models

Returns a comma-separated list of supported devices.

**Default Value**: N/A

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Supported Instrument Models |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-syncadvancetriggerdistline.html language=enus -->
## TOPIC 00154: Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Advance Trigger Dist Line

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-syncadvancetriggerdistline.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-syncadvancetriggerdistline.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which external trigger line distributes the synchronized Advance Trigger signal. When synchronizing the Advance Trigger, configure all devices to use the same Advance Trigger distribution line. Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device in the N

### Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Advance Trigger Dist Line

Specifies which external trigger line distributes the synchronized Advance Trigger signal. When synchronizing the Advance Trigger, configure all devices to use the same Advance Trigger distribution line.

Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

**Valid Values**: PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

**Default Value**: "" (empty string)

**Supported Devices**: PXIe-5644/5645/5646

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sync Advance Trigger Dist Line |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-syncadvancetriggermaster.html language=enus -->
## TOPIC 00155: Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Advance Trigger Master

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-syncadvancetriggermaster.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-syncadvancetriggermaster.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device is the master for synchronizing the shared Advance Trigger between multiple devices. The master device distributes the synchronized Advance Trigger to all devices in the system through the Advance Trigger distribution line. When synchronizing the Advance Trigger, one dev

### Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Advance Trigger Master

Specifies whether the device is the master for synchronizing the shared Advance Trigger between multiple devices. The master device distributes the synchronized Advance Trigger to all devices in the system through the Advance Trigger distribution line.

When synchronizing the Advance Trigger, one device must always be designated as the master. When the device is configured as a master, it actively drives the Advance Trigger distribution line. When the device is configured as a slave, set the [Advance Trigger Type](pnirfsa-advancetrig-type.html) property to **Digital Edge**, and the [Advance Trigger Digital Edge Source](pnirfsa-advancetrig-digedge-src.html) property to **Sync_Advance**.

Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

**Default Value**: FALSE

**Supported Devices**: PXIe-5644/5645/5646

| TRUE | The device is the master device for synchronizing the Advance Trigger. |
| --- | --- |
| FALSE | The device is not the master device for synchronizing the Advance Trigger. |

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sync Advance Trigger Master |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-syncreftriggerdistline.html language=enus -->
## TOPIC 00156: Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Ref Trigger Dist Line

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-syncreftriggerdistline.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-syncreftriggerdistline.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which external trigger line distributes the synchronized Reference Trigger signal. When synchronizing the Reference Trigger, configure all devices to use the same Reference Trigger distribution line. Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device in

### Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Ref Trigger Dist Line

Specifies which external trigger line distributes the synchronized Reference Trigger signal. When synchronizing the Reference Trigger, configure all devices to use the same Reference Trigger distribution line.

Refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic appropriate to your device in the *NI RF Vector Signal Analyzers Help* for more information about device synchronization for vector signal transceivers.

**Valid Values**: PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

**Default Value**: "" (empty string)

**Supported Devices**: PXIe-5644/5645/5646

**Related Topics**

[Triggers](https://ni.com/docs/en-US/csh?pubname=ni-rfsa&topicname=ni-rfsa-triggers-vst)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sync Ref Trigger Dist Line |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-syncsampleclockmaster.html language=enus -->
## TOPIC 00157: Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Sample Clock Master

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-syncsampleclockmaster.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-syncsampleclockmaster.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device is the master when synchronizing the Sample Clock between multiple devices. The master device distributes the Sample Clock sync signal to all devices in the system through the Sample Clock sync distribution line. When synchronizing the Sample Clock, one device must alway

### Device Specific:Vector Signal Transceiver:Triggers:Synchronization:Sync Sample Clock Master

Specifies whether the device is the master when synchronizing the Sample Clock between multiple devices. The master device distributes the Sample Clock sync signal to all devices in the system through the Sample Clock sync distribution line.

When synchronizing the Sample Clock, one device must always be designated as the master. The master device actively drives the Sample Clock sync distribution line.

Refer to [Synchronization Using NI-RFSA and NI-RFSG](https://ni.com/docs/en-US/csh?pubname=pxie-5644-feature&topicname=sample-clock-sync) for more information about device synchronization for the PXIe-5646.

**Default Value**: FALSE

**Supported Devices**: PXIe-5646

| TRUE | The device is the master device for synchronizing the Sample Clock. |
| --- | --- |
| FALSE | The device is not the master device for synchronizing the Sample Clock. |

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

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-temperaturereadinterval.html language=enus -->
## TOPIC 00158: Device Characteristics:Temperature Read Interval

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-temperaturereadinterval.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-temperaturereadinterval.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the minimum time between temperature sensor readings in seconds. When you call the niRFSA Read Power Spectrum VI, niRFSA Read IQ VI, or niRFSA Initiate VI, NI-RFSA checks if at least the amount of time specified by this property has elapsed before reading the hardware temperature. NI-RFSA

### Device Characteristics:Temperature Read Interval

Indicates the minimum time between temperature sensor readings in seconds. When you call the [niRFSA Read Power Spectrum](/csh?context=nirfsa_nirfsa_javascript:launchmergedhelp() VI, [niRFSA Read IQ](/csh?context=nirfsa_nirfsa_javascript:launchmergedhelp() VI, or [niRFSA Initiate](/csh?context=nirfsa_nirfsa_javascript:launchmergedhelp() VI, NI-RFSA checks if at least the amount of time specified by this property has elapsed before reading the hardware temperature.

Note

niRFSA Perform Thermal Correction

Downconverter Gain

**Default Value**: 30 seconds

**Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Temperature Read Interval |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties

<!--NI_TOPIC bundle=niRFSA-labview-api-ref path=instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-timerstartsource.html language=enus -->
## TOPIC 00159: Configuration List:Advanced:Timer Start Source

- bundle_id: `niRFSA-labview-api-ref`
- source_path: `instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-timerstartsource.html`
- source_url: https://docs-be.ni.com/bundle/niRFSA-labview-api-ref/raw/resource/enus/instr-lib/nirfsa/nirfsa-rc/nirfsa/pnirfsa-timerstartsource.html
- document_id: `niRFSA-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property is not for customer use. Remarks The following table lists the characteristics of this property. Short Name Timer Start Source Data type cstr.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes

### Configuration List:Advanced:Timer Start Source

This property is not for customer use.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Timer Start Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niRFSA Properties
