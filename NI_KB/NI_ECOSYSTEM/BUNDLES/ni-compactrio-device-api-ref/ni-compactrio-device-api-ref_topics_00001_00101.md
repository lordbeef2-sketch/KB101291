# NI DOCUMENT BUNDLE: ni-compactrio-device-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-compactrio-device-api-ref start=1 end=101 -->
<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=946x/9469_Errors.html language=enus -->
## TOPIC 00001: NI 9469 Module Error Codes

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `946x/9469_Errors.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/946x/9469_Errors.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: 30 Error Code Name Condition Accessible From d65642 The trigger could not be sent. Make sure that None (Input) is selected as the line source of the trigger and that it is not configured to carry a clock or another module's trigger. Sending a trigger when source of the trigger line is different than

### NI 9469 Module Error Codes

| Error Code | Name | Condition | Accessible From |
| --- | --- | --- | --- |
| d65642 | The trigger could not be sent. Make sure that None (Input) is selected as the line source of the trigger and that it is not configured to carry a clock or another module's trigger. | Sending a trigger when source of the trigger line is different than None (Input). | Send Trigger method |
| d65643 | The Wait On Trigger method cannot execute on a trigger line configured to carry a clock. Select another trigger line or change the clock routing configuration in the C Series Module Properties dialog box. | Waiting for a trigger in Trigger 3 when it is used to import/export the oversample clock. | Wait On Trigger method |
| d65644 | Port line direction change failed because the maximum number of port lines are configured for output on the module. Refer to the module help documentation for the maximum number of simultaneous port line outputs. | Having more than 8 outputs. | Set Line Source method |
| d65645 | The specified line does not support the selected source. Refer to the module help documentation for a list of valid sources for each line. | Setting an invalid source for a line (eg Port0/Line0 to Port1/Line2). As a general rule, only lines with the same number of lines and different ports can be connected between each other, also the clock can only be connected to the third line of each port. | Set Line Source method |
| d65646 | The specified line is not configured to import a clock or it is already configured as the source of another line. | Setting an output line as the Clock Source. The Clock Source can be either the internal oscillator, or an input line (Trigger when importing from another module, or one of the port lines when importing from another NI 9469 in another chassis). Also, if the line is set to be the source of another line when trying to make it the Clock Source | Set Clock Source method/Set Line Source method |
| d65647 | The configuration of the specified line cannot be changed because it is configured to carry a clock or a trigger. | Changing the configuration of a line when it is used to carry the clock, either from the chassis or from an external source. For Trigger 3, the carrier FPGA routing is meant to support only the configuration specified in the Configuration sub panel page and it is not allowed to modify it in run time. It is not allowed to have triggers routed through a trigger configured to carry the Clock. For the lines importing the clock from an external source, once that line 3 is configured to be the Clock Source, it cannot be modified to be connected to any other line. In order to change this it is required to change the Clock Source to be another line. | Set Line Source method |
| d65648 | The specified line does not support the selected source because the source is configured to carry a clock. To export the clock carried on the selected source, set the source of the specified line to be the clock. | It is not allowed to connect the Trigger 3, when it is configured to carry the oversample clock, or the current Clock Source directly to a port line. | Set Line Source method |
| d65651 | The source of the specified trigger cannot be set to clock since it is not configured to export the clock. Change the clock routing configuration in the C Series Module Properties dialog box in order to output the clock from the specified trigger. | If Trigger 3 is not configured to carry the Clock from the Configuration sub panel, it cannot be changed during run time. | Set Line Source method |
| d65649 (Warning) | The module did not export the generated trigger because this trigger line is not configured as the source for any of the port lines. | If there is no other line connected to the trigger line, it will not be exported outside the module, however this trigger can be read back with the Wait On Trigger method for the same trigger line. | Send Trigger method |
| d65672 | The specified timebase frequency cannot be selected. Verify that all the modules importing this timebase support the specified frequency. | Trying to set the internal timebase frequency to a value not supported by any slave module of the 9469. | Set Internal Timebase Frequency |

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=946x/9469_Propertiesdialog.html language=enus -->
## TOPIC 00002: C Series Module Properties Dialog Box for the NI 9469

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `946x/9469_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/946x/9469_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Delta-Sigma Synchronization Module Right-click the NI 9469 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to fully configure the NI 9469. This dialog box includes the following components: Name—Specifies the

### C Series Module Properties Dialog Box for the NI 9469

Delta-Sigma Synchronization Module

