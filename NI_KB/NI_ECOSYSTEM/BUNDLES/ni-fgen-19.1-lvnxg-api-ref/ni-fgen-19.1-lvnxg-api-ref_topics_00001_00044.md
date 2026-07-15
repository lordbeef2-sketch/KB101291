# NI DOCUMENT BUNDLE: ni-fgen-19.1-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-fgen-19.1-lvnxg-api-ref start=1 end=44 -->
<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=adjust-flatness-calibration.html language=enus -->
## TOPIC 00001: Adjust Flatness Calibration

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `adjust-flatness-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/adjust-flatness-calibration.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration constants pertaining to flatness. During external calibration, the waveform generator is configured with the different analog settings, and measurements are taken of the resulting output voltage at different frequencies. Using the configuration data and the measurements, this

Adjust Flatness Calibration

Calculates calibration constants pertaining to flatness.

During external calibration, the waveform generator is configured with the different analog settings, and measurements are taken of the resulting output voltage at different frequencies. Using the configuration data and the measurements, this node calculates the appropriate calibration constants and, when the calibration session is committed, stores them in the onboard EEPROM.

[IMAGE alt='1378' src='Adjust_Flatness_Calibration.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### frequencies array

Frequencies at which different sine tones were generated in hertz (Hz).

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### configuration

Configuration of the waveform generator for this stage of calibration.

| NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_0DB | 0 | The waveform generator was configured to use the low-gain amplifier path with preamplifier gain of 0 dB. |
| --- | --- | --- |
| NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_3DB | 1 | The waveform generator was configured to use the low-gain amplifier path with preamplifier gain of -3 dB. |
| NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_6DB | 2 | The waveform generator was configured to use the low-gain amplifier path with preamplifier gain of -6 dB. |
| NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_9DB | 3 | The waveform generator was configured to use the low-gain amplifier path with preamplifier gain of -9 dB. |
| NIFGEN_VAL_CAL_CONFIG_LOW_GAIN_PATH_PRE_AMP_12DB | 4 | The waveform generator was configured to use the low-gain amplifier path with preamplifier gain of -12 dB. |
| NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_0DB | 5 | The waveform generator was configured to use the high-gain amplifier path with preamplifier gain of 0 dB. |
| NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_3DB | 6 | The waveform generator was configured to use the high-gain amplifier path with preamplifier gain of -3 dB. |
| NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_6DB | 7 | The waveform generator was configured to use the high-gain amplifier path with preamplifier gain of -6 dB. |
| NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_9DB | 8 | The waveform generator was configured to use the high-gain amplifier path with preamplifier gain of -9 dB. |
| NIFGEN_VAL_CAL_CONFIG_HIGH_GAIN_PATH_PRE_AMP_12DB | 9 | The waveform generator was configured to use the high-gain amplifier path with preamplifier gain of -12 dB. |
| NIFGEN_VAL_CAL_CONFIG_DIRECT_PATH | 10 | The waveform generator was configured to use the direct path. |
| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_0DB | 12 | The waveform generator was configured to use the main path with preamplifier gain of 0 dB. |
| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_9DB | 13 | The waveform generator was configured to use the main path with preamplifier gain of -9 dB. |
| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_33DB | 14 | The waveform generator was configured to use the main path with preamplifier gain of -33 dB. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### requested amplitude

Amplitude used to generate the sine tones at different frequencies in volts (V).

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### measured amplitudes array

Amplitudes measured for each corresponding frequency in the frequencies array input in volts (V).

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Flatness Control Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=adjust-main-path-pre-amp-offset-calibration.html language=enus -->
## TOPIC 00002: Adjust Main Path Pre Amp Offset Calibration

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `adjust-main-path-pre-amp-offset-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/adjust-main-path-pre-amp-offset-calibration.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates calibration constants pertaining to the preamplifier gain of the main analog path. During external calibration, you can put the waveform generator in different configurations; program different gain, offset, and main DAC values; and take measurements of the resulting output voltages. Usin

Adjust Main Path Pre Amp Offset Calibration

Calculates calibration constants pertaining to the preamplifier gain of the main analog path.

During external calibration, you can put the waveform generator in different configurations; program different gain, offset, and main DAC values; and take measurements of the resulting output voltages. Using the configuration data and the measurements, this node calculates the appropriate calibration constants and, when the calibration session is committed, stores them in the onboard EEPROM.

