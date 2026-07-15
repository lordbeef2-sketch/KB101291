# NI DOCUMENT BUNDLE: ni-5690-driver-software-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-5690-driver-software-lvnxg-api-ref start=1 end=7 -->
<!--NI_TOPIC bundle=ni-5690-driver-software-lvnxg-api-ref path=close.html language=enus -->
## TOPIC 00001: Close

- bundle_id: `ni-5690-driver-software-lvnxg-api-ref`
- source_path: `close.html`
- source_url: https://docs-be.ni.com/bundle/ni-5690-driver-software-lvnxg-api-ref/raw/resource/enus/close.html
- document_id: `ni-5690-driver-software-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Terminates the instrument I/O session, destroys the instrument driver session and any attributes, and deallocates any memory resources used by the NI-5690 instrument driver and supported hardware. session in Instrument session obtained from Initialize. error in Error conditions that occur before thi

Close

Terminates the instrument I/O session, destroys the instrument driver session and any attributes, and deallocates any memory resources used by the NI-5690 instrument driver and supported hardware.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize](initialize.html#GUID-6489A6EE-A223-42B9-8CE4-04773CAFD79A).

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

- PXI-5690
- PXI-5691
- PXI-5695

Parent topic:

NI-5690 Nodes

<!--NI_TOPIC bundle=ni-5690-driver-software-lvnxg-api-ref path=configure-gain.html language=enus -->
## TOPIC 00002: Configure Gain

- bundle_id: `ni-5690-driver-software-lvnxg-api-ref`
- source_path: `configure-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-5690-driver-software-lvnxg-api-ref/raw/resource/enus/configure-gain.html
- document_id: `ni-5690-driver-software-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the gain (in dB) of a channel. A negative value indicates attenuation. This node returns an error if the requested gain is too high or too low for the device to configure at the specified frequency. The node also returns an error if the appropriate channel name is not specified. session i

Configure Gain

Configures the gain (in dB) of a channel.

A negative value indicates attenuation. This node returns an error if the requested gain is too high or too low for the device to configure at the specified frequency. The node also returns an error if the appropriate channel name is not specified.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize](initialize.html#GUID-6489A6EE-A223-42B9-8CE4-04773CAFD79A).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Channel through which the input RF signal is routed and in which gain is applied.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### gain

Gain applied to the input RF signal in dB.

Actual gain may be set to the closest higher available gain setting. The gain may be set to a negative number to indicate attenuation.

Default value: 
 0 dB

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency

Frequency of the input RF signal in Hz.

Default value: 
 100 MHz

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

- PXI-5690
- PXI-5691
- PXI-5695

#### Device-Specific Configurable Gain Support

The PXI-5690 and PXI-5691 support configurable gain for CH 1 only, while the PXI-5695 supports configurable gain for CH 0 only.

Parent topic:

NI-5690 Nodes

<!--NI_TOPIC bundle=ni-5690-driver-software-lvnxg-api-ref path=configure-path.html language=enus -->
## TOPIC 00003: Configure Path

- bundle_id: `ni-5690-driver-software-lvnxg-api-ref`
- source_path: `configure-path.html`
- source_url: https://docs-be.ni.com/bundle/ni-5690-driver-software-lvnxg-api-ref/raw/resource/enus/configure-path.html
- document_id: `ni-5690-driver-software-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the path through which the signal is routed. The direct path routes the input signal directly to the output of the RF signal conditioning device. This node reports errors if the appropriate channel name is not specified. session in Instrument session obtained from Initialize. error in Erro

Configure Path

Specifies the path through which the signal is routed.

