# NI DOCUMENT BUNDLE: ni-digital-pattern-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-digital-pattern-labview-api-ref start=1 end=153 -->
<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=api-reference.html language=enus -->
## TOPIC 00001: NI-Digital Pattern Driver LabVIEW API Reference

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `api-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/api-reference.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This API reference provides information about the programmatic elements available for this product. Looking for Something Else? For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse R

### NI-Digital Pattern Driver LabVIEW API Reference

This API reference provides information about the programmatic elements available for this product.

#### Looking for Something Else?

For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse *Related Information*.

Related information:

- NI-Digital Pattern Driver Downloads
- NI-Digital Pattern Driver Release Notes
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/action-mnu.html language=enus -->
## TOPIC 00002: Action

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/action-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/action-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to perform tasks with a digital pattern instrument. icon

### Action

Use these VIs to perform tasks with a digital pattern instrument.

[IMAGE alt='icon' src='action-mnu.png']

- [niDigital Burst Pattern VI](../../instr-lib/nidigital/nidigital-llb/nidigital-burst-pattern-vi.html) Uses the start label you specify to burst the pattern on the sites you specify. Digital pins retain their state at the end of a pattern burst until the first vector of the pattern burst, a call to niDigital Write Static, or a call to niDigital Apply Levels and Timing.
- [Source and Capture](../../instr-lib/nidigital/sourcecaptureaction-mnu.html) Use these VIs to create, configure, write, and fetch source and capture waveforms with the NI-Digital Pattern Driver. Refer to the Source Waveform Configurations topic and the Capture Waveform Configurations topic for more information about configuring source and capture waveforms, respectively.
- [Sequencer Flags and Registers](../../instr-lib/nidigital/sequencerflagsandregisters-mnu.html) Use these VIs to create and configure sequencer flags and registers with the NI-Digital Pattern Driver. Refer to the Sequencer Flags and Registers topic for more information about sequencer flags and registers.
- [Static](../../instr-lib/nidigital/static-mnu.html) Use these VIs to program read and write static states for the pin driver.
- [PPMU](../../instr-lib/nidigital/ppmuaction-mnu.html) Use these VIs to source voltage or current from the PPMU and measure voltage or current from the DUT. Refer to the Pin Parametric Measurement Unit (PPMU) topic for more information about the PPMU.
- [Frequency Counter](../../instr-lib/nidigital/frequencycounteraction-mnu.html) Use this VI to measure frequency.
- [Clock Generator](../../instr-lib/nidigital/clockgeneratoraction-mnu.html) Use these VIs to drive a free-running clock at a specified frequency from a digital pin.
- [History RAM](../../instr-lib/nidigital/historyramaction-mnu.html) Use these VIs to fetch History RAM cycle information.
- [Low Level](../../instr-lib/nidigital/lowlevelaction-mnu.html) Use these VIs to perform low-level tasks with a digital pattern instrument.

Parent topic:

NI-Digital

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/calibration-mnu.html language=enus -->
## TOPIC 00003: Calibration

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/calibration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/calibration-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to perform a self-calibration or an external calibration on a digital pattern instrument. Refer to the Calibration topic for more information about calibrating a digital pattern instrument. icon

### Calibration

Use these VIs to perform a self-calibration or an external calibration on a digital pattern instrument. Refer to the [Calibration](/csh?context=niDigital_digipat6570_calibration) topic for more information about calibrating a digital pattern instrument.

[IMAGE alt='icon' src='calibration-mnu.png']

- [niDigital Self Calibrate VI](../../instr-lib/nidigital/nidigital-llb/nidigital-self-calibrate-vi.html) Performs self-calibration on a digital pattern instrument.

Parent topic:

NI-Digital

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/dccurrent-mnu.html language=enus -->
## TOPIC 00004: DC Current

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/dccurrent-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/dccurrent-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to change channel settings when the channel is configured for DC current. icon

### DC Current

Use these VIs to change channel settings when the channel is configured for DC current.

[IMAGE alt='icon' src='dccurrent-mnu.png']

- [niDigital PPMU Configure Current Level VI](../../instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-current-level-vi.html) Specifies the current level that the PPMU forces to the DUT.
- [niDigital PPMU Configure Current Level Range VI](../../instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-current-level-range-vi.html) The configured range defines the valid values that the current level can be set to using the niDigital PPMU Configure Current Level VI. The current level range setting is applicable only if the channel is set to the DC Current output function using the niDigital PPMU Configure Output Function VI.
- [niDigital PPMU Configure Voltage Limits VI](../../instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-voltage-limits-vi.html) Specifies the voltage limit high, or high clamp voltage (V CH ), and voltage limit low, or low clamp voltage (V CL ) for the specified pins when forcing current.

Parent topic:

PPMU

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/frequencycounteraction-mnu.html language=enus -->
## TOPIC 00005: Frequency Counter

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/frequencycounteraction-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/frequencycounteraction-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this VI to measure frequency. icon

### Frequency Counter

Use this VI to measure frequency.

[IMAGE alt='icon' src='frequencycounteraction-mnu.png']

- [niDigital Frequency Counter Measure Frequency VI](../../instr-lib/nidigital/nidigital-llb/nidigital-frequency-counter-measure-frequency-vi.html) Measures the frequency on the specified channel(s) over the configured measurement time. All channels in the channelList should have the same measurement time.

Parent topic:

Action

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/frequencycounterconfiguration-mnu.html language=enus -->
## TOPIC 00006: Frequency Counter

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/frequencycounterconfiguration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/frequencycounterconfiguration-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to configure measurement settings for frequency counters. icon

### Frequency Counter

Use these VIs to configure measurement settings for frequency counters.

[IMAGE alt='icon' src='frequencycounterconfiguration-mnu.png']

- [niDigital Frequency Counter Configure Measurement Time VI](../../instr-lib/nidigital/nidigital-llb/nidigital-frequency-counter-configure-measurement-time-vi.html) Configures the measurement time for the frequency counter on the specified channel(s).
- [niDigital Frequency Counter Configure Measurement Mode VI](../../instr-lib/nidigital/nidigital-llb/nidigital-frequency-counter-configure-measurement-mode-vi.html) Determines how the frequency counters of a digital pattern instrument make measurements.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/historyramaction-mnu.html language=enus -->
## TOPIC 00007: History RAM

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/historyramaction-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/historyramaction-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to fetch History RAM cycle information. icon

### History RAM

Use these VIs to fetch History RAM cycle information.

[IMAGE alt='icon' src='historyramaction-mnu.png']

- [niDigital Get History RAM Sample Count VI](../../instr-lib/nidigital/nidigital-llb/nidigital-get-history-ram-sample-count-vi.html) Returns the number of samples History RAM acquired on the last pattern burst.
- [niDigital Fetch History RAM Cycle Information VI](../../instr-lib/nidigital/nidigital-llb/nidigital-fetch-history-ram-cycle-information-vi.html) Returns the acquired pattern information for the specified cycles.
- [niDigital Fetch History RAM Scan Cycle Numbers VI](../../instr-lib/nidigital/nidigital-llb/nidigital-fetch-history-ram-scan-cycle-numbers-vi.html) Returns the scan cycle numbers acquired for the specified cycles.

Parent topic:

Action

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/historyramconfiguration-mnu.html language=enus -->
## TOPIC 00008: History RAM

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/historyramconfiguration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/historyramconfiguration-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to configure the History RAM acquisition. icon

### History RAM

Use these VIs to configure the History RAM acquisition.

[IMAGE alt='icon' src='historyramconfiguration-mnu.png']

- [niDigital Configure History RAM Cycles To Acquire VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-history-ram-cycles-to-acquire-vi.html) Configures whether History RAM acquires all cycles or only failed cycles after triggering conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/levels-mnu.html language=enus -->
## TOPIC 00009: Levels

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/levels-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/levels-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to program the voltage levels, termination mode, and active load levels on each channel or pin of a digital pattern instrument when not using levels sheets. icon

### Levels

Use these VIs to program the voltage levels, termination mode, and active load levels on each channel or pin of a digital pattern instrument when not using levels sheets.

[IMAGE alt='icon' src='levels-mnu.png']

- [niDigital Configure Voltage Levels VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-voltage-levels-vi.html) Configures voltage levels for the pins you specify when not using levels sheets.
- [niDigital Configure Termination Mode VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-termination-mode-vi.html) Specifies the behavior of the pin when the pin driver is in a non-drive pin state (L, H, X, V, M, E).
- [niDigital Configure Active Load Levels VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-active-load-levels-vi.html) Configures I OL , I OH , and V COM levels for the active load on the pins you specify when not using levels sheets.

Parent topic:

Levels and Timing

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/levelsandtiming-mnu.html language=enus -->
## TOPIC 00010: Levels and Timing

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/levelsandtiming-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/levelsandtiming-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to configure levels and timing. Levels and timing can be configured through levels and timing sheets or directly through configure VI parameters. Refer to the Timing and the Levels topics for more information about configuring levels and timing. icon

### Levels and Timing

Use these VIs to configure levels and timing. Levels and timing can be configured through levels and timing sheets or directly through configure VI parameters. Refer to the [Timing](/csh?context=niDigital_digipat_timingtwo) and the [Levels](/csh?context=niDigital_digipat_levels) topics for more information about configuring levels and timing.

[IMAGE alt='icon' src='levelsandtiming-mnu.png']

- [niDigital Load Specifications Levels and Timing VI](../../instr-lib/nidigital/nidigital-llb/nidigital-load-specifications-levels-and-timing-vi.html) Loads settings in specifications, levels, and timing sheets. These settings are not applied to the digital pattern instrument until the niDigital Apply Levels and Timing VI is called.
- [niDigital Unload Specifications VI](../../instr-lib/nidigital/nidigital-llb/nidigital-unload-specifications-vi.html) Unloads the given specifications sheet(s) present in the previously loaded specifications file(s) that you select.
- [niDigital Apply Levels and Timing VI](../../instr-lib/nidigital/nidigital-llb/nidigital-apply-levels-and-timing-vi.html) Applies digital levels and timing values defined in previously loaded levels and timing sheets.
- [Levels](../../instr-lib/nidigital/levels-mnu.html) Use these VIs to program the voltage levels, termination mode, and active load levels on each channel or pin of a digital pattern instrument when not using levels sheets.
- [Time Set](../../instr-lib/nidigital/timesets-mnu.html) Use these VIs to program time sets for a digital pattern instrument. Use these VIs to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. These VIs do not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; they only affect the values of the current timing context.
- [TDR](../../instr-lib/nidigital/tdr-mnu.html) Use these VIs to measure pin propagation delay using Time-Domain Reflectometry (TDR) and to apply delay values to the pins of a digital pattern instrument.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/lowlevelaction-mnu.html language=enus -->
## TOPIC 00011: Low Level

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/lowlevelaction-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/lowlevelaction-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to perform low-level tasks with a digital pattern instrument. icon

### Low Level

Use these VIs to perform low-level tasks with a digital pattern instrument.

[IMAGE alt='icon' src='lowlevelaction-mnu.png']

- [niDigital Initiate VI](../../instr-lib/nidigital/nidigital-llb/nidigital-initiate-vi.html) Starts bursting the pattern. If you do not call the niDigital Commit VI, the niDigital Initiate VI implicitly calls the niDigital Commit VI for you.
- [niDigital Abort VI](../../instr-lib/nidigital/nidigital-llb/nidigital-abort-vi.html) Stops bursting the pattern.
- [niDigital Is Done VI](../../instr-lib/nidigital/nidigital-llb/nidigital-is-done-vi.html) Checks the hardware to determine if the pattern burst has completed or if any errors have occurred.
- [niDigital Wait Until Done VI](../../instr-lib/nidigital/nidigital-llb/nidigital-wait-until-done-vi.html) Waits until the pattern burst has completed or the timeout has expired.
- [niDigital Send Software Edge Trigger VI](../../instr-lib/nidigital/nidigital-llb/nidigital-send-software-edge-trigger-vi.html) Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this VI as a software override.
- [niDigital Commit VI](../../instr-lib/nidigital/nidigital-llb/nidigital-commit-vi.html) Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the niDigital Commit VI, the niDigital Initiate VI or niDigital Burst Pattern VI implicitly calls this VI for you. Calling this VI moves the session from the Uncommitted state to the Committed state.
- [niDigital Abort Keep Alive VI](../../instr-lib/nidigital/nidigital-llb/nidigital-abort-keep-alive-vi.html) Stops the keep alive pattern if it is currently running.
- [niDigital Get Site Pass Fail VI](../../instr-lib/nidigital/nidigital-llb/nidigital-get-site-pass-fail-vi.html) Returns the pass or fail results for each site.
- [niDigital Get Fail Count VI](../../instr-lib/nidigital/nidigital-llb/nidigital-get-fail-count-vi.html) Returns the comparison fail count for pins in the channel list .
- [niDigital Configure Pattern Burst Sites VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-pattern-burst-sites-vi.html) Configures which sites burst the pattern on the next call to the niDigital Initiate VI. The pattern burst sites can also be modified through the site list parameter in the niDigital Burst Pattern VI. If a site has been disabled through the niDigital Disable Sites VI, the sites does not burst a pattern even if included in the pattern burst sites.

Parent topic:

Action

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/lowlevelpinmap-mnu.html language=enus -->
## TOPIC 00012: Low Level

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/lowlevelpinmap-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/lowlevelpinmap-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to configure low-level settings of pin maps and pin groups. Use these VIs if you are not loading a pin map file using the niDigital Load Pin Map VI. icon

### Low Level

Use these VIs to configure low-level settings of pin maps and pin groups. Use these VIs if you are not loading a pin map file using the niDigital Load Pin Map VI.

[IMAGE alt='icon' src='lowlevelpinmap-mnu.png']

- [niDigital Create Pin Map VI](../../instr-lib/nidigital/nidigital-llb/nidigital-create-pin-map-vi.html) Creates and loads a pin map. Use this VI if you are not loading a pin map file using the niDigital Load Pin Map VI.
- [niDigital Create Pin Group VI](../../instr-lib/nidigital/nidigital-llb/nidigital-create-pin-group-vi.html) Creates a pin group, which is an alias for a list of pins.
- [niDigital Create Channel Map VI](../../instr-lib/nidigital/nidigital-llb/nidigital-create-channel-map-vi.html) Creates a channel map, which translates the pin maps and sites to instrument channels. You must create the pin map using the niDigital Create Pin Map VI before calling this VI. Use this VI if you are not loading a pin map file using the niDigital Load Pin Map VI.
- [niDigital Map Pin to Channel VI](../../instr-lib/nidigital/nidigital-llb/nidigital-map-pin-to-channel-vi.html) Maps a pin to a digital pattern instrument channel. For DUT pins, you must call this VI multiple times for each pin and once for each site. For system pins, call this VI only once per pin because the VI ignores the site parameter for system pins. You must call the niDigital Create Channel Map VI before you call this VI, and call niDigital End Channel Map VI after creating all connections.
- [niDigital End Channel Map VI](../../instr-lib/nidigital/nidigital-llb/nidigital-end-channel-map-vi.html) Call this VI to indicate that the channel map configuration is complete after you create channel map connections using the niDigital Map Pin to Channel VI.

Parent topic:

Pin Map

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/lowleveltimesets-mnu.html language=enus -->
## TOPIC 00013: Low Level

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/lowleveltimesets-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/lowleveltimesets-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to program time sets for a digital pattern instrument. Use these VIs to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. These VIs do not modify the timing sheet

### Low Level

Use these VIs to program time sets for a digital pattern instrument. Use these VIs to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. These VIs do not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; they only affect the values of the current timing context.

[IMAGE alt='icon' src='lowleveltimesets-mnu.png']

- [niDigital Configure Time Set Edge VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-edge-vi.html) Configures the edge placement for the pins specified in the pin list. Use this function to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; it only affects the values of the current timing context.
- [niDigital Configure Time Set Drive Format VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-format-vi.html) Configures the drive format for the pins specified in the pin list. Use this function to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; it only affects the values of the current timing context.
- [niDigital Get Time Set Period VI](../../instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-period-vi.html) Gets the period time of the time set.
- [niDigital Get Time Set Drive Format VI](../../instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-drive-format-vi.html) Gets the edge multiplier time of the time set.
- [niDigital Get Time Set Edge VI](../../instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-edge-vi.html) Gets the edge time of the pin in the time set.
- [niDigital Get Time Set Edge Multiplier VI](../../instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-edge-multiplier-vi.html) Gets the edge multiplier of the time set.

Parent topic:

Time Set

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-burst-pattern-pass-fail-vi.html language=enus -->
## TOPIC 00014: niDigital Burst Pattern (Pass Fail) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-burst-pattern-pass-fail-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-burst-pattern-pass-fail-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uses the start label you specify to burst the pattern on the sites you specify, waits for the burst to complete, and returns comparison results for each site. icon Inputs/Outputs cbool.png select digital function? (T) select digital function? (T) specifies to select the digital function for the pins

### niDigital Burst Pattern (Pass Fail) VI

Uses the **start label** you specify to burst the pattern on the sites you specify, waits for the burst to complete, and returns comparison results for each site.

[IMAGE alt='icon' src='nidigital-burst-pattern-pass-fail-vi.png']

#### Inputs/Outputs

| select digital function? (T) — select digital function? (T) specifies to select the digital function for the pins in the channel list prior to initiating clock generation. The default is TRUE. start label — start label specifies the pattern name or exported pattern label from which to start bursting the pattern. instrument handle — instrument handle identifies a particular instrument session. site list — site list specifies the sites on which to burst the pattern as a comma-delimited list of strings in the form siteN, where N is the site number. If you specify an empty string, the pattern is burst on all sites. timeout (s) — timeout (s) specifies the maximum time allowed for this VI to complete in seconds. If this VI does not complete within this time interval, this VI returns an error. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. pass — pass returns an array of pass (TRUE) and fail results for the sites you specify in the site list parameter. If sites span multiple digital pattern instruments, you must use an AND operator for the partial results for those sites returned by each instrument. If a site is disabled or not enabled for burst, the VI does not return data for that site. Use the niDigital Sort Site Results (Boolean) VI to order and combine the data to match the site list. You can also use the niDigital Get Site Results Site Numbers VI to determine the order of the sites returned from this VI call so that you can match the pass array with site numbers. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niDigital Burst Pattern VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-clock-generator-initiate-vi.html language=enus -->
## TOPIC 00015: niDigital Clock Generator Initiate VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-clock-generator-initiate-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-clock-generator-initiate-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates clock generation on the specified channel(s) or pin(s) and pin group(s). icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png channel list channel list specifies the list of channel names or list of pins for this VI. The cha

### niDigital Clock Generator Initiate VI

Initiates clock generation on the specified channel(s) or pin(s) and pin group(s).

[IMAGE alt='icon' src='nidigital-clock-generator-initiate-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel list — channel list specifies the list of channel names or list of pins for this VI. The channel list should consist of channel names or pin names. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels. Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This VI ignores pins that are not mapped to the digital pattern instrument. Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, and 3 are the channel names. To specify channels from multiple instruments, use the form PXI1Slot2/0,PXI1Slot2/2-3,PXI1Slot3/2-3. The instruments must be in the same chassis. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-close-vi.html language=enus -->
## TOPIC 00016: niDigital Close VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-close-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-close-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the instrument session to a digital pattern instrument that the instrument handle parameter specifies, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state. icon Inputs/Outputs civrn.png instrument handle instrument h

### niDigital Close VI

Closes the instrument session to a digital pattern instrument that the **instrument handle** parameter specifies, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state.

[IMAGE alt='icon' src='nidigital-close-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI-Digital

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-commit-vi.html language=enus -->
## TOPIC 00017: niDigital Commit VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-commit-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-commit-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the niDigital Commit VI, the niDigital Initiate VI or niDigital Burst Pattern VI implicitly calls this VI for you. Calling this VI moves the sessi

### niDigital Commit VI

Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the niDigital Commit VI, the niDigital Initiate VI or niDigital Burst Pattern VI implicitly calls this VI for you. Calling this VI moves the session from the Uncommitted state to the Committed state.

**Related information**

- niDigital Initiate VI
- niDigital Burst Pattern VI
- Session State Model

[IMAGE alt='icon' src='nidigital-commit-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-cycle-number-history-ram-trigger-vi.html language=enus -->
## TOPIC 00018: niDigital Configure Cycle Number History RAM Trigger VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-cycle-number-history-ram-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-cycle-number-history-ram-trigger-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures History RAM to acquire pattern information starting from a specified cycle number. Related information Fetch History RAM Sample Count VI Fetch History RAM Cycle Information VI Configure History RAM Cycles to Acquire VI icon Inputs/Outputs civrn.png instrument handle instrument handle iden

### niDigital Configure Cycle Number History RAM Trigger VI

Configures History RAM to acquire pattern information starting from a specified cycle number.

**Related information**

- Fetch History RAM Sample Count VI
- Fetch History RAM Cycle Information VI
- Configure History RAM Cycles to Acquire VI

[IMAGE alt='icon' src='nidigital-configure-cycle-number-history-ram-trigger-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. cycle number — cycle number specifies the number of cycles to execute in the current pattern burst before triggering History RAM. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. pretrigger samples — pretrigger samples specifies the number of samples to acquire before the trigger conditions are met. The instrument may capture up to 15 pretrigger samples. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niDigital Configure Trigger VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-digital-edge-conditional-jump-trigger-vi.html language=enus -->
## TOPIC 00019: niDigital Configure Digital Edge Conditional Jump Trigger VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-digital-edge-conditional-jump-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-digital-edge-conditional-jump-trigger-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the conditional jump trigger instance to trigger on an incoming digital edge and routes the specified signal source to the instrument. Related information Triggers and Events Flow Control Opcodes icon Inputs/Outputs cstr.png trigger ID trigger ID specifies which instance of the conditiona

### niDigital Configure Digital Edge Conditional Jump Trigger VI

Configures the conditional jump trigger instance to trigger on an incoming digital edge and routes the specified signal source to the instrument.

**Related information**

- Triggers and Events
- Flow Control Opcodes

[IMAGE alt='icon' src='nidigital-configure-digital-edge-conditional-jump-trigger-vi.png']

#### Inputs/Outputs

| trigger ID — trigger ID specifies which instance of the conditional jump trigger you want to override. conditionalJumpTrigger0 Configures the conditional jump trigger instance you specify. conditionalJumpTrigger1 Configures the conditional jump trigger instance you specify. conditionalJumpTrigger2 Configures the conditional jump trigger instance you specify. conditionalJumpTrigger3 Configures the conditional jump trigger instance you specify. instrument handle — instrument handle identifies a particular instrument session. source — source The string identifier for a supported trigger source to route into the instrument for the conditional jump trigger instance. The PXIe-6570/6571 supports triggers routed through the PXI trigger bus. edge — edge specifies the polarity of the incoming trigger signal that will assert this conditional jump trigger instance. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| conditionalJumpTrigger0 | Configures the conditional jump trigger instance you specify. |
| conditionalJumpTrigger1 | Configures the conditional jump trigger instance you specify. |
| conditionalJumpTrigger2 | Configures the conditional jump trigger instance you specify. |
| conditionalJumpTrigger3 | Configures the conditional jump trigger instance you specify. |

Parent topic:

niDigital Configure Trigger VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-digital-edge-rio-trigger-vi.html language=enus -->
## TOPIC 00020: niDigital Configure Digital Edge RIO Trigger VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-digital-edge-rio-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-digital-edge-rio-trigger-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RIO trigger instance to trigger on an incoming digital edge and routes the specified signal source to the instrument. Related information Triggers and Events icon Inputs/Outputs cstr.png trigger ID trigger ID specifies which instance of the conditional jump trigger you want to overrid

### niDigital Configure Digital Edge RIO Trigger VI

Configures the RIO trigger instance to trigger on an incoming digital edge and routes the specified signal source to the instrument.

**Related information**

- Triggers and Events

[IMAGE alt='icon' src='nidigital-configure-digital-edge-rio-trigger-vi.png']

#### Inputs/Outputs

| trigger ID — trigger ID specifies which instance of the conditional jump trigger you want to override. conditionalJumpTrigger0 Configures the conditional jump trigger instance you specify. conditionalJumpTrigger1 Configures the conditional jump trigger instance you specify. conditionalJumpTrigger2 Configures the conditional jump trigger instance you specify. conditionalJumpTrigger3 Configures the conditional jump trigger instance you specify. instrument handle — instrument handle identifies a particular instrument session. source — source The string identifier for a supported trigger source to route into the instrument for the conditional jump trigger instance. The PXIe-6570/6571 supports triggers routed through the PXI trigger bus. edge — edge specifies the polarity of the incoming trigger signal that will assert this conditional jump trigger instance. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| conditionalJumpTrigger0 | Configures the conditional jump trigger instance you specify. |
| conditionalJumpTrigger1 | Configures the conditional jump trigger instance you specify. |
| conditionalJumpTrigger2 | Configures the conditional jump trigger instance you specify. |
| conditionalJumpTrigger3 | Configures the conditional jump trigger instance you specify. |

Parent topic:

niDigital Configure Trigger VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-digital-edge-start-trigger-vi.html language=enus -->
## TOPIC 00021: niDigital Configure Digital Edge Start Trigger VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-digital-edge-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-digital-edge-start-trigger-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start trigger for digital edge triggering. The digital pattern instrument responds to the trigger on a physical PXI chassis backplane trigger line and waits for this trigger after you call the niDigital Initiate VI or the niDigital Burst Pattern VI. The pattern does not burst until it

### niDigital Configure Digital Edge Start Trigger VI

Configures the Start trigger for digital edge triggering. The digital pattern instrument responds to the trigger on a physical PXI chassis backplane trigger line and waits for this trigger after you call the niDigital Initiate VI or the niDigital Burst Pattern VI. The pattern does not burst until it receives this trigger.

**Related information**

- niDigital Initiate VI
- niDigital Burst Pattern VI
- Triggers and Events

[IMAGE alt='icon' src='nidigital-configure-digital-edge-start-trigger-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. source — source configures the niDigital Configure Digital Edge Start Trigger Source property. PXI_Trig0 Specifies PXI trigger line 0. PXI_Trig1 Specifies PXI trigger line 1. PXI_Trig2 Specifies PXI trigger line 2. PXI_Trig3 Specifies PXI trigger line 3. PXI_Trig4 Specifies PXI trigger line 4. PXI_Trig5 Specifies PXI trigger line 5. PXI_Trig6 Specifies PXI trigger line 6. PXI_Trig7 Specifies PXI trigger line 7. edge — edge specifies the active edge for the Start trigger. Rising Edge (1800) Specifies the signal transition from low level to high level. This is the default. Falling Edge (1801) Specifies the signal transition from high level to low level. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| PXI_Trig0 | Specifies PXI trigger line 0. |
| PXI_Trig1 | Specifies PXI trigger line 1. |
| PXI_Trig2 | Specifies PXI trigger line 2. |
| PXI_Trig3 | Specifies PXI trigger line 3. |
| PXI_Trig4 | Specifies PXI trigger line 4. |
| PXI_Trig5 | Specifies PXI trigger line 5. |
| PXI_Trig6 | Specifies PXI trigger line 6. |
| PXI_Trig7 | Specifies PXI trigger line 7. |
| Rising Edge (1800) | Specifies the signal transition from low level to high level. This is the default. |
| Falling Edge (1801) | Specifies the signal transition from high level to low level. |

Parent topic:

niDigital Configure Trigger VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-first-failure-history-ram-trigger-vi.html language=enus -->
## TOPIC 00022: niDigital Configure First Failure History RAM Trigger VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-first-failure-history-ram-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-first-failure-history-ram-trigger-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures History RAM to acquire pattern information starting from the first failed cycle encountered. Depending on the cycles History RAM is configured to acquire, samples may include passing and failing cycles. Related information Fetch History RAM Sample Count VI Fetch History RAM Cycle Informat

### niDigital Configure First Failure History RAM Trigger VI

Configures History RAM to acquire pattern information starting from the first failed cycle encountered. Depending on the cycles History RAM is configured to acquire, samples may include passing and failing cycles.

**Related information**

- Fetch History RAM Sample Count VI
- Fetch History RAM Cycle Information VI
- Configure History RAM Cycles to Acquire VI

[IMAGE alt='icon' src='nidigital-configure-first-failure-history-ram-trigger-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. pretrigger samples — pretrigger samples specifies the number of samples to acquire before the trigger conditions are met. The instrument may capture up to 15 pretrigger samples. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niDigital Configure Trigger VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-history-ram-cycles-to-acquire-vi.html language=enus -->
## TOPIC 00023: niDigital Configure History RAM Cycles To Acquire VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-history-ram-cycles-to-acquire-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-history-ram-cycles-to-acquire-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether History RAM acquires all cycles or only failed cycles after triggering conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0. icon Inputs/Outputs civrn.png instrument handle instrument handle identi

### niDigital Configure History RAM Cycles To Acquire VI

Configures whether History RAM acquires all cycles or only failed cycles after triggering conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.

[IMAGE alt='icon' src='nidigital-configure-history-ram-cycles-to-acquire-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. cycles to acquire — cycles to acquire specifies the cycles to be acquired by History RAM after the triggering conditions are met. All Cycles (2304) Acquires all cycles after the triggering conditions are met. Failed Cycles (2303) Only acquires cycles that fail a compare after the triggering conditions are met. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| All Cycles (2304) | Acquires all cycles after the triggering conditions are met. |
| Failed Cycles (2303) | Only acquires cycles that fail a compare after the triggering conditions are met. |

Parent topic:

History RAM

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-pattern-burst-sites-vi.html language=enus -->
## TOPIC 00024: niDigital Configure Pattern Burst Sites VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-pattern-burst-sites-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-pattern-burst-sites-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures which sites burst the pattern on the next call to the niDigital Initiate VI. The pattern burst sites can also be modified through the site list parameter in the niDigital Burst Pattern VI. If a site has been disabled through the niDigital Disable Sites VI, the sites does not burst a patte

### niDigital Configure Pattern Burst Sites VI

Configures which sites burst the pattern on the next call to the niDigital Initiate VI. The pattern burst sites can also be modified through the **site list** parameter in the niDigital Burst Pattern VI. If a site has been disabled through the niDigital Disable Sites VI, the sites does not burst a pattern even if included in the pattern burst sites.

[IMAGE alt='icon' src='nidigital-configure-pattern-burst-sites-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. site list — site list specifies a comma-delimited list of strings in the form of siteN, where N is the site number to include in the list of pattern burst sites. If the string is empty, all sites are configured for pattern bursting. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-start-label-vi.html language=enus -->
## TOPIC 00025: niDigital Configure Start Label VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-start-label-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-start-label-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the pattern name or exported label in the loaded patterns from which to start bursting the pattern. If you want to start bursting the pattern from the first vector, specify the pattern name. Related information Start Label Property icon Inputs/Outputs civrn.png instrument handle instrumen

### niDigital Configure Start Label VI

Configures the pattern name or exported label in the loaded patterns from which to start bursting the pattern. If you want to start bursting the pattern from the first vector, specify the pattern name.

**Related information**

- Start Label Property

[IMAGE alt='icon' src='nidigital-configure-start-label-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. start label — start label specifies the pattern name or exported pattern label from which to start bursting the pattern. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Pattern

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-termination-mode-vi.html language=enus -->
## TOPIC 00026: niDigital Configure Termination Mode VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-termination-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-termination-mode-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the pin when the pin driver is in a non-drive pin state (L, H, X, V, M, E). Related information Pin Driver niDigital Termination Mode Property icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png channel list

### niDigital Configure Termination Mode VI

Specifies the behavior of the pin when the pin driver is in a non-drive pin state (L, H, X, V, M, E).

**Related information**

- Pin Driver
- niDigital Termination Mode Property

[IMAGE alt='icon' src='nidigital-configure-termination-mode-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel list — channel list specifies the list of channel names or list of pins for this VI. The channel list should consist of channel names or pin names. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels. Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This VI ignores pins that are not mapped to the digital pattern instrument. Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, and 3 are the channel names. To specify channels from multiple instruments, use the form PXI1Slot2/0,PXI1Slot2/2-3,PXI1Slot3/2-3. The instruments must be in the same chassis. termination mode — termination mode specifies the behavior of the pin. High Z (1202) Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver is put in a high-impedance state and the active load is disabled. Active Load (1200) Specifies that, for non-drive pin states (L, H, X, V, M, E), the active load is connected and the instrument sources or sinks a defined amount of current to load the DUT. The amount of current sourced by the instrument and therefore sunk by the DUT is specified by IOL. The amount of current sunk by the instrument and therefore sourced by the DUT is specified by IOH. The voltage at which the instrument changes between sourcing and sinking is specified by VCOM. Vterm (1201) Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver terminates the pin to the configured VTERM voltage through a 50 Ω impedance. VTERM is adjustable to allow for the pin to terminate at a set level. This is useful for devices that might operate incorrectly if an instrument pin is unterminated and is allowed to float to any voltage level within the instrument voltage range. To address this issue, enable VTERM by configuring the VTERM pin level to the desired voltage and selecting the VTERM termination mode. Setting VTERM to 0 V and selecting the VTERM termination mode has the effect of connecting a 50 Ω termination to ground, which provides an effective 50 Ω impedance for the pin. This can be useful for improving signal integrity of certain DUTs by reducing reflections while the DUT drives the pin. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| High Z (1202) | Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver is put in a high-impedance state and the active load is disabled. |
| Active Load (1200) | Specifies that, for non-drive pin states (L, H, X, V, M, E), the active load is connected and the instrument sources or sinks a defined amount of current to load the DUT. The amount of current sourced by the instrument and therefore sunk by the DUT is specified by IOL. The amount of current sunk by the instrument and therefore sourced by the DUT is specified by IOH. The voltage at which the instrument changes between sourcing and sinking is specified by VCOM. |
| Vterm (1201) | Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver terminates the pin to the configured VTERM voltage through a 50 Ω impedance. VTERM is adjustable to allow for the pin to terminate at a set level. This is useful for devices that might operate incorrectly if an instrument pin is unterminated and is allowed to float to any voltage level within the instrument voltage range. To address this issue, enable VTERM by configuring the VTERM pin level to the desired voltage and selecting the VTERM termination mode. Setting VTERM to 0 V and selecting the VTERM termination mode has the effect of connecting a 50 Ω termination to ground, which provides an effective 50 Ω impedance for the pin. This can be useful for improving signal integrity of certain DUTs by reducing reflections while the DUT drives the pin. |

Parent topic:

Levels

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-edges-2x-vi.html language=enus -->
## TOPIC 00027: niDigital Configure Time Set Drive Edges (2x) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-edges-2x-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-edges-2x-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the drive edges of the pins in the time set, including the 2x edges. Use this VI to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This VI does not modify the tim

### niDigital Configure Time Set Drive Edges (2x) VI

Configures the drive edges of the pins in the time set, including the 2x edges. Use this VI to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This VI does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; it only affects the values of the current timing context.

[IMAGE alt='icon' src='nidigital-configure-time-set-drive-edges-2x-vi.png']

#### Inputs/Outputs

| drive data 2 (s) — drive data 2 (s) specifies the delay from the beginning of the vector period until the pattern data in the second DUT cycle is driven to the pattern value. drive data (s) — drive data (s) specifies the delay from the beginning of the vector period until the pattern data is driven to the pattern value. drive on (s) — drive on (s) specifies the delay from the beginning of the vector period for turning on the pin driver. This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven. instrument handle — instrument handle identifies a particular instrument session. pin list — pin list specifies the list of pin and pin group names for which to configure the time set edges. time set — time set specifies the time set name. drive format — drive format specifies the drive format of the time set. NR (1500) Non-return. RL (1501) Return to low. RH (1502) Return to high. SBC (1503) Surround by complement. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. drive return (s) — drive return (s) specifies the delay from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format. drive off (s) — drive off (s) specifies the delay from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E). drive return 2 (s) — drive return 2 (s) specifies the delay from the beginning of the vector period until the pin changes from the pattern data in the second DUT cycle to the return value, as specified in the format. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| NR (1500) | Non-return. |
| RL (1501) | Return to low. |
| RH (1502) | Return to high. |
| SBC (1503) | Surround by complement. |

Parent topic:

niDigital Configure Time Set Drive Edges (Poly) VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-edges-poly-vi.html language=enus -->
## TOPIC 00028: niDigital Configure Time Set Drive Edges (Poly) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-edges-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-edges-poly-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the drive format and drive edge placement for the specified pins. Use this VI to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This VI does not modify the timing

### niDigital Configure Time Set Drive Edges (Poly) VI

Configures the drive format and drive edge placement for the specified pins. Use this VI to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This VI does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; it affects the values of the current timing context.

[IMAGE alt='icon' src='nidigital-configure-time-set-drive-edges-poly-vi.png']

- [niDigital Configure Time Set Drive Edges VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-edges-vi.html) Configures the drive format and drive edge placement for the pins specified in the pin list . Use this VI to modify time set values after applying a timing sheet with the niDigital Apply Levels And Timing VI, or to create time sets programmatically without the use of timing sheets. This VI does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels And Timing; it only affects the values of the current timing context.
- [niDigital Configure Time Set Drive Edges (2x) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-edges-2x-vi.html) Configures the drive edges of the pins in the time set, including the 2x edges. Use this VI to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This VI does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; it only affects the values of the current timing context.

Parent topic:

Time Set

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-edges-vi.html language=enus -->
## TOPIC 00029: niDigital Configure Time Set Drive Edges VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-edges-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-edges-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the drive format and drive edge placement for the pins specified in the pin list. Use this VI to modify time set values after applying a timing sheet with the niDigital Apply Levels And Timing VI, or to create time sets programmatically without the use of timing sheets. This VI does not m

### niDigital Configure Time Set Drive Edges VI

Configures the drive format and drive edge placement for the pins specified in the **pin list**. Use this VI to modify time set values after applying a timing sheet with the niDigital Apply Levels And Timing VI, or to create time sets programmatically without the use of timing sheets. This VI does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels And Timing; it only affects the values of the current timing context.

[IMAGE alt='icon' src='nidigital-configure-time-set-drive-edges-vi.png']

#### Inputs/Outputs

| drive data (s) — drive data (s) specifies the delay from the beginning of the vector period until the pattern data is driven to the pattern value. drive on (s) — drive on (s) specifies the delay from the beginning of the vector period for turning on the pin driver. This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven. instrument handle — instrument handle identifies a particular instrument session. pin list — pin list specifies the list of pin and pin group names for which to configure the time set edges. time set — time set specifies the time set name. drive format — drive format specifies the drive format of the time set. NR (1500) Non-return. RL (1501) Return to low. RH (1502) Return to high. SBC (1503) Surround by complement. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. drive return (s) — drive return (s) specifies the delay from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format. drive off (s) — drive off (s) specifies the delay from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E). instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| NR (1500) | Non-return. |
| RL (1501) | Return to low. |
| RH (1502) | Return to high. |
| SBC (1503) | Surround by complement. |

Parent topic:

niDigital Configure Time Set Drive Edges (Poly) VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-format-vi.html language=enus -->
## TOPIC 00030: niDigital Configure Time Set Drive Format VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-format-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-format-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the drive format for the pins specified in the pin list. Use this function to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This function does not modify the tim

### niDigital Configure Time Set Drive Format VI

Configures the drive format for the pins specified in the pin list. Use this function to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; it only affects the values of the current timing context.

[IMAGE alt='icon' src='nidigital-configure-time-set-drive-format-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. pin list — pin list specifies the list of pin and pin group names for which to configure the time set edges. time set — time set specifies the time set name. format — format specifies the drive format of the time set. NR (1500) Non-return. RL (1501) Return to low. RH (1502) Return to high. SBC (1503) Surround by complement. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| NR (1500) | Non-return. |
| RL (1501) | Return to low. |
| RH (1502) | Return to high. |
| SBC (1503) | Surround by complement. |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-edge-vi.html language=enus -->
## TOPIC 00031: niDigital Configure Time Set Edge VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-edge-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-edge-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the edge placement for the pins specified in the pin list. Use this function to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This function does not modify the t

### niDigital Configure Time Set Edge VI

Configures the edge placement for the pins specified in the pin list. Use this function to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; it only affects the values of the current timing context.

[IMAGE alt='icon' src='nidigital-configure-time-set-edge-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. pin list — pin list specifies the list of pin and pin group names for which to configure the time set edges. time set — time set specifies the time set name. edge — edge specifies the time set edge to configure. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. time (s) — instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-trigger-vi.html language=enus -->
## TOPIC 00032: niDigital Configure Trigger VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-trigger-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures triggers. icon

### niDigital Configure Trigger VI

Configures triggers.

[IMAGE alt='icon' src='nidigital-configure-trigger-vi.png']

- [niDigital Disable Start Trigger VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-disable-start-trigger-vi.html) Disables a previously configured Start trigger. The digital pattern instrument does not wait for a Start trigger after you call the niDigital Initiate VI or the niDigital Burst Pattern VI before bursting a pattern.
- [niDigital Configure Digital Edge Start Trigger VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-configure-digital-edge-start-trigger-vi.html) Configures the Start trigger for digital edge triggering. The digital pattern instrument responds to the trigger on a physical PXI chassis backplane trigger line and waits for this trigger after you call the niDigital Initiate VI or the niDigital Burst Pattern VI. The pattern does not burst until it receives this trigger.
- [niDigital Configure Software Edge Start Trigger VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-configure-software-edge-start-trigger-vi.html) Configures the Start trigger for software triggering. The digital pattern instrument waits for this trigger after you call the niDigital Initiate VI or the niDigital Burst Pattern VI, and does not burst a pattern until it receives this trigger. Use the niDigital Send Software Edge Trigger VI to send the software trigger to the digital pattern instrument.
- [niDigital Configure First Failure History RAM Trigger VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-configure-first-failure-history-ram-trigger-vi.html) Configures History RAM to acquire pattern information starting from the first failed cycle encountered. Depending on the cycles History RAM is configured to acquire, samples may include passing and failing cycles.
- [niDigital Configure Pattern Label History RAM Trigger VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-configure-pattern-label-history-ram-trigger-vi.html) Configures History RAM to acquire pattern information starting from a specified label. The trigger can be offset by an additional number of vectors and then by a number of cycles.
- [niDigital Configure Cycle Number History RAM Trigger VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-configure-cycle-number-history-ram-trigger-vi.html) Configures History RAM to acquire pattern information starting from a specified cycle number.
- [niDigital Disable Conditional Jump Trigger VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-disable-conditional-jump-trigger-vi.html) Disables the conditional jump trigger instance and releases the existing route for the trigger.
- [niDigital Configure Digital Edge Conditional Jump Trigger VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-configure-digital-edge-conditional-jump-trigger-vi.html) Configures the conditional jump trigger instance to trigger on an incoming digital edge and routes the specified signal source to the instrument.
- [niDigital Configure Software Edge Conditional Jump Trigger VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-configure-software-edge-conditional-jump-trigger-vi.html) Configures the conditional jump trigger instance to trigger on a software function call.
- [niDigital Disable RIO Trigger VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-disable-rio-trigger-vi.html) Disables the conditional RIO instance and releases the existing route for the trigger.
- [niDigital Configure Digital Edge RIO Trigger VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-configure-digital-edge-rio-trigger-vi.html) Configures the RIO trigger instance to trigger on an incoming digital edge and routes the specified signal source to the instrument.

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-configure-voltage-levels-vi.html language=enus -->
## TOPIC 00033: niDigital Configure Voltage Levels VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-configure-voltage-levels-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-configure-voltage-levels-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures voltage levels for the pins you specify when not using levels sheets. Related information Pin Driver Dual Comparator icon Inputs/Outputs cdbl.png voh (V) voh (V) specifies the output voltage above which the comparator on the pin driver interprets a logic high (H). cdbl.png vol (V) vol (V)

### niDigital Configure Voltage Levels VI

Configures voltage levels for the pins you specify when not using levels sheets.

**Related information**

- Pin Driver
- Dual Comparator

[IMAGE alt='icon' src='nidigital-configure-voltage-levels-vi.png']

#### Inputs/Outputs

| voh (V) — voh (V) specifies the output voltage above which the comparator on the pin driver interprets a logic high (H). vol (V) — vol (V) specifies the output voltage below which the comparator on the pin driver interprets a logic low (L). instrument handle — instrument handle identifies a particular instrument session. channel list — channel list specifies the list of channel names or list of pins for this VI. The channel list should consist of channel names or pin names. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels. Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This VI ignores pins that are not mapped to the digital pattern instrument. Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, and 3 are the channel names. To specify channels from multiple instruments, use the form PXI1Slot2/0,PXI1Slot2/2-3,PXI1Slot3/2-3. The instruments must be in the same chassis. vih (V) — vih (V) specifies the voltage that the instrument will apply to the input of the DUT when the test instrument drives a logic high (1). vil (V) — vil (V) specifies the voltage that the instrument will apply to the input of the DUT when the pin driver drives a logic low (0). error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. vterm (V) — vterm (V) specifies the termination voltage the instrument applies during non-drive cycles when the termination mode is set to Vterm. The instrument applies the termination voltage through a 50 Ω parallel termination resistance. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Levels

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-parallel-vi.html language=enus -->
## TOPIC 00034: niDigital Create Capture Waveform (Parallel) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-parallel-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-parallel-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the capture waveform settings for parallel acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created. icon Inputs/Outputs cstr.png waveform name waveform name specifies the waveform name to use. Use

### niDigital Create Capture Waveform (Parallel) VI

Sets the capture waveform settings for parallel acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

[IMAGE alt='icon' src='nidigital-create-capture-waveform-parallel-vi.png']

#### Inputs/Outputs

| waveform name — waveform name specifies the waveform name to use. Use the waveform name with the capture_start opcode in your pattern. instrument handle — instrument handle identifies a particular instrument session. pin list — pin list specifies a list of capture pins from the waveform. The pin list must match the capture pins in the pattern that references the waveform. The pin order in the pin list determines the bit positions of the data captured by the niDigital Fetch Capture Waveform VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niDigital Create Capture Waveform VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-serial-vi.html language=enus -->
## TOPIC 00035: niDigital Create Capture Waveform (Serial) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-serial-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-serial-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the capture waveform settings for serial acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created. icon Inputs/Outputs cstr.png waveform name waveform name specifies the waveform name to use. Use th

### niDigital Create Capture Waveform (Serial) VI

Sets the capture waveform settings for serial acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

[IMAGE alt='icon' src='nidigital-create-capture-waveform-serial-vi.png']

#### Inputs/Outputs

| waveform name — waveform name specifies the waveform name to use. Use the waveform name with the capture_start opcode in your pattern. instrument handle — instrument handle identifies a particular instrument session. pin list — pin list specifies a list of capture pins from the waveform. The pin list must match the capture pins in the pattern that references the waveform. The pin order in the pin list determines the bit positions of the data captured by the niDigital Fetch Capture Waveform VI. sample width — sample width specifies the width in bits of each serial sample. Valid values are between 1 and 32. bit order — bit order specifies the order in which to shift the bits. MSB first (2500) Specifies the bit order by most significant bit first. This is the default value. LSB first (2501) Specifies the bit order by least significant bit. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| MSB first (2500) | Specifies the bit order by most significant bit first. This is the default value. |
| LSB first (2501) | Specifies the bit order by least significant bit. |

Parent topic:

niDigital Create Capture Waveform VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-vi.html language=enus -->
## TOPIC 00036: niDigital Create Capture Waveform VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates waveforms to acquire data during a pattern burst. Related information Session State Model Source and Capture Opcodes Source and Capture Overview icon

### niDigital Create Capture Waveform VI

Creates waveforms to acquire data during a pattern burst.

**Related information**

- Session State Model
- Source and Capture Opcodes
- Source and Capture Overview

[IMAGE alt='icon' src='nidigital-create-capture-waveform-vi.png']

- [niDigital Create Capture Waveform (Parallel) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-parallel-vi.html) Sets the capture waveform settings for parallel acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.
- [niDigital Create Capture Waveform (Serial) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-serial-vi.html) Sets the capture waveform settings for serial acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.
- [niDigital Create Capture Waveform From File (Digicapture) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-from-file-digicapture-vi.html) Creates a capture waveform with the configuration information from a Digicapture file generated by the Digital Pattern Editor.

Parent topic:

Source and Capture

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-create-channel-map-vi.html language=enus -->
## TOPIC 00037: niDigital Create Channel Map VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-create-channel-map-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-create-channel-map-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a channel map, which translates the pin maps and sites to instrument channels. You must create the pin map using the niDigital Create Pin Map VI before calling this VI. Use this VI if you are not loading a pin map file using the niDigital Load Pin Map VI. You cannot modify the channel map wi

### niDigital Create Channel Map VI

Creates a channel map, which translates the pin maps and sites to instrument channels. You must create the pin map using the niDigital Create Pin Map VI before calling this VI. Use this VI if you are not loading a pin map file using the niDigital Load Pin Map VI.

You cannot modify the channel map within an instrument session after you load patterns or waveforms on the digital pattern instrument.

**Related information**

- niDigital Create Pin Map VI
- niDigital Load Pin Map VI
- niDigital Map Pin to Channel VI
- niDigital End Channel Map VI

[IMAGE alt='icon' src='nidigital-create-channel-map-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. number of sites — number of sites specifies the number of sites to include in the channel map. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-create-pin-group-vi.html language=enus -->
## TOPIC 00038: niDigital Create Pin Group VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-create-pin-group-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-create-pin-group-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a pin group, which is an alias for a list of pins. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png pin group name pin group name specifies the name of the pin group. c1dstr.png pins pins specifies the list of pins to incl

### niDigital Create Pin Group VI

Creates a pin group, which is an alias for a list of pins.

[IMAGE alt='icon' src='nidigital-create-pin-group-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. pin group name — pin group name specifies the name of the pin group. pins — pins specifies the list of pins to include in the pin group. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-create-pin-map-vi.html language=enus -->
## TOPIC 00039: niDigital Create Pin Map VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-create-pin-map-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-create-pin-map-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates and loads a pin map. Use this VI if you are not loading a pin map file using the niDigital Load Pin Map VI. Related information niDigital Reset VI icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. c1dstr.png DUT pin names DUT pin na

### niDigital Create Pin Map VI

Creates and loads a pin map. Use this VI if you are not loading a pin map file using the niDigital Load Pin Map VI.

**Related information**

- niDigital Reset VI

[IMAGE alt='icon' src='nidigital-create-pin-map-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. DUT pin names — DUT pin names specifies an array of device under test (DUT) pin names to include in the pin map. DUT pins are duplicated for all sites and are used in patterns. system pin names — system pin names specifies an array of system pins to include in the pin map. System pins do not scale with the number of sites and are not used with pattern functions. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-from-file-tdms-vi.html language=enus -->
## TOPIC 00040: niDigital Create Source Waveform From File (TDMS) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-from-file-tdms-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-from-file-tdms-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a source waveform with configuration information from a TDMS file generated by the Digital Pattern Editor. It also optionally writes waveform data from the file. icon Inputs/Outputs cstr.png waveform name waveform name specifies the waveform name to use from the file. You must specify wavefo

### niDigital Create Source Waveform From File (TDMS) VI

Creates a source waveform with configuration information from a TDMS file generated by the Digital Pattern Editor. It also optionally writes waveform data from the file.

[IMAGE alt='icon' src='nidigital-create-source-waveform-from-file-tdms-vi.png']

#### Inputs/Outputs

| waveform name — waveform name specifies the waveform name to use from the file. You must specify waveform name if the file contains multiple waveforms. Use the waveform name with the source_start opcode in your pattern. instrument handle — instrument handle identifies a particular instrument session. waveform file — waveform file specifies the absolute file path to the load source waveform file (.tdms). write waveform data (T) — write waveform data (T) writes waveform data to source memory if TRUE and the waveform data is in the file. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niDigital Create Source Waveform VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-parallel-vi.html language=enus -->
## TOPIC 00041: niDigital Create Source Waveform (Parallel) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-parallel-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-parallel-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source waveform settings required for parallel sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created. icon Inputs/Outputs ci32.png data mapping data mapping specifies how to map data on multiple

### niDigital Create Source Waveform (Parallel) VI

Sets the source waveform settings required for parallel sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

[IMAGE alt='icon' src='nidigital-create-source-waveform-parallel-vi.png']

#### Inputs/Outputs

| data mapping — data mapping specifies how to map data on multiple sites. Broadcast (2600) Broadcasts the waveform you specify to all sites. Site Unique (2601) Sources unique waveform data to each site. waveform name — waveform name specifies the name to assign to the waveform. Use the waveform name with source_start opcode in your pattern. instrument handle — instrument handle identifies a particular instrument session. pin list — pin list specifies the source pins for the waveform. The pin list must match the source pins in the pattern that references the waveform. The pin order in the pin list determines the bit positions of the data written by the niDigital Write Source Waveform VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Broadcast (2600) | Broadcasts the waveform you specify to all sites. |
| Site Unique (2601) | Sources unique waveform data to each site. |

Parent topic:

niDigital Create Source Waveform VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-serial-vi.html language=enus -->
## TOPIC 00042: niDigital Create Source Waveform (Serial) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-serial-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-serial-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source waveform settings required for serial sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created. icon Inputs/Outputs ci32.png data mapping data mapping specifies how to map data on multiple s

### niDigital Create Source Waveform (Serial) VI

Sets the source waveform settings required for serial sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

[IMAGE alt='icon' src='nidigital-create-source-waveform-serial-vi.png']

#### Inputs/Outputs

| data mapping — data mapping specifies how to map data on multiple sites. Broadcast (2600) Broadcasts the waveform you specify to all sites. Site Unique (2601) Sources unique waveform data to each site. waveform name — waveform name specifies the name to assign to the waveform. Use the waveform name with source_start opcode in your pattern. instrument handle — instrument handle identifies a particular instrument session. pin list — pin list specifies the source pins for the waveform. The pin list must match the source pins in the pattern that references the waveform. The pin order in the pin list determines the bit positions of the data written by the niDigital Write Source Waveform VI. sample width — sample width specifies the width in bits of each serial sample. Valid values are between 1 and 32. bit order — bit order specifies the order in which to shift the bits. MSB first (2500) Specifies the bit order by most significant bit first. This is the default value. LSB first (2501) Specifies the bit order by least significant bit. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Broadcast (2600) | Broadcasts the waveform you specify to all sites. |
| Site Unique (2601) | Sources unique waveform data to each site. |
| MSB first (2500) | Specifies the bit order by most significant bit first. This is the default value. |
| LSB first (2501) | Specifies the bit order by least significant bit. |

Parent topic:

niDigital Create Source Waveform VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-vi.html language=enus -->
## TOPIC 00043: niDigital Create Source Waveform VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a source waveform. Use source waveforms to specify drive data for a pattern burst at runtime instead of compiling drive pin states into the pattern. Related information Opcodes Source Waveform Configurations Capture Waveform Configurations icon

### niDigital Create Source Waveform VI

Creates a source waveform. Use source waveforms to specify drive data for a pattern burst at runtime instead of compiling drive pin states into the pattern.

**Related information**

- Opcodes
- Source Waveform Configurations
- Capture Waveform Configurations

[IMAGE alt='icon' src='nidigital-create-source-waveform-vi.png']

- [niDigital Create Source Waveform (Parallel) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-parallel-vi.html) Sets the source waveform settings required for parallel sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.
- [niDigital Create Source Waveform (Serial) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-serial-vi.html) Sets the source waveform settings required for serial sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.
- [niDigital Create Source Waveform From File (TDMS) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-from-file-tdms-vi.html) Creates a source waveform with configuration information from a TDMS file generated by the Digital Pattern Editor. It also optionally writes waveform data from the file.

Parent topic:

Source and Capture

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-disable-sites-vi.html language=enus -->
## TOPIC 00044: niDigital Disable Sites VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-disable-sites-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-disable-sites-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the sites you specify. Disabled sites are not included in pattern bursts initiated by niDigital Initiate VI or niDigital Burst Pattern VI, even if the site is specified in the list of pattern burst sites in niDigital Configure Pattern Burst Sites VI or in the site list parameter of the niDi

### niDigital Disable Sites VI

Disables the sites you specify. Disabled sites are not included in pattern bursts initiated by niDigital Initiate VI or niDigital Burst Pattern VI, even if the site is specified in the list of pattern burst sites in niDigital Configure Pattern Burst Sites VI or in the **site list** parameter of the niDigital Burst Pattern VI. Additionally, if you specify a list of pin or pin group names in a **channel list** parameter in any NI-Digital VI, digital pattern instrument channels mapped to disabled sites are not affected by the VI. VIs that return per-pin data, such as niDigital PPMU Measure VI, do not return data for channels mapped to disabled sites.

The digital pattern instrument channels mapped to the sites specified are left in their current state.

NI TestStand Semiconductor Module requires all sites to always be enabled, and manages the set of active sites without disabling the sites in the digital instrument session. Do not use this VI with the Semiconductor Module.

**Related information**

- niDigital Enable Sites VI
- niDigital Burst Pattern VI
- niDigital Initiate VI
- niDigital Configure Burst Sites VI

[IMAGE alt='icon' src='nidigital-disable-sites-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. site list — site list specifies a comma-delimited list of strings in the form of siteN, where N is the site number. If you enter an empty string, the VI disables all sites. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Pin Map

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-disable-start-trigger-vi.html language=enus -->
## TOPIC 00045: niDigital Disable Start Trigger VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-disable-start-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-disable-start-trigger-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables a previously configured Start trigger. The digital pattern instrument does not wait for a Start trigger after you call the niDigital Initiate VI or the niDigital Burst Pattern VI before bursting a pattern. Related information niDigital Initiate VI niDigital Burst Pattern VI Triggers and Eve

### niDigital Disable Start Trigger VI

Disables a previously configured Start trigger. The digital pattern instrument does not wait for a Start trigger after you call the niDigital Initiate VI or the niDigital Burst Pattern VI before bursting a pattern.

**Related information**

- niDigital Initiate VI
- niDigital Burst Pattern VI
- Triggers and Events

[IMAGE alt='icon' src='nidigital-disable-start-trigger-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niDigital Configure Trigger VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-enable-match-fail-combination-poly-vi.html language=enus -->
## TOPIC 00046: niDigital Enable Match Fail Combination (Poly) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-enable-match-fail-combination-poly-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-enable-match-fail-combination-poly-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures synchronized digital pattern instruments as well as the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across digital pattern instruments based on those results. icon

### niDigital Enable Match Fail Combination (Poly) VI

Configures synchronized digital pattern instruments as well as the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across digital pattern instruments based on those results.

[IMAGE alt='icon' src='nidigital-enable-match-fail-combination-poly-vi.png']

- [niDigital Enable Match Fail Combination (NI-Digital Session) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-enable-match-fail-combination-ni-digital-session-vi.html) Configures digital pattern instruments in a multi-instrument session as well as the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across all digital pattern instruments in the multi-instrument session, based on those results.
- [niDigital Enable Match Fail Combination VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-enable-match-fail-combination-vi.html) Configures multiple digital pattern instruments in the session as well as the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across all digital pattern instruments in the session, based on those results.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-error-message-vi.html language=enus -->
## TOPIC 00047: niDigital Error Message VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-error-message-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-error-message-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the error message. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. ci32.png error code error code specifies the error code. cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this

### niDigital Error Message VI

Returns the error message.

[IMAGE alt='icon' src='nidigital-error-message-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error code — error code specifies the error code. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error message — error message returns the error information formatted as a string. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-fetch-capture-waveform-u32-vi.html language=enus -->
## TOPIC 00048: niDigital Fetch Capture Waveform (U32) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-fetch-capture-waveform-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-fetch-capture-waveform-u32-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches a defined number of samples for a specific list of sites. This VI only returns data from sites that are enabled when fetch is called. icon Inputs/Outputs cstr.png waveform name waveform name specifies the waveform name you create with the niDigital Create Capture Waveform VI. Use the wavefor

### niDigital Fetch Capture Waveform (U32) VI

Fetches a defined number of samples for a specific list of sites.

This VI only returns data from sites that are enabled when fetch is called.

[IMAGE alt='icon' src='nidigital-fetch-capture-waveform-u32-vi.png']

#### Inputs/Outputs

| waveform name — waveform name specifies the waveform name you create with the niDigital Create Capture Waveform VI. Use the waveform name with capture_start opcode in your pattern. instrument handle — instrument handle identifies a particular instrument session. site list — site list specifies a comma-delimited list of strings in the form of siteN, where N is the site number. If you enter an empty string, the VI fetches data from all sites. timeout (s) — timeout (s) specifies the maximum time allowed for this VI to complete in seconds. If this VI does not complete within this time interval, this VI returns an error. samples to read — samples to read specifies the number of samples to fetch. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. data — data returns a 2D array of digital states read from the sites in the site list. Each row in the 2D array corresponds to a site in the list. If a site is disabled, not enabled for burst, or the current digital pattern instrument does not include any capture pins, the VI does not return data for that site. Use the niDigital Sort Site Results (U32 Waveform) VI to order and combine the data to match the site list. You can also use the niDigital Get Site Results Site Numbers VI to determine the order of the sites returned from this VI call so that you can match the pass array with site numbers. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Source and Capture

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-fetch-history-ram-cycle-information-1d-pin-states-vi.html language=enus -->
## TOPIC 00049: niDigital Fetch History RAM Cycle Information (1D Pin States) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-fetch-history-ram-cycle-information-1d-pin-states-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-fetch-history-ram-cycle-information-1d-pin-states-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the pattern information acquired for the specified cycles. This variant may only be used for patterns not using the edge multiplier feature. An error is returned if a specified sample contains multiple DUT cycles. icon Inputs/Outputs cstr.png pin list pin list specifies the pins for which to

### niDigital Fetch History RAM Cycle Information (1D Pin States) VI

Returns the pattern information acquired for the specified cycles. This variant may only be used for patterns not using the edge multiplier feature. An error is returned if a specified sample contains multiple DUT cycles.

[IMAGE alt='icon' src='nidigital-fetch-history-ram-cycle-information-1d-pin-states-vi.png']

#### Inputs/Outputs

| pin list — pin list specifies the pins for which to retrieve History RAM data. If empty, the pin list from the pattern containing the start label is used. Call niDigital Get Pattern Pin List or niDigital Get Pattern Pin Names with the start label to retrieve the pins associated with the pattern burst. instrument handle — instrument handle identifies a particular instrument session. site — site specifies the site as a string in the form of siteN, where N is the site number. The VI returns an error if more than one site is specified. samples to read (-1) — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. position — position specifies the sample index from which to start fetching pattern information. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. cycle information — cycle information returns the acquired History RAM cycle information. pattern name — pattern name Returns the name of the pattern for the acquired cycle. time set name — time set name Returns the time set for the acquired cycle. vector number — vector number Returns the vector number within the pattern for the acquired cycle. Vector numbers start at 0 from the beginning of the pattern. cycle number — cycle number Returns the cycle number acquired by this History RAM sample. Cycle numbers start at 0 from the beginning of the pattern burst. expected pin states — expected pin states Returns the pin state as expected by the loaded pattern in the order specified in the pin list. actual pin states — actual pin states Returns the pin state acquired by History RAM in the order specified in the pin list. per pin pass fail — per pin pass fail Returns the pass fail information for pins in the order specified in the pin list. Pins without defined edges in the specified DUT cycle will return pass (True). error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| pattern name — pattern name Returns the name of the pattern for the acquired cycle. time set name — time set name Returns the time set for the acquired cycle. vector number — vector number Returns the vector number within the pattern for the acquired cycle. Vector numbers start at 0 from the beginning of the pattern. cycle number — cycle number Returns the cycle number acquired by this History RAM sample. Cycle numbers start at 0 from the beginning of the pattern burst. expected pin states — expected pin states Returns the pin state as expected by the loaded pattern in the order specified in the pin list. actual pin states — actual pin states Returns the pin state acquired by History RAM in the order specified in the pin list. per pin pass fail — per pin pass fail Returns the pass fail information for pins in the order specified in the pin list. Pins without defined edges in the specified DUT cycle will return pass (True). |

Parent topic:

niDigital Fetch History RAM Cycle Information VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-fetch-history-ram-cycle-information-2d-pin-states-vi.html language=enus -->
## TOPIC 00050: niDigital Fetch History RAM Cycle Information (2D Pin States) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-fetch-history-ram-cycle-information-2d-pin-states-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-fetch-history-ram-cycle-information-2d-pin-states-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the pattern information acquired for the specified cycles. Use this variant if the pattern is using the edge multiplier feature. Cycle numbers represent tester cycles, each of which may consist of multiple DUT cycles. When using pins with mixed edge multipliers, pins may return 'Not a Pin St

### niDigital Fetch History RAM Cycle Information (2D Pin States) VI

Returns the pattern information acquired for the specified cycles. Use this variant if the pattern is using the edge multiplier feature. Cycle numbers represent tester cycles, each of which may consist of multiple DUT cycles. When using pins with mixed edge multipliers, pins may return 'Not a Pin State' for DUT cycles where those pins do not have edges defined.

[IMAGE alt='icon' src='nidigital-fetch-history-ram-cycle-information-2d-pin-states-vi.png']

#### Inputs/Outputs

| pin list — pin list specifies the pins for which to retrieve History RAM data. If empty, the pin list from the pattern containing the start label is used. Call niDigital Get Pattern Pin List or niDigital Get Pattern Pin Names with the start label to retrieve the pins associated with the pattern burst. instrument handle — instrument handle identifies a particular instrument session. site — site specifies the site as a string in the form of siteN, where N is the site number. The VI returns an error if more than one site is specified. samples to read (-1) — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. position — position specifies the sample index from which to start fetching pattern information. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. cycle information — cycle information returns the acquired History RAM cycle information. pattern name — pattern name Returns the name of the pattern for the acquired cycle. time set name — time set name Returns the time set for the acquired cycle. vector number — vector number Returns the vector number within the pattern for the acquired cycle. Vector numbers start at 0 from the beginning of the pattern. cycle number — cycle number Returns the cycle number acquired by this History RAM sample. Cycle numbers start at 0 from the beginning of the pattern burst. expected pin states — expected pin states Returns the pin state as expected by the loaded pattern in the order specified in the pin list. Pins without defined edges in the specified DUT cycle will return 'Not a Pin State.' actual pin states — actual pin states Returns the pin state acquired by History RAM in the order specified in the pin list. Pins without defined edges in the specified DUT cycle will return 'Not a Pin State.' per pin pass fail — per pin pass fail Returns the pass fail information for pins in the order specified in the pin list. Pins without defined edges in the specified DUT cycle will return pass (True). error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| pattern name — pattern name Returns the name of the pattern for the acquired cycle. time set name — time set name Returns the time set for the acquired cycle. vector number — vector number Returns the vector number within the pattern for the acquired cycle. Vector numbers start at 0 from the beginning of the pattern. cycle number — cycle number Returns the cycle number acquired by this History RAM sample. Cycle numbers start at 0 from the beginning of the pattern burst. expected pin states — expected pin states Returns the pin state as expected by the loaded pattern in the order specified in the pin list. Pins without defined edges in the specified DUT cycle will return 'Not a Pin State.' actual pin states — actual pin states Returns the pin state acquired by History RAM in the order specified in the pin list. Pins without defined edges in the specified DUT cycle will return 'Not a Pin State.' per pin pass fail — per pin pass fail Returns the pass fail information for pins in the order specified in the pin list. Pins without defined edges in the specified DUT cycle will return pass (True). |

Parent topic:

niDigital Fetch History RAM Cycle Information VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-frequency-counter-configure-measurement-mode-vi.html language=enus -->
## TOPIC 00051: niDigital Frequency Counter Configure Measurement Mode VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-frequency-counter-configure-measurement-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-frequency-counter-configure-measurement-mode-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines how the frequency counters of a digital pattern instrument make measurements. The NI-Digital Pattern Driver includes the following frequency counter measurement modes: Banked mode: each discrete frequency counter is mapped to specific channels and makes frequency measurements from only th

### niDigital Frequency Counter Configure Measurement Mode VI

Determines how the frequency counters of a digital pattern instrument make measurements.

The NI-Digital Pattern Driver includes the following frequency counter measurement modes:

- Banked mode: each discrete frequency counter is mapped to specific channels and makes frequency measurements from only those channels. Use banked mode when you need access to the full measure frequency range of the instrument.
 Note If you request frequency measurements from multiple channels within the same bank, the measurements are made in series for the channels in that bank.
- Parallel mode: all discrete frequency counters make frequency measurements from all channels in parallel with one another. Use parallel mode to increase the speed of frequency measurements if you do not need access to the full measure frequency range of the instrument; in parallel mode, you can also add hysteresis to reduce measurement noise.

**Related information**

- Frequency Measurements
- Frequency Counter Hysteresis Enabled property

[IMAGE alt='icon' src='nidigital-frequency-counter-configure-measurement-mode-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. measurement mode — measurement mode specifies how the frequency counters make measurements. Banked (3700) Frequency measurements are made serially for groups of channels associated with a single frequency counter for each group. Maximum frequency measured: 200 MHz Parallel (3701) Frequency measurements are made by multiple frequency counters in parallel. Maximum frequency measured: 100 MHz error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Banked (3700) | Frequency measurements are made serially for groups of channels associated with a single frequency counter for each group. Maximum frequency measured: 200 MHz |
| Parallel (3701) | Frequency measurements are made by multiple frequency counters in parallel. Maximum frequency measured: 100 MHz |

Parent topic:

Frequency Counter

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-get-session-reference-vi.html language=enus -->
## TOPIC 00052: niDigital Get Session Reference VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-get-session-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-get-session-reference-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a session reference you can pass to NI-TClk VIs to synchronize multiple digital pattern instruments and/or other types of instruments. The session reference parameter is a generic type. Related information Related Documentation icon Inputs/Outputs civrn.png instrument handle instrument handl

### niDigital Get Session Reference VI

Returns a session reference you can pass to NI-TClk VIs to synchronize multiple digital pattern instruments and/or other types of instruments. The **session reference** parameter is a generic type.

**Related information**

- Related Documentation

[IMAGE alt='icon' src='nidigital-get-session-reference-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. session reference — session reference passes the handle that identifies the session to NI-TClk VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-get-site-pass-fail-vi.html language=enus -->
## TOPIC 00053: niDigital Get Site Pass Fail VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-get-site-pass-fail-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-get-site-pass-fail-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the pass or fail results for each site. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png site list site list specifies a comma-delimited list of strings in the form of siteN, where N is the site number. If you specify an e

### niDigital Get Site Pass Fail VI

Returns the pass or fail results for each site.

[IMAGE alt='icon' src='nidigital-get-site-pass-fail-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. site list — site list specifies a comma-delimited list of strings in the form of siteN, where N is the site number. If you specify an empty string, the VI returns pass or fail results for all sites. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. pass — pass returns an array of pass (TRUE) and fail results for the sites you specify in the site list parameter. If sites span multiple digital pattern instruments, you must use an AND operator for the partial results for those sites returned by each instrument. If a site is disabled or not enabled for burst, the VI does not return data for that site. Use the niDigital Sort Site Results (Boolean) VI to order and combine the data to match the site list. You can also use the niDigital Get Site Results Site Numbers VI to determine the order of the sites returned from this VI call so that you can match the pass array with site numbers. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-drive-format-vi.html language=enus -->
## TOPIC 00054: niDigital Get Time Set Drive Format VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-drive-format-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-drive-format-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the edge multiplier time of the time set. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png pin pin specifies the name of the pin. cstr.png time set time set specifies the time set name. cerrcodeclst.png error in error in desc

### niDigital Get Time Set Drive Format VI

Gets the edge multiplier time of the time set.

[IMAGE alt='icon' src='nidigital-get-time-set-drive-format-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. pin — pin specifies the name of the pin. time set — time set specifies the time set name. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. format — format returns the drive format of the time set for the specified pin. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-edge-multiplier-vi.html language=enus -->
## TOPIC 00055: niDigital Get Time Set Edge Multiplier VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-edge-multiplier-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-edge-multiplier-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the edge multiplier of the time set. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png pin pin specifies the name of the pin. cstr.png time set time set specifies the time set name. cerrcodeclst.png error in error in describes

### niDigital Get Time Set Edge Multiplier VI

Gets the edge multiplier of the time set.

[IMAGE alt='icon' src='nidigital-get-time-set-edge-multiplier-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. pin — pin specifies the name of the pin. time set — time set specifies the time set name. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. edge multiplier — edge multiplier returns the edge multiplier of the time set for the specified pin. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-edge-vi.html language=enus -->
## TOPIC 00056: niDigital Get Time Set Edge VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-edge-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-get-time-set-edge-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the edge time of the pin in the time set. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.png pin pin specifies the name of the pin. cstr.png time set time set specifies the time set name. ci32.png edge edge specifies the time s

### niDigital Get Time Set Edge VI

Gets the edge time of the pin in the time set.

[IMAGE alt='icon' src='nidigital-get-time-set-edge-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. pin — pin specifies the name of the pin. time set — time set specifies the time set name. edge — edge specifies the time set edge to configure. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. time (s) — time (s) The time from the beginning of the vector period in which to place the edge. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-initialize-for-grpc-session-vi.html language=enus -->
## TOPIC 00057: niDigital Initialize for gRPC Session VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-initialize-for-grpc-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-initialize-for-grpc-session-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new NI-Digital session on the specified NI gRPC Device Server using the specified instrument(s) and channel(s). This VI initializes a NI-Digital session on the specified NI gRPC Device Server and attaches to it from LabVIEW. If the session name is specified in the gRPC options and the

### niDigital Initialize for gRPC Session VI

Initializes a new NI-Digital session on the specified NI gRPC Device Server using the specified instrument(s) and channel(s).

This VI initializes a NI-Digital session on the specified NI gRPC Device Server and attaches to it from LabVIEW. If the session name is specified in the gRPC options and the same session name is already in use on the server, then NI-Digital will return an error. If the session name in the gRPC options is empty, the resource name will be used as a session name.

The resulting session in LabVIEW forwards driver calls to the corresponding session on the server.

[IMAGE alt='icon' src='nidigital-initialize-for-grpc-session-vi.png']

#### Inputs/Outputs

| gRPC options — gRPC options specifies the information used to connect to the server. session name — session name specifies the name of the MeasurementLink gRPC session. address (localhost) — address (localhost) specifies the address of the NI gRPC Device Server. port (31763) — port (31763) specifies the port that the NI gRPC Device Server monitors for connections. option string — option string sets initial values of certain properties for the NI-Digital Pattern Driver session. The string can be empty. You can use the DriverSetup flag to simulate a digital pattern instrument. When simulating a digital pattern instrument, you must specify the model you want to simulate. For example, Simulate = 1, DriverSetup = Model:6570. resource name — resource name specifies the resource name assigned by Measurement & Automation Explorer (MAX) to a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. resource name can also be a logical IVI name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where PXI1Slot2 is one instrument resource name and PXI1Slot3 is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map. Note You only can specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and PXIe-6571. The instruments must be in the same chassis. reset (F) — reset (F) specifies whether to reset a digital pattern instrument to a known state when the session is initialized. The default value is FALSE. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle — instrument handle returns the instrument session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| session name — session name specifies the name of the MeasurementLink gRPC session. address (localhost) — address (localhost) specifies the address of the NI gRPC Device Server. port (31763) — port (31763) specifies the port that the NI gRPC Device Server monitors for connections. |

Parent topic:

MeasurementLink

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-map-pin-to-channel-vi.html language=enus -->
## TOPIC 00058: niDigital Map Pin to Channel VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-map-pin-to-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-map-pin-to-channel-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maps a pin to a digital pattern instrument channel. For DUT pins, you must call this VI multiple times for each pin and once for each site. For system pins, call this VI only once per pin because the VI ignores the site parameter for system pins. You must call the niDigital Create Channel Map VI bef

### niDigital Map Pin to Channel VI

Maps a pin to a digital pattern instrument channel. For DUT pins, you must call this VI multiple times for each pin and once for each site. For system pins, call this VI only once per pin because the VI ignores the **site** parameter for system pins. You must call the niDigital Create Channel Map VI before you call this VI, and call niDigital End Channel Map VI after creating all connections.

**Related information**

- niDigital Create Channel Map VI
- niDigital End Channel Map VI

[IMAGE alt='icon' src='nidigital-map-pin-to-channel-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. pin name — pin name specifies the name of the pin to map to the channel you specify. site — site specifies the site number for the pin mapped to the channel you specify. If the pin is a system pin, the VI ignores this parameter. channel — channel specifies the channel to map to the specified pin and site. Specify channel names using the channel number, for example, "0" or "31." To specify channels used in multi-instrument sessions, use the form PXI1Slot2/0 or PXI1Slot2/31. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-aperture-time-vi.html language=enus -->
## TOPIC 00059: niDigital PPMU Configure Aperture Time VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-aperture-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-aperture-time-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the aperture time for the PPMU measurement on the specified channel(s). Related information niDigital PPMU Aperture Time Property niDigital PPMU Aperture Time Units Property Pin Parametric Measurement Unit (PPMU) Session State Model icon Inputs/Outputs ci32.png aperture time units apertur

### niDigital PPMU Configure Aperture Time VI

Configures the aperture time for the PPMU measurement on the specified channel(s).

**Related information**

- niDigital PPMU Aperture Time Property
- niDigital PPMU Aperture Time Units Property
- Pin Parametric Measurement Unit (PPMU)
- Session State Model

[IMAGE alt='icon' src='nidigital-ppmu-configure-aperture-time-vi.png']

#### Inputs/Outputs

| aperture time units — aperture time units specifies the units of the measurement aperture time. Seconds (2100) Specifies the aperture time in seconds. instrument handle — instrument handle identifies a particular instrument session. channel list — channel list specifies the list of channel names or list of pins for this VI. The channel list should consist of channel names or pin names. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels. Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This VI ignores pins that are not mapped to the digital pattern instrument. Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, and 3 are the channel names. To specify channels from multiple instruments, use the form PXI1Slot2/0,PXI1Slot2/2-3,PXI1Slot3/2-3. The instruments must be in the same chassis. aperture time — aperture time specifies the measurement aperture time for the PPMU. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Seconds (2100) | Specifies the aperture time in seconds. |

Parent topic:

PPMU

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-current-level-range-vi.html language=enus -->
## TOPIC 00060: niDigital PPMU Configure Current Level Range VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-current-level-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-current-level-range-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The configured range defines the valid values that the current level can be set to using the niDigital PPMU Configure Current Level VI. The current level range setting is applicable only if the channel is set to the DC Current output function using the niDigital PPMU Configure Output Function VI. Yo

### niDigital PPMU Configure Current Level Range VI

The configured range defines the valid values that the current level can be set to using the niDigital PPMU Configure Current Level VI. The current level range setting is applicable only if the channel is set to the DC Current output function using the niDigital PPMU Configure Output Function VI.

You must call the niDigital PPMU Source VI for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing.

**Related information**

- niDigital PPMU Configure Current Level VI
- niDigital PPMU Configure Output Function VI
- niDigital PPMU Current Level Range Property
- niDigital PPMU Source VI
- Pin Parametric Measurement Unit (PPMU)
- Pin View Pane DCPower Section

[IMAGE alt='icon' src='nidigital-ppmu-configure-current-level-range-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel list — channel list specifies the list of channel names or list of pins for this VI. The channel list should consist of channel names or pin names. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels. Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This VI ignores pins that are not mapped to the digital pattern instrument. Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, and 3 are the channel names. To specify channels from multiple instruments, use the form PXI1Slot2/0,PXI1Slot2/2-3,PXI1Slot3/2-3. The instruments must be in the same chassis. current level range (A) — current level range (A) specifies the current level range, in amps, to use when forcing a current from the PPMU to a DUT. Selecting the smallest range adequate for the desired current level provides the best current accuracy for the force current and measure current operations. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DC Current

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-current-level-vi.html language=enus -->
## TOPIC 00061: niDigital PPMU Configure Current Level VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-current-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-current-level-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current level that the PPMU forces to the DUT. You must call the niDigital PPMU Source VI for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing. Related information niDigital PPMU Configure Current Level Range VI niDigital PPMU Current Level Propert

### niDigital PPMU Configure Current Level VI

Specifies the current level that the PPMU forces to the DUT.

You must call the niDigital PPMU Source VI for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing.

**Related information**

- niDigital PPMU Configure Current Level Range VI
- niDigital PPMU Current Level Property
- niDigital PPMU Configure Output Function VI
- niDigital PPMU Source VI
- Pin Parametric Measurement Unit (PPMU)

[IMAGE alt='icon' src='nidigital-ppmu-configure-current-level-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel list — channel list specifies the list of channel names or list of pins for this VI. The channel list should consist of channel names or pin names. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels. Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This VI ignores pins that are not mapped to the digital pattern instrument. Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, and 3 are the channel names. To specify channels from multiple instruments, use the form PXI1Slot2/0,PXI1Slot2/2-3,PXI1Slot3/2-3. The instruments must be in the same chassis. current level (A) — current level (A) specifies the current level, in amps, that the PPMU forces to the DUT. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DC Current

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-current-limit-range-vi.html language=enus -->
## TOPIC 00062: niDigital PPMU Configure Current Limit Range VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-current-limit-range-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-current-limit-range-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit range for the specified pins when forcing voltage. When forcing voltage by setting niDigital PPMU Configure Output VI to DC Voltage, the current sourced or sunk is moderated by the specified current limit range. Select the smallest current range that meets the expected cu

### niDigital PPMU Configure Current Limit Range VI

Specifies the current limit range for the specified pins when forcing voltage.

When forcing voltage by setting niDigital PPMU Configure Output VI to **DC Voltage**, the current sourced or sunk is moderated by the specified current limit range. Select the smallest current range that meets the expected current requirements of the DUT.

You must call the niDigital PPMU Source VI for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing.

If the current required by the DUT exceeds the selected current limit range, the voltage output may not meet the specified voltage level. Choose a larger current limit range if needed.

**Related information**

- niDigital PPMU Configure Current Limit VI
- niDigital Current Limit Range Property
- Pin Parametric Measurement Unit (PPMU)
- Pin View Pane DCPower Section

[IMAGE alt='icon' src='nidigital-ppmu-configure-current-limit-range-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel list — channel list specifies the list of channel names or list of pins for this VI. The channel list should consist of channel names or pin names. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels. Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This VI ignores pins that are not mapped to the digital pattern instrument. Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, and 3 are the channel names. To specify channels from multiple instruments, use the form PXI1Slot2/0,PXI1Slot2/2-3,PXI1Slot3/2-3. The instruments must be in the same chassis. current limit range (A) — current limit range (A) specifies the current range, in amps, to use when forcing a voltage from the PPMU to a DUT. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-output-function-vi.html language=enus -->
## TOPIC 00063: niDigital PPMU Configure Output Function VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-output-function-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-output-function-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures to source DC voltage or DC current from the PPMU. You must call the niDigital PPMU Source VI for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing. Related information niDigital PPMU Source VI Pin Parametric Measurement Unit (PPMU) Pin View Pane PPMU S

### niDigital PPMU Configure Output Function VI

Configures to source DC voltage or DC current from the PPMU.

You must call the niDigital PPMU Source VI for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing.

**Related information**

- niDigital PPMU Source VI
- Pin Parametric Measurement Unit (PPMU)
- Pin View Pane PPMU
- Session State Model

[IMAGE alt='icon' src='nidigital-ppmu-configure-output-function-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel list — channel list specifies the list of channel names or list of pins for this VI. The channel list should consist of channel names or pin names. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels. Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This VI ignores pins that are not mapped to the digital pattern instrument. Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, and 3 are the channel names. To specify channels from multiple instruments, use the form PXI1Slot2/0,PXI1Slot2/2-3,PXI1Slot3/2-3. The instruments must be in the same chassis. output function — output function configures the operation to use for the channels or pins you specify. DC Voltage (1300) Specifies the output function to DC Voltage. DC Current (1301) Specifies the output function to DC Current. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| DC Voltage (1300) | Specifies the output function to DC Voltage. |
| DC Current (1301) | Specifies the output function to DC Current. |

Parent topic:

PPMU

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-voltage-level-vi.html language=enus -->
## TOPIC 00064: niDigital PPMU Configure Voltage Level VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-voltage-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-voltage-level-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the voltage level the PPMU outputs to the DUT. You must call the niDigital PPMU Source VI for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing. Related information niDigital PPMU Source VI niDigital PPMU Configure Output Function VI niDigital Voltage

### niDigital PPMU Configure Voltage Level VI

Configures the voltage level the PPMU outputs to the DUT. You must call the niDigital PPMU Source VI for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing.

**Related information**

- niDigital PPMU Source VI
- niDigital PPMU Configure Output Function VI
- niDigital Voltage Level Property
- Pin Parametric Measurement Unit (PPMU)

[IMAGE alt='icon' src='nidigital-ppmu-configure-voltage-level-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel list — channel list specifies the list of channel names or list of pins for this VI. The channel list should consist of channel names or pin names. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels. Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This VI ignores pins that are not mapped to the digital pattern instrument. Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, and 3 are the channel names. To specify channels from multiple instruments, use the form PXI1Slot2/0,PXI1Slot2/2-3,PXI1Slot3/2-3. The instruments must be in the same chassis. voltage level (V) — voltage level (V) specifies the voltage level that the PPMU forces to the DUT pin. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-voltage-limits-vi.html language=enus -->
## TOPIC 00065: niDigital PPMU Configure Voltage Limits VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-voltage-limits-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-voltage-limits-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage limit high, or high clamp voltage (V[CH]), and voltage limit low, or low clamp voltage (V[CL]) for the specified pins when forcing current. When forcing current by setting the niDigital PPMU Configure Output VI to DC Current, the voltage is clamped to the specified voltage limi

### niDigital PPMU Configure Voltage Limits VI

Specifies the voltage limit high, or high clamp voltage (V<sub>CH</sub>), and voltage limit low, or low clamp voltage (V<sub>CL</sub>) for the specified pins when forcing current.

When forcing current by setting the niDigital PPMU Configure Output VI to **DC Current**, the voltage is clamped to the specified voltage limits. Select the smallest voltage limits appropriate for the DUT.

You must call the niDigital PPMU Source VI for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing.

If the voltage required by the DUT exceeds the specified voltage limits, the current output may not meet the specified current level. Choose larger voltage limits as needed and appropriate for the DUT.

**Related information**

- niDigital PPMU Source VI
- Pin Parametric Measurement Unit (PPMU)

[IMAGE alt='icon' src='nidigital-ppmu-configure-voltage-limits-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. channel list — channel list specifies the list of channel names or list of pins for this VI. The channel list should consist of channel names or pin names. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels. Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This VI ignores pins that are not mapped to the digital pattern instrument. Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, and 3 are the channel names. To specify channels from multiple instruments, use the form PXI1Slot2/0,PXI1Slot2/2-3,PXI1Slot3/2-3. The instruments must be in the same chassis. voltage limit high (V) — voltage limit high (V) specifies the nominal voltage at the pin at which the high side voltage clamp activates when the PPMU forces current to the DUT. voltage limit low (V) — voltage limit low (V) specifies the nominal voltage at the pin at which the low side voltage clamp activates when the PPMU forces current to the DUT. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

DC Current

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-property-node-vi.html language=enus -->
## TOPIC 00066: niDigital Property Node VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-property-node-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads) and/or sets (writes) the niDigital Properties for the NI-Digital Pattern Driver. Related information niDigital Properties icon Inputs/Outputs civrn.png reference reference accepts a reference from a previous VI. cerrcodeclst.png error in (no error) error in describes error conditions th

### niDigital Property Node VI

Gets (reads) and/or sets (writes) the niDigital Properties for the NI-Digital Pattern Driver.

**Related information**

- niDigital Properties

[IMAGE alt='icon' src='nidigital-property-node-vi.png']

#### Inputs/Outputs

| reference — reference accepts a reference from a previous VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. reference out — reference out returns a reference from the NI-Digital Pattern Driver session to another VI. error out — error out contains error information. This output provides standard error out functionality. Property — |
| --- |

Parent topic:

NI-Digital

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-read-sequencer-flag-vi.html language=enus -->
## TOPIC 00067: niDigital Read Sequencer Flag VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-read-sequencer-flag-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-read-sequencer-flag-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program. Related information Opcodes icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. cstr.pn

### niDigital Read Sequencer Flag VI

Reads the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.

**Related information**

- Opcodes

[IMAGE alt='icon' src='nidigital-read-sequencer-flag-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. sequencer flag — sequencer flag specifies one of the following pattern sequencer flags to read. seqflag0 Reads pattern sequencer flag 0. seqflag1 Reads pattern sequencer flag 1. seqflag2 Reads pattern sequencer flag 2. seqflag3 Reads pattern sequencer flag 3. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. state — state returns the Boolean state of the pattern sequencer flag you specify. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| seqflag0 | Reads pattern sequencer flag 0. |
| seqflag1 | Reads pattern sequencer flag 1. |
| seqflag2 | Reads pattern sequencer flag 2. |
| seqflag3 | Reads pattern sequencer flag 3. |

Parent topic:

Sequencer Flags and Registers

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-self-test-vi.html language=enus -->
## TOPIC 00068: niDigital Self Test VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-self-test-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-self-test-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns self test results from a digital pattern instrument. This test requires several minutes to execute. icon Inputs/Outputs civrn.png instrument handle in instrument handle in identifies a particular instrument session. cerrcodeclst.png error in error in can accept error information wired from V

### niDigital Self Test VI

Returns self test results from a digital pattern instrument. This test requires several minutes to execute.

[IMAGE alt='icon' src='nidigital-self-test-vi.png']

#### Inputs/Outputs

| instrument handle in — instrument handle in identifies a particular instrument session. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. self test result — self test result indicates if the self test passed (0) or failed (!=0). self test message — self test message returns the self test status message. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-send-software-edge-trigger-vi.html language=enus -->
## TOPIC 00069: niDigital Send Software Edge Trigger VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-send-software-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-send-software-edge-trigger-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this VI as a software override. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. ci32.png trigger trigger specifies the trig

### niDigital Send Software Edge Trigger VI

Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this VI as a software override.

[IMAGE alt='icon' src='nidigital-send-software-edge-trigger-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. trigger — trigger specifies the trigger you want to override. Start trigger (2000) Overrides the Start trigger. You must specify an empty string in the trigger ID parameter. Conditional Jump trigger (2001) Specifies to route a conditional jump trigger. You must specify a conditional jump trigger in the trigger ID parameter. trigger ID — trigger ID specifies which instance of the conditional jump trigger you want to override. conditionalJumpTrigger0 Configures the conditional jump trigger instance you specify. conditionalJumpTrigger1 Configures the conditional jump trigger instance you specify. conditionalJumpTrigger2 Configures the conditional jump trigger instance you specify. conditionalJumpTrigger3 Configures the conditional jump trigger instance you specify. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Start trigger (2000) | Overrides the Start trigger. You must specify an empty string in the trigger ID parameter. |
| Conditional Jump trigger (2001) | Specifies to route a conditional jump trigger. You must specify a conditional jump trigger in the trigger ID parameter. |
| conditionalJumpTrigger0 | Configures the conditional jump trigger instance you specify. |
| conditionalJumpTrigger1 | Configures the conditional jump trigger instance you specify. |
| conditionalJumpTrigger2 | Configures the conditional jump trigger instance you specify. |
| conditionalJumpTrigger3 | Configures the conditional jump trigger instance you specify. |

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-sort-pin-results-by-site-dbl-vi.html language=enus -->
## TOPIC 00070: niDigital Sort Pin Results By Site (DBL) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-sort-pin-results-by-site-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-sort-pin-results-by-site-dbl-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Organizes data read from multiple digital pattern instruments by grouping the data by site number. To use this VI, read data from each instrument using the same list of pins and pin groups for the channel list parameter, and combine the data in a two-dimensional array. Each instrument returns data o

### niDigital Sort Pin Results By Site (DBL) VI

Organizes data read from multiple digital pattern instruments by grouping the data by site number.

To use this VI, read data from each instrument using the same list of pins and pin groups for the **channel list** parameter, and combine the data in a two-dimensional array. Each instrument returns data only for the pins that are mapped to its channels. Pass the data array and the same channel list as parameters to this VI.

[IMAGE alt='icon' src='nidigital-sort-pin-results-by-site-dbl-vi.png']

#### Inputs/Outputs

| read pin names (F) — read pin names (F) specifies whether the DUT pin names and system pin names are returned. instrument handles — instrument handles identifies the instrument sessions. channel list — channel list specifies the channel list you use to read data in the results array. This VI requires that the channel list contain only pin and pin group names. results — results specifies the data read from the digital pattern instruments, combined into a two-dimensional array. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. DUT pin names — DUT pin names returns a list of DUT pin names and site numbers corresponding to the values in DUT pin results. Results for each site are returned in the order specified by the channel list. site number — pin names — system pin names — system pin names returns the system pin names corresponding to the values in system pin results. instrument handles out — instrument handles out returns the handles that identify the session in all subsequent VI calls. DUT pin results — DUT pin results returns an array containing data for the DUT pins in the channel list, grouped by site number and in the order you specify in the channel list. site number — results — system pin results — system pin results returns an array containing data for the system pins in the channel list in the order you specify. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| site number — pin names — |
| site number — results — |

Parent topic:

niDigital Sort Results VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-sort-results-vi.html language=enus -->
## TOPIC 00071: niDigital Sort Results VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-sort-results-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-sort-results-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Organizes pin and site data for multiple digital pattern instruments. Pin and site data are grouped by site number. Related information Session State Model icon

### niDigital Sort Results VI

Organizes pin and site data for multiple digital pattern instruments. Pin and site data are grouped by site number.

**Related information**

- Session State Model

[IMAGE alt='icon' src='nidigital-sort-results-vi.png']

- [niDigital Sort Pin Results By Site (DBL) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-sort-pin-results-by-site-dbl-vi.html) Organizes data read from multiple digital pattern instruments by grouping the data by site number.
- [niDigital Sort Pin Results By Site (I64) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-sort-pin-results-by-site-i64-vi.html) Organizes data read from multiple digital pattern instruments by grouping the data by site number.
- [niDigital Sort Pin Results By Site (Pin State) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-sort-pin-results-by-site-pin-state-vi.html) Organizes data read from multiple digital pattern instruments by grouping the data by site number.
- [niDigital Sort Site Results (Boolean) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-sort-site-results-boolean-vi.html) Orders site data read from multiple instruments to match the site list you specify and combines data from digital pattern instruments mapped to the same site.
- [niDigital Sort Site Results (U32 Waveform) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-sort-site-results-u32-waveform-vi.html) Orders site data read from multiple instruments to match the site list you specify and combines data from instruments mapped to the same site.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-sort-site-results-boolean-vi.html language=enus -->
## TOPIC 00072: niDigital Sort Site Results (Boolean) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-sort-site-results-boolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-sort-site-results-boolean-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Orders site data read from multiple instruments to match the site list you specify and combines data from digital pattern instruments mapped to the same site. To use this VI, read data from each instrument using the same site list parameter and combine the data in a two-dimensional array. Each instr

### niDigital Sort Site Results (Boolean) VI

Orders site data read from multiple instruments to match the **site list** you specify and combines data from digital pattern instruments mapped to the same site.

To use this VI, read data from each instrument using the same **site list** parameter and combine the data in a two-dimensional array. Each instrument returns data only for the sites on which the instrument is configured to burst patterns. Pass the data array and the same **site list** as parameters to this VI. The VI returns the **sorted results** in the same order as values read using the [niDigital Burst Pattern](/csh?context=niDigital_nidigitalviref_nidigital_burst_pattern) VI and the [niDigital Get Site Pass Fail](/csh?context=niDigital_nidigitalviref_nidigital_get_site_pass_fail) VI.

[IMAGE alt='icon' src='nidigital-sort-site-results-boolean-vi.png']

#### Inputs/Outputs

| site result type — site result type specifies the type of data in the results array. instrument handles — instrument handles identifies the instrument sessions. site list — site list specifies a comma-delimited list of strings of form siteN, where N is the site number. results — results specifies the data read from the digital pattern instruments, combined into a two-dimensional array. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handles out — instrument handles out returns the handles that identify the session in all subsequent VI calls. sorted results — sorted results returns the data in the results array sorted by the order in the site list, along with the site number that corresponds to each value. site number — pass/fail — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| site number — pass/fail — |

Parent topic:

niDigital Sort Results VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-sort-site-results-u32-waveform-vi.html language=enus -->
## TOPIC 00073: niDigital Sort Site Results (U32 Waveform) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-sort-site-results-u32-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-sort-site-results-u32-waveform-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Orders site data read from multiple instruments to match the site list you specify and combines data from instruments mapped to the same site. To use this VI, read data from each instrument using the same site list parameter and combine the data in a three-dimensional array. Each instrument returns

### niDigital Sort Site Results (U32 Waveform) VI

Orders site data read from multiple instruments to match the **site list** you specify and combines data from instruments mapped to the same site.

To use this VI, read data from each instrument using the same **site list** parameter and combine the data in a three-dimensional array. Each instrument returns data using the [niDigital Fetch Capture Waveform (U32)](/csh?context=niDigital_nidigitalviref_nidigital_fetch_capture_waveform_(u32)) VI for the enabled sites on which the instrument is configured to capture waveforms. Disabled sites return an empty array. Pass the data array and the same **site list** as parameters to this VI. The VI returns **sorted waveforms** in the same order as the captured waveforms.

[IMAGE alt='icon' src='nidigital-sort-site-results-u32-waveform-vi.png']

#### Inputs/Outputs

| site result type — site result type specifies the type of data in the results array. instrument handles — instrument handles identifies the instrument sessions. site list — site list specifies a comma-delimited list of strings of form siteN, where N is the site number. The sites you specify are enabled for pattern bursting. If you specify an empty string, the pattern is burst on all sites. waveforms — waveforms specifies waveform data read from the digital pattern instruments, combined into a three-dimensional array. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handles out — instrument handles out returns the handles that identify the session in all subsequent VI calls. sorted waveforms — sorted waveforms returns the data in the results array sorted by the order in the site list, along with the site number that corresponds to each value.. site number — data — error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| site number — data — |

Parent topic:

niDigital Sort Results VI

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-write-sequencer-flag-synchronized-vi.html language=enus -->
## TOPIC 00074: niDigital Write Sequencer Flag (Synchronized) VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-write-sequencer-flag-synchronized-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-write-sequencer-flag-synchronized-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a Boolean value to the pattern sequencer flag for synchronized devices. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime program. icon Inputs/Outputs c1divrn.png instrument handles instrument handles identifies the instrument sessions. cstr.png s

### niDigital Write Sequencer Flag (Synchronized) VI

Writes a Boolean value to the pattern **sequencer flag** for synchronized devices. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime program.

[IMAGE alt='icon' src='nidigital-write-sequencer-flag-synchronized-vi.png']

#### Inputs/Outputs

| instrument handles — instrument handles identifies the instrument sessions. sequencer flag — sequencer flag specifies one of the following pattern sequencer flags to write. seqflag0 Writes pattern sequencer flag 0. seqflag1 Writes pattern sequencer flag 1. seqflag2 Writes pattern sequencer flag 2. seqflag3 Writes pattern sequencer flag 3. state (T) — state (T) specifies the Boolean state to assign to the pattern sequencer flag you specify. The default value is TRUE. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handles out — instrument handles out returns the handles that identify the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| seqflag0 | Writes pattern sequencer flag 0. |
| seqflag1 | Writes pattern sequencer flag 1. |
| seqflag2 | Writes pattern sequencer flag 2. |
| seqflag3 | Writes pattern sequencer flag 3. |

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-write-sequencer-register-vi.html language=enus -->
## TOPIC 00075: niDigital Write Sequencer Register VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-write-sequencer-register-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-write-sequencer-register-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a value to a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. Related information Opcodes icon Inputs/Outputs civrn.png instrument handle instrument handle identifies a particular instrument session. c

### niDigital Write Sequencer Register VI

Writes a value to a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program.

**Related information**

- Opcodes

[IMAGE alt='icon' src='nidigital-write-sequencer-register-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies a particular instrument session. sequencer register — sequencer register specifies one of the following sequencer registers to write to. reg0 Writes sequencer register 0. reg1 Writes sequencer register 1. reg2 Writes sequencer register 2. reg3 Writes sequencer register 3. reg4 Writes sequencer register 4. reg5 Writes sequencer register 5. reg6 Writes sequencer register 6. reg7 Writes sequencer register 7. reg8 Writes sequencer register 8. reg9 Writes sequencer register 9. reg10 Writes sequencer register 10. reg11 Writes sequencer register 11. reg12 Writes sequencer register 12. reg13 Writes sequencer register 13. reg14 Writes sequencer register 14. reg15 Writes sequencer register 15. value — value specifies the value to write to the register. error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. instrument handle out — instrument handle out returns the handle that identifies the session in all subsequent VI calls. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| reg0 | Writes sequencer register 0. |
| reg1 | Writes sequencer register 1. |
| reg2 | Writes sequencer register 2. |
| reg3 | Writes sequencer register 3. |
| reg4 | Writes sequencer register 4. |
| reg5 | Writes sequencer register 5. |
| reg6 | Writes sequencer register 6. |
| reg7 | Writes sequencer register 7. |
| reg8 | Writes sequencer register 8. |
| reg9 | Writes sequencer register 9. |
| reg10 | Writes sequencer register 10. |
| reg11 | Writes sequencer register 11. |
| reg12 | Writes sequencer register 12. |
| reg13 | Writes sequencer register 13. |
| reg14 | Writes sequencer register 14. |
| reg15 | Writes sequencer register 15. |

Parent topic:

Sequencer Flags and Registers

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-llb/nidigital-write-source-waveform-vi.html language=enus -->
## TOPIC 00076: niDigital Write Source Waveform VI

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-llb/nidigital-write-source-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-llb/nidigital-write-source-waveform-vi.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a source waveform after a waveform is created. Related information Session State Model Source and Capture Opcodes Source and Capture Overview icon

### niDigital Write Source Waveform VI

Writes a source waveform after a waveform is created.

**Related information**

- Session State Model
- Source and Capture Opcodes
- Source and Capture Overview

[IMAGE alt='icon' src='nidigital-write-source-waveform-vi.png']

- [niDigital Write Source Waveform (Broadcast U32) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-write-source-waveform-broadcast-u32-vi.html) Writes the same waveform data to all sites. Use this instance of the niDigital Write Source Waveform VI if you set the data mapping parameter of the niDigital Create Source Waveform VI to Broadcast .
- [niDigital Write Source Waveform (Site Unique U32) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-write-source-waveform-site-unique-u32-vi.html) Writes one waveform per site. Use this instance of the niDigital Write Source Waveform VI if you set the data mapping parameter of the niDigital Create Source Waveform VI to Site Unique .
- [niDigital Write Source Waveform Data From File (TDMS) VI](../../../instr-lib/nidigital/nidigital-llb/nidigital-write-source-waveform-data-from-file-tdms-vi.html) Writes a source waveform based on the waveform data and configuration information the file contains.

Parent topic:

Source and Capture

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pni-haltonkeep-alive.html language=enus -->
## TOPIC 00077: Keep Alive:Halt on keep_alive Opcode

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pni-haltonkeep-alive.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pni-haltonkeep-alive.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether keep_alive opcodes should behave like halt opcodes. Remarks The following table lists the characteristics of this property. Short Name Halt on keep_alive Data type cbool.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes

### Keep Alive:Halt on keep_alive Opcode

Specifies whether keep_alive opcodes should behave like halt opcodes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Halt on keep_alive |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pni-iskeepaliveactive.html language=enus -->
## TOPIC 00078: Keep Alive:Is Keep Alive Active

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pni-iskeepaliveactive.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pni-iskeepaliveactive.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if the digital pattern instrument is driving the keep alive pattern. Remarks The following table lists the characteristics of this property. Short Name Is Keep Alive Active Data type cbool.png Permissions Read Only High-level VIs N/A Channel-based No Resettable Yes

### Keep Alive:Is Keep Alive Active

Returns true if the digital pattern instrument is driving the keep alive pattern.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Is Keep Alive Active |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pni-tdrendpointtermination.html language=enus -->
## TOPIC 00079: TDR:TDR Endpoint Termination

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pni-tdrendpointtermination.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pni-tdrendpointtermination.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether TDR Channels are connected to an open circuit or a short to ground. Remarks The following table lists the characteristics of this property. Short Name TDR Endpoint Termination Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes TDR to open c

### TDR:TDR Endpoint Termination

Specifies whether TDR Channels are connected to an open circuit or a short to ground.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TDR Endpoint Termination |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| TDR to open circuit | 3600 | Select this option if TDR channels are connected to an open circuit |
| --- | --- | --- |
| TDR to short to ground | 3601 | Select this option if TDR channels are connected to a short to ground |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pni-tdroffset.html language=enus -->
## TOPIC 00080: TDR:TDR Offset

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pni-tdroffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pni-tdroffset.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the TDR Offset. Remarks The following table lists the characteristics of this property. Short Name TDR Offset Data type cdbl.png Permissions Read/Write High-level VIs N/A Channel-based No Resettable Yes

### TDR:TDR Offset

Specifies the TDR Offset.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TDR Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pni-timingabsolutedelay.html language=enus -->
## TOPIC 00081: Timing:Advanced:Timing Absolute Delay

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pni-timingabsolutedelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pni-timingabsolutedelay.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a timing delay, measured in seconds, and applies the delay to the digital pattern instrument in addition to TDR and calibration adjustments. If the Timing Absolute Delay Enabled property is set to true, this value is the intermodule skew measured by NI-TClk. You can modify this value to ov

### Timing:Advanced:Timing Absolute Delay

Specifies a timing delay, measured in seconds, and applies the delay to the digital pattern instrument in addition to TDR and calibration adjustments.

If the Timing Absolute Delay Enabled property is set to true, this value is the intermodule skew measured by NI-TClk. You can modify this value to override the timing delay and align the I/O timing of this instrument with another instrument that shares the same reference clock.

If the Timing Absolute Delay Enabled property is false, this property will return 0.0. Changing the Timing Absolute Delay Enabled property from false to true will set the Timing Absolute Delay value back to your previously set value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Timing Absolute Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pni-timingabsolutedelayenabled.html language=enus -->
## TOPIC 00082: Timing:Advanced:Timing Absolute Delay Enabled

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pni-timingabsolutedelayenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pni-timingabsolutedelayenabled.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the Timing Absolute Delay property should be applied to adjust the digital pattern instrument timing reference relative to other instruments in the system. Do not use this feature with digital pattern instruments in a Semiconductor Test System (STS). Timing absolute delay conflicts

### Timing:Advanced:Timing Absolute Delay Enabled

Specifies whether the Timing Absolute Delay property should be applied to adjust the digital pattern instrument timing reference relative to other instruments in the system.

Do not use this feature with digital pattern instruments in a Semiconductor Test System (STS). Timing absolute delay conflicts with the adjustment performed during STS timing calibration.

When set to True, the digital pattern instrument automatically adjusts the timing absolute delay to correct the instrument timing reference relative to other instruments in the system for better timing alignment among synchronized instruments.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Timing Absolute Delay Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-clockgeneratorfrequency.html language=enus -->
## TOPIC 00083: Clock Generator:Frequency

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-clockgeneratorfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-clockgeneratorfrequency.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency for the clock generator. Remarks The following table lists the characteristics of this property. Short Name Clock Generator Frequency Data type cdbl.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes

### Clock Generator:Frequency

Specifies the frequency for the clock generator.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Clock Generator Frequency |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-clockgeneratorisrunning.html language=enus -->
## TOPIC 00084: Clock Generator:Is Running

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-clockgeneratorisrunning.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-clockgeneratorisrunning.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the clock generator is running. Remarks The following table lists the characteristics of this property. Short Name Clock Generator Is Running Data type cbool.png Permissions Read Only High-level VIs N/A Channel-based Yes Resettable Yes

### Clock Generator:Is Running

Indicates whether the clock generator is running.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Clock Generator Is Running |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-conditionaljumptriggerterminalname.html language=enus -->
## TOPIC 00085: Triggers:Conditional Jump:Terminal Name

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-conditionaljumptriggerterminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-conditionaljumptriggerterminalname.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal name from which the exported conditional jump trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the conditional jump trigger instance asserts on the digital pattern instrument. Remarks The f

### Triggers:Conditional Jump:Terminal Name

Specifies the terminal name from which the exported conditional jump trigger signal may be routed to other instruments through the PXI trigger bus.

You can use this signal to trigger other instruments when the conditional jump trigger instance asserts on the digital pattern instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Conditional Jump Trigger Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-conditionaljumptriggertype.html language=enus -->
## TOPIC 00086: Triggers:Conditional Jump:Type

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-conditionaljumptriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-conditionaljumptriggertype.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the conditional jump trigger type. Conditional jump triggers can control conditional flow control opcodes, such as jump_if, in a digital pattern. They can be asserted by a digital edge, such as one from an external instrument, or by software. Remarks The following table lists the character

### Triggers:Conditional Jump:Type

Specifies the conditional jump trigger type.

Conditional jump triggers can control conditional flow control opcodes, such as jump_if, in a digital pattern. They can be asserted by a digital edge, such as one from an external instrument, or by software.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Conditional Jump Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| None | 1700 | Disables the Conditional Jump trigger. The opcode will assess that the Conditional Jump trigger did not assert. |
| --- | --- | --- |
| Digital Edge | 1701 | The opcode evaluates whether the Conditional Jump trigger asserted on a digital edge. Specify the source of the digital edge using the niDigital Digital Edge Conditional Jump Trigger Source property, and specify the active edge using the niDigital Digital Edge Conditional Jump Trigger Edge property. Related information niDigital Digital Edge Conditional Jump Trigger Source niDigital Digital Edge Conditional Jump Trigger Edge |
| Software | 1702 | The opcode evaluates whether the digital pattern instrument received a software Conditional Jump trigger. Create a software Conditional Jump trigger by calling the niDigital Send Software Edge Trigger VI and selecting conditional jump trigger in the trigger parameter. Related information niDigital Send Software Edge Trigger VI |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-cyclenumberhistoryramtriggercyclenumber.html language=enus -->
## TOPIC 00087: Triggers:History RAM:Cycle Number:Cycle Number

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-cyclenumberhistoryramtriggercyclenumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-cyclenumberhistoryramtriggercyclenumber.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the cycle number on which History RAM starts acquiring pattern information when configured for a cycle number trigger. Remarks The following table lists the characteristics of this property. Short Name Cycle Number History RAM Trigger Cycle Number Data type ci64.png Permissions Read/Write

### Triggers:History RAM:Cycle Number:Cycle Number

Specifies the cycle number on which History RAM starts acquiring pattern information when configured for a cycle number trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cycle Number History RAM Trigger Cycle Number |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-description.html language=enus -->
## TOPIC 00088: Inherent IVI Attributes:Driver Identification:Description

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-description.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-description.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains a brief description of the NI-Digital Pattern driver. Remarks The following table lists the characteristics of this property. Short Name Description Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Inherent IVI Attributes:Driver Identification:Description

Returns a string that contains a brief description of the NI-Digital Pattern driver.

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

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-digitaledgeriotriggersource.html language=enus -->
## TOPIC 00089: Triggers:RIO:Digital Edge:Source

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-digitaledgeriotriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-digitaledgeriotriggersource.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the RIO trigger. You can specify terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,

### Triggers:RIO:Digital Edge:Source

Specifies the source terminal for the RIO trigger.

You can specify terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/SourceCompleteEvent.

| Do not export signal | The signal is not exported. |
| --- | --- |
| PXI_Trig0 | PXI trigger line 0 |
| PXI_Trig1 | PXI trigger line 1 |
| PXI_Trig2 | PXI trigger line 2 |
| PXI_Trig3 | PXI trigger line 3 |
| PXI_Trig4 | PXI trigger line 4 |
| PXI_Trig5 | PXI trigger line 5 |
| PXI_Trig6 | PXI trigger line 6 |
| PXI_Trig7 | PXI trigger line 7 |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Edge RIO Trigger Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-digitaledgestarttriggersource.html language=enus -->
## TOPIC 00090: Triggers:Start:Digital Edge:Source

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-digitaledgestarttriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-digitaledgestarttriggersource.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the Start trigger. Use this property when the niDigital Start Trigger Type property is set to Digital Edge . You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the term

### Triggers:Start:Digital Edge:Source

Specifies the source terminal for the Start trigger. Use this property when the niDigital Start Trigger Type property is set to **Digital Edge** .

You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/StartTrigger.

**Related information**

[niDigital Start Trigger Type](pnidigital-starttriggertype.html)

| PXI_Trig0 | PXI trigger line 0 |
| --- | --- |
| PXI_Trig1 | PXI trigger line 1 |
| PXI_Trig2 | PXI trigger line 2 |
| PXI_Trig3 | PXI trigger line 3 |
| PXI_Trig4 | PXI trigger line 4 |
| PXI_Trig5 | PXI trigger line 5 |
| PXI_Trig6 | PXI trigger line 6 |
| PXI_Trig7 | PXI trigger line 7 |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Edge Start Trigger Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital Configure Trigger (poly) |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-driverprefix.html language=enus -->
## TOPIC 00091: Inherent IVI Attributes:Driver Identification:Driver Prefix

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-driverprefix.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-driverprefix.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the prefix for the NI-Digital Pattern driver. Remarks The following table lists the characteristics of this property. Short Name Driver Prefix Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Inherent IVI Attributes:Driver Identification:Driver Prefix

Returns a string that contains the prefix for the NI-Digital Pattern driver.

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

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-driversetup.html language=enus -->
## TOPIC 00092: Inherent IVI Attributes:User Options:Driver Setup

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-driversetup.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-driversetup.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Driver Setup property returns initial values for the NI-Digital Pattern Driver properties as a string. Remarks The following table lists the characteristics of this property. Short Name Driver Setup Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Inherent IVI Attributes:User Options:Driver Setup

The Driver Setup property returns initial values for the NI-Digital Pattern Driver properties as a string.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Driver Setup |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-drivervendor.html language=enus -->
## TOPIC 00093: Inherent IVI Attributes:Driver Identification:Driver Vendor

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-drivervendor.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-drivervendor.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string ("National Instruments") that contains the name of the vendor that supplies the NI-Digital Pattern driver. Remarks The following table lists the characteristics of this property. Short Name Driver Vendor Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Re

### Inherent IVI Attributes:Driver Identification:Driver Vendor

Returns a string ("National Instruments") that contains the name of the vendor that supplies the NI-Digital Pattern driver.

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

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-exportedpatternopcodeeventoutputterminal.html language=enus -->
## TOPIC 00094: Events:Pattern Opcode:Export Output Terminal

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-exportedpatternopcodeeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-exportedpatternopcodeeventoutputterminal.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for exporting the Pattern Opcode Event. You can specify terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the s

### Events:Pattern Opcode:Export Output Terminal

Specifies the destination terminal for exporting the Pattern Opcode Event.

You can specify terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

| PXI_Trig0 | PXI trigger line 0 |
| --- | --- |
| PXI_Trig1 | PXI trigger line 1 |
| PXI_Trig2 | PXI trigger line 2 |
| PXI_Trig3 | PXI trigger line 3 |
| PXI_Trig4 | PXI trigger line 4 |
| PXI_Trig5 | PXI trigger line 5 |
| PXI_Trig6 | PXI trigger line 6 |
| PXI_Trig7 | PXI trigger line 7 |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported Pattern Opcode Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-exportedrioeventoutputterminal.html language=enus -->
## TOPIC 00095: Events:RIO:Export Output Terminal

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-exportedrioeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-exportedrioeventoutputterminal.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for exporting the RIO Event. You can specify terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened te

### Events:RIO:Export Output Terminal

Specifies the destination terminal for exporting the RIO Event.

You can specify terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

| PXI_Trig0 | PXI trigger line 0 |
| --- | --- |
| PXI_Trig1 | PXI trigger line 1 |
| PXI_Trig2 | PXI trigger line 2 |
| PXI_Trig3 | PXI trigger line 3 |
| PXI_Trig4 | PXI trigger line 4 |
| PXI_Trig5 | PXI trigger line 5 |
| PXI_Trig6 | PXI trigger line 6 |
| PXI_Trig7 | PXI trigger line 7 |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Exported RIO Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-historyramcyclestoacquire.html language=enus -->
## TOPIC 00096: History RAM:Cycles to Acquire

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-historyramcyclestoacquire.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-historyramcyclestoacquire.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0. Remarks The following table lists the characteristics of this property. Short Name History RAM Cycl

### History RAM:Cycles to Acquire

Configures which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | History RAM Cycles to Acquire |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| Failed Cycles | 2303 | Only acquires cycles that fail a compare after the triggering conditions are met. |
| --- | --- | --- |
| All Cycles | 2304 | Acquires all cycles after the triggering conditions are met. |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-historyrammaxsamplestoacquirepersite.html language=enus -->
## TOPIC 00097: History RAM:Max Samples To Acquire Per Site

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-historyrammaxsamplestoacquirepersite.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-historyrammaxsamplestoacquirepersite.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full. Remarks The following table lists the characteristics of this property. Short Name History RAM Max Samples To Acquire Per Site Data type ci32.p

### History RAM:Max Samples To Acquire Per Site

Specifies the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | History RAM Max Samples To Acquire Per Site |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-historyramnumberofsamplesisfinite.html language=enus -->
## TOPIC 00098: History RAM:Number of Samples is Finite

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-historyramnumberofsamplesisfinite.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-historyramnumberofsamplesisfinite.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the digital pattern instrument acquires a finite number of History RAM samples or acquires samples continuously. When acquiring continuously, samples can be fetched during pattern burst. Remarks The following table lists the characteristics of this property. Short Name History RAM

### History RAM:Number of Samples is Finite

Specifies whether the digital pattern instrument acquires a finite number of History RAM samples or acquires samples continuously. When acquiring continuously, samples can be fetched during pattern burst.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | History RAM Number of Samples is Finite |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ioh.html language=enus -->
## TOPIC 00099: Levels:Active Load:Ioh

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ioh.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ioh.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current that the DUT sources to the active load while outputting a voltage above V[COM]. Remarks The following table lists the characteristics of this property. Short Name Ioh Data type cdbl.png Permissions Read/Write High-level VIs niDigital Configure Active Load Levels Channel-based

### Levels:Active Load:Ioh

Specifies the current that the DUT sources to the active load while outputting a voltage above V<sub>COM</sub>.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ioh |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital Configure Active Load Levels |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-iol.html language=enus -->
## TOPIC 00100: Levels:Active Load:Iol

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-iol.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-iol.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current that the DUT sinks from the active load while outputting a voltage below V[COM]. Remarks The following table lists the characteristics of this property. Short Name Iol Data type cdbl.png Permissions Read/Write High-level VIs niDigital Configure Active Load Levels Channel-based

### Levels:Active Load:Iol

Specifies the current that the DUT sinks from the active load while outputting a voltage below V<sub>COM</sub>.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Iol |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital Configure Active Load Levels |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-manufacturer.html language=enus -->
## TOPIC 00101: Inherent IVI Attributes:Instrument Identification:Manufacturer

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-manufacturer.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-manufacturer.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string ("National Instruments") that contains the name of the manufacturer of the digital pattern instrument. Remarks The following table lists the characteristics of this property. Short Name Manufacturer Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resetta

### Inherent IVI Attributes:Instrument Identification:Manufacturer

Returns a string ("National Instruments") that contains the name of the manufacturer of the digital pattern instrument.

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

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-maskcompare.html language=enus -->
## TOPIC 00102: Patterns:Mask Compare

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-maskcompare.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-maskcompare.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the pattern comparisons are masked or not. When set to true for a specified pin, failures on that pin will be masked. Remarks The following table lists the characteristics of this property. Short Name Mask Compare Data type cbool.png Permissions Read/Write High-level VIs N/A Channe

### Patterns:Mask Compare

Specifies whether the pattern comparisons are masked or not. When set to true for a specified pin, failures on that pin will be masked.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mask Compare |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-model.html language=enus -->
## TOPIC 00103: Inherent IVI Attributes:Instrument Identification:Model

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-model.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-model.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the model number or name of the digital pattern instrument. Remarks The following table lists the characteristics of this property. Short Name Model Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Inherent IVI Attributes:Instrument Identification:Model

Returns a string that contains the model number or name of the digital pattern instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Model |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-patternlabelhistoryramtriggercycleoffset.html language=enus -->
## TOPIC 00104: Triggers:History RAM:Pattern Label:Cycle Offset

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-patternlabelhistoryramtriggercycleoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-patternlabelhistoryramtriggercycleoffset.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of cycles that follow the specified pattern label and vector offset, after which History RAM will start acquiring pattern information when configured for a pattern label trigger. Remarks The following table lists the characteristics of this property. Short Name Pattern Label His

### Triggers:History RAM:Pattern Label:Cycle Offset

Specifies the number of cycles that follow the specified pattern label and vector offset, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pattern Label History RAM Trigger Cycle Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-patternlabelhistoryramtriggerlabel.html language=enus -->
## TOPIC 00105: Triggers:History RAM:Pattern Label:Label

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-patternlabelhistoryramtriggerlabel.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-patternlabelhistoryramtriggerlabel.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pattern label, augmented by the vector and cycle offset, to determine the point where History RAM will start acquiring pattern information when configured for a pattern label trigger. Remarks The following table lists the characteristics of this property. Short Name Pattern Label Histo

### Triggers:History RAM:Pattern Label:Label

Specifies the pattern label, augmented by the vector and cycle offset, to determine the point where History RAM will start acquiring pattern information when configured for a pattern label trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pattern Label History RAM Trigger Label |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-patternlabelhistoryramtriggervectoroffset.html language=enus -->
## TOPIC 00106: Triggers:History RAM:Pattern Label:Vector Offset

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-patternlabelhistoryramtriggervectoroffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-patternlabelhistoryramtriggervectoroffset.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of vectors that follow the specified pattern label, after which History RAM will start acquiring pattern information when configured for a pattern label trigger. Remarks The following table lists the characteristics of this property. Short Name Pattern Label History RAM Trigger

### Triggers:History RAM:Pattern Label:Vector Offset

Specifies the number of vectors that follow the specified pattern label, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pattern Label History RAM Trigger Vector Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-patternopcodeeventterminalname.html language=enus -->
## TOPIC 00107: Events:Pattern Opcode:Terminal Name

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-patternopcodeeventterminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-patternopcodeeventterminalname.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal name for the output trigger signal of the specified instance of a Pattern Opcode Event. You can use this terminal name as an input signal source for another trigger. Remarks The following table lists the characteristics of this property. Short Name Pattern Opcode Event Termina

### Events:Pattern Opcode:Terminal Name

Specifies the terminal name for the output trigger signal of the specified instance of a Pattern Opcode Event.

You can use this terminal name as an input signal source for another trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pattern Opcode Event Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuallowextendedvoltagerange.html language=enus -->
## TOPIC 00108: PPMU:Advanced:Allow Extended Voltage Range

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuallowextendedvoltagerange.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuallowextendedvoltagerange.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the instrument to operate in additional voltage ranges where instrument specifications may differ from standard ranges. When set to True, this property enables extended voltage range operation. Review specification deviations for application suitability before using this property. NI recomme

### PPMU:Advanced:Allow Extended Voltage Range

Enables the instrument to operate in additional voltage ranges where instrument specifications may differ from standard ranges. When set to True, this property enables extended voltage range operation. Review specification deviations for application suitability before using this property. NI recommends setting this property to False when not using the extended voltage range to avoid unintentional use of this range.

The extended voltage range is supported only for PPMU, with the output function set to DC Voltage. A voltage glitch may occur when you change the PPMU output voltage from a standard range to the extended voltage range, or vice-versa, while the PPMU is sourcing. NI recommends temporarily changing the Selected Function property to Off before sourcing a voltage level that requires a range change.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPMU Allow Extended Voltage Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuaperturetime.html language=enus -->
## TOPIC 00109: PPMU:Aperture Time

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuaperturetime.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuaperturetime.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement aperture time for the PPMU. The PPMU Aperture Time Units property sets the units of the PPMU aperture time. Related information niDigital PPMU Aperture Time Units property Remarks The following table lists the characteristics of this property. Short Name PPMU Aperture Time

### PPMU:Aperture Time

Specifies the measurement aperture time for the PPMU.

The PPMU Aperture Time Units property sets the units of the PPMU aperture time.

**Related information**

[niDigital PPMU Aperture Time Units property](pnidigital-ppmuaperturetimeunits.html)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPMU Aperture Time |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuaperturetimeunits.html language=enus -->
## TOPIC 00110: PPMU:Aperture Time Units

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuaperturetimeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuaperturetimeunits.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of the measurement aperture time for the PPMU. Remarks The following table lists the characteristics of this property. Short Name PPMU Aperture Time Units Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based Yes Resettable Yes Seconds 2100 Specifies seconds

### PPMU:Aperture Time Units

Specifies the units of the measurement aperture time for the PPMU.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPMU Aperture Time Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

| Seconds | 2100 | Specifies seconds as the aperture time unit. |
| --- | --- | --- |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlevel.html language=enus -->
## TOPIC 00111: PPMU:Source:DC Current:Current Level

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlevel.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current level, in amps, that the PPMU forces to the DUT. This property is applicable only when you set the PPMU Output Function property to DC Current. Specify valid values for the current level using the niDigital PPMU Configure Current Level Range VI. Related information niDigital PP

### PPMU:Source:DC Current:Current Level

Specifies the current level, in amps, that the PPMU forces to the DUT. This property is applicable only when you set the PPMU Output Function property to **DC Current**.

Specify valid values for the current level using the niDigital PPMU Configure Current Level Range VI.

**Related information**

- niDigital PPMU Configure Output Function VI
- niDigital PPMU Configure Current Level Range VI

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPMU Current Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital PPMU Configure Current Level |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlevelrange.html language=enus -->
## TOPIC 00112: PPMU:Source:DC Current:Current Level Range

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlevelrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlevelrange.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the range of valid values for the current level, in amps, that the PPMU forces to the DUT. This property is applicable only when you set the PPMU Output Function property to DC Current. Related information niDigital Current Level property Remarks The following table lists the characteristi

### PPMU:Source:DC Current:Current Level Range

Specifies the range of valid values for the current level, in amps, that the PPMU forces to the DUT. This property is applicable only when you set the PPMU Output Function property to **DC Current**.

**Related information**

- niDigital Current Level property

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPMU Current Level Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital PPMU Configure Current Level Range |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlimit.html language=enus -->
## TOPIC 00113: PPMU:Source:DC Voltage:Current Limit

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlimit.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. This property is applicable only when you set the PPMU Output Function property to DC Voltage. The PXIe-6570/6571 does not support the Current Limit property and allows only configuration of

### PPMU:Source:DC Voltage:Current Limit

Specifies the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. This property is applicable only when you set the PPMU Output Function property to **DC Voltage**. The PXIe-6570/6571 does not support the Current Limit property and allows only configuration of the Current Limit Range.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPMU Current Limit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlimitrange.html language=enus -->
## TOPIC 00114: PPMU:Source:DC Voltage:Current Limit Range

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlimitrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlimitrange.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. This property is applicable only when you set the PPMU Output Function property to DC Voltage. Related information niDigital PPMU Configure Voltage Level VI Remarks The following table

### PPMU:Source:DC Voltage:Current Limit Range

Specifies the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. This property is applicable only when you set the PPMU Output Function property to **DC Voltage**.

**Related information**

- niDigital PPMU Configure Voltage Level VI

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPMU Current Limit Range |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital PPMU Configure Current Limit Range |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlimitsupported.html language=enus -->
## TOPIC 00115: PPMU:Source:DC Voltage:Current Limit Supported

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlimitsupported.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmucurrentlimitsupported.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the device supports configuration of a current limit when you set the PPMU Output Function property to DC Voltage. Remarks The following table lists the characteristics of this property. Short Name PPMU Current Limit Supported Data type cbool.png Permissions Read Only High-level VIs

### PPMU:Source:DC Voltage:Current Limit Supported

Returns whether the device supports configuration of a current limit when you set the PPMU Output Function property to **DC Voltage**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPMU Current Limit Supported |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmulowervoltagelimit.html language=enus -->
## TOPIC 00116: PPMU:Source:DC Current:Voltage Limit Low

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmulowervoltagelimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmulowervoltagelimit.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum voltage limit, or low clamp voltage (V[CL]), in volts, at the pin when the PPMU forces current to the DUT. This property is applicable only when you set the PPMU Output Function property to DC Current. Related information niDigital Current Level property Remarks The following t

### PPMU:Source:DC Current:Voltage Limit Low

Specifies the minimum voltage limit, or low clamp voltage (V<sub>CL</sub>), in volts, at the pin when the PPMU forces current to the DUT. This property is applicable only when you set the PPMU Output Function property to **DC Current**.

**Related information**

- niDigital Current Level property

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPMU Voltage Limit Low |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital PPMU Configure Voltage Limit |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuoutputfunction.html language=enus -->
## TOPIC 00117: PPMU:Source:Output Function

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuoutputfunction.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuoutputfunction.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the PPMU forces voltage or current to the DUT. Remarks The following table lists the characteristics of this property. Short Name PPMU Output Function Data type ci32.png Permissions Read/Write High-level VIs niDigital PPMU Configure Output Function Channel-based Yes Resettable Yes

### PPMU:Source:Output Function

Specifies whether the PPMU forces voltage or current to the DUT.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPMU Output Function |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital PPMU Configure Output Function |
| Channel-based | Yes |
| Resettable | Yes |

| DC Voltage | 1300 | Sets the PPMU source function to DC voltage. |
| --- | --- | --- |
| DC Current | 1301 | Sets the PPMU source function to DC current. |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuuppervoltagelimit.html language=enus -->
## TOPIC 00118: PPMU:Source:DC Current:Voltage Limit High

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuuppervoltagelimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuuppervoltagelimit.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum voltage limit, or high clamp voltage (V[CH]), in volts, at the pin when the PPMU forces current to the DUT. This property is applicable only when you set the PPMU Output Function property to DC Current. Related information niDigital Current Level property Remarks The following

### PPMU:Source:DC Current:Voltage Limit High

Specifies the maximum voltage limit, or high clamp voltage (V<sub>CH</sub>), in volts, at the pin when the PPMU forces current to the DUT. This property is applicable only when you set the PPMU Output Function property to **DC Current**.

**Related information**

- niDigital Current Level property

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPMU Voltage Limit High |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital PPMU Configure Voltage Limit |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuvoltagelevel.html language=enus -->
## TOPIC 00119: PPMU:Source:DC Voltage:Voltage Level

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuvoltagelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-ppmuvoltagelevel.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level, in volts, that the PPMU forces to the DUT. This property is applicable only when you set the PPMU Output Function property to DC Voltage. Related information niDigital PPMU Configure Output Function VI niDigital PPMU Configure Current Limit Range VI Remarks The following

### PPMU:Source:DC Voltage:Voltage Level

Specifies the voltage level, in volts, that the PPMU forces to the DUT. This property is applicable only when you set the PPMU Output Function property to **DC Voltage**.

**Related information**

- niDigital PPMU Configure Output Function VI
- niDigital PPMU Configure Current Limit Range VI

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPMU Voltage Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital PPMU Configure Voltage_Level |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-queryinstrumentstatus.html language=enus -->
## TOPIC 00120: Inherent IVI Attributes:User Options:Query Instrument Status

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-queryinstrumentstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-queryinstrumentstatus.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the NI-Digital Pattern Driver queries the digital pattern instrument status after each operation. The instrument status is always queried, regardless of the property setting. Remarks The following table lists the characteristics of this property. Short Name Query Instrument Status

### Inherent IVI Attributes:User Options:Query Instrument Status

Specifies whether the NI-Digital Pattern Driver queries the digital pattern instrument status after each operation.

The instrument status is always queried, regardless of the property setting.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Query Instrument Status |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-rangecheck.html language=enus -->
## TOPIC 00121: Inherent IVI Attributes:User Options:Range Check

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-rangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-rangecheck.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the range and validates parameter and property values you pass to NI-Digital Pattern Driver VIs. Ranges are always checked, regardless of the property setting. Remarks The following table lists the characteristics of this property. Short Name Range Check Data type cbool.png Permissions Read O

### Inherent IVI Attributes:User Options:Range Check

Checks the range and validates parameter and property values you pass to NI-Digital Pattern Driver VIs.

Ranges are always checked, regardless of the property setting.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Range Check |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-recordvaluecoercions.html language=enus -->
## TOPIC 00122: Inherent IVI Attributes:User Options:Record Value Coercions

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-recordvaluecoercions.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-recordvaluecoercions.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties. Enabling record value coercions is not supported. Remarks The following table lists the characteristics of this property. Short Name Record Value Coercions Data type cbool.png Permissi

### Inherent IVI Attributes:User Options:Record Value Coercions

Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties. Enabling record value coercions is not supported.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Record Value Coercions |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-resourcedescriptor.html language=enus -->
## TOPIC 00123: Inherent IVI Attributes:Advanced Session Information:Resource Descriptor

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-resourcedescriptor.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-resourcedescriptor.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the resource descriptor that the NI-Digital Pattern Driver uses to identify the digital pattern instrument. Remarks The following table lists the characteristics of this property. Short Name Resource Descriptor Data type cstr.png Permissions Read Only High-level VIs N/

### Inherent IVI Attributes:Advanced Session Information:Resource Descriptor

Returns a string that contains the resource descriptor that the NI-Digital Pattern Driver uses to identify the digital pattern instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Resource Descriptor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-revision.html language=enus -->
## TOPIC 00124: Inherent IVI Attributes:Driver Identification:Revision

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-revision.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-revision.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains additional version information about the NI-Digital Pattern driver. For example, the driver can return Driver: NI-Digital 16.0 as the value of this property. Remarks The following table lists the characteristics of this property. Short Name Revision Data type cstr.png

### Inherent IVI Attributes:Driver Identification:Revision

Returns a string that contains additional version information about the NI-Digital Pattern driver. For example, the driver can return Driver: NI-Digital 16.0 as the value of this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Revision |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-rioeventterminalname.html language=enus -->
## TOPIC 00125: Events:RIO:Terminal Name

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-rioeventterminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-rioeventterminalname.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal name for the output trigger signal of the specified instance of a RIO Event. You can use this terminal name as an input signal source for another trigger. Remarks The following table lists the characteristics of this property. Short Name RIO Event Terminal Name Data type cstr.

### Events:RIO:Terminal Name

Specifies the terminal name for the output trigger signal of the specified instance of a RIO Event.

You can use this terminal name as an input signal source for another trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RIO Event Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-riotriggerterminalname.html language=enus -->
## TOPIC 00126: Triggers:RIO:Terminal Name

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-riotriggerterminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-riotriggerterminalname.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal name from which the exported RIO trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the RIO trigger instance asserts on the digital pattern instrument. Remarks The following table lists the c

### Triggers:RIO:Terminal Name

Specifies the terminal name from which the exported RIO trigger signal may be routed to other instruments through the PXI trigger bus.

You can use this signal to trigger other instruments when the RIO trigger instance asserts on the digital pattern instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RIO Trigger Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-riotriggertype.html language=enus -->
## TOPIC 00127: Triggers:RIO:Type

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-riotriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-riotriggertype.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RIO trigger type. RIO triggers can be asserted by a digital edge, such as one from an external instrument. Remarks The following table lists the characteristics of this property. Short Name RIO Trigger Type Data type ci32.png Permissions Read/Write High-level VIs N/A Channel-based No R

### Triggers:RIO:Type

Specifies the RIO trigger type.

RIO triggers can be asserted by a digital edge, such as one from an external instrument.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RIO Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| None | 1700 | Disables the RIO trigger. |
| --- | --- | --- |
| Digital Edge | 1701 | Specify the source of the digital edge using the niDigital Digital Edge RIO Trigger Source property, and specify the active edge using the niDigital Digital Edge RIO Trigger Edge property. Related information niDigital Digital Edge RIO Trigger Source niDigital Digital Edge RIO Trigger Edge |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-selectedfunction.html language=enus -->
## TOPIC 00128: Selected Function

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-selectedfunction.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-selectedfunction.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether digital pattern instrument channels are controlled by the pattern sequencer or PPMU, disconnected, or off. Related information niDigital Burst Pattern VI niDigital PPMU Source VI Programming Pin Electronics Remarks The following table lists the characteristics of this property. Sho

### Selected Function

Specifies whether digital pattern instrument channels are controlled by the pattern sequencer or PPMU, disconnected, or off.

**Related information**

- niDigital Burst Pattern VI
- niDigital PPMU Source VI
- Programming Pin Electronics

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Selected Function |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital Select Function |
| Channel-based | Yes |
| Resettable | Yes |

| Digital | 1100 | The pin is connected to the driver, comparator, and active load functions. The PPMU is not sourcing, but can make voltage measurements. The state of the digital pin driver when you change the selected function to Digital is determined by the most recent call to the niDigital Write Static VI or the last vector of the most recently executed pattern burst, whichever happened last. Use the niDigital Write Static VI to control the state of the digital pin driver through software. Use the niDigital Burst Pattern VI to control the state of the digital pin driver through a pattern. Set the select digital function parameter of the niDigital Burst Pattern VI to TRUE to automatically switch the selected function of the pins in the pattern burst to Digital. |
| --- | --- | --- |
| PPMU | 1101 | The pin is connected to the PPMU. The driver, comparator, and active load are off while this function is selected. Call the niDigital PPMU Source VI to source a voltage or current. The niDigital PPMU Source VI automatically switches the selected function to the PPMU state and starts sourcing from the PPMU. Changing the selected function to Disconnect, Off, or Digital causes the PPMU to stop sourcing. If you change the selected function to PPMU using the niDigital Select Function VI, the PPMU is initially not sourcing. Note You can make PPMU voltage measurements using the niDigital PPMU Measure VI from within any selected function. |
| Off | 1102 | The pin is electrically connected, and the PPMU and digital pin driver are off while this function is selected. |
| Disconnect | 1103 | The pin is electrically disconnected from instrument functions. Selecting this function causes the PPMU to stop sourcing prior to disconnecting the pin. Caution In the Disconnect state, some I/O protection and sensing circuitry remains exposed. Do not subject the instrument to voltage beyond its operating range. |
| Rio | 1104 | Yields control of the specified pin(s) to LabVIEW FPGA. |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-sequencerflagterminalname.html language=enus -->
## TOPIC 00129: Triggers:Sequencer Flag:Terminal Name

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-sequencerflagterminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-sequencerflagterminalname.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal name for the output trigger signal of the Sequencer Flags trigger. You can use this terminal name as an input signal source for another trigger. Remarks The following table lists the characteristics of this property. Short Name Sequencer Flag Terminal Name Data type cstr.png P

### Triggers:Sequencer Flag:Terminal Name

Specifies the terminal name for the output trigger signal of the Sequencer Flags trigger.

You can use this terminal name as an input signal source for another trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sequencer Flag Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-serialnumber.html language=enus -->
## TOPIC 00130: Device Characteristics:Serial Number

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-serialnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-serialnumber.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the serial number of the device. Remarks The following table lists the characteristics of this property. Short Name Serial Number Data type cstr.png Permissions Read Only High-level VIs N/A Channel-based No Resettable No

### Device Characteristics:Serial Number

Returns the serial number of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Serial Number |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-simulate.html language=enus -->
## TOPIC 00131: Inherent IVI Attributes:User Options:Simulate

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-simulate.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-simulate.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Simulates I/O operations. After you open a session, you cannot change the simulation state. Use the niDigital Initialize with Options VI to enable simulation. Remarks The following table lists the characteristics of this property. Short Name Simulate Data type cbool.png Permissions Read Only High-le

### Inherent IVI Attributes:User Options:Simulate

Simulates I/O operations. After you open a session, you cannot change the simulation state. Use the niDigital Initialize with Options VI to enable simulation.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Simulate |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-startlabel.html language=enus -->
## TOPIC 00132: Patterns:Start Label

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-startlabel.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-startlabel.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pattern name or exported pattern label from which to start bursting the pattern. Remarks The following table lists the characteristics of this property. Short Name Start Label Data type cstr.png Permissions Read/Write High-level VIs niDigital Configure Start Label Channel-based No Rese

### Patterns:Start Label

Specifies the pattern name or exported pattern label from which to start bursting the pattern.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Label |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital Configure Start Label |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-starttriggerterminalname.html language=enus -->
## TOPIC 00133: Triggers:Start:Terminal Name

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-starttriggerterminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-starttriggerterminalname.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal name for the output trigger signal of the Start trigger. You can use this terminal name as an input signal source for another trigger. Remarks The following table lists the characteristics of this property. Short Name Start Trigger Terminal Name Data type cstr.png Permissions

### Triggers:Start:Terminal Name

Specifies the terminal name for the output trigger signal of the Start trigger.

You can use this terminal name as an input signal source for another trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-starttriggertype.html language=enus -->
## TOPIC 00134: Triggers:Start:Type

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-starttriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-starttriggertype.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Start trigger type. The digital pattern instrument waits for this trigger after you call the niDigital Initiate VI or the niDigital Burst Pattern VI, and does not burst a pattern until this trigger is received. Related information niDigital Burst Pattern VI niDigital Initiate VI Remark

### Triggers:Start:Type

Specifies the Start trigger type.

The digital pattern instrument waits for this trigger after you call the niDigital Initiate VI or the niDigital Burst Pattern VI, and does not burst a pattern until this trigger is received.

**Related information**

- niDigital Burst Pattern VI
- niDigital Initiate VI

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

| None | 1700 | Disable the Start trigger. Pattern bursting starts immediately after you call the niDigital Initiate VI or the niDigital Burst Pattern VI. |
| --- | --- | --- |
| Digital Edge | 1701 | Pattern bursting does not start until the digital pattern instrument detects a digital edge. |
| Software | 1702 | Pattern burst does not start until the digital pattern instrument receives a software Start trigger. Create a software Start trigger by calling the niDigital Send Software Edge Trigger VI and selecting start trigger in the trigger parameter. Related information niDigital Send Software Edge Trigger VI |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-supportedinstrumentmodels.html language=enus -->
## TOPIC 00135: Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-supportedinstrumentmodels.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-supportedinstrumentmodels.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a comma delimited string that contains the supported digital pattern instrument models for the specific driver. Remarks The following table lists the characteristics of this property. Short Name Supported Instrument Models Data type cstr.png Permissions Read Only High-level VIs N/A Channel-b

### Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models

Returns a comma delimited string that contains the supported digital pattern instrument models for the specific driver.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Supported Instrument Models |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-terminationmode.html language=enus -->
## TOPIC 00136: Levels:Termination Mode

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-terminationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-terminationmode.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of the pin during non-drive cycles. Remarks The following table lists the characteristics of this property. Short Name Termination Mode Data type ci32.png Permissions Read/Write High-level VIs niDigital Configure Termination Mode Channel-based Yes Resettable Yes High Z 1202 Sp

### Levels:Termination Mode

Specifies the behavior of the pin during non-drive cycles.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Termination Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital Configure Termination Mode |
| Channel-based | Yes |
| Resettable | Yes |

| High Z | 1202 | Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver is put in a high-impedance state and the active load is disabled. |
| --- | --- | --- |
| Active Load | 1200 | Specifies that, for non-drive pin states (L, H, X, V, M, E), the active load is connected and the digital pattern instrument sources or sinks a defined amount of current to load the DUT. The amount of current sourced by the instrument and therefore sunk by the DUT is specified by IOL. The amount of current sunk by the instrument and therefore sourced by the DUT is specified by IOH. The voltage at which the instrument changes between sourcing and sinking is specified by VCOM. |
| Vterm | 1201 | Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver terminates the pin to the configured VTERM voltage through a 50 ohms impedance. VTERM is adjustable to allow for the pin to terminate at a set level. This is useful for devices that might operate incorrectly if an instrument pin is unterminated and is allowed to float to any voltage level within the instrument voltage range. To address this issue, enable VTERM by configuring the VTERM pin level to the desired voltage and selecting the VTERM termination mode. Setting VTERM to 0 V and selecting the VTERM termination mode has the effect of connecting a 50 ohms termination to ground, which provides an effective 50 ohms impedance for the pin. This can be useful for improving signal integrity of certain DUTs by reducing reflections while the DUT drives the pin. |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vcom.html language=enus -->
## TOPIC 00137: Levels:Active Load:Vcom

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vcom.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vcom.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level at which the active load circuit switches between sourcing current and sinking current. Remarks The following table lists the characteristics of this property. Short Name Vcom Data type cdbl.png Permissions Read/Write High-level VIs niDigital Configure Active Load Levels

### Levels:Active Load:Vcom

Specifies the voltage level at which the active load circuit switches between sourcing current and sinking current.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Vcom |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital Configure Active Load Levels |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vih.html language=enus -->
## TOPIC 00138: Levels:Vih

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vih.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vih.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic high (1). Remarks The following table lists the characteristics of this property. Short Name Vih Data type cdbl.png Permissions Read/Write High-level VIs niDigital Con

### Levels:Vih

Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic high (1).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Vih |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital Configure Voltage Levels |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vil.html language=enus -->
## TOPIC 00139: Levels:Vil

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vil.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vil.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic low (0). Remarks The following table lists the characteristics of this property. Short Name Vil Data type cdbl.png Permissions Read/Write High-level VIs niDigital Conf

### Levels:Vil

Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic low (0).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Vil |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital Configure Voltage Levels |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-voh.html language=enus -->
## TOPIC 00140: Levels:Voh

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-voh.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-voh.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output voltage from the DUT above which the comparator on the digital pattern test instrument interprets a logic high (H). Remarks The following table lists the characteristics of this property. Short Name Voh Data type cdbl.png Permissions Read/Write High-level VIs niDigital Configure

### Levels:Voh

Specifies the output voltage from the DUT above which the comparator on the digital pattern test instrument interprets a logic high (H).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Voh |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital Configure Voltage Levels |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vol.html language=enus -->
## TOPIC 00141: Levels:Vol

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vol.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vol.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output voltage from the DUT below which the comparator on the digital pattern test instrument interprets a logic low (L). Remarks The following table lists the characteristics of this property. Short Name Vol Data type cdbl.png Permissions Read/Write High-level VIs niDigital Configure

### Levels:Vol

Specifies the output voltage from the DUT below which the comparator on the digital pattern test instrument interprets a logic low (L).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Vol |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital Configure Voltage Levels |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vterm.html language=enus -->
## TOPIC 00142: Levels:Vterm

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vterm.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/nidigital-rc/nidigital/pnidigital-vterm.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the termination voltage the digital pattern instrument applies during non-drive cycles when the termination mode is set to V[term]. The instrument applies the termination voltage through a 50 ohms parallel termination resistance. Remarks The following table lists the characteristics of thi

### Levels:Vterm

Specifies the termination voltage the digital pattern instrument applies during non-drive cycles when the termination mode is set to V<sub>term</sub>. The instrument applies the termination voltage through a 50 ohms parallel termination resistance.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Vterm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niDigital Configure Voltage Levels |
| Channel-based | Yes |
| Resettable | Yes |

Parent topic:

niDigital Properties

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/patterns-mnu.html language=enus -->
## TOPIC 00143: Pattern

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/patterns-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/patterns-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to load and unload digital patterns and to specify patterns to burst. Refer to the Patterns topic for more information about configuring patterns. icon

### Pattern

Use these VIs to load and unload digital patterns and to specify patterns to burst. Refer to the [Patterns](/csh?context=niDigital_digipat_patterns-overview) topic for more information about configuring patterns.

[IMAGE alt='icon' src='patterns-mnu.png']

- [niDigital Load Pattern VI](../../instr-lib/nidigital/nidigital-llb/nidigital-load-pattern-vi.html) Loads the specified pattern file.
- [niDigital Configure Start Label VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-start-label-vi.html) Configures the pattern name or exported label in the loaded patterns from which to start bursting the pattern. If you want to start bursting the pattern from the first vector, specify the pattern name.
- [niDigital Get Pattern Pins VI](../../instr-lib/nidigital/nidigital-llb/nidigital-get-pattern-pins-vi.html) Returns the names of the pins referenced by the pattern.
- [niDigital Unload All Patterns VI](../../instr-lib/nidigital/nidigital-llb/nidigital-unload-all-patterns-vi.html) Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/pinmap-mnu.html language=enus -->
## TOPIC 00144: Pin Map

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/pinmap-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/pinmap-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to interact with or create pin maps. Refer to the Pin and Channel Map Editor topic for more information about configuring pin and channel maps. icon

### Pin Map

Use these VIs to interact with or create pin maps. Refer to the [Pin and Channel Map Editor](/csh?context=niDigital_digipat_pin-channel-map-editor) topic for more information about configuring pin and channel maps.

[IMAGE alt='icon' src='pinmap-mnu.png']

- [niDigital Load Pin Map VI](../../instr-lib/nidigital/nidigital-llb/nidigital-load-pin-map-vi.html) Loads a pin map file.
- [niDigital Enable Sites VI](../../instr-lib/nidigital/nidigital-llb/nidigital-enable-sites-vi.html) Enables the sites you specify. All sites are enabled by default. NI TestStand Semiconductor Module requires all sites to always be enabled, and manages the set of active sites without disabling the sites in the digital pattern instrument session. Do not use this VI with the Semiconductor Module.
- [niDigital Disable Sites VI](../../instr-lib/nidigital/nidigital-llb/nidigital-disable-sites-vi.html) Disables the sites you specify. Disabled sites are not included in pattern bursts initiated by niDigital Initiate VI or niDigital Burst Pattern VI, even if the site is specified in the list of pattern burst sites in niDigital Configure Pattern Burst Sites VI or in the site list parameter of the niDigital Burst Pattern VI. Additionally, if you specify a list of pin or pin group names in a channel list parameter in any NI-Digital VI, digital pattern instrument channels mapped to disabled sites are not affected by the VI. VIs that return per-pin data, such as niDigital PPMU Measure VI, do not return data for channels mapped to disabled sites.
- [niDigital Is Site Enabled VI](../../instr-lib/nidigital/nidigital-llb/nidigital-is-site-enabled-vi.html) Checks if a site you specify is enabled.
- [Low Level](../../instr-lib/nidigital/lowlevelpinmap-mnu.html) Use these VIs to configure low-level settings of pin maps and pin groups. Use these VIs if you are not loading a pin map file using the niDigital Load Pin Map VI.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/ppmuaction-mnu.html language=enus -->
## TOPIC 00145: PPMU

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/ppmuaction-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/ppmuaction-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to source voltage or current from the PPMU and measure voltage or current from the DUT. Refer to the Pin Parametric Measurement Unit (PPMU) topic for more information about the PPMU. icon

### PPMU

Use these VIs to source voltage or current from the PPMU and measure voltage or current from the DUT. Refer to the [Pin Parametric Measurement Unit (PPMU)](/csh?context=niDigital_digipat6570_ppmu-overview) topic for more information about the PPMU.

[IMAGE alt='icon' src='ppmuaction-mnu.png']

- [niDigital PPMU Source VI](../../instr-lib/nidigital/nidigital-llb/nidigital-ppmu-source-vi.html) Starts sourcing voltage or current from the PPMU. This VI automatically selects the PPMU function. Changes to PPMU source settings do not take effect until you call this VI.
- [niDigital PPMU Measure VI](../../instr-lib/nidigital/nidigital-llb/nidigital-ppmu-measure-vi.html) Instructs the PPMU to measure voltage or current. This VI can be called to take a voltage measurement even if the pin function is not set to PPMU.

Parent topic:

Action

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/ppmuconfiguration-mnu.html language=enus -->
## TOPIC 00146: PPMU

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/ppmuconfiguration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/ppmuconfiguration-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to configure the current and voltage levels that the PPMU outputs or measures to the DUT. Refer to the Pin Parametric Measurement Unit (PPMU) topic for more information about configuring the PPMU. icon

### PPMU

Use these VIs to configure the current and voltage levels that the PPMU outputs or measures to the DUT. Refer to the [Pin Parametric Measurement Unit (PPMU)](/csh?context=niDigital_digipat6570_ppmu-overview) topic for more information about configuring the PPMU.

[IMAGE alt='icon' src='ppmuconfiguration-mnu.png']

- [niDigital PPMU Configure Output Function VI](../../instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-output-function-vi.html) Configures to source DC voltage or DC current from the PPMU.
- [niDigital PPMU Configure Aperture Time VI](../../instr-lib/nidigital/nidigital-llb/nidigital-ppmu-configure-aperture-time-vi.html) Configures the aperture time for the PPMU measurement on the specified channel(s).
- [DC Voltage](../../instr-lib/nidigital/dcvoltage-mnu.html) Use these VIs to change channel settings when the channel is configured for DC voltage.
- [DC Current](../../instr-lib/nidigital/dccurrent-mnu.html) Use these VIs to change channel settings when the channel is configured for DC current.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/sequencerflagsandregisters-mnu.html language=enus -->
## TOPIC 00147: Sequencer Flags and Registers

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/sequencerflagsandregisters-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/sequencerflagsandregisters-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to create and configure sequencer flags and registers with the NI-Digital Pattern Driver. Refer to the Sequencer Flags and Registers topic for more information about sequencer flags and registers. icon

### Sequencer Flags and Registers

Use these VIs to create and configure sequencer flags and registers with the NI-Digital Pattern Driver. Refer to the [Sequencer Flags and Registers](/csh?context=niDigital_digipat6570_sequencer-flags-registers) topic for more information about sequencer flags and registers.

[IMAGE alt='icon' src='sequencerflagsandregisters-mnu.png']

- [niDigital Write Sequencer Flag VI](../../instr-lib/nidigital/nidigital-llb/nidigital-write-sequencer-flag-vi.html) Writes the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.
- [niDigital Read Sequencer Flag VI](../../instr-lib/nidigital/nidigital-llb/nidigital-read-sequencer-flag-vi.html) Reads the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.
- [niDigital Write Sequencer Register VI](../../instr-lib/nidigital/nidigital-llb/nidigital-write-sequencer-register-vi.html) Writes a value to a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program.
- [niDigital Read Sequencer Register VI](../../instr-lib/nidigital/nidigital-llb/nidigital-read-sequencer-register-vi.html) Reads the value of a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. For example, you can use this VI to read a register modified by the write_reg opcode during a pattern burst.

Parent topic:

Action

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/sourcecaptureaction-mnu.html language=enus -->
## TOPIC 00148: Source and Capture

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/sourcecaptureaction-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/sourcecaptureaction-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to create, configure, write, and fetch source and capture waveforms with the NI-Digital Pattern Driver. Refer to the Source Waveform Configurations topic and the Capture Waveform Configurations topic for more information about configuring source and capture waveforms, respectively. ico

### Source and Capture

Use these VIs to create, configure, write, and fetch source and capture waveforms with the NI-Digital Pattern Driver. Refer to the [Source Waveform Configurations](/csh?context=niDigital_digipat_source-waveform-config) topic and the [Capture Waveform Configurations](/csh?context=niDigital_digipat_capture-waveform-config) topic for more information about configuring source and capture waveforms, respectively.

[IMAGE alt='icon' src='sourcecaptureaction-mnu.png']

- [niDigital Create Source Waveform VI](../../instr-lib/nidigital/nidigital-llb/nidigital-create-source-waveform-vi.html) Creates a source waveform. Use source waveforms to specify drive data for a pattern burst at runtime instead of compiling drive pin states into the pattern.
- [niDigital Write Source Waveform VI](../../instr-lib/nidigital/nidigital-llb/nidigital-write-source-waveform-vi.html) Writes a source waveform after a waveform is created.
- [niDigital Create Capture Waveform VI](../../instr-lib/nidigital/nidigital-llb/nidigital-create-capture-waveform-vi.html) Creates waveforms to acquire data during a pattern burst.
- [niDigital Fetch Capture Waveform (U32) VI](../../instr-lib/nidigital/nidigital-llb/nidigital-fetch-capture-waveform-u32-vi.html) Fetches a defined number of samples for a specific list of sites.

Parent topic:

Action

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/static-mnu.html language=enus -->
## TOPIC 00149: Static

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/static-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/static-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to program read and write static states for the pin driver. icon

### Static

Use these VIs to program read and write static states for the pin driver.

[IMAGE alt='icon' src='static-mnu.png']

- [niDigital Write Static VI](../../instr-lib/nidigital/nidigital-llb/nidigital-write-static-vi.html) Writes a static state to the specified pins. The selected pins remain in the specified state until the next pattern burst or call to this VI. If there are uncommitted changes to levels or the termination mode, this VI commits the changes to the pins.
- [niDigital Read Static VI](../../instr-lib/nidigital/nidigital-llb/nidigital-read-static-vi.html) Reads the current state of comparators for pins you specify in the channel list parameter. If there are uncommitted changes to levels or the termination mode, this VI commits the changes to the pins.

Parent topic:

Action

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/tdr-mnu.html language=enus -->
## TOPIC 00150: TDR

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/tdr-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/tdr-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to measure pin propagation delay using Time-Domain Reflectometry (TDR) and to apply delay values to the pins of a digital pattern instrument. icon

### TDR

Use these VIs to measure pin propagation delay using Time-Domain Reflectometry (TDR) and to apply delay values to the pins of a digital pattern instrument.

[IMAGE alt='icon' src='tdr-mnu.png']

- [niDigital TDR VI](../../instr-lib/nidigital/nidigital-llb/nidigital-tdr-vi.html) Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR).
- [niDigital Apply TDR Offsets VI](../../instr-lib/nidigital/nidigital-llb/nidigital-apply-tdr-offsets-vi.html) Applies the correction for propagation delay offsets to a digital pattern instrument. Use this VI to apply TDR offsets that are stored from a past measurement or are measured by means other than the niDigital TDR VI. Also use this VI to apply correction for offsets if the apply offsets input of the niDigital TDR VI was set to False at the time of measurement.

Parent topic:

Levels and Timing

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/timesets-mnu.html language=enus -->
## TOPIC 00151: Time Set

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/timesets-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/timesets-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to program time sets for a digital pattern instrument. Use these VIs to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. These VIs do not modify the timing sheet

### Time Set

Use these VIs to program time sets for a digital pattern instrument. Use these VIs to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. These VIs do not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; they only affect the values of the current timing context.

[IMAGE alt='icon' src='timesets-mnu.png']

- [niDigital Create Time Set VI](../../instr-lib/nidigital/nidigital-llb/nidigital-create-time-set-vi.html) Creates a time set with the name that you specify. Use this VI when you want to create time sets programmatically rather than with a timing sheet.
- [niDigital Configure Time Set Period VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-period-vi.html) Configures the period of a time set. Use this function to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; it only affects the values of the current timing context.
- [niDigital Configure Time Set Drive Edges (Poly) VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-drive-edges-poly-vi.html) Configures the drive format and drive edge placement for the specified pins. Use this VI to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This VI does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; it affects the values of the current timing context.
- [niDigital Configure Time Set Compare Edges (Poly) VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-compare-edges-poly-vi.html) Configures the strobe edge time for the specified pins. Use this function to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; it only affects the values of the current timing context.
- [niDigital Configure Time Set Edge Multiplier VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-time-set-edge-multiplier-vi.html) Configures the edge multiplier of the pins in the time set. Use this function to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; it only affects the values of the current timing context.
- [niDigital Delete All Time Sets VI](../../instr-lib/nidigital/nidigital-llb/nidigital-delete-all-time-sets-vi.html) Deletes all time sets from digital pattern instrument memory.
- [Low Level](../../instr-lib/nidigital/lowleveltimesets-mnu.html) Use these VIs to program time sets for a digital pattern instrument. Use these VIs to modify time set values after applying a timing sheet with the niDigital Apply Levels and Timing VI, or to create time sets programmatically without the use of timing sheets. These VIs do not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital Apply Levels and Timing; they only affect the values of the current timing context.

Parent topic:

Levels and Timing

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/trigger-mnu.html language=enus -->
## TOPIC 00152: Trigger

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/trigger-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/trigger-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to configure triggers. icon

### Trigger

Use these VIs to configure triggers.

[IMAGE alt='icon' src='trigger-mnu.png']

- [niDigital Configure Trigger VI](../../instr-lib/nidigital/nidigital-llb/nidigital-configure-trigger-vi.html) Configures triggers.
- [niDigital Export Signal VI](../../instr-lib/nidigital/nidigital-llb/nidigital-export-signal-vi.html) Routes trigger and event signals to the output terminal you specify.

Parent topic:

Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-labview-api-ref path=instr-lib/nidigital/utility-mnu.html language=enus -->
## TOPIC 00153: Utility

- bundle_id: `ni-digital-pattern-labview-api-ref`
- source_path: `instr-lib/nidigital/utility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-labview-api-ref/raw/resource/enus/instr-lib/nidigital/utility-mnu.html
- document_id: `ni-digital-pattern-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these VIs to program NI-Digital Pattern Driver functionality. icon

### Utility

Use these VIs to program NI-Digital Pattern Driver functionality.

[IMAGE alt='icon' src='utility-mnu.png']

- [niDigital Reset VI](../../instr-lib/nidigital/nidigital-llb/nidigital-reset-vi.html) Resets a digital pattern instrument to a known state.
- [niDigital Reset Device VI](../../instr-lib/nidigital/nidigital-llb/nidigital-reset-device-vi.html) Returns a digital pattern instrument to a known state.
- [niDigital Self Test VI](../../instr-lib/nidigital/nidigital-llb/nidigital-self-test-vi.html) Returns self test results from a digital pattern instrument. This test requires several minutes to execute.
- [niDigital Sort Results VI](../../instr-lib/nidigital/nidigital-llb/nidigital-sort-results-vi.html) Organizes pin and site data for multiple digital pattern instruments. Pin and site data are grouped by site number.
- [niDigital Get Results Pin Map Information VI](../../instr-lib/nidigital/nidigital-llb/nidigital-get-results-pin-map-information-vi.html) Returns the pin names and site numbers that correspond to data read from the digital pattern instrument.
- [niDigital Get Session Reference VI](../../instr-lib/nidigital/nidigital-llb/nidigital-get-session-reference-vi.html) Returns a session reference you can pass to NI-TClk VIs to synchronize multiple digital pattern instruments and/or other types of instruments. The session reference parameter is a generic type.
- [niDigital Enable Match Fail Combination (Poly) VI](../../instr-lib/nidigital/nidigital-llb/nidigital-enable-match-fail-combination-poly-vi.html) Configures synchronized digital pattern instruments as well as the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across digital pattern instruments based on those results.
- [niDigital Burst Pattern (Synchronized) VI](../../instr-lib/nidigital/nidigital-llb/nidigital-burst-pattern-synchronized-vi.html) Uses the start label you specify to burst a pattern on the sites you specify. Use this VI to burst a pattern on digital pattern instruments that you have previously synchronized using NI-TClk.
- [niDigital Write Sequencer Flag (Synchronized) VI](../../instr-lib/nidigital/nidigital-llb/nidigital-write-sequencer-flag-synchronized-vi.html) Writes a Boolean value to the pattern sequencer flag for synchronized devices. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime program.
- [niDigital Error Message VI](../../instr-lib/nidigital/nidigital-llb/nidigital-error-message-vi.html) Returns the error message.
- [niDigital Get Channel Name (Poly) VI](../../instr-lib/nidigital/nidigital-llb/nidigital-get-channel-name-poly-vi.html) Returns a channel name or a comma-delimited list of channel names.
- [MeasurementLink](../../instr-lib/nidigital/measurementlink-mnu.html) Use the VIs on this palette in conjunction with MeasurementLink Session Management.

Parent topic:

NI-Digital
