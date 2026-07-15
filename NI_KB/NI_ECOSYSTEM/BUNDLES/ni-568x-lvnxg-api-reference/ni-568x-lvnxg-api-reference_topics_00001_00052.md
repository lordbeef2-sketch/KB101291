# NI DOCUMENT BUNDLE: ni-568x-lvnxg-api-reference

<!--NI_BUNDLE_CHUNK bundle=ni-568x-lvnxg-api-reference start=1 end=52 -->
<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=abort.html language=enus -->
## TOPIC 00001: Abort

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `abort.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/abort.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts all previously initiated measurements and returns the power meter to the Idle state. This node does not check the instrument status. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input

Abort

Aborts all previously initiated measurements and returns the power meter to the Idle state.

This node does not check the instrument status.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Measurement

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=close.html language=enus -->
## TOPIC 00002: Close

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `close.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/close.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the following closing operations: closes the instrument I/O session, destroys the NI-568x session, and deallocates any memory resources that NI-568x uses. After calling Close, you cannot use NI-568x again until you call Initialize With Options. session in Instrument session obtained from In

Close

Performs the following closing operations: closes the instrument I/O session, destroys the NI-568x session, and deallocates any memory resources that NI-568x uses.

Note

NI-568x

Initialize With Options

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

NI-568x Nodes

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configuration.html language=enus -->
## TOPIC 00003: Configuration

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configuration.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`

Configuration

NI-568x Nodes

Use NI-568x nodes to develop applications for your RF power meter.

Configure Units

Configures the unit to which the RF power is converted after measurement.

Configure Acquisition Mode

NI-568x

Configure Range Auto Enabled

Enables or disables auto-ranging on the channel specified.

Configure Averaging Auto Enabled

Enables or disables the auto-averaging.

Configure Offset

Specifies the offset, in decibels (dB), to apply to the measured value.

Configure Correction Frequency

Specifies the frequency, in hertz (Hz), of the input signal.

Configure Range

Configures the lower and upper range values for a given channel.

Configure Averaging Count

Sets the manual average count that the instrument uses in manual averaging mode.

Configure Duty Cycle Correction

Enables or disables the duty cycle correction and configures the duty cycle correction for pulse power measurements.

Parent topic:

NI-568x Nodes

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-acquisition-mode.html language=enus -->
## TOPIC 00004: Configure Acquisition Mode

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-acquisition-mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-acquisition-mode.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the NI-568x acquisition mode. Some nodes and properties are only available with certain acquisition modes. The USB-5680 supports only continuous acquisition mode. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node run

Configure Acquisition Mode

Configures the NI-568x acquisition mode.

Some nodes and properties are only available with certain acquisition modes. The USB-5680 supports only continuous acquisition mode.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### mode

Operating mode for the NI-568x device.

| Continuous Mode | 10000 | Continuous mode is the default power meter measuring mode. In continuous mode, the power meter starts measuring power immediately after the operation is initiated and stops when the measurement is complete. |
| --- | --- | --- |
| Time Slot Mode | 20000 | In time slot mode, the trigger initiates the power sensor, which divides the power measurement into the time slots you define for the measurement and calculates the average power reading for each individual slot. Use Configure Time Slot or Configure Time Slot Exclusion to configure time slot acquisition mode input and outputs. |
| Scope Mode | 30000 | In scope mode, the trigger initiates the power sensor measurement with respect to time. The power meter reads a record of multiple points. You can configure a gate and a fence for the measurement to control which portion of the time domain data is recorded. Use the Configure Scope nodes to configure Time Slot acquisition mode inputs and outputs. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-averaging-auto-enabled.html language=enus -->
## TOPIC 00005: Configure Averaging Auto Enabled

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-averaging-auto-enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-averaging-auto-enabled.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables the auto-averaging. When auto-averaging is enabled, the sensor chooses an averaging number based on the power level currently being measured. For most power levels, enabling auto-averaging results in the power reading fluctuating by no more than twice the value you select for the

Configure Averaging Auto Enabled

Enables or disables the auto-averaging.

When auto-averaging is enabled, the sensor chooses an averaging number based on the power level currently being measured. For most power levels, enabling auto-averaging results in the power reading fluctuating by no more than twice the value you select for the Auto Average Resolution property. Auto-averaging only stabilizes the readings to compensate for noise contributed by the power sensor electronics.

If you disable auto-averaging, you can configure the number of samples to average using 
 [Configure Averaging Count](configure-averaging-count.html#GUID-D5B64019-3752-4DE7-8A96-2E38F64A5011).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### auto averaging enabled

Boolean value that enables or disables the auto-averaging mode used for the channel you specify in channel name.

NI-568x sets the Averaging Auto Enabled property to this value.

When you disable auto-averaging, you must specify the number of samples that NI-568x averages by calling [Configure Averaging Count](configure-averaging-count.html#GUID-D5B64019-3752-4DE7-8A96-2E38F64A5011).

| True | Enables auto-averaging. |
| --- | --- |
| False | Disables auto-averaging. False is the only supported value for the USB-5680. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-averaging-count.html language=enus -->
## TOPIC 00006: Configure Averaging Count

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-averaging-count.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-averaging-count.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the manual average count that the instrument uses in manual averaging mode. The averaging count specifies the number of samples that the instrument takes before the measurement is complete. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur

Configure Averaging Count

Sets the manual average count that the instrument uses in manual averaging mode.

The averaging count specifies the number of samples that the instrument takes before the measurement is complete.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### averaging count

Averaging count, which is the number of samples the NI-568x device takes before completing the measurement. The NI-568x driver sets the Averaging Count property to this value.

Valid Range USB-5680: 1 to 256

Valid Range USB-5681/5683/5684: 1 to 40,000

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-correction-frequency.html language=enus -->
## TOPIC 00007: Configure Correction Frequency

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-correction-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-correction-frequency.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency, in hertz (Hz), of the input signal. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: N

Configure Correction Frequency

Specifies the frequency, in hertz (Hz), of the input signal.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency

Frequency of the input signal in hertz.

The instrument uses this value to determine the appropriate correction factor for the sensor.

To obtain the most accurate measurement, specify the correction frequency as close as possible to the actual frequency of the input signal. The driver sets the Correction Frequency property to this value.

| Device | Valid Range |
| --- | --- |
| USB-5680 | 50 x 106 to 6 x 109 |
| USB-5681 | 10 x 106 to 18 x 109 |
| USB-5683 | 10 x 106 to 8 x 109 |
| USB-5684 | 10 x 106 to 18 x 109 |

| Device | Default Value |
| --- | --- |
| USB-5680 | 50 x 106 |
| USB-5681 | 10 x 106 |
| USB-5683 | 10 x 106 |
| USB-5684 | 10 x 106 |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-duty-cycle-correction.html language=enus -->
## TOPIC 00008: Configure Duty Cycle Correction

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-duty-cycle-correction.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-duty-cycle-correction.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables the duty cycle correction and configures the duty cycle correction for pulse power measurements. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard

Configure Duty Cycle Correction

Enables or disables the duty cycle correction and configures the duty cycle correction for pulse power measurements.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### correction enabled

Boolean value that specifies if the power meter performs a duty cycle correction on the specified channel.

| True | Enables duty cycle correction. |
| --- | --- |
| False | Disables duty cycle correction. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### correction

Duty cycle correction the power meter uses to calculate the pulse power of a pulse-modulated signal.

The duty cycle indicates the percentage of time a signal is active high, so specifying a higher value indicates that the device expects the measured signal to be active high a greater portion of the time. The value of this input is specified as a percentage.

Valid Range: 0.01 to 100

Default value: 100

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-external-trigger.html language=enus -->
## TOPIC 00009: Configure External Trigger

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-external-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-external-trigger.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the external trigger source and slope of the trigger. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default valu

Configure External Trigger

Configures the external trigger source and slope of the trigger.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source channel name

Name of the channel to use as the external trigger source.

The NI-568x has only one channel, so you must specify 
 0 as the value of this control.

Valid Values:

- TTL0
- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### slope

Polarity of the external trigger slope.

| Positive | Sets the trigger to occur on the rising edge (a transition from low to high) of the trigger pulse. |
| --- | --- |
| Negative | Sets the trigger to occur on the falling edge (a transition from high to low) of the trigger pulse. |

Default value: Positive

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-internal-trigger-level.html language=enus -->
## TOPIC 00010: Configure Internal Trigger Level

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-internal-trigger-level.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-internal-trigger-level.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the internal trigger level of the power meter. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No e

Configure Internal Trigger Level

Configures the internal trigger level of the power meter.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### trigger level

Trigger level for the measurement signal.

The value of this input is specified in the same unit as the value of the Units property.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-internal-trigger.html language=enus -->
## TOPIC 00011: Configure Internal Trigger

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-internal-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-internal-trigger.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the internal trigger source and slope of the trigger. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default valu

Configure Internal Trigger

Configures the internal trigger source and slope of the trigger.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source channel name

Name of the channel to use as the internal trigger source.

The USB-568x has only one channel, so you must specify 
 0 as the value of this control.

Valid Values:

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### slope

Polarity of the internal trigger slope.

| Positive | Sets the trigger to occur on the rising edge (a transition from low to high) of the trigger pulse. |
| --- | --- |
| Negative | Sets the trigger to occur on the falling edge (a transition from high to low) of the trigger pulse. |

Default value: Positive

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-offset.html language=enus -->
## TOPIC 00012: Configure Offset

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-offset.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset, in decibels (dB), to apply to the measured value. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Defau

Configure Offset

Specifies the offset, in decibels (dB), to apply to the measured value.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### offset

Offset for the measured value. NI-568x sets the Offset property to this value.

Valid Range: -100 to 100

Default value: 0

##### Compensating for System Losses and Gains

NI-568x uses the offset to compensate for system losses or gains between the device under test (DUT) and the power meter sensor. Use a positive value for loss compensation. Use a negative value for gain compensation. For example, you can compensate for a cable loss of 2 dB by setting offset to 
 2. Similarly, you can compensate for a gain stage of 10 dB by setting offset to 
 -10. In both cases, the NI-568x reading indicates the power at the DUT rather than the power at the NI-568x device.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-range-auto-enabled.html language=enus -->
## TOPIC 00013: Configure Range Auto Enabled

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-range-auto-enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-range-auto-enabled.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables auto-ranging on the channel specified. Auto-ranging means that the sensor firmware determines the appropriate range for sensor operation. If you disable auto-ranging, specify the range using Configure Range. session in Instrument session obtained from Initialize With Options. err

Configure Range Auto Enabled

Enables or disables auto-ranging on the channel specified.

Auto-ranging means that the sensor firmware determines the appropriate range for sensor operation. If you disable auto-ranging, specify the range using [Configure Range](configure-range.html#GUID-A8C8C771-97E7-4A00-9D96-4C91A3A4F0F2).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### range auto enabled

Boolean value that specifies whether the NI-568x device automatically determines the optimal measurement range of power.

False is the only supported value for the USB-5680.

| True | Auto-ranging is enabled. |
| --- | --- |
| False | Auto-ranging is not enabled. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-range.html language=enus -->
## TOPIC 00014: Configure Range

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-range.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-range.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the lower and upper range values for a given channel. The supported ranges for the NI RF power meter are located in the specifications document for your device. NI-568x coerces the values passed to this node to a valid device range. session in Instrument session obtained from Initialize W

Configure Range

Configures the lower and upper range values for a given channel.

The supported ranges for the NI RF power meter are located in the specifications document for your device. NI-568x coerces the values passed to this node to a valid device range.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### range lower

Lower limit of the expected value of the measurement.

The value of this input is specified in the same units as specified with the Units property.

Default value: 1e-6

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### range upper

Upper limit of the expected value of the measurement.

The value of this input is specified in the same units as specified with the Units property.

Default value: .01

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-scope-fence.html language=enus -->
## TOPIC 00015: Configure Scope Fence

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-scope-fence.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-scope-fence.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the scope mode fence inputs and outputs. This node is applicable only if you select Scope Mode as the mode within Configure Acquisition Mode. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds

Configure Scope Fence

Configures the scope mode fence inputs and outputs.

This node is applicable only if you select Scope Mode as the mode within [Configure Acquisition Mode](configure-acquisition-mode.html#GUID-E4748F71-DF20-413E-97B4-2B2BFD850E26).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### fence enabled

Boolean value that specifies if the fence region should be used.

| True | Enables the fence. |
| --- | --- |
| False | Disables the fence. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### fence start time

Number of seconds from the start of the acquisition at which to start the fence region of the waveform acquisition.

Valid Range: 0.0 to 0.300

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### fence end time

Number of seconds from the start of the acquisition at which to end the fence region of the waveform acquisition.

Valid Range: 0.0 to 0.300

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

#### Fence Background Information

The fence is a region within the gate region where the data points are not included in the average gate power calculation. The fence takes effect only if you set fence enabledto True. The fence region should fall entirely inside the gate region. If the fence start time and fence end time values are the same, the fence is disabled.

Parent topic:

Scope

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-scope-gate.html language=enus -->
## TOPIC 00016: Configure Scope Gate

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-scope-gate.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-scope-gate.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of seconds from the start of the acquisition at which to start the gate region of the waveform acquisition. This node is applicable only if you select Scope Mode as the mode within Configure Acquisition Mode. session in Instrument session obtained from Initialize With Options. e

Configure Scope Gate

Specifies the number of seconds from the start of the acquisition at which to start the gate region of the waveform acquisition.

This node is applicable only if you select Scope Mode as the mode within [Configure Acquisition Mode](configure-acquisition-mode.html#GUID-E4748F71-DF20-413E-97B4-2B2BFD850E26).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### gate enabled

Boolean value that specifies if the gate region should be used.

| True | Enables the gate. |
| --- | --- |
| False | Disables the gate. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### gate start time

Number of seconds from the start of the acquisition at which to start the gate region of the waveform acquisition.

Valid Range: 0.0 to 0.300

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### gate end time

Number of seconds from the start of the acquisition at which to end the gate region of the waveform acquisition.

Valid Range: 0.0 to 0.300

Default value: 0.02

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

#### Configuring a Gate or Fence for a Scope Acquisition Mode Application

To configure a gate or fence for your scope acquisition mode application, use [Configure Scope Gate](#GUID-7DC29C76-D179-4A50-814D-32255605C45F) or [Configure Scope Fence](configure-scope-fence.html#GUID-2BE09D2E-6FC3-43FA-B7BA-458790668C92).

Parent topic:

Scope

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-scope.html language=enus -->
## TOPIC 00017: Configure Scope

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-scope.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-scope.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the length of each scope mode acquisition record and the number of points in each record. This node is applicable only if you select Scope Mode as the mode within Configure Acquisition Mode. session in Instrument session obtained from Initialize With Options. error in Error conditions tha

Configure Scope

Configures the length of each scope mode acquisition record and the number of points in each record.

This node is applicable only if you select Scope Mode as the mode within [Configure Acquisition Mode](configure-acquisition-mode.html#GUID-E4748F71-DF20-413E-97B4-2B2BFD850E26).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### points per record

Number of data points within each record.

Valid Range: 2 to 1,024

Default value: 200

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### scope record length

Total duration of time, in seconds, of each Scope mode measurement.

Valid Range: 0.00001 to 0.300

Default value: 0.020

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

#### Configuring a Gate or Fence for a Scope Acquisition Mode Application

To configure a gate or fence for your scope acquisition mode application, use [Configure Scope Gate](configure-scope-gate.html#GUID-7DC29C76-D179-4A50-814D-32255605C45F) or [Configure Scope Fence](configure-scope-fence.html#GUID-2BE09D2E-6FC3-43FA-B7BA-458790668C92).

Parent topic:

Scope

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-time-slot-exclusion.html language=enus -->
## TOPIC 00018: Configure Time Slot Exclusion

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-time-slot-exclusion.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-time-slot-exclusion.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the exclusion period for each time slot. If you enable an exclusion period, a small amount of time at the start and end of each time slot is excluded from the power measurement calculation of each slot. This node is applicable only if you set the mode to Time Slot Mode in Configure Acquis

Configure Time Slot Exclusion

Configures the exclusion period for each time slot.

If you enable an exclusion period, a small amount of time at the start and end of each time slot is excluded from the power measurement calculation of each slot.

This node is applicable only if you set the mode to Time Slot Mode in [Configure Acquisition Mode](configure-acquisition-mode.html#GUID-E4748F71-DF20-413E-97B4-2B2BFD850E26).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### exclusion enabled

Boolean value that specifies if the exclusion period is used.

| True | The exclusion period is used. |
| --- | --- |
| False | The exclusion period is not used. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### exclusion time for slot start

Duration of time, in seconds, from the start of each time slot that should not be considered for the power measurement.

Valid Range: 0 to 0.010

Default value: 0.0002

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### exclusion time for slot end

Duration of time, in seconds, from the end of each time slot that should not be considered for the power measurement.

Note

exclusion time for slot end

exclusion time for slot start

slot width

Valid Range: 0 to 0.010

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

Parent topic:

Time Slot

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-time-slot.html language=enus -->
## TOPIC 00019: Configure Time Slot

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-time-slot.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-time-slot.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the time slot mode inputs and outputs. This node is applicable only if you set the mode to Time Slot Mode in Configure Acquisition Mode. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to th

Configure Time Slot

Configures the time slot mode inputs and outputs.

This node is applicable only if you set the mode to Time Slot Mode in [Configure Acquisition Mode](configure-acquisition-mode.html#GUID-E4748F71-DF20-413E-97B4-2B2BFD850E26).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### slot width

Width of each time slot, in seconds.

Valid Range: 1.0 x 10<sup>-5</sup> to 0.100

Note

USB-5681: The product of slot count and slot width cannot be greater than 300 ms.

USB-5683/5684: The product of slot count and slot width cannot be greater than 1000 ms.

Default value: 0.008

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### slot count

Number of time slots to acquire at a time.

Valid Range: 2 to 128

Default value: 8

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

Parent topic:

Time Slot

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-trigger-delay.html language=enus -->
## TOPIC 00020: Configure Trigger Delay

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-trigger-delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-trigger-delay.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the delay between the trigger and the actual measurement. You can configure a trigger delay only when you set the trigger source input of Configure Trigger Source to Internal or External. session in Instrument session obtained from Initialize With Options. error in Error conditions that o

Configure Trigger Delay

Configures the delay between the trigger and the actual measurement.

You can configure a trigger delay only when you set the trigger source input of [Configure Trigger Source](configure-trigger-source.html#GUID-C657EB4B-378D-4F25-A490-FC4C5A60ED03) to Internal or External.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### trigger delay enabled

Boolean value that specifies if the RF power meter uses a trigger delay when making a triggered measurement.

| True | The RF power meter uses a delay. |
| --- | --- |
| False | The RF power meter does not use a delay. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### trigger delay time

Trigger delay time in seconds.

A negative delay means the sensor takes measurements before the trigger occurs.

Valid Range: -5 x 10<sup>-3</sup> to 10.0

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-trigger-hysteresis.html language=enus -->
## TOPIC 00021: Configure Trigger Hysteresis

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-trigger-hysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-trigger-hysteresis.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the trigger hysteresis value, in dB. The hysteresis level describes the arming range of the trigger. The slope input set in Configure Internal Trigger determines whether the hysteresis range is above or below the trigger level input set in Configure Internal Trigger Level. You can configu

Configure Trigger Hysteresis

Configures the trigger hysteresis value, in dB.

The hysteresis level describes the arming range of the trigger. The slope input set in [Configure Internal Trigger](configure-internal-trigger.html#GUID-D8E1E141-9C00-4A58-AE6C-C284B61D4D95) determines whether the hysteresis range is above or below the trigger level input set in [Configure Internal Trigger Level](configure-internal-trigger-level.html#GUID-8E3BEC72-A03D-44C8-8E15-BF395F1C5554).

You can configure trigger hysteresis only when you set the trigger source input of [Configure Trigger Source](configure-trigger-source.html#GUID-C657EB4B-378D-4F25-A490-FC4C5A60ED03) to Internal.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### trigger hysteresis enabled

Boolean value that specifies if the trigger hysteresis value is considered when making triggered measurements.

| True | The trigger hysteresis value is used. |
| --- | --- |
| False | The trigger hysteresis value is not used. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### trigger hysteresis

Hysteresis value in dB relative to the trigger level that must be crossed before the trigger is armed.

This property is valid only if you set the Trigger Hysteresis Enabled property to True.

Valid Values: 
 1.0 to 
 10.0 in .01 increments

Default value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5683
- USB-5684

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-trigger-noise-immunity.html language=enus -->
## TOPIC 00022: Configure Trigger Noise Immunity

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-trigger-noise-immunity.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-trigger-noise-immunity.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sensor to wait for the trigger immunity factor before asserting the trigger. You can configure a trigger immunity factor only when you set the trigger source input of Configure Trigger Source to Internal. session in Instrument session obtained from Initialize With Options. error in Er

Configure Trigger Noise Immunity

Configures the sensor to wait for the trigger immunity factor before asserting the trigger.

You can configure a trigger immunity factor only when you set the trigger source input of [Configure Trigger Source](configure-trigger-source.html#GUID-C657EB4B-378D-4F25-A490-FC4C5A60ED03) to Internal.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### trigger immunity enabled

Boolean value that specifies the trigger noise immunity factor used when triggering.

| True | The trigger noise immunity factor is used. |
| --- | --- |
| False | The trigger noise immunity factor is not used. |

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### trigger immunity factor

Number of data points that must cross the triggering threshold before the trigger is recognized.

Valid Range: 1 to 10

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-trigger-source.html language=enus -->
## TOPIC 00023: Configure Trigger Source

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-trigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-trigger-source.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type of trigger source for the RF power meter. Some nodes are only available with certain trigger sources. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to stan

Configure Trigger Source

Configures the type of trigger source for the RF power meter.

Some nodes are only available with certain trigger sources.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### trigger source

Type of trigger source.

| Immediate | The device does not wait for a trigger and makes the measurement immediately. |
| --- | --- |
| External | The device starts an acquisition based on the signal on the external trigger input terminal meeting specified criteria, such as slope and trigger delay. |
| Internal | The device starts an acquisition based on the input signal you are measuring meeting specified criteria, such as slope, level, trigger delay, and trigger noise immunity. |
| Software | The device waits for a software trigger. After configuring the trigger type, you assert this trigger by calling Send Software Trigger. |

Default value: Immediate

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=configure-units.html language=enus -->
## TOPIC 00024: Configure Units

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `configure-units.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/configure-units.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the unit to which the RF power is converted after measurement. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Def

