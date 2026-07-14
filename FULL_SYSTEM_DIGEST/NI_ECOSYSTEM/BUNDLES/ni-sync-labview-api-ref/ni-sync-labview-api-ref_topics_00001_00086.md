# NI DOCUMENT BUNDLE: ni-sync-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-sync-labview-api-ref start=1 end=86 -->
<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/1588_prop.html language=enus -->
## TOPIC 00001: 1588

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/1588_prop.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/1588_prop.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

1588

[Clock Accuracy](nisync_attr_1588_clock_accuracy.html)

[Clock Class](nisync_attr_1588_clock_class.html)

[Clock ID](nisync_attr_1588_clock_id.html)

[Clock State](nisync_attr_1588_clock_state.html)

[Frequency Traceable](nisync_attr_1588_frequency_traceable.html)

[Grandmaster Clock Accuracy](nisync_attr_1588_grandmaster_clock_accuracy.html)

[Grandmaster Clock Class](nisync_attr_1588_grandmaster_clock_class.html)

[Grandmaster Clock ID](nisync_attr_1588_grandmaster_clock_id.html)

[Grandmaster Clock Priority1](nisync_attr_1588_grandmaster_priority1.html)

[Grandmaster Clock Priority2](nisync_attr_1588_grandmaster_priority2.html)

[IP Address](nisync_attr_1588_ip_address.html)

[Leap59](nisync_attr_1588_leap59.html)

[Leap61](nisync_attr_1588_leap61.html)

[Log Sync Interval](nisync_attr_1588_log_sync_interval.html)

[Mean Path Delay](nisync_attr_1588_mean_path_delay.html)

[Offset Scaled Log Variance](nisync_attr_1588_offset_scaled_log_variance.html)

[Priority1](nisync_attr_1588_priority1.html)

[Priority2](nisync_attr_1588_priority2.html)

[Steps to Grandmaster](nisync_attr_1588_steps_to_grandmaster.html)

[Time Source](nisync_attr_1588_time_source.html)

[Time Traceable](nisync_attr_1588_time_traceable.html)

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/8021as_prop.html language=enus -->
## TOPIC 00002: 802.1AS Properties

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/8021as_prop.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/8021as_prop.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

802.1AS Properties

[Port State](nisync_attr_8021as_port_state.html)

[Clock ID](nisync_attr_8021as_clock_id.html)

[Clock Class](nisync_attr_8021as_clock_class.html)

[Clock Accuracy](nisync_attr_8021as_clock_accuracy.html)

[Priority1](nisync_attr_8021as_priority1.html)

[Priority2](nisync_attr_8021as_priority2.html)

[Grandmaster Clock ID](nisync_attr_8021as_grandmaster_clock_id.html)

[Grandmaster Clock Class](nisync_attr_8021as_grandmaster_clock_class.html)

[Grandmaster Clock Accuracy](nisync_attr_8021as_grandmaster_clock_accuracy.html)

[Grandmaster Priority1](nisync_attr_8021as_grandmaster_priority1.html)

[Grandmaster Priority2](nisync_attr_8021as_grandmaster_priority2.html)

[Log Sync Interval](nisync_attr_8021as_log_sync_interval.html)

[Log Announce Interval](nisync_attr_8021as_log_announce_interval.html)

[Neighbor Propagation Delay Threshold](nisync_attr_8021as_neighbor_prop_delay_thresh.html)

[AS Capable](nisync_attr_8021as_as_capable.html)

[Interface Name](nisync_attr_8021as_interface_name.html)

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/advanced_subpalette.html language=enus -->
## TOPIC 00003: Advanced VIs

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/advanced_subpalette.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/advanced_subpalette.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Advanced VIs

**Owning Palette:** [NI-Sync VIs](nisynclv.html)

**Requires:** NI-Sync

Use the Advanced VIs in this palette to perform functions for advanced users, such as configuring the FPGA and measuring the frequency of a hardware line.

| Palette Object | Description |
| --- | --- |
| niSync Configure FPGA | Directly programs the FPGA on the module with an alternate bitstream file. |
| niSync Measure Frequency | Measures the frequency of a signal at the specified terminal. Using this VI, you can measure the oscillator of the system timing module, the frequency of an external clock connected to a front panel input, or the frequency of a full speed or divided synchronization clock. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/calibration_palette.html language=enus -->
## TOPIC 00004: Calibration VIs

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/calibration_palette.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/calibration_palette.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration VIs

**Owning Palette:** [NI-Sync VIs](nisynclv.html)

**Requires:** NI-Sync

Use the VIs on the Calibration palette to calibrate an NI-Sync compatible module using an external calibration reference. Using these VIs, you can write new calibration constants to your device's non-volatile onboard memory. You should perform external calibration at regular intervals to make sure your devices are operating at an optimal level.

| Palette Object | Description |
| --- | --- |
| niSync Adjust Clk10 Phase Voltage | Sets the Clk10 phase voltage value to be written to the specified device's non-volatile onboard memory using an external calibration reference. |
| niSync Adjust DDS Start Pulse Phase Voltage | Sets the DDS start trigger phase voltage to be written to the specified device's non-volatile onboard memory using an external calibration reference. |
| niSync Adjust Oscillator Voltage | Sets the oscillator voltage value to be written to the specified device's non-volatile onboard memory using an external calibration reference. |
| niSync Close External Calibration | Closes an instrument I/O session and deallocate any memory resources the driver uses. You can choose whether or not to write the new calibration constants set by an external calibration VI to your device's non-volatile onboard memory using this VI. |
| niSync Initialize External Calibration | Begins an external calibration session for the associated device. The VI returns an instrument driver session handle that you can use to adjust calibration constants for the module or display current calibration constants stored in the device's non-volatile onboard memory. |

| Subpalette | Description |
| --- | --- |
| Calibration Utility | Use the Calibration Utility VIs to perform miscellaneous tasks related to external calibration, such as changing the calibration password, displaying current calibration constants, and determining when to schedule your next external calibration session. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/calibration_prop.html language=enus -->
## TOPIC 00005: Calibration Properties

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/calibration_prop.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/calibration_prop.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration Properties

[Clk10 Phase Adjust](nisync_attr_clk10_phase_adjust.html)

[Oscillator Voltage](nisync_attr_oscillator_voltage.html)

[PFI0 Threshold](nisync_attr_pfi0_threshold.html)

[PFI1 Threshold](nisync_attr_pfi1_threshold.html)

[PFI2 Threshold](nisync_attr_pfi2_threshold.html)

[PFI3 Threshold](nisync_attr_pfi3_threshold.html)

[PFI4 Threshold](nisync_attr_pfi4_threshold.html)

[PFI5 Threshold](nisync_attr_pfi5_threshold.html)

[PFI0 1kOhm Termination Enable](nisync_attr_pfi0_1kohm_enable.html)

[PFI1 1kOhm Termination Enable](nisync_attr_pfi1_1kohm_enable.html)

[PFI2 1kOhm Termination Enable](nisync_attr_pfi2_1kohm_enable.html)

[PFI3 1kOhm Termination Enable](nisync_attr_pfi3_1kohm_enable.html)

[PFI4 1kOhm Termination Enable](nisync_attr_pfi4_1kohm_enable.html)

[PFI5 1kOhm Termination Enable](nisync_attr_pfi5_1kohm_enable.html)

[PFI0 10kOhm Termination Enable](nisync_attr_pfi0_10kohm_enable.html)

[PFI1 10kOhm Termination Enable](nisync_attr_pfi1_10kohm_enable.html)

[PFI2 10kOhm Termination Enable](nisync_attr_pfi2_10kohm_enable.html)

[PFI3 10kOhm Termination Enable](nisync_attr_pfi3_10kohm_enable.html)

[PFI4 10kOhm Termination Enable](nisync_attr_pfi4_10kohm_enable.html)

[PFI5 10kOhm Termination Enable](nisync_attr_pfi5_10kohm_enable.html)

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/calibration_utility_palette.html language=enus -->
## TOPIC 00006: Calibration Utility VIs

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/calibration_utility_palette.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/calibration_utility_palette.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Calibration Utility VIs

**Owning Palette:** [Calibration VIs](calibration_palette.html)

**Requires:** NI-Sync

Use the VIs on the Calibration Utility palette to perform advanced external calibration functions, such as reading the last external calibration date and time and displaying the recommended external calibration interval.

| Palette Object | Description |
| --- | --- |
| niSync Change External Calibration Password | Changes the external calibration password for the module. |
| niSync Get Clk10 Phase Voltage | Returns the Clk10 phase voltage, in volts, currently stored in the device's non-volatile onboard memory. |
| niSync Get DDS Start Phase Voltage | Returns the DDS start pulse phase voltage, in volts, currently stored in the device's non-volatile onboard memory. |
| niSync Get External Calibration Last Date and Time | Returns the date and time, in Greenwich Mean Time (GMT), of the module's last external calibration session. |
| niSync Get External Calibration Last Temperature | Returns the circuitry's temperature, in degrees Celsius, at the time of the last external calibration. |
| niSync Get External Calibration Recommended Interval | Returns the recommended time, in months, between external calibration sessions for the module. |
| niSync Get Oscillator Voltage | Returns the voltage that controls the oscillator's frequency, in volts, currently stored in the device's non-volatile onboard memory. |
| niSync Read Current Temperature | Reads the current temperature, in degrees Celsius, of the device's circuitry. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/clk_prop.html language=enus -->
## TOPIC 00007: Clk Properties

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/clk_prop.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/clk_prop.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Clk Properties