[IMAGE alt='1378' src='Adjust_Main_Path_Pre_Amp_Offset_Calibration.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### configuration

Configuration of the waveform generator for this stage of calibration.

| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_0DB | 0 | The waveform generator was configured to have the analog filter disabled and preamplifier gain of 0 dB. |
| --- | --- | --- |
| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_3DB | 1 | The waveform generator was configured to have the analog filter disabled and preamplifier gain of -3 dB. |
| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_6DB | 2 | The waveform generator was configured to have the analog filter disabled and preamplifier gain of -6 dB. |
| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_9DB | 3 | The waveform generator was configured to have the analog filter disabled and preamplifier gain of -9 dB. |
| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_OFF_12DB | 4 | The waveform generator was configured to have the analog filter disabled and preamplifier gain of -12 dB. |
| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_0DB | 5 | The waveform generator was configured to have the analog filter enabled and preamplifier gain of 0 dB. |
| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_3DB | 6 | The waveform generator was configured to have the analog filter enabled and preamplifier gain of -3 dB. |
| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_6DB | 7 | The waveform generator was configured to have the analog filter enabled and preamplifier gain of -6 dB. |
| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_9DB | 8 | The waveform generator was configured to have the analog filter enabled and preamplifier gain of -9 dB. |
| NIFGEN_VAL_CAL_CONFIG_MAIN_PATH_FILTER_ON_12DB | 9 | The waveform generator was configured to have the analog filter enabled and preamplifier gain of -12 dB. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### gain DAC values

Array of the values programmed to the gain calibration DAC during this calibration stage.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### measured outputs

Array of the analog output voltages measured during this calibration stage.

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### offset DAC values

Array of the values programmed to the offset calibration DAC during this calibration stage.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Analog Output Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=adjust-sample-clock-relative-delay.html language=enus -->
## TOPIC 00003: Adjust Sample Clock Relative Delay

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `adjust-sample-clock-relative-delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/adjust-sample-clock-relative-delay.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Delays (or phase shifts) the Sample Clock, which delays the output of the waveform generator. The delay takes effect immediately after this node is called. Delaying the Sample Clock can be useful when lining up the output of multiple instruments or when intentionally phase shifting the output relati

Adjust Sample Clock Relative Delay

Delays (or phase shifts) the Sample Clock, which delays the output of the waveform generator.

The delay takes effect immediately after this node is called. Delaying the Sample Clock can be useful when lining up the output of multiple instruments or when intentionally phase shifting the output relative to a fixed reference, such as the PLL Reference Clock.

[IMAGE alt='1378' src='Adjust_Sample_Clock_Relative_Delay.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### adjustment time

Amount of time to adjust the Sample Clock delay in seconds (s).

adjustment time can be positive or negative, but it must be less than or equal to the Sample Clock period.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Calling this node after calling NI-TClk Synchronize breaks synchronization.

#### Delaying an External Sample Clock

To delay an external Sample Clock, set the Sample Clock Absolute Delay property.

Parent topic:

Clock Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=analog-output-nodes.html language=enus -->
## TOPIC 00004: Analog Output Nodes

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `analog-output-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/analog-output-nodes.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN analog output nodes only when following the calibration DC gain and offset portion of the waveform generator calibration procedure.

Analog Output Nodes

Use the NI-FGEN analog output nodes only when following the calibration DC gain and offset portion of the waveform generator calibration procedure.

External Calibration Nodes

NI-FGEN

waveform generator

Adjust Direct Path Gain Calibration

Calculates calibration constants pertaining to the gain of the direct analog path.

Adjust Direct Path Output Impedance Calibration

Calculates calibration constants pertaining to direct analog path output impedance.

Adjust Main Path Output Impedance Calibration

Calculates calibration constants pertaining to main analog path output impedance.

Adjust Main Path Pre Amp Gain Calibration

Calculates calibration constants pertaining to the preamplifier gain of the main analog path.

Adjust Main Path Pre Amp Offset Calibration

Calculates calibration constants pertaining to the preamplifier gain of the main analog path.

Adjust Main Path Post Amp Gain And Offset Calibration

Calculates calibration constants pertaining to the postamplifier gain and offset of the main analog path.

Initialize Analog Output Calibration

waveform generator

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=arbsequence-waveform-nodes.html language=enus -->
## TOPIC 00005: ArbSequence Waveform Nodes

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `arbsequence-waveform-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/arbsequence-waveform-nodes.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN arbitrary sequence waveform nodes to configure, define, and clear an arbitrary sequence.

ArbSequence Waveform Nodes

Use the NI-FGEN arbitrary sequence waveform nodes to configure, define, and clear an arbitrary sequence.

Configuration Nodes

NI-FGEN

waveform generator

Clear Arbitrary Sequence

waveform generator

Configure Arbitrary Sequence

waveform generator

Create Advanced Arbitrary Sequence

Creates an arbitrary sequence from an array of waveform references and an array of corresponding loop counts with the ability to set the number of samples in each sequence step and to set marker locations.

Create Arbitrary Sequence

Creates an arbitrary sequence from an array of waveform references and an array of corresponding loop counts.

Query Arbitrary Sequence Capabilities

waveform generator

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=clear-arbitrary-memory.html language=enus -->
## TOPIC 00006: Clear Arbitrary Memory

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `clear-arbitrary-memory.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/clear-arbitrary-memory.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes all previously created arbitrary waveforms, sequences, and scripts from the waveform generator memory and invalidates all waveform references, sequence references, and waveform names. The waveform generator must not be in the Generating state when you call this node. session in Handle that i

Clear Arbitrary Memory

Removes all previously created arbitrary waveforms, sequences, and scripts from the waveform generator memory and invalidates all waveform references, sequence references, and waveform names.

The waveform generator must not be in the Generating state when you call this node.

[IMAGE alt='1378' src='Clear_Arbitrary_Memory.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Arbitrary Waveform Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=clear-frequency-list.html language=enus -->
## TOPIC 00007: Clear Frequency List

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `clear-frequency-list.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/clear-frequency-list.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a previously created frequency list from the waveform generator memory and invalidates the handle of the specified frequency list. The waveform generator must not be in the Generating state when you call this node. session in Handle that identifies your instrument session previously allocate

Clear Frequency List

Removes a previously created frequency list from the waveform generator memory and invalidates the handle of the specified frequency list.

The waveform generator must not be in the Generating state when you call this node.

[IMAGE alt='1378' src='Clear_Frequency_List.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### frequency list reference

Handle of the frequency list you want the waveform generator to remove.

You can create multiple frequency lists using Create Frequency List, which returns a reference that you use to identify each list. Specify a value of 
 -1 to clear all frequency lists.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

List Mode Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=clear-user-standard-waveform.html language=enus -->
## TOPIC 00008: Clear User Standard Waveform

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `clear-user-standard-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/clear-user-standard-waveform.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a previously created user-defined waveform created by Define User Standard Waveform from the waveform generator memory and invalidates the handle of the specified frequency list. session in Handle that identifies your instrument session previously allocated by Initialize With Channels. error

Clear User Standard Waveform

Removes a previously created user-defined waveform created by Define User Standard Waveform from the waveform generator memory and invalidates the handle of the specified frequency list.

[IMAGE alt='1378' src='Clear_User_Standard_Waveform.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Standard Waveform Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=clock-nodes.html language=enus -->
## TOPIC 00009: Clock Nodes

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `clock-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/clock-nodes.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN clock nodes to configure waveform generator clocking and data generation speed.

Clock Nodes

Use the NI-FGEN clock nodes to configure waveform generator clocking and data generation speed.

Configuration Nodes

NI-FGEN

waveform generator

Adjust Sample Clock Relative Delay

waveform generator

Configure Clock Mode

waveform generator

Configure Reference Clock

waveform generator

Configure Sample Clock Source

waveform generator

Set Sample Rate

waveform generator

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=close-external-calibration.html language=enus -->
## TOPIC 00010: Close External Calibration

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `close-external-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/close-external-calibration.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM. session in Handle that identifies your instrument session previously allocated by Initialize External Calibration. error in Error

Close External Calibration

Closes an external calibration session and, if specified, stores the new calibration constants and calibration data, such as time and temperature, in the onboard EEPROM.

[IMAGE alt='1378' src='Close_External_Calibration.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### action

Action the node performs upon closing the external calibration session.

| NIFGEN_VAL_EXT_CAL_ABORT | 0 | Disregards the new calibration constants before closing. |
| --- | --- | --- |
| NIFGEN_VAL_EXT_CAL_COMMIT | 1 | Stores the new calibration constants in the waveform generator EEPROM before closing. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

External Calibration Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=commit.html language=enus -->
## TOPIC 00011: Commit

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `commit.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/commit.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Causes a transition to the Committed state. Verifies property values, reserves the waveform generator, and commits the property values to the waveform generator. If the property values are all valid, the waveform generator hardware configuration is set to match the session configuration. Waveforms,

Commit

Causes a transition to the Committed state. Verifies property values, reserves the waveform generator, and commits the property values to the waveform generator.

If the property values are all valid, the waveform generator hardware configuration is set to match the session configuration. Waveforms, scripts, and sequences can be loaded into memory when the session is in the Committed state.

If any properties are changed, the session transitions back to the Idle state. This node has no effect if the waveform generator is already in the Committed or Generating states and returns a successful status value.

[IMAGE alt='1378' src='Commit.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node does not support the PXI-5404.

#### Programming Patterns

Initiate Generation

- Routes are committed, so signals are exported or imported.
- Any Reference Clock and External Clock circuits are phase-locked.
- A subsequent Initiate Generation can run faster because the waveform generator is already configured.

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=configure-arbitrary-sequence.html language=enus -->
## TOPIC 00012: Configure Arbitrary Sequence

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `configure-arbitrary-sequence.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/configure-arbitrary-sequence.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the waveform generator properties that affect arbitrary sequence generation, selecting the arbitrary sequence to produce and setting the gain and offset. The waveform generator must not be in the Generating state when you call this node. offset Offset value the waveform generator adds to

Configure Arbitrary Sequence

Configures the waveform generator properties that affect arbitrary sequence generation, selecting the arbitrary sequence to produce and setting the gain and offset.

The waveform generator must not be in the Generating state when you call this node.

[IMAGE alt='1378' src='Configure_Arbitrary_Sequence.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### offset

Offset value the waveform generator adds to the arbitrary waveform in volts (V).

When you create an arbitrary waveform, you must first normalize the data points to a range of -1.00 to +1.00. You can use this input to shift the range of the arbitrary waveform.

For example, to configure the output signal to range from 0.00 V to 2.00 V, set offset to 
 1.00.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### gain

Factor by which the waveform generator scales the arbitrary waveforms in the sequence.

When you create an arbitrary waveform, you must first normalize the data points to a range of -1.00 to +1.00. You can use this input to scale the waveform to other ranges. The gain is applied before the offset is added.

For example, to configure the output signal to range from -2.00 V to +2.00 V, set gain to 2.00.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### sequence reference

The handle of the arbitrary sequence to produce.

Wire the sequence reference output of Create Arbitrary Sequence or Create Advanced Arbitrary Sequence to this input to specify the sequence.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

You must set the output mode input of Configure Output Mode to 
 arbitrary sequence before calling this node.

Parent topic:

ArbSequence Waveform Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=configure-arbitrary-waveform.html language=enus -->
## TOPIC 00013: Configure Arbitrary Waveform

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `configure-arbitrary-waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/configure-arbitrary-waveform.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the properties of the waveform generator that affect arbitrary waveform generation, selecting the arbitrary waveform to produce and setting the gain and offset. The waveform generator must not be in the Generating state when you call this node. offset Offset value the waveform generator a

Configure Arbitrary Waveform

Configures the properties of the waveform generator that affect arbitrary waveform generation, selecting the arbitrary waveform to produce and setting the gain and offset.

The waveform generator must not be in the Generating state when you call this node.

[IMAGE alt='1378' src='Configure_Arbitrary_Waveform.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### offset

Offset value the waveform generator adds to the arbitrary waveform in volts (V).

When you create an arbitrary waveform, you must first normalize the data points to a range of -1.00 to +1.00. You can use this input to shift the range of the arbitrary waveform.

For example, to configure the output signal to range from 0.00 V to 2.00 V, set offset to 
 1.00.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### gain

Factor by which the waveform generator scales the arbitrary waveforms in the sequence.

When you create an arbitrary waveform, you must first normalize the data points to a range of -1.00 to +1.00. You can use this input to scale the waveform to other ranges. The gain is applied before the offset is added.

For example, to configure the output signal to range from -2.00 V to +2.00 V, set gain to 2.00.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### waveform reference in

Arbitrary waveform to produce.

You can create multiple arbitrary waveforms using Create Waveform, which returns a reference that you use to identify each waveform.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

You must set the output mode input of Configure Output Mode to 
 arbitrary waveform before calling this node.

Parent topic:

Arbitrary Waveform Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=configure-channels.html language=enus -->
## TOPIC 00014: Configure Channels

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `configure-channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/configure-channels.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the channels that are used with the waveform generator instrument. If you call this node, you must call it immediately after initializing your session and before configuring any properties or writing data. session in Handle that identifies your instrument session previously allocated by I

Configure Channels

Configures the channels that are used with the waveform generator instrument.

If you call this node, you must call it immediately after initializing your session and before configuring any properties or writing data.

[IMAGE alt='1378' src='Configure_Channels.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channels

Non-negative integer representing the channel or channels that all subsequent channel-based properties in the session set.

0 is the only valid value on waveform generators with one channel, however waveform generators with two channels support values of 0 and 1. You can specify more than one channel by inserting a comma between values.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=configure-clock-mode.html language=enus -->
## TOPIC 00015: Configure Clock Mode

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `configure-clock-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/configure-clock-mode.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the clock mode for the waveform generator. The waveform generator must not be in the Generating state when you call this node. session in Handle that identifies your instrument session previously allocated by Initialize With Channels. error in Error conditions that occur before this node run

Configure Clock Mode

Selects the clock mode for the waveform generator.

The waveform generator must not be in the Generating state when you call this node.

[IMAGE alt='1378' src='Configure_Clock_Mode.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### clock mode

The clock mode of the waveform generator.

| Hi Resolution Sampling | 0 | Sample rate is generated by a high-resolution clock source and can be set to any value. |
| --- | --- | --- |
| Divide Down Sampling | 1 | Sample rate is rounded to a frequency that can be achieved by dividing down the onboard Sample Clock Timebase. |
| Automatic | 2 | The node selects either Hi Resolution Sampling or Divide Down Sampling based on the sample rate, using divide down sampling when possible. |

Default value: Divide-Down Sampling

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

You must set the output mode input of Configure Output Mode to 
 arbitrary waveform or 
 arbitrary sequence before calling this node.

Parent topic:

Clock Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=configure-custom-fir-filter-coefficients.html language=enus -->
## TOPIC 00016: Configure Custom FIR Filter Coefficients

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `configure-custom-fir-filter-coefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/configure-custom-fir-filter-coefficients.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the FIR filter coefficients used by the onboard signal processing block. The values are coerced to the closest settings achievable by the waveform generator. The waveform generator must not be in the Generating state when you call this node. session in Handle that identifies your instrument ses

Configure Custom FIR Filter Coefficients

Sets the FIR filter coefficients used by the onboard signal processing block. The values are coerced to the closest settings achievable by the waveform generator.

The waveform generator must not be in the Generating state when you call this node.

[IMAGE alt='1378' src='Configure_Custom_FIR_Filter_Coefficients.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### FIR filter coefficients

Array of data that the onboard signal processor uses for the FIR filter coefficients.

The coefficients should range between -1.00 and +1.00. You must wire a symmetric array of 95 coefficients to this input.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node is supported only for the PXI-5441.

Parent topic:

Filter Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=configure-digital-edge-script-trigger.html language=enus -->
## TOPIC 00017: Digital Edge

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `configure-digital-edge-script-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/configure-digital-edge-script-trigger.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a Script Trigger for edge triggering, setting the trigger source and edge to detect. The waveform generator must not be in the Generating state when you call this node. session in Handle that identifies your instrument session previously allocated by Initialize With Channels. trigger ID S

Digital Edge

Configures a Script Trigger for edge triggering, setting the trigger source and edge to detect.

The waveform generator must not be in the Generating state when you call this node.

[IMAGE alt='1378' src='Configure_Digital_Edge_Script_Trigger.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### trigger ID

Script Trigger used for triggering.

Default value: Script Trigger 0

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

Trigger source the waveform generator uses.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### edge

Edge to detect.

| Rising Edge | 101 | The node sets triggering for when the signal transitions from low level to high level. |
| --- | --- | --- |
| Falling Edge | 102 | The node sets triggering for when the signal transitions from high level to low level. |

Default value: Rising Edge

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=configure-digital-edge-start-trigger.html language=enus -->
## TOPIC 00018: Digital Edge

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `configure-digital-edge-start-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/configure-digital-edge-start-trigger.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start Trigger for edge triggering, setting the trigger source and edge to detect. The waveform generator must not be in the Generating state when you call this node. session in Handle that identifies your instrument session previously allocated by Initialize With Channels. source Trig

Digital Edge

Configures the Start Trigger for edge triggering, setting the trigger source and edge to detect.

The waveform generator must not be in the Generating state when you call this node.

[IMAGE alt='1378' src='Configure_Digital_Edge_Start_Trigger.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

Trigger source the waveform generator uses.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### edge

Edge to detect.

| Rising Edge | 101 | The node sets triggering for when the signal transitions from low level to high level. |
| --- | --- | --- |
| Falling Edge | 102 | The node sets triggering for when the signal transitions from high level to low level. |

Default value: Rising Edge

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configure Trigger

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=configure-digital-filter.html language=enus -->
## TOPIC 00019: Configure Digital Filter

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `configure-digital-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/configure-digital-filter.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables the digital filter for the waveform generator. You can apply the digital filter setting in arbitrary waveform, arbitrary sequence, or script output modes. When used with user-defined functions, the digital filter setting can also be applied in frequency list or standard function

Configure Digital Filter

Enables or disables the digital filter for the waveform generator.

You can apply the digital filter setting in arbitrary waveform, arbitrary sequence, or script output modes. When used with user-defined functions, the digital filter setting can also be applied in frequency list or standard function output modes.

[IMAGE alt='1378' src='Configure_Digital_Filter.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable

Boolean value that specifies whether or not to enable the digital filter.

| True | Enables the digital filter. |
| --- | --- |
| False | Disables the digital filter. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Filter Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=is-done.html language=enus -->
## TOPIC 00020: Is Done

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `is-done.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/is-done.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether or not the current generation has completed. This node returns True if the session is in the Idle or Committed states and only after the current generation is complete in Single Trigger mode. session in Handle that identifies your instrument session previously allocated by Initial

Is Done

Determines whether or not the current generation has completed.

This node returns 
 True if the session is in the Idle or Committed states and only after the current generation is complete in Single Trigger mode.

[IMAGE alt='1378' src='Is_Done.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### done

Boolean value that specifies whether or not the current generation has completed.

| True | The current generation has completed. The session is in the Idle or Committed states. |
| --- | --- |
| False | The current generation is still active. The session is in the Generating state. |

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=list-mode-nodes.html language=enus -->
## TOPIC 00021: List Mode Nodes

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `list-mode-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/list-mode-nodes.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN list mode nodes to configure, define, and clear a frequency list.

List Mode Nodes

Use the NI-FGEN list mode nodes to configure, define, and clear a frequency list.

Configuration Nodes

NI-FGEN

waveform generator

Clear Frequency List

waveform generator

Configure Frequency List

waveform generator

Create Frequency List

Creates a frequency list from an array of frequencies and an array of durations.

Query Freq List Capabilities

waveform generator

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=ni-fgen-nodes.html language=enus -->
## TOPIC 00022: NI-FGEN Nodes

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `ni-fgen-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/ni-fgen-nodes.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN nodes to develop applications for your NI waveform generator.

NI-FGEN Nodes

Use the NI-FGEN nodes to develop applications for your NI waveform generator.

Action Nodes

NI-FGEN

Calibration Nodes

NI-FGEN

waveform generator

waveform generator

Close

NI-FGEN

NI-FGEN

Configuration Nodes

NI-FGEN

waveform generator

Initialize With Channels

NI-FGEN

waveform generator

NI-FGEN

NI-FGEN Properties

Sets, gets, or checks properties.

Utility Nodes

NI-FGEN

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=nifgen-properties.html language=enus -->
## TOPIC 00023: NI-FGEN Properties

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `nifgen-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/nifgen-properties.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets, gets, or checks properties. Some NI-FGEN properties are channel based. When a property is channel based, you can specify an active channel before setting, getting, or checking properties. nifgen in Handle that identifies your instrument session. error in Error conditions that occur before this

NI-FGEN Properties

Sets, gets, or checks properties.

Some NI-FGEN properties are channel based. When a property is channel based, you can specify an active channel before setting, getting, or checking properties.

[IMAGE alt='1378' src='PropertyNode.niFgen.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### nifgen in

Handle that identifies your instrument session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### nifgen out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

NI-FGEN Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=output-enable.html language=enus -->
## TOPIC 00024: Output Enable

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `output-enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/output-enable.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the waveform generator to generate a signal at the channel output connector. session in Handle that identifies your instrument session previously allocated by Initialize With Channels. error in Error conditions that occur before this node runs. The node responds to this input according to

Output Enable

Configures the waveform generator to generate a signal at the channel output connector.

[IMAGE alt='1378' src='Output_Enable.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### output enable

Boolean value that specifies whether or not to enable the output enable relay.

| True | Enables the relay. |
| --- | --- |
| False | Disables the relay. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=query-arbitrary-sequence-capabilities.html language=enus -->
## TOPIC 00025: Query Arbitrary Sequence Capabilities

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `query-arbitrary-sequence-capabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/query-arbitrary-sequence-capabilities.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the properties of the waveform generator that are related to creating arbitrary sequences. session in Handle that identifies your instrument session previously allocated by Initialize With Channels. error in Error conditions that occur before this node runs. The node responds to this input a

Query Arbitrary Sequence Capabilities

Returns the properties of the waveform generator that are related to creating arbitrary sequences.

[IMAGE alt='1378' src='Query_Arbitrary_Sequence_Capabilities.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maximum number of sequences

Maximum number of arbitrary waveform sequences that the waveform generator supports.

On some waveform generators, this value may vary with remaining onboard memory.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### minimum sequence length

Minimum number of arbitrary waveforms the waveform generator supports in a sequence.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maximum sequence length

Maximum number of arbitrary waveforms the waveform generator supports in a sequence.

On some waveform generators, this value may vary with remaining onboard memory.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maximum loop count

Maximum number of times the waveform generator can repeat an arbitrary waveform in a sequence.

Parent topic:

ArbSequence Waveform Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=query-arbitrary-waveform-capabilities.html language=enus -->
## TOPIC 00026: Query Arbitrary Waveform Capabilities

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `query-arbitrary-waveform-capabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/query-arbitrary-waveform-capabilities.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the properties of the waveform generator that are related to creating arbitrary waveforms. session in Handle that identifies your instrument session previously allocated by Initialize With Channels. error in Error conditions that occur before this node runs. The node responds to this input a

Query Arbitrary Waveform Capabilities

Returns the properties of the waveform generator that are related to creating arbitrary waveforms.

[IMAGE alt='1378' src='Query_Arbitrary_Waveform_Capabilities.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maximum number of waveforms

Maximum number of arbitrary waveforms that the waveform generator allows.

On some waveform generators, this value may vary with remaining onboard memory.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### waveform quantum

Size (number of points) of each waveform, which must be a multiple of a constant quantum value.

This output obtains the quantum value that the waveform generator uses; this means that if the output returns a value of 8, all waveform sizes must be a multiple of 8.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maximum waveform size

Maximum number of points that the waveform generator allows in a waveform.

On some waveform generators, this value may vary with remaining onboard memory.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### minimum waveform size

Minimum number of points that the waveform generator allows in a waveform.

For some waveform generators, you may need to supply a larger waveform than the value specified by this output.

Parent topic:

Arbitrary Waveform Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=query-freq-list-capabilities.html language=enus -->
## TOPIC 00027: Query Freq List Capabilities

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `query-freq-list-capabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/query-freq-list-capabilities.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the properties of the waveform generator that are related to creating frequency lists. session in Handle that identifies your instrument session previously allocated by Initialize With Channels. error in Error conditions that occur before this node runs. The node responds to this input accor

Query Freq List Capabilities

Returns the properties of the waveform generator that are related to creating frequency lists.

[IMAGE alt='1378' src='Query_Freq_List_Capabilities.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### minimum frequency list duration

Minimum duration that the waveform generator supports in a step of a frequency list.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### maximum frequency list duration

Maximum duration that the waveform generator supports in a step of a frequency list.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maximum number of frequency lists

Maximum number of frequency lists that the waveform generator supports.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### frequency list duration quantum

Quantum that all durations must be a multiple of returned in a frequency list.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maximum frequency list length

Maximum number of steps that the waveform generator supports in a frequency list.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### minimum frequency list length

Minimum number of steps that the waveform generator supports in a frequency list.

Parent topic:

List Mode Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=read-calibration-adc.html language=enus -->
## TOPIC 00028: Read Calibration ADC

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `read-calibration-adc.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/read-calibration-adc.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Takes one or more voltage measurements from the onboard calibration ADC and returns their average value. The signal that the ADC actually measures can be specified using the Cal ADC Input property. The ADC has some inherent gain and offset. These values can be determined during an external calibrati

Read Calibration ADC

Takes one or more voltage measurements from the onboard calibration ADC and returns their average value.

The signal that the ADC actually measures can be specified using the Cal ADC Input property. The ADC has some inherent gain and offset. These values can be determined during an external calibration session and stored in the calibration EEPROM.

[IMAGE alt='1378' src='Read_Calibration_ADC.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number of reads to average

Number of measurements to be taken and averaged to determine the return value.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### return calibrated value

Boolean value that specifies whether or not the voltage returned from the ADC should be adjusted to account for the gain and offset of the ADC.

| True | The value that is returned from the ADC is adjusted to account for the gain and offset of the ADC. |
| --- | --- |
| False | The raw voltage value reported by the ADC is returned. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### calibration ADC value

Average of the voltage measurements taken from the onboard calibration ADC.

Parent topic:

ADC Control Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=reset-device.html language=enus -->
## TOPIC 00029: Reset Device

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `reset-device.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/reset-device.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a hard reset on the waveform generator. Generation is stopped, all routes are released, external bidirectional terminals are tri-stated, FPGAs are reset, hardware is configured to its default state, and all session properties are reset to their default states. session in Handle that identif

Reset Device

Performs a hard reset on the waveform generator.

Generation is stopped, all routes are released, external bidirectional terminals are tri-stated, FPGAs are reset, hardware is configured to its default state, and all session properties are reset to their default states.

[IMAGE alt='1378' src='Reset_Device.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Reset

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=reset-with-defaults.html language=enus -->
## TOPIC 00030: Reset With Defaults

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `reset-with-defaults.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/reset-with-defaults.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the waveform generator to a known state and resets session attributes to values specified in the IVI configuration store. If the session was created without a logical name, the node is equivalent to Reset. For the PXI/PCI-5421, the node performs a "soft reset" in which generation stops, all r

Reset With Defaults

Resets the waveform generator to a known state and resets session attributes to values specified in the IVI configuration store.

If the session was created without a logical name, the node is equivalent to Reset.

For the PXI/PCI-5421, the node performs a "soft reset" in which generation stops, all routes are released, external bidirectional terminals are tri-stated, and all session attributes are reset to the IVI configuration store values. Default session attributes are not programmed to hardware until Commit is called.

[IMAGE alt='1378' src='Reset_With_Defaults.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Reset

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=restore-last-external-calibration-constants.html language=enus -->
## TOPIC 00031: Restore Last External Calibration Constants

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `restore-last-external-calibration-constants.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/restore-last-external-calibration-constants.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Overwrites the current calibration constants with those from the last successful external calibration. Invalidates data from any self-calibrations performed since the last time an external calibration was performed. session in Handle that identifies your instrument session previously allocated by In

Restore Last External Calibration Constants

Overwrites the current calibration constants with those from the last successful external calibration. Invalidates data from any self-calibrations performed since the last time an external calibration was performed.

[IMAGE alt='1378' src='Restore_Last_External_Calibration_Constants.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

External Calibration Utility Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=revision-query.html language=enus -->
## TOPIC 00032: Revision Query

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `revision-query.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/revision-query.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision numbers of the NI-FGEN software and the instrument firmware. session in Handle that identifies your instrument session previously allocated by Initialize With Channels. error in Error conditions that occur before this node runs. The node responds to this input according to stand

Revision Query

Returns the revision numbers of the NI-FGEN software and the instrument firmware.

[IMAGE alt='1378' src='Revision_Query.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### size of instrument driver revision

Maximum size of the instrument driver revision output string, which must be set to a minimum of 2,048.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### size of firmware revision

Maximum size of the firmware revision output string, which must be set to a minimum of 2,048.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### instrument driver revision

NI-FGEN software revision numbers in the form of a string.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### firmware revision

Instrument firmware revision numbers in the form of a string. Not all instruments have firmware information available.

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=route-signal-out.html language=enus -->
## TOPIC 00033: Route Signal Out

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `route-signal-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/route-signal-out.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes various signals to the backplane trigger lines or front panel terminals. The waveform generator must not be in the Generating state when you call this node. route signal from The source of the signal to route. You can clear a previously routed signal by routing NONE to the destination termina

Route Signal Out

Routes various signals to the backplane trigger lines or front panel terminals.

The waveform generator must not be in the Generating state when you call this node.

[IMAGE alt='1378' src='Route_Signal_Out.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### route signal from

The source of the signal to route.

You can clear a previously routed signal by routing NONE to the destination terminal.

| NONE | 0 | A previously routed signal is cleared, and no source is sent to the destination terminal. |
| --- | --- | --- |
| MARKER | 1 | The node uses a marker event as the source of the signal to route. |
| SYNC OUT | 2 | The node uses the SYNC OUT source as the signal to route. |
| OUT START TRIGGER | 3 | The node uses a Start Trigger as the source of the signal to route. |
| BOARD CLOCK | 4 | The node uses a 20 MHz source derived from the Sample Clock Timebase as the signal to route. |
| SYNCHRONIZATION | 5 | The node uses the synchronization source as the signal to route. |
| SOFTWARE TRIGGER | 6 | The node routes a signal generated by Send Software Edge Trigger or niFgen_SendSoftwareEdgeTrigger. |
| REF IN | 7 | The node uses the REF IN front panel connector as the source of the signal to route. |
| PXI_CLK10 | 8 | The node uses the 10 MHz PXI backplane clock as the source of the signal to route. |
| PXI STAR | 9 | The node uses the PXI_Star trigger line from the PXI backplane as the source of the signal to route. |
| PFI 0 | 10 | The node uses the PFI 0 front panel connector as the source of the signal to route. |
| PXI_Trig0 | 11 | The node uses the RTSI 0 PCI backplane trigger line or PXI_Trig 0 PXI backplane trigger line as the source of the signal to route. |
| PXI_Trig1 | 12 | The node uses the RTSI 1 PCI backplane trigger line or PXI_Trig 1 PXI backplane trigger line as the source of the signal to route. |
| PXI_Trig2 | 13 | The node uses the RTSI 2 PCI backplane trigger line or PXI_Trig 2 PXI backplane trigger line as the source of the signal to route. |
| PXI_Trig3 | 14 | The node uses the RTSI 3 PCI backplane trigger line or PXI_Trig 3 PXI backplane trigger line as the source of the signal to route. |
| PXI_Trig4 | 15 | The node uses the RTSI 4 PCI backplane trigger line or PXI_Trig 4 PXI backplane trigger line as the source of the signal to route. |
| PXI_Trig5 | 16 | The node uses the RTSI 5 PCI backplane trigger line or PXI_Trig 5 PXI backplane trigger line as the source of the signal to route. |
| PXI_Trig6 | 17 | The node uses the RTSI 6 PCI backplane trigger line or PXI_Trig 6 PXI backplane trigger line as the source of the signal to route. |
| PXI_Trig7 | 18 | The node uses the RTSI 7 PCI backplane trigger line or PXI_Trig 7 PXI backplane trigger line as the source of the signal to route. |
| RTSI CLOCK | 19 | The node uses the RTSI_CLOCK line from the PCI backplane as the source of the signal to route. |
| CLOCK OUT | 20 | The node uses the CLOCK Out front panel connector as the source of the signal to route. |
| PLL REF SOURCE | 21 | The node uses the PLL REF front panel connector as the source of the signal to route. |
| UPDATE CLOCK | 22 | The node uses the Update Clock as the source of the signal to route. |
| ONBOARD REF CLOCK | 23 | The node uses the onboard Reference Clock as the source of the signal to route. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### route signal to

The destination of the signal to route.

| PXI_Trig0 | 0 | The node routes the signal to the RTSI 0 PCI backplane trigger line or PXI_Trig 0 PXI backplane trigger line. |
| --- | --- | --- |
| PXI_Trig1 | 1 | The node routes the signal to the RTSI 1 PCI backplane trigger line or PXI_Trig 1 PXI backplane trigger line. |
| PXI_Trig2 | 2 | The node routes the signal to the RTSI 2 PCI backplane trigger line or PXI_Trig 2 PXI backplane trigger line. |
| PXI_Trig3 | 3 | The node routes the signal to the RTSI 3 PCI backplane trigger line or PXI_Trig 3 PXI backplane trigger line. |
| PXI_Trig4 | 4 | The node routes the signal to the RTSI 4 PCI backplane trigger line or PXI_Trig 4 PXI backplane trigger line. |
| PXI_Trig5 | 5 | The node routes the signal to the RTSI 5 PCI backplane trigger line or PXI_Trig 5 PXI backplane trigger line. |
| PXI_Trig6 | 6 | The node routes the signal to the RTSI 6 PCI backplane trigger line or PXI_Trig 6 PXI backplane trigger line. |
| RTSI CLOCK | 7 | The node routes the signal to the RTSI_CLOCK PCI backplane line. |
| REF OUT | 8 | The node routes the signal to the REF OUT front panel connector. |
| PFI 0 | 9 | The node routes the signal to the PFI 0 front panel connector. |
| PXI_Trig7 | 10 | The node routes the signal to the RTSI 7 PCI backplane trigger line or PXI_Trig 7 PXI backplane trigger line. |
| PFI 1 | 11 | The node routes the signal to the PFI 1 front panel connector. |
| PFI 4 | 12 | The node routes the signal to the PFI 4 line on the DIGITAL DATA & CONTROL (DDC) front panel connector. |
| PFI 5 | 13 | The node routes the signal to the PFI 5 line on the DIGITAL DATA & CONTROL (DDC) front panel connector. |
| PXI STAR | 14 | The node routes the signal to the PXI_Star trigger line on the PXI backplane. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Trigger Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=self-test.html language=enus -->
## TOPIC 00034: Self-Test

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/self-test.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs the instrument self-test routine and returns the test results. For some waveform generators, the hardware is reset after this node runs. If you use this node, your waveform generator may not be in its previously configured state after the node runs. session in Handle that identifies your instru

Self-Test

Runs the instrument self-test routine and returns the test results.

For some waveform generators, the hardware is reset after this node runs. If you use this node, your waveform generator may not be in its previously configured state after the node runs.

[IMAGE alt='1378' src='Self-Test.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### self-test result

Value returned from the waveform generator self-test. A returned value of zero indicates success.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### self-test message

Self-test response string from the waveform generator.

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=set-calibration-user-defined-info.html language=enus -->
## TOPIC 00035: Set Calibration User Defined Info

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `set-calibration-user-defined-info.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/set-calibration-user-defined-info.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores user-defined information in the onboard EEPROM. session in Handle that identifies your instrument session previously allocated by Initialize External Calibration. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior.

Set Calibration User Defined Info

Stores user-defined information in the onboard EEPROM.

[IMAGE alt='1378' src='Set_Calibration_User_Defined_Info.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### info

Information to be stored in the EEPROM.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

External Calibration Utility Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=set-named-waveform-next-write-position.html language=enus -->
## TOPIC 00036: Set Named Waveform Next Write Position

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `set-named-waveform-next-write-position.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/set-named-waveform-next-write-position.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the position in the named waveform to which data is written at the next write. Allows you to write to arbitrary locations within the waveform. This node only applies settings to the next write to the specified waveform. Subsequent writes to the waveform begin where the last write left off, unle

Set Named Waveform Next Write Position

Sets the position in the named waveform to which data is written at the next write. Allows you to write to arbitrary locations within the waveform.

This node only applies settings to the next write to the specified waveform. Subsequent writes to the waveform begin where the last write left off, unless this node is called again.

[IMAGE alt='1378' src='Set_Named_Waveform_Next_Write_Position.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

Offset from the position specified by the relative to input at which to start loading the data into the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

Name of the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### relative to

Reference position in the waveform. This position and the offset together determine where to start loading data into the waveform.

| NIFGEN_VAL_WAVEFORM_POSITION_CURRENT | 0 | The reference position is relative to the current position. |
| --- | --- | --- |
| NIFGEN_VAL_WAVEFORM_POSITION_START | 1 | The reference position is relative to the start of the waveform. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### waveform name out

Name of the named waveform.

#### Programming Patterns

The waveform name input must have been created by a call to Allocate Named Waveform and wired to this node.

Parent topic:

Script Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=set-waveform-next-write-position.1.html language=enus -->
## TOPIC 00037: Set Waveform Next Write Position

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `set-waveform-next-write-position.1.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/set-waveform-next-write-position.1.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the position in the waveform at which data is written during the next write. Allows you to write to arbitrary locations within the waveform. This node only applies settings to the next write to the specified waveform. Subsequent writes to the waveform begin where the last write left off, unless

Set Waveform Next Write Position

Sets the position in the waveform at which data is written during the next write. Allows you to write to arbitrary locations within the waveform.

This node only applies settings to the next write to the specified waveform. Subsequent writes to the waveform begin where the last write left off, unless this node is called again.

[IMAGE alt='1378' src='Set_Waveform_Next_Write_Position.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### relative to

Reference position in the waveform. This position and the offset together determine where to start loading data into the waveform.

| NIFGEN_VAL_WAVEFORM_POSITION_CURRENT | 0 | The reference position is relative to the current position. |
| --- | --- | --- |
| NIFGEN_VAL_WAVEFORM_POSITION_START | 1 | The reference position is relative to the start of the waveform. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### waveform reference in

Reference to the arbitrary waveform previously allocated with Allocate Waveform or Create Waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

Offset from the position specified by the relative to input at which to start loading the data into the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### waveform reference out

Reference that identifies the waveform.

#### Programming Patterns

The waveform reference in input must have been created by a call to Allocate Waveform or Create Waveform and wired to this node.

Parent topic:

Arbitrary Waveform Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=trigger-nodes.html language=enus -->
## TOPIC 00038: Trigger Nodes

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `trigger-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/trigger-nodes.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN trigger nodes to configure waveform generator triggering and to route signals from the waveform generator to other instruments.

Trigger Nodes

Use the NI-FGEN trigger nodes to configure waveform generator triggering and to route signals from the waveform generator to other instruments.

Configuration Nodes

NI-FGEN

waveform generator

Configure Trigger

waveform generator

Configure Trigger Mode

waveform generator

Export Signal

Routes signals (clocks, triggers, and events) to the output terminal you specify.

Get NI-TClk Session Reference

NI-TClk

Route Signal Out

Routes various signals to the backplane trigger lines or front panel terminals.

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=utility-nodes.html language=enus -->
## TOPIC 00039: Utility Nodes

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `utility-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/utility-nodes.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN utility nodes to control common instrument operations. These operations include many that VXIplug&play require, such as reset, self-test, revision query, and error message.

Utility Nodes

Use the NI-FGEN utility nodes to control common instrument operations. These operations include many that VXIplug&play require, such as reset, self-test, revision query, and error message.

NI-FGEN Nodes

NI-FGEN

waveform generator

Error Message

NI-FGEN

Get Stream Endpoint Handle

waveform generator

Reset

waveform generator

Revision Query

NI-FGEN

Self-Test

Runs the instrument self-test routine and returns the test results.

Parent topic:

NI-FGEN Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=wait-until-done.html language=enus -->
## TOPIC 00040: Wait Until Done

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `wait-until-done.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/wait-until-done.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the waveform generator is done generating or until the set maximum time expires to report the session reference to the next node. This node reports the instrument handle output to the next node only after the current generation is complete in Single Trigger mode. session in Handle that i

Wait Until Done

Waits until the waveform generator is done generating or until the set maximum time expires to report the session reference to the next node.

This node reports the instrument handle output to the next node only after the current generation is complete in Single Trigger mode.

[IMAGE alt='1378' src='Wait_Until_Done.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum time (ms)

Timeout value in milliseconds.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Action Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=write-binary-16-analog-static-value.1.html language=enus -->
## TOPIC 00041: Write Binary 16 Analog Static Value

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `write-binary-16-analog-static-value.1.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/write-binary-16-analog-static-value.1.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a 16-bit value to the DAC, which could be output as a DC voltage. This node writes to the DAC only when used in an external calibration session. session in Handle that identifies your instrument session previously allocated by Initialize External Calibration. error in Error conditions that oc

Write Binary 16 Analog Static Value

Writes a 16-bit value to the DAC, which could be output as a DC voltage.

This node writes to the DAC only when used in an external calibration session.

[IMAGE alt='1378' src='Write_Binary_16_Analog_Static_Value.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize External Calibration.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### value

Value to write.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

ADC Control Nodes

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=write-named-waveform-direct-dma-i16.html language=enus -->
## TOPIC 00042: Direct DMA I16

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `write-named-waveform-direct-dma-i16.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/write-named-waveform-direct-dma-i16.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a specified amount of data from a Direct DMA-compatible waveform generator to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. By default, a call to this node continues writing data from the position of

Direct DMA I16

Writes a specified amount of data from a Direct DMA-compatible waveform generator to the named waveform in onboard memory.

If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. By default, a call to this node continues writing data from the position of the last sample written.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

Name of the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### window address

Windows address of the Direct DMA-compatible data source.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### samples to write

Number of samples to write from the Direct DMA-compatible data source.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### waveform name out

Name of the named waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

You can change the write position and offset using Set Waveform Next Write Position.

Parent topic:

Write Named Waveform

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=write-named-waveform-i16.html language=enus -->
## TOPIC 00043: I16

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `write-named-waveform-i16.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/write-named-waveform-i16.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes binary data to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. By default, a call to this node continues writing data from the position of the last sample written. session in Handle that identifies your

I16

Writes binary data to the named waveform in onboard memory.

If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. By default, a call to this node continues writing data from the position of the last sample written.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

Name of the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/c1di16.png']

##### waveform data

Array of data you want to load into the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### waveform name out

Name of the named waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

You can change the write position and offset using Set Waveform Next Write Position.

#### Write Complex Binary 16 Data

This node can write complex data to a waveform in onboard memory on waveform generators with the OSP Enabled property set to 
 True and the Data Processing Mode property set to 
 Complex. To write complex data with this node, you must interleave the I/Q pairs.

Parent topic:

Write Named Waveform

<!--NI_TOPIC bundle=ni-fgen-19.1-lvnxg-api-ref path=write-named-waveform-wdt.html language=enus -->
## TOPIC 00044: WDT

- bundle_id: `ni-fgen-19.1-lvnxg-api-ref`
- source_path: `write-named-waveform-wdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-19.1-lvnxg-api-ref/raw/resource/enus/write-named-waveform-wdt.html
- document_id: `ni-fgen-19.1-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes waveform data type (WDT) data to the named waveform in onboard memory. If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. By default, a call to this node continues writing data from the position of the last sample written. session in Handle th

WDT

Writes waveform data type (WDT) data to the named waveform in onboard memory.

If streaming is enabled, you can write more data than the allocated waveform size in onboard memory. By default, a call to this node continues writing data from the position of the last sample written.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Handle that identifies your instrument session previously allocated by Initialize With Channels.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the waveform generator channel that the node uses.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### waveform name

Name of the waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### use waveform dT for sample rate

Boolean value that specifies whether or not the sample rate should be set to match the sampling information contained in the waveform input.

| True | The node obtains rate information from data specified by the waveform input and uses the inverse of the dT as the rate. |
| --- | --- |
| False | The node takes no action unless you set the sample rate by calling Set Sample Rate or by setting the Sample Rate property, in which case the node uses that rate. |

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform

Data you want to use for the arbitrary waveform.

The data must be between -1.0 and +1.0. Use the gain input of Configure Arbitrary Waveform or Configure Arbitrary Sequence to generate different voltages.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session to wire to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### waveform name out

Name of the named waveform.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

You can change the write position and offset using Set Waveform Next Write Position.

Parent topic:

Write Named Waveform