Right-click the [NI 9469](https://ni.com/docs/en-US/csh?context=ni-compactrio_946x_crio-9469) C Series module in the
 Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to fully configure the NI 9469.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Configuration —Sets the NI 9469 routing inside the module.
 Depending on the configuration, different options are made available.
  - Master Configuration —This configuration sets the
 NI 9469 to Master Mode. This makes the triggers inputs of the module
 (Setting them to send triggers through them), Port 1 and Port 2 will be
 connected to the triggers and Port 0 will not be connected. The options
 for the Master Configuration are:
    - Export Clock —Specifies whether or not the
 NI 9469 is going to Export the Clock to other modules in the
 same chassis and to other chassis. When this option is set, only
 Line 3 of Port 1, Port 2 and trigger will export the Clock
 Source. The Clock Source will be set to the Internal
 Timebase.
    - Exported Clock Frequency —Specifies the
 frequency of the Internal Timebase on the NI 9469.
  - Slave Configuration —This configuration sets the
 NI 9469 to Slave Mode. This means that the triggers will be outputs of
 the module (Setting them to receive triggers from another NI 9469); Port
 1, Port 2 and the triggers will be connected to Port 0. The options for
 the Slave Configuration are:
    - Import Clock —Specifies whether or not the
 NI 9469 is going to Import the Clock from another NI 9469
 through the Port 0/Line 3. When this option is set, only Line 3
 of Port 1, Port 2 and trigger will export the Clock Source. The
 Clock Source will be set to be the Port 0/Line 3.
    - Imported Clock Frequency —Specifies the
 frequency of the Imported Clock. Note that this frequency will
 also set the Internal Timebase Frequency if the Clock Source is
 changed to be the Internal Timebase in Run Time.
  - Custom Configuration —Click the Set
 Custom Configuration button to open the
 Custom Configuration dialog box. This dialog
 box allows full configuration of the NI 9469. Refer to the Custom
 Configuration dialog box for more information.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=946x/9469_Propertiesdialog_customconfig.html language=enus -->
## TOPIC 00003: Custom Configuration Dialog Box for the NI 9469

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `946x/9469_Propertiesdialog_customconfig.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/946x/9469_Propertiesdialog_customconfig.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Delta-Sigma Synchronization Module Right-click the NI 9469 C Series module in the Project Explorer window and select Custom Configuration from the shortcut menu to display this dialog box. This dialog box allows the full configuration of the NI 9469. This dialog box includes the following components

### Custom Configuration Dialog Box for the NI 9469

Delta-Sigma Synchronization Module

Right-click the [NI 9469](https://ni.com/docs/en-US/csh?context=ni-compactrio_946x_crio-9469) C Series module in the
 Project Explorer window and select Custom
 Configuration from the shortcut menu to display this dialog box.

This dialog box allows the full configuration of the NI 9469.

This
 dialog box includes the following components:

- Custom Configuration —Click the Set Custom
 Configuration button to open the Custom
 Configuration dialog box. This dialog box allows full
 configuration of the NI 9469:
  - Source —Specifies the valid configuration of each
 line of the NI 9469 (Port0/Line0, Port0/Line1, Port0/Line2, Port0/Line3,
 Port1/Line0, Port1/Line1, Port1/Line2, Port1/Line3, Port2/Line0,
 Port2/Line1, Port2/Line2, Port2/Line3, Trig0, Trig1, Trig2, Trig3).
 None (Input) means the specified line will be
 receiving the trigger or clock from another module (or from the Send
 Trigger method for the trigger lines); Clock means the specified line
 will be exporting the Clock Source. If a line is not going to be used,
 set it to None (Input) . Modules set to export
 their Reference Trigger will be listed as source options for Trig0,
 Trig1, Trig2, and Trig3. Select a module to set the trigger lines as
 slaves of that module.
  - Clock Source —Specifies the Clock Source of the NI
 9469, it could come from another NI 9469 through the Port0/Line3,
 Port1/Line3 or Port2/Line3; from the Internal Timebase of the NI 9469 or
 from another module in the same chassis when that module is set to
 export its Internal Timebase.
  - Internal Timebase Frequency —When Internal
 Timebase is selected as the Clock Source, it specifies the frequency
 that the NI 9469 will generate.
  - Imported Clock Frequency —When Port0/Line3,
 Port1/Line3 or Port2/Line3 are selected as the Clock Source, it
 specifies the Imported Frequency from another NI 9469. This information
 is not obtained automatically from the other NI 9469, so the correct
 frequency must be set depending on the other NI 9469 Exported Frequency.
 When another module on the same chassis is selected as the Clock Source,
 it specifies the Imported Frequency, this will be detected
 automatically.
  - Set to Master Configuration —This button resets
 the configuration of the NI 9469 to Master Configuration from the
 C Series Module Properties dialog box.
  - Set to Slave Configuration —This button resets the
 configuration of the NI 9469 to Slave Configuration from the
 C Series Module Properties dialog box.
  - Clear Configuration —This button resets the
 configuration of the NI 9469 so all the lines will be set to
 None (Input) . This configuration will not
 make any connections, however it is useful to create a configuration
 from the start.

Parent topic:

C Series Module Properties Dialog Box for the NI 9469

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9201_Propertiesdialog.html language=enus -->
## TOPIC 00004: C Series Module Properties Dialog Box for the NI 9201/9221 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9201_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9201_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9201 or NI 9221 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series mod

### C Series Module Properties Dialog Box for the NI 9201/9221 (FPGA Interface)

Right-click an [NI 9201](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9201) or [NI 9221](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9221) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is signed, with a word length of 16 bits and an integer
 word length of 5 bits for the NI 9201 and 7 bits for the NI 9221. Select
 Raw if you want the FPGA I/O Node to return
 uncalibrated, binary data from the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Minimum Time Between Conversions —Specifies the minimum time between conversions in µs.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9202_Propertiesdialog.html language=enus -->
## TOPIC 00005: C Series Module Properties Dialog Box for the NI 9202 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9202_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9202_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9202 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9202 (FPGA Interface)

Right-click an [NI 9202](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9202) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Type —Specifies the type of C Series module. You cannot
 change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module. The fixed-point
 data is signed, with 24-bits word length and 4-bits integer word length. Select
 Raw if you want the FPGA I/O Node to return
 calibrated, binary data from the module. If you select
 Raw , you must convert the binary data to the actual analog input values in the host VI.
 In Raw mode, you also need to apply some gain correction
 constants for some data rates. The default is
 Calibrated .
- Master Timebase Source —Specifies the master timebase source that the module uses.
- Export Onboard Clock —Place a checkmark in this checkbox
 if you want to make this module accessible as a master timebase source to other
 modules.
- Data Rate —Specifies the rate at which the module acquires
 data.
- Filter Frequency Config —Sets the frequency of the first
 notch in the filter response. Setting changes apply to all channels. Available
 values:
  - Data Rate/1
  - Data Rate/2
  - Data Rate/4
  - Data Rate/8
  - Data Rate/16

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9203_Propertiesdialog.html language=enus -->
## TOPIC 00006: C Series Module Properties Dialog Box for the NI 9203 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9203_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9203_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9203 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9203 (FPGA Interface)

Right-click an [NI 9203](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9203) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of amps.
 The fixed-point data is signed, with a word length of 21 bits and an integer
 word length of –4 bits. Select Raw if you want the FPGA
 I/O Node to return uncalibrated, binary data from the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Minimum Time Between Conversions —Specifies the minimum
 time between conversions in µs.
- Channel Configuration —Specifies the input range for each
 channel.
  - Channels —Specifies the channel(s) for which you
 want to select the input range.
  - Input Range —Specifies the input range for the
 selected channel(s) as either 0–20 mA or ±20 mA.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9205_Propertiesdialog.html language=enus -->
## TOPIC 00007: C Series Module Properties Dialog Box for the NI 9204/9205/9206 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9205_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9205_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9204, NI 9205, or NI 9206 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C

### C Series Module Properties Dialog Box for the NI 9204/9205/9206 (FPGA Interface)

Right-click an [NI 9204](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9204), [NI 9205](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9205), or [NI 9206](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9206) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is signed, with a word length of 26 bits and an integer
 word length of 5 bits. Select Raw if you want the FPGA
 I/O Node to return uncalibrated, binary data from the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Channel Configuration —Specifies the input range for each
 channel.
  - Channels —Specifies the channel(s) for which you
 want to select the input range.
  - Input Range —Specifies the input range for the
 selected channel(s) as ±10 V, ±5 V, ±1 V, or ±200 mV.
  - Terminal Mode —Specifies the terminal mode for the
 selected channel(s) as RSE (referenced single-ended), NRSE
 (non-referenced single-ended ), or DIFF (differential).
- Minimum Time Between Conversions —Specifies the minimum time between conversions 
 in µs.
- Enable Advanced Self-Calibration Nodes —Place a checkmark
 in this checkbox if you want to enable Self-Calibration support in the FPGA for this module.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9207_Propertiesdialog.html language=enus -->
## TOPIC 00008: C Series Module Properties Dialog Box for the NI 9207 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9207_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9207_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9207 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9207 (FPGA Interface)

Right-click an [NI 9207](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9207) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module. Refer to the table
 below for information about the units and encoding of the fixed-point data
 depending on the channel type. Select Raw if you want the
 FPGA I/O Node to return calibrated, binary data from the module. If you select
 Raw , you must convert the binary values to engineering units. The default is
 Calibrated . Table 4.Channel TypeUnits of Fixed-Point DataInteger TypeWord LengthInteger Word LengthVoltageVoltsSigned24 bits5 bitsCurrentAmpsSigned24 bits–4 bits
- Conversion Time —Specifies the time it takes to acquire
 one point of data from one or more channels in a single FPGA I/O Node. You can
 select High Speed or High
 Resolution . The default is High
 Resolution . Refer to the NI 9207 hardware documentation on
 ni.com/manuals for more information about the High Speed 
 and High Resolution conversion times.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9208_Propertiesdialog.html language=enus -->
## TOPIC 00009: C Series Module Properties Dialog Box for the NI 9208 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9208_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9208_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9208 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9208 (FPGA Interface)

Right-click an [NI 9208](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9208) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of amps.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of –4 bits. Select Raw if you want the FPGA
 I/O Node to return calibrated, binary data from the module. If you select
 Raw , you must convert the binary current values to amps. The default is
 Calibrated .
- Conversion Time —Specifies the time it takes to acquire
 one point of data from one or more channels in a single FPGA I/O Node. You can
 select High Speed or High
 Resolution . The default is High
 Resolution . Refer to the NI 9208 hardware documentation on
 ni.com/manuals for more information about the High Speed 
 and High Resolution conversion times.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9209_Propertiesdialog.html language=enus -->
## TOPIC 00010: C Series Module Properties Dialog Box for the NI 9209 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9209_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9209_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9209 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9209 (FPGA Interface)

Right-click an [NI 9209](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9209) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated fixed-point data from the module in units of volts.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of 5 bits. Select Raw if you want the FPGA
 I/O Node to return calibrated, binary data from the module. If you select
 Raw , you must convert the binary current values to amps. The default is Calibrated .
- Conversion Time —Specifies the time it takes to acquire
 one point of data from one or more channels in a single FPGA I/O Node. You can
 select High Speed or High
 Resolution . The default is High
 Resolution . Refer to the NI 9209 hardware documentation on
 ni.com/manuals for more information about the High Speed 
 and High Resolution conversion times.
- Channels —Specifies which channels you want to configure
 settings for.
- Terminal Mode —Specifies the terminal mode for the
 selected channels as RSE (referenced single-ended) or DIFF (differential).

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9210_Propertiesdialog.html language=enus -->
## TOPIC 00011: C Series Module Properties Dialog Box for the NI 9210 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9210_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9210_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9210 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9210 (FPGA Interface)

Right-click an [NI 9210](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9210) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of –2 bits. If you select Calibrated , you
 must convert the fixed-point CJC data to binary CJC data and then convert the
 binary CJC data to temperature. Select Raw if you want
 the FPGA I/O Node to return calibrated, binary data from the module. If you
 select Raw , you must convert the binary thermocouple values to voltage and convert the binary
 CJC data to temperature. The default is Calibrated .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9211_Propertiesdialog.html language=enus -->
## TOPIC 00012: C Series Module Properties Dialog Box for the NI 9211 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9211_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9211_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9211 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9211 (FPGA Interface)

Right-click an [NI 9211](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9211) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of –2 bits. If you select Calibrated , you
 must convert the fixed-point CJC data to binary CJC data and then convert the
 binary CJC data to temperature. Select Raw if you want
 the FPGA I/O Node to return calibrated, binary data from the module. If you
 select Raw , you must convert the binary thermocouple values to voltage and convert the binary
 CJC data to temperature. The default is Calibrated .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9212_Propertiesdialog.html language=enus -->
## TOPIC 00013: C Series Module Properties Dialog Box for the NI 9212 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9212_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9212_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9212 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9212 (FPGA Interface)

Right-click an [NI 9212](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9212) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of –2 bits. If you select Calibrated , you
 must convert 
 the CJC data from voltage to temperature. Select Raw if
 you want the FPGA I/O Node to return calibrated, binary data from the module. If
 you select Raw , you must convert 
 the binary thermocouple and CJC values to voltage and then convert the CJC data
 from voltage to temperature. The default is
 Calibrated .
- Conversion Time —Specifies the time it takes to acquire
 one point of data from one or more channels in a single FPGA I/O Node. You can
 select High Speed , Best 60 Hz
 Rejection , Best 50 Hz Rejection , or
 High Resolution . The default is High
 Resolution . Refer to the NI 9212 with NI TB-9212
 Datasheet for more information about the High
 Speed , Best 60 Hz Rejection ,
 Best 50 Hz Rejection , and High
 Resolution conversion times.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9213_Propertiesdialog.html language=enus -->
## TOPIC 00014: C Series Module Properties Dialog Box for the NI 9213 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9213_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9213_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9213 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9213 (FPGA Interface)

Right-click an [NI 9213](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9213) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of –2 bits. If you select Calibrated , you
 must convert 
 the CJC data from voltage to temperature. Select Raw if
 you want the FPGA I/O Node to return calibrated, binary data from the module. If
 you select Raw , you must convert 
 the binary thermocouple and CJC values to voltage and then convert the CJC data
 from voltage to temperature. The default is
 Calibrated .
- Conversion Time —Specifies the time it takes to acquire
 one point of data from one or more channels in a single FPGA I/O Node. You can
 select High Speed or High
 Resolution . The default is High
 Resolution . Refer to the NI 9213 hardware documentation on
 ni.com/manuals for more information about the High Speed 
 and High Resolution conversion times.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9214_Propertiesdialog.html language=enus -->
## TOPIC 00015: C Series Module Properties Dialog Box for the NI 9214 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9214_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9214_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9214 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9214 (FPGA Interface)

Right-click an [NI 9214](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9214) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return
 calibrated,
 fixed-point
 data from the module in units of volts. The fixed-point data is signed, with a
 word length of 24 bits and an integer word length of –2 bits. If you select
 Calibrated , you must convert 
 the CJC data from voltage to temperature. Select Raw if
 you want the FPGA I/O Node to return calibrated, binary data from the module. If
 you select Raw , you must convert 
 the binary thermocouple and CJC values to voltage and then convert the CJC data
 from voltage to temperature. The default is
 Calibrated .
- Conversion Time —Specifies the time it takes to acquire
 one point of data from one or more channels in a single FPGA I/O Node. You can
 select High Speed or High
 Resolution . The default is High
 Resolution . Refer to the NI 9214 with NI TB-9214
 Operating Instructions and Specifications for more information
 about the High Speed and High
 Resolution conversion times.
- Enable Open Thermocouple Detection —Place a checkmark in
 this checkbox if you want to enable open
 thermocouple detection on the
 module. Note Enabling open thermocouple detection on the NI 9214
 results in a small current leakage in the thermocouple measurement. Refer to
 the Overview of Open Thermocouple
 Detection
 support document for more information about compensating for this error.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9215_Propertiesdialog.html language=enus -->
## TOPIC 00016: C Series Module Properties Dialog Box for the NI 9215 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9215_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9215_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9215 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9215 (FPGA Interface)

Right-click an [NI 9215](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9215) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data for the module in units of volts.
 The fixed-point data is signed, with a word length of 20 bits and an integer
 word length of 5 bits. Select Raw if you want the FPGA
 I/O Node to return uncalibrated, binary data for the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9216_Propertiesdialog.html language=enus -->
## TOPIC 00017: C Series Module Properties Dialog Box for the NI 9216 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9216_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9216_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9216 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9216 (FPGA Interface)

Right-click an [NI 9216](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9216) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of ohms.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of 10 bits. Select Raw if you want the FPGA
 I/O Node to return uncalibrated, binary data from the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Conversion Time —Specifies the time it takes to acquire
 one point of data from all channels. You can select 200
 ms or 2.5 ms .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9217_Propertiesdialog.html language=enus -->
## TOPIC 00018: C Series Module Properties Dialog Box for the NI 9217 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9217_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9217_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9217 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9217 (FPGA Interface)

Right-click an [NI 9217](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9217) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of ohms.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of 10 bits. Select Raw if you want the FPGA
 I/O Node to return uncalibrated, binary data from the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Conversion Time —Specifies the time it takes to acquire
 one point of data from all channels. You can select 200
 ms or 2.5 ms .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9218_Propertiesdialog.html language=enus -->
## TOPIC 00019: C Series Module Properties Dialog Box for the NI 9218 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9218_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9218_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9218 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9218 (FPGA Interface)

Right-click an [NI 9218](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9218) C Series module in the
 Project Explorer window and select
 Properties from the shortcut menu to display this dialog box.

Use this dialog box to configure a C Series module.

This dialog box includes
 the following components:

- Name —Specifies the name of the C Series module, which appears in
 the Project Explorer window. LabVIEW assigns a default name to the
 module based on the slot number. You can use this field to give the module a descriptive
 name.
- Type —Specifies the type of C Series module. You cannot change
 this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C Series
 module. Select Calibrated if you want the FPGA I/O
 Node to return
 calibrated,
 fixed-point data
 from the module. Refer to the table below for information about the units and encoding of
 the fixed-point data depending on the channel mode. Select Raw if
 you want the FPGA I/O Node to return calibrated, binary data from the module. If you
 select Raw , you must convert the analog input values in the host VI. The default is
 Calibrated . Table 5.Channel ModeUnits of Fixed-Point DataInteger TypeWord LengthInteger Word LengthTypical Measurement Range±16 VVoltsSigned35 bits7 bits±16.3 V±20 mAAmpsSigned35 bits7 bits24.4 mA±22 mV/V BridgeVolts/voltSigned35 bits7 bits22.1 mV/V±5 V IEPEVoltsSigned35 bits7 bits5.33 V±60 VVoltsSigned35 bits7 bits±62.1 V±65 mVVoltsSigned35 bits7 bits73.5 mV
- Data Rate —Specifies the rate at which the module acquires
 data.
- Enable TEDS Support —Place a checkmark in this checkbox if you
 want to enable TEDS support in the FPGA and host VIs
 for this module.
- Channels —Specifies the channel(s) for which you want to select
 the mode and range.
- Master Timebase Source —Specifies the master timebase source that the
 module uses.
- Export Onboard Clock —Place a checkmark in this checkbox if you
 want to make this module accessible as a master timebase source to other modules.
- Selected Channel(s) Settings —Specifies the mode and range for
 each channel. Note The following channel modes require a connection accessory. Table 6.Channel ModeConnection Accessory±20 mANI 9983D±22 mV/V Bridge120 Ω Quarter-Bridge CompletionNI 9984D350 Ω Quarter-Bridge CompletionNI 9985DHalf-Bridge CompletionNI 9986D±60 VNI 9987D
  - Input Configuration —Sets the mode for the selected
 channel(s).

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9219_Propertiesdialog.html language=enus -->
## TOPIC 00020: C Series Module Properties Dialog Box for the NI 9219 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9219_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9219_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9219 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9219 (FPGA Interface)

Right-click an [NI 9219](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9219) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module. Refer to the table
 below for information about the units and encoding of the fixed-point data
 depending on the channel mode. If you select Calibrated 
 and an NI 9219 channel is in Thermocouple mode, you must convert the CJC data in the host VI. Select Raw if
 you want the FPGA I/O Node to return calibrated, binary data from the module. If
 you select Raw , you must convert the analog input values in the host VI. The default is
 Calibrated . Table 7.Channel ModeUnits of Fixed-Point DataInteger TypeWord LengthInteger Word LengthVoltageVoltsSigned32 bits7 bitsCurrentAmpsSigned32 bits–1 bitsResistance and RTDOhmsUnsigned32 bits14 bitsThermocoupleVoltsSigned32 bits–1 bitsQuarter BridgeVolts/voltUnsigned32 bits14 bitsHalf BridgeVolts/voltSigned32 bits7 bitsFull BridgeVolts/voltSigned32 bits–1 bits
- Channels —Specifies the channel(s) for which you want to
 select the mode and range.
- Selected Channel(s) Settings —Specifies the mode and range
 for each channel.
  - Channel Mode —Sets the mode for the selected
 channel(s).
  - Range —Sets the range for the selected
 channel(s).
  - Threshold — Sets
 the Digital In threshold for the selected channel(s). This option is available only
 if you select Digital In for the channel
 mode.
- Conversion Time —Specifies the time it takes to acquire
 one point of data from all channels. You can select High
 Speed , Best 60 Hz Rejection ,
 Best 50 Hz Rejection , or High
 Resolution . Refer to the NI 9207 hardware documentation on
 ni.com/manuals for more information about these conversion times.
- Enable TEDS Support —Place a checkmark in this checkbox if
 you want to enable TEDS support 
 in the FPGA and host VIs for this module.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9220_Propertiesdialog.html language=enus -->
## TOPIC 00021: C Series Module Properties Dialog Box for the NI 9220 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9220_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9220_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9220 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9220 (FPGA Interface)

Right-click an [NI 9220](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9220) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data for the module in units of volts.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of 5 bits. Select Raw if you want the FPGA
 I/O Node to return uncalibrated, binary data for the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9222_Propertiesdialog.html language=enus -->
## TOPIC 00022: C Series Module Properties Dialog Box for the NI 9222/9223 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9222_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9222_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9222 or NI 9223 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series mod

### C Series Module Properties Dialog Box for the NI 9222/9223 (FPGA Interface)

Right-click an [NI 9222](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9222) or [NI 9223](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9223) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data for the module in units of volts.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of 5 bits. Select Raw if you want the FPGA
 I/O Node to return uncalibrated, binary data for the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9224_Propertiesdialog.html language=enus -->
## TOPIC 00023: C Series Module Properties Dialog Box for the NI 9224 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9224_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9224_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9224 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9224 (FPGA Interface)

Right-click an [NI 9224](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9224) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of 5 bits. Select Raw if you want the FPGA
 I/O Node to return calibrated, binary data from the module. If you select
 Raw , you must convert 
 the binary values to engineering units. The default is
 Calibrated .
- Conversion Time —Specifies the time it takes to acquire
 one point of data from one or more channels in a single FPGA I/O Node. You can
 select High Speed (1k S/s) , Medium Speed (100
 S/s) , Medium Resolution (50/60Hz rejection – 12
 S/s) , or High Resolution (50/60Hz rejection – 2
 S/s) . The default is High Resolution (50/60Hz
 rejection – 2 S/s) .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9226_Propertiesdialog.html language=enus -->
## TOPIC 00024: C Series Module Properties Dialog Box for the NI 9226 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9226_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9226_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9226 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9226 (FPGA Interface)

Right-click an [NI 9226](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9226) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of ohms.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of 14 bits. Select Raw if you want the FPGA
 I/O Node to return uncalibrated, binary data from the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Conversion Time —Specifies the time it takes to acquire
 one point of data from all channels. You can select 200
 ms or 2.5 ms .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9228_Propertiesdialog.html language=enus -->
## TOPIC 00025: C Series Module Properties Dialog Box for the NI 9228 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9228_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9228_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9228 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9228 (FPGA Interface)

Right-click an [NI 9228](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9228) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of 7 bits. Select Raw if you want the FPGA
 I/O Node to return calibrated, binary data from the module. If you
 select Raw , you must convert 
 the binary values to engineering units. The default is
 Calibrated .
- Conversion Time —Specifies the time it takes to acquire
 one point of data from one or more channels in a single FPGA I/O Node. You can
 select High Speed (1k S/s) , Medium Speed (100
 S/s) , Medium Resolution (50/60Hz rejection – 12
 S/s) , or High Resolution (50/60Hz rejection – 2
 S/s) . The default is High Resolution (50/60Hz
 rejection – 2 S/s) .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9231_Propertiesdialog.html language=enus -->
## TOPIC 00026: C Series Module Properties Dialog Box for the NI 9231 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9231_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9231_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9231 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9231 (FPGA Interface)

Right-click an [NI 9231](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9231) C Series module in the
 Project Explorer window and select
 Properties from the shortcut menu to display this dialog box.

Use this dialog box to configure a C Series module.

This dialog box includes
 the following components:

- Name —Specifies the name of the C Series module, which appears in
 the Project Explorer window. LabVIEW assigns a default name to the
 module based on the slot number. You can use this field to give the module a descriptive
 name.
- Type —Specifies the type of C Series module. You cannot change
 this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C Series
 module. Select Calibrated if you want the FPGA I/O Node to return
 calibrated, fixed-point data from the module. The fixed-point data is signed, with 24-bits
 word length and 4-bits integer word length. Select Raw if you want
 the FPGA I/O Node to return calibrated, binary data from the module. If you select
 Raw , you must convert the binary data to the actual analog input values in the host VI. The default
 is Calibrated .
- Master Timebase Source —Specifies the master timebase source that the
 module uses.
- Export Onboard Clock —Place a checkmark in this checkbox if you
 want to make this module accessible as a master timebase source to other modules.
- Data Rate —Specifies the rate at which the module acquires
 data.
- Enable TEDS Support —Place a checkmark in this checkbox if you
 want to enable TEDS support in the FPGA and host VIs
 for this module.
- Channels —Specifies the channel(s) for which you want to select
 the input configuration.
- Selected Channel(s) Settings —Specifies the input configuration
 for each channel.
  - Input Configuration — Sets the
 input configuration for the selected channel(s). Select AC Coupled for AC coupling, DC Coupled
 for DC coupling, IEPE AC Coupled for AC coupling with IEPE enabled.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9234_Propertiesdialog.html language=enus -->
## TOPIC 00027: C Series Module Properties Dialog Box for the NI 9230/9232/9234 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9234_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9234_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9230, NI 9232, or NI 9234 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C

### C Series Module Properties Dialog Box for the NI 9230/9232/9234 (FPGA Interface)

Right-click an [NI 9230](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9230), [NI 9232](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9232), or [NI 9234](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9234) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of 7 bits for the NI 9230/9232 and 4 bits for the NI 9234. Select
 Raw if you want the FPGA I/O Node to return
 uncalibrated, binary data from the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Master Timebase Source —Specifies the master timebase source that the module uses.
- Export Onboard Clock —Place a checkmark in this checkbox
 if you want to make this module accessible as a master timebase source to other
 modules.
- Data Rate —Specifies the rate at which the module acquires
 data.
- Enable TEDS Support —Place a checkmark in this checkbox if
 you want to enable TEDS support 
 in the FPGA and host VIs for this module.
- Channels —Specifies the channel(s) for which you want to
 select the input configuration.
- Selected Channel(s) Settings —Specifies the input
 configuration for each channel.
  - Input Configuration — Sets the input configuration for the selected channel(s). Select AC
 Coupled for AC coupling with IEPE excitation off,
 DC Coupled for DC coupling with IEPE
 excitation off, or IEPE AC Coupled for AC
 coupling with IEPE excitation on.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9235_Propertiesdialog.html language=enus -->
## TOPIC 00028: C Series Module Properties Dialog Box for the NI 9235/9236 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9235_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9235_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9235 or NI 9236 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series mod

### C Series Module Properties Dialog Box for the NI 9235/9236 (FPGA Interface)

Right-click an [NI 9235](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9235) or [NI 9236](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9236) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of
 volts/volt. The fixed-point data is signed, with a word length of 24 bits and an
 integer word length of –4 bits. Select Raw if you want
 the FPGA I/O Node to return uncalibrated, binary data from the module. If you
 select Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Master Timebase Source —Specifies the master timebase source that the module uses.
- Export Onboard Clock —Place a checkmark in this checkbox
 if you want to make this module accessible as a master timebase source to other
 modules.
- Data Rate —Specifies the rate at which the module acquires
 data.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9237_Propertiesdialog.html language=enus -->
## TOPIC 00029: C Series Module Properties Dialog Box for the NI 9237 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9237_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9237_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9237 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9237 (FPGA Interface)

Right-click an [NI 9237](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9237) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of
 volts/volt. The fixed-point data is signed, with a word length of 24 bits and an
 integer word length of –4 bits. Select Raw if you want
 the FPGA I/O Node to return uncalibrated, binary data from the module. If you
 select Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Master Timebase Source —Specifies the master timebase source that the module uses.
- Export Onboard Clock —Place a checkmark in this checkbox
 if you want to make this module accessible as a master timebase source to other
 modules.
- Data Rate —Specifies the rate at which the module acquires
 data.
- Enable TEDS Support —Place a checkmark in this checkbox if
 you want to enable TEDS support 
 in the FPGA and host VIs for this module.
- Excitation Voltage —Specifies the excitation voltage for
 the module to output to bridges, or specifies external excitation.
- Enable Half-Bridge Completion —Enables half-bridge
 completion for individual channels.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9239_Propertiesdialog.html language=enus -->
## TOPIC 00030: C Series Module Properties Dialog Box for the NI 9225/9227/9229/9238/9239/9246/9247 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9239_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9239_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9225/NI 9227/NI 9229/NI 9238/NI 9239/NI 9246/NI 9247 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—S

### C Series Module Properties Dialog Box for the NI 9225/9227/9229/9238/9239/9246/9247 (FPGA
 Interface)

Right-click an [NI 9225](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9225)/[NI 9227](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9227)/[NI 9229](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9229)/[NI 9238](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9238)/[NI 9239](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9239)/[NI 9246](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9246)/[NI 9247](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9247) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module.
  - Select Calibrated , which is the default, if you
 want the FPGA I/O Node to return calibrated, signed, fixed-point data
 from the module. The following table describes the units and integer
 word length of the returned data: Table 8.ModuleUnitsWord Length (bits)Integer Word Length (bits)NI 9225V2410NI 9227A245NI 9229V247NI 9238V241NI 9239V245NI 9246A247NI 9247A249
  - Select Raw if you want the FPGA I/O Node to
 return uncalibrated, binary data from the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI.
- Master Timebase Source —Specifies the master timebase source that the module uses.
- Export Onboard Clock —Place a checkmark in this checkbox
 if you want to make this module accessible as a master timebase source to other
 modules.
- Data Rate —Specifies the rate at which the module acquires
 data.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9242_9244_Propertiesdialog.html language=enus -->
## TOPIC 00031: C Series Module Properties Dialog Box for the NI 9242/9244 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9242_9244_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9242_9244_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9242 or NI 9244 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series mod

### C Series Module Properties Dialog Box for the NI 9242/9244 (FPGA Interface)

Right-click an [NI 9242](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9242) or [NI 9244](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9244) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of 10 bits. Select Raw if you want the FPGA
 I/O Node to return calibrated, binary data from the module. If you select
 Raw , you must scale the analog input values in the host VI. The default is
 Calibrated .
- Master Timebase Source —Specifies the master timebase source that the module uses.
- Export Onboard Clock —Place a checkmark in this checkbox
 if you want to make this module accessible as a master timebase source to other
 modules.
- Data Rate —Specifies the rate at which the module acquires
 data.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9250_Propertiesdialog.html language=enus -->
## TOPIC 00032: C Series Module Properties Dialog Box for the NI 9250 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9250_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9250_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9250 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9250 (FPGA Interface)

Right-click an [NI 9250](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9250) C Series module in the
 Project Explorer window and select
 Properties from the shortcut menu to display this dialog box.

Use this dialog box to configure a C Series module.

This dialog box includes
 the following components:

- Name —Specifies the name of the C Series module, which appears in
 the Project Explorer window. LabVIEW assigns a default name to the
 module based on the slot number. You can use this field to give the module a descriptive
 name.
- Type —Specifies the type of C Series module. You cannot change
 this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C Series
 module. Select Calibrated if you want the FPGA I/O Node to return
 calibrated, fixed-point data from the module. The fixed-point data is signed, with 24-bits
 word length and 4-bits integer word length. Select Raw if you want
 the FPGA I/O Node to return calibrated, binary data from the module. If you select
 Raw , you must convert the binary data to the actual analog input values in the host VI. The default
 is Calibrated .
- Master Timebase Source —Specifies the master timebase source that the
 module uses.
- Export Onboard Clock —Place a checkmark in this checkbox if you
 want to make this module accessible as a master timebase source to other modules.
- Data Rate —Specifies the rate at which the module acquires
 data.
- Enable TEDS Support —Place a checkmark in this checkbox if you
 want to enable TEDS support in the FPGA and host VIs
 for this module.
- Channels —Specifies the channel(s) for which you want to select
 the input configuration.
- Selected Channel(s) Settings —Specifies the input configuration
 for each channel.
  - Input Configuration — Sets the
 input configuration for the selected channel(s). Select AC Coupled for AC coupling, DC Coupled
 for DC coupling, IEPE AC Coupled for AC coupling with IEPE enabled.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9251_Propertiesdialog.html language=enus -->
## TOPIC 00033: C Series Module Properties Dialog Box for the NI 9251 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9251_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9251_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9251 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9251 (FPGA Interface)

Right-click an [NI 9251](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9251) C Series module in the
 Project Explorer window and select
 Properties from the shortcut menu to display this dialog box.

Use this dialog box to configure a C Series module.

This dialog box includes
 the following components:

- Name —Specifies the name of the C Series module, which appears in
 the Project Explorer window. LabVIEW assigns a default name to the
 module based on the slot number. You can use this field to give the module a descriptive
 name.
- Type —Specifies the type of C Series module. You cannot change
 this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C Series
 module. Select Calibrated if you want the FPGA I/O Node to return
 calibrated, fixed-point data from the module. The fixed-point data is signed, with 24-bits
 word length and 4-bits integer word length. Select Raw if you want
 the FPGA I/O Node to return calibrated, binary data from the module. If you select
 Raw , you must convert the binary data to the actual analog input values in the host VI. The default
 is Calibrated .
- Master Timebase Source —Specifies the master timebase source that the
 module uses.
- Export Onboard Clock —Place a checkmark in this checkbox if you
 want to make this module accessible as a master timebase source to other modules.
- Data Rate —Specifies the rate at which the module acquires
 data.
- Channels —Specifies the channel(s) for which you want to select
 the input configuration.
- Selected Channel(s) Settings —Specifies the input configuration
 for each channel.
  - Input Configuration — Sets the
 input configuration for the selected channel(s). Select AC Coupled for
 AC coupling, DC Coupled for DC coupling.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9252_Propertiesdialog.html language=enus -->
## TOPIC 00034: C Series Module Properties Dialog Box for the NI 9252 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9252_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9252_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9252 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9252 (FPGA Interface)

Right-click an [NI 9252](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9252) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Type —Specifies the type of C Series module. You cannot
 change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module. The fixed-point
 data is signed, with 24-bits word length and 4-bits integer word length. Select
 Raw if you want the FPGA I/O Node to return
 calibrated, binary data from the module. If you select
 Raw , you must convert the binary data to the actual analog input values in the host VI.
 The default is Calibrated .
- Master Timebase Source —Specifies the master timebase source that the module uses.
- Export Onboard Clock —Place a checkmark in this checkbox
 if you want to make this module accessible as a master timebase source to other
 modules.
- Data Rate —Specifies the rate at which the module acquires
 data.
- Filter Response —Sets the AI digital filter types
 supported by the device. Filters supported by this module are the Comb (default)
 and Butterworth filter.
- Filter Order —Sets the Filter Order for the Butterworth
 filter. This setting would only take effect if the module is currently
 configured to the Butterworth filter.
- Filter Frequency —Configures the cut-off frequency of the
 filter. It is dependent on the data rate. Available values: Table 9.Filter SettingsCut-off FrequencyCombButterworth12.8 MHz13.1 MHzFilter Frequency - 1Data Rate/14000 Hz4096 HzFilter Frequency - 2Data Rate/22000 Hz2048 HzFilter Frequency - 3Data Rate/41000 Hz1024 HzFilter Frequency - 4Data Rate/8500 Hz512 HzFilter Frequency - 5Data Rate/16250 Hz256 HzFilter Frequency - 6Data Rate/16125 Hz128 HzNotes: When the module is
 configured to the Comb filter, Filter Frequency - 5 and
 Filter Frequency - 6 sets the Notch Frequency at Data
 Rate/16.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9253_Propertiesdialog.html language=enus -->
## TOPIC 00035: C Series Module Properties Dialog Box for the NI 9253 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9253_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9253_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9253 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9253 (FPGA Interface)

Right-click an [NI 9253](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9253) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Type —Specifies the type of C Series module. You cannot
 change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module. The fixed-point
 data is signed, with 24-bits word length and -4-bits integer word length. Select
 Raw if you want the FPGA I/O Node to return
 calibrated, binary data from the module. If you select
 Raw , you must convert the binary data to the actual analog input values in the host VI.
 The default is Calibrated .
- Master Timebase Source —Specifies the master timebase source that the module uses.
- Export Onboard Clock —Place a checkmark in this checkbox
 if you want to make this module accessible as a master timebase source to other
 modules.
- Data Rate —Specifies the rate at which the module acquires
 data.
- Filter Response —Sets the AI digital filter types
 supported by the device. Filters supported by this module are the Comb (default)
 and Butterworth filter.
- Filter Order —Sets the Filter Order for the Butterworth
 filter. This setting would only take effect if the module is currently
 configured to the Butterworth filter.
- Filter Frequency —Configures the cut-off frequency of the
 filter. It is dependent on the data rate. Available values: Table 10.Filter SettingsCut-off FrequencyCombButterworth12.8 MHz13.1 MHzFilter Frequency - 1Data Rate/14000 Hz4096 HzFilter Frequency - 2Data Rate/22000 Hz2048 HzFilter Frequency - 3Data Rate/41000 Hz1024 HzFilter Frequency - 4Data Rate/8500 Hz512 HzFilter Frequency - 5Data Rate/16250 Hz256 HzFilter Frequency - 6Data Rate/16125 Hz128 HzNotes: When the module is
 configured to the Comb filter, Filter Frequency - 5 and
 Filter Frequency - 6 sets the Notch Frequency at Data
 Rate/16.
- Diagnostic Settings —Clicking on this button brings up a
 new dialog box which allows the diagnostics of the module to be selected.
  - Field-Side Power Fault Detection Enable —Placing a
 checkmark in the checkbox will enable the module to detect field-side
 power fault.
  - Input Limits Fault Detection Enable —Placing a
 checkmark in the checkbox enables the module to detect if the readings
 are within the set limits. It will also bring up the option to set the
 upper limit and the lower limit.
  - Lower Fault Detection Limit —Sets the Channel's
 Lower Fault Detection Limit of the corresponding channel. The range of
 valid current limit values is 0—0.0219 A (default value is 0.0 A).
  - Upper Fault Detection Limit —Sets the Channel's
 Upper Fault Detection Limit of the corresponding channel. The range of
 valid current limit values is 0—0.0219 A (default value is 0.0219 A).

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9260_Propertiesdialog.html language=enus -->
## TOPIC 00036: C Series Module Properties Dialog Box for the NI 9260 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9260_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9260_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9260 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9260 (FPGA Interface)

Right-click an [NI 9260](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9260) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to accept fixed-point data in units of volts when writing to the module.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of 4 bits. Select Raw if you want the FPGA
 I/O Node to accept calibrated, binary data when writing to the module. If you
 select Raw , you must convert the analog output values in the host VI before you write them to
 the module. The default is Calibrated .
- Master Timebase Source —Specifies the master timebase
 source that the module uses.
- Export Onboard Clock —Place a checkmark in this checkbox
 if you want to make this module accessible as a master timebase source to other
 modules.
- Data Rate —Specifies the rate at which the module acquires
 data.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9265_Propertiesdialog.html language=enus -->
## TOPIC 00037: C Series Module Properties Dialog Box for the NI 9265 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9265_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9265_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9265 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9265 (FPGA Interface)

Right-click an [NI 9265](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9265) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to accept fixed-point data in units of amps when writing to the module. The
 fixed-point data is unsigned, with a word length of 20 bits and an integer word
 length of –5 bits. Select Raw if you want the FPGA I/O
 Node to accept calibrated, binary data when writing to the module. If you select
 Raw , you must convert the analog output values in the host VI before you write them to
 the module. The default is Calibrated .
- Hot Swap Behavior —Specifies the state of the output
 channels when the C Series module is removed and reinserted with the FPGA VI
 loaded and running. The power-on output state is the state that a C Series
 output module is in when power is applied to the module. The default is
 Last output value .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9266_Propertiesdialog.html language=enus -->
## TOPIC 00038: C Series Module Properties Dialog Box for the NI 9266 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9266_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9266_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9266 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9266 (FPGA Interface)

Right-click an [NI 9266](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9266) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to accept fixed-point data in units of amps when writing to the module. The
 fixed-point data is unsigned, with a word length of 20 bits and an integer word
 length of –5 bits. Select Raw if you want the FPGA I/O
 Node to accept calibrated, binary data when writing to the module. If you select
 Raw , you must convert the analog output values in the host VI before you write them to
 the module. The default is Calibrated .
- Hot Swap Behavior —Specifies the state of the output
 channels when the C Series module is removed and reinserted with the FPGA VI
 loaded and running. The power-on output state is the state that a C Series
 output module is in when power is applied to the module. The default is
 Last output value .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/926x_Propertiesdialog.html language=enus -->
## TOPIC 00039: C Series Module Properties Dialog Box for the NI 9262/9263/9264/9269 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/926x_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/926x_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9262, NI 9263, NI 9264, or NI 9269 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name

### C Series Module Properties Dialog Box for the NI 9262/9263/9264/9269 (FPGA
 Interface)

Right-click an [NI 9262](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9262), [NI 9263](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9263), [NI 9264](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9264), or [NI 9269](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9269) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to accept fixed-point data in units of volts when writing to the module.
 The fixed-point data is signed, with a word length of 20 bits and an integer
 word length of 5 bits. Select Raw if you want the FPGA
 I/O Node to accept calibrated, binary data when writing to the module. If you
 select Raw , you must convert the analog output values in the host VI before you write them to
 the module. The default is Calibrated .
- Hot Swap Behavior —Specifies the state of the output
 channels when the C Series module is removed and reinserted with the FPGA VI
 loaded and running. The power-on output state is the state that a C Series
 output module is in when power is applied to the module. The default is
 Last output value .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9320_Propertiesdialog.html language=enus -->
## TOPIC 00040: C Series Module Properties Dialog Box for the NI 9320 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9320_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9320_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9320 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9320 (FPGA Interface)

Right-click an [NI 9320](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9320) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data for the module in units of volts.
 The fixed-point data is signed, with a word length of 24 bits and an integer
 word length of 5 bits. Select Raw if you want the FPGA
 I/O Node to return calibrated, binary data for the module. If you select
 Raw , you must convert the binary data to the actual analog input values in the host VI. The default is
 Calibrated .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9326_Propertiesdialog.html language=enus -->
## TOPIC 00041: C Series Module Properties Dialog Box for the NI 9326 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9326_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9326_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9326 C Series module in the Project Explorer window and select Properties from the shortcut menu to launch the C Series Module Properties dialog box, that includes the following components, which you can use to configure a C Series module. Name—Specifies the name of the C Series mo

### C Series Module Properties Dialog Box for the NI 9326 (FPGA Interface)

Right-click an [NI 9326](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9326) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to launch the
 C Series Module Properties dialog box, that includes the
 following components, which you can use to configure a C Series module.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. Use this field to assign a
 descriptive name to the module.
- Type —Specifies the type of C Series module. You cannot
 change this option.
- Location —Specifies the slot in the chassis used by the C
 Series module.
- Digital Input Mode —Specifies the mode of module. If this
 property is checked, only digital input channel, DIx will be supported.
  - Digital Input Channels—Specifies the list of input channels available in
 the module, which you can select to configure.
  - Active Edge—Sets the triggering edge of the input signal.
  - Threshold (V)—Sets the threshold value for the input channel.
  - Hysteresis Value (V)—Sets the hysteresis value for the input channel.
 Note Changing this option will change the [FPGA interface](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9326).
- Channel —Specifies the list of counters available in the
 module, which you can select to configure.
- Measurement —Specifies the selected measurement mode of
 the corresponding counter.
- Terminals —Specifies the selected terminal settings of the
 corresponding counter.
- Settings —Specifies the selected configuration of the
 corresponding counter.
- Measurement Mode —Sets the measurement mode of the
 corresponding counter. Table 11.Measurement ModeConfiguration TypeDescriptionEdge CountingInitial CountSets the initial counter value.PauseEnables or disables the Pause feature.HW ResetEnables or disables the Hardware Reset.Reset CountSets the value the counter resets to when HW Reset is
 triggered.DirectionSets the count direction to Count Up, Count Down, or
 Externally Controlled.PeriodEnable Butterworth FilterEnables or disables Butterworth filter.Filter Frequency*Sets the Butterworth filter’s cut-off frequency.Sample Rate (Hz)Specifies the rate at which data is being sampled from
 the counter. This value is used to calculate the Measurement
 Time and Divisor of the counter.Maximum Measurable Period (ms)Specifies the maximum (slowest) period of the input
 signal that can be measured.Maximum Freq (Hz)Specifies the maximum input frequency. This value is used
 along with the Sample Rate to calculate the Measurement Time
 and Divisor of the counter. * The following table specifies the available cut-off frequecies. Table 12.Filter FrequencyCut-off FrequencyFilter Frequency—16167 HzFilter Frequency—22941 HzFilter Frequency—31439 HzFilter Frequency—4712 HzFilter Frequency—5354 HzFilter Frequency—6177 HzFilter Frequency—788 HzFilter Frequency—844 HzFilter Frequency—922 HzFilter Frequency—1011 HzFilter Frequency—116 HzFilter Frequency—123 HzFilter Frequency—131 Hz
- Advanced Configuration —Launches the Advanced
 Configuration dialog box.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9344_Propertiesdialog.html language=enus -->
## TOPIC 00042: C Series Module Properties Dialog Box for the NI 9344 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9344_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9344_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9344 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9344 (FPGA Interface)

Right-click an [NI 9344](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9344) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9344_Propertiesdialog_2.html language=enus -->
## TOPIC 00043: C Series Module Properties Dialog Box for the NI 9344 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9344_Propertiesdialog_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9344_Propertiesdialog_2.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9344 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9344 (FPGA Interface)

Right-click an [NI 9344](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9344) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9361_Propertiesdialog.html language=enus -->
## TOPIC 00044: C Series Module Properties Dialog Box for the NI 9361 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9361_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9361_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9361 C Series module in the Project Explorer window and select Properties from the shortcut menu to launch the C Series Module Properties dialog box, that includes the following components, which you can use to configure a C Series module. Name—Specifies the name of the C Series mo

### C Series Module Properties Dialog Box for the NI 9361 (FPGA Interface)

Right-click an [NI 9361](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9361) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to launch the
 C Series Module Properties dialog box, that includes the
 following components, which you can use to configure a C Series module.

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. Use this field to assign a
 descriptive name to the module.
- Type —Specifies the type of C Series module. You cannot
 change this option.
- Location —Specifies the slot in the chassis used by the C
 Series module.
- Channel —Specifies the list of counters available in the
 module, which you can select to configure.
- Measurement —Specifies the selected measurement mode of
 the corresponding counter.
- Terminals —Specifies the selected terminal settings of the
 corresponding counter.
- Settings —Specifies the selected configuration of the
 corresponding counter.
- Measurement Mode —Sets the measurement mode of the
 corresponding counter. Table 13.Measurement ModeConfiguration TypeDescriptionEdge CountingInitial CountSets the initial counter value.Active EdgeSets the active edge of the counter.PauseEnables or disables the Pause feature.Pause WhenConfigures the Pause trigger to Pause When High or Pause
 When Low.HW ResetEnables or disables the Hardware Reset.Reset EdgeConfigures the HW Reset to trigger on the rising or
 falling edge.Reset CountSets the value the counter resets to when HW Reset is
 triggered.DirectionSets the count direction to Count Up, Count Down, or
 Externally Controlled.Count Up WhenSets the counter to Count Up when the external terminal
 is high or low.PeriodStarting EdgeConfigures the counter to start counting on the rising or
 falling edge.Sample Rate (Hz)Specifies the rate at which data is being sampled from
 the counter. This value is used to calculate the Measurement
 Time and Divisor of the counter.Maximum Measurable Period (ms)Specifies the maximum (slowest) period input signal that
 can be measured.Maximum Freq (Hz)Specifies the maximum input frequency. This value is used
 to calculate the Measurement Time and Divisor of the
 counter.PulseStarting EdgeConfigures the counter to start counting on the rising or
 falling edge.Maximum Measurable Period (ms)Specifies the maximum (slowest) period input signal that
 can be measured.Pulse WidthStarting EdgeConfigures the counter to start counting on the rising or
 falling edge.Maximum Measurable Period (ms)Specifies the maximum (slowest) period input signal that
 can be measured.Two Edge SeparationFirst EdgeConfigures the first edge to either rising or
 falling.Second EdgeConfigures the second edge to either rising or
 falling.Maximum Measurable Separation (ms)Specifies the maximum separation that can be measured
 between the first input signal and the second input
 signal.Quadrature Encoder PositionInitial PositionSets the initial counter value.Decoding TypeConfigures the decoding type (x1, x2, or x4).Z Index EnableEnables or disables the usage of the Z terminal.Z Index ValueSets the value that is loaded to the counter when the Z
 terminal is triggered.Z Index PhaseConfigures the AB phase in which the Z Index value is
 loaded to the counter when the Z Terminal is
 triggered.Two Pulse EncoderInitial PositionSets the initial counter value.HW ResetEnables or disables the Hardware Reset.Reset EdgeConfigures the HW Reset to trigger on the rising or
 falling edge.Reset PositionSets the value the counter resets to when HW Reset is
 triggered.Quadrature Encoder VelocityDecoding TypeConfigures the decoding type (x1, x2, and x4).Sample Rate (Hz)Specifies the rate at which data is being sampled from
 the counter. This value is used to calculate the Measurement
 Time and Divisor of the counter.Maximum Measurable Count Period (ms)Specifies the maximum (slowest) period between encoder
 input counts that can be measured.Maximum Count Rate (Hz)Specifies the maximum count rate. This value is used to
 calculate the Measurement Time and Divisor of the
 counter.Two Pulse Encoder VelocitySample Rate (Hz)Specifies the rate at which data is being sampled from
 the counter. This value is used to calculate the Measurement
 Time and Divisor of the counter.Maximum Measurable Count Period (ms)Specifies the maximum (slowest) period between encoder
 input counts that can be measured.Maximum Count Rate (Hz)Specifies the maximum count rate. This value is used to
 calculate the Measurement Time and Divisor of the
 counter.
- Advanced Configuration —Launches the Advanced
 Configuration dialog box.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9381_Propertiesdialog.html language=enus -->
## TOPIC 00045: C Series Module Properties Dialog Box for the NI 9381 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9381_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9381_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9381 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9381 (FPGA Interface)

Right-click an [NI 9381](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9381) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is unsigned, with a word length of 18 bits and an integer
 word length of 3 bits for the analog input channels and a word length of 16 bits
 and an integer word length of 3 bits for the analog output channels. Select
 Raw if you want the FPGA I/O Node to return
 uncalibrated, binary data from the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Channels —Specifies the channel(s) for which you want to
 select the direction.
- Selected Channel(s) Settings —Specifies the direction for
 each channel.
- Hot Swap Behavior (Analog Output) —Specifies the state of
 the analog output channels when the C Series module is removed and reinserted
 with the FPGA VI loaded and running. The power-on output state is the state that
 a C Series output module is in when power is applied to the module. The default
 is Last output value.
- Allow Programmatic DIO Line Direction Change —Place a
 checkmark in this checkbox if you want to enable programmable DIO line changes
 on the module. Caution Performing a DIO line direction change
 will affect the timing of any concurrent AI, AO, and DO operations. Refer to
 the [Avoiding Timing Uncertainty](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_9381_timing_uncertainty) topic for more information.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9381_Propertiesdialog_2.html language=enus -->
## TOPIC 00046: C Series Module Properties Dialog Box for the NI 9381 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9381_Propertiesdialog_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9381_Propertiesdialog_2.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9381 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9381 (FPGA Interface)

Right-click an [NI 9381](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9381) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is unsigned, with a word length of 18 bits and an integer
 word length of 3 bits for the analog input channels and a word length of 16 bits
 and an integer word length of 3 bits for the analog output channels. Select
 Raw if you want the FPGA I/O Node to return
 uncalibrated, binary data from the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Channels —Specifies the channel(s) for which you want to
 select the direction.
- Selected Channel(s) Settings —Specifies the direction for
 each channel.
- Hot Swap Behavior (Analog Output) —Specifies the state of
 the analog output channels when the C Series module is removed and reinserted
 with the FPGA VI loaded and running. The power-on output state is the state that
 a C Series output module is in when power is applied to the module. The default
 is Last output value.
- Allow Programmatic DIO Line Direction Change —Place a
 checkmark in this checkbox if you want to enable programmable DIO line changes
 on the module. Caution Performing a DIO line direction change
 will affect the timing of any concurrent AI, AO, and DO operations. Refer to
 the [Avoiding Timing Uncertainty](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_9381_timing_uncertainty) topic for more information.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9381_Propertiesdialog_3.html language=enus -->
## TOPIC 00047: C Series Module Properties Dialog Box for the NI 9381 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9381_Propertiesdialog_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9381_Propertiesdialog_3.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9381 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9381 (FPGA Interface)

Right-click an [NI 9381](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9381) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is unsigned, with a word length of 18 bits and an integer
 word length of 3 bits for the analog input channels and a word length of 16 bits
 and an integer word length of 3 bits for the analog output channels. Select
 Raw if you want the FPGA I/O Node to return
 uncalibrated, binary data from the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Channels —Specifies the channel(s) for which you want to
 select the direction.
- Selected Channel(s) Settings —Specifies the direction for
 each channel.
- Hot Swap Behavior (Analog Output) —Specifies the state of
 the analog output channels when the C Series module is removed and reinserted
 with the FPGA VI loaded and running. The power-on output state is the state that
 a C Series output module is in when power is applied to the module. The default
 is Last output value.
- Allow Programmatic DIO Line Direction Change —Place a
 checkmark in this checkbox if you want to enable programmable DIO line changes
 on the module. Caution Performing a DIO line direction change
 will affect the timing of any concurrent AI, AO, and DO operations. Refer to
 the [Avoiding Timing Uncertainty](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_9381_timing_uncertainty) topic for more information.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9381_Propertiesdialog_4.html language=enus -->
## TOPIC 00048: C Series Module Properties Dialog Box for the NI 9381 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9381_Propertiesdialog_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9381_Propertiesdialog_4.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9381 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9381 (FPGA Interface)

Right-click an [NI 9381](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9381) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Select Calibrated if you want the FPGA I/O
 Node to return calibrated, fixed-point data from the module in units of volts.
 The fixed-point data is unsigned, with a word length of 18 bits and an integer
 word length of 3 bits for the analog input channels and a word length of 16 bits
 and an integer word length of 3 bits for the analog output channels. Select
 Raw if you want the FPGA I/O Node to return
 uncalibrated, binary data from the module. If you select
 Raw , you must convert and calibrate the analog input values in the host VI. The default is
 Calibrated .
- Channels —Specifies the channel(s) for which you want to
 select the direction.
- Selected Channel(s) Settings —Specifies the direction for
 each channel.
- Hot Swap Behavior (Analog Output) —Specifies the state of
 the analog output channels when the C Series module is removed and reinserted
 with the FPGA VI loaded and running. The power-on output state is the state that
 a C Series output module is in when power is applied to the module. The default
 is Last output value.
- Allow Programmatic DIO Line Direction Change —Place a
 checkmark in this checkbox if you want to enable programmable DIO line changes
 on the module. Caution Performing a DIO line direction change
 will affect the timing of any concurrent AI, AO, and DO operations. Refer to
 the [Avoiding Timing Uncertainty](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_9381_timing_uncertainty) topic for more information.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9401_Propertiesdialog.html language=enus -->
## TOPIC 00049: C Series Module Properties Dialog Box for the NI 9401 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9401_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9401_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9401 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9401 (FPGA Interface)

Right-click an [NI 9401](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9401) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Initial Line Direction —Sets the initial line direction for each digital port to digital input or digital output. The
 default is digital input.
- Advanced —Launches the Advanced
 Configuration dialog box.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9401_Propertiesdialog_2.html language=enus -->
## TOPIC 00050: C Series Module Properties Dialog Box for the NI 9401 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9401_Propertiesdialog_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9401_Propertiesdialog_2.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9401 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9401 (FPGA Interface)

Right-click an [NI 9401](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9401) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Initial Line Direction —Sets the initial line direction for each digital port to digital input or digital output. The
 default is digital input.
- Advanced —Launches the Advanced
 Configuration dialog box.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9402_Propertiesdialog.html language=enus -->
## TOPIC 00051: C Series Module Properties Dialog Box for the NI 9402 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9402_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9402_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9402 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9402 (FPGA Interface)

Right-click an [NI 9402](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9402) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Channels —Specifies the channel(s) for which you want to
 select the line direction.
- Selected Channel(s) Settings —Specifies the line direction
 for each channel.
  - Direction — Sets
 the line direction for the selected channel(s) to digital input or digital
 output. The default is digital input.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9402_Propertiesdialog_2.html language=enus -->
## TOPIC 00052: C Series Module Properties Dialog Box for the NI 9402 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9402_Propertiesdialog_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9402_Propertiesdialog_2.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9402 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9402 (FPGA Interface)

Right-click an [NI 9402](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9402) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Channels —Specifies the channel(s) for which you want to
 select the line direction.
- Selected Channel(s) Settings —Specifies the line direction
 for each channel.
  - Direction — Sets
 the line direction for the selected channel(s) to digital input or digital
 output. The default is digital input.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9403_Propertiesdialog.html language=enus -->
## TOPIC 00053: C Series Module Properties Dialog Box for the NI 9403 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9403_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9403_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9403 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9403 (FPGA Interface)

Right-click an [NI 9403](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9403) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Channels —Specifies the channel(s) for which you want to
 select the line direction.
- Selected Channel(s) Settings —Specifies the line direction
 for each channel.
  - Direction — Sets
 the line direction for the selected channel(s) to digital input or digital
 output. The default is digital input.
- Disable Arbitration —Place a checkmark in this checkbox if
 you want to change the arbitration setting to Never Arbitrate and reduce the
 amount of FPGA logic used by VIs. Check this box only if you are sure that the
 design of the FPGA VI will never allow more than one digital function to execute
 at the same time, even on different channels. If more than one digital function
 could execute simultaneously in the FPGA VI, leave the box unchecked to keep the
 default Arbitrate if Multiple Requestors Only arbitration setting.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9403_Propertiesdialog_2.html language=enus -->
## TOPIC 00054: C Series Module Properties Dialog Box for the NI 9403 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9403_Propertiesdialog_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9403_Propertiesdialog_2.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9403 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9403 (FPGA Interface)

Right-click an [NI 9403](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9403) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Channels —Specifies the channel(s) for which you want to
 select the line direction.
- Selected Channel(s) Settings —Specifies the line direction
 for each channel.
  - Direction — Sets
 the line direction for the selected channel(s) to digital input or digital
 output. The default is digital input.
- Disable Arbitration —Place a checkmark in this checkbox if
 you want to change the arbitration setting to Never Arbitrate and reduce the
 amount of FPGA logic used by VIs. Check this box only if you are sure that the
 design of the FPGA VI will never allow more than one digital function to execute
 at the same time, even on different channels. If more than one digital function
 could execute simultaneously in the FPGA VI, leave the box unchecked to keep the
 default Arbitrate if Multiple Requestors Only arbitration setting.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9411_Propertiesdialog.html language=enus -->
## TOPIC 00055: C Series Module Properties Dialog Box for the NI 9375/9411/9421/9422/9423/9425/9426/9435/9436/9437/950x (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9411_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9411_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9375, NI 9411, NI 9421, NI 9422, NI 9423, NI 9425, NI 9426, NI 9435, NI 9436, NI 9437, NI 9501, or NI 9505 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. Thi

### C Series Module Properties Dialog Box for the NI
 9375/9411/9421/9422/9423/9425/9426/9435/9436/9437/950x (FPGA Interface)

Right-click an [NI 9375](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9375), [NI 9411](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9411), [NI 9421](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9421), [NI 9422](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9422), [NI 9423](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9423), [NI 9425](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9425), [NI 9426](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9426), [NI 9435](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9435), [NI 9436](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9436), [NI 9437](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9437), [NI 9501](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_9501_io_reference),
 or [NI 9505](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_9505_io_reference) C
 Series module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9411_Propertiesdialog_2.html language=enus -->
## TOPIC 00056: C Series Module Properties Dialog Box for the NI 9375/9411/9421/9422/9423/9425/9426/9435/9436/9437/950x (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9411_Propertiesdialog_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9411_Propertiesdialog_2.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9375, NI 9411, NI 9421, NI 9422, NI 9423, NI 9425, NI 9426, NI 9435, NI 9436, NI 9437, NI 9501, or NI 9505 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. Thi

### C Series Module Properties Dialog Box for the NI
 9375/9411/9421/9422/9423/9425/9426/9435/9436/9437/950x (FPGA Interface)

Right-click an [NI 9375](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9375), [NI 9411](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9411), [NI 9421](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9421), [NI 9422](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9422), [NI 9423](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9423), [NI 9425](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9425), [NI 9426](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9426), [NI 9435](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9435), [NI 9436](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9436), [NI 9437](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9437), [NI 9501](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_9501_io_reference),
 or [NI 9505](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_9505_io_reference) C
 Series module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9411_Propertiesdialog_3.html language=enus -->
## TOPIC 00057: C Series Module Properties Dialog Box for the NI 9375/9411/9421/9422/9423/9425/9426/9435/9436/9437/950x (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9411_Propertiesdialog_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9411_Propertiesdialog_3.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9375, NI 9411, NI 9421, NI 9422, NI 9423, NI 9425, NI 9426, NI 9435, NI 9436, NI 9437, NI 9501, or NI 9505 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. Thi

### C Series Module Properties Dialog Box for the NI
 9375/9411/9421/9422/9423/9425/9426/9435/9436/9437/950x (FPGA Interface)

Right-click an [NI 9375](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9375), [NI 9411](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9411), [NI 9421](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9421), [NI 9422](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9422), [NI 9423](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9423), [NI 9425](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9425), [NI 9426](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9426), [NI 9435](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9435), [NI 9436](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9436), [NI 9437](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9437), [NI 9501](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_9501_io_reference),
 or [NI 9505](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_9505_io_reference) C
 Series module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9411_Propertiesdialog_4.html language=enus -->
## TOPIC 00058: C Series Module Properties Dialog Box for the NI 9375/9411/9421/9422/9423/9425/9426/9435/9436/9437/950x (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9411_Propertiesdialog_4.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9411_Propertiesdialog_4.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9375, NI 9411, NI 9421, NI 9422, NI 9423, NI 9425, NI 9426, NI 9435, NI 9436, NI 9437, NI 9501, or NI 9505 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. Thi

### C Series Module Properties Dialog Box for the NI
 9375/9411/9421/9422/9423/9425/9426/9435/9436/9437/950x (FPGA Interface)

Right-click an [NI 9375](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9375), [NI 9411](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9411), [NI 9421](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9421), [NI 9422](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9422), [NI 9423](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9423), [NI 9425](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9425), [NI 9426](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9426), [NI 9435](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9435), [NI 9436](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9436), [NI 9437](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9437), [NI 9501](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_9501_io_reference),
 or [NI 9505](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_9505_io_reference) C
 Series module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9470_Propertiesdialog.html language=enus -->
## TOPIC 00059: C Series Module Properties Dialog Box for the NI 9470

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9470_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9470_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9470 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9470

Right-click an [NI 9470](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9470) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Master Timebase Source —Specifies the master timebase source that the module uses.
- Export Onboard Clock —Place a checkmark in this checkbox
 if you want to make this module accessible as a master timebase source to other
 modules.
- Data Rate —Specifies the rate at which the module acquires
 data.
- Channel Configuration —Launches the channel configuration
 dialog box to configure the channel settings.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9472_Propertiesdialog.html language=enus -->
## TOPIC 00060: C Series Module Properties Dialog Box for the NI 9472/9474/9475/9481/9482/9485 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9472_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9472_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9472, NI 9474, NI 9475, NI 9481, NI 9482, or NI 9485 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—S

### C Series Module Properties Dialog Box for the NI 9472/9474/9475/9481/9482/9485 (FPGA
 Interface)

Right-click an [NI 9472](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9472), [NI 9474](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9474), [NI 9475](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9475), [NI 9481](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9481), [NI 9482](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9482), or [NI 9485](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9485) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Advanced —Launches the Advanced
 Configuration dialog box.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9476_Propertiesdialog.html language=enus -->
## TOPIC 00061: C Series Module Properties Dialog Box for the NI 9476/9477 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9476_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9476_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9476 or NI 9477 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series mod

### C Series Module Properties Dialog Box for the NI 9476/9477 (FPGA Interface)

Right-click an [NI 9476](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9476) or [NI 9477](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9476) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Disable Arbitration —Place a checkmark in this checkbox if
 you want to change the arbitration setting to Never Arbitrate and reduce the
 amount of FPGA logic used by VIs. Check this box only if you are sure that the
 design of the FPGA VI will never allow more than one digital output function to
 execute at the same time, even on different channels. If more than one digital
 output function could execute simultaneously in the FPGA VI, leave the box
 unchecked to keep the default Arbitrate if Multiple Requestors Only arbitration
 setting.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9478_Propertiesdialog.html language=enus -->
## TOPIC 00062: C Series Module Properties Dialog Box for the NI 9478 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9478_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9478_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9478 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9478 (FPGA Interface)

Right-click an [NI 9478](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9478) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Channels —Specifies the channel(s) for which you want to
 select the active current limit.
- Selected Channel(s) Settings —Specifies the active current
 limit for each channel.
  - Active Limit — Sets the active current limit for the selected channel(s). Select Limit
 A if you want to set the active current limit for the
 channel(s) to Current Limit A. Select Limit B if
 you want to set the active current limit for the channel(s) to Current
 Limit B. Select No Limit if you want the
 channel(s) to have no current limit.
- Module Settings —Specifies the current limit threshold
 settings for the module.
  - Current Limit A —Sets the current limit threshold
 for Current Limit A in amperes. Valid values are 0–5.1 A.
  - Current Limit B —Sets the current limit threshold
 for Current Limit B in amperes. Valid values are 0–5.1 A.
  - Enable Overcurrent Refresh —Place a checkmark in
 this checkbox if you want to enable a channel to automatically recover
 if the channel exceeds its active current limit threshold. If
 overcurrent refresh is disabled, the channel remains off after an
 overcurrent condition until you write to the channel using an FPGA I/O
 Node.
  - Overcurrent Refresh Period —Sets the time in µs it
 takes a channel to automatically recover if the channel exceeds its
 active current limit threshold. Valid values are 20–2550 µs. This option
 is available only if you select Enable Overcurrent
 Refresh .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9770_Propertiesdialog.html language=enus -->
## TOPIC 00063: C Series Module Properties Dialog Box for the NI 9770 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9770_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9770_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9770 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9770 (FPGA Interface)

Right-click an [NI 9770](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9770) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Master Timebase Source —Specifies the master timebase
 source used by the module.
- Export Onboard Clock —Place a checkmark in this checkbox
 if you want to make this module accessible as a master timebase source to other
 modules.
- Data Rate —Specifies the rate at which the module acquires
 data.
- Center Frequency (Hz) —Specifies the RF center frequency
 at which the module acquires data.
- Reference Level (dBm) —Specifies the expected total power
 in dBm of the RF input signal.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/9775_Propertiesdialog.html language=enus -->
## TOPIC 00064: C Series Module Properties Dialog Box for the NI 9775 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/9775_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/9775_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9775 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9775 (FPGA Interface)

Right-click an [NI 9775](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9775) C Series
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Calibration Mode —Sets the calibration mode for the C
 Series module. Can be either "Calibrated" or "Raw."
- Reference Clock Source —Specifies the master timebase
 source used by the module.
- Export Reference Clock —Place a checkmark in this checkbox
 if you want to make this module accessible as a master timebase source to other
 modules.
- Record Data Rate —Specifies the rate at which the module
 acquires data for the Record Acquisition.
- Record Pre-Trigger Samples —Sets the number of acquired
 samples prior to the trigger of a record.
- Record Samples —Specifies the number of samples per
 record. The maximum number of record samples depend on the number of channels
 enabled.
- Continuous Data Rate —Specifies the rate at which the
 module acquires data in continuous mode. The maximum data rate depends on the
 number of channels enabled.
- Channel Configuration — Enables or disables each channel.
 Also sets the analog filter configuration for each channel.
- Timing Mode —Changes the module configuration between
 high-speed and high-resolution.
- Maximum Number of Records —Indicates the maximum number of
 records that can be potentially triggered based on the number of channels
 enabled and the record samples.
- Reference Trigger Source —Specifies the master trigger
 source used by this module. The default value is "Same as Ref Clock," which will
 set the trigger source for this module to the same as the reference clock
 source. You can configure a different reference trigger source as the reference
 clock source.
- Export Reference Trigger —Allows you to select this module
 as a reference trigger source for other modules. This checkbox will not appear
 if the reference trigger source is set to "Same as Ref Clock."

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/cRIO-9326_Advanced_Configuration_Dialog_Box.html language=enus -->
## TOPIC 00065: Advanced Configuration Dialog Box (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/cRIO-9326_Advanced_Configuration_Dialog_Box.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/cRIO-9326_Advanced_Configuration_Dialog_Box.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Advanced Configuration button on the C Series Module Properties dialog box for the NI 9326 to launch the Advanced Configuration dialog box, which you can use to configure the counter input terminals and each digital input line. Counters—Configures the corresponding counter terminal. Measur

### Advanced Configuration Dialog Box (FPGA Interface)

Click the Advanced Configuration button on the [C
 Series Module Properties](9326_Propertiesdialog.html) dialog box for the [NI 9326](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9326) to launch
 the Advanced Configuration dialog box, which you can use to
 configure the counter input terminals and each digital input line.

- Counters —Configures the corresponding counter terminal.
  - Measurement Mode—Displays the measurement mode of the selected
 counter.
  - Reset Terminals to Default—Reset the terminal settings to the factory
 defaults.
  - Terminals of the selected counters:
    - For Edge Counting, there are up to 4 terminals per counter
 (Input, Reset, Direction, and Pause).
    - For Period, there is only one terminal per counter.
- Digital Inputs —Configures the corresponding digital
 inputs lines.
  - Digital Input Channels—Selects the Digital Inputs to configure.
  - Active Edge—Sets the triggering edge of the input signal.
  - Digital Filter—Enables or disables the digital input filter.
  - Minimum Pulse Width (ms)—Configures the minimum pulse width of the
 digital input filter. Pulses that are shorter than the minimum pulse
 width will be filtered out (Applies only when Digital Filter is
 enabled).
  - Threshold (V)—Sets the threshold value for the digital input.
  - Hysteresis Value (V)—Sets the hysteresis value for the digital
 input.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/cRIO-9361_Advanced_Configuration_Dialog_Box.html language=enus -->
## TOPIC 00066: Advanced Configuration Dialog Box (FPGA Interface) 1

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/cRIO-9361_Advanced_Configuration_Dialog_Box.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/cRIO-9361_Advanced_Configuration_Dialog_Box.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Advanced Configuration button on the C Series Module Properties dialog box for the NI 9361 to launch the Advanced Configuration dialog box, which you can use to configure the counter input terminals and each digital input line. Counters—Configures the corresponding counter terminal. Measur

### Advanced Configuration Dialog Box (FPGA Interface) 1

Click the Advanced Configuration button on the [C
 Series Module Properties](9361_Propertiesdialog.html) dialog box for the [NI 9361](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9361) to launch
 the Advanced Configuration dialog box, which you can use to
 configure the counter input terminals and each digital input line.

- Counters —Configures the corresponding counter terminal.
  - Measurement Mode—Displays the measurement mode of the selected
 counter.
  - Reset Terminals to Default—Reset the terminal settings to the factory
 defaults.
  - Terminals of the selected counters:
    - For Edge Counting, there are up to 4 terminals per counter
 (Input, Reset, Direction, and Pause).
    - For Quadrature Encoder Position and Two Pulse Encoder, there are
 up to 3 terminals per counter (A Input, B Input, and Z or
 Reset).
    - For Two Edge Separation, there are two terminals per counter
 (First Input and Second Input).
    - For Quadrature Encoder Velocity and Two Pulse Encoder Velocity,
 there are two terminals per counter (A Input and B Input).
    - For Period, Pulse, and Pulse Width, there is only one terminal
 per counter.
- Digital Inputs —Configures the corresponding digital
 inputs lines.
  - Digital Input Channels—Selects the Digital Inputs to configure.
  - Terminal Mode—Configures the terminal mode (Differential, Single-Ended,
 or Single-Ended with Pull-up) of the selected digital input.
  - Digital Filter—Enables or disables the digital input filter.
  - Minimum Pulse Width (ms)—Configures the minimum pulse width of the
 digital input filter. Pulses that are shorter than the minimum pulse
 width will be filtered out (Applies only when Digital Filter is
 enabled).
  - Threshold (V)—Sets the threshold value for the counter (Applies only to
 terminals that are not differential).

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/cRIO-9401_Advanced_Configuration_Dialog_Box.html language=enus -->
## TOPIC 00067: Advanced Configuration Dialog Box (FPGA Interface) 2

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/cRIO-9401_Advanced_Configuration_Dialog_Box.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/cRIO-9401_Advanced_Configuration_Dialog_Box.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Advanced button on the C Series Module Properties dialog box for the NI 9401, NI 9472, NI 9474, NI 9475, NI 9481, or NI 9485 to display this dialog box. Use this dialog box to configure the number of output synchronizing registers for each DO channel in a single-cycle Timed Loop. This dial

### Advanced Configuration Dialog Box (FPGA Interface) 2

Click the Advanced button on the [C Series Module
 Properties](9472_Propertiesdialog.html) dialog box for the [NI
 9401](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9401), [NI 9472](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9472), [NI 9474](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9474), [NI 9475](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9475), [NI 9481](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9481), or [NI 9485](https://ni.com/docs/en-US/csh?context=ni-compactrio_criodevicehelp_crio-9485) to display
 this dialog box.

Use this dialog box to configure the number of output
 synchronizing registers for each DO channel in a single-cycle Timed Loop.

This dialog box includes the following components:

- Channels —Select the channel for which you want to
 configure the number of output synchronizing registers.
- Channel Configuration —Specifies the number of
 synchronizing registers between the DO channel executing on the FPGA target and
 the FPGA target hardware interface. The FPGA target hardware interface might be
 a physical I/O connector on the device or a connection to a section of the FPGA
 that contains circuitry designed by NI. Each synchronizing register executes in
 one clock cycle. Caution Select 0 only if
 you also use the IP Integration Node and the code contains its own
 synchronization registers.
  - 0 —Specifies that the FPGA VI uses no
 synchronizing registers. Do not select this option for most FPGA Module
 applications. Note If you select 0
 for digital output resources in a single-cycle Timed Loop, you
 create a combinatorial circuit between the two resources. The
 combinatorial circuit might cause glitches on the output
 signal.
  - 1 —Specifies that the FPGA VI uses one
 synchronizing register between the DO channel and the FPGA target
 hardware interface.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criodevicehelp/FPGA_IO_channel_config.html language=enus -->
## TOPIC 00068: Channel Configuration Page (FPGA I/O Properties Dialog Box)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criodevicehelp/FPGA_IO_channel_config.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criodevicehelp/FPGA_IO_channel_config.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: FPGA Module Select Channel Configuration in the Category list of the FPGA I/O Properties dialog box to display this page. Use this page to configure channel options. This page displays only the options and values supported by the selected FPGA I/O. Some FPGA targets might not allow access

### Channel Configuration Page (FPGA I/O Properties Dialog Box)

Requires: FPGA Module

Select Channel
 Configuration in the Category list of the
 FPGA I/O Properties dialog box to display this page.

Use this page to
 configure channel options. This page displays only the options and values supported
 by the selected FPGA I/O. Some FPGA targets might not allow access to this page at
 all.

This page can contain the following options:

- Terminal Mode —Specifies the terminal mode for the
 channel. This option can include RSE and
 DIFF .
- Voltage Range —Specifies the voltage range for the
 channel. This option can include ±10V ,
 ±5V , ±2V , and
 ±1V .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=criomax/topic-help/IDD_SOFT_SWITCH_DIALOG.html language=enus -->
## TOPIC 00069: Controller Settings

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `criomax/topic-help/IDD_SOFT_SWITCH_DIALOG.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/criomax/topic-help/IDD_SOFT_SWITCH_DIALOG.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: On this tab, you can configure settings for the CompactRIO controller. If you format the hard drive of the controller, these settings revert to the default condition, which is off. What do you want to do? Restore the factory default network settings of the controller so that it attempts to establish

### Controller Settings

On this tab, you can configure settings for the CompactRIO controller. If you
 format the hard drive of the controller, these settings revert to the default
 condition, which is off.

#### What do you want to do?

#### Restore the factory default network settings of the controller so that it
 attempts to establish a new DHCP connection.

When you reboot the controller with the IP Reset setting on, the controller attempts
 to establish a new DHCP connection. If it fails, it assigns itself a link-local IP
 address. Place a check in the IP Reset box, click
 Save, and restart the controller to establish a new DHCP
 connection.

#### Enable or disable startup applications.

To disable a LabVIEW Real-Time startup application, place a check in the
 Disable RT Startup App box and click
 Save before restarting the controller. To disable a
 LabVIEW FPGA startup application, place a check in the Disable FPGA
 Startup App box and click Save before
 restarting the controller. Restarting the controller in safe mode also disables all
 startup applications.

#### See what version of LabVIEW is installed on the controller, check the IP
 address, or diagnose unexplained controller behavior.

You can use Console Out and a serial terminal program to check the LabVIEW version
 and IP address of the controller or to help you in troubleshooting. Complete the
 following steps to use Console Out:

1. Use a null-modem cable to connect the serial port of the controller to the
 serial port of the host computer.
2. Configure the serial terminal on the host computer with the following settings:
  - 9,600 bits per second
  - Eight data bits
  - No parity
  - One stop bit
  - No flow control
3. Place a check in the Console Out box on this tab.
4. Click Save .
5. Restart the controller.

#### Format the hard drive of the controller.

To format the hard drive, right-click the controller item under Remote
 Systems and select Format Disk from the
 shortcut menu. If you format the controller, all controller settings on this tab
 revert to the default condition, which is off.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=cserieshelp/add_module.html language=enus -->
## TOPIC 00070: New C Series Module Dialog Box

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `cserieshelp/add_module.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/cserieshelp/add_module.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click the FPGA Target or chassis item in the Project Explorer window and select New»C Series Modules to display the Add Targets and Devices dialog box. Select New target or device, select C Series Module, and click the OK button to display the New C Series Module dialog box. Use this dialog bo

### New C Series Module Dialog Box

Right-click the FPGA Target or chassis item in the Project
 Explorer window and select New»C Series
 Modules to display the Add Targets and Devices dialog box. Select
 New target or device, select C Series
 Module, and click the OK button to display
 the New C Series Module dialog box.

Use this dialog
 box to select a module name, the type of module, and the chassis slot in which the
 module is installed.

This dialog box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Type —Specifies the type of C Series module you want to
 add to the chassis in the Project Explorer window.
- Location —Specifies a slot in the chassis for the C Series
 module.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=cserieshelp/add_RMC.html language=enus -->
## TOPIC 00071: New RIO Mezzanine Card Dialog Box

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `cserieshelp/add_RMC.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/cserieshelp/add_RMC.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click the FPGA Target in the Project Explorer window and select New»RIO Mezzanine Card to display this dialog box. Use this dialog box to enter a RIO mezzanine card name and select the type of RIO mezzanine card. Name—You can use this text box to enter a name for the RIO mezzanine card. Type—Y

### New RIO Mezzanine Card Dialog Box

Right-click the FPGA Target in the Project Explorer
 window and select New»RIO Mezzanine Card to display this
 dialog box. Use this dialog box to enter a RIO mezzanine card name and select the
 type of RIO mezzanine card.

- Name —You can use this text box to enter a name for the
 RIO mezzanine card.
- Type —You can use this pull-down menu to select the type
 of RIO mezzanine card.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=cserieshelp/cRIO_Chassis_Properties_rt.html language=enus -->
## TOPIC 00072: CompactRIO or Single-Board RIO Chassis Properties Dialog Box

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `cserieshelp/cRIO_Chassis_Properties_rt.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/cserieshelp/cRIO_Chassis_Properties_rt.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click a CompactRIO or Single-Board RIO chassis in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a CompactRIO or Single-Board RIO chassis. This dialog box includes the following components: Name—Specifies th

### CompactRIO or Single-Board RIO Chassis Properties Dialog Box

Right-click a CompactRIO or Single-Board RIO chassis in the Project
 Explorer window and select Properties from
 the shortcut menu to display this dialog box.

Use this dialog box to
 configure a CompactRIO or Single-Board RIO chassis.

This dialog box includes
 the following components:

- Name —Specifies the name of the chassis, which appears in
 the Project Explorer window. You can use this field to
 give the chassis a descriptive name.
- Type —Specifies the type of chassis. You cannot change
 this value.
- Programming Mode —You can specify the programming mode for
 the chassis here. Note Some chassis do not support Scan Interface programming
 mode. However, in LabVIEW FPGA Interface mode, you can [use the Scan Interface for individual modules](https://ni.com/docs/en-US/csh?context=ni-compactrio_target6devicehelp_scan_interface_for_modules_rt) even with some chassis that do not support Scan Interface
 programming mode. Refer to Software Support for CompactRIO, CompactDAQ,
 Single-Board RIO, R Series, and
 EtherCAT
 for information about which controllers and chassis support use of the Scan
 Interface for individual modules. Note Changing the programming mode will take effect the next
 time you deploy setting to the chassis. To deploy settings, right-click the
 chassis item in the Project Explorer window and
 select Deploy from the shortcut menu.
  - Scan Interface —Enables you to use C Series
 modules directly from LabVIEW Real-Time. Modules that you use in Scan
 Interface mode appear under the Real-Time Scan Resources item in the
 Project Explorer window.
  - LabVIEW FPGA Interface —Enables you to use C
 Series modules from LabVIEW FPGA VIs. Modules that you use in LabVIEW
 FPGA Interface mode appear directly under the FPGA Target in the
 Project Explorer window.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=cserieshelp/discovery_status_rt.html language=enus -->
## TOPIC 00073: CompactRIO Discovery Status Dialog Box

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `cserieshelp/discovery_status_rt.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/cserieshelp/discovery_status_rt.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: When you add a CompactRIO controller or chassis or a Single-Board RIO device to a LabVIEW project, LabVIEW finds all C Series modules in the new system. This dialog box appears if LabVIEW returns errors while looking for C Series modules installed in the system. The Description field contains inform

### CompactRIO Discovery Status Dialog Box

When you add a CompactRIO controller or chassis or a Single-Board RIO device to
 a LabVIEW project, LabVIEW finds all C Series modules in the new system.

This
 dialog box appears if LabVIEW returns errors while looking for C Series modules
 installed in the system. The Description field contains
 information about each type of error condition.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=cserieshelp/enet_RIO_general.html language=enus -->
## TOPIC 00074: Ethernet RIO General Properties Page

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `cserieshelp/enet_RIO_general.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/cserieshelp/enet_RIO_general.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Project Explorer window, right-click an Ethernet RIO target and select Properties from the shortcut menu to display the Ethernet RIO Properties dialog box. Select General from the Category list to display this page. This page includes the following components: Name—Defines the name for the Et

### Ethernet RIO General Properties Page

In the Project Explorer window, right-click an Ethernet RIO target and select
 Properties from the shortcut menu to display the
 Ethernet RIO Properties dialog box. Select
 General from the Category list to
 display this page.

This page includes the following components:

- Name —Defines the name for the Ethernet RIO target.
- IP Address / DNS Name —Defines the IP address or DNS name
 server name for the Ethernet RIO target.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=cserieshelp/MXIe_Chassis_Properties_rt.html language=enus -->
## TOPIC 00075: MXIe-RIO Chassis Properties Dialog Box

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `cserieshelp/MXIe_Chassis_Properties_rt.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/cserieshelp/MXIe_Chassis_Properties_rt.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click a MXIe-RIO chassis in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a MXIe-RIO chassis. This dialog box includes the following components: Name—Specifies the name of the chassis, which appears in the

### MXIe-RIO Chassis Properties Dialog Box

Right-click a MXIe-RIO chassis in the Project Explorer
 window and select Properties from the shortcut menu to
 display this dialog box.

Use this dialog box to configure a MXIe-RIO chassis.

This dialog box includes the following components:

- Name —Specifies the name of the chassis, which appears in
 the Project Explorer window. You can use this field to
 give the chassis a descriptive name.
- Type —Specifies the type of chassis. You cannot change
 this value.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=cserieshelp/program_mode_rt.html language=enus -->
## TOPIC 00076: Select Programming Mode Dialog Box

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `cserieshelp/program_mode_rt.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/cserieshelp/program_mode_rt.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this dialog box to select the programming mode you want to start programming the system with. You can change the programming mode later using the CompactRIO Chassis Properties dialog box. The Select Programming Mode dialog box appears when you add a chassis that supports the Scan Interface to yo

### Select Programming Mode Dialog Box

Use this dialog box to select the programming mode you want to start programming
 the system with. You can change the programming mode later using the [CompactRIO Chassis Properties](cRIO_Chassis_Properties_rt.html) dialog box. The Select
 Programming Mode dialog box appears when you add a chassis that
 supports the Scan Interface to your project and you have the LabVIEW FPGA Module
 installed on the host computer.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=cserieshelp/RIO_ENet_Chassis_Properties.html language=enus -->
## TOPIC 00077: Ethernet RIO Chassis Properties Dialog Box

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `cserieshelp/RIO_ENet_Chassis_Properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/cserieshelp/RIO_ENet_Chassis_Properties.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an Ethernet RIO chassis in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure an Ethernet RIO chassis. This dialog box includes the following components: Name—Specifies the name of the chassis, which appea

### Ethernet RIO Chassis Properties Dialog Box

Right-click an Ethernet RIO chassis in the Project
 Explorer window and select Properties from
 the shortcut menu to display this dialog box.

Use this dialog box to
 configure an Ethernet RIO chassis.

This dialog box includes the following
 components:

- Name —Specifies the name of the chassis, which appears in
 the Project Explorer window. You can use this field to
 give the chassis a descriptive name.
- Type —Specifies the type of chassis. You cannot change
 this value.
- Programming Mode —You can specify the programming mode for
 the chassis here. Note Some chassis do not support Scan Interface programming
 mode. However, you can compile [Scan
 Interface support for individual modules](https://ni.com/docs/en-US/csh?context=ni-compactrio_target6devicehelp_scan_interface_for_modules_rt) into your application. Note Changing the programming mode will take effect the next
 time you deploy setting to the chassis. To deploy settings, right-click the
 chassis item in the Project Explorer window and
 select Deploy from the shortcut menu.
  - Scan Interface —Enables you to use C Series
 modules directly from LabVIEW Real-Time. Modules that you use in Scan
 Interface mode appear under the Real-Time Scan Resources item in the
 Project Explorer window.
  - LabVIEW FPGA Interface —Enables you to use C
 Series modules from LabVIEW FPGA VIs. Modules that you use in LabVIEW
 FPGA Interface mode appear directly under the FPGA Target in the
 Project Explorer window.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=lvaddon11/987x_9870_Propertiesdialog.html language=enus -->
## TOPIC 00078: C Series Module Properties Dialog Box for the NI 9870

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `lvaddon11/987x_9870_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/lvaddon11/987x_9870_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: CompactRIO Serial 4-Port, RS232 Module (DTE interface) Right-click an NI 9870 C Series serial module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series serial module. This dialog box includes the followi

### C Series Module Properties Dialog Box for the NI 9870

CompactRIO Serial 4-Port, RS232 Module (DTE interface)

Right-click an
 [NI 9870](https://ni.com/docs/en-US/csh?context=ni-compactrio_lvaddon11_crio_9870) C Series serial
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series serial module.

This
 dialog box includes the following components:

- Name —Specifies the name of the C Series serial module,
 which appears in the Project Explorer window.
- Module Type —Specifies the type of C Series serial module.
 You cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 serial module.
- Desired Baud Rate (bps) —Specifies the target baud rate
 for the port. To enter a non-standard rate, select
 <Other> and type in the desired value. Note If you define a desired baud rate, the prescaler and divider
 will be automatically defined by the software to achieve a baud rate as
 close to the target as possible, but because the prescaler and divider are
 integers used as divisors to a floating point constant, not every actual
 baud rate will necessarily be an integer. Since the prescaler and divider
 must be integers, not every desired baud rate is
 possible with the hardware. Querying the Actual Baud Rate returns the
 precise result used by the software.
- Actual Baud Rate (bps) —Returns the actual baud rate
 closest to the Desired Baud Rate. The Actual Baud Rate is calculated with the
 following equation: Actual Baud Rate = 3.6864 Mbps / (Prescaler *
 Divider) The maximum is 921.6 Kbps, and the minimum is 14 bps.
- Divider —Returns the divider for the desired baud rate as
 an unsigned 16-bit value within the range 4–65535. Note The
 divider is set automatically in the C Series Module
 Properties dialog box according to the Desired Baud Rate. To
 set a custom baud rate programmatically, use this dialog box as a calculator
 to find the necessary divider for the desired custom baud rate. Then pass
 this value in as an integer to the I/O property Baud Rate Divider on your
 block diagram.
- Prescaler —Returns the prescaler for the desired baud
 rate, either 1 or 4. A value of 4 is normally used only for very low baud rates.
 Note The prescaler is set automatically in the C
 Series Module Properties dialog box according to the Desired
 Baud Rate. To set a custom baud rate programmatically, use this dialog box
 as a calculator to find the necessary prescaler for the desired custom baud
 rate. Then pass this value in to the I/O property Baud Rate Prescaler on
 your block diagram.
- % Error —Returns the percentage of error in accuracy
 between the Desired Baud Rate and the Actual Baud Rate.
- Parity —Specifies the
 parity
 used with every frame that is transmitted or received. Valid values are
 None , Odd ,
 Even , Mark , and
 Space . The default parity is
 None .
- Data Bits —Specifies the number of data bits contained in
 each frame. Valid values are 5 , 6 ,
 7 , and 8 . If you select 5 data
 bits, you can select only 1 or 1.5 stop bits. If you select 6, 7, or 8 data
 bits, you can select only 1 or 2 stop bits. The default is
 8 .
- Stop Bits —Specifies the number of stop bits used to
 indicate the end of a frame. Valid values are 1 ,
 1.5 , and 2 . You can select
 1.5 stop bits only if you set Data Bits to
 5 , and you can select 2 stop
 bits only if you set Data Bits to 6 ,
 7 , or 8 . The default is
 1 .
- Flow Control —Specifies the flow control method used for
 transmitting and receiving data. Valid values are None ,
 Software XON/XOFF , Hardware
 RTS/CTS . DTR/DSR flow control is not available, but can be
 implemented using DTR State and DSR State properties. Note that if Hardware
 (RTS/CTS) flow control is used, the RTS State write property cannot control the
 RTS state. The default is None .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=lvaddon11/987x_9871_Propertiesdialog.html language=enus -->
## TOPIC 00079: C Series Module Properties Dialog Box for the NI 9871

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `lvaddon11/987x_9871_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/lvaddon11/987x_9871_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: CompactRIO Serial 4-Port, RS485/RS422 Module Right-click an NI 9871 C Series serial module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series serial module. This dialog box includes the following compone

### C Series Module Properties Dialog Box for the NI 9871

CompactRIO Serial 4-Port, RS485/RS422 Module

Right-click an [NI 9871](https://ni.com/docs/en-US/csh?context=ni-compactrio_lvaddon11_crio_9871) C Series serial
 module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series serial module.

This
 dialog box includes the following components:

- Name —Specifies the name of the C Series serial module,
 which appears in the Project Explorer window.
- Module Type —Specifies the type of C Series serial module.
 You cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 serial module.
- Desired Baud Rate (bps) —Specifies the target baud rate
 for the port. To enter a non-standard rate, select
 <Other> and type in the desired value. Note If you define a desired baud rate, the prescaler and divider
 will be automatically defined by the software to achieve a baud rate as
 close to the target as possible, but because the prescaler and divider are
 integers used as divisors to a floating point constant, not every actual
 baud rate will necessarily be an integer. Since the prescaler and divider
 must be integers, not every desired baud rate is
 possible with the hardware. Querying the Actual Baud Rate returns the
 precise result used by the software.
- Actual Baud Rate (bps) —Returns the actual baud rate
 closest to the Desired Baud Rate. The Actual Baud Rate is calculated with the
 following equation: Actual Baud Rate = 3.6864 Mbps / (Prescaler *
 Divider) The maximum is 3.6864 Mbps, and the minimum is 14 bps.
- Divider —Returns the divider for the desired baud rate as
 an unsigned 16-bit value within the range 1–65535. Note The
 divider is set automatically in the C Series Module
 Properties dialog box according to the Desired Baud Rate. To
 set a custom baud rate programmatically, use this dialog box as a calculator
 to find the necessary divider for the desired custom baud rate. Then pass
 this value in as an integer to the I/O property Baud Rate Divider on your
 block diagram.
- Prescaler —Returns the prescaler for the desired baud
 rate, either 1 or 4. A value of 4 is normally used only for very low baud rates.
 Note The prescaler is set automatically in the C
 Series Module Properties dialog box according to the Desired
 Baud Rate. To set a custom baud rate programmatically, use this dialog box
 as a calculator to find the necessary prescaler for the desired custom baud
 rate. Then pass this value in to the I/O property Baud Rate Prescaler on
 your block diagram.
- % Error —Returns the percentage of error in accuracy
 between the Desired Baud Rate and the Actual Baud Rate.
- Parity —Specifies the
 parity
 used with every frame that is transmitted or received. Valid values are
 None , Odd ,
 Even , Mark , and
 Space . The default parity is
 None .
- Transceiver Mode —Specifies the current RS485
 wire/transceiver mode. Valid values are: Table 29.ModeTransmitterReceiver4 WireAlways enabledAlways enabled2 Wire DTR Controlled with EchoEnabled when DTR assertedAlways enabled2 Wire DTR ControlledEnabled when DTR assertedEnabled when DTR unasserted2 Wire AutoEnabled when transmitting dataEnabled when not transmitting data Note Two-wire mode: Auto Control disables the handshaking lines,
 and this mode supercedes both Hardware Flow Control and the RTS State
 property.
- Flow Control —Specifies the flow control method used for
 transmitting and receiving data. Valid values are None ,
 Software XON/XOFF , Hardware
 RTS/CTS . DTR/DSR flow control is not available, but can be
 implemented using DTR State and DSR State properties. DTR/DSR flow control is
 not available, but can be implemented using DTR State and DSR State properties.
 Note that if Hardware (RTS/CTS) flow control is used, the RTS State write
 property cannot control the RTS state. The default is
 None .
- Data Bits —Specifies the number of data bits contained in
 each frame. Valid values are 5 , 6 ,
 7 , and 8 . If you select 5 data
 bits, you can select only 1 or 1.5 stop bits. If you select 6, 7, or 8 data
 bits, you can select only 1 or 2 stop bits. The default is
 8 .
- Stop Bits —Specifies the number of stop bits used to
 indicate the end of a frame. Valid values are 1 ,
 1.5 , and 2 . You can select
 1.5 stop bits only if you set Data Bits to
 5 , and you can select 2 stop
 bits only if you set Data Bits to 6 ,
 7 , or 8 . The default is
 1 .

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=lvaddon11/987x_Errors.html language=enus -->
## TOPIC 00080: C Series Serial Module Error Codes

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `lvaddon11/987x_Errors.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/lvaddon11/987x_Errors.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use of error terminals for Serial development is recommended. For some Serial nodes, the error terminals are essential. For example, you may need to evaluate error out from a Serial Input node to determine if a data error occurred while reading bytes. The only cost of using error terminals is slight

### C Series Serial Module Error Codes

Use of error terminals for Serial development is recommended. For some Serial
 nodes, the error terminals are essential. For example, you may need to evaluate
 error out from a Serial Input node to determine if a data
 error occurred while reading bytes. The only cost of using error terminals is slight
 FPGA gate usage, not performance.

To detect errors, right-click the Serial
 node in the diagram and select Show Error Terminals. The
 resulting error in and error out
 terminals provide the standard LabVIEW error cluster for error handling.

[Some error descriptions](../target6devicehelp/CompactRIO_Error_Codes.html) in the Explain Error
 dialog box are generic to all CompactRIO modules. The following table provides
 information specific to C Series serial modules.

| Code | Description |
| --- | --- |
| 65570 | An external power error has occurred since the last time the module was accessed. Ensure that power (8–28VDC) is correctly applied to the VSUP and COM terminals on the front panel of the module. |
| 65571 | An over-temperature error has occurred since the last time the module was accessed. Check for fault conditions or extraneous voltages on the I/O port. |
| 65572 | A serial break has occurred (the RXD input was held at SPACE for at least one byte time frame). |
| 65573 | A framing error has occurred in the data being read. Check the serial cable connections and module configuration options such as Baud Rate, Stop Bits, and Data Bits. |
| 65574 | A parity error has occurred in the data being read. Ensure that the module Parity is configured correctly. |
| 65575 | An overrun error has occurred in the data being read. Ensure that the module Flow Control is configured correctly. |

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=riodevicesetup/RIODeviceutility.html language=enus -->
## TOPIC 00081: RIO Device Setup

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `riodevicesetup/RIODeviceutility.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/riodevicesetup/RIODeviceutility.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RIO Device Setup dialog box to download a bitfile to the flash memory on an FPGA device. LabVIEW creates a bitfile when you compile an FPGA VI. You also can use this dialog box to configure when the bitfile loads from flash memory, which analog input mode the device uses for measurements, an

### RIO Device Setup

Use the RIO Device Setup dialog box to download a bitfile
 to the flash memory on an FPGA device. LabVIEW creates a bitfile when you compile an
 FPGA VI. You also can use this dialog box to configure when the bitfile loads from
 flash memory, which analog input mode the device uses for measurements, and whether
 the device clock is synchronized to the clock of the PXI chassis. You can use one of
 the following methods to launch the RIO Device Setup dialog
 box:

- Right-click the FPGA target to which you want to download a bitfile in the
 Project Explorer window in LabVIEW and select
 RIO Device Setup from the shortcut menu to display
 the RIO Device Setup dialog box.
- Select Start»All Programs»NI»RIO Device Setup to display
 the RIO Device Setup dialog box. When you display the
 dialog box in this manner, you must select the FPGA target to which you want to
 download a bitfile from the Device pull-down menu.

The RIO Device Setup dialog box includes the following
 components:

- Resource —Select the FPGA device to which you want to
 download the bitfile.
- Download Bitfile to Flash —Includes the following
 components:
  - Bitfile to Download —Determines the bitfile to
 download to flash memory on the FPGA device. The VI must be compiled for
 the device.
  - Download Bitfile —Downloads the bitfile to flash
 memory of the device.
  - Erase Bitfile on Flash —Deletes the existing
 bitfile on the flash memory of the device. Downloading a new bitfile
 also deletes any existing bitfile.
- Device Settings —Includes the following components:
  - Load VI from Flash Memory —Determines when the
 bitfile loads to the FPGA from flash memory.
    - Do not autoload VI —Does not load the
 bitfile from flash memory at startup.
    - Autoload VI on device powerup —Loads the
 bitfile that is stored in flash memory to the FPGA when the
 system powers up.
    - Autoload VI on device reboot —Loads the
 bitfile that is stored in flash memory to the FPGA when you
 reboot the system either with or without cycling power.
  - Analog Input Mode —Determines which measurement
 system the device uses. This option is available only for analog input
 devices.
    - Differential —Uses a measurement system in
 which you do not need to connect either input to a fixed
 reference, such as earth or building ground.
    - Referenced single-ended —Uses a
 measurement system in which all measurements are made with
 respect to a common reference or a ground.
    - Nonreferenced single-ended —Uses a
 measurement system in which all measurements are made with
 respect to a common reference, but the voltage at this reference
 can vary with respect to the measurement system ground.
  - Synchronize FPGA clock to PXI/PXI_Clk10 —Phase
 locks the NI 78 xx R clock to the 10 MHz clock of the
 PXI chassis. This option is available only for
 NI PXI-78 xx R devices.
 FlexRIO PXI-795 x R devices automatically
 synchronize to the PXI_Clk10 of the PXI chassis. This setting does not
 take effect until you reset the device. Note 
 FlexRIO PXIe-796xR devices automatically
 synchronize to the PXIe/PXIe_Clk100 of the PXIe chassis. The
 Synchronize FPGA clock to PXI/PXI_Clk10
 option is not available on these devices.
  - Apply Settings —Downloads the settings you
 configured.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=sbriohelp/9651_properties.html language=enus -->
## TOPIC 00082: General Page (sbRIO-9651 Socket Properties Dialog Box)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `sbriohelp/9651_properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/sbriohelp/9651_properties.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Component-Level IP Properties dialog box for the sbRIO-9651, select General from the Category list to display this page, which you can use to select a socketed CLIP you created for the sbRIO-9651. This page includes the following options: sbRIO-9651 Socketed Component Level IP Declaration—The

### General Page (sbRIO-9651 Socket Properties Dialog Box)

In the Component-Level IP Properties dialog box for the [sbRIO-9651](https://ni.com/docs/en-US/csh?context=ni-compactrio_sbriohelp_ni_9651), select
 General from the Category list to
 display this page, which you can use to select a [socketed CLIP you created](https://ni.com/docs/en-US/csh?context=ni-compactrio_sbriohelp_9651_clip) for the
 sbRIO-9651.

This page includes the following options:

- sbRIO-9651 Socketed Component Level IP Declaration —The
 socketed CLIP to add to the LabVIEW project. The drop-down list includes all
 CLIP declarations saved in the following directories, or you can browse for a
 CLIP declaration saved in a different location: Note Leave <Select CLIP Declaration>
 selected if you do not want the socket to use a CLIP. All I/O on the
 sbRIO-9651 connector will be unused. Note If the selected CLIP declaration is invalid, you cannot
 navigate to other pages of or click the OK button in
 the Component-Level IP Properties dialog box. Cancel the Component-Level IP
 Properties dialog box and correct any errors in the CLIP declaration before
 you try selecting the CLIP declaration in the Component-Level IP Properties
 dialog box again.
  - Documents\LabVIEW Data\CompactRIO\CLIPs\sbRIO-9651 —The
 directory in which the sbRIO CLIP Generator saves created CLIPs.
  - <NI>\Shared\CompactRIO\CLIPs —The directory in
 which CLIPs may be distributed by an installer.
- Description —The description you provided in the sbRIO
 CLIP Generator for the selected CLIP declaration.

#### Related Topics

[Getting Started with the sbRIO-9651 in LabVIEW](https://ni.com/docs/en-US/csh?context=ni-compactrio_sbriohelp_9651_start)

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=sbriohelp/9683_Propertiesdialog.html language=enus -->
## TOPIC 00083: RIO Mezzanine Card Properties Dialog Box for the NI 9683 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `sbriohelp/9683_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/sbriohelp/9683_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9683 RIO Mezzanine Card (RMC) in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure an RMC. This dialog box includes the following components: Name—Specifies the name of the RMC, which appears in the

### RIO Mezzanine Card Properties Dialog Box for the NI 9683 (FPGA Interface)

Right-click an [NI 9683](https://ni.com/docs/en-US/csh?context=ni-compactrio_sbriohelp_rmc_9683) RIO Mezzanine Card
 (RMC) in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure an RMC.

This dialog box includes
 the following components:

- Name —Specifies the name of the RMC, which appears in the
 Project Explorer window. LabVIEW assigns a default
 name to the device. You can use this field to give the device a descriptive
 name.
- Type —Specifies the type of RMC. You cannot change this
 option.
- Scaling Mode —Sets the scaling mode for the RMC. Select
 Scaled if you want the FPGA I/O Node to return
 scaled, fixed-point data from the device in units of volts. The fixed-point data
 is signed, with a word length of 20 bits and an integer word length of 5 bits
 for simultaneous AI and unsigned, with a word length of 16 bits and an integer
 word length of 3 bits for scanned AI and AO. Select Raw 
 if you want the FPGA I/O Node to return unscaled, binary data from the device.
 If you select Raw , you must scale the
 analog input values in the host VI. The default is
 Scaled .
- Simultaneous AI - Default Voltage Range —Specifies the
 input range for each simultaneous analog input bank. The NI 9683 contains eight
 banks consisting of two channels each.
- Sinking DO - Disable Arbitration —Place a checkmark in
 this checkbox if you want to change the arbitration setting to Never Arbitrate
 and reduce the amount of FPGA logic used by VIs. Check this box only if you are
 sure that the design of the FPGA VI will never allow more than one digital
 function to execute at the same time, even on different channels. If more than
 one digital function could execute simultaneously in the FPGA VI, leave the box
 unchecked to keep the default Arbitrate if Multiple Requestors Only arbitration
 setting.
- LVTTL DIO - Initial Line Direction —Sets the initial line
 direction for each LVTTL DIO channel to input or output. The default is input.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=sbriohelp/9684_Propertiesdialog.html language=enus -->
## TOPIC 00084: RIO Mezzanine Card Properties Dialog Box for the sbRIO-9684 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `sbriohelp/9684_Propertiesdialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/sbriohelp/9684_Propertiesdialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an sbRIO-9684 RIO Mezzanine Card (RMC) in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure an RMC. This dialog box includes the following components: Name—Specifies the name of the RMC, which appears in

### RIO Mezzanine Card Properties Dialog Box for the sbRIO-9684 (FPGA Interface)

Right-click an [sbRIO-9684](https://ni.com/docs/en-US/csh?context=ni-compactrio_sbriohelp_rmc_9684) RIO Mezzanine Card
 (RMC) in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure an RMC.

This dialog box includes
 the following components:

- Name —Specifies the name of the RMC, which appears in the
 Project Explorer window. LabVIEW assigns a default
 name to the device. You can use this field to give the device a descriptive
 name.
- Type —Specifies the type of RMC. You cannot change this
 option.
- Scaling Mode —Sets the scaling mode for the RMC. Select
 Scaled if you want the FPGA I/O Node to return
 scaled, fixed-point data from the device in units of volts. The fixed-point data
 is signed, with a word length of 20 bits and an integer word length of 5 bits
 for simultaneous AI and unsigned, with a word length of 16 bits and an integer
 word length of 3 bits for scanned AI and AO. Select Raw 
 if you want the FPGA I/O Node to return unscaled, binary data from the device.
 If you select Raw , you must scale the
 analog input values in the host VI. The default is
 Scaled .
- Simultaneous AI - Default Voltage Range —Specifies the
 input range for each simultaneous analog input bank. The sbRIO-9684 contains
 eight banks consisting of two channels each.
- Sinking DO - Disable Arbitration —Place a checkmark in
 this checkbox if you want to change the arbitration setting to Never Arbitrate
 and reduce the amount of FPGA logic used by VIs. Check this box only if you are
 sure that the design of the FPGA VI will never allow more than one digital
 function to execute at the same time, even on different channels. If more than
 one digital function could execute simultaneously in the FPGA VI, leave the box
 unchecked to keep the default Arbitrate if Multiple Requestors Only arbitration
 setting.
- LVTTL DIO - Initial Line Direction —Sets the initial line
 direction for each LVTTL DIO channel to input or output. The default is input.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=sbriohelp/custom_baud_rate.html language=enus -->
## TOPIC 00085: Custom Baud Rate Dialog Box

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `sbriohelp/custom_baud_rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/sbriohelp/custom_baud_rate.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This dialog configures advanced properties for the CAN port when in classical CAN or FD + BRS CAN mode. You can access this dialog from the FPGA I/O Properties dialog box. Baud Rate Specifies the custom Baud Rate for the transceiver when in classical CAN mode or when transmitting data before the BRS

### Custom Baud Rate Dialog Box

This dialog configures advanced properties for the CAN port when in classical
 CAN or FD + BRS CAN mode. You can access this dialog from the [FPGA I/O Properties dialog
 box](sbcombo_fpga_io_properties.html).

#### Baud Rate

Specifies the custom Baud Rate for the transceiver when in classical CAN mode or when
 transmitting data before the BRS bit in CAN FD + BRS mode. The default Baud Rate is
 500 kb/s.

#### Bit Timing Register

Specifies the custom CAN baud rate by setting the nominal Bit Timing and Prescaler
 register of the CAN controller. The fields are:

- Time quantum (Tq) —Programs the baud rate prescaler. Valid
 values are 25 to 12800, in increments of 0x19 (25 decimal). The default Tq is
 50.
- Synchronization Jump Width (SJW) —Valid values are 0 to
 127. The default SJW is 4. The actual hardware interpretation of this value is
 one more than the programmed value.
- Time Segment 1 (TSEG1) —Time segment before the sample
 point. Valid values are 1 to 0xFF (1 to 255 decimal). The default TSEG1 is 33.
 The actual hardware interpretation of this value is one more than the programmed
 value.
- Time Segment 2 (TSEG2) —Time segment after the sample
 point. Valid values are 0 to 0x7F (0 to 127 decimal). The default TSEG2 is 4.
 The actual hardware interpretation of this value is one more than the programmed
 value.

#### Sample Point

Specifies the custom sample point in classical CAN mode or when transmitting data
 before the BRS bit in CAN FD + BRS mode. The default sample point is 87.5%.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=sbriohelp/custom_fd_baud_rate.html language=enus -->
## TOPIC 00086: Custom FD Baud Rate Dialog Box

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `sbriohelp/custom_fd_baud_rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/sbriohelp/custom_fd_baud_rate.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This dialog box allows you to configure advanced properties for the CAN port when in FD or FD + BRS CAN mode. You can access this dialog from the FPGA I/O Properties Page. FD Baud Rate Specifies the custom Baud Rate for the transceiver when transmitting data after the BRS bit in FD + BRS CAN mode. T

### Custom FD Baud Rate Dialog Box

This dialog box allows you to configure advanced properties for the CAN port
 when in FD or FD + BRS CAN mode. You can access this dialog from the [FPGA I/O Properties
 Page.](sbcombo_fpga_io_properties.html)

#### FD Baud Rate

Specifies the custom Baud Rate for the transceiver when transmitting data after the
 BRS bit in FD + BRS CAN mode. The default FD Baud Rate is 500 kb/s.

#### Bit Timing Register

Specifies the custom CAN FD baud rate with flexible data rate by setting the data Bit
 Timing and Prescaler register of the CAN controller. The fields are:

- Time quantum (Tq) —Programs the baud rate prescaler. Valid
 values are 25 to 800, in increments of 25 ns. The default Tq is 100.
- Synchronization Jump Width (SJW) —Valid values are 0 to
 15. The default SJW is 3. The actual hardware interpretation of this value is
 one more than the programmed value.
- Time Segment 1 (TSEG1) —Time segment before the sample
 point. Valid values are 0 to 31. The default TSEG1 is 14. The actual hardware
 interpretation of this value is one more than the programmed value.
- Time Segment 2 (TSEG2) —Time segment after the sample
 point. Valid values are 0 to 15. The default TSEG2 is 3. The actual hardware
 interpretation of this value is one more than the programmed value.
- Transmitter Delay Compensation (TDC) —Enables or disables
 this feature. Table 15.Unchecked (default)TDC disabledCheckedTDC enabled
- Transmitter Delay Compensation Offset (TDCO) —Defines the
 distance between the delay from transmit to receive point and secondary sample
 point. Valid values are 0 to 127. The default TDCO is 0.
- Transmitter Delay Compensation Filter Window Length
 (TDCF) —Defines the minimum value for the secondary sample point
 position. It is enabled when TDCF is greater than TDCO. Valid values are 0 to
 127. The default TDCF is 0.

#### Sample Point

Specifies the custom sample point in classical CAN FD mode or when transmitting data
 before the BRS bit in CAN FD + BRS mode. The default sample point is 80.0%.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=sbriohelp/sbcombo_fpga_io_properties.html language=enus -->
## TOPIC 00087: CAN FPGA I/O Properties Dialog Box

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `sbriohelp/sbcombo_fpga_io_properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/sbriohelp/sbcombo_fpga_io_properties.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The CAN FPGA I/O Properties dialog box includes the following properties that you can use to configure the CAN functionality. To open the dialog box, right-click CAN0 in the Project Explorer window and select Properties. Baud Rate This property specifies the Baud Rate for the transceiver when in cla

### CAN FPGA I/O Properties Dialog Box

The CAN FPGA I/O Properties dialog box includes the following properties that
 you can use to configure the CAN functionality. To open the dialog box, right-click
 CAN0 in the Project Explorer window and select
 Properties.

#### Baud Rate

This property specifies the Baud Rate for the transceiver when in classical CAN mode
 or when transmitting data before the BRS bit when in CAN FD + BRS mode. You must
 always set Baud Rate even when the I/O Mode is set to CAN FD + BRS because the CAN
 FD + BRS protocol always has a portion of the frame that transfer in classical CAN
 mode.

Typical baud rates are listed as kilobits per second. The supported values are 5.00,
 6.150, 10.00, 12.5, 16.00, 20.00, 25.00, 31.25, 33.33, 40.00, 50.00, 62.50, 80.00,
 83.33, 100.0, 125.0, 160.0, 200.0, 250.0, 400.0, 500.0, 800.0, and 1000. These bit
 fields are selected to create the desired baud rate with a default sample point of
 87.5%. The default baud rate is 500.0 kb/s.

If you prefer a custom sample point, select <Custom> and the [Custom Baud Rate dialog
 box](custom_fd_baud_rate.html) will appear that you can use to determine the values to put in this
 field to obtain the desired sample point.

#### FD Baud Rate

This property specifies the baud rate for the transceiver when in FD + BRS CAN mode
 while transmitting data after the BRS bit. You need to set the FD Baud Rate or FD
 Baud Rate Advanced properties only when the I/O Mode is set to CAN FD + BRS.

Typical FD baud rates are listed as kilobits per second. The supported values are
 200, 250, 400, 500, 800, 1000, 1250, 1600, 2000, 2500, 4000, and 5000. These bit
 fields are selected to create the desired baud rate with a default sample point of
 87.5%. The default FD Baud Rate is 500.0 kb/s.

If you prefer a custom sample point, select <Custom> and the Custom FD Baud
 Rate dialog box will appear that you can use to determine the values to put in this
 field to obtain the desired sample point.

#### I/O Mode

This configures the CAN operating mode. The values are:

| CAN(default) | Default CAN 2.0 |
| --- | --- |
| CAN FD | CAN FD mode as specified in the CAN with Flexible Data-Rate specification, version 1.0 |
| CAN FD + BRS | CAN FD as specified in the CAN with Flexible Data-Rate specification, version 1.0, with the optional Baud Rate Switching enabled. |

#### Input Timeout (ms)

The Input Timeout (ms) property specifies how long to wait for a new frame to be
 received. It is a signed 32-bit integer with a resolution of milliseconds, thus
 allowing a maximum value of approximately 25 days. Special values of 0 (do not wait)
 and -1 (wait indefinitely) are supported. The default input timeout is 10000 ms.

If you specify an Input Timeout (ms) of 0, the CAN Input node will simply check to
 see if a new frame has arrived (non-blocking). If a new frame exists, CAN Input
 returns the frame with an error status of FALSE (success). If no new frame exists,
 CAN Input returns an error status of TRUE (error). Therefore, you must enable Error
 Terminals for the CAN Input node in order to poll for new frames when using an input
 timeout of 0. When an error is returned, you must invoke the CAN Input node again at
 a later time to ensure no data is lost.

#### Output Timeout (ms)

The Output Timeout (ms) property specifies how long to wait for a new element to
 become available, which occurs when a frame from a previous CAN Output transmits
 successfully onto the network. If you specify an Output Timeout (ms) of 0, the CAN
 Output node returns an error status of TRUE (error) if a new element is not
 available in the FIFO (non-blocking). When an error is returned, you must attempt
 CAN Output of the same frame again at a later time. Special values of 0 (do not
 wait) and -1 (wait indefinitely) are supported. The default output timeout is 10000
 ms.

#### Auto Start

This Boolean property indicates whether to invoke the Start method automatically when
 the FPGA VI runs. The default is TRUE (enabled).

When Auto Start is TRUE (enabled), the Start method is invoked automatically when the
 FPGA VI runs, and the Stop method is invoked automatically when the FPGA VI stops
 running. This enables your FPGA VI diagram to begin using CAN Input and CAN Output
 nodes without first using an explicit Start method.

When Auto Start is FALSE (disabled), the Start method is not invoked automatically.
 You must use the Start method in your FPGA VI diagram in order to start
 communication.

#### Log Bus Errors

This Boolean control indicates whether to enable the Log Bus Errors feature for
 logging of bus errors as frames that can be read using the CAN Input node. The
 default is FALSE(disabled).

When Log Bus Errors is TRUE (enabled), the bus errors will be logged as frames and
 can be read using the CAN Input node.

When Log Bus Errors is FALSE (disabled), the bus errors will not be logged and cannot
 be read using the CAN Input node (default).

#### Log Transceiver Faults

This Boolean control indicates whether to enable the Log Transceiver Faults feature
 for logging of transceiver faults as frames that can be read using the CAN Input
 node. The default is FALSE(disabled).

When Log Transceiver Faults is TRUE (enabled), the logging is enabled and the
 transceiver faults will be logged as frames which can be monitored using the CAN
 Input node.

When Log Transceiver Faults is FALSE (disabled), the transceiver faults will not be
 logged as frames.

#### Self Reception

This Boolean control indicates whether to enable the Self Reception feature to echo
 successfully transmitted CAN frames to be read using CAN Input node. The default is
 FALSE(disabled).

When Self Reception is TRUE (enabled), the transmits are echoed.

When Self Reception is FALSE (disabled), the transmits are not echoed.

#### Single Shot Transmit

This Boolean control indicates whether to enable the Single Shot Transmit feature to
 prevent failed CAN frame transmissions from retrying. The default is FALSE
 (disabled).

When Single Shot Transmit is TRUE (enabled), single-shot is enabled. If a CAN frame
 is not transmitted successfully, the CAN controller will not retry.

When Single Shot Transmit is FALSE (disabled), the failed CAN frame transmissions are
 automatically retried.

#### Listen Only

This Boolean control indicates whether to enable the Listen Only feature for passive
 monitoring of the network. The default is FALSE (disabled).

When Listen Only is FALSE (disabled), you can transmit CAN messages normally using
 CAN Output. When CAN messages are received, those messages are acknowledged.

When Listen Only is TRUE (enabled), you cannot transmit CAN messages. When CAN
 messages are received, those messages are not acknowledged. The TCAN4550 CAN
 controller enters error passive state when Listen Only is enabled. Checking Listen
 Only enables passive monitoring of network traffic, which can be useful for
 debugging scenarios in which only one device exists on the network.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=sbriohelp/sbrio_9628_38_module_properties.html language=enus -->
## TOPIC 00088: Module Properties Dialog Box for the sbRIO-9628/9629/9638 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `sbriohelp/sbrio_9628_38_module_properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/sbriohelp/sbrio_9628_38_module_properties.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an onboard I/O module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure an onboard I/O module. For all onboard I/O modules, this dialog box includes the following components: Name—Specifies the name of

### Module Properties Dialog Box for the sbRIO-9628/9629/9638 (FPGA Interface)

Right-click an onboard I/O module in the Project Explorer
 window and select Properties from the shortcut menu to
 display this dialog box.

Use this dialog box to configure an onboard I/O
 module.

For all onboard I/O modules, this dialog box includes the following
 components:

- Name —Specifies the name of the onboard I/O module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the connector number and channel numbers.
 You can use this field to give the onboard module a descriptive name.
- Module Type —Specifies the type of module. You cannot
 change this option.
- Location —Specifies the connector containing the onboard
 module’s channels. You cannot change this option.

The onboard AI module’s dialog box also includes the following:

- Calibration Mode —Sets the calibration mode for the
 onboard module. Select Calibrated if you want the FPGA
 I/O Node to return calibrated, fixed-point data for the module in units of
 volts. The fixed-point data is signed, with a word length of 24 bits and an
 integer word length of 5 bits. Select Raw if you want the
 FPGA I/O Node to return uncalibrated, binary data for the module. If you select
 Raw , you must convert and calibrate the analog input
 values in the host VI. The default is Calibrated .
- Channel Configuration —Specifies the input range for each
 channel.
  - Channels —Specifies the channel(s) for which you
 want to select the input range.
  - Input Range —Specifies the input range for the
 selected channel(s) as ±10 V, ±5 V, ±2 V, or ±1 V.
  - Terminal Mode —Specifies the terminal mode for the
 selected channel(s) as RSE (referenced single-ended) or DIFF
 (differential).
- Minimum Time Between Conversions —Specifies the minimum
 time between conversions in µs. This time determines the shortest possible time
 between any two conversions. For channels sampled within the same FPGA I/O Node,
 the time you set determines the exact time between conversions. For channels
 sampled within separate FPGA I/O Nodes or for conversions caused by looping on
 an FPGA I/O Node, the time you set may be less than the actual time between
 conversions. However, the minimum time you set is never greater than the time
 between conversions. If the application tries to execute an FPGA I/O Node faster
 than the specified minimum time between conversions, the conversion is delayed
 until the minimum time you set is satisfied. The default minimum time between
 conversions is 8 µs. The accuracy specifications in the sbRIO-9638 hardware
 documentation on ni.com/manuals are based on this default value. If you set the
 minimum time between conversions to at least 8 µs, the accuracy of the module is
 not affected. If you set the minimum time between conversions to less than 8 µs,
 the accuracy of the onboard module degrades if you sample data from multiple
 channels.

The onboard AO module’s dialog box also includes the following:

- Calibration Mode —Sets the calibration mode for the
 onboard module. Select Calibrated if you want the FPGA
 I/O Node to accept fixed-point data in units of volts when writing to the
 module. The fixed-point data is signed, with a word length of 20 bits and an
 integer word length of 5 bits. Select Raw if you want the
 FPGA I/O Node to accept calibrated, binary data when writing to the module. If
 you select Raw , you must convert the analog output values
 in the host VI before you write them to the module. The default is
 Calibrated .

The onboard DIO module’s dialog box also includes the following:

- Channels —Specifies the channel(s) for which you want to
 select the direction.
- Selected Channel(s) Settings —Specifies the default line
 direction for each channel.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=sbriohelp/sbrio_9628_38_module_properties_2.html language=enus -->
## TOPIC 00089: Module Properties Dialog Box for the sbRIO-9628/9629/9638 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `sbriohelp/sbrio_9628_38_module_properties_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/sbriohelp/sbrio_9628_38_module_properties_2.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an onboard I/O module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure an onboard I/O module. For all onboard I/O modules, this dialog box includes the following components: Name—Specifies the name of

### Module Properties Dialog Box for the sbRIO-9628/9629/9638 (FPGA Interface)

Right-click an onboard I/O module in the Project Explorer
 window and select Properties from the shortcut menu to
 display this dialog box.

Use this dialog box to configure an onboard I/O
 module.

For all onboard I/O modules, this dialog box includes the following
 components:

- Name —Specifies the name of the onboard I/O module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the connector number and channel numbers.
 You can use this field to give the onboard module a descriptive name.
- Module Type —Specifies the type of module. You cannot
 change this option.
- Location —Specifies the connector containing the onboard
 module’s channels. You cannot change this option.

The onboard AI module’s dialog box also includes the following:

- Calibration Mode —Sets the calibration mode for the
 onboard module. Select Calibrated if you want the FPGA
 I/O Node to return calibrated, fixed-point data for the module in units of
 volts. The fixed-point data is signed, with a word length of 24 bits and an
 integer word length of 5 bits. Select Raw if you want the
 FPGA I/O Node to return uncalibrated, binary data for the module. If you select
 Raw , you must convert and calibrate the analog input
 values in the host VI. The default is Calibrated .
- Channel Configuration —Specifies the input range for each
 channel.
  - Channels —Specifies the channel(s) for which you
 want to select the input range.
  - Input Range —Specifies the input range for the
 selected channel(s) as ±10 V, ±5 V, ±2 V, or ±1 V.
  - Terminal Mode —Specifies the terminal mode for the
 selected channel(s) as RSE (referenced single-ended) or DIFF
 (differential).
- Minimum Time Between Conversions —Specifies the minimum
 time between conversions in µs. This time determines the shortest possible time
 between any two conversions. For channels sampled within the same FPGA I/O Node,
 the time you set determines the exact time between conversions. For channels
 sampled within separate FPGA I/O Nodes or for conversions caused by looping on
 an FPGA I/O Node, the time you set may be less than the actual time between
 conversions. However, the minimum time you set is never greater than the time
 between conversions. If the application tries to execute an FPGA I/O Node faster
 than the specified minimum time between conversions, the conversion is delayed
 until the minimum time you set is satisfied. The default minimum time between
 conversions is 8 µs. The accuracy specifications in the sbRIO-9638 hardware
 documentation on ni.com/manuals are based on this default value. If you set the
 minimum time between conversions to at least 8 µs, the accuracy of the module is
 not affected. If you set the minimum time between conversions to less than 8 µs,
 the accuracy of the onboard module degrades if you sample data from multiple
 channels.

The onboard AO module’s dialog box also includes the following:

- Calibration Mode —Sets the calibration mode for the
 onboard module. Select Calibrated if you want the FPGA
 I/O Node to accept fixed-point data in units of volts when writing to the
 module. The fixed-point data is signed, with a word length of 20 bits and an
 integer word length of 5 bits. Select Raw if you want the
 FPGA I/O Node to accept calibrated, binary data when writing to the module. If
 you select Raw , you must convert the analog output values
 in the host VI before you write them to the module. The default is
 Calibrated .

The onboard DIO module’s dialog box also includes the following:

- Channels —Specifies the channel(s) for which you want to
 select the direction.
- Selected Channel(s) Settings —Specifies the default line
 direction for each channel.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=target2devicehelp/add_expansion_chassis.html language=enus -->
## TOPIC 00090: New R Series Expansion Chassis Dialog Box

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `target2devicehelp/add_expansion_chassis.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/target2devicehelp/add_expansion_chassis.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This dialog box appears when you right-click an R Series device in the Project Explorer window and select New»R Series Expansion Chassis from the shortcut menu. Use this dialog box to enter a name for the NI 9151 R Series Expansion chassis and select the connector to which it is installed. Name—You

### New R Series Expansion Chassis Dialog Box

This dialog box appears when you right-click an R Series device in the
 Project Explorer window and select New»R
 Series Expansion Chassis from the shortcut menu. Use this dialog box
 to enter a name for the NI 9151 R Series Expansion chassis and select the connector
 to which it is installed.

- Name —You can use this text box to enter a name for the
 chassis.
- Location —You can use this pull-down menu to select the
 connector to which the chassis is connected.
- Discover C Series modules —Place a checkmark in this
 checkbox if you want LabVIEW to find all C Series modules installed in the
 chassis. Do not check this checkbox if you do not have an expansion chassis
 installed to the connector selected in the Location 
 pull-down menu.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=target2devicehelp/r_series_expansion_chassis_properties.html language=enus -->
## TOPIC 00091: R Series Expansion Chassis Properties Dialog Box

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `target2devicehelp/r_series_expansion_chassis_properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/target2devicehelp/r_series_expansion_chassis_properties.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This dialog box appears when you right-click an NI 9151 R Series Expansion chassis in the Project Explorer window and select Properties from the shortcut menu. Use this dialog box to enter a name for the R Series Expansion chassis and select the connector to which it is installed. Name—You can use t

### R Series Expansion Chassis Properties Dialog Box

This dialog box appears when you right-click an NI 9151 R Series Expansion
 chassis in the Project Explorer window and select
 Properties from the shortcut menu. Use this dialog box to
 enter a name for the R Series Expansion chassis and select the connector to which it
 is installed.

- Name —You can use this text box to enter a new name for
 the chassis.
- Location —You can use this pull-down menu to select the
 connector to which the chassis is connected.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=target4devicehelp/9502_propertiesDialog.html language=enus -->
## TOPIC 00092: C Series Module Properties Dialog Box for the NI 9502 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `target4devicehelp/9502_propertiesDialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/target4devicehelp/9502_propertiesDialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9502 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9502 (FPGA Interface)

Right-click an [NI 9502](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_9502_io_reference) C
 Series module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.
- Commutation Mode —Sets the commutation mode for the C Series module. Valid values are Field
 Oriented Control and Trapezoidal . The
 default is Field Oriented Control .

Note

Commutation Mode

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=target4devicehelp/9503_propertiesDialog.html language=enus -->
## TOPIC 00093: C Series Module Properties Dialog Box for the NI 9503 (FPGA Interface)

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `target4devicehelp/9503_propertiesDialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/target4devicehelp/9503_propertiesDialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9503 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C Series module, which

### C Series Module Properties Dialog Box for the NI 9503 (FPGA Interface)

Right-click an [NI 9503](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_9503_io_reference) C
 Series module in the Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=target4devicehelp/951x_propertiesDialog.html language=enus -->
## TOPIC 00094: C Series Module Properties Dialog Box for the NI 951x

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `target4devicehelp/951x_propertiesDialog.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/target4devicehelp/951x_propertiesDialog.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9512, NI 9514, or NI 9516 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C

### C Series Module Properties Dialog Box for the NI 951x

Right-click an NI 9512, NI 9514, or NI 9516 C Series module in the
 Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.

#### 951x Firmware Update Utility

You can [download firmware](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_updatefirmware951x)
 to the NI 951x modules and check that the version on the module is the most recent
 version using this utility.

Note

- Check Version —Checks the firmware version currently
 installed on the module.
- Firmware Version on Module —Displays the firmware version
 on the module after clicking Check Version .
- Download —Updates the firmware on the module with the
 version displayed in Available Firmware Version .
- Available Firmware Version —Displays the firmware version
 currently available on the host.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=target4devicehelp/951x_propertiesDialog_2.html language=enus -->
## TOPIC 00095: C Series Module Properties Dialog Box for the NI 951x

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `target4devicehelp/951x_propertiesDialog_2.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/target4devicehelp/951x_propertiesDialog_2.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9512, NI 9514, or NI 9516 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C

### C Series Module Properties Dialog Box for the NI 951x

Right-click an NI 9512, NI 9514, or NI 9516 C Series module in the
 Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.

#### 951x Firmware Update Utility

You can [download firmware](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_updatefirmware951x)
 to the NI 951x modules and check that the version on the module is the most recent
 version using this utility.

Note

- Check Version —Checks the firmware version currently
 installed on the module.
- Firmware Version on Module —Displays the firmware version
 on the module after clicking Check Version .
- Download —Updates the firmware on the module with the
 version displayed in Available Firmware Version .
- Available Firmware Version —Displays the firmware version
 currently available on the host.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=target4devicehelp/951x_propertiesDialog_3.html language=enus -->
## TOPIC 00096: C Series Module Properties Dialog Box for the NI 951x

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `target4devicehelp/951x_propertiesDialog_3.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/target4devicehelp/951x_propertiesDialog_3.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an NI 9512, NI 9514, or NI 9516 C Series module in the Project Explorer window and select Properties from the shortcut menu to display this dialog box. Use this dialog box to configure a C Series module. This dialog box includes the following components: Name—Specifies the name of the C

### C Series Module Properties Dialog Box for the NI 951x

Right-click an NI 9512, NI 9514, or NI 9516 C Series module in the
 Project Explorer window and select
 Properties from the shortcut menu to display this dialog
 box.

Use this dialog box to configure a C Series module.

This dialog
 box includes the following components:

- Name —Specifies the name of the C Series module, which
 appears in the Project Explorer window. LabVIEW assigns a
 default name to the module based on the slot number. You can use this field to
 give the module a descriptive name.
- Module Type —Specifies the type of C Series module. You
 cannot change this option.
- Location —Specifies a slot in the chassis for the C Series
 module.

#### 951x Firmware Update Utility

You can [download firmware](https://ni.com/docs/en-US/csh?context=ni-compactrio_target4devicehelp_updatefirmware951x)
 to the NI 951x modules and check that the version on the module is the most recent
 version using this utility.

Note

- Check Version —Checks the firmware version currently
 installed on the module.
- Firmware Version on Module —Displays the firmware version
 on the module after clicking Check Version .
- Download —Updates the firmware on the module with the
 version displayed in Available Firmware Version .
- Available Firmware Version —Displays the firmware version
 currently available on the host.

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=target6devicehelp/CompactRIO_Error_Codes.html language=enus -->
## TOPIC 00097: CompactRIO Errors

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `target6devicehelp/CompactRIO_Error_Codes.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/target6devicehelp/CompactRIO_Error_Codes.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The FPGA interface and Scan interface can return the following error codes for CompactRIO. FPGA Interface Errors 1 Code Description −65634 The value entered for the Rated Phase Current property is not in the valid range. Valid values are between 0 A and 2 A −65633 The Rated Phase Current cannot be 0

### CompactRIO Errors

The FPGA interface and Scan interface can return the following error codes for
 CompactRIO.

#### FPGA Interface Errors

| Code | Description |
| --- | --- |
| −65634 | The value entered for the Rated Phase Current property is not in the valid range. Valid values are between 0 A and 2 A |
| −65633 | The Rated Phase Current cannot be 0. Change the Rated Phase Current to a valid non-zero value. Refer to the help documentation for more information about this property. |
| −65632 | The drive is disabled due to a fault or other hardware issue. Use the Get Status method to determine the source of the issue, resolve the issue, then execute the Enable Drive method. |
| −65631 | You cannot execute this node when the drive is disabled. Enable the drive and try again. |
| −65630 | You cannot update this property when the drive is enabled. Disable the drive before updating this property. |
| −65629 | The value entered for the Splines per Scan property is not in the valid range. Valid values are 1 to 65,536. |
| −65628 | The value entered for the Spline Rate or Setpoint Rate property is not in the valid range. Valid values are 2000 to 20,000 module clock ticks. |
| −65627 | You cannot update this property when the module is in Fault state or Active state. Switch the module to Configuration state before updating this property. |
| −65626 | You cannot update properties when the module is in Initialization state. Switch to Configuration state before changing any properties. |
| −65625 | You cannot use this method when the module is in Initialization or Configuration state. Switch to Active or Fault state before executing this method. |
| −65624 | You cannot switch to Active state from Fault state until you clear the fault condition(s). |
| −65623 | You cannot switch from Initialization state to Active state or Fault state. The only valid state change from Initialization state is to Configuration state. |
| −65622 | Unable to communicate with the module. Reinsert the module and check connections. If the problem persists, contact NI. |
| −65621 | The project contains a module in slot 16 that does not match the type of the module in slot 16 of the chassis. |
| −65620 | The project contains a module in slot 15 that does not match the type of the module in slot 15 of the chassis. |
| −65619 | The project contains a module in slot 14 that does not match the type of the module in slot 14 of the chassis. |
| −65618 | The project contains a module in slot 13 that does not match the type of the module in slot 13 of the chassis. |
| −65617 | The project contains a module in slot 12 that does not match the type of the module in slot 12 of the chassis. |
| −65616 | The project contains a module in slot 11 that does not match the type of the module in slot 11 of the chassis. |
| −65615 | The project contains a module in slot 10 that does not match the type of the module in slot 10 of the chassis. |
| −65614 | The project contains a module in slot 9 that does not match the type of the module in slot 9 of the chassis. |
| −65613 | The project contains a module in slot 8 that does not match the type of the module in slot 8 of the chassis. |
| −65612 | The project contains a module in slot 7 that does not match the type of the module in slot 7 of the chassis. |
| −65611 | The project contains a module in slot 6 that does not match the type of the module in slot 6 of the chassis. |
| −65610 | The project contains a module in slot 5 that does not match the type of the module in slot 5 of the chassis. |
| −65609 | The project contains a module in slot 4 that does not match the type of the module in slot 4 of the chassis. |
| −65608 | The project contains a module in slot 3 that does not match the type of the module in slot 3 of the chassis. |
| −65607 | The project contains a module in slot 2 that does not match the type of the module in slot 2 of the chassis. |
| −65606 | The project contains a module in slot 1 that does not match the type of the module in slot 1 of the chassis. |
| −65605 | The project contains a module in slot 16 but slot 16 is empty. |
| −65604 | The project contains a module in slot 15 but slot 15 is empty. |
| −65603 | The project contains a module in slot 14 but slot 14 is empty. |
| −65602 | The project contains a module in slot 13 but slot 13 is empty. |
| −65601 | The project contains a module in slot 12 but slot 12 is empty. |
| −65600 | The project contains a module in slot 11 but slot 11 is empty. |
| −65599 | The project contains a module in slot 10 but slot 10 is empty. |
| −65598 | The project contains a module in slot 9 but slot 9 is empty. |
| −65597 | The project contains a module in slot 8 but slot 8 is empty. |
| −65596 | The project contains a module in slot 7 but slot 7 is empty. |
| −65595 | The project contains a module in slot 6 but slot 6 is empty. |
| −65594 | The project contains a module in slot 5 but slot 5 is empty. |
| −65593 | The project contains a module in slot 4 but slot 4 is empty. |
| −65592 | The project contains a module in slot 3 but slot 3 is empty. |
| −65591 | The project contains a module in slot 2 but slot 2 is empty. |
| −65590 | The project contains a module in slot 1 but slot 1 is empty. |
| −65587 | The bitfile required by the RIO Scan Interface is either missing or corrupt. Reinstall the software on the LabVIEW Real-Time target. |
| −65582 | An open thermocouple was detected. |
| −65581 | The FPGA personality currently running on the CompactRIO chassis does not support the RIO Scan Interface in this slot. |
| −65580 | The FPGA personality running on the RIO target does not have enough specialty digital resources to support this module. |
| −65537 | The module that was detected is different than the module that was expected. Make sure the slot the module is configured for in software matches the physical location of the module. |
| −65536 | Unable to communicate with the module. Reinsert the module and check connections. If the chassis is in FPGA Interface programming mode, make sure you have opened an FPGA reference to a bitfile or FPGA VI with Scan Interface support for the module you are trying to access using the Scan Interface. |
| −65512 | The data transfer for some IO Variables on this target could not be completed in the allotted time and some values' updates may have been delayed. Please slow down the IO Scan rate to avoid this problem. |
| −65408 | This deploy operation did not succeed because the model number of the module in the slot did match the project. |
| −65407 | Too many specialty digital slots. In Scan Interface mode, you can configure only two slots for specialty digital I/O. If you want more specialty digital slots, add an FPGA target under the chassis to put the chassis in LabVIEW FPGA interface mode. |
| −63043 | The session is invalid. The target may have been reset or rebooted, or the network connection may have timed out because of processor overuse. Check the network connection, reduce the demand on the processor, and decrease the timeout of the operation that failed. If the problem persists, visit ni.com/info and enter the Info Code expd6p. |
| −63035 | The attempt to open a RIO session failed because the driver was not yet initialized. |
| 65000 | Unable to mount drive. The given device is either not present or not recognizable as a mountable device. |
| 65001 | No partitions found. The partition table on the device is corrupt or the device has zero partitions on it. |
| 65002 | Invalid drive handle. The given handle does not represent an active mounted drive. |
| 65003 | Drive already mounted. The given device is already mounted as a drive. |
| 65004 | The channel, slot, or connector number you wired to the method input is invalid. Change the method input to match the configuration of the CompactRIO system. |
| 65005 | The C Series module at the specified location does not support TEDS or TEDS access is not enabled for the module. |
| 65006 | Communication with the module timed out. The module is busy performing another action or LabVIEW is unable to communicate with the module. |
| 65007 | No TEDS sensor was detected on the specified channel. Make sure that the C Series module and sensor are properly connected. Make sure the specified location matches the sensor location. |
| 65008 | CompactRIO does not support the TEDS sensor connected to this channel. |
| 65009 | The PXI trigger that you have selected to reserve or unreserve is invalid. Valid PXI triggers are 0 through 7, inclusive. |
| 65011 | Data could not be read. Unable to determine TEDS standard template type. Verify sensor connections and that the sensor is a standard type. If the problem persists, read the entire sensor EEPROM by selecting Entire EEPROM on the Data to Read terminal of the Read TEDS Invoke Method. |
| 65100 | You have entered a data rate that is not supported by the selected module and oversample clock frequency. |
| 65200 | DIO Line Access Conflict. Invalid module configuration. A single physical DIO line cannot be accessed by multiple types of output nodes when the Number of Synchronizing Registers=0 and any of the output accesses is in a Single-Cycle Timed Loop. Either change the number of Synchronizing Registers to 1 in the module's properties dialog, or access the resource exclusively as a port or an individual line, not both. |
| 65201 | Duplicate Terminals In The Same Node. An FPGA I/O Node has duplicate terminals. Delete the duplicate terminal from the I/O Node. |
| 65202 | Digital Resource Access Conflict. The digital I/O resource cannot be accessed in a Single-Cycle Timed Loop from both a Digital Output function and a Digital Port Output function. If you need to access this resource in a Single-Cycle Timed Loop, please exclusively use just the Digital Output function or Digital Port Output function, not both. |
| 65203 | Module Timebase Configuration Error. LabVIEW detected an invalid configuration for an FPGA I/O Node that contains channels from a module with a configurable timebase. If channels of multiple modules with a configurable timebase are in the same FPGA I/O Node, make sure you configure the modules to share the same timebase. Use the C Series Module Properties dialog box to configure the module timebase. Refer to the LabVIEW Help for information about how to synchronize multiple C Series modules. |
| 65204 | Digital Resource Access Conflict. The digital I/O resource cannot be accessed from both a Digital Output function and a Digital Port Output function if the Never Arbitrate option is used. Please change the arbitration of the Digital Line and/or Digital Port to something other than Never Arbitrate, or exclusively use just the Digital Output function or Digital Port Output function, not both. |
| 65205 | Invalid C Series Module Configuration. Possible reasons for the invalid configuration include that the master timebase source module is unable to be identified, the master timebase source module is not configured to export its timebase, or the master timebase source module is not a valid module type. Use the C Series Module Properties dialog box to configure the module timebase. Refer to the LabVIEW Help for information about how to synchronize multiple C Series modules. |
| 65206 | Invalid top-level clock. You must use a top-level clock of 40 MHz when using this module. To change the top-level clock, right click on your FPGA target in the LabVIEW Project Explorer and select properties. From the Top-Level Clock category, choose a 40 MHz clock. |
| 65207 | The digital output resource cannot be accessed from both a Digital Output function and a Digital Port Output function. Please exclusively use just the Digital Output function or Digital Port Output function, not both. |
| 65208 | The NI 9151 R Series Expansion chassis no longer supports synchronizing multiple NI 9225/9227/9229/923x modules. Use the C Series Module Properties dialog box to set the master timebase source of the slave module(s) to the onboard clock. Right-click the module in the project and select Properties to display the C Series Module Properties dialog box. Contact NI technical support with questions or concerns. |
| 65209 | You cannot write to the Sleep channel if you are using the Scan Interface with any modules in the system. |
| 65210 | You must use a top-level clock of 80 MHz or less when using this module. To change the top-level clock, right click on your FPGA target in the Project Explorer window and select Properties. Select Top-Level Clock from the Category list and choose an 80 MHz or slower clock rate. |
| 65211 | You have reached the limit of the user-defined variable address space. This is caused by using too many user-defined variables in your LabVIEW FPGA VI. The number of allowed user-defined variables in a LabVIEW FPGA VI is around 500 to 1000 user-defined variables depending on the data type of the variables. Remove some of the variable nodes from the LabVIEW FPGA VI and try compiling again. |
| 65212 | The module timing constraints for the FPGA target you are using were not found. Please contact NI. |
| 65213 | The NI 9151 R Series Expansion chassis does not support this module. |
| 65215 | One or more nodes have been incorrectly placed inside of a Single Cycle Timed Loop. Please ensure that only SCTL nodes are used inside of the Single Cycle Timed Loop. |
| 65216 | One or more nodes have been incorrectly placed outside of a Single Cycle Timed Loop. Please ensure that only non-SCTL nodes are used outside of the Single Cycle Timed Loop. |
| 65217 | A particular node has been placed on the diagram more than once. This type of node can only have one instantiation on the diagram. Please remove the duplicate instantiations of the node. |
| 65218 | A module in your project contains invalid module support files. Please contact the module vendor. |
| 65400 | The FPGA target is either running an FPGA VI or has loaded an FPGA VI. |
| 65401 | One or more discovered C Series modules are not supported by the current versions of LabVIEW and NI-RIO. |
| 65402 | An internal software error in NI-RIO has occurred. Please contact NI technical support at ni.com/support. |
| 65403 | An unexpected error occurred when Discovering C Series Modules. Make sure the LabVIEW Project is set up properly. |
| 65404 | The controller you selected has an unconfigured (0.0.0.0) IP address. If the controller is online, configure it in Measurement & Automation Explorer (MAX), then make sure the IP address in LabVIEW matches the IP address in MAX. If it is offline, you cannot discover connected targets and devices, but you can add new, offline targets and devices. |
| 65405 | Module not found. The module whose configuration you deployed is not present in the chassis. |
| 65406 | Different module. The module whose configuration you deployed does not match the model currently in the chassis. |
| 65407 | Too many specialty digital slots. In Scan Interface mode, you can configure only two slots for specialty digital I/O. If you want more specialty digital slots, add an FPGA target under the chassis to put the chassis in LabVIEW FPGA Interface mode. |
| 65536 | Unable to communicate with the module. Reinsert the module and check connections. |
| 65537 | The module that was detected is different than the module that was expected. Make sure the slot the module is configured for in software matches the physical location of the module. |
| 65538 | The operation failed to complete in time. Make sure the module is not busy and the system is configured properly. |
| 65539 | The input function missed one or more data points. Make sure the loop can execute as fast as the module data rate. |
| 65540 | The I/O Resource is not in communication mode. You must start communication mode before you can perform this operation. |
| 65541 | The I/O Resource is in communication mode. You must stop communication mode before you can perform this operation. |
| 65542 | One or more channels have detected an open current loop. Check the module connections. |
| 65543 | The power supply voltage level is out of range. Check the supply voltage and the module connections. |
| 65544 | One or more channels are in overcurrent protection mode. The device connected to the channel is passing more current than is allowed through the channel. Check for possible shorts or external device failure. |
| 65545 | An input parameter, or a combination of parameters, is invalid. |
| 65546 | Your application uses a feature that is not supported by your C Series hardware. |
| 65547 | Too many CAN bus error frames are detected. Please refer to the description of the 'Error Terminals' for more information. |
| 65548 | One or more channels are in overcurrent or overvoltage protection mode. Check the terminals for any fault condition that could be causing an out-of-range voltage or current on the channels. |
| 65549 | A general or undefined error has occurred. Verify that the card is inserted properly and that the door is closed. If the error occurs again, run CHKDSK on the card. |
| 65550 | A problem was found in the file system. Remove the SD card and run CHKDSK. |
| 65551 | The SD card is in use by RT. Try again after RT unmounts the card. |
| 65552 | The SD card is not ready. Verify that the card is inserted properly and that the door is closed. |
| 65553 | The SD card door was opened while a file on the card was open. |
| 65554 | The specified file does not exist on the card. |
| 65555 | The Open method tried to open a new file for writing, but a file with the same name already exists on the disk. |
| 65556 | A Read or Write method tried to access a file that was not opened in the required mode. |
| 65558 | A Close method tried to close a file that was not open. |
| 65559 | A method tried to open a file on the SD card when a file was already open. This device supports only one file open at a time. This error is also returned when an illegal attempt to call the Delete File or Get File Size method is made when a file is open on the card. |
| 65560 | An attempt to allocate storage failed because the file system is full. |
| 65561 | Attempted to exceed the limit of 512 root directory entries. |
| 65562 | A Read method tried to read beyond the end of a file. This may have occurred when the method read the end of a file using a U16 or U32 data type when the actual number of bytes in the file (as reported by the directory) was not an integer multiple of the number of bytes in the read data type. |
| 65563 | A problem was found with the format of the SD card. Verify that the SD card is formatted with a valid FAT16 file system. |
| 65577 | An open thermocouple was detected on at least one channel. Check the module connections. |
| 65578 | The common-mode voltage is outside of acceptable limits on at least one channel. Check the terminals for any fault condition that could be causing an out-of-range voltage on the channels. |
| 65579 | The module is in overcurrent protection mode. Check the terminals for any fault condition that could be causing an out-of-range current. |
| 65582 | The operation did not complete because the acquisition has not started. Use the Start and Stop channels to put the module in and out of acquisition mode. |
| 65583 | The module failed to complete the operation. Reinsert the module and check connections. If the problem persists, contact NI technical support. |
| 65584 | The device cannot be powered down because it is actively connected to a host. |
| 65585 | Open thermocouple detection is currently disabled. The Check Cached Status method cannot accurately report whether or not there are disconnected thermocouples. |
| 65586 | The operation did not complete because a user controlled I/O sampling reset is in progress. |
| 65588 | The module is not yet initialized. If you are using the User-Controlled I/O Sampling functions, you must first call the Reset I/O Method function and wait for it to complete before calling any other User-Controlled I/O Sampling functions. |
| 65638 | The value for the cable delay property is out of range. Refer to the module help documentation for the maximum cable compensation delay. |
| 65639 | At least one of the coordinates provided is out of range. Latitude must be in the following range, -90° ≤ Latitude ≤ 90°. Longitude must be in the following range, -180° < Longitude ≤ 180°. Refer to the module help documentation for the appropriate altitude range. |
| 65640 | The firmware on the module is not compatible with this version of the NI RIO software. Please visit ni.com for instructions on how to update the firmware. |
| 65641 | Valid data for the requested field has yet to be received from the module. Use the appropriate Wait Method to receive notification of when data is available. |
| 65642 | The trigger could not be sent. Make sure that To Module is selected as the line direction of the trigger and that it is not configured to carry a clock. |
| 65643 | The Wait On Trigger method cannot execute on a trigger line configured to carry a clock. Select another trigger line or change the clock routing configuration in the C Series Module Properties dialog box. |
| 65644 | Port line direction change failed because the maximum number of port lines are configured for output on the module. Refer to the module help documentation for the maximum number of simultaneous port line outputs. |
| 65645 | The specified line does not support the selected source. Refer to the module help documentation for a list of valid sources for each line. |
| 65646 | Invalid clock source direction. Select To Module as the line direction for the line specified as the clock source. |
| 65647 | The line source and direction of the specified trigger cannot be changed because it is configured to carry a clock. |
| 65648 | The specified port line does not support the selected trigger line as a source because the trigger line is configured to carry a clock. To export the clock carried on the trigger line, set the module's Clock source to the trigger line and select Clock as the port line source. |
| 65649 | The module did not export the generated trigger because this trigger line is not configured as the source for any of the port lines. |
| 65650 | The operation failed to complete in time because the imported oversample clock was not ready. Make sure the system is configured correctly. |
| 65652 | A DO update was attempted while the module was not ready to perform this operation. The DO update was delayed or gated. |
| 65654 | One or more channels has an open loop or an excitation fault. Check the module connections. |
| 65656 | The signal attenuation level is invalid. Consult the module documentation for the valid range of attenuation values. |
| 65657 | The RF center frequency is invalid. Consult the module documentation for the valid range of center frequency values. |
| 65658 | The LO In frequency is invalid. Consult the module documentation for the valid range of LO In frequency values. |
| 65659 | The specified combination of RF center frequency and LO In frequency values is invalid. Consult the module documentation for information about how to configure these parameters. |
| 65660 | The LO Out signal cannot be disabled while the module is in its currently configured state. Consult the module documentation for information about how to configure the LO Out signal. |
| 65661 | An overflow was detected in the IQ data. Reduce the input power level or configure the reference level to a higher value. |
| 65662 | The sample clock PLL is not locked, which can cause samples to be incorrectly synchronized across modules. Refer to the module documentation for more information on what can cause the sample clock to be incorrectly locked. |
| 65663 | The LO PLL is not locked, which can cause samples to be incorrectly synchronized across modules. Refer to the module documentation for more information on what can cause the LO to be incorrectly locked. |
| 65664 | Module cannot run the Start node while it is in data operation mode. Run Stop node before running Start node. |
| 65665 | The acquisition cannot be started because the selected data rate is not valid. Select a data rate that is allowed based on the timing mode and number of channels. |
| 65666 | The acquisition cannot be started because the length of the record pre-trigger samples is greater than the length of the record samples. Select a record pre-trigger samples that is shorter than the record samples. |
| 65667 | The I/O Node cannot acquire data after fetching data from the record or using hardware triggers. Restart the acquisition to access continuous data. |
| 65668 | No data is available for fetching. Trigger a record before fetching samples. |
| 65669 | No more records can be triggered. Fetch all sample records before triggering a new record. |
| 65670 | The sample clock PLL was lost while acquiring the record. Refer to the module documentation for more information on what can cause the sample clock to be incorrectly locked. |
| 65671 | Triggering not supported on the selected channel. Enable the selected channel through the configuration subpanel. |

#### Scan Interface Errors

I/O variables can
 return the following error codes.

| Code | Description |
| --- | --- |
| −65627 | You cannot update this property when the module is in Fault state or Active state. Switch the module to Configuration state before updating this property. |
| −65626 | You cannot update properties when the module is in Initialization state. Switch to Configuration state before changing any properties. |
| −65625 | You cannot use this method when the module is in Initialization or Configuration state. Switch to Active or Fault state before executing this method. |
| −65624 | You cannot switch to Active state from Fault state until you clear the fault condition(s). |
| −65623 | You cannot switch from Initialization state to Active state or Fault state. The only valid state change from Initialization state is to Configuration state. |
| −65622 | Unable to communicate with the module. Reinsert the module and check connections. If the problem persists, contact NI. |
| −65621 | The project contains a module in slot 16 that does not match the type of the module in slot 16 of the chassis. |
| −65620 | The project contains a module in slot 15 that does not match the type of the module in slot 15 of the chassis. |
| −65619 | The project contains a module in slot 14 that does not match the type of the module in slot 14 of the chassis. |
| −65618 | The project contains a module in slot 13 that does not match the type of the module in slot 13 of the chassis. |
| −65617 | The project contains a module in slot 12 that does not match the type of the module in slot 12 of the chassis. |
| −65616 | The project contains a module in slot 11 that does not match the type of the module in slot 11 of the chassis. |
| −65615 | The project contains a module in slot 10 that does not match the type of the module in slot 10 of the chassis. |
| −65614 | The project contains a module in slot 9 that does not match the type of the module in slot 9 of the chassis. |
| −65613 | The project contains a module in slot 8 that does not match the type of the module in slot 8 of the chassis. |
| −65612 | The project contains a module in slot 7 that does not match the type of the module in slot 7 of the chassis. |
| −65611 | The project contains a module in slot 6 that does not match the type of the module in slot 6 of the chassis. |
| −65610 | The project contains a module in slot 5 that does not match the type of the module in slot 5 of the chassis. |
| −65609 | The project contains a module in slot 4 that does not match the type of the module in slot 4 of the chassis. |
| −65608 | The project contains a module in slot 3 that does not match the type of the module in slot 3 of the chassis. |
| −65607 | The project contains a module in slot 2 that does not match the type of the module in slot 2 of the chassis. |
| −65606 | The project contains a module in slot 1 that does not match the type of the module in slot 1 of the chassis. |
| −65605 | The project contains a module in slot 16 but slot 16 is empty. |
| −65604 | The project contains a module in slot 15 but slot 15 is empty. |
| −65603 | The project contains a module in slot 14 but slot 14 is empty. |
| −65602 | The project contains a module in slot 13 but slot 13 is empty. |
| −65601 | The project contains a module in slot 12 but slot 12 is empty. |
| −65600 | The project contains a module in slot 11 but slot 11 is empty. |
| −65599 | The project contains a module in slot 10 but slot 10 is empty. |
| −65598 | The project contains a module in slot 9 but slot 9 is empty. |
| −65597 | The project contains a module in slot 8 but slot 8 is empty. |
| −65596 | The project contains a module in slot 7 but slot 7 is empty. |
| −65595 | The project contains a module in slot 6 but slot 6 is empty. |
| −65594 | The project contains a module in slot 5 but slot 5 is empty. |
| −65593 | The project contains a module in slot 4 but slot 4 is empty. |
| −65592 | The project contains a module in slot 3 but slot 3 is empty. |
| −65591 | The project contains a module in slot 2 but slot 2 is empty. |
| −65590 | The project contains a module in slot 1 but slot 1 is empty. |
| −65587 | The bitfile required by the RIO Scan Interface is either missing or corrupt. Reinstall the software on the LabVIEW Real-Time target. |
| −65583 | A common-mode range error was detected. |
| −65582 | An open thermocouple was detected. |
| −65581 | The FPGA personality currently running on the CompactRIO chassis does not support the RIO Scan Interface in this slot. |
| −65580 | The FPGA personality running on the RIO target does not have enough specialty digital resources to support this module. |
| −65537 | The module that was detected is different than the module that was expected. Make sure the slot the module is configured for in software matches the physical location of the module. |
| −65536 | Unable to communicate with the module. Reinsert the module and check connections. If the chassis is in FPGA Interface programming mode, make sure you have opened an FPGA reference to a bitfile or FPGA VI with Scan Interface support for the module you are trying to access using the Scan Interface. |
| −65500 | Module is in download process and can't perform the invoke node until download completes. |
| −65499 | The parameter of "set mode" invoke node is invalid. |
| −65498 | Unable to communicate with the module, please make sure the module is powered on and properly plugged in. |
| −65497 | Please download the user program again, the last download process could have been interrupted. |
| −65496 | Please download the user program again, the module has timed out due to download process error. |
| −65495 | Please check the mode of the module. If the module is in unprogrammed mode, please download a user program to the module. If the module is in fail safe mode, please restart the module. If the module is in download mode, please restart and download the user program again. |
| −65494 | The module is not in the correct state. Please wait a moment in case the module is restarting. If that doesn't work, please restart the module because the last download process was interrupted. |
| −65493 | The operation failed because of CRC error. |
| −65492 | The operation failed because of CRC error. |
| −65491 | An internal software error with SIL module has occurred. Please check the compatibility of the software and hardware. |
| −65490 | The latest data cannot be retrieved, please check the power of the module and wait for one scan period. |
| −65489 | An internal software error with SIL module has occurred. Please contact NI technical support at ni.com/support with following information: The C Series Functional Safety modules has internal faults. |
| −65488 | The user program file is corrupted, please check the user program file and download again. |
| −65487 | The file type of the user program file is not correct, please check the user program file and download again. |
| −65407 | Too many specialty digital slots. In Scan Interface mode, you can configure only two slots for specialty digital I/O. If you want more specialty digital slots, add an FPGA target under the chassis to put the chassis in LabVIEW FPGA interface mode. |
| −63043 | The session is invalid. The target may have been reset or rebooted, or the network connection may have timed out because of processor overuse. Check the network connection, reduce the demand on the processor, and decrease the timeout of the operation that failed. If the problem persists, refer to NI KnowledgeBase article 4CJDJBLX. |
| −63035 | The attempt to open a RIO session failed because the driver was not yet initialized. |
| 65000 | Unable to mount drive. The given device is either not present or not recognizable as a mountable device. |
| 65001 | No partitions found. The partition table on the device is corrupt or the device has zero partitions on it. |
| 65002 | Invalid drive handle. The given handle does not represent an active mounted drive. |
| 65003 | Drive already mounted. The given device is already mounted as a drive. |
| 65004 | The channel, slot, or connector number you wired to the method input is invalid. Change the method input to match the configuration of the CompactRIO system. |
| 65005 | The C Series module at the specified location does not support TEDS or TEDS access is not enabled for the module. |
| 65006 | Communication with the module timed out. The module is busy performing another action or LabVIEW is unable to communicate with the module. |
| 65007 | No TEDS sensor was detected on the specified channel. Make sure that the C Series module and sensor are properly connected. Make sure the specified location matches the sensor location. |
| 65008 | CompactRIO does not support the TEDS sensor connected to this channel. |
| 65009 | The PXI trigger that you have selected to reserve or unreserve is invalid. Valid PXI triggers are 0 through 7, inclusive. |
| 65200 | DIO Line Access Conflict. Invalid module configuration. A single physical DIO line cannot be accessed by multiple types of output nodes when the Number of Synchronizing Registers=0 and any of the output accesses is in a Single-Cycle Timed Loop. Either change the number of Synchronizing Registers to 1 in the module's properties dialog, or access the resource exclusively as a port or an individual line, not both. |
| 65201 | Duplicate Terminals In The Same Node. An FPGA I/O Node has duplicate terminals. Delete the duplicate terminal from the I/O Node. |
| 65202 | Digital Resource Access Conflict. The digital I/O resource cannot be accessed in a Single-Cycle Timed Loop from both a Digital Output function and a Digital Port Output function. If you need to access this resource in a Single-Cycle Timed Loop, please exclusively use just the Digital Output function or Digital Port Output function, not both. |
| 65203 | Module Timebase Configuration Error. LabVIEW detected an invalid configuration for an FPGA I/O Node that contains channels from a module with a configurable timebase. If channels of multiple modules with a configurable timebase are in the same FPGA I/O Node, make sure you configure the modules to share the same timebase. Use the C Series Module Properties dialog box to configure the module timebase. Refer to the LabVIEW Help for information about how to synchronize multiple C Series modules. |
| 65204 | Digital Resource Access Conflict. The digital I/O resource cannot be accessed from both a Digital Output function and a Digital Port Output function if the Never Arbitrate option is used. Please change the arbitration of the Digital Line and/or Digital Port to something other than Never Arbitrate, or exclusively use just the Digital Output function or Digital Port Output function, not both. |
| 65205 | Invalid C Series Module Configuration. Possible reasons for the invalid configuration include that the master timebase source module is unable to be identified, the master timebase source module is not configured to export its timebase, or the master timebase source module is not a valid module type. Use the C Series Module Properties dialog box to configure the module timebase. Refer to the LabVIEW Help for information about how to synchronize multiple C Series modules. |
| 65206 | Invalid top-level clock. You must use a top-level clock of 40 MHz when using this module. To change the top-level clock, right click on your FPGA target in the LabVIEW Project Explorer and select properties. From the Top-Level Clock category, choose a 40 MHz clock. |
| 65207 | The digital output resource cannot be accessed from both a Digital Output function and a Digital Port Output function. Please exclusively use just the Digital Output function or Digital Port Output function, not both. |
| 65208 | The NI 9151 R Series Expansion chassis no longer supports synchronizing multiple NI 9225/9227/9229/923x modules. Use the C Series Module Properties dialog box to set the master timebase source of the slave module(s) to the onboard clock. Right-click the module in the project and select Properties to display the C Series Module Properties dialog box. Contact NI technical support with questions or concerns. |
| 65209 | You cannot write to the Sleep channel if you are using the Scan Interface with any modules in the system. |
| 65210 | You must use a top-level clock of 80 MHz or less when using this module. To change the top-level clock, right click on your FPGA target in the Project Explorer window and select Properties. Select Top-Level Clock from the Category list and choose an 80 MHz or slower clock rate. |
| 65211 | You have reached the limit of the user-defined variable address space. This is caused by using too many user-defined variables in your LabVIEW FPGA VI. The number of allowed user-defined variables in a LabVIEW FPGA VI is around 500 to 1000 user-defined variables depending on the data type of the variables. Remove some of the variable nodes from the LabVIEW FPGA VI and try compiling again. |
| 65212 | The module timing constraints for the FPGA target you are using were not found. Please contact NI. |
| 65400 | The FPGA target is either running an FPGA VI or has loaded an FPGA VI. |
| 65401 | One or more discovered C Series modules are not supported by the current versions of LabVIEW and NI-RIO. |
| 65402 | An internal software error in NI-RIO has occurred. Please contact NI technical support at ni.com/support. |
| 65403 | An unexpected error occurred when Discovering C Series Modules. Make sure the LabVIEW Project is set up properly. |
| 65404 | The controller you selected has an unconfigured (0.0.0.0) IP address. If the controller is online, configure it in Measurement & Automation Explorer (MAX), then make sure the IP address in LabVIEW matches the IP address in MAX. If it is offline, you cannot discover connected targets and devices, but you can add new, offline targets and devices. |
| 65405 | Module not found. The module whose configuration you deployed is not present in the chassis. |
| 65406 | Different module. The module whose configuration you deployed does not match the model currently in the chassis. |
| 65407 | Too many specialty digital slots. In Scan Interface mode, you can configure only two slots for specialty digital I/O. If you want more specialty digital slots, add an FPGA target under the chassis to put the chassis in LabVIEW FPGA Interface mode. |
| 65536 | Unable to communicate with the module. Reinsert the module and check connections. |
| 65537 | The module that was detected is different than the module that was expected. Make sure the slot the module is configured for in software matches the physical location of the module. |
| 65538 | The operation failed to complete in time. Make sure the module is not busy and the system is configured properly. |
| 65539 | The input function missed one or more data points. Make sure the loop can execute as fast as the module data rate. |
| 65540 | The I/O Resource is not in communication mode. You must start communication mode before you can perform this operation. |
| 65541 | The I/O Resource is in communication mode. You must stop communication mode before you can perform this operation. |
| 65542 | One or more channels have detected an open current loop. Check the module connections. |
| 65543 | The power supply voltage level is out of range. Check the supply voltage and the module connections. |
| 65544 | One or more channels are in overcurrent protection mode. The device connected to the channel is passing more current than is allowed through the channel. Check for possible shorts or external device failure. |
| 65545 | An input parameter, or a combination of parameters, is invalid. |
| 65546 | Your application uses a feature that is not supported by your C Series hardware. |
| 65547 | Too many CAN bus error frames are detected. Please refer to the description of the 'Error Terminals' for more information. |
| 65548 | One or more channels are in overcurrent or overvoltage protection mode. Check the terminals for any fault condition that could be causing an out-of-range voltage or current on the channels. |
| 65549 | A general or undefined error has occurred. Verify that the card is inserted properly and that the door is closed. If the error occurs again, run CHKDSK on the card. |
| 65550 | A problem was found in the file system. Remove the SD card and run CHKDSK. |
| 65551 | The SD card is in use by RT. Try again after RT unmounts the card. |
| 65552 | The SD card is not ready. Verify that the card is inserted properly and that the door is closed. |
| 65553 | The SD card door was opened while a file on the card was open. |
| 65554 | The specified file does not exist on the card. |
| 65555 | The Open method tried to open a new file for writing, but a file with the same name already exists on the disk. |
| 65556 | A Read or Write method tried to access a file that was not opened in the required mode. |
| 65558 | A Close method tried to close a file that was not open. |
| 65559 | A method tried to open a file on the SD card when a file was already open. This device supports only one file open at a time. This error is also returned when an illegal attempt to call the Delete File or Get File Size method is made when a file is open on the card. |
| 65560 | An attempt to allocate storage failed because the file system is full. |
| 65561 | Attempted to exceed the limit of 512 root directory entries. |
| 65562 | A Read method tried to read beyond the end of a file. This may have occurred when the method read the end of a file using a U16 or U32 data type when the actual number of bytes in the file (as reported by the directory) was not an integer multiple of the number of bytes in the read data type. |
| 65563 | A problem was found with the format of the SD card. Verify that the SD card is formatted with a valid FAT16 file system. |
| 65571 | Serial module over-temperature error: An over-temperature error has occurred since the last time the module was accessed. Check for fault conditions or extraneous voltages on the I/O port. |
| 65577 | An open thermocouple was detected on at least one channel. Check the module connections. |
| 65578 | The common-mode voltage is outside of acceptable limits on at least one channel. Check the terminals for any fault condition that could be causing an out-of-range voltage on the channels. |
| 65579 | The module is in overcurrent protection mode. Check the terminals for any fault condition that could be causing an out-of-range current. |
| 65582 | The operation did not complete because the acquisition has not started. Use the Start and Stop channels to put the module in and out of acquisition mode. |
| 65583 | The module failed to complete the operation. Reinsert the module and check connections. If the problem persists, contact NI technical support. |
| 65700 | Unable to communicate with the module. Reinsert the module and check connections. |
| 65701 | The module that was detected is different than the module that was expected. Make sure the slot the module is configured for in software matches the physical location of the module. |
| 65702 | The FPGA personality currently running on the CompactRIO chassis does not support the RIO Scan Interface in this slot. |
| 65703 | Remote module access is not supported. |
| 65704 | Could not resolve RSI module URL. |
| 65705 | This RSI module does not accept configuration for this channel. |
| 65706 | The value for 9205 minimum time between conversion must be at least 4 us. |
| 65707 | The value for 9219 digital threshold must be between 0 and 60. |
| 65708 | Invalid direction string |
| 65709 | Current limit values must be between 0 and 5.1. |
| 65710 | The value for overcurrent refresh period must be between 2 and 255. |
| 65711 | It is invalid to change the mode of a 9219 channel programmatically. |
| 65712 | Digital input modules cannot be configured to be a PWM or a counter slave. |
| 65713 | Digital output modules cannot be configured to be a counter or a quadrature. |
| 65714 | RTD A constant must be between 0.001 and 0.01. |
| 65715 | RTD B constant must be between -1E-7 and -1E-6. |
| 65716 | RTD C constant must be between -1E-12 and -1E-11. |
| 65717 | RTD Ro constant must be between 0 and 1000. |
| 65718 | Invalid Input Configuration change. |
| 65719 | The enum value is out of range. |
| 65720 | This property is not valid for this module, or is not valid for the current configuration of this module. |
| 65721 | You can use the Reset Counter method only to reset a counter configured to count edges. |
| 65722 | This method is not valid for this module, or is not valid for the current configuration of this module. |
| 65723 | This module cannot be configured while the controller engine is in its current mode. |
| 65724 | Specialty digital configuration is not supported for EtherCAT modules. |
| 65725 | The value used is out of range. |
| 65726 | Configuration information for this Property was not found. The Property might need to be set before it can be read. |
| 65727 | Invalid slot number. |
| 65728 | This version of the EtherCAT software does not support this operation. |
| 65730 | An expected user program is four bytes aligned, please check the size of your user program file. |
| 65731 | A user program is being downloaded. Reading IOV will get stale data, and writing IOV may not take effect. |
| 65732 | The module is not in the correct state. Please wait a moment in case the module is restarting. If that doesn't work, please check the mode of the module for more information. |
| 65733 | The latest IOV data cannot be retrieved, please check the power of the module and wait for one scan period. |

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=target6devicehelp/HMB_pal.html language=enus -->
## TOPIC 00098: Host Memory Buffer

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `target6devicehelp/HMB_pal.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/target6devicehelp/HMB_pal.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: NI-RIO Operations for accessing a host memory buffer. 16 Palette Object Description Memory Barrier Instructs the CPU to enforce an ordering constraint on memory operations before and after the VI is called. OpenHMB Returns a data value reference that provides access to a host memory buffer

### Host Memory Buffer

Requires: NI-RIO

Operations for accessing a host memory
 buffer.

| Palette Object | Description |
| --- | --- |
| Memory Barrier | Instructs the CPU to enforce an ordering constraint on memory operations before and after the VI is called. |
| OpenHMB | Returns a data value reference that provides access to a host memory buffer. |

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=target6devicehelp/Memory_Barrier.html language=enus -->
## TOPIC 00099: Memory Barrier VI

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `target6devicehelp/Memory_Barrier.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/target6devicehelp/Memory_Barrier.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Host Memory Buffer Requires: NI-RIO Instructs the CPU to enforce an ordering constraint on memory operations before and after the VI is called. 1 17 error in (no error) describes the error status before this VI or function runs. The default is no error. If an error occurred before th

### Memory Barrier VI

Owning Palette:
 [Host Memory
 Buffer](HMB_pal.html)
 Requires:
 NI-RIO

Instructs the CPU to enforce an ordering constraint on
 memory operations before and after the VI is called.

Figure 1.

[IMAGE alt='image' src='../images/Memory_Barrier.gif']

|  | error in (no error) describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
| --- | --- |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

Host Memory Buffer

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=target6devicehelp/NI_RIO_FCF_error_codes.html language=enus -->
## TOPIC 00100: NI-RIO FPGA Communications Framework Error Codes

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `target6devicehelp/NI_RIO_FCF_error_codes.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/target6devicehelp/NI_RIO_FCF_error_codes.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The FPGA Interface functions can return the following error codes for CompactRIO devices. 3 Code Description −63198 The system has run out of resources. Close a session and retry the operation. −63197 An invalid attribute value has been specified. −63196 An invalid attribute has been specified. −631

### NI-RIO FPGA Communications Framework Error Codes

The FPGA Interface functions can return the following error codes for CompactRIO
 devices.

| Code | Description |
| --- | --- |
| −63198 | The system has run out of resources. Close a session and retry the operation. |
| −63197 | An invalid attribute value has been specified. |
| −63196 | An invalid attribute has been specified. |
| −63195 | The handle for device communication is invalid or has been closed. Restart the application. |
| −63194 | The NI-RIO software on the remote system is not compatible with the local NI-RIO software. Upgrade the NI-RIO software on the remote system. |
| −63193 | The requested feature is not supported. |
| −63192 | Either the supplied resource name is invalid as a RIO resource name, or the device was not found. Use MAX to find the proper resource name for the intended device. |
| −63189 | The supplied search pattern is invalid. |
| −63188 | The operation is no longer supported. |
| −63187 | This remote system does not support connections to other remote systems. |
| −63183 | An invalid port was specified. The RIO server port must be between 0 and 65535, where 0 indicates a dynamically assigned port. Port 3580 is reserved and cannot be used. |
| −63182 | An invalid device access setting was specified. RIO device access patterns may contain only alphanumerics, '-', '_', '.', and '*'. |
| −63181 | The supplied alias was not found. |
| −63180 | The alias name is invalid. A valid alias name must meet the following conditions: Cannot be or contain a reserved word.Can use only alphanumeric characters, hyphens, and underscores.Cannot conflict with the default alias of another device. A default alias is the name that the NI-RIO Device Driver assigns to a device based on its attributes if you have not assigned a custom alias to the device using MAX or the System Configuration API. For example, 'PXI1Slot3' is the default alias for the device at Slot 3 of PXI Chassis 1, and it cannot be used as an alias name for any other device. Refer to the LabVIEW Help for NI-RIO for more information about aliases. |
| −63150 | An unspecified hardware failure has occurred. The operation could not be completed. |
| −63082 | The operation could not complete because another session is accessing the FIFO. Close the other session and retry. |
| −63081 | The caller did not allocate a memory buffer. |
| −63080 | The allocated buffer is too small. |
| −63073 | The specified event did not occur within the specified time period, in milliseconds. Extend the time period, or ignore if the result was expected. |
| −63072 | The specified RIO event has not been enabled for this session. Attempting a Wait on IRQ after an Abort causes this error. |
| −63071 | The specified RIO event has already been enabled for this session. |
| −63070 | The specified event type is invalid. |
| −63052 | Trigger lines are not supported or enabled. For PXI, identify the controller and chassis using MAX. |
| −63051 | The specified trigger line is not reserved in the current session. |
| −63050 | The specified trigger line is already reserved. Consult the MAX Trigger settings or the trigger reservations for each device within the system. |
| −63044 | The RIO server could not be found on the specified remote device. Ensure that NI-RIO software is installed and that the RIO server is running and properly configured. For NI-RIO 2.3 and later, refer to Software»NI-RIO»NI-RIO Settings under the system in MAX. Prior to NI-RIO 2.3, refer to Software»NI-VISA»VISA Options under the system in MAX. |
| −63043 | The session is invalid. The target may have reset or been rebooted. Check the network connection and retry the operation. |
| −63042 | A fault on the network caused the operation to fail. |
| −63041 | The connection to the remote device has been lost due to an error on the remote device. Retry the operation. If the remote device continues to report this error, check its power supply and look for diagnostic messages on the console. |
| −63040 | A connection could not be established to the specified remote device. Ensure that the device is on and accessible over the network, that NI-RIO software is installed, and that the RIO server is running and properly configured. For NI-RIO 2.3 and forward, refer to Software»NI-RIO»NI-RIO Settings under the system in MAX. Prior to NI-RIO 2.3, refer to Software»NI-VISA»VISA Options under the system in MAX. |
| −63033 | Access to the remote system was denied. Use MAX to check the Remote Device Access settings under Software»NI-RIO»NI-RIO Settings on the remote system. |
| −63031 | The operation could not be completed because another session is accessing the device. Close all other sessions and retry. |
| −63030 | Operation failed due to device reconfiguration. Multiple sessions to FPGA devices are not supported. Close the other session and retry this operation. This error code can occur only with LabVIEW 8.2 and earlier versions. The operation could not complete because another session has reconfigured the device. |
| −63001 | DMA from host to FPGA target is not supported for this remote system. Use another method for I/O or change the controller associated with the FPGA target. |
| 63033 | Access to the remote system was denied. Use MAX to check the Remote Device Access settings under Software»NI-RIO»NI-RIO Settings on the remote system. |
| 63073 | The specified event did not occur within the specified time period, in milliseconds. Extend the time period, or ignore if the result was expected. |
| 63186 | The number of open RIO sessions exceeds the recommended limit. For optimal performance, close RIO sessions when you no longer need them. |
| 63188 | The operation is no longer supported. |
| 63194 | The target software is older than, but compatible with, the host. Upgrade target software to get full functionality. |

<!--NI_TOPIC bundle=ni-compactrio-device-api-ref path=target6devicehelp/OpenHMB.html language=enus -->
## TOPIC 00101: OpenHMB VI

- bundle_id: `ni-compactrio-device-api-ref`
- source_path: `target6devicehelp/OpenHMB.html`
- source_url: https://docs-be.ni.com/bundle/ni-compactrio-device-api-ref/raw/resource/enus/target6devicehelp/OpenHMB.html
- document_id: `ni-compactrio-device-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Host Memory Buffer Requires: NI-RIO Returns a data value reference that provides access to a host memory buffer. Use the pull-down menu to select an instance of this VI. OpenHMB_I8 Returns a data value reference that provides access to a host memory buffer. 2 18 FPGA VI Reference In

### OpenHMB VI

Owning Palette:
 [Host Memory
 Buffer](HMB_pal.html)
 Requires:
 NI-RIO

Returns a data value reference that provides access to
 a host memory buffer.

Use the pull-down menu to select an
 instance of this VI.

#### OpenHMB_I8

Returns a data value reference that provides access to a host memory
 buffer.

Figure 2.

[IMAGE alt='image' src='../images/OpenHMB_I8.gif']

|  | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| --- | --- |
|  | Memory Name the name of the memory created in the project under the FPGA, with DRAM:Host MemoryBuffer selected as its type. |
|  | error in (no error) describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | FPGA VI Reference Out returns a reference to an FPGA VI. |
|  | lvEDVR is the output to wire to an in-place element structure with a data value reference node. The data type of this output will change depending on which data type selected in the polymorphic VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

#### OpenHMB_I16

Returns a data value reference that provides access to a host memory
 buffer.

Figure 3.

[IMAGE alt='image' src='../images/OpenHMB_I16.gif']

|  | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| --- | --- |
|  | Memory Name the name of the memory created in the project under the FPGA, with DRAM:Host MemoryBuffer selected as its type. |
|  | error in (no error) describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | FPGA VI Reference Out returns a reference to an FPGA VI. |
|  | lvEDVR is the output to wire to an in-place element structure with a data value reference node. The data type of this output will change depending on which data type selected in the polymorphic VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

#### OpenHMB_I32

Returns a data value reference that provides access to a host memory
 buffer.

Figure 4.

[IMAGE alt='image' src='../images/OpenHMB_I32.gif']

|  | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| --- | --- |
|  | Memory Name the name of the memory created in the project under the FPGA, with DRAM:Host MemoryBuffer selected as its type. |
|  | error in (no error) describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | FPGA VI Reference Out returns a reference to an FPGA VI. |
|  | lvEDVR is the output to wire to an in-place element structure with a data value reference node. The data type of this output will change depending on which data type selected in the polymorphic VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

#### OpenHMB_I64

Returns a data value reference that provides access to a host memory
 buffer.

Figure 5.

[IMAGE alt='image' src='../images/OpenHMB_I64.gif']

|  | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| --- | --- |
|  | Memory Name the name of the memory created in the project under the FPGA, with DRAM:Host MemoryBuffer selected as its type. |
|  | error in (no error) describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | FPGA VI Reference Out returns a reference to an FPGA VI. |
|  | lvEDVR is the output to wire to an in-place element structure with a data value reference node. The data type of this output will change depending on which data type selected in the polymorphic VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

#### OpenHMB_U8

Returns a data value reference that provides access to a host memory
 buffer.

Figure 6.

[IMAGE alt='image' src='../images/OpenHMB_U8.gif']

|  | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| --- | --- |
|  | Memory Name the name of the memory created in the project under the FPGA, with DRAM:Host MemoryBuffer selected as its type. |
|  | error in (no error) describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | FPGA VI Reference Out returns a reference to an FPGA VI. |
|  | lvEDVR is the output to wire to an in-place element structure with a data value reference node. The data type of this output will change depending on which data type selected in the polymorphic VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

#### OpenHMB_U16

Returns a data value reference that provides access to a host memory
 buffer.

Figure 7.

[IMAGE alt='image' src='../images/OpenHMB_U16.gif']

|  | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| --- | --- |
|  | Memory Name the name of the memory created in the project under the FPGA, with DRAM:Host MemoryBuffer selected as its type. |
|  | error in (no error) describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | FPGA VI Reference Out returns a reference to an FPGA VI. |
|  | lvEDVR is the output to wire to an in-place element structure with a data value reference node. The data type of this output will change depending on which data type selected in the polymorphic VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

#### OpenHMB_U32

Returns a data value reference that provides access to a host memory
 buffer.

Figure 8.

[IMAGE alt='image' src='../images/OpenHMB_U32.gif']

|  | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| --- | --- |
|  | Memory Name the name of the memory created in the project under the FPGA, with DRAM:Host MemoryBuffer selected as its type. |
|  | error in (no error) describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | FPGA VI Reference Out returns a reference to an FPGA VI. |
|  | lvEDVR is the output to wire to an in-place element structure with a data value reference node. The data type of this output will change depending on which data type selected in the polymorphic VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

#### OpenHMB_U64

Returns a data value reference that provides access to a host memory
 buffer.

Figure 9.

[IMAGE alt='image' src='../images/OpenHMB_U64.gif']

|  | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| --- | --- |
|  | Memory Name the name of the memory created in the project under the FPGA, with DRAM:Host MemoryBuffer selected as its type. |
|  | error in (no error) describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | FPGA VI Reference Out returns a reference to an FPGA VI. |
|  | lvEDVR is the output to wire to an in-place element structure with a data value reference node. The data type of this output will change depending on which data type selected in the polymorphic VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

#### OpenHMB_SGL

Returns a data value reference that provides access to a host memory
 buffer.

Figure 10.

[IMAGE alt='image' src='../images/OpenHMB_SGL.gif']

|  | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| --- | --- |
|  | Memory Name the name of the memory created in the project under the FPGA, with DRAM:Host MemoryBuffer selected as its type. |
|  | error in (no error) describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | FPGA VI Reference Out returns a reference to an FPGA VI. |
|  | lvEDVR is the output to wire to an in-place element structure with a data value reference node. The data type of this output will change depending on which data type selected in the polymorphic VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

#### OpenHMB_BOOL

Returns a data value reference that provides access to a host memory
 buffer.

Figure 11.

[IMAGE alt='image' src='../images/OpenHMB_BOOL.gif']

|  | FPGA VI Reference In is a reference to an FPGA VI. You must open a reference to the FPGA VI to use this parameter. |
| --- | --- |
|  | Memory Name the name of the memory created in the project under the FPGA, with DRAM:Host MemoryBuffer selected as its type. |
|  | error in (no error) describes the error status before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | FPGA VI Reference Out returns a reference to an FPGA VI. |
|  | lvEDVR is the output to wire to an in-place element structure with a data value reference node. The data type of this output will change depending on which data type selected in the polymorphic VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source describes the origin of the error or warning and is, in most cases, the name of the VI or function that produced the error or warning. The default is an empty string. |

Parent topic:

Host Memory Buffer