[ClkOut Gain Enable](nisync_attr_clkout_gain_enable.html)

[Disable ClkIn Attenuation](nisync_attr_clkin_attenuation_disable.html)

[PLL Frequency](nisync_attr_clkin_pll_freq.html)

[PLL Locked?](nisync_attr_clkin_pll_locked.html)

[PXI_Clk10 Present?](nisync_attr_pxiclk10_present.html)

[Use PLL?](nisync_attr_clkin_use_pll.html)

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/dds_prop.html language=enus -->
## TOPIC 00008: DDS Properties

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/dds_prop.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/dds_prop.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

DDS Properties

[DDS Frequency](nisync_attr_dds_freq.html)

[DDS Initial Delay](nisync_attr_dds_initial_delay.html)

[DDS Update Signal Source](nisync_attr_dds_update_source.html)

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/gps_palette.html language=enus -->
## TOPIC 00009: GPS VIs

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/gps_palette.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/gps_palette.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

GPS VIs

**Owning Palette:** [Timing VIs](timing_palette.html)

**Requires:** NI-Sync

Use the VIs in the GPS palette to perform tasks using the onboard GPS receiver of a timing and synchronization module, such as creating GPS timestamps or getting the current location and velocity of your module.

| Palette Object | Description |
| --- | --- |
| niSync Disable GPS or IRIG Timestamping | Disables GPS or IRIG timestamping on the specified device. |
| niSync Enable GPS or IRIG Timestamping | Timestamps an incoming GPS or IRIG signal with the current board time of the specified device. |
| niSync Get Location | Returns the last calculated latitude, longitude, and altitude of your device's onboard GPS receiver. |
| niSync Get Velocity | Returns the last calculated velocity of the associated device's onboard GPS receiver. Using this VI, you can display east velocity, north velocity, and up velocity in meters per second. |
| niSync Read Last GPS or IRIG Timestamp | Returns the last GPS or IRIG timestamp received from a specified device. This VI returns two timestamps: one with the board time when the pulse was received, and one with the time of the GPS receiver or IRIG message, depending on which instance you choose. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/gps_prop.html language=enus -->
## TOPIC 00010: GPS

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/gps_prop.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/gps_prop.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

GPS

[Is Antenna Connected](nisync_attr_gps_antenna_connected.html)

[Mobile Mode](nisync_attr_gps_mobile_mode.html)

[Percent Complete of Self Survey](nisync_attr_gps_self_survey.html)

[Recalculate Position on Reboot](nisync_attr_gps_recalculate_position.html)

[Satellites Available](nisync_attr_gps_satellites_available.html)

[Status](nisync_attr_gps_status.html)

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/interface_prop.html language=enus -->
## TOPIC 00011: Interface Properties

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/interface_prop.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/interface_prop.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Interface Properties

[Interface Number](nisync_attr_intf_num.html)

[Serial Number](nisync_attr_serial_num.html)

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_adjust_clk10_phase_voltage.html language=enus -->
## TOPIC 00012: niSync Adjust Clk10 Phase Voltage (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_adjust_clk10_phase_voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_adjust_clk10_phase_voltage.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Adjust Clk10 Phase Voltage (VI)

Installed With:

Sets the Clk10 phase voltage value to be written to the specified device's non-volatile onboard memory using an external calibration reference.

The value you enter in **new voltage** is written to the non-volatile onboard memory of the specified device and becomes the new calibration constant if you set **Action** of [niSync Close External Calibration](nisync_close_external_calibration.html) to Commit. You must use this VI in a session created with [niSync Initialize External Calibration](nisync_initialize_external_calibration.html).

The Clk10 phase voltage controls the phase between PXI_Clk10 and an external reference clock connected to ClkIn when the specified device is configured to route ClkIn to PXI_Clk10_In. This can be used to minimize the time between the rising edges of the reference clock and PXI_Clk10. You must connect an external calibration reference to the module in order to adjust the default Clk10 phase voltage.

|  | Note Use niSync Get Clk10 Phase Voltage to return the Clk10 phase voltage value currently stored in the device's non-volatile onboard memory. This VI does not immediately change the Clk10 phase voltage. Use the Clk10 Phase Adjust property of the niSync Property Node to immediately adjust the Clk10 phase voltage. |
| --- | --- |

[IMAGE alt='niSync Adjust Clk10 Phase Voltage' src='nisync_adjust_clk10_phase_voltage.gif']

|  | instrument handle specifies the session handle that you obtain from niSync Initialize External Calibration. The handle identifies the device to calibrate. |
| --- | --- |
|  | new voltage (0.00E+0) specifies the new Clk10 phase voltage value, in volts, to write to the non-volatile onboard memory of the instrument you are calibrating. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | instrument handle out returns the session handle that you obtained from niSync Initialize External Calibration. The handle identifies the device you have calibrated. |
|  | old voltage returns the Clk10 phase voltage value, in volts, that was last written to the specified device's non-volatile onboard memory. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_adjust_dds_start_pulse_phase_voltage.html language=enus -->
## TOPIC 00013: niSync Adjust DDS Start Pulse Phase Voltage (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_adjust_dds_start_pulse_phase_voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_adjust_dds_start_pulse_phase_voltage.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Adjust DDS Start Pulse Phase Voltage (VI)

Installed With:

Sets the DDS start pulse phase voltage to be written to the specified device's non-volatile onboard memory using an external calibration reference.

The value you enter in **new voltage** is written to the non-volatile onboard memory of the specified device and becomes the new calibration constant only if you set **Action** of [niSync Close External Calibration](nisync_close_external_calibration.html) to Commit. You must use this VI in a session created with [niSync Initialize External Calibration](nisync_initialize_external_calibration.html).

|  | Note Use niSync Get DDS Start Pulse Phase Voltage to return the DDS start pulse phase voltage currently stored on the device's onboard memory. This node does not immediately change the DDS start pulse phase voltage. Use the DDS Phase Adjust Voltage property of the niSync Property Node to immediately adjust the DDS start pulse phase voltage. |
| --- | --- |

[IMAGE alt='niSync Adjust DDS Start Pulse Phase Voltage' src='nisync_adjust_dds_start_pulse_phase_voltage.gif']

|  | instrument handle specifies the session handle that you obtain from niSync Initialize External Calibration. The handle identifies the device to calibrate. |
| --- | --- |
|  | new voltage (0.00E+0) specifies the new DDS start pulse phase voltage value, in volts, to write to the non-volatile onboard memory of the instrument you are calibrating. This value will only be written to the EEPROM if you set the action terminal of niSync Close External Calibration to Commit. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | instrument handle out returns the session handle that you obtained from niSync Initialize External Calibration. The handle identifies the device you have calibrated. |
|  | old voltage returns the DDS start pulse phase voltage, in volts, last written to the device's non-volatile onboard memory. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_adjust_oscillator_voltage.html language=enus -->
## TOPIC 00014: niSync Adjust Oscillator Voltage (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_adjust_oscillator_voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_adjust_oscillator_voltage.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Adjust Oscillator Voltage (VI)

Installed With:

Sets the oscillator voltage value to be written to the specified device's non-volatile onboard memory using an external calibration reference.

The oscillator voltage controls the frequency of the specified device's oscillator. The value you enter in **new voltage** is written to the non-volatile onboard memory of the specified device only if you set the **Action** parameter of [niSync Close External Calibration](nisync_close_external_calibration.html) to Commit. You must use this VI in a session created with [niSync Initialize External Calibration](nisync_initialize_external_calibration.html).

|  | Note Use niSync Get Oscillator Voltage to return the oscillator voltage value currently stored in the device's non-volatile onboard memory. This VI does not immediately change the oscillator voltage. Use the Oscillator Voltage property of the niSync Property Node to immediately adjust the oscillator voltage. |
| --- | --- |

[IMAGE alt='niSync Adjust Oscillator Voltage' src='nisync_adjust_oscillator_voltage.gif']

|  | instrument handle specifies the session handle that you obtain from niSync Initialize External Calibration. The handle identifies the device to calibrate. |
| --- | --- |
|  | new voltage (0.00E+0) specifies the value of the new oscillator voltage, in volts, to write to the device's non-volatile onboard memory. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | instrument handle out returns the session handle that you obtained from niSync Initialize External Calibration. The handle identifies the device you have calibrated. |
|  | old voltage returns the value of the oscillator voltage, in volts, last written to the device's non-volatile onboard memory. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_avail_timestamps.html language=enus -->
## TOPIC 00015: Available Time Stamps

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_avail_timestamps.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_avail_timestamps.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Available Time Stamps

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the number of timestamps available to read for the specified terminal.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information.You must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Stamps»Available Time Stamps

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_bmca_mode.html language=enus -->
## TOPIC 00016: BMCA Mode

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_bmca_mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_bmca_mode.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

