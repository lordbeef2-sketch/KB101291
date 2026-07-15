# NI DOCUMENT BUNDLE: rfmx-pulse-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-pulse-vi start=1 end=29 -->
<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/advanced_pal.html language=enus -->
## TOPIC 00001: Advanced

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/advanced_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/advanced_pal.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

Advanced

Owning Palette:

RFmx Pulse VIs

Use the VIs on this palette to use advanced features.

| Palette Object | Description |
| --- | --- |
| RFmxPulse Abort Measurements | Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxPulse Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error. |
| RFmxPulse Analyze (IQ, 1 Wfm) | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended Acquisition Type property value is either IQ or IQ or Spectral. |
| RFmxPulse Create Signal Configuration | Creates a new instance of a signal. |
| RFmxPulse Clone Signal Configuration | Creates a new instance of a signal by copying all the property values from an existing signal instance. |
| RFmxPulse Delete Signal Configuration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxPulse Get All Named Result Names | Returns all the named result names of the signal that you specify in the Selector String parameter. |
| RFmxPulse Clear Named Result | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxPulse Clear All Named Results | Clears all results for the signal that you specify in the Selector String parameter. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/configuration_pal.html language=enus -->
## TOPIC 00002: Configuration

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/configuration_pal.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

Configuration

Owning Palette:

RFmx Pulse VIs

Use the VIs on this palette to configure RFmxPulse measurements. You can use the [RFmxPulse Property Node](../rfmxpulsevi/rfmxpulse_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxPulse Configure RF | Configures the RF properties of the signal specified by the selector string. |
| RFmxPulse Configure Frequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| RFmxPulse Configure Reference Level | Configures the reference level, which represents the maximum expected power of an RF input signal. |
| RFmxPulse Auto Level | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level. |
| RFmxPulse Configure External Attenuation | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. |
| RFmxPulse Configure Trigger | Configures the reference trigger to use to acquire the signal. |
| RFmxPulse Send Software Edge Trigger | Sends a trigger to the device when you use the RFmxPulse Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/fetch_pal.html language=enus -->
## TOPIC 00003: Fetch

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/fetch_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/fetch_pal.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

Fetch

Owning Palette:

RFmx Pulse VIs

Use the VIs on this palette to fetch measurement results and traces.

| Palette Object | Description |
| --- | --- |
| RFmxPulse Fetch | Fetches pulse measurement results. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/pulse_pal.html language=enus -->
## TOPIC 00004: RFmx Pulse VIs

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/pulse_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/pulse_pal.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmx Pulse VIs

Use the VIs on this palette to perform Pulse measurements. You can use the [RFmxPulse Property Node](../rfmxpulsevi/rfmxpulse_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxPulse Select Measurement | Specifies the measurement that you want to enable. |
| RFmxPulse Initiate | Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the RFmxPulse Wait for Measurement Complete VI or RFmxPulse Check Measurement Status VI. |
| RFmxPulse Property Node | Gets (reads), sets (writes), or resets (sets to default value) RFmxPulse properties. |

| Subpalette | Description |
| --- | --- |
| Configuration | Use the VIs on this palette to configure RFmxPulse measurements. You can use the RFmxPulse Property Node to configure additional properties. |
| Fetch | Use the VIs on this palette to fetch measurement results and traces. |
| Utility | Use the VIs on this palette to configure RFmx Pulse utilities. |
| Advanced | Use the VIs on this palette to use advanced features. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_abort_measurements.html language=enus -->
## TOPIC 00005: RFmxPulse Abort Measurements (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_abort_measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_abort_measurements.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Abort Measurements (VI)

Owning Palette:

Advanced

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxPulse Initiate](rfmxpulse_initiate.html) VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='RFmxPulse Abort Measurements' src='rfmxpulse_abort_measurements.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_analyze_(iq_1_wfm).html language=enus -->
## TOPIC 00006: RFmxPulse Analyze (IQ, 1 Wfm) (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_analyze_(iq_1_wfm).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_analyze_(iq_1_wfm).html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Analyze (IQ, 1 Wfm) (VI)

Owning Palette:

Advanced

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?topicname=rfmxinstrprop/attr27.html) property value is either **IQ** or **IQ or Spectral**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmx Pulse Commit VI. |
| --- | --- |

