# NI DOCUMENT BUNDLE: labview-nxg-ivi-compliance-package

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-ivi-compliance-package start=1 end=71 -->
<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=GUID-87AB4024-39D6-4C2B-AF0E-B1DF0D2835CD.html language=enus -->
## TOPIC 00001: IVIDCPwr Interchangeability Info Nodes

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `GUID-87AB4024-39D6-4C2B-AF0E-B1DF0D2835CD.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/GUID-87AB4024-39D6-4C2B-AF0E-B1DF0D2835CD.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVIDCPwr Interchangeability Info Nodes

IVIDCPwr Utility Nodes

IviDCPwr Get Next Interchange Warning

Returns the interchangeability warnings associated with the IVI session.

IviDCPwr Clear Interchange Warnings

Clears the list of current interchange warnings.

IviDCPwr Reset Interchange Check

Determines if each test module completely configures the state of each instrument it uses. By calling this node at the beginning of a test module, you can determine whether the test module has dependencies on the operation of previously executed test modules.

Parent topic:

IVIDCPwr Utility Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=icp-nodes.html language=enus -->
## TOPIC 00002: IVI Compliance Package Nodes

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `icp-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/icp-nodes.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Compliance Package Nodes

IVI Oscilloscope

IVI Dmm

IVI Function Generator

IVI DC Power Supply

Develop interchangeable applications for your DC power supply.

IVI Switch

IVI RF Signal Generator

IVI Spectrum Analyzer Nodes

IVI Pwr Meter Nodes

Develop interchangeable applications for your power meter.

IVI Counter Nodes

IVI AC Power Supply

IVI Digitizer Nodes

IVI Upconverter Nodes

IVI Downconverter Nodes

Advanced

Perform advanced IVI session functions.

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=iviacpwr-abort-current-ramp.html language=enus -->
## TOPIC 00003: IviACPwr Abort Current Ramp [CR]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `iviacpwr-abort-current-ramp.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/iviacpwr-abort-current-ramp.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts a current ramp. If a current ramp is not in progress, this VI does nothing. instrument handle The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options. The handle identifies a particular instrument session. Default value: None error in Error condition

IviACPwr Abort Current Ramp [CR]

Aborts a current ramp. If a current ramp is not in progress, this VI does nothing.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### phase name

Specifies the name of the output on which to configure the current limit.

Pass the virtual output phase name that you assign to the instrument in the IVI Configuration utility.

Users who want to achieve interchangeability should use a virtual output phase name. The virtual output phase name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical output phase name.

Virtual output phase names are aliases for instrument-specific output phase strings, which can differ from one instrument to another. With virtual output phase names, you can use and swap instruments without having to change the output phase names in your source code. Assign a virtual output phase name to an instrument-specific output phase through the IVI Configuration utility. This control accepts virtual output phase names you have assigned to the specific instrument you are using and also accepts the instrument-specific output phase names.

Default Value: ""

Note

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI AC Power Current Ramp Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=iviacpwr-abort-voltage-ramp.html language=enus -->
## TOPIC 00004: IviACPwr Abort Voltage Ramp [VR]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `iviacpwr-abort-voltage-ramp.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/iviacpwr-abort-voltage-ramp.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts a voltage ramp. If a voltage ramp is not in progress, this VI does nothing. instrument handle The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options. The handle identifies a particular instrument session. Default value: None error in Error condition

IviACPwr Abort Voltage Ramp [VR]

Aborts a voltage ramp. If a voltage ramp is not in progress, this VI does nothing.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### phase name

Specifies the name of the output on which to configure the current limit.

Pass the virtual output phase name that you assign to the instrument in the IVI Configuration utility.

Users who want to achieve interchangeability should use a virtual output phase name. The virtual output phase name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical output phase name.

Virtual output phase names are aliases for instrument-specific output phase strings, which can differ from one instrument to another. With virtual output phase names, you can use and swap instruments without having to change the output phase names in your source code. Assign a virtual output phase name to an instrument-specific output phase through the IVI Configuration utility. This control accepts virtual output phase names you have assigned to the specific instrument you are using and also accepts the instrument-specific output phase names.

Default Value: ""

Note

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI AC Power Voltage Ramp Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=iviacpwr-action-status-nodes.html language=enus -->
## TOPIC 00005: IVI AC Power Action Status Nodes

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `iviacpwr-action-status-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/iviacpwr-action-status-nodes.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI AC Power Action Status Nodes

IVI AC Power Supply

IVI AC Power Voltage Ramp Nodes

IVI AC Power Current Ramp Nodes

IVI AC Power Frequency Ramp Nodes

Parent topic:

IVI AC Power Supply

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=iviacpwr-arb-waveform.html language=enus -->
## TOPIC 00006: IviACPwr Arb Waveform Nodes

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `iviacpwr-arb-waveform.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/iviacpwr-arb-waveform.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IviACPwr Arb Waveform Nodes

IVI AC Power Supply Configuration Nodes

IviACPwr Clear Arb Waveform [ARB]

This VI deletes individual user-defined waveforms from the memory of the power source.

IviACPwr Query Arb Waveform Catalog [ARB]

This VI returns a comma delimited string of user-defined and/or fixed vendor-defined waveform names currently stored in the AC power source.

IviACPwr Write Arb Waveform [ARB]

Writes an individual user-defined waveform to the AC power source's memory. If the power source cannot store any more arbitrary waveforms, this VI returns the No Waveforms Available error.

Parent topic:

IVI AC Power Supply Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=iviacpwr-configure-voltage-protection-vp.html language=enus -->
## TOPIC 00007: IviACPwr Configure Voltage Protection [VP]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `iviacpwr-configure-voltage-protection-vp.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/iviacpwr-configure-voltage-protection-vp.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures voltage protection. When the Over Volt Protection Enabled input and/or Under Volt Protection Enabled input is True, the AC power source enters the voltage protection state (tripped) and disables the output when the output voltage is below the value in the Under Voltage Limit control or ab

IviACPwr Configure Voltage Protection [VP]

Configures voltage protection. When the Over Volt Protection Enabled input and/or Under Volt Protection Enabled input is True, the AC power source enters the voltage protection state (tripped) and disables the output when the output voltage is below the value in the Under Voltage Limit control or above the value in the Over Voltage Limit control. When the Over Volt Protection Enabled input and/or Under Volt Protection Enabled input is False, the corresponding limit does not affect the instrument's behavior and under and/or over voltage protection is disabled.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### Over Voltage Limit

Specifies the over voltage protection limit. The driver uses this value to set the IviACPwr Over Voltage Protection Limit [VP] property. 
 
Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### Over Volt Protection Enabled (True)

Enables or disables the over voltage protection. The driver uses this value to set IviACPwr Over Voltage Protection Enabled [VP] property. 
 
Valid Values: 
TRUE - Enables the over voltage protection. 
FALSE - Disables the over voltage protection. 
 
Default Value: 
True

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### Phase Name ("")

Specifies the name of the output phase to configure. Pass the virtual output phase name that you assign to the instrument in the IVI Configuration utility. Users who want to achieve interchangeability should use a virtual output phase name. The virtual output phase name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical output phase name. Virtual output phase names are aliases for instrument-specific output phase strings, which can differ from one instrument to another. With virtual output phase names, you can use and swap instruments without having to change the output phase names in your source code. Assign a virtual output phase name to an instrument-specific output phase through the IVI Configuration utility. This control accepts virtual output phase names you have assigned to the specific instrument you are using and also accepts the instrument-specific output phase names. Default Value: "" Note: You can specify the output phase name as a string variable or as a literal enclosed in double quotes.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### Under Volt Protection Enabled (True)

Enables or disables the under voltage protection. The driver uses this value to set IviACPwr Under Voltage Protection Enabled [VP] property. 
 
Valid Values: 
TRUE - Enables the under voltage protection. 
FALSE - Disables the under voltage protection. 
 
Default Value: 
True

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### Under Voltage Limit

Specifies the under voltage protection limit. The driver uses this value to set IviACPwr Under Voltage Protection Limit [VP] property. 
 
Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IviACPower Voltage Protection Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=iviacpwr-configure-voltage-range.html language=enus -->
## TOPIC 00008: IviACPwr Configure Voltage Range

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `iviacpwr-configure-voltage-range.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/iviacpwr-configure-voltage-range.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the voltage range of the AC power source. instrument handle The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options. The handle identifies a particular instrument session. Default value: None error in Error conditions that occur before this node

IviACPwr Configure Voltage Range

Configures the voltage range of the AC power source.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### phase name

Specifies the name of the output on which to configure the current limit.

Pass the virtual output phase name that you assign to the instrument in the IVI Configuration utility.

Users who want to achieve interchangeability should use a virtual output phase name. The virtual output phase name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical output phase name.

Virtual output phase names are aliases for instrument-specific output phase strings, which can differ from one instrument to another. With virtual output phase names, you can use and swap instruments without having to change the output phase names in your source code. Assign a virtual output phase name to an instrument-specific output phase through the IVI Configuration utility. This control accepts virtual output phase names you have assigned to the specific instrument you are using and also accepts the instrument-specific output phase names.

Default Value: ""

Note

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### range

Specifies the voltage range of the power source.

The driver uses this value to set the IviACPwr Voltage Range property.

Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI AC Power Supply Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=iviacpwr-error-message.html language=enus -->
## TOPIC 00009: IviACPwr Error Message

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `iviacpwr-error-message.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/iviacpwr-error-message.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a status code returned by an instrument driver node into a user-readable string. instrument handle The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options. The handle identifies a particular instrument session. Default value: None error in Error co

IviACPwr Error Message

Converts a status code returned by an instrument driver node into a user-readable string.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### error code

Passes the Status value that is returned from any of the instrument driver nodes.

Default Value: 0 (VI_SUCCESS (0))

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### error message

Returns the error message string read from the instrument's error message queue.

256 bytes

Parent topic:

IVI AC Power Supply Utility Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=iviacpwr-error-query.html language=enus -->
## TOPIC 00010: IviACPwr Error-Query

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `iviacpwr-error-query.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/iviacpwr-error-query.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads an error code and a message from the instrument's error queue. instrument handle The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options. The handle identifies a particular instrument session. Default value: None error in Error conditions that occur b

IviACPwr Error-Query

Reads an error code and a message from the instrument's error queue.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### error code

Returns the error code read from the instrument's error queue.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### error message

Returns the error message string read from the instrument's error message queue.

256 bytes

Parent topic:

IVI AC Power Supply Utility Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=iviacpwr-reset-with-defaults.html language=enus -->
## TOPIC 00011: IviACPwr Reset With Defaults

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `iviacpwr-reset-with-defaults.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/iviacpwr-reset-with-defaults.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the instrument and applies initial user-specified settings from the logical name which was used to initialize the session. If the session was created without a logical name, this node is equivalent to the IviACPwr Reset Node. instrument handle The instrument handle that you obtain from IviACP

IviACPwr Reset With Defaults

Resets the instrument and applies initial user-specified settings from the 
logical name which was used to initialize the session. If the session was created without a 
logical name, this node is equivalent to the IviACPwr Reset Node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from IviACPwr Initialize or IviACPwr Initialize With Options.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI AC Power Supply Utility Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivicounter-config-edge-time-rfrnc-levels.html language=enus -->
## TOPIC 00012: IviCounter Configure Edge Time Reference Levels

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivicounter-config-edge-time-rfrnc-levels.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivicounter-config-edge-time-rfrnc-levels.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the IviCounter Edge Time Reference Type, IviCounter Edge Time Estimate, IviCounter Edge Time Resolution, IviCounter Edge Time High Reference Level, and IviCounter Edge Time Low Reference Level properties for an edge time measurement. If the channel slope is positive a rise-time measuremen

IviCounter Configure Edge Time Reference Levels

Configures the IviCounter Edge Time Reference Type, IviCounter Edge Time Estimate, IviCounter Edge Time Resolution, IviCounter Edge Time High Reference Level, and IviCounter Edge Time Low Reference Level properties for an edge time measurement. If the channel slope is positive a rise-time measurement is performed, if the channel slope is negative, a fall-time measurement is performed.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### reference type

Specifies the reference type. The driver sets the IviCounter Edge Time Reference Type property to this value. Valid Values: IVICOUNTER_VAL_VOLTAGE_REFERENCE_TYPE - Voltage IVICOUNTER_VAL_PERCENT_REFERENCE_TYPE - Percent Default Value: IVICOUNTER_VAL_VOLTAGE_REFERENCE_TYPE

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle you obtain from the IviCounter Initialize node or IviCounter Initialize With Options node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel ("")

Specifies the name of the channel to configure. The driver sets the IviCounter Edge Time Channel property to this value.

Users who want to achieve interchangeability should use a virtual channel name. The virtual channel name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical channel name.

Default Value: ""

Notes: You can specify the channel name as a string variable or as a literal enclosed in double quotes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### estimate (0.1 s)

Specifies the estimated measurement edge time. The driver sets the IviCounter Edge Time Estimate property to this value. Units: seconds Default Value: 0.1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### resolution (0.01 s)

Specifies the resolution of the edge time measurement. It is the quantization size, or the smallest delta value that can be detected. The driver sets the IviCounter Edge Time Resolution property to this value. Units: seconds Default Value: 0.01

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### high reference (0.1)

Specifies the high reference level for the edge time. The driver sets the IviCounter Edge Time High Reference property to this value. Units: volt or percent Default Value: 0.1

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### low reference (0.9)

Specifies the low reference level for the edge time. The driver sets the IviCounter Edge Time Low Reference property to this value. Units: volt or percent Default Value: 0.9

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle you obtain from IviCounter Initialize or IviCounter Initialize With Options. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Counter Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividcpwr-initiate.html language=enus -->
## TOPIC 00013: IviDCPwr Initiate [TRG]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividcpwr-initiate.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividcpwr-initiate.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates output changes that you previously specified. After you call this VI, the power supply waits for the trigger you specify with the IviDCPwr Configure Trigger Source [TRG] VI. After the power supply detects the trigger, it updates its voltage level and current limit to the values you specify

IviDCPwr Initiate [TRG]

Initiates output changes that you previously specified.
 After you call this VI, the power supply waits for the trigger you specify with the IviDCPwr Configure Trigger Source [TRG] VI. After the power supply detects the trigger, it updates its voltage level and current limit to the values you specify with the IviDCPwr Configure Triggered Voltage Level [TRG] and IviDCPwr Configure Triggered Current Limit [TRG] VIs.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDCPwr Initialize or IviDCPwr Initialize With Options node. The handle identifies a particular instrument session. Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDCPwr Initialize or IviDCPwr Initialize With Options node. The handle identifies a particular instrument session. Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVIDCPwr Output Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividcpwr-query-max-current-limit.html language=enus -->