BMCA Mode

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns which mode of the Best Master Clock algorithm (BMCA) to use for the time reference specified in Active Item.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information.You must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»BMCA Mode

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_clk_resolution.html language=enus -->
## TOPIC 00017: Clock Resolution

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_clk_resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_clk_resolution.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Clock Resolution

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the resolution, in nanoseconds, of the device's clock. The clock resolution represents the duration of a single tick of the clock.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information |
| --- | --- |

#### Property Node Path

niSync»Timing»Clock Resolution

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_clock_accuracy.html language=enus -->
## TOPIC 00018: 1588 Clock Accuracy

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_clock_accuracy.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_clock_accuracy.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

1588 Clock Accuracy

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the accuracy of the device's 1588 clock in comparison to the currently selected time reference.

|  | Note For Linux RT devices, you must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Clock Accuracy

#### Defined Values

| Unknown | 0 |
| --- | --- |
| Within25nsec | 1 |
| Within100nsec | 2 |
| Within250nsec | 3 |
| Within1usec | 4 |
| Within2500nsec | 5 |
| Within10usec | 6 |
| Within25usec | 7 |
| Within100usec | 8 |
| Within250usec | 9 |
| Within1msec | 10 |
| Within2500usec | 11 |
| Within10msec | 12 |
| Within25msec | 13 |
| Within100msec | 14 |
| Within250msec | 15 |
| Within1sec | 16 |
| Within10sec | 17 |
| GreaterThan10sec | 18 |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_clock_class.html language=enus -->
## TOPIC 00019: 1588 Clock Class

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_clock_class.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_clock_class.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

1588 Clock Class

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the traceability of the time or frequency distributed by the 1588 clock on the specified time reference.

|  | Note For Linux RT devices, you must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Clock Class

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_clock_id.html language=enus -->
## TOPIC 00020: 1588 Clock ID

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_clock_id.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_clock_id.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

1588 Clock ID

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns a string that represents the 64-bit Global Identifier (EUI-64) for the 1588 clock.

|  | Note For Linux RT devices, you must specify the Active Item that contains the time reference before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time References»1588»Clock ID

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_clock_state.html language=enus -->
## TOPIC 00021: 1588 Clock State

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_clock_state.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_clock_state.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

1588 Clock State

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the state of the 1588 clock. You can query this property to determine if this clock has reached a steady state before the application continues with other operations dependent on this clock, or to determine if an error occurred during synchronization.

|  | Note For Linux RT devices, you must specify the time reference using the Active Item property before you can call this property. This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

#### Defined Values

| Name | # | Description |
| --- | --- | --- |
| Not Defined | -1 | The clock is in an unknown state. |
| Initializing | 0 | The clock is in the process of starting. |
| Faulty | 1 | The clock is no longer synchronized with other 1588 devices. |
| Disabled | 2 | The clock is not active. |
| Listening | 3 | The clock is waiting to receive timestamps from the Master clock. |
| Pre-Master | 4 | The clock is preparing to enter the Master state. |
| Master | 5 | The clock is the master 1588 device from which all the slave devices get their concept of time. |
| Passive | 6 | The clock is not participating in PTP, but accepts timestamps from the Master device in order to determine when it should change states. |
| Uncalibrated | 7 | The clock is receiving timestamps from the master clock, but it is not yet synchronized to the master. |
| Slave | 8 | The clock is synchronized to the master 1588 clock. |
| Stopped | 9 | The clock is stopped. |

#### Property Node Path

niSync»Timing»Time Reference»1588»Clock State

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_frequency_traceable.html language=enus -->
## TOPIC 00022: Frequency Traceable

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_frequency_traceable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_frequency_traceable.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Frequency Traceable

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

A Boolean indicating whether the clock frequency can be traced.

|  | Note For Linux RT devices, you must specify the Active Item before you can call this property. This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Frequency Traceable

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_grandmaster_clock_accuracy.html language=enus -->
## TOPIC 00023: 1588 Grandmaster Clock Accuracy

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_grandmaster_clock_accuracy.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_grandmaster_clock_accuracy.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

1588 Grandmaster Clock Accuracy

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the accuracy of the 1588 grandmaster clock.

|  | Note For Linux RT devices, you must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Defined Values

| Unknown | 0 |
| --- | --- |
| Within25nsec | 1 |
| Within100nsec | 2 |
| Within250nsec | 3 |
| Within1usec | 4 |
| Within2500nsec | 5 |
| Within10usec | 6 |
| Within25usec | 7 |
| Within100usec | 8 |
| Within250usec | 9 |
| Within1msec | 10 |
| Within2500usec | 11 |
| Within10msec | 12 |
| Within25msec | 13 |
| Within100msec | 14 |
| Within250msec | 15 |
| Within1sec | 16 |
| Within10sec | 17 |
| GreaterThan10sec | 18 |

#### Property Node Path

niSync»Timing»Time Reference»1588»Grandmaster Clock Accuracy

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_grandmaster_clock_class.html language=enus -->
## TOPIC 00024: 1588 Grandmaster Clock Class

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_grandmaster_clock_class.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_grandmaster_clock_class.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

1588 Grandmaster Clock Class

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the traceability of the time or frequency distributed by the 1588 grandmaster clock.

|  | Note For Linux RT devices, you must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Grandmaster Clock Class

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_grandmaster_clock_id.html language=enus -->
## TOPIC 00025: 1588 Grandmaster Clock ID

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_grandmaster_clock_id.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_grandmaster_clock_id.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

1588 Grandmaster Clock ID

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns a string that represents the 64-bit Global Identifier (EUI-64) for the 1588 grandmaster clock.

|  | Note For Linux RT devices, you must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Grandmaster Clock ID

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_grandmaster_ip_address.html language=enus -->
## TOPIC 00026: Grandmaster IP Address

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_grandmaster_ip_address.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_grandmaster_ip_address.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Grandmaster IP Address

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the IP address of the 1588 grandmaster clock used by the time reference specified in Active Item.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties and VIs for more information.You must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Grandmaster IP Address

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_grandmaster_priority1.html language=enus -->
## TOPIC 00027: Grandmaster Priority1

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_grandmaster_priority1.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_grandmaster_priority1.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Grandmaster Priority1

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the 1st order priority assigned to the 1588 grandmaster clock. This property can range from 0 to 255. A lower value indicates a higher priority.

|  | Note For Linux RT devices, you must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Grandmaster Priority1

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_grandmaster_priority2.html language=enus -->
## TOPIC 00028: Grandmaster Priority2

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_grandmaster_priority2.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_grandmaster_priority2.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Grandmaster Priority2

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the 2nd order priority assigned to the 1588 grandmaster clock. This property can range from 0 to 255. A lower value increases the priority.

|  | Note For Linux RT devices, you must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Grandmaster Priority2

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_interface_name.html language=enus -->
## TOPIC 00029: Interface Name

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_interface_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_interface_name.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Interface Name

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the name of the network interface used by the time reference specified in Active Item.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information.You must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Interface Name

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_ip_address.html language=enus -->
## TOPIC 00030: IP Address

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_ip_address.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_ip_address.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

IP Address

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Returns the IP address assigned to the 1588 device associated with this session.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»IP Address

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_leap59.html language=enus -->
## TOPIC 00031: Leap59

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_leap59.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_leap59.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Leap59

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

A Boolean indicating whether the last minute of the current UTC day contains 59 seconds.

|  | Note For Linux RT devices, you must specify the Active Item before you can call this property. This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Leap59

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_leap61.html language=enus -->
## TOPIC 00032: Leap61

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_leap61.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_leap61.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Leap61

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

A Boolean indicating whether the last minute of the current UTC day contains 61 seconds.

|  | Note For Linux RT devices, you must specify the Active Item before you can call this property. This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Leap61

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_log_sync_interval.html language=enus -->
## TOPIC 00033: Log Sync Interval

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_log_sync_interval.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_log_sync_interval.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Log Sync Interval

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns the mean sync interval used by the 1588 clock. Use a smaller sync interval to make clocks respond more quickly to changes in the time reference. Use a larger sync interval to send packets less frequently and decrease network load.

The sync interval of the grandmaster clock becomes the sync interval for the entire PTP subdomain. Therefore, when setting this value, remember that it will be used only if the Best Master Clock (BMC) algorithm chooses the local clock to be the grandmaster.

|  | Note For Linux RT devices, you must specify the time reference using the Active Item property before you can call this property. This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

#### Defined Values

| 500 Milliseconds | -1 |
| --- | --- |
| 1 Second | 0 |
| 2 Seconds | 1 |

#### Property Node Path

niSync»Timing»Time Reference»1588»Log Sync Interval

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_mean_path_delay.html language=enus -->
## TOPIC 00034: Mean Path Delay

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_mean_path_delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_mean_path_delay.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Mean Path Delay

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the mean propagation delay, in seconds, between the 1588 clock associated with this session and the 1588 master clock. The mean propagation delay is the average amount of time it takes for a packet to reach a slave device from the 1588 master.