[IMAGE alt='RFmxPulse Analyze (IQ, 1 Wfm)' src='rfmxpulse_analyze_(iq,_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with the option string as "AnalysisOnly=1". |
| --- | --- |
|  | IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 specifies the start time of the input y array. This value is expressed in seconds. dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input y array. This value is expressed in seconds. |
|  | dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter on Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_auto_level.html language=enus -->
## TOPIC 00007: RFmxPulse Auto Level (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_auto_level.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Auto Level (VI)

Owning Palette:

Configuration

Examines the input signal to calculate the peak power level and sets it as the value of the [Reference Level](/csh?topicname=rfmxpulseprop/attrc00002.html) property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxPulse Auto Level VI does the following:

1. Resets the mixer level, mixer level offset and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

You can also specify the starting reference level using the [Auto Level Initial Reference Level](/csh?topicname=rfmxpulseprop/attrc0000d.html) property.

When using PXIe-5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmx Pulse Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this VI, thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='RFmxPulse Auto Level' src='rfmxpulse_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Bandwidth (Hz) specifies the bandwidth, in Hz, of the signal to be analyzed. The default value is 80 MHz. |
|  | Measurement Interval (s) specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Reference Level returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and as Vpk-pk for baseband devices. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_check_measurement_status.html language=enus -->
## TOPIC 00008: RFmxPulse Check Measurement Status (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_check_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_check_measurement_status.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Check Measurement Status (VI)

Owning Palette:

Utility

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='RFmxPulse Check Measurement Status' src='rfmxpulse_check_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | done? indicates whether the measurement is complete. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_clear_all_named_results.html language=enus -->
## TOPIC 00009: RFmxPulse Clear All Named Results (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_clear_all_named_results.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_clear_all_named_results.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Clear All Named Results (VI)

Owning Palette:

Advanced

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxPulse Clear All Named Results' src='rfmxpulse_clear_all_named_results.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_clear_named_result.html language=enus -->
## TOPIC 00010: RFmxPulse Clear Named Result (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_clear_named_result.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_clear_named_result.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Clear Named Result (VI)

Owning Palette:

Advanced

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='RFmxPulse Clear Named Result' src='rfmxpulse_clear_named_result.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_clone_signal_configuration.html language=enus -->
## TOPIC 00011: RFmxPulse Clone Signal Configuration (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_clone_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_clone_signal_configuration.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Clone Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='RFmxPulse Clone Signal Configuration' src='rfmxpulse_clone_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
|  | Old Signal Name specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter on Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_commit.html language=enus -->
## TOPIC 00012: RFmxPulse Commit (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_commit.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Commit (VI)

Owning Palette:

Utility

Commits settings to the hardware. Calling this VI is optional. RFmxPulse commits settings to the hardware when you call the [RFmxPulse Initiate](rfmxpulse_initiate.html) VI or any of the measurement Read VIs.

[IMAGE alt='RFmxPulse Commit' src='rfmxpulse_commit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_configure_external_attenuation.html language=enus -->
## TOPIC 00013: RFmxPulse Configure External Attenuation (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_configure_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_configure_external_attenuation.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Configure External Attenuation (VI)

Owning Palette:

Configuration

Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer.

[IMAGE alt='RFmxPulse Configure External Attenuation' src='rfmxpulse_configure_external_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | External Attenuation specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_configure_frequency.html language=enus -->
## TOPIC 00014: RFmxPulse Configure Frequency (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_configure_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_configure_frequency.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Configure Frequency (VI)

Owning Palette:

Configuration

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

[IMAGE alt='RFmxPulse Configure Frequency' src='rfmxpulse_configure_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency (Hz) specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_configure_reference_level.html language=enus -->
## TOPIC 00015: RFmxPulse Configure Reference Level (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_configure_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_configure_reference_level.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Configure Reference Level (VI)

Owning Palette:

Configuration

Configures the reference level, which represents the maximum expected power of an RF input signal.

[IMAGE alt='RFmxPulse Configure Reference Level' src='rfmxpulse_configure_reference_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Level specifies the reference level which represents the maximum expected power of an RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default of this property is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_configure_reference_waveform_(1_wfm).html language=enus -->
## TOPIC 00016: RFmxPulse Configure Reference Waveform (1 Wfm) (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_configure_reference_waveform_(1_wfm).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_configure_reference_waveform_(1_wfm).html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Configure Reference Waveform (1 Wfm) (VI)

Configures the reference pulse waveform used for time sidelobe measurements.

[IMAGE alt='RFmxPulse Configure Reference Waveform (1 Wfm)' src='rfmxpulse_configure_reference_waveform_(1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Waveform specifies the reference waveform used for correlation computation in time sidelobe Measurements. The default value is an empty waveform. x0 specifies the starting time of the reference waveform. This value is expressed in seconds. dx specifies the sampling interval of the reference waveform. This value is expressed in seconds. y specifies an array of waveform samples of the reference waveform. |
|  | x0 specifies the starting time of the reference waveform. This value is expressed in seconds. |
|  | dx specifies the sampling interval of the reference waveform. This value is expressed in seconds. |
|  | y specifies an array of waveform samples of the reference waveform. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_configure_rf.html language=enus -->
## TOPIC 00017: RFmxPulse Configure RF (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_configure_rf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_configure_rf.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Configure RF (VI)

Owning Palette:

Configuration

Configures the RF properties of the signal specified by the selector string.

[IMAGE alt='RFmxPulse Configure RF' src='rfmxpulse_configure_rf.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency (Hz) specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. |
|  | Reference Level specifies the reference level which represents the maximum expected power of an RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default of this property is hardware dependent. |
|  | External Attenuation specifies the attenuation, in dB, of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_configure_trigger.html language=enus -->
## TOPIC 00018: RFmxPulse Configure Trigger (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_configure_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_configure_trigger.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Configure Trigger (VI)

Owning Palette:

Configuration

Configures the reference trigger to use to acquire the signal.

#### RFmxPulse Configure IQ Power Edge Trigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.

To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

[IMAGE alt='RFmxPulse Configure IQ Power Edge Trigger' src='rfmxpulse_configure_iq_power_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | IQ Power Edge Source specifies the channel from which the device monitors the trigger. The default of this property is hardware dependent. |
|  | IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
|  | IQ Power Edge Level (dB or dBm) specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative and is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this property is hardware dependent. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Trigger Delay (s) specifies the trigger delay time, in seconds. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | Minimum Quiet Time Mode specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Manual. Manual (0) The minimum quiet time used for triggering is the value of the Min Quiet Time parameter. Auto (1) The measurement computes the minimum quiet time used for triggering. |
| Manual (0) | The minimum quiet time used for triggering is the value of the Min Quiet Time parameter. |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |
|  | Minimum Quiet Time (s) specifies the duration, in seconds, for which the signal must be quiet before the signal analyzer arms the I/Q Power Edge trigger. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default of this property is hardware dependent. |
|  | IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. The default value is Absolute. Relative (0) The IQ Power Edge Level parameter is relative to the value of the Reference Level property. Absolute (1) The IQ Power Edge Level parameter specifies the absolute power. |
| Relative (0) | The IQ Power Edge Level parameter is relative to the value of the Reference Level property. |
| Absolute (1) | The IQ Power Edge Level parameter specifies the absolute power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Configure Software Edge Trigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

[IMAGE alt='RFmxPulse Configure Software Edge Trigger' src='rfmxpulse_configure_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Trigger Delay (s) specifies the trigger delay time, in seconds. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Configure Digital Edge Trigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

[IMAGE alt='RFmxPulse Configure Digital Edge Trigger' src='rfmxpulse_configure_digital_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Digital Edge Source specifies the source terminal for the digital edge trigger. The default of this property is hardware dependent. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. PXIe_DStarB (PXIe_DStarB ) The trigger is received on the PXIe DStar B trigger line. TimerEvent (TimerEvent) The trigger is received from the timer event. |
| PFI0 (PFI0) | The trigger is received on PFI 0. |
| PFI1 (PFI1) | The trigger is received on PFI 1. |
| PXI_Trig0 (PXI_Trig0) | The trigger is received on PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | The trigger is received on PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | The trigger is received on PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | The trigger is received on PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | The trigger is received on PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | The trigger is received on PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | The trigger is received on PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | The trigger is received on PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | The trigger is received on the PXI star trigger line. |
| PXIe_DStarB (PXIe_DStarB ) | The trigger is received on the PXIe DStar B trigger line. |
| TimerEvent (TimerEvent) | The trigger is received from the timer event. |
|  | Digital Edge specifies the trigger edge to detect. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. |
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |
|  | Trigger Delay (s) specifies the trigger delay time, in seconds. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Disable Trigger

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='RFmxPulse Disable Trigger' src='rfmxpulse_disable_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_create_signal_configuration.html language=enus -->
## TOPIC 00019: RFmxPulse Create Signal Configuration (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_create_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_create_signal_configuration.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Create Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal.

[IMAGE alt='RFmxPulse Create Signal Configuration' src='rfmxpulse_create_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter on Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_delete_signal_configuration.html language=enus -->
## TOPIC 00020: RFmxPulse Delete Signal Configuration (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_delete_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_delete_signal_configuration.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Delete Signal Configuration (VI)

Owning Palette:

Advanced

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='RFmxPulse Delete Signal Configuration' src='rfmxpulse_delete_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_fetch.html language=enus -->
## TOPIC 00021: RFmxPulse Fetch (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_fetch.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Fetch (VI)

Owning Palette:

Fetch

Fetches pulse measurement results.

#### RFmxPulse Fetch Amplitude Trace

Fetches the amplitude trace of the selected pulse.

[IMAGE alt='RFmxPulse Fetch Amplitude Trace' src='rfmxpulse_fetch_amplitude_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Amplitude returns the trace of amplitude measured in units specified by Amplitude Trace Unit property. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the amplitude, in dBm. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the amplitude, in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Fetch IQ Trace

Fetches the IQ trace of the selected pulse.

[IMAGE alt='RFmxPulse Fetch IQ Trace' src='rfmxpulse_fetch_iq_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | IQ Data returns the trace of IQ data in time domain. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the in-phase and quadrature-phase values, in Volts. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the in-phase and quadrature-phase values, in Volts. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Fetch Stability Trace

Fetches the stability trace of the selected pulse.

[IMAGE alt='RFmxPulse Fetch Stability Trace' src='rfmxpulse_fetch_stability_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Pulse Amplitude Stability (dB) returns the trace of pulse amplitude stability, in dB. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the amplitude stability, in dB. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the amplitude stability, in dB. |
|  | Pulse Phase Stability (dB) returns the trace of pulse phase stability, in dB. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the phase stability, in dB. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the phase stability, in dB. |
|  | Pulse Total Stability (dB) returns the trace of pulse total stability, in dB. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the total stability, in dB. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the total stability, in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Fetch Pulse To Pulse Stability Trace

Fetches the pulse to pulse stability trace.

[IMAGE alt='RFmxPulse Fetch Pulse To Pulse Stability Trace' src='rfmxpulse_fetch_pulse_to_pulse_stability_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Pulse Index returns the pulse index. |
|  | Pulse To Pulse Amplitude Stability (dB) returns the trace of pulse to pulse amplitude stability, in dB. |
|  | Pulse To Pulse Phase Stability (dB) returns the trace of pulse to pulse phase stability, in dB. |
|  | Pulse To Pulse Total Stability (dB) returns the trace of pulse to pulse total stability, in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Fetch Burst Selected Position Stability Trace

Fetches the burst stability trace of the selected position.

[IMAGE alt='RFmxPulse Fetch Burst Selected Position Stability Trace' src='rfmxpulse_fetch_burst_selected_position_stability_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Pulse Amplitude Stability (dB) returns the trace of pulse amplitude stability, in dB. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the amplitude stability, in dB. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the amplitude stability, in dB. |
|  | Pulse Phase Stability (dB) returns the trace of pulse phase stability, in dB. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the phase stability, in dB. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the phase stability, in dB. |
|  | Pulse Total Stability (dB) returns the trace of pulse total stability, in dB. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the total stability, in dB. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the total stability, in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Fetch Multiple Measurement Points Stability Trace

Fetches the multiple measurement points stability trace.

[IMAGE alt='RFmxPulse Fetch Multiple Measurement Points Stability Trace' src='rfmxpulse_fetch_multiple_measurement_points_stability_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Pulse Average Amplitude Stability (dB) returns the pulse average amplitude stability trace at multiple measurement points. This value is expressed in dB. x0 returns the start time of measurement window, in seconds. dx returns the sample duration of measurement window, in seconds. y returns the average amplitude stability of multiple measurement points, in dB. |
|  | x0 returns the start time of measurement window, in seconds. |
|  | dx returns the sample duration of measurement window, in seconds. |
|  | y returns the average amplitude stability of multiple measurement points, in dB. |
|  | Pulse Average Phase Stability (dB) returns the pulse average phase stability trace at multiple measurement points. This value is expressed in dB. x0 returns the start time of measurement window, in seconds. dx returns the sample duration of measurement window, in seconds. y returns the average phase stability of multiple measurement points, in dB. |
|  | x0 returns the start time of measurement window, in seconds. |
|  | dx returns the sample duration of measurement window, in seconds. |
|  | y returns the average phase stability of multiple measurement points, in dB. |
|  | Pulse Average Total Stability (dB) returns the pulse average total stability trace at multiple measurement points. This value is expressed in dB. x0 returns the start time of measurement window, in seconds. dx returns the sample duration of measurement window, in seconds. y returns the average total stability of multiple measurement points, in dB. |
|  | x0 returns the start time of measurement window, in seconds. |
|  | dx returns the sample duration of measurement window, in seconds. |
|  | y returns the average total stability of multiple measurement points, in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Fetch Intrapulse Stability Trace

Fetches the intrapulse stability trace over multiple measurement points, for the selected pulse or position.

[IMAGE alt='RFmxPulse Fetch Intrapulse Stability Trace' src='rfmxpulse_fetch_intrapulse_stability_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Intrapulse Amplitude Stability (dB) returns the intrapulse amplitude stability trace at multiple measurement points. This value is expressed in dB. x0 returns the start time of measurement window, in seconds. dx returns the sample duration of measurement window, in seconds. y returns the intrapulse amplitude stability of multiple measurement points, in dB. |
|  | x0 returns the start time of measurement window, in seconds. |
|  | dx returns the sample duration of measurement window, in seconds. |
|  | y returns the intrapulse amplitude stability of multiple measurement points, in dB. |
|  | Intrapulse Phase Stability (dB) returns the intrapulse phase stability trace at multiple measurement points. This value is expressed in dB. x0 returns the start time of measurement window, in seconds. dx returns the sample duration of measurement window, in seconds. y returns the intrapulse phase stability of multiple measurement points, in dB. |
|  | x0 returns the start time of measurement window, in seconds. |
|  | dx returns the sample duration of measurement window, in seconds. |
|  | y returns the intrapulse phase stability of multiple measurement points, in dB. |
|  | Intrapulse Total Stability (dB) returns the intrapulse total stability trace at multiple measurement points. This value is expressed in dB. x0 returns the start time of measurement window, in seconds. dx returns the sample duration of measurement window, in seconds. y returns the intrapulse total stability of multiple measurement points, in dB. |
|  | x0 returns the start time of measurement window, in seconds. |
|  | dx returns the sample duration of measurement window, in seconds. |
|  | y returns the intrapulse total stability of multiple measurement points, in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Fetch Burst Intrapulse Stability Trace

Fetches the burst intrapulse stability trace, averaged across the pulses within a positional average burst, over multiple measurement points.

[IMAGE alt='RFmxPulse Fetch Burst Intrapulse Stability Trace' src='rfmxpulse_fetch_burst_intrapulse_stability_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Intrapulse Average Amplitude Stability (dB) returns the intrapulse average amplitude stability trace at multiple measurement points. This value is expressed in dB. x0 returns the start time of measurement window, in seconds. dx returns the sample duration of measurement window, in seconds. y returns the intrapulse average amplitude stability of multiple measurement points, in dB. |
|  | x0 returns the start time of measurement window, in seconds. |
|  | dx returns the sample duration of measurement window, in seconds. |
|  | y returns the intrapulse average amplitude stability of multiple measurement points, in dB. |
|  | Intrapulse Average Phase Stability (dB) returns the intrapulse average phase stability trace at multiple measurement points. This value is expressed in dB. x0 returns the start time of measurement window, in seconds. dx returns the sample duration of measurement window, in seconds. y returns the intrapulse average phase stability of multiple measurement points, in dB. |
|  | x0 returns the start time of measurement window, in seconds. |
|  | dx returns the sample duration of measurement window, in seconds. |
|  | y returns the intrapulse average phase stability of multiple measurement points, in dB. |
|  | Intrapulse Average Total Stability (dB) returns the intrapulse average total stability trace at multiple measurement points. This value is expressed in dB. x0 returns the start time of measurement window, in seconds. dx returns the sample duration of measurement window, in seconds. y returns the intrapulse average total stability of multiple measurement points, in dB. |
|  | x0 returns the start time of measurement window, in seconds. |
|  | dx returns the sample duration of measurement window, in seconds. |
|  | y returns the intrapulse average total stability of multiple measurement points, in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Fetch Phase (Wrapped) Trace

Fetches the wrapped phase trace of the selected pulse.

[IMAGE alt='RFmxPulse Fetch Phase (Wrapped) Trace' src='rfmxpulse_fetch_phase_(wrapped)_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Wrapped Phase (deg) returns the trace of wrapped phase, in degrees. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the wrapped phase, in degrees. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the wrapped phase, in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Fetch Frequency Trace

Fetches the frequency trace of the selected pulse.

[IMAGE alt='RFmxPulse Fetch Frequency Trace' src='rfmxpulse_fetch_frequency_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Frequency (Hz) returns the trace of frequency, in Hz. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the frequency, in Hz. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the frequency, in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxPulse Fetch Time Sidelobe Trace

Fetches the time sidelobe trace for the selected pulse.

[IMAGE alt='RFmxPulse Fetch Time Sidelobe Trace' src='rfmxpulse_fetch_time_sidelobe_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Time Sidelobe (dBm) returns the trace of correlated magnitude, in dBm. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the correlated magnitude, in dBm. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the correlated magnitude, in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_get_all_named_result_names.html language=enus -->
## TOPIC 00022: RFmxPulse Get All Named Result Names (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_get_all_named_result_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_get_all_named_result_names.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Get All Named Result Names (VI)

Owning Palette:

Advanced

Returns all the named result names of the signal that you specify in the Selector String parameter.

[IMAGE alt='RFmxPulse Get All Named Result Names' src='rfmxpulse_get_all_named_result_names.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Result Names returns an array of result names. |
|  | Default Result Exists? indicates whether the default result exists. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_initiate.html language=enus -->
## TOPIC 00023: RFmxPulse Initiate (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_initiate.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Initiate (VI)

Owning Palette:

RFmx Pulse VIs

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the [RFmxPulse Wait for Measurement Complete](rfmxpulse_wait_for_measurement_complete.html) VI or [RFmxPulse Check Measurement Status](rfmxpulse_check_measurement_status.html) VI.

[IMAGE alt='RFmxPulse Initiate' src='rfmxpulse_initiate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter on Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_property_node.html language=enus -->
## TOPIC 00024: RFmxPulse Property Node (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_property_node.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_property_node.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Property Node (VI)

Owning Palette:

RFmx Pulse VIs

Gets (reads), sets (writes), or resets (sets to default value) [RFmxPulse properties](/csh?topicname=rfmxpulseprop/crfmxspecan.html).

[IMAGE alt='RFmxPulse Property Node' src='rfmxpulse_property_node.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_reset_to_default.html language=enus -->
## TOPIC 00025: RFmxPulse Reset to Default (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_reset_to_default.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_reset_to_default.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Reset to Default (VI)

Owning Palette:

Utility

Resets a signal to the default values.

[IMAGE alt='RFmxPulse Reset to Default' src='rfmxpulse_reset_to_default.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_select_measurement.html language=enus -->
## TOPIC 00026: RFmxPulse Select Measurement (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_select_measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_select_measurement.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Select Measurement (VI)

Owning Palette:

RFmx Pulse VIs

Specifies the measurement that you want to enable.

#### RFmxPulse Select Measurement (Single)

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='RFmxPulse Select Measurement (Single)' src='rfmxpulse_select_measurement_(single).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement specifies the measurement to perform. You can specify one of the following measurements. The default value is Pulse. Pulse (0) Enables Pulse measurement. |
| Pulse (0) | Enables Pulse measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_send_software_edge_trigger.html language=enus -->
## TOPIC 00027: RFmxPulse Send Software Edge Trigger (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_send_software_edge_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_send_software_edge_trigger.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Send Software Edge Trigger (VI)

Owning Palette:

Configuration

Sends a trigger to the device when you use the [RFmxPulse Configure Trigger](rfmxpulse_configure_trigger.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxPulse Initiate VI.

[IMAGE alt='RFmxPulse Send Software Edge Trigger' src='rfmxpulse_send_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/rfmxpulse_wait_for_measurement_complete.html language=enus -->
## TOPIC 00028: RFmxPulse Wait for Measurement Complete (VI)

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/rfmxpulse_wait_for_measurement_complete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/rfmxpulse_wait_for_measurement_complete.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

RFmxPulse Wait for Measurement Complete (VI)

Owning Palette:

Utility

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='RFmxPulse Wait for Measurement Complete' src='rfmxpulse_wait_for_measurement_complete.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout (s) specifies the time, in seconds, for which the VI waits for the measurement to complete. A value of -1 specifies that the VI waits until the measurement is complete. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-pulse-vi path=rfmxpulsevi/utility_pal.html language=enus -->
## TOPIC 00029: Utility

- bundle_id: `rfmx-pulse-vi`
- source_path: `rfmxpulsevi/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-vi/raw/resource/enus/rfmxpulsevi/utility_pal.html
- document_id: `rfmx-pulse-vi`
- page_type: `leaf`
- content_type: ``

Utility

Owning Palette:

RFmx Pulse VIs

Use the VIs on this palette to configure RFmx Pulse utilities.

| Palette Object | Description |
| --- | --- |
| RFmxPulse Commit | Commits settings to the hardware. Calling this VI is optional. RFmxPulse commits settings to the hardware when you call the RFmxPulse Initiate VI or any of the measurement Read VIs. |
| RFmxPulse Reset to Default | Resets a signal to the default values. |
| RFmxPulse Wait for Measurement Complete | Waits for the specified number for seconds for all the measurements to complete. |
| RFmxPulse Check Measurement Status | Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