## TOPIC 00014: IviDCPwr Query Max Current Limit

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividcpwr-query-max-current-limit.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividcpwr-query-max-current-limit.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum programmable current limit that the power supply accepts for a particular voltage level on a channel for the output range to which the power supply is currently configured. instrument handle The instrument handle that you obtain from the IviDCPwr Initialize or IviDCPwr Initialize

IviDCPwr Query Max Current Limit

Returns the maximum programmable current limit that the power supply accepts for a particular voltage level on a channel for the output range to which the power supply is currently configured.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDCPwr Initialize or IviDCPwr Initialize With Options node. The handle identifies a particular instrument session. Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name ("CHANNEL1")

Specifies the virtual channel name that you assign to the instrument in the Configuration Utility.

Default value: "CHANNEL1"

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### voltage level (0.0 Volts)

Pass the voltage level for which to determine the maximum programmable current limit. 

Units: volts (V).

Default Value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDCPwr Initialize or IviDCPwr Initialize With Options node. The handle identifies a particular instrument session. Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### max current limit

This parameter returns the maximum programmable current limit for the voltage level you specify.

Units: amps (A)

Parent topic:

IVIDCPwr Output Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividcpwr-query-max-voltage-level.html language=enus -->
## TOPIC 00015: IviDCPwr Query Max Voltage Level

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividcpwr-query-max-voltage-level.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividcpwr-query-max-voltage-level.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum programmable voltage level that the power supply accepts for a particular current limit on a channel for the output range to which the power supply is currently configured. instrument handle The instrument handle that you obtain from the IviDCPwr Initialize or IviDCPwr Initialize

IviDCPwr Query Max Voltage Level

Returns the maximum programmable voltage level that the power supply accepts for a particular current limit on a channel for the output range to which the power supply is currently configured.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDCPwr Initialize or IviDCPwr Initialize With Options node. The handle identifies a particular instrument session. Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name ("CHANNEL1")

Specifies the virtual channel name that you assign to the instrument in the Configuration Utility.

Default value: "CHANNEL1"

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### current limit (0.0 Amps)

Pass the current limit for which to determine the maximum programmable voltage level. 

Units: amps (A).

Default Value: 0.0

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDCPwr Initialize or IviDCPwr Initialize With Options node. The handle identifies a particular instrument session. Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### max voltage level

This parameter returns the maximum programmable voltage level for the current limit you specify.

Units: volts (V)

Parent topic:

IVIDCPwr Output Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividcpwr-query-output-state.html language=enus -->
## TOPIC 00016: IviDCPwr Query Output State

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividcpwr-query-output-state.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividcpwr-query-output-state.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the power supply is in a particular output state. When either an over-voltage condition or an over-current condition occurs, the power supply's output protection disables the output. If the power supply is in an over-voltage or over-current state, it does not produce power until the

IviDCPwr Query Output State

Returns whether the power supply is in a particular output state. When either an over-voltage condition or an over-current condition occurs, the power supply's output protection disables the output. If the power supply is in an over-voltage or over-current state, it does not produce power until the output protection is reset. The IviDCPwr Reset Output Protection Node resets the output protection. Once the output protection is reset, the power supply resumes generating a power signal.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDCPwr Initialize or IviDCPwr Initialize With Options node. The handle identifies a particular instrument session. Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name ("CHANNEL1")

Specifies the virtual channel name that you assign to the instrument in the Configuration Utility.

Default value: "CHANNEL1"

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### output state (Constant Voltage)

Pass the output state for which you want to query.

Defined Values:
IVIDCPWR_VAL_OUTPUT_CONSTANT_VOLTAGE - Constant Voltage State

IVIDCPWR_VAL_OUTPUT_CONSTANT_CURRENT - Constant Current State

IVIDCPWR_VAL_OUTPUT_UNREGULATED - Unregulated State

IVIDCPWR_VAL_OUTPUT_OVER_VOLTAGE - Over-voltage State

IVIDCPWR_VAL_OUTPUT_OVER_CURRENT - Over-current State

Default Value: IVIDCPWR_VAL_OUTPUT_CONSTANT_VOLTAGE

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDCPwr Initialize or IviDCPwr Initialize With Options node. The handle identifies a particular instrument session. Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### in state

This parameter returns TRUE if the power supply is currently in the state you specify with the OutputState parameter, and FALSE if it is not.

#### Output Conditions

1. A constant voltage condition occurs when the output voltage is equal to the value of the IviDCPwr>>Basic Operation>>Voltage Level property and the current is less than or equal to the value of the IviDCPwr>>Basic Operation>>Current Limit property.
2. A constant current condition occurs when the output current is equal to the value of the IviDCPwr>>Basic Operation>>Current Limit property and the IviDCPwr>>Basic Operation>>Current Limit Behavior property is set to IVIDCPWR_VAL_CURRENT_REGULATE.
3. An unregulated condition occurs when the output voltage is less than the value of the IviDCPwr>>Basic Operation>>Voltage Level property and the current is less than the value of the IviDCPwr>>Basic Operation>>Current Limit property.
4. An over-voltage condition occurs when the output voltage is equal to or greater than the value of the IviDCPwr>>Basic Operation>>OVP Limit property and the IviDCPwr>>Basic Operation>>OVP Enabled property is set to TRUE.
5. An over-current condition occurs when the output current is equal to or greater than the value of the IviDCPwr>>Basic Operation>>Current Limit property and the IviDCPwr>>Basic Operation>>Current Limit Behavior property is set to IVIDCPWR_VAL_CURRENT_TRIP.

Parent topic:

IVIDCPwr Output Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividigitizer-configure-glitch-arm-source.html language=enus -->
## TOPIC 00017: IviDigitizer Configure Glitch Arm Source [GA]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividigitizer-configure-glitch-arm-source.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividigitizer-configure-glitch-arm-source.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the glitch arm. A glitch arm occurs when the arm signal has a pulse with a width that is less than or greater than the glitch width. The end user specifies which comparison criterion to use with the GlitchCondition parameter. The end-user specifies the glitch width with the Glitch Width i

IviDigitizer Configure Glitch Arm Source [GA]

Configures the glitch arm. A glitch arm occurs when the arm signal has a pulse with a width that is less than or greater than the glitch width.

The end user specifies which comparison criterion to use with the GlitchCondition parameter. The end-user specifies the glitch width with the Glitch Width input. The end-user specifies the polarity of the pulse with the Glitch Polarity input.

The arm does not actually occur until the edge of a pulse that corresponds to the Glitch Width input and Glitch Polarity input crosses the threshold the end-user specifies in the trigger level parameter. This node affects instrument behavior only if the arm type is glitch arm.

Note

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### Glitch Polarity (Positive)

Specifies the glitch polarity. This value sets the IviDigitizer Glitch Arm Polarity property.

Valid Values:

- IVIDIGITIZER_VAL_GLITCH_POSITIVE (1) 
 The digitizer triggers on a positive glitch.

- IVIDIGITIZER_VAL_GLITCH_NEGATIVE (2) 
 The digitizer triggers on a negative glitch.

- IVIDIGITIZER_VAL_GLITCH_EITHER (3) 
 The digitizer triggers on either a positive or negative glitch.

Default Value: IVIDIGITIZER_VAL_GLITCH_POSITIVE (1)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### Glitch Width (0.1)

Specifies the glitch arming glitch width, in seconds. This value sets the IviDigitizer Glitch Arm Width property.

Unit: second

Default Value: 0.1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### Glitch Condition (Less Than)

Specifies the glitch condition. This value sets the IviDigitizer Glitch Arm Condition property.

Valid Values:

- IVIDIGITIZER_VAL_GLITCH_LESS_THAN (1) 
 The digitizer triggers when the pulse width is less than the value you specify with the IviDigitizer Glitch Arm Width property.

- IVIDIGITIZER_VAL_GLITCH_GREATER_THAN (2) 
 The digitizer triggers when the pulse width is greater than the value you specify with the IviDigitizer Glitch Arm Width property.

Default Value: IVIDIGITIZER_VAL_GLITCH_LESS_THAN (1)

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### Arm Level (1.0)

Specifies the arm level. This value sets the IviDigitizer Arm Level property.

Unit: volt

Default Value: 1.0

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### Arm Source ("")

Specifies the arm source. This value sets the arm source property.

Users who want to achieve interchangeability should use a virtual arm source name. The virtual arm source name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical arm source name.

Default Value: ""

Note:

You can specify the trace name as a string variable or as a literal enclosed in double quotes.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

Parent topic:

IVI Digitizer Arm Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividigitizer-configure-pretrigger-samples.html language=enus -->
## TOPIC 00018: IviDigitizer Configure Pretrigger Samples [PS]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividigitizer-configure-pretrigger-samples.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividigitizer-configure-pretrigger-samples.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pretrigger samples of the digitizer. This node is part of the IviDigitizerPretriggerSamples [PS] extension group. Pretrigger Samples (1) Specifies the pretrigger samples. This value sets the IviDigitizer Pretrigger Samples property. Default Value: 1 instrument handle out The instrumen

IviDigitizer Configure Pretrigger Samples [PS]

Configures the pretrigger samples of the digitizer.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### Pretrigger Samples (1)

Specifies the pretrigger samples. This value sets the IviDigitizer Pretrigger Samples property.

Default Value: 1

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

Parent topic:

IVI Digitizer Trigger Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividigitizer-configure-reference-oscillator-output-enabled.html language=enus -->
## TOPIC 00019: IviDigitizer Configure Reference Oscillator Output Enabled [RO]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividigitizer-configure-reference-oscillator-output-enabled.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividigitizer-configure-reference-oscillator-output-enabled.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether or not the reference frequency signal appears at an output of the digitizer. This node is part of the IviDigitizerReferenceOscillator [RO] extension group. Output Enabled (Off) Specifies whether or not the reference frequency signal appears at a reference output of the digitizer.

IviDigitizer Configure Reference Oscillator Output Enabled [RO]

Configures whether or not the reference frequency signal appears at an output of the digitizer.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### Output Enabled (Off)

Specifies whether or not the reference frequency signal appears at a reference output of the digitizer. This value sets the IviDigitizer Reference Oscillator Output Enabled property.

Valid Values:
TRUE - Enable Reference Oscillator Output
FALSE - Disable Reference Oscillator Output

Default Value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

Parent topic:

IVI Digitizer Reference Oscillator Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividigitizer-configure-reference-oscillator.html language=enus -->
## TOPIC 00020: IviDigitizer Configure Reference Oscillator [RO]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividigitizer-configure-reference-oscillator.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividigitizer-configure-reference-oscillator.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference oscillator of the digitizer. This node is part of the IviDigitizerReferenceOscillator [RO] extension group. Oscillator Frequency (1.0e6) Specifies the frequency of the external reference oscillator. This input is used only if the Oscillator SourceOscillator Source input is s

IviDigitizer Configure Reference Oscillator [RO]

Configures the reference oscillator of the digitizer.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### Oscillator Frequency (1.0e6)

Specifies the frequency of the external reference oscillator. This input is used only if the Oscillator SourceOscillator Source input is set to External. The driver uses this value to set the IviDigitizer Reference Oscillator External Frequency property.

Unit: Hertz

Default Value: 1.0e6

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### Oscillator Source (Internal)

Specifies the source of the reference frequency signal. The driver uses this value to set the IviDigitizer Reference Oscillator Source property.

Valid Values:

- IVIDIGITIZER_VAL_REFERENCE_OSCILLATOR_SOURCE_INTERNAL (0) 
 The internal reference oscillator is used.

- IVIDIGITIZER_VAL_REFERENCE_OSCILLATOR_SOURCE_EXTERNAL (1) 
 An external reference oscillator is used.

IVIDIGITIZER_VAL_REFERENCE_OSCILLATOR_SOURCE_PXI_CLK10 (2)
 The PXI/PXIe backplane 10 MHz reference. 

IVIDIGITIZER_VAL_REFERENCE_OSCILLATOR_SOURCE_PXIE_CLK100 (3)
 The PXIe backplane 100 MHz reference.

Default Value: IVIDIGITIZER_VAL_REFERENCE_OSCILLATOR_SOURCE_INTERNAL (0)

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

Parent topic:

IVI Digitizer Reference Oscillator Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividigitizer-fetch-multi-record-waveform-int8.html language=enus -->
## TOPIC 00021: IviDigitizer Fetch Multi Record Waveform Int8 [MRA]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividigitizer-fetch-multi-record-waveform-int8.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividigitizer-fetch-multi-record-waveform-int8.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the (multi-record) waveform the digitizer acquired for the specified channel. The waveform is from a previously initiated acquisition.The acquired waveform records can be retrieved all together, or in chunks. You specify the first record and the number of consecutive records to fetch. Note t

IviDigitizer Fetch Multi Record Waveform Int8 [MRA]

Returns the (multi-record) waveform the digitizer acquired for the specified channel. The waveform is from a previously initiated acquisition.The acquired waveform records can be retrieved all together, or in chunks. You specify the first record and the number of consecutive records to fetch. Note that the record number is zero-based, and reset when you initiate a new acquisition, i.e. record 0 is the first record of the last acquisition. The Actual Records output indicates how many of the requested records have actually completed successfully. The Actual Points, First Valid Point, Initial X Offset, Initial X Time Seconds and Initial X Time Fraction ouputs have a value for each record, and therefore are arrays of size NumRecords. However, if the value of ActualRecords is smaller than the requested number of records, these arrays shall have only their first ActualRecords elements valid. If a NULL pointer is passed in for any of these parameters, the driver ignores it.

The value of First Valid Point is relative to the start of the waveform array, such that:

Sample i of record R = WaveformArray[FirstValidPoint[R]+i]

Note

You must use the IviDigitizer Initiate Acquisition node to start a multi-record (Num Record > 1) acquisition on the channels that the end-user configures with the IviDigitizer Configure Channel node. The digitizer acquires waveforms on the concurrently enabled channels. If the channel is not enabled for the acquisition, this node returns the channel not enabled error.

Note

You can use the IviDigitizer Acquisition Status node to determine when the acquisition is complete. You must call theIviDigitizer Fetch Multi Record Waveform Int8 node separately for each enabled channel to obtain the waveforms. Alternatively, you can use the IviDigitizer Wait For Acquisition Complete node to block the calling program until the acquisition is finished.

Note

Note

Note

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Initial X Offset

The time in relation to the Trigger Event of the first point in the waveform in seconds. Negative values mean that the first point in the waveform array was acquired before the trigger event.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Initial X Time Seconds

Specifies the seconds portion of the absolute time at which the first data point was acquired. Note that the actual time is the sum of Initial X Time SecondsInitial X Time Seconds and Initial X Time FractionInitial X Time Fractionn. The time is specified as the sum of two values because a single double-precision floating-point number does not have sufficient range and resolution to specify the time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Initial X Time Fraction

