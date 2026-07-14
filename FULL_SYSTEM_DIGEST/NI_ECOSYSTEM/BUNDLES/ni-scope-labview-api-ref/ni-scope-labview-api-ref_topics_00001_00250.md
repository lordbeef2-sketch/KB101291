# NI DOCUMENT BUNDLE: ni-scope-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-scope-labview-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=api-reference.html language=enus -->
## TOPIC 00001: NI-SCOPE LabVIEW API Reference

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `api-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/api-reference.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This API reference provides information about the programmatic elements available for this product. Looking for Something Else? For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse R

### NI-SCOPE LabVIEW API Reference

This API reference provides information about the programmatic elements available for this product.

#### Looking for Something Else?

For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse *Related Information*.

Related information:

- NI-SCOPE Driver Downloads
- NI-SCOPE Release Notes
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/dir-mnu.html language=enus -->
## TOPIC 00002: NI-SCOPE

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/dir-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE VIs to develop applications for your NI high-speed digitizer. The following tables show an overview of the VIs and subpalettes on the main NI-SCOPE palette. icon

### NI-SCOPE

Use the NI-SCOPE VIs to develop applications for your NI high-speed digitizer.

The following tables show an overview of the VIs and subpalettes on the main NI-SCOPE palette.

[IMAGE alt='icon' src='dir-mnu.png']

- [niScope Initialize VI](../../instr-lib/niscope/niscope-llb/niscope-initialize-vi.html) Performs the following initialization actions:
- [niScope Configure Vertical VI](../../instr-lib/niscope/niscope-llb/niscope-configure-vertical-vi.html) Configures the most commonly configured properties of the digitizer vertical subsystem, such as the range, offset, coupling, probe attenuation, and the channel name.
- [niScope Configure Horizontal Timing VI](../../instr-lib/niscope/niscope-llb/niscope-configure-horizontal-timing-vi.html) Configures the common properties of the horizontal subsystem for a single record or multirecord acquisition, such as minimum sample rate and acquisition size.
- [niScope Configure Trigger (poly) VI](../../instr-lib/niscope/niscope-llb/niscope-configure-trigger-poly-vi.html) Configures the digitizer for different types of triggering.
- [niScope Read (poly) VI](../../instr-lib/niscope/niscope-llb/niscope-read-poly-vi.html) Initiates an acquisition, waits for it to complete, and acquires data.
- [niScope Close VI](../../instr-lib/niscope/niscope-llb/niscope-close-vi.html) Performs the following actions:
- [niScope Initialize With Options VI](../../instr-lib/niscope/niscope-llb/niscope-initialize-with-options-vi.html) Performs the following initialization actions:
- [Configuration](../../instr-lib/niscope/niscope-configuration-mnu.html) Use the NI-SCOPE Configuration VIs to set up and transfer the parameters of your acquisition, or use Auto Setup to automatically configure device settings.
- [Timing](../../instr-lib/niscope/niscope-clocking-mnu.html) Use the NI-SCOPE Timing VIs to configure common timing properties for your digitizer.
- [Triggering](../../instr-lib/niscope/niscope-configurationtrigger-mnu.html) Use the NI-SCOPE Triggering VIs to configure the trigger properties.
- [Acquisition](../../instr-lib/niscope/niscope-lowlevelacq-mnu.html) Use the NI-SCOPE Acquisition VIs to control your data acquisition and to retrieve data from your device.
- [Calibration](../../instr-lib/niscope/niscope-calibration-mnu.html) Use the NI-SCOPE Calibration VIs to self-calibrate your digitizer and to access lower-level external calibration functions.
- [niScope Property Node VI](../../instr-lib/niscope/niscope-llb/niscope-property-node-vi.html) The niScope Property Node is used to set, get, or check properties.
- [Measurements](../../instr-lib/niscope/niscope-measurement-mnu.html) Use the NI-SCOPE Measurements VIs to perform waveform measurements, including scalar and array measurements.
- [Utility Functions](../../instr-lib/niscope/niscope-utility-mnu.html) Use the NI-SCOPE Utility VIs to perform various tasks such as resetting the digitizer and returning the revision numbers of the driver and the instrument firmware.

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/ni5110-ext-cal-api-mnu.html language=enus -->
## TOPIC 00003: 5110 Ext Cal

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/ni5110-ext-cal-api-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/ni5110-ext-cal-api-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE 5110 Ext Cal VIs to perform external calibration of the DC reference and compensated attenuator on the PXIe-5110. icon

### 5110 Ext Cal

Use the NI-SCOPE 5110 Ext Cal VIs to perform external calibration of the DC reference and compensated attenuator on the PXIe-5110.

[IMAGE alt='icon' src='ni5110-ext-cal-api-mnu.png']

- [Open Ext Cal Session VI](../../instr-lib/niscope/niscope-llb/open-ext-cal-session-vi.html) Opens an external calibration session for the specified device.
- [Close Ext Cal Session VI](../../instr-lib/niscope/niscope-llb/close-ext-cal-session-vi.html) Closes the external calibration session. You can choose to either commit or disregard the results of the calibration session.
- [Utilities](../../instr-lib/niscope/ni5110-ext-cal-utilities-mnu.html) External calibration utilities for the PXIe-5113.
- [DC Reference Cal Initialize VI](../../instr-lib/niscope/niscope-llb/dc-reference-cal-initialize-vi.html) Prepares the oscilloscope for adjusting the DC reference on the channel that you specify.
- [DC Reference Cal Configure VI](../../instr-lib/niscope/niscope-llb/dc-reference-cal-configure-vi.html) Configures the oscilloscope for the next DC reference calibration test point and waits for the oscilloscope to settle.
- [DC Reference Cal Adjust VI](../../instr-lib/niscope/niscope-llb/dc-reference-cal-adjust-vi.html) Measures the input voltage on the specified channel, compares it with the actual voltage generated, performs an adjustment, and computes the calibration coefficients.
- [Compensated Attenuator Cal Initialize VI](../../instr-lib/niscope/niscope-llb/compensated-attenuator-cal-initialize-vi.html) Prepares the oscilloscope for adjusting the compensated attenuator on the channel you specify.
- [Compensated Attenuator Cal Configure VI](../../instr-lib/niscope/niscope-llb/compensated-attenuator-cal-configure-vi.html) Configures the oscilloscope for the next compensated attenuator calibration test point and waits for the oscilloscope to settle.
- [Compensated Attenuator Cal Adjust VI](../../instr-lib/niscope/niscope-llb/compensated-attenuator-cal-adjust-vi.html) Acquires the square waveform on the specified channel, calculates flatness error, performs an adjustment, and computes the calibration coefficients.
- [Get Misc Info VI](../../instr-lib/niscope/niscope-llb/get-misc-info-vi.html) Returns the text information set by the Set Misc Info VI of this library.
- [Set Misc Info VI](../../instr-lib/niscope/niscope-llb/set-misc-info-vi.html) Stores custom text information that is stored until you close the current calibration session. You can choose to commit this information to the device when you close the calibration session.
- [Get Adjustment Date And Temperature VI](../../instr-lib/niscope/niscope-llb/get-adjustment-date-and-temperature-vi.html) Returns the date of the last successful external calibration and the onboard temperature, in degrees Celsius, of the device at the time of that calibration.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/ni5110-ext-cal-utilities-mnu.html language=enus -->
## TOPIC 00004: Utilities

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/ni5110-ext-cal-utilities-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/ni5110-ext-cal-utilities-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: External calibration utilities for the PXIe-5113. icon

### Utilities

External calibration utilities for the PXIe-5113.

[IMAGE alt='icon' src='ni5110-ext-cal-utilities-mnu.png']

- [Change External Cal Password VI](../../instr-lib/niscope/niscope-llb/change-external-cal-password-vi.html) Changes the password used to begin an external calibration session.
- [Get External Cal Due Date VI](../../instr-lib/niscope/niscope-llb/get-external-cal-due-date-vi.html) Returns the current external calibration due date of the device.
- [Set External Cal Due Date VI](../../instr-lib/niscope/niscope-llb/set-external-cal-due-date-vi.html) Sets the external calibration due date of the device.
- [Get External Cal Verification Date VI](../../instr-lib/niscope/niscope-llb/get-external-cal-verification-date-vi.html) Returns the most recent external calibration verification date of the device.
- [Set External Cal Verification Date VI](../../instr-lib/niscope/niscope-llb/set-external-cal-verification-date-vi.html) Sets the most recent external calibration verification date of the device.

Parent topic:

5110 Ext Cal

Parent topic:

5111 Ext Cal

Parent topic:

5113 Ext Cal

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/ni5111-ext-cal-api-mnu.html language=enus -->
## TOPIC 00005: 5111 Ext Cal

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/ni5111-ext-cal-api-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/ni5111-ext-cal-api-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE 5110 Ext Cal VIs to perform external calibration of the DC reference and compensated attenuator on the PXIe-5111. icon

### 5111 Ext Cal

Use the NI-SCOPE 5110 Ext Cal VIs to perform external calibration of the DC reference and compensated attenuator on the PXIe-5111.

[IMAGE alt='icon' src='ni5111-ext-cal-api-mnu.png']

- [Open Ext Cal Session VI](../../instr-lib/niscope/niscope-llb/open-ext-cal-session-vi.html) Opens an external calibration session for the specified device.
- [Close Ext Cal Session VI](../../instr-lib/niscope/niscope-llb/close-ext-cal-session-vi.html) Closes the external calibration session. You can choose to either commit or disregard the results of the calibration session.
- [Utilities](../../instr-lib/niscope/ni5110-ext-cal-utilities-mnu.html) External calibration utilities for the PXIe-5113.
- [DC Reference Cal Initialize VI](../../instr-lib/niscope/niscope-llb/dc-reference-cal-initialize-vi.html) Prepares the oscilloscope for adjusting the DC reference on the channel that you specify.
- [DC Reference Cal Configure VI](../../instr-lib/niscope/niscope-llb/dc-reference-cal-configure-vi.html) Configures the oscilloscope for the next DC reference calibration test point and waits for the oscilloscope to settle.
- [DC Reference Cal Adjust VI](../../instr-lib/niscope/niscope-llb/dc-reference-cal-adjust-vi.html) Measures the input voltage on the specified channel, compares it with the actual voltage generated, performs an adjustment, and computes the calibration coefficients.
- [Compensated Attenuator Cal Initialize VI](../../instr-lib/niscope/niscope-llb/compensated-attenuator-cal-initialize-vi.html) Prepares the oscilloscope for adjusting the compensated attenuator on the channel you specify.
- [Compensated Attenuator Cal Configure VI](../../instr-lib/niscope/niscope-llb/compensated-attenuator-cal-configure-vi.html) Configures the oscilloscope for the next compensated attenuator calibration test point and waits for the oscilloscope to settle.
- [Compensated Attenuator Cal Adjust VI](../../instr-lib/niscope/niscope-llb/compensated-attenuator-cal-adjust-vi.html) Acquires the square waveform on the specified channel, calculates flatness error, performs an adjustment, and computes the calibration coefficients.
- [Get Misc Info VI](../../instr-lib/niscope/niscope-llb/get-misc-info-vi.html) Returns the text information set by the Set Misc Info VI of this library.
- [Set Misc Info VI](../../instr-lib/niscope/niscope-llb/set-misc-info-vi.html) Stores custom text information that is stored until you close the current calibration session. You can choose to commit this information to the device when you close the calibration session.
- [Get Adjustment Date And Temperature VI](../../instr-lib/niscope/niscope-llb/get-adjustment-date-and-temperature-vi.html) Returns the date of the last successful external calibration and the onboard temperature, in degrees Celsius, of the device at the time of that calibration.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/ni5113-ext-cal-api-mnu.html language=enus -->
## TOPIC 00006: 5113 Ext Cal

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/ni5113-ext-cal-api-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/ni5113-ext-cal-api-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE 5110 Ext Cal VIs to perform external calibration of the DC reference and compensated attenuator on the PXIe-5113. icon

### 5113 Ext Cal

Use the NI-SCOPE 5110 Ext Cal VIs to perform external calibration of the DC reference and compensated attenuator on the PXIe-5113.

[IMAGE alt='icon' src='ni5113-ext-cal-api-mnu.png']

- [Open Ext Cal Session VI](../../instr-lib/niscope/niscope-llb/open-ext-cal-session-vi.html) Opens an external calibration session for the specified device.
- [Close Ext Cal Session VI](../../instr-lib/niscope/niscope-llb/close-ext-cal-session-vi.html) Closes the external calibration session. You can choose to either commit or disregard the results of the calibration session.
- [Utilities](../../instr-lib/niscope/ni5110-ext-cal-utilities-mnu.html) External calibration utilities for the PXIe-5113.
- [DC Reference Cal Initialize VI](../../instr-lib/niscope/niscope-llb/dc-reference-cal-initialize-vi.html) Prepares the oscilloscope for adjusting the DC reference on the channel that you specify.
- [DC Reference Cal Configure VI](../../instr-lib/niscope/niscope-llb/dc-reference-cal-configure-vi.html) Configures the oscilloscope for the next DC reference calibration test point and waits for the oscilloscope to settle.
- [DC Reference Cal Adjust VI](../../instr-lib/niscope/niscope-llb/dc-reference-cal-adjust-vi.html) Measures the input voltage on the specified channel, compares it with the actual voltage generated, performs an adjustment, and computes the calibration coefficients.
- [Compensated Attenuator Cal Initialize VI](../../instr-lib/niscope/niscope-llb/compensated-attenuator-cal-initialize-vi.html) Prepares the oscilloscope for adjusting the compensated attenuator on the channel you specify.
- [Compensated Attenuator Cal Configure VI](../../instr-lib/niscope/niscope-llb/compensated-attenuator-cal-configure-vi.html) Configures the oscilloscope for the next compensated attenuator calibration test point and waits for the oscilloscope to settle.
- [Compensated Attenuator Cal Adjust VI](../../instr-lib/niscope/niscope-llb/compensated-attenuator-cal-adjust-vi.html) Acquires the square waveform on the specified channel, calculates flatness error, performs an adjustment, and computes the calibration coefficients.
- [Get Misc Info VI](../../instr-lib/niscope/niscope-llb/get-misc-info-vi.html) Returns the text information set by the Set Misc Info VI of this library.
- [Set Misc Info VI](../../instr-lib/niscope/niscope-llb/set-misc-info-vi.html) Stores custom text information that is stored until you close the current calibration session. You can choose to commit this information to the device when you close the calibration session.
- [Get Adjustment Date And Temperature VI](../../instr-lib/niscope/niscope-llb/get-adjustment-date-and-temperature-vi.html) Returns the date of the last successful external calibration and the onboard temperature, in degrees Celsius, of the device at the time of that calibration.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-actual-mnu.html language=enus -->
## TOPIC 00007: Actual Values

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-actual-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-actual-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on the Actual Values palette to configure actual sample mode, record length, and sample rate. icon

### Actual Values

Use the VIs on the Actual Values palette to configure actual sample mode, record length, and sample rate.

[IMAGE alt='icon' src='niscope-actual-mnu.png']

- [niScope Actual Sample Mode VI](../../instr-lib/niscope/niscope-llb/niscope-actual-sample-mode-vi.html) Returns the sample mode the digitizer is currently using.
- [niScope Actual Record Length VI](../../instr-lib/niscope/niscope-llb/niscope-actual-record-length-vi.html) Returns the actual number of points the digitizer acquires for each channel. After configuring the digitizer for an acquisition, call this VI to determine the size of the waveforms that the digitizer acquires. The value is equal to or greater than the minimum number of points specified in any of the Configure Horizontal VIs.
- [niScope Sample Rate VI](../../instr-lib/niscope/niscope-llb/niscope-sample-rate-vi.html) Returns the effective sample rate, in samples per second, of the acquired waveform using the current configuration.

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-calibration-mnu.html language=enus -->
## TOPIC 00008: Calibration

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-calibration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-calibration-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE Calibration VIs to self-calibrate your digitizer and to access lower-level external calibration functions. icon

### Calibration

Use the NI-SCOPE Calibration VIs to self-calibrate your digitizer and to access
 lower-level external calibration functions.

[IMAGE alt='icon' src='niscope-calibration-mnu.png']

- [niScope Cal Self Calibrate VI](../../instr-lib/niscope/niscope-llb/niscope-cal-self-calibrate-vi.html) Self-calibrates most NI digitizers, including all SMC-based devices.
- [External Calibration](../../instr-lib/niscope/niscope-extcalibration-mnu.html) Use the NI-SCOPE External Calibration VIs to externally calibrate your digitizer. Some of these functions are device-specific; refer to the manual calibration procedure for your device for more information.
- [5110 Ext Cal](../../instr-lib/niscope/ni5110-ext-cal-api-mnu.html) Use the NI-SCOPE 5110 Ext Cal VIs to perform external calibration of the DC reference and compensated attenuator on the PXIe-5110.
- [5111 Ext Cal](../../instr-lib/niscope/ni5111-ext-cal-api-mnu.html) Use the NI-SCOPE 5110 Ext Cal VIs to perform external calibration of the DC reference and compensated attenuator on the PXIe-5111.
- [5113 Ext Cal](../../instr-lib/niscope/ni5113-ext-cal-api-mnu.html) Use the NI-SCOPE 5110 Ext Cal VIs to perform external calibration of the DC reference and compensated attenuator on the PXIe-5113.

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-clocking-mnu.html language=enus -->
## TOPIC 00009: Timing

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-clocking-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-clocking-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE Timing VIs to configure common timing properties for your digitizer. icon

### Timing

Use the NI-SCOPE Timing VIs to configure common timing properties for your digitizer.

[IMAGE alt='icon' src='niscope-clocking-mnu.png']

- [niScope Configure Clock VI](../../instr-lib/niscope/niscope-llb/niscope-configure-clock-vi.html) Configures the properties for synchronizing the digitizer to an external clock or sending the digitizer's clock output to be used as a synchronizing clock for other devices.
- [niScope Export Signal VI](../../instr-lib/niscope/niscope-llb/niscope-export-signal-vi.html) Configures the digitizer to generate a signal that other devices can detect when configured for digital triggering or sharing clocks. The signal parameter specifies what condition causes the digitizer to generate the signal. The output terminal parameter specifies where to send the signal on the hardware (such as a PFI connector or RTSI line).
- [niScope Adjust Sample Clock Relative Delay VI](../../instr-lib/niscope/niscope-llb/niscope-adjust-sample-clock-relative-delay-vi.html) Applies offset, in seconds, to the sample clock relative to the reference clock when using the onboard clock.
- [Actual Values](../../instr-lib/niscope/niscope-actual-mnu.html) Use the VIs on the Actual Values palette to configure actual sample mode, record length, and sample rate.
- [niScope Configure Horizontal Timing VI](../../instr-lib/niscope/niscope-llb/niscope-configure-horizontal-timing-vi.html) Configures the common properties of the horizontal subsystem for a single record or multirecord acquisition, such as minimum sample rate and acquisition size.

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-configuration-mnu.html language=enus -->
## TOPIC 00010: Configuration

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-configuration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-configuration-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE Configuration VIs to set up and transfer the parameters of your acquisition, or use Auto Setup to automatically configure device settings. icon

### Configuration

Use the NI-SCOPE Configuration VIs to set up and transfer the parameters of your acquisition, or use Auto Setup to automatically configure device settings.

[IMAGE alt='icon' src='niscope-configuration-mnu.png']

- [niScope Auto Setup VI](../../instr-lib/niscope/niscope-llb/niscope-auto-setup-vi.html) Automatically configures the digitizer.
- [niScope Import Attribute Configuration (Poly) VI](../../instr-lib/niscope/niscope-llb/niscope-import-attribute-configuration-poly-vi.html) Imports an attribute configuration to the session from either a file or a buffer.
- [Configure Onboard Signal Processing](../../instr-lib/niscope/niscope-configurationosp-mnu.html) Use the VIs on this palette to configure Onboard Signal Processing (OSP) for devices that support OSP.
- [niScope Configure Acquisition VI](../../instr-lib/niscope/niscope-llb/niscope-configure-acquisition-vi.html) Configures how the oscilloscope acquires data and fills the waveform record.
- [niScope Configure Chan Characteristics VI](../../instr-lib/niscope/niscope-llb/niscope-configure-chan-characteristics-vi.html) Configures the properties that control the electrical characteristics of the channel. These properties are the input impedance and the bandwidth.
- [niScope Export Attribute Configuration (Poly) VI](../../instr-lib/niscope/niscope-llb/niscope-export-attribute-configuration-poly-vi.html) Exports the attribute configuration of a session to either a file or a buffer.
- [niScope Configure Vertical VI](../../instr-lib/niscope/niscope-llb/niscope-configure-vertical-vi.html) Configures the most commonly configured properties of the digitizer vertical subsystem, such as the range, offset, coupling, probe attenuation, and the channel name.

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-configurationosp-mnu.html language=enus -->
## TOPIC 00011: Configure Onboard Signal Processing

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-configurationosp-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-configurationosp-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure Onboard Signal Processing (OSP) for devices that support OSP. icon

### Configure Onboard Signal Processing

Use the VIs on this palette to configure Onboard Signal Processing (OSP) for devices that support OSP.

[IMAGE alt='icon' src='niscope-configurationosp-mnu.png']

- [niScope Configure Equalization Filter Coefficients VI](../../instr-lib/niscope/niscope-llb/niscope-configure-equalization-filter-coefficients-vi.html) Configures the custom coefficients for the equalization FIR filter on the device. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and -1.
- [niScope Get Frequency Response VI](../../instr-lib/niscope/niscope-llb/niscope-get-frequency-response-vi.html) Gets the frequency response of the digitizer for the current configurations of the channel attributes. This VI can be used only with high-speed digitizers that support onboard signal processing (OSP).
- [niScope Get Equalization Filter Coefficients VI](../../instr-lib/niscope/niscope-llb/niscope-get-equalization-filter-coefficients-vi.html) Retrieves the custom coefficients for the equalization FIR filter on the device.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-configurationtrigger-mnu.html language=enus -->
## TOPIC 00012: Triggering

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-configurationtrigger-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-configurationtrigger-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE Triggering VIs to configure the trigger properties. icon

### Triggering

Use the NI-SCOPE Triggering VIs to configure the trigger properties.

[IMAGE alt='icon' src='niscope-configurationtrigger-mnu.png']

- [niScope Send Software Trigger Edge VI](../../instr-lib/niscope/niscope-llb/niscope-send-software-trigger-edge-vi.html) Sends the selected trigger to the digitizer. If you called niScope Configure Trigger Software, call this VI when you want the reference trigger to occur. You can also call this VI to override a misused edge, digital, or hysteresis reference trigger. If you have configured an Acquisition Arm Source, an Arm Reference Trigger Source, or an Advance Trigger Source, call this VI when you want to send the corresponding trigger to the digitizer.
- [niScope Configure Trigger (poly) VI](../../instr-lib/niscope/niscope-llb/niscope-configure-trigger-poly-vi.html) Configures the digitizer for different types of triggering.
- [niScope Export Signal VI](../../instr-lib/niscope/niscope-llb/niscope-export-signal-vi.html) Configures the digitizer to generate a signal that other devices can detect when configured for digital triggering or sharing clocks. The signal parameter specifies what condition causes the digitizer to generate the signal. The output terminal parameter specifies where to send the signal on the hardware (such as a PFI connector or RTSI line).

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-extcalibration-mnu.html language=enus -->
## TOPIC 00013: External Calibration

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-extcalibration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-extcalibration-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE External Calibration VIs to externally calibrate your digitizer. Some of these functions are device-specific; refer to the manual calibration procedure for your device for more information. icon

### External Calibration

Use the NI-SCOPE External Calibration VIs to externally calibrate your digitizer. Some of these functions are device-specific; refer to the manual calibration procedure for your device for more information.

[IMAGE alt='icon' src='niscope-extcalibration-mnu.png']

- [niScope Cal Start VI](../../instr-lib/niscope/niscope-llb/niscope-cal-start-vi.html) Opens an external calibration session and produces a calibration session handle that is required by the external calibration VIs.
- [niScope Cal End VI](../../instr-lib/niscope/niscope-llb/niscope-cal-end-vi.html) Closes an external calibration session. You must call this VI each time you call niScope Cal Start , even if an error occurs during calibration.
- [niScope Cal Change Password VI](../../instr-lib/niscope/niscope-llb/niscope-cal-change-password-vi.html) Verifies the old password against the one stored in the EEPROM.
- [niScope Cal Store Misc Info VI](../../instr-lib/niscope/niscope-llb/niscope-cal-store-misc-info-vi.html) Allows you to store miscellaneous information in the EEPROM. For example, you can store an operator ID for the person or company performing a calibration. The information is stored immediately.
- [niScope Cal Fetch Date VI](../../instr-lib/niscope/niscope-llb/niscope-cal-fetch-date-vi.html) Returns the last self-calibration, external calibration, or manufacturer calibration date.
- [niScope Cal Fetch Count VI](../../instr-lib/niscope/niscope-llb/niscope-cal-fetch-count-vi.html) Returns the number of times the digitizer has been calibrated.
- [niScope Cal Fetch Temperature VI](../../instr-lib/niscope/niscope-llb/niscope-cal-fetch-temperature-vi.html) For SMC-based digitizers, this VI returns the onboard temperature of the digitizer at the time of the last self-calibration or external calibration, in degrees Celsius.
- [niScope Cal Fetch Misc Info VI](../../instr-lib/niscope/niscope-llb/niscope-cal-fetch-misc-info-vi.html) Returns the miscellaneous information you can store during an external calibration using niScope Cal Store Misc Info .
- [niScope Cal Adjust Range VI](../../instr-lib/niscope/niscope-llb/niscope-cal-adjust-range-vi.html) This VI externally calibrates the vertical range for the specified channel and vertical range setting.
- [niScope Cal Adjust Compensation Attenuator VI](../../instr-lib/niscope/niscope-llb/niscope-cal-adjust-compensation-attenuator-vi.html) This VI externally calibrates the compensation attenuator.
- [niScope Cal Adjust Offset Range VI](../../instr-lib/niscope/niscope-llb/niscope-cal-adjust-offset-range-vi.html) This VI externally calibrates the vertical offset.
- [niScope Cal Adjust VCXO VI](../../instr-lib/niscope/niscope-llb/niscope-cal-adjust-vcxo-vi.html) For SMC-based devices, this VI calibrates the sample rate of the digitizer.
- [niScope Cal Adjust DCM VI](../../instr-lib/niscope/niscope-llb/niscope-cal-adjust-dcm-vi.html) For PXIe/PXI/PCI-5105 digitizers, this VI calibrates the external clock digital clock managers (DCMs). DCM calibration ensures that data can be sampled at the correct time in the clock period.
- [niScope Cal Adjust Frequency Response VI](../../instr-lib/niscope/niscope-llb/niscope-cal-adjust-frequency-response-vi.html) For the PXIe-5622, calibrates the frequency response of the device. The VI is called multiple times, one for each frequency point in the sweep. The user must supply the stimulus frequency in hertz and stimulus amplitude in volts of the input signal.
- [niScope Cal Adjust Accessory Gain And Offset VI](../../instr-lib/niscope/niscope-llb/niscope-cal-adjust-accessory-gain-and-offset-vi.html) For the PXI-5900 differential amplifier, this VI calibrates the gain and offset.
- [niScope Cal Set Accessory Source VI](../../instr-lib/niscope/niscope-llb/niscope-cal-set-accessory-source-vi.html) For the PXI-5900 differential amplifier, this VI connects the specified channel to the calibration source and sets the calibration source to +/-10 V or to GND.
- [niScope Cal Measure RIS Distribution VI](../../instr-lib/niscope/niscope-llb/niscope-cal-measure-ris-distribution-vi.html) Calls niScope Read Waveform 2,000 times to take an acquisition from the specified channel and retrieve the initial X value, which includes the time-to-digital conversion.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/change-external-cal-password-vi.html language=enus -->
## TOPIC 00014: Change External Cal Password VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/change-external-cal-password-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/change-external-cal-password-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the password used to begin an external calibration session. Supported Devices: PXIe-5110 PXIe-5111 PXIe-5113 icon Inputs/Outputs civrn.png resource name in resource name in identifies the device. cstr.png external cal password external cal password is the calibration password for the device.

### Change External Cal Password VI

Changes the password used to begin an external calibration session.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='change-external-cal-password-vi.png']

#### Inputs/Outputs

| resource name in — resource name in identifies the device. external cal password — external cal password is the calibration password for the device. This password is required to perform external calibration, set the calibration due date, and set the date and time of verification. The default password is NI. new external cal password — new external cal password is the new password to store in the EEPROM of the device. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. resource name out — resource name out passes the device name to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/close-ext-cal-session-vi.html language=enus -->
## TOPIC 00015: Close Ext Cal Session VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/close-ext-cal-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/close-ext-cal-session-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the external calibration session. You can choose to either commit or disregard the results of the calibration session. Supported Devices: PXIe-5110 PXIe-5111 PXIe-5113 icon Inputs/Outputs cnclst.png external cal session external cal session is the external calibration session to close. cu32.p

### Close Ext Cal Session VI

Closes the external calibration session. You can choose to either commit or disregard the results of the calibration session.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='close-ext-cal-session-vi.png']

#### Inputs/Outputs

| external cal session — external cal session is the external calibration session to close. session — action — action specifies the action to take if the external adjustment procedure completed without any errors or if the errors were corrected and the adjustment step was rerun using the same external calibration session. Cancel (0) Disregard the new calibration constants without changing any of the calibration data stored in the nonvolatile memory of the oscilloscope. Commit (1) Store the new calibration constants, adjustment time, adjustment date, and adjustment temperature in the nonvolatile memory of the oscilloscope. Default Value: Cancel error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| session — |  |
| Cancel (0) | Disregard the new calibration constants without changing any of the calibration data stored in the nonvolatile memory of the oscilloscope. |
| Commit (1) | Store the new calibration constants, adjustment time, adjustment date, and adjustment temperature in the nonvolatile memory of the oscilloscope. |

Parent topic:

5110 Ext Cal

Parent topic:

5111 Ext Cal

Parent topic:

5113 Ext Cal

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/compensated-attenuator-cal-adjust-vi.html language=enus -->
## TOPIC 00016: Compensated Attenuator Cal Adjust VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/compensated-attenuator-cal-adjust-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/compensated-attenuator-cal-adjust-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquires the square waveform on the specified channel, calculates flatness error, performs an adjustment, and computes the calibration coefficients. Refer to the calibration procedure for the oscilloscope you are calibrating for detailed instructions on the appropriate use of this VI. Supported Devi

### Compensated Attenuator Cal Adjust VI

Acquires the square waveform on the specified channel, calculates flatness error, performs an adjustment, and computes the calibration coefficients.

Refer to the calibration procedure for the oscilloscope you are calibrating for detailed instructions on the appropriate use of this VI.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='compensated-attenuator-cal-adjust-vi.png']

#### Inputs/Outputs

| external cal session in — external cal session in identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. session — actual frequency generated (Hz) — actual frequency generated (Hz) specifies the frequency of the square waveform applied to the channel under adjustment. Note This frequency can vary by as much as ±1% from the requested frequency as defined by the frequency to generate parameter of Compensated Attenuator Cal ConfigureCompensated Attenuator Cal Configure. If the variation exceeds ±1%, NI‑SCOPE generates as error. actual amplitude generated (Vpk-pk) — actual amplitude generated (Vpk-pk) specifies the amplitude of the square waveform applied to the channel under adjustment. Note This frequency can vary by as much as ±1% from the requested frequency as defined by the amplitude to generate parameter of Compensated Attenuator Cal ConfigureCompensated Attenuator Cal Configure. If the variation exceeds ±1%, NI‑SCOPE generates as error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. external cal session out — external cal session out passes a reference to your session to the next VI. session — compensated attenuator cal complete — compensated attenuator cal complete indicates whether the compensated attenuator calibration is complete for the specified channel and the specified impedance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session — |
| session — |

Parent topic:

5110 Ext Cal

Parent topic:

5111 Ext Cal

Parent topic:

5113 Ext Cal

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/compensated-attenuator-cal-configure-vi.html language=enus -->
## TOPIC 00017: Compensated Attenuator Cal Configure VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/compensated-attenuator-cal-configure-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/compensated-attenuator-cal-configure-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the oscilloscope for the next compensated attenuator calibration test point and waits for the oscilloscope to settle. Refer to the calibration procedure for the oscilloscope you are calibrating for detailed instructions on the appropriate use of this VI. Supported Devices: PXIe-5110 PXIe-

### Compensated Attenuator Cal Configure VI

Configures the oscilloscope for the next compensated attenuator calibration test point and waits for the oscilloscope to settle.

Refer to the calibration procedure for the oscilloscope you are calibrating for detailed instructions on the appropriate use of this VI.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='compensated-attenuator-cal-configure-vi.png']

#### Inputs/Outputs

| external cal session in — external cal session in identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. session — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. external cal session out — external cal session out passes a reference to your session to the next VI. session — frequency to generate (Hz) — frequency to generate (Hz) specifies the frequency of the square waveform to generate for the current test point. amplitude to generate (Vpk-pk) — amplitude to generate (Vpk-pk) specifies the amplitude of the square waveform to generate for the current test point. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session — |
| session — |

Parent topic:

5110 Ext Cal

Parent topic:

5111 Ext Cal

Parent topic:

5113 Ext Cal

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/compensated-attenuator-cal-initialize-vi.html language=enus -->
## TOPIC 00018: Compensated Attenuator Cal Initialize VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/compensated-attenuator-cal-initialize-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/compensated-attenuator-cal-initialize-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Prepares the oscilloscope for adjusting the compensated attenuator on the channel you specify. Refer to the calibration procedure for the oscilloscope you are calibrating for detailed instructions on the appropriate use of this VI. Supported Devices: PXIe-5110 PXIe-5111 PXIe-5113 icon Inputs/Outputs

### Compensated Attenuator Cal Initialize VI

Prepares the oscilloscope for adjusting the compensated attenuator on the channel you specify.

Refer to the calibration procedure for the oscilloscope you are calibrating for detailed instructions on the appropriate use of this VI.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='compensated-attenuator-cal-initialize-vi.png']

#### Inputs/Outputs

| external cal session in — external cal session in identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. session — channel — channel specifies the input channel on which to perform the compensated attenuator adjustment. input impedance — input impedance specifies the input impedance to apply for the compensated attenuator adjustment. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. external cal session out — external cal session out passes a reference to your session to the next VI. session — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session — |
| session — |

Parent topic:

5110 Ext Cal

Parent topic:

5111 Ext Cal

Parent topic:

5113 Ext Cal

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/dc-reference-cal-adjust-vi.html language=enus -->
## TOPIC 00019: DC Reference Cal Adjust VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/dc-reference-cal-adjust-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/dc-reference-cal-adjust-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measures the input voltage on the specified channel, compares it with the actual voltage generated, performs an adjustment, and computes the calibration coefficients. Refer to the calibration procedure for the oscilloscope you are calibrating for detailed instructions on the appropriate use of this

### DC Reference Cal Adjust VI

Measures the input voltage on the specified channel, compares it with the actual voltage generated, performs an adjustment, and computes the calibration coefficients.

Refer to the calibration procedure for the oscilloscope you are calibrating for detailed instructions on the appropriate use of this VI.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='dc-reference-cal-adjust-vi.png']

#### Inputs/Outputs

| external cal session in — external cal session in identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. session — actual voltage generated (V) — actual voltage generated (V) specifies the voltage applied to the channel under adjustment. Note This voltage can vary by as much as ±5% from the requested voltage as defined by the voltage to generate parameter of DC Reference Cal ConfigureDC Reference Cal Configure. If the variation exceeds ±5%, NI‑SCOPE generates as error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. external cal session out — external cal session out passes a reference to your session to the next VI. session — dc reference cal complete — dc reference cal complete indicates whether the DC reference calibration is complete for the specified channel and the specified impedance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session — |
| session — |

Parent topic:

5110 Ext Cal

Parent topic:

5111 Ext Cal

Parent topic:

5113 Ext Cal

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/dc-reference-cal-configure-vi.html language=enus -->
## TOPIC 00020: DC Reference Cal Configure VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/dc-reference-cal-configure-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/dc-reference-cal-configure-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the oscilloscope for the next DC reference calibration test point and waits for the oscilloscope to settle. Refer to the calibration procedure for the oscilloscope you are calibrating for detailed instructions on the appropriate use of this VI. Supported Devices: PXIe-5110 PXIe-5111 PXIe-

### DC Reference Cal Configure VI

Configures the oscilloscope for the next DC reference calibration test point and waits for the oscilloscope to settle.

Refer to the calibration procedure for the oscilloscope you are calibrating for detailed instructions on the appropriate use of this VI.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='dc-reference-cal-configure-vi.png']

#### Inputs/Outputs

| external cal session in — external cal session in identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. session — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. external cal session out — external cal session out passes a reference to your session to the next VI. session — voltage to generate (V) — voltage to generate (V) specifies the DC voltage to generate for the current test point. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session — |
| session — |

Parent topic:

5110 Ext Cal

Parent topic:

5111 Ext Cal

Parent topic:

5113 Ext Cal

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/dc-reference-cal-initialize-vi.html language=enus -->
## TOPIC 00021: DC Reference Cal Initialize VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/dc-reference-cal-initialize-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/dc-reference-cal-initialize-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Prepares the oscilloscope for adjusting the DC reference on the channel that you specify. Refer to the calibration procedure for the oscilloscope you are calibrating for detailed instructions on the appropriate use of this VI. Supported Devices: PXIe-5110 PXIe-5111 PXIe-5113 icon Inputs/Outputs cncl

### DC Reference Cal Initialize VI

Prepares the oscilloscope for adjusting the DC reference on the channel that you specify.

Refer to the calibration procedure for the oscilloscope you are calibrating for detailed instructions on the appropriate use of this VI.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='dc-reference-cal-initialize-vi.png']

#### Inputs/Outputs

| external cal session in — external cal session in identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. session — channel — channel specifies the input channel on which to perform the DC reference adjustment. input impedance — input impedance specifies the input impedance to apply for the DC reference adjustment. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. external cal session out — external cal session out passes a reference to your session to the next VI. session — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session — |
| session — |

Parent topic:

5110 Ext Cal

Parent topic:

5111 Ext Cal

Parent topic:

5113 Ext Cal

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/get-adjustment-date-and-temperature-vi.html language=enus -->
## TOPIC 00022: Get Adjustment Date And Temperature VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/get-adjustment-date-and-temperature-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/get-adjustment-date-and-temperature-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date of the last successful external calibration and the onboard temperature, in degrees Celsius, of the device at the time of that calibration. Supported Devices: PXIe-5110 PXIe-5111 PXIe-5113 icon Inputs/Outputs cnclst.png external cal session in external cal session in identifies your

### Get Adjustment Date And Temperature VI

Returns the date of the last successful external calibration and the onboard temperature, in degrees Celsius, of the device at the time of that calibration.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='get-adjustment-date-and-temperature-vi.png']

#### Inputs/Outputs

| external cal session in — external cal session in identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. session — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. external cal session out — external cal session out passes a reference to your session to the next VI. session — adjustment date — adjustment date returns the date and time of the last successful external calibration. adjustment temperature (°C) — adjustment temperature (°C) returns the temperature, in degrees Celsius, of the last successful external calibration. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session — |
| session — |

Parent topic:

5110 Ext Cal

Parent topic:

5111 Ext Cal

Parent topic:

5113 Ext Cal

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/get-external-cal-due-date-vi.html language=enus -->
## TOPIC 00023: Get External Cal Due Date VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/get-external-cal-due-date-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/get-external-cal-due-date-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current external calibration due date of the device. Supported Devices: PXIe-5110 PXIe-5111 PXIe-5113 icon Inputs/Outputs civrn.png resource name in resource name in identifies the device. cerrcodeclst.png error in error in describes error conditions that occur before this node runs. Thi

### Get External Cal Due Date VI

Returns the current external calibration due date of the device.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='get-external-cal-due-date-vi.png']

#### Inputs/Outputs

| resource name in — resource name in identifies the device. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. resource name out — resource name out passes the device name to the next VI. external cal due date — external cal due date returns the date and time of the external calibration due date. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/get-external-cal-verification-date-vi.html language=enus -->
## TOPIC 00024: Get External Cal Verification Date VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/get-external-cal-verification-date-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/get-external-cal-verification-date-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the most recent external calibration verification date of the device. Supported Devices: PXIe-5110 PXIe-5111 PXIe-5113 icon Inputs/Outputs civrn.png resource name in resource name in identifies the device. cerrcodeclst.png error in error in describes error conditions that occur before this n

### Get External Cal Verification Date VI

Returns the most recent external calibration verification date of the device.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='get-external-cal-verification-date-vi.png']

#### Inputs/Outputs

| resource name in — resource name in identifies the device. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. resource name out — resource name out passes the device name to the next VI. external cal verification date — external cal verification date returns the date and time of the most recent successful external verification of the device. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/get-misc-info-vi.html language=enus -->
## TOPIC 00025: Get Misc Info VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/get-misc-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/get-misc-info-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the text information set by the Set Misc Info VI of this library. If you have not yet run the Set Misc Info VI during the calibration session, this VI will return the miscellaneous information that was last committed to the device. Supported Devices: PXIe-5110 PXIe-5111 PXIe-5113 icon Inputs

### Get Misc Info VI

Returns the text information set by the [Set Misc Info](/csh?topicname=set-misc-info-vi.html) VI of this library.

If you have not yet run the [Set Misc Info](set-misc-info-vi.html) VI during the calibration session, this VI will return the **miscellaneous information** that was last committed to the device.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='get-misc-info-vi.png']

#### Inputs/Outputs

| external cal session in — external cal session in identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. session — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. external cal session out — external cal session out passes a reference to your session to the next VI. session — miscellaneous information — miscellaneous information returns the text information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session — |
| session — |

Parent topic:

5110 Ext Cal

Parent topic:

5111 Ext Cal

Parent topic:

5113 Ext Cal

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-abort-vi.html language=enus -->
## TOPIC 00026: niScope Abort VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-abort-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-abort-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts an acquisition without changing the settings on the digitizer. Use this VI if the digitizer times out waiting for a trigger. Related topics NI-SCOPE Programming Flow icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png

### niScope Abort VI

Aborts an acquisition without changing the settings on the digitizer. Use this VI if the 
 digitizer times out waiting for a trigger.

**Related topics**

- NI-SCOPE Programming Flow

[IMAGE alt='icon' src='niscope-abort-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Acquisition

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-acquisition-status-vi.html language=enus -->
## TOPIC 00027: niScope Acquisition Status VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-acquisition-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-acquisition-status-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns status information indicating whether an acquisition is in progress, complete, or unknown to the acquisition status output parameter. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in error in describes err

### niScope Acquisition Status VI

Returns status information indicating whether an acquisition is in progress, complete,
 or unknown to the **acquisition status** output parameter.

[IMAGE alt='icon' src='niscope-acquisition-status-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. acquisition status — acquisition status returns whether the acquisition is in progress, complete, or unknown. Defined Values Acquisition in progress (0) Acquisition complete (1) Status unknown (-1) error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Acquisition

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-actual-meas-wfm-size-vi.html language=enus -->
## TOPIC 00028: niScope Actual Meas Wfm Size VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-actual-meas-wfm-size-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-actual-meas-wfm-size-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total available size of an array measurement acquisition in samples. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. ci32.png arrayMeasFunction arrayMeasFunction is the measurement to perform. Refer to the list of NI-SCOPE Arr

### niScope Actual Meas Wfm Size VI

Returns the total available size of an array measurement acquisition in samples.

[IMAGE alt='icon' src='niscope-actual-meas-wfm-size-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. arrayMeasFunction — arrayMeasFunction is the measurement to perform. Refer to the list of NI-SCOPE Array Measurements for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. meas wfm size — meas wfm size returns the size of the resulting analysis waveform in samples. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-actual-num-wfms-vi.html language=enus -->
## TOPIC 00029: niScope Actual Num Wfms VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-actual-num-wfms-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-actual-num-wfms-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allows you to declare appropriately sized waveforms. NI-SCOPE handles the channel list parsing for you. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png channels channels specifies the channel(s) from which to acquire data. For mo

### niScope Actual Num Wfms VI

Allows you to declare appropriately sized waveforms. NI-SCOPE handles the channel list parsing for you.

[IMAGE alt='icon' src='niscope-actual-num-wfms-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. actual num wfms — actual num wfms returns the number of records times the number of channels; if the acquisition Type parameter of the niScope Configure Acquisition VI is set to DDC, this value is multiplied by two. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-actual-record-length-vi.html language=enus -->
## TOPIC 00030: niScope Actual Record Length VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-actual-record-length-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-actual-record-length-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the actual number of points the digitizer acquires for each channel. After configuring the digitizer for an acquisition, call this VI to determine the size of the waveforms that the digitizer acquires. The value is equal to or greater than the minimum number of points specified in any of the

### niScope Actual Record Length VI

Returns the actual number of points the digitizer acquires for each channel. After configuring the digitizer for an acquisition, call this VI to determine the size of the waveforms that the digitizer acquires. The value is equal to or greater than the minimum number of points specified in any of the Configure Horizontal VIs.

Use the record length returned by this VI as the input to the **numSamples**
 parameter of the Read and Fetch VIs.

**Related topics**

- Record Length
- Coercions of Horizontal Parameters
- Making Multiple Record Acquisitions
- Acquiring Data Continuously

[IMAGE alt='icon' src='niscope-actual-record-length-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. actual record length — actual record length returns the actual number of points the digitizer acquires for each channel. NI-SCOPE returns the value held in the Horizontal Actual Record Length property; refer to Coercions of Horizontal Parameters for more information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Actual Values

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-actual-sample-mode-vi.html language=enus -->
## TOPIC 00031: niScope Actual Sample Mode VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-actual-sample-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-actual-sample-mode-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sample mode the digitizer is currently using. Related topics: Sampling Methods icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in error in describes error conditions that occur before this node runs. Thi

### niScope Actual Sample Mode VI

Returns the sample mode the digitizer is currently using.

**Related topics:**

- Sampling Methods

[IMAGE alt='icon' src='niscope-actual-sample-mode-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. sample mode — sample mode returns the sample mode the digitizer is currently using. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Actual Values

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-add-waveform-processing-vi.html language=enus -->
## TOPIC 00032: niScope Add Waveform Processing VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-add-waveform-processing-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-add-waveform-processing-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds one measurement to the list of processing steps that are completed before the measurement. The processing is added on a per channel basis, and the processing measurements are completed in the same order they are registered. All waveform measurements (for example, adding channels or applying a B

### niScope Add Waveform Processing VI

Adds one measurement to the list of processing steps that are completed before the measurement. The processing is added on a per channel basis, and the processing measurements are completed in the same order they are registered. All waveform measurements (for example, adding channels or applying a Bessel filter) are cached at the time of registering the processing, and this set of measurements is used during the processing step. The processing measurements are streamed, so the result of the first processing step is used as the input for the next step. The processing happens before any other measurements.

For example, you can use a property node to set the NI-SCOPE 
 property filter type to lowpass, and then register a Bessel Filter as a processing step using this
 VI. Then you can set the filter type to bandpass and register a Chebyshev filter. In a loop, 
 call [niScope Read Measurement](niscope-read-measurement-vi.html) with the scalar measurement function set to Voltage RMS. 
 This process would repeatedly fetch a new waveform from the digitizer, perform the lowpass filter, 
 perform the bandpass filter, and then compute the voltage RMS on the filtered waveform.

Refer to [Array Measurements](/csh?context=niscope_digitizers_array_measurements_refs) for more information about the available measurements.

**Related topics:**

- Array Measurements in NI-SCOPE
- Scalar Measurements in NI-SCOPE

[IMAGE alt='icon' src='niscope-add-waveform-processing-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. array measurement — array measurement is the array measurement to add as a processing step. Default Value: None Refer to the list of NI-SCOPE Array Measurements for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Measurements

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-adjust-sample-clock-relative-delay-vi.html language=enus -->
## TOPIC 00033: niScope Adjust Sample Clock Relative Delay VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-adjust-sample-clock-relative-delay-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-adjust-sample-clock-relative-delay-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies offset, in seconds, to the sample clock relative to the reference clock when using the onboard clock. Each time this VI is called, the sample clock is offset from the reference clock by the specified amount of time. Adjustment range: +-1 Sample Clock Period per call Related topics: Improving

### niScope Adjust Sample Clock Relative Delay VI

Applies offset, in seconds, to the sample clock relative to the reference clock when using the onboard clock.

Each time this VI is called, the sample clock is offset from the reference clock by the specified amount of time.

Adjustment range: +-1 *Sample Clock Period* per call

**Related topics:**

- Improving NI-TClk Synchronization of Oscilloscopes with Manual Adjustment
- Sample Clock
- Reference Clock/Phase-Lock Loop
- NI-TClk Overview

[IMAGE alt='icon' src='niscope-adjust-sample-clock-relative-delay-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. delay — delay is the amount of time (in seconds) to delay the sample clock. This value is relative, so repeated calls to this VI delay the sample clock by this amount every time. Default Value: None error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Programming Patterns**

Use this VI when performing manual adjustment to correct for skew and jitter between oscilloscopes synchronized with NI-TClk.

1. Apply time offset with this VI to reduce skew and/or jitter.
2. Use the Oscillator Phase DAC Value property to convert this time offset into a value that can apply the manual adjustment across sessions and improve synchronization repeatability.

For details on performing manual adjustment, refer to [Improving NI-TClk Synchronization of Oscilloscopes with Manual Adjustment](/csh?context=niscope_digitizers_ni-tclk-manual-adjustment-oscilloscopes).

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-attach-grpc-session-vi.html language=enus -->
## TOPIC 00034: niScope Attach gRPC Session VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-attach-grpc-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-attach-grpc-session-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Attaches to an existing NI-SCOPE session with the specified session name on the specified NI gRPC Device Server. Returns a session handle to be used in all subsequent NI-SCOPE VI calls. If you do not specify a session name for the server, or if the specified session name did not previously exist on

### niScope Attach gRPC Session VI

Attaches to an existing NI-SCOPE session with the specified session name on the specified NI gRPC Device Server. Returns a session handle to be used in all subsequent NI-SCOPE VI calls.

Note

This VI creates a new session in LabVIEW that corresponds to the session name specified in the server. If a session with the specified name did not previously exist on the server, then NI-SCOPE will return an error.

The resulting session in LabVIEW forwards driver calls to the corresponding session on the server.

[IMAGE alt='icon' src='niscope-attach-grpc-session-vi.png']

#### Inputs/Outputs

| gRPC options — gRPC options specifies the information used to connect to the server. session name — session name specifies the name of the MeasurementLink gRPC session. address (localhost) — address (localhost) specifies the address of the NI gRPC Device Server. port (31763) — port (31763) specifies the port that the NI gRPC Device Server monitors for connections. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle — instrument handle identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session name — session name specifies the name of the MeasurementLink gRPC session. address (localhost) — address (localhost) specifies the address of the NI gRPC Device Server. port (31763) — port (31763) specifies the port that the NI gRPC Device Server monitors for connections. |

Parent topic:

MeasurementLink

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-auto-setup-vi.html language=enus -->
## TOPIC 00035: niScope Auto Setup VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-auto-setup-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-auto-setup-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automatically configures the digitizer. When you call this VI, the digitizer senses the input signal and automatically configures many of the instrument settings. If a signal is detected on a channel, the driver chooses the smallest available vertical range that is larger than the signal range. For

### niScope Auto Setup VI

Automatically configures the digitizer.

When you call this VI, the digitizer senses the input signal and automatically 
 configures many of the instrument settings. If a signal is detected on a channel, the driver chooses
 the smallest available vertical range that is larger than the signal range. For example, if the signal is
 a 1.2 Vpk-pk sine wave, and the device supports 1 V and 2 V vertical ranges,
 the driver will choose the 2 V vertical range for that channel.

If no signal is found on any analog input channel, a warning is returned and all channels 
 are enabled. A channel is considered to have a signal present if the signal is at least 10% of the 
 smallest vertical range available for that channel.

**Related topics**

- Configuring an Acquisition using Auto_Setup

[IMAGE alt='icon' src='niscope-auto-setup-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Settings Changed by Auto Setup**

This VI changes the following settings to the following values:

| General |  |
| --- | --- |
| Acquisition mode | Normal |
| Reference clock | Internal |
| Vertical |  |
| Vertical coupling | AC (when AC is supported; otherwise DC) |
| Vertical bandwidth | Full |
| Vertical range | Changed by Auto Setup |
| Vertical offset | 0 V |
| Probe attenuation | Unchanged by Auto Setup |
| Input impedance | Unchanged by Auto Setup |
| Horizontal |  |
| Sample rate | Changed by Auto Setup |
| Min record length | Changed by Auto Setup |
| Enforce realtime | True |
| Number of Records | Changed to 1 |
| Triggering |  |
| Trigger type | Edge if signal present, otherwise immediate |
| Trigger channel | Lowest numbered channel with a signal present |
| Trigger slope | Positive |
| Trigger coupling | DC |
| Reference position | 50% |
| Trigger level | 50% of signal on trigger channel |
| Trigger delay | 0 |
| Trigger holdoff | 0 |
| Trigger output | None |

**PXIe-5185 and PXIe-5186 Unique Behavior**

Because PXIe-5185 and PXIe-5186 modules have two physical connectors (50 ohm input impedance, 1 Mohm input impedance) for each channel, this VI has unique behavior for these modules.

When you use niScope Properties to specify the input impedance on either channel or both channels, this VI searches for a signal on only that input connector. If no signal is detected, NI-SCOPE returns a warning and both channels are enabled for the input impedance specified.

If you do not specify an input impedance, this VI searches for a signal on both input connectors (first on the 50 ohm input connector, then on the 1 Mohm input connector). If NI-SCOPE detects a signal on the 50 ohm connector (default) then it uses that signal. If NI-SCOPE does not detect a signal on the 50 ohm connector, it then searches the 1 Mohm connector for a signal. If a signal is not detected on any connectors, NI-SCOPE returns a warning and both channels are enabled with 50 ohm impedance.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cablesense-signal-start-vi.html language=enus -->
## TOPIC 00036: niScope CableSense Signal Start VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cablesense-signal-start-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cablesense-signal-start-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates the CableSense signal on all channels of an oscilloscope for which the signal is enabled, as configured by the CableSense Mode property. The input impedance of the channel(s) to convey the CableSense signal must be set to 50 Ω. You can call this VI only during an acquisition. If you call t

### niScope CableSense Signal Start VI

Generates the CableSense signal on all channels of an oscilloscope for which the signal is enabled, as configured by the [CableSense Mode](/csh?context=niscope_scopepropref_pniscope_cablesensemode) property.

Note

You can call this VI only during an acquisition. If you call this VI while your oscilloscope is not acquiring, NI‑SCOPE generates an error.

**Supported Devices**

- PXIe-5110
- PXIe-5111
- PXIe-5113
- PXIe-5160
- PXIe-5162

[IMAGE alt='icon' src='niscope-cablesense-signal-start-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cablesense-signal-stop-vi.html language=enus -->
## TOPIC 00037: niScope CableSense Signal Stop VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cablesense-signal-stop-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cablesense-signal-stop-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the CableSense signal on all channels of an oscilloscope for which the signal is enabled. Supported Devices PXIe-5110 PXIe-5111 PXIe-5113 PXIe-5160 PXIe-5162 icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error

### niScope CableSense Signal Stop VI

Disables the CableSense signal on all channels of an oscilloscope for which the signal is enabled.

**Supported Devices**

- PXIe-5110
- PXIe-5111
- PXIe-5113
- PXIe-5160
- PXIe-5162

[IMAGE alt='icon' src='niscope-cablesense-signal-stop-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-adjust-accessory-gain-and-offset-vi.html language=enus -->
## TOPIC 00038: niScope Cal Adjust Accessory Gain And Offset VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-adjust-accessory-gain-and-offset-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-adjust-accessory-gain-and-offset-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the PXI-5900 differential amplifier, this VI calibrates the gain and offset. icon Inputs/Outputs civrn.png instrument handle instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. cstr.png channels channels specif

### niScope Cal Adjust Accessory Gain And Offset VI

For the PXI-5900 differential amplifier, this VI calibrates the gain and offset.

[IMAGE alt='icon' src='niscope-cal-adjust-accessory-gain-and-offset-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. channels — channels specifies the channel(s) to calibrate. For more information, refer to Channel String Syntax. posFS — posFS is calculated during the external calibration procedure. gnd — gnd is calculated during the external calibration procedure. negFS — negFS is calculated during the external calibration procedure. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-adjust-compensation-attenuator-vi.html language=enus -->
## TOPIC 00039: niScope Cal Adjust Compensation Attenuator VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-adjust-compensation-attenuator-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-adjust-compensation-attenuator-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI externally calibrates the compensation attenuator. icon Inputs/Outputs civrn.png instrument handle instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. cstr.png channels channels specifies the channel(s) to

### niScope Cal Adjust Compensation Attenuator VI

This VI externally calibrates the compensation attenuator.

[IMAGE alt='icon' src='niscope-cal-adjust-compensation-attenuator-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. channels — channels specifies the channel(s) to calibrate. For more information, refer to Channel String Syntax. range (V) — range (V) is the vertical range to calibrate. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-adjust-dcm-vi.html language=enus -->
## TOPIC 00040: niScope Cal Adjust DCM VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-adjust-dcm-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-adjust-dcm-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For PXIe/PXI/PCI-5105 digitizers, this VI calibrates the external clock digital clock managers (DCMs). DCM calibration ensures that data can be sampled at the correct time in the clock period. icon Inputs/Outputs civrn.png instrument handle instrument handle is the instrument handle that you obtain

### niScope Cal Adjust DCM VI

For PXIe/PXI/PCI-5105 digitizers, this VI calibrates the external clock digital clock managers (DCMs). DCM calibration ensures that data can be sampled at the correct time in the clock period.

[IMAGE alt='icon' src='niscope-cal-adjust-dcm-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. channels — channels specifies the channel(s) to calibrate. For more information, refer to Channel String Syntax. stimulus frequency — stimulus frequency is the external stimulus applied to the digitizer. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-adjust-frequency-response-vi.html language=enus -->
## TOPIC 00041: niScope Cal Adjust Frequency Response VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-adjust-frequency-response-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-adjust-frequency-response-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the PXIe-5622, calibrates the frequency response of the device. The VI is called multiple times, one for each frequency point in the sweep. The user must supply the stimulus frequency in hertz and stimulus amplitude in volts of the input signal. icon Inputs/Outputs civrn.png instrument handle in

### niScope Cal Adjust Frequency Response VI

For the PXIe-5622, calibrates the frequency response of the device. The VI is called multiple times, one for each frequency point in the sweep. The user must supply the **stimulus frequency** in hertz and **stimulus amplitude** in volts of the input signal.

[IMAGE alt='icon' src='niscope-cal-adjust-frequency-response-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. channels — channels specifies the channel(s) to calibrate. For more information, refer to Channel String Syntax. range (V) — range (V) is the vertical range to calibrate. stimulus amplitude — stimulus amplitude is the amplitude of the external stimulus applied to the digitizer. For valid values, refer to the calibration procedure document for the device. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. stimulus frequency — stimulus frequency is the external stimulus applied to the digitizer. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-adjust-offset-range-vi.html language=enus -->
## TOPIC 00042: niScope Cal Adjust Offset Range VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-adjust-offset-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-adjust-offset-range-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI externally calibrates the vertical offset. icon Inputs/Outputs civrn.png instrument handle instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. cstr.png channels channels specifies the channel(s) to calibrat

### niScope Cal Adjust Offset Range VI

This VI externally calibrates the vertical offset.

[IMAGE alt='icon' src='niscope-cal-adjust-offset-range-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. channels — channels specifies the channel(s) to calibrate. For more information, refer to Channel String Syntax. range (V) — range (V) is the vertical range to calibrate. stimulus — stimulus is the voltage of the applied DC signal. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-adjust-range-vi.html language=enus -->
## TOPIC 00043: niScope Cal Adjust Range VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-adjust-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-adjust-range-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI externally calibrates the vertical range for the specified channel and vertical range setting. Related topics: Coercions of Vertical Parameters icon Inputs/Outputs civrn.png instrument handle instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identi

### niScope Cal Adjust Range VI

This VI externally calibrates the vertical range for the specified channel and vertical range setting.

**Related topics:**

- Coercions of Vertical Parameters

[IMAGE alt='icon' src='niscope-cal-adjust-range-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. channels — channels specifies the channel(s) to calibrate. For more information, refer to Channel String Syntax. range (V) — range (V) is the vertical range to calibrate. stimulus — stimulus is the voltage of the applied DC signal. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-adjust-vcxo-vi.html language=enus -->
## TOPIC 00044: niScope Cal Adjust VCXO VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-adjust-vcxo-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-adjust-vcxo-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For SMC-based devices, this VI calibrates the sample rate of the digitizer. The VI adjusts the frequency of the voltage controlled crystal oscillator (VCXO) that serves as the digitizer's onboard sample rate timebase. Check the calibration procedure specific to your device and set the value of frequ

### niScope Cal Adjust VCXO VI

For SMC-based devices, this VI calibrates the sample rate of the digitizer.

The VI adjusts the frequency of the voltage controlled crystal oscillator (VCXO) that serves as
 the digitizer's onboard sample rate timebase. Check the calibration procedure specific to your device and set the value of **frequency parameter**. Before calling this VI, connect an accurate, stable reference signal to 
 channel 0. (The channel used is not configurable.) The VI adjusts frequency calibration constants 
 until the digitizer measures the frequency of the reference signal. The new calibration 
 constants take effect immediately for the duration of the external calibration session. 
 The constants are written to EEPROM if you call [niScope Cal End](niscope-cal-end-vi.html) 
 with no errors and with **action** set to Store Calibration.

Note

Start»All Programs»National Instruments»NI-SCOPE»Documentation»Calibration

[IMAGE alt='icon' src='niscope-cal-adjust-vcxo-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. stimulus frequency (Hz) — stimulus frequency (Hz) is the frequency of the external reference clock connected to channel 0. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-change-password-vi.html language=enus -->
## TOPIC 00045: niScope Cal Change Password VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-change-password-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-change-password-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Verifies the old password against the one stored in the EEPROM. If the two match, the VI stores the new password in the EEPROM. The password is stored as four characters, but shorter strings are acceptable. For most digitizers, the default password is an empty string. For SMC-based devices, the defa

### niScope Cal Change Password VI

Verifies the **old password**against the one stored in the 
 EEPROM.

If the two match, the VI stores the new password in the EEPROM. The password is 
 stored as four characters, but shorter strings are acceptable. For most digitizers, the default 
 password is an empty string. For SMC-based devices, the default password is "NI". If you forget 
 your password, call National Instruments for assistance.

[IMAGE alt='icon' src='niscope-cal-change-password-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. old password — old password is the password currently stored in the EEPROM. new password — new password is the new password to store in the EEPROM. A maximum of 4 characters can be stored. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-end-vi.html language=enus -->
## TOPIC 00046: niScope Cal End VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-end-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-end-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an external calibration session. You must call this VI each time you call niScope Cal Start, even if an error occurs during calibration. icon Inputs/Outputs civrn.png instrument handle instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a p

### niScope Cal End VI

Closes an external calibration session. You must call this VI each time you call [niScope Cal Start](/csh?topicname=niscope-cal-start-vi.html), even if an error occurs during calibration.

[IMAGE alt='icon' src='niscope-cal-end-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. action — action either stores the calibration constants or aborts the calibration and discards any calibration results. Store Calibration (0) Stores the new calibration constants in the EEPROM. For most oscilloscopes, the current system date and the incremented calibration count are also stored. For SMC-based oscilloscopes, the current system date and onboard temperature are also stored. Abort Calibration (1) Closes the session and discards any new calibration constants. Some devices may write to the EEPROM during calibration, in which case this action restores the EEPROM to its original state. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Store Calibration (0) | Stores the new calibration constants in the EEPROM. For most oscilloscopes, the current system date and the incremented calibration count are also stored. For SMC-based oscilloscopes, the current system date and onboard temperature are also stored. |
| Abort Calibration (1) | Closes the session and discards any new calibration constants. Some devices may write to the EEPROM during calibration, in which case this action restores the EEPROM to its original state. |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-fetch-count-vi.html language=enus -->
## TOPIC 00047: niScope Cal Fetch Count VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-fetch-count-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-fetch-count-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of times the digitizer has been calibrated. icon Inputs/Outputs civrn.png instrument handle instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. ci32.png which count which count specifies which ca

### niScope Cal Fetch Count VI

Returns the number of times the digitizer has been calibrated.

[IMAGE alt='icon' src='niscope-cal-fetch-count-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. which count — which count specifies which calibration count to return (self-calibration or external calibration). error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. count — count is the number of times the digitizer has been calibrated. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-fetch-date-vi.html language=enus -->
## TOPIC 00048: niScope Cal Fetch Date VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-fetch-date-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-fetch-date-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the last self-calibration, external calibration, or manufacturer calibration date. icon Inputs/Outputs civrn.png instrument handle instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. ci32.png which date whi

### niScope Cal Fetch Date VI

Returns the last self-calibration, external calibration, or manufacturer calibration date.

[IMAGE alt='icon' src='niscope-cal-fetch-date-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. which date — which date specifies which calibration count to return (self-calibration, external calibration, or manufacturer calibration). error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. year — year is the year of the last calibration, such as 2007. month — month is the month of the last calibration (1–12). day — day is the day of the last calibration (1–31). error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-fetch-misc-info-vi.html language=enus -->
## TOPIC 00049: niScope Cal Fetch Misc Info VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-fetch-misc-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-fetch-misc-info-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the miscellaneous information you can store during an external calibration using niScope Cal Store Misc Info. icon Inputs/Outputs civrn.png instrument handle instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument sessi

### niScope Cal Fetch Misc Info VI

Returns the miscellaneous information you can store during an external 
 calibration using [niScope Cal Store Misc Info](/csh?topicname=niscope-cal-store-misc-info-vi.html).

[IMAGE alt='icon' src='niscope-cal-fetch-misc-info-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. miscellaneous information — miscellaneous information is four characters that are stored in the EEPROM; however, it can be fewer than four characters if NULL-terminated. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-fetch-temperature-vi.html language=enus -->
## TOPIC 00050: niScope Cal Fetch Temperature VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-fetch-temperature-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-fetch-temperature-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For SMC-based digitizers, this VI returns the onboard temperature of the digitizer at the time of the last self-calibration or external calibration, in degrees Celsius. The temperature returned by this VI is an onboard temperature read from a sensor on the surface of the digitizer. This temperature

### niScope Cal Fetch Temperature VI

For SMC-based digitizers, this VI returns the onboard temperature of the digitizer at the time of the 
 last self-calibration or external calibration, in degrees Celsius.

The temperature returned by this
 VI is an onboard temperature read from a sensor on the surface of the digitizer. This temperature 
 should not be confused with the environmental temperature of the digitizer's surroundings. 
 During operation, the onboard temperature is normally higher than the environmental 
 temperature.

Temperature-sensitive parameters are calibrated during self-calibration. 
 Therefore, the self-calibration temperature is usually the more important one to read.

**Related topics**

- Thermal Shutdown
- PXI/PXIe Chassis Cooling

[IMAGE alt='icon' src='niscope-cal-fetch-temperature-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. which temperature — which temperature specifies the calibration temperature to return, either the self-calibration or external calibration temperature. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. temperature (Celsius) — temperature (Celsius) is the returned temperature of the last successful calibration in degrees Celsius. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-measure-ris-distribution-vi.html language=enus -->
## TOPIC 00051: niScope Cal Measure RIS Distribution VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-measure-ris-distribution-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-measure-ris-distribution-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calls niScope Read Waveform 2,000 times to take an acquisition from the specified channel and retrieve the initial X value, which includes the time-to-digital conversion. The time-to-digital conversion should be a uniform distribution between two sample points, because triggers should occur randomly

### niScope Cal Measure RIS Distribution VI

Calls niScope Read Waveform 2,000 times to take an acquisition from the 
 specified channel and retrieve the initial X value, which includes the time-to-digital conversion.

The time-to-digital conversion should be a uniform distribution between two sample points, 
 because triggers should occur randomly. To test this distribution, the distribution of initial X values 
 is created. The percentage of triggers in the smallest bin of this distribution is returned for 
 comparison to a specification to determine if RIS is operating correctly.

**Related topics**

- Random Interleaved Sampling (RIS)

[IMAGE alt='icon' src='niscope-cal-measure-ris-distribution-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. max time (ms) — max time (ms) is the maximum time to allow for each acquisition. channels — channels specifies the channel(s) to calibrate. For more information, refer to Channel String Syntax. distribution size — distribution size is the number of bins in the initial x distribution. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. min bin percent — min bin percent is the percent of triggers in the minimum bin (0–100.0). distribution array — distribution array is the returned distribution of trigger times. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-self-calibrate-vi.html language=enus -->
## TOPIC 00052: niScope Cal Self Calibrate VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-self-calibrate-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-self-calibrate-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Self-calibrates most NI digitizers, including all SMC-based devices. For SMC-based devices, if the self-calibration is performed successfully in a regular session, the calibration constants are immediately stored in the self-calibration area of the EEPROM. If the self-calibration is performed in an

### niScope Cal Self Calibrate VI

Self-calibrates most NI digitizers, including all SMC-based devices.

For SMC-based devices, if the self-calibration is performed successfully in
 a regular session, the calibration constants are immediately stored in the self-calibration area of 
 the EEPROM. If the self-calibration is performed in an external calibration session, the calibration 
 constants take effect immediately for the duration of the session. However, they are not stored in 
 the EEPROM until you call [niScope Cal End](niscope-cal-end-vi.html) with 
 **action** set to Store Calibration and no errors occur.

Note

Features Supported by
 Device

[IMAGE alt='icon' src='niscope-cal-self-calibrate-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) to calibrate. For more information, refer to Channel String Syntax. Option — Option allows you to self-calibrate all channels or restore the external calibration. Defined Values Self-Calibrate All Channels (Default) Restore External Calibration error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-set-accessory-source-vi.html language=enus -->
## TOPIC 00053: niScope Cal Set Accessory Source VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-set-accessory-source-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-set-accessory-source-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For the PXI-5900 differential amplifier, this VI connects the specified channel to the calibration source and sets the calibration source to +/-10 V or to GND. icon Inputs/Outputs civrn.png instrument handle instrument handle is the instrument handle that you obtain from niScope Cal Start. The handl

### niScope Cal Set Accessory Source VI

For the PXI-5900 differential amplifier, this VI connects the specified channel to the calibration source and sets the calibration source to +/-10 V or 
 to GND.

[IMAGE alt='icon' src='niscope-cal-set-accessory-source-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. channels — channels specifies the channel(s) to calibrate. For more information, refer to Channel String Syntax. calSource — calSource specifies calibration signal source. Default Value: GND Defined Values GND -10V +10V error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-start-vi.html language=enus -->
## TOPIC 00054: niScope Cal Start VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-start-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-start-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens an external calibration session and produces a calibration session handle that is required by the external calibration VIs. All other calibration VIs, such as verification and fetch VIs, work with both a calibration session and a session handle obtained from niScope Initialize. Acceptable sess

### niScope Cal Start VI

Opens an external calibration session and produces a calibration session handle that is required by the external calibration VIs.

All other calibration VIs, such as verification and fetch VIs, work with both a 
 calibration session and a session handle obtained from niScope Initialize. Acceptable session 
 handles are documented for each VI in the manual calibration procedure document for each device.

Only one session handle can be obtained at a time, and every session started with this VI must be 
 closed by calling [niScope Cal End](niscope-cal-end-vi.html). If you fail to close the 
 session, you must unload the niScope_32.dll by closing your application or application 
 development environment (ADE) before you can open another session.

[IMAGE alt='icon' src='niscope-cal-start-vi.png']

#### Inputs/Outputs

| resource name — resource name specifies the device name assigned by Measurement & Automation Explorer (MAX). Examples Example Device Type Syntax 1 NI-DAQmx device myDAQmxDevice (myDAQmxDevice = device name) 2 NI-DAQmx device DAQ::myDAQmxDevice (myDAQmxDevice = device name) 3 NI-DAQmx device DAQ::2 (2 = device name) 4 IVI logical name or IVI virtual name myLogicalName (myLogicalName = name) For NI-DAQmx devices, the syntax is just the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by right-clicking on the name in MAX and entering a new name. An alternative syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx device name, as shown in Example 2. This naming convention allows for the use of an NI-DAQmx device in an application that was originally designed for a Traditional NI-DAQ device. For example, if the application expects DAQ::1, you can rename the NI-DAQmx device to 1 in MAX and pass in DAQ::1 for the resource name, as shown in Example 3. You can also pass in the name of an IVI logical name or an IVI virtual name configured with the IVI Configuration utility, as shown in Example 4. A logical name identifies a particular virtual instrument. A virtual name identifies a specific device and specifies the initial settings for the session. Note NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must make sure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. password — password is the password that must match the password in the EEPROM to produce a valid calibration session. The default password for most digitizers is the empty string, " ". The default password for SMC-based devices is "NI". error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle — instrument handle identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |  |
| --- | --- | --- |
| Example | Device Type | Syntax |
| 1 | NI-DAQmx device | myDAQmxDevice (myDAQmxDevice = device name) |
| 2 | NI-DAQmx device | DAQ::myDAQmxDevice (myDAQmxDevice = device name) |
| 3 | NI-DAQmx device | DAQ::2 (2 = device name) |
| 4 | IVI logical name or IVI virtual name | myLogicalName (myLogicalName = name) |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-cal-store-misc-info-vi.html language=enus -->
## TOPIC 00055: niScope Cal Store Misc Info VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-cal-store-misc-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-cal-store-misc-info-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allows you to store miscellaneous information in the EEPROM. For example, you can store an operator ID for the person or company performing a calibration. The information is stored immediately. Four characters are stored in the EEPROM, and nonprintable characters are valid. However, NULL is treated

### niScope Cal Store Misc Info VI

Allows you to store miscellaneous information in the EEPROM. For example, you can store 
 an operator ID for the person or company performing a calibration. The information is stored 
 immediately.

Four characters are stored in the EEPROM, and nonprintable characters
 are valid. However, NULL is treated as an end-of-string marker, and all characters following the first 
 NULL are set to NULL.

[IMAGE alt='icon' src='niscope-cal-store-misc-info-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle is the instrument handle that you obtain from niScope Cal Start. The handle identifies a particular instrument session. miscellaneous information — miscellaneous information is four characters that are stored in the EEPROM; however, can be fewer than four if NULL-terminated. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Calibration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-clear-error-info-vi.html language=enus -->
## TOPIC 00056: niScope Clear Error Info VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-clear-error-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-clear-error-info-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the error information for the current execution thread and the IVI session you specify. If you pass VI_NULL for the Instrument Handle, this VI clears the error information only for the current execution thread. The error information includes a primary error, secondary error, and an error elab

### niScope Clear Error Info VI

Clears the error information for the current execution thread and the IVI session you specify. 
 If you pass VI_NULL for the Instrument Handle, this VI clears the error information only for the 
 current execution thread.

The error information includes a primary error, secondary error, and an error 
 elaboration string. For a particular session, this information is the same as the values held in the 
 following properties:

niScope>>Inherent IVI Settings>>Error Info>>Primary Error

niScope>>Inherent IVI Settings>>Error Info>>Secondary Error

niScope>>Inherent IVI Settings>>Error Info>>Error Elaboration

This VI sets the primary and secondary error codes to VI_SUCCESS (0), and sets the error 
 elaboration string to " ".

Note

[IMAGE alt='icon' src='niscope-clear-error-info-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-clear-waveform-measurement-stats-vi.html language=enus -->
## TOPIC 00057: niScope Clear Waveform Measurement Stats VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-clear-waveform-measurement-stats-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-clear-waveform-measurement-stats-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the waveform statistics on the channel and measurement you specify. This VI clears the statistical information and the multi-acquisition array measurements. Every time a measurement is called, the statistics information is updated, including the min, max, mean, standard deviation, and number

### niScope Clear Waveform Measurement Stats VI

Clears the waveform statistics on the channel and measurement you specify. This 
 VI clears the statistical information and the multi-acquisition array measurements.

Every time a measurement is called, the statistics information is updated, including the 
 min, max, mean, standard deviation, and number of updates.

[IMAGE alt='icon' src='niscope-clear-waveform-measurement-stats-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. clearable measurement — clearable measurement is the measurement for which to clear the statistics. Refer to the list of NI-SCOPE Scalar Measurements or Array Measurements for constants. To clear all of the measurements, specify All Measurements. Default Value: All Measurements error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Measurements

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-clear-waveform-processing-vi.html language=enus -->
## TOPIC 00058: niScope Clear Waveform Processing VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-clear-waveform-processing-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-clear-waveform-processing-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the list of processing steps assigned to the given channel. The processing steps are added with niScope Add Waveform Processing, where the steps are completed in the same order in which they are registered. The processing measurements are streamed, so the result of the first processing step i

### niScope Clear Waveform Processing VI

Clears the list of processing steps assigned to the given channel.

The processing steps are added with [niScope Add Waveform Processing](niscope-add-waveform-processing-vi.html), 
 where the steps are completed in the same order in which they are registered. The processing 
 measurements are streamed, so the result of the first processing step is used as the input for the next 
 step. The processing is also done before any other measurements.

[IMAGE alt='icon' src='niscope-clear-waveform-processing-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Measurements

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-close-vi.html language=enus -->
## TOPIC 00059: niScope Close VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-close-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-close-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the following actions: -Closes the instrument I/O session. -Destroys the IVI session and all of its properties. -Deallocates any memory resources used by the IVI session. Call this VI when you are finished using an instrument driver session. Related topics NI-SCOPE Programming Flow icon Inp

### niScope Close VI

Performs the following actions:

-Closes the instrument I/O session.

-Destroys the IVI session and all of its properties.

-Deallocates any memory resources used by the IVI session.

Call this VI when you are finished using an instrument driver session.

**Related topics**

- NI-SCOPE Programming Flow

[IMAGE alt='icon' src='niscope-close-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-commit-vi.html language=enus -->
## TOPIC 00060: niScope Commit VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-commit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-commit-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits to hardware all the parameter settings associated with the task. Use this VI if you want a parameter change to be immediately reflected in the hardware. After using a Configuration VI to set a parameter, call this VI, which causes the driver to write the new configuration to the digitizer ha

### niScope Commit VI

Commits to hardware all the parameter settings associated with the task.
 Use this VI if you want a parameter change to be immediately reflected in the hardware.

After using a Configuration VI to set a parameter, call this VI, 
 which causes the driver to write the new configuration to the digitizer hardware immediately instead of waiting until the next call to [niScope Initiate Acquisition](niscope-initiate-acquisition-vi.html).

**Related topics:**

- SMC-Based Digitizers Acquisition Engine State Diagram
- NI-SCOPE Programming Flow

[IMAGE alt='icon' src='niscope-commit-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Acquisition

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-acquisition-vi.html language=enus -->
## TOPIC 00061: niScope Configure Acquisition VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-acquisition-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-acquisition-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures how the oscilloscope acquires data and fills the waveform record. Related topics Acquisition Functions icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. ci32.png acquisition Type acquisition Type is the manner in which the oscill

### niScope Configure Acquisition VI

Configures how the oscilloscope acquires data and fills the waveform record.

**Related topics**

- Acquisition Functions

[IMAGE alt='icon' src='niscope-configure-acquisition-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. acquisition Type — acquisition Type is the manner in which the oscilloscope acquires data and fills the waveform record. Not all oscilloscopes support all acquisition types; refer to Features Supported by Device for more information. Default Value: Normal Defined Values Normal (0) Sets the oscilloscope to normal resolution mode. The oscilloscope can use real-time sampling or equivalent-time sampling. Flex Res (1) Sets legacy oscilloscopes to flexible resolution mode, if supported. DDC (3) Sets legacy oscilloscopes to DDC mode, if supported. To use DDC mode for the PXI/PCI-5142 or PXIe-5622, set this parameter to Normal and set the DDC Enabled property to True. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Normal (0) | Sets the oscilloscope to normal resolution mode. The oscilloscope can use real-time sampling or equivalent-time sampling. |
| Flex Res (1) | Sets legacy oscilloscopes to flexible resolution mode, if supported. |
| DDC (3) | Sets legacy oscilloscopes to DDC mode, if supported. To use DDC mode for the PXI/PCI-5142 or PXIe-5622, set this parameter to Normal and set the DDC Enabled property to True. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-chan-characteristics-vi.html language=enus -->
## TOPIC 00062: niScope Configure Chan Characteristics VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-chan-characteristics-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-chan-characteristics-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the properties that control the electrical characteristics of the channel. These properties are the input impedance and the bandwidth. Related topics: Using Configure Chan Characteristics Impedance and Impedance Matching icon Inputs/Outputs civrn.png instrument handle instrument handle id

### niScope Configure Chan Characteristics VI

Configures the properties that control the electrical characteristics of the channel.
 These properties are the input impedance and the bandwidth.

**Related topics:**

- Using Configure Chan Characteristics
- Impedance and Impedance Matching

[IMAGE alt='icon' src='niscope-configure-chan-characteristics-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. input impedance — input impedance is the input impedance for the channel. Default Value: 1 mega ohm Defined Values 1 mega ohm 50 ohms max input frequency — maximum input frequency specifies the bandwidth of the channel at which the input circuitry attenuates the signal by 3 dB. Pass 0 for this value to use the hardware default bandwidth. Pass -1 for this value to achieve full bandwidth. Default Value: 0.00 Hz error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-clock-vi.html language=enus -->
## TOPIC 00063: niScope Configure Clock VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-clock-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-clock-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the properties for synchronizing the digitizer to an external clock or sending the digitizer's clock output to be used as a synchronizing clock for other devices. Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. Related topics

### niScope Configure Clock VI

Configures the properties for synchronizing the digitizer to an external clock or sending the digitizer's clock output to be used as a synchronizing clock for other devices.

Note

Features Supported by Device

**Related topics**

- Sample Clock
- Sample Rate
- Coercions of Horizontal Parameters

[IMAGE alt='icon' src='niscope-configure-clock-vi.png']

#### Inputs/Outputs

| reference (input) clock source — input clock source specifies the input source for the PLL reference clock (such as the 1-20 MHz clock on SMC-based devices) to which the digitizer is phase-locked for all digitizers. Refer to the Reference (Input) Clock Source property for defined values. Default Value: None instrument handle — instrument handle identifies a particular instrument session. clock sync pulse source — clock sync pulse source specifies the line on which the sample clock or the one-time sync pulse is sent or received. Default Value: RTSI 0 Refer to the Clock Sync Pulse Source property for defined values. master enabled — master enabled specifies whether the device is a master or a slave; the master device is typically the originator of the trigger signal and clock sync pulse. For a standalone device, set this parameter to FALSE. Default Value: FALSE error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. output clock source — output clock source specifies the output source for the PLL reference clock to which the sample clock of another digitizer can be phase-locked. Refer to the Output Clock Source property for more information. Default Value: None instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-equalization-filter-coefficients-vi.html language=enus -->
## TOPIC 00064: niScope Configure Equalization Filter Coefficients VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-equalization-filter-coefficients-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-equalization-filter-coefficients-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the custom coefficients for the equalization FIR filter on the device. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should

### niScope Configure Equalization Filter Coefficients VI

Configures the custom coefficients for the equalization FIR filter on the device. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and -1.

Note

[IMAGE alt='icon' src='niscope-configure-equalization-filter-coefficients-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. coefficients — coefficients are the custom coefficients for the equalization FIR filter on the device. These coefficients should be between +1 and –1. You can obtain the number of coefficients from the Equalization Num Coefficients property. The Equalization Filter Enabled property must be set to TRUE to enable the filter. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Onboard Signal Processing

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-horizontal-timing-vi.html language=enus -->
## TOPIC 00065: niScope Configure Horizontal Timing VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-horizontal-timing-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-horizontal-timing-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the common properties of the horizontal subsystem for a single record or multirecord acquisition, such as minimum sample rate and acquisition size. Related topics Configuring the Horizontal Settings NI-TClk Overview Coercions of Horizontal Parameters icon Inputs/Outputs cbool.png enforce

### niScope Configure Horizontal Timing VI

Configures the common properties of the horizontal subsystem for a single record or multirecord acquisition, such as minimum sample rate and acquisition size.

**Related topics**

- Configuring the Horizontal Settings
- NI-TClk Overview
- Coercions of Horizontal Parameters

[IMAGE alt='icon' src='niscope-configure-horizontal-timing-vi.png']

#### Inputs/Outputs

| enforce realtime — enforce realtime indicates whether the digitizer enforces real-time measurements or allows equivalent-time (RIS) measurements. Default Value:TRUE Defined Values TRUE (Default)—Allow real-time acquisitions only FALSE—Allow real-time and RIS acquisitions Note Not all digitizers support RIS—refer to Features Supported by Device for more information. number of records — number of records specifies the number of records to acquire. Default Value: 1 instrument handle — instrument handle identifies a particular instrument session. min sample rate — min sample rate specifies the sample rate for the acquisition. Default Value: 20 MS/s reference position — reference position specifies the position of the Reference Event in the waveform record as a percentage of the record. Default Value: 50% error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. min record length — min record length passes the minimum number of points you need in the record for each channel. Call niScope Actual Record Length to obtain the actual record length used. Refer to Coercions of Horizontal Parameters for more information about why the record length may be different than what was specified. The value must be greater than 1 and is limited by available memory. Default Value: 1000 instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SCOPE

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-trigger-digital-vi.html language=enus -->
## TOPIC 00066: niScope Configure Trigger Digital VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-trigger-digital-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-trigger-digital-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the common properties of a digital trigger. Digital triggering is not supported in RIS mode. icon Inputs/Outputs ci32.png trigger slope trigger slope specifies either a rising edge or a falling edge to trigger the digitizer. Refer to the Trigger Slope property for defined values. civrn.pn

### niScope Configure Trigger Digital VI

Configures the common properties of a digital trigger.

Note

RIS mode

[IMAGE alt='icon' src='niscope-configure-trigger-digital-vi.png']

#### Inputs/Outputs

| trigger slope — trigger slope specifies either a rising edge or a falling edge to trigger the digitizer. Refer to the Trigger Slope property for defined values. instrument handle — instrument handle identifies a particular instrument session. trigger source — trigger source passes the source you want the digitizer to monitor for a trigger. Default Value: Channel 0 Refer to the Trigger Source property for defined values. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. trigger holdoff — trigger holdoff specifies the length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Default Value: 0.0 s trigger delay — trigger delay specifies how long the digitizer waits after it receives the trigger to start acquiring data. Default Value: 0.0 s instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-trigger-edge-vi.html language=enus -->
## TOPIC 00067: niScope Configure Trigger Edge VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-trigger-edge-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-trigger-edge-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures common properties for edge triggering. An edge trigger occurs when a signal crosses a trigger threshold you specify. icon Inputs/Outputs cu16.png trigger coupling trigger coupling specifies how to couple the trigger signal. Refer to the Trigger Coupling property for defined values. ci32.p

### niScope Configure Trigger Edge VI

Configures common properties for edge triggering.

An edge trigger occurs when a signal crosses a trigger threshold you specify.

[IMAGE alt='icon' src='niscope-configure-trigger-edge-vi.png']

#### Inputs/Outputs

| trigger coupling — trigger coupling specifies how to couple the trigger signal. Refer to the Trigger Coupling property for defined values. trigger slope — trigger slope specifies either a rising edge or a falling edge to trigger the digitizer. Refer to the Trigger Slope property for defined values. instrument handle — instrument handle identifies a particular instrument session. trigger source (Channel 0) — trigger source passes the source you want the digitizer to monitor for a trigger. Default Value: Channel 0 Refer to the Trigger Source property for defined values. trigger level — trigger level specifies the voltage threshold for the trigger. Default Value: 0.0 V error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. trigger holdoff — trigger holdoff specifies the length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Default Value: 0.0 s trigger delay — trigger delay specifies how long the digitizer waits after it receives the trigger to start acquiring data. Default Value: 0.0 s instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-trigger-glitch-vi.html language=enus -->
## TOPIC 00068: niScope Configure Trigger Glitch VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-trigger-glitch-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-trigger-glitch-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures common properties for glitch triggering. A glitch trigger occurs when a pulse that crosses a vertical threshold you specify and with a polarity you specify also has a width that is either greater than or less than a duration you specify. icon Inputs/Outputs cdbl.png width width specifies,

### niScope Configure Trigger Glitch VI

Configures common properties for glitch triggering.

A glitch trigger occurs when a pulse that crosses a vertical threshold you specify and with a polarity you specify also has a width that is either greater than or less than a duration you specify.

[IMAGE alt='icon' src='niscope-configure-trigger-glitch-vi.png']

#### Inputs/Outputs

| width — width specifies, in seconds, the glitch duration to be used in combination with the glitch condition that triggers the oscilloscope. The oscilloscope triggers when it detects a pulse of duration either less than or greater than this value depending on the value of the Glitch Condition property. Refer to the Glitch Width property for more information. trigger coupling — trigger coupling specifies how to couple the trigger signal. Refer to the Trigger Coupling property for defined values. polarity — polarity specifies the polarity of the pulses that trigger the oscilloscope for glitch triggering. Refer to the Glitch Polarity property for defined values. instrument handle — instrument handle identifies a particular instrument session. trigger source — trigger source passes the source you want the digitizer to monitor for a trigger. Default Value: Channel 0 Refer to the Trigger Source property for defined values. trigger level — trigger level specifies the voltage threshold for the trigger. Default Value: 0.0 V glitch condition — glitch condition specifies whether the oscilloscope triggers on pulses of duration less than or greater than the specified Glitch Width. Refer to the Glitch Condition property for defined values. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. trigger holdoff — trigger holdoff specifies the length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Default Value: 0.0 s trigger delay — trigger delay specifies how long the digitizer waits after it receives the trigger to start acquiring data. Default Value: 0.0 s instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-trigger-hysteresis-vi.html language=enus -->
## TOPIC 00069: niScope Configure Trigger Hysteresis VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-trigger-hysteresis-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-trigger-hysteresis-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures common properties for hysteresis triggering. This kind of trigger specifies an additional value, specified in the hysteresis parameter, that a signal must pass through before a trigger can occur. This additional value acts as a buffer zone that keeps noise from triggering an acquisition.

### niScope Configure Trigger Hysteresis VI

Configures common properties for hysteresis triggering. This kind of trigger specifies
 an additional value, specified in the **hysteresis** parameter,
 that a signal must pass through before a trigger can occur. This additional value acts
 as a buffer zone that keeps noise from triggering an acquisition.

[IMAGE alt='icon' src='niscope-configure-trigger-hysteresis-vi.png']

#### Inputs/Outputs

| trigger coupling — trigger coupling specifies how to couple the trigger signal. Refer to the Trigger Coupling property for defined values. trigger slope — trigger slope specifies either a rising edge or a falling edge to trigger the digitizer. Refer to the Trigger Slope property for defined values. instrument handle — instrument handle identifies a particular instrument session. trigger source (Channel 0) — trigger source passes the source you want the digitizer to monitor for a trigger. Default Value: Channel 0 Refer to the Trigger Source property for defined values. trigger level — trigger level specifies the voltage threshold for the trigger. Default Value: 0.0 V hysteresis — hysteresis specifies, in volts, the size of the hysteresis window on either side of the trigger level. The digitizer triggers when the trigger signal passes through the hysteresis value you specify with this parameter, has the slope you specify with the trigger slope, and passes through the trigger level. Default Value: 0.05 V Valid Values Positive trigger slope 0 <= Hysteresis <= Trigger Level + (Vertical Range / 2) - Vertical Offset Negative trigger slope 0 <= Hysteresis <= (Vertical Range / 2) + Vertical Offset - Trigger Level error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. trigger holdoff — trigger holdoff specifies the length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Default Value: 0.0 s trigger delay — trigger delay specifies how long the digitizer waits after it receives the trigger to start acquiring data. Default Value: 0.0 s instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Positive trigger slope | 0 <= Hysteresis <= Trigger Level + (Vertical Range / 2) - Vertical Offset |
| Negative trigger slope | 0 <= Hysteresis <= (Vertical Range / 2) + Vertical Offset - Trigger Level |

Parent topic:

niScope Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-trigger-immediate-vi.html language=enus -->
## TOPIC 00070: niScope Configure Trigger Immediate VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-trigger-immediate-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-trigger-immediate-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures common properties for immediate triggering. Immediate triggering means the digitizer triggers itself. Related topics: Immediate Triggers icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in error in describ

### niScope Configure Trigger Immediate VI

Configures common properties for immediate triggering. Immediate triggering means the
 digitizer triggers itself.

**Related topics:**

- Immediate Triggers

[IMAGE alt='icon' src='niscope-configure-trigger-immediate-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-trigger-output-vi.html language=enus -->
## TOPIC 00071: niScope Configure Trigger Output VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-trigger-output-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-trigger-output-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the digitizer to generate a signal pulse that other digitizers can detect when configured for digital triggering. For NI-DAQmx devices, closing the session clears the routes. However, if you want to clear the routes before closing the session, call this VI again, routing the Stop Trigger

### niScope Configure Trigger Output VI

Configures the digitizer to generate a signal pulse that other digitizers can detect when configured for digital triggering.

For NI-DAQmx devices, closing the session clears the routes. However, if you want to clear the routes before closing the session, call this VI again, routing the Stop Trigger to None.

This VI is obsolete. Consider using [niScope Export Signal](niscope-export-signal-vi.html) instead.

[IMAGE alt='icon' src='niscope-configure-trigger-output-vi.png']

#### Inputs/Outputs

| trigger event — trigger event specifies the condition in which this device will generate a digital pulse. instrument handle — instrument handle identifies a particular instrument session. trigger output source — trigger output source specifies the hardware signal line on which the digital pulse is generated. Default Value: No event (none) Defined Values None RTSI 0 RTSI 1 RTSI 2 RTSI 3 RTSI 4 RTSI 5 RTSI 6 RTSI 7 PFI 0 PFI 1 PFI 2 PXI Star error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-trigger-poly-vi.html language=enus -->
## TOPIC 00072: niScope Configure Trigger (poly) VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-trigger-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-trigger-poly-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the digitizer for different types of triggering. When you initiate an acquisition, the trigger system operates in the following manner: The digitizer waits for the start trigger, which is configured through the Start Trigger Source property. The default is VAL_IMMEDIATE. Upon receiving th

### niScope Configure Trigger (poly) VI

Configures the digitizer for different types of triggering.

When you initiate an acquisition, the trigger system operates in the following manner:

- The digitizer waits for the start trigger, which is configured through the Start Trigger Source property. The default is VAL_IMMEDIATE.
- Upon receiving the start trigger, the digitizer begins sampling pretrigger points.
- After the digitizer finishes sampling pretrigger points, the digitizer waits for a reference (stop) trigger that you specify with a Configure Trigger instance.
- Upon receiving the reference trigger, the digitizer finishes the acquisition after completing posttrigger sampling.

With each Configure Trigger instance, you specify configuration parameters such as the trigger source and the amount of trigger delay. Additionally, you can adjust the amount of pretrigger and posttrigger samples using the **reference position** parameter in [niScope Configure Horizontal Timing](niscope-configure-horizontal-timing-vi.html). The default is half the record length.

For multirecord acquisitions, all records after the first record are started based on the setting of the [Advance Trigger Source](/csh?context=niscope_scopepropref_pniscope_advancetriggersource) property. The default is VAL_IMMEDIATE.

|  | Note Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. |
| --- | --- |

**Related topics**

- Triggering
- NI-SCOPE Programming Flow

[IMAGE alt='icon' src='niscope-configure-trigger-poly-vi.png']

- [niScope Configure Trigger Edge VI](../../../instr-lib/niscope/niscope-llb/niscope-configure-trigger-edge-vi.html) Configures common properties for edge triggering.
- [niScope Configure Trigger Hysteresis VI](../../../instr-lib/niscope/niscope-llb/niscope-configure-trigger-hysteresis-vi.html) Configures common properties for hysteresis triggering. This kind of trigger specifies an additional value, specified in the hysteresis parameter, that a signal must pass through before a trigger can occur. This additional value acts as a buffer zone that keeps noise from triggering an acquisition.
- [niScope Configure Video Trigger VI](../../../instr-lib/niscope/niscope-llb/niscope-configure-video-trigger-vi.html) Configures the common properties specific to video triggering. The video triggering properties are polarity, enable DC restore, signal format, event, and line number. A video trigger occurs when the digitizer finds a valid video signal sync. Use the trigger holdoff to skip a specific number of frames between acquisitions. For example, to acquire a specific line number multiple times and repeat the same chroma phase, skip one frame in NTSC (121 ms < holdoff < 159 ms) and five frames in SECAM (201 ms < holdoff < 239 ms).
- [niScope Configure Trigger Window VI](../../../instr-lib/niscope/niscope-llb/niscope-configure-trigger-window-vi.html) Configures common properties for window triggering. A window trigger occurs when a signal enters or leaves a window you specify with the high level or low level parameters.
- [niScope Configure Trigger Glitch VI](../../../instr-lib/niscope/niscope-llb/niscope-configure-trigger-glitch-vi.html) Configures common properties for glitch triggering.
- [niScope Configure Trigger Runt VI](../../../instr-lib/niscope/niscope-llb/niscope-configure-trigger-runt-vi.html) Configures common properties for runt triggering.
- [niScope Configure Trigger Width VI](../../../instr-lib/niscope/niscope-llb/niscope-configure-trigger-width-vi.html) Configures common properties for width triggering.
- [niScope Configure Trigger Digital VI](../../../instr-lib/niscope/niscope-llb/niscope-configure-trigger-digital-vi.html) Configures the common properties of a digital trigger.
- [niScope Configure Trigger Immediate VI](../../../instr-lib/niscope/niscope-llb/niscope-configure-trigger-immediate-vi.html) Configures common properties for immediate triggering. Immediate triggering means the digitizer triggers itself.
- [niScope Configure Trigger Software VI](../../../instr-lib/niscope/niscope-llb/niscope-configure-trigger-software-vi.html) Configures common properties for software triggering. This VI only works in an Initiate/Fetch operation.

Parent topic:

NI-SCOPE

Parent topic:

Triggering

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-trigger-runt-vi.html language=enus -->
## TOPIC 00073: niScope Configure Trigger Runt VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-trigger-runt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-trigger-runt-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures common properties for runt triggering. A runt trigger occurs when both the leading edge and trailing edge of a pulse cross only one of two trigger thresholds you specify and with a polarity you specify, where the polarity is relative to the threshold crossed. You can add time qualificatio

### niScope Configure Trigger Runt VI

Configures common properties for runt triggering.

A runt trigger occurs when both the leading edge and trailing edge of a pulse cross only one of two trigger thresholds you specify and with a polarity you specify, where the polarity is relative to the threshold crossed.

Note

Runt Time Condition

Runt Time Low Limit

Runt Time High Limit

[IMAGE alt='icon' src='niscope-configure-trigger-runt-vi.png']

#### Inputs/Outputs

| trigger coupling — trigger coupling specifies how to couple the trigger signal. Refer to the Trigger Coupling property for defined values. polarity — polarity specifies the polarity of the runt pulses, relative to the runt threshold the pulses cross, that trigger the oscilloscope for runt triggering. Refer to the Runt Polarity property for defined values. instrument handle — instrument handle identifies a particular instrument session. trigger source (Channel 0) — trigger source passes the source you want the digitizer to monitor for a trigger. Default Value: Channel 0 Refer to the Trigger Source property for defined values. low threshold — low threshold specifies, in volts, the lower of two thresholds that bound the vertical range to examine for runt pulses. Refer to the Runt Low Threshold property for more information. high threshold — high threshold specifies, in volts, the higher of two thresholds that bound the vertical range to examine for runt pulses. Refer to the Runt High Threshold property for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. trigger holdoff — trigger holdoff specifies the length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Default Value: 0.0 s trigger delay — trigger delay specifies how long the digitizer waits after it receives the trigger to start acquiring data. Default Value: 0.0 s instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-trigger-software-vi.html language=enus -->
## TOPIC 00074: niScope Configure Trigger Software VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-trigger-software-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-trigger-software-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures common properties for software triggering. This VI only works in an Initiate/Fetch operation. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in error in describes error conditions that occur before this

### niScope Configure Trigger Software VI

Configures common properties for software triggering. This VI only works in an
 Initiate/Fetch operation.

[IMAGE alt='icon' src='niscope-configure-trigger-software-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. trigger holdoff — trigger holdoff specifies the length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Default Value: 0.0 s trigger delay — trigger delay specifies how long the digitizer waits after it receives the trigger to start acquiring data. Default Value: 0.0 s instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-trigger-width-vi.html language=enus -->
## TOPIC 00075: niScope Configure Trigger Width VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-trigger-width-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-trigger-width-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures common properties for width triggering. A width trigger occurs when a pulse that crosses a vertical threshold you specify and with a polarity you specify also has a duration that is either within or outside a duration range you specify. icon Inputs/Outputs cdbl.png low threshold low thres

### niScope Configure Trigger Width VI

Configures common properties for width triggering.

A width trigger occurs when a pulse that crosses a vertical threshold you specify and with a polarity you specify also has a duration that is either within or outside a duration range you specify.

[IMAGE alt='icon' src='niscope-configure-trigger-width-vi.png']

#### Inputs/Outputs

| low threshold — low threshold specifies, in seconds, the lower bound on the range of pulse durations that triggers the oscilloscope. Refer to the Width Low Threshold property for more information. trigger coupling — trigger coupling specifies how to couple the trigger signal. Refer to the Trigger Coupling property for defined values. polarity — polarity specifies the polarity of the pulses that trigger the oscilloscope for width triggering. Refer to the Width Polarity property for defined values. instrument handle — instrument handle identifies a particular instrument session. trigger source — trigger source passes the source you want the digitizer to monitor for a trigger. Default Value: Channel 0 Refer to the Trigger Source property for defined values. trigger level — trigger level specifies the voltage threshold for the trigger. Default Value: 0.0 V width condition — width condition specifies whether the oscilloscope triggers on pulses of duration within or outside the range of pulse durations bounded by low threshold and high threshold. Refer to the Width Condition property for defined values. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. trigger holdoff — trigger holdoff specifies the length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Default Value: 0.0 s trigger delay — trigger delay specifies how long the digitizer waits after it receives the trigger to start acquiring data. Default Value: 0.0 s high threshold — high threshold specifies, in seconds, the upper bound on the range of pulse durations that triggers the oscilloscope. Refer to the Width High Threshold property for more information. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-trigger-window-vi.html language=enus -->
## TOPIC 00076: niScope Configure Trigger Window VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-trigger-window-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-trigger-window-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures common properties for window triggering. A window trigger occurs when a signal enters or leaves a window you specify with the high level or low level parameters. icon Inputs/Outputs cu16.png trigger coupling trigger coupling specifies how to couple the trigger signal. Refer to the Trigger

### niScope Configure Trigger Window VI

Configures common properties for window triggering. A window trigger occurs when a
 signal enters or leaves a window you specify with the **high level** or **low level**
 parameters.

[IMAGE alt='icon' src='niscope-configure-trigger-window-vi.png']

#### Inputs/Outputs

| trigger coupling — trigger coupling specifies how to couple the trigger signal. Refer to the Trigger Coupling property for defined values. trigger window mode — trigger window mode specifies whether the trigger should occur when the signal is entering or leaving a window. Default Value: Entering instrument handle — instrument handle identifies a particular instrument session. trigger source (Channel 0) — trigger source passes the source you want the digitizer to monitor for a trigger. Default Value: Channel 0 Refer to the Trigger Source property for defined values. low level — low level passes the voltage threshold for the digitizer to use for low triggering. Default Value: 0 V high level — high level passes the voltage threshold for the digitizer to use for high triggering. Default Value: 0.10 V error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. trigger holdoff — trigger holdoff specifies the length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Default Value: 0.0 s trigger delay — trigger delay specifies how long the digitizer waits after it receives the trigger to start acquiring data. Default Value: 0.0 s instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-vertical-vi.html language=enus -->
## TOPIC 00077: niScope Configure Vertical VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-vertical-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-vertical-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the most commonly configured properties of the digitizer vertical subsystem, such as the range, offset, coupling, probe attenuation, and the channel name. Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. Related topics Configur

### niScope Configure Vertical VI

Configures the most commonly configured properties of the digitizer vertical
 subsystem, such as the range, offset, coupling, probe attenuation, and the channel name.

Note

Features Supported by
 Device

**Related topics**

- Configuring the Vertical Settings
- NI-SCOPE Programming Flow
- Coercions of Vertical Parameters

[IMAGE alt='icon' src='niscope-configure-vertical-vi.png']

#### Inputs/Outputs

| vertical coupling — vertical coupling specifies how to couple the input signal. When input coupling changes, the input stage takes a finite amount of time to settle. probe attenuation — probe attenuation specifies the probe attenuation for the input channel. Default Value: 1 instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. vertical range — vertical range specifies the absolute value of the input range for a channel. For example, to acquire a sine wave that spans between –5 and +5 V, set the vertical range to 10.0 V. vertical offset — vertical offset specifies the location of the center of the range with respect to ground. For example, to acquire a sine wave that spans between 0.0 and 10.0 V, set this property to 5.0 V. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. channel enabled — channel enabled specifies whether the channel is enabled for acquisition. Default Value: TRUE instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SCOPE

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-configure-video-trigger-vi.html language=enus -->
## TOPIC 00078: niScope Configure Video Trigger VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-configure-video-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-configure-video-trigger-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the common properties specific to video triggering. The video triggering properties are polarity, enable DC restore, signal format, event, and line number. A video trigger occurs when the digitizer finds a valid video signal sync. Use the trigger holdoff to skip a specific number of frame

### niScope Configure Video Trigger VI

Configures the common properties specific to video triggering. The video triggering properties are polarity, enable DC restore, signal format, event, and line number. A video trigger occurs when the digitizer finds a valid video signal sync. Use the **trigger holdoff** to skip a specific number of frames between acquisitions. For example, to acquire a specific line number multiple times and repeat the same chroma phase, skip one frame in NTSC (121 ms < holdoff < 159 ms) and five frames in SECAM (201 ms < holdoff < 239 ms).

[IMAGE alt='icon' src='niscope-configure-video-trigger-vi.png']

#### Inputs/Outputs

| TV event — TV event specifies what TV event to trigger on. Refer to the Event property for defined values. trigger coupling — trigger coupling specifies how to couple the trigger signal. Refer to the Trigger Coupling property for defined values. polarity — polarity specifies the polarity of the video sync. Default Value: negative Defined Values: positive negative instrument handle — instrument handle identifies a particular instrument session. trigger source (Channel 0) — trigger source passes the source you want the digitizer to monitor for a trigger. Default Value: Channel 0 Refer to the Trigger Source property for defined values. enable DC restore — enable DC restore offsets each video line so the clamping level (the portion of the video line between the color burst and the beginning of the active image) is moved to zero volt. Default Value: FALSE signal format (M-NTSC) — signal format specifies the video format to use. Refer to the Signal Format property for defined values. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. trigger holdoff — trigger holdoff specifies the length of time the digitizer waits after detecting a trigger before enabling NI-SCOPE to detect another trigger. Default Value: 0.0 s trigger delay — trigger delay specifies how long the digitizer waits after it receives the trigger to start acquiring data. Default Value: 0.0 s line number — line number specifies the line number to trigger on. The line number range covers an entire frame and is referenced as shown in Vertical Blanking and Synchronization Signal. The number of lines available depends on the format. For valid ranges, refer to the Line Number property. Default value: 1 instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Configure Trigger (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-detach-grpc-session-vi.html language=enus -->
## TOPIC 00079: niScope Detach gRPC Session VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-detach-grpc-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-detach-grpc-session-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the session specified in instrument handle but leaves the session open on the NI gRPC Device Server. NI-SCOPE returns an error unless an open session at instrument handle exists and was created using the niScope Initialize for gRPC session VI or the niScope Attach gRPC session VI. icon Inputs

### niScope Detach gRPC Session VI

Closes the session specified in **instrument handle** but leaves the session open on the NI gRPC Device Server.

NI-SCOPE returns an error unless an open session at **instrument handle** exists and was created using the [niScope Initialize for gRPC session](/csh?context=niscope_scopeviref_scopeviref.chm::niscope_initialize_for_grpc_session) VI or the [niScope Attach gRPC session](/csh?context=niscope_scopeviref_scopeviref.chm::niscope_attach_grpc_session) VI.

[IMAGE alt='icon' src='niscope-detach-grpc-session-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

MeasurementLink

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-disable-vi.html language=enus -->
## TOPIC 00080: niScope Disable VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-disable-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-disable-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts the current task, opens the data channel relays, and releases all RTSI and PFI lines. Use this VI for a condition where you want to stop the current acquisition and disable the channels. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument sessi

### niScope Disable VI

Aborts the current task, opens the data channel relays, and releases all RTSI and PFI
 lines. Use this VI for a condition where you want to stop the current acquisition and
 disable the channels.

[IMAGE alt='icon' src='niscope-disable-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-error-message-vi.html language=enus -->
## TOPIC 00081: niScope Error Message VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-error-message-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-error-message-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Takes the error code returned by NI-SCOPE VIs and returns the interpretation as a user-readable string. VI_NULL can be passed as the instrument handle, which is useful to interpret errors if niScope Initialize has failed. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a

### niScope Error Message VI

Takes the error code returned by NI-SCOPE VIs and returns the interpretation as a
 user-readable string.

VI_NULL can be passed as the instrument handle, which is
 useful to
 interpret errors if [niScope Initialize](niscope-initialize-vi.html) has failed.

[IMAGE alt='icon' src='niscope-error-message-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error code (0) — error code (0) is the status code returned by any NI-SCOPE VI. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error message — error message returns the interpreted error code as a user-readable string. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-export-attribute-configuration-buffer-vi.html language=enus -->
## TOPIC 00082: niScope Export Attribute Configuration Buffer VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-export-attribute-configuration-buffer-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-export-attribute-configuration-buffer-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the attribute configuration of the session to a buffer. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in error in describes error conditions that occur before this node runs. This input provides standard e

### niScope Export Attribute Configuration Buffer VI

Exports the attribute configuration of the session to a buffer.

[IMAGE alt='icon' src='niscope-export-attribute-configuration-buffer-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. buffer — buffer is a byte array that contains the exported attribute configuration. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Device Mapping Behavior**

When exporting and importing configurations between NI‑SCOPE sessions that were both initialized with multiple instruments, the configurations of the exporting instruments are mapped to the importing instruments in the order you specify in the **resource name** input to the [niScope Initialize With Options](niscope-initialize-with-options-vi.html) or [niScope Initialize](niscope-initialize-vi.html) VIs.

For example, if your entry for **resource name** is PXI1Slot1,PXI1Slot2 for the exporting session and PXI2Slot2,PXI2Slot3 for the importing session:

- The configuration exported from PXI1Slot1 is imported into PXI2Slot2.
- The configuration exported from PXI1Slot2 is imported into PXI2Slot3.

Note

Parent topic:

niScope Export Attribute Configuration (Poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-export-attribute-configuration-file-vi.html language=enus -->
## TOPIC 00083: niScope Export Attribute Configuration File VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-export-attribute-configuration-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-export-attribute-configuration-file-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the attribute configuration of the session to the specified file. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cpath.png file path file path is the absolute path to a placeholder file you must create to contain the attribute co

### niScope Export Attribute Configuration File VI

Exports the attribute configuration of the session to the specified file.

[IMAGE alt='icon' src='niscope-export-attribute-configuration-file-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. file path — file path is the absolute path to a placeholder file you must create to contain the attribute configuration you want to export. If you specify an empty or relative path, this VI returns an error. Default file extension: .niscopeconfig error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Device Mapping Behavior**

When exporting and importing configurations between NI‑SCOPE sessions that were both initialized with multiple instruments, the configurations of the exporting instruments are mapped to the importing instruments in the order you specify in the **resource name** input to the [niScope Initialize With Options](niscope-initialize-with-options-vi.html) or [niScope Initialize](niscope-initialize-vi.html) VIs.

For example, if your entry for **resource name** is PXI1Slot1,PXI1Slot2 for the exporting session and PXI2Slot2,PXI2Slot3 for the importing session:

- The configuration exported from PXI1Slot1 is imported into PXI2Slot2.
- The configuration exported from PXI1Slot2 is imported into PXI2Slot3.

Note

Parent topic:

niScope Export Attribute Configuration (Poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-export-attribute-configuration-poly-vi.html language=enus -->
## TOPIC 00084: niScope Export Attribute Configuration (Poly) VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-export-attribute-configuration-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-export-attribute-configuration-poly-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the attribute configuration of a session to either a file or a buffer. You can export and import session attribute configurations only between NI‑SCOPE devices with identical bus types, model numbers, channel counts, and onboard memory sizes and between NI-SCOPE sessions with the same number

### niScope Export Attribute Configuration (Poly) VI

Exports the attribute configuration of a session to either a file or a buffer.

You can export and import session attribute configurations only between NI‑SCOPE devices with identical bus types, model numbers, channel counts, and onboard memory sizes and between NI-SCOPE sessions with the same number of initialized channels.

This VI verifies that the attributes you have configured for the session are valid. If the configuration is invalid, NI‑SCOPE returns an error.

**Related topics:**

[Attributes and Attribute Functions](/csh?context=niscope_digitizers_attributes_and_attribute_functions)

[Setting Attributes Before Reading Attributes](/csh?context=niscope_digitizers_setting_before_reading_attributes)

[IMAGE alt='icon' src='niscope-export-attribute-configuration-poly-vi.png']

#### Details

**Device Mapping Behavior**

When exporting and importing configurations between NI‑SCOPE sessions that were both initialized with multiple instruments, the configurations of the exporting instruments are mapped to the importing instruments in the order you specify in the **resource name** input to the [niScope Initialize With Options](niscope-initialize-with-options-vi.html) or [niScope Initialize](niscope-initialize-vi.html) VIs.

For example, if your entry for **resource name** is PXI1Slot1,PXI1Slot2 for the exporting session and PXI2Slot2,PXI2Slot3 for the importing session:

- The configuration exported from PXI1Slot1 is imported into PXI2Slot2.
- The configuration exported from PXI1Slot2 is imported into PXI2Slot3.

Note

- [niScope Export Attribute Configuration File VI](../../../instr-lib/niscope/niscope-llb/niscope-export-attribute-configuration-file-vi.html) Exports the attribute configuration of the session to the specified file.
- [niScope Export Attribute Configuration Buffer VI](../../../instr-lib/niscope/niscope-llb/niscope-export-attribute-configuration-buffer-vi.html) Exports the attribute configuration of the session to a buffer.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-export-signal-vi.html language=enus -->
## TOPIC 00085: niScope Export Signal VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-export-signal-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-export-signal-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the digitizer to generate a signal that other devices can detect when configured for digital triggering or sharing clocks. The signal parameter specifies what condition causes the digitizer to generate the signal. The output terminal parameter specifies where to send the signal on the har

### niScope Export Signal VI

Configures the digitizer to generate a signal that other devices can detect when configured for digital triggering or sharing clocks. The **signal** parameter specifies what condition causes the digitizer to generate the signal. The **output terminal** parameter specifies where to send the signal on the hardware (such as a PFI connector or RTSI line).

In cases where multiple instances of a particular signal exist, use the signal identifier input to specify which instance to control. For normal events, only one instance exists and you should leave signal identifier set to None. You can call this VI multiple times, and set each line available to a different signal.

To unprogram a specific line on a device, call this VI with the signal you no longer want to export and set **output terminal** to None.

Note

niScope Configure Trigger Output

**Related topics:**

- Triggering
- SMC-Based Digitizers Acquisition Engine State Diagram
- PXI Trigger Lines

[IMAGE alt='icon' src='niscope-export-signal-vi.png']

#### Inputs/Outputs

| signal identifier (None) — signal identifier describes the signal being exported. instrument handle — instrument handle identifies a particular instrument session. signal (Start Trigger) — signal specifies the signal (clock, trigger, or event) to export. Defined Values None (0)—Do not generate a digital pulse. Reference Trigger (1)—Generate a pulse when detecting the stop/reference trigger. Start Trigger (2)—Generate a pulse at the start of the acquisition. End of Acquisition (3)—Generate a pulse at the end of the acquisition. End of Record (4)—Generate a pulse at the end of each record. Record Advance (5)—Generate a pulse when the digitizer is advancing to the next record. Ready for Record Advance (6)—Asserts when the digitizer is ready to advance to the next record. Ready for Start (7)—Asserts when the digitizer is initiated and ready to accept a start trigger to begin sampling. Ready for Reference Trigger (10)—Asserts when the digitizer is ready to accept a reference trigger. Reference Clock (100)—Export the reference clock for the digitizer to the specified terminal. Sample Clock (101)— Export the sample clock for the digitizer to the specified terminal. 5 Volt Power (13)— Export a 5 V power source. output terminal (None) — output terminal identifies the hardware signal line on which the digital pulse is generated. Defined Values None (default) PXI Trigger Line 0/RTSI 0 PXI Trigger Line 1/RTSI 1 PXI Trigger Line 2/RTSI 2 PXI Trigger Line 3/RTSI 3 PXI Trigger Line 4/RTSI 4 PXI Trigger Line 5/RTSI 5 PXI Trigger Line 6/RTSI 6 PXI Trigger Line 7/RTSI 7 (RTSI Clock) PXI Star Trigger PFI 0 PFI 1 PFI 2 PFI 3 PFI 4 PFI 5 PFI 6 PFI 7 Clock Out error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Timing

Parent topic:

Triggering

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-array-measurement-cluster-vi.html language=enus -->
## TOPIC 00086: niScope Fetch Array Measurement Cluster VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-array-measurement-cluster-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-array-measurement-cluster-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains a waveform from the digitizer and returns the specified measurement array for a single channel and record as a cluster along with timing data. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE

### niScope Fetch Array Measurement Cluster VI

Obtains a waveform from the digitizer and returns the specified measurement array for
 a single channel and record as a cluster along with timing data.

[IMAGE alt='icon' src='niscope-fetch-array-measurement-cluster-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. array measurement — array measurement is the array measurement to add as a processing step. Default Value: None Refer to the list of NI-SCOPE Array Measurements for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. meas waveform size — meas waveform size is the maximum number of samples returned in the measurement waveform array for each waveform measurement. Default Value: –1 (returns all available samples) Note Use the property Fetch Meas Num Samples to set the number of samples to fetch when performing a measurement. instrument handle out — instrument handle out has the same value as the instrument handle. meas wfm info — meas wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. meas waveform — meas waveform returns a single record for single channel as a cluster for wiring to a graph, including the timing information. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. measWfm — measWfm returns a one-dimensional array of data for one waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |
| relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. measWfm — measWfm returns a one-dimensional array of data for one waveform. |

Parent topic:

niScope Fetch Measurement (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-array-measurement-vi.html language=enus -->
## TOPIC 00087: niScope Fetch Array Measurement VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-array-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-array-measurement-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains a waveform from the digitizer and returns the specified measurement voltage data for a single channel and record. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currentl

### niScope Fetch Array Measurement VI

Obtains a waveform from the digitizer and returns the specified measurement voltage
 data for a single channel and record.

[IMAGE alt='icon' src='niscope-fetch-array-measurement-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. array measurement — array measurement is the array measurement to add as a processing step. Default Value: None Refer to the list of NI-SCOPE Array Measurements for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. meas waveform size — meas waveform size is the maximum number of samples returned in the measurement waveform array for each waveform measurement. Default Value: –1 (returns all available samples) Note Use the property Fetch Meas Num Samples to set the number of samples to fetch when performing a measurement. instrument handle out — instrument handle out has the same value as the instrument handle. meas wfm info — meas wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. measWfm — measWfm returns a one-dimensional array of data for one waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch Measurement (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-binary-16-vi.html language=enus -->
## TOPIC 00088: niScope Fetch Binary 16 VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-binary-16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-binary-16-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from a single channel and record. Returns a one-dimensional array of binary 16-bit values. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Usi

### niScope Fetch Binary 16 VI

Retrieves data from a single channel and record. Returns a one-dimensional array of
 binary 16-bit values.

[IMAGE alt='icon' src='niscope-fetch-binary-16-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm returns a one-dimensional array of data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-binary-32-vi.html language=enus -->
## TOPIC 00089: niScope Fetch Binary 32 VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-binary-32-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-binary-32-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from a single channel and record. Returns a one-dimensional array of binary 32-bit values. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Usi

### niScope Fetch Binary 32 VI

Retrieves data from a single channel and record. Returns a one-dimensional array of
 binary 32-bit values.

[IMAGE alt='icon' src='niscope-fetch-binary-32-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm returns a one-dimensional array of data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-binary-8-vi.html language=enus -->
## TOPIC 00090: niScope Fetch Binary 8 VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-binary-8-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-binary-8-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from a single channel and record. Returns a one-dimensional array of binary 8-bit values. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Usin

### niScope Fetch Binary 8 VI

Retrieves data from a single channel and record. Returns a one-dimensional array of
 binary 8-bit values.

[IMAGE alt='icon' src='niscope-fetch-binary-8-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm returns a one-dimensional array of data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-cluster-complex-double-vi.html language=enus -->
## TOPIC 00091: niScope Fetch Cluster Complex Double VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-cluster-complex-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-cluster-complex-double-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from single channels and records. Returns a complex, scaled waveform in a cluster that contains timing information. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is

### niScope Fetch Cluster Complex Double VI

Retrieves data from single channels and records. Returns a complex, scaled waveform in
 a cluster that contains timing information.

[IMAGE alt='icon' src='niscope-fetch-cluster-complex-double-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. waveform — waveform is a cluster containing the initial time value, time increment, and a waveform array. The initial time value in the cluster is relative to the trigger. The relative initial time value is the time from the trigger to the first point so the trigger always occurs at time equals zero. t0 — t0 is the initial time value relative to the trigger, such that the trigger always occurs at time equals zero. dt — dt is the time interval between two samples in the waveform. This value is 1/(sampling rate) for time-domain acquisitions. Y — Y is an array of waveform data containing one waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |
| t0 — t0 is the initial time value relative to the trigger, such that the trigger always occurs at time equals zero. dt — dt is the time interval between two samples in the waveform. This value is 1/(sampling rate) for time-domain acquisitions. Y — Y is an array of waveform data containing one waveform. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-cluster-vi.html language=enus -->
## TOPIC 00092: niScope Fetch Cluster VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-cluster-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-cluster-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the waveform the digitizer has acquired for the specified channel from a previously initiated acquisition. Returns scaled voltage waveforms in a cluster that includes timing information. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquir

### niScope Fetch Cluster VI

Retrieves the waveform the digitizer has acquired for the specified channel from a
 previously initiated acquisition. Returns scaled voltage waveforms in a cluster that
 includes timing information.

[IMAGE alt='icon' src='niscope-fetch-cluster-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. waveform — waveform is a cluster containing the initial x value, xIincrement, and a waveform array. This output can be wired directly to the LabVIEW waveform graph, so the waveform is plotted with timing information. The initial x value in the cluster is relative to the trigger. The relative initial x value is the time from the trigger to the first point so the trigger always occurs at time equals zero. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. wfm — wfm is an array of waveform data containing one waveform without any timing information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |
| relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. wfm — wfm is an array of waveform data containing one waveform without any timing information. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-complex-double-vi.html language=enus -->
## TOPIC 00093: niScope Fetch Complex Double VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-complex-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-complex-double-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from single channels and records. Returns a one-dimensional array of complex, scaled waveforms. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available

### niScope Fetch Complex Double VI

Retrieves data from single channels and records. Returns a one-dimensional array of
 complex, scaled waveforms.

[IMAGE alt='icon' src='niscope-fetch-complex-double-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm is an array of waveform data containing one waveform without timing information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-complex-wdt-vi.html language=enus -->
## TOPIC 00094: niScope Fetch Complex WDT VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-complex-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-complex-wdt-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves complex waveforms the digitizer has acquired for the specified channel. Returns a two-dimensional array of LabVIEW complex waveform data types that includes timing information. icon Inputs/Outputs ci32.png timestamp type timestamp Type specifies the time basis for the timestamp on the WDT

### niScope Fetch Complex WDT VI

Retrieves complex waveforms the digitizer has acquired for the specified channel. Returns a two-dimensional array of LabVIEW complex waveform data types that includes timing information.

[IMAGE alt='icon' src='niscope-fetch-complex-wdt-vi.png']

#### Inputs/Outputs

| timestamp type — timestamp Type specifies the time basis for the timestamp on the WDT data. Defined Values absolute relative timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm returns data for wiring to a graph, including the timing information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-measurement-poly-vi.html language=enus -->
## TOPIC 00095: niScope Fetch Measurement (poly) VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-measurement-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-measurement-poly-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains a waveform from the digitizer and returns the specified measurement. Refer to Using Fetch VIs for more information. Many of the measurements use the low, mid, and high reference levels. You configure the low, mid, and high references by using a property with Chan Based Low Ref Level, Chan Ba

### niScope Fetch Measurement (poly) VI

Obtains a waveform from the digitizer and returns the specified measurement.

Refer to [Using Fetch VIs](/csh?context=niscope_digitizers_using_fetch_vis) for more information. 
 Many of the measurements use the low, mid, and high reference levels. 
 You configure the low, mid, and high references by using a property with 
 [Chan Based Low Ref Level](/csh?context=niscope_scopepropref_pniscope_chan.basedlowref),
 [Chan Based Mid Ref Level](/csh?context=niscope_scopepropref_pniscope_chan.basedmidref), 
 and [Chan Based High Ref Level](/csh?context=niscope_scopepropref_pniscope_chanbasedhighref) properties to set each channel differently.

**Related topics**

- Making Waveform Measurements

[IMAGE alt='icon' src='niscope-fetch-measurement-poly-vi.png']

- [niScope Fetch Array Measurement Cluster VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-array-measurement-cluster-vi.html) Obtains a waveform from the digitizer and returns the specified measurement array for a single channel and record as a cluster along with timing data.
- [niScope Fetch Array Measurement VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-array-measurement-vi.html) Obtains a waveform from the digitizer and returns the specified measurement voltage data for a single channel and record.
- [niScope Fetch Measurement Stats VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-measurement-stats-vi.html) Obtains a waveform measurement and returns the measurement value for a single channel and record. Specify a particular measurement type, such as rise time, frequency, or voltage peak-to-peak. The waveform on which the digitizer calculates the waveform measurement is from an acquisition that you previously initiated. The statistics for the specified measurement are also returned, where the statistics are updated once every acquisition when the specified measurement is fetched by any of the Fetch/Read measurement VIs.
- [niScope Fetch Measurement VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-measurement-vi.html) Obtains a waveform from the digitizer and returns the specified measurement voltage data for a single channel and record.
- [niScope Multi Fetch Array Measurement Cluster VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-array-measurement-cluster-vi.html) Obtains a waveform from the digitizer and returns the specified array measurement for multiple channels and records as a cluster.
- [niScope Multi Fetch Array Measurement VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-array-measurement-vi.html) Obtains a waveform from the digitizer and returns the specified measurement voltage data. Unlike the Measurement 1D DBL instance of the niScope Fetch Measurement VI, the Measurement 2D DBL instance can fetch data from multiple channels and records.
- [niScope Multi Fetch Measurement Stats VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-measurement-stats-vi.html) Obtains a waveform measurement and returns the measurement value for multiple channel and multiple record acquisitions.
- [niScope Multi Fetch Measurement VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-measurement-vi.html) Fetches a waveform from the digitizer and performs the specified waveform measurement. Use this function for multiple channel and multiple record acquisitions.

Parent topic:

Measurements

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-measurement-stats-vi.html language=enus -->
## TOPIC 00096: niScope Fetch Measurement Stats VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-measurement-stats-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-measurement-stats-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains a waveform measurement and returns the measurement value for a single channel and record. Specify a particular measurement type, such as rise time, frequency, or voltage peak-to-peak. The waveform on which the digitizer calculates the waveform measurement is from an acquisition that you prev

### niScope Fetch Measurement Stats VI

Obtains a waveform measurement and returns the measurement value for a single channel
 and record. Specify a particular measurement type, such as rise time, frequency, or
 voltage peak-to-peak. The waveform on which the digitizer calculates the waveform
 measurement is from an acquisition that you previously initiated. The statistics for the
 specified measurement are also returned, where the statistics are updated once every
 acquisition when the specified measurement is fetched by any of the Fetch/Read
 measurement VIs.

[IMAGE alt='icon' src='niscope-fetch-measurement-stats-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. scalar measurement — scalar measurement is the measurement to perform on the waveform read from the digitizer. Refer to the list of NI-SCOPE Scalar Measurements for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. stats — stats contains the resulting measurement data. result — result contains the measurement acquired. mean — mean returns the mean scalar value, which is obtained by averaging each niScope Fetch Measurement Stats call. stdev — stdev returns the standard deviation. min — min returns the smallest scalar value acquired. max — max returns the largest scalar value acquired. num in stats — num in stats returns the number of measurements used to calculate the statistics. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| result — result contains the measurement acquired. mean — mean returns the mean scalar value, which is obtained by averaging each niScope Fetch Measurement Stats call. stdev — stdev returns the standard deviation. min — min returns the smallest scalar value acquired. max — max returns the largest scalar value acquired. num in stats — num in stats returns the number of measurements used to calculate the statistics. |

Parent topic:

niScope Fetch Measurement (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-measurement-vi.html language=enus -->
## TOPIC 00097: niScope Fetch Measurement VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-measurement-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains a waveform from the digitizer and returns the specified measurement voltage data for a single channel and record. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currentl

### niScope Fetch Measurement VI

Obtains a waveform from the digitizer and returns the specified measurement voltage
 data for a single channel and record.

[IMAGE alt='icon' src='niscope-fetch-measurement-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. scalar measurement — scalar measurement is the measurement to perform on the waveform read from the digitizer. Refer to the list of NI-SCOPE Scalar Measurements for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. result — result contains the measurement acquired. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Fetch Measurement (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-poly-vi.html language=enus -->
## TOPIC 00098: niScope Fetch (poly) VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-poly-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data that the digitizer has acquired from a previously initiated acquisition. Related topics Fetching Data Acquiring Data Continuously icon

### niScope Fetch (poly) VI

Retrieves data that the digitizer has acquired from a previously initiated
 acquisition.

**Related topics**

- Fetching Data
- Acquiring Data Continuously

[IMAGE alt='icon' src='niscope-fetch-poly-vi.png']

- [niScope Fetch Cluster VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-cluster-vi.html) Retrieves the waveform the digitizer has acquired for the specified channel from a previously initiated acquisition. Returns scaled voltage waveforms in a cluster that includes timing information.
- [niScope Fetch Binary 8 VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-binary-8-vi.html) Retrieves data from a single channel and record. Returns a one-dimensional array of binary 8-bit values.
- [niScope Fetch Binary 16 VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-binary-16-vi.html) Retrieves data from a single channel and record. Returns a one-dimensional array of binary 16-bit values.
- [niScope Fetch Binary 32 VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-binary-32-vi.html) Retrieves data from a single channel and record. Returns a one-dimensional array of binary 32-bit values.
- [niScope Fetch VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-vi.html) Retrieves data from a single channel and record. Returns a one-dimensional array of scaled voltages.
- [niScope Fetch Complex WDT VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-complex-wdt-vi.html) Retrieves complex waveforms the digitizer has acquired for the specified channel. Returns a two-dimensional array of LabVIEW complex waveform data types that includes timing information.
- [niScope Fetch WDT VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-wdt-vi.html) Retrieves a waveform the digitizer has acquired for the specified channel. Returns scaled voltage data in a waveform data type that includes timing information.
- [niScope Fetch Complex Double VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-complex-double-vi.html) Retrieves data from single channels and records. Returns a one-dimensional array of complex, scaled waveforms.
- [niScope Fetch Cluster Complex Double VI](../../../instr-lib/niscope/niscope-llb/niscope-fetch-cluster-complex-double-vi.html) Retrieves data from single channels and records. Returns a complex, scaled waveform in a cluster that contains timing information.
- [niScope Multi Fetch Cluster VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-cluster-vi.html) Retrieves the waveform the digitizer has acquired for multiple channels and records. Returns scaled voltage waveforms in a cluster that includes timing information.
- [niScope Multi Fetch Binary 8 VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-binary-8-vi.html) Retrieves data from multiple channels and records. Returns a two-dimensional array of binary 8-bit waveforms.
- [niScope Multi Fetch Binary 16 VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-binary-16-vi.html) Retrieves data from multiple channels and records. Returns a two-dimensional array of binary 16-bit waveforms.
- [niScope Multi Fetch Binary 32 VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-binary-32-vi.html) Retrieves data from multiple channels and records. Returns a two-dimensional array of binary 32-bit waveforms.
- [niScope Multi Fetch VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-vi.html) Retrieves data from multiple records or multiple channels. Returns a two-dimensional array of scaled voltage waveforms. This VI makes it easy for you to save data to a disk or perform math operations.
- [niScope Multi Fetch Complex WDT VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-complex-wdt-vi.html) Retrieves complex waveforms the digitizer has acquired from multiple records or multiple channels. Returns a two-dimensional array of LabVIEW complex waveform data types that includes timing information.
- [niScope Multi Fetch WDT VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-wdt-vi.html) Retrieves waveforms the digitizer has acquired from multiple records or multiple channels. Returns a two-dimensional array of LabVIEW waveform data types that includes timing information.
- [niScope Multi Fetch Complex Double VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-complex-double-vi.html) Retrieves data from multiple channels and records. Returns a two-dimensional array of complex, scaled waveforms.
- [niScope Multi Fetch Cluster Complex Double VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-fetch-cluster-complex-double-vi.html) Retrieves the waveform the digitizer has acquired for multiple channels and records. Returns a one-dimensional array of complex, scaled waveforms in clusters that include timing information.

Parent topic:

Acquisition

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-vi.html language=enus -->
## TOPIC 00099: niScope Fetch VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from a single channel and record. Returns a one-dimensional array of scaled voltages. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1

### niScope Fetch VI

Retrieves data from a single channel and record. Returns a one-dimensional array of
 scaled voltages.

[IMAGE alt='icon' src='niscope-fetch-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm is an array of waveform data containing one waveform without any timing information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-fetch-wdt-vi.html language=enus -->
## TOPIC 00100: niScope Fetch WDT VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-fetch-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-fetch-wdt-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves a waveform the digitizer has acquired for the specified channel. Returns scaled voltage data in a waveform data type that includes timing information. icon Inputs/Outputs ci32.png timestamp type timestamp Type specifies the time basis for the timestamp on the WDT data. Defined Values absol

### niScope Fetch WDT VI

Retrieves a waveform the digitizer has acquired for the specified channel. Returns
 scaled voltage data in a waveform data type that includes timing information.

[IMAGE alt='icon' src='niscope-fetch-wdt-vi.png']

#### Inputs/Outputs

| timestamp type — timestamp Type specifies the time basis for the timestamp on the WDT data. Defined Values absolute relative timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm returns data for wiring to a graph, including the timing information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-get-channel-name-from-string-vi.html language=enus -->
## TOPIC 00101: niScope Get Channel Name From String VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-get-channel-name-from-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-get-channel-name-from-string-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a comma-separated list of channel names from a string index list. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png index index specifies an index list for the channels in the session. Valid values are from zero to the tota

### niScope Get Channel Name From String VI

Returns a comma-separated list of channel names from a string index list.

[IMAGE alt='icon' src='niscope-get-channel-name-from-string-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. index — index specifies an index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats: A comma-separated list - for example, "0,2,3,1" A range using a hyphen - for example, "0-3" A range using a colon - for example, "0:3" You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indicies are supported ("2,3,0", "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incremeting or decrementing. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. channel name — channel name returns a string of the channel name(s). error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Get Channel Name (Poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-get-channel-name-poly-vi.html language=enus -->
## TOPIC 00102: niScope Get Channel Name (Poly) VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-get-channel-name-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-get-channel-name-poly-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a comma-delimited list of channel names. icon

### niScope Get Channel Name (Poly) VI

Returns a comma-delimited list of channel names.

[IMAGE alt='icon' src='niscope-get-channel-name-poly-vi.png']

- [niScope Get Channel Name VI](../../../instr-lib/niscope/niscope-llb/niscope-get-channel-name-vi.html) Returns the channel name(s) from a one-based index.
- [niScope Get Channel Name From String VI](../../../instr-lib/niscope/niscope-llb/niscope-get-channel-name-from-string-vi.html) Returns a comma-separated list of channel names from a string index list.

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-get-channel-name-vi.html language=enus -->
## TOPIC 00103: niScope Get Channel Name VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-get-channel-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-get-channel-name-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the channel name(s) from a one-based index. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. ci32.png index index specifies a one-based index for the desired channel in the session. Valid values are from one to the total number of

### niScope Get Channel Name VI

Returns the channel name(s) from a one-based index.

[IMAGE alt='icon' src='niscope-get-channel-name-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. index — index specifies a one-based index for the desired channel in the session. Valid values are from one to the total number of channels in the session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. channel name — channel name returns a string of the channel name(s). error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Get Channel Name (Poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-get-equalization-filter-coefficients-vi.html language=enus -->
## TOPIC 00104: niScope Get Equalization Filter Coefficients VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-get-equalization-filter-coefficients-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-get-equalization-filter-coefficients-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the custom coefficients for the equalization FIR filter on the device. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the device. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be

### niScope Get Equalization Filter Coefficients VI

Retrieves the custom coefficients for the equalization FIR filter on the device.

This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the device. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and -1.

Note

[IMAGE alt='icon' src='niscope-get-equalization-filter-coefficients-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. coefficients — coefficients are the custom coefficients for the equalization FIR filter on the device. These coefficients should be between +1 and –1. You can obtain the number of coefficients from the Equalization Num Coefficients property. The Equalization Filter Enabled property must be set to TRUE to enable the filter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Onboard Signal Processing

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-get-frequency-response-vi.html language=enus -->
## TOPIC 00105: niScope Get Frequency Response VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-get-frequency-response-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-get-frequency-response-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency response of the digitizer for the current configurations of the channel attributes. This VI can be used only with high-speed digitizers that support onboard signal processing (OSP). icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrumen

### niScope Get Frequency Response VI

Gets the frequency response of the digitizer for the current configurations of the channel attributes. This VI can be used only with high-speed digitizers that support onboard signal processing (OSP).

[IMAGE alt='icon' src='niscope-get-frequency-response-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. frequencies — frequencies is an array of frequencies that corresponds with the amplitude and phase response of the device. magnitudes — magnitudes is the array of magnitudes that correspond with the magnitude response of the device. phases — phases is the array of phases that correspond with the phase response of the device. error out — error out contains error information. This output provides standard error out functionality. numberOfFrequencies — numberOfFrequencies returns the number of frequencies in the returned spectrum. |
| --- |

Parent topic:

Configure Onboard Signal Processing

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-get-normalization-coefficients-vi.html language=enus -->
## TOPIC 00106: niScope Get Normalization Coefficients VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-get-normalization-coefficients-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-get-normalization-coefficients-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns coefficients that can be used to convert binary data to normalized and calibrated data. Refer to Scaling and Normalization of Binary Data for more information. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png channels chan

### niScope Get Normalization Coefficients VI

Returns coefficients that can be used to convert binary data to normalized and calibrated data.

Refer to [Scaling and Normalization of Binary Data](/csh?context=niscope_digitizers_scaling_and_norm_binary_data) for more information.

[IMAGE alt='icon' src='niscope-get-normalization-coefficients-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. coefficient info — coefficient info is an array of structures containing gain and offset coefficients for a given channel. offset — offset is the offset factor of the given channel. Use for normalizing binary data with the following formula: normalized binary data = raw binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for normalizing binary data with the following formula: normalized binary data = raw binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| offset — offset is the offset factor of the given channel. Use for normalizing binary data with the following formula: normalized binary data = raw binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for normalizing binary data with the following formula: normalized binary data = raw binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Get Wfm Coefficients (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-get-scaling-coefficients-vi.html language=enus -->
## TOPIC 00107: niScope Get Scaling Coefficients VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-get-scaling-coefficients-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-get-scaling-coefficients-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns coefficients that can be used to scale binary data to volts. Refer to Scaling and Normalization of Binary Data for more information. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png channels channels specifies the channel(

### niScope Get Scaling Coefficients VI

Returns coefficients that can be used to scale binary data to volts.

Refer to [Scaling and Normalization of Binary Data](/csh?context=niscope_digitizers_scaling_and_norm_binary_data) for more information.

[IMAGE alt='icon' src='niscope-get-scaling-coefficients-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. coefficient info — coefficient info is an array of structures containing gain and offset coefficients for a given channel. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Get Wfm Coefficients (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-get-session-reference-vi.html language=enus -->
## TOPIC 00108: niScope Get Session Reference VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-get-session-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-get-session-reference-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts a session that can be passed to NI-TClk VIs. Session References are of generic type, which means that the corresponding wires are blue-green, unlike the wires for regular instrument driver sessions. Related topics: NI-TClk Overview icon Inputs/Outputs civrn.png instrument handle instrument

### niScope Get Session Reference VI

Extracts a session that can be passed to NI-TClk VIs. Session References are of
 generic type, which means that the corresponding wires are blue-green, unlike the wires
 for regular instrument driver sessions.

**Related topics:**

- NI-TClk Overview

[IMAGE alt='icon' src='niscope-get-session-reference-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. session reference — session reference references the device session that can be passed to NI-TClk VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-get-stream-endpoint-handle-vi.html language=enus -->
## TOPIC 00109: niScope Get Stream Endpoint Handle VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-get-stream-endpoint-handle-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-get-stream-endpoint-handle-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a writer endpoint that can be used with NI-P2P to configure a peer-to-peer stream with a digitizer endpoint. Related topics: Peer-to-Peer Streaming icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png stream endpoint stream en

### niScope Get Stream Endpoint Handle VI

Returns a writer endpoint that can be used with NI-P2P to configure a peer-to-peer stream with a digitizer endpoint.

**Related topics:**

- Peer-to-Peer Streaming

[IMAGE alt='icon' src='niscope-get-stream-endpoint-handle-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. stream endpoint — stream endpoint is the stream endpoint FIFO to configure. Refer to the device-specific documentation for peer-to-peer streaming in the High-Speed Digitizers Help for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. writer handle — writer handle is a reference to a peer-to-peer writer FIFO that can be used to create a peer-to-peer streaming session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-get-wfm-coefficients-poly-vi.html language=enus -->
## TOPIC 00110: niScope Get Wfm Coefficients (poly) VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-get-wfm-coefficients-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-get-wfm-coefficients-poly-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns coefficients that can be used to scale or normalize binary waveform data. icon

### niScope Get Wfm Coefficients (poly) VI

Returns coefficients that can be used to scale or normalize binary waveform data.

[IMAGE alt='icon' src='niscope-get-wfm-coefficients-poly-vi.png']

- [niScope Get Scaling Coefficients VI](../../../instr-lib/niscope/niscope-llb/niscope-get-scaling-coefficients-vi.html) Returns coefficients that can be used to scale binary data to volts.
- [niScope Get Normalization Coefficients VI](../../../instr-lib/niscope/niscope-llb/niscope-get-normalization-coefficients-vi.html) Returns coefficients that can be used to convert binary data to normalized and calibrated data.

Parent topic:

Acquisition

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-import-attribute-configuration-buffer-vi.html language=enus -->
## TOPIC 00111: niScope Import Attribute Configuration Buffer VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-import-attribute-configuration-buffer-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-import-attribute-configuration-buffer-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports an attribute configuration to the session from the specified buffer. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. c1du8.png buffer buffer is a byte array that contains the attribute configuration to import. cerrcodeclst.png err

### niScope Import Attribute Configuration Buffer VI

Imports an attribute configuration to the session from the specified buffer.

[IMAGE alt='icon' src='niscope-import-attribute-configuration-buffer-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. buffer — buffer is a byte array that contains the attribute configuration to import. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Device Mapping Behavior**

When exporting and importing configurations between NI‑SCOPE sessions that were both initialized with multiple instruments, the configurations of the exporting instruments are mapped to the importing instruments in the order you specify in the **resource name** input to the [niScope Initialize With Options](niscope-initialize-with-options-vi.html) or [niScope Initialize](niscope-initialize-vi.html) VIs.

For example, if your entry for **resource name** is PXI1Slot1,PXI1Slot2 for the exporting session and PXI2Slot2,PXI2Slot3 for the importing session:

- The configuration exported from PXI1Slot1 is imported into PXI2Slot2.
- The configuration exported from PXI1Slot2 is imported into PXI2Slot3.

Note

Parent topic:

niScope Import Attribute Configuration (Poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-import-attribute-configuration-file-vi.html language=enus -->
## TOPIC 00112: niScope Import Attribute Configuration File VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-import-attribute-configuration-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-import-attribute-configuration-file-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports an attribute configuration to the session from the specified file. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cpath.png file path file path is the absolute path to the file that contains the attribute configuration to import.

### niScope Import Attribute Configuration File VI

Imports an attribute configuration to the session from the specified file.

[IMAGE alt='icon' src='niscope-import-attribute-configuration-file-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. file path — file path is the absolute path to the file that contains the attribute configuration to import. If you specify an empty or relative path, this VI returns an error. Default file extension: .niscopeconfig error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

**Device Mapping Behavior**

When exporting and importing configurations between NI‑SCOPE sessions that were both initialized with multiple instruments, the configurations of the exporting instruments are mapped to the importing instruments in the order you specify in the **resource name** input to the [niScope Initialize With Options](niscope-initialize-with-options-vi.html) or [niScope Initialize](niscope-initialize-vi.html) VIs.

For example, if your entry for **resource name** is PXI1Slot1,PXI1Slot2 for the exporting session and PXI2Slot2,PXI2Slot3 for the importing session:

- The configuration exported from PXI1Slot1 is imported into PXI2Slot2.
- The configuration exported from PXI1Slot2 is imported into PXI2Slot3.

Note

Parent topic:

niScope Import Attribute Configuration (Poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-import-attribute-configuration-poly-vi.html language=enus -->
## TOPIC 00113: niScope Import Attribute Configuration (Poly) VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-import-attribute-configuration-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-import-attribute-configuration-poly-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports an attribute configuration to the session from either a file or a buffer. You can export and import session attribute configurations only between NI‑SCOPE devices with identical bus types, model numbers, channel counts, and onboard memory sizes and between NI-SCOPE sessions with the same num

### niScope Import Attribute Configuration (Poly) VI

Imports an attribute configuration to the session from either a file or a buffer.

You can export and import session attribute configurations only between NI‑SCOPE devices with identical bus types, model numbers, channel counts, and onboard memory sizes and between NI-SCOPE sessions with the same number of initialized channels.

Note

**Related topics:**

[Attributes and Attribute Functions](/csh?context=niscope_digitizers_attributes_and_attribute_functions)

[Setting Attributes Before Reading Attributes](/csh?context=niscope_digitizers_setting_before_reading_attributes)

[IMAGE alt='icon' src='niscope-import-attribute-configuration-poly-vi.png']

#### Details

**Device Mapping Behavior**

When exporting and importing configurations between NI‑SCOPE sessions that were both initialized with multiple instruments, the configurations of the exporting instruments are mapped to the importing instruments in the order you specify in the **resource name** input to the [niScope Initialize With Options](niscope-initialize-with-options-vi.html) or [niScope Initialize](niscope-initialize-vi.html) VIs.

For example, if your entry for **resource name** is PXI1Slot1,PXI1Slot2 for the exporting session and PXI2Slot2,PXI2Slot3 for the importing session:

- The configuration exported from PXI1Slot1 is imported into PXI2Slot2.
- The configuration exported from PXI1Slot2 is imported into PXI2Slot3.

Note

- [niScope Import Attribute Configuration File VI](../../../instr-lib/niscope/niscope-llb/niscope-import-attribute-configuration-file-vi.html) Imports an attribute configuration to the session from the specified file.
- [niScope Import Attribute Configuration Buffer VI](../../../instr-lib/niscope/niscope-llb/niscope-import-attribute-configuration-buffer-vi.html) Imports an attribute configuration to the session from the specified buffer.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-initialize-for-grpc-session-vi.html language=enus -->
## TOPIC 00114: niScope Initialize for gRPC Session VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-initialize-for-grpc-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-initialize-for-grpc-session-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new NI-SCOPE session on the specified NI gRPC Device Server using the specified instrument and options. This VI initializes a NI-SCOPE session on the specified NI gRPC Device Server and attaches to it from LabVIEW. If the session name is specified in the gRPC options and the same sessi

### niScope Initialize for gRPC Session VI

Initializes a new NI-SCOPE session on the specified NI gRPC Device Server using the specified instrument and options.

This VI initializes a NI-SCOPE session on the specified NI gRPC Device Server and attaches to it from LabVIEW. If the session name is specified in the gRPC options and the same session name previously exists on the server, then NI-SCOPE will return an error. If the session name in the gRPC options is empty, the resource name will be used as a session name.

The resulting session in LabVIEW forwards driver calls to the corresponding session on the server.

[IMAGE alt='icon' src='niscope-initialize-for-grpc-session-vi.png']

#### Inputs/Outputs

| gRPC options — gRPC options specifies the information used to connect to the server. session name — session name specifies the name of the MeasurementLink gRPC session. address (localhost) — address (localhost) specifies the address of the NI gRPC Device Server. port (31763) — port (31763) specifies the port that the NI gRPC Device Server monitors for connections. resource name — resource name specifies the device name assigned by Measurement & Automation Explorer (MAX) to an NI-SCOPE instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot3,PXI1Slot4, where PXI1Slot3 is one instrument resource name and PXI1Slot4 is another. Note You can only specify multiple instruments of identical model numbers, bus types, channel counts, and onboard memory sizes. The instruments must be in the same chassis. Examples Example Device Type Syntax 1 NI-DAQmx device myDAQmxDevice (myDAQmxDevice = device name) 2 NI-DAQmx device DAQ::myDAQmxDevice (myDAQmxDevice = device name) 3 NI-DAQmx device DAQ::2 (2 = device name) 4 IVI logical name or IVI virtual name myLogicalName (myLogicalName = name) For NI-DAQmx devices, the syntax is just the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by right-clicking on the name in MAX and entering a new name. An alternative syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx device name, as shown in Example 2. This naming convention allows for the use of an NI-DAQmx device in an application that was originally designed for a Traditional NI-DAQ device. For example, if the application expects DAQ::1, you can rename the NI-DAQmx device to 1 in MAX and pass in DAQ::1 for the resource name, as shown in Example 3. You can also pass in the name of an IVI logical name or an IVI virtual name configured with the IVI Configuration utility, as shown in Example 4. A logical name identifies a particular virtual instrument. A virtual name identifies a specific device and specifies the initial settings for the session. Note NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must make sure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. option string — option string sets the initial value of certain properties for the session. The following table lists the properties and the name you use in this parameter to identify the property. Name Attribute Defined Constant Default Value RangeCheck niScope»Inherent IVI Settings»User Options»Range Check TRUE Cache niScope»Inherent IVI Settings»User Options»Cache TRUE Simulate niScope»Inherent IVI Settings»User Options»Simulate FALSE RecordCoercions niScope»Inherent IVI Settings»User Options»Record Value Coercions FALSE QueryInstrStatus niScope»Inherent IVI Settings»User Options»Query Instrument Status TRUE Default Values: "Simulate=0,RangeCheck=1,Cache=1" You can use the DriverSetup flag to simulate a device, attach an accessory to your device session, or load a bitfile to a device FPGA. To simulate a device, specify the model and board type you wish to simulate. For example, Simulate = 1, DriverSetup = Model:5122; BoardType:PXI will simulate a NI 5122. To attach an accessory to your device session, specify the name given to the accessory by MAX. For example, DriverSetup = Accessory:Dev1 will attach the accessory named "Dev1" in MAX to your device session. For instructions on how to load a bitfile to a device FPGA, refer to Using NI-SCOPE Instrument Driver FPGA Extensions. For more information about simulation, refer to the niScope EX Simulated Acquisition example. To see this parameter used in a VI, refer to the niScope EX External Amplifier example. reset device — reset device specifies whether to reset the instrument during the initialization procedure. Default Value: FALSE error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle — instrument handle identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |  |
| --- | --- | --- |
| session name — session name specifies the name of the MeasurementLink gRPC session. address (localhost) — address (localhost) specifies the address of the NI gRPC Device Server. port (31763) — port (31763) specifies the port that the NI gRPC Device Server monitors for connections. |  |  |
| Example | Device Type | Syntax |
| 1 | NI-DAQmx device | myDAQmxDevice (myDAQmxDevice = device name) |
| 2 | NI-DAQmx device | DAQ::myDAQmxDevice (myDAQmxDevice = device name) |
| 3 | NI-DAQmx device | DAQ::2 (2 = device name) |
| 4 | IVI logical name or IVI virtual name | myLogicalName (myLogicalName = name) |
| Name | Attribute Defined Constant | Default Value |
| RangeCheck | niScope»Inherent IVI Settings»User Options»Range Check | TRUE |
| Cache | niScope»Inherent IVI Settings»User Options»Cache | TRUE |
| Simulate | niScope»Inherent IVI Settings»User Options»Simulate | FALSE |
| RecordCoercions | niScope»Inherent IVI Settings»User Options»Record Value Coercions | FALSE |
| QueryInstrStatus | niScope»Inherent IVI Settings»User Options»Query Instrument Status | TRUE |

Parent topic:

MeasurementLink

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-initialize-vi.html language=enus -->
## TOPIC 00115: niScope Initialize VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-initialize-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-initialize-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the following initialization actions: -Creates a new IVI instrument driver session. -Opens a session to the device(s) that you specify in the resource name parameter. -Queries each instrument ID and verifies that it is valid for this instrument driver. -Resets the instrument(s) to a known s

### niScope Initialize VI

Performs the following initialization actions:

-Creates a new IVI instrument driver session.

-Opens a session to the device(s) that you specify in the resource name parameter.

-Queries each instrument ID and verifies that it is valid for this instrument driver.

-Resets the instrument(s) to a known state if the reset device parameter is set to TRUE; refer to niScope Reset for the default state of each digitizer.

-Sends initialization commands to set the instrument(s) to the state necessary for the operation of the instrument driver.

-Returns an instrument handle that you use to identify the instrument(s) in all subsequent instrument driver VI calls.

You can create sessions that include multiple instruments of the same model and in the same chassis. This automatically synchronizes all channels of the included instruments, simplifying your test program development and maintenance.

**Related topics**

- NI-SCOPE Programming Flow
- NI-SCOPE Tutorial

[IMAGE alt='icon' src='niscope-initialize-vi.png']

#### Inputs/Outputs

| resource name — resource name specifies the device name assigned by Measurement & Automation Explorer (MAX) to an NI-SCOPE instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot3,PXI1Slot4, where PXI1Slot3 is one instrument resource name and PXI1Slot4 is another. Note You can only specify multiple instruments of identical model numbers, bus types, channel counts, and onboard memory sizes. The instruments must be in the same chassis. Examples Example Device Type Syntax 1 NI-DAQmx device myDAQmxDevice (myDAQmxDevice = device name) 2 NI-DAQmx device DAQ::myDAQmxDevice (myDAQmxDevice = device name) 3 NI-DAQmx device DAQ::2 (2 = device name) 4 IVI logical name or IVI virtual name myLogicalName (myLogicalName = name) For NI-DAQmx devices, the syntax is just the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by right-clicking on the name in MAX and entering a new name. An alternative syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx device name, as shown in Example 2. This naming convention allows for the use of an NI-DAQmx device in an application that was originally designed for a Traditional NI-DAQ device. For example, if the application expects DAQ::1, you can rename the NI-DAQmx device to 1 in MAX and pass in DAQ::1 for the resource name, as shown in Example 3. You can also pass in the name of an IVI logical name or an IVI virtual name configured with the IVI Configuration utility, as shown in Example 4. A logical name identifies a particular virtual instrument. A virtual name identifies a specific device and specifies the initial settings for the session. Note NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must make sure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. id query — id query verifies that the digitizer you initialize is supported by NI-SCOPE. NI-SCOPE automatically performs this query, so setting this parameter is not necessary. reset device — reset device specifies whether to reset the instrument during the initialization procedure. Default Value: TRUE error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle — instrument handle identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |  |
| --- | --- | --- |
| Example | Device Type | Syntax |
| 1 | NI-DAQmx device | myDAQmxDevice (myDAQmxDevice = device name) |
| 2 | NI-DAQmx device | DAQ::myDAQmxDevice (myDAQmxDevice = device name) |
| 3 | NI-DAQmx device | DAQ::2 (2 = device name) |
| 4 | IVI logical name or IVI virtual name | myLogicalName (myLogicalName = name) |

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-initialize-with-options-vi.html language=enus -->
## TOPIC 00116: niScope Initialize With Options VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-initialize-with-options-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-initialize-with-options-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the following initialization actions: -Creates a new IVI instrument driver session and optionally sets the initial state of the following session properties: Range Check, Cache, Simulate, Record Value Coercions. -Opens a session to the device(s) that you specify in the resource name paramet

### niScope Initialize With Options VI

Performs the following initialization actions:

-Creates a new IVI instrument driver session and optionally sets the initial state of the following session properties: Range Check, Cache, Simulate, Record Value Coercions.

-Opens a session to the device(s) that you specify in the resource name parameter.

-Queries each instrument ID and verifies that it is valid for this instrument driver.

-Resets the instrument(s) to a known state if the reset device parameter is set to TRUE; refer to niScope Reset for the default state of each digitizer.

-Returns an instrument handle that you use to identify the instrument(s) in all subsequent instrument driver VI calls.

You can create sessions that include multiple instruments of the same model and in the same chassis. This automatically synchronizes all channels of the included instruments, simplifying your test program development and maintenance.

**Related topics**

- NI-SCOPE Programming Flow
- NI-SCOPE Tutorial

[IMAGE alt='icon' src='niscope-initialize-with-options-vi.png']

#### Inputs/Outputs

| resource name — resource name specifies the device name assigned by Measurement & Automation Explorer (MAX) to an NI-SCOPE instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot3,PXI1Slot4, where PXI1Slot3 is one instrument resource name and PXI1Slot4 is another. Note You can only specify multiple instruments of identical model numbers, bus types, channel counts, and onboard memory sizes. The instruments must be in the same chassis. Examples Example Device Type Syntax 1 NI-DAQmx device myDAQmxDevice (myDAQmxDevice = device name) 2 NI-DAQmx device DAQ::myDAQmxDevice (myDAQmxDevice = device name) 3 NI-DAQmx device DAQ::2 (2 = device name) 4 IVI logical name or IVI virtual name myLogicalName (myLogicalName = name) For NI-DAQmx devices, the syntax is just the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by right-clicking on the name in MAX and entering a new name. An alternative syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx device name, as shown in Example 2. This naming convention allows for the use of an NI-DAQmx device in an application that was originally designed for a Traditional NI-DAQ device. For example, if the application expects DAQ::1, you can rename the NI-DAQmx device to 1 in MAX and pass in DAQ::1 for the resource name, as shown in Example 3. You can also pass in the name of an IVI logical name or an IVI virtual name configured with the IVI Configuration utility, as shown in Example 4. A logical name identifies a particular virtual instrument. A virtual name identifies a specific device and specifies the initial settings for the session. Note NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must make sure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. id query — id query verifies that the digitizer you initialize is supported by NI-SCOPE. NI-SCOPE automatically performs this query, so setting this parameter is not necessary. option string — option string sets the initial value of certain properties for the session. The following table lists the properties and the name you use in this parameter to identify the property. Name Attribute Defined Constant Default Value RangeCheck niScope»Inherent IVI Settings»User Options»Range Check TRUE Cache niScope»Inherent IVI Settings»User Options»Cache TRUE Simulate niScope»Inherent IVI Settings»User Options»Simulate FALSE RecordCoercions niScope»Inherent IVI Settings»User Options»Record Value Coercions FALSE QueryInstrStatus niScope»Inherent IVI Settings»User Options»Query Instrument Status TRUE Default Values: "Simulate=0,RangeCheck=1,Cache=1" You can use the DriverSetup flag to simulate a device, attach an accessory to your device session, or load a bitfile to a device FPGA. To simulate a device, specify the model and board type you wish to simulate. For example, Simulate = 1, DriverSetup = Model:5122; BoardType:PXI will simulate a NI 5122. To attach an accessory to your device session, specify the name given to the accessory by MAX. For example, DriverSetup = Accessory:Dev1 will attach the accessory named "Dev1" in MAX to your device session. For instructions on how to load a bitfile to a device FPGA, refer to Using NI-SCOPE Instrument Driver FPGA Extensions. For more information about simulation, refer to the niScope EX Simulated Acquisition example. To see this parameter used in a VI, refer to the niScope EX External Amplifier example. reset device — reset device specifies whether to reset the instrument during the initialization procedure. Default Value: TRUE error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle — instrument handle identifies a particular instrument session. error out — error out contains error information. This output provides standard error out functionality. |  |  |
| --- | --- | --- |
| Example | Device Type | Syntax |
| 1 | NI-DAQmx device | myDAQmxDevice (myDAQmxDevice = device name) |
| 2 | NI-DAQmx device | DAQ::myDAQmxDevice (myDAQmxDevice = device name) |
| 3 | NI-DAQmx device | DAQ::2 (2 = device name) |
| 4 | IVI logical name or IVI virtual name | myLogicalName (myLogicalName = name) |
| Name | Attribute Defined Constant | Default Value |
| RangeCheck | niScope»Inherent IVI Settings»User Options»Range Check | TRUE |
| Cache | niScope»Inherent IVI Settings»User Options»Cache | TRUE |
| Simulate | niScope»Inherent IVI Settings»User Options»Simulate | FALSE |
| RecordCoercions | niScope»Inherent IVI Settings»User Options»Record Value Coercions | FALSE |
| QueryInstrStatus | niScope»Inherent IVI Settings»User Options»Query Instrument Status | TRUE |

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-initiate-acquisition-vi.html language=enus -->
## TOPIC 00117: niScope Initiate Acquisition VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-initiate-acquisition-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-initiate-acquisition-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates a waveform acquisition. After you call this VI, the digitizer leaves the Idle state and waits for a trigger. The digitizer acquires a waveform for each channel you enable with niScope Configure Vertical. Related topics SMC-Based Digitizers Acquisition Engine State Diagram NI-SCOPE Programm

### niScope Initiate Acquisition VI

Initiates a waveform acquisition.

After you call this VI, the digitizer leaves the Idle state and waits for a trigger.
 The digitizer acquires a waveform for each channel you enable with [niScope Configure Vertical](niscope-configure-vertical-vi.html).

**Related topics**

- SMC-Based Digitizers Acquisition Engine State Diagram
- NI-SCOPE Programming Flow

[IMAGE alt='icon' src='niscope-initiate-acquisition-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Acquisition

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-is-device-ready-vi.html language=enus -->
## TOPIC 00118: niScope Is Device Ready VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-is-device-ready-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-is-device-ready-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the device is ready to be used to the Device Ready? parameter. Related topics SMC-Based Digitizers Acquisition Engine State Diagram icon Inputs/Outputs civrn.png resource name resource name specifies the device name assigned by Measurement & Automation Explorer (MAX). Examples Exampl

### niScope Is Device Ready VI

Returns whether the device is ready to be used to the **Device Ready?** parameter.

**Related topics**

- SMC-Based Digitizers Acquisition Engine State Diagram

[IMAGE alt='icon' src='niscope-is-device-ready-vi.png']

#### Inputs/Outputs

| resource name — resource name specifies the device name assigned by Measurement & Automation Explorer (MAX). Examples Example Device Type Syntax 1 NI-DAQmx device myDAQmxDevice (myDAQmxDevice = device name) 2 NI-DAQmx device DAQ::myDAQmxDevice (myDAQmxDevice = device name) 3 NI-DAQmx device DAQ::2 (2 = device name) 4 IVI logical name or IVI virtual name myLogicalName (myLogicalName = name) For NI-DAQmx devices, the syntax is just the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by right-clicking on the name in MAX and entering a new name. An alternative syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx device name, as shown in Example 2. This naming convention allows for the use of an NI-DAQmx device in an application that was originally designed for a Traditional NI-DAQ device. For example, if the application expects DAQ::1, you can rename the NI-DAQmx device to 1 in MAX and pass in DAQ::1 for the resource name, as shown in Example 3. You can also pass in the name of an IVI logical name or an IVI virtual name configured with the IVI Configuration utility, as shown in Example 4. A logical name identifies a particular virtual instrument. A virtual name identifies a specific device and specifies the initial settings for the session. Note NI-DAQmx device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use logical names, driver session names, or virtual names in your program, you must make sure that the name you use matches the name in the IVI Configuration Store file exactly, without any variations in the case of the characters. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ready? — Device Ready? Returns whether the device is ready to use. Default Value: None error out — error out contains error information. This output provides standard error out functionality. |  |  |
| --- | --- | --- |
| Example | Device Type | Syntax |
| 1 | NI-DAQmx device | myDAQmxDevice (myDAQmxDevice = device name) |
| 2 | NI-DAQmx device | DAQ::myDAQmxDevice (myDAQmxDevice = device name) |
| 3 | NI-DAQmx device | DAQ::2 (2 = device name) |
| 4 | IVI logical name or IVI virtual name | myLogicalName (myLogicalName = name) |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-array-measurement-cluster-vi.html language=enus -->
## TOPIC 00119: niScope Multi Fetch Array Measurement Cluster VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-array-measurement-cluster-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-array-measurement-cluster-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains a waveform from the digitizer and returns the specified array measurement for multiple channels and records as a cluster. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is

### niScope Multi Fetch Array Measurement Cluster VI

Obtains a waveform from the digitizer and returns the specified array measurement for
 multiple channels and records as a cluster.

[IMAGE alt='icon' src='niscope-multi-fetch-array-measurement-cluster-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. array measurement — array measurement is the array measurement to add as a processing step. Default Value: None Refer to the list of NI-SCOPE Array Measurements for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. meas waveform size — meas waveform size is the maximum number of samples returned in the measurement waveform array for each waveform measurement. Default Value: –1 (returns all available samples) Note Use the property Fetch Meas Num Samples to set the number of samples to fetch when performing a measurement. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. meas waveform — meas waveform returns an array of clusters for wiring to a graph, including the timing information. If you specify a channel list, NI-SCOPE returns the waveforms in the list order. NI-SCOPE returns these records sequentially, so all record 0 waveforms are first. For example, with a two-channel list, you would have the following index values: index 0 = record 0, channel 0 index 1 = record 0, channel 1 index 2 = record 1, channel 0 index 3 = record 1, channel 1 relativeInitialX — relativeInitialX is the initial x value relative to the trigger, such that the trigger always occurs at time equals zero. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. measWfm — measWfm returns a one-dimensional array of data for one waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |
| relativeInitialX — relativeInitialX is the initial x value relative to the trigger, such that the trigger always occurs at time equals zero. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. measWfm — measWfm returns a one-dimensional array of data for one waveform. |

Parent topic:

niScope Fetch Measurement (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-array-measurement-vi.html language=enus -->
## TOPIC 00120: niScope Multi Fetch Array Measurement VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-array-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-array-measurement-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains a waveform from the digitizer and returns the specified measurement voltage data. Unlike the Measurement 1D DBL instance of the niScope Fetch Measurement VI, the Measurement 2D DBL instance can fetch data from multiple channels and records. icon Inputs/Outputs cdbl.png timeout timeout is the

### niScope Multi Fetch Array Measurement VI

Obtains a waveform from the digitizer and returns the specified measurement voltage
 data. Unlike the Measurement 1D DBL instance of the niScope Fetch Measurement VI, the
 Measurement 2D DBL instance can fetch data from multiple channels and records.

[IMAGE alt='icon' src='niscope-multi-fetch-array-measurement-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. array measurement — array measurement is the array measurement to add as a processing step. Default Value: None Refer to the list of NI-SCOPE Array Measurements for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. meas waveform size — meas waveform size is the maximum number of samples returned in the measurement waveform array for each waveform measurement. Default Value: –1 (returns all available samples) Note Use the property Fetch Meas Num Samples to set the number of samples to fetch when performing a measurement. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm is an array of waveforms; that is, a two-dimensional array. This output can be wired directly to the LabVIEW waveform graph, but each waveform is plotted without timing information. The 2D array includes waveforms from multiple channels, records, and acquisition types. For example, if the acquisition type is normal, there is one waveform per channel per record. If you call the fetch VI during a normal acquisition with the channel string "0,1" and the record number set to –1, the order of the output is: record 0, channel 0 record 0, channel 1 record 1, channel 0 record 1, channel 1 The order of the channels is the order specified by the channels parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch Measurement (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-binary-16-vi.html language=enus -->
## TOPIC 00121: niScope Multi Fetch Binary 16 VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-binary-16-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-binary-16-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from multiple channels and records. Returns a two-dimensional array of binary 16-bit waveforms. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available

### niScope Multi Fetch Binary 16 VI

Retrieves data from multiple channels and records. Returns a two-dimensional array of
 binary 16-bit waveforms.

[IMAGE alt='icon' src='niscope-multi-fetch-binary-16-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm returns a two-dimensional array of binary data; if you specify a channel list, NI-SCOPE returns the waveforms in the list order. NI-SCOPE returns these records sequentially, so all record 0 waveforms are first. For example, with a two-channel list, you would have the following index values: index 0 = record 0, channel 0 index 1 = record 0, channel 1 index 2 = record 1, channel 0 index 3 = record 1, channel 1 error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-binary-32-vi.html language=enus -->
## TOPIC 00122: niScope Multi Fetch Binary 32 VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-binary-32-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-binary-32-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from multiple channels and records. Returns a two-dimensional array of binary 32-bit waveforms. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available

### niScope Multi Fetch Binary 32 VI

Retrieves data from multiple channels and records. Returns a two-dimensional array of
 binary 32-bit waveforms.

[IMAGE alt='icon' src='niscope-multi-fetch-binary-32-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm is an array of clusters. Each waveform in the output array has some corresponding information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-binary-8-vi.html language=enus -->
## TOPIC 00123: niScope Multi Fetch Binary 8 VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-binary-8-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-binary-8-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from multiple channels and records. Returns a two-dimensional array of binary 8-bit waveforms. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available.

### niScope Multi Fetch Binary 8 VI

Retrieves data from multiple channels and records. Returns a two-dimensional array of
 binary 8-bit waveforms.

[IMAGE alt='icon' src='niscope-multi-fetch-binary-8-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm returns a two-dimensional array of binary data; if you specify a channel list, NI-SCOPE returns the waveforms in the list order. NI-SCOPE returns these records sequentially, so all record 0 waveforms are first. For example, with a two-channel list, you would have the following index values: index 0 = record 0, channel 0 index 1 = record 0, channel 1 index 2 = record 1, channel 0 index 3 = record 1, channel 1 error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-cluster-complex-double-vi.html language=enus -->
## TOPIC 00124: niScope Multi Fetch Cluster Complex Double VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-cluster-complex-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-cluster-complex-double-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the waveform the digitizer has acquired for multiple channels and records. Returns a one-dimensional array of complex, scaled waveforms in clusters that include timing information. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Us

### niScope Multi Fetch Cluster Complex Double VI

Retrieves the waveform the digitizer has acquired for multiple channels and records.
 Returns a one-dimensional array of complex, scaled waveforms in clusters that include
 timing information.

[IMAGE alt='icon' src='niscope-multi-fetch-cluster-complex-double-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. waveform — waveform is an array of clusters, each containing the initial time value, time increment, and a waveform array. The initial time value in the cluster is the value relative to the trigger. The relative initial time value is the time from the trigger to the first point so the trigger always occurs at time equals zero. The array of clusters includes waveforms from multiple channels, records, and acquisition types. For example, if the acquisition type is normal there is one waveform per channel per record. If you call the fetch VI during a normal acquisition with the channel string "0,1" the order of the output is: record 0, channel 0, record 0, channel 1, record 1, channel 0, record 1, channel 1, The order of the channels is the order specified by the channels parameter. t0 — t0 is the initial time value relative to the trigger, such that the trigger always occurs at time equals zero. dt — dt is the time interval between two samples in the waveform. This value is 1/(sampling rate) for time-domain acquisitions. Y — Y is an array of waveform data containing one waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |
| t0 — t0 is the initial time value relative to the trigger, such that the trigger always occurs at time equals zero. dt — dt is the time interval between two samples in the waveform. This value is 1/(sampling rate) for time-domain acquisitions. Y — Y is an array of waveform data containing one waveform. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-cluster-vi.html language=enus -->
## TOPIC 00125: niScope Multi Fetch Cluster VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-cluster-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-cluster-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves the waveform the digitizer has acquired for multiple channels and records. Returns scaled voltage waveforms in a cluster that includes timing information. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to

### niScope Multi Fetch Cluster VI

Retrieves the waveform the digitizer has acquired for multiple channels and records.
 Returns scaled voltage waveforms in a cluster that includes timing information.

[IMAGE alt='icon' src='niscope-multi-fetch-cluster-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. waveform — waveform is an array of clusters, each containing the initial x value, x increment, and a waveform array. This output can be wired directly to the LabVIEW waveform graph, so each waveform in the array is plotted with timing information. The initial x value in the cluster is the value relative to the trigger. The relative initial x value is the time from the trigger to the first point so the trigger always occurs at time equals zero. The array of clusters includes waveforms from multiple channels, records, and acquisition types. For example, if the acquisition type is normal there is one waveform per channel per record. If you call the fetch VI during a normal acquisition with the channel string "0,1" the order of the output is: record 0, channel 0 record 0, channel 1 record 1, channel 0 record 1, channel 1 relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. wfm — wfm contains the voltage data (the y-axis data in the graph). error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |
| relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. wfm — wfm contains the voltage data (the y-axis data in the graph). |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-complex-double-vi.html language=enus -->
## TOPIC 00126: niScope Multi Fetch Complex Double VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-complex-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-complex-double-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from multiple channels and records. Returns a two-dimensional array of complex, scaled waveforms. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently availab

### niScope Multi Fetch Complex Double VI

Retrieves data from multiple channels and records. Returns a two-dimensional array of
 complex, scaled waveforms.

[IMAGE alt='icon' src='niscope-multi-fetch-complex-double-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm is an array of waveforms; that is, a two-dimensional array. The 2D array includes waveforms from multiple channels, records, and acquisition types. For example, if the acquisition type is normal, one waveform per channel per record is acquired. If you call the fetch VI during a normal acquisition with the channel string "0,1" and the record number set to –1, the order of the output is: record 0, channel 0, record 0, channel 1, record 1, channel 0, record 1, channel 1 The order of the channels is the order specified by the channels parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-complex-wdt-vi.html language=enus -->
## TOPIC 00127: niScope Multi Fetch Complex WDT VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-complex-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-complex-wdt-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves complex waveforms the digitizer has acquired from multiple records or multiple channels. Returns a two-dimensional array of LabVIEW complex waveform data types that includes timing information. icon Inputs/Outputs ci32.png timestamp type timestamp Type specifies the time basis for the time

### niScope Multi Fetch Complex WDT VI

Retrieves complex waveforms the digitizer has acquired from multiple records or multiple channels. Returns a two-dimensional array of LabVIEW complex waveform data types that includes timing information.

[IMAGE alt='icon' src='niscope-multi-fetch-complex-wdt-vi.png']

#### Inputs/Outputs

| timestamp type — timestamp Type specifies the time basis for the timestamp on the WDT data. Defined Values absolute relative timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm returns a one-dimensional array of LabVIEW waveform data types that contain timing information. If you specify a channel list, NI-SCOPE returns the waveforms in the list order. NI-SCOPE returns these records sequentially, so all record 0 waveforms are first. For example, with a two-channel list, you would have the following index values: index 0 = record 0, channel 0 index 1 = record 0, channel 1 index 2 = record 1, channel 0 index 3 = record 1, channel 1 error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-measurement-stats-vi.html language=enus -->
## TOPIC 00128: niScope Multi Fetch Measurement Stats VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-measurement-stats-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-measurement-stats-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains a waveform measurement and returns the measurement value for multiple channel and multiple record acquisitions. Specify a particular measurement type, such as rise time, frequency, or voltage peak-to-peak. The waveform on which the digitizer calculates the waveform measurement is from an acq

### niScope Multi Fetch Measurement Stats VI

Obtains a waveform measurement and returns the measurement value for multiple channel
 and multiple record acquisitions.

Specify a particular measurement type, such as rise
 time, frequency, or voltage peak-to-peak. The waveform on which the digitizer calculates
 the waveform measurement is from an acquisition that you previously initiated. The
 statistics for the specified measurement are also returned, where the statistics are
 updated once every acquisition when the specified measurement is fetched by any of the
 Fetch/Read waveform measurement VIs.

[IMAGE alt='icon' src='niscope-multi-fetch-measurement-stats-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. scalar measurement — scalar measurement is the measurement to perform on the waveform read from the digitizer. Refer to the list of NI-SCOPE Scalar Measurements for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. stats — stats is an array of clusters with scalar measurement results and statistics. The array of clusters includes waveforms from multiple channels, records, and acquisition types. For example, if the acquisition type is normal there is one waveform per channel per record. If you call the multi fetch measurement VI during a normal acquisition with the channel list "0,1", the order of the results output is: statistics for record 0, channel 0, statistics for record 0, channel 1, statistics for record 1, channel 0, statistics for record 1, channel 1 The order of the channels is the order specified by the channels parameter. scalar result — scalar result contains the measurement. mean — mean returns the mean scalar value, which is obtained by averaging each niScope Multi Fetch Measurement Stats call. stdev — stdev returns the standard deviation. min — min returns the smallest scalar value acquired. max — max returns the largest scalar value acquired. num in stats — num in stats returns the number of measurements used to calculate the statistics. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| scalar result — scalar result contains the measurement. mean — mean returns the mean scalar value, which is obtained by averaging each niScope Multi Fetch Measurement Stats call. stdev — stdev returns the standard deviation. min — min returns the smallest scalar value acquired. max — max returns the largest scalar value acquired. num in stats — num in stats returns the number of measurements used to calculate the statistics. |

Parent topic:

niScope Fetch Measurement (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-measurement-vi.html language=enus -->
## TOPIC 00129: niScope Multi Fetch Measurement VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-measurement-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches a waveform from the digitizer and performs the specified waveform measurement. Use this function for multiple channel and multiple record acquisitions. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell

### niScope Multi Fetch Measurement VI

Fetches a waveform from the digitizer and performs the specified waveform measurement. Use
 this function for multiple channel and multiple record acquisitions.

[IMAGE alt='icon' src='niscope-multi-fetch-measurement-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. scalar measurement — scalar measurement is the measurement to perform on the waveform read from the digitizer. Refer to the list of NI-SCOPE Scalar Measurements for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. results — results contains the measurements acquired as a one-dimensional array; if you specify a channel list, NI-SCOPE returns the waveforms in the list order. NI-SCOPE returns these records sequentially, so all record 0 waveforms are first. For example, with a two-channel list, you would have the following index values: index 0 = record 0, channel 0 index 1 = record 0, channel 1 index 2 = record 1, channel 0 index 3 = record 1, channel 1 error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niScope Fetch Measurement (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-vi.html language=enus -->
## TOPIC 00130: niScope Multi Fetch VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves data from multiple records or multiple channels. Returns a two-dimensional array of scaled voltage waveforms. This VI makes it easy for you to save data to a disk or perform math operations. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be ac

### niScope Multi Fetch VI

Retrieves data from multiple records or multiple channels. Returns a two-dimensional
 array of scaled voltage waveforms. This VI makes it easy for you to save data to a disk
 or perform math operations.

[IMAGE alt='icon' src='niscope-multi-fetch-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm is an array of waveforms; that is, a two-dimensional array. This output can be wired directly to the LabVIEW waveform graph, but each waveform is plotted without timing information. The 2D array includes waveforms from multiple channels, records, and acquisition types. For example, if the acquisition type is normal, there is one waveform per channel per record. If you call the fetch VI during a normal acquisition with the channel string "0,1" and the record number set to –1, the order of the output is: record 0, channel 0 record 0, channel 1 record 1, channel 0 record 1, channel 1 The order of the channels is the order specified by the channels parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-fetch-wdt-vi.html language=enus -->
## TOPIC 00131: niScope Multi Fetch WDT VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-fetch-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-fetch-wdt-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves waveforms the digitizer has acquired from multiple records or multiple channels. Returns a two-dimensional array of LabVIEW waveform data types that includes timing information. icon Inputs/Outputs ci32.png timestamp type timestamp Type specifies the time basis for the timestamp on the WDT

### niScope Multi Fetch WDT VI

Retrieves waveforms the digitizer has acquired from multiple records or multiple channels.
 Returns a two-dimensional array of LabVIEW waveform data types that includes timing information.

[IMAGE alt='icon' src='niscope-multi-fetch-wdt-vi.png']

#### Inputs/Outputs

| timestamp type — timestamp Type specifies the time basis for the timestamp on the WDT data. Defined Values absolute relative timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm returns a one-dimensional array of LabVIEW waveform data types that contain timing information. If you specify a channel list, NI-SCOPE returns the waveforms in the list order. NI-SCOPE returns these records sequentially, so all record 0 waveforms are first. For example, with a two-channel list, you would have the following index values: index 0 = record 0, channel 0 index 1 = record 0, channel 1 index 2 = record 1, channel 0 index 3 = record 1, channel 1 error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Fetch (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-read-cluster-vi.html language=enus -->
## TOPIC 00132: niScope Multi Read Cluster VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-read-cluster-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-read-cluster-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates an acquisition, waits for it to complete, and retrieves the data for multiple channels and records. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available.

### niScope Multi Read Cluster VI

Initiates an acquisition, waits for it to complete, and retrieves the data for
 multiple channels and records.

[IMAGE alt='icon' src='niscope-multi-read-cluster-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. waveform — waveform is an array of clusters, each containing the initial x value, x increment, and a waveform array. This output can be wired directly to the LabVIEW waveform graph, so each waveform in the array is plotted with timing information. The initial x value in the cluster is the value relative to the trigger. The relative initial x value is the time from the trigger to the first point so the trigger always occurs at time equals zero. The array of clusters includes waveforms from multiple channels, records, and acquisition types. For example, if the acquisition type is normal there is one waveform per channel per record. If you call the fetch VI during a normal acquisition with the channel string "0,1" the order of the output is: record 0, channel 0 record 0, channel 1 record 1, channel 0 record 1, channel 1 relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. wfm — wfm is an array of waveform data containing one waveform without any timing information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |
| relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. wfm — wfm is an array of waveform data containing one waveform without any timing information. |

Parent topic:

niScope Read (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-read-measurement-vi.html language=enus -->
## TOPIC 00133: niScope Multi Read Measurement VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-read-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-read-measurement-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates an acquisition, waits for it to complete, and performs the specified waveform measurement for multiple channels and records. Use niScope Read Measurement for a single channel and record. Related topics: Making Waveform Measurements Acquisition Functions icon Inputs/Outputs cdbl.png timeout

### niScope Multi Read Measurement VI

Initiates an acquisition, waits for it to complete, and performs the specified
 waveform measurement for multiple channels and records.

Use [niScope Read Measurement](niscope-read-measurement-vi.html) for a single
 channel and record.

**Related topics:**

- Making Waveform Measurements
- Acquisition Functions

[IMAGE alt='icon' src='niscope-multi-read-measurement-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. scalar measurement — scalar measurement is the measurement to perform on the waveform read from the digitizer. Refer to the list of NI-SCOPE Scalar Measurements for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. results — results contains the measurements acquired as a one-dimensional array; if you specify a channel list, NI-SCOPE returns the waveforms in the list order. NI-SCOPE returns these records sequentially, so all record 0 waveforms are first. For example, with a two-channel list, you would have the following index values: index 0 = record 0, channel 0 index 1 = record 0, channel 1 index 2 = record 1, channel 0 index 3 = record 1, channel 1 error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Measurements

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-multi-read-wdt-vi.html language=enus -->
## TOPIC 00134: niScope Multi Read WDT VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-multi-read-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-multi-read-wdt-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates an acquisition and returns a one-dimensional array of LabVIEW waveform data types that includes timing information. This VI is only supported in LabVIEW 7.0 or later. icon Inputs/Outputs ci32.png timestamp type timestamp Type specifies the time basis for the timestamp on the WDT data. Defi

### niScope Multi Read WDT VI

Initiates an acquisition and returns a one-dimensional array of LabVIEW waveform data
 types that includes timing information. This VI is only supported in LabVIEW 7.0 or
 later.

[IMAGE alt='icon' src='niscope-multi-read-wdt-vi.png']

#### Inputs/Outputs

| timestamp type — timestamp Type specifies the time basis for the timestamp on the WDT data. Defined Values absolute relative timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm returns a one-dimensional array of LabVIEW waveform data types that contain timing information. If you specify a channel list, NI-SCOPE returns the waveforms in the list order. NI-SCOPE returns these records sequentially, so all record 0 waveforms are first. For example, with a two-channel list, you would have the following index values: index 0 = record 0, channel 0 index 1 = record 0, channel 1 index 2 = record 1, channel 0 index 3 = record 1, channel 1 error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Read (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-probe-compensation-signal-start-vi.html language=enus -->
## TOPIC 00135: niScope Probe Compensation Signal Start VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-probe-compensation-signal-start-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-probe-compensation-signal-start-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a 1 kHz square wave signal for probe compensation. Most oscilloscopes output the probe compesation signal on PFI 1. The following oscilloscopes output the probe compensation signal in unique locations. Device Output Location Notes PXIe‑5110PXIe‑5111PXIe‑5113 Probe compensation terminal The

### niScope Probe Compensation Signal Start VI

Generates a 1 kHz square wave signal for probe compensation.

Most oscilloscopes output the probe compesation signal on PFI 1.

The following oscilloscopes output the probe compensation signal in unique locations.

| Device | Output Location | Notes |
| --- | --- | --- |
| PXIe‑5110PXIe‑5111PXIe‑5113 | Probe compensation terminal | The signal at this terminal is enabled by default. |
| PXIe‑5163PXIe‑5164 | SMB PFI 0 | Though the PFI 0 line is also available from the AUX 0 MHDMR connector of these oscilloscopes, the probe compensation signal is available only from SMB PFI 0. |

Note

Features Supported by Device

[IMAGE alt='icon' src='niscope-probe-compensation-signal-start-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-probe-compensation-signal-stop-vi.html language=enus -->
## TOPIC 00136: niScope Probe Compensation Signal Stop VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-probe-compensation-signal-stop-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-probe-compensation-signal-stop-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the 1 kHz square wave signal for probe compensation. Some features are not supported by all digitizers. Refer to Features Supported by Device for more information. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png

### niScope Probe Compensation Signal Stop VI

Disables the 1 kHz square wave signal for probe compensation.

Note

Features Supported by Device

[IMAGE alt='icon' src='niscope-probe-compensation-signal-stop-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-property-node-vi.html language=enus -->
## TOPIC 00137: niScope Property Node VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-property-node-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The niScope Property Node is used to set, get, or check properties. icon Inputs/Outputs civrn.png reference reference is the refnum associated with the object for which you want to set or get properties. If the Property Node class is Application or VI, you do not have to wire a refnum to this input.

### niScope Property Node VI

The niScope Property Node is used to set, get, or check properties.

[IMAGE alt='icon' src='niscope-property-node-vi.png']

#### Inputs/Outputs

| reference — reference is the refnum associated with the object for which you want to set or get properties. If the Property Node class is Application or VI, you do not have to wire a refnum to this input. For the Application class, the default is the current application instance. For the VI class, the default is the VI containing the Property Node. You also can wire a LabVIEW class to the reference input to access the private data of the LabVIEW class. error in (no error) — error in (no error) describes error conditions that occur before this VI runs. If an error occurred before this VI runs, the VI passes the error in value to error out. This VI runs normally only if no error occurs before this VI runs. If an error occurs while this VI runs, it continues and sets its own error status in error out. Use niScope Error Message to display the description of the error code. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. reference out — reference out returns reference unchanged. error out — error out contains error information. This output provides standard error out functionality. Property — property are examples of properties you want to get (read). |
| --- |

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-read-cluster-vi.html language=enus -->
## TOPIC 00138: niScope Read Cluster VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-read-cluster-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-read-cluster-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates an acquisition, waits for it to complete, and retrieves the data for a single channel and record. icon Inputs/Outputs cdbl.png timeout timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. U

### niScope Read Cluster VI

Initiates an acquisition, waits for it to complete, and retrieves the data for a
 single channel and record.

[IMAGE alt='icon' src='niscope-read-cluster-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. waveform — waveform is a cluster containing the initial x value, xIincrement, and a waveform array. This output can be wired directly to the LabVIEW waveform graph, so the waveform is plotted with timing information. The initial x value in the cluster is relative to the trigger. The relative initial x value is the time from the trigger to the first point so the trigger always occurs at time equals zero. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. wfm — wfm is an array of waveform data containing one waveform without any timing information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |
| relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. wfm — wfm is an array of waveform data containing one waveform without any timing information. |

Parent topic:

niScope Read (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-read-measurement-vi.html language=enus -->
## TOPIC 00139: niScope Read Measurement VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-read-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-read-measurement-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates an acquisition, waits for it to complete, and performs the specified waveform measurement for a single channel and record. Use niScope Multi Read Measurement for multiple records and channels. Related topics Making Waveform Measurements Acquisition Functions icon Inputs/Outputs cdbl.png ti

### niScope Read Measurement VI

Initiates an acquisition, waits for it to complete, and performs the specified
 waveform measurement for a single channel and record.

Use [niScope Multi Read Measurement](niscope-multi-read-measurement-vi.html) for
 multiple records and channels.

**Related topics**

- Making Waveform Measurements
- Acquisition Functions

[IMAGE alt='icon' src='niscope-read-measurement-vi.png']

#### Inputs/Outputs

| timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. scalar measurement — scalar measurement is the measurement to perform on the waveform read from the digitizer. Refer to the list of NI-SCOPE Scalar Measurements for more information. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. result — result contains the measurement acquired. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Measurements

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-read-poly-vi.html language=enus -->
## TOPIC 00140: niScope Read (poly) VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-read-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-read-poly-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates an acquisition, waits for it to complete, and acquires data. Related topics: Acquisition Functions NI-SCOPE Programming Flow icon

### niScope Read (poly) VI

Initiates an acquisition, waits for it to complete, and acquires data.

**Related topics:**

- Acquisition Functions
- NI-SCOPE Programming Flow

[IMAGE alt='icon' src='niscope-read-poly-vi.png']

- [niScope Read Cluster VI](../../../instr-lib/niscope/niscope-llb/niscope-read-cluster-vi.html) Initiates an acquisition, waits for it to complete, and retrieves the data for a single channel and record.
- [niScope Multi Read Cluster VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-read-cluster-vi.html) Initiates an acquisition, waits for it to complete, and retrieves the data for multiple channels and records.
- [niScope Read WDT VI](../../../instr-lib/niscope/niscope-llb/niscope-read-wdt-vi.html) Returns the waveform the digitizer acquires for the specified channel. The VI initiates an acquisition that returns a scaled voltage waveform in a waveform data type that includes timing information.
- [niScope Multi Read WDT VI](../../../instr-lib/niscope/niscope-llb/niscope-multi-read-wdt-vi.html) Initiates an acquisition and returns a one-dimensional array of LabVIEW waveform data types that includes timing information. This VI is only supported in LabVIEW 7.0 or later.

Parent topic:

NI-SCOPE

Parent topic:

Acquisition

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-read-wdt-vi.html language=enus -->
## TOPIC 00141: niScope Read WDT VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-read-wdt-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-read-wdt-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the waveform the digitizer acquires for the specified channel. The VI initiates an acquisition that returns a scaled voltage waveform in a waveform data type that includes timing information. icon Inputs/Outputs ci32.png timestamp type timestamp Type specifies the time basis for the timestam

### niScope Read WDT VI

Returns the waveform the digitizer acquires for the specified channel. The VI
 initiates an acquisition that returns a scaled voltage waveform in a waveform data type
 that includes timing information.

[IMAGE alt='icon' src='niscope-read-wdt-vi.png']

#### Inputs/Outputs

| timestamp type — timestamp Type specifies the time basis for the timestamp on the WDT data. Defined Values absolute relative timeout — timeout is the time (in seconds) to wait for the data to be acquired. Use 0 for this parameter to tell NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout. instrument handle — instrument handle identifies a particular instrument session. channels — channels specifies the channel(s) from which to acquire data. For more information, refer to Channel String Syntax. numSamples — numSamples is the maximum number of samples to fetch for each waveform; if the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. Use –1 for this parameter if you want to fetch all available samples. The VI reads the actual record length and attempts to acquire all available samples. If it fails to complete within the timeout period, the VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. wfm info — wfm info contains all the timing and scaling information about the waveform. actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. wfm — wfm returns data for wiring to a graph, including the timing information. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| actualSamples — actualSamples is the actual number of samples in the acquired waveform; this number may be less than numSamples if the number you request is not available. absoluteInitialX — absoluteInitialX is the timestamp in seconds of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output. relativeInitialX — relativeInitialX is the time in seconds from the trigger to the first sample in the acquired waveform. xIncrement — xIncrement indicates the time in seconds between two samples in the acquired waveform. offset — offset is the offset factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset gain — gain is the gain factor of the given channel. Use for scaling binary data with the following formula: voltage = binary data × gain factor + offset reserved1 — reserved1 is reserved. Do not use. reserved2 — reserved2 is reserved. Do not use. |

Parent topic:

niScope Read (poly) VI

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-reset-device-vi.html language=enus -->
## TOPIC 00142: niScope Reset Device VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-reset-device-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-reset-device-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a hard reset of the device. Acquisition stops, all routes are released, RTSI and PFI lines are tristated, FPGAs are reset, hardware is configured to its default state, and all session attributes are reset to their default states. Related Topics Thermal Shutdown icon Inputs/Outputs civrn.png

### niScope Reset Device VI

Performs a hard reset of the device. Acquisition stops, all routes are released, RTSI
 and PFI lines are tristated, FPGAs are reset, hardware is configured to its default
 state, and all session attributes are reset to their default states.

**Related Topics**

- Thermal Shutdown

[IMAGE alt='icon' src='niscope-reset-device-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-reset-vi.html language=enus -->
## TOPIC 00143: niScope Reset VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-reset-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-reset-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the digitizer to its default state. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in error in describes error conditions that occur before this node runs. The default is no error. This node executes regardl

### niScope Reset VI

Resets the digitizer to its default state.

[IMAGE alt='icon' src='niscope-reset-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-reset-with-defaults-vi.html language=enus -->
## TOPIC 00144: niScope Reset with Defaults VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-reset-with-defaults-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-reset-with-defaults-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the device to the default state and applies any initial default settings from the IVI Configuration Store. This VI uses default parameters to do a software reset on the device The changes are not immediately committed to hardware. icon Inputs/Outputs civrn.png instrument handle instrument han

### niScope Reset with Defaults VI

Resets the device to the default state and applies any initial default settings from
 the IVI Configuration Store. This VI uses default parameters to do a software reset on
 the device The changes are not immediately committed to hardware.

[IMAGE alt='icon' src='niscope-reset-with-defaults-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. The default is no error. This node executes regardless of an incoming error. This input contains status, code, and source, which provide standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-revision-query-vi.html language=enus -->
## TOPIC 00145: niScope Revision Query VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-revision-query-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-revision-query-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision numbers of the instrument driver and instrument firmware. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in error in describes error conditions that occur before this node runs. This input prov

### niScope Revision Query VI

Returns the revision numbers of the instrument driver and instrument firmware.

[IMAGE alt='icon' src='niscope-revision-query-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. firmware revision — firmware revision returns the instrument firmware revision numbers. instrument driver revision — instrument driver revision returns the instrument driver software revision numbers. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-sample-rate-vi.html language=enus -->
## TOPIC 00146: niScope Sample Rate VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-sample-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-sample-rate-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the effective sample rate, in samples per second, of the acquired waveform using the current configuration. Refer to Coercions of Horizontal Parameters for more information about sample rate coercion. Related topics Sample Rate Coercions of Horizontal Parameters Sample Clock icon Inputs/Outp

### niScope Sample Rate VI

Returns the effective sample rate, in samples per second, of the acquired waveform
 using the current configuration.

Refer to [Coercions of Horizontal Parameters](/csh?context=niscope_digitizers_horizontal_parameters) for more information about sample rate coercion.

**Related topics**

- Sample Rate
- Coercions of Horizontal Parameters
- Sample Clock

[IMAGE alt='icon' src='niscope-sample-rate-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. actual sample rate — actual sample rate returns the effective sample rate of the acquired waveform the digitizer acquires for each channel. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Actual Values

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-self-test-vi.html language=enus -->
## TOPIC 00147: niScope Self Test VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-self-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-self-test-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs the device self-test routine and returns the test result(s). icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cerrcodeclst.png error in error in describes error conditions that occur before this node runs. This input provides standard

### niScope Self Test VI

Runs the device self-test routine and returns the test result(s).

[IMAGE alt='icon' src='niscope-self-test-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. self-test message — self-test message returns the self-test response string from the device. self test result — self test result contains the value returned from the device self-test. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/niscope-send-software-trigger-edge-vi.html language=enus -->
## TOPIC 00148: niScope Send Software Trigger Edge VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/niscope-send-software-trigger-edge-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/niscope-send-software-trigger-edge-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the selected trigger to the digitizer. If you called niScope Configure Trigger Software, call this VI when you want the reference trigger to occur. You can also call this VI to override a misused edge, digital, or hysteresis reference trigger. If you have configured an Acquisition Arm Source,

### niScope Send Software Trigger Edge VI

Sends the selected trigger to the digitizer. If you called niScope Configure Trigger
 Software, call this VI when you want the reference trigger to occur. You can also call
 this VI to override a misused edge, digital, or hysteresis reference trigger. If you
 have configured an Acquisition Arm Source, an Arm Reference Trigger Source, or an
 Advance Trigger Source, call this VI when you want to send the corresponding trigger to
 the digitizer.

**Related topics:**

- Software Triggers

[IMAGE alt='icon' src='niscope-send-software-trigger-edge-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. which trigger — which trigger specifies the type of trigger to send to the digitizer. Defined Values Start Trigger Arm Reference Trigger Reference Trigger Advance Trigger error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out has the same value as the instrument handle. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Triggering

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/open-ext-cal-session-vi.html language=enus -->
## TOPIC 00149: Open Ext Cal Session VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/open-ext-cal-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/open-ext-cal-session-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens an external calibration session for the specified device. This VI returns an error if you specify a device that is not supported by this calibration library. This VI also downloads the calibration bitstream to the device FPGA if not already present. Supported Devices: PXIe-5110 PXIe-5111 PXIe-

### Open Ext Cal Session VI

Opens an external calibration session for the specified device.

This VI returns an error if you specify a device that is not supported by this calibration library. This VI also downloads the calibration bitstream to the device FPGA if not already present.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='open-ext-cal-session-vi.png']

#### Inputs/Outputs

| resource name — resource name identifies the device to perform an external calibration on. external cal password — external cal password is the calibration password for the device. This password is required to perform external calibration, set the calibration due date, and set the date and time of verification. The default password is NI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. external cal session — external cal session returns a new external calibration session reference for the device specified by resource name. Use this reference as an input to other external calibration VIs in this library. session — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session — |

Parent topic:

5110 Ext Cal

Parent topic:

5111 Ext Cal

Parent topic:

5113 Ext Cal

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/set-external-cal-due-date-vi.html language=enus -->
## TOPIC 00150: Set External Cal Due Date VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/set-external-cal-due-date-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/set-external-cal-due-date-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the external calibration due date of the device. Supported Devices: PXIe-5110 PXIe-5111 PXIe-5113 icon Inputs/Outputs civrn.png resource name in resource name in identifies the device. catrn.png external cal due date external cal due date sets the new due date and time of the external calibrati

### Set External Cal Due Date VI

Sets the external calibration due date of the device.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='set-external-cal-due-date-vi.png']

#### Inputs/Outputs

| resource name in — resource name in identifies the device. external cal due date — external cal due date sets the new due date and time of the external calibration. external cal password — external cal password is the calibration password for the device. This password is required to perform external calibration, set the calibration due date, and set the date and time of verification. The default password is NI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. resource name out — resource name out passes the device name to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/set-external-cal-verification-date-vi.html language=enus -->
## TOPIC 00151: Set External Cal Verification Date VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/set-external-cal-verification-date-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/set-external-cal-verification-date-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the most recent external calibration verification date of the device. Supported Devices: PXIe-5110 PXIe-5111 PXIe-5113 icon Inputs/Outputs civrn.png resource name in resource name in identifies the device. catrn.png external cal verification date external cal verification date sets the updated

### Set External Cal Verification Date VI

Sets the most recent external calibration verification date of the device.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='set-external-cal-verification-date-vi.png']

#### Inputs/Outputs

| resource name in — resource name in identifies the device. external cal verification date — external cal verification date sets the updated date and time of the most recent successful external verification of the device. external cal password — external cal password is the calibration password for the device. This password is required to perform external calibration, set the calibration due date, and set the date and time of verification. The default password is NI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. resource name out — resource name out passes the device name to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-llb/set-misc-info-vi.html language=enus -->
## TOPIC 00152: Set Misc Info VI

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-llb/set-misc-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-llb/set-misc-info-vi.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores custom text information that is stored until you close the current calibration session. You can choose to commit this information to the device when you close the calibration session. Committing this information to the device allows you to access it in subsequent calibration sessions with the

### Set Misc Info VI

Stores custom text information that is stored until you close the current calibration session. You can choose to commit this information to the device when you close the calibration session.

Committing this information to the device allows you to access it in subsequent calibration sessions with the [Get Misc Info](get-misc-info-vi.html) VI of this library.

**Supported Devices:**

- PXIe-5110
- PXIe-5111
- PXIe-5113

[IMAGE alt='icon' src='set-misc-info-vi.png']

#### Inputs/Outputs

| external cal session in — external cal session in identifies your session. This parameter is obtained from the Open Ext Cal Session VI of this library. session — miscellaneous information — miscellaneous information is the text information to store. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. external cal session out — external cal session out passes a reference to your session to the next VI. session — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session — |
| session — |

Parent topic:

5110 Ext Cal

Parent topic:

5111 Ext Cal

Parent topic:

5113 Ext Cal

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-lowlevelacq-mnu.html language=enus -->
## TOPIC 00153: Acquisition

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-lowlevelacq-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-lowlevelacq-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE Acquisition VIs to control your data acquisition and to retrieve data from your device. icon

### Acquisition

Use the NI-SCOPE Acquisition VIs to control your data acquisition and to retrieve data from your device.

[IMAGE alt='icon' src='niscope-lowlevelacq-mnu.png']

- [niScope Get Wfm Coefficients (poly) VI](../../instr-lib/niscope/niscope-llb/niscope-get-wfm-coefficients-poly-vi.html) Returns coefficients that can be used to scale or normalize binary waveform data.
- [niScope Commit VI](../../instr-lib/niscope/niscope-llb/niscope-commit-vi.html) Commits to hardware all the parameter settings associated with the task. Use this VI if you want a parameter change to be immediately reflected in the hardware.
- [niScope Initiate Acquisition VI](../../instr-lib/niscope/niscope-llb/niscope-initiate-acquisition-vi.html) Initiates a waveform acquisition.
- [niScope Fetch (poly) VI](../../instr-lib/niscope/niscope-llb/niscope-fetch-poly-vi.html) Retrieves data that the digitizer has acquired from a previously initiated acquisition.
- [niScope Abort VI](../../instr-lib/niscope/niscope-llb/niscope-abort-vi.html) Aborts an acquisition without changing the settings on the digitizer. Use this VI if the digitizer times out waiting for a trigger.
- [niScope Acquisition Status VI](../../instr-lib/niscope/niscope-llb/niscope-acquisition-status-vi.html) Returns status information indicating whether an acquisition is in progress, complete, or unknown to the acquisition status output parameter.
- [niScope Read (poly) VI](../../instr-lib/niscope/niscope-llb/niscope-read-poly-vi.html) Initiates an acquisition, waits for it to complete, and acquires data.

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-measurement-mnu.html language=enus -->
## TOPIC 00154: Measurements

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-measurement-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-measurement-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE Measurements VIs to perform waveform measurements, including scalar and array measurements. icon

### Measurements

Use the NI-SCOPE Measurements VIs to perform waveform measurements, including scalar and array measurements.

[IMAGE alt='icon' src='niscope-measurement-mnu.png']

- [niScope Clear Waveform Processing VI](../../instr-lib/niscope/niscope-llb/niscope-clear-waveform-processing-vi.html) Clears the list of processing steps assigned to the given channel.
- [niScope Add Waveform Processing VI](../../instr-lib/niscope/niscope-llb/niscope-add-waveform-processing-vi.html) Adds one measurement to the list of processing steps that are completed before the measurement. The processing is added on a per channel basis, and the processing measurements are completed in the same order they are registered. All waveform measurements (for example, adding channels or applying a Bessel filter) are cached at the time of registering the processing, and this set of measurements is used during the processing step. The processing measurements are streamed, so the result of the first processing step is used as the input for the next step. The processing happens before any other measurements.
- [niScope Fetch Measurement (poly) VI](../../instr-lib/niscope/niscope-llb/niscope-fetch-measurement-poly-vi.html) Obtains a waveform from the digitizer and returns the specified measurement.
- [niScope Read Measurement VI](../../instr-lib/niscope/niscope-llb/niscope-read-measurement-vi.html) Initiates an acquisition, waits for it to complete, and performs the specified waveform measurement for a single channel and record.
- [niScope Clear Waveform Measurement Stats VI](../../instr-lib/niscope/niscope-llb/niscope-clear-waveform-measurement-stats-vi.html) Clears the waveform statistics on the channel and measurement you specify. This VI clears the statistical information and the multi-acquisition array measurements.
- [niScope Multi Read Measurement VI](../../instr-lib/niscope/niscope-llb/niscope-multi-read-measurement-vi.html) Initiates an acquisition, waits for it to complete, and performs the specified waveform measurement for multiple channels and records.

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-measurementlink-mnu.html language=enus -->
## TOPIC 00155: MeasurementLink

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-measurementlink-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-measurementlink-mnu.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette in conjunction with MeasurementLink Session Management. icon

### MeasurementLink

Use the VIs on this palette in conjunction with MeasurementLink Session Management.

[IMAGE alt='icon' src='niscope-measurementlink-mnu.png']

- [niScope Initialize for gRPC Session VI](../../instr-lib/niscope/niscope-llb/niscope-initialize-for-grpc-session-vi.html) Initializes a new NI-SCOPE session on the specified NI gRPC Device Server using the specified instrument and options.
- [niScope Attach gRPC Session VI](../../instr-lib/niscope/niscope-llb/niscope-attach-grpc-session-vi.html) Attaches to an existing NI-SCOPE session with the specified session name on the specified NI gRPC Device Server. Returns a session handle to be used in all subsequent NI-SCOPE VI calls.
- [niScope Detach gRPC Session VI](../../instr-lib/niscope/niscope-llb/niscope-detach-grpc-session-vi.html) Closes the session specified in instrument handle but leaves the session open on the NI gRPC Device Server.

Parent topic:

Utility Functions

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope-p.html language=enus -->
## TOPIC 00156: niScope Properties

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope-p.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE properties to access advanced configuration options for high-speed digitizer applications.

### niScope Properties

Use the NI-SCOPE properties to access advanced configuration options for high-speed digitizer applications.

- [Active Channel](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-activechannel.html) Specifies the channel name used to access all subsequent properties in this instance of the property node. If the property you want to use is Channel Based, you need to first select this property and then pass the name of the specific channel. If the property you specify is not channel based, pass an empty string, or omit setting this property. The default value is " ".
- [Vertical:Channel Enabled](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-channelenabled.html) Specifies whether the digitizer acquires a waveform for the channel.
- [Vertical:Vertical Range](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-verticalrange.html) Specifies the absolute value of the input range for a channel. The units are volts. For example, to acquire a sine wave that spans between -5 and +5 V, set this property to 10.0 V.
- [Vertical:Vertical Offset](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-verticaloffset.html) Specifies the location of the center of the range. The value is with respect to ground and is in volts. For example, to acquire a sine wave that spans between 0.0 and 10.0 V, set this property to 5.0 V. This property is not supported by all digitizers.
- [Vertical:Maximum Input Frequency](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-maxinputfrequency.html) Specifies the bandwidth of the channel in hertz. Express this value as the frequency at which the input circuitry attenuates the input signal by 3 dB.
- [Vertical:Vertical Coupling](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-verticalcoupling.html) Specifies how the digitizer couples the input signal for the channel. When you change input coupling, the input stage takes a finite amount of time to settle.
- [Vertical:Input Impedance](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-inputimpedance.html) Specifies the input impedance for the channel in ohms.
- [Vertical:Probe Attenuation](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-probeattenuation.html) Specifies the probe attenuation for the input channel. For example, for a 10:1 probe, you would set this property to 10.0.
- [Vertical:Channel Terminal Configuration](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-terminalconfiguration.html) Specifies how the digitizer configures the channel terminal.
- [Vertical:Advanced:Digital Gain](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-digitalgain.html) Applies gain to the specified channel in hardware before any onboard signal processing occurs. The default value is 1.
- [Vertical:Advanced:Digital Offset](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-digitaloffset.html) Applies offset to the specified channel in hardware before any onboard signal processing occurs. The default value is 0.
- [Vertical:Advanced:Bandpass Filter Enabled](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-bandpassfilterenabled.html) Enables the bandpass filter on the specified channel. For the NI PXIe-5622, set the value to TRUE to enable the IF filtered path 50MHz bandpass filter centered at 187MHz. The default value is FALSE.
- [Vertical:Advanced:Dither Enabled](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-ditherenabled.html) Enables or disables the analog dither on the device. Using dither can improve the spectral performance of the device by reducing the effects of quantization. However, adding dither increases the power level to the ADC, so you may need to either decrease the signal level or increase the vertical range. The default value is FALSE.
- [Vertical:Advanced:Flex FIR Antialias Filter Type](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-flexfirantialiasfiltertype.html) The NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass antialias filter. Use this property to select from several types of filters to achieve desired filtering characteristics. For most applications, the default value of this property is recommended. The other available filters are useful for optimizing settling time measurements of step responses. The default value is 48 Tap Standard.
- [Vertical:Advanced:High Pass Filter Frequency](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-highpassfilterfrequency.html) Specifies the frequency for the highpass filter in Hz. The device uses one of the valid values listed below. If an invalid value is specified, no coercion occurs. The default value is 0.
- [Vertical:Advanced:Interleaving Offset Correction Enabled](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-interleavingoffsetcorrectionenabled.html) Enables the interleaving offset correction on the specified channel. The default value is TRUE.
- [Horizontal:Min Sample Rate](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-minsamplerate.html) Specifies the sampling rate (in Samples/second) for the acquisition. This attribute is invalid when the device is configured to use an external sample clock timebase. When a DDC is enabled, this attribute specifices the IQ rate. When both the Time Per Record Property and the Min Sample Rate Property are set, the attribute that was set first is ignored.
- [Horizontal:Min Number of Points](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-minnumberofpoints.html) Specifies the minimum number of points you require in the waveform record for each channel.
- [Horizontal:Number of Records](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-numberofrecords.html) Specify the number of records to acquire.
- [Horizontal:Reference Position](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-referenceposition.html) Specifies the position of the Reference Event in the waveform record as a percentage of the record.
- [Horizontal:Actual Sample Rate](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-actualsamplerate.html) Returns the actual sample rate used for the acquisition.
- [Horizontal:Actual Record Length](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-actualrecordlength.html) Returns the actual number of points the digitizer acquires for each channel. The value is equal to or greater than the value you specify in the niScope Configure Horizontal Timing VI.
- [Horizontal:Enable Time Interleaved Sampling](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-enabletis.html) Extends the maximum sample rate on the specified Active Channel for some devices that support Time Interleaved Sampling (TIS). TIS enables the device to use multiple ADCs to sample the same waveform at a higher effective real-time rate. NI 5152/5153/5154 devices fully support Read/Write ability for this property. For other devices that use TIS mode, such as the NI 5185/5186, this property is Read Only.
- [Horizontal:Enforce Realtime](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-enforcerealtime.html) Indicates whether the digitizer enforces real-time measurements or allows equivalent-time measurements.
- [Horizontal:Enable Records > Memory](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-enablerecordsmemory.html) Allows you to acquire more records than fit in onboard memory.
- [Horizontal:RIS Num Avg](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-risnumavg.html) Specifies the number of averages in each RIS bin.
- [Horizontal:RIS Method](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-rismethod.html) Specifies the algorithm for random-interleaved sampling, which is used if the sample rate exceeds the Max Realtime Sample Rate .
- [Horizontal:Maximum Real Time Sample Rate](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-maximumrealtimesamplerate.html) Returns the maximum real-time sample rate in hertz.
- [Horizontal:Maximum RIS Rate](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-maximumrisrate.html) Returns the maximum RIS sampling rate in hertz.
- [Horizontal:Memory Size](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-memorysize.html) Returns the total combined amount of onboard memory for all channels in bytes.
- [Horizontal:Advanced:Enable TDC](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-enabletdc.html) Specifies that the digitizer should record the trigger position precisely using time-digital conversion (TDC).
- [Horizontal:Advanced:Time Per Record](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-timeperrecord.html) Specifies the length of time (in seconds) that corresponds to the record length. This attribute is invalid when the device is configured to use an external sample clock timebase. This attribute is also invalid when a DDC is enabled. When both the Time Per Record Property and the Min Sample Rate Property are set, the attribute that was set first is ignored.
- [Horizontal:Advanced:Acquisition Start Time](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-acqstarttime.html) Specifies the length of time (in seconds) from the trigger event to the first point in the waveform record.
- [Triggering:Trigger Type](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggertype.html) Specifies the type of trigger to use.
- [Triggering:Trigger Source](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggersource.html) Specifies the source the digitizer monitors for the trigger event. The value must be selected from one of the following valid values.
- [Triggering:Trigger Output Terminal](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-reftrig-outputterm.html) Specifies the destination to export the Reference (Stop) Trigger Refer to the device specifications document for a list of valid destinations.
- [Triggering:Terminal Name](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-referencetriggerterminalname.html) Returns the fully qualified name for the Reference Trigger terminal.
- [Triggering:Trigger Level](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggerlevel.html) Specifies the voltage threshold for the trigger. The units are volts.
- [Triggering:Trigger Modifier](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggermodifier.html) Configures the device to automatically complete an acquisition if a trigger has not been received.
- [Triggering:Auto Triggered](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-autotriggered.html) Specifies whether the acquisition was triggered automatically. Auto triggering occurs if the Trigger Modifier property is set to Auto Trigger and no trigger has been received for a certain amount of time.
- [Triggering:Trigger Hysteresis](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggerhysteresis.html) Specifies the size of the hysteresis window, in volts, on either side of the trigger level.
- [Triggering:Trigger Delay](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggerdelay.html) Specifies the trigger delay time in seconds.
- [Triggering:Trigger Holdoff](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggerholdoff.html) Specifies the length of time the digitizer waits after detecting a trigger before enabling the trigger subsystem to detect another trigger. The units are seconds.
- [Triggering:Trigger Slope](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggerslope.html) Specifies whether a rising or a falling edge triggers the digitizer.
- [Triggering:Trigger Coupling](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggercoupling.html) Specifies how the digitizer couples the trigger source.
- [Triggering:Trigger Impedance](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggerimpedance.html) Sets the impedance for the external trigger input.
- [Triggering:Start To Ref Trigger Holdoff](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-starttoreftriggerholdoff.html) Pass the length of time (in seconds) you want the digitizer to wait after it starts acquiring data until the digitizer enables the trigger system to detect a reference (stop) trigger.
- [Triggering:End of Record to Advance Trigger Holdoff](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-recordadvanceholdoff.html) End of Record to Advance Trigger Holdoff is the length of time (in seconds) that a device waits between the completion of one record and the acquisition of pre-trigger samples for the next record. During this time, the acquisition engine state delays the transition to the Wait for Advance Trigger state, and will not store samples in onboard memory, accept an Advance Trigger, or trigger on the input signal..
- [Triggering:Trigger Window:Window Mode](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggerwindowmode.html) Specifies whether to trigger when the signal enters or leaves the window specified by the Trigger Window Low Level property or the Trigger Window High Level property.
- [Triggering:Trigger Window:Low Level](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggerwindowlowlevel.html) Pass the lower voltage threshold you want the digitizer to use for window triggering.
- [Triggering:Trigger Window:High Level](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-triggerwindowhighlevel.html) Pass the upper voltage threshold you want the digitizer to use for window triggering.
- [Triggering:Trigger Video:Signal Format](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-videosignalformat.html) Specifies the video signal format to use.
- [Triggering:Trigger Video:Line Number](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-videolinenumber.html) Specifies the line number to trigger on.
- [Triggering:Trigger Video:Polarity](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-videopolarity.html) Specifies whether the video signal is positive or negative.
- [Triggering:Trigger Video:Event](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-videotriggerevent.html) Specifies the event to trigger on.
- [Triggering:Trigger Video:Enable DC Restore](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-enabledcrestore.html) Restores the video-triggered data retrieved by the digitizer to the video signal's zero reference point. The default value is FALSE.
- [Triggering:Trigger Glitch:Glitch Condition](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-glitchcondition.html) Specifies whether the oscilloscope triggers on pulses of duration less than or greater than the specified Glitch Width .
- [Triggering:Trigger Glitch:Glitch Width](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-glitchwidth.html) Specifies the glitch duration, in seconds.
- [Triggering:Trigger Glitch:Glitch Polarity](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-glitchpolarity.html) Specifies the polarity of pulses that trigger the oscilloscope for glitch triggering.
- [Triggering:Trigger Width:Width Condition](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-widthcondition.html) Specifies whether the oscilloscope triggers on pulses within or outside the duration range bounded by the Width Low Threshold and Width High Threshold properties.
- [Triggering:Trigger Width:Width Low Threshold](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-widthlowthreshold.html) Specifies the low width threshold, in seconds.
- [Triggering:Trigger Width:Width High Threshold](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-widthhighthreshold.html) Specifies the high width threshold, in seconds.
- [Triggering:Trigger Width:Width Polarity](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-widthpolarity.html) Specifies the polarity of pulses that trigger the oscilloscope for width triggering.
- [Triggering:Trigger Runt:Runt Low Threshold](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-runtlowthreshold.html) Specifies the lower of two thresholds, in volts, that bound the vertical range to examine for runt pulses.
- [Triggering:Trigger Runt:Runt High Threshold](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-runthighthreshold.html) Specifies the higher of two thresholds, in volts, that bound the vertical range to examine for runt pulses.
- [Triggering:Trigger Runt:Runt Polarity](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-runtpolarity.html) Specifies the polarity of pulses that trigger the oscilloscope for runt triggering.
- [Triggering:Trigger Runt:Runt Time Condition](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-runttimecondition.html) Specifies whether runt triggers are time qualified, and if so, how the oscilloscope triggers in relation to the duration range bounded by the Runt Time Low Limit and Runt Time High Limit properties.
- [Triggering:Trigger Runt:Runt Time Low Limit](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-runttimelowlimit.html) Specifies, in seconds, the low runt threshold time.
- [Triggering:Trigger Runt:Runt Time High Limit](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-runttimehighlimit.html) Specifies, in seconds, the high runt threshold time.
- [Device:CableSense:Voltage](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-cablesensevoltage.html) Returns the voltage of the CableSense signal that is written to the EEPROM of the oscilloscope during factory calibration.
- [Device:CableSense:Mode](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-cablesensemode.html) Specifies whether and how the oscilloscope is configured to generate a CableSense signal on the specified channels when the niScope CableSense Signal Start VI is called.
- [Acquisition:Enabled Channels](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-enabledchannels.html) Returns a comma-separated list of the channels enabled for the session in ascending order.
- [Triggering:Onboard Signal Processing:Ref Trigger Detection Location](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-reftriggerdetectorlocation.html) Specifies which reference trigger detection circuitry to use on the device.
- [Triggering:Onboard Signal Processing:Ref Trigger Min Quiet Time](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-reftriggerminquiettime.html) Specifies the amount of time (in seconds) the trigger circuit must not detect a signal above the trigger level (or below the trigger level if the trigger slope is negative) before the trigger is armed. This property is useful for triggering at the beginning of signal bursts instead of in the middle of signal bursts. The default value is 0.
- [Fetch:Fetch Record Number](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-fetchrecordnumber.html) Sets the record to fetch. The record is from a channel you specify. The default value is 0.
- [Fetch:Fetch Number of Records](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-fetchnumberofrecords.html) Fetches multiple records. If you want to fetch all records from the record you specify in the Fetch Record Number property to the last record configured, use -1. The default value is -1.
- [Fetch:Fetch Relative To](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-fetchrelativeto.html) Specifies which point in the acquired waveform is the first to be fetched. This property specifies what the 'Fetch Offset' is relative to.
- [Fetch:Fetch Offset](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-fetchoffset.html) Sets the offset in samples; the samples returned also depend on the Fetch Relative To property. The default value is 0.
- [Fetch:Data Transfer Block Size](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-datatransferblocksize.html) Specifies the maximum number of samples to transfer at one time from the device to host memory. Increasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may also increase the amount of page-locked memory required from the system.
- [Fetch:Fetch Meas Num Samples](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-fetchmeasnumberofsamples.html) Determines the number of samples to fetch from a digitizer when performing a measurement. -1 means fetch all samples from the Fetch Offset property to the end of the current record. The default value is -1.
- [Fetch:Points Done](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-pointsdone.html) Actual number of samples acquired relative to the configured value for Fetch Relative To , including Fetch Offset , and for the current configured Fetch Record Number .
- [Fetch:Fetch Backlog](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-fetchbacklog.html) Specifies the number of points acquired that have not been fetched yet.
- [Fetch:Records Done](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-recordsdone.html) Returns the number of records your digitizer has acquired.
- [Fetch:Advanced:Maximum Bandwidth](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-maximumbandwidth.html) Specifies the maximum bandwidth that the device is allowed to consume. The NI device limits itself to transfer fewer bytes per second on the PCIe bus than the value you specify for this property.
- [Fetch:Advanced:Preferred Packet Size](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-preferredpacketsize.html) Specifies the preferred size of the data field in the PCI Express packet. In general, the larger the packet size, the more efficiently the device uses the bus. However, some systems, because of their implementation, perform better with smaller packet sizes. The value of this property must be a power of two (64, 128, ... , 512).
- [Clocking:Reference (Input) Clock Source](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-referenceclocksource.html) Specifies the input source for the PLL reference clock.
- [Clocking:Reference Clock Rate](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-referenceclockrate.html) If Reference Clock Source is an external source, specifies the frequency (in hertz) of the input clock (reference clock) to which the internal sample clock timebase is synchronized.
- [Clocking:Output Clock Source](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-outputclocksource.html) Specifies the output source for the 10 MHz clock to which the sample clock of another digitizer can be phase-locked.
- [Clocking:Sample Clock Timebase Source](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-sampleclocktimebasesource.html) Specifies the source of the sample clock timebase, which is the timebase used to control waveform sampling.
- [Clocking:Sample Clock Timebase Rate](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-sampleclocktimebaserate.html) Specifies, in hertz, the frequency of the external clock used as the timebase source if the Sample Clock Timebase Source is an external source or, if the timebase source is the internal clock for oscilloscopes that support multiple onboard clock rates, of the internal clock.
- [Clocking:Sample Clock Timebase Divisor](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-sampleclocktimebasedivisor.html) If Sample Clock Timebase Source is an external source, specifies the ratio between the sample clock timebase rate and the actual sample rate, which can be slower.
- [Clocking:Sample Clock Timebase Multiplier](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-sampleclocktimebasemultiplier.html) If Sample Clock Timebase Source is an external source, this property specifies the ratio between the Sample Clock Timebase Rate and the actual sample rate, which can be higher. This property can be used in conjunction with the Sample Clock Timebase Divisor Property .
- [Clocking:Exported Sample Clock Output Terminal](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-exportedsampleclockoutputterminal.html) Exports the sample clock to a specified terminal. This property is not supported by all digitizers.
- [Clocking:Clock Sync Pulse Source](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-clocksyncpulsesource.html) Specifies the line on which the sample clock or the one-time sync pulse is sent or received.
- [Clocking:PLL Lock Status](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-plllocked.html) If TRUE, the PLL has remained locked to the external reference clock since it was last checked. If FALSE, the PLL has become unlocked from the external reference clock since it was last checked.
- [Clocking:Advanced:Oscillator Phase DAC Value](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-oscillatorphasedacvalue.html) Gets or sets the binary phase DAC value that controls the delay added to the phase-locked loop (PLL) of the sample clock.
- [Clocking:Advanced:Absolute Sample Clock Offset](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-absolutesampleclockoffset.html) Gets or sets the absolute time offset, in seconds, of the sample clock relative to the reference clock.
- [Device:FPGA Bitfile Path](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-fpgabitfilepath.html) Gets the absolute file path to the bitfile loaded on the FPGA.
- [Synchronization:Start Trigger (Acq. Arm): Source](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-starttriggersource.html) Specifies the source the digitizer monitors for an acquisition arm trigger. When an acquisition arm trigger is received, the digitizer begins acquiring pretrigger samples.
- [Synchronization:Start Trigger (Acq. Arm): Output Terminal](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-starttrig-outputterm.html) Specifies the destination to export the Start trigger. When the start trigger is received, the digitizer begins acquiring data. Refer to the device specifications document for a list of valid destinations.
- [Synchronization:Start Trigger (Acq. Arm):Terminal Name](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-starttriggerterminalname.html) Returns the fully qualified name for the Start Trigger terminal.
- [Synchronization:Ready for Start:Output Terminal](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-rdyforstartevent-outputterm.html) Specifies the destination to export the Start trigger. When the start trigger is received, the digitizer begins acquiring data. Refer to the device specifications document for a list of valid destinations.
- [Synchronization:Ready for Start:Terminal Name](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-readyforstarteventterminalname.html) Returns the fully qualified name for the Ready for Start Event terminal.
- [Synchronization:Advance Trigger:Source](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-advancetriggersource.html) Specifies the source the digitizer monitors for an advance trigger. When the advance trigger is received, the digitizer begins acquiring pretrigger samples for the next record.
- [Synchronization:Advance Trigger:Output Terminal](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-advtrig-outputterm.html) Specifies the destination for the advance trigger. When the advance trigger is received, the digitizer begins acquiring pretrigger samples.
- [Synchronization:Advance Trigger:Terminal Name](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-advancetriggerterminalname.html) Returns the fully qualified name for the Advance Trigger terminal.
- [Synchronization:Ready for Advance:Output Terminal](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-rdyforadvevent-outputterm.html) Specifies the destination for the advance trigger. When the advance trigger is received, the digitizer begins acquiring pretrigger samples.
- [Synchronization:Ready for Advance:Terminal Name](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-readyforadvanceeventterminalname.html) Returns the fully qualified name for the Ready for Advance Event terminal.
- [Synchronization:Arm Reference Trigger:Source](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-armreferencetriggersource.html) Specifies the source the digitizer monitors for an arm reference trigger. When the arm reference trigger is received, the digitizer begins searching for the reference (stop) trigger from the user-configured trigger source.
- [Synchronization:Ready for Reference:Output Terminal](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-rdyforrefevent-outputterm.html) Specifies the destination for the Ready for Reference Event. When this event is asserted, the digitizer is ready to receive a reference trigger. Refer to the device-specific documentation in the NI High-Speed Digitizers Help for a list of valid destinations for your device.
- [Synchronization:Ready for Reference:Terminal Name](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-readyforreferenceeventterminalname.html) Returns the fully qualified name for the Ready for Reference Event terminal.
- [Synchronization:End of Record:Output Terminal](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-endofrecevent-outputterm.html) Specifies the destination for the End of Record event. When this event is asserted, the digitizer has completed sampling a record. Refer to the device specifications document for a list of valid destinations.
- [Synchronization:End of Record:Terminal Name](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-endofrecordeventterminalname.html) Returns the fully qualified name for the End of Record Event terminal.
- [Synchronization:End of Acquisition:Output Terminal](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-endofacqevent-outputterm.html) Specifies the destination for the End of Acquisition event. When this event is asserted, the digitizer has completed sampling all records. Refer to the device specifications document for a list of valid destinations.
- [Synchronization:End of Acquisition:Terminal Name](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-endofacquisitioneventterminalname.html) Returns the fully qualified name for the End of Acquisition Event terminal.
- [Synchronization:5 Volt Power:Output Terminal](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-5voltpower-outputterm.html) Specifies the destination for the 5 Volt power signal. Refer to the device specifications document for a list of valid destinations.
- [Synchronization:Master Enable](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-masterenable.html) Specifies whether the device is a master or a slave.
- [Acquisition:Binary Sample Width](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-binarysamplewidth.html) Indicates the bit width of the binary data in the acquired waveform, which can help you determine which Binary Fetch to use.
- [Acquisition:Resolution](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-resolution.html) Indicates the actual resolution in bits of valid data (as opposed to padding bits) in the acquired waveform. Compare to the Binary Sample Width property.
- [Acquisition:Acquisition Type](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-acquisitiontype.html) Specifies how the oscilloscope acquires data and fills the waveform record.
- [Acquisition:Sample Mode](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-samplemode.html) Returns the sample mode the digitizer is currently using.
- [Acquisition:Advanced:Enable RIS in Auto Setup](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-enablerisinautosetup.html) Indicates whether the digitizer should use RIS sample rates when searching for a frequency in autosetup.
- [Waveform Measurement:Other Channel](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-otherchannel.html) Specifies the second channel for two-channel measurements, such as Add Channels . If processing steps are registered with this channel, the processing happens before the waveform is used in a two-channel measurement. The default value is 0.
- [Waveform Measurement:Array Gain](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-arraygain.html) Every element of an array is multiplied by this scalar value during the array gain measurement. The default value is 1.0.
- [Waveform Measurement:Array Offset](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-arrayoffset.html) Every element of an array is added to this scalar value during the array offset measurement. The default value is 0.0.
- [Waveform Measurement:Hysteresis Percent](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-hysteresispercent.html) Digital hysteresis that is used in several of the scalar waveform measurements. This property specifies the percentage of the full-scale vertical range for the hysteresis window size. The default value is 2%.
- [Waveform Measurement:Last Acq. Histogram Size](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-lastacq-histogramsize.html) Specifies the size (that is, the number of bins) in the last acquisition histogram. This histogram is used to determine several scalar measurements, most importantly voltage low and voltage high. The default value is 256.
- [Waveform Measurement:Voltage Histogram:Size](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-v-hist-size.html) Specifies the number of bins in the running voltage histogram. The default value is 256.
- [Waveform Measurement:Voltage Histogram:Low Volts](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-v-hist-lowvolts.html) Specifies the minimum voltage value in the running voltage histogram. The default value is -10.0.
- [Waveform Measurement:Voltage Histogram:High Volts](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-v-hist-highvolts.html) Specifies the maximum voltage value in the running voltage histogram. The default value is 10.0.
- [Waveform Measurement:Time Histogram:Size](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-timehist-size.html) Determines the multiple acquisition time histogram size. The size is set during the first call to a time histogram measurement after you clear the measurement history with niScope Clear Waveform Measurement Stats .
- [Waveform Measurement:Time Histogram:Low Volts](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-timehist-lowvolts.html) Specifies the low voltage limit for the multi-acquisition time histogram. Only points in the waveform between the low and high voltage limits are included in the histogram. The default value is -10.0.
- [Waveform Measurement:Time Histogram:High Volts](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-timehist-highvolts.html) Specifies the high voltage limit for the Multi-Acquisition time histogram. Only points in the waveform between the low and high voltage limits are included in the histogram. The default value is 10.0 V.
- [Waveform Measurement:Time Histogram:Low Time](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-timehist-lowtime.html) Specifies the minimum time limit (in seconds) of the multi-acquisition time histogram, where the time is in seconds relative to the trigger position. Only points in the waveform between the low and high time limits are included in the histogram. The default value is -5.0e-4 .
- [Waveform Measurement:Time Histogram:High Time](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-timehist-hightime.html) Specifies the maximum time limit (in seconds) of the Multi-Acquisition time histogram, where the time is in seconds relative to the trigger position. Only points in the waveform between the low and high time limits are included in the histogram. The default value is 5.0e-4 .
- [Waveform Measurement:Interpolation:Polynomial Interpolation Order](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-poly-interp-order.html) Specifies the order of the polynomial used during the polynomial interpolation array measurement. For example, an order of 1 is linear interpolation whereas an order of 2 specifies parabolic interpolation. Any positive integer is valid. The default value is 1 (linear interpolation).
- [Waveform Measurement:Interpolation:Sampling Factor](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-interp-samplingfactor.html) The new number of points for polynomial interpolation is the sampling factor times the input number of points. The default value is 0.0.
- [Waveform Measurement:Filter:Type](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-filtertype.html) Specifies the type of digital filter. The default value is lowpass.
- [Waveform Measurement:Filter:FIR Taps](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-filtertaps.html) Specifies the number of taps for the finite impulse response filter. This value must be odd if the filter type is highpass or bandstop. Otherwise, the magnitude response goes to zero as the frequency goes to half the sampling rate. The default value is 25.
- [Waveform Measurement:Filter:FIR Window](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-firfilterwindow.html) Specifies the FIR window type. The symmetric windows are applied to the FIR filter coefficients to limit passband ripple in FIR filters. The default value is None (0).
- [Waveform Measurement:Filter:Width](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-filterwidth.html) Specifies the width (in Hz) of a bandpass or bandstop filter. The cutoff frequencies are the (center frequency property ± 0.5 × filter width). The default value is 1.0e3.
- [Waveform Measurement:Filter:IIR Order](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-filterorder.html) Specifies the order of the infinite impulse response filter. The default value is 2.
- [Waveform Measurement:Filter:Cutoff Frequency](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-filtercutofffrequency.html) Specifies the cutoff frequency in hertz for filters of type lowpass and highpass. The cutoff frequency definition varies depending on the filter. The default value is 1.0e6 Hz.
- [Waveform Measurement:Filter:Center Frequency](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-filtercenterfrequency.html) The center frequency in hertz for filters of type bandpass and bandstop. The width of the filter is specified by Filter Width, where the cutoff frequencies are the center width. The default value is 1.0e6 Hz.
- [Waveform Measurement:Filter:Ripple](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-filterripple.html) Specifies the amount of passband ripple (in dB) for Chebyshev filters. More ripple gives a sharper cutoff for a given filter order. The default value is 0.1.
- [Waveform Measurement:Filter:Percent Waveform Transient](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-percentwaveformtransient.html) The percentage (0 - 100%) of the infinite impulse response (IIR) filtered waveform to eliminate from the beginning of the waveform. This action allows eliminating the transient portion of the waveform that is undefined due to the assumptions necessary at the boundary condition. The default value is 20.0%.
- [Waveform Measurement:Reference Levels:Channel Based Low Ref Level](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-chan-basedlowref.html) Specifies the low reference level used in many scalar measurements. The default value is 10.0%.
- [Waveform Measurement:Reference Levels:Channel Based Mid Ref Level](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-chan-basedmidref.html) Specifies the mid reference level used in many scalar measurements. The default value is 50%.
- [Waveform Measurement:Reference Levels:Channel Based High Ref Level](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-chanbasedhighref.html) Specifies the high reference level used in many scalar measurements. The default value is 90%.
- [Waveform Measurement:Reference Levels:Units](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-ref-levelunits.html) Specifies the units for the waveform measurement reference levels.
- [Waveform Measurement:Reference Levels:Percentage Units Method](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-percentagemethod.html) Specifies the method used to map percentage reference units to voltages. The default value is BaseTop.
- [Onboard Signal Processing:DDC:DDC Enabled](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-ddcenabled.html) Enables/disables the digital downconverter (DDC) block of the digitizer. When the DDC block is disabled, all DDC-related properties are disabled and have no effect on the acquired signal. The default value is FALSE.
- [Onboard Signal Processing:DDC:Data Processing Mode](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-dataprocessingmode.html) The way in which data is processed by the DDC block. The default value is Complex.
- [Onboard Signal Processing:DDC:Frequency Translation Enabled](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-frequencytranslationenabled.html) Enables/disables frequency translating the data around the user-selected center frequency down to baseband. The default value is TRUE.
- [Onboard Signal Processing:DDC:Center Frequency](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-centerfrequency.html) The frequency at which the DDC block frequency translates the input data. The default value is 10 MHz.
- [Onboard Signal Processing:DDC:Fetch Interleaved IQ Data](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-fetchinterleavediqdata.html) Specifies whether a fetch call retrieves a single waveform with I and Q interleaved, or two separate waveforms. If enabled, the number of elements returned by scalar fetch types (such as 16-bit integer) is twice the requested number of samples. If disabled during DDC acquisitions in Complex mode, two noninterleaved arrays of data are returned per channel, per record.
- [Onboard Signal Processing:DDC:Q Source](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-qsource.html) Specifies the channel that is the input to the Q data stream of the DDC .
- [Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase I](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-frequencytranslationphasei.html) The I oscillator phase in degrees at the first point acquired. The default value is 0.
- [Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase Q](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-frequencytranslationphaseq.html) The Q oscillator phase in degrees at the first point acquired. Use this property only when the Data Processing Mode property is set to Complex. The default value is 90.
- [Onboard Signal Processing:Equalization:Equalization Filter Enabled](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-equalizationfilterenabled.html) Enables the onboard signal processing equalization FIR block, which is connected directly to the input signal. The equalization filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and -1. The default value is FALSE.
- [Onboard Signal Processing:Equalization:Equalization Num Coefficients](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-equalizationnumcoefficients.html) Returns the number of coefficients that the equalization FIR filter can accept. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and -1.
- [Onboard Signal Processing:Fractional Resample:Fractional Resample Enabled](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-fractionalresampleenabled.html) Enables the onboard signal processing block that resamples the input waveform to the user desired sample rate. The default value is FALSE.
- [Onboard Signal Processing:OSP Overflow Error Reporting](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-overflowerrorreporting.html) Configures error reporting when the onboard signal processing block detects an overflow in any of its stages. Overflows lead to clipping of the waveform. The default value is Warning.
- [Peer-to-Peer:P2P Enabled](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2penabled.html) Specifies whether the digitizer writes data to the peer-to-peer endpoint. This property is endpoint-based.
- [Peer-to-Peer:Channels to Stream](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pchannelstostream.html) Specifies which channels will be written to a peer-to-peer endpoint. If multiple channels are specified, they will be interleaved by sample. This property is endpoint-based. The default value is 0.
- [Peer-to-Peer:Endpoint Size](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pendpointsize.html) Returns the size, in samples, of the peer-to-peer endpoint. This property is endpoint-based.
- [Peer-to-Peer:Samples Available In Endpoint](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2psamplesavailableinendpoint.html) Returns the current number of samples available to stream from a peer-to-peer endpoint. This property is endpoint-based.
- [Peer-to-Peer:Most Samples Available in Endpoint](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pmostsamplesavailableinendpoint.html) Returns the most number of samples available to stream from a peer-to-peer endpoint since the last time this property was read. This property is endpoint-based.
- [Peer-to-Peer:Samples Transferred](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2psamplestransferred.html) Returns the number of samples transferred through the peer-to-peer endpoint since the endpoint was last reset. This property is endpoint-based.
- [Peer-to-Peer:Endpoint Overflow](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pendpointoverflow.html) Returns TRUE if the peer-to-peer endpoint has overflowed. Reset the endpoint to clear the overflow condition. This property is endpoint-based.
- [Peer-to-Peer:FIFO Endpoint Count](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pfifoendpointcount.html) Returns the number of FIFO-based peer-to-peer endpoints this device supports.
- [Peer-to-Peer:Onboard Memory Enabled](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-onboardmemoryenabled.html) Specifies whether the digitizer writes data to onboard memory when a peer-to-peer endpoint is enabled.
- [Peer-to-Peer:Stream Relative To](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pstreamrelativeto.html) Determines which trigger peer-to-peer data is streamed relative to. The default value is Start Trigger .
- [Peer-to-Peer:Samples Transferred Per Record](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2psamplestransferredperrecord.html) Returns the number of samples transferred per record when you set the Stream Relative To property to Reference Trigger or Sync Trigger .
- [Peer-to-Peer:Manual:Manual Configuration Enabled](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pmanualconfigurationenabled.html) Enables and disables manual configuration of a peer-to-peer endpoint. These attributes cannot be used if an endpoint is being configured by NI-P2P, or a resource reservation error will result. This property is endpoint-based.
- [Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pdatatransferpermissionaddress.html) Returns the address of a hardware register used to grant permission for the peer-to-peer endpoint to write data to another peer. The type of this address is determined by the Data Transfer Permission Address Type property. Permission is granted in bytes and the register is additive. This property is endpoint-based.
- [Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address Type](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pdatatransferpermissionaddresstype.html) Specifies the type of address returned to the user from the Data Transfer Permission Address property. This property is endpoint-based.
- [Peer-to-Peer:Manual:Configuration:Destination Window Address](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pdestinationwindowaddress.html) Specifies the destination for data written by the peer-to-peer endpoint. The type of this address is specified by the Destination Window Address Type property. This property is endpoint-based.
- [Peer-to-Peer:Manual:Configuration:Destination Window Address Type](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pdestinationwindowaddresstype.html) Specifies the type of the Destination Window Address property. This property is endpoint-based.
- [Peer-to-Peer:Manual:Configuration:Destination Window Size](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pdestinationwindowsize.html) Specifies the size, in bytes, of the destination window determined by the Destination Window Address and Destination Window Address Type properties. This property is endpoint-based.
- [Peer-to-Peer:Manual:Notification:Push Message On](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2ppushmessageon.html) Specifies the event to push the Message Push Value property to the Message Push Address property. Specifying Done will push the message when the acquisition has completed. This property is endpoint-based.
- [Peer-to-Peer:Manual:Notification:Message Push Address](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pmessagepushaddress.html) Specifies the address to push the Message Push Value to on the event specified by the Push Message On property. This property is endpoint-based.
- [Peer-to-Peer:Manual:Notification:Message Push Address Type](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pmessagepushaddresstype.html) Specifies the type of the Message Push Address property. This property is endpoint-based.
- [Peer-to-Peer:Manual:Notification:Message Push Value](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-p2pmessagepushvalue.html) Specifies the value to be pushed to the Message Push Address property on the event specified in the Push Message On property. This property is endpoint-based.
- [Device:Temperature](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-devicetemperature.html) Returns the temperature of the device in degrees Celsius from the onboard sensor.
- [Device:Serial Number](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-serialnumber.html) Returns the serial number of the device.
- [Device:Accessory:Gain](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-accessorygain.html) Returns the calibration gain for the current device configuration.
- [Device:Accessory:Offset](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-accessoryoffset.html) Returns the calibration offset for the current device configuration.
- [Inherent IVI Attributes:User Options:Range Check](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-rangecheck.html) Specifies whether to validate property values and function parameters. If enabled, the instrument driver validates the parameter values that you pass to driver functions. Range checking parameters is very useful for debugging. After you validate your program, you can set this property to FALSE to disable range checking and maximize performance. The default value is TRUE. Use niScope Initialize with Options to override this value.
- [Inherent IVI Attributes:User Options:Query Instrument Status](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-queryinstrumentstatus.html) Specifies whether the instrument driver queries the instrument status after each operation. Querying the instrument status is very useful for debugging. After you validate your program, you can set this property to FALSE to disable status checking and maximize performance. The instrument driver can choose to ignore status checking for particular properties regardless of the setting of this property. The default value is TRUE. Use niScope Initialize with Options to override this value.
- [Inherent IVI Attributes:User Options:Cache](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-cache.html) Specifies whether to cache the value of properties. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. Thus, you can significantly increase execution speed. The instrument driver can choose always to cache or never to cache particular properties, regardless of the setting of this property. The default value is TRUE. Use niScope Initialize with Options to override this value.
- [Inherent IVI Attributes:User Options:Simulate](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-simulate.html) Specifies whether to simulate instrument driver I/O operations. The default value is FALSE. Use niScope Initialize with Options to override this value.
- [Inherent IVI Attributes:User Options:Record Value Coercions](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-recordvaluecoercions.html) Specifies whether the IVI engine keeps a list of the value coercions it makes for ViInt32 and DBL properties. The default value is FALSE. Use niScope Initialize with Options to override this value.
- [Inherent IVI Attributes:User Options:Interchange Check](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-interchangecheck.html) Specifies whether to perform interchangeability checking and log interchangeability warnings when you call VIs. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior.
- [Inherent IVI Attributes:Driver Identification:Description](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-description.html) A string that contains the description of the instrument.
- [Inherent IVI Attributes:Driver Identification:Driver Prefix](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-driverprefix.html) A string that contains the prefix for the instrument driver. The name of each user-callable function in this driver starts with this prefix.
- [Inherent IVI Attributes:Driver Identification:Driver Vendor](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-drivervendor.html) A string that contains the name of the vendor that supplies this driver, for example, " National Instruments ".
- [Inherent IVI Attributes:Driver Identification:Revision](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-revision.html) The string that contains additional version information about this instrument driver.
- [Inherent IVI Attributes:Driver Identification:Class Specification Major Version](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-classspecificationmajorversion.html) The major version number of the class specification with which this driver is compliant.
- [Inherent IVI Attributes:Driver Identification:Class Specification Minor Version](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-classspecificationminorversion.html) The minor version number of the class specification with which this driver is compliant.
- [Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-supportedinstrumentmodels.html) A string that contains a comma-separated list of the instrument model numbers supported by this driver.
- [Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-classgroupcapabilities.html) A string that contains a comma-separated list of class-extension groups that this driver implements.
- [Inherent IVI Attributes:Driver Capabilities:Channel Count](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-channelcount.html) Indicates the number of channels that the specific instrument driver supports. For channel based properties, the IVI engine maintains a separate cache value for each channel.
- [Inherent IVI Attributes:Instrument Identification:Manufacturer](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-manufacturer.html) A string that contains the name of the instrument manufacturer, for example, "National Instruments".
- [Inherent IVI Attributes:Instrument Identification:Model](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-model.html) A string that contains the model number of the current instrument.
- [Inherent IVI Attributes:Instrument Identification:Firmware Revision](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-firmwarerevision.html) A string that contains the firmware revision information for the current instrument.
- [Inherent IVI Attributes:Advanced Session Information:Logical Name](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-logicalname.html) A string that contains the logical name you specified when opening the current IVI session.
- [Inherent IVI Attributes:Advanced Session Information:Resource Descriptor](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-resourcedescriptor.html) Indicates the resource descriptor the driver uses to identify the physical device. If you initialize the driver with a logical name, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration utility. If you initialize the instrument driver with the resource descriptor, this property contains that value.
- [Device Specific:IF Digitizer:Fetch Interleaved Data](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-fetchinterleaveddata.html) Specifies whether to interleave I and Q data retrieved from the IF digitizer in a single array or to retrieve two separate arrays, one for I data and another for Q data.
- [Device Specific:IF Digitizer:Device Number](../../../instr-lib/niscope/niscope-rc/niscope/pniscope-devicenumber.html) Returns the device number of the IF digitizer associated with the current session.

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/channel-string-syntax.html language=enus -->
## TOPIC 00157: Channel String Syntax

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/channel-string-syntax.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/channel-string-syntax.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For most VIs, the input parameter channels has the following options: a single channel, such as "0" a list of channels, such as "0,1" or "3,2,1,0" a range of channels, such as "0–7" or "0:7" all channels, which is designated by the empty string, "" a combination of channels from multiple instruments

### Channel String Syntax

For most VIs, the input parameter **channels** has the following options:

- a single channel, such as "0"
- a list of channels, such as "0,1" or "3,2,1,0"
- a range of channels, such as "0–7" or "0:7"
- all channels, which is designated by the empty string, ""
- a combination of channels from multiple instruments, such as "PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3"

Note

**Exceptions for Fetch/Read VIs**

If you use an empty string in a fetch or read VI to designate all channels, NI-SCOPE returns an error.

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-5voltpower-outputterm.html language=enus -->
## TOPIC 00158: Synchronization:5 Volt Power:Output Terminal

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-5voltpower-outputterm.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-5voltpower-outputterm.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination for the 5 Volt power signal. Refer to the device specifications document for a list of valid destinations. This property is supported only for NI 5152/5153/5154 devices. Defined Values VAL_RTSI_0 VAL_RTSI_1 VAL_RTSI_2 VAL_RTSI_3 VAL_RTSI_4 VAL_RTSI_5 VAL_RTSI_6 VAL_PFI_0 VA

### Synchronization:5 Volt Power:Output Terminal

Specifies the destination for the 5 Volt power signal. Refer to the device specifications document for a list of valid destinations.

Note

**Defined Values**

VAL_RTSI_0

VAL_RTSI_1

VAL_RTSI_2

VAL_RTSI_3

VAL_RTSI_4

VAL_RTSI_5

VAL_RTSI_6

VAL_PFI_0

VAL_PFI_1

VAL_PFI_2

VAL_PXI_STAR

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | 5VoltPower.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Export Signal |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-absolutesampleclockoffset.html language=enus -->
## TOPIC 00159: Clocking:Advanced:Absolute Sample Clock Offset

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-absolutesampleclockoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-absolutesampleclockoffset.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the absolute time offset, in seconds, of the sample clock relative to the reference clock. Valid Values: [-0.5 Sample Clock Period, 0.5 Sample Clock Period] Default Value: 0 Use this property when performing manual adjustment to correct for skew and jitter between oscilloscopes synchron

### Clocking:Advanced:Absolute Sample Clock Offset

Gets or sets the absolute time offset, in seconds, of the sample clock relative to the reference clock.

**Valid Values**: [-0.5 *Sample Clock Period*, 0.5 *Sample Clock Period*]

**Default Value**: 0

Use this property when performing manual adjustment to correct for skew and jitter between oscilloscopes synchronized with NI-TClk.

Apply offset with this property to reduce skew and jitter, and write the value you set to apply the manual adjustment across sessions and improve synchronization repeatability.

For details on performing manual adjustment, refer to [Improving NI-TClk Synchronization of Oscilloscopes with Manual Adjustment](/csh?context=niscope_digitizers_ni-tclk-manual-adjustment-oscilloscopes).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Absolute Sample Clock Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-accessorygain.html language=enus -->
## TOPIC 00160: Device:Accessory:Gain

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-accessorygain.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-accessorygain.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the calibration gain for the current device configuration. This property is only supported by the NI PXI-5900 differential amplifier. Related topics: NI 5122/5124/5142 Calibration Remarks The following table lists the characteristics of this property. Short Name Accessory Gain Data type cdbl

### Device:Accessory:Gain

Returns the calibration gain for the current device configuration.

Note

**Related topics:**

- NI 5122/5124/5142 Calibration

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Accessory Gain |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-accessoryoffset.html language=enus -->
## TOPIC 00161: Device:Accessory:Offset

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-accessoryoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-accessoryoffset.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the calibration offset for the current device configuration. This property is supported only by the NI PXI-5900 differential amplifier. Related topics: NI 5122/5124/5142 Calibration Remarks The following table lists the characteristics of this property. Short Name Accessory Offset Data type

### Device:Accessory:Offset

Returns the calibration offset for the current device configuration.

Note

**Related topics:**

- NI 5122/5124/5142 Calibration

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Accessory Offset |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-acqstarttime.html language=enus -->
## TOPIC 00162: Horizontal:Advanced:Acquisition Start Time

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-acqstarttime.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-acqstarttime.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of time (in seconds) from the trigger event to the first point in the waveform record. If the value is positive, the first point in the waveform record occurs after the trigger event (same as specifying a trigger delay). If the value is negative, the first point in the waveform

### Horizontal:Advanced:Acquisition Start Time

Specifies the length of time (in seconds) from the trigger event to the first point in the waveform record.

If the value is positive, the first point in the waveform record occurs after the trigger event (same as specifying a trigger delay). If the value is negative, the first point in the waveform record occurs before the trigger event (same as specifying Reference Position).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Acq Start Time |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-acquisitiontype.html language=enus -->
## TOPIC 00163: Acquisition:Acquisition Type

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-acquisitiontype.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-acquisitiontype.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the oscilloscope acquires data and fills the waveform record. Remarks The following table lists the characteristics of this property. Short Name Acquisition Type Data type ci32.png Permissions Read/Write High-level VIs niScope Configure Acquisition Channel-based No Resettable No Normal

### Acquisition:Acquisition Type

Specifies how the oscilloscope acquires data and fills the waveform record.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Acquisition Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Acquisition |
| Channel-based | No |
| Resettable | No |

| Normal | 0 | Sets the oscilloscope to normal resolution mode. The oscilloscope can use real-time sampling or equivalent-time sampling. |
| --- | --- | --- |
| Flex Res | 1001 | Sets legacy oscilloscopes to flexible resolution mode, if supported. |
| DDC | 1002 | Sets legacy oscilloscopes to DDC mode, if supported. To use DDC mode for the PXI/PCI-5142 or PXIe-5622, set this property to Normal and set the DDC Enabled property to True. |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-activechannel.html language=enus -->
## TOPIC 00164: Active Channel

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-activechannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-activechannel.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel name used to access all subsequent properties in this instance of the property node. If the property you want to use is Channel Based, you need to first select this property and then pass the name of the specific channel. If the property you specify is not channel based, pass a

### Active Channel

Specifies the channel name used to access all subsequent properties in this instance of the property node. If the property you want to use is Channel Based, you need to first select this property and then pass the name of the specific channel. If the property you specify is not channel based, pass an empty string, or omit setting this property. The default value is " ".

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Channel |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-actualrecordlength.html language=enus -->
## TOPIC 00165: Horizontal:Actual Record Length

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-actualrecordlength.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-actualrecordlength.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the actual number of points the digitizer acquires for each channel. The value is equal to or greater than the value you specify in the niScope Configure Horizontal Timing VI. Valid Values: 1 to the maximum memory size Record Length Coercions of Horizontal Parameters Remarks The following ta

### Horizontal:Actual Record Length

Returns the actual number of points the digitizer acquires for each channel.

 The value is equal to or greater than the value you specify in the [niScope Configure Horizontal Timing](/csh?context=niscope_scopeviref_niscope_configure_horizontal_timing) VI.

Valid Values: 1 to the maximum memory size

- Record Length
- Coercions of Horizontal Parameters

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Actual Record Length |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niScope Actual Record Length |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-actualsamplerate.html language=enus -->
## TOPIC 00166: Horizontal:Actual Sample Rate

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-actualsamplerate.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-actualsamplerate.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the actual sample rate used for the acquisition. Units: hertz (Samples / Second) Related topics: Sample Clock Remarks The following table lists the characteristics of this property. Short Name Actual Sample Rate Data type cdbl.png Permissions Read Only High-level VIs niScope Sample Rate Chan

### Horizontal:Actual Sample Rate

Returns the actual sample rate used for the acquisition.

Units: hertz (Samples / Second)

**Related topics:**

- Sample Clock

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Actual Sample Rate |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niScope Sample Rate |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-advancetriggersource.html language=enus -->
## TOPIC 00167: Synchronization:Advance Trigger:Source

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-advancetriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-advancetriggersource.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source the digitizer monitors for an advance trigger. When the advance trigger is received, the digitizer begins acquiring pretrigger samples for the next record. Defined Values VAL_IMMEDIATE VAL_RTSI_0 VAL_RTSI_1 VAL_RTSI_2 VAL_RTSI_3 VAL_RTSI_4 VAL_RTSI_5 VAL_RTSI_6 VAL_PFI_0 VAL_PFI

### Synchronization:Advance Trigger:Source

Specifies the source the digitizer monitors for an advance trigger. When the advance trigger is received, the digitizer begins acquiring pretrigger samples for the next record.

**Defined Values**

VAL_IMMEDIATE

VAL_RTSI_0

VAL_RTSI_1

VAL_RTSI_2

VAL_RTSI_3

VAL_RTSI_4

VAL_RTSI_5

VAL_RTSI_6

VAL_PFI_0

VAL_PFI_1

VAL_PFI_2

VAL_PFI_3

VAL_PFI_4

VAL_PFI_5

VAL_PFI_6

VAL_PFI_7

VAL_PXI_STAR

VAL_SW_TRIG_FUNC

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Advance Trigger Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-advancetriggerterminalname.html language=enus -->
## TOPIC 00168: Synchronization:Advance Trigger:Terminal Name

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-advancetriggerterminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-advancetriggerterminalname.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified name for the Advance Trigger terminal. You can use this terminal as the source for another trigger. Remarks The following table lists the characteristics of this property. Short Name Advance Trigger Terminal Name Data type cstr.png Permissions Read Only High-level VIs N/A

### Synchronization:Advance Trigger:Terminal Name

Returns the fully qualified name for the Advance Trigger terminal.

You can use this terminal as the source for another trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Advance Trigger Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-advtrig-outputterm.html language=enus -->
## TOPIC 00169: Synchronization:Advance Trigger:Output Terminal

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-advtrig-outputterm.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-advtrig-outputterm.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination for the advance trigger. When the advance trigger is received, the digitizer begins acquiring pretrigger samples. Remarks The following table lists the characteristics of this property. Short Name AdvTrig.OutputTerm Data type cstr.png Permissions Read/Write High-level VIs N

### Synchronization:Advance Trigger:Output Terminal

Specifies the destination for the advance trigger. When the advance trigger is received, the digitizer begins acquiring pretrigger samples.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdvTrig.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-armreferencetriggersource.html language=enus -->
## TOPIC 00170: Synchronization:Arm Reference Trigger:Source

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-armreferencetriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-armreferencetriggersource.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source the digitizer monitors for an arm reference trigger. When the arm reference trigger is received, the digitizer begins searching for the reference (stop) trigger from the user-configured trigger source. Defined Values VAL_IMMEDIATE VAL_RTSI_0 VAL_RTSI_1 VAL_RTSI_2 VAL_RTSI_3 VAL_

### Synchronization:Arm Reference Trigger:Source

Specifies the source the digitizer monitors for an arm reference trigger. When the arm reference trigger is received, the digitizer begins searching for the reference (stop) trigger from the user-configured trigger source.

**Defined Values**

VAL_IMMEDIATE

VAL_RTSI_0

VAL_RTSI_1

VAL_RTSI_2

VAL_RTSI_3

VAL_RTSI_4

VAL_RTSI_5

VAL_RTSI_6

VAL_PFI_0

VAL_PFI_1

VAL_PFI_2

VAL_PFI_3

VAL_PFI_4

VAL_PFI_5

VAL_PFI_6

VAL_PFI_7

VAL_PXI_STAR

VAL_SW_TRIG_FUNC

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Arm Reference Trigger Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-arraygain.html language=enus -->
## TOPIC 00171: Waveform Measurement:Array Gain

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-arraygain.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-arraygain.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Every element of an array is multiplied by this scalar value during the array gain measurement. The default value is 1.0. Remarks The following table lists the characteristics of this property. Short Name Array Gain Data type cdbl.png Permissions Read/Write High-level VIs N/A Channel-based Yes Reset

### Waveform Measurement:Array Gain

Every element of an array is multiplied by this scalar value during the array gain measurement. The default value is 1.0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Array Gain |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-arrayoffset.html language=enus -->
## TOPIC 00172: Waveform Measurement:Array Offset

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-arrayoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-arrayoffset.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Every element of an array is added to this scalar value during the array offset measurement. The default value is 0.0. Remarks The following table lists the characteristics of this property. Short Name Array Offset Data type cdbl.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resett

### Waveform Measurement:Array Offset

Every element of an array is added to this scalar value during the array offset measurement. The default value is 0.0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Array Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-autotriggered.html language=enus -->
## TOPIC 00173: Triggering:Auto Triggered

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-autotriggered.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-autotriggered.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the acquisition was triggered automatically. Auto triggering occurs if the Trigger Modifier property is set to Auto Trigger and no trigger has been received for a certain amount of time. Related topics: Trigger Types Remarks The following table lists the characteristics of this pro

### Triggering:Auto Triggered

Specifies whether the acquisition was triggered automatically. Auto triggering occurs if the Trigger Modifier property is set to Auto Trigger and no trigger has been received for a certain amount of time.

**Related topics:**

- Trigger Types

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto Triggered |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-bandpassfilterenabled.html language=enus -->
## TOPIC 00174: Vertical:Advanced:Bandpass Filter Enabled

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-bandpassfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-bandpassfilterenabled.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the bandpass filter on the specified channel. For the NI PXIe-5622, set the value to TRUE to enable the IF filtered path 50MHz bandpass filter centered at 187MHz. The default value is FALSE. Related topics: Bandwidth Remarks The following table lists the characteristics of this property. Sho

### Vertical:Advanced:Bandpass Filter Enabled

Enables the bandpass filter on the specified channel. For the NI PXIe-5622, set the value to TRUE to enable the IF filtered path 50MHz bandpass filter centered at 187MHz. The default value is FALSE.

**Related topics:**

- Bandwidth

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Bandpass Filter Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-binarysamplewidth.html language=enus -->
## TOPIC 00175: Acquisition:Binary Sample Width

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-binarysamplewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-binarysamplewidth.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the bit width of the binary data in the acquired waveform, which can help you determine which Binary Fetch to use. To configure the device to store samples with a lower resolution than the native, set this property to the desired binary width. This configuration can be useful for streaming

### Acquisition:Binary Sample Width

Indicates the bit width of the binary data in the acquired waveform, which can help you determine which Binary Fetch to use.

To configure the device to store samples with a lower resolution than the native, set this property to the desired binary width. This configuration can be useful for streaming at faster speeds, but at the cost of resolution. The least significant bits are lost with this configuration. Compare to the [Resolution](pniscope-resolution.html) property.

Valid Values:

 8, 16, 32

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Binary Sample Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-cablesensemode.html language=enus -->
## TOPIC 00176: Device:CableSense:Mode

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-cablesensemode.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-cablesensemode.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether and how the oscilloscope is configured to generate a CableSense signal on the specified channels when the niScope CableSense Signal Start VI is called. The input impedance of the channel(s) to convey the CableSense signal must be set to 50 ohms. Device-Specific Behavior PXIe‑5160 P

### Device:CableSense:Mode

Specifies whether and how the oscilloscope is configured to generate a CableSense signal on the specified channels when the [niScope CableSense Signal Start](/csh?context=niscope_scopeviref_niscope_cablesense_signal_start) VI is called.

Note

**Device-Specific Behavior**

| PXIe‑5160 PXIe‑5162 | The value of this property must be identical across all channels whose input impedance is set to 50 ohms. If this property is set to a value other than Disabled for any channel(s), the input impedance of all channels for which this property is set to Disabled must be set to 1 M Ohm. |
| --- | --- |

**Supported Devices**

- PXIe-5110
- PXIe-5111
- PXIe-5113
- PXIe-5160
- PXIe-5162

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CableSense Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

| Disabled | 0 | The oscilloscope is not configured to emit a CableSense signal. |
| --- | --- | --- |
| On Demand | 1 | The oscilloscope is configured to emit a single CableSense pulse. |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-cablesensevoltage.html language=enus -->
## TOPIC 00177: Device:CableSense:Voltage

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-cablesensevoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-cablesensevoltage.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the voltage of the CableSense signal that is written to the EEPROM of the oscilloscope during factory calibration. Supported Devices PXIe-5110 PXIe-5111 PXIe-5113 PXIe-5160 PXIe-5162 Remarks The following table lists the characteristics of this property. Short Name CableSense Voltage Data ty

### Device:CableSense:Voltage

Returns the voltage of the CableSense signal that is written to the EEPROM of the oscilloscope during factory calibration.

**Supported Devices**

- PXIe-5110
- PXIe-5111
- PXIe-5113
- PXIe-5160
- PXIe-5162

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CableSense Voltage |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-cache.html language=enus -->
## TOPIC 00178: Inherent IVI Attributes:User Options:Cache

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-cache.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-cache.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to cache the value of properties. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. Thus, you can significantly increase execution speed. The instrument driver can choose always to

### Inherent IVI Attributes:User Options:Cache

Specifies whether to cache the value of properties. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. Thus, you can significantly increase execution speed. The instrument driver can choose always to cache or never to cache particular properties, regardless of the setting of this property.
 The default value is TRUE. Use [niScope Initialize with Options](/csh?context=niscope_scopeviref_niscope_initialize_with_options) to override this value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cache |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Initialize With Options |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-centerfrequency.html language=enus -->
## TOPIC 00179: Onboard Signal Processing:DDC:Center Frequency

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-centerfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-centerfrequency.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The frequency at which the DDC block frequency translates the input data. The default value is 10 MHz. This property can be used only with high-speed digitizers that support onboard signal processing (OSP). NI-SCOPE returns an error if you use this property with a device that does not support OSP. V

### Onboard Signal Processing:DDC:Center Frequency

The frequency at which the [DDC](/csh?context=niscope_digitizers_glossary_ddc) block frequency translates the input data. The default value is 10 MHz.

Note

**Valid Values**

0 - (0.5 × Sample Clock Timebase Rate for digitizer)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Center Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-chan-basedlowref.html language=enus -->
## TOPIC 00180: Waveform Measurement:Reference Levels:Channel Based Low Ref Level

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-chan-basedlowref.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-chan-basedlowref.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the low reference level used in many scalar measurements. The default value is 10.0%. Units: Percentage of the signal based on the selected Percentage Units Method property. Remarks The following table lists the characteristics of this property. Short Name Chan. Based Low Ref Data type cdb

### Waveform Measurement:Reference Levels:Channel Based Low Ref Level

Specifies the low reference level used in many scalar measurements. The default value is 10.0%.

Units: Percentage of the signal based on the selected [Percentage Units Method](pniscope-percentagemethod.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Chan. Based Low Ref |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-chan-basedmidref.html language=enus -->
## TOPIC 00181: Waveform Measurement:Reference Levels:Channel Based Mid Ref Level

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-chan-basedmidref.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-chan-basedmidref.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mid reference level used in many scalar measurements. The default value is 50%. Units: Percentage of the signal based on the selected Percentage Units Method property. Remarks The following table lists the characteristics of this property. Short Name Chan. Based Mid Ref Data type cdbl.

### Waveform Measurement:Reference Levels:Channel Based Mid Ref Level

Specifies the mid reference level used in many scalar measurements. The default value is 50%.

Units: Percentage of the signal based on the selected [Percentage Units Method](pniscope-percentagemethod.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Chan. Based Mid Ref |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-chanbasedhighref.html language=enus -->
## TOPIC 00182: Waveform Measurement:Reference Levels:Channel Based High Ref Level

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-chanbasedhighref.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-chanbasedhighref.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the high reference level used in many scalar measurements. The default value is 90%. Units: Percentage of the signal based on the selected Percentage Units Method property. Remarks The following table lists the characteristics of this property. Short Name Chan Based High Ref Data type cdbl

### Waveform Measurement:Reference Levels:Channel Based High Ref Level

Specifies the high reference level used in many scalar measurements. The default value is 90%.

Units: Percentage of the signal based on the selected [Percentage Units Method](pniscope-percentagemethod.html)
 property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Chan Based High Ref |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-channelcount.html language=enus -->
## TOPIC 00183: Inherent IVI Attributes:Driver Capabilities:Channel Count

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-channelcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-channelcount.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of channels that the specific instrument driver supports. For channel based properties, the IVI engine maintains a separate cache value for each channel. Remarks The following table lists the characteristics of this property. Short Name Channel Count Data type ci32.png Permissio

### Inherent IVI Attributes:Driver Capabilities:Channel Count

Indicates the number of channels that the specific instrument driver supports. For channel based properties, the IVI engine maintains a separate cache value for each channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Channel Count |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-channelenabled.html language=enus -->
## TOPIC 00184: Vertical:Channel Enabled

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-channelenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-channelenabled.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the digitizer acquires a waveform for the channel. Remarks The following table lists the characteristics of this property. Short Name Channel Enabled Data type cbool.png Permissions Read/Write High-level VIs niScope Configure Vertical Channel-based Yes Resettable Yes

### Vertical:Channel Enabled

Specifies whether the digitizer acquires a waveform for the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Channel Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Vertical |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-classgroupcapabilities.html language=enus -->
## TOPIC 00185: Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-classgroupcapabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-classgroupcapabilities.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string that contains a comma-separated list of class-extension groups that this driver implements. Remarks The following table lists the characteristics of this property. Short Name Class Group Capabilities Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities

A string that contains a comma-separated list of class-extension groups that this driver implements.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Class Group Capabilities |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-classspecificationmajorversion.html language=enus -->
## TOPIC 00186: Inherent IVI Attributes:Driver Identification:Class Specification Major Version

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-classspecificationmajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-classspecificationmajorversion.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The major version number of the class specification with which this driver is compliant. Remarks The following table lists the characteristics of this property. Short Name Class Specification Major Version Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Inherent IVI Attributes:Driver Identification:Class Specification Major Version

The major version number of the class specification with which this driver is compliant.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Class Specification Major Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-classspecificationminorversion.html language=enus -->
## TOPIC 00187: Inherent IVI Attributes:Driver Identification:Class Specification Minor Version

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-classspecificationminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-classspecificationminorversion.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The minor version number of the class specification with which this driver is compliant. Remarks The following table lists the characteristics of this property. Short Name Class Specification Minor Version Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Inherent IVI Attributes:Driver Identification:Class Specification Minor Version

The minor version number of the class specification with which this driver is compliant.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Class Specification Minor Version |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-clocksyncpulsesource.html language=enus -->
## TOPIC 00188: Clocking:Clock Sync Pulse Source

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-clocksyncpulsesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-clocksyncpulsesource.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the line on which the sample clock or the one-time sync pulse is sent or received. This line should be the same for all devices to be synchronized. Defined Values VAL_NO_SOURCE VAL_RTSI_0 VAL_RTSI_1 VAL_RTSI_2 VAL_RTSI_3 VAL_RTSI_4 VAL_RTSI_5 VAL_RTSI_6 VAL_PFI_1 VAL_PFI_2 Remarks The foll

### Clocking:Clock Sync Pulse Source

Specifies the line on which the sample clock or the one-time sync pulse is sent or received.

This line should be the same for all devices to be synchronized.

**Defined Values**

VAL_NO_SOURCE

VAL_RTSI_0

VAL_RTSI_1

VAL_RTSI_2

VAL_RTSI_3

VAL_RTSI_4

VAL_RTSI_5

VAL_RTSI_6

VAL_PFI_1

VAL_PFI_2

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Clock Sync Pulse Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Clock |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-dataprocessingmode.html language=enus -->
## TOPIC 00189: Onboard Signal Processing:DDC:Data Processing Mode

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-dataprocessingmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-dataprocessingmode.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The way in which data is processed by the DDC block. The default value is Complex. This property can be used only with high-speed digitizers that support onboard signal processing (OSP). NI-SCOPE returns an error if you use this property with a device that does not support OSP. Remarks The following

### Onboard Signal Processing:DDC:Data Processing Mode

The way in which data is processed by the DDC block. The default value is Complex.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Processing Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

| Real | 0 | The waveform data points are real numbers (I data). |
| --- | --- | --- |
| Complex | 1 | The waveform data points are complex numbers (IQ data). |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-datatransferblocksize.html language=enus -->
## TOPIC 00190: Fetch:Data Transfer Block Size

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-datatransferblocksize.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-datatransferblocksize.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of samples to transfer at one time from the device to host memory. Increasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may also increase the amount of page

### Fetch:Data Transfer Block Size

Specifies the maximum number of samples to transfer at one time from the device to host memory. Increasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may also increase the amount of page-locked memory required from the system.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Data Transfer Block Size |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-ddcenabled.html language=enus -->
## TOPIC 00191: Onboard Signal Processing:DDC:DDC Enabled

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-ddcenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-ddcenabled.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables/disables the digital downconverter (DDC) block of the digitizer. When the DDC block is disabled, all DDC-related properties are disabled and have no effect on the acquired signal. The default value is FALSE. This property can be used only with high-speed digitizers that support onboard signa

### Onboard Signal Processing:DDC:DDC Enabled

Enables/disables the digital downconverter (DDC) block of the digitizer. When the DDC block is disabled, all DDC-related properties are disabled and have no effect on the acquired signal. The default value is FALSE.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DDC Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-description.html language=enus -->
## TOPIC 00192: Inherent IVI Attributes:Driver Identification:Description

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-description.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-description.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string that contains the description of the instrument. Remarks The following table lists the characteristics of this property. Short Name Description Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Inherent IVI Attributes:Driver Identification:Description

A string that contains the description of the instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Description |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-devicenumber.html language=enus -->
## TOPIC 00193: Device Specific:IF Digitizer:Device Number

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-devicenumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-devicenumber.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the device number of the IF digitizer associated with the current session. Remarks The following table lists the characteristics of this property. Short Name Device Number Data type ci32.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Device Specific:IF Digitizer:Device Number

Returns the device number of the IF digitizer associated with the current session.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Device Number |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-devicetemperature.html language=enus -->
## TOPIC 00194: Device:Temperature

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-devicetemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-devicetemperature.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature of the device in degrees Celsius from the onboard sensor. Related topics: Thermal Shutdown PXI/PXIe Chassis Cooling Remarks The following table lists the characteristics of this property. Short Name Device Temperature Data type cdbl.png Permissions Read Only High-level VIs N/

### Device:Temperature

Returns the temperature of the device in degrees Celsius from the onboard sensor.

**Related topics:**

- Thermal Shutdown
- PXI/PXIe Chassis Cooling

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Device Temperature |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-digitalgain.html language=enus -->
## TOPIC 00195: Vertical:Advanced:Digital Gain

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-digitalgain.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-digitalgain.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies gain to the specified channel in hardware before any onboard signal processing occurs. The default value is 1. The output of the digital gain/offset block is as follows: (ADC value × digital gain) + digital offset Units: Unitless Valid Values: -1.5 to 1.5 This property can be used only with

### Vertical:Advanced:Digital Gain

Applies gain to the specified channel in hardware before any onboard signal processing occurs. The default value is 1.

The output of the digital gain/offset block is as follows:

(*ADC value* × *digital gain*) + *digital offset*

Units: Unitless

Valid Values: -1.5 to 1.5

Note

**Related topics:**

- NI 5622 Onboard Signal Processing (OSP)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Gain |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-digitaloffset.html language=enus -->
## TOPIC 00196: Vertical:Advanced:Digital Offset

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-digitaloffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-digitaloffset.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies offset to the specified channel in hardware before any onboard signal processing occurs. The default value is 0. Units: Volts Valid Values ±(Vertical Range × 0.4) The output of the digital gain/offset block is as follows: (ADC value × digital gain) + digital offset This property can be used

### Vertical:Advanced:Digital Offset

Applies offset to the specified channel in hardware before any onboard signal processing occurs. The default value is 0.

Units: Volts

**Valid Values**

±(Vertical Range × 0.4)

The output of the digital gain/offset block is as follows:

(*ADC value* × *digital gain*) + *digital offset*

Note

**Related topics:**

- NI 5622 Onboard Signal Processing (OSP)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-ditherenabled.html language=enus -->
## TOPIC 00197: Vertical:Advanced:Dither Enabled

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-ditherenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-ditherenabled.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables the analog dither on the device. Using dither can improve the spectral performance of the device by reducing the effects of quantization. However, adding dither increases the power level to the ADC, so you may need to either decrease the signal level or increase the vertical rang

### Vertical:Advanced:Dither Enabled

Enables or disables the analog dither on the device. Using dither can improve the spectral performance of the device by reducing the effects of quantization. However, adding dither increases the power level to the ADC, so you may need to either decrease the signal level or increase the vertical range. The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Dither Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-driverprefix.html language=enus -->
## TOPIC 00198: Inherent IVI Attributes:Driver Identification:Driver Prefix

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-driverprefix.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-driverprefix.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string that contains the prefix for the instrument driver. The name of each user-callable function in this driver starts with this prefix. Remarks The following table lists the characteristics of this property. Short Name Driver Prefix Data type cstr.png Permissions Read Only High-level VIs N/A Ch

### Inherent IVI Attributes:Driver Identification:Driver Prefix

A string that contains the prefix for the instrument driver. The name of each user-callable function in this driver starts with this prefix.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Driver Prefix |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-drivervendor.html language=enus -->
## TOPIC 00199: Inherent IVI Attributes:Driver Identification:Driver Vendor

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-drivervendor.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-drivervendor.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string that contains the name of the vendor that supplies this driver, for example, "National Instruments". Remarks The following table lists the characteristics of this property. Short Name Driver Vendor Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Inherent IVI Attributes:Driver Identification:Driver Vendor

A string that contains the name of the vendor that supplies this driver, for example, "National Instruments".

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Driver Vendor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-enabledchannels.html language=enus -->
## TOPIC 00200: Acquisition:Enabled Channels

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-enabledchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-enabledchannels.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a comma-separated list of the channels enabled for the session in ascending order. Property-Specific Syntax If no channels are enabled, this property returns an empty string, "". If all channels are enabled, this property enumerates all of the channels. Because this property returns channels

### Acquisition:Enabled Channels

Returns a comma-separated list of the channels enabled for the session in ascending order.

**Property-Specific Syntax**

- If no channels are enabled, this property returns an empty string, "".
- If all channels are enabled, this property enumerates all of the channels.

Note

channels

Channel String Syntax

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enabled Channels |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-enabledcrestore.html language=enus -->
## TOPIC 00201: Triggering:Trigger Video:Enable DC Restore

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-enabledcrestore.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-enabledcrestore.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Restores the video-triggered data retrieved by the digitizer to the video signal's zero reference point. The default value is FALSE. Remarks The following table lists the characteristics of this property. Short Name Enable DC Restore Data type cbool.png Permissions Read/Write High-level VIs niScope

### Triggering:Trigger Video:Enable DC Restore

Restores the video-triggered data retrieved by the digitizer to the video signal's zero reference point. The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enable DC Restore |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Trigger Video (Video Ref Trigger) |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-enablerecordsmemory.html language=enus -->
## TOPIC 00202: Horizontal:Enable Records > Memory

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-enablerecordsmemory.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-enablerecordsmemory.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allows you to acquire more records than fit in onboard memory. TRUE—Enables NI-SCOPE to fetch more records than fit in memory FALSE—Disables NI-SCOPE from fetching more records than fit in memory The property can be used only in digitizers that support continuous acquisition. Refer to Features Suppo

### Horizontal:Enable Records > Memory

Allows you to acquire more records than fit in onboard memory.

TRUE—Enables NI-SCOPE to fetch more records than fit in memory

FALSE—Disables NI-SCOPE from fetching more records than fit in memory

Note

Features Supported by Device

**Related topics:**

- Time Interleaved Sampling

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enable Records > Memory |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-enablerisinautosetup.html language=enus -->
## TOPIC 00203: Acquisition:Advanced:Enable RIS in Auto Setup

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-enablerisinautosetup.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-enablerisinautosetup.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the digitizer should use RIS sample rates when searching for a frequency in autosetup. Remarks The following table lists the characteristics of this property. Short Name Enable RIS in Auto Setup Data type cbool.png Permissions Read/Write High-level VIs N/A Channel-based No Resettab

### Acquisition:Advanced:Enable RIS in Auto Setup

Indicates whether the digitizer should use RIS sample rates when searching for a frequency in autosetup.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enable RIS in Auto Setup |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-enabletdc.html language=enus -->
## TOPIC 00204: Horizontal:Advanced:Enable TDC

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-enabletdc.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-enabletdc.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies that the digitizer should record the trigger position precisely using time-digital conversion (TDC). Related topics: TDC Remarks The following table lists the characteristics of this property. Short Name Enable TDC Data type cbool.png Permissions Read/Write High-level VIs N/A Channel-based

### Horizontal:Advanced:Enable TDC

Specifies that the digitizer should record the trigger position precisely using time-digital conversion (TDC).

**Related topics:**

- TDC

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enable TDC |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-enabletis.html language=enus -->
## TOPIC 00205: Horizontal:Enable Time Interleaved Sampling

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-enabletis.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-enabletis.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extends the maximum sample rate on the specified Active Channel for some devices that support Time Interleaved Sampling (TIS). TIS enables the device to use multiple ADCs to sample the same waveform at a higher effective real-time rate. NI 5152/5153/5154 devices fully support Read/Write ability for

### Horizontal:Enable Time Interleaved Sampling

Extends the maximum sample rate on the specified Active Channel for some devices that support Time Interleaved Sampling (TIS). TIS enables the device to use multiple ADCs to sample the same waveform at a higher effective real-time rate. NI 5152/5153/5154 devices fully support Read/Write ability for this property. For other devices that use TIS mode, such as the NI 5185/5186, this property is Read Only.

**Related topics:**

- Time Interleaved Sampling
- Configuring the Horizontal Settings

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enable TIS |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-endofacqevent-outputterm.html language=enus -->
## TOPIC 00206: Synchronization:End of Acquisition:Output Terminal

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-endofacqevent-outputterm.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-endofacqevent-outputterm.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination for the End of Acquisition event. When this event is asserted, the digitizer has completed sampling all records. Refer to the device specifications document for a list of valid destinations. Defined Values VAL_RTSI_0 VAL_RTSI_1 VAL_RTSI_2 VAL_RTSI_3 VAL_RTSI_4 VAL_RTSI_5 VA

### Synchronization:End of Acquisition:Output Terminal

Specifies the destination for the End of Acquisition event. When this event is asserted, the digitizer has completed sampling all records. Refer to the device specifications document for a list of valid destinations.

**Defined Values**

VAL_RTSI_0

VAL_RTSI_1

VAL_RTSI_2

VAL_RTSI_3

VAL_RTSI_4

VAL_RTSI_5

VAL_RTSI_6

VAL_PFI_0

VAL_PFI_1

VAL_PFI_2

VAL_PFI_3

VAL_PFI_4

VAL_PFI_5

VAL_PFI_6

VAL_PFI_7

VAL_PXI_STAR

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | EndOfAcqEvent.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Export Signal |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-endofacquisitioneventterminalname.html language=enus -->
## TOPIC 00207: Synchronization:End of Acquisition:Terminal Name

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-endofacquisitioneventterminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-endofacquisitioneventterminalname.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified name for the End of Acquisition Event terminal. You can use this terminal as the source for a trigger. Remarks The following table lists the characteristics of this property. Short Name End of Acquisition Event Terminal Name Data type cstr.png Permissions Read Only High-l

### Synchronization:End of Acquisition:Terminal Name

Returns the fully qualified name for the End of Acquisition Event terminal.

You can use this terminal as the source for a trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | End of Acquisition Event Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-endofrecevent-outputterm.html language=enus -->
## TOPIC 00208: Synchronization:End of Record:Output Terminal

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-endofrecevent-outputterm.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-endofrecevent-outputterm.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination for the End of Record event. When this event is asserted, the digitizer has completed sampling a record. Refer to the device specifications document for a list of valid destinations. Defined Values VAL_RTSI_0 VAL_RTSI_1 VAL_RTSI_2 VAL_RTSI_3 VAL_RTSI_4 VAL_RTSI_5 VAL_RTSI_6

### Synchronization:End of Record:Output Terminal

Specifies the destination for the End of Record event. When this event is asserted, the digitizer has completed sampling a record. Refer to the device specifications document for a list of valid destinations.

**Defined Values**

VAL_RTSI_0

VAL_RTSI_1

VAL_RTSI_2

VAL_RTSI_3

VAL_RTSI_4

VAL_RTSI_5

VAL_RTSI_6

VAL_PFI_0

VAL_PFI_1

VAL_PFI_2

VAL_PFI_3

VAL_PFI_4

VAL_PFI_5

VAL_PFI_6

VAL_PFI_7

VAL_PXI_STAR

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | EndOfRecEvent.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Export Signal |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-endofrecordeventterminalname.html language=enus -->
## TOPIC 00209: Synchronization:End of Record:Terminal Name

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-endofrecordeventterminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-endofrecordeventterminalname.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified name for the End of Record Event terminal. You can use this terminal as the source for a trigger. Remarks The following table lists the characteristics of this property. Short Name End of Record Event Terminal Name Data type cstr.png Permissions Read Only High-level VIs N

### Synchronization:End of Record:Terminal Name

Returns the fully qualified name for the End of Record Event terminal.

You can use this terminal as the source for a trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | End of Record Event Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-enforcerealtime.html language=enus -->
## TOPIC 00210: Horizontal:Enforce Realtime

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-enforcerealtime.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-enforcerealtime.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the digitizer enforces real-time measurements or allows equivalent-time measurements. Related topics: Sampling Methods Real-Time Sampling Remarks The following table lists the characteristics of this property. Short Name Enforce Realtime Data type cbool.png Permissions Read/Write H

### Horizontal:Enforce Realtime

Indicates whether the digitizer enforces real-time measurements or allows equivalent-time measurements.

**Related topics:**

- Sampling Methods
- Real-Time Sampling

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Enforce Realtime |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Horizontal Timing |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-equalizationfilterenabled.html language=enus -->
## TOPIC 00211: Onboard Signal Processing:Equalization:Equalization Filter Enabled

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-equalizationfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-equalizationfilterenabled.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the onboard signal processing equalization FIR block, which is connected directly to the input signal. The equalization filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coeffici

### Onboard Signal Processing:Equalization:Equalization Filter Enabled

Enables the onboard signal processing equalization FIR block, which is connected directly to the input signal. The equalization filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and -1. The default value is FALSE.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Equalization Filter Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-equalizationnumcoefficients.html language=enus -->
## TOPIC 00212: Onboard Signal Processing:Equalization:Equalization Num Coefficients

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-equalizationnumcoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-equalizationnumcoefficients.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of coefficients that the equalization FIR filter can accept. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should b

### Onboard Signal Processing:Equalization:Equalization Num Coefficients

Returns the number of coefficients that the equalization FIR filter can accept. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and -1.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Equalization Num Coefficients |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-exportedsampleclockoutputterminal.html language=enus -->
## TOPIC 00213: Clocking:Exported Sample Clock Output Terminal

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-exportedsampleclockoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-exportedsampleclockoutputterminal.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the sample clock to a specified terminal. This property is not supported by all digitizers. The full sample clock rate can be exported to the CLK_OUT connector. If decimating, the divided down sample clock rate can be exported to any of the valid destinations. Defined Values VAL_CLK_OUT VAL_

### Clocking:Exported Sample Clock Output Terminal

Exports the sample clock to a specified terminal. This property is not supported by all digitizers.

The full sample clock rate can be exported to the CLK_OUT connector. If decimating, the divided down sample clock rate can be exported to any of the valid destinations.

**Defined Values**

VAL_CLK_OUT

VAL_RTSI_0

VAL_RTSI_1

VAL_RTSI_2

VAL_RTSI_3

VAL_RTSI_4

VAL_RTSI_5

VAL_RTSI_6

VAL_PXI_STAR

VAL_PFI_0

VAL_PFI_1

VAL_PFI_2

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Sample Clock Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Export Signal |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-fetchbacklog.html language=enus -->
## TOPIC 00214: Fetch:Fetch Backlog

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-fetchbacklog.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-fetchbacklog.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of points acquired that have not been fetched yet. Related topics: Fetching Data Remarks The following table lists the characteristics of this property. Short Name Fetch Backlog Data type cdbl.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Fetch:Fetch Backlog

Specifies the number of points acquired that have not been fetched yet.

**Related topics:**

- Fetching Data

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fetch Backlog |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-fetchinterleaveddata.html language=enus -->
## TOPIC 00215: Device Specific:IF Digitizer:Fetch Interleaved Data

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-fetchinterleaveddata.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-fetchinterleaveddata.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to interleave I and Q data retrieved from the IF digitizer in a single array or to retrieve two separate arrays, one for I data and another for Q data. Default Value: FALSE TRUE Retrieves a single array of alternating I and Q values. The resulting array is twice the size of the act

### Device Specific:IF Digitizer:Fetch Interleaved Data

Specifies whether to interleave I and Q data retrieved from the IF digitizer in a single array or to retrieve two separate arrays, one for I data and another for Q data.

Default Value: FALSE

| TRUE | Retrieves a single array of alternating I and Q values. The resulting array is twice the size of the actual record length. |
| --- | --- |
| FALSE | Retrieves two arrays, one for I values and another for Q values. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fetch Interleaved Data |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-fetchinterleavediqdata.html language=enus -->
## TOPIC 00216: Onboard Signal Processing:DDC:Fetch Interleaved IQ Data

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-fetchinterleavediqdata.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-fetchinterleavediqdata.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether a fetch call retrieves a single waveform with I and Q interleaved, or two separate waveforms. If enabled, the number of elements returned by scalar fetch types (such as 16-bit integer) is twice the requested number of samples. If disabled during DDC acquisitions in Complex mode, tw

### Onboard Signal Processing:DDC:Fetch Interleaved IQ Data

Specifies whether a fetch call retrieves a single waveform with I and Q interleaved, or two separate waveforms. If enabled, the number of elements returned by scalar fetch types (such as 16-bit integer) is twice the requested number of samples. If disabled during DDC acquisitions in Complex mode, two noninterleaved arrays of data are returned per channel, per record.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fetch Interleaved IQ Data |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-fetchmeasnumberofsamples.html language=enus -->
## TOPIC 00217: Fetch:Fetch Meas Num Samples

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-fetchmeasnumberofsamples.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-fetchmeasnumberofsamples.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the number of samples to fetch from a digitizer when performing a measurement. -1 means fetch all samples from the Fetch Offset property to the end of the current record. The default value is -1. Remarks The following table lists the characteristics of this property. Short Name Fetch Meas

### Fetch:Fetch Meas Num Samples

Determines the number of samples to fetch from a digitizer when performing a measurement. -1 means fetch all samples from the [Fetch Offset](/csh?topicname=pniscope-fetchoffset.html) property to the end of the current record. The default value is -1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fetch Meas Number of Samples |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-fetchnumberofrecords.html language=enus -->
## TOPIC 00218: Fetch:Fetch Number of Records

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-fetchnumberofrecords.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-fetchnumberofrecords.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches multiple records. If you want to fetch all records from the record you specify in the Fetch Record Number property to the last record configured, use -1. The default value is -1. Related topics: Making Multiple-Record Acquisitions Fetching Multiple-Record Acquisitions Remarks The following t

### Fetch:Fetch Number of Records

Fetches multiple records. If you want to fetch all records from the record you specify in the
 [Fetch Record Number](/csh?topicname=pniscope-fetchrecordnumber.html) property to the last record configured, use -1. The default value is -1.

**Related topics:**

- Making Multiple-Record Acquisitions
- Fetching Multiple-Record Acquisitions

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fetch Number of Records |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-fetchoffset.html language=enus -->
## TOPIC 00219: Fetch:Fetch Offset

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-fetchoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-fetchoffset.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the offset in samples; the samples returned also depend on the Fetch Relative To property. The default value is 0. Valid Values: All integers Remarks The following table lists the characteristics of this property. Short Name Fetch Offset Data type ci32.png Permissions Read/Write High-level VIs

### Fetch:Fetch Offset

Sets the offset in samples; the samples returned also depend on the
[Fetch Relative To](/csh?topicname=pniscope-fetchrelativeto.html) property. The default value is 0.

Valid Values: All integers

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fetch Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-fetchrecordnumber.html language=enus -->
## TOPIC 00220: Fetch:Fetch Record Number

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-fetchrecordnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-fetchrecordnumber.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the record to fetch. The record is from a channel you specify. The default value is 0. Valid Values: Values greater than or equal to 0 Remarks The following table lists the characteristics of this property. Short Name Fetch Record Number Data type ci32.png Permissions Read/Write High-level VIs

### Fetch:Fetch Record Number

Sets the record to fetch. The record is from a channel you specify. The default value is 0.

Valid Values: Values greater than or equal to 0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fetch Record Number |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-fetchrelativeto.html language=enus -->
## TOPIC 00221: Fetch:Fetch Relative To

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-fetchrelativeto.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-fetchrelativeto.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which point in the acquired waveform is the first to be fetched. This property specifies what the 'Fetch Offset' is relative to. Remarks The following table lists the characteristics of this property. Short Name Fetch Relative To Data type ci32.png Permissions Read/Write High-level VIs N/A

### Fetch:Fetch Relative To

Specifies which point in the acquired waveform is the first to be fetched. This property specifies what the 'Fetch Offset' is relative to.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fetch Relative To |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

| Start | 482 | Fetch data starting at the first point sampled by the digitizer. |
| --- | --- | --- |
| Trigger | 483 | Fetch at the first posttrigger sample. |
| Pretrigger | 477 | Fetches relative to the first pretrigger point requested with the niScope Configure Horizontal Timing VI. |
| Now | 481 | Fetch data at the last sample acquired. |
| Read Pointer | 388 | The read pointer is set to zero when a new acquisition is initiated. After every fetch the read pointer is incremented to be the sample after the last sample retrieved. Therefore, you can repeatedly fetch relative to the read pointer for a continuous acquisition program. |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-filtercenterfrequency.html language=enus -->
## TOPIC 00222: Waveform Measurement:Filter:Center Frequency

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-filtercenterfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-filtercenterfrequency.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The center frequency in hertz for filters of type bandpass and bandstop. The width of the filter is specified by Filter Width, where the cutoff frequencies are the center width. The default value is 1.0e6 Hz. Remarks The following table lists the characteristics of this property. Short Name Filter C

### Waveform Measurement:Filter:Center Frequency

The center frequency in hertz for filters of type bandpass and bandstop. The width of the filter is specified by Filter Width, where the cutoff frequencies are the center width. The default value is 1.0e6 Hz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Filter Center Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-filtercutofffrequency.html language=enus -->
## TOPIC 00223: Waveform Measurement:Filter:Cutoff Frequency

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-filtercutofffrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-filtercutofffrequency.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the cutoff frequency in hertz for filters of type lowpass and highpass. The cutoff frequency definition varies depending on the filter. The default value is 1.0e6 Hz. Remarks The following table lists the characteristics of this property. Short Name Filter Cutoff Frequency Data type cdbl.p

### Waveform Measurement:Filter:Cutoff Frequency

Specifies the cutoff frequency in hertz for filters of type lowpass and highpass. The cutoff frequency definition varies depending on the filter. The default value is 1.0e6 Hz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Filter Cutoff Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-filterorder.html language=enus -->
## TOPIC 00224: Waveform Measurement:Filter:IIR Order

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-filterorder.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-filterorder.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the order of the infinite impulse response filter. The default value is 2. Valid Values: >0 Remarks The following table lists the characteristics of this property. Short Name Filter Order Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable No

### Waveform Measurement:Filter:IIR Order

Specifies the order of the infinite impulse response filter. The default value is 2.

Valid Values: >0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Filter Order |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-filterripple.html language=enus -->
## TOPIC 00225: Waveform Measurement:Filter:Ripple

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-filterripple.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-filterripple.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of passband ripple (in dB) for Chebyshev filters. More ripple gives a sharper cutoff for a given filter order. The default value is 0.1. Valid Values: >0.0 Remarks The following table lists the characteristics of this property. Short Name Filter Ripple Data type cdbl.png Permiss

### Waveform Measurement:Filter:Ripple

Specifies the amount of passband ripple (in dB) for Chebyshev filters. More ripple gives a sharper cutoff for a given filter order. The default value is 0.1.

Valid Values: >0.0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Filter Ripple |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-filtertaps.html language=enus -->
## TOPIC 00226: Waveform Measurement:Filter:FIR Taps

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-filtertaps.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-filtertaps.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of taps for the finite impulse response filter. This value must be odd if the filter type is highpass or bandstop. Otherwise, the magnitude response goes to zero as the frequency goes to half the sampling rate. The default value is 25. Valid Values: >0 Remarks The following tabl

### Waveform Measurement:Filter:FIR Taps

Specifies the number of taps for the finite impulse response filter. This value must be odd if the filter type is highpass or bandstop. Otherwise, the magnitude response goes to zero as the frequency goes to half the sampling rate. The default value is 25.

Valid Values: >0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Filter Taps |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-filtertype.html language=enus -->
## TOPIC 00227: Waveform Measurement:Filter:Type

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-filtertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-filtertype.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of digital filter. The default value is lowpass. Remarks The following table lists the characteristics of this property. Short Name Filter Type Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable No lowpass 0 Specifies lowpass as the filter typ

### Waveform Measurement:Filter:Type

Specifies the type of digital filter. The default value is lowpass.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Filter Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

| lowpass | 0 | Specifies lowpass as the filter type. |
| --- | --- | --- |
| highpass | 1 | Specifies highpass as the filter type. |
| bandpass | 2 | Specifies bandpass as the filter type. |
| bandstop | 3 | Specifies bandstop as the filter type. |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-filterwidth.html language=enus -->
## TOPIC 00228: Waveform Measurement:Filter:Width

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-filterwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-filterwidth.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width (in Hz) of a bandpass or bandstop filter. The cutoff frequencies are the (center frequency property ± 0.5 × filter width). The default value is 1.0e3. Remarks The following table lists the characteristics of this property. Short Name Filter Width Data type cdbl.png Permissions Re

### Waveform Measurement:Filter:Width

Specifies the width (in Hz) of a bandpass or bandstop filter. The cutoff frequencies are the (center frequency property ± 0.5 × filter width). The default value is 1.0e3.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Filter Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-firfilterwindow.html language=enus -->
## TOPIC 00229: Waveform Measurement:Filter:FIR Window

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-firfilterwindow.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-firfilterwindow.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FIR window type. The symmetric windows are applied to the FIR filter coefficients to limit passband ripple in FIR filters. The default value is None (0). Remarks The following table lists the characteristics of this property. Short Name FIR Filter Window Data type ci32.png Permissions

### Waveform Measurement:Filter:FIR Window

Specifies the FIR window type. The symmetric windows are applied to the FIR filter coefficients to limit passband ripple in FIR filters. The default value is None (0).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FIR Filter Window |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

| None | 0 | No window. |
| --- | --- | --- |
| Hanning | 409 | Specifies a Hanning window. |
| Hamming | 420 | Specifies a Hamming window. |
| Flat Top | 410 | Specifies a Flat Top window. |
| Triangle | 423 | Specifies a Triangle window. |
| Blackman | 424 | Specifies a Blackman window. |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-firmwarerevision.html language=enus -->
## TOPIC 00230: Inherent IVI Attributes:Instrument Identification:Firmware Revision

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-firmwarerevision.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-firmwarerevision.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string that contains the firmware revision information for the current instrument. Remarks The following table lists the characteristics of this property. Short Name Firmware Revision Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Inherent IVI Attributes:Instrument Identification:Firmware Revision

A string that contains the firmware revision information for the current instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Firmware Revision |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-flexfirantialiasfiltertype.html language=enus -->
## TOPIC 00231: Vertical:Advanced:Flex FIR Antialias Filter Type

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-flexfirantialiasfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-flexfirantialiasfiltertype.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass antialias filter. Use this property to select from several types of filters to achieve desired filtering characteristics. For most applications, the default value of this property is recommended. The other available filters are us

### Vertical:Advanced:Flex FIR Antialias Filter Type

The NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass antialias filter. Use this property to select from several types of filters to achieve desired filtering characteristics. For most applications, the default value of this property is recommended. The other available filters are useful for optimizing settling time measurements of step responses. The default value is 48 Tap Standard.

Note

NI PXI-5922 Specifications

**Related topics:**

- Aliasing
- FIR Filters

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Flex FIR Antialias Filter Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

| 48 Tap Standard | 0 | 48 Tap Standard filter is optimized for alias protection and frequency-domain flatness. |
| --- | --- | --- |
| 48 Tap Hanning | 1 | 48 Tap Hanning filter is optimized for the lowest possible bandwidth for a 48 tap filter and maximizes the SNR. |
| 16 Tap Hanning | 2 | 16 Tap Hanning is optimized for the lowest possible bandwidth for a 16 tap filter and maximizes the SNR. |
| 8 Tap Hanning | 3 | 8 Tap Hanning filter is optimized for the lowest possible bandwidth for a 8 tap filter and maximizes the SNR. |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-fpgabitfilepath.html language=enus -->
## TOPIC 00232: Device:FPGA Bitfile Path

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-fpgabitfilepath.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-fpgabitfilepath.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the absolute file path to the bitfile loaded on the FPGA. Gets the absolute file path to the bitfile loaded on the FPGA. Remarks The following table lists the characteristics of this property. Short Name FPGA Bitfile Path Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based

### Device:FPGA Bitfile Path

Gets the absolute file path to the bitfile loaded on the FPGA.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FPGA Bitfile Path |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-fractionalresampleenabled.html language=enus -->
## TOPIC 00233: Onboard Signal Processing:Fractional Resample:Fractional Resample Enabled

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-fractionalresampleenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-fractionalresampleenabled.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the onboard signal processing block that resamples the input waveform to the user desired sample rate. The default value is FALSE. This property can be used only with high-speed digitizers that support onboard signal processing (OSP). NI-SCOPE returns an error if you use this property with a

### Onboard Signal Processing:Fractional Resample:Fractional Resample Enabled

Enables the onboard signal processing block that resamples the input waveform to the user desired sample rate. The default value is FALSE.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Fractional Resample Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-frequencytranslationenabled.html language=enus -->
## TOPIC 00234: Onboard Signal Processing:DDC:Frequency Translation Enabled

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-frequencytranslationenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-frequencytranslationenabled.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables/disables frequency translating the data around the user-selected center frequency down to baseband. The default value is TRUE. This property can be used only with high-speed digitizers that support onboard signal processing (OSP). NI-SCOPE returns an error if you use this property with a dev

### Onboard Signal Processing:DDC:Frequency Translation Enabled

Enables/disables frequency translating the data around the user-selected center frequency down to baseband. The default value is TRUE.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frequency Translation Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-frequencytranslationphasei.html language=enus -->
## TOPIC 00235: Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase I

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-frequencytranslationphasei.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-frequencytranslationphasei.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The I oscillator phase in degrees at the first point acquired. The default value is 0. Valid Values -360 to 360 This property can be used only with high-speed digitizers that support onboard signal processing (OSP). NI-SCOPE returns an error if you use this property with a device that does not suppo

### Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase I

The I oscillator phase in degrees at the first point acquired. The default value is 0.

**Valid Values**

-360 to 360

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frequency Translation Phase I |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-frequencytranslationphaseq.html language=enus -->
## TOPIC 00236: Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase Q

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-frequencytranslationphaseq.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-frequencytranslationphaseq.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Q oscillator phase in degrees at the first point acquired. Use this property only when the Data Processing Mode property is set to Complex. The default value is 90. Valid Values -360 to 360 This property can be used only with high-speed digitizers that support onboard signal processing (OSP). NI

### Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase Q

The Q oscillator phase in degrees at the first point acquired. Use this property only when the
 [Data Processing Mode](/csh?topicname=pniscope-dataprocessingmode.html) property is set to Complex. The default value is 90.

**Valid Values**

-360 to 360

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frequency Translation Phase Q |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-glitchcondition.html language=enus -->
## TOPIC 00237: Triggering:Trigger Glitch:Glitch Condition

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-glitchcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-glitchcondition.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the oscilloscope triggers on pulses of duration less than or greater than the specified Glitch Width. Default Value: Greater Than Remarks The following table lists the characteristics of this property. Short Name Glitch Condition Data type ci32.png Permissions Read/Write High-level

### Triggering:Trigger Glitch:Glitch Condition

Specifies whether the oscilloscope triggers on pulses of duration less than or greater than the specified [Glitch Width](/csh?topicname=pniscope-glitchwidth.html).

Default Value: Greater Than

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Glitch Condition |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Trigger Glitch (Glitch Trigger) |
| Channel-based | No |
| Resettable | No |

| Less Than | 1 | The oscilloscope triggers on pulses with a duration shorter than the specified glitch width. |
| --- | --- | --- |
| Greater Than | 2 | The oscilloscope triggers on pulses with a duration longer than the specified glitch width. |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-glitchpolarity.html language=enus -->
## TOPIC 00238: Triggering:Trigger Glitch:Glitch Polarity

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-glitchpolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-glitchpolarity.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of pulses that trigger the oscilloscope for glitch triggering. Default Value: Positive Remarks The following table lists the characteristics of this property. Short Name Glitch Polarity Data type ci32.png Permissions Read/Write High-level VIs niScope Configure Trigger Glitch (

### Triggering:Trigger Glitch:Glitch Polarity

Specifies the polarity of pulses that trigger the oscilloscope for glitch triggering.

Default Value: Positive

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Glitch Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Trigger Glitch (Glitch Trigger) |
| Channel-based | No |
| Resettable | No |

| Positive | 1 | The oscilloscope triggers on pulses of positive polarity relative to the trigger threshold. |
| --- | --- | --- |
| Negative | 2 | The oscilloscope triggers on pulses of negative polarity relative to the trigger threshold. |
| Either | 3 | The oscilloscope triggers on pulses of either positive or negative polarity. |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-glitchwidth.html language=enus -->
## TOPIC 00239: Triggering:Trigger Glitch:Glitch Width

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-glitchwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-glitchwidth.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the glitch duration, in seconds. The oscilloscope triggers when it detects a pulse of duration either less than or greater than this value depending on the value of the Glitch Condition property. Default Value: 0.0 Remarks The following table lists the characteristics of this property. Sho

### Triggering:Trigger Glitch:Glitch Width

Specifies the glitch duration, in seconds.

The oscilloscope triggers when it detects a pulse of duration either less than or greater than this value depending on the value of the [Glitch Condition](pniscope-glitchcondition.html) property.

Default Value: 0.0

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Glitch Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Trigger Glitch (Glitch Trigger) |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-highpassfilterfrequency.html language=enus -->
## TOPIC 00240: Vertical:Advanced:High Pass Filter Frequency

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-highpassfilterfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-highpassfilterfrequency.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency for the highpass filter in Hz. The device uses one of the valid values listed below. If an invalid value is specified, no coercion occurs. The default value is 0. (PXIe-5164) Valid Values: 0 90 450 Related topics: Digital Filtering Remarks The following table lists the charac

### Vertical:Advanced:High Pass Filter Frequency

Specifies the frequency for the highpass filter in Hz. The device uses one of the valid values listed below. If an invalid value is specified, no coercion occurs. The default value is 0.

**(PXIe-5164) Valid Values:**

- 0
- 90
- 450

**Related topics:**

- Digital Filtering

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | High Pass Filter Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-hysteresispercent.html language=enus -->
## TOPIC 00241: Waveform Measurement:Hysteresis Percent

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-hysteresispercent.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-hysteresispercent.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Digital hysteresis that is used in several of the scalar waveform measurements. This property specifies the percentage of the full-scale vertical range for the hysteresis window size. The default value is 2%. Remarks The following table lists the characteristics of this property. Short Name Hysteres

### Waveform Measurement:Hysteresis Percent

Digital hysteresis that is used in several of the scalar waveform measurements. This property specifies the percentage of the full-scale vertical range for the hysteresis window size. The default value is 2%.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Hysteresis Percent |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-inputimpedance.html language=enus -->
## TOPIC 00242: Vertical:Input Impedance

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-inputimpedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-inputimpedance.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input impedance for the channel in ohms. Defined Values 50 Ohm 1 M Ohm Related topics: Impedance and Impedance Matching Remarks The following table lists the characteristics of this property. Short Name Input Impedance Data type cdbl.png Permissions Read/Write High-level VIs niScope Co

### Vertical:Input Impedance

Specifies the input impedance for the channel in ohms.

**Defined Values**

50 Ohm

1 M Ohm

**Related topics:**

- Impedance and Impedance Matching

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Input Impedance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Chan Characteristics |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-interchangecheck.html language=enus -->
## TOPIC 00243: Inherent IVI Attributes:User Options:Interchange Check

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-interchangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-interchangecheck.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to perform interchangeability checking and log interchangeability warnings when you call VIs. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. Remarks The following table lists the characteristics of this p

### Inherent IVI Attributes:User Options:Interchange Check

Specifies whether to perform interchangeability checking and log interchangeability warnings when you call VIs. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Interchange Check |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-interleavingoffsetcorrectionenabled.html language=enus -->
## TOPIC 00244: Vertical:Advanced:Interleaving Offset Correction Enabled

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-interleavingoffsetcorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-interleavingoffsetcorrectionenabled.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the interleaving offset correction on the specified channel. The default value is TRUE. If disabled, warranted specifications are not guaranteed. Related topics: Timed Interleaved Sampling Remarks The following table lists the characteristics of this property. Short Name Interleaving Offset

### Vertical:Advanced:Interleaving Offset Correction Enabled

Enables the interleaving offset correction on the specified channel. The default value is TRUE.

Note

**Related topics:**

- Timed Interleaved Sampling

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Interleaving Offset Correction Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-interp-samplingfactor.html language=enus -->
## TOPIC 00245: Waveform Measurement:Interpolation:Sampling Factor

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-interp-samplingfactor.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-interp-samplingfactor.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The new number of points for polynomial interpolation is the sampling factor times the input number of points. The default value is 0.0. For example, if you acquire 1,000 points with the digitizer and set this property to 2.5, calling the niScope Fetch Measurement (poly) VI (Measurement Scalar DBL i

### Waveform Measurement:Interpolation:Sampling Factor

The new number of points for polynomial interpolation is the sampling factor times the input number of points. The default value is 0.0.

For example, if you acquire 1,000 points with the digitizer and set this property to 2.5, calling the [niScope Fetch Measurement (poly)](/csh?context=niscope_scopeviref_niscope_fetch_measurement_(poly)) VI
 (Measurement Scalar DBL instance), with the Polynomial Interpolation measurement resamples the waveform to 2,500 points.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Interp. Sampling Factor |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-lastacq-histogramsize.html language=enus -->
## TOPIC 00246: Waveform Measurement:Last Acq. Histogram Size

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-lastacq-histogramsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-lastacq-histogramsize.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the size (that is, the number of bins) in the last acquisition histogram. This histogram is used to determine several scalar measurements, most importantly voltage low and voltage high. The default value is 256. Remarks The following table lists the characteristics of this property. Short

### Waveform Measurement:Last Acq. Histogram Size

Specifies the size (that is, the number of bins) in the last acquisition histogram. This histogram is used to determine several scalar measurements, most importantly voltage low and voltage high. The default value is 256.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Last Acq. Histogram Size |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-logicalname.html language=enus -->
## TOPIC 00247: Inherent IVI Attributes:Advanced Session Information:Logical Name

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-logicalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-logicalname.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string that contains the logical name you specified when opening the current IVI session. You can pass a logical name to niScope Initialize or niScope Initialize with Options. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instr

### Inherent IVI Attributes:Advanced Session Information:Logical Name

A string that contains the logical name you specified when opening the current IVI session.

You can pass a logical name to [niScope Initialize](/csh?context=niscope_scopeviref_niscope_initialize) or [niScope Initialize with Options](/csh?context=niscope_scopeviref_niscope_initialize_with_options). The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI Configuration file. The virtual instrument section specifies a physical device and initial user options.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logical Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-manufacturer.html language=enus -->
## TOPIC 00248: Inherent IVI Attributes:Instrument Identification:Manufacturer

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-manufacturer.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-manufacturer.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A string that contains the name of the instrument manufacturer, for example, "National Instruments". Remarks The following table lists the characteristics of this property. Short Name Manufacturer Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Inherent IVI Attributes:Instrument Identification:Manufacturer

A string that contains the name of the instrument manufacturer, for example, "National Instruments".

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Manufacturer |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-masterenable.html language=enus -->
## TOPIC 00249: Synchronization:Master Enable

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-masterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-masterenable.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device is a master or a slave. The master device is typically the originator of the trigger signal and clock sync pulse. For a stand-alone device, set this property to FALSE. Valid Range TRUE—Master FALSE—Slave Remarks The following table lists the characteristics of this prope

### Synchronization:Master Enable

Specifies whether the device is a master or a slave.

The master device is typically the originator of the trigger signal and clock sync pulse. For a stand-alone device, set this property to FALSE.

**Valid Range**

TRUE—Master

FALSE—Slave

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Master Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niScope Configure Clock |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties

<!--NI_TOPIC bundle=ni-scope-labview-api-ref path=instr-lib/niscope/niscope-rc/niscope/pniscope-maximumbandwidth.html language=enus -->
## TOPIC 00250: Fetch:Advanced:Maximum Bandwidth

- bundle_id: `ni-scope-labview-api-ref`
- source_path: `instr-lib/niscope/niscope-rc/niscope/pniscope-maximumbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-scope-labview-api-ref/raw/resource/enus/instr-lib/niscope/niscope-rc/niscope/pniscope-maximumbandwidth.html
- document_id: `ni-scope-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum bandwidth that the device is allowed to consume. The NI device limits itself to transfer fewer bytes per second on the PCIe bus than the value you specify for this property. Related topics: Bandwidth Remarks The following table lists the characteristics of this property. Short

### Fetch:Advanced:Maximum Bandwidth

Specifies the maximum bandwidth that the device is allowed to consume. The NI device limits itself to transfer fewer bytes per second on the PCIe bus than the value you specify for this property.

**Related topics:**

- Bandwidth

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum Bandwidth |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niScope Properties
