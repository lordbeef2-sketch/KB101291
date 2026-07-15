# NI DOCUMENT BUNDLE: ni-579x-lvnxg-host-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-579x-lvnxg-host-api-ref start=1 end=44 -->
<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=clocking-nodes.html language=enus -->
## TOPIC 00001: Clocking Nodes

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `clocking-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/clocking-nodes.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`

Clocking Nodes

ni579x Configure Clock

Configures the source of the Sample Clock and the Reference Clock.

ni579x Configure LO Enable

Enables the internal LO and waits for LO Enable to complete.

ni579x Configure LO Frequency

Configures the frequency of the internal LO and returns the coerced frequency.

ni579x Configure LO Filter

Configures the mixer LO input filter.

ni579x Configure Clock Phase DAC

Configures the value of the clock phase digital-to-analog converter (DAC) and modifies the phase of the reference used to generate the Sample Clock and LO if the reference frequency source is external.

ni579x Wait for Lock

Waits for the specified circuit to complete its configuration and report a successful lock to the supplied reference.

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=configuration-nodes.html language=enus -->
## TOPIC 00002: Configuration Nodes

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `configuration-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/configuration-nodes.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`

Configuration Nodes

ni579x Open

Opens a session to the NI-579x Configuration nodes, creates a session to the Register Bus nodes, and initializes the CLIP.

ni579x Configure Mixer

Configures the mixer (RF upconverter/downconverter) by enabling the LO, setting the LO frequency, configuring the LO filter, and making any necessary routes.

ni579x Configure Reference Level

Configures the specified reference level.

ni579x Configure Output Power

Configures the specified output power.

ni579x Close

Closes the session to the NI-579x Configuration nodes.

ni579x Route Signal

Routes a signal in the adapter module from the specified source to the specified destination terminal.

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=conversions-nodes.html language=enus -->
## TOPIC 00003: Conversions Nodes

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `conversions-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/conversions-nodes.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`

Conversions Nodes

From Byte Array

Converts a byte array to the specified data type.

To Byte Array

Converts an input data type to a byte array.

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=eeprom-nodes.html language=enus -->
## TOPIC 00004: EEPROM Nodes

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `eeprom-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/eeprom-nodes.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`

EEPROM Nodes

ni579x Load Characterization Data (Single Channel)

Reads characterization data from the on-device EEPROM and returns headers and characterization data for the specified channel.

ni579x Store Characterization Data (EEPROM)

Stores headers and per-channel characterization data in the on-device EEPROM.

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=from-byte-array-f32.html language=enus -->
## TOPIC 00005: From Byte Array (F32)

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `from-byte-array-f32.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/from-byte-array-f32.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a byte array to an F32 data type. byte array in The byte array to convert. element out The converted data type.

From Byte Array (F32)

Converts a byte array to an F32 data type.

[IMAGE alt='1378' src='From_Byte_Array_(F32).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### byte array in

The byte array to convert.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### element out

The converted data type.

Parent topic:

From Byte Array

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=from-byte-array-lv-timestamp.html language=enus -->
## TOPIC 00006: From Byte Array (LV Timestamp)

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `from-byte-array-lv-timestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/from-byte-array-lv-timestamp.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a byte array to an LV Timestamp data type. byte array in The byte array to convert. element out The converted data type.

From Byte Array (LV Timestamp)

Converts a byte array to an LV Timestamp data type.

