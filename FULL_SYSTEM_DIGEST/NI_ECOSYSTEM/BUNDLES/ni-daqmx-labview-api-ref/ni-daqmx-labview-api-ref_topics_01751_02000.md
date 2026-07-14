# NI DOCUMENT BUNDLE: ni-daqmx-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-labview-api-ref start=1751 end=2000 -->
<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-write/attr3140.html language=enus -->
## TOPIC 01751: Status:Synchronization:Unlocked Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-write/attr3140.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-write/attr3140.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the channels from devices in an unlocked target. Remarks The following table lists the characteristics of this property. Short Name Sync.UnlockedChans Data type c1dstr.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine Tru

### Status:Synchronization:Unlocked Channels

Indicates the channels from devices in an unlocked target.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sync.UnlockedChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Write Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11601-calibration-vi.html language=enus -->
## TOPIC 01752: DAQmx Adjust 11601 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11601-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11601-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a FD-11601 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 11601 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a FD-11601 device.

[IMAGE alt='icon' src='daqmx-adjust-11601-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust FieldDAQ Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11603-calibration-vi.html language=enus -->
## TOPIC 01753: DAQmx Adjust 11603 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11603-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11603-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a FD-11603 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 11603 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a FD-11603 device.

[IMAGE alt='icon' src='daqmx-adjust-11603-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust FieldDAQ Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11605-calibration-vi.html language=enus -->
## TOPIC 01754: DAQmx Adjust 11605 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11605-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11605-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a FD-11605 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 11605 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a FD-11605 device.

[IMAGE alt='icon' src='daqmx-adjust-11605-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust FieldDAQ Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11613-calibration-vi.html language=enus -->
## TOPIC 01755: DAQmx Adjust 11613 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11613-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11613-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a FD-11613 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 11613 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a FD-11613 device.

[IMAGE alt='icon' src='daqmx-adjust-11613-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust FieldDAQ Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11614-calibration-vi.html language=enus -->
## TOPIC 01756: DAQmx Adjust 11614 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11614-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11614-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a FD-11614 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 11614 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a FD-11614 device.

[IMAGE alt='icon' src='daqmx-adjust-11614-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust FieldDAQ Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11634-calibration-vi.html language=enus -->
## TOPIC 01757: DAQmx Adjust 11634 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11634-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11634-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a FD-11634 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 11634 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a FD-11634 device.

[IMAGE alt='icon' src='daqmx-adjust-11634-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust FieldDAQ Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11637-calibration-vi.html language=enus -->
## TOPIC 01758: DAQmx Adjust 11637 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11637-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11637-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a FD-11637 device. For full bridge configurations, gain and offset constants are adjusted. For all other bridge configurations, only offset constants are adjusted. This VI reports the as found error for gain and offset of the device. icon Inputs/Outputs

### DAQmx Adjust 11637 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a FD-11637 device. For full bridge configurations, gain and offset constants are adjusted. For all other bridge configurations, only offset constants are adjusted. This VI reports the as found error for gain and offset of the device.

[IMAGE alt='icon' src='daqmx-adjust-11637-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference value — reference value specifies the reference value measured using a calibrator. The value to specify depends on the bridge mode you are using. For full bridge mode, this value is the ratio, in V/V, of the DMM readings of AI+ vs AI- and EX+ vs EX-. For half bridge mode, this value is the ratio, in V/V, of the DMM readings of AI+ vs EX- and EX+ vs EX-. For quarter bridge modes, this value is the measured value of the connected resistor, in ohms. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. actualReading — actualReading indicates the value the device read during calibration. This value is used to determine gain and offset errors. asFoundGainError — asFoundGainError indicates the calculated gain error. asFoundOffsetError — asFoundOffsetError indicates the calculated offset error. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust FieldDAQ Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-15100-calibration-vi.html language=enus -->
## TOPIC 01759: DAQmx Adjust 15100 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-15100-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-15100-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a TS-15100 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference value reference value specifies in volts the know

### DAQmx Adjust 15100 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a TS-15100 device.

[IMAGE alt='icon' src='daqmx-adjust-15100-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference value — reference value specifies in volts the known voltage to use as a reference for calibration. Refer to the hardware calibration procedure for details. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust TS Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-15110-calibration-vi.html language=enus -->
## TOPIC 01760: DAQmx Adjust 15110 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-15110-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-15110-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a TS-15110 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 15110 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a TS-15110 device.

[IMAGE alt='icon' src='daqmx-adjust-15110-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies in volts the known voltage to use as a reference for calibration. Refer to the hardware calibration procedure for details. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust TS Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-15200-calibration-vi.html language=enus -->
## TOPIC 01761: DAQmx Adjust 15200 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-15200-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-15200-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a TS-15200 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 15200 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a TS-15200 device.

[IMAGE alt='icon' src='daqmx-adjust-15200-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies in volts or amperes the known voltage or amperage to use as a reference for calibration. Refer to the hardware calibration procedure for details. calibrationType — calibrationType specifies the type of adjustment data to apply during calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust TS Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4204-calibration-vi.html language=enus -->
## TOPIC 01762: DAQmx Adjust 4204 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4204-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4204-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the internal and external calibration constants for an NI 4204 device. You must connect a known voltage to the device and specify that voltage with reference voltage. icon Inputs/Outputs cdbl.png reference voltage reference voltage specifies in volts the known voltage to use as a reference f

### DAQmx Adjust 4204 Calibration VI

Adjusts the [internal and external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 4204 device. You must connect a known voltage to the device and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-4204-calibration-vi.png']

#### Inputs/Outputs

| reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. lowpass filter cutoff frequency — lowpass filter cutoff frequency specifies in Hz which lowpass filter cutoff frequency to calibrate. sample and hold enable — sample and hold enable specifies whether to calibrate the channel(s) with the sample and hold circuitry of the channel enabled. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx 42xx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4220-calibration-vi.html language=enus -->
## TOPIC 01763: DAQmx Adjust 4220 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4220-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4220-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the internal and external calibration constants for an NI 4220 device. This device requires reference signals of 0.0 volts at gains of 1, 15, 20, and 310 on a particular channel in order to perform an offset calibration for that channel. If you do not manually supply those reference signals,

### DAQmx Adjust 4220 Calibration VI

Adjusts the [internal and external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 4220 device. This device requires reference signals of 0.0 volts at gains of 1, 15, 20, and 310 on a particular channel in order to perform an offset calibration for that channel. If you do not manually supply those reference signals, the device measures them internally with sample and hold circuitry enabled.

[IMAGE alt='icon' src='daqmx-adjust-4220-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. gain — gain specifies the gain setting to calibrate. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx 42xx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4224-calibration-vi.html language=enus -->
## TOPIC 01764: DAQmx Adjust 4224 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4224-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4224-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the internal and external calibration constants for an NI 4224 device. You must connect a known voltage to the device and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the D

### DAQmx Adjust 4224 Calibration VI

Adjusts the [internal and external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 4224 device. You must connect a known voltage to the device and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-4224-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. gain — gain specifies the gain setting to calibrate. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx 42xx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4300-calibration-vi.html language=enus -->
## TOPIC 01765: DAQmx Adjust 4300 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4300-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4300-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4300. You must connect a known voltage to the device and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize

### DAQmx Adjust 4300 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4300. You must connect a known voltage to the device and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-4300-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4302-calibration-vi.html language=enus -->
## TOPIC 01766: DAQmx Adjust 4302 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4302-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4302-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4302 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference voltage reference voltage specifies the refe

### DAQmx Adjust 4302 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4302 device.

[IMAGE alt='icon' src='daqmx-adjust-4302-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies the reference value collected when verifying the calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4303-calibration-vi.html language=enus -->
## TOPIC 01767: DAQmx Adjust 4303 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4303-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4303-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4303 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference voltage reference voltage specifies the refe

### DAQmx Adjust 4303 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4303 device.

[IMAGE alt='icon' src='daqmx-adjust-4303-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies the reference value collected when verifying the calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4304-calibration-vi.html language=enus -->
## TOPIC 01768: DAQmx Adjust 4304 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4304-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4304-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4304 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference voltage reference voltage specifies the refe

### DAQmx Adjust 4304 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4304 device.

[IMAGE alt='icon' src='daqmx-adjust-4304-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies the reference value collected when verifying the calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4305-calibration-vi.html language=enus -->
## TOPIC 01769: DAQmx Adjust 4305 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4305-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4305-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4305 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference voltage reference voltage specifies the refe

### DAQmx Adjust 4305 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4305 device.

[IMAGE alt='icon' src='daqmx-adjust-4305-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies the reference value collected when verifying the calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4309-calibration-vi.html language=enus -->
## TOPIC 01770: DAQmx Adjust 4309 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4309-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4309-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4309 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference voltage reference voltage specifies the refe

### DAQmx Adjust 4309 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4309 device.

[IMAGE alt='icon' src='daqmx-adjust-4309-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies the reference value collected when verifying the calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4310-calibration-vi.html language=enus -->
## TOPIC 01771: DAQmx Adjust 4310 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4310-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4310-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4310. You must connect a known voltage to the device and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize

### DAQmx Adjust 4310 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4310. You must connect a known voltage to the device and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-4310-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4311-calibration-vi.html language=enus -->
## TOPIC 01772: DAQmx Adjust 4311 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4311-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4311-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4311 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png maximum value maximum value specifies the maximum valu

### DAQmx Adjust 4311 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4311 device.

[IMAGE alt='icon' src='daqmx-adjust-4311-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. maximum value — maximum value specifies the maximum value in the range. minimum value — minimum value specifies the minimum value in the range. reference voltage — reference voltage specifies the reference value collected when verifying the calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4322-calibration-vi.html language=enus -->
## TOPIC 01773: DAQmx Adjust 4322 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4322-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4322-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4322. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the phys

### DAQmx Adjust 4322 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4322.

[IMAGE alt='icon' src='daqmx-adjust-4322-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4339-calibration-vi.html language=enus -->
## TOPIC 01774: DAQmx Adjust 4339 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4339-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4339-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4339 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference voltage reference voltage specifies in volts

### DAQmx Adjust 4339 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4339 device.

[IMAGE alt='icon' src='daqmx-adjust-4339-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-433x-calibration-vi.html language=enus -->
## TOPIC 01775: DAQmx Adjust 433x Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-433x-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-433x-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4330 or NI PXIe-4331 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference voltage reference voltage is

### DAQmx Adjust 433x Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4330 or NI PXIe-4331 device.

[IMAGE alt='icon' src='daqmx-adjust-433x-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage is the voltage across the AI+ and AI- terminals, measured using a DMM. reference excitation — reference excitation is the voltage across the EX+ and EX- terminals, measured using a second DMM. shunt location — shunt location specifies the resistive leg of the Wheatstone bridge that has an external shunt resistor connected in parallel. R3 (12467) R3. R4 (14813) R4. None (10230) No shunt resistor connected. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| R3 (12467) | R3. |
| R4 (14813) | R4. |
| None (10230) | No shunt resistor connected. |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4353-calibration-vi.html language=enus -->
## TOPIC 01776: DAQmx Adjust 4353 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4353-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4353-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4353. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the phys

### DAQmx Adjust 4353 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4353.

[IMAGE alt='icon' src='daqmx-adjust-4353-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value collected when verifying the calibration. For ai0:1, this value is the reference voltage connected across AI0+/AI0- or AI1+/AI1-, measured using a DMM. For _cjtemp0, this value is the reference resistor connected across CJC0+/CJC0-, measured using a DMM. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4357-calibration-vi.html language=enus -->
## TOPIC 01777: DAQmx Adjust 4357 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4357-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4357-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI PXIe-4357. Refer to the calibration procedure for your device for specific calibration instructions. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize Exter

### DAQmx Adjust 4357 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI PXIe-4357. Refer to the calibration procedure for your device for specific calibration instructions.

[IMAGE alt='icon' src='daqmx-adjust-4357-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference values — reference values specifies the reference value of each physical channel measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4463-calibration-vi.html language=enus -->
## TOPIC 01778: DAQmx Adjust 4463 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4463-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4463-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for the analog output section of a NI 4463. You must connect a known voltage to the device and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created usi

### DAQmx Adjust 4463 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for the analog output section of a NI 4463. You must connect a known voltage to the device and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-4463-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust DSA Calibration Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4466-calibration-vi.html language=enus -->
## TOPIC 01779: DAQmx Adjust 4466 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4466-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4466-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the internal and external calibration for a PXIe-4466. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference voltage reference voltage specifies in volts the kno

### DAQmx Adjust 4466 Calibration VI

Adjusts the [internal and external calibration](/csh?context=nidaqmx_mxcncpts_calibration) for a PXIe-4466.

[IMAGE alt='icon' src='daqmx-adjust-4466-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust DSA Calibration Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4468-calibration-vi.html language=enus -->
## TOPIC 01780: DAQmx Adjust 4468 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4468-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4468-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the internal and external calibration for a PXIe-4468. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference voltage reference voltage specifies in volts the kno

### DAQmx Adjust 4468 Calibration VI

Adjusts the [internal and external calibration](/csh?context=nidaqmx_mxcncpts_calibration) for a PXIe-4468.

[IMAGE alt='icon' src='daqmx-adjust-4468-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust DSA Calibration Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4610-calibration-vi.html language=enus -->
## TOPIC 01781: DAQmx Adjust 4610 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4610-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4610-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 4610 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channel physical channel specifies the phys

### DAQmx Adjust 4610 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 4610 device.

[IMAGE alt='icon' src='daqmx-adjust-4610-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channel — physical channel specifies the physical channel(s) to calibrate. gain — gain specifies the gain setting to calibrate. offset — offset specifies an offset at which to begin a read operation. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust DSA Calibration Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-64xx-calibration-vi.html language=enus -->
## TOPIC 01782: DAQmx Adjust 64xx Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-64xx-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-64xx-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a 64xx Series device. You must connect a known voltage to the device and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initi

### DAQmx Adjust 64xx Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for a 64xx Series device. You must [connect a known voltage to the device](/csh?context=nidaqmx_mxdevconsid_calsigeseries) and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-64xx-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9201-calibration-vi.html language=enus -->
## TOPIC 01783: DAQmx Adjust 9201 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9201-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9201-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9201 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9201 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9201 device.

[IMAGE alt='icon' src='daqmx-adjust-9201-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9202-calibration-vi.html language=enus -->
## TOPIC 01784: DAQmx Adjust 9202 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9202-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9202-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9202 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9202 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9202 device.

[IMAGE alt='icon' src='daqmx-adjust-9202-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9203-gain-calibration-vi.html language=enus -->
## TOPIC 01785: DAQmx Adjust 9203 Gain Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9203-gain-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9203-gain-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration gain constants for an NI 9203 device. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in amps. cdbl.png rangeMax rangeMax specifies the maximum value in the range, in amps. cu32.png calhandle in calhandle in is a reference to

### DAQmx Adjust 9203 Gain Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9203 device.

[IMAGE alt='icon' src='daqmx-adjust-9203-gain-calibration-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in amps. rangeMax — rangeMax specifies the maximum value in the range, in amps. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9203-offset-calibration-vi.html language=enus -->
## TOPIC 01786: DAQmx Adjust 9203 Offset Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9203-offset-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9203-offset-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration offset constants for an NI 9203 device. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in amps. cdbl.png rangeMax rangeMax specifies the maximum value in the range, in amps. cu32.png calhandle in calhandle in is a reference t

### DAQmx Adjust 9203 Offset Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9203 device.

[IMAGE alt='icon' src='daqmx-adjust-9203-offset-calibration-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in amps. rangeMax — rangeMax specifies the maximum value in the range, in amps. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9204-calibration-vi.html language=enus -->
## TOPIC 01787: DAQmx Adjust 9204 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9204-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9204-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9204 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference value reference value specifies the reference val

### DAQmx Adjust 9204 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9204 device.

[IMAGE alt='icon' src='daqmx-adjust-9204-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9205-calibration-vi.html language=enus -->
## TOPIC 01788: DAQmx Adjust 9205 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9205-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9205-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9205 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference value reference value specifies the reference val

### DAQmx Adjust 9205 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9205 device.

[IMAGE alt='icon' src='daqmx-adjust-9205-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9206-calibration-vi.html language=enus -->
## TOPIC 01789: DAQmx Adjust 9206 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9206-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9206-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9206 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference value reference value specifies the reference val

### DAQmx Adjust 9206 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9206 device.

[IMAGE alt='icon' src='daqmx-adjust-9206-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9207-gain-calibration-vi.html language=enus -->
## TOPIC 01790: DAQmx Adjust 9207 Gain Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9207-gain-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9207-gain-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration gain constants for an NI 9207 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies t

### DAQmx Adjust 9207 Gain Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9207 device.

[IMAGE alt='icon' src='daqmx-adjust-9207-gain-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9207-offset-calibration-vi.html language=enus -->
## TOPIC 01791: DAQmx Adjust 9207 Offset Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9207-offset-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9207-offset-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration offset constants for an NI 9207 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies

### DAQmx Adjust 9207 Offset Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9207 device.

[IMAGE alt='icon' src='daqmx-adjust-9207-offset-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9208-gain-calibration-vi.html language=enus -->
## TOPIC 01792: DAQmx Adjust 9208 Gain Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9208-gain-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9208-gain-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration gain constants for an NI 9208 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies t

### DAQmx Adjust 9208 Gain Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9208 device.

[IMAGE alt='icon' src='daqmx-adjust-9208-gain-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9208-offset-calibration-vi.html language=enus -->
## TOPIC 01793: DAQmx Adjust 9208 Offset Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9208-offset-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9208-offset-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration offset constants for an NI 9208 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies

### DAQmx Adjust 9208 Offset Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9208 device.

[IMAGE alt='icon' src='daqmx-adjust-9208-offset-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9209-gain-calibration-vi.html language=enus -->
## TOPIC 01794: DAQmx Adjust 9209 Gain Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9209-gain-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9209-gain-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration gain constants for an NI 9209 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies t

### DAQmx Adjust 9209 Gain Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9209 device.

[IMAGE alt='icon' src='daqmx-adjust-9209-gain-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. input terminal configuration — input terminal configuration specifies the terminal configuration of the device. Differential (10106) Differential. RSE (10083) Non-referenced single-ended mode. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Differential (10106) | Differential. |
| RSE (10083) | Non-referenced single-ended mode. |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9209-offset-calibration-vi.html language=enus -->
## TOPIC 01795: DAQmx Adjust 9209 Offset Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9209-offset-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9209-offset-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration offset constants for an NI 9209 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies

### DAQmx Adjust 9209 Offset Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9209 device.

[IMAGE alt='icon' src='daqmx-adjust-9209-offset-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9210-calibration-vi.html language=enus -->
## TOPIC 01796: DAQmx Adjust 9210 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9210-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9210-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9210 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9210 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9210 device.

[IMAGE alt='icon' src='daqmx-adjust-9210-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9211-calibration-vi.html language=enus -->
## TOPIC 01797: DAQmx Adjust 9211 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9211-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9211-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9211 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9211 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9211 device.

[IMAGE alt='icon' src='daqmx-adjust-9211-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9212-calibration-vi.html language=enus -->
## TOPIC 01798: DAQmx Adjust 9212 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9212-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9212-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9212 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9212 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9212 device.

[IMAGE alt='icon' src='daqmx-adjust-9212-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9213-calibration-vi.html language=enus -->
## TOPIC 01799: DAQmx Adjust 9213 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9213-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9213-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9213 device. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in volts. cdbl.png rangeMax rangeMax specifies the maximum value in the range, in volts. cu32.png calhandle in calhandle in is a reference to the

### DAQmx Adjust 9213 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9213 device.

[IMAGE alt='icon' src='daqmx-adjust-9213-calibration-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in volts. rangeMax — rangeMax specifies the maximum value in the range, in volts. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9214-calibration-vi.html language=enus -->
## TOPIC 01800: DAQmx Adjust 9214 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9214-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9214-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9214 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9214 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9214 device.

[IMAGE alt='icon' src='daqmx-adjust-9214-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9215-calibration-vi.html language=enus -->
## TOPIC 01801: DAQmx Adjust 9215 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9215-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9215-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9215 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9215 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9215 device.

[IMAGE alt='icon' src='daqmx-adjust-9215-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9216-calibration-vi.html language=enus -->
## TOPIC 01802: DAQmx Adjust 9216 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9216-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9216-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9216 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9216 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9216 device.

[IMAGE alt='icon' src='daqmx-adjust-9216-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9217-calibration-vi.html language=enus -->
## TOPIC 01803: DAQmx Adjust 9217 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9217-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9217-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9217 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9217 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9217 device.

[IMAGE alt='icon' src='daqmx-adjust-9217-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9218-calibration-vi.html language=enus -->
## TOPIC 01804: DAQmx Adjust 9218 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9218-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9218-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9218 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9218 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9218 device.

[IMAGE alt='icon' src='daqmx-adjust-9218-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9219-calibration-vi.html language=enus -->
## TOPIC 01805: DAQmx Adjust 9219 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9219-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9219-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9219 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9219 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9219 device.

[IMAGE alt='icon' src='daqmx-adjust-9219-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9220-calibration-vi.html language=enus -->
## TOPIC 01806: DAQmx Adjust 9220 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9220-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9220-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9220 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9220 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9220 device.

[IMAGE alt='icon' src='daqmx-adjust-9220-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9221-calibration-vi.html language=enus -->
## TOPIC 01807: DAQmx Adjust 9221 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9221-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9221-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9221 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9221 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9221 device.

[IMAGE alt='icon' src='daqmx-adjust-9221-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9222-calibration-vi.html language=enus -->
## TOPIC 01808: DAQmx Adjust 9222 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9222-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9222-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9222 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9222 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9222 device.

[IMAGE alt='icon' src='daqmx-adjust-9222-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9223-calibration-vi.html language=enus -->
## TOPIC 01809: DAQmx Adjust 9223 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9223-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9223-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9223 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9223 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9223 device.

[IMAGE alt='icon' src='daqmx-adjust-9223-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9224-calibration-vi.html language=enus -->
## TOPIC 01810: DAQmx Adjust 9224 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9224-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9224-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9224 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9224 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9224 device.

[IMAGE alt='icon' src='daqmx-adjust-9224-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9225-calibration-vi.html language=enus -->
## TOPIC 01811: DAQmx Adjust 9225 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9225-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9225-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9225 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9225 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9225 device.

[IMAGE alt='icon' src='daqmx-adjust-9225-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9226-calibration-vi.html language=enus -->
## TOPIC 01812: DAQmx Adjust 9226 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9226-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9226-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9226 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9226 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9226 device.

[IMAGE alt='icon' src='daqmx-adjust-9226-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9227-calibration-vi.html language=enus -->
## TOPIC 01813: DAQmx Adjust 9227 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9227-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9227-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9227 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9227 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9227 device.

[IMAGE alt='icon' src='daqmx-adjust-9227-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9228-calibration-vi.html language=enus -->
## TOPIC 01814: DAQmx Adjust 9228 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9228-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9228-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9228 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9228 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9228 device.

[IMAGE alt='icon' src='daqmx-adjust-9228-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9229-calibration-vi.html language=enus -->
## TOPIC 01815: DAQmx Adjust 9229 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9229-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9229-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9229 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9229 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9229 device.

[IMAGE alt='icon' src='daqmx-adjust-9229-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9230-calibration-vi.html language=enus -->
## TOPIC 01816: DAQmx Adjust 9230 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9230-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9230-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9230 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9230 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9230 device.

[IMAGE alt='icon' src='daqmx-adjust-9230-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9231-calibration-vi.html language=enus -->
## TOPIC 01817: DAQmx Adjust 9231 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9231-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9231-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9231 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9231 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9231 device.

[IMAGE alt='icon' src='daqmx-adjust-9231-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9232-calibration-vi.html language=enus -->
## TOPIC 01818: DAQmx Adjust 9232 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9232-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9232-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9232 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9232 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9232 device.

[IMAGE alt='icon' src='daqmx-adjust-9232-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9234-gain-calibration-vi.html language=enus -->
## TOPIC 01819: DAQmx Adjust 9234 Gain Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9234-gain-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9234-gain-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration gain constants for an NI 9234 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies t

### DAQmx Adjust 9234 Gain Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) gain constants for an NI 9234 device.

[IMAGE alt='icon' src='daqmx-adjust-9234-gain-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a list or range of physical channels to this input. If you have an array of physical channels, use the DAQmx Flatten Channel String VI to convert the array to a list. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9234-offset-calibration-vi.html language=enus -->
## TOPIC 01820: DAQmx Adjust 9234 Offset Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9234-offset-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9234-offset-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration offset constants for an NI 9234 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies

### DAQmx Adjust 9234 Offset Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) offset constants for an NI 9234 device.

[IMAGE alt='icon' src='daqmx-adjust-9234-offset-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a list or range of physical channels to this input. If you have an array of physical channels, use the DAQmx Flatten Channel String VI to convert the array to a list. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9238-calibration-vi.html language=enus -->
## TOPIC 01821: DAQmx Adjust 9238 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9238-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9238-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9238 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9238 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9238 device.

[IMAGE alt='icon' src='daqmx-adjust-9238-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9239-calibration-vi.html language=enus -->
## TOPIC 01822: DAQmx Adjust 9239 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9239-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9239-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9239 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9239 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9239 device.

[IMAGE alt='icon' src='daqmx-adjust-9239-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9242-calibration-vi.html language=enus -->
## TOPIC 01823: DAQmx Adjust 9242 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9242-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9242-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9242 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the na

### DAQmx Adjust 9242 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9242 device.

[IMAGE alt='icon' src='daqmx-adjust-9242-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a list or range of physical channels to this input. If you have an array of physical channels, use the DAQmx Flatten Channel String VI to convert the array to a list. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9244-calibration-vi.html language=enus -->
## TOPIC 01824: DAQmx Adjust 9244 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9244-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9244-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9244 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the na

### DAQmx Adjust 9244 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9244 device.

[IMAGE alt='icon' src='daqmx-adjust-9244-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a list or range of physical channels to this input. If you have an array of physical channels, use the DAQmx Flatten Channel String VI to convert the array to a list. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9246-calibration-vi.html language=enus -->
## TOPIC 01825: DAQmx Adjust 9246 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9246-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9246-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration calibration constants for an NI 9246 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels spec

### DAQmx Adjust 9246 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) calibration constants for an NI 9246 device.

[IMAGE alt='icon' src='daqmx-adjust-9246-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9247-calibration-vi.html language=enus -->
## TOPIC 01826: DAQmx Adjust 9247 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9247-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9247-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration calibration constants for an NI 9247 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels spec

### DAQmx Adjust 9247 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) calibration constants for an NI 9247 device.

[IMAGE alt='icon' src='daqmx-adjust-9247-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9250-calibration-vi.html language=enus -->
## TOPIC 01827: DAQmx Adjust 9250 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9250-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9250-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9250 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9250 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9250 device.

[IMAGE alt='icon' src='daqmx-adjust-9250-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9251-calibration-vi.html language=enus -->
## TOPIC 01828: DAQmx Adjust 9251 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9251-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9251-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9251 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9251 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9251 device.

[IMAGE alt='icon' src='daqmx-adjust-9251-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9252-calibration-vi.html language=enus -->
## TOPIC 01829: DAQmx Adjust 9252 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9252-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9252-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9252 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9252 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9252 device.

[IMAGE alt='icon' src='daqmx-adjust-9252-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9253-calibration-vi.html language=enus -->
## TOPIC 01830: DAQmx Adjust 9253 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9253-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9253-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9253 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9253 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9253 device.

[IMAGE alt='icon' src='daqmx-adjust-9253-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9260-calibration-vi.html language=enus -->
## TOPIC 01831: DAQmx Adjust 9260 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9260-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9260-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9260 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9260 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9260 device.

[IMAGE alt='icon' src='daqmx-adjust-9260-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9262-calibration-vi.html language=enus -->
## TOPIC 01832: DAQmx Adjust 9262 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9262-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9262-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9262 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the na

### DAQmx Adjust 9262 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9262 device.

[IMAGE alt='icon' src='daqmx-adjust-9262-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a list or range of physical channels to this input. If you have an array of physical channels, use the DAQmx Flatten Channel String VI to convert the array to a list. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9263-calibration-vi.html language=enus -->
## TOPIC 01833: DAQmx Adjust 9263 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9263-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9263-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9263 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the na

### DAQmx Adjust 9263 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9263 device.

[IMAGE alt='icon' src='daqmx-adjust-9263-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a list or range of physical channels to this input. If you have an array of physical channels, use the DAQmx Flatten Channel String VI to convert the array to a list. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9264-calibration-vi.html language=enus -->
## TOPIC 01834: DAQmx Adjust 9264 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9264-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9264-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9264 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the na

### DAQmx Adjust 9264 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9264 device.

[IMAGE alt='icon' src='daqmx-adjust-9264-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a list or range of physical channels to this input. If you have an array of physical channels, use the DAQmx Flatten Channel String VI to convert the array to a list. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9265-calibration-vi.html language=enus -->
## TOPIC 01835: DAQmx Adjust 9265 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9265-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9265-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9265 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the na

### DAQmx Adjust 9265 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9265 device.

[IMAGE alt='icon' src='daqmx-adjust-9265-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a list or range of physical channels to this input. If you have an array of physical channels, use the DAQmx Flatten Channel String VI to convert the array to a list. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9266-calibration-vi.html language=enus -->
## TOPIC 01836: DAQmx Adjust 9266 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9266-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9266-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9266 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9266 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9266 device.

[IMAGE alt='icon' src='daqmx-adjust-9266-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9269-calibration-vi.html language=enus -->
## TOPIC 01837: DAQmx Adjust 9269 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9269-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9269-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9269 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the na

### DAQmx Adjust 9269 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9269 device.

[IMAGE alt='icon' src='daqmx-adjust-9269-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a list or range of physical channels to this input. If you have an array of physical channels, use the DAQmx Flatten Channel String VI to convert the array to a list. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9320-calibration-vi.html language=enus -->
## TOPIC 01838: DAQmx Adjust 9320 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9320-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9320-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9320 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9320 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9320 device.

[IMAGE alt='icon' src='daqmx-adjust-9320-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9628-ai-calibration-vi.html language=enus -->
## TOPIC 01839: DAQmx Adjust 9628 AI Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9628-ai-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9628-ai-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for the 9628 AI channels. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in amps. cdbl.png rangeMax rangeMax specifies the maximum value in the range, in amps. cu32.png calhandle in calhandle in is a reference to th

### DAQmx Adjust 9628 AI Calibration VI

Adjusts the external calibration constants for the 9628 AI channels.

[IMAGE alt='icon' src='daqmx-adjust-9628-ai-calibration-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in amps. rangeMax — rangeMax specifies the maximum value in the range, in amps. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9628-ao-calibration-vi.html language=enus -->
## TOPIC 01840: DAQmx Adjust 9628 AO Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9628-ao-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9628-ao-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for NI 9628 AO channels. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the

### DAQmx Adjust 9628 AO Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for NI 9628 AO channels.

[IMAGE alt='icon' src='daqmx-adjust-9628-ao-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9629-ai-calibration-vi.html language=enus -->
## TOPIC 01841: DAQmx Adjust 9629 AI Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9629-ai-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9629-ai-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for the 9629 AI channels. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in amps. cdbl.png rangeMax rangeMax specifies the maximum value in the range, in amps. cu32.png calhandle in calhandle in is a reference to th

### DAQmx Adjust 9629 AI Calibration VI

Adjusts the external calibration constants for the 9629 AI channels.

[IMAGE alt='icon' src='daqmx-adjust-9629-ai-calibration-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in amps. rangeMax — rangeMax specifies the maximum value in the range, in amps. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9629-ao-calibration-vi.html language=enus -->
## TOPIC 01842: DAQmx Adjust 9629 AO Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9629-ao-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9629-ao-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for NI 9629 AO channels. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the

### DAQmx Adjust 9629 AO Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for NI 9629 AO channels.

[IMAGE alt='icon' src='daqmx-adjust-9629-ao-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9638-ai-calibration-vi.html language=enus -->
## TOPIC 01843: DAQmx Adjust 9638 AI Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9638-ai-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9638-ai-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for the 9638 AI channels. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in amps. cdbl.png rangeMax rangeMax specifies the maximum value in the range, in amps. cu32.png calhandle in calhandle in is a reference to th

### DAQmx Adjust 9638 AI Calibration VI

Adjusts the external calibration constants for the 9638 AI channels.

[IMAGE alt='icon' src='daqmx-adjust-9638-ai-calibration-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in amps. rangeMax — rangeMax specifies the maximum value in the range, in amps. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9638-ao-calibration-vi.html language=enus -->
## TOPIC 01844: DAQmx Adjust 9638 AO Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9638-ao-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9638-ao-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for NI 9638 AO channels. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the

### DAQmx Adjust 9638 AO Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for NI 9638 AO channels.

[IMAGE alt='icon' src='daqmx-adjust-9638-ao-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9775-calibration-vi.html language=enus -->
## TOPIC 01845: DAQmx Adjust 9775 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9775-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9775-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an NI 9775 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies the ph

### DAQmx Adjust 9775 Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an NI 9775 device.

[IMAGE alt='icon' src='daqmx-adjust-9775-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. reference value — reference value specifies the reference value measured using a calibrator. coupling — coupling specifies the coupling setting to calibrate. AC (10045) AC coupling. DC (10050) DC coupling. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| AC (10045) | AC coupling. |
| DC (10050) | DC coupling. |

Parent topic:

DAQmx Adjust C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-ao-series-calibration-vi.html language=enus -->
## TOPIC 01846: DAQmx Adjust AO-Series Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-ao-series-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-ao-series-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an AO Series device. You must connect a known voltage to the device and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust AO-Series Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an AO Series device. You must [connect a known voltage to the device](/csh?context=nidaqmx_mxdevconsid_calsigaoseries) and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-ao-series-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-c-series-calibration-vi.html language=enus -->
## TOPIC 01847: DAQmx Adjust C Series Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-c-series-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-c-series-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a C Series device. The instances of this polymorphic VI correspond to the model of the device you want to calibrate. Refer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, you cannot u

### DAQmx Adjust C Series Calibration VI

Adjusts the external calibration constants for a C Series device.
 The instances of this [polymorphic VI](/csh?context=lvcore_lvhelp_using_polymorphic_vis) correspond to the model of the device you want to calibrate.
 Refer to the [calibration procedure for your device](http://www.ni.com/cgi-bin/redirect.cgi?dest=infcoprod&src=help&openagent&code=rdcalp) for detailed calibration instructions.

Note

[IMAGE alt='icon' src='daqmx-adjust-c-series-calibration-vi.png']

- [DAQmx Adjust 9201 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9201-calibration-vi.html) Adjusts the external calibration constants for an NI 9201 device.
- [DAQmx Adjust 9202 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9202-calibration-vi.html) Adjusts the external calibration constants for an NI 9202 device.
- [DAQmx Adjust 9203 Gain Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9203-gain-calibration-vi.html) Adjusts the external calibration gain constants for an NI 9203 device.
- [DAQmx Adjust 9203 Offset Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9203-offset-calibration-vi.html) Adjusts the external calibration offset constants for an NI 9203 device.
- [DAQmx Adjust 9204 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9204-calibration-vi.html) Adjusts the external calibration constants for an NI 9204 device.
- [DAQmx Adjust 9205 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9205-calibration-vi.html) Adjusts the external calibration constants for an NI 9205 device.
- [DAQmx Adjust 9206 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9206-calibration-vi.html) Adjusts the external calibration constants for an NI 9206 device.
- [DAQmx Adjust 9207 Gain Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9207-gain-calibration-vi.html) Adjusts the external calibration gain constants for an NI 9207 device.
- [DAQmx Adjust 9207 Offset Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9207-offset-calibration-vi.html) Adjusts the external calibration offset constants for an NI 9207 device.
- [DAQmx Adjust 9208 Gain Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9208-gain-calibration-vi.html) Adjusts the external calibration gain constants for an NI 9208 device.
- [DAQmx Adjust 9208 Offset Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9208-offset-calibration-vi.html) Adjusts the external calibration offset constants for an NI 9208 device.
- [DAQmx Adjust 9209 Gain Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9209-gain-calibration-vi.html) Adjusts the external calibration gain constants for an NI 9209 device.
- [DAQmx Adjust 9209 Offset Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9209-offset-calibration-vi.html) Adjusts the external calibration offset constants for an NI 9209 device.
- [DAQmx Adjust 9210 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9210-calibration-vi.html) Adjusts the external calibration constants for an NI 9210 device.
- [DAQmx Adjust 9211 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9211-calibration-vi.html) Adjusts the external calibration constants for an NI 9211 device.
- [DAQmx Adjust 9212 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9212-calibration-vi.html) Adjusts the external calibration constants for an NI 9212 device.
- [DAQmx Adjust 9213 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9213-calibration-vi.html) Adjusts the external calibration constants for an NI 9213 device.
- [DAQmx Adjust 9214 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9214-calibration-vi.html) Adjusts the external calibration constants for an NI 9214 device.
- [DAQmx Adjust 9215 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9215-calibration-vi.html) Adjusts the external calibration constants for an NI 9215 device.
- [DAQmx Adjust 9216 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9216-calibration-vi.html) Adjusts the external calibration constants for an NI 9216 device.
- [DAQmx Adjust 9217 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9217-calibration-vi.html) Adjusts the external calibration constants for an NI 9217 device.
- [DAQmx Adjust 9218 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9218-calibration-vi.html) Adjusts the external calibration constants for an NI 9218 device.
- [DAQmx Adjust 9219 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9219-calibration-vi.html) Adjusts the external calibration constants for an NI 9219 device.
- [DAQmx Adjust 9220 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9220-calibration-vi.html) Adjusts the external calibration constants for an NI 9220 device.
- [DAQmx Adjust 9221 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9221-calibration-vi.html) Adjusts the external calibration constants for an NI 9221 device.
- [DAQmx Adjust 9222 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9222-calibration-vi.html) Adjusts the external calibration constants for an NI 9222 device.
- [DAQmx Adjust 9223 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9223-calibration-vi.html) Adjusts the external calibration constants for an NI 9223 device.
- [DAQmx Adjust 9224 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9224-calibration-vi.html) Adjusts the external calibration constants for an NI 9224 device.
- [DAQmx Adjust 9225 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9225-calibration-vi.html) Adjusts the external calibration constants for an NI 9225 device.
- [DAQmx Adjust 9226 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9226-calibration-vi.html) Adjusts the external calibration constants for an NI 9226 device.
- [DAQmx Adjust 9227 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9227-calibration-vi.html) Adjusts the external calibration constants for an NI 9227 device.
- [DAQmx Adjust 9228 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9228-calibration-vi.html) Adjusts the external calibration constants for an NI 9228 device.
- [DAQmx Adjust 9229 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9229-calibration-vi.html) Adjusts the external calibration constants for an NI 9229 device.
- [DAQmx Adjust 9230 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9230-calibration-vi.html) Adjusts the external calibration constants for an NI 9230 device.
- [DAQmx Adjust 9231 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9231-calibration-vi.html) Adjusts the external calibration constants for an NI 9231 device.
- [DAQmx Adjust 9232 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9232-calibration-vi.html) Adjusts the external calibration constants for an NI 9232 device.
- [DAQmx Adjust 9234 Gain Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9234-gain-calibration-vi.html) Adjusts the external calibration gain constants for an NI 9234 device.
- [DAQmx Adjust 9234 Offset Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9234-offset-calibration-vi.html) Adjusts the external calibration offset constants for an NI 9234 device.
- [DAQmx Adjust 9238 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9238-calibration-vi.html) Adjusts the external calibration constants for an NI 9238 device.
- [DAQmx Adjust 9239 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9239-calibration-vi.html) Adjusts the external calibration constants for an NI 9239 device.
- [DAQmx Adjust 9242 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9242-calibration-vi.html) Adjusts the external calibration constants for an NI 9242 device.
- [DAQmx Adjust 9244 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9244-calibration-vi.html) Adjusts the external calibration constants for an NI 9244 device.
- [DAQmx Adjust 9246 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9246-calibration-vi.html) Adjusts the external calibration calibration constants for an NI 9246 device.
- [DAQmx Adjust 9247 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9247-calibration-vi.html) Adjusts the external calibration calibration constants for an NI 9247 device.
- [DAQmx Adjust 9250 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9250-calibration-vi.html) Adjusts the external calibration constants for an NI 9250 device.
- [DAQmx Adjust 9251 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9251-calibration-vi.html) Adjusts the external calibration constants for an NI 9251 device.
- [DAQmx Adjust 9252 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9252-calibration-vi.html) Adjusts the external calibration constants for an NI 9252 device.
- [DAQmx Adjust 9253 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9253-calibration-vi.html) Adjusts the external calibration constants for an NI 9253 device.
- [DAQmx Adjust 9260 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9260-calibration-vi.html) Adjusts the external calibration constants for an NI 9260 device.
- [DAQmx Adjust 9262 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9262-calibration-vi.html) Adjusts the external calibration constants for an NI 9262 device.
- [DAQmx Adjust 9263 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9263-calibration-vi.html) Adjusts the external calibration constants for an NI 9263 device.
- [DAQmx Adjust 9264 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9264-calibration-vi.html) Adjusts the external calibration constants for an NI 9264 device.
- [DAQmx Adjust 9265 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9265-calibration-vi.html) Adjusts the external calibration constants for an NI 9265 device.
- [DAQmx Adjust 9266 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9266-calibration-vi.html) Adjusts the external calibration constants for an NI 9266 device.
- [DAQmx Adjust 9269 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9269-calibration-vi.html) Adjusts the external calibration constants for an NI 9269 device.
- [DAQmx Adjust 9320 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9320-calibration-vi.html) Adjusts the external calibration constants for an NI 9320 device.
- [DAQmx Adjust 9628 AI Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9628-ai-calibration-vi.html) Adjusts the external calibration constants for the 9628 AI channels.
- [DAQmx Adjust 9628 AO Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9628-ao-calibration-vi.html) Adjusts the external calibration constants for NI 9628 AO channels.
- [DAQmx Adjust 9629 AI Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9629-ai-calibration-vi.html) Adjusts the external calibration constants for the 9629 AI channels.
- [DAQmx Adjust 9629 AO Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9629-ao-calibration-vi.html) Adjusts the external calibration constants for NI 9629 AO channels.
- [DAQmx Adjust 9638 AI Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9638-ai-calibration-vi.html) Adjusts the external calibration constants for the 9638 AI channels.
- [DAQmx Adjust 9638 AO Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9638-ao-calibration-vi.html) Adjusts the external calibration constants for NI 9638 AO channels.
- [DAQmx Adjust 9775 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-9775-calibration-vi.html) Adjusts the external calibration constants for an NI 9775 device.

Parent topic:

DAQmx C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ai-calibration-vi.html language=enus -->
## TOPIC 01848: DAQmx Adjust DSA AI Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ai-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ai-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for the analog input section of a DSA device. You must connect a known voltage to the device and specify that voltage with reference voltage. icon Inputs/Outputs cbool.png inputs shorted inputs shorted specifies whether the input terminals are shorted for t

### DAQmx Adjust DSA AI Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for the analog input section of a DSA device. You must connect a known voltage to the device and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-dsa-ai-calibration-vi.png']

#### Inputs/Outputs

| inputs shorted — inputs shorted specifies whether the input terminals are shorted for the calibration procedure. Refer to the calibration procedure for your device for more information. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust DSA Calibration Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ai-calibration-with-gain-and-coupling-vi.html language=enus -->
## TOPIC 01849: DAQmx Adjust DSA AI Calibration With Gain and Coupling VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ai-calibration-with-gain-and-coupling-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ai-calibration-with-gain-and-coupling-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs external calibration adjustment on a DSA device with the specified gain and coupling configuration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png reference voltag

### DAQmx Adjust DSA AI Calibration With Gain and Coupling VI

Performs external calibration adjustment on a DSA device with the specified gain and coupling configuration.

[IMAGE alt='icon' src='daqmx-adjust-dsa-ai-calibration-with-gain-and-coupling-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. This unit is Vrms for AC coupling or VDC for DC coupling. gain (dB) — gain (dB) specifies the gain setting to calibrate, in decibels. coupling — coupling specifies the coupling setting to calibrate. AC (10045) AC coupling. DC (10050) DC coupling. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| AC (10045) | AC coupling. |
| DC (10050) | DC coupling. |

Parent topic:

DAQmx Adjust DSA Calibration Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ao-calibration-vi.html language=enus -->
## TOPIC 01850: DAQmx Adjust DSA AO Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ao-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ao-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for the analog output section of a DSA device. You must use the device to generate a high voltage and low voltage at a specified gain, measure the high and low voltages, then specify the requested high voltage, low voltage, and gain along with the actual hi

### DAQmx Adjust DSA AO Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for the analog output section of a DSA device. You must use the device to generate a high voltage and low voltage at a specified gain, measure the high and low voltages, then specify the requested high voltage, low voltage, and gain along with the actual high voltage and low voltage.

[IMAGE alt='icon' src='daqmx-adjust-dsa-ao-calibration-vi.png']

#### Inputs/Outputs

| actual high voltage — actual high voltage is the actual high voltage an external sensor measures. requested high voltage — requested high voltage is the high voltage you attempted to generate at the gain setting you specified. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. channel — channel is the number of the channel to calibrate. This number is the numeric portion of the physical channel name, not the full physical channel name. requested low voltage — requested low voltage is the low voltage you attempted to generate at the gain setting you specified. actual low voltage — actual low voltage is the actual low voltage an external sensor measures. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. gain setting — gain setting is the gain setting you used when you attempted to generate the requested high voltage and requested low voltage. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust DSA Calibration Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ao-timebase-calibration-vi.html language=enus -->
## TOPIC 01851: DAQmx Adjust DSA AO Timebase Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ao-timebase-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ao-timebase-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for the timebase of a DSA device with an adjustable oscillator. You must first call the DAQmx Setup DSA AO Timebase Calibration VI and measure the frequency of the resulting sine wave. Repeat this process until calibration complete returns true. icon Inputs

### DAQmx Adjust DSA AO Timebase Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for the timebase of a DSA device with an adjustable oscillator. You must first call the DAQmx Setup DSA AO Timebase Calibration VI and measure the frequency of the resulting sine wave. Repeat this process until **calibration complete** returns true.

[IMAGE alt='icon' src='daqmx-adjust-dsa-ao-timebase-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. measured frequency — measured frequency specifies the measured frequency of the sine wave generated by the device. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. calibration complete — calibration complete returns TRUE if calibration of the device is complete. If this parameter returns FALSE, repeat the calibration process. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust DSA Calibration Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-calibration-polymorphic-vi.html language=enus -->
## TOPIC 01852: DAQmx Adjust DSA Calibration Polymorphic VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-calibration-polymorphic-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-calibration-polymorphic-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants of a DSA device. The instances of this polymorphic VI specify whether to use a specified gain and coupling configuration. icon

### DAQmx Adjust DSA Calibration Polymorphic VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants of a DSA device.

The instances of this [polymorphic VI](/csh?context=lvcore_lvhelp_using_polymorphic_vis) specify whether to use a specified gain and coupling configuration.

[IMAGE alt='icon' src='daqmx-adjust-dsa-calibration-polymorphic-vi.png']

- [DAQmx Adjust DSA AI Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ai-calibration-vi.html) Adjusts the external calibration constants for the analog input section of a DSA device. You must connect a known voltage to the device and specify that voltage with reference voltage .
- [DAQmx Adjust DSA AI Calibration With Gain and Coupling VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ai-calibration-with-gain-and-coupling-vi.html) Performs external calibration adjustment on a DSA device with the specified gain and coupling configuration.
- [DAQmx Adjust DSA Timebase Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-timebase-calibration-vi.html) Adjusts the external calibration constant for the timebase of a DSA device with an adjustable oscillator. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with reference frequency .
- [DAQmx Adjust DSA AO Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ao-calibration-vi.html) Adjusts the external calibration constants for the analog output section of a DSA device. You must use the device to generate a high voltage and low voltage at a specified gain, measure the high and low voltages, then specify the requested high voltage, low voltage, and gain along with the actual high voltage and low voltage.
- [DAQmx Adjust DSA AO Timebase Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-ao-timebase-calibration-vi.html) Adjusts the external calibration constants for the timebase of a DSA device with an adjustable oscillator. You must first call the DAQmx Setup DSA AO Timebase Calibration VI and measure the frequency of the resulting sine wave. Repeat this process until calibration complete returns true.
- [DAQmx Adjust 4463 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4463-calibration-vi.html) Adjusts the external calibration constants for the analog output section of a NI 4463. You must connect a known voltage to the device and specify that voltage with reference voltage .
- [DAQmx Adjust 4610 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4610-calibration-vi.html) Adjusts the external calibration constants for an NI 4610 device.
- [DAQmx Adjust 4466 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4466-calibration-vi.html) Adjusts the internal and external calibration for a PXIe-4466.
- [DAQmx Adjust DSA Device Timebase Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-device-timebase-calibration-vi.html) Adjusts the external calibration constant for the timebase of a DSA device with an adjustable oscillator. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with reference frequency .
- [DAQmx Adjust 4468 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4468-calibration-vi.html) Adjusts the internal and external calibration for a PXIe-4468.

Parent topic:

DAQmx DSA Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-device-timebase-calibration-vi.html language=enus -->
## TOPIC 01853: DAQmx Adjust DSA Device Timebase Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-device-timebase-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-device-timebase-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constant for the timebase of a DSA device with an adjustable oscillator. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with reference frequency. icon Inputs/Outputs cu32.png calhandle in calhandle in is a referen

### DAQmx Adjust DSA Device Timebase Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constant for the timebase of a DSA device with an adjustable oscillator. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with **reference frequency**.

[IMAGE alt='icon' src='daqmx-adjust-dsa-device-timebase-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference frequency — reference frequency specifies in hertz the frequency of the signal to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust DSA Calibration Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-timebase-calibration-vi.html language=enus -->
## TOPIC 01854: DAQmx Adjust DSA Timebase Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-timebase-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-dsa-timebase-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constant for the timebase of a DSA device with an adjustable oscillator. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with reference frequency. icon Inputs/Outputs cu32.png calhandle in calhandle in is a referen

### DAQmx Adjust DSA Timebase Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constant for the timebase of a DSA device with an adjustable oscillator. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with **reference frequency**.

[IMAGE alt='icon' src='daqmx-adjust-dsa-timebase-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference frequency — reference frequency specifies in hertz the frequency of the signal to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust DSA Calibration Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-e-series-calibration-vi.html language=enus -->
## TOPIC 01855: DAQmx Adjust E-Series Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-e-series-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-e-series-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an E Series device. You must connect a known voltage to the device and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initial

### DAQmx Adjust E-Series Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an E Series device. You must [connect a known voltage to the device](/csh?context=nidaqmx_mxdevconsid_calsigeseries) and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-e-series-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-fielddaq-calibration-vi.html language=enus -->
## TOPIC 01856: DAQmx Adjust FieldDAQ Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-fielddaq-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-fielddaq-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for a FieldDAQ device. The instances of this polymorphic VI correspond to the model of the device you want to calibrate. Refer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, you cannot u

### DAQmx Adjust FieldDAQ Calibration VI

Adjusts the external calibration constants for a FieldDAQ device. 
 The instances of this [polymorphic VI](/csh?context=lvcore_lvhelp_using_polymorphic_vis) correspond to the model of the device you want to calibrate.
 Refer to the [calibration procedure for your device](http://www.ni.com/cgi-bin/redirect.cgi?dest=infcoprod&src=help&openagent&code=rdcalp) for detailed calibration instructions.

Note

[IMAGE alt='icon' src='daqmx-adjust-fielddaq-calibration-vi.png']

- [DAQmx Adjust 11601 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11601-calibration-vi.html) Adjusts the external calibration constants for a FD-11601 device.
- [DAQmx Adjust 11603 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11603-calibration-vi.html) Adjusts the external calibration constants for a FD-11603 device.
- [DAQmx Adjust 11605 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11605-calibration-vi.html) Adjusts the external calibration constants for a FD-11605 device.
- [DAQmx Adjust 11613 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11613-calibration-vi.html) Adjusts the external calibration constants for a FD-11613 device.
- [DAQmx Adjust 11614 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11614-calibration-vi.html) Adjusts the external calibration constants for a FD-11614 device.
- [DAQmx Adjust 11634 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11634-calibration-vi.html) Adjusts the external calibration constants for a FD-11634 device.
- [DAQmx Adjust 11637 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-11637-calibration-vi.html) Adjusts the external calibration constants for a FD-11637 device. For full bridge configurations, gain and offset constants are adjusted. For all other bridge configurations, only offset constants are adjusted. This VI reports the as found error for gain and offset of the device.

Parent topic:

DAQmx FieldDAQ Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-m-series-calibration-vi.html language=enus -->
## TOPIC 01857: DAQmx Adjust M-Series Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-m-series-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-m-series-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an M Series device. You must connect a known voltage to the device and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initial

### DAQmx Adjust M-Series Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an M Series device. You must [connect a known voltage to the device](/csh?context=nidaqmx_mxdevconsid_mcalconn) and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-m-series-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-s-series-calibration-vi.html language=enus -->
## TOPIC 01858: DAQmx Adjust S-Series Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-s-series-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-s-series-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an S Series device. You must connect a known voltage to the device and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initial

### DAQmx Adjust S-Series Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an S Series device. You must connect a known voltage to the device and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-s-series-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-sc-baseboard-calibration-vi.html language=enus -->
## TOPIC 01859: DAQmx Adjust SC Baseboard Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-sc-baseboard-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-sc-baseboard-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for the baseboard of an SC Series device. You must connect a known voltage to the device and specify that voltage with reference voltage. Use the DAQmx 42xx Calibration VIs to calibrate the full signal path of NI 42xx devices after using this VI. icon Input

### DAQmx Adjust SC Baseboard Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for the baseboard of an SC Series device. You must connect a known voltage to the device and specify that voltage with **reference voltage**.

Use the [DAQmx 42xx Calibration VIs](/csh?context=nidaqmx_lvdaqmx_pal42xxcal) to calibrate the full signal path of NI 42xx devices after using this VI.

[IMAGE alt='icon' src='daqmx-adjust-sc-baseboard-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx 42xx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-sc-express-calibration-vi.html language=enus -->
## TOPIC 01860: DAQmx Adjust SC Express Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-sc-express-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-sc-express-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SC Express device. The instances of this polymorphic VI correspond to the model of the device you want to calibrate. Refer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, you canno

### DAQmx Adjust SC Express Calibration VI

Adjusts the external calibration constants for an SC Express device. 
 The instances of this [polymorphic VI](/csh?context=lvcore_lvhelp_using_polymorphic_vis) correspond to the model of the device you want to calibrate.
 Refer to the [calibration procedure for your device](http://www.ni.com/cgi-bin/redirect.cgi?dest=infcoprod&src=help&openagent&code=rdcalp) for detailed calibration instructions.

Note

[IMAGE alt='icon' src='daqmx-adjust-sc-express-calibration-vi.png']

- [DAQmx Adjust 4300 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4300-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4300. You must connect a known voltage to the device and specify that voltage with reference voltage .
- [DAQmx Adjust 4302 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4302-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4302 device.
- [DAQmx Adjust 4303 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4303-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4303 device.
- [DAQmx Adjust 4304 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4304-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4304 device.
- [DAQmx Adjust 4305 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4305-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4305 device.
- [DAQmx Adjust 4309 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4309-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4309 device.
- [DAQmx Adjust 4310 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4310-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4310. You must connect a known voltage to the device and specify that voltage with reference voltage .
- [DAQmx Adjust 4311 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4311-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4311 device.
- [DAQmx Adjust 4322 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4322-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4322.
- [DAQmx Adjust 433x Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-433x-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4330 or NI PXIe-4331 device.
- [DAQmx Adjust 4339 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4339-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4339 device.
- [DAQmx Adjust 4353 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4353-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4353.
- [DAQmx Adjust 4357 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-4357-calibration-vi.html) Adjusts the external calibration constants for an NI PXIe-4357. Refer to the calibration procedure for your device for specific calibration instructions.

Parent topic:

DAQmx SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1102-calibration-vi.html language=enus -->
## TOPIC 01861: DAQmx Adjust SCXI 1102 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1102-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1102-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1102 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust SCXI 1102 Calibration VI

Adjusts the external calibration constants for an SCXI-1102 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1102-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1104-calibration-vi.html language=enus -->
## TOPIC 01862: DAQmx Adjust SCXI 1104 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1104-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1104-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1104 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust SCXI 1104 Calibration VI

Adjusts the external calibration constants for an SCXI-1104 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1104-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1112-calibration-vi.html language=enus -->
## TOPIC 01863: DAQmx Adjust SCXI 1112 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1112-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1112-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1112 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust SCXI 1112 Calibration VI

Adjusts the external calibration constants for an SCXI-1112 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1112-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1122-calibration-vi.html language=enus -->
## TOPIC 01864: DAQmx Adjust SCXI 1122 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1122-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1122-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1122 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust SCXI 1122 Calibration VI

Adjusts the external calibration constants for an SCXI-1122 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1122-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1124-calibration-vi.html language=enus -->
## TOPIC 01865: DAQmx Adjust SCXI 1124 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1124-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1124-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1124 module. You must use the DAQmx Setup SCXI Calibration VI to generate a voltage or current. Measure that voltage or current, and specify the measured value with measured output. icon Inputs/Outputs cu32.png calhandle in calhandle in is a ref

### DAQmx Adjust SCXI 1124 Calibration VI

Adjusts the external calibration constants for an SCXI-1124 module. 
 You must use the [DAQmx Setup SCXI Calibration](/csh?context=nidaqmx_lvdaqmx_mxsetupscxical) VI to generate a voltage or current. Measure that voltage or current, and specify the measured value with **measured output**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1124-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. measured output — measured output specifies in volts or amperes the voltage or current measured at the output channel specified in the DAQmx Setup SCXI Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1125-calibration-vi.html language=enus -->
## TOPIC 01866: DAQmx Adjust SCXI 1125 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1125-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1125-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1125 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust SCXI 1125 Calibration VI

Adjusts the external calibration constants for an SCXI-1125 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1125-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1126-calibration-vi.html language=enus -->
## TOPIC 01867: DAQmx Adjust SCXI 1126 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1126-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1126-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1126 module. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with reference frequency. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you

### DAQmx Adjust SCXI 1126 Calibration VI

Adjusts the external calibration constants for an SCXI-1126 module. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with **reference frequency**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1126-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference frequency — reference frequency specifies in hertz the frequency of the signal to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1141-calibration-vi.html language=enus -->
## TOPIC 01868: DAQmx Adjust SCXI 1141 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1141-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1141-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1141 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust SCXI 1141 Calibration VI

Adjusts the external calibration constants for an SCXI-1141 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1141-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1142-calibration-vi.html language=enus -->
## TOPIC 01869: DAQmx Adjust SCXI 1142 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1142-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1142-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1142 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust SCXI 1142 Calibration VI

Adjusts the external calibration constants for an SCXI-1142 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1142-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1143-calibration-vi.html language=enus -->
## TOPIC 01870: DAQmx Adjust SCXI 1143 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1143-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1143-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1143 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust SCXI 1143 Calibration VI

Adjusts the external calibration constants for an SCXI-1143 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1143-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1502-calibration-vi.html language=enus -->
## TOPIC 01871: DAQmx Adjust SCXI 1502 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1502-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1502-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1502 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust SCXI 1502 Calibration VI

Adjusts the external calibration constants for an SCXI-1502 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1502-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1503-calibration-vi.html language=enus -->
## TOPIC 01872: DAQmx Adjust SCXI 1503 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1503-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1503-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1503 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust SCXI 1503 Calibration VI

Adjusts the external calibration constants for an SCXI-1503 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1503-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1503-current-calibration-vi.html language=enus -->
## TOPIC 01873: DAQmx Adjust SCXI 1503 Current Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1503-current-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1503-current-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the current calibration constants for an SCXI-1503 module. You must measure the current generated on the physical channel you specify and specify the measured current in measured output. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you

### DAQmx Adjust SCXI 1503 Current Calibration VI

Adjusts the current calibration constants for an SCXI-1503 module. You must measure the current generated on the **physical channel** you specify and specify the measured current in **measured output**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1503-current-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channel — physical channel specifies the physical channel to calibrate. measured current — measured current specifies in amperes the current measured at the specified physical channel. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1520-calibration-vi.html language=enus -->
## TOPIC 01874: DAQmx Adjust SCXI 1520 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1520-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1520-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1520 module. This module requires reference signals of 0.0 V at gains of 1, 15, 20, and 310 on a particular channel to perform an offset calibration for that channel. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the c

### DAQmx Adjust SCXI 1520 Calibration VI

Adjusts the external calibration constants for an SCXI-1520 module. This module requires reference signals of 0.0 V at gains of 1, 15, 20, and 310 on a particular channel to perform an offset calibration for that channel.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1520-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1521-calibration-vi.html language=enus -->
## TOPIC 01875: DAQmx Adjust SCXI 1521 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1521-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1521-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1521 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust SCXI 1521 Calibration VI

Adjusts the external calibration constants for an SCXI-1521 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1521-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-153x-calibration-vi.html language=enus -->
## TOPIC 01876: DAQmx Adjust SCXI 153x Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-153x-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-153x-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1530 or SCXI-1531 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the

### DAQmx Adjust SCXI 153x Calibration VI

Adjusts the external calibration constants for an SCXI-1530 or SCXI-1531 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-153x-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1540-calibration-vi.html language=enus -->
## TOPIC 01877: DAQmx Adjust SCXI 1540 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1540-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1540-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI-1540 module. You must connect a known voltage to the module and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initia

### DAQmx Adjust SCXI 1540 Calibration VI

Adjusts the external calibration constants for an SCXI-1540 module. You must connect a known voltage to the module and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-scxi-1540-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. input calibration source — input calibration source specifies the input source selection. Loopback0 Loopback the internal excitation voltage with 0 degree phase shift. Loopback180 Loopback the internal excitation voltage with 180 degree phase shift. Ground Connect the channel to ground. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. measured output — measured output specifies in volts the voltage measured at the output of the module. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Loopback0 | Loopback the internal excitation voltage with 0 degree phase shift. |
| Loopback180 | Loopback the internal excitation voltage with 180 degree phase shift. |
| Ground | Connect the channel to ground. |

Parent topic:

DAQmx Adjust SCXI Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-calibration-vi.html language=enus -->
## TOPIC 01878: DAQmx Adjust SCXI Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an SCXI module. The instances of this polymorphic VI correspond to the SCXI module you want to calibrate. Refer to the calibration procedure for your module for detailed calibration instructions. After you commit the calibration, you cannot undo it. If

### DAQmx Adjust SCXI Calibration VI

Adjusts the external calibration constants for an SCXI module. 
 The instances of this [polymorphic VI](/csh?context=lvcore_lvhelp_using_polymorphic_vis) correspond to the SCXI module you want to calibrate.
 Refer to the [calibration procedure for your module](http://www.ni.com/cgi-bin/redirect.cgi?dest=infcoprod&src=help&openagent&code=rdcalp) for detailed calibration instructions.

Note

[IMAGE alt='icon' src='daqmx-adjust-scxi-calibration-vi.png']

- [DAQmx Adjust SCXI 1102 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1102-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1102 module. You must connect a known voltage to the module and specify that voltage with reference voltage .
- [DAQmx Adjust SCXI 1104 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1104-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1104 module. You must connect a known voltage to the module and specify that voltage with reference voltage .
- [DAQmx Adjust SCXI 1112 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1112-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1112 module. You must connect a known voltage to the module and specify that voltage with reference voltage .
- [DAQmx Adjust SCXI 1122 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1122-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1122 module. You must connect a known voltage to the module and specify that voltage with reference voltage .
- [DAQmx Adjust SCXI 1124 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1124-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1124 module. You must use the DAQmx Setup SCXI Calibration VI to generate a voltage or current. Measure that voltage or current, and specify the measured value with measured output .
- [DAQmx Adjust SCXI 1125 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1125-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1125 module. You must connect a known voltage to the module and specify that voltage with reference voltage .
- [DAQmx Adjust SCXI 1126 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1126-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1126 module. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with reference frequency .
- [DAQmx Adjust SCXI 1141 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1141-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1141 module. You must connect a known voltage to the module and specify that voltage with reference voltage .
- [DAQmx Adjust SCXI 1142 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1142-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1142 module. You must connect a known voltage to the module and specify that voltage with reference voltage .
- [DAQmx Adjust SCXI 1143 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1143-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1143 module. You must connect a known voltage to the module and specify that voltage with reference voltage .
- [DAQmx Adjust SCXI 1502 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1502-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1502 module. You must connect a known voltage to the module and specify that voltage with reference voltage .
- [DAQmx Adjust SCXI 1503 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1503-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1503 module. You must connect a known voltage to the module and specify that voltage with reference voltage .
- [DAQmx Adjust SCXI 1503 Current Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1503-current-calibration-vi.html) Adjusts the current calibration constants for an SCXI-1503 module. You must measure the current generated on the physical channel you specify and specify the measured current in measured output .
- [DAQmx Adjust SCXI 1520 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1520-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1520 module. This module requires reference signals of 0.0 V at gains of 1, 15, 20, and 310 on a particular channel to perform an offset calibration for that channel.
- [DAQmx Adjust SCXI 1521 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1521-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1521 module. You must connect a known voltage to the module and specify that voltage with reference voltage .
- [DAQmx Adjust SCXI 153x Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-153x-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1530 or SCXI-1531 module. You must connect a known voltage to the module and specify that voltage with reference voltage .
- [DAQmx Adjust SCXI 1540 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-scxi-1540-calibration-vi.html) Adjusts the external calibration constants for an SCXI-1540 module. You must connect a known voltage to the module and specify that voltage with reference voltage .

Parent topic:

DAQmx SCXI Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-tio-timebase-calibration-vi.html language=enus -->
## TOPIC 01879: DAQmx Adjust TIO Timebase Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-tio-timebase-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-tio-timebase-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constant for the timebase of a TIO device. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with reference frequency. You cannot calibrate PXI-6608 devices with this VI. Refer to KnowledgeBase 40KGCD2F for more info

### DAQmx Adjust TIO Timebase Calibration VI

Adjusts the external calibration constant for the timebase of a TIO device. You must connect a sinusoidal signal with a known frequency to the device and specify that frequency with **reference frequency**.

Note

[IMAGE alt='icon' src='daqmx-adjust-tio-timebase-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference frequency — reference frequency specifies in hertz the frequency of the signal to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx TIO Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-ts-series-calibration-vi.html language=enus -->
## TOPIC 01880: DAQmx Adjust TS Series Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-ts-series-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-ts-series-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for NI TestScale devices. icon

### DAQmx Adjust TS Series Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for NI TestScale devices.

[IMAGE alt='icon' src='daqmx-adjust-ts-series-calibration-vi.png']

- [DAQmx Adjust 15100 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-15100-calibration-vi.html) Adjusts the external calibration constants for a TS-15100 device.
- [DAQmx Adjust 15110 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-15110-calibration-vi.html) Adjusts the external calibration constants for a TS-15110 device.
- [DAQmx Adjust 15200 Calibration VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-15200-calibration-vi.html) Adjusts the external calibration constants for a TS-15200 device.

Parent topic:

TS Cal

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-x-series-calibration-vi.html language=enus -->
## TOPIC 01881: DAQmx Adjust X Series Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-x-series-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-adjust-x-series-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjusts the external calibration constants for an X Series device. You must connect a known voltage to the device and specify that voltage with reference voltage. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initial

### DAQmx Adjust X Series Calibration VI

Adjusts the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants for an X Series device. You must [connect a known voltage to the device](/csh?context=nidaqmx_mxdevconsid_xcalconn) and specify that voltage with **reference voltage**.

[IMAGE alt='icon' src='daqmx-adjust-x-series-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. reference voltage — reference voltage specifies in volts the known voltage to use as a reference for calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-calibration-info-property-node-vi.html language=enus -->
## TOPIC 01882: DAQmx Calibration Info Property Node

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-calibration-info-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-calibration-info-property-node-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Property Node with the DAQmx Calibration Info class preselected. Right-click the Property Node and choose Select Filter from the shortcut menu to make the Property Node show only the properties supported by a particular device installed in the system or supported by all the devices installed in th

### DAQmx Calibration Info Property Node

A Property Node with the [DAQmx Calibration Info](/csh?context=nidaqmx_nidaq_daqmx_calibration_info_p) class preselected. Right-click the Property Node and choose **Select Filter** from the shortcut menu to make the Property Node show only the properties supported by a particular device installed in the system or supported by all the devices installed in the system.

[IMAGE alt='icon' src='daqmx-calibration-info-property-node-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. Active Device — Active Device is an example of a property you want to get (read) or set (write). error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

Parent topic:

DAQmx Constants & Property Nodes

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-change-external-calibration-password-vi.html language=enus -->
## TOPIC 01883: DAQmx Change External Calibration Password VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-change-external-calibration-password-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-change-external-calibration-password-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the external calibration password of the device. icon Inputs/Outputs cdaqmxscale.png device in device in is the name as configured in MAX of the device to which this operation applies. A DAQmx device name constant lists all devices installed in the system. cstr.png password password is the c

### DAQmx Change External Calibration Password VI

Changes the external calibration password of the device.

[IMAGE alt='icon' src='daqmx-change-external-calibration-password-vi.png']

#### Inputs/Outputs

| device in — device in is the name as configured in MAX of the device to which this operation applies. A DAQmx device name constant lists all devices installed in the system. password — password is the current calibration password for the device. This password is case sensitive. The default password for SCXI-15xx devices is SCXI. The default password for all other NI products is NI. newpassword — newpassword is the new password for the device. The password can be no longer than four characters. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-close-external-calibration-vi.html language=enus -->
## TOPIC 01884: DAQmx Close External Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-close-external-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-close-external-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open external calibration session. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cu32.png action action specifies how to close the calibration session. cancel (1) Closes

### DAQmx Close External Calibration VI

Closes an open [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) session.

[IMAGE alt='icon' src='daqmx-close-external-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. action — action specifies how to close the calibration session. cancel (1) Closes the session without saving any calibration changes. commit (0) Saves the calibration changes you made in the session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| cancel (1) | Closes the session without saving any calibration changes. |
| commit (0) | Saves the calibration changes you made in the session. |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-connect-sc-express-calibration-accessory-channels-vi.html language=enus -->
## TOPIC 01885: DAQmx Connect SC Express Calibration Accessory Channels VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-connect-sc-express-calibration-accessory-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-connect-sc-express-calibration-accessory-channels-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a connection on the SC Express accessory for the specified physical channel(s). icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical

### DAQmx Connect SC Express Calibration Accessory Channels VI

Configures a connection on the SC Express accessory for the specified physical channel(s).

[IMAGE alt='icon' src='daqmx-connect-sc-express-calibration-accessory-channels-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the names of the SC Express physical channel(s) to use. You can use a list or range of physical channels with this input. connection — connection specifies how channels on the SC Express accessory should be configured. The resulting configuration could connect channels to a particular external signal or some onboard terminal. The supported connections depend on the accessory. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-disconnect-sc-express-calibration-accessory-channels-vi.html language=enus -->
## TOPIC 01886: DAQmx Disconnect SC Express Calibration Accessory Channels VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-disconnect-sc-express-calibration-accessory-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-disconnect-sc-express-calibration-accessory-channels-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disconnects the configured connection on an SC Express accessory and connects the accessory in the default configuration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst

### DAQmx Disconnect SC Express Calibration Accessory Channels VI

Disconnects the configured connection on an SC Express accessory and connects the accessory in the default configuration.

[IMAGE alt='icon' src='daqmx-disconnect-sc-express-calibration-accessory-channels-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11601-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01887: DAQmx Get 11601 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11601-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11601-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be measured by a reference device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error conditions that

### DAQmx Get 11601 Calibration Adjustment Points VI

Returns the reference values to be measured by a reference device.

[IMAGE alt='icon' src='daqmx-get-11601-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get FieldDAQ Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11603-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01888: DAQmx Get 11603 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11603-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11603-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be measured by a reference device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error conditions that

### DAQmx Get 11603 Calibration Adjustment Points VI

Returns the reference values to be measured by a reference device.

[IMAGE alt='icon' src='daqmx-get-11603-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get FieldDAQ Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11605-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01889: DAQmx Get 11605 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11605-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11605-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be measured by a reference device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error conditions that

### DAQmx Get 11605 Calibration Adjustment Points VI

Returns the reference values to be measured by a reference device.

[IMAGE alt='icon' src='daqmx-get-11605-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get FieldDAQ Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11613-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01890: DAQmx Get 11613 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11613-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11613-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be measured by a reference device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error conditions that

### DAQmx Get 11613 Calibration Adjustment Points VI

Returns the reference values to be measured by a reference device.

[IMAGE alt='icon' src='daqmx-get-11613-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get FieldDAQ Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11614-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01891: DAQmx Get 11614 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11614-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11614-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be measured by a reference device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error conditions that

### DAQmx Get 11614 Calibration Adjustment Points VI

Returns the reference values to be measured by a reference device.

[IMAGE alt='icon' src='daqmx-get-11614-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get FieldDAQ Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11634-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01892: DAQmx Get 11634 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11634-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11634-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be measured by a reference device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error conditions that

### DAQmx Get 11634 Calibration Adjustment Points VI

Returns the reference values to be measured by a reference device.

[IMAGE alt='icon' src='daqmx-get-11634-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get FieldDAQ Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-15110-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01893: DAQmx Get 15110 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-15110-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-15110-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the DAC values with which to configure the device under calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 15110 Calibration Adjustment Points VI

Returns the DAC values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-15110-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get TS Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-15200-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01894: DAQmx Get 15200 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-15200-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-15200-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the DAC values with which to configure the device under calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. ci32.png calibrationType calibrationType specifies the ty

### DAQmx Get 15200 Calibration Adjustment Points VI

Returns the DAC values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-15200-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. calibrationType — calibrationType specifies the type of adjustment data to apply during calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get TS Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4302-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01895: DAQmx Get 4302 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4302-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4302-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to pass to DAQmx Adjust SC Express Calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 4302 Calibration Adjustment Points VI

Returns the reference values to pass to [DAQmx Adjust SC Express Calibration](/csh?context=nidaqmx_lvdaqmx_mxadjustscexpresscal).

[IMAGE alt='icon' src='daqmx-get-4302-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get SC Express Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4303-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01896: DAQmx Get 4303 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4303-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4303-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to pass to DAQmx Adjust SC Express Calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 4303 Calibration Adjustment Points VI

Returns the reference values to pass to [DAQmx Adjust SC Express Calibration](/csh?context=nidaqmx_lvdaqmx_mxadjustscexpresscal).

[IMAGE alt='icon' src='daqmx-get-4303-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get SC Express Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4304-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01897: DAQmx Get 4304 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4304-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4304-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to pass to DAQmx Adjust SC Express Calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 4304 Calibration Adjustment Points VI

Returns the reference values to pass to [DAQmx Adjust SC Express Calibration](/csh?context=nidaqmx_lvdaqmx_mxadjustscexpresscal).

[IMAGE alt='icon' src='daqmx-get-4304-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get SC Express Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4305-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01898: DAQmx Get 4305 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4305-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4305-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to pass to DAQmx Adjust SC Express Calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 4305 Calibration Adjustment Points VI

Returns the reference values to pass to [DAQmx Adjust SC Express Calibration](/csh?context=nidaqmx_lvdaqmx_mxadjustscexpresscal).

[IMAGE alt='icon' src='daqmx-get-4305-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get SC Express Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4322-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01899: DAQmx Get 4322 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4322-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4322-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be measured by a reference device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. ci32.png output type output type specifies the type of measurement

### DAQmx Get 4322 Calibration Adjustment Points VI

Returns the reference values to be measured by a reference device.

[IMAGE alt='icon' src='daqmx-get-4322-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. output type — output type specifies the type of measurement for the device. Voltage (10322) Voltage generation. Current (10134) Current generation. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustment Points — adjustment points is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Voltage (10322) | Voltage generation. |
| Current (10134) | Current generation. |

Parent topic:

DAQmx Get SC Express Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4339-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01900: DAQmx Get 4339 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4339-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4339-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be measured by a reference device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error conditions that

### DAQmx Get 4339 Calibration Adjustment Points VI

Returns the reference values to be measured by a reference device.

[IMAGE alt='icon' src='daqmx-get-4339-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get SC Express Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4463-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01901: DAQmx Get 4463 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4463-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4463-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be measured by a reference device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. ci32.png terminal configuration terminal configuration specifies th

### DAQmx Get 4463 Calibration Adjustment Points VI

Returns the reference values to be measured by a reference device.

[IMAGE alt='icon' src='daqmx-get-4463-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. terminal configuration — terminal configuration specifies the terminal configuration of the device. Differential (10106) Differential. Pseudodifferential (12529) Pseudodifferential. gain (dB) — gain (dB) specifies the gain setting to calibrate, in decibels. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Differential (10106) | Differential. |
| Pseudodifferential (12529) | Pseudodifferential. |

Parent topic:

DAQmx Get DSA Calibration Adjustment Points Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9201-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01902: DAQmx Get 9201 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9201-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9201-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9201 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9201-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9202-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01903: DAQmx Get 9202 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9202-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9202-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9202 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9202-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9203-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01904: DAQmx Get 9203 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9203-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9203-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference current values to be used by a reference device to create a reference signal. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in amps. cdbl.png rangeMax rangeMax specifies the maximum value in the range, in amps. cu32.png calhandle in ca

### DAQmx Get 9203 Calibration Adjustment Points VI

Returns the reference current values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9203-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in amps. rangeMax — rangeMax specifies the maximum value in the range, in amps. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9207-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01905: DAQmx Get 9207 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9207-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9207-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage or current values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physica

### DAQmx Get 9207 Calibration Adjustment Points VI

Returns the reference voltage or current values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9207-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9208-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01906: DAQmx Get 9208 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9208-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9208-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference current values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9208 Calibration Adjustment Points VI

Returns the reference current values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9208-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9209-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01907: DAQmx Get 9209 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9209-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9209-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9209 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9209-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9212-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01908: DAQmx Get 9212 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9212-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9212-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels

### DAQmx Get 9212 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9212-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9213-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01909: DAQmx Get 9213 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9213-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9213-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in volts. cdbl.png rangeMax rangeMax specifies the maximum value in the range, in volts. cu32.png calhandle in

### DAQmx Get 9213 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9213-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in volts. rangeMax — rangeMax specifies the maximum value in the range, in volts. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9214-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01910: DAQmx Get 9214 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9214-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9214-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage or resistance values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cstr.png physical ch

### DAQmx Get 9214 Calibration Adjustment Points VI

Returns the reference voltage or resistance values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9214-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9215-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01911: DAQmx Get 9215 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9215-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9215-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9215 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9215-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9216-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01912: DAQmx Get 9216 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9216-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9216-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9216 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9216-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9217-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01913: DAQmx Get 9217 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9217-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9217-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describ

### DAQmx Get 9217 Calibration Adjustment Points VI

Returns the reference values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9217-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9218-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01914: DAQmx Get 9218 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9218-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9218-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describ

### DAQmx Get 9218 Calibration Adjustment Points VI

Returns the reference values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9218-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9219-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01915: DAQmx Get 9219 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9219-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9219-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describ

### DAQmx Get 9219 Calibration Adjustment Points VI

Returns the reference values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9219-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9220-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01916: DAQmx Get 9220 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9220-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9220-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9220 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9220-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9221-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01917: DAQmx Get 9221 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9221-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9221-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9221 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9221-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9222-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01918: DAQmx Get 9222 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9222-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9222-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9222 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9222-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9223-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01919: DAQmx Get 9223 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9223-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9223-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9223 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9223-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9224-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01920: DAQmx Get 9224 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9224-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9224-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describ

### DAQmx Get 9224 Calibration Adjustment Points VI

Returns the reference values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9224-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9225-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01921: DAQmx Get 9225 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9225-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9225-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9225 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9225-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9226-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01922: DAQmx Get 9226 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9226-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9226-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9226 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9226-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9227-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01923: DAQmx Get 9227 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9227-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9227-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference current values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9227 Calibration Adjustment Points VI

Returns the reference current values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9227-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9228-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01924: DAQmx Get 9228 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9228-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9228-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describ

### DAQmx Get 9228 Calibration Adjustment Points VI

Returns the reference values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9228-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9229-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01925: DAQmx Get 9229 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9229-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9229-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9229 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9229-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9230-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01926: DAQmx Get 9230 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9230-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9230-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9230 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9230-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9231-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01927: DAQmx Get 9231 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9231-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9231-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9231 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9231-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9232-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01928: DAQmx Get 9232 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9232-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9232-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9232 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9232-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9234-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01929: DAQmx Get 9234 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9234-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9234-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9234 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9234-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9238-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01930: DAQmx Get 9238 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9238-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9238-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describ

### DAQmx Get 9238 Calibration Adjustment Points VI

Returns the reference values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9238-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9239-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01931: DAQmx Get 9239 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9239-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9239-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9239 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9239-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9242-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01932: DAQmx Get 9242 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9242-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9242-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9242 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9242-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9244-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01933: DAQmx Get 9244 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9244-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9244-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9244 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9244-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9246-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01934: DAQmx Get 9246 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9246-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9246-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9246 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9246-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9247-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01935: DAQmx Get 9247 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9247-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9247-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9247 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9247-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9250-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01936: DAQmx Get 9250 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9250-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9250-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describ

### DAQmx Get 9250 Calibration Adjustment Points VI

Returns the reference values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9250-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9251-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01937: DAQmx Get 9251 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9251-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9251-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describ

### DAQmx Get 9251 Calibration Adjustment Points VI

Returns the reference values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9251-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9252-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01938: DAQmx Get 9252 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9252-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9252-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9252 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9252-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9253-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01939: DAQmx Get 9253 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9253-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9253-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describ

### DAQmx Get 9253 Calibration Adjustment Points VI

Returns the reference values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9253-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9260-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01940: DAQmx Get 9260 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9260-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9260-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the DAC values with which to configure the device under calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 9260 Calibration Adjustment Points VI

Returns the DAC values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9260-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9262-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01941: DAQmx Get 9262 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9262-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9262-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the DAC values with which to configure the device under calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 9262 Calibration Adjustment Points VI

Returns the DAC values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9262-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9263-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01942: DAQmx Get 9263 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9263-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9263-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the DAC values with which to configure the device under calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 9263 Calibration Adjustment Points VI

Returns the DAC values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9263-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9264-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01943: DAQmx Get 9264 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9264-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9264-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the DAC values with which to configure the device under calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 9264 Calibration Adjustment Points VI

Returns the DAC values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9264-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9265-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01944: DAQmx Get 9265 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9265-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9265-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the DAC values with which to configure the device under calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 9265 Calibration Adjustment Points VI

Returns the DAC values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9265-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9266-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01945: DAQmx Get 9266 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9266-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9266-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the DAC values with which to configure the device under calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 9266 Calibration Adjustment Points VI

Returns the DAC values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9266-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9269-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01946: DAQmx Get 9269 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9269-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9269-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the DAC values with which to configure the device under calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 9269 Calibration Adjustment Points VI

Returns the DAC values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9269-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9320-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01947: DAQmx Get 9320 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9320-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9320-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in

### DAQmx Get 9320 Calibration Adjustment Points VI

Returns the reference voltage values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9320-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9628-ai-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01948: DAQmx Get 9628 AI Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9628-ai-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9628-ai-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values with which to configure the device under calibration. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in volts. cdbl.png rangeMax rangeMax specifies the maximum value in the range, in volts. cu32.png calhandle in calhandle

### DAQmx Get 9628 AI Calibration Adjustment Points VI

Returns the reference voltage values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9628-ai-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in volts. rangeMax — rangeMax specifies the maximum value in the range, in volts. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9628-ao-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01949: DAQmx Get 9628 AO Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9628-ao-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9628-ao-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the DAC values with which to configure the device under calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describes error condit

### DAQmx Get 9628 AO Calibration Adjustment Points VI

Returns the DAC values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9628-ao-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9629-ai-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01950: DAQmx Get 9629 AI Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9629-ai-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9629-ai-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values with which to configure the device under calibration. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in volts. cdbl.png rangeMax rangeMax specifies the maximum value in the range, in volts. cu32.png calhandle in calhandle

### DAQmx Get 9629 AI Calibration Adjustment Points VI

Returns the reference voltage values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9629-ai-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in volts. rangeMax — rangeMax specifies the maximum value in the range, in volts. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9629-ao-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01951: DAQmx Get 9629 AO Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9629-ao-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9629-ao-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values with which to configure the device under calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describe

### DAQmx Get 9629 AO Calibration Adjustment Points VI

Returns the reference voltage values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9629-ao-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9638-ai-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01952: DAQmx Get 9638 AI Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9638-ai-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9638-ai-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values with which to configure the device under calibration. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in volts. cdbl.png rangeMax rangeMax specifies the maximum value in the range, in volts. cu32.png calhandle in calhandle

### DAQmx Get 9638 AI Calibration Adjustment Points VI

Returns the reference voltage values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9638-ai-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in volts. rangeMax — rangeMax specifies the maximum value in the range, in volts. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9638-ao-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01953: DAQmx Get 9638 AO Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9638-ao-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9638-ao-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference voltage values with which to configure the device under calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cerrcodeclst.png error in error in describe

### DAQmx Get 9638 AO Calibration Adjustment Points VI

Returns the reference voltage values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-9638-ao-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9775-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01954: DAQmx Get 9775 Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9775-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9775-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to be used by a reference device to create a reference signal. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. ci32.png coupling coupling specifies the c

### DAQmx Get 9775 Calibration Adjustment Points VI

Returns the reference values to be used by a reference device to create a reference signal.

[IMAGE alt='icon' src='daqmx-get-9775-calibration-adjustment-points-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. coupling — coupling specifies the coupling setting to calibrate. AC (10045) AC coupling. DC (10050) DC coupling. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. adjustmentPoints — adjustmentPoints is the array of adjustment points returned by the VI. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| AC (10045) | AC coupling. |
| DC (10050) | DC coupling. |

Parent topic:

DAQmx Get C Series Calibration Adjustment Points VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-c-series-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01955: DAQmx Get C Series Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-c-series-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-c-series-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to pass to DAQmx Adjust C Series Calibration. The instances of this polymorphic VI correspond to the model of the device you want to calibrate. Refer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, you

### DAQmx Get C Series Calibration Adjustment Points VI

Returns the reference values to pass to DAQmx Adjust C Series Calibration.
 The instances of this [polymorphic VI](/csh?context=lvcore_lvhelp_using_polymorphic_vis) correspond to the model of the device you want to calibrate.
 Refer to the [calibration procedure for your device](http://www.ni.com/cgi-bin/redirect.cgi?dest=infcoprod&src=help&openagent&code=rdcalp) for detailed calibration instructions.

Note

[IMAGE alt='icon' src='daqmx-get-c-series-calibration-adjustment-points-vi.png']

- [DAQmx Get 9201 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9201-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9202 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9202-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9203 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9203-calibration-adjustment-points-vi.html) Returns the reference current values to be used by a reference device to create a reference signal.
- [DAQmx Get 9207 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9207-calibration-adjustment-points-vi.html) Returns the reference voltage or current values to be used by a reference device to create a reference signal.
- [DAQmx Get 9208 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9208-calibration-adjustment-points-vi.html) Returns the reference current values to be used by a reference device to create a reference signal.
- [DAQmx Get 9209 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9209-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9212 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9212-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9213 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9213-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9214 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9214-calibration-adjustment-points-vi.html) Returns the reference voltage or resistance values to be used by a reference device to create a reference signal.
- [DAQmx Get 9215 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9215-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9216 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9216-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9217 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9217-calibration-adjustment-points-vi.html) Returns the reference values to be used by a reference device to create a reference signal.
- [DAQmx Get 9218 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9218-calibration-adjustment-points-vi.html) Returns the reference values to be used by a reference device to create a reference signal.
- [DAQmx Get 9219 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9219-calibration-adjustment-points-vi.html) Returns the reference values to be used by a reference device to create a reference signal.
- [DAQmx Get 9220 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9220-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9221 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9221-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9222 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9222-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9223 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9223-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9224 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9224-calibration-adjustment-points-vi.html) Returns the reference values to be used by a reference device to create a reference signal.
- [DAQmx Get 9225 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9225-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9226 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9226-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9227 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9227-calibration-adjustment-points-vi.html) Returns the reference current values to be used by a reference device to create a reference signal.
- [DAQmx Get 9228 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9228-calibration-adjustment-points-vi.html) Returns the reference values to be used by a reference device to create a reference signal.
- [DAQmx Get 9229 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9229-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9230 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9230-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9231 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9231-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9232 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9232-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9234 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9234-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9238 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9238-calibration-adjustment-points-vi.html) Returns the reference values to be used by a reference device to create a reference signal.
- [DAQmx Get 9239 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9239-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9242 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9242-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9244 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9244-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9246 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9246-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9247 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9247-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9250 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9250-calibration-adjustment-points-vi.html) Returns the reference values to be used by a reference device to create a reference signal.
- [DAQmx Get 9251 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9251-calibration-adjustment-points-vi.html) Returns the reference values to be used by a reference device to create a reference signal.
- [DAQmx Get 9252 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9252-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9253 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9253-calibration-adjustment-points-vi.html) Returns the reference values to be used by a reference device to create a reference signal.
- [DAQmx Get 9260 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9260-calibration-adjustment-points-vi.html) Returns the DAC values with which to configure the device under calibration.
- [DAQmx Get 9262 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9262-calibration-adjustment-points-vi.html) Returns the DAC values with which to configure the device under calibration.
- [DAQmx Get 9263 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9263-calibration-adjustment-points-vi.html) Returns the DAC values with which to configure the device under calibration.
- [DAQmx Get 9264 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9264-calibration-adjustment-points-vi.html) Returns the DAC values with which to configure the device under calibration.
- [DAQmx Get 9265 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9265-calibration-adjustment-points-vi.html) Returns the DAC values with which to configure the device under calibration.
- [DAQmx Get 9266 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9266-calibration-adjustment-points-vi.html) Returns the DAC values with which to configure the device under calibration.
- [DAQmx Get 9269 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9269-calibration-adjustment-points-vi.html) Returns the DAC values with which to configure the device under calibration.
- [DAQmx Get 9320 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9320-calibration-adjustment-points-vi.html) Returns the reference voltage values to be used by a reference device to create a reference signal.
- [DAQmx Get 9628 AI Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9628-ai-calibration-adjustment-points-vi.html) Returns the reference voltage values with which to configure the device under calibration.
- [DAQmx Get 9628 AO Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9628-ao-calibration-adjustment-points-vi.html) Returns the DAC values with which to configure the device under calibration.
- [DAQmx Get 9629 AI Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9629-ai-calibration-adjustment-points-vi.html) Returns the reference voltage values with which to configure the device under calibration.
- [DAQmx Get 9629 AO Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9629-ao-calibration-adjustment-points-vi.html) Returns the reference voltage values with which to configure the device under calibration.
- [DAQmx Get 9638 AI Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9638-ai-calibration-adjustment-points-vi.html) Returns the reference voltage values with which to configure the device under calibration.
- [DAQmx Get 9638 AO Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9638-ao-calibration-adjustment-points-vi.html) Returns the reference voltage values with which to configure the device under calibration.
- [DAQmx Get 9775 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-9775-calibration-adjustment-points-vi.html) Returns the reference values to be used by a reference device to create a reference signal.

Parent topic:

DAQmx C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-dsa-calibration-adjustment-points-polymorphic-vi.html language=enus -->
## TOPIC 01956: DAQmx Get DSA Calibration Adjustment Points Polymorphic VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-dsa-calibration-adjustment-points-polymorphic-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-dsa-calibration-adjustment-points-polymorphic-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to pass to DAQmx Adjust DSA Calibration. The instances of this polymorphic VI correspond to the model of the device you want to calibrate. Refer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, you cann

### DAQmx Get DSA Calibration Adjustment Points Polymorphic VI

Returns the reference values to pass to DAQmx Adjust DSA Calibration.
 The instances of this [polymorphic VI](/csh?context=lvcore_lvhelp_using_polymorphic_vis) correspond to the model of the device you want to calibrate.
 Refer to the [calibration procedure for your device](http://www.ni.com/cgi-bin/redirect.cgi?dest=infcoprod&src=help&openagent&code=rdcalp) for detailed calibration instructions.

Note

[IMAGE alt='icon' src='daqmx-get-dsa-calibration-adjustment-points-polymorphic-vi.png']

- [DAQmx Get 4463 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4463-calibration-adjustment-points-vi.html) Returns the reference values to be measured by a reference device.

Parent topic:

DAQmx DSA Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-fielddaq-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01957: DAQmx Get FieldDAQ Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-fielddaq-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-fielddaq-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to pass to DAQmx Adjust FieldDAQ Calibration. The instances of this polymorphic VI correspond to the model of the device you want to calibrate. Refer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, you

### DAQmx Get FieldDAQ Calibration Adjustment Points VI

Returns the reference values to pass to DAQmx Adjust FieldDAQ Calibration.
 The instances of this [polymorphic VI](/csh?context=lvcore_lvhelp_using_polymorphic_vis) correspond to the model of the device you want to calibrate.
 Refer to the [calibration procedure for your device](http://www.ni.com/cgi-bin/redirect.cgi?dest=infcoprod&src=help&openagent&code=rdcalp) for detailed calibration instructions.

Note

[IMAGE alt='icon' src='daqmx-get-fielddaq-calibration-adjustment-points-vi.png']

- [DAQmx Get 11601 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11601-calibration-adjustment-points-vi.html) Returns the reference values to be measured by a reference device.
- [DAQmx Get 11603 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11603-calibration-adjustment-points-vi.html) Returns the reference values to be measured by a reference device.
- [DAQmx Get 11605 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11605-calibration-adjustment-points-vi.html) Returns the reference values to be measured by a reference device.
- [DAQmx Get 11613 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11613-calibration-adjustment-points-vi.html) Returns the reference values to be measured by a reference device.
- [DAQmx Get 11614 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11614-calibration-adjustment-points-vi.html) Returns the reference values to be measured by a reference device.
- [DAQmx Get 11634 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-11634-calibration-adjustment-points-vi.html) Returns the reference values to be measured by a reference device.

Parent topic:

DAQmx FieldDAQ Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-possible-sc-express-calibration-accessory-connections-vi.html language=enus -->
## TOPIC 01958: DAQmx Get Possible SC Express Calibration Accessory Connections VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-possible-sc-express-calibration-accessory-connections-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-possible-sc-express-calibration-accessory-connections-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the available connections on an SC Express accessory for the specified physical channel(s). Connections specify how channels on the SC Express accessory should be configured. The resulting configuration could connect channels to a particular external signal or an onboard terminal. icon Inputs/O

### DAQmx Get Possible SC Express Calibration Accessory Connections VI

Gets the available connections on an SC Express accessory for the specified physical channel(s). Connections specify how channels on the SC Express accessory should be configured. The resulting configuration could connect channels to a particular external signal or an onboard terminal.

[IMAGE alt='icon' src='daqmx-get-possible-sc-express-calibration-accessory-connections-vi.png']

#### Inputs/Outputs

| device — device specifies the name of the SC Express accessory to use. physical channels — physical channels specifies the names of the SC Express physical channel(s) to use. You can use a list or range of physical channels with this input. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. connections — connections contains the available connections for your accessory. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-sc-express-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01959: DAQmx Get SC Express Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-sc-express-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-sc-express-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference values to pass to DAQmx Adjust SC Express Calibration. The instances of this polymorphic VI correspond to the model of the device you want to calibrate. Refer to the calibration procedure for your device for detailed calibration instructions. After you commit the calibration, y

### DAQmx Get SC Express Calibration Adjustment Points VI

Returns the reference values to pass to DAQmx Adjust SC Express Calibration.
 The instances of this [polymorphic VI](/csh?context=lvcore_lvhelp_using_polymorphic_vis) correspond to the model of the device you want to calibrate.
 Refer to the [calibration procedure for your device](http://www.ni.com/cgi-bin/redirect.cgi?dest=infcoprod&src=help&openagent&code=rdcalp) for detailed calibration instructions.

Note

[IMAGE alt='icon' src='daqmx-get-sc-express-calibration-adjustment-points-vi.png']

- [DAQmx Get 4302 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4302-calibration-adjustment-points-vi.html) Returns the reference values to pass to DAQmx Adjust SC Express Calibration .
- [DAQmx Get 4303 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4303-calibration-adjustment-points-vi.html) Returns the reference values to pass to DAQmx Adjust SC Express Calibration .
- [DAQmx Get 4304 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4304-calibration-adjustment-points-vi.html) Returns the reference values to pass to DAQmx Adjust SC Express Calibration .
- [DAQmx Get 4305 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4305-calibration-adjustment-points-vi.html) Returns the reference values to pass to DAQmx Adjust SC Express Calibration .
- [DAQmx Get 4322 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4322-calibration-adjustment-points-vi.html) Returns the reference values to be measured by a reference device.
- [DAQmx Get 4339 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-4339-calibration-adjustment-points-vi.html) Returns the reference values to be measured by a reference device.

Parent topic:

DAQmx SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-ts-series-calibration-adjustment-points-vi.html language=enus -->
## TOPIC 01960: DAQmx Get TS Series Calibration Adjustment Points VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-ts-series-calibration-adjustment-points-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-ts-series-calibration-adjustment-points-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the DAC or reference values with which to configure the device under calibration. icon

### DAQmx Get TS Series Calibration Adjustment Points VI

Returns the DAC or reference values with which to configure the device under calibration.

[IMAGE alt='icon' src='daqmx-get-ts-series-calibration-adjustment-points-vi.png']

- [DAQmx Get 15110 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-15110-calibration-adjustment-points-vi.html) Returns the DAC values with which to configure the device under calibration.
- [DAQmx Get 15200 Calibration Adjustment Points VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-get-15200-calibration-adjustment-points-vi.html) Returns the DAC values with which to configure the device under calibration.

Parent topic:

TS Cal

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-initialize-external-calibration-vi.html language=enus -->
## TOPIC 01961: DAQmx Initialize External Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-initialize-external-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-initialize-external-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts an external calibration session on a device. icon Inputs/Outputs cdaqmxscale.png device in device in is the name as configured in MAX of the device to which this operation applies. A DAQmx device name constant lists all devices installed in the system. cstr.png password password is the curren

### DAQmx Initialize External Calibration VI

Starts an [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) session on a device.

[IMAGE alt='icon' src='daqmx-initialize-external-calibration-vi.png']

#### Inputs/Outputs

| device in — device in is the name as configured in MAX of the device to which this operation applies. A DAQmx device name constant lists all devices installed in the system. password — password is the current calibration password for the device. This password is case sensitive. The default password for SCXI-15xx devices is SCXI. The default password for all other NI products is NI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-bridge-offset-nulling-calibration-vi.html language=enus -->
## TOPIC 01962: DAQmx Perform Bridge Offset Nulling Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-bridge-offset-nulling-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-bridge-offset-nulling-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a bridge offset nulling calibration on the channels in the task. If the task measures both bridge-based sensors and non-bridge-based sensors, use the channels input to specify the names of the channels that measure bridge-based sensors. icon Inputs/Outputs cgenclassrntag.png task/channels i

### DAQmx Perform Bridge Offset Nulling Calibration VI

Performs a bridge offset nulling calibration on the channels in the task. If the task measures both bridge-based sensors and non-bridge-based sensors, use the **channels** input to specify the names of the channels that measure bridge-based sensors.

[IMAGE alt='icon' src='daqmx-perform-bridge-offset-nulling-calibration-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. channels — channels is a subset of virtual channels in the task that you want to calibrate. Use this input if you do not want to calibrate all the channels in the task or if some channels in the task measure non-bridge-based sensors. If the input is empty, this VI attempts to calibrate all virtual channels in the task. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. skip unsupported channels — skip unsupported channels specifies whether or not to skip channels that do not support calibration. If skip unsupported channels is TRUE, this VI calibrates only supported channels. If FALSE, this VI calibrates the channels specified by channels. The default is FALSE. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-shunt-calibration-ex-bridge-vi.html language=enus -->
## TOPIC 01963: DAQmx Perform Shunt Calibration Ex (Bridge) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-shunt-calibration-ex-bridge-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-shunt-calibration-ex-bridge-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs shunt calibration for the specified channels using a bridge sensor. icon Inputs/Outputs ci32.png shunt source shunt source specifies which shunt to use. Default (-1) Use the default shunt. User Provided (10167) Use an external shunt. Built-In (10200) Use the internal shunt. ci32.png shunt s

### DAQmx Perform Shunt Calibration Ex (Bridge) VI

Performs shunt calibration for the specified channels using a bridge sensor.

[IMAGE alt='icon' src='daqmx-perform-shunt-calibration-ex-bridge-vi.png']

#### Inputs/Outputs

| shunt source — shunt source specifies which shunt to use. Default (-1) Use the default shunt. User Provided (10167) Use an external shunt. Built-In (10200) Use the internal shunt. shunt select — shunt select specifies which shunt calibration switch to enable. A (12513) Switch A. B (12514) Switch B. bridge resistance — bridge resistance specifies the bridge resistance in ohms. A value of -1 means to use the nominal bridge resistance specified when you created the virtual channel. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. channels — channels is a subset of virtual channels in the task that you want to calibrate. Use this input if you do not want to calibrate all the channels in the task or if some channels in the task measure non-bridge-based sensors. If the input is empty, this VI attempts to calibrate all virtual channels in the task. shunt resistance — shunt resistance specifies the shunt resistance in ohms. shunt element location — shunt element location specifies the location of the shunt resistor. R1 (12465) Between VCH- and VEX+. R2 (12466) Between VCH- and VEX-. R3 (12467) Between VCH+ and VEX-. R4 (14813) Between VCH+ and VEX+. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. skip unsupported channels — skip unsupported channels specifies whether or not to skip channels that do not support calibration. If skip unsupported channels is TRUE, this VI calibrates only supported channels. If FALSE, this VI calibrates the channels specified by channels. The default is FALSE. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Default (-1) | Use the default shunt. |
| User Provided (10167) | Use an external shunt. |
| Built-In (10200) | Use the internal shunt. |
| A (12513) | Switch A. |
| B (12514) | Switch B. |
| R1 (12465) | Between VCH- and VEX+. |
| R2 (12466) | Between VCH- and VEX-. |
| R3 (12467) | Between VCH+ and VEX-. |
| R4 (14813) | Between VCH+ and VEX+. |

Parent topic:

DAQmx Perform Shunt Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-shunt-calibration-ex-strain-vi.html language=enus -->
## TOPIC 01964: DAQmx Perform Shunt Calibration Ex (Strain) VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-shunt-calibration-ex-strain-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-shunt-calibration-ex-strain-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs shunt calibration for the specified channels using a strain gage sensor. icon Inputs/Outputs ci32.png shunt source shunt source specifies which shunt to use. Default (-1) Use the default shunt. User Provided (10167) Use an external shunt. Built-In (10200) Use the internal shunt. ci32.png sh

### DAQmx Perform Shunt Calibration Ex (Strain) VI

Performs shunt calibration for the specified channels using a strain gage sensor.

[IMAGE alt='icon' src='daqmx-perform-shunt-calibration-ex-strain-vi.png']

#### Inputs/Outputs

| shunt source — shunt source specifies which shunt to use. Default (-1) Use the default shunt. User Provided (10167) Use an external shunt. Built-In (10200) Use the internal shunt. shunt select — shunt select specifies which shunt calibration switch to enable. A (12513) Switch A. B (12514) Switch B. task/channels in — task/channels in is the name of the task or a list of virtual channels to which the operation applies. If you provide a list of virtual channels, NI-DAQmx creates a task automatically. channels — channels is a subset of virtual channels in the task that you want to calibrate. Use this input if you do not want to calibrate all the channels in the task or if some channels in the task measure non-bridge-based sensors. If the input is empty, this VI attempts to calibrate all virtual channels in the task. shunt resistance — shunt resistance specifies the shunt resistance in ohms. shunt element location — shunt element location specifies the location of the shunt resistor. R1 (12465) Between VCH- and VEX+. R2 (12466) Between VCH- and VEX-. R3 (12467) Between VCH+ and VEX-. R4 (14813) Between VCH+ and VEX+. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. skip unsupported channels — skip unsupported channels specifies whether or not to skip channels that do not support calibration. If skip unsupported channels is TRUE, this VI calibrates only supported channels. If FALSE, this VI calibrates the channels specified by channels. The default is FALSE. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Default (-1) | Use the default shunt. |
| User Provided (10167) | Use an external shunt. |
| Built-In (10200) | Use the internal shunt. |
| A (12513) | Switch A. |
| B (12514) | Switch B. |
| R1 (12465) | Between VCH- and VEX+. |
| R2 (12466) | Between VCH- and VEX-. |
| R3 (12467) | Between VCH+ and VEX-. |
| R4 (14813) | Between VCH+ and VEX+. |

Parent topic:

DAQmx Perform Shunt Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-shunt-calibration-vi.html language=enus -->
## TOPIC 01965: DAQmx Perform Shunt Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-shunt-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-shunt-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs shunt calibration for the specified channels of the task. The instances of this polymorphic VI correspond to the type of bridge sensor. Refer to the calibration procedure for your module for detailed calibration instructions. icon

### DAQmx Perform Shunt Calibration VI

Performs shunt calibration for the specified channels of the task. The instances of this [polymorphic VI](/csh?context=lvcore_lvhelp_using_polymorphic_vis) correspond to the type of bridge sensor. Refer to the calibration procedure for your module for detailed calibration instructions.

[IMAGE alt='icon' src='daqmx-perform-shunt-calibration-vi.png']

- [DAQmx Perform Shunt Calibration Ex (Strain) VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-shunt-calibration-ex-strain-vi.html) Performs shunt calibration for the specified channels using a strain gage sensor.
- [DAQmx Perform Shunt Calibration Ex (Bridge) VI](../../../../vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-shunt-calibration-ex-bridge-vi.html) Performs shunt calibration for the specified channels using a bridge sensor.

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-thermocouple-lead-offset-nulling-calibration-vi.html language=enus -->
## TOPIC 01966: DAQmx Perform Thermocouple Lead Offset Nulling Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-thermocouple-lead-offset-nulling-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-perform-thermocouple-lead-offset-nulling-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. Keep the measured temperature as constant as possible while performing this adjustment. icon Inputs/Outputs cgenclassrntag.png task/channels in task/

### DAQmx Perform Thermocouple Lead Offset Nulling Calibration VI

Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection.

Keep the measured temperature as constant as possible while performing this adjustment.

[IMAGE alt='icon' src='daqmx-perform-thermocouple-lead-offset-nulling-calibration-vi.png']

#### Inputs/Outputs

| task/channels in — task/channels in is the task that contains the local or global channel you want to save. If you use a DAQmx global channel constant or control to select a global channel to modify and save, wire that constant or control to both this input and the channel name input. channels — channels is a subset of virtual channels in the task that you want to calibrate. Use this input if you do not want to calibrate all the channels in the task or if some channels in the task have open thermocouple detection disabled. If the input is empty, this VI attempts to calibrate all virtual channels in the task. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. skip unsupported channels — skip unsupported channels specifies whether or not to skip channels that do not support calibration. If skip unsupported channels is TRUE, this VI calibrates only supported channels. If FALSE, this VI calibrates the channels specified by channels. The default is FALSE. task out — task out is a reference to the task after this VI or function runs. If you wired a channel or list of channels to task/channels in, NI-DAQmx creates this task automatically. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-restore-last-external-calibration-constants-vi.html language=enus -->
## TOPIC 01967: DAQmx Restore Last External Calibration Constants VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-restore-last-external-calibration-constants-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-restore-last-external-calibration-constants-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the self-calibration constants of the device to the external calibration constants. NI sets the external calibration constants at the factory, and those constants remain in effect until you perform a new external calibration on the device. This VI nullifies any self-calibration you perform on t

### DAQmx Restore Last External Calibration Constants VI

Sets the [self-calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants of the device to the [external calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants. NI sets the external calibration constants at the factory, and those constants remain in effect until you perform a new external calibration on the device.

This VI nullifies any self-calibration you perform on the device. If you have never performed a self-calibration on the device, this VI has no effect.

[IMAGE alt='icon' src='daqmx-restore-last-external-calibration-constants-vi.png']

#### Inputs/Outputs

| device in — device in is the name as configured in MAX of the device to which this operation applies. A DAQmx device name constant lists all devices installed in the system. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-self-calibrate-vi.html language=enus -->
## TOPIC 01968: DAQmx Self Calibrate VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-self-calibrate-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-self-calibrate-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measures the onboard reference voltage of the device and adjusts the self-calibration constants to account for any errors caused by short-term fluctuations in the operating environment. When you self-calibrate a device, no external signal connections are necessary. For 42xx devices, this VI performs

### DAQmx Self Calibrate VI

Measures the onboard reference voltage of the device and adjusts the [self-calibration](/csh?context=nidaqmx_mxcncpts_calibration) constants to account for any errors caused by short-term fluctuations in the operating environment. When you self-calibrate a device, no external signal connections are necessary.

For 42xx devices, this VI performs a self-calibration on the 4200 baseboard, then performs an offset-only calibration on the full signal path of the device.

[IMAGE alt='icon' src='daqmx-self-calibrate-vi.png']

#### Inputs/Outputs

| device in — device in is the name as configured in MAX of the device to which this operation applies. A DAQmx device name constant lists all devices installed in the system. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-sc-express-calibration-accessory-bridge-output-vi.html language=enus -->
## TOPIC 01969: DAQmx Set SC Express Calibration Accessory Bridge Output VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-sc-express-calibration-accessory-bridge-output-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-sc-express-calibration-accessory-bridge-output-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an SC Express accessory to produce the bridge output specified in volts-per-volt. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png bridge output bridge output spec

### DAQmx Set SC Express Calibration Accessory Bridge Output VI

Configures an SC Express accessory to produce the bridge output specified in volts-per-volt.

[IMAGE alt='icon' src='daqmx-set-sc-express-calibration-accessory-bridge-output-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. bridge output — bridge output specifies the bridge output in volts-per-volt to be set on the SC Express accessory. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx SC Express Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-temperature-c-series-calibration-vi.html language=enus -->
## TOPIC 01970: DAQmx Set Temperature C Series Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-temperature-c-series-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-temperature-c-series-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the temperature of a C Series device for the current external calibration session. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png temperature temperature specifie

### DAQmx Set Temperature C Series Calibration VI

Specifies the temperature of a C Series device for the current external calibration session.

[IMAGE alt='icon' src='daqmx-set-temperature-c-series-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. temperature — temperature specifies the temperature of the device, in degrees Celsius. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx C Series Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-temperature-dsa-calibration-vi.html language=enus -->
## TOPIC 01971: DAQmx Set Temperature DSA Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-temperature-dsa-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-temperature-dsa-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the temperature of a DSA device for the current external calibration session. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png temperature temperature specifies the

### DAQmx Set Temperature DSA Calibration VI

Specifies the temperature of a DSA device for the current external calibration session.

[IMAGE alt='icon' src='daqmx-set-temperature-dsa-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. temperature — temperature specifies the temperature of the device, in degrees Celsius. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx DSA Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-temperature-fielddaq-calibration-vi.html language=enus -->
## TOPIC 01972: DAQmx Set Temperature FieldDAQ Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-temperature-fielddaq-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-temperature-fielddaq-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the temperature of a FieldDAQ device for the current external calibration session. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png temperature temperature specifie

### DAQmx Set Temperature FieldDAQ Calibration VI

Specifies the temperature of a FieldDAQ device for the current external calibration session.

[IMAGE alt='icon' src='daqmx-set-temperature-fielddaq-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. temperature — temperature specifies the temperature of the device, in degrees Celsius. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx FieldDAQ Calibration

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-temperature-ts-series-calibration-vi.html language=enus -->
## TOPIC 01973: DAQmx Set Temperature TS Series Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-temperature-ts-series-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-set-temperature-ts-series-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the temperature of a TestScale device for the current external calibration session. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdbl.png temperature temperature specifi

### DAQmx Set Temperature TS Series Calibration VI

Specifies the temperature of a TestScale device for the current external calibration session.

[IMAGE alt='icon' src='daqmx-set-temperature-ts-series-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. temperature — temperature specifies the temperature of the device, in degrees Celsius. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

TS Cal

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-11605-calibration-vi.html language=enus -->
## TOPIC 01974: DAQmx Setup 11605 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-11605-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-11605-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes the NI FD-11605 device with the specified range. Refer to the calibration procedure for your device for specific calibration instructions. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range. cdbl.png rangeMax rangeMax specifies the maximum value in th

### DAQmx Setup 11605 Calibration VI

Initializes the NI FD-11605 device with the specified range. Refer to the calibration procedure for your device for specific calibration instructions.

[IMAGE alt='icon' src='daqmx-setup-11605-calibration-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range. rangeMax — rangeMax specifies the maximum value in the range. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup FieldDAQ Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-11634-calibration-vi.html language=enus -->
## TOPIC 01975: DAQmx Setup 11634 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-11634-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-11634-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes the NI FD-11634 device with the specified range. Refer to the calibration procedure for your device for specific calibration instructions. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range. cdbl.png rangeMax rangeMax specifies the maximum value in th

### DAQmx Setup 11634 Calibration VI

Initializes the NI FD-11634 device with the specified range. Refer to the calibration procedure for your device for specific calibration instructions.

[IMAGE alt='icon' src='daqmx-setup-11634-calibration-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range. rangeMax — rangeMax specifies the maximum value in the range. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup FieldDAQ Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-11637-calibration-vi.html language=enus -->
## TOPIC 01976: DAQmx Setup 11637 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-11637-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-11637-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets up external calibration of a single channel for a FD-11637 device. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels specifies

### DAQmx Setup 11637 Calibration VI

Sets up external calibration of a single channel for a FD-11637 device.

[IMAGE alt='icon' src='daqmx-setup-11637-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. bridge config — bridge config specifies the Wheatstone bridge configuration connected to the channel. Full Bridge (10182) Four active sensing elements in the bridge. Half Bridge (10187) Two active sensing elements in the bridge. Quarter Bridge 350 Ohm Completion Resistor (16164) One active sensing element with a 350 ohm completion resistor. Quarter Bridge 120 Ohm Completion Resistor (16163) One active sensing element with a 120 ohm completion resistor. excitationValue — excitationValue specifies in volts the amount of excitation supplied to the sensor. Refer to the sensor documentation to determine appropriate excitation values. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Full Bridge (10182) | Four active sensing elements in the bridge. |
| Half Bridge (10187) | Two active sensing elements in the bridge. |
| Quarter Bridge 350 Ohm Completion Resistor (16164) | One active sensing element with a 350 ohm completion resistor. |
| Quarter Bridge 120 Ohm Completion Resistor (16163) | One active sensing element with a 120 ohm completion resistor. |

Parent topic:

DAQmx Setup FieldDAQ Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-15110-calibration-vi.html language=enus -->
## TOPIC 01977: DAQmx Setup 15110 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-15110-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-15110-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the specified binary value to the DAC on the specified physical channel. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels sp

### DAQmx Setup 15110 Calibration VI

Writes the specified binary value to the DAC on the specified physical channel.

[IMAGE alt='icon' src='daqmx-setup-15110-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a list or range of physical channels to this input. If you have an array of physical channels, use the DAQmx Flatten Channel String VI to convert the array to a list. DAC value — DAC value specifies, in volts, the known voltage to use as a reference for calibration. Refer to the hardware calibration procedure for details. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup TS Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-15200-calibration-vi.html language=enus -->
## TOPIC 01978: DAQmx Setup 15200 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-15200-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-15200-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the specified binary value to the DAC on the specified physical channel. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physical channels physical channels sp

### DAQmx Setup 15200 Calibration VI

Writes the specified binary value to the DAC on the specified physical channel.

[IMAGE alt='icon' src='daqmx-setup-15200-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the names of the physical channels to use to create virtual channels. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a list or range of physical channels to this input. If you have an array of physical channels, use the DAQmx Flatten Channel String VI to convert the array to a list. adjustment point — adjustment point is the adjustment point value to read from the ADC. calibrationType — calibrationType specifies the type of adjustment data to apply during calibration. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup TS Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4302-calibration-vi.html language=enus -->
## TOPIC 01979: DAQmx Setup 4302 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4302-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4302-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an NI PXIe-4302 device with the specified mode, range, and excitation for calibration. Refer to the calibration procedure for your device for specific calibration instructions. icon Inputs/Outputs cdbl.png range min range min specifies the minimum value in the range. cdbl.png range max r

### DAQmx Setup 4302 Calibration VI

Initializes an NI PXIe-4302 device with the specified mode, range, and excitation for calibration. Refer to the calibration procedure for your device for specific calibration instructions.

[IMAGE alt='icon' src='daqmx-setup-4302-calibration-vi.png']

#### Inputs/Outputs

| range min — range min specifies the minimum value in the range. range max — range max specifies the maximum value in the range. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4303-calibration-vi.html language=enus -->
## TOPIC 01980: DAQmx Setup 4303 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4303-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4303-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an NI PXIe-4303 device with the specified mode, range, and excitation for calibration. Refer to the calibration procedure for your device for specific calibration instructions. icon Inputs/Outputs cdbl.png range min range min specifies the minimum value in the range. cdbl.png range max r

### DAQmx Setup 4303 Calibration VI

Initializes an NI PXIe-4303 device with the specified mode, range, and excitation for calibration. Refer to the calibration procedure for your device for specific calibration instructions.

[IMAGE alt='icon' src='daqmx-setup-4303-calibration-vi.png']

#### Inputs/Outputs

| range min — range min specifies the minimum value in the range. range max — range max specifies the maximum value in the range. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4304-calibration-vi.html language=enus -->
## TOPIC 01981: DAQmx Setup 4304 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4304-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4304-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an NI PXIe-4304 device with the specified mode, range, and excitation for calibration. Refer to the calibration procedure for your device for specific calibration instructions. icon Inputs/Outputs cdbl.png range min range min specifies the minimum value in the range. cdbl.png range max r

### DAQmx Setup 4304 Calibration VI

Initializes an NI PXIe-4304 device with the specified mode, range, and excitation for calibration. Refer to the calibration procedure for your device for specific calibration instructions.

[IMAGE alt='icon' src='daqmx-setup-4304-calibration-vi.png']

#### Inputs/Outputs

| range min — range min specifies the minimum value in the range. range max — range max specifies the maximum value in the range. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4305-calibration-vi.html language=enus -->
## TOPIC 01982: DAQmx Setup 4305 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4305-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4305-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an NI PXIe-4305 device with the specified mode, range, and excitation for calibration. Refer to the calibration procedure for your device for specific calibration instructions. icon Inputs/Outputs cdbl.png range min range min specifies the minimum value in the range. cdbl.png range max r

### DAQmx Setup 4305 Calibration VI

Initializes an NI PXIe-4305 device with the specified mode, range, and excitation for calibration. Refer to the calibration procedure for your device for specific calibration instructions.

[IMAGE alt='icon' src='daqmx-setup-4305-calibration-vi.png']

#### Inputs/Outputs

| range min — range min specifies the minimum value in the range. range max — range max specifies the maximum value in the range. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4322-calibration-vi.html language=enus -->
## TOPIC 01983: DAQmx Setup 4322 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4322-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4322-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the specified value to the DAC on the specified physical channel(s) for an NI PXIe-4322. This device requires a sweep of values obtained from the calibration procedure. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the

### DAQmx Setup 4322 Calibration VI

Writes the specified value to the DAC on the specified physical channel(s) for an NI PXIe-4322. This device requires a sweep of values obtained from the calibration procedure.

[IMAGE alt='icon' src='daqmx-setup-4322-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. output type — output type specifies the type of measurement for the device. Voltage (10322) Voltage generation. Current (10134) Current generation. output value — output value specifies value to write to the device, in the units of output type. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Voltage (10322) | Voltage generation. |
| Current (10134) | Current generation. |

Parent topic:

DAQmx Setup SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4339-calibration-vi.html language=enus -->
## TOPIC 01984: DAQmx Setup 4339 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4339-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4339-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an NI PXIe-4339 device with the specified mode, range, and excitation for calibration. Refer to the calibration procedure for your device for specific calibration instructions. icon Inputs/Outputs cdbl.png range min range min specifies the minimum value in the range. cdbl.png range max r

### DAQmx Setup 4339 Calibration VI

Initializes an NI PXIe-4339 device with the specified mode, range, and excitation for calibration. Refer to the calibration procedure for your device for specific calibration instructions.

[IMAGE alt='icon' src='daqmx-setup-4339-calibration-vi.png']

#### Inputs/Outputs

| range min — range min specifies the minimum value in the range. range max — range max specifies the maximum value in the range. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. cal mode — cal mode specifies the calibration mode for the device. Voltage (10322) Voltage mode. Ratiometric (15908) Ratiometric mode. excitation voltage — excitation voltage specifies the excitation voltage setting to calibrate error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Voltage (10322) | Voltage mode. |
| Ratiometric (15908) | Ratiometric mode. |

Parent topic:

DAQmx Setup SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-433x-calibration-vi.html language=enus -->
## TOPIC 01985: DAQmx Setup 433x Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-433x-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-433x-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an NI PXIe-4330 or NI PXIe-4331 device with the specified excitation voltage value for calibration. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. cdaqmxscale.png physic

### DAQmx Setup 433x Calibration VI

Initializes an NI PXIe-4330 or NI PXIe-4331 device with the specified excitation voltage value for calibration.

[IMAGE alt='icon' src='daqmx-setup-433x-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. excitation voltage — excitation voltage specifies the excitation voltage setting to calibrate error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup SC Express Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4463-calibration-vi.html language=enus -->
## TOPIC 01986: DAQmx Setup 4463 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4463-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4463-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a specified voltage from the device. You must measure the voltage and pass that value into the DAQmx Adjust 4463 Calibration VI. icon Inputs/Outputs cdbl.png output voltage output voltage specifies, in Hz, the output voltage to generate. cu32.png calhandle in calhandle in is a reference to

### DAQmx Setup 4463 Calibration VI

Generates a specified voltage from the device. You must measure the voltage and pass that value into the DAQmx Adjust 4463 Calibration VI.

[IMAGE alt='icon' src='daqmx-setup-4463-calibration-vi.png']

#### Inputs/Outputs

| output voltage — output voltage specifies, in Hz, the output voltage to generate. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. terminal configuration — terminal configuration specifies the terminal configuration of the device. Differential (10106) Differential. Pseudodifferential (12529) Pseudodifferential. gain (dB) — gain (dB) specifies the gain setting to calibrate, in decibels. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Differential (10106) | Differential. |
| Pseudodifferential (12529) | Pseudodifferential. |

Parent topic:

DAQmx Setup DSA Calibration Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4480-calibration-vi.html language=enus -->
## TOPIC 01987: DAQmx Setup 4480 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4480-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-4480-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a PXIe-4480 device for calibrating the specified channel type. Refer to the calibration procedure for your device for specific calibration instructions. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created using the DAQmx Initi

### DAQmx Setup 4480 Calibration VI

Initializes a PXIe-4480 device for calibrating the specified channel type. Refer to the calibration procedure for your device for specific calibration instructions.

[IMAGE alt='icon' src='daqmx-setup-4480-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the physical channel(s) to calibrate. cal mode — cal mode specifies the calibration mode for the device. Voltage (10322) Voltage mode. Charge (16105) Charge mode. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Voltage (10322) | Voltage mode. |
| Charge (16105) | Charge mode. |

Parent topic:

DAQmx Setup DSA Calibration Polymorphic VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9218-calibration-vi.html language=enus -->
## TOPIC 01988: DAQmx Setup 9218 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9218-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9218-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets up external calibration for an NI 9218 device. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in the units of the measurement type specified by measType. The units for the range inputs should correspond to the measurement type. cdbl.png rangeMax rangeMa

### DAQmx Setup 9218 Calibration VI

Sets up external calibration for an NI 9218 device.

[IMAGE alt='icon' src='daqmx-setup-9218-calibration-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in the units of the measurement type specified by measType. The units for the range inputs should correspond to the measurement type. rangeMax — rangeMax specifies the maximum value in the range, in the units of the measurement type specified by measType. The units for the range inputs should correspond to the measurement type. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. measType — measType specifies the type of measurement for the device. Voltage (10322) Voltage. Current (10134) Current. Bridge (15908) Wheatstone bridge. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Voltage (10322) | Voltage. |
| Current (10134) | Current. |
| Bridge (15908) | Wheatstone bridge. |

Parent topic:

DAQmx Setup C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9219-calibration-vi.html language=enus -->
## TOPIC 01989: DAQmx Setup 9219 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9219-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9219-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets up external calibration for an NI 9219 device. icon Inputs/Outputs cdbl.png rangeMin rangeMin specifies the minimum value in the range, in the units of the measurement type specified by measType. If your measType is RTD, you must specify your minimum range in ohms. cdbl.png rangeMax rangeMax sp

### DAQmx Setup 9219 Calibration VI

Sets up external calibration for an NI 9219 device.

[IMAGE alt='icon' src='daqmx-setup-9219-calibration-vi.png']

#### Inputs/Outputs

| rangeMin — rangeMin specifies the minimum value in the range, in the units of the measurement type specified by measType. If your measType is RTD, you must specify your minimum range in ohms. rangeMax — rangeMax specifies the maximum value in the range, in the units of the measurement type specified by measType. If your measType is RTD, you must specify your maximum range in ohms. calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. measType — measType specifies the type of measurement for the device. Voltage (10322) Voltage. Current (10134) Current. Resistance (10278) Resistance. RTD (10301) RTD. Bridge (15908) Wheatstone bridge. bridgeConfig — bridgeConfig specifies the Wheatstone bridge configuration connected to the channel. Full Bridge (10182) Four active sensing elements in the bridge. Half Bridge (10187) Two active sensing elements in the bridge. No Bridge (10228) Sensor is not a Wheatstone bridge. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |  |
| --- | --- |
| Voltage (10322) | Voltage. |
| Current (10134) | Current. |
| Resistance (10278) | Resistance. |
| RTD (10301) | RTD. |
| Bridge (15908) | Wheatstone bridge. |
| Full Bridge (10182) | Four active sensing elements in the bridge. |
| Half Bridge (10187) | Two active sensing elements in the bridge. |
| No Bridge (10228) | Sensor is not a Wheatstone bridge. |

Parent topic:

DAQmx Setup C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9242-calibration-vi.html language=enus -->
## TOPIC 01990: DAQmx Setup 9242 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9242-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9242-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the specified value from the ADC on the specified physical channel. This module requires a sweep of adjustment points obtained from the DAQmx Get 9242 Calibration Adjustment Points VI. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you cre

### DAQmx Setup 9242 Calibration VI

Reads the specified value from the ADC on the specified physical channel. This module requires a sweep of adjustment points obtained from the DAQmx Get 9242 Calibration Adjustment Points VI.

[IMAGE alt='icon' src='daqmx-setup-9242-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. adjustment point — adjustment point is the adjustment point value to read from the ADC. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9244-calibration-vi.html language=enus -->
## TOPIC 01991: DAQmx Setup 9244 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9244-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9244-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the specified value from the ADC on the specified physical channel. This module requires a sweep of adjustment points obtained from the DAQmx Get 9244 Calibration Adjustment Points VI. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you cre

### DAQmx Setup 9244 Calibration VI

Reads the specified value from the ADC on the specified physical channel. This module requires a sweep of adjustment points obtained from the DAQmx Get 9244 Calibration Adjustment Points VI.

[IMAGE alt='icon' src='daqmx-setup-9244-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. adjustment point — adjustment point is the adjustment point value to read from the ADC. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9260-calibration-vi.html language=enus -->
## TOPIC 01992: DAQmx Setup 9260 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9260-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9260-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmx Get 9260 Calibration Adjustment Points VI. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you crea

### DAQmx Setup 9260 Calibration VI

Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmx Get 9260 Calibration Adjustment Points VI.

[IMAGE alt='icon' src='daqmx-setup-9260-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. DAC value — DAC value is the binary number to write to the DAC. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9262-calibration-vi.html language=enus -->
## TOPIC 01993: DAQmx Setup 9262 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9262-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9262-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmx Get 9262 Calibration Adjustment Points VI. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you crea

### DAQmx Setup 9262 Calibration VI

Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmx Get 9262 Calibration Adjustment Points VI.

[IMAGE alt='icon' src='daqmx-setup-9262-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. DAC value — DAC value is the binary number to write to the DAC. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9263-calibration-vi.html language=enus -->
## TOPIC 01994: DAQmx Setup 9263 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9263-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9263-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmx Get 9263 Calibration Adjustment Points VI. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you crea

### DAQmx Setup 9263 Calibration VI

Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmx Get 9263 Calibration Adjustment Points VI.

[IMAGE alt='icon' src='daqmx-setup-9263-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. DAC value — DAC value is the binary number to write to the DAC. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9264-calibration-vi.html language=enus -->
## TOPIC 01995: DAQmx Setup 9264 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9264-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9264-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmx Get 9264 Calibration Adjustment Points VI. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you crea

### DAQmx Setup 9264 Calibration VI

Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmx Get 9264 Calibration Adjustment Points VI.

[IMAGE alt='icon' src='daqmx-setup-9264-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. DAC value — DAC value is the binary number to write to the DAC. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9265-calibration-vi.html language=enus -->
## TOPIC 01996: DAQmx Setup 9265 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9265-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9265-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmx Get 9265 Calibration Adjustment Points VI. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you crea

### DAQmx Setup 9265 Calibration VI

Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmx Get 9265 Calibration Adjustment Points VI.

[IMAGE alt='icon' src='daqmx-setup-9265-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. DAC value — DAC value is the binary number to write to the DAC. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9266-calibration-vi.html language=enus -->
## TOPIC 01997: DAQmx Setup 9266 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9266-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9266-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of adjustment points obtained from the DAQmx Get 9266 Calibration Adjustment Points VI. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that y

### DAQmx Setup 9266 Calibration VI

Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of adjustment points obtained from the DAQmx Get 9266 Calibration Adjustment Points VI.

[IMAGE alt='icon' src='daqmx-setup-9266-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. DAC value — DAC value is the binary number to write to the DAC. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9269-calibration-vi.html language=enus -->
## TOPIC 01998: DAQmx Setup 9269 Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9269-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9269-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmx Get 9269 Calibration Adjustment Points VI. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you crea

### DAQmx Setup 9269 Calibration VI

Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values obtained from the DAQmx Get 9269 Calibration Adjustment Points VI.

[IMAGE alt='icon' src='daqmx-setup-9269-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. DAC value — DAC value is the binary number to write to the DAC. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9628-ao-calibration-vi.html language=enus -->
## TOPIC 01999: DAQmx Setup 9628 AO Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9628-ao-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9628-ao-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values from the DAQmx Get 9628:AO Calibration Adjustment Points VI. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created us

### DAQmx Setup 9628 AO Calibration VI

Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values from the DAQmx Get 9628:AO Calibration Adjustment Points VI.

[IMAGE alt='icon' src='daqmx-setup-9628-ao-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. DAC value — DAC value is the binary number to write to the DAC. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup C Series Calibration VI

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9629-ao-calibration-vi.html language=enus -->
## TOPIC 02000: DAQmx Setup 9629 AO Calibration VI

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9629-ao-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/vi-lib/daqmx/calibration/calibrationinfo-llb/daqmx-setup-9629-ao-calibration-vi.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values from the DAQmx Get 9629 AO Calibration Adjustment Points VI. icon Inputs/Outputs cu32.png calhandle in calhandle in is a reference to the calibration session that you created us

### DAQmx Setup 9629 AO Calibration VI

Writes the specified binary value to the DAC on the specified physical channel. This module requires a sweep of DAC values from the DAQmx Get 9629 AO Calibration Adjustment Points VI.

[IMAGE alt='icon' src='daqmx-setup-9629-ao-calibration-vi.png']

#### Inputs/Outputs

| calhandle in — calhandle in is a reference to the calibration session that you created using the DAQmx Initialize External Calibration VI. physical channels — physical channels specifies the name of the physical channel to use to create the virtual channel. The DAQmx physical channel constant lists all physical channels on devices and modules installed in the system. You also can wire a string that contains a physical channel to this input. You cannot specify more than one physical channel. DAC value — DAC value is the binary number to write to the DAC. error in — error in describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. If an error occurs while this VI or function runs, the VI or function runs normally and sets its own error status in error out. Use the Simple Error Handler or General Error Handler VIs to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. calhandle out — calhandle out is a reference to the calibration session. Wire this output to other external calibration VIs. error out — error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, error out describes the error status that this VI or function produces. Right-click the error out indicator on the front panel and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx Setup C Series Calibration VI
