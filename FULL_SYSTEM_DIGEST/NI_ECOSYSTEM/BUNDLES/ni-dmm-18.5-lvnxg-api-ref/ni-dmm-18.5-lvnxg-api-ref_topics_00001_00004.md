# NI DOCUMENT BUNDLE: ni-dmm-18.5-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-dmm-18.5-lvnxg-api-ref start=1 end=4 -->
<!--NI_TOPIC bundle=ni-dmm-18.5-lvnxg-api-ref path=abort.html language=enus -->
## TOPIC 00001: Abort

- bundle_id: `ni-dmm-18.5-lvnxg-api-ref`
- source_path: `abort.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-18.5-lvnxg-api-ref/raw/resource/enus/abort.html
- document_id: `ni-dmm-18.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts a previously initiated measurement and returns the DMM to the Idle state. session in Instrument identifier from previous NI-DMM nodes. Default value: None error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard

Abort

Aborts a previously initiated measurement and returns the DMM to the Idle state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument identifier from previous NI-DMM nodes.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Instrument identifier for subsequent NI-DMM nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Low Level Measurement

<!--NI_TOPIC bundle=ni-dmm-18.5-lvnxg-api-ref path=adjust-ac-filter-cal.html language=enus -->
## TOPIC 00002: Adjust AC Filter Calibration

- bundle_id: `ni-dmm-18.5-lvnxg-api-ref`
- source_path: `adjust-ac-filter-cal.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-18.5-lvnxg-api-ref/raw/resource/enus/adjust-ac-filter-cal.html
- document_id: `ni-dmm-18.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calibrates the filter coefficients used for AC measurements. Refer to the calibration procedure for your device before using this node. session in Instrument identifier from previous NI-DMM nodes. Default value: None function Calibration mode used to acquire the measurement. range Range to calibrate

Adjust AC Filter Calibration

Calibrates the filter coefficients used for AC measurements.

Refer to the calibration procedure for your device before using this node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument identifier from previous NI-DMM nodes.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### function

Calibration mode used to acquire the measurement.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### range

Range to calibrate.

Auto Range is not supported for calibration operations.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### expected value

Expected value of the measurement.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency

Frequency of the input signal.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Instrument identifier for subsequent NI-DMM nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Hardware Support

This feature is supported on the PXIe-4080/4081/4082, PXI-4070/4071/4072, and PCI-4070.

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-dmm-18.5-lvnxg-api-ref path=set-cal-user-defined-info.html language=enus -->
## TOPIC 00003: Set Calibration User Defined Info

- bundle_id: `ni-dmm-18.5-lvnxg-api-ref`
- source_path: `set-cal-user-defined-info.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-18.5-lvnxg-api-ref/raw/resource/enus/set-cal-user-defined-info.html
- document_id: `ni-dmm-18.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores user-defined information in the EEPROM. Use Get Calibration User Defined Info Maximum Size to see the maximum allowed string size. session in Instrument identifier from previous NI-DMM nodes. Default value: None info Custom information to be stored in the EEPROM. error in Error conditions tha

Set Calibration User Defined Info

Stores user-defined information in the EEPROM.

Use Get Calibration User Defined Info Maximum Size to see the maximum allowed string size.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument identifier from previous NI-DMM nodes.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### info

Custom information to be stored in the EEPROM.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Instrument identifier for subsequent NI-DMM nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Exceeding Maximum String Size

If the Info string size is larger than the maximum string size, NI-DMM stores as much of the information as possible, truncates the remainder, and returns a warning.

#### Examples

Use this node to store information that could be useful for future calibrations, such as the name of the person who performed the calibration or specifics about the calibration system.

Parent topic:

Calibration Utilities

<!--NI_TOPIC bundle=ni-dmm-18.5-lvnxg-api-ref path=temperature.html language=enus -->
## TOPIC 00004: Temperature

- bundle_id: `ni-dmm-18.5-lvnxg-api-ref`
- source_path: `temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-18.5-lvnxg-api-ref/raw/resource/enus/temperature.html
- document_id: `ni-dmm-18.5-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure a DMM for temperature measurements.

Temperature

Configure a DMM for temperature measurements.

Configuration

Configure and control a DMM.

Configure Fixed Reference Junction

Configures the fixed reference junction temperature for a thermocouple with a fixed reference junction type.

Configure RTD Custom

Configures the A, B, and C parameters for a custom RTD.

Configure RTD Type

Configures the RTD Type and RTD Resistance properties for an RTD.

Configure Thermistor Custom

Configures the A, B, and C parameters for a custom thermistor.

Configure Thermistor Type

Configures the thermistor type.

Configure Thermocouple

Configures the thermocouple type and reference junction type for a chosen thermocouple.

Configure Transducer Type

Configures the transducer type.

Parent topic:

Configuration