|  | Note For Linux RT devices, you must specify the Active Item before you can call this property. This property is not supported when you are using the IEEE 1588-2008 BC time reference type, as used in CompactDAQ Ethernet chassis. To verify the type, refer to the Time Reference Type property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Mean Path Delay

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_offset_scaled_log_variance.html language=enus -->
## TOPIC 00035: Offset Scaled Log Variance

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_offset_scaled_log_variance.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_offset_scaled_log_variance.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Offset Scaled Log Variance

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the log-scaled value representing the clock's precision.

|  | Note For Linux RT devices, you must specify the Active Item before you can call this property. This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Offset Scaled Log Variance

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_priority1.html language=enus -->
## TOPIC 00036: Priority1

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_priority1.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_priority1.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Priority1

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns the 1st order priority assigned to the 1588 clock. This property can range from 0 to 255. A lower value indicates a higher priority.

|  | Note For Linux RT devices, you must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Priority1

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_priority2.html language=enus -->
## TOPIC 00037: Priority2

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_priority2.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_priority2.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Priority2

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns the second order priority assigned to the 1588 clock. This property can range from 0 to 255. A lower value indicates a higher priority.

|  | Note For Linux RT devices, you must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Priority2

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_steps_to_grandmaster.html language=enus -->
## TOPIC 00038: Steps to Grandmaster

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_steps_to_grandmaster.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_steps_to_grandmaster.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Steps to Grandmaster

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the number of steps that the 1588 clock is away from the grandmaster.

|  | Note For Linux RT devices, you must specify the time reference using the Active Item property before you can call this property. This property is not supported when you are using the IEEE 1588-2008 BC time reference type, as used in CompactDAQ Ethernet chassis. To verify the type, refer to the Time Reference Type property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Steps to Grandmaster

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_time_source.html language=enus -->
## TOPIC 00039: Time Source

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_time_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_time_source.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Time Source

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

An integer enumeration indicating the clock's time source, as obtained from the leader clock.

|  | Note For Linux RT devices, you must specify the Active Item before you can call this property. This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Time Source

#### Defined Values

| Name | # |
| --- | --- |
| Unknown | 0 |
| AtomicClock | 1 |
| Gps | 2 |
| TerrestrialRadio | 3 |
| Ptp | 4 |
| Ntp | 5 |
| HandSet | 6 |
| Other | 7 |
| InternalOscillator | 8 |
| AlternatePTP* | 9 |
| Reserved* | 10 |

* Only available on Linux.

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_time_traceable.html language=enus -->
## TOPIC 00040: Time Traceable

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_time_traceable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_time_traceable.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Time Traceable

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

A Boolean indicating whether time can be traced.

|  | Note For Linux RT devices, you must specify the Active Item before you can call this property. This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»1588»Time Traceable

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_1588_timestamp_buf_size.html language=enus -->
## TOPIC 00041: Time Stamp Buffer Size

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_1588_timestamp_buf_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_1588_timestamp_buf_size.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Time Stamp Buffer Size

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns the software buffer size, in number of timestamps, for the specified terminal. The default is 1000.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information.You must specify the terminal using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Stamps»Time Stamp Buffer Size

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_8021as_as_capable.html language=enus -->
## TOPIC 00042: AS Capable

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_8021as_as_capable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_8021as_as_capable.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

AS Capable

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns whether the time reference specified in Active Item is capable of participating in the IEEE 802.1AS protocol. This value is TRUE only if this time-aware system and the time-aware system it is linked to can inter-operate with each other via the 802.1AS protocol.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information.You must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»802.1AS»AS Capable

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_8021as_clock_accuracy.html language=enus -->
## TOPIC 00043: Clock Accuracy

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_8021as_clock_accuracy.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_8021as_clock_accuracy.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Clock Accuracy

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the accuracy of the 802.1AS clock used by the time reference specified in Active Item.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information.You must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

| Value | Description |
| --- | --- |
| 32 | Within25nsec |
| 33 | Within100nsec |
| 34 | Within250nsec |
| 35 | Within1usec |
| 36 | Within2500nsec |
| 37 | Within10usec |
| 38 | Within25usec |
| 39 | Within100usec |
| 40 | Within250usec |
| 41 | Within1msec |
| 42 | Within2500usec |
| 43 | Within10msec |
| 44 | Within25msec |
| 45 | Within100msec |
| 46 | Within250msec |
| 47 | Within1sec |
| 48 | Within10sec |
| 49 | GreaterThan10sec |
| 254 | Unknown |

#### Property Node Path

niSync»Timing»Time Reference»802.1AS»Clock Accuracy

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_8021as_clock_class.html language=enus -->
## TOPIC 00044: Clock Class

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_8021as_clock_class.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_8021as_clock_class.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Clock Class

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the traceability of the time or frequency distributed by the 802.1AS clock used by the time reference specified in Active Item.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information.You must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

| Integer | Clock Class Specification |
| --- | --- |
| 0 | Reserved to enable compatibility with future versions. |
| 1—5 | Reserved |
| 6 | The clock is synchronized to a primary time reference. The distributed timescale is PTP. A clock in this class cannot be a slave to another clock in the domain. |
| 7 | The clock has previously been designated as Clock Class 6, but has lost the ability to synchronize to a primary time reference. A clock in this class is in holdover mode and operates within holdover specifications. The distributed timescale is PTP. A clock in this class cannot be a slave to another clock in the domain. |
| 8 | Reserved |
| 9—10 | Reserved to enable compatibility with future versions. |
| 11—12 | Reserved |
| 13 | The clock is synchronized to an application-specific time source. The distributed timescale is ARB. A clock in this class cannot be a slave to another clock in the domain. |
| 14 | The clock has previously been designated as Clock Class 13, but has lost the ability to synchronize to an application-specific time source. A clock in this class is in holdover mode and operates within holdover specifications. The distributed timescale is ARB. A clock in this class cannot be a slave to another clock in the domain. |
| 15—51 | Reserved |
| 52 | The clock is degradation alternative A for a Clock Class 7 clock that is not within holdover specification. A clock in this class cannot be a slave to another clock in the domain. |
| 53—57 | Reserved |
| 58 | The clock is degredation alternative A for a Clock Class 14 clock that is not within holdover specification. A clock in this class cannot be a slave to another clock in the domain. |
| 59—67 | Reserved |
| 68—122 | The clock uses an alternate PTP profile. |
| 123—127 | Reserved |
| 128—132 | Reserved |
| 133—170 | The clock uses an alternate PTP profile. |
| 171—186 | Reserved |
| 187 | The clock is degredation alternative B for a Clock Class 7 clock that is not within holdover specification. A clock in this class can be a slave to another clock in the domain. |
| 188—192 | Reserved |
| 193 | The clock is degredation alternative B for a Clock Class 14 clock that is not within holdover specification. A clock of this class can be a slave to another clock in the domain. |
| 194—215 | Reserved |
| 216—232 | The clock uses an alternate PTP profile. |
| 233—247 | Reserved |
| 248 | The default Clock Class. This class is used if none of the other class definitions apply. |
| 249—250 | Reserved |
| 251 | Reserved for version 1 compatibility. |
| 252—254 | Reserved |
| 255 | The clock is a slave-only clock. |

#### Property Node Path

niSync»Timing»Time Reference»802.1AS»Clock Class

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_8021as_grandmaster_clock_accuracy.html language=enus -->
## TOPIC 00045: Grandmaster Clock Accuracy

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_8021as_grandmaster_clock_accuracy.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_8021as_grandmaster_clock_accuracy.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Grandmaster Clock Accuracy

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the accuracy of the 802.1AS grandmaster clock used by the time reference specified in Active Item.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information.You must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

| Value | Description |
| --- | --- |
| 0 | Unknown |
| 1 | Within25nsec |
| 2 | Within100nsec |
| 3 | Within250nsec |
| 4 | Within1usec |
| 5 | Within2500nsec |
| 6 | Within10usec |
| 7 | Within25usec |
| 8 | Within100usec |
| 9 | Within250usec |
| 10 | Within1msec |
| 11 | Within2500usec |
| 12 | Within10msec |
| 13 | Within25msec |
| 14 | Within100msec |
| 15 | Within250msec |
| 16 | Within1sec |
| 17 | Within10sec |
| 18 | GreaterThan10sec |

#### Property Node Path

niSync»Timing»Time Reference»802.1AS»Grandmaster Clock Accuracy

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_8021as_log_sync_interval.html language=enus -->
## TOPIC 00046: Log Sync Interval

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_8021as_log_sync_interval.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_8021as_log_sync_interval.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Log Sync Interval

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns the mean sync interval used by the 802.1AS clock in the time reference specified by Active Item. This value will be used only if the Best Master Clock algorithm (BMCA) chooses the local clock to be the grandmaster. The default is 0. This value is the logarithm to the base 2.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information.You must specify the time reference specified by the Active Item property before you can call this property. |
| --- | --- |

| Value | Description |
| --- | --- |
| -3 | 125 milliseconds |
| -2 | 250 milliseconds |
| -1 | 500 milliseconds |
| 0 | 1 second |
| 1 | 2 seconds |