Configure Units

Configures the unit to which the RF power is converted after measurement.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### units

Unit to which the RF power is converted after measurement.

The NI-568x sets the Units property to this value.

The value of this property is used to determine the units in which the Range Upper and Range Lower properties are specified. The units of the values obtained from [Read Power](read-power.html#GUID-DD2DF365-3277-4202-A166-3BE4E86D6B87) and [Fetch Power](fetch-power.html#GUID-6F59535F-68C0-4A72-8832-D291041546BD) reflect the value set in this input.

| dBm | 1 | Sets the units to dBm. |
| --- | --- | --- |
| Watts | 4 | Sets the units to watts. |
| mWatts | 1001 | Sets the units to milliwatts. |
| uWatts | 1002 | Sets the units to microwatts. |

Default value: dBm

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=disable.html language=enus -->
## TOPIC 00025: Disable

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/disable.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected. If a measurement is in progress when you call this function, the measurement is aborted. session in Instrument session obtained from Initialize With Options. error in Error conditions

Disable

Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected.

If a measurement is in progress when you call this function, the measurement is aborted.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=error-message.html language=enus -->
## TOPIC 00026: Error Message

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `error-message.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/error-message.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a status code returned by any NI-568x node into a user-readable string. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behav

Error Message

Converts a status code returned by any NI-568x node into a user-readable string.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### error code

Error code to be converted.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### error message

Error message string read from the error message queue of the instrument.

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=error-query.html language=enus -->
## TOPIC 00027: Error Query

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `error-query.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/error-query.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an error code and message from the NI-568x error queue. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value

Error Query

Returns an error code and message from the NI-568x error queue.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### error code

Error code read from the device error queue.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### error message

Error message string read from the error message queue of the instrument.

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=fetch-array.html language=enus -->
## TOPIC 00028: Fetch Array

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `fetch-array.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/fetch-array.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches a previously initiated array of power measurements. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error error out Error information. The node produces this output acc

Fetch Array

Fetches a previously initiated array of power measurements.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### power

Value measured by the NI-568x device. The result units are specified by the units input with [Configure Units](configure-units.html#GUID-FF5738D7-F9E1-4CA6-AA19-5D335663B40A).

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

#### Programming Patterns

Call [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528) to initiate a measurement before calling Fetch Array.

Parent topic:

Fetch Power

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=fetch-power.html language=enus -->
## TOPIC 00029: Fetch Power

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `fetch-power.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/fetch-power.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the result from a previously initiated measurement. After Fetch Power executes, the value of the power output contains an actual reading or array of readings on the channel. The power units are specified by the Units property.

Fetch Power

Returns the result from a previously initiated measurement. After Fetch Power executes, the value of the power output contains an actual reading or array of readings on the channel. The power units are specified by the Units property.

Measurement

Fetch

Fetches a previously initiated power measurement.

Fetch Array

Fetches a previously initiated array of power measurements.

Parent topic:

Measurement

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=fetch.html language=enus -->
## TOPIC 00030: Fetch

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `fetch.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/fetch.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches a previously initiated power measurement. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error error out Error information. The node produces this output according to

Fetch

Fetches a previously initiated power measurement.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### power

Value measured by the NI-568x device. The result units are specified by the units input with [Configure Units](configure-units.html#GUID-FF5738D7-F9E1-4CA6-AA19-5D335663B40A).

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

#### Programming Patterns

Call [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528) to initiate a measurement before calling Fetch.

Parent topic:

Fetch Power

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=initialize-with-options.html language=enus -->
## TOPIC 00031: Initialize With Options

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `initialize-with-options.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/initialize-with-options.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new session to the device and specifies initialization options, such as setting default values or enabling simulation. resource name Resource name of the device to initialize. error in Error conditions that occur before this node runs. The node responds to this input according to standard

Initialize With Options

Creates a new session to the device and specifies initialization options, such as setting default values or enabling simulation.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### resource name

Resource name of the device to initialize.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### id query

Boolean value that specifies whether NI-568x performs an ID query.

Regardless of how you set this input, NI-568x always checks the device type.

| True | NI-568x performs an ID query. |
| --- | --- |
| False | NI-568x does not perform an ID query. |

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset device

Boolean value that specifies whether to reset the NI-568x device to a known initialization state.

| True | The device is reset. |
| --- | --- |
| False | The device is not reset. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### option string

Initial value of certain properties for the session.

You can set the following properties using this input:

- Range Check
- Query Instrument Status
- Cache
- Record Coercions
- Driver Setup
- Simulate

##### Option String Syntax

The syntax for option string consists of the following relations:

propertyName=value

where

- propertyName is the name of the property.
- value is the value to which the property is set.

##### Syntax for Setting Multiple Properties

To set multiple properties, separate their assignments with a comma.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

NI-568x Nodes

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=initiate.html language=enus -->
## TOPIC 00032: Initiate

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `initiate.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/initiate.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates a measurement or arms the trigger on all enabled channels. This node does not check the instrument status. To check the instrument status, call Error Query at the conclusion of the measurement. session in Instrument session obtained from Initialize With Options. error in Error conditions t

Initiate

Initiates a measurement or arms the trigger on all enabled channels.

This node does not check the instrument status. To check the instrument status, call [Error Query](error-query.html#GUID-ED938E08-3B6F-4325-8E38-FEACAD74D09F) at the conclusion of the measurement.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Measurement

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=invalidate-all-attributes.html language=enus -->
## TOPIC 00033: Invalidate All Attributes

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `invalidate-all-attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/invalidate-all-attributes.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Invalidates the cached values of all properties for the device session. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Defau

Invalidate All Attributes

Invalidates the cached values of all properties for the device session.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=is-measurement-complete.html language=enus -->
## TOPIC 00034: Is Measurement Complete

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `is-measurement-complete.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/is-measurement-complete.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the instrument to determine if measurements are still in progress, complete, or if the measurement status is unknown. This node does not check the instrument status. To check the instrument status, call Error Query at the conclusion of the measurement. session in Instrument session obtained

Is Measurement Complete

Queries the instrument to determine if measurements are still in progress, complete, or if the measurement status is unknown.

This node does not check the instrument status. To check the instrument status, call [Error Query](error-query.html#GUID-ED938E08-3B6F-4325-8E38-FEACAD74D09F) at the conclusion of the measurement.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### measurement status

Status of the measurement.

| Complete | Measurement is complete. |
| --- | --- |
| In Progress | Measurement is in progress. |
| Status Unknown | Measurement status is unknown. |

##### Measurement Status Behavior

Is Measurement Complete

Complete

measurement status

Status Unknown

measurement status

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Measurement

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=is-zero-correction-complete.html language=enus -->
## TOPIC 00035: Is Zero Correction Complete

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `is-zero-correction-complete.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/is-zero-correction-complete.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the instrument to determine if all zero correction operations initiated by Zero are still in progress, complete, or if the status is unknown. This node does not check the instrument status. To check the instrument status, call Error Queryat the conclusion of the measurement. session in Instr

Is Zero Correction Complete

Queries the instrument to determine if all zero correction operations initiated by [Zero](zero.html#GUID-299E64B3-D9B6-4A1C-9315-941876D81398) are still in progress, complete, or if the status is unknown.

This node does not check the instrument status. To check the instrument status, call [Error Query](error-query.html#GUID-ED938E08-3B6F-4325-8E38-FEACAD74D09F)at the conclusion of the measurement.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### zero status

Status of the zeroing.

| 0 | The zero correction is still in progress. |
| --- | --- |
| 1 | A zero correction is complete. |
| -1 | The NI-568x cannot query the device to determine its state. |

##### Zero Status Behavior

This node returns a 
 **1** in the zero status output only when zero corrections are complete on all enabled channels. If the driver cannot query the instrument to determine its state, the driver returns 
 **-1** in the zero status value.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Zeroing

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=measurement.html language=enus -->
## TOPIC 00036: Measurement

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `measurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/measurement.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`

Measurement

NI-568x Nodes

Use NI-568x nodes to develop applications for your RF power meter.

Read Power

power

Initiate

Initiates a measurement or arms the trigger on all enabled channels.

Fetch Power

Returns the result from a previously initiated measurement. After Fetch Power executes, the value of the power output contains an actual reading or array of readings on the channel. The power units are specified by the Units property.

Abort

Aborts all previously initiated measurements and returns the power meter to the Idle state.

Is Measurement Complete

Queries the instrument to determine if measurements are still in progress, complete, or if the measurement status is unknown.

Send Software Trigger

Sends a software trigger to the device.

Parent topic:

NI-568x Nodes

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=ni-568x-properties.html language=enus -->
## TOPIC 00037: NI-568x Properties

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `ni-568x-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/ni-568x-properties.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads) or sets (writes) NI-568x properties. When you read a property, NI-568x analyzes the current configuration to return the coerced value for that property. NI-568x verifies many properties upon reading, thereby either transitioning the session to the verified state or alerting you of an in

NI-568x Properties

Gets (reads) or sets (writes) NI-568x properties.

When you read a property, NI-568x analyzes the current configuration to return the coerced value for that property. NI-568x verifies many properties upon reading, thereby either transitioning the session to the verified state or alerting you of an invalid configuration. Setting or resetting a property transitions the session to an unverified state.

For a list of supported properties, refer to NI-568x Properties.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### NI-568x in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### NI-568x out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

NI-568x Nodes

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=ni568x-nodes.html language=enus -->
## TOPIC 00038: NI-568x Nodes

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `ni568x-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/ni568x-nodes.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use NI-568x nodes to develop applications for your RF power meter.

NI-568x Nodes

Use NI-568x nodes to develop applications for your RF power meter.

Initialize With Options

Creates a new session to the device and specifies initialization options, such as setting default values or enabling simulation.

Close

NI-568x

NI-568x

NI-568x Properties

NI-568x

Configuration

Trigger

NI-568x

Time Slot

Scope

Measurement

Utility

Zeroing

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=read-array.html language=enus -->
## TOPIC 00039: Read Array

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `read-array.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/read-array.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of power measurements. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error error out Error information. The node produces this output according to standard e

Read Array

Returns an array of power measurements.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum time

Maximum time in milliseconds to wait for a return value.

Instead of passing the time in milliseconds, you can pass a predefined constant. 0 specifies an immediate timeout and -1 specifies an infinite timeout.

Default value: 5000

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### power

Value measured by the NI-568x device. The result units are specified by the units input with [Configure Units](configure-units.html#GUID-FF5738D7-F9E1-4CA6-AA19-5D335663B40A).

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

Parent topic:

Read Power

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=read-power.html language=enus -->
## TOPIC 00040: Read Power

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `read-power.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/read-power.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates a measurement, waits until the measurement is complete and returns to the idle state before returning the measurement result(s) in the power output.The units of the power output are the same as the value of the Units property.

Read Power

Initiates a measurement, waits until the measurement is complete and returns to the idle state before returning the measurement result(s) in the power output.The units of the power output are the same as the value of the Units property.

Measurement

Read

Returns a single power measurement.

Read Array

Returns an array of power measurements.

Parent topic:

Measurement

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=read.html language=enus -->
## TOPIC 00041: Read

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `read.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/read.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a single power measurement. Read is only applicable if you set Configure Acquisition Mode to continuous and set buffer size equal to 1. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior De

Read

Returns a single power measurement.

Read is only applicable if you set [Configure Acquisition Mode](configure-acquisition-mode.html#GUID-E4748F71-DF20-413E-97B4-2B2BFD850E26) to continuous and set buffer size equal to 1.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum time

Maximum time in milliseconds to wait for a return value.

Instead of passing the time in milliseconds, you can pass a predefined constant. 0 specifies an immediate timeout and -1 specifies an infinite timeout.

Default value: 5000

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### power

Value measured by the NI-568x device. The result units are specified by the units input with [Configure Units](configure-units.html#GUID-FF5738D7-F9E1-4CA6-AA19-5D335663B40A).

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Read Power

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=reset-with-defaults.html language=enus -->
## TOPIC 00042: Reset With Defaults

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `reset-with-defaults.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/reset-with-defaults.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the instrument and applies initial user-specified settings from the Logical Name used to initialize the session. If the session was created without a Logical Name, this node is equivalent to Reset. session in Instrument session obtained from Initialize With Options. error in Error conditions

Reset With Defaults

Resets the instrument and applies initial user-specified settings from the Logical Name used to initialize the session.

If the session was created without a Logical Name, this node is equivalent to [Reset](reset.html#GUID-991BF771-5DCB-4A5B-8E98-6BD4253E042D).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=reset.html language=enus -->
## TOPIC 00043: Reset

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/reset.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the instrument to a known state. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session out R

Reset

Resets the instrument to a known state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=revision-query.html language=enus -->
## TOPIC 00044: Revision Query

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `revision-query.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/revision-query.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision numbers of the instrument driver and instrument firmware. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavio

Revision Query

Returns the revision numbers of the instrument driver and instrument firmware.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### instrument driver revision

Instrument driver revision number.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### firmware revision

Instrument firmware revision number.

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=scope.html language=enus -->
## TOPIC 00045: Scope

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `scope.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/scope.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`

Scope

NI-568x Nodes

Use NI-568x nodes to develop applications for your RF power meter.

Configure Scope

Configures the length of each scope mode acquisition record and the number of points in each record.

Configure Scope Gate

Specifies the number of seconds from the start of the acquisition at which to start the gate region of the waveform acquisition.

Configure Scope Fence

Configures the scope mode fence inputs and outputs.

Parent topic:

NI-568x Nodes

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=self-test.html language=enus -->
## TOPIC 00046: Self-Test

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `self-test.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/self-test.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a self-test on the NI-568x device and returns the test result. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Defau

Self-Test

Performs a self-test on the NI-568x device and returns the test result.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### self-test result

Value returned from the instrument self test.

When the returned value is 0, the instrument passed the self-test. When the returned value is 1, the instrument failed the self-test.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### self-test message

Self-test response string from the instrument.

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=send-software-trigger.html language=enus -->
## TOPIC 00047: Send Software Trigger

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `send-software-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/send-software-trigger.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a software trigger to the device. Send Software Trigger returns an error if you configure an invalid trigger or you have not previously called Initiate. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node res

Send Software Trigger

Sends a software trigger to the device.

Send Software Trigger returns an error if you configure an invalid trigger or you have not previously called [Initiate](initiate.html#GUID-C099ED68-E609-44AE-8B44-40CE0085DDA1).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5681
- USB-5683
- USB-5684

#### Programming Patterns

To use the software trigger, first call [Configure Trigger Source](configure-trigger-source.html#GUID-C657EB4B-378D-4F25-A490-FC4C5A60ED03), and set the trigger source input to Software.

Parent topic:

Measurement

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=timeslot.html language=enus -->
## TOPIC 00048: Time Slot

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `timeslot.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/timeslot.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`

Time Slot

NI-568x Nodes

Use NI-568x nodes to develop applications for your RF power meter.

Configure Time Slot

Configures the time slot mode inputs and outputs.

Configure Time Slot Exclusion

Configures the exclusion period for each time slot.

Parent topic:

NI-568x Nodes

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=trigger.html language=enus -->
## TOPIC 00049: Trigger

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/trigger.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-568x Trigger nodes to configure triggering configuration options.

Trigger

Use the NI-568x Trigger nodes to configure triggering configuration options.

NI-568x Nodes

Use NI-568x nodes to develop applications for your RF power meter.

Configure Trigger Source

Configures the type of trigger source for the RF power meter.

Configure Internal Trigger

Configures the internal trigger source and slope of the trigger.

Configure Internal Trigger Level

Configures the internal trigger level of the power meter.

Configure External Trigger

Configures the external trigger source and slope of the trigger.

Configure Trigger Delay

Configures the delay between the trigger and the actual measurement.

Configure Trigger Noise Immunity

trigger immunity factor

Configure Trigger Hysteresis

Configures the trigger hysteresis value, in dB.

Parent topic:

NI-568x Nodes

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=utility.html language=enus -->
## TOPIC 00050: Utility

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `utility.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/utility.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`

Utility

NI-568x Nodes

Use NI-568x nodes to develop applications for your RF power meter.

Reset

Resets the instrument to a known state.

Reset With Defaults

Resets the instrument and applies initial user-specified settings from the Logical Name used to initialize the session.

Self-Test

NI-568x

Disable

Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected.

Revision Query

Returns the revision numbers of the instrument driver and instrument firmware.

Error Query

NI-568x

Error Message

NI-568x

Invalidate All Attributes

Invalidates the cached values of all properties for the device session.

Parent topic:

NI-568x Nodes

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=zero.html language=enus -->
## TOPIC 00051: Zero

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `zero.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/zero.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a zero correction on the specified channel. session in Instrument session obtained from Initialize With Options. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error

Zero

Performs a zero correction on the specified channel.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize With Options](initialize-with-options.html#GUID-6A156403-7F02-4834-B082-70CA4C877528).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Name of the channel you want to configure.

- 0
- empty string 
 ""

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This node supports the following hardware:

- USB-5680
- USB-5681
- USB-5683
- USB-5684

#### Programming Patterns

You can use [Is Zero Correction Complete](is-zero-correction-complete.html#GUID-24EEECBE-179E-4A60-B97C-0D73AB34C53C) to determine when the zero correction is complete.

Parent topic:

Zeroing

<!--NI_TOPIC bundle=ni-568x-lvnxg-api-reference path=zeroing.html language=enus -->
## TOPIC 00052: Zeroing

- bundle_id: `ni-568x-lvnxg-api-reference`
- source_path: `zeroing.html`
- source_url: https://docs-be.ni.com/bundle/ni-568x-lvnxg-api-reference/raw/resource/enus/zeroing.html
- document_id: `ni-568x-lvnxg-api-reference`
- page_type: `leaf`
- content_type: `reference`

Zeroing

NI-568x Nodes

Use NI-568x nodes to develop applications for your RF power meter.

Zero

Performs a zero correction on the specified channel.

Is Zero Correction Complete

Zero

Parent topic:

NI-568x Nodes