Specifies the fractional portion of the absolute time at which the first data point was acquired. Note that the actual time is the sum of Initial X Time SecondsInitial X Time Seconds and Initial X Time FractionInitial X Time Fraction. The time is specified as the sum of two values because a single double-precision floating-point number does not have sufficient range and resolution to specify the time.

[IMAGE alt='datatype_icon' src='/assets/img/i1di32.png']

##### Waveform Array

Buffer into which the acquired waveform is stored. 

Notes:
This array is always user allocated, and it must contain at least as many elements as the value you specify with theWaveform Array SizeWaveform Array Size parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ii64.png']

##### Actual Records

Indicates how many records in the acquisition completed successfully.

[IMAGE alt='datatype_icon' src='/assets/img/i1di64.png']

##### Actual Points

Indicates how many data points were actually retrieved from the instrument for each completed record. This is an array of size at least 
Num of RecordsNum of Records or a NULL pointer. For IVI-C, this array is always user allocated.

[IMAGE alt='datatype_icon' src='/assets/img/i1di64.png']

##### First Valid Point

Indicates the index of the first valid data point in the output Data array for each completed record. This value will often be zero. However, some digitizer hardware designs transfer data most efficiently when the data is aligned with specific memory address boundaries. In those cases, the hardware may return a few invalid data points at the beginning of a record. This eliminates the need to shift the data during the transfer, ensuring maximum data transfer rates. This is an array of size at least 
Num of RecordsNum of Records or a NULL pointer. For IVI-C, this array is always user allocated.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### X Increment

The time between points in the acquired waveform in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Scale Factor

Scaling factor for the waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Scale Offset

Scaling offset for the waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### Num of Points Per Record (256)

Specifies the number of data points to return.

This number may be larger than the amount of data available. Use the Actual PointsActual Points output to determine how many data points were returned.

Default Value: 256

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### Offset Within Record (0)

Specifies the start index within the record from which the data should be retrieved.

While normally zero, this parameter allows users to retrieve partial records using non-zero values. Data that comes before the Offset Within RecordOffset Within Record index will not be retrieved. This is perhaps most useful when retrieving very large data records because it allows records to be retrieved in several smaller chunks.

Default Value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### Num of Records (256)

Specifies the number of consecutive records to read.

If Num of RecordsNum of Records is greater than 1, this input allows full or partial (if Offset Within RecordOffset Within Record and Num of Points Per RecordNum of Points Per Record are specified accordingly) data to be retrieved from multiple digitizer records in a single Fetch call. If Num of RecordsNum of Records is less than or equal to zero, an error will be returned.

Default Value: 256

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### First Record (0)

Specifies the number of the first record to read.

Default Value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### Channel Name ("")

Specifies the name of the channel from which to retrieve the data.

Users who want to achieve interchangeability should use a virtual channel name. The virtual channel name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical channel name.

Default Value: ""

Note:

You can specify the trace name as a string variable or as a literal enclosed in double quotes.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### Waveform Array Size (256)

Specifies the allocated size of the WaveformArray buffer, in number of data points.

If this value is smaller than the total number of points to be retrieved, the driver will fill the waveform buffer as fully as possible and return the actual number of points retrieved in the Actual PointsActual Points parameter.

Default Value: 256

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

Parent topic:

IVI Digitizer Multi-Record Acquisition Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividigitizer-fetch-multi-record-waveform-real64.html language=enus -->
## TOPIC 00022: IviDigitizer Fetch Multi Record Waveform Real64 [MRA]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividigitizer-fetch-multi-record-waveform-real64.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividigitizer-fetch-multi-record-waveform-real64.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the (multi-record) waveform the digitizer acquired for the specified channel. The waveform is from a previously initiated acquisition.The acquired waveform records can be retrieved all together, or in chunks. You specify the first record and the number of consecutive records to fetch. Note t

IviDigitizer Fetch Multi Record Waveform Real64 [MRA]

Returns the (multi-record) waveform the digitizer acquired for the specified channel. The waveform is from a previously initiated acquisition.The acquired waveform records can be retrieved all together, or in chunks. You specify the first record and the number of consecutive records to fetch. Note that the record number is zero-based, and reset when you initiate a new acquisition, i.e. record 0 is the first record of the last acquisition. The Actual Records output indicates how many of the requested records have actually completed successfully. The Actual Points, First Valid Point, Initial X Offset, Initial X Time Seconds and Initial X Time Fraction ouputs have a value for each record, and therefore are arrays of size NumRecords. However, if the value of ActualRecords is smaller than the requested number of records, these arrays shall have only their first ActualRecords elements valid. If a NULL pointer is passed in for any of these parameters, the driver ignores it.

The value of First Valid Point is relative to the start of the waveform array, such that:

Sample i of record R = WaveformArray[FirstValidPoint[R]+i]

Note

You must use the IviDigitizer Initiate Acquisition node to start a multi-record (Num Record > 1) acquisition on the channels that the end-user configures with the IviDigitizer Configure Channel node. The digitizer acquires waveforms on the concurrently enabled channels. If the channel is not enabled for the acquisition, this node returns the channel not enabled error.

Note

Note

Note

Note

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Initial X Offset

The time in relation to the Trigger Event of the first point in the waveform in seconds. Negative values mean that the first point in the waveform array was acquired before the trigger event.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Initial X Time Seconds

Specifies the seconds portion of the absolute time at which the first data point was acquired. Note that the actual time is the sum of Initial X Time SecondsInitial X Time Seconds and Initial X Time FractionInitial X Time Fractionn. The time is specified as the sum of two values because a single double-precision floating-point number does not have sufficient range and resolution to specify the time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Initial X Time Fraction

Specifies the fractional portion of the absolute time at which the first data point was acquired. Note that the actual time is the sum of Initial X Time SecondsInitial X Time Seconds and Initial X Time FractionInitial X Time Fraction. The time is specified as the sum of two values because a single double-precision floating-point number does not have sufficient range and resolution to specify the time.

[IMAGE alt='datatype_icon' src='/assets/img/i1di32.png']

##### Waveform Array

Buffer into which the acquired waveform is stored. 

Notes:
This array is always user allocated, and it must contain at least as many elements as the value you specify with theWaveform Array SizeWaveform Array Size parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ii64.png']

##### Actual Records

Indicates how many records in the acquisition completed successfully.

[IMAGE alt='datatype_icon' src='/assets/img/i1di64.png']

##### Actual Points

Indicates how many data points were actually retrieved from the instrument for each completed record. This is an array of size at least 
Num of RecordsNum of Records or a NULL pointer. For IVI-C, this array is always user allocated.

[IMAGE alt='datatype_icon' src='/assets/img/i1di64.png']

##### First Valid Point

Indicates the index of the first valid data point in the output Data array for each completed record. This value will often be zero. However, some digitizer hardware designs transfer data most efficiently when the data is aligned with specific memory address boundaries. In those cases, the hardware may return a few invalid data points at the beginning of a record. This eliminates the need to shift the data during the transfer, ensuring maximum data transfer rates. This is an array of size at least 
Num of RecordsNum of Records or a NULL pointer. For IVI-C, this array is always user allocated.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### X Increment

The time between points in the acquired waveform in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### Num of Points Per Record (256)

Specifies the number of data points to return.

This number may be larger than the amount of data available. Use the Actual PointsActual Points output to determine how many data points were returned.

Default Value: 256

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### Offset Within Record (0)

Specifies the start index within the record from which the data should be retrieved.

While normally zero, this parameter allows users to retrieve partial records using non-zero values. Data that comes before the Offset Within RecordOffset Within Record index will not be retrieved. This is perhaps most useful when retrieving very large data records because it allows records to be retrieved in several smaller chunks.

Default Value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### Num of Records (256)

Specifies the number of consecutive records to read.

If Num of RecordsNum of Records is greater than 1, this input allows full or partial (if Offset Within RecordOffset Within Record and Num of Points Per RecordNum of Points Per Record are specified accordingly) data to be retrieved from multiple digitizer records in a single Fetch call. If Num of RecordsNum of Records is less than or equal to zero, an error will be returned.

Default Value: 256

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### First Record (0)

Specifies the number of the first record to read.

Default Value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### Channel Name ("")

Specifies the name of the channel from which to retrieve the data.

Users who want to achieve interchangeability should use a virtual channel name. The virtual channel name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical channel name.

Default Value: ""

Note:

You can specify the trace name as a string variable or as a literal enclosed in double quotes.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### Waveform Array Size (256)

Specifies the allocated size of the WaveformArray buffer, in number of data points.

If this value is smaller than the total number of points to be retrieved, the driver will fill the waveform buffer as fully as possible and return the actual number of points retrieved in the Actual PointsActual Points parameter.

Default Value: 256

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

Parent topic:

IVI Digitizer Multi-Record Acquisition Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividigitizer-fetch-waveform-int16.html language=enus -->
## TOPIC 00023: IviDigitizer Fetch Waveform Int16

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividigitizer-fetch-waveform-int16.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividigitizer-fetch-waveform-int16.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI returns the waveform the digitizer acquired for the specified channel. The waveform is from a previously initiated acquisition. Notes: (1) You use the IviDigitizer Initiate Acquisition Node to start an acquisition on the channels that the end-user configures with the IviDigitizer Configure C

IviDigitizer Fetch Waveform Int16

This VI returns the waveform the digitizer acquired for the specified channel. The waveform is from a previously initiated acquisition. Notes: (1) You use the IviDigitizer Initiate Acquisition Node to start an acquisition on the channels that the end-user configures with the IviDigitizer Configure Channel Node. The digitizer acquires waveforms on the concurrently enabled channels. If the channel is not enabled for the acquisition, this node returns the Channel Not Enabled error. (2) You can use the IviDigitizer Acquisition Status Node to determine when the acquisition is complete. You must call the IviDigitizer Fetch Waveform Int16 Node separately for each enabled channel to obtain the waveforms. Alternatively, you can use the IviDigitizer Wait For Acquisition Complete Node to block the calling program until the acquisition is finished. (3) You can call the IviDigitizer Read Waveform Int16 Node instead of the IviDigitizer Initiate Acquisition Node. The IviDigitizer Read Waveform Int16 Node starts an acquisition on all enabled channels, waits for the acquisition to complete, and returns the waveform (as well as various waveform parameters) for the specified channel. You call this node to obtain the waveforms for each of the remaining channels. (4) After this node executes, each element in the Waveform Array parameter is an unscaled value directly from the digitizer's analog-to-digital converter (ADC). (5) This node does not check the instrument status. Typically, the end-user calls this node only in a sequence of calls to other low-level driver VIs. The sequence performs one operation. The end-user uses the low-level nodes to optimize one or more aspects of interaction with the instrument. Call the IviDigitizer Error Query Node at the conclusion of the sequence to check the instrument status. (6) The data type of the returned waveform array is ViInt16.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Initial X Time Seconds

Specifies the seconds portion of the absolute time at which the first data point was acquired. Note that the actual time is the sum of Initial X Time SecondsInitial X Time Seconds and Initial X Time FractionInitial X Time Fraction. The time is specified as the sum of two values because a single double-precision floating-point number does not have sufficient range and resolution to specify the time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Initial X Offset

The time in relation to the Trigger Event of the first point in the waveform in seconds. Negative values mean that the first point in the waveform array was acquired before the trigger event.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Initial X Time Fraction

Specifies the fractional portion of the absolute time at which the first data point was acquired. Note that the actual time is the sum of Initial X Time SecondsInitial X Time Seconds and Initial X Time FractionInitial X Time Fraction. The time is specified as the sum of two values because a single double-precision floating-point number does not have sufficient range and resolution to specify the time.

[IMAGE alt='datatype_icon' src='/assets/img/i1di16.png']

##### Waveform Array

Buffer into which the acquired waveform is stored. 

Notes:
This array is always user allocated, and it must contain at least as many elements as the value you specify with the Number of Points parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ii64.png']

##### Actual Points

Indicates how many data points were actually retrieved from the instrument.

[IMAGE alt='datatype_icon' src='/assets/img/ii64.png']

##### First Valid Point

Indicates the index of the first valid data point in the output Data array. This value will often be zero. However, some digitizer hardware designs transfer data most efficiently when the data is aligned with specific memory address boundaries. In those cases, the hardware may return a few invalid data points at the beginning of a record. This eliminates the need to shift the data during the transfer, ensuring maximum data transfer rates.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### X Increment

The time between points in the acquired waveform in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Scale Offset

Scaling offset for the waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Scale Factor

Scaling factor for the waveform data.

[IMAGE alt='datatype_icon' src='/assets/img/ci64.png']

##### Waveform Array Size (256)

Specifies the allocated size of the WaveformArray buffer, in number of data points.

If this value is smaller than the total number of points to be retrieved, the driver will fill the waveform buffer as fully as possible and return the actual number of points retrieved in the Actual PointsActual Points parameter.

Default Value: 256

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### Channel Name ("")

Specifies the name of the channel from which to retrieve the data.

Users who want to achieve interchangeability should use a virtual channel name. The virtual channel name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical channel name.

Default Value: ""

Note:

You can specify the trace name as a string variable or as a literal enclosed in double quotes.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

Parent topic:

IVI Digitizer Low Level Acquisition Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividigitizer-get-arm-source-name.html language=enus -->
## TOPIC 00024: IviDigitizer Get Arm Source Name [ARM]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividigitizer-get-arm-source-name.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividigitizer-get-arm-source-name.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the physical channel identifier that corresponds to the one-based index that the user specifies. If the driver defines a qualified arm source name, this node returns the qualified name. If the value that the user passes for the Source Index parameter is less than one or greater than the valu

IviDigitizer Get Arm Source Name [ARM]

Returns the physical channel identifier that corresponds to the one-based index that the user specifies.

Note

Note

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### Source Name

Returns the arm source name that corresponds to the Index.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### Source Index (1)

A one-based index that defines which name to return.

Default Value: 1

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

Parent topic:

IVI Digitizer Arm Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividigitizer-is-measuring.html language=enus -->
## TOPIC 00025: IviDigitizer Is Measuring

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividigitizer-is-measuring.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividigitizer-is-measuring.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines if the digitizer is currently in the Measuring state. Status Returns whether the digitizer is currently in the Measuring state. If the driver cannot query the instrument to determine its state, the driver returns the value Unknown. Possible Values: - IVIDIGITIZER_VAL_ACQUISITION_STATUS_RE

IviDigitizer Is Measuring

Determines if the digitizer is currently in the Measuring state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Status

Returns whether the digitizer is currently in the Measuring state. If the driver cannot query the instrument to determine its state, the driver returns the value Unknown.

Possible Values:

- IVIDIGITIZER_VAL_ACQUISITION_STATUS_RESULT_TRUE (1) 
 The digitizer is currently in the Measuring state.

- IVIDIGITIZER_VAL_ACQUISITION_STATUS_RESULT_FALSE (2) 
 The digitizer is not currently in the Measuring state.

