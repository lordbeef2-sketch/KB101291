# NI DOCUMENT BUNDLE: ni-scope-20.0-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-scope-20.0-lvnxg-api-ref start=1 end=32 -->
<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=adjust-range-calibration.html language=enus -->
## TOPIC 00001: Adjust Range Calibration

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `adjust-range-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/adjust-range-calibration.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Externally calibrates the vertical range for the specified channel and vertical range setting. session in The instrument handle that you obtain from Initialize External Calibration. The handle identifies a particular instrument session. error in Error conditions that occur before this node runs. The

Adjust Range Calibration

Externally calibrates the vertical range for the specified channel and vertical range setting.

[IMAGE alt='1378' src='Adjust_Range_Calibration.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The instrument handle that you obtain from Initialize External Calibration. The handle identifies a particular instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channels

The channel(s) to calibrate.

##### Channel String Syntax

This input parameter has the following syntax options:

- A single channel, such as
 0
- A list of channels, such as 
 0,1 or 
 3,2,1,0
- A range of channels, such as
 0-7 or 0:7
- All channels, which is designated by an empty
 string
- A combination of channels from multiple instruments,
 such as PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3

Note

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### range

The vertical range, in volts, to calibrate.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### stimulus

The voltage of the applied DC signal.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=adjust-sample-clock-relative-delay.html language=enus -->
## TOPIC 00002: Adjust Sample Clock Relative Delay

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `adjust-sample-clock-relative-delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/adjust-sample-clock-relative-delay.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies offset, in seconds, to the sample clock relative to the reference clock when using the onboard clock. Each time this node is called, the sample clock is offset from the reference clock by the specified amount of time. Adjustment range: ±1 Sample Clock Period per call session in Handle that i

Adjust Sample Clock Relative Delay

Applies offset, in seconds, to the sample clock relative to the reference clock when using
 the onboard clock.

Each time this node is called, the sample clock is offset from the reference clock by the
 specified amount of time.

Adjustment range: ±1 *Sample Clock Period* per call