The direct path routes the input signal directly to the output of the RF signal conditioning device. This node reports errors if the appropriate channel name is not specified.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize](initialize.html#GUID-6489A6EE-A223-42B9-8CE4-04773CAFD79A).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Channel in which to use the specified path.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### path

Path used by the device.

Default value: Main Path

##### Main Path and Direct Path Behavior by Device

The following table shows how the main path and direct path vary by device.

[IMAGE alt='1378' src='GUID-17906CA4-AB00-4C92-8BD1-BAE8B2EE8E2A-a5.svg']

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

- PXI-5690
- PXI-5691
- PXI-5695

#### Device-Specific Configurable Path Support

The PXI-5690 and PXI-5691 support configurable paths for CH 1 only, while the PXI-5695 supports configurable gain for CH 0 only.

For the PXI-5690 and PXI-5691, the main path allows you to configure gain using [Configure Gain](configure-gain.html#GUID-AF5823AD-EF86-4048-A1F0-BF00F0E9A5A7).

Parent topic:

NI-5690 Nodes

<!--NI_TOPIC bundle=ni-5690-driver-software-lvnxg-api-ref path=get-actual-gain.html language=enus -->
## TOPIC 00004: Get Actual Gain

- bundle_id: `ni-5690-driver-software-lvnxg-api-ref`
- source_path: `get-actual-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-5690-driver-software-lvnxg-api-ref/raw/resource/enus/get-actual-gain.html
- document_id: `ni-5690-driver-software-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the actual gain (in dB) applied to the input signal for the channel and frequency you specify. If you want to retain the previous state of the device, do not call Get Actual Gain before you call Configure Path or Configure Gain. session in Instrument session obtained from Initialize. error i

Get Actual Gain

Returns the actual gain (in dB) applied to the input signal for the channel and frequency you specify.

If you want to retain the previous state of the device, do not call Get Actual Gain before you call [Configure Path](configure-path.html#GUID-0427FBA0-B221-442A-8C0C-FD1D492F535D) or [Configure Gain](configure-gain.html#GUID-AF5823AD-EF86-4048-A1F0-BF00F0E9A5A7).

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize](initialize.html#GUID-6489A6EE-A223-42B9-8CE4-04773CAFD79A).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name

Channel in which the actual gain is applied.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency

Frequency of the input RF signal in Hz.

Default value: 
 100 MHz

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

Reference to your instrument session passed to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### actual gain

Gain applied in the specified channel name at the specified frequency at normal ambient temperature, in dB.

For spectral measurements, subtract this gain from your calculated spectrum to remove the effect of the RF signal conditioning device on the measurements. For I/Q measurements, convert the gain to linear units and then apply the correction to the I/Q data. Negative values indicate attenuation.

#### Hardware Support

This node supports the following hardware:

- PXI-5690
- PXI-5691
- PXI-5695

#### Device-Specific Get Actual Gain Support

For the PXI-5695, when you call Get Actual Gain before [Configure Path](configure-path.html#GUID-0427FBA0-B221-442A-8C0C-FD1D492F535D) for CH 0, CH 0 reinitializes to a default state (Main Path). When you call Get Actual Gain before [Configure Gain](configure-gain.html#GUID-AF5823AD-EF86-4048-A1F0-BF00F0E9A5A7) for CH 1, CH 1 reinitializes to its default state (maximum attenuation).

For the PXI-5690 and PXI-5691, when you call Get Actual Gain before [Configure Path](configure-path.html#GUID-0427FBA0-B221-442A-8C0C-FD1D492F535D) or [Configure Gain](configure-gain.html#GUID-AF5823AD-EF86-4048-A1F0-BF00F0E9A5A7) for CH 1, CH 1 reinitializes to its default state (maximum gain and Main Path). Additionally, if you call [Configure Path](configure-path.html#GUID-0427FBA0-B221-442A-8C0C-FD1D492F535D) before you call [Configure Gain](configure-gain.html#GUID-AF5823AD-EF86-4048-A1F0-BF00F0E9A5A7), CH 1 reinitializes to the default state for the path (Main Path).

Parent topic:

NI-5690 Nodes

<!--NI_TOPIC bundle=ni-5690-driver-software-lvnxg-api-ref path=get-temperature.html language=enus -->
## TOPIC 00005: Get Temperature

- bundle_id: `ni-5690-driver-software-lvnxg-api-ref`
- source_path: `get-temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-5690-driver-software-lvnxg-api-ref/raw/resource/enus/get-temperature.html
- document_id: `ni-5690-driver-software-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current temperature of the hardware module in degrees Celsius. session in Instrument session obtained from Initialize. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value:

Get Temperature

Returns the current temperature of the hardware module in degrees Celsius.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

Instrument session obtained from [Initialize](initialize.html#GUID-6489A6EE-A223-42B9-8CE4-04773CAFD79A).

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

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### temperature

Current temperature of the hardware module in degrees Celsius.

#### Hardware Support

This node supports the following hardware:

- PXI-5690
- PXI-5691
- PXI-5695

Parent topic:

NI-5690 Nodes

<!--NI_TOPIC bundle=ni-5690-driver-software-lvnxg-api-ref path=initialize.html language=enus -->
## TOPIC 00006: Initialize

- bundle_id: `ni-5690-driver-software-lvnxg-api-ref`
- source_path: `initialize.html`
- source_url: https://docs-be.ni.com/bundle/ni-5690-driver-software-lvnxg-api-ref/raw/resource/enus/initialize.html
- document_id: `ni-5690-driver-software-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instrument session to the hardware and performs device-specific initialization actions. resource name Resource name of the device to initialize. Default value: " " (empty string) Device Name Syntax For NI-5690 devices, the syntax is the device name specified in MAX. The typical default

Initialize

Creates a new instrument session to the hardware and performs device-specific initialization actions.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### resource name

Resource name of the device to initialize.

Default value: " " (empty string)

##### Device Name Syntax

For NI-5690 devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is 
 PXI1Slot2. You can rename your devices by right-clicking the name in MAX, selecting 
 Rename from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility.

Note

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### id query

This input is not supported in this version of the NI-5690 instrument driver.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset

Boolean value that specifies whether to reset the RF signal conditioning device during the initialization procedure.

| True | The RF signal conditioning device is initialized to the default state. |
| --- | --- |
| False | No changes are made to the pre-existing hardware state during initialization. |

Default value: False

##### Device-Specific Initialization States

The initialization states for each device are as follows:

- For the PXI-5690 , the gain input in [Configure Gain](configure-gain.html#GUID-AF5823AD-EF86-4048-A1F0-BF00F0E9A5A7) is set to maximum gain.
- For the PXI-5691 , the gain input in [Configure Gain](configure-gain.html#GUID-AF5823AD-EF86-4048-A1F0-BF00F0E9A5A7) is set to minimum gain.
- For the PXI-5695 , the gain input in [Configure Gain](configure-gain.html#GUID-AF5823AD-EF86-4048-A1F0-BF00F0E9A5A7) is set to maximum attenuation.
- For all RF signal conditioning devices, the path is set to Main Path.

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

- PXI-5690
- PXI-5691
- PXI-5695

#### Device-Specific Initialization Actions

Initialize performs the following device-specific initialization actions:

- Returns a session that you use to identify the PXI-5690 device in all subsequent NI-5690 instrument driver nodes.
- For the PXI-5690 , when reset is True, initializes all configurable channels to use maximum gain and main path for variable path channels.
- For the PXI-5691 and PXI-5695 , when reset is True, initializes all configurable channels to use minimum gain and main path for variable path channels.

Parent topic:

NI-5690 Nodes

<!--NI_TOPIC bundle=ni-5690-driver-software-lvnxg-api-ref path=ni5690-nodes.html language=enus -->
## TOPIC 00007: NI-5690 Nodes

- bundle_id: `ni-5690-driver-software-lvnxg-api-ref`
- source_path: `ni5690-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-5690-driver-software-lvnxg-api-ref/raw/resource/enus/ni5690-nodes.html
- document_id: `ni-5690-driver-software-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use NI-5690 nodes to develop applications for your RF signal conditioning device.

NI-5690 Nodes

Use NI-5690 nodes to develop applications for your RF signal conditioning device.

Initialize

Creates a new instrument session to the hardware and performs device-specific initialization actions.

Configure Gain

Configures the gain (in dB) of a channel.

Close

NI-5690 instrument driver

Configure Path

Specifies the path through which the signal is routed.

Get Actual Gain

Returns the actual gain (in dB) applied to the input signal for the channel and frequency you specify.

Get Temperature

Returns the current temperature of the hardware module in degrees Celsius.