#### Property Node Path

niSync»Timing»Time Reference»802.1AS»Log Sync Interval

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_active_item.html language=enus -->
## TOPIC 00047: Active Item

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_active_item.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_active_item.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Active Item

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | WO | N/A | None | None |

#### Description

Specifies the time reference or terminal used to access all subsequent properties in this instance of the property node. You must specify an Active Item for properties that require it.

#### Property Node Path

niSync»Active Item

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_clk10_phase_adjust.html language=enus -->
## TOPIC 00048: Clk10 Phase Adjust

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_clk10_phase_adjust.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_clk10_phase_adjust.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Clk10 Phase Adjust

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns the phase voltage between an external clock and PXI_Clk10 when you are using the PLL circuit to lock PXI_CLK10 to an external reference clock. You can minimize the time between rising edges of PXI_CLK10 and the external reference clock using this parameter.

#### Property Node Path

niSync»Calibration Properties»Clk10 Phase Adjust

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_clkin_attenuation_disable.html language=enus -->
## TOPIC 00049: Disable ClkIn Attenuation

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_clkin_attenuation_disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_clkin_attenuation_disable.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Disable ClkIn Attenuation

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies whether or not to attenuate the signal at ClkIn. Setting this property to TRUE disables the ClkIn attenuation.

#### Property Node Path

niSync»Clk Properties»Disable ClkIn Attenuation

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_clkin_pll_freq.html language=enus -->
## TOPIC 00050: PLL Frequency

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_clkin_pll_freq.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_clkin_pll_freq.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PLL Frequency

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns the frequency of the clock the PLL circuit should lock to. Refer to your hardware manual to determine the specific frequency range the device's PLL circuit can lock to.

#### Property Node Path

niSync»Clk Properties»PLL Frequency

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_clkin_pll_locked.html language=enus -->
## TOPIC 00051: PLL Locked?

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_clkin_pll_locked.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_clkin_pll_locked.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PLL Locked?

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns whether or not the PLL circuit is locked to the external reference clock. This property returns TRUE when the PLL is locked.

#### Property Node Path

niSync»Clk Properties»PLL Locked?

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_clkin_use_pll.html language=enus -->
## TOPIC 00052: Use PLL?

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_clkin_use_pll.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_clkin_use_pll.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Use PLL?

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns whether or not the connection between ClkIn and PXI_Clk10 should use the PLL circuit. If this parameter is set to TRUE, the PLL circuit will be used to lock to the frequency of the external clock at ClkIn when connecting to PXI_CLK10. You must set this property before connecting the external clock to PXI_Clk10_In.

#### Property Node Path

niSync»Clk Properties»Use PLL?

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_clkout_gain_enable.html language=enus -->
## TOPIC 00053: ClkOut Gain Enable

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_clkout_gain_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_clkout_gain_enable.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

ClkOut Gain Enable

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Set this parameter to TRUE to increase the amplitude of the ClkOut terminal from 1 peak-to-peak volt to 2.5 peak-to-peak volts. Enable this parameter if you are distributing a clock between chassis to give the clock enough gain to reach its destination. Set the parameter to FALSE to return the amplitude to 1 peak-to-peak volt.

#### Property Node Path

niSync»Clk Properties»ClkOut Gain Enable

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_oscillator_voltage.html language=enus -->
## TOPIC 00054: Oscillator Voltage

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_oscillator_voltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_oscillator_voltage.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Oscillator Voltage

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns the tuning voltage for the selected device's oscillator. You can vary the oscillator frequency over a small range (between 0 and 3 volts). The tuning voltage adjusts the output frequency.

#### Property Node Path

niSync»Calibration Properties»Oscillator Voltage

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_pfi0_10kohm_enable.html language=enus -->
## TOPIC 00055: PFI0 10kOhm Termination Enable

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_pfi0_10kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_pfi0_10kohm_enable.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PFI0 10kOhm Termination Enable

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI0 terminal should be terminated with 10 k[IMAGE alt='Omega' src='omega2.gif'] impedance.

#### Property Node Path

niSync»Calibration Properties»PFI0 10kOhm Termination Enable

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_pfi0_1kohm_enable.html language=enus -->
## TOPIC 00056: PFI0 1kOhm Termination Enable

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_pfi0_1kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_pfi0_1kohm_enable.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PFI0 1kOhm Termination Enable

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI0 terminal should be terminated with 1 k[IMAGE alt='Omega' src='omega2.gif'] impedance.

#### Property Node Path

niSync»Calibration Properties»PFI0 1kOhm Termination Enable

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_pfi0_threshold.html language=enus -->
## TOPIC 00057: PFI0 Threshold

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_pfi0_threshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_pfi0_threshold.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PFI0 Threshold

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns the voltage threshold, in volts, for the PFI0 terminal of the associated device.

#### Property Node Path

niSync»Calibration Properties»PFI0 Threshold

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_pfi1_10kohm_enable.html language=enus -->
## TOPIC 00058: PFI1 10kOhm Termination Enable

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_pfi1_10kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_pfi1_10kohm_enable.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PFI1 10kOhm Termination Enable

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI1 terminal should be terminated with 10 k[IMAGE alt='Omega' src='omega2.gif'] impedance.

#### Property Node Path

niSync»Calibration Properties»PFI1 10kOhm Termination Enable

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_pfi1_1kohm_enable.html language=enus -->
## TOPIC 00059: PFI1 1kOhm Termination Enable

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_pfi1_1kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_pfi1_1kohm_enable.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PFI1 1kOhm Termination Enable

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI1 terminal should be terminated with 1 k[IMAGE alt='Omega' src='omega2.gif'] impedance.

#### Property Node Path

niSync»Calibration Properties»PFI1 1kOhm Termination Enable

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_pfi1_threshold.html language=enus -->
## TOPIC 00060: PFI1 Threshold

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_pfi1_threshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_pfi1_threshold.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PFI1 Threshold

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns the voltage threshold, in volts, of the PFI1 terminal of the associated device.

#### Property Node Path

niSync»Calibration Properties»PFI1 Threshold

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_pfi2_10kohm_enable.html language=enus -->
## TOPIC 00061: PFI2 10kOhm Termination Enable

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_pfi2_10kohm_enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_pfi2_10kohm_enable.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PFI2 10kOhm Termination Enable

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies whether or not the PFI2 terminal should be terminated with 10 k[IMAGE alt='Omega' src='omega2.gif'] impedance.

#### Property Node Path

niSync»Calibration Properties»PFI2 10kOhm Termination Enable

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_serial_num.html language=enus -->
## TOPIC 00062: Serial Number

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_serial_num.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_serial_num.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Serial Number

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the serial number of the connected NI-Sync device.

#### Property Node Path

niSync»Interface Properties»Serial Number

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_sync_clk_div1.html language=enus -->
## TOPIC 00063: Clock Divisor 1

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_sync_clk_div1.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_sync_clk_div1.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Clock Divisor 1

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns the value of the first clock divisor. Use this number to divide the full-speed synchronization clock and produce Divided Clock 1. The value must be a power of two between 2 and 512.

#### Property Node Path

niSync»Synchronization Clock Properties»Clock Divisor 1

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_terminal_state_pfilvds.html language=enus -->
## TOPIC 00064: PFI_LVDS Line State

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_terminal_state_pfilvds.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_terminal_state_pfilvds.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PFI_LVDS Line State

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Indicates the current state of a chassis' PFI_LVDS terminals by returning a bitmap represented by a 32-bit integer. In binary, bit 0 corresponds to PFI_LVDS0, bit 1 corresponds to PFI_LVDS1, etc.

Refer to [Displaying the State of a Trigger Line](ni.com/docs/csh?context=ni-sync_nisynclv_displaylinestate) to display the PFI_LVDS line state with a Boolean array on the front panel.

|  | Note Terminal state information is valid only for terminals with I/O (timestamping, clocks, or future time events) enabled. |
| --- | --- |

#### Property Node Path

niSync»Trigger State Properties»PFI_LVDS Line State

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_terminal_state_pxiedstarc.html language=enus -->
## TOPIC 00065: PXIe_DStarC Line State

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_terminal_state_pxiedstarc.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_terminal_state_pxiedstarc.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PXIe_DStarC Line State

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Indicates the current state of a chassis' PXIe_DStarC lines by returning a bitmap represented by a 32-bit integer. In binary, bit 0 corresponds to PXIe_DStarC0, bit 1 corresponds to PXIe_DStarC1, and so on.

Refer to [Displaying the State of a Trigger Line](ni.com/docs/csh?context=ni-sync_nisynclv_displaylinestate) to display the PXIe_DStarC line state with a Boolean array on the front panel.

|  | NoteTerminal state information is valid only for terminals with I/O (timestamping, clocks, or future time events) enabled. PXIe_DStarC lines default to the logic high state. |
| --- | --- |

#### Property Node Path

niSync»Trigger State Properties»PXIe_DStarC Line State

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_terminal_state_pxistar.html language=enus -->
## TOPIC 00066: PXI_Star Line State

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_terminal_state_pxistar.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_terminal_state_pxistar.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PXI_Star Line State

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Indicates the current state of a chassis' PXI_Star lines by returning a bitmap represented by a 32-bit integer. In binary, bit 0 corresponds to PXI_Star0, bit 1 corresponds to PXI_Star1, and so on.