- IVIDIGITIZER_VAL_ACQUISITION_STATUS_RESULT_UNKNOWN (3) 
 The driver cannot query the instrument to determine if the digitizer is in the Measuring state.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

Parent topic:

IVI Digitizer Low Level Acquisition Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividigitizer-is-waiting-for-arm.html language=enus -->
## TOPIC 00026: IviDigitizer Is Waiting For Arm

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividigitizer-is-waiting-for-arm.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividigitizer-is-waiting-for-arm.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines if the digitizer is currently in the Waiting For Arm state. Status Returns whether the digitizer is currently in the Waiting For Arm state. If the driver cannot query the instrument to determine its state, the driver returns the value Unknown. Possible Values: - IVIDIGITIZER_VAL_ACQUISITI

IviDigitizer Is Waiting For Arm

Determines if the digitizer is currently in the Waiting For Arm state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Status

Returns whether the digitizer is currently in the Waiting For Arm state. If the driver cannot query the instrument to determine its state, the driver returns the value Unknown.

Possible Values:

- IVIDIGITIZER_VAL_ACQUISITION_STATUS_RESULT_TRUE (1) 
 The digitizer is currently in the Waiting For Arm state.

- IVIDIGITIZER_VAL_ACQUISITION_STATUS_RESULT_FALSE (2) 
 The digitizer is not currently in the Waiting For Arm state.

- IVIDIGITIZER_VAL_ACQUISITION_STATUS_RESULT_UNKNOWN (3) 
 The driver cannot query the instrument to determine if the digitizer is in the Waiting For Arm state.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

Parent topic:

IVI Digitizer Low Level Acquisition Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividigitizer-is-waiting-for-trigger.html language=enus -->
## TOPIC 00027: IviDigitizer Is Waiting For Trigger

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividigitizer-is-waiting-for-trigger.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividigitizer-is-waiting-for-trigger.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines if the digitizer is currently in the Waiting For Trigger state. instrument handle out The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session. Default value: None Status

IviDigitizer Is Waiting For Trigger

Determines if the digitizer is currently in the Waiting For Trigger state.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Status

Returns whether the digitizer is currently in the Waiting For Trigger state. If the driver cannot query the instrument to determine its state, the driver returns the value Unknown.

Possible Values:

- IVIDIGITIZER_VAL_ACQUISITION_STATUS_RESULT_TRUE (1) 
 The digitizer is currently in the Waiting For Trigger state.

- IVIDIGITIZER_VAL_ACQUISITION_STATUS_RESULT_FALSE (2) 
 The digitizer is not currently in the Waiting For Trigger state.

- IVIDIGITIZER_VAL_ACQUISITION_STATUS_RESULT_UNKNOWN (3) 
 The driver cannot query the instrument to determine if the digitizer is in the Waiting For Trigger state.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDigitizer Initialize Node or IviDigitizer Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

Parent topic:

IVI Digitizer Low Level Acquisition Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividigitizer-low-level-acquisition.html language=enus -->
## TOPIC 00028: IVI Digitizer Low Level Acquisition Nodes

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividigitizer-low-level-acquisition.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividigitizer-low-level-acquisition.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Digitizer Low Level Acquisition Nodes

IVI Digitizer Waveform Acquisition Nodes

IviDigitizer Abort

Aborts an acquisition and returns the digitizer to the Idle state. Note: This node does not check the instrument status. Typically, you call this node only in a sequence of calls to other low-level driver nodes. The sequence performs one operation. Use the low-level nodes to optimize one or more aspects of interaction with the instrument. If you want to check the instrument status, call the IviDigitizer Error-Query Node at the conclusion of the sequence.

IviDigitizer Fetch Waveform Int16

This VI returns the waveform the digitizer acquired for the specified channel. The waveform is from a previously initiated acquisition. Notes: (1) You use the IviDigitizer Initiate Acquisition Node to start an acquisition on the channels that the end-user configures with the IviDigitizer Configure Channel Node. The digitizer acquires waveforms on the concurrently enabled channels. If the channel is not enabled for the acquisition, this node returns the Channel Not Enabled error. (2) You can use the IviDigitizer Acquisition Status Node to determine when the acquisition is complete. You must call the IviDigitizer Fetch Waveform Int16 Node separately for each enabled channel to obtain the waveforms. Alternatively, you can use the IviDigitizer Wait For Acquisition Complete Node to block the calling program until the acquisition is finished. (3) You can call the IviDigitizer Read Waveform Int16 Node instead of the IviDigitizer Initiate Acquisition Node. The IviDigitizer Read Waveform Int16 Node starts an acquisition on all enabled channels, waits for the acquisition to complete, and returns the waveform (as well as various waveform parameters) for the specified channel. You call this node to obtain the waveforms for each of the remaining channels. (4) After this node executes, each element in the Waveform Array parameter is an unscaled value directly from the digitizer's analog-to-digital converter (ADC). (5) This node does not check the instrument status. Typically, the end-user calls this node only in a sequence of calls to other low-level driver VIs. The sequence performs one operation. The end-user uses the low-level nodes to optimize one or more aspects of interaction with the instrument. Call the IviDigitizer Error Query Node at the conclusion of the sequence to check the instrument status. (6) The data type of the returned waveform array is ViInt16.

IviDigitizer Fetch Waveform Int32

This node returns the waveform the digitizer acquired for the specified channel. The waveform is from a previously initiated acquisition. Notes: (1) You use the IviDigitizer Initiate Acquisition Node to start an acquisition on the channels that the end-user configures with the IviDigitizer Configure Channel Node. The digitizer acquires waveforms on the concurrently enabled channels. If the channel is not enabled for the acquisition, this node returns the Channel Not Enabled error. (2) You can use the IviDigitizer Acquisition Status Node to determine when the acquisition is complete. You must call the IviDigitizer Fetch Waveform Int32 Node separately for each enabled channel to obtain the waveforms. Alternatively, you can use the IviDigitizer Wait For Acquisition Complete Node to block the calling program until the acquisition is finished. (3) You can call the IviDigitizer Read Waveform Int32 Node instead of the IviDigitizer Initiate Acquisition Node. The IviDigitizer Read Waveform Int32 Node starts an acquisition on all enabled channels, waits for the acquisition to complete, and returns the waveform (as well as various waveform parameters) for the specified channel. You call this node to obtain the waveforms for each of the remaining channels. (4) After this node executes, each element in the Waveform Array parameter is an unscaled value directly from the digitizer's analog-to-digital converter (ADC). (5) This node does not check the instrument status. Typically, the end-user calls this node only in a sequence of calls to other low-level driver nodes. The sequence performs one operation. The end-user uses the low-level nodes to optimize one or more aspects of interaction with the instrument. Call the IviDigitizer Error Query Node at the conclusion of the sequence to check the instrument status. (6) The data type of the returned waveform array is ViInt32.

IviDigitizer Fetch Waveform Int8

Returns the waveform the digitizer acquired for the specified channel. The waveform is from a previously initiated acquisition. Notes: (1) You use the IviDigitizer Initiate Acquisition Node to start an acquisition on the channels that the end-user configures with the IviDigitizer Configure Channel Node. The digitizer acquires waveforms on the concurrently enabled channels. If the channel is not enabled for the acquisition, this node returns the Channel Not Enabled error. (2) You can use the IviDigitizer Acquisition Status Node to determine when the acquisition is complete. You must call the IviDigitizer Fetch Waveform Int8 Node separately for each enabled channel to obtain the waveforms. Alternatively, you can use the IviDigitizer Wait For Acquisition Complete Node to block the calling program until the acquisition is finished. (3) You can call the IviDigitizer Read Waveform Int8 Node instead of the IviDigitizer Initiate Acquisition Node. The IviDigitizer Read Waveform Int8 Node starts an acquisition on all enabled channels, waits for the acquisition to complete, and returns the waveform (as well as various waveform parameters) for the specified channel. You call this node to obtain the waveforms for each of the remaining channels. (4) After this node executes, each element in the Waveform Array parameter is an unscaled value directly from the digitizer's analog-to-digital converter (ADC). (5) This node does not check the instrument status. Typically, the end-user calls this node only in a sequence of calls to other low-level driver nodes. The sequence performs one operation. The end-user uses the low-level nodes to optimize one or more aspects of interaction with the instrument. Call the IviDigitizer Error Query Node at the conclusion of the sequence to check the instrument status. (6) The data type of the returned waveform array is ViInt8.

IviDigitizer Fetch Waveform Real64

This node returns the waveform the digitizer acquired for the specified channel. The waveform is from a previously initiated acquisition. Notes: (1) You use the IviDigitizer Initiate Acquisition Node to start an acquisition on the channels that the end-user configures with the IviDigitizer Configure Channel Node. The digitizer acquires waveforms on the concurrently enabled channels. If the channel is not enabled for the acquisition, this node returns the Channel Not Enabled error. (2) You can use the IviDigitizer Acquisition Status Node to determine when the acquisition is complete. You must call the IviDigitizer Fetch Waveform Real64 Node separately for each enabled channel to obtain the waveforms. Alternatively, you can use the IviDigitizer Wait For Acquisition Complete Node to block the calling program until the acquisition is finished. (3) You can call the IviDigitizer Read Waveform Real64 Node instead of the IviDigitizer Initiate Acquisition Node. The IviDigitizer Read Waveform Real64 Node starts an acquisition on all enabled channels, waits for the acquisition to complete, and returns the waveform (as well as various waveform parameters) for the specified channel. You call this node to obtain the waveforms for each of the remaining channels. (4) After completion each element in the Waveform Array parameter is the actual sampled voltage in Volts. (5) This node does not check the instrument status. Typically, the end-user calls this node only in a sequence of calls to other low-level driver nodes. The sequence performs one operation. The end-user uses the low-level nodes to optimize one or more aspects of interaction with the instrument. Call the IviDigitizer Error Query Node at the conclusion of the sequence to check the instrument status. (6) The data type of the returned waveform array is ViReal64.

IviDigitizer Initiate Acquisition

Initiates a waveform acquisition. After calling this node, the digitizer leaves the idle state and waits for a trigger. The digitizer acquires a waveform for each channel the end-user has enabled with the IviDigitizer Configure Channel Node. Notes: This node does not check the instrument status. Typically, the end-user calls this node only in a sequence of calls to other low-level driver nodes. The sequence performs one operation. The end-user uses the low-level nodes to optimize one or more aspects of interaction with the instrument. Call the IviDigitizer Error Query Node at the conclusion of the sequence to check the instrument status.

IviDigitizer Is Idle

Determines if the digitizer is currently in the Idle state.

IviDigitizer Is Measuring

Determines if the digitizer is currently in the Measuring state.

IviDigitizer Is Waiting For Arm

Determines if the digitizer is currently in the Waiting For Arm state.

IviDigitizer Is Waiting For Trigger

Determines if the digitizer is currently in the Waiting For Trigger state.

IviDigitizer Query Min Waveform Memory

Determines the minimum amount of memory that is needed to fetch or read data from the digitizer with maximum performance. The returned value includes the memory needed to handle DMA alignment issues and any internal memory that is used by the digitizer hardware or the driver. The parameters to this node are similar to the parameters used in Read and Fetch VIs. Users should call this node before allocating data buffer memory, and then call a Read or Fetch Node with the same parameter values. Notes: This node will return a value that can be used to allocate the optimally-sized memory buffer for Read and Fetch calls with the same passed parameters. If the Read and Fetch calls specify fewer data points, the data buffer will still be large enough and no performance penalty will be realized (aside from wasted memory space). If the Read and Fetch calls specify more data points they will simply fill the allocated memory buffer as fully as possible. Subsequent Fetch calls can then be made to retrieve the remaining data.

IviDigitizer Wait For Acquisition Complete

Maximum Time

IviDigitizer Send Software Arm [SA]

This node sends a software-generated arm to the instrument. It is only applicable for instruments using interfaces or protocols which support an explicit arm function.

IviDigitizer Send Software Trigger [ST]

Sends a software-generated trigger to the instrument.

Parent topic:

IVI Digitizer Waveform Acquisition Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividmm-is-over-range.html language=enus -->
## TOPIC 00029: IviDmm Is Over-Range

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividmm-is-over-range.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividmm-is-over-range.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Takes a measurement value that you obtain from either the Read or Fetch nodes and determines if the value is a valid measurement value or a value indicating that an over-range condition occurred. Notes: (1) If an over-range condition occurs, the measurement value contains an IEEE defined NaN (Not a

IviDmm Is Over-Range

Takes a measurement value that you obtain from either the Read or Fetch nodes and determines if the value is a valid measurement value or a value indicating that an over-range condition occurred.
 Notes: (1) If an over-range condition occurs, the measurement value contains an IEEE defined NaN (Not a Number) value indicating that an over-range condition occurred. (2) This node does not check the instrument status.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDmm Initialize Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### measurement value

Pass the measurement value that you obtain from either the Read or Fetch VIs. The driver tests this value to determine if the value is a valid measurement value or a value indicating that an over-range condition occurred. 

Default Value: 0.0

Notes:

(1) If an over-range condition occurs, the measurement value contains an IEEE defined NaN (Not a Number) value indicating that an over-range occurred.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDmm Initialize Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### is over-range

Returns whether the measured value is a valid measurement or a value indicating that an over-range condition occurred.

Return Values:
True - The value indicates an over-range condition occurred.
False - The value is a valid measurement.

Notes:

(1) If an over-range condition occurs, the measurement value contains an IEEE defined NaN (Not a Number) value indicating that an over-range occurred.

Parent topic:

IVI Digital Multimeter Low-Level Measurement

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividmm-low-level-measurement.html language=enus -->
## TOPIC 00030: IVI Digital Multimeter Low-Level Measurement

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividmm-low-level-measurement.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividmm-low-level-measurement.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Digital Multimeter Low-Level Measurement

IVI Digital Multimeter

IviDmm Initiate

Initiates a measurement.

IviDmm Send Software Trigger [SWT]

Sends a command to trigger the DMM. Call this node if you pass IVIDMM_VAL_SOFTWARE_TRIG for the Trigger Source parameter of the Configure Trigger Node or the Sample Trigger parameter of the Configure Multi-Point [MP] Node.

IviDmm Fetch

Returns the value from a previously initiated measurement.

IviDmm Fetch Multi-Point [MP]

Returns an array of values from a previously initiated multi-point measurement. The number of measurements the DMM takes is determined by the values you specify for the Trigger Count and Sample Count parameters of the IviDmm Configure Multi-Point [MP] Node.

IviDmm Abort

Aborts a previously initiated measurement and returns the DMM to the Idle state.

IviDmm Is Over-Range

Takes a measurement value that you obtain from either the Read or Fetch nodes and determines if the value is a valid measurement value or a value indicating that an over-range condition occurred.

Parent topic:

IVI Digital Multimeter

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividmm-measurement.html language=enus -->
## TOPIC 00031: IVI Digital Multimeter

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividmm-measurement.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividmm-measurement.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Digital Multimeter

IVI Dmm

IviDmm Read

Initiates a measurement, waits until the DMM has returned to the Idle state, and returns the measured value.

IviDmm Read Multi-Point [MP]

Initiates the measurement, waits for the DMM to return to the Idle state, and returns an array of measured values.

IVI Digital Multimeter Low-Level Measurement

Parent topic:

IVI Dmm

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividmm-revision-query.html language=enus -->
## TOPIC 00032: IviDmm Revision Query

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividmm-revision-query.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividmm-revision-query.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision numbers of the instrument driver and instrument firmware. instrument handle The instrument handle that you obtain from the IviDmm Initialize Node. The handle identifies a particular instrument session. Default value: None error in Error conditions that occur before this node run

IviDmm Revision Query

Returns the revision numbers of the instrument driver and instrument firmware.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDmm Initialize Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDmm Initialize Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### instrument driver revision

Returns the instrument driver software revision numbers in the form of a string.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### firmware revision

Returns the instrument firmware revision numbers in the form of a string.

Parent topic:

IVI Digital Multimeter Utility

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividmm-specific-measurements.html language=enus -->
## TOPIC 00033: IVI Digital Multimeter Specific Measurements

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividmm-specific-measurements.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividmm-specific-measurements.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Digital Multimeter Specific Measurements

IVI Dmm

IviDmm Configure AC Bandwidth [AC]

Configures the AC minimum and maximum frequency for DMMs that take AC voltage or AC current measurements.

IviDmm Configure Frequency Voltage Range [FRQ]

Configures the frequency voltage range of the DMM for frequency and period measurements

IVI Digital Multimeter Temperature

Parent topic:

IVI Dmm

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividmm-temperature.html language=enus -->
## TOPIC 00034: IVI Digital Multimeter Temperature

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividmm-temperature.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividmm-temperature.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Digital Multimeter Temperature

IVI Digital Multimeter Specific Measurements

IviDmm Configure Transducer Type [TMP]

Passes the type of device used to measure the temperature.

IviDmm Configure Thermocouple [TC]

Configures the thermocouple type and the reference junction type of the thermocouple for DMMs that take temperature measurements using a thermocouple transducer type.

IviDmm Configure Fixed Ref Junction [TC]

Configures the fixed reference junction for a thermocouple with a fixed reference junction type.

IviDmm Configure RTD [RTD]

Configures the alpha and resistance parameters for a resistance temperature device.

IviDmm Configure Thermistor [THM]

Configures the resistance for a thermistor temperature measurement device.

Parent topic:

IVI Digital Multimeter Specific Measurements

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividmm-trigger.html language=enus -->
## TOPIC 00035: IVI Digital Multimeter Trigger

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividmm-trigger.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividmm-trigger.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Digital Multimeter Trigger

IVI Dmm

IviDmm Configure Trigger

Configures the common DMM trigger properties.

IviDmm Configure Trigger Slope [TS]

Configures the polarity of the external trigger source of the DMM.

Parent topic:

IVI Dmm

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividmm-utility.html language=enus -->
## TOPIC 00036: IVI Digital Multimeter Utility

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividmm-utility.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividmm-utility.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Digital Multimeter Utility

IVI Dmm

IviDmm Reset

Resets the instrument to a known state and sends initialization commands to the instrument.

IviDmm Reset With Defaults

Resets the instrument and applies initial user specified settings from the Logical Name which was used to initialize the session.

IviDmm Self-Test

Runs the instrument's self test routine and returns the test result(s).

IviDmm Revision Query

Returns the revision numbers of the instrument driver and instrument firmware.

IviDmm Invalidate All Attributes

Invalidates the cached values of all properties for the session.

IviDmm Disable

Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected.

IviDmm Error-Query

Reads an error code and a message from the instrument's error queue.

IviDmm Error Message

Converts a status code returned by an instrument driver into a user-readable string.

IviDmm Get Next Coercion Record

Obtains the coercion information associated with the IVI session. It retrieves and clears the oldest instance in which the specific driver coerced a value you specified to another value. If you set the IviDmm>>Inherent IVI Settings>>User Options>>Record Value Coercions property to TRUE, the specific driver keeps a list of all coercions it makes on ViInt32 or ViReal64 values you pass to instrument driver nodes. You use this node to retrieve information from that list. The node returns an empty string in the Coercion Record parameter if no coercion records remain for the session.

IVI Digital Multimeter Interchangeability Info

Get interchangeability information about your digital multimeter.

Parent topic:

IVI Dmm

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividownconverter-cnfg-preselector-enabled.html language=enus -->
## TOPIC 00037: IviDownconverter Configure Preselector Enabled [PS]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividownconverter-cnfg-preselector-enabled.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividownconverter-cnfg-preselector-enabled.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether or not to bypass the preselection filter for the active RF Input. instrument handle The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Node. The handle identifies a particular instrument session. Default value: No

IviDownconverter Configure Preselector Enabled [PS]

Configures whether or not to bypass the preselection filter for the active RF Input.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### preselector enabled (False)

Enable or disable bypassing the pre-selection filter for the active RF Input. The driver uses this value to set the IviDownconverter Preselector Enabled [PS] property. 
 
Default Value: FALSE

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Nodes. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Downconverter RF Input Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividownconverter-initialize-with-options.html language=enus -->
## TOPIC 00038: IviDownconverter Initialize With Options

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividownconverter-initialize-with-options.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividownconverter-initialize-with-options.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new IVI instrument driver and optionally sets the initial session properties state. Opens a session to the specified device using the interface and address you specify for the Resource Name parameter. Sends initialization commands to set the instrument to the state necessary for the operat

IviDownconverter Initialize With Options

Creates a new IVI instrument driver and optionally sets the initial session properties state.
 Opens a session to the specified device using the interface and address you specify for the Resource Name parameter. Sends initialization commands to set the instrument to the state necessary for the operation of the instrument driver. Returns an instrument handle that you use to identify the instrument in all subsequent instrument driver node calls.

Note

The IVI Foundation and its member companies make no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The IVI Foundation and its member companies shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Nodes. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### id query

Boolean value that specifies whether you want the instrument driver to perform an ID Query.

Default value: True

| True | Perform ID Query. The driver verifies that the instrument type you initialize is supported. |
| --- | --- |
| False | Skip ID Query. The node initializes the instrument without performing an ID query. |

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset device

Boolean value that specifies whether you want to reset the instrument during the initialization procedure.

Default value: true

| True | Reset Device |
| --- | --- |
| False | Don't Reset Device |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### logical name ("SampleDownconverter")

Pass the logical name that identifies the particular driver session to use. The driver session, in turn, identifies a specific driver and device and specifies the initial settings for the session.

Default value: "SampleDownconverter"

Note

##### IVI Configuration Utility

##### Using Your Program with a Different Instrument

If you want to use your program with a different physical instrument, change the configuration of the logical name to use the driver session for the new physical instrument. You can change the initial settings for the session by changing the configuration of the driver session.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### option string

String you can use to set the initial value of certain properties for the session.

| RangeCheck | TRUE |
| --- | --- |
| QueryInstrStatus | FALSE |
| Cache | TRUE |
| Simulate | FALSE |

| Name |
| --- |
| RangeCheck |
| QueryInstrStatus |
| Cache |
| Simulate |
| RecordCoercions |
| Spy |
| InterchangeCheck |
| DriverSetup |

##### Valid Values for ViBoolean Properties

| True | TRUE, 1, True |
| --- | --- |
| False | FALSE, 0, False |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

#### Optional Session Properties

IviDownconverter>>Inherent IVI Settings>>User Options>>Range Check

IviDownconverter>>Inherent IVI Settings>>User Options>>Query Instrument Status

IviDownconverter>>Inherent IVI Settings>>User Options>>Cache

IviDownconverter>>Inherent IVI Settings>>User Options>>Simulate

IviDownconverter>Inherent IVI Settings>>User Options>>Record Value Coercions

#### ID Query

#### Reset

If the Reset parameter is set to True, this node resets the instrument to a known state.

Parent topic:

IVI Downconverter Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividownconverter-initialize.html language=enus -->
## TOPIC 00039: IviDownconverter Initialize

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividownconverter-initialize.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividownconverter-initialize.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new IVI instrument driver session. Opens a session to the specific driver using the logical name of the IVI driver session. Sends initialization commands to set the instrument to the state necessary for the operation of the instrument driver. Returns an instrument handle that you use to id

IviDownconverter Initialize

Creates a new IVI instrument driver session. Opens a session to the specific driver using the logical name of the IVI driver session.
 Sends initialization commands to set the instrument to the state necessary for the operation of the instrument driver. Returns an instrument handle that you use to identify the instrument in all subsequent instrument driver node calls.

Note

Content from the IVI specifications reproduced with permission from the IVI Foundation.

The IVI Foundation and its member companies make no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The IVI Foundation and its member companies shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### reset device

Boolean value that specifies whether you want to reset the instrument during the initialization procedure.

Default value: true

| True | Reset Device |
| --- | --- |
| False | Don't Reset Device |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Nodes. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### id query

Boolean value that specifies whether you want the instrument driver to perform an ID Query.

Default value: True

| True | Perform ID Query. The driver verifies that the instrument type you initialize is supported. |
| --- | --- |
| False | Skip ID Query. The node initializes the instrument without performing an ID query. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### logical name ("SampleDownconverter")

Pass the logical name that identifies the particular driver session to use. The driver session, in turn, identifies a specific driver and device and specifies the initial settings for the session.

Default value: "SampleDownconverter"

Note

##### IVI Configuration Utility

##### Using Your Program with a Different Instrument

If you want to use your program with a different physical instrument, change the configuration of the logical name to use the driver session for the new physical instrument. You can change the initial settings for the session by changing the configuration of the driver session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Downconverter Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividownconverter-set-active-if-output.html language=enus -->
## TOPIC 00040: IviDownconverter Set Active IF Output

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividownconverter-set-active-if-output.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividownconverter-set-active-if-output.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects one of the available IF outputs, and makes it the active IF output. instrument handle The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Node. The handle identifies a particular instrument session. Default value: None error

IviDownconverter Set Active IF Output

Selects one of the available IF outputs, and makes it the active IF output.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### IF output name ("")

Pass the active IF output name. The driver uses this value to set the IviDownconverter Active IF Output property. 

Users who want to achieve interchangeability should use a virtual IF output name. The virtual IF output name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical IF output name.

Default Value: ""

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Nodes. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Downconverter IF Output Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividownconverter-set-active-rf-input.html language=enus -->
## TOPIC 00041: IviDownconverter Set Active RF Input

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividownconverter-set-active-rf-input.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividownconverter-set-active-rf-input.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects one of the available RF inputs, and makes it the active RF input. instrument handle The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Node. The handle identifies a particular instrument session. Default value: None error in

IviDownconverter Set Active RF Input

Selects one of the available RF inputs, and makes it the active RF input.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### RF input name ("")

Pass the active RF input name. The driver uses this value to set the IviDownconverter Active RF Input property. 

Users who want to achieve interchangeability should use a virtual RF input name. The virtual RF input name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical RF input name.

Default Value: ""

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Nodes. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Downconverter RF Input Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividownconverter-wait-freq-sweep-complete.html language=enus -->
## TOPIC 00042: IviDownconverter Wait Until Frequency Sweep Complete [FSW]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividownconverter-wait-freq-sweep-complete.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividownconverter-wait-freq-sweep-complete.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the frequency sweep is complete. If no frequency sweep is currently running, this node returns immediately. If the sweep does not complete within the maximum time designated, the node returns the Max Time Exceeded error. instrument handle The instrument handle that you obtain from the Iv

IviDownconverter Wait Until Frequency Sweep Complete [FSW]

Waits until the frequency sweep is complete. If no frequency sweep is currently running, this node returns immediately. If the sweep does not complete within the maximum time designated, the node returns the Max Time Exceeded error.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum time (5000 ms)

Pass the maximum length of time.

Defined Values:
IVIDOWNCONVERTER_VAL_MAX_TIME_IMMEDIATE (0)
IVIDOWNCONVERTER_VAL_MAX_TIME_INFINITE (-1)

Default Value: 5000 ms

Notes:

(1) The maximum timemaximum time parameter applies only to this VI. It has no effect on other timeout parameters or properties.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Nodes. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Downconverter Action Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ividownconverter-wait-until-settled.html language=enus -->
## TOPIC 00043: IviDownconverter Wait Until Settled

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ividownconverter-wait-until-settled.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ividownconverter-wait-until-settled.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until all of the signals flowing through the downconverter have settled. If the signals do not settle within the maximum time designated, the node returns the Max Time Exceeded error. instrument handle The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconvert

IviDownconverter Wait Until Settled

Waits until all of the signals flowing through the downconverter have settled. If the signals do not settle within the maximum time designated, the node returns the Max Time Exceeded error.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum time (5000 ms)

Pass the maximum length of time.

Defined Values:
IVIDOWNCONVERTER_VAL_MAX_TIME_IMMEDIATE (0)
IVIDOWNCONVERTER_VAL_MAX_TIME_INFINITE (-1)

Default Value: 5000 ms

Notes:

(1) The maximum timemaximum time parameter applies only to this VI. It has no effect on other timeout parameters or properties.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviDownconverter Initialize or IviDownconverter Initialize With Options Nodes. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Downconverter Action Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-abort-generation.html language=enus -->
## TOPIC 00044: IviFgen Abort Generation

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-abort-generation.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-abort-generation.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts a previously initiated signal generation. If the function generator is in the Output Generation State, this node moves the function generator to the Configuration State. If the function generator is already in the Configuration State, the node does nothing. You can configure the output of the

IviFgen Abort Generation

Aborts a previously initiated signal generation. If the function generator is in the Output Generation State, this node moves the function generator to the Configuration State. If the function generator is already in the Configuration State, the node does nothing. You can configure the output of the function generator regardless of whether the function generator is in the Configuration State or the Generation State. This means that you are not required to call the IviFgen Abort Generation Node prior to configuring the output of the function generator. Many function generators constantly generate an output signal, and do not require you to abort signal generation prior to configuring the instrument. If a function generator's output cannot be aborted (i.e., the function generator cannot stop generating a signal) this function does nothing. You are not required to call the IviFgen Initiate Generation and IviFgen Abort Generation nodes. Whether you choose to call these nodes in an application program has no impact on interchangeability. You can choose to use these nodes if you want to optimize your application for instruments that exhibit increased performance when output configuration is performed while the instrument is not generating a signal. Notes: (1) This node does not normally check the instrument status. Typically, you call this node only in a sequence of calls to other low-level driver nodes. The sequence performs one operation. You use the low-level nodes to optimize one or more aspects of interaction with the instrument. If you want to check the instrument status, call the IviFgen Error-Query Node at the conclusion of the sequence.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviSpecAn Initialize Node or IviSpecAn Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviSpecAn Initialize Node or IviSpecAn Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Function Generator Action Status Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-arbitrary-sequence-nodes.html language=enus -->
## TOPIC 00045: IVI Function Generator Arbitrary Sequence Nodes

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-arbitrary-sequence-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-arbitrary-sequence-nodes.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Function Generator Arbitrary Sequence Nodes

IVI Function Generator Configuration Nodes

IviFgen Configure Sample Rate [SEQ]

Configures the rate at which the function generator produces the points that make up arbitrary sequences.

IviFgen Query Arb Sequence Capabilities [SEQ]

Returns the properties of the function generator that are related to creating arbitrary sequences.

IviFgen Create Arbitrary Sequence [SEQ]

Creates an arbitrary sequence from an array of waveform handles and an array of corresponding loop counts. The VI returns a handle that identifies the sequence.

IviFgen Configure Arbitrary Sequence [SEQ]

Configures the properties of the function generator that affect arbitrary sequence generation.

IviFgen Clear Arbitrary Sequence [SEQ]

Removes a previously created arbitrary sequence from the function generator's memory and invalidates the sequence's handle.

IviFgen Clear Arbitrary Memory [SEQ]

Removes all previously created arbitrary waveforms and sequences from the function generator's memory. It also invalidates all waveform and sequence handles.

Parent topic:

IVI Function Generator Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-clear-arbitrary-memory.html language=enus -->
## TOPIC 00046: IviFgen Clear Arbitrary Memory [SEQ]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-clear-arbitrary-memory.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-clear-arbitrary-memory.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes all previously created arbitrary waveforms and sequences from the function generator's memory. It also invalidates all waveform and sequence handles. This node is part of the IviFgenArbSeq [SEQ] extension group. instrument handle The instrument handle that you obtain from the IviFgen Initial

IviFgen Clear Arbitrary Memory [SEQ]

Removes all previously created arbitrary waveforms and sequences from the function generator's memory. It also invalidates all waveform and sequence handles.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Function Generator Arbitrary Sequence Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-configure-stop-trigger.html language=enus -->
## TOPIC 00047: IviFgen Configure Stop Trigger [SPT]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-configure-stop-trigger.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-configure-stop-trigger.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the properties that control the function generator's stop trigger. These properties are the stop trigger source and slope. A stop trigger terminates any generation and has the same effect as calling IviFgen Abort Generation. This node is part of the IviFgenStopTrigger [SPT] extension grou

IviFgen Configure Stop Trigger [SPT]

Configures the properties that control the function generator's stop trigger. These properties are the stop trigger source and slope.

A stop trigger terminates any generation and has the same effect as calling IviFgen Abort Generation.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### Trigger Slope (Positive)

Specifies the slope of the stop trigger. The driver sets the IviFgen Stop Trigger Slope [SPT] property to this value. 

Valid Values:
IVIFGEN_VAL_TRIGGER_POSITIVE (0) - Triggers on a positive slope.
IVIFGEN_VAL_TRIGGER_NEGATIVE (1) - Triggers on a negative slope.
IVIFGEN_VAL_TRIGGER_EITHER (2) - Triggers on either a positive or negative slope.

Default Value:
IVIFGEN_VAL_TRIGGER_POSITIVE (0) - Triggers on a positive slope.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name ("CHANNEL1")

Specifies the virtual channel name that you assign to the instrument in the Configuration Utility.

Default value: "CHANNEL1"

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### Trigger Source (None)

Specifies the source of the stop trigger. The driver sets the IviFgen Stop Trigger Source [SPT] property to this value. 

Valid Values:
IVIFGEN_VAL_TRIGGER_SOURCE_NONE ("") - No trigger source
IVIFGEN_VAL_TRIGGER_SOURCE_IMMEDIATE ("Immediate") - Trigger immediately
IVIFGEN_VAL_TRIGGER_SOURCE_EXTERNAL ("External") - External trigger source
IVIFGEN_VAL_TRIGGER_SOURCE_INTERNAL ("Internal") - Internal trigger source
IVIFGEN_VAL_TRIGGER_SOURCE_SOFTWARE ("Software") - Software trigger 
IVIFGEN_VAL_TRIGGER_SOURCE_LAN0 ("LAN0") - LAN0
IVIFGEN_VAL_TRIGGER_SOURCE_LAN1 ("LAN1") - LAN1
IVIFGEN_VAL_TRIGGER_SOURCE_LAN2 ("LAN2") - LAN2
IVIFGEN_VAL_TRIGGER_SOURCE_LAN3 ("LAN3") - LAN3
IVIFGEN_VAL_TRIGGER_SOURCE_LAN4 ("LAN4") - LAN4
IVIFGEN_VAL_TRIGGER_SOURCE_LAN5 ("LAN5") - LAN5
IVIFGEN_VAL_TRIGGER_SOURCE_LAN6 ("LAN6") - LAN6
IVIFGEN_VAL_TRIGGER_SOURCE_LAN7 ("LAN7") - LAN7
IVIFGEN_VAL_TRIGGER_SOURCE_LXI0 ("LXI0") - LXI Trigger Bus Line 0
IVIFGEN_VAL_TRIGGER_SOURCE_LXI1 ("LXI1") - LXI Trigger Bus Line 1
IVIFGEN_VAL_TRIGGER_SOURCE_LXI2 ("LXI2") - LXI Trigger Bus Line 2
IVIFGEN_VAL_TRIGGER_SOURCE_LXI3 ("LXI3") - LXI Trigger Bus Line 3
IVIFGEN_VAL_TRIGGER_SOURCE_LXI4 ("LXI4") - LXI Trigger Bus Line 4
IVIFGEN_VAL_TRIGGER_SOURCE_LXI5 ("LXI5") - LXI Trigger Bus Line 5
IVIFGEN_VAL_TRIGGER_SOURCE_LXI6 ("LXI6") - LXI Trigger Bus Line 6
IVIFGEN_VAL_TRIGGER_SOURCE_LXI7 ("LXI7") - LXI Trigger Bus Line 7
IVIFGEN_VAL_TRIGGER_SOURCE_TTL0 ("TTL0") - TTL Interface 0
IVIFGEN_VAL_TRIGGER_SOURCE_TTL1 ("TTL1") - TTL Interface 1
IVIFGEN_VAL_TRIGGER_SOURCE_TTL2 ("TTL2") - TTL Interface 2
IVIFGEN_VAL_TRIGGER_SOURCE_TTL3 ("TTL3") - TTL Interface 3
IVIFGEN_VAL_TRIGGER_SOURCE_TTL4 ("TTL4") - TTL Interface 4
IVIFGEN_VAL_TRIGGER_SOURCE_TTL5 ("TTL5") - TTL Interface 5
IVIFGEN_VAL_TRIGGER_SOURCE_TTL6 ("TTL6") - TTL Interface 6
IVIFGEN_VAL_TRIGGER_SOURCE_TTL7 ("TTL7") - TTL Interface 7
IVIFGEN_VAL_TRIGGER_SOURCE_PXI_STAR ("PXI_STAR") - PXI Star Interface
IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG0 ("PXI_TRIG0") - PXI Trigger Bus Line 0
IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG1 ("PXI_TRIG1") - PXI Trigger Bus Line 1
IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG2 ("PXI_TRIG2") - PXI Trigger Bus Line 2
IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG3 ("PXI_TRIG3") - PXI Trigger Bus Line 3
IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG4 ("PXI_TRIG4") - PXI Trigger Bus Line 4
IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG5 ("PXI_TRIG5") - PXI Trigger Bus Line 5
IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG6 ("PXI_TRIG6") - PXI Trigger Bus Line 6
IVIFGEN_VAL_TRIGGER_SOURCE_PXI_TRIG7 ("PXI_TRIG7") - PXI Trigger Bus Line 7
IVIFGEN_VAL_TRIGGER_SOURCE_PXIE_DSTARA ("PXIe_DSTARA") 
 - PXI Express DStar Line A
IVIFGEN_VAL_TRIGGER_SOURCE_PXIE_DSTARB ("PXIe_DSTARB") 
 - PXI Express DStar Line B
IVIFGEN_VAL_TRIGGER_SOURCE_PXIE_DSTARC ("PXIe_DSTARC") 
 - PXI Express DStar Line C
IVIFGEN_VAL_TRIGGER_SOURCE_RTSI0 ("RTSI0") - RTSI Bus Line 0
IVIFGEN_VAL_TRIGGER_SOURCE_RTSI1 ("RTSI1") - RTSI Bus Line 1 
IVIFGEN_VAL_TRIGGER_SOURCE_RTSI2 ("RTSI2") - RTSI Bus Line 2
IVIFGEN_VAL_TRIGGER_SOURCE_RTSI3 ("RTSI3") - RTSI Bus Line 3
IVIFGEN_VAL_TRIGGER_SOURCE_RTSI4 ("RTSI4") - RTSI Bus Line 4
IVIFGEN_VAL_TRIGGER_SOURCE_RTSI5 ("RTSI5") - RTSI Bus Line 5
IVIFGEN_VAL_TRIGGER_SOURCE_RTSI6 ("RTSI6") - RTSI Bus Line 6

Default: 
IVIFGEN_VAL_TRIGGER_SOURCE_NONE ("") - No trigger source

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Function Generator Trigger Burst Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-create-channel-arbitrary-waveform-i16.html language=enus -->
## TOPIC 00048: IviFgen Create Channel Arbitrary Waveform Int16 [AB]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-create-channel-arbitrary-waveform-i16.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-create-channel-arbitrary-waveform-i16.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a channel-specific arbitrary waveform and returns a handle that identifies that waveform. Data is passed in as 16-bit binary data. If the arbitrary waveform generator supports formats smaller than 16 bits, read the IviFgen Binary Alignment [AB] property to determine whether to left or right

IviFgen Create Channel Arbitrary Waveform Int16 [AB]

Creates a channel-specific arbitrary waveform and returns a handle that identifies that waveform.

Data is passed in as 16-bit binary data. If the arbitrary waveform generator supports formats smaller than 16 bits, read the IviFgen Binary Alignment [AB] property to determine whether to left or right justify the data before passing it to this call.

You pass this handle to IviFgen Configure Arbitrary Waveform [ARB] to produce that waveform. You also use the handles this node returns to specify a sequence of arbitrary waveforms with IviFgen Create Arbitrary Sequence [SEQ].

If the instrument does not support channel-based arbitrary waveform creation, use IviFgen Create Arbitrary Waveform [ARB].

Use IviFgen Create Channel Arbitrary Waveform Int32 [AB] to create a channel-specific arbitrary waveform if you want to pass data in 32-bit binary. Use IviFgen Create Channel Arbitrary Waveform [ACH] to create a channel-specific arbitrary waveform with normalized data.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di16.png']

##### Waveform Data Array

Specify the array of data you want to use for the new arbitrary waveform. The array must have at least as many elements as the value you specify in the waveform size control.

When creating a multi-channel waveform, this array is the concatenation of the waveform arrays for each channel. In this case, all waveforms must be of the same length.

Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name ("CHANNEL1")

Specifies the virtual channel name that you assign to the instrument in the Configuration Utility.

Default value: "CHANNEL1"

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Waveform Handle

Returns the handle that identifies the new arbitrary waveform. Pass this handle to the IviFgen Create Arbitrary Waveform [ARB] VI to generate the arbitrary waveform. Pass an array of these handles to the IviFgen Create Arbitrary Sequence [SEQ] VI to create an arbitrary sequence.

Parent topic:

IVI Function Generator Arbitrary Waveform Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-create-channel-arbitrary-waveform-i32.html language=enus -->
## TOPIC 00049: IviFgen Create Channel Arbitrary Waveform Int32 [AB]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-create-channel-arbitrary-waveform-i32.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-create-channel-arbitrary-waveform-i32.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a channel-specific arbitrary waveform and returns a handle that identifies that waveform. Data is passed in as 32-bit binary data. If the arbitrary waveform generator supports formats smaller than 32 bits, read the IviFgen Binary Alignment [AB] property to determine whether to left or right

IviFgen Create Channel Arbitrary Waveform Int32 [AB]

Creates a channel-specific arbitrary waveform and returns a handle that identifies that waveform.

Data is passed in as 32-bit binary data. If the arbitrary waveform generator supports formats smaller than 32 bits, read the IviFgen Binary Alignment [AB] property to determine whether to left or right justify the data before passing it to this call.

You pass this handle to IviFgen Configure Arbitrary Waveform [ARB] to produce that waveform. You also use the handles this node returns to specify a sequence of arbitrary waveforms with IviFgen Create Arbitrary Sequence [SEQ].

If the instrument does not support channel-based arbitrary waveform creation, use IviFgen Create Arbitrary Waveform.

Use IviFgen Create Channel Arbitrary Waveform Int16 [AB] to create a channel-specific arbitrary waveform if you want to pass data in 16-bit binary. Use IviFgen Create Channel Arbitrary Waveform [ACH] to create a channel-specific arbitrary waveform with normalized data.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1di32.png']

##### Waveform Data Array

Specify the array of data you want to use for the new arbitrary waveform. The array must have at least as many elements as the value you specify in the waveform size control.

When you create a multi-channel waveform, this array is the concatenation of the waveform arrays for each channel. In this case, all waveforms must be of the same length.

Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name ("CHANNEL1")

Specifies the virtual channel name that you assign to the instrument in the Configuration Utility.

Default value: "CHANNEL1"

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Waveform Handle

Returns the handle that identifies the new arbitrary waveform. Pass this handle to the IviFgen Create Arbitrary Waveform [ARB] VI to generate the arbitrary waveform. Pass an array of these handles to the IviFgen Create Arbitrary Sequence [SEQ] VI to create an arbitrary sequence.

Parent topic:

IVI Function Generator Arbitrary Waveform Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-create-channel-arbitrary-waveform.html language=enus -->
## TOPIC 00050: IviFgen Create Channel Arbitrary Waveform [ACH]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-create-channel-arbitrary-waveform.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-create-channel-arbitrary-waveform.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a channel-specific arbitrary waveform and returns a handle that identifies that waveform. You pass this handle to IviFgen Configure Arbitrary Waveform [ARB] to produce that waveform. You also use the handles this node returns to specify a sequence of arbitrary waveforms with IviFgen Create A

IviFgen Create Channel Arbitrary Waveform [ACH]

Creates a channel-specific arbitrary waveform and returns a handle that identifies that waveform.

You pass this handle to IviFgen Configure Arbitrary Waveform [ARB] to produce that waveform. You also use the handles this node returns to specify a sequence of arbitrary waveforms with IviFgen Create Arbitrary Sequence [SEQ].

If the instrument does not support channel-based arbitrary waveform creation, use the IviFgen Create Arbitrary Waveform VI.

Use the following VIs to create a channel-specific arbitrary waveform if you want to pass data in 16-bit or 32-bit binary:

- IviFgen Create Channel Arbitrary Waveform Int16 [AB] VI

- IviFgen Create Channel Arbitrary Waveform Int32 [AB] VI

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### Waveform Data Array

Specify the array of data you want to use for the new arbitrary waveform. The array must have at least as many elements as the value you specify in the waveform size control.

You must normalize the data points in the array to be between -1.00 and +1.00.

When you create a multi-channel waveform, this array is the concatenation of the waveform arrays for each channel. In this case, all waveforms must be of the same length.

Default Value: None

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name ("CHANNEL1")

Specifies the virtual channel name that you assign to the instrument in the Configuration Utility.

Default value: "CHANNEL1"

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### Waveform Handle

Returns the handle that identifies the new arbitrary waveform. Pass this handle to the IviFgen Create Arbitrary Waveform [ARB] VI to generate the arbitrary waveform. Pass an array of these handles to the IviFgen Create Arbitrary Sequence [SEQ] VI to create an arbitrary sequence.

Parent topic:

IVI Function Generator Arbitrary Waveform Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-disable-all-data-markers.html language=enus -->
## TOPIC 00051: IviFgen Disable All Data Markers [DM]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-disable-all-data-markers.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-disable-all-data-markers.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables all of the data markers by setting their IviFgen Data Marker Destination [DM] property to None. This node is part of the IviFgenDataMarker [DM] extension group. instrument handle The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The h

IviFgen Disable All Data Markers [DM]

Disables all of the data markers by setting their IviFgen Data Marker Destination [DM] property to None.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Function Generator Marker Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-send-software-hold-trigger-ht.html language=enus -->
## TOPIC 00052: IviFgen Send Software Hold Trigger [HT]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-send-software-hold-trigger-ht.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-send-software-hold-trigger-ht.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a software-generated hold trigger to the function generator. If the trigger source is not set to software trigger, this node returns the error IVIFGEN_ERROR_TRIGGER_NOT_SOFTWARE. Notes: (1) This node does not normally check the instrument status. Typically, you call this node only in a sequenc

IviFgen Send Software Hold Trigger [HT]

Sends a software-generated hold trigger to the function generator. If the trigger source is not set to software trigger, this node returns the error IVIFGEN_ERROR_TRIGGER_NOT_SOFTWARE. Notes: (1) This node does not normally check the instrument status. Typically, you call this node only in a sequence of calls to other low-level driver nodes. The sequence performs one operation. You use the low-level nodes to optimize one or more aspects of interaction with the instrument. If you want to check the instrument status, call the IviFgen Error-Query node at the conclusion of the sequence. (2) This node is part of the IviFgenHoldTrigger [HT] extension group.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Function Generator Action Status Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-send-software-resume-trigger-rt.html language=enus -->
## TOPIC 00053: IviFgen Send Software Resume Trigger [RT]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-send-software-resume-trigger-rt.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-send-software-resume-trigger-rt.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a software-generated resume trigger to the function generator. If the trigger source is not set to software trigger, this node returns the error IVIFGEN_ERROR_TRIGGER_NOT_SOFTWARE. Notes: (1) This node does not normally check the instrument status. Typically, you call this node only in a seque

IviFgen Send Software Resume Trigger [RT]

Sends a software-generated resume trigger to the function generator. If the trigger source is not set to software trigger, this node returns the error IVIFGEN_ERROR_TRIGGER_NOT_SOFTWARE. Notes: (1) This node does not normally check the instrument status. Typically, you call this node only in a sequence of calls to other low-level driver nodes. The sequence performs one operation. You use the low-level nodes to optimize one or more aspects of interaction with the instrument. If you want to check the instrument status, call the IviFgen Error-Query node at the conclusion of the sequence. (2) This node is part of the IviFgenResumeTrigger [RT] extension group.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Function Generator Action Status Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-send-software-stop-trigger-spt.html language=enus -->
## TOPIC 00054: IviFgen Send Software Stop Trigger [SPT]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-send-software-stop-trigger-spt.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-send-software-stop-trigger-spt.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a software-generated stop trigger to the function generator. If the trigger source is not set to software trigger, this node returns the error IVIFGEN_ERROR_TRIGGER_NOT_SOFTWARE. Notes: (1) This node does not normally check the instrument status. Typically, you call this node only in a sequenc

IviFgen Send Software Stop Trigger [SPT]

Sends a software-generated stop trigger to the function generator. If the trigger source is not set to software trigger, this node returns the error IVIFGEN_ERROR_TRIGGER_NOT_SOFTWARE. Notes: (1) This node does not normally check the instrument status. Typically, you call this node only in a sequence of calls to other low-level driver nodes. The sequence performs one operation. You use the low-level nodes to optimize one or more aspects of interaction with the instrument. If you want to check the instrument status, call the IviFgen Error-Query node at the conclusion of the sequence. (2) This node is part of the IviFgenStopTrigger [SPT] extension group.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Function Generator Action Status Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-send-software-trigger-trg.html language=enus -->
## TOPIC 00055: IviFgen Send Software Trigger [TRG]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-send-software-trigger-trg.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-send-software-trigger-trg.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to trigger the function generator. If the trigger source is not set software trigger, this node returns the error IVIFGEN_ERROR_TRIGGER_NOT_SOFTWARE. Notes: (1) This node does not normally check the instrument status. Typically, you call this node only in a sequence of calls to other

IviFgen Send Software Trigger [TRG]

Sends a command to trigger the function generator. If the trigger source is not set software trigger, this node returns the error IVIFGEN_ERROR_TRIGGER_NOT_SOFTWARE. Notes: (1) This node does not normally check the instrument status. Typically, you call this node only in a sequence of calls to other low-level driver nodes. The sequence performs one operation. You use the low-level nodes to optimize one or more aspects of interaction with the instrument. If you want to check the instrument status, call the IviFgen Error-Query node at the conclusion of the sequence. (2) This node is part of the IviFgenTrigger [TRG] extension group.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

The instrument handle that you obtain from the IviFgen Initialize or IviFgen Initialize With Options Node. The handle identifies a particular instrument session.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Function Generator Action Status Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-trigger-burst-nodes.2.html language=enus -->
## TOPIC 00056: IVI Function Generator Frequency Modulation Nodes

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-trigger-burst-nodes.2.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-trigger-burst-nodes.2.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Function Generator Frequency Modulation Nodes

IVI Function Generator Configuration Nodes

IviFgen Configure AM Enabled [AM]

Configures whether the function generator applies frequency modulation to the channel.

IviFgen Configure FM Source [FM]

Configures the source of the frequency modulating signal the function generator uses for the channel.

IviFgen Configure FM Internal [FM]

Configures the properties that control the function generator's internal frequency modulation source. These properties are the modulation depth, waveform, and frequency.

Parent topic:

IVI Function Generator Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivifgen-trigger-burst-nodes.3.html language=enus -->
## TOPIC 00057: IVI Function Generator Trigger Burst Nodes

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivifgen-trigger-burst-nodes.3.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivifgen-trigger-burst-nodes.3.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Function Generator Trigger Burst Nodes

IVI Function Generator Configuration Nodes

IviFgen Configure Trigger Source [TRG]

Configures the trigger source for a channel.

IviFgen Configure Internal Trigger Rate [IT]

Configures the rate at which the function generator's internal trigger source generates trigger signals.

IviFgen Configure Start Trigger [STT]

Configures the rate at which the function generator's internal trigger source generates trigger signals.

IviFgen Configure Stop Trigger [SPT]

Configures the properties that control the function generator's stop trigger. These properties are the stop trigger source and slope.

IviFgen Configure Hold Trigger [HT]

Configures the properties that control the function generator's hold trigger. These properties are the hold trigger source and slope.

IviFgen Configure Resume Trigger [RT]

Configures the properties that control the function generator's resume trigger. These properties are the resume trigger source and slope.

IviFgen Configure Advance Trigger [AT]

Configures the properties that control the function generator's advance trigger. These properties are the advance trigger source and slope.

IviFgen Configure Burst Count [BST]

Configures the burst count.

Parent topic:

IVI Function Generator Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-configure-averaging-count.html language=enus -->
## TOPIC 00058: IviPwrMeter Configure Averaging Count [AVG]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-configure-averaging-count.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-configure-averaging-count.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the average count that the instrument uses in manual averaging mode. The averaging count specifies the number of samples that the instrument takes before the measurement is complete. instrument handle out Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or Ivi

IviPwrMeter Configure Averaging Count [AVG]

Sets the average count that the instrument uses in manual averaging mode. The averaging count specifies the number of samples that the instrument takes before the measurement is complete.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

Parent topic:

IVI Power Meter Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-configure-channel-enabled.html language=enus -->
## TOPIC 00059: IviPwrMeter Configure Channel Enabled [CH]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-configure-channel-enabled.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-configure-channel-enabled.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables a specified channel for measurement. channel enabled (True) Pass TRUE to enable the channel. Pass FALSE to disable the channel. The driver sets the IviPwrMeter>>Basic Operation>>Channel Acquisition>>Channel Enabled [CH] property to this value. Valid Values: TRUE - "On" FALSE - "O

IviPwrMeter Configure Channel Enabled [CH]

Enables or disables a specified channel for measurement.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### channel enabled (True)

Pass TRUE to enable the channel. Pass FALSE to disable the channel. The driver sets the IviPwrMeter>>Basic Operation>>Channel Acquisition>>Channel Enabled [CH]
property to this value. 

Valid Values: 
 TRUE - "On" 
 FALSE - "Off"

Default Value: 
 TRUE - "On"

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### Channel Name

Pass the virtual channel name that you assign to the instrument in the Configuration Utility. Users who want to achieve interchangeability should use a virtual channel name. The virtual channel name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical channel name. Virtual channel names are aliases for instrument-specific channel strings. The instrument-specific channel strings can differ from one instrument to another. Virtual channel names allow you to use and swap instruments without having to change the channel names in your source code. You assign a virtual channel name to an instrument-specific channel through the Configuration Utility. This control accepts virtual channel names you have assigned to the specific instrument you are using. It also accepts the instrument-specific channel names.

Default value: ""

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

Parent topic:

IVI Power Meter Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-configure-correction-freq.html language=enus -->
## TOPIC 00060: IviPwrMeter Configure Correction Frequency

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-configure-correction-freq.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-configure-correction-freq.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency of the input signal in Hertz. The instrument uses this value to determine the appropriate correction factor for the sensor. instrument handle Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter

IviPwrMeter Configure Correction Frequency

Specifies the frequency of the input signal in Hertz.
 The instrument uses this value to determine the appropriate correction factor for the sensor.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name ("")

The name of the channel to be configured.

Pass the virtual channel name that you assign to the instrument in the Configuration Utility.

Users who want to achieve interchangeability should use a virtual channel name. The virtual channel name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical channel name.

Virtual channel names are aliases for instrument-specific channel strings. The instrument-specific channel strings can differ from one instrument to another. Virtual channel names allow you to use and swap instruments without having to change the channel names in your source code. You assign a virtual channel name to an instrument-specific channel through the Configuration Utility. This control accepts virtual channel names you have assigned to the specific instrument you are using. It also accepts the instrument-specific channel names.

Default Value: ""

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency (50 MHz)

Specifies the expected frequency of the input signal in Hertz. The instrument uses this parameter to determine the appropriate correction factor for the sensor. The driver sets the IviPwrMeter>>Basic Operation>>Correction Frequency property to this value.

Units: Hz

Default Value: 50 MHz

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Power Meter Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-configure-duty-cycle-correction.html language=enus -->
## TOPIC 00061: IviPwrMeter Configure Duty Cycle Correction [DC]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-configure-duty-cycle-correction.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-configure-duty-cycle-correction.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables the duty cycle correction and sets the duty cycle correction for pulse power measurements.. correction value (100 %) Specifies the duty cycle correction the power meter uses to calculate the pulse power of a pulse-modulated signal. The driver sets the IviPwrMeter>>Duty Cycle>>Dut

IviPwrMeter Configure Duty Cycle Correction [DC]

Enables or disables the duty cycle correction and sets the duty cycle correction for pulse power measurements..

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### correction value (100 %)

Specifies the duty cycle correction the power meter uses to calculate the pulse power of a pulse-modulated signal. The driver sets the IviPwrMeter>>Duty Cycle>>Duty Cycle Correction [DC] property to this value. 

The power meter measures the average power of the pulsed input signal and then divides the result by the duty cycle correction value to obtain a pulse power reading. 

The value of this property is specified as a percentage.
For a pulse with a duty cycle of 10%, this property should be given the value 0.1. 

Units: percentage ( % ).

Default Value: 100 %

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### correction enabled (False)

Enables or disables the duty cycle correction. The driver sets the IviPwrMeter>>Duty Cycle>>Duty Cycle Correction [DC]_ENABLED property to this value.

Valid Values: 
 TRUE - "On" 
 FALSE - "Off"

Default Value: 
 FALSE - "Off"

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name ("")

The name of the channel for which to specify the duty cycle correction.

Pass the virtual channel name that you assign to the instrument in the Configuration Utility.

Users who want to achieve interchangeability should use a virtual channel name. The virtual channel name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical channel name.

Virtual channel names are aliases for instrument-specific channel strings. The instrument-specific channel strings can differ from one instrument to another. Virtual channel names allow you to use and swap instruments without having to change the channel names in your source code. You assign a virtual channel name to an instrument-specific channel through the Configuration Utility. This control accepts virtual channel names you have assigned to the specific instrument you are using. It also accepts the instrument-specific channel names.

Default Value: ""

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

Parent topic:

IVI Power Meter Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-configure-internal-trigger-level.html language=enus -->
## TOPIC 00062: IviPwrMeter Configure Internal Trigger Level [IT]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-configure-internal-trigger-level.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-configure-internal-trigger-level.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the internal trigger level of the power meter. trigger level (0.001) The signal trigger level. The driver sets the IviPwrMeter>>Trigger>>Internal Trigger>>Internal Trigger Level [IT] property to this value. The value of this property is specified in the same unit as the value of the IviPw

IviPwrMeter Configure Internal Trigger Level [IT]

Configures the internal trigger level of the power meter.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### trigger level (0.001)

The signal trigger level. The driver sets the IviPwrMeter>>Trigger>>Internal Trigger>>Internal Trigger Level [IT] property to this value.

The value of this property is specified in the same unit as the value of the IviPwrMeter>>Basic Operation>>Units property which you can set by calling the IviPwrMeter Configure Units.vi.

Default Value: 0.001

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

Parent topic:

IVI Power Meter Trigger Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-configure-internal-trigger.html language=enus -->
## TOPIC 00063: IviPwrMeter Configure Internal Trigger [IT]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-configure-internal-trigger.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-configure-internal-trigger.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the internal trigger event source and the internal trigger slope of the power meter. slope (Positive) The internal trigger slope. The driver sets the IviPwrMeter>>Trigger>>Internal Trigger>>Internal Trigger Slope [IT] property to this value. Valid Values: IVIPWRMETER_VAL_POSITIVE - Sets t

IviPwrMeter Configure Internal Trigger [IT]

Configures the internal trigger event source and the internal trigger slope of the power meter.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### slope (Positive)

The internal trigger slope. The driver sets the IviPwrMeter>>Trigger>>Internal Trigger>>Internal Trigger Slope [IT] property to this value.

Valid Values:

 IVIPWRMETER_VAL_POSITIVE - Sets the trigger event 
 to occur on the rising edge of the trigger pulse. 

 IVIPWRMETER_VAL_NEGATIVE (Difference) - Sets the 
 trigger event to occur on the falling edge of 
 the trigger pulse.

Default Value:

 IVIPWRMETER_VAL_POSITIVE

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### event source ("")

The name of the channel to use as the internal trigger event source. The driver sets the IviPwrMeter>>Trigger>>Internal Trigger>>Internal Trigger Event Source [IT] property to this value.

Pass the virtual channel name that you assign to the instrument in the Configuration Utility.

Users who want to achieve interchangeability should use a virtual channel name. The virtual channel name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical channel name.

Virtual channel names are aliases for instrument-specific channel strings. The instrument-specific channel strings can differ from one instrument to another. Virtual channel names allow you to use and swap instruments without having to change the channel names in your source code. You assign a virtual channel name to an instrument-specific channel through the Configuration Utility. This control accepts virtual channel names you have assigned to the specific instrument you are using. It also accepts the instrument-specific channel names.

Default Value: ""

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

Parent topic:

IVI Power Meter Trigger Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-configure-measurement.html language=enus -->
## TOPIC 00064: IviPwrMeter Configure Measurement

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-configure-measurement.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-configure-measurement.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the instrument to take single or dual channel measurements. For single channel measurements, this node enables the channel specified by Operand1 and disables all other channels. The result returned by the Fetch or Read nodes is the measurement taken at the channel specified by Operand1. A

IviPwrMeter Configure Measurement

Configures the instrument to take single or dual channel measurements.

For single channel measurements, this node enables the channel specified by Operand1 and disables all other channels. The result returned by the Fetch or Read nodes is the measurement taken at the channel specified by Operand1. Although, the driver measures the power in Watts, the result is converted to the same unit as the value of the IviPwrMeter>>Basic Operation>>Units property.

For dual channel measurements, this node enables the channels specified by Operand1 and Operand2 and disables all other channels. The result returned by the Fetch or Read nodes is the result of the specified math operation applied to the measurements on the channels specified by Operand1 and Operand2.

Although, the math operation is performed on the measured values in Watts,the result is converted to the appropriate units depending on the value of the Units property and the value of the Operator.

For Difference and Sum operations, the resulting units is the same as the Units property.

For Quotient operations, the resulting units are in dB, except when Units are set to Watts. When set to Watts, the resulting measurement is without units.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### operator (No Operator)

The math VI applied to the operands.

Valid Values:

 IVIPWRMETER_VAL_NONE (No Operator) - Return the 
 measured value for Operand1. 

 IVIPWRMETER_VAL_DIFFERENCE (Difference) - Subtract the 
 power measured on Operand2 from the power measured 
 on Operand1.

 IVIPWRMETER_VAL_SUM (Sum) - Add the power measured on 
 Operand2 to the power measured on Operand1.

 IVIPWRMETER_VAL_QUOTIENT (Quotient) - Divide the power
 measured on Operand1 by the power measured on 
 Operand2.

Default Value:
 IVIPWRMETER_VAL_NONE (No Operator)

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### operand 1 ("")

The name of the channel from which the value for the first operand of the math VI is measured.

Default Value: ""

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### operand 2 ("")

The name of the channel from which the value for the second operand of the math VI is measured.

Default Value: ""

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Power Meter Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-configure-offset.html language=enus -->
## TOPIC 00065: IviPwrMeter Configure Offset

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-configure-offset.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-configure-offset.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset to be added to the measured value in units of dB. instrument handle Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options. Default value: None error in Error conditions that o

IviPwrMeter Configure Offset

Specifies the offset to be added to the measured value in units of dB.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name ("")

The name of the channel for which to set the Offset.

Pass the virtual channel name that you assign to the instrument in the Configuration Utility.

Users who want to achieve interchangeability should use a virtual channel name. The virtual channel name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical channel name.

Virtual channel names are aliases for instrument-specific channel strings. The instrument-specific channel strings can differ from one instrument to another. Virtual channel names allow you to use and swap instruments without having to change the channel names in your source code. You assign a virtual channel name to an instrument-specific channel through the Configuration Utility. This control accepts virtual channel names you have assigned to the specific instrument you are using. It also accepts the instrument-specific channel names.

Default Value: ""

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### offset (0.0 dB)

Specifies an offset to be added to the measured value. The units of this property are dB. This property can be used to compensate for system losses or gains between the unit under test and the sensor of the power meter. The driver sets the IviPwrMeter>>Basic Operation>>Offset property to this value.

For example, a cable loss of 2 dB could be compensated for by setting this property to 2. Similarly, a gain stage of 10 dB could be accounted for by setting the value of this property to -10. In both cases, the reading from the power meter will indicate the power at the unit under test rather than power at the power meter's sensor.

Unit: dB

Default Value: 0.0 dB

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Power Meter Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-configure-range-auto-enabled.html language=enus -->
## TOPIC 00066: IviPwrMeter Configure Range Auto Enabled

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-configure-range-auto-enabled.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-configure-range-auto-enabled.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables the auto range mode for a given channel. instrument handle Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options. Default value: None error in Error conditions that occur befor

IviPwrMeter Configure Range Auto Enabled

Enables or disables the auto range mode for a given channel.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name ("")

The name of the channel to configure.

Pass the virtual channel name that you assign to the instrument in the Configuration Utility.

Users who want to achieve interchangeability should use a virtual channel name. The virtual channel name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical channel name.

Virtual channel names are aliases for instrument-specific channel strings. The instrument-specific channel strings can differ from one instrument to another. Virtual channel names allow you to use and swap instruments without having to change the channel names in your source code. You assign a virtual channel name to an instrument-specific channel through the Configuration Utility. This control accepts virtual channel names you have assigned to the specific instrument you are using. It also accepts the instrument-specific channel names.

Default Value: ""

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### range auto enabled (True)

Specifies the auto range mode. Pass TRUE to turn auto ranging on. Pass FALSE to turn auto ranging off. The driver sets the IviPwrMeter>>Basic Operation>>Range Auto Enabled property to this value.

Valid Values: 
 TRUE - "On"
 FALSE - "Off"

Default Value: 
 TRUE - "On"

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

IVI Power Meter Configuration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-is-calibration-complete.html language=enus -->
## TOPIC 00067: IviPwrMeter Is Calibration Complete [CAL]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-is-calibration-complete.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-is-calibration-complete.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the instrument to determine the status of all calibration operations initiated by the IviPwrMeter Calibrate [CAL] node. This node returns the IVIPWRMETER_VAL_CALIBRATION_COMPLETE (1) value in the Status parameter only when calibration is complete on all channels. If some calibration operatio

IviPwrMeter Is Calibration Complete [CAL]

Queries the instrument to determine the status of all calibration operations initiated by the IviPwrMeter Calibrate [CAL] node. This node returns the IVIPWRMETER_VAL_CALIBRATION_COMPLETE (1) value in the Status parameter only when calibration is complete on all channels.

If some calibration operations are still in progress on one or more channels, the driver returns the IVIPWRMETER_VAL_CALIBRATION_IN_PROGRESS (0) value. If the driver cannot query the instrument to determine its state, the driver returns the IVIPWRMETER_VAL_CALIBRATION_STATUS_UNKNOWN (-1) value.

Note

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### calibration status

Returns the status of the calibration.

This driver defines the following calibration status:

IVIPWRMETER_VAL_CALIBRATION_COMPLETE (1)
 - The power meter has completed the calibration on 
 all enabled channels.

IVIPWRMETER_VAL_CALIBRATION_IN_PROGRESS (0)
 - The power meter is still taking a calibration on 
 one or more enabled channels.

IVIPWRMETER_VAL_CALIBRATION_STATUS_UNKNOWN (-1)
 - The power meter cannot determine the status of 
 the calibration.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

Parent topic:

IviPwrMeter Calibration Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-low-level-measurement.html language=enus -->
## TOPIC 00068: IVI Power Meter Low-Level Measurement Nodes

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-low-level-measurement.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-low-level-measurement.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Power Meter Low-Level Measurement Nodes

IVI Power Meter Measurement Nodes

IviPwrMeter Abort

Aborts all previously initiated measurements and returns the power meter to the Idle state.

IviPwrMeter Fetch

Returns the result from a previously initiated single or dual channel measurement.

IviPwrMeter Fetch Channel [CH]

Returns the result from a previously initiated measurement on a specified channel. Call the IviPwrMeter Initiate node to initiate a measurement before calling this node.

IviPwrMeter Initiate

Initiates a measurement on all enabled channels.

IviPwrMeter Is Measurement Complete

Queries the instrument to determine the status of the measurement initiated by IviPwrMeter Initiate.

IviPwrMeter Query Result Range Type

Takes a measurement value that is returned from one of the Fetch, Fetch Channel, Read, or Read Channel nodes and determines if the value is a valid measurement value or a value indicating that an out-of-range condition occurred.

IviPwrMeter Send Software Trigger [SWT]

Sends a command to trigger the power meter. Call this node if you pass IVIPWRMETER_VAL_SOFTWARE_TRIG for the IviPwrMeter>>Trigger>>Trigger Source [TRG] property or the Trigger Source parameter of the IviPwrMeter Configure Trigger Source [TRG] node.

Parent topic:

IVI Power Meter Measurement Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-measurement.html language=enus -->
## TOPIC 00069: IVI Power Meter Measurement Nodes

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-measurement.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-measurement.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`

IVI Power Meter Measurement Nodes

IVI Pwr Meter Nodes

Develop interchangeable applications for your power meter.

IviPwrMeter Read

Initiates a measurement, waits until the power meter has returned to the Idle state, and returns the result of the measurement.

IviPwrMeter Read Channel [CH]

Initiates a measurement, waits until the power meter has returned to the Idle state, and returns the result of the measurement on the specified channel.

IVI Power Meter Low-Level Measurement Nodes

Parent topic:

IVI Pwr Meter Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter-read-channel.html language=enus -->
## TOPIC 00070: IviPwrMeter Read Channel [CH]

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter-read-channel.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter-read-channel.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates a measurement, waits until the power meter has returned to the Idle state, and returns the result of the measurement on the specified channel. After this node executes, the Reading parameter contains an actual reading on the channel specified by the Channel parameter. If the specified chan

IviPwrMeter Read Channel [CH]

Initiates a measurement, waits until the power meter has returned to the Idle state, and returns the result of the measurement on the specified channel.

After this node executes, the Reading parameter contains an actual reading on the channel specified by the Channel parameter. If the specified channel is not enabled for measurement, this node returns the Channel Not Enabled (0xBFFA2001) error. The Reading result is in the same unit as the value of the Units property.

After this node executes, the Reading parameter may contain a value indicating that an out-of-range condition occurred. If an out-of-range condition occurs, the Result parameter contains an IEEE defined -Inf (Negative Infinity) or +Inf (Positive Infinity) value and the node returns the Under Range (0x3FFA2001) or Over Range (0x3FFA2002) warning. Test if the measurement value is out of range with the IviPwrMeter Query Result Range Type node.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### reading

The data read from the power meter.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### maximum time (5000 ms)

Pass the maximum length of time in which to allow the read operation to complete. Express this value in milliseconds. 

If the operation does not complete within this time interval, the VI returns the IVIPWRMETER_ERROR_MAX_TIME_EXCEEDED (0xBFFA2020) error code. When this occurs, you can call IviPwrMeter Abort.vi to cancel the read operation and return the instrument to the Idle state. 

Defined Values:
IVIPWRMETER_VAL_MAX_TIME_INFINITE (-1) - Wait indefinitely for a timeout.
IVIPWRMETER_VAL_MAX_TIME_IMMEDIATE (0) - Do not wait for a timeout.

Default Value: 5000 ms

Notes:

(1) The Maximum Time parameter affects only this VI. It has no effect on other timeout parameters or properties.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### channel name ("")

The name of the channel from which to read the measurement.

Pass the virtual channel name that you assign to the instrument in the Action Utility.

Users who want to achieve interchangeability should use a virtual channel name. The virtual channel name should be sufficiently specific to the test system such that it is unlikely to conflict with a physical channel name.

Virtual channel names are aliases for instrument-specific channel strings. The instrument-specific channel strings can differ from one instrument to another. Virtual channel names allow you to use and swap instruments without having to change the channel names in your source code. You assign a virtual channel name to an instrument-specific channel through the Configuration Utility. This control accepts virtual channel names you have assigned to the specific instrument you are using. It also accepts the instrument-specific channel names.

Default Value: ""

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### instrument handle out

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### instrument handle

Instrument handle that you obtain from IviPwrMeter InitializeIviPwrMeter Initialize or IviPwrMeter Initialize With OptionsIviPwrMeter Initialize With Options.

Default value: None

Parent topic:

IVI Power Meter Measurement Nodes

<!--NI_TOPIC bundle=labview-nxg-ivi-compliance-package path=ivipwrmeter.html language=enus -->
## TOPIC 00071: IVI Pwr Meter Nodes

- bundle_id: `labview-nxg-ivi-compliance-package`
- source_path: `ivipwrmeter.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-ivi-compliance-package/raw/resource/enus/ivipwrmeter.html
- document_id: `labview-nxg-ivi-compliance-package`
- page_type: `leaf`
- content_type: `reference`
- source_description: Develop interchangeable applications for your power meter.

IVI Pwr Meter Nodes

Develop interchangeable applications for your power meter.

IVI Compliance Package Nodes

IviPwrMeter Initialize

Creates a new IVI instrument driver session. Opens a session to the specific driver using the logical name of the IVI driver session.

IviPwrMeter Initialize With Options

Creates a new IVI instrument driver and optionally sets the initial session properties state.

IviPwrMeter Close

Closes the instrument I/O session.

IviPwrMeter Property Node

Gets (reads) and/or sets (writes) properties of IviPwrMeter.

IVI Power Meter Configuration Nodes

IVI Power Meter Measurement Nodes

IVI Power Meter Zeroing Nodes

IviPwrMeter Calibration Nodes

IVI Power Meter Configuration Nodes

Parent topic:

IVI Compliance Package Nodes