[IMAGE alt='1378' src='From_Byte_Array_(LV_Timestamp).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### byte array in

The byte array to convert.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### element out

The converted data type.

Parent topic:

From Byte Array

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=from-byte-array-u16.html language=enus -->
## TOPIC 00007: From Byte Array (U16)

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `from-byte-array-u16.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/from-byte-array-u16.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a byte array to a U16 data type. byte array in The byte array to convert. element out The converted data type.

From Byte Array (U16)

Converts a byte array to a U16 data type.

[IMAGE alt='1378' src='From_Byte_Array_(U16).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### byte array in

The byte array to convert.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### element out

The converted data type.

Parent topic:

From Byte Array

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=from-byte-array-u32.html language=enus -->
## TOPIC 00008: From Byte Array (U32)

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `from-byte-array-u32.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/from-byte-array-u32.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a byte array to a U32 data type. byte array in The byte array to convert. element out The converted data type.

From Byte Array (U32)

Converts a byte array to a U32 data type.

[IMAGE alt='1378' src='From_Byte_Array_(U32).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### byte array in

The byte array to convert.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### element out

The converted data type.

Parent topic:

From Byte Array

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=from-byte-array-u8.html language=enus -->
## TOPIC 00009: From Byte Array (U8)

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `from-byte-array-u8.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/from-byte-array-u8.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a byte array to a U8 data type. byte array in The byte array to convert. element out The converted data type.

From Byte Array (U8)

Converts a byte array to a U8 data type.

[IMAGE alt='1378' src='From_Byte_Array_(U8).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### byte array in

The byte array to convert.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### element out

The converted data type.

Parent topic:

From Byte Array

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=from-byte-array.html language=enus -->
## TOPIC 00010: From Byte Array

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `from-byte-array.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/from-byte-array.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a byte array to the specified data type.

From Byte Array

Converts a byte array to the specified data type.

Conversions Nodes

From Byte Array (F32)

Converts a byte array to an F32 data type.

From Byte Array (LV Timestamp)

Converts a byte array to an LV Timestamp data type.

From Byte Array (U16)

Converts a byte array to a U16 data type.

From Byte Array (U32)

Converts a byte array to a U32 data type.

From Byte Array (U8)

Converts a byte array to a U8 data type.

Parent topic:

Conversions Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-close.html language=enus -->
## TOPIC 00011: ni579x Close

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-close.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-close.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session to the NI-579x Configuration nodes. This node destroys the session to the Register Bus object. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. error in Error conditions that occur before this node runs. Th

ni579x Close

Closes the session to the NI-579x Configuration nodes.

This node destroys the session to the Register Bus object.

[IMAGE alt='1378' src='ni579x_Close.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### fpga ref

Reference to the FPGA VI that is associated with this session of the Register Bus object.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-configure-amplifier.html language=enus -->
## TOPIC 00012: ni579x Configure Amplifier

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-configure-amplifier.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-configure-amplifier.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the baseband amplifier and returns True if the scope input is valid. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. enable? Specifies whether to enable the baseband amplifier. error in Error conditions that occur be

ni579x Configure Amplifier

Enables the baseband amplifier and returns True if the scope input is valid.

[IMAGE alt='1378' src='ni579x_Configure_Amplifier.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable?

Specifies whether to enable the baseband amplifier.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Specifies the mixer to configure. The only valid value is 
rx.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### coerced enable

Returns True if the baseband amplifier is enabled, and returns False if the baseband amplifier is not enabled.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

RF Front End Configuration Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-configure-attenuation.html language=enus -->
## TOPIC 00013: ni579x Configure Attenuation

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-configure-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-configure-attenuation.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the attenuation level and returns the coerced attenuation level. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. attenuation [dB] Specifies the attenuation, in dB, in the stopband. If attenuation is less than or e

ni579x Configure Attenuation

Configures the attenuation level and returns the coerced attenuation level.

[IMAGE alt='1378' src='ni579x_Configure_Attenuation.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### attenuation [dB]

Specifies the attenuation, in dB, in the stopband.

If attenuation is less than or equal to 0, the node returns 0 as well as an error.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Specifies the mixer to configure. Valid values are 
rx/atten1, 
rx/atten2, and 
tx.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced attenuation [dB]

Returns the actual attenuation, in dB.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

RF Front End Configuration Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-configure-clock-phase-dac.html language=enus -->
## TOPIC 00014: ni579x Configure Clock Phase DAC

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-configure-clock-phase-dac.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-configure-clock-phase-dac.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the value of the clock phase digital-to-analog converter (DAC) and modifies the phase of the reference used to generate the Sample Clock and LO if the reference frequency source is external. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-

ni579x Configure Clock Phase DAC

Configures the value of the clock phase digital-to-analog converter (DAC) and modifies the phase of the reference used to generate the Sample Clock and LO if the reference frequency source is external.

[IMAGE alt='1378' src='ni579x_Configure_Clock_Phase_DAC.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### clock phase DAC value

The value to set to the clock phase DAC.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Ignored.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### coerced clock phase DAC value

The coerced value programmed to the clock phase DAC.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Clocking Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-configure-clock.html language=enus -->
## TOPIC 00015: ni579x Configure Clock

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-configure-clock.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-configure-clock.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the source of the Sample Clock and the Reference Clock. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. clock source The source of the Sample Clock. Valid values: Internal–Internally-sourced Sample Clock. ClkIn–Sa

ni579x Configure Clock

Configures the source of the Sample Clock and the Reference Clock.

[IMAGE alt='1378' src='ni579x_Configure_Clock.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### clock source

The source of the Sample Clock.

Valid values:

- Internal –Internally-sourced Sample Clock.
- ClkIn –Sample Clock is sourced through the CLK IN front panel connector.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### reference clock source

The source of the clock that serves as a Reference Clock for the Sample Clock and local oscillator (LO).

Valid values:

- Internal –Reference Clock is internally sourced.
- PXI_CLK –Reference Clock is sourced through the PXI backplane.
- ClkIn –Reference Clock is sourced through the CLK IN front panel connector.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Mixer to configure. Valid values are 
rx and 
tx.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Clocking Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-configure-lo-enable.html language=enus -->
## TOPIC 00016: ni579x Configure LO Enable

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-configure-lo-enable.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-configure-lo-enable.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the internal LO and waits for LO Enable to complete. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. enable? Specifies whether to enable the internal local oscillator (LO). wait for enable completion? Specifies wheth

ni579x Configure LO Enable

Enables the internal LO and waits for LO Enable to complete.

[IMAGE alt='1378' src='ni579x_Configure_LO_Enable.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable?

Specifies whether to enable the internal local oscillator (LO).

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### wait for enable completion?

Specifies whether to wait for the LO Enable node to complete.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Mixer to configure. Valid values are 
rx and 
tx.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Clocking Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-configure-lo-filter.html language=enus -->
## TOPIC 00017: ni579x Configure LO Filter

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-configure-lo-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-configure-lo-filter.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the mixer LO input filter. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. frequency [Hz] Specifies the frequency the LO is tuned to for the measurement. error in Error conditions that occur before this node runs.

ni579x Configure LO Filter

Configures the mixer LO input filter.

[IMAGE alt='1378' src='ni579x_Configure_LO_Filter.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency [Hz]

Specifies the frequency the LO is tuned to for the measurement.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Mixer to configure. Valid values are 
rx and 
tx.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced frequency [Hz]

Actual frequency used to tune the LO.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Clocking Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-configure-lo-frequency.html language=enus -->
## TOPIC 00018: ni579x Configure LO Frequency

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-configure-lo-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-configure-lo-frequency.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency of the internal LO and returns the coerced frequency. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. frequency [Hz] Frequency to tune the LO. If you are using an external LO source, this parameter s

ni579x Configure LO Frequency

Configures the frequency of the internal LO and returns the coerced frequency.

[IMAGE alt='1378' src='ni579x_Configure_LO_Frequency.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency [Hz]

Frequency to tune the LO. If you are using an external LO source, this parameter specifies the frequency of the incoming LO.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Mixer to configure. Valid values are 
rx and 
tx.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced frequency [Hz]

Actual frequency used to tune the LO.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Clocking Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-configure-mixer.html language=enus -->
## TOPIC 00019: ni579x Configure Mixer

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-configure-mixer.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-configure-mixer.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the mixer (RF upconverter/downconverter) by enabling the LO, setting the LO frequency, configuring the LO filter, and making any necessary routes. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. frequency [Hz] Fre

ni579x Configure Mixer

Configures the mixer (RF upconverter/downconverter) by enabling the LO, setting the LO frequency, configuring the LO filter, and making any necessary routes.

[IMAGE alt='1378' src='ni579x_Configure_Mixer.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency [Hz]

Frequency to tune the LO. If you are using an external LO source, this parameter specifies the frequency of the incoming LO.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### LO source

Source of the local oscillator used by the specified mixer. Specify 
LO1 for the internal LO. Specify 
LO In to use an external LO source.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Mixer to configure. Valid values are 
rx and 
tx.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced frequency [Hz]

Actual frequency used to tune the LO.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-configure-output-power.html language=enus -->
## TOPIC 00020: ni579x Configure Output Power

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-configure-output-power.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-configure-output-power.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the specified output power. This node performs the following actions to configure the specified output power: Configures the Tx front end attenuators and filters. Returns the I/Q impairment correction data, which you can use to correct I/Q impairments. Returns the residual digital gain th

ni579x Configure Output Power

Configures the specified output power.

This node performs the following actions to configure the specified output power:

- Configures the Tx front end attenuators and filters.
- Returns the I/Q impairment correction data, which you can use to correct I/Q impairments.
- Returns the residual digital gain that you can apply to the signal to achieve the specified output power.
- Sets the RF filter to the specified frequency.

[IMAGE alt='1378' src='ni579x_Configure_Output_Power.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### output power [dBm]

Specifies the power, in dBm, at the output terminal of the device that corresponds to the full-scale range of the DAC binary data.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency [Hz]

Frequency to tune the LO. If you are using an external LO source, this parameter specifies the frequency of the incoming LO.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Mixer to configure. Valid values are 
rx and 
tx.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### characterization data

A set of data that describes the characteristics of this device that allow the node to calculate the proper attenuation and I/Q imbalance correction settings for the specified frequency. This data is stored in the EEPROM and can be retrieved using the ni579x Load Characterization Data (Single Channel) node. For the NI 5791, the Tx data is index 1 in the array of characterization data returned by the ni579x Load Characterization Data (Single Channel) node.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### correct IQ imbalance?

Specifies whether to calculate the I/Q impairment correction values. Set this parameter to FALSE if you are not using the I/Q impairment correction DSP blocks in the FPGA.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced output power [dBm]

The actual output power the device was configured to, not including any additional digital gain applied by the DSP block in the FPGA.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### digital gain

Applies residual digital gain values to the DSP Gain block in the FPGA.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### IQ impairment correction

The values to apply to the I/Q Impairment Correction DSP block in the FPGA, in order to correct gain and phase imbalances in the mixer.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-configure-reference-level.html language=enus -->
## TOPIC 00021: ni579x Configure Reference Level

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-configure-reference-level.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-configure-reference-level.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the specified reference level. This node performs the following actions to configure the specified reference level: Configures the Rx front end attenuators and filters. Returns the I/Q impairment correction data, which you can use to correct I/Q impairments. Returns the resulting vertical

ni579x Configure Reference Level

Configures the specified reference level.

This node performs the following actions to configure the specified reference level:

- Configures the Rx front end attenuators and filters.
- Returns the I/Q impairment correction data, which you can use to correct I/Q impairments.
- Returns the resulting vertical range that you can use to scale binary data retrieved from the device.
- Sets the RF filter to the specified frequency.

[IMAGE alt='1378' src='ni579x_Configure_Reference_Level.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### reference level [dBm]

Specifies the maximum power, in dBm, of the signals expected at the input terminal of the device. The RF signal path of the device is configured to maximize the dynamic range of the measurement relative to this power level.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### headroom [dB]

Specifies the amount of headroom to leave in the range of the ADC if the signal input to the device is at the reference level power. Leave enough headroom to avoid clipping or over range errors and DSP overflows.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency [Hz]

Specifies the frequency the LO is tuned to for the measurement.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Mixer to configure. Valid values are 
rx and 
tx.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### characterization data

A set of data that describes the characteristics of this device that allow the node to calculate the proper attenuation and I/Q imbalance correction settings for the specified frequency. This data is stored in the EEPROM and can be retrieved using the ni579x Load Characterization Data (Single Channel) node. For the NI 5791, the Tx data is index 1 in the array of characterization data returned by the ni579x Load Characterization Data (Single Channel) node.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### correct IQ imbalance?

Specifies whether to calculate the I/Q impairment correction values. Set this parameter to FALSE if you are not using the I/Q impairment correction DSP blocks in the FPGA.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced reference level [dBm]

The actual reference level the device is configured to. This value is the maximum power level that can be input to the device without exceeding the vertical range of the ADCs.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced vertical range [Vpp]

The peak-to-peak vertical range, in volts, of the device. You can use this value to scale binary data retrieved from the device to volts. This value assumes that the I/Q impairment correction values returned by this node are applied to the signal using the I/Q Impairment Correction DSP block in the FPGA.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### IQ impairment correction

The values to apply to the I/Q Impairment Correction DSP block in the FPGA, in order to correct gain and phase imbalances in the mixer.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-configure-rf-filter.html language=enus -->
## TOPIC 00022: ni579x Configure RF Filter

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-configure-rf-filter.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-configure-rf-filter.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RF filter frequency and returns the coerced frequency. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. frequency [Hz] Frequency to tune the LO. If you are using an external LO source, this parameter specifies

ni579x Configure RF Filter

Configures the RF filter frequency and returns the coerced frequency.

[IMAGE alt='1378' src='ni579x_Configure_RF_Filter.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### frequency [Hz]

Frequency to tune the LO. If you are using an external LO source, this parameter specifies the frequency of the incoming LO.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Mixer to configure. Valid values are 
rx and 
tx.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### coerced frequency [Hz]

Actual frequency used to tune the LO.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

RF Front End Configuration Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-fpga-self-synchronization.html language=enus -->
## TOPIC 00023: ni579x FPGA Self Synchronization

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-fpga-self-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-fpga-self-synchronization.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this synchronization method in conjunction with ni579x FPGA Align on the FPGA to synchronize the FPGAs. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error sync.cptr.peri

ni579x FPGA Self Synchronization

Use this synchronization method in conjunction with [ni579x FPGA Align](/csh?topicname=ni579x-fpga-align.html) on the FPGA to synchronize the FPGAs.

[IMAGE alt='1378' src='ni579x_FPGA_Self_Synchronization.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### sync.cptr.period

The period, in clocks, of the Common Periodic Time Reference (CPTR). The CPTR period controls the rate at which synchronized signals are realized. This parameter is required, and you must specify a value for each target to be synchronized.

ni579x FPGA Align

sync.cptr.period

sync.meas.Reference Clock

PXI_Clk10

IO Module\Sample Clock

(130 MHz / 10 MHz)

ni579x Host Align

63

sync.cptr.period

sync.cptr.FPGA I/O

50 ns

7

130 MHz

IO Module\Sample Clock

7.692 ns

7 clocks

50 ns

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-get-fam-clip-error.html language=enus -->
## TOPIC 00024: ni579x Get FAM CLIP Error

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-get-fam-clip-error.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-get-fam-clip-error.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns any FAM CLIP errors that exist. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standa

ni579x Get FAM CLIP Error

Returns any FAM CLIP errors that exist.

[IMAGE alt='1378' src='ni579x_Get_FAM_CLIP_Error.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-host-driven-synchronization.html language=enus -->
## TOPIC 00025: ni579x Host Driven Synchronization

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-host-driven-synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-host-driven-synchronization.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this synchronization method in conjunction with ni579x FPGA Aligns on the FPGA to synchronize the FPGAs. Refer to the FPGA nodes for documentation. Register Buses Specifies the Register Buses to which the Synchronization library is connected in the FPGA nodes. error in Error conditions that occu

ni579x Host Driven Synchronization

Use this synchronization method in conjunction with ni579x FPGA Aligns on the FPGA to synchronize the FPGAs.

Refer to the FPGA nodes for documentation.

[IMAGE alt='1378' src='ni579x_Host_Driven_Synchronization.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Buses

Specifies the Register Buses to which the Synchronization library is connected in the FPGA nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### sync.cptr.period

The period, in clocks, of the Common Periodic Time Reference (CPTR). The CPTR period controls the rate at which synchronized signals are realized. This parameter is required, and you must specify a value for each target to be synchronized.

ni579x FPGA Align

sync.cptr.period

sync.meas.Reference Clock

PXI_Clk10

IO Module\Sample Clock

(130 MHz / 10 MHz)

ni579x Host Align

63

sync.cptr.period

sync.cptr.FPGA I/O

50 ns

7

130 MHz

IO Module\Sample Clock

7.692 ns

7 clocks

50 ns

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Buses (out)

Passes the Register Buses to the next node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-load-char-data-single-channel.html language=enus -->
## TOPIC 00026: ni579x Load Characterization Data (Single Channel)

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-load-char-data-single-channel.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-load-char-data-single-channel.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads characterization data from the on-device EEPROM and returns headers and characterization data for the specified channel. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. start address The start offset of the data in the

ni579x Load Characterization Data (Single Channel)

Reads characterization data from the on-device EEPROM and returns headers and characterization data for the specified channel.

[IMAGE alt='1378' src='ni579x_Load_Characterization_Data_(Single_Channel).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### start address

The start offset of the data in the EEPROM.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### EEPROM Data Section

The EEPROM can contain characterization data measured and calculated by the manufacturer (Factory Data), as well as data measured and calculated by the user (User Data).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

The channel to read characterization data for. Valid values are 
rx and 
tx.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### EEPROM Header

Header information for the entire EEPROM.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### EEPROM Calibration Header

Header information describing the calibration sections.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### Device Data Header

Header information describing the device characterization data sections.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### Characterization Data

Characterization data for the specified channel.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

EEPROM Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-nodes.html language=enus -->
## TOPIC 00027: NI-579x Host API for LabVIEW NXG

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-nodes.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`

NI-579x Host API for LabVIEW NXG

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-open.html language=enus -->
## TOPIC 00028: ni579x Open

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-open.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-open.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session to the NI-579x Configuration nodes, creates a session to the Register Bus nodes, and initializes the CLIP. fpga ref A reference to LabVIEW FPGA created using the Open FPGA VI Reference node. re-initialize Specifies whether to re-initialize the adapter module CLIP (resets the device c

ni579x Open

Opens a session to the NI-579x Configuration nodes, creates a session to the Register Bus nodes, and initializes the CLIP.

[IMAGE alt='1378' src='ni579x_Open.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### fpga ref

A reference to LabVIEW FPGA created using the Open FPGA VI Reference node.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### re-initialize

Specifies whether to re-initialize the adapter module CLIP (resets the device configuration to its defaults).

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### bus instance

Specifies the bus used if creating multiple Register Buses to the same device.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-repeat-host-driven-sync.html language=enus -->
## TOPIC 00029: ni579x Repeat Host Driven Synchronization

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-repeat-host-driven-sync.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-repeat-host-driven-sync.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this synchronization method in conjunction with ni579x FPGA Align on the FPGA to synchronize the FPGAs. This synchronization method returns to a known synchronization state from a previous run. If the synchronization data in values are incorrect, the FPGAs are not synchronized. Synchronization d

ni579x Repeat Host Driven Synchronization

Use this synchronization method in conjunction with ni579x FPGA Align on the FPGA to synchronize the FPGAs.

This synchronization method returns to a known synchronization state from a previous run. If the synchronization data in values are incorrect, the FPGAs are not synchronized. Synchronization data is also only valid for a given system configuration. If FlexRIO FPGA modules, FlexRIO adapter modules, chassis, or slot locations change then synchronization data may not be valid.

[IMAGE alt='1378' src='ni579x_Repeat_Host_Driven_Synchronization.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### synchronization data in valid

A flag to use the values from a previous synchronization run (synchronization data in) to return the FPGAs to that synchronization state.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### synchronization data in

The synchronization data from a previous synchronization run that can be used to return the FPGAs to that synchronization state.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### sync.cptr.period

The period, in clocks, of the Common Periodic Time Reference (CPTR). The CPTR period controls the rate at which synchronized signals are realized. This parameter is required, and you must specify a value for each target to be synchronized.

ni579x FPGA Align

sync.cptr.period

sync.meas.Reference Clock

PXI_Clk10

IO Module\Sample Clock

(130 MHz / 10 MHz)

ni579x Host Align

63

sync.cptr.period

sync.cptr.FPGA I/O

50 ns

7

130 MHz

IO Module\Sample Clock

7.692 ns

7 clocks

50 ns

[IMAGE alt='datatype_icon' src='/assets/img/i1du16.png']

##### synchronization data out

Synchronization data from the completed synchronization run that can be used to return the FPGAs to that synchronization state.

The data is valid only if the FPGAs were successfully synchronized with no output error.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Synchronization Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-route-signal.html language=enus -->
## TOPIC 00030: ni579x Route Signal

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-route-signal.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-route-signal.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes a signal in the adapter module from the specified source to the specified destination terminal. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. destination The destination terminal. Valid values: Rx Mixer Input–The mo

ni579x Route Signal

Routes a signal in the adapter module from the specified source to the specified destination terminal.

[IMAGE alt='1378' src='ni579x_Route_Signal.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### destination

The destination terminal.

Valid values:

- Rx Mixer Input–The modulation signal input to the Rx mixer.
- Rx Mixer LO Input–The LO signal input to the Rx mixer.
- Tx Mixer LO Input–The LO signal input to the Tx mixer.
- Tx Out–The TX OUT front panel connector.
- LO Out–The LO OUT front panel connector.
- Clk Out–The CLK OUT front panel connector.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### source

The source signal.

Valid values:

- None–Disconnects route to destination.
- LO1–The local oscillator (LO).
- LO In–The LO IN front panel connector.
- RX In–The RX IN front panel connector.
- Tx Mixer Output–The output of the TX mixer.
- TX I (Mixer Bypass)–The I component of the baseband Tx signal, bypassing the Tx Mixer.
- Sample Clock–The signal used as the Sample Clock.
- Reference Clock–The signal used as the Reference Clock for the Sample Clock and the LO.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Configuration Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-send-fam-register-operations.html language=enus -->
## TOPIC 00031: ni579x Send FAM Register Operations

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-send-fam-register-operations.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-send-fam-register-operations.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the FAM register operations using the register bus. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. FAM Register Operations Use this node to address registers within a specific device. For example, to write to register

ni579x Send FAM Register Operations

Sends the FAM register operations using the register bus.

[IMAGE alt='1378' src='ni579x_Send_FAM_Register_Operations.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### FAM Register Operations

Use this node to address registers within a specific device.

For example, to write to register 0 × 25 on the ADC, set the Register Bus Address to 0×01000025.

FAM Register Offset specifies the register to be written to. Valid values:

- ADC
- DAC
- Clock Distribution Chip
- Frequency/Phase Adjust DAC
- EEPROM
- EEPROM Commands
- LO1
- Rx Atten Pre-LNA
- Rx Atten Post-LNA
- Tx Atten
- Other

Address– use the Address offsets to address registers within a specific device.

Write(T)/Read (F)– specify True to write to the register address, and specify False to read from the register address.

Write Data– specifies the number of times to write the data.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Ignored.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### FAM Register Read Data

Returns the FAM Register data.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-send-user-command.html language=enus -->
## TOPIC 00032: ni579x Send User Command

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-send-user-command.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-send-user-command.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends user commands using the register bus. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. User Command Refer to the following table for valid commands, arguments, and return values. User Setting User Command Value (U8) Use

ni579x Send User Command

Sends user commands using the register bus.

[IMAGE alt='1378' src='ni579x_Send_User_Command.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### User Command

| User Setting | User Command Value (U8) | User Data 0 Value (U16) | User Data 1 Value (U8) |
| --- | --- | --- | --- |
| Set Clock Select – Sets the Sample Clock to the specified setting. | 0 | 0 = Internal Sample Clock. 1 = Internal Sample Clock locked to an external Reference Clock through the CLK IN connector. 2 = External Sample Clock through the CLK IN connector. 3 = Internal Sample Clock locked to an external Reference Clock through the IoModSyncClock. | N/A |
| Set CLK OUT Source – Determines the CLK OUT output. | 1 | 0 = disabled 1 = Reference Clock 2 = Sample Clock | N/A |
| DAC Sync User Start – Sets up the DAC to receive a user supplied SYNC pulse. After this command returns, send a rising edge on the Synchronize DAC CLIP signal to send a SYNC pulse to the DAC, then send CmdDacSyncUserEnd. Refer to the DAC datasheet for the use of the SYNC signal. | 2 | N/A | N/A |
| DAC Sync User End – Finalizes DAC synchronization and checks for errors. | 3 | N/A | N/A |
| Set Tx Attenuation – Sets the Tx Programmable Attenuator to the attenuation specified in UserData0. | 9 | Attenuation (.25 dB per LSB, max 31.75 dB or 0x7F) | N/A |
| Set LO Filter – Configures the Tx LO filter path. | 32 | Non-zero = Tx LO | Byte setting. Refer to the following list for cut-off frequencies for each byte. 0xF1 : 316 MHz0xEC : 474 MHz0xE9 : 711 MHz0xD6 : 1,066 MHz0xD3 : 1,600 MHz0xCE : 2,400 MHz0xCB : 3,600 MHz0xF : >3,600 MHz |
| Set Front End Filter – Configures the Tx front end filters. | 33 | Non-zero = Tx | Byte setting. Refer to the following list for cut-off frequencies for each byte. 0x00 : <3,600 MHz0x01 : <2,400 MHz0x02 : <1,600 MHz0x03 : <1,066 MHz0x04 : <711 MHz0x05 : <474 MHz0x06 : <316 MHz0x07 : >3,600 MHz |
| Set LO Power – Turns the LO and the LO power supply on and off. | 34 | 0 = LO | 0 = off Non-zero = on |
| Set Routing Mux – Configures all the multiplexers that control LO paths and signal paths (not including filters). Each mux is either 2:1 or 1:2, so there are only two options for UserData1 per mux. | 37 | Refer to the Mux Select Enumeration table. | 0 = off/default Non-zero = on Refer to the Mux Select Enumeration table for details. |
| Read Revision Lower – Reads the lower two bytes of the CLIP Revision. | 240 | N/A | N/A |
| Read Revision Upper - Reads the upper two bytes of the CLIP Revision | 241 | N/A | N/A |
| Read Oldest Compatible Revision Lower - Reads the lower two bytes of the oldest compatible revision of the CLIP. | 242 | N/A | N/A |
| Read Oldest Compatible Version Upper - Reads the upper two bytes of the oldest compatible revision of the CLIP. | 243 | N/A | N/A |
| Reinitialize - Reinitializes the module and CLIP. The CLIP pulls the Initialization Done signal low before acquiring the Reinitialize command. Wait for the Initialization Done signal to go high before proceeding. | 255 | Refer to the Mux Select Enumeration table. | 0 = off/default Non-zero = on Refer to the Mux Select Enumeration table for details. |

| Value | Name | Setting |
| --- | --- | --- |
| 0 | LoSource | 0 = Internal LO Non-zero = External LO |
| 2 | LoOut | 0 = LO Out off Non-zero = LO Out on |
| 3 | TxModBypass | 0 = Tx modulator bypass disable Non-zero = Tx modulator bypass enable |

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout

Specifies the amount of time that the node waits, in ms, for the operation to complete.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Ignored.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### wait for completion?

Specifies whether to wait for the node to complete.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### read return values?

Specifies whether to read return values from the user return value parameter.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### user command status

Indicates whether the previous command completed successfully.

0 = successful

Nonzero = unsuccessful

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### user return value

Returns data configured by the 
User Command signal.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### user command error

Indicates that an error occurred and that you must reinitialize the device .

0 = no error

Nonzero = error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-store-char-data-eeprom.html language=enus -->
## TOPIC 00033: ni579x Store Characterization Data (EEPROM)

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-store-char-data-eeprom.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-store-char-data-eeprom.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores headers and per-channel characterization data in the on-device EEPROM. This node erases existing data in the EEPROM. Contact National Instruments before using this node. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

ni579x Store Characterization Data (EEPROM)

Stores headers and per-channel characterization data in the on-device EEPROM.

Notice

[IMAGE alt='1378' src='ni579x_Store_Characterization_Data_(EEPROM).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### EEPROM Calibration Header

Header information describing the calibration sections.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### Device Data Header

Header information describing the device characterization data sections.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### Characterization Data

Characterization data for the specified channel.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

The EEPROM to read characterization data from. The only valid value is 
characterization data eeprom.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### EEPROM Header

Header information for the entire EEPROM.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### start address

The start offset of the data in the EEPROM.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### EEPROM Data Section

The EEPROM can contain characterization data measured and calculated by the manufacturer (Factory Data), as well as data measured and calculated by the user (User Data).

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

EEPROM Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-wait-for-initialization.html language=enus -->
## TOPIC 00034: ni579x Wait for Initialization

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-wait-for-initialization.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-wait-for-initialization.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the IO Module initialization to complete with the specified timeout. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. timeout [s] Specifies how long to wait, in seconds. error in Error conditions that occur before t

ni579x Wait for Initialization

Waits for the IO Module initialization to complete with the specified timeout.

[IMAGE alt='1378' src='ni579x_Wait_for_Initialization.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout [s]

Specifies how long to wait, in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Utility Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=ni579x-wait-for-lock.html language=enus -->
## TOPIC 00035: ni579x Wait for Lock

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `ni579x-wait-for-lock.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/ni579x-wait-for-lock.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified circuit to complete its configuration and report a successful lock to the supplied reference. Register Bus Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes. timeout [s] Specifies how long to wait, in seconds. error

ni579x Wait for Lock

Waits for the specified circuit to complete its configuration and report a successful lock to the supplied reference.

[IMAGE alt='1378' src='ni579x_Wait_for_Lock.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### Register Bus

Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### timeout [s]

Specifies how long to wait, in seconds.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### scope

Specifies the circuit to wait for. Valid values are 
PLL for the Reference Clock circuit and 
LO1 for the local oscillator (LO).

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### Register Bus (out)

The Register Bus object created by ni579x Open and used as the session handle for the NI-579x Configuration nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Clocking Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=rf-and-front-end-config-nodes.html language=enus -->
## TOPIC 00036: RF Front End Configuration Nodes

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `rf-and-front-end-config-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/rf-and-front-end-config-nodes.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`

RF Front End Configuration Nodes

ni579x Configure Attenuation

Configures the attenuation level and returns the coerced attenuation level.

ni579x Configure RF Filter

Configures the RF filter frequency and returns the coerced frequency.

ni579x Configure Amplifier

scope

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=synchronization-nodes.html language=enus -->
## TOPIC 00037: Synchronization Nodes

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `synchronization-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/synchronization-nodes.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`

Synchronization Nodes

ni579x Host Driven Synchronization

Use this synchronization method in conjunction with ni579x FPGA Aligns on the FPGA to synchronize the FPGAs.

ni579x Repeat Host Driven Synchronization

Use this synchronization method in conjunction with ni579x FPGA Align on the FPGA to synchronize the FPGAs.

ni579x FPGA Self Synchronization

ni579x FPGA Align

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=to-byte-array-f32.html language=enus -->
## TOPIC 00038: To Byte Array (F32)

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `to-byte-array-f32.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/to-byte-array-f32.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an input F32 data type to a byte array. element in (0) The data type to convert. byte array out The converted byte array.

To Byte Array (F32)

Converts an input F32 data type to a byte array.

[IMAGE alt='1378' src='To_Byte_Array_(F32).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### element in (0)

The data type to convert.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### byte array out

The converted byte array.

Parent topic:

To Byte Array

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=to-byte-array-lv-timestamp.html language=enus -->
## TOPIC 00039: To Byte Array (LV Timestamp)

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `to-byte-array-lv-timestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/to-byte-array-lv-timestamp.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an LV Timestamp data type to a byte array. element in (0) The data type to convert. byte array out The converted byte array.

To Byte Array (LV Timestamp)

Converts an LV Timestamp data type to a byte array.

[IMAGE alt='1378' src='To_Byte_Array_(LV_Timestamp).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### element in (0)

The data type to convert.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### byte array out

The converted byte array.

Parent topic:

To Byte Array

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=to-byte-array-u16.html language=enus -->
## TOPIC 00040: To Byte Array (U16)

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `to-byte-array-u16.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/to-byte-array-u16.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an input U16 data type to a byte array. element in (0) The data type to convert. byte array out The converted byte array.

To Byte Array (U16)

Converts an input U16 data type to a byte array.

[IMAGE alt='1378' src='To_Byte_Array_(U16).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### element in (0)

The data type to convert.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### byte array out

The converted byte array.

Parent topic:

To Byte Array

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=to-byte-array-u32.html language=enus -->
## TOPIC 00041: To Byte Array (U32)

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `to-byte-array-u32.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/to-byte-array-u32.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an input U32 data type to a byte array. element in (0) The data type to convert. byte array out The converted byte array.

To Byte Array (U32)

Converts an input U32 data type to a byte array.

[IMAGE alt='1378' src='To_Byte_Array_(U32).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### element in (0)

The data type to convert.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### byte array out

The converted byte array.

Parent topic:

To Byte Array

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=to-byte-array-u8.html language=enus -->
## TOPIC 00042: To Byte Array (U8)

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `to-byte-array-u8.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/to-byte-array-u8.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an input U8 data type to a byte array. element in (0) The data type to convert. byte array out The converted byte array.

To Byte Array (U8)

Converts an input U8 data type to a byte array.

[IMAGE alt='1378' src='To_Byte_Array_(U8).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu8.png']

##### element in (0)

The data type to convert.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### byte array out

The converted byte array.

Parent topic:

To Byte Array

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=to-byte-array.html language=enus -->
## TOPIC 00043: To Byte Array

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `to-byte-array.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/to-byte-array.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an input data type to a byte array.

To Byte Array

Converts an input data type to a byte array.

Conversions Nodes

To Byte Array (F32)

Converts an input F32 data type to a byte array.

To Byte Array (LV Timestamp)

Converts an LV Timestamp data type to a byte array.

To Byte Array (U8)

Converts an input U8 data type to a byte array.

To Byte Array (U16)

Converts an input U16 data type to a byte array.

To Byte Array (U32)

Converts an input U32 data type to a byte array.

Parent topic:

Conversions Nodes

<!--NI_TOPIC bundle=ni-579x-lvnxg-host-api-ref path=utility-nodes.html language=enus -->
## TOPIC 00044: Utility Nodes

- bundle_id: `ni-579x-lvnxg-host-api-ref`
- source_path: `utility-nodes.html`
- source_url: https://docs-be.ni.com/bundle/ni-579x-lvnxg-host-api-ref/raw/resource/enus/utility-nodes.html
- document_id: `ni-579x-lvnxg-host-api-ref`
- page_type: `leaf`
- content_type: `reference`

Utility Nodes

ni579x Get FAM CLIP Error

Returns any FAM CLIP errors that exist.

ni579x Send FAM Register Operations

Sends the FAM register operations using the register bus.

ni579x Send User Command

Sends user commands using the register bus.

ni579x Wait for Initialization

Waits for the IO Module initialization to complete with the specified timeout.