Refer to [Displaying the State of a Trigger Line](ni.com/docs/csh?context=ni-sync_nisynclv_displaylinestate) to display the PXI_Star line state with a Boolean array on the front panel.

|  | NoteTerminal state information is valid only for terminals with I/O (timestamping, clocks, or future time events) enabled. PXI_Star lines default to the logic high state. |
| --- | --- |

#### Property Node Path

niSync»Trigger State Properties»PXI_Star Line State

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_terminal_state_pxistarperipheral.html language=enus -->
## TOPIC 00067: PXI_Star Peripheral Line State

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_terminal_state_pxistarperipheral.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_terminal_state_pxistarperipheral.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PXI_Star Peripheral Line State

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the logical state of the PXI_Star peripheral terminal. This value is only valid when the board is in a peripheral slot.

|  | Note Terminal state information is valid only for terminals with I/O (timestamping, clocks, or future time events) enabled. |
| --- | --- |

#### Property Node Path

niSync»Trigger State Properties»PXI_Star Peripheral Line State

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_terminal_state_pxitrig.html language=enus -->
## TOPIC 00068: PXI_Trig Line State

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_terminal_state_pxitrig.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_terminal_state_pxitrig.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

PXI_Trig Line State

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Indicates the current state of a chassis' PXI_Trig lines by returning a bitmap represented by a 32-bit integer. In binary, bit 0 corresponds to PXI_Trig0, bit 1 corresponds to PXI_Trig1, and so on.

Refer to [Displaying the State of a Trigger Line](ni.com/docs/csh?context=ni-sync_nisynclv_displaylinestate) to display the PXI_Trig line state with a Boolean array on the front panel.

|  | NoteTerminal state information is valid only for terminals with I/O (timestamping, clocks, or future time events) enabled. PXI_Trig lines default to the logic high state. |
| --- | --- |

#### Property Node Path

niSync»Trigger State Properties»PXI_Trig Line State

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_timeref_correction.html language=enus -->
## TOPIC 00069: Time Reference Correction

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_timeref_correction.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_timeref_correction.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Time Reference Correction

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns a manual correction, in seconds, to apply to the specified module's board time. Use this property to calibrate the board time manually to achieve better synchronization with a selected time reference.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference Correction

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_timeref_enabled.html language=enus -->
## TOPIC 00070: Time Reference Enabled

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_timeref_enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_timeref_enabled.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Time Reference Enabled

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | R/W | N/A | None | None |

#### Description

Specifies or returns whether the time reference connected to the Active Item property is enabled.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more informationYou must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»Time Reference Enabled

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_timeref_is_selected.html language=enus -->
## TOPIC 00071: Is Time Reference Selected

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_timeref_is_selected.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_timeref_is_selected.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Is Time Reference Selected

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns whether the time reference specified in the Active Item property is the selected time reference for the device.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more informationYou must specify the time reference using the Active Item property before you can call this property. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»Is Time Reference Selected

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_timeref_last_sync_id.html language=enus -->
## TOPIC 00072: Last Synchronization ID

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_timeref_last_sync_id.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_timeref_last_sync_id.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Last Synchronization ID

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Increments when a synchronization message is received from the current time reference.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more informationSynchronization messages are not received if the time reference is set to Free Running, or if the time reference is set to 1588 and the 1588 clock is a master. |
| --- | --- |

#### Property Node Path

niSync»Timing»Last Synchronization ID

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_timeref_offset_ns.html language=enus -->
## TOPIC 00073: Offset from Time Reference (ns)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_timeref_offset_ns.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_timeref_offset_ns.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Offset from Time Reference (ns)

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the calculated offset, in nanoseconds, between the specified device's clock and its selected time reference. Use this property to determine when the local clock is sufficiently synchronized with the selected time reference to continue operations.

#### Property Node Path

niSync»Timing»Offset from Time Reference (ns)

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_timeref_present.html language=enus -->
## TOPIC 00074: Is Time Reference Present

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_timeref_present.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_timeref_present.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Is Time Reference Present

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns TRUE if the selected time reference is currently providing a valid time signal. You must set an external time reference for this parameter to function.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

#### Property Node Path

niSync»Timing»Time Reference»Is Time Reference Present

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_timeref_selected_name.html language=enus -->
## TOPIC 00075: Selected Time Reference Name

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_timeref_selected_name.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_timeref_selected_name.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Selected Time Reference Name

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the name of the selected time reference.

#### Property Node Path

niSync»Timing»Selected Time Reference Name

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_attr_timeref_selected_type.html language=enus -->
## TOPIC 00076: Selected Time Reference Type

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_attr_timeref_selected_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_attr_timeref_selected_type.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

Selected Time Reference Type

| DataType | Access | Applies to | Coercion | High-Level VIs |
| --- | --- | --- | --- | --- |
|  | RO | N/A | None | None |

#### Description

Returns the time synchronization protocol (1588, EtherCAT, GPS, etc.) being used by the selected time reference of the specified device.

#### Defined Values

| Description | Value |
| --- | --- |
| IEEE 1588-2008 | A network-based time synchronization protocol (also referred to as PTP) that synchronizes devices to a single grandmaster clock. Each IEEE 1588-2008 time reference instance is associated with a single network interface on the device and can either be a slave to the network's grandmaster, or the grandmaster to a network of devices. |
| IEEE 1588-2008 BC | Similar to the IEEE 1588-2008 protocol, except each instance of the IEEE 1588-2008 BC (boundary clock) time reference is associated with multiple ports, typically on a device that acts as a network switch. |
| IEEE 802.1AS-2011 | A network-based time synchronization protocol similar to IEEE 1588-2008, but optimized for time-sensitive applications. IEEE 802.1AS-2011 also provides fewer configuration options and requires IEEE 802.1AS-compatible network infrastructure. Each IEEE 802.1AS-2011 time reference instance is associated with a single network interface on the device and can either be a slave to the network's grandmaster or the grandmaster to a network of devices. |
| IEEE 802.1AS-2011 TAB | Similar to the IEEE 802.1AS-2011 protocol, except each IEEE 802.1AS-2011 TAB (time-aware bridge) time reference instance is associated with multiple ports, typically on a device that acts as a network switch. |
| IRIG-B | An encoded TTL signal that carries the absolute time, including the day, year, and straight binary seconds. IRIG-B is similar to a pulse per second (PPS) signal, but instead of outputting a single uniform pulse every second, IRIG-B sends coded bits that make up a one-second long data frame, and it repeats or re-synchronizes every second. |

|  | Note The values defined above are not a complete list of time reference types. Other time reference types can be installed by other NI software. |
| --- | --- |

#### Property Node Path

niSync»Timing»Selected Time Reference Type

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_clear_clock.html language=enus -->
## TOPIC 00077: niSync Clear Clock (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_clear_clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_clear_clock.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Clear Clock (VI)

Installed With:

Frees a resource that contains a clock generated by [niSync Create Clock](nisync_create_clock.html). Once you clear the clock, you can use the associated terminal for other operations.

|  | Note This function is supported only on certain targets. Refer to Target Support for Timing Properties and VIs to determine whether or not this VI is supported on your chosen target. |
| --- | --- |

[IMAGE alt='niSync Clear Clock' src='nisync_clear_clock.gif']

|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |
| --- | --- |
|  | terminal specifies the line that contains the generated clock to clear. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. |
|  | instrument handle out returns the instrument handle that you obtain from niSync Initialize. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_clear_future_time_events.html language=enus -->
## TOPIC 00078: niSync Clear Future Time Events (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_clear_future_time_events.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_clear_future_time_events.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Clear Future Time Events (VI)

Installed With:

Frees the specified terminal of any future time events previously created with [niSync Create Future Time Event](nisync_create_future_time_event.html).

Once you invoke this VI, you can use the associated terminal for other operations. The specified terminal is tri-stated and the resource is freed.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

[IMAGE alt='niSync Clear Future Time Events' src='nisync_clear_future_time_events.gif']

|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |
| --- | --- |
|  | terminal specifies the terminal from which to clear future time events. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. |
|  | instrument handle out returns the instrument handle that you obtain from niSync Initialize. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_close.html language=enus -->
## TOPIC 00079: niSync Close (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_close.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_close.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Close (VI)

Installed With:

Ends an NI-Sync instrument driver session and frees the device for other operations.

You must use this VI any time you begin a session using [niSync Initialize](nisync_initialize.html). This VI clears or disables any generated clocks, future time events, and timestamp triggers on the associated device.

|  | Note Calling this VI will not un-route any clock or trigger terminals that are connected while the session is open. You must close clock terminals using niSync Disconnect Clock Terminals, and you must close trigger terminals using niSync Disconnect Trigger Terminals or niSync Disconnect Software Trigger. You can also close these terminal routes by resetting the module. |
| --- | --- |

[IMAGE alt='niSync Close' src='nisync_close.gif']