[IMAGE alt='1378' src='Adjust_Sample_Clock_Relative_Delay.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### delay

The amount of time, in seconds, to delay the sample clock.

This value is relative, so repeated calls to this node delay the sample clock by this amount every time.

Default value: 0.00

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node does not support the following hardware:

- PXIe-5110
- PXIe-5111
- PXIe-5113
- PXIe-5160
- PXIe-5162
- PXIe-5163
- PXIe-5164
- PXIe-5170
- PXIe-5171
- PXIe-5172
- PXIe-5185
- PXIe-5186

#### Programming Patterns

NI-TClk

1. Apply time offset with this node to reduce skew and/or
 jitter.
2. Use the NI-SCOPE Oscillator Phase DAC Value property to convert this time offset
 into a value that can apply the manual adjustment across sessions and improve
 synchronization repeatability.

NI-TClk

Parent topic:

Clock

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=adjust-vcxo-calibration.html language=enus -->
## TOPIC 00003: Adjust VCXO Calibration

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `adjust-vcxo-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/adjust-vcxo-calibration.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calibrates the sample rate of SMC-based digitizers. Use this node only when following the external calibration procedure for your device. This node adjusts the frequency of the voltage controlled crystal oscillator (VCXO) that serves as the digitizer's onboard sample rate timebase. Check the calibra

Adjust VCXO Calibration

Calibrates the sample rate of SMC-based digitizers.

Note

This node adjusts the frequency of the voltage controlled crystal oscillator (VCXO) that serves as the digitizer's onboard sample rate timebase. Check the calibration procedure of your device and set the value of stimulus frequency. Before calling this node, connect an accurate, stable reference signal to channel 0 (the channel used is not configurable).

This node adjusts frequency calibration constants until the digitizer measures the frequency of the reference signal. The new calibration constants take effect immediately for the duration of the external calibration session. The constants are written to the EEPROM if you call Close External Calibration with no errors and with action set to 
 Store Calibration.

[IMAGE alt='1378' src='Adjust_VCXO_Calibration.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The instrument handle that you obtain from Initialize External Calibration. The handle identifies a particular instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### stimulus frequency

The frequency of the external reference clock connected to channel 0.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=auto-setup.html language=enus -->
## TOPIC 00004: Auto Setup

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `auto-setup.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/auto-setup.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automatically configures the oscilloscope. When you call this node, the oscilloscope senses the input signal and automatically configures many of the instrument settings. If a signal is detected on a channel, the driver chooses the smallest available vertical range that is larger than the signal ran

Auto Setup

Automatically configures the oscilloscope.

When you call this node, the oscilloscope senses the input signal and automatically configures many of the instrument settings. If a signal is detected on a channel, the driver chooses the smallest available vertical range that is larger than the signal range. For example, if the signal is a 1.2 Vpk-pk sine wave, and the device supports 1 V and 2 V vertical ranges, the driver will choose the 2 V vertical range for that channel.

If no signal is found on any analog input channel, a warning is returned and all channels are enabled. A channel is considered to have a signal present if the signal is at least 10% of the smallest vertical range available for that channel.

[IMAGE alt='1378' src='Auto_Setup.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Settings Changed by Auto Setup

This node changes the following settings to the following values:

| General Settings | Value |
| --- | --- |
| Acquisition Mode | Normal |
| Reference Clock | Internal |

| Vertical Settings | Value |
| --- | --- |
| Vertical Coupling | AC (when AC is supported; otherwise DC) |
| Vertical Bandwidth | Full |
| Vertical Range | Changed by Auto Setup |
| Vertical Offset | 0 V |
| Probe Attenuation | Unchanged by Auto Setup |
| Input Impedance | Unchanged by Auto Setup |

| Horizontal Settings | Value |
| --- | --- |
| Sample Rate | Changed by Auto Setup |
| Min Record Length | Changed by Auto Setup |
| Enforce Realtime | True |
| Number of Records | 1 |

| Triggering Settings | Value |
| --- | --- |
| Trigger Type | Edge if signal present, otherwise immediate. |
| Trigger Channel | Lowest numbered channel with a signal present. |
| Trigger Slope | Positive |
| Trigger Coupling | DC |
| Reference Position | 50% |
| Trigger Level | 50% of signal on trigger channel |
| Trigger Delay | 0 |
| Trigger Holdoff | 0 |
| Trigger Output | None |

#### PXIe-5185 and PXIe-5186 Unique Behavior

Because PXIe-5185 and PXIe-5186 modules have two physical connectors (50 Ω input impedance, 1 MΩ input impedance) for each channel, this node has unique behavior for these modules.

When you use niScope Properties to specify the input impedance on either channel or both channels, this node searches for a signal on only that input connector. If no signal is detected, NI-SCOPE returns a warning and both channels are enabled for the input impedance specified.

If you do not specify an input impedance, this node searches for a signal on both input connectors (first on the 50 Ω input connector, then on the 1 MΩ input connector). If NI-SCOPE detects a signal on the 50 Ω connector (default), then it uses that signal. If NI-SCOPE does not detect a signal on the 50 Ω connector, then it searches the 1 MΩ connector for a signal. If a signal is not detected on any connectors, NI-SCOPE returns a warning and both channels are enabled with 50 Ω impedance.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=cablesense-signal-start.html language=enus -->
## TOPIC 00005: CableSense Signal Start

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `cablesense-signal-start.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/cablesense-signal-start.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates the CableSense signal on all channels of an oscilloscope for which the signal is enabled, as configured by the CableSense Mode property. The input impedance of the channel(s) to convey the CableSense signal must be set to 50 Ω. You can call this node only during an acquisition. If you call

CableSense Signal Start

Generates the CableSense signal on all channels of an oscilloscope for which the signal is enabled, as configured by the CableSense Mode property.

Note

50 Ω

You can call this node only during an acquisition. If you call this node while your oscilloscope is not acquiring, NI-SCOPE generates an error.

[IMAGE alt='1378' src='CableSense_Signal_Start.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5110
- PXIe-5111
- PXIe-5113
- PXIe-5160
- PXIe-5162

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=cablesense-signal-stop.html language=enus -->
## TOPIC 00006: CableSense Signal Stop

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `cablesense-signal-stop.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/cablesense-signal-stop.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the CableSense signal on all channels of an oscilloscope for which the signal is enabled. session in Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options . error in Error conditions that occur before this node runs. The node responds to t

CableSense Signal Stop

Disables the CableSense signal on all channels of an oscilloscope for which the signal is enabled.

[IMAGE alt='1378' src='CableSense_Signal_Stop.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- PXIe-5110
- PXIe-5111
- PXIe-5113
- PXIe-5160
- PXIe-5162

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=calibration-category.html language=enus -->
## TOPIC 00007: Calibration

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `calibration-category.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/calibration-category.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calibration functions for NI-SCOPE.

Calibration

Calibration functions for NI-SCOPE.

NI-SCOPE Nodes

Nodes for programming oscilloscopes.

Self Calibrate

Self-calibrates most NI digitizers, including all SMC-based devices.

External Calibration

External calibration functions for NI-SCOPE.

Parent topic:

NI-SCOPE Nodes

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=change-calibration-password.html language=enus -->
## TOPIC 00008: Change Calibration Password

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `change-calibration-password.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/change-calibration-password.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the password used to begin an external calibration session. This node verifies old password against the password stored in the device's EEPROM. If the two passwords match, the node stores the new password in the device's EEPROM. The password is stored as four characters, but shorter strings

Change Calibration Password

Changes the password used to begin an external calibration session.

This node verifies old password against the password stored in the device's EEPROM. If the two passwords match, the node stores the new password in the device's EEPROM. The password is stored as four characters, but shorter strings are acceptable.

[IMAGE alt='1378' src='Change_Calibration_Password.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The instrument handle that you obtain from Initialize External Calibration. The handle identifies a particular instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### old password

The password currently stored in the device's EEPROM.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### new password

The new password to store in the device's EEPROM. A maximum of 4 characters can be stored.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Default Passwords

NI

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=clear-waveform-measurement-stats.html language=enus -->
## TOPIC 00009: Clear Waveform Measurement Stats

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `clear-waveform-measurement-stats.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/clear-waveform-measurement-stats.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the waveform statistics on the channel and measurement you specify. Clears the statistical information and the multi-acquisition array measurements. Every time a measurement is called, the statistics information is updated, including the min, max, mean, standard deviation, and number of updat

Clear Waveform Measurement Stats

Clears the waveform statistics on the channel and measurement you specify.

Clears the statistical information and the multi-acquisition array measurements. Every time a measurement is called, the statistics information is updated, including the min, max, mean, standard deviation, and number of updates.

[IMAGE alt='1378' src='Clear_Waveform_Measurement_Stats.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channels

The channel(s) from which to acquire data.

##### Channel String Syntax

This input parameter has the following syntax options:

- A single channel, such as 
 0
- A list of channels, such as
 0,1 or 3,2,1,0
- A range of channels, such as
 0-7 or 0:7
- A combination of channels from multiple instruments,
 such as PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3

Note

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### clearable measurement

The measurement for which to clear the statistics.

| All Measurements | 10000 | Clears all measurements. |
| --- | --- | --- |
| Multi Acq. Voltage Histogram | 4004 | Corresponds to the NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM C or C++ command. |
| Multi Acq. Time Histogram | 4005 | Corresponds to the NISCOPE_VAL_MULTI_TIME_HISTOGRAM C or C++ command. |
| Multi Acq. Average | 4016 | Corresponds to the NISCOPE_VAL_MULTI_ACQ_AVERAGE C or C++ command. |
| Frequency | 2 | Corresponds to the NISCOPE_VAL_FREQUENCY C or C++ command.1.0 divided by the frequency, in hertz. |
| Average Frequency | 1016 | Corresponds to the NISCOPE_VAL_AVERAGE_FREQUENCY C or C++ command.1.0 divided by the average period. |
| FFT Frequency | 1008 | Corresponds to the NISCOPE_VAL_FFT_FREQUENCY C or C++ command. |
| Period | 3 | Corresponds to the NISCOPE_VAL_PERIOD C or C++ command. |
| Average Period | 1015 | Corresponds to the NISCOPE_VAL_AVERAGE_PERIOD C or C++ command. |
| Rise Time | 0 | Corresponds to the NISCOPE_VAL_RISE_TIME C or C++ command. |
| Fall Time | 1 | Corresponds to the NISCOPE_VAL_FALL_TIME command. |
| Rising Slew Rate | 1010 | Corresponds to the NISCOPE_VAL_RISE_SLEW_RATE C or C++ command. |
| Falling Slew Rate | 1011 | Corresponds to the NISCOPE_VAL_FALL_SLEW_RATE C or C++ command. |
| Overshoot | 18 | Corresponds to the NISCOPE_VAL_OVERSHOOT C or C++ command. |
| Preshoot | 19 | Corresponds to the NISCOPE_VAL_PRESHOOT C or C++ command. |
| Voltage RMS | 4 | Corresponds to the NISCOPE_VAL_VOLTAGE_RMS C or C++ command. |
| Voltage Cycle RMS | 4 | Corresponds to the NISCOPE_VAL_VOLTAGE_CYCLE_RMS C or C++ command. |
| AC Estimate | 1012 | Corresponds to the NISCOPE_VAL_AC_ESTIMATE C or C++ command. |
| FFT Amplitude | 1009 | Corresponds to the NISCOPE_VAL_FFT_AMPLITUDE C or C++ command. |
| Voltage Average | 10 | Corresponds to the NISCOPE_VAL_VOLTAGE_AVERAGE C or C++ command. |
| Voltage Cycle Average | 17 | Corresponds to the NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE |
| DC Estimate | 1013 | Corresponds to the NISCOPE_VAL_DC_ESTIMATE C or C++ command. |
| Voltage Max | 6 | Corresponds to the NISCOPE_VAL_VOLTAGE_MAX C or C++ command. |
| Voltage Min | 7 | Corresponds to the NISCOPE_VAL_VOLTAGE_MIN C or C++ command. |
| Voltage Peak-to-Peak | 5 | Corresponds to the NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK C or C++ command. |
| Voltage High | 8 | Corresponds to the NISCOPE_VAL_VOLTAGE_HIGH C or C++ command. |
| Voltage Low | 9 | Corresponds to the NISCOPE_VAL_VOLTAGE_LOW C or C++ command. |
| Voltage Amplitude | 15 | Corresponds to the NISCOPE_VAL_AMPLITUDE C or C++ command. |
| Voltage Top | 1007 | Corresponds to the NISCOPE_VAL_VOLTAGE_TOP C or C++ command. |
| Voltage Base | 1006 | Corresponds to the NISCOPE_VAL_VOLTAGE_BASE C or C++ command. |
| Voltage Base to Top | 1017 | Corresponds to the NISCOPE_VAL_VOLTAGE_BASE_TO_TOP C or C++ command. |
| Negative Width | 11 | Corresponds to the NISCOPE_VAL_WIDTH_NEG C or C++ Command. |
| Positive Width | 12 | Corresponds to the NISCOPE_VAL_WIDTH_POS C or C++ command. |
| Negative Duty Cycle | 13 | Corresponds to the NISCOPE_VAL_DUTY_CYCLE_NEG C or C++ command. |
| Positive Duty Cycle | 14 | Corresponds to the NISCOPE_VAL_DUTY_CYCLE_POS C or C++ command. |
| Integral | 1005 | Corresponds to the NISCOPE_VAL_INTEGRAL C or C++ command. |
| Area | 1003 | Corresponds to the NISCOPE_VAL_AREA C or C++ command. |
| Cycle Area | 1004 | Corresponds to the NISCOPE_VAL_CYCLE_AREA C or C++ command. |
| Time Delay | 1014 | Corresponds to the NISCOPE_VAL_TIME_DELAY C or C++ command |
| Phase Delay | 1018 | Corresponds to the NISCOPE_VAL_PHASE_DELAY C or C++ command. |
| Low Ref Volts | 1000 | Corresponds to the NISCOPE_VAL_LOW_REF_VOLTS C or C++ command. |
| Mid Ref Volts | 1001 | Corresponds to the NISCOPE_VAL_MID_REF_VOLTS C or C++ command. |
| High Ref Volts | 1002 | Corresponds to the NISCOPE_VAL_HIGH_REF_VOLTS C or C++ command. |
| Volt. Hist. Mean | 2000 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN C or C++ command. |
| Volt. Hist. Stdev | 2001 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV C or C++ command. |
| Volt. Hist. Median | 2003 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN C or C++ command. |
| Volt. Hist. Mode | 2010 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE C or C++ command. |
| Volt Hist. Max | 2005 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX C or C++ command. |
| Volt. Hist. Min | 2006 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN C or C++ command. |
| Volt. Hist. Peak-to-Peak | 2002 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK C or C++ command. |
| Volt. Hist. Mean + Stdev | 2007 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV C or C++ command. |
| Volt. Hist. Mean + 2 Stdev | 2008 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV C or C++ command. |
| Volt. Hist. Mean + 3 Stdev | 2009 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV C or C++ command. |
| Volt. Hist. Hits | 2004 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS C or C++ command. |
| Volt. Hist. New Hits | 2011 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS C or C++ command. |
| Time Hist. Mean | 3000 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MEAN C or C++ command. |
| Time Hist. Stdev | 3001 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_STDEV C or C++ command. |
| Time Hist. Median | 3003 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MEDIAN C or C++ command. |
| Time Hist. Mode | 3010 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MODE C or C++ command. |
| Time Hist. Max | 3005 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MAX C or C++ command. |
| Time Hist. Min | 3006 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MIN C or C++ command. |
| Time Hist. Peak-to-Peak | 3002 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK C or C++ command. |
| Time Hist. Mean + Stdev | 3007 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV C or C++ command. |
| Time Hist. Mean + 2 Stdev | 3008 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV C or C++ command. |
| Time Hist. Mean + 3 Stdev | 3009 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_3_STDEV C or C++ command. |
| Time Hist. Hits | 3004 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_HITS C or C++ command. |
| Time Hist. New Hits | 3011 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS C or C++ command. |

Default value: All Measurements

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Measurements

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=clear-waveform-processing.html language=enus -->
## TOPIC 00010: Clear Waveform Processing

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `clear-waveform-processing.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/clear-waveform-processing.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the list of processing steps assigned to the given channel. session in Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options . error in Error conditions that occur before this node runs. The node responds to this input according to standard

Clear Waveform Processing

Clears the list of processing steps assigned to the given channel.

[IMAGE alt='1378' src='Clear_Waveform_Processing.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channels

The channel(s) from which to acquire data.

##### Channel String Syntax

This input parameter has the following syntax options:

- A single channel, such as 
 0
- A list of channels, such as
 0,1 or 3,2,1,0
- A range of channels, such as
 0-7 or 0:7
- A combination of channels from multiple instruments,
 such as PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3

Note

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Processing Steps

Add Waveform Processing

Parent topic:

Measurements

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=clock-category.html language=enus -->
## TOPIC 00011: Clock

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `clock-category.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/clock-category.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clock functions for NI-SCOPE.

Clock

Clock functions for NI-SCOPE.

Configuration

Use the NI-SCOPE Configuration functions to set up the parameters of your acquisition, or use Auto Setup to automatically configure device settings.

Adjust Sample Clock Relative Delay

Applies offset, in seconds, to the sample clock relative to the reference clock when using the onboard clock.

Configure Clock

Configures the properties for synchronizing the digitizer to an external clock or sending the digitizer's clock output to be used as a synchronizing clock for other devices.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=close-external-calibration.html language=enus -->
## TOPIC 00012: Close External Calibration

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `close-external-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/close-external-calibration.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an external calibration session. You must call this node each time you call Initialize External Calibration, even if an error occurs during calibration. session in The instrument handle that you obtain from Initialize External Calibration. The handle identifies a particular instrument session

Close External Calibration

Closes an external calibration session.
 
 You must call this node each time you call Initialize External Calibration, even if an error occurs during calibration.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The instrument handle that you obtain from Initialize External Calibration. The handle identifies a particular instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### action

The action to take with the calibration constants.

| Store Calibration | 0 | Stores the new calibration constants in the EEPROM. For most digitizers, the current system date and the incremented calibration count are also stored. For SMC-based digitizers, the current system date and the onboard temperature are also stored. |
| --- | --- | --- |
| Abort Calibration | 1 | Closes the session and discards any new calibration constants. Some devices may write to the EEPROM during calibration, in which case this action restores the EEPROM to its original state. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=close.html language=enus -->
## TOPIC 00013: Close

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `close.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/close.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Ends an niScope instrument I/O session and performs closing actions. This function performs the following actions: Closes the instrument I/O session. Destroys the IVI session and all of its properties Deallocates memory resources used by the IVI session. session in Handle that identifies the NI-SCOP

Close

Ends an niScope instrument I/O session and performs closing actions.

This function performs the following actions:

- Closes the instrument I/O session.
- Destroys the IVI session and all of its properties
- Deallocates memory resources used by the IVI session.

[IMAGE alt='1378' src='Close.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

NI-SCOPE Nodes

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=commit.html language=enus -->
## TOPIC 00014: Commit

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `commit.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/commit.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits to hardware all the parameter settings associated with the task. Use this function if you want a parameter change to be immediately reflected in the hardware. session in Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options . error in Error

Commit

Commits to hardware all the parameter settings associated with the task.
 
 Use this function if you want a parameter change to be immediately reflected in the hardware.

[IMAGE alt='1378' src='Commit.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Immediately Writing New Configuration Settings

NI-SCOPE

Commit

Initiate Acquisition

Parent topic:

Low Level Acquisition

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=configuration-category.html language=enus -->
## TOPIC 00015: Configuration

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `configuration-category.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/configuration-category.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE Configuration functions to set up the parameters of your acquisition, or use Auto Setup to automatically configure device settings.

Configuration

Use the NI-SCOPE Configuration functions to set up the parameters of your acquisition, or use Auto Setup to automatically configure device settings.

NI-SCOPE Nodes

Nodes for programming oscilloscopes.

Auto Setup

Automatically configures the oscilloscope.

Configure Channel Characteristics

Configures the properties that control the electrical characteristics of the channel.

Configure Horizontal Timing

Configures the common properties of the horizontal subsystem for a single record or multi-record acquisition.

Configure Vertical

Configures the most commonly configured properties of the digitizer vertical subsystem, such as the range, offset, coupling, probe attenuation, and the channel name.

Export Attribute Configuration

Exports the attribute configuration of a session to either a file or a buffer.

Import Attribute Configuration

Imports an attribute configuration to the session from either a file or a buffer.

Configuration Information

Configuration information functions for NI-SCOPE.

Trigger

Functions to configure triggers in NI-SCOPE.

Clock

Clock functions for NI-SCOPE.

Onboard Signal Processing

Functions to configure the parameters NI-SCOPE uses to process onboard signals.

Parent topic:

NI-SCOPE Nodes

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=configure-acquisition.html language=enus -->
## TOPIC 00016: Configure Acquisition

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `configure-acquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/configure-acquisition.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures how the digitizer acquires data and fills the waveform record. session in Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options . error in Error conditions that occur before this node runs. The node responds to this input according to st

Configure Acquisition

Configures how the digitizer acquires data and fills the waveform record.

[IMAGE alt='1378' src='Configure_Acquisition.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### acquisition type

The manner in which the oscilloscope acquires data and fills the waveform record.

Not all oscilloscopes support all acquisition types.

| Normal | 0 | Sets the oscilloscope to normal resolution mode. The oscilloscope can use real-time sampling or equivalent-time sampling. |
| --- | --- | --- |
| Flex Res | 1 | Sets legacy oscilloscopes to flexible resolution mode, if supported. |
| DDC | 3 | Sets legacy oscilloscopes to DDC mode, if supported. Note To use DDC mode for the PXI/PCI-5142 or PXIe-5622, set this parameter to Normal and set the DDC Enabled property to True. |

Default value: Normal

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Onboard Signal Processing

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=onboard-signal-processing-category.html language=enus -->
## TOPIC 00017: Onboard Signal Processing

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `onboard-signal-processing-category.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/onboard-signal-processing-category.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Functions to configure the parameters NI-SCOPE uses to process onboard signals.

Onboard Signal Processing

Functions to configure the parameters NI-SCOPE uses to process onboard signals.

Configuration

Use the NI-SCOPE Configuration functions to set up the parameters of your acquisition, or use Auto Setup to automatically configure device settings.

Configure Acquisition

Configures how the digitizer acquires data and fills the waveform record.

Configure Equalization Filter Coefficients

Configures the custom coefficients for the equalization finite impulse response (FIR) filter on the device.

Get Equalization Filter Coefficients

Retrieves the custom coefficients for the equalization FIR filter on the device.

Get Frequency Response

Gets the frequency response of the digitizer for the current configurations of the channel attributes.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=probe-compensation-signal-start.html language=enus -->
## TOPIC 00018: Probe Compensation Signal Start

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `probe-compensation-signal-start.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/probe-compensation-signal-start.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a 1 kHz square wave signal for probe compensation. Most oscilloscopes output the probe compensation signal on PFI 1. session in Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options . error in Error conditions that occur before this node

Probe Compensation Signal Start

Generates a 1 kHz square wave signal for probe compensation.

Most oscilloscopes output the probe compensation signal on PFI 1.

[IMAGE alt='1378' src='Probe_Compensation_Signal_Start.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node does not support the following hardware:

- PXIe-5185
- PXIe-5186
- PXIe-5622
- PXI/PCI-5922

#### Device-Specific Behavior

The following oscilloscopes output the probe compensation signal in unique locations.

| Device | Output Location |
| --- | --- |
| PXIe-5110 PXIe-5111 PXIe-5113 | Probe compensation terminal Note The signal at this terminal is enabled by default. |
| PXIe-5163 PXIe-5164 | SMB PFI 0 Note Though the PFI 0 line is also available from the AUX 0 MHDMR connector of these oscilloscopes, the probe compensation signal is available only from SMB PFI 0. |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=probe-compensation-signal-stop.html language=enus -->
## TOPIC 00019: Probe Compensation Signal Stop

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `probe-compensation-signal-stop.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/probe-compensation-signal-stop.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the 1 kHz square wave signal for probe compensation. session in Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options . error in Error conditions that occur before this node runs. The node responds to this input according to standard error

Probe Compensation Signal Stop

Disables the 1 kHz square wave signal for probe compensation.

[IMAGE alt='1378' src='Probe_Compensation_Signal_Stop.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node does not support the following hardware:

- PXIe-5185
- PXIe-5186
- PXIe-5622
- PXI/PCI-5922

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=read-measurement-multimode.html language=enus -->
## TOPIC 00020: Read Measurement

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `read-measurement-multimode.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/read-measurement-multimode.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates an acquisition, waits for it to complete, and performs the specified waveform measurement.

Read Measurement

Initiates an acquisition, waits for it to complete, and performs the specified waveform measurement.

Measurements

NI-SCOPE functions for performing waveform measurements.

Read Measurement

Initiates an acquisition, waits for it to complete, and performs the specified waveform measurement for a single channel and record.

Read Multiple Measurement

Initiates an acquisition, waits for it to complete, and performs the specified waveform measurement for multiple channels and records.

Parent topic:

Measurements

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=read-measurement.html language=enus -->
## TOPIC 00021: Read Measurement

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `read-measurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/read-measurement.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates an acquisition, waits for it to complete, and performs the specified waveform measurement for a single channel and record. session in Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options . error in Error conditions that occur before this

Read Measurement

Initiates an acquisition, waits for it to complete, and performs the specified waveform measurement for a single channel and record.

[IMAGE alt='1378' src='Read_Measurement.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channels

The channel(s) from which to acquire data.

##### Channel String Syntax

This input parameter has the following syntax options:

- A single channel, such as 
 0
- A list of channels, such as
 0,1 or 3,2,1,0
- A range of channels, such as
 0-7 or 0:7
- A combination of channels from multiple instruments,
 such as PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3

Note

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### scalar measurement

The measurement to perform on the waveform read from the digitizer.

| None | 4000 | No scalar measurement is performed. |
| --- | --- | --- |
| Frequency | 2 | Corresponds to the NISCOPE_VAL_FREQUENCY C or C++ command. 1.0 divided by the period, in hertz. |
| Average Frequency | 1016 | Corresponds to the NISCOPE_VAL_AVERAGE_FREQUENCY C or C++ command. 1.0 divided by the average period, in hertz. |
| FFT Frequency | 1008 | Corresponds to the NISCOPE_VAL_FFT_FREQUENCY C or C++ command. The FFT amplitude spectrum is calculated using a split-radix real FFT, and the frequency corresponding to the maximum amplitude is returned. If the input waveform size is not a power of two, the waveform is zero padded to the next higher power of two. The frequency resolution is sampling rate / number of points.The DC bin of the FFT is ignored when searching for the maximum amplitude, so the FFT frequency should ignore any DC offsets. However, the zero padding used in the FFT measurement can introduce other low frequency components if the waveform has a large DC offset. To avoid problems, make sure the Horizontal Actual Record Length property is a power of 2, so no zero padding occurs. This property can be fetched using niScope Actual Record Length. Alternatively, configuring the digitizer for AC coupling solves the problem. |
| Period | 3 | Corresponds to the NISCOPE_VAL_PERIOD C or C++ command. Finds the time, in seconds, between the first and third mid reference level crosspoints. A hysteresis window is applied when finding crosspoints. The mid reference level is 50% by default and is set with the Channel Based Mid Ref Level property. |
| Average Period | 1015 | Corresponds to the NISCOPE_VAL_AVERAGE_PERIOD C or C++ command. Up to 256 mid reference level crossings are found on the waveform using a digital hysteresis. The time difference between the last crossing and the first crossing is divided by the number of periods found in the waveform. The last crossing is defined as the last crossing in the waveform with the same slope as the first crossing, so an integer number of periods exist in the waveform. |
| Rise Time | 0 | Corresponds to the NISCOPE_VAL_RISE_TIME C or C++ command. The time span, in seconds, from when the waveform crosses the low reference level until it crosses the high reference level. The measurement starts at the left edge of the waveform and finds all low reference level crossings until a high reference level crossing. The final low reference level crossing is used in the calculation.The reference levels are specified by Channel Based Low Ref and Channel Based High Ref, and their default values are 10% and 90%. |
| Fall Time | 1 | Corresponds to the NISCOPE_VAL_FALL_TIME C or C++ command. The time span, in seconds, from when the waveform crosses the high reference level until it crosses the low reference level. The measurement starts at the left edge of the waveform and finds all high reference level crossings until a low reference level crossing. The final high reference level crossing is used in the calculation.The reference levels are specified by Channel Based Low Ref and Channel Based High Ref, and their default values are 10% and 90%. |
| Rising Slew Rate | 1010 | Corresponds to the NISCOPE_VAL_RISE_SLEW_RATE C or C++ command. The high reference voltage minus the low reference voltage is divided by the rise-time calculation. |
| Falling Slew Rate | 1011 | Corresponds to the NISCOPE_VAL_FALL_SLEW_RATE C or C++ command. The low reference voltage minus the high reference voltage is divided by the fall-time calculation. The result is always negative. |
| Overshoot | 18 | Corresponds to the NISCOPE_VAL_OVERSHOOT C or C++ command. The measurement is taken on the first edge of the waveform. If two edges exist, the algorithm finds the time interval from the first edge until one half the time to the second edge. The local maxima and minima are found in this interval. If only one edge is present in the waveform, the local maximum and minimum is found between the first edge and the end of the waveform. If the first edge is positive sloped, overshoot = 100 × (local maximum - voltage high) / voltage amplitude.If the first edge is negative sloped, overshoot = 100 × (voltage low - local minimum) / voltage amplitude. |
| Preshoot | 19 | Corresponds to the NISCOPE_VAL_PRESHOOT C or C++ command. The measurement is taken on the second edge of the waveform if two edges exist. The algorithm finds the time interval from the middle time between the two edges until the second edge. The local maxima and minima are found in this interval. If only one edge is present in the waveform, the local maximum and minimum are found from the start of the waveform to the first edge.If the edge is negative sloped, preshoot = 100 × (local maximum - voltage high) / voltage amplitude.If the edge is positive sloped, preshoot = 100 × (voltage low - local minimum) / voltage amplitude. |
| Voltage RMS | 4 | Corresponds to the NISCOPE_VAL_VOLTAGE_RMS C or C++ command. Voltage RMS is determined by the following equation:Voltage RMS = √[( Σ waveform[i]2) / numPoints] |
| Voltage Cycle RMS | 16 | Corresponds to the NISCOPE_VAL_VOLTAGE_CYCLE_RMS C or C++ command. Voltage Cycle RMS = √[(Σ waveform[i]2) / pointsPerPeriod]The number points in a period is calculated using the equation:pointsPerPeriod = period / dtwhere period is the measured period of the signal and dt is the time between two points. The result will then be converted to an integer from a floating point value. |
| AC Estimate | 1012 | Corresponds with the NISCOPE_VAL_AC_ESTIMATE C or C++ command. The DC estimate is subtracted from the waveform, and a Hanning window is applied to give a processed waveform. The RMS voltage is calculated with the following equation:√([Σ processed waveform[i]2] / [numPoints × enbw × cg2]),where the equivalent noise bandwidth (enbw) for the Hanning window is 1.5, and the coherent gain (cg) is 0.5.This algorithm minimizes the effect of an uneven number of waveform cycles in the measurement, which could arbitrarily increase or decrease the RMS value. |
| FFT Amplitude | 1009 | Corresponds to the NISCOPE_VAL_FFT_AMPLITUDE C or C++ command. The FFT amplitude spectrum is calculated using a split-radix real FFT, and the maximum amplitude is returned. If the input waveform size is not a power of two, the waveform is zero-padded to the next highest power of two. For best results, verify that your actual record length is a power of 2. |
| Voltage Average | 10 | Corresponds to the NISCOPE_VAL_VOLTAGE C or C++ command. The voltage average is determined by the following equation:Voltage Average = Σ waveform[i] / numPoints |
| Voltage Cycle Average | 17 | Corresponds to the NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE C or C++ command. Voltage Cycle Average = ( Σ waveform[i]) / pointsPerPeriodThe number of points in a period in volts is calculated using the following equation:pointsPerPeriod = period / dtwhere period is the measured period of the signal and dt is the time between two points. The result will then be converted to an integer from a floating point value. |
| DC Estimate | 1013 | Corresponds to the NISCOPE_VAL_DC_ESTIMATE C or C++ command. A Hanning window is applied to give a processed waveform and the voltage average is calculated with the following equation:voltage average = (Σ processed waveform[i]) / (cg × numPoints),where the coherent gain (cg) of the Hanning window is 0.5 - the DC gain of the window.The algorithm minimizes the effect of an uneven number of waveform cycles. For example, performing a simple voltage average on 5.5 cycles of a sine waveform gives a slightly incorrect DC estimate if the extra half cycle is not evenly divided between the positive and negative portions of the sine wave. |
| Voltage Max | 6 | Corresponds to the NISCOPE_VAL_VOLTAGE_MAX C or C++ command. Searches the waveform for its maximum point. |
| Voltage Min | 7 | Corresponds to the NISCOPE_VAL_VOLTAGE_MIN C or C++ command. Searches the waveform for the minimum point in volts. |
| Voltage Peak-to-Peak | 5 | Corresponds to the NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK C or C++ command. The maximum voltage minus the minimum voltage in volts. |
| Voltage High | 8 | Corresponds to the NISCOPE_VAL_VOLTAGE_HIGH C or C++ command. Uses the last-acquisition histogram method, where the voltage high result is the voltage of the histogram bin with the maximum number of hits above 60% of the waveform's voltage peak-to-peak value. This calculation is useful for ignoring the overshoot and preshoot on square waves. |
| Voltage Low | 9 | Corresponds to the NISCOPE_VAL_VOLTAGE_LOW C or C++ command. The last acquisition histogram method is used where the voltage low result is the voltage of the histogram bin with the maximum number of hits below 40% of the waveform's voltage peak-to-peak value. This calculation is useful for ignoring the overshoot and preshoot on square waves. |
| Voltage Amplitude | 15 | Corresponds to the NISCOPE_VAL_VOLTAGE_AMPLITUDE C or C++ command. The voltage amplitude is calculated by the voltage high minus the voltage low. |
| Voltage Top | 1007 | Corresponds to the NISCOPE_VAL_VOLTAGE_TOP C or C++ command. If the histogram bin corresponding to voltage high has over fiver percent of the total hits, the voltage high result is returned. Otherwise, the voltage maximum calculation is returned. Otherwise, the voltage maximum calculation is returned. This allows using the voltage top to get a reasonable answer for either a square wave (ignoring the overshoot and preshoot) or a triangle wave (where a histogram fails). |
| Voltage Base | 1006 | Corresponds to the NISCOPE_VAL_VOLTAGE_BASE C or C++ command. If the histogram bin corresponding to voltage low has over five percent of the total hits, the voltage low result is returned. Otherwise, the voltage minimum calculation is returned. Otherwise, the voltage minimum calculation is returned. This allows using the voltage base to get a reasonable answer for either a square wave (ignoring the overshoot and preshoot) or a triangle wave (where a histogram fails). |
| Voltage Base-to-Top | 1017 | Corresponds to the NISCOPE_VAL_VOLTAGE_BASE_TO_TOP C or C++ command. Voltage Base-to-Top is calculated by subtracting voltage base from voltage top. |
| Negative Width | 11 | Corresponds to the NISCOPE_VAL_WIDTH_NEG C or C++ command. The time difference between the first two mid reference level crossings, where the slopes are negative and positive, respectively. A digital hysteresis is used when finding the crosspoints. |
| Positive Width | 12 | Corresponds to the NISCOPE_VAL_WIDTH_POS C or C++ command. The time difference, in seconds, between the first two mid reference level crossings, where the slopes are positive and negative respectively. A digital hysteresis is used when finding the crosspoints. |
| Negative Duty Cycle | 13 | Corresponds to the NISCOPE_VAL_DITY_CYCLE_NEG C or C++ command. The negative duty cycle is the negative width divided by the period times 100. |
| Positive Duty Cycle | 14 | Corresponds to the NISCOPE_VAL_DUTY_CYCLE_POS C or C++ command. Positive duty cycle is the positive width divided by the period times 100. |
| Integral | 1005 | Corresponds to the NISCOPE_VAL_INTEGRAL C or C++ command. Performs numerical integration using Simpson's rule, in units of volts × seconds. |
| Area | 1003 | Corresponds to the NISCOPE_VAL_AREA C or C++ command. Calculates the area between two points using the following equation:area = voltage average × numPoints × delta time |
| Cycle Area | 1004 | Corresponds to the NISCOPE_VAL_CYCLE C or C++ command. Uses the following equation:Cycle area = voltage cycle average × pointsPerPeriod × dtwhere pointsPerPeriod = period / dt. |
| Time Delay | 1014 | Corresponds to the NISCOPE_VAL_TIME_DELAY C or C++ command. The algorithm finds the first time, in seconds, that the waveform from the channel specified by the channel parameter crosses its mid-reference level. Next, the algorithm finds the first two times that the waveform from the Other Channel property crosses its mid-reference level.Note If you want to measure from falling edge to falling edge, you can invert the data from both channels by adding a processing step and using the array measurement gain with a value of -1. With this method, you can also measure from rising edge to falling edge or from falling edge to rising edge by inverting a signal on one of the two channels. The mid-reference level is stored on a per channel basis, and mid-reference levels do not need to be the same. All reference levels use a digital hysteresis. |
| Phase Delay | 1018 | Corresponds to the NISCOPE_VAL_PHASE_DELAY C or C++ command. Phase Delay is the time delay divided by the period (of the waveform on the channel specified by the measurement node) times 360 degrees. |
| Low Ref Volts | 1000 | Corresponds to the NISCOPE_VAL_LOW_REF_VOLTS C or C++ command. The voltage corresponding to the low reference level. If the Reference Level Units property is set to Voltage, the value of the Channel Based Low Ref Level property is returned.If the Reference Level Units property is set to Percentage, the voltage is calculated with the method specified by the Percentage Units Method property. |
| Mid Ref Volts | 1001 | Corresponds to the NISCOPE_VAL_MID_REF_VOLTS C or C++ command. The voltage corresponding to the mid reference level. If the Reference Level Units property is set to Voltage, the value of the Channel Based Mid Ref property is returned.If the Reference Level Units is set to Percentage, the voltage is calculated with the method specified by the Percentage Units Method property. |
| High Ref Volts | 1002 | Corresponds to the NISCOPE_VAL_HIGH_REF_VOLTS C or C++ command. The voltage corresponding to the high reference level. If the Reference Level Units property is set to Voltage, the value of the Channel Based High Ref property is returned.If the Reference Level Units property is set to Percentage, the voltage is calculated with the method specified by the Percentage Units Method property. |
| Volt. Hist. Mean | 2000 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN C or C++ command. Histogram Mean = [∑(bin hits × bin value) ] / volt hist hitsThe bin value is the center voltage value of the histogram bin. |
| Volt. Hist. Stdev | 2001 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV command. Histogram Stdev = √∑[bin hits × (bin value - histogram mean)2]/(total hits - 1) |
| Volt. Hist. Median | 2003 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN C or C++ command. The bin value where half the histogram hits are above it and half the histogram hits are below. |
| Volt Hist. Mode | 2010 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE C or C++ command. The bin value with the most hits. If there is a tie, the lower voltage or time value is returned. |
| Volt. Hist. Max | 2005 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX C or C++ command. The highest bin value with at least one hit. |
| Volt. Hist. Min | 2006 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN C or C++ command. The lowest bin value with at least one hit. |
| Volt. Hist. Peak to Peak | 2002 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK C or C++ command. Histogram maximum minus the histogram minimum. |
| Volt. Hist. Mean + Stdev | 2007 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV C or C++ command. The percentage of hits in the histogram between mean minus the standard deviation and mean plus the standard deviation. The percentage is returned in the range 0-100. |
| Volt. Hist. Mean + 2 Stdev | 2008 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV C or C++ command. The percentage of hits in the histogram between the mean minus two times the standard deviation and the mean plus to times the standard deviation.The percentage is returned in the range 0-100. |
| Volt. Hist. Mean + 3 Stdev | 2009 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV C or C++ command. The percentage of hits in the histogram between the mean minus three times the standard deviation and the mean plus three times the standard deviation. The percentage is returned in the range 0-100. |
| Volt. Hist. Hits | 2004 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS C or C++ command. Number of points in the histogram. |
| Volt. Hist. New Hits | 2011 | Corresponds to the NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS C or C++ command. Number of points added to the histogram by the most recent acquisition. |
| Time Hist. Mean | 3000 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MEAN C or C++ command. Histogram Mean = [ Σ (bin hits × bin value) ] / time hist hits.The bin value is the center time value of the histogram bin. |
| Time Hist. Stdev | 3001 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_STDEV C or C++ command. Histogram Stdev = √Σ[bin hits × (bin value - histogram mean)2]/(total hits - 1) |
| Time Hist. Median | 3003 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MEDIA C or C++ command. The bin value where half the histogram hits are above it and half the histogram hits are below. |
| Time Hist. Mode | 3010 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MODE C or C++ command. The bin value with the most hits. If there is a tie, the lower voltage or time value is returned. |
| Time Hist. Max | 3005 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MAX C or C++ command. The highest bin value with at least one hit. |
| Time Hist. Min | 3006 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MIN C or C++ command. The lowest bin value with at least one hit. |
| Time Hist. Peak-to-Peak | 3002 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK C or C++ command. Histogram maximum minus the histogram minimum. |
| Time Hist. Mean + Stdev | 3007 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV C or C++ command. The percentage of hits in the histogram between mean minus the standard deviation and mean plus the standard deviation. The percentage is returned in the range 0-100. |
| Time Hist. Mean + 2 Stdev | 3008 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV C or C++ command. The percentage of hits in the histogram between the mean minus two times the standard deviation and the mean plus two times the standard deviation. The percentage is returned in the range 0-100. |
| Time Hist. Mean + 3 Stdev | 3009 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_3_STDEV C or C++ command. The percentage of hits in the histogram between the mean minus three times the standard deviation and the mean plus three times the standard deviation. The percentage is returned in the range 0-100. |
| Time Hist. Hits | 3004 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_HITS C or C++ command. Number of points in the histogram. |
| Time Hist. New Hits | 3011 | Corresponds to the NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS C or C++ command. Number of points added to the histogram by the most recent acquisition. |

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

The time, in seconds, to wait for the data to be acquired.

Default value: 5

##### Alternate Uses

Use 
 0 for this parameter to fetch whatever is currently available. Use 
 -1 for this parameter to imply an infinite timeout.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### result

The acquired measurement.

Parent topic:

Read Measurement

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=read.html language=enus -->
## TOPIC 00022: Read

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `read.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/read.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates an acquisition, waits for it to complete, and acquires data.

Read

Initiates an acquisition, waits for it to complete, and acquires data.

Waveform Acquisition

NI-SCOPE functions for waveform acquisition.

Parent topic:

Waveform Acquisition

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=reset-reset-device.html language=enus -->
## TOPIC 00023: Reset Device

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `reset-reset-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/reset-reset-device.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a hard reset of the device. During a hard reset, acquisition stops, all routes are released, RTSI and PFI lines are tri-stated, FPGAs are reset, hardware is configured to its default state, and all session attributes are reset to their default states. session in Handle that identifies the N

Reset Device

Performs a hard reset of the device.

During a hard reset, acquisition stops, all routes are released, RTSI and PFI lines are tri-stated, FPGAs are reset, hardware is configured to its default state, and all session attributes are reset to their default states.

[IMAGE alt='1378' src='Reset_Device.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Reset

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=revision-query.html language=enus -->
## TOPIC 00024: Revision Query

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `revision-query.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/revision-query.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision numbers of the instrument driver and instrument firmware. session in Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options . error in Error conditions that occur before this node runs. The node responds to this input according

Revision Query

Returns the revision numbers of the instrument driver and instrument firmware.

[IMAGE alt='1378' src='Revision_Query.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### instrument driver revision

The instrument driver software revision numbers.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### firmware revision

The instrument firmware revision numbers.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=self-calibrate.html language=enus -->
## TOPIC 00025: Self Calibrate

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `self-calibrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/self-calibrate.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Self-calibrates most NI digitizers, including all SMC-based devices. session in Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options . error in Error conditions that occur before this node runs. The node responds to this input according to standar

Self Calibrate

Self-calibrates most NI digitizers, including all SMC-based devices.

[IMAGE alt='1378' src='Self_Calibrate.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channels

The channel(s) to calibrate.

##### Channel String Syntax

This input parameter has the following syntax options:

- A single channel, such as
 0
- A list of channels, such as 
 0,1 or 
 3,2,1,0
- A range of channels, such as
 0-7 or 0:7
- All channels, which is designated by an empty
 string
- A combination of channels from multiple instruments,
 such as PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3

Note

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### option

Self-calibrates all channels or restores the external calibration.

| Self Calibrate All Channels | 0 | Performs a self-calibration on all available channels. |
| --- | --- | --- |
| Restore External Calibration | 1 | Restores the external calibration. |

Default value: Self Calibrate All Channels

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Self-Calibrating SMC-Based Devices

Close External Calibration

action

Store Calibration

Note

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=self-test.html language=enus -->
## TOPIC 00026: Self-Test

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/self-test.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs the device self-test routine and returns the test result(s). session in Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options . error in Error conditions that occur before this node runs. The node responds to this input according to standard e

Self-Test

Runs the device self-test routine and returns the test result(s).

[IMAGE alt='1378' src='Self-Test.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### self-test result

The value returned from the device self-test.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### self-test message

The self-test response string from the device.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=send-software-trigger-edge.html language=enus -->
## TOPIC 00027: Send Software Trigger Edge

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `send-software-trigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/send-software-trigger-edge.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the selected trigger to the digitizer. You can also call this node to override a misused edge, digital, or hysteresis reference trigger. session in Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options . error in Error conditions that occur b

Send Software Trigger Edge

Sends the selected trigger to the digitizer.

You can also call this node to override a misused edge, digital, or hysteresis reference trigger.

[IMAGE alt='1378' src='Send_Software_Trigger_Edge.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies the NI-SCOPE instrument session as previously allocated by Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### trigger type

The type of trigger to send to the digitizer.

| Start Trigger | 0 | Sends the start trigger to the digitizer. |
| --- | --- | --- |
| Arm Reference Trigger | 1 | Sends the arm reference trigger to the digitizer. |
| Reference Trigger | 2 | Sends the reference trigger to the digitizer. |
| Advance Trigger | 3 | Sends the advance trigger to the digitizer. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Using with Configure Trigger

Configure Trigger

Parent topic:

Low Level Acquisition

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=set-accessory-source-calibration.html language=enus -->
## TOPIC 00028: Set Accessory Source Calibration

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `set-accessory-source-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/set-accessory-source-calibration.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the PXI-5900 PXI RF Amplifier, this node connects the specified channel to the calibration source and sets the calibration source to ±10 V or to GND. session in The instrument handle that you obtain from Initialize External Calibration. The handle identifies a particular instrument session. erro

Set Accessory Source Calibration

For the PXI-5900 PXI RF Amplifier, this node connects the specified channel to the calibration source and sets the calibration source to ±10 V or to GND.

[IMAGE alt='1378' src='Set_Accessory_Source_Calibration.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The instrument handle that you obtain from Initialize External Calibration. The handle identifies a particular instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channels

The channel(s) to calibrate.

##### Channel String Syntax

This input parameter has the following syntax options:

- A single channel, such as
 0
- A list of channels, such as 
 0,1 or 
 3,2,1,0
- A range of channels, such as
 0-7 or 0:7
- All channels, which is designated by an empty
 string
- A combination of channels from multiple instruments,
 such as PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3

Note

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### calibration source

The source of the calibration signal.

| +10V | 1 | Ground plus 10 volts. |
| --- | --- | --- |
| GND | 0 | Ground. |
| -10V | 2 | Ground minus 10 volts. |

Default value: GND

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=set-calibration-user-defined-info.html language=enus -->
## TOPIC 00029: Set Calibration User-Defined Info

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `set-calibration-user-defined-info.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/set-calibration-user-defined-info.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allows you to store miscellaneous information in the EEPROM of a device. For example, you can store an operator ID for the person or company performing a calibration. The information is stored immediately. session in The instrument handle that you obtain from Initialize External Calibration. The han

Set Calibration User-Defined Info

Allows you to store miscellaneous information in the EEPROM of a device.

For example, you can store an operator ID for the person or company performing a calibration. The information is stored immediately.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

The instrument handle that you obtain from Initialize External Calibration. The handle identifies a particular instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### info

Four characters that are stored in the EEPROM of the device.

This parameter can contain fewer than four characters if it is NULL-terminated.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to the NI-SCOPE instrument session to pass to the next node in the program.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Valid Characters

NULL

NULL

NULL

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=trigger-category.html language=enus -->
## TOPIC 00030: Trigger

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `trigger-category.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/trigger-category.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Functions to configure triggers in NI-SCOPE.

Trigger

Functions to configure triggers in NI-SCOPE.

Configuration

Use the NI-SCOPE Configuration functions to set up the parameters of your acquisition, or use Auto Setup to automatically configure device settings.

Configure Trigger

Configures the oscilloscope for different types of triggering.

Export Signal

Configures the digitizer to generate a signal that other devices can detect when configured for digital triggering or sharing clocks.

Get NI-TClk Session Reference

Extracts a session that can be passed to NI-TClk nodes.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=utility-category.html language=enus -->
## TOPIC 00031: Utility

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `utility-category.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/utility-category.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Utility functions for NI-SCOPE.

Utility

Utility functions for NI-SCOPE.

NI-SCOPE Nodes

Nodes for programming oscilloscopes.

CableSense Signal Start

Generates the CableSense signal on all channels of an oscilloscope for which the signal is enabled, as configured by the CableSense Mode property.

CableSense Signal Stop

Disables the CableSense signal on all channels of an oscilloscope for which the signal is enabled.

Error Message

Takes the error code returned by NI-SCOPE functions and returns the interpretation as a user-readable string.

Get Channel Name

Returns a comma-delimited list of channel names.

Get Stream Endpoint Handle

Returns a writer endpoint that can be used with NI-P2P to configure a peer-to-peer stream with a digitizer endpoint.

Probe Compensation Signal Start

1 kHz

Probe Compensation Signal Stop

1 kHz

Reset

Resets the device.

Revision Query

Returns the revision numbers of the instrument driver and instrument firmware.

Self-Test

Runs the device self-test routine and returns the test result(s).

Parent topic:

NI-SCOPE Nodes

<!--NI_TOPIC bundle=ni-scope-20.0-lvnxg-api-ref path=waveform-acquisition-category.html language=enus -->
## TOPIC 00032: Waveform Acquisition

- bundle_id: `ni-scope-20.0-lvnxg-api-ref`
- source_path: `waveform-acquisition-category.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-20.0-lvnxg-api-ref/raw/resource/enus/waveform-acquisition-category.html
- document_id: `ni-scope-20.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: NI-SCOPE functions for waveform acquisition.

Waveform Acquisition

NI-SCOPE functions for waveform acquisition.

NI-SCOPE Nodes

Nodes for programming oscilloscopes.

Low Level Acquisition

Low level acquisition functions for NI-SCOPE.

Read

Initiates an acquisition, waits for it to complete, and acquires data.

Parent topic:

NI-SCOPE Nodes