|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_close_external_calibration.html language=enus -->
## TOPIC 00080: niSync Close External Calibration (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_close_external_calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_close_external_calibration.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Close External Calibration (VI)

Installed With:

Ends an external calibration session you began using [niSync Initialize External Calibration](nisync_initialize_external_calibration.html).

When you set new calibration constants using an external calibration VI such as [niSync Adjust Clk10 Phase Voltage](nisync_adjust_clk10_phase_voltage.html), [niSync Adjust DDS Start Pulse Phase Voltage](nisync_adjust_dds_start_pulse_phase_voltage.html), or [niSync Adjust Oscillator Voltage](nisync_adjust_oscillator_voltage.html), you *must* set the **action** parameter to Commit to write the new calibration constants to the device's EEPROM. If you do not set **action** to Commit, changes made using external calibration VIs will not be applied.

|  | Note After invoking niSync Close External Calibration, you cannot use the the NI-Sync session handle again until you invoke niSync Initialize or niSync Initialize External Calibration. If you invoke this VI with action set to Commit, the VI updates the external calibration date stored in the device's non-volatile onboard memory, even if no calibration constants were changed. |
| --- | --- |

[IMAGE alt='niSync Close External Calibration' src='nisync_close_external_calibration.gif']

|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |
| --- | --- |
|  | action (Abort) specifies whether or not to write the external calibration constants set using an external calibration VI to the device's non-volatile onboard memory. Valid values: Abort Discards any changes made with an external calibration VI and maintains calibration constants at their original values. Commit Writes any changes made with an external calibration VI to the device's non-volatile onboard memory. These are the new default calibration constants for the device. |
| Abort | Discards any changes made with an external calibration VI and maintains calibration constants at their original values. |
| Commit | Writes any changes made with an external calibration VI to the device's non-volatile onboard memory. These are the new default calibration constants for the device. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_configure_fpga.html language=enus -->
## TOPIC 00081: niSync Configure FPGA (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_configure_fpga.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_configure_fpga.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Configure FPGA (VI)

Installed With:

Reprograms the FPGA circuits on the specified device using an alternate bitstream file.

|  | Caution Use this VI carefully: it is an advanced operation that requires in-depth knowledge of your hardware. |
| --- | --- |

[IMAGE alt='niSync Configure FPGA' src='nisync_configure_fpga.gif']

|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |
| --- | --- |
|  | fpga program path specifies the absolute path to an FPGA bitstream file on disk. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | instrument handle out returns the instrument handle that you obtain from niSync Initialize. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_connect_clock_terminals.html language=enus -->
## TOPIC 00082: niSync Connect Clock Terminals (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_connect_clock_terminals.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_connect_clock_terminals.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Connect Clock Terminals (VI)

Installed With:

Connects a source clock terminal to a destination clock terminal.

A clock terminal connection is characterized by its source terminal and destination terminal. Refer to [Clock Terminal Connections](ni.com/docs/csh?context=ni-sync_nisynclv_clockterminalconnections) to choose a compatible clock source and destination terminal.

[IMAGE alt='niSync Connect Clock Terminals' src='nisync_connect_clock_terminals.gif']

|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |  |  |
| --- | --- | --- | --- |
|  | source terminal specifies the source terminal of the clock you would like to connect. Valid values: ClkIn PXI_Clk10 Oscillator DDS Clock PFI_LVDS<n> PXIe_DStarC<n> PXIe_DStarA |  |  |
| ClkIn | PXI_Clk10 | Oscillator | DDS Clock |
| PFI_LVDS<n> | PXIe_DStarC<n> | PXIe_DStarA |  |
|  | destination terminal specifies where to route the clock signal specified in the source terminal. Valid values: PXI_Clk10_In ClkOut BoardClk PFI_LVDS<n> PXIe_DStarA<n> |  |  |
| PXI_Clk10_In | ClkOut | BoardClk |  |
| PFI_LVDS<n> | PXIe_DStarA<n> |  |  |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |  |
|  | instrument handle out returns the instrument handle that you obtain from niSync Initialize. |  |  |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |  |  |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_connect_software_trigger.html language=enus -->
## TOPIC 00083: niSync Connect Software Trigger (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_connect_software_trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_connect_software_trigger.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Connect Software Trigger (VI)

Installed With:

Connects the global software trigger to a destination trigger terminal.

Once you connect the global software trigger, you can fire the trigger using [niSync Send Software Trigger](nisync_send_software_trigger.html).

|  | Note The destination terminal you specify in this VI determines the full-speed synchronization clock used by the global software trigger. PFI and PFI_LVDS lines are in the front trigger zone, and PXI_Trig, PXI_Star, and PXIe_DStarB lines are in the rear trigger zone. You can select the source of the synchronization clock for a given trigger zone and adjust the speed of the divided clocks with the niSync Property Node. |
| --- | --- |

This VI also allows you to modify the signal at the destination terminal in multiple ways:

- Invert the signal so that the rising edges become the falling edges and vice versa.
- Synchronize the signal to the rising or falling edge of the synchronization clock.
- Delay the signal by up to 15 synchronization clock cycles.

[IMAGE alt='niSync Connect Software Trigger' src='nisync_connect_software_trigger.gif']

|  | update edge (Rising Edge) specifies on which update edge of the synchronization clock to propagate the global software trigger: Valid values: Rising Edge Propagates the global software trigger when the digital signal of the synchronization clock transitions from low to high, i.e. the rising edge. Falling Edge Propagates the global software trigger when the digital signal of the synchronization clock transitions from high to low, i.e. the falling edge. |  |
| --- | --- | --- |
| Rising Edge | Propagates the global software trigger when the digital signal of the synchronization clock transitions from low to high, i.e. the rising edge. |  |
| Falling Edge | Propagates the global software trigger when the digital signal of the synchronization clock transitions from high to low, i.e. the falling edge. |  |
|  | synchronization clock specifies whether to use the full-speed or a divided synchronization clock to control when the global software trigger fires. The global software trigger will be synchronized with the rising or falling edge of the clock you select in this terminal. Note Asynchronous connections are not valid for software trigger terminal connections. Valid values: Full Speed Clock Uses the full speed frequency of the synchronization clock to synchronize the trigger. Divided Clock 1 Divides the synchronization clock by the value specified in the Clock Divisor 1 parameter of the niSync Property Node and uses the frequency of the divided clock to synchronize the trigger. Divided Clock 2 Divides the synchronization clock by the value specified in the Clock Divisor 2 parameter of the niSync Property Node and uses the frequency of the divided clock to synchronize the trigger. |  |
|  | Note Asynchronous connections are not valid for software trigger terminal connections. |  |
| Full Speed Clock | Uses the full speed frequency of the synchronization clock to synchronize the trigger. |  |
| Divided Clock 1 | Divides the synchronization clock by the value specified in the Clock Divisor 1 parameter of the niSync Property Node and uses the frequency of the divided clock to synchronize the trigger. |  |
| Divided Clock 2 | Divides the synchronization clock by the value specified in the Clock Divisor 2 parameter of the niSync Property Node and uses the frequency of the divided clock to synchronize the trigger. |  |
|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |  |
|  | source terminal specifies the source software trigger terminal to connect to the destination terminal. The only acceptable value is Global Software Trigger. |  |
|  | destination terminal specifies the terminal where the Global Software Trigger will fire. Valid values: PXI_Trig<n> PXI_Star<n> PFI<n> PFI_LVDS<n> PXIe_DStarB<n> PXIe_DStarC |  |
| PXI_Trig<n> | PXI_Star<n> | PFI<n> |
| PFI_LVDS<n> | PXIe_DStarB<n> | PXIe_DStarC |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | invert specifies whether or not to invert the digital signal of the Global Software Trigger when it reaches the destination terminal: Don't Invert Signal Keeps the digital signal of the Global Software Trigger in its original format. Invert Signal Inverts the digital signal of the Global Software Trigger so that its rising edges become its falling edges, and vice versa. |  |
| Don't Invert Signal | Keeps the digital signal of the Global Software Trigger in its original format. |  |
| Invert Signal | Inverts the digital signal of the Global Software Trigger so that its rising edges become its falling edges, and vice versa. |  |
|  | delay (0.00 seconds) specifies the amount of time, in seconds, to delay the global software trigger pulse. The delay must be a multiple of the synchronization clock period. The global software trigger can be delayed up to 15 clock cycles for each route. Note This input is not supported on the PXIe-6674T. |  |
|  | Note This input is not supported on the PXIe-6674T. |  |
|  | instrument handle out returns the instrument handle that you obtain from niSync Initialize. |  |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |  |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_create_clock.html language=enus -->
## TOPIC 00084: niSync Create Clock (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_create_clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_create_clock.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Create Clock (VI)

Installed With:

Generates a clock synchronized to the board time of the module you specify with **instrument handle**. Once you generate the clock in the specified terminal, you cannot use that terminal for other operations until you clear the clock with [niSync Clear Clock](nisync_clear_clock.html) or close the session with [niSync Close](nisync_close.html).

When you invoke this VI, the digital signal on the specified terminal is driven low until the clock starts. After you create the clock, you can route it to other modules and devices using [niSync Connect Clock Terminals](nisync_connect_clock_terminals.html). Depending on the instance you select, you can modify the clock's duty cycle, number of ticks, or the frequency at which it runs.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

#### niSync Create Clock (Time)

When you create a clock using this instance, you can specify how long the clock runs at a high logic level and how long it runs at a low logic level.

[IMAGE alt='niSync Create Clock (Time)' src='nisync_create_clock_(time).gif']

|  | low time specifies, in seconds, how long you want the generated clock to run at the low logic state. Note Because you can only generate clocks on exact multiples of clock ticks, the requested low time and the actual clock low time may differ slightly. You can display the actual low time of the generated clock by wiring an indicator to the coerced low time terminal. |
| --- | --- |
|  | Note Because you can only generate clocks on exact multiples of clock ticks, the requested low time and the actual clock low time may differ slightly. You can display the actual low time of the generated clock by wiring an indicator to the coerced low time terminal. |
|  | high time specifies, in seconds, how long you want the generated clock to run at the high logic state. Note Because you can only generate clocks on exact multiples of clock ticks, the high time you request and the actual high time may differ slightly. You can display the actual high time of the generated clock by wiring an indicator to the coerced high time terminal. |
|  | Note Because you can only generate clocks on exact multiples of clock ticks, the high time you request and the actual high time may differ slightly. You can display the actual high time of the generated clock by wiring an indicator to the coerced high time terminal. |
|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |
|  | terminal specifies the line you would like to generate the clock on. You cannot use this terminal for other operations until you clear the generated clock using niSync Clear Clock or you close the session with niSync Close. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | start time specifies when to start the generated clock. This time is synchronized with the board time of the module you use to create the clock. The default value is immediate, which generates the clock as soon as the VI is invoked. |
|  | stop time specifies when to stop the generated clock. This time is synchronized with the board time of the module you use to create the clock. The default value is never, in which case the clock will not stop until you invoke niSync Clear Clock or close the session. |
|  | instrument handle out returns the instrument handle that you obtain from niSync Initialize. |
|  | coerced low time returns the actual duration, in seconds, of the generated clock's logic low state. |
|  | coerced high time returns the actual duration, in seconds, of the generated clock's logic high state. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

#### niSync Create Clock (Ticks)

Using this instance, you can generate a clock that runs for a specified number of high and low ticks every cycle.

[IMAGE alt='niSync Create Clock (Ticks)' src='nisync_create_clock_(ticks).gif']

|  | low ticks specifies the number of ticks the generated clock should spend in the low logic state. You can view the length of a tick using the Clock Resolution parameter of the niSync Property Node. |
| --- | --- |
|  | high ticks specifies the number of ticks the generated clock should spend in the high logic state. You can view the length of a tick using the Clock Resolution parameter in the niSync Property Node. |
|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |
|  | terminal specifies the line you would like to generate the clock on. You cannot use this terminal for other operations until you clear the generated clock using niSync Clear Clock or you close the session with niSync Close. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | start time specifies when to start the generated clock. This time is synchronized with the board time of the module you use to create the clock. The default value is immediate, which generates the clock as soon as the VI is invoked. |
|  | stop time specifies when to stop the generated clock. This time is synchronized with the board time of the module you use to create the clock. The default value is never, in which case the clock will not stop until you invoke niSync Clear Clock or close the session. |
|  | instrument handle out returns the instrument handle that you obtain from niSync Initialize. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

#### niSync Create Clock (Frequency)

Using this instance, you can generate a clock that runs at a custom frequency and duty cycle.

[IMAGE alt='niSync Create Clock (Frequency)' src='nisync_create_clock_(frequency).gif']

|  | duty cycle specifies the desired duty cycle—the ratio of high ticks to low ticks—of the generated clock. Note Because you can only generate clocks on exact multiples of clock ticks, the duty cycle you request and the actual duty cycle may differ slightly. You can display the actual duty cycle of the generated clock by wiring an indicator to the coerced duty cycle terminal. |
| --- | --- |
|  | Note Because you can only generate clocks on exact multiples of clock ticks, the duty cycle you request and the actual duty cycle may differ slightly. You can display the actual duty cycle of the generated clock by wiring an indicator to the coerced duty cycle terminal. |
|  | frequency specifies the desired frequency of the generated clock. Note Because you can only generate clocks on exact multiples of clock ticks, the frequency you request and the actual clock frequency may differ slightly. You can display the actual frequency of the generated clock by wiring an indicator to the coerced frequency terminal. |
|  | Note Because you can only generate clocks on exact multiples of clock ticks, the frequency you request and the actual clock frequency may differ slightly. You can display the actual frequency of the generated clock by wiring an indicator to the coerced frequency terminal. |
|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |
|  | terminal specifies the line you would like to generate the clock on. You cannot use this terminal for other operations until you clear the generated clock using niSync Clear Clock or you close the session with niSync Close. |
|  | start time specifies when to start the generated clock. This time is synchronized with the board time of the module you use to create the clock. The default value is immediate, which generates the clock as soon as the VI is invoked. |
|  | stop time specifies when to stop the generated clock. This time is synchronized with the board time of the module you use to create the clock. The default value is never, in which case the clock will not stop until you invoke niSync Clear Clock or close the session. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | instrument handle out returns the instrument handle that you obtain from niSync Initialize. |
|  | coerced frequency returns the actual frequency of the generated clock. |
|  | coerced duty cycle returns the actual duty cycle of the generated clock. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_create_future_time_event.html language=enus -->
## TOPIC 00085: niSync Create Future Time Event (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_create_future_time_event.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_create_future_time_event.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Create Future Time Event (VI)

Installed With:

Schedules a future time event. A future time event changes the digital signal at the terminal you specify—either from low to high or high to low—when the board time of the specified module reaches the time you specify with **time**. The future time event you create with this VI is synchronized with the board time of the module you specify with **instrument handle**.

To create multiple future time events, invoke this VI multiple times. Once you generate a future time event on a terminal, that terminal cannot be used for operations other than generating future time events until you clear all future time events with [niSync Clear Future Time Events](nisync_clear_future_time_events.html) or you close the session with [niSync Close](nisync_close.html). When you invoke this VI, the digital signal on the specified terminal is driven low until the first future time event occurs.

|  | Note This property is supported only on certain targets; refer to Target Support for Timing Properties for more information. |
| --- | --- |

[IMAGE alt='niSync Create Future Time Event' src='nisync_create_future_time_event.gif']

|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |
| --- | --- |
|  | terminal specifies the terminal whose digital signal will be changed by the future time event. |
|  | output level specifies the level to set the digital signal to when the future time event occurs. The enumerated values for this input are high and low. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | time specifies the board time when the future time event occurs. When the board time of the module you specify in the instrument handle terminal reaches this time, the digital signal of the terminal input changes to the value you specify in the output level terminal. The default value of this input is immediate, which triggers the future time event as soon as the VI is invoked. |
|  | instrument handle out returns the instrument handle that you obtain from niSync Initialize. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=ni-sync-labview-api-ref path=ni-sync-api-ref/nisync_disable_gps_or_irig_timestamping.html language=enus -->
## TOPIC 00086: niSync Disable GPS or IRIG Timestamping (VI)

- bundle_id: `ni-sync-labview-api-ref`
- source_path: `ni-sync-api-ref/nisync_disable_gps_or_irig_timestamping.html`
- source_url: https://docs-be.ni.com/bundle/ni-sync-labview-api-ref/raw/resource/enus/ni-sync-api-ref/nisync_disable_gps_or_irig_timestamping.html
- document_id: `ni-sync-labview-api-ref`
- page_type: `leaf`
- content_type: ``

niSync Disable GPS or IRIG Timestamping (VI)

Installed With:

Ends GPS or IRIG timestamping on the specified device. You must use this VI every time you invoke [niSync Enable GPS or IRIG Timestamping](nisync_enable_gps_or_irig_timestamping.html).

|  | Note This function is supported only on certain targets; refer to Target Support for Timing Properties and VIs for more information. |
| --- | --- |

#### niSync Disable GPS or IRIG Timestamping (IRIG)

Use this instance to disable timestamping of IRIG-B AM or IRIG-B DC decodes.

[IMAGE alt='niSync Disable GPS or IRIG Timestamping (IRIG)' src='nisync_disable_gps_or_irig_timestamping_(irig).gif']

|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |
| --- | --- |
|  | terminal specifies the terminal on which to disable IRIG decoding. You can then use this terminal for other operations. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. |
|  | instrument handle out returns the instrument handle that you obtain from niSync Initialize. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |

#### niSync Disable GPS or IRIG Timestamping (GPS)

Use this instance to disable timestamping of the GPS pulse per second.

[IMAGE alt='niSync Disable GPS or IRIG Timestamping (GPS)' src='nisync_disable_gps_or_irig_timestamping_(gps).gif']

|  | instrument handle specifies the instrument handle that you obtain from niSync Initialize. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. |
|  | instrument handle out returns the instrument handle that you obtain from niSync Initialize. |
|  | error out returns error conditions that occur after this node runs. This output provides standard error out functionality. |
