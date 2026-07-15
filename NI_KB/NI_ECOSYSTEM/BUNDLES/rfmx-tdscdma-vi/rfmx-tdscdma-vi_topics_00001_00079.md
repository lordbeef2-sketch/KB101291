# NI DOCUMENT BUNDLE: rfmx-tdscdma-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-tdscdma-vi start=1 end=79 -->
<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/acp_pal.html language=enus -->
## TOPIC 00001: rfmxtdscdmavi/acp_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/acp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/acp_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

ACP

ACP

Owning Palette:

Configuration

Use the VIs on this palette to configure adjacent channel power (ACP) measurements. You can use the [RFmxTDSCDMA Property Node](rfmxtdscdma_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA ACP Configure Averaging | Configures averaging for the ACP measurement. |
| RFmxTDSCDMA ACP Configure Sweep Time | Configures the sweep time. |
| RFmxTDSCDMA ACP Configure Number of Offsets | Configures the number of offsets for the ACP measurement. |
| RFmxTDSCDMA ACP Configure Measurement Method | Configures the method for performing the ACP measurement. |
| RFmxTDSCDMA ACP Configure Noise Compensation Enabled | Configures channel power compensation for the inherent noise floor of the signal analyzer. |
| RFmxTDSCDMA ACP Configure RBW Filter | Configures the RBW filter. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/advanced_pal.html language=enus -->
## TOPIC 00002: rfmxtdscdmavi/advanced_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/advanced_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/advanced_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

Advanced

Advanced

Owning Palette:

RFmx TDSCDMA VIs

Use the VIs on this palette to use advanced features.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA Abort Measurements | Stops the acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. The acquisition and measurements were previously initiated by the RFmxTDSCDMA Initiate VI or measurement read VIs. |
| RFmxTDSCDMA Analyze2 | Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the Spectrum instance. |
| RFmxTDSCDMA Create Signal Configuration | Creates a new instance of a signal. |
| RFmxTDSCDMA Clone Signal Configuration | Creates a new instance of a signal by copying all the property values from an existing signal instance. |
| RFmxTDSCDMA Delete Signal Configuration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxTDSCDMA Clear Named Result | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxTDSCDMA Clear All Named Results | Clears all results for the signal that you specify in the Selector String parameter. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/build_string_pal.html language=enus -->
## TOPIC 00003: rfmxtdscdmavi/build_string_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/build_string_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/build_string_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

Build String

Build String

Owning Palette:

RFmx TDSCDMA VIs

Use the VIs on this palette to create selector strings for configurations and results that require a selector string.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA Build Signal String | Creates a selector string to use with configuration or fetch properties and VIs. |
| RFmxTDSCDMA Build Channel String | Creates a selector string to use with channel-specific configuration or fetch properties and VIs. |
| RFmxTDSCDMA Build Offset String | Creates the offset string to use as the selector string with spectral emissions mask (SEM) and adjacent channel power (ACP) offset configuration or fetch properties and VIs. |
| RFmxTDSCDMA Build Segment String | Creates the segment string to use as the selector string with the power versus time (PVT) segment configuration or fetch properties and VIs. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/cda_pal.html language=enus -->
## TOPIC 00004: rfmxtdscdmavi/cda_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/cda_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/cda_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

CDA

CDA

Owning Palette:

Configuration

Use the VIs on this palette to configure code domain analysis (CDA) measurements. You can use the [RFmxTDSCDMA Property Node](rfmxtdscdma_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA CDA Configure Averaging | Configures averaging for the CDA measurement. |
| RFmxTDSCDMA CDA Configure Power Unit | Configures the unit of measurement for the measurement results. |
| RFmxTDSCDMA CDA Configure Synchronization Mode and Offset | Configures the synchronization mode and the measurement offset for the code domain analysis (CDA) measurement. You can select a specific time slot for the measurement using this VI. |
| RFmxTDSCDMA CDA Configure Measurement Channel | Configures the physical channel to be analyzed using the Spreading Factor parameter and the Channelization Code parameter. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/chp_pal.html language=enus -->
## TOPIC 00005: rfmxtdscdmavi/chp_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/chp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/chp_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

CHP

CHP

Owning Palette:

Configuration

Use the VIs on this palette to configure channel power (CHP) measurements. You can use the [RFmxTDSCDMA Property Node](rfmxtdscdma_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA CHP Configure Averaging | Configures averaging for the CHP measurement. |
| RFmxTDSCDMA CHP Configure Sweep Time | Configures the sweep time. |
| RFmxTDSCDMA CHP Configure RBW Filter | Configures the RBW filter. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/configuration_pal.html language=enus -->
## TOPIC 00006: rfmxtdscdmavi/configuration_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/configuration_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

Configuration

Configuration

Owning Palette:

RFmx TDSCDMA VIs

Use the VIs on this palette to configure RFmx TD-SCDMA measurements. You can use the [RFmxTDSCDMA Property Node](rfmxtdscdma_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA Configure RF | Configures the RF properties of the signal specified by the Selector String parameter. |
| RFmxTDSCDMA Configure Frequency | Configures the center frequency of the RF signal to acquire according to the Center Frequency value in Hz or according to the Channel Number. The signal analyzer tunes to this frequency. |
| RFmxTDSCDMA Configure Reference Level | Configures the reference level. The reference level represents the maximum expected power of an input RF signal. |
| RFmxTDSCDMA Auto Level | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to calculate an approximate setting for the reference level. |
| RFmxTDSCDMA Configure External Attenuation | Specifies external attenuation to be considered by RFmx TD-SCDMA measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector. |
| RFmxTDSCDMA Configure Trigger | Configures the Reference Trigger that the signal analyzer uses to acquire the signal. |
| RFmxTDSCDMA Send Software Edge Trigger | Sends a trigger to the device when you use the RFmxTDSCDMA Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. |
| RFmxTDSCDMA Configure Channel Configuration Mode | Configures RFmx TD-SCDMA to detect the channels automatically or to use a specified channel configuration. |
| RFmxTDSCDMA Configure Number of Channels | Configures the number of channels for the user-defined channel configuration when the channel configuration mode is set to User Defined. |
| RFmxTDSCDMA Configure User Defined Channel | Configures an individual user-defined channel when the channel configuration mode is set to User Defined. Use "channel<n>" as the selector string to configure this VI. |
| RFmxTDSCDMA Configure User Defined Channel (Array) | Configures all user-defined channels when the channel configuration mode is set to User Defined. |
| RFmxTDSCDMA Configure Uplink Scrambling Code | Configures the scrambling code used for the uplink transmission. |
| RFmxTDSCDMA Configure Midamble Shift | Configures the Midamble Auto Detection Mode, Maximum Number of Users, and Midamble Shift parameters. |
| RFmxTDSCDMA Build Signal String | Creates a selector string to use with configuration or fetch properties and VIs. |
| RFmxTDSCDMA Build Channel String | Creates a selector string to use with channel-specific configuration or fetch properties and VIs. |

| Subpalette | Description |
| --- | --- |
| ModAcc | Use the VIs on this palette to configure ModAcc measurements. You can use the RFmxTDSCDMA Property Node to configure additional properties. |
| ACP | Use the VIs on this palette to configure adjacent channel power (ACP) measurements. You can use the RFmxTDSCDMA Property Node to configure additional properties. |
| CHP | Use the VIs on this palette to configure channel power (CHP) measurements. You can use the RFmxTDSCDMA Property Node to configure additional properties. |
| OBW | Use the VIs on this palette to configure occupied bandwidth (OBW) measurements. You can use the RFmxTDSCDMA Property Node to configure additional properties. |
| SEM | Use the VIs on this palette to configure spectral emission mask (SEM) measurements. You can use the RFmxTDSCDMA Property Node to configure additional properties. |
| CDA | Use the VIs on this palette to configure code domain analysis (CDA) measurements. You can use the RFmxTDSCDMA Property Node to configure additional properties. |
| PVT | Use the VIs on this palette to configure power versus time (PVT) measurements. You can use the RFmxTDSCDMA Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/fetch_pal.html language=enus -->
## TOPIC 00007: rfmxtdscdmavi/fetch_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/fetch_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/fetch_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

Fetch

Fetch

Owning Palette:

RFmx TDSCDMA VIs

Use the VIs on this palette to fetch measurement results and traces.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA ModAcc Fetch | Fetches the ModAcc measurement results. |
| RFmxTDSCDMA ACP Fetch | Fetches the ACP measurement results. |
| RFmxTDSCDMA CHP Fetch | Fetches the CHP measurement results. |
| RFmxTDSCDMA OBW Fetch | Fetches the OBW measurement results. |
| RFmxTDSCDMA SEM Fetch | Fetches the SEM measurement results. |
| RFmxTDSCDMA CDA Fetch | Fetches the code domain analysis (CDA) measurement results. |
| RFmxTDSCDMA PVT Fetch | Fetches the power versus time (PVT) measurement results. |
| RFmxTDSCDMA SlotPower Fetch | Fetches the SlotPower measurement results. |

| Subpalette | Description |
| --- | --- |
| Build String | Use the VIs on this palette to create selector strings for configurations and results that require a selector string. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/modacc_pal.html language=enus -->
## TOPIC 00008: rfmxtdscdmavi/modacc_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/modacc_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/modacc_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

ModAcc

ModAcc

Owning Palette:

Configuration

Use the VIs on this palette to configure ModAcc measurements. You can use the [RFmxTDSCDMA Property Node](rfmxtdscdma_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA ModAcc Configure Averaging | Configures averaging for the ModAcc measurement. |
| RFmxTDSCDMA ModAcc Configure Synchronization Mode and Interval | Configures the synchronization mode, measurement offset, and measurement length for ModAcc analysis. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/obw_pal.html language=enus -->
## TOPIC 00009: rfmxtdscdmavi/obw_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/obw_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/obw_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

OBW

OBW

Owning Palette:

Configuration

Use the VIs on this palette to configure occupied bandwidth (OBW) measurements. You can use the [RFmxTDSCDMA Property Node](rfmxtdscdma_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA OBW Configure Averaging | Configures averaging for the OBW measurement. |
| RFmxTDSCDMA OBW Configure Sweep Time | Configures the sweep time. |
| RFmxTDSCDMA OBW Configure RBW Filter | Configures the RBW filter. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/pvt_pal.html language=enus -->
## TOPIC 00010: rfmxtdscdmavi/pvt_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/pvt_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/pvt_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

PVT

PVT

Owning Palette:

Configuration

Use the VIs on this palette to configure power versus time (PVT) measurements. You can use the [RFmxTDSCDMA Property Node](rfmxtdscdma_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA PVT Configure Averaging | Configures averaging for the power versus time (PVT) measurement. |
| RFmxTDSCDMA PVT Configure Measurement Method | Configures the measurement method for the power versus time (PVT) measurement. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_abort_measurements.html language=enus -->
## TOPIC 00011: rfmxtdscdmavi/rfmxtdscdma_abort_measurements.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_abort_measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_abort_measurements.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Abort Measurements (VI)

RFmxTDSCDMA Abort Measurements (VI)

Owning Palette:

Advanced

Stops the acquisition and measurements associated with the signal instance that you specify in the **Selector String** parameter. The acquisition and measurements were previously initiated by the [RFmxTDSCDMA Initiate](rfmxtdscdma_initiate.html) VI or measurement read VIs.

Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='RFmxTDSCDMA Abort Measurements' src='rfmxtdscdma_abort_measurements.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_acp_configure_averaging.html language=enus -->
## TOPIC 00012: rfmxtdscdmavi/rfmxtdscdma_acp_configure_averaging.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_acp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_acp_configure_averaging.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA ACP Configure Averaging (VI)

RFmxTDSCDMA ACP Configure Averaging (VI)

Owning Palette:

ACP

Configures averaging for the ACP measurement.

[IMAGE alt='RFmxTDSCDMA ACP Configure Averaging' src='rfmxtdscdma_acp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled enables averaging for spectrum measurements. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The ACP measurement uses the value of the ACP Averaging Count property as the number of acquisitions over which the ACP measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The ACP measurement uses the value of the ACP Averaging Count property as the number of acquisitions over which the ACP measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. Refer to the Averaging section of the Spectrum topic for more information about averaging types. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_acp_configure_measurement_method.html language=enus -->
## TOPIC 00013: rfmxtdscdmavi/rfmxtdscdma_acp_configure_measurement_method.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_acp_configure_measurement_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_acp_configure_measurement_method.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA ACP Configure Measurement Method (VI)

RFmxTDSCDMA ACP Configure Measurement Method (VI)

Owning Palette:

ACP

Configures the method for performing the ACP measurement.

[IMAGE alt='RFmxTDSCDMA ACP Configure Measurement Method' src='rfmxtdscdma_acp_configure_measurement_method.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Method specifies the method for performing the ACP measurement. The default value is Normal. Normal (0) The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. Dynamic Range (1) The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. Sequential FFT (2) The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of these chunks is defined by the ACP Sequential FFT Size property, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. Accuracy of the results may be reduced when using this measurement method. For accurate power measurements, when the power characteristics of the signal vary over time, Averaging is allowed. The following properties have limited support when you set the ACP Meas Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads 1 Note For multi-span FFT, the averaging count should be 1. |
| Normal (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| Dynamic Range (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. |
| Sequential FFT (2) | The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of these chunks is defined by the ACP Sequential FFT Size property, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. Accuracy of the results may be reduced when using this measurement method. For accurate power measurements, when the power characteristics of the signal vary over time, Averaging is allowed. The following properties have limited support when you set the ACP Meas Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads 1 |
| Property | Supported Value |
| ACP RBW Auto | True |
| ACP RBW Filter Type | FFT Based |
| ACP Averaging Count | >=1 |
| ACP Noise Comp Enabled | False |
| ACP Num Analysis Threads | 1 |
|  | Note For multi-span FFT, the averaging count should be 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_acp_configure_noise_compensation_enabled.html language=enus -->
## TOPIC 00014: rfmxtdscdmavi/rfmxtdscdma_acp_configure_noise_compensation_enabled.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_acp_configure_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_acp_configure_noise_compensation_enabled.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA ACP Configure Noise Compensation Enabled (VI)

RFmxTDSCDMA ACP Configure Noise Compensation Enabled (VI)

Owning Palette:

ACP

Configures channel power compensation for the inherent noise floor of the signal analyzer.

[IMAGE alt='RFmxTDSCDMA ACP Configure Noise Compensation Enabled' src='rfmxtdscdma_acp_configure_noise_compensation_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Noise Compensation Enabled enables the channel powers to compensate for the inherent noise floor of the signal analyzer. The default value is False. False (0) Disables compensation of the channel powers for the signal analyzer noise floor. True (1) Enables compensation of the channel powers for the signal analyzer noise floor. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R/5830/5831/5832/5842 |
| False (0) | Disables compensation of the channel powers for the signal analyzer noise floor. |
| True (1) | Enables compensation of the channel powers for the signal analyzer noise floor. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R/5830/5831/5832/5842 |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_acp_configure_number_of_offsets.html language=enus -->
## TOPIC 00015: rfmxtdscdmavi/rfmxtdscdma_acp_configure_number_of_offsets.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_acp_configure_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_acp_configure_number_of_offsets.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA ACP Configure Number of Offsets (VI)

RFmxTDSCDMA ACP Configure Number of Offsets (VI)

Owning Palette:

ACP

Configures the number of offsets for the ACP measurement.

[IMAGE alt='RFmxTDSCDMA ACP Configure Number of Offsets' src='rfmxtdscdma_acp_configure_number_of_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Offsets specifies the number of offset channels. The default value is 2. Valid values are constrained by the bandwidth of the signal analyzer. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_acp_configure_rbw_filter.html language=enus -->
## TOPIC 00016: rfmxtdscdmavi/rfmxtdscdma_acp_configure_rbw_filter.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_acp_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_acp_configure_rbw_filter.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA ACP Configure RBW Filter (VI)

RFmxTDSCDMA ACP Configure RBW Filter (VI)

Owning Palette:

ACP

Configures the RBW filter.

[IMAGE alt='RFmxTDSCDMA ACP Configure RBW Filter' src='rfmxtdscdma_acp_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. The default value is True. False (0) The measurement uses the RBW that you specify in the ACP RBW property. True (1) The measurement calculates the RBW. Refer to the RBW and Sweep Time section in the ACP topic for more information about RBW and sweep time. |
| False (0) | The measurement uses the RBW that you specify in the ACP RBW property. |
| True (1) | The measurement calculates the RBW. |
|  | RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 5.636 kHz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is FFT Based. FFT Based (0) An RBW filter with a fast Fourier transform (FFT)-based response is applied. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_acp_configure_sweep_time.html language=enus -->
## TOPIC 00017: rfmxtdscdmavi/rfmxtdscdma_acp_configure_sweep_time.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_acp_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_acp_configure_sweep_time.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA ACP Configure Sweep Time (VI)

RFmxTDSCDMA ACP Configure Sweep Time (VI)

Owning Palette:

ACP

Configures the sweep time.

[IMAGE alt='RFmxTDSCDMA ACP Configure Sweep Time' src='rfmxtdscdma_acp_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of .00066 seconds (s). Refer to the RBW and Sweep Time section in the ACP topic for more details on RBW and sweep time. |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of .00066 seconds (s). |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 0.00066 s. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_acp_fetch.html language=enus -->
## TOPIC 00018: rfmxtdscdmavi/rfmxtdscdma_acp_fetch.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_acp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_acp_fetch.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA ACP Fetch (VI)

RFmxTDSCDMA ACP Fetch (VI)

Owning Palette:

Fetch

Fetches the ACP measurement results.

#### RFmxTDSCDMA ACP Fetch Carrier Absolute Power

Returns the absolute carrier power.

[IMAGE alt='RFmxTDSCDMA ACP Fetch Carrier Absolute Power' src='rfmxtdscdma_acp_fetch_carrier_absolute_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Carrier Absolute Power returns the absolute measured carrier power. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ACP Fetch Offset Measurement

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier.

Use "offset<n>" as the selector string to read results from this VI.

[IMAGE alt='RFmxTDSCDMA ACP Fetch Offset Measurement' src='rfmxtdscdma_acp_fetch_offset_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxTDSCDMA Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Lower Relative Power returns the lower offset channel power measured relative to the integrated power of the carrier. This value is expressed in dB. |
|  | Upper Relative Power returns the upper offset channel power measured relative to the integrated power of the carrier. This value is expressed in dB. |
|  | Lower Absolute Power returns the lower offset channel absolute power. This value is expressed in dBm. |
|  | Upper Absolute Power returns the upper offset channel absolute power. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ACP Fetch Offset Measurement (Array)

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier.

[IMAGE alt='RFmxTDSCDMA ACP Fetch Offset Measurement (Array)' src='rfmxtdscdma_acp_fetch_offset_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Lower Relative Power returns the array of lower offset channel powers measured relative to the integrated power of the carrier. This value is expressed in dB. |
|  | Upper Relative Power returns the array of upper offset channel powers measured relative to the integrated power of the carrier. This value is expressed in dB. |
|  | Lower Absolute Power returns the array of lower offset channel powers. This value is expressed in dBm. |
|  | Upper Absolute Power returns the array of upper offset channel powers. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ACP Fetch Spectrum

Fetches the spectrum used for the ACP measurement.

[IMAGE alt='RFmxTDSCDMA ACP Fetch Spectrum' src='rfmxtdscdma_acp_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ACP Fetch Relative Powers Trace

Fetches the relative powers trace for the ACP measurement.

[IMAGE alt='RFmxTDSCDMA ACP Fetch Relative Powers Trace' src='rfmxtdscdma_acp_fetch_relative_powers_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Relative Powers returns the trace of power levels representing the absolute mask in the spectral domain. x0 returns the start frequency of the trace. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the relative power measured in each channel relative to power reference carrier. This value is expressed in dB. |
|  | x0 returns the start frequency of the trace. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the relative power measured in each channel relative to power reference carrier. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ACP Fetch Absolute Powers Trace

Fetches the absolute powers trace for ACP measurement.

[IMAGE alt='RFmxTDSCDMA ACP Fetch Absolute Powers Trace' src='rfmxtdscdma_acp_fetch_absolute_powers_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Powers returns the trace of measured integrated power. This value is expressed in dBm. x0 returns the start frequency of the trace. This value is expressed in Hz. dx returns the frequency bin spacing of the trace. This value is expressed in Hz. y returns the absolute power trace measured in each channel. This value is expressed in dB. |
|  | x0 returns the start frequency of the trace. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing of the trace. This value is expressed in Hz. |
|  | y returns the absolute power trace measured in each channel. This value is expressed in dB. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_analyze2.html language=enus -->
## TOPIC 00019: rfmxtdscdmavi/rfmxtdscdma_analyze2.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_analyze2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_analyze2.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Analyze2 (VI)

RFmxTDSCDMA Analyze2 (VI)

Owning Palette:

Advanced

Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the Spectrum instance.

#### RFmxTDSCDMA Analyze (IQ, 1 Wfm)

Performs the enabled measurements on the I/Q complex waveform that you specify in the **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.

Use this VI only if the Recommended Acquisition Type property value is either **IQ** or **IQ or Spectral**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmxTDSCDMA Commit VI. |
| --- | --- |

[IMAGE alt='RFmxTDSCDMA Analyze (IQ 1 Wfm)' src='rfmxtdscdma_analyze_(iq_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with the option string as "AnalysisOnly=1". |
| --- | --- |
|  | IQ specifies the data for a complex I/Q waveform including the start, delta, and actual values. x0 specifies the start time of the input y array. This value is expressed in seconds. dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input y array. This value is expressed in seconds. |
|  | dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name input. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by the Result Name input or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String input for Fetch VIs when using named signal configurations or named results. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA Analyze (Spectrum, 1 Wfm)

Performs the enabled measurements on the Spectrum waveform that you specify in the **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.

Use this VI only if the Recommended Acquisition Type property value is either **Spectral** or **IQ or Spectral**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmxTDSCDMA Commit VI. |
| --- | --- |

[IMAGE alt='RFmxTDSCDMA Analyze (Spectrum 1 Wfm)' src='rfmxtdscdma_analyze_(spectrum_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with the option string as "AnalysisOnly=1". |
| --- | --- |
|  | Spectrum specifies the data for a Spectrum waveform including the start, delta, and actual values. x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx specifies the frequency interval between data points in the spectrum. y specifies the real-value power spectrum. |
|  | x0 specifies the start frequency of the spectrum. This value is expressed in Hz. |
|  | dx specifies the frequency interval between data points in the spectrum. |
|  | y specifies the real-value power spectrum. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name input. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by the Result Name input or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String input for Fetch VIs when using named signal configurations or named results. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_auto_level.html language=enus -->
## TOPIC 00020: rfmxtdscdmavi/rfmxtdscdma_auto_level.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_auto_level.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Auto Level (VI)

RFmxTDSCDMA Auto Level (VI)

Owning Palette:

Configuration

Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to calculate an approximate setting for the reference level.

The RFmxTDSCDMA Auto Level VI completes the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the Auto Level Initial Ref Level property.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxTDSCDMA Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='RFmxTDSCDMA Auto Level' src='rfmxtdscdma_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Interval specifies the acquisition length. This value is expressed in seconds. Use this value to calculate the number of samples to acquire from the signal analyzer. The default value is 5 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Reference Level returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_build_channel_string.html language=enus -->
## TOPIC 00021: rfmxtdscdmavi/rfmxtdscdma_build_channel_string.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_build_channel_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_build_channel_string.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Build Channel String (VI)

RFmxTDSCDMA Build Channel String (VI)

Owning Palette:

Configuration

Creates a selector string to use with channel-specific configuration or fetch properties and VIs.

Refer to the Selector String topic for information about the string syntax for named signals.

[IMAGE alt='RFmxTDSCDMA Build Channel String' src='rfmxtdscdma_build_channel_string.gif']

|  | Channel Number specifies the channel number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string you can use in the Selector String input for configuration VIs, fetch VIs, or the RFmxTDSCDMA Initiate VI. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_build_offset_string.html language=enus -->
## TOPIC 00022: rfmxtdscdmavi/rfmxtdscdma_build_offset_string.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_build_offset_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_build_offset_string.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Build Offset String (VI)

RFmxTDSCDMA Build Offset String (VI)

Owning Palette:

Build String

Creates the offset string to use as the selector string with spectral emissions mask (SEM) and adjacent channel power (ACP) offset configuration or fetch properties and VIs.

Refer to the Selector String topic for information about the string syntax for named signals.

[IMAGE alt='RFmxTDSCDMA Build Offset String' src='rfmxtdscdma_build_offset_string.gif']

|  | Offset Number specifies the offset number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string you can use in the Selector String input for configuration VIs, fetch VIs, or the RFmxTDSCDMA Initiate VI. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_build_segment_string.html language=enus -->
## TOPIC 00023: rfmxtdscdmavi/rfmxtdscdma_build_segment_string.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_build_segment_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_build_segment_string.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Build Segment String (VI)

RFmxTDSCDMA Build Segment String (VI)

Owning Palette:

Build String

Creates the segment string to use as the selector string with the power versus time (PVT) segment configuration or fetch properties and VIs.

Refer to the Selector String topic for information about the string syntax for named signals.

[IMAGE alt='RFmxTDSCDMA Build Segment String' src='rfmxtdscdma_build_segment_string.gif']

|  | Segment Number specifies the segment number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string you can use in the Selector String input for configuration VIs, fetch VIs, or the RFmxTDSCDMA Initiate VI. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_build_signal_string.html language=enus -->
## TOPIC 00024: rfmxtdscdmavi/rfmxtdscdma_build_signal_string.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_build_signal_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_build_signal_string.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Build Signal String (VI)

RFmxTDSCDMA Build Signal String (VI)

Owning Palette:

Configuration

Creates a selector string to use with configuration or fetch properties and VIs.

Refer to the Selector String topic for information about the string syntax for named signals.

[IMAGE alt='RFmxTDSCDMA Build Signal String' src='rfmxtdscdma_build_signal_string.gif']

|  | Result Name specifies the name of the result when performing overlapped measurements. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string). Examples: "" "result::r1" "r1" |
| --- | --- |
|  | Signal Name specifies the name of the signal when using named signal configurations. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Examples: "" "signal::sig1" "sig1" |
|  | Selector String returns the selector string you can use in the Selector String input for configuration VIs, fetch VIs, or other VIs that build selector strings. This string contains the signal and/or result names with their appropriate prefixes. Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_cda_configure_averaging.html language=enus -->
## TOPIC 00025: rfmxtdscdmavi/rfmxtdscdma_cda_configure_averaging.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_cda_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_cda_configure_averaging.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA CDA Configure Averaging (VI)

RFmxTDSCDMA CDA Configure Averaging (VI)

Owning Palette:

CDA

Configures averaging for the CDA measurement.

[IMAGE alt='RFmxTDSCDMA CDA Configure Averaging' src='rfmxtdscdma_cda_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the CDA measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The CDA measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the CDA measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The CDA measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the CDA measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_cda_configure_measurement_channel.html language=enus -->
## TOPIC 00026: rfmxtdscdmavi/rfmxtdscdma_cda_configure_measurement_channel.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_cda_configure_measurement_channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_cda_configure_measurement_channel.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA CDA Configure Measurement Channel (VI)

RFmxTDSCDMA CDA Configure Measurement Channel (VI)

Owning Palette:

CDA

Configures the physical channel to be analyzed using the **Spreading Factor** parameter and the **Channelization Code** parameter.

[IMAGE alt='RFmxTDSCDMA CDA Configure Measurement Channel' src='rfmxtdscdma_cda_configure_measurement_channel.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Spreading Factor specifies the base spreading factor for code domain power (CDP) analysis. The default value is 16. |
|  | Channelization Code specifies the channelization code of the code domain analysis (CDA) measurement channel. The default value is 1. The valid values are 1 to 16. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_cda_configure_power_unit.html language=enus -->
## TOPIC 00027: rfmxtdscdmavi/rfmxtdscdma_cda_configure_power_unit.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_cda_configure_power_unit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_cda_configure_power_unit.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA CDA Configure Power Unit (VI)

RFmxTDSCDMA CDA Configure Power Unit (VI)

Owning Palette:

CDA

Configures the unit of measurement for the measurement results.

[IMAGE alt='RFmxTDSCDMA CDA Configure Power Unit' src='rfmxtdscdma_cda_configure_power_unit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Power Unit specifies the measurement unit of the measured code domain power results. The default value is dB. dB (0) The measurement unit for code domain power results is dB. dBm (1) The measurement unit for code domain power results is dBm. |
| dB (0) | The measurement unit for code domain power results is dB. |
| dBm (1) | The measurement unit for code domain power results is dBm. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_cda_configure_synchronization_mode_and_offset.html language=enus -->
## TOPIC 00028: rfmxtdscdmavi/rfmxtdscdma_cda_configure_synchronization_mode_and_offset.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_cda_configure_synchronization_mode_and_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_cda_configure_synchronization_mode_and_offset.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA CDA Configure Synchronization Mode and Offset (VI)

RFmxTDSCDMA CDA Configure Synchronization Mode and Offset (VI)

Owning Palette:

CDA

Configures the synchronization mode and the measurement offset for the code domain analysis (CDA) measurement. You can select a specific time slot for the measurement using this VI.

[IMAGE alt='RFmxTDSCDMA CDA Configure Synchronization Mode and Offset' src='rfmxtdscdma_cda_configure_synchronization_mode_and_offset.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Mode specifies the synchronization mode for the CDA measurement. Currently, only the Slot mode is supported. Slot (0) The measurement uses slot synchronization mode. The slot boundary in the acquired signal is detected, and the measurement is performed over one slot, starting from the boundary specified by the CDA Meas Offset property. |
| Slot (0) | The measurement uses slot synchronization mode. The slot boundary in the acquired signal is detected, and the measurement is performed over one slot, starting from the boundary specified by the CDA Meas Offset property. |
|  | Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_cda_fetch.html language=enus -->
## TOPIC 00029: rfmxtdscdmavi/rfmxtdscdma_cda_fetch.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_cda_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_cda_fetch.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA CDA Fetch (VI)

RFmxTDSCDMA CDA Fetch (VI)

Owning Palette:

Fetch

Fetches the code domain analysis (CDA) measurement results.

#### RFmxTDSCDMA CDA Fetch IQ Impairments

Returns the I/Q origin offset, I/Q gain imbalance, and I/Q quadrature error.

[IMAGE alt='RFmxTDSCDMA CDA Fetch IQ Impairments' src='rfmxtdscdma_cda_fetch_iq_impairments.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | IQ Origin Offset returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. |
|  | IQ Gain Imbalance returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. |
|  | IQ Quadrature Error returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA CDA Fetch Code Domain Power

Fetches the scalar code domain measurement results.

[IMAGE alt='RFmxTDSCDMA CDA Fetch Code Domain Power' src='rfmxtdscdma_cda_fetch_code_domain_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Total Power returns the total power measured in the code domain of the base spreading factor, averaged over all averaging iterations. This value is expressed in dBm. |
|  | Mean Total Active Power returns the total active code power measured in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the CDA Pwr Unit property to dB, or in dBm, if you set the CDA Pwr Unit property to dBm. |
|  | Mean Active Power returns the average of the active code power measured in the code domain of the base spreading factor, normalized to the total CDP. This value is expressed in dB, if you set the CDA Pwr Unit property to dB, or in dBm, if you set the CDA Pwr Unit property to dBm. |
|  | Mean Inactive Power returns the average of the code power measured among the set of inactive channels in the code domain of the base spreading factor, normalized to the total CDP. This value is expressed in dB, if you set the CDA Pwr Unit property to dB, or in dBm, if you set the CDA Pwr Unit property to dBm. |
|  | Maximum Peak Active Power returns the maximum value among all averaging iterations of the maximum active code power measured in the code domain of the base spreading factor, normalized to the total CDP. This value is expressed in dB, if you set the CDA Pwr Unit property to dB, or in dBm, if you set the CDA Pwr Unit property to dBm. |
|  | Maximum Peak Inactive Power returns the maximum value among all averaging iterations of the highest measured code power among the set of inactive channels in the code domain of the base spreading factor, normalized to the total CDP. This value is expressed in dB, if you set the CDA Pwr Unit property to dB, or in dBm, if you set the CDA Pwr Unit property to dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA CDA Fetch Symbol EVM

Fetches the ModAcc related measurements for the configured measurement channel.

[IMAGE alt='RFmxTDSCDMA CDA Fetch Symbol EVM' src='rfmxtdscdma_cda_fetch_symbol_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean RMS Symbol EVM returns the RMS symbol EVM for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage. |
|  | Maximum Peak Symbol EVM returns the maximum value of the peak symbol EVMs, among all averaging iterations for the selected time slot and channel. This value is expressed as a percentage. |
|  | Frequency Error returns the frequency error averaged over all measured slots. This value is expressed in Hz. |
|  | Mean RMS Symbol Magnitude Error returns the RMS symbol magnitude error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage. |
|  | Chip Rate Error returns the chip rate error. This value is expressed in ppm. |
|  | Mean RMS Symbol Phase Error returns the RMS symbol phase error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed in degrees. |
|  | Mean Symbol Power returns the mean symbol power for the selected time slot and channel. This value is expressed in dB if you set the CDA Pwr Unit property to dB, and in dBm if you set the CDA Pwr Unit property to dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA CDA Fetch Mean Symbol EVM Trace

Fetches the averaged symbol EVM trace of the code domain analysis (CDA) measurement channel.

[IMAGE alt='RFmxTDSCDMA CDA Fetch Mean Symbol EVM Trace' src='rfmxtdscdma_cda_fetch_mean_symbol_evm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Symbol EVM returns an array of the averaged symbol EVM traces for the configured measurement channel. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA CDA Fetch Maximum Symbol EVM Trace

Fetches the maximum hold trace of the symbol EVM for the code domain analysis (CDA) measurement.

[IMAGE alt='RFmxTDSCDMA CDA Fetch Maximum Symbol EVM Trace' src='rfmxtdscdma_cda_fetch_maximum_symbol_evm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Symbol EVM returns an array of the maximum hold traces of the symbol EVM for the CDA measurement. This value is expressed as a percentage. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA CDA Fetch Mean Symbol Magnitude Error Trace

Fetches the averaged symbol magnitude error trace for the code domain analysis (CDA) measurement.

[IMAGE alt='RFmxTDSCDMA CDA Fetch Mean Symbol Magnitude Error Trace' src='rfmxtdscdma_cda_fetch_mean_symbol_magnitude_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Symbol Magnitude Error returns an array of the averaged symbol magnitude error traces for the configured measurement channel. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA CDA Fetch Maximum Symbol Magnitude Error Trace

Returns the maximum hold trace of the symbol magnitude error for the code domain analysis (CDA) measurement.

[IMAGE alt='RFmxTDSCDMA CDA Fetch Maximum Symbol Magnitude Error Trace' src='rfmxtdscdma_cda_fetch_maximum_symbol_magnitude_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Symbol Magnitude Error returns an array of the maximum hold traces of the symbol magnitude error for the CDA measurement. This value is expressed as a percentage. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA CDA Fetch Mean Symbol Phase Error Trace

Fetches the averaged symbol phase error trace for the code domain analysis (CDA) measurement.

[IMAGE alt='RFmxTDSCDMA CDA Fetch Mean Symbol Phase Error Trace' src='rfmxtdscdma_cda_fetch_mean_symbol_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Symbol Phase Error returns an array of the averaged symbol phase error traces for the configured measurement channel. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA CDA Fetch Maximum Symbol Phase Error Trace

Fetches the maximum hold trace of the symbol phase error for the code domain analysis (CDA) measurement.

[IMAGE alt='RFmxTDSCDMA CDA Fetch Maximum Symbol Phase Error Trace' src='rfmxtdscdma_cda_fetch_maximum_symbol_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Symbol Phase Error returns an array of the maximum hold traces of the symbol phase error for the CDA measurement. This value is expressed in degrees. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA CDA Fetch Symbol Constellation Trace

Fetches the symbol constellation trace of the code domain analysis (CDA) measurement channel.

[IMAGE alt='RFmxTDSCDMA CDA Fetch Symbol Constellation Trace' src='rfmxtdscdma_cda_fetch_symbol_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Symbol Constellation returns an array of the symbol constellation traces of the configured measurement channel. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA CDA Fetch Mean Code Domain Power Trace

Fetches the averaged trace value of the code powers measured in the code domain of the base spreading factor.

[IMAGE alt='RFmxTDSCDMA CDA Fetch Mean Code Domain Power Trace' src='rfmxtdscdma_cda_fetch_mean_code_domain_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Code Domain Powers returns an array of the averaged code power traces measured in the code domain of the base spreading factor. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA CDA Fetch Maximum Code Domain Power Trace

Fetches the maximum hold trace of the power measured in the code domain of the base spreading factor.

[IMAGE alt='RFmxTDSCDMA CDA Fetch Maximum Code Domain Power Trace' src='rfmxtdscdma_cda_fetch_maximum_code_domain_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Code Domain Powers returns an array of the max hold traces of the code powers measured in the code domain of the base spreading factor. This value is expressed in dB. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_check_measurement_status.html language=enus -->
## TOPIC 00030: rfmxtdscdmavi/rfmxtdscdma_check_measurement_status.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_check_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_check_measurement_status.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Check Measurement Status (VI)

RFmxTDSCDMA Check Measurement Status (VI)

Owning Palette:

Utility

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='RFmxTDSCDMA Check Measurement Status' src='rfmxtdscdma_check_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | done? indicates whether the measurement is complete. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_chp_configure_averaging.html language=enus -->
## TOPIC 00031: rfmxtdscdmavi/rfmxtdscdma_chp_configure_averaging.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_chp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_chp_configure_averaging.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA CHP Configure Averaging (VI)

RFmxTDSCDMA CHP Configure Averaging (VI)

Owning Palette:

CHP

Configures averaging for the CHP measurement.

[IMAGE alt='RFmxTDSCDMA CHP Configure Averaging' src='rfmxtdscdma_chp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled enables averaging for spectrum measurements. The default value is False. False (0) Disables averaging for the CHP measurement. True (1) The CHP measurement uses the CHP Averaging Count property as the number of acquisitions over which the CHP measurement is averaged. |
| False (0) | Disables averaging for the CHP measurement. |
| True (1) | The CHP measurement uses the CHP Averaging Count property as the number of acquisitions over which the CHP measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. Refer to the Averaging section of the Spectrum topic for more information about averaging types. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_chp_configure_rbw_filter.html language=enus -->
## TOPIC 00032: rfmxtdscdmavi/rfmxtdscdma_chp_configure_rbw_filter.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_chp_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_chp_configure_rbw_filter.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA CHP Configure RBW Filter (VI)

RFmxTDSCDMA CHP Configure RBW Filter (VI)

Owning Palette:

CHP

Configures the RBW filter.

[IMAGE alt='RFmxTDSCDMA CHP Configure RBW Filter' src='rfmxtdscdma_chp_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. The default value is True. False (0) The measurement uses the RBW you specify. True (1) RFmx TD-SCDMA automatically calculates the RBW. Refer to the RBW and Sweep Time section in the CHP topic for more information about RBW and sweep time. |
| False (0) | The measurement uses the RBW you specify. |
| True (1) | RFmx TD-SCDMA automatically calculates the RBW. |
|  | RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 5.636 kHz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is FFT Based. FFT Based (0) An RBW filter with a fast Fourier transform (FFT)-based response is applied. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_chp_configure_sweep_time.html language=enus -->
## TOPIC 00033: rfmxtdscdmavi/rfmxtdscdma_chp_configure_sweep_time.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_chp_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_chp_configure_sweep_time.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA CHP Configure Sweep Time (VI)

RFmxTDSCDMA CHP Configure Sweep Time (VI)

Owning Palette:

CHP

Configures the sweep time.

[IMAGE alt='RFmxTDSCDMA CHP Configure Sweep Time' src='rfmxtdscdma_chp_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of .00066 seconds (s). Refer to the RBW and Sweep Time section in the CHP topic for more details on RBW and sweep time. |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of .00066 seconds (s). |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 0.00066 s. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_chp_fetch.html language=enus -->
## TOPIC 00034: rfmxtdscdmavi/rfmxtdscdma_chp_fetch.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_chp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_chp_fetch.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA CHP Fetch (VI)

RFmxTDSCDMA CHP Fetch (VI)

Owning Palette:

Fetch

Fetches the CHP measurement results.

#### RFmxTDSCDMA CHP Fetch Carrier Absolute Power

Returns the absolute power of the selected carrier.

[IMAGE alt='RFmxTDSCDMA CHP Fetch Carrier Absolute Power' src='rfmxtdscdma_chp_fetch_carrier_absolute_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Carrier Absolute Power returns the absolute power of the carrier. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA CHP Fetch Spectrum

Fetches the spectrum used for the CHP measurement.

[IMAGE alt='RFmxTDSCDMA CHP Fetch Spectrum' src='rfmxtdscdma_chp_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_clear_all_named_results.html language=enus -->
## TOPIC 00035: rfmxtdscdmavi/rfmxtdscdma_clear_all_named_results.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_clear_all_named_results.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_clear_all_named_results.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Clear All Named Results (VI)

RFmxTDSCDMA Clear All Named Results (VI)

Owning Palette:

Advanced

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxTDSCDMA Clear All Named Results' src='rfmxtdscdma_clear_all_named_results.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_clear_named_result.html language=enus -->
## TOPIC 00036: rfmxtdscdmavi/rfmxtdscdma_clear_named_result.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_clear_named_result.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_clear_named_result.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Clear Named Result (VI)

RFmxTDSCDMA Clear Named Result (VI)

Owning Palette:

Advanced

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='RFmxTDSCDMA Clear Named Result' src='rfmxtdscdma_clear_named_result.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_clone_signal_configuration.html language=enus -->
## TOPIC 00037: rfmxtdscdmavi/rfmxtdscdma_clone_signal_configuration.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_clone_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_clone_signal_configuration.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Clone Signal Configuration (VI)

RFmxTDSCDMA Clone Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='RFmxTDSCDMA Clone Signal Configuration' src='rfmxtdscdma_clone_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | New Signal Name specifies the name of the new signal. This input accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
|  | Old Signal Name specifies the name of an existing signal. This input accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string you can use in the Selector String input for configuration VIs, fetch VIs, or the RFmxTDSCDMA Initiate VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_commit.html language=enus -->
## TOPIC 00038: rfmxtdscdmavi/rfmxtdscdma_commit.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_commit.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Commit (VI)

RFmxTDSCDMA Commit (VI)

Owning Palette:

Utility

Commits settings to the hardware. Calling this VI is optional. RFmxTDSCDMA commits settings to the hardware when you call the [RFmxTDSCDMA Initiate](rfmxtdscdma_initiate.html) VI.

[IMAGE alt='RFmxTDSCDMA Commit' src='rfmxtdscdma_commit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_configure_channel_configuration_mode.html language=enus -->
## TOPIC 00039: rfmxtdscdmavi/rfmxtdscdma_configure_channel_configuration_mode.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_configure_channel_configuration_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_configure_channel_configuration_mode.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Configure Channel Configuration Mode (VI)

RFmxTDSCDMA Configure Channel Configuration Mode (VI)

Owning Palette:

Configuration

Configures RFmx TD-SCDMA to detect the channels automatically or to use a specified channel configuration.

[IMAGE alt='RFmxTDSCDMA Configure Channel Configuration Mode' src='rfmxtdscdma_configure_channel_configuration_mode.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Channel Configuration Mode specifies whether to detect the channels automatically or to use a specified channel configuration. The default value is Auto Detect. Auto Detect (0) RFmx TD-SCDMA detects the channels automatically. User Defined (1) The channel configuration is defined manually. This mode increases measurement speed because no time is spent on channel detection. |
| Auto Detect (0) | RFmx TD-SCDMA detects the channels automatically. |
| User Defined (1) | The channel configuration is defined manually. This mode increases measurement speed because no time is spent on channel detection. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_configure_external_attenuation.html language=enus -->
## TOPIC 00040: rfmxtdscdmavi/rfmxtdscdma_configure_external_attenuation.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_configure_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_configure_external_attenuation.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Configure External Attenuation (VI)

RFmxTDSCDMA Configure External Attenuation (VI)

Owning Palette:

Configuration

Specifies external attenuation to be considered by RFmx TD-SCDMA measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector.

[IMAGE alt='RFmxTDSCDMA Configure External Attenuation' src='rfmxtdscdma_configure_external_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | External Attenuation specifies the level of external attenuation that is considered by the selected measurement. This value is expressed in dB. The default value is 0. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_configure_frequency.html language=enus -->
## TOPIC 00041: rfmxtdscdmavi/rfmxtdscdma_configure_frequency.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_configure_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_configure_frequency.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Configure Frequency (VI)

RFmxTDSCDMA Configure Frequency (VI)

Owning Palette:

Configuration

Configures the center frequency of the RF signal to acquire according to the **Center Frequency** value in Hz or according to the **Channel Number**. The signal analyzer tunes to this frequency.

#### RFmxTDSCDMA Configure Frequency (Channel Number)

Configures the carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency.

[IMAGE alt='RFmxTDSCDMA Configure Frequency (Channel Number)' src='rfmxtdscdma_configure_frequency_(channel_number).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Channel Number specifies the number of the channel to be measured. The center frequency is derived from this value. The default value is 5000. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA Configure Frequency (Frequency)

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

[IMAGE alt='RFmxTDSCDMA Configure Frequency (Frequency)' src='rfmxtdscdma_configure_frequency_(frequency).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. The default of this parameter is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_configure_midamble_shift.html language=enus -->
## TOPIC 00042: rfmxtdscdmavi/rfmxtdscdma_configure_midamble_shift.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_configure_midamble_shift.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_configure_midamble_shift.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Configure Midamble Shift (VI)

RFmxTDSCDMA Configure Midamble Shift (VI)

Owning Palette:

Configuration

Configures the **Midamble Auto Detection Mode**, **Maximum Number of Users**, and **Midamble Shift** parameters.

[IMAGE alt='RFmxTDSCDMA Configure Midamble Shift' src='rfmxtdscdma_configure_midamble_shift.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Midamble Auto Detection Mode enables automatic midamble detection. The default value is Midamble Shift. Off (0) Automatic midamble detection is disabled. Midamble Shift (1) The midamble shift is automatically detected from K possible midamble shift values, where K is specified by the Maximum Number of Users parameter. The K possible midamble shift values are: Midamble Shift = k * floor(P/K), where P = 128, is the length of the basic midamble code, and k is an integer from 0 to K-1. |
| Off (0) | Automatic midamble detection is disabled. |
| Midamble Shift (1) | The midamble shift is automatically detected from K possible midamble shift values, where K is specified by the Maximum Number of Users parameter. The K possible midamble shift values are: Midamble Shift = k * floor(P/K), where P = 128, is the length of the basic midamble code, and k is an integer from 0 to K-1. |
|  | Maximum Number of Users configures the maximum number of users. The default value is 16. 2 (2) The maximum number of users are 2. 4 (4) The maximum number of users are 4. 6 (6) The maximum number of users are 6. 8 (8) The maximum number of users are 8. 10 (10) The maximum number of users are 10. 12 (12) The maximum number of users are 12. 14 (14) The maximum number of users are 14. 16 (16) The maximum number of users are 16. |
| 2 (2) | The maximum number of users are 2. |
| 4 (4) | The maximum number of users are 4. |
| 6 (6) | The maximum number of users are 6. |
| 8 (8) | The maximum number of users are 8. |
| 10 (10) | The maximum number of users are 10. |
| 12 (12) | The maximum number of users are 12. |
| 14 (14) | The maximum number of users are 14. |
| 16 (16) | The maximum number of users are 16. |
|  | Midamble Shift specifies the midamble shift used when the Midamble Auto Detection Mode parameter is set to Off. This value is expressed in chips. The default value is 8. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_configure_number_of_channels.html language=enus -->
## TOPIC 00043: rfmxtdscdmavi/rfmxtdscdma_configure_number_of_channels.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_configure_number_of_channels.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_configure_number_of_channels.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Configure Number of Channels (VI)

RFmxTDSCDMA Configure Number of Channels (VI)

Owning Palette:

Configuration

Configures the number of channels for the user-defined channel configuration when the channel configuration mode is set to **User Defined**.

[IMAGE alt='RFmxTDSCDMA Configure Number of Channels' src='rfmxtdscdma_configure_number_of_channels.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Channels specifies the number of user-defined channels. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_configure_pilot.html language=enus -->
## TOPIC 00044: rfmxtdscdmavi/rfmxtdscdma_configure_pilot.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_configure_pilot.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_configure_pilot.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Configure Pilot (VI)

RFmxTDSCDMA Configure Pilot (VI)

Configures the pilot code of the TD-SCDMA signal.

[IMAGE alt='RFmxTDSCDMA Configure Pilot' src='rfmxtdscdma_configure_pilot.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | Pilot Code specifies the SYNC-UL code used by the uplink pilot time slot (UpPTS). This code is used when the ModAcc Sync Mode property is set to Subframe, or the ModAcc Slot Type property is set to Pilot. The default value is 0. The valid range is 0 to 255. The Code Group of the parameter is determined by the following formula: Code Group = floor (Pilot Code / 8) The code group of the parameter should match the code group of the UL Scrambling Code property. For more information on code allocations, refer to the Code Allocation in Section 8.3 of 3GPP TS 25.223, v.11.0.0 Release 11. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_configure_reference_level.html language=enus -->
## TOPIC 00045: rfmxtdscdmavi/rfmxtdscdma_configure_reference_level.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_configure_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_configure_reference_level.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Configure Reference Level (VI)

RFmxTDSCDMA Configure Reference Level (VI)

Owning Palette:

Configuration

Configures the reference level. The reference level represents the maximum expected power of an input RF signal.

[IMAGE alt='RFmxTDSCDMA Configure Reference Level' src='rfmxtdscdma_configure_reference_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Level specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_configure_rf.html language=enus -->
## TOPIC 00046: rfmxtdscdmavi/rfmxtdscdma_configure_rf.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_configure_rf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_configure_rf.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Configure RF (VI)

RFmxTDSCDMA Configure RF (VI)

Owning Palette:

Configuration

Configures the RF properties of the signal specified by the **Selector String** parameter.

[IMAGE alt='RFmxTDSCDMA Configure RF' src='rfmxtdscdma_configure_rf.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. The default of this parameter is hardware dependent. |
|  | Reference Level specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent. |
|  | External Attenuation specifies the level of external attenuation that is considered by the selected measurement. This value is expressed in dB. The default value is 0. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_configure_trigger.html language=enus -->
## TOPIC 00047: rfmxtdscdmavi/rfmxtdscdma_configure_trigger.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_configure_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_configure_trigger.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Configure Trigger (VI)

RFmxTDSCDMA Configure Trigger (VI)

Owning Palette:

Configuration

Configures the Reference Trigger that the signal analyzer uses to acquire the signal.

#### RFmxTDSCDMA Configure IQ Power Edge Trigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

To trigger on burst signals, specify a minimum quiet time. The minimum quiet time ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts but large enough to ignore power changes within a burst.

[IMAGE alt='RFmxTDSCDMA Configure IQ Power Edge Trigger' src='rfmxtdscdma_configure_iq_power_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | IQ Power Edge Source specifies the channel from which the device monitors the trigger. The default of this parameter is hardware dependent. |
|  | IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
|  | IQ Power Edge Level specifies the threshold above or below which the signal analyzer triggers, depending on the value of the IQ Power Edge Slope parameter. The value is expressed in dB if IQ Power Edge Level Type is set to Relative or in dBm if it is set to Absolute. The default of this parameter is hardware dependent. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | Minimum Quiet Time Mode specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Auto. Manual (0) The measurement uses the minimum quiet time value you specify using the Minimum Quiet Time parameter. Auto (1) The measurement calculates the minimum quiet time used for triggering. |
| Manual (0) | The measurement uses the minimum quiet time value you specify using the Minimum Quiet Time parameter. |
| Auto (1) | The measurement calculates the minimum quiet time used for triggering. |
|  | Minimum Quiet Time specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default of this parameter is hardware dependent. |
|  | IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. This parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value is Relative. Relative (0) The IQ Power Edge Level is relative to the reference level. Absolute (1) The IQ Power Edge Level specifies the absolute power. |
| Relative (0) | The IQ Power Edge Level is relative to the reference level. |
| Absolute (1) | The IQ Power Edge Level specifies the absolute power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA Configure Software Edge Trigger

Configures the device to wait for a software trigger to mark a reference point within the record.

[IMAGE alt='RFmxTDSCDMA Configure Software Edge Trigger' src='rfmxtdscdma_configure_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA Configure Digital Edge Trigger

Configures the device to wait for a digital edge trigger to mark a reference point within the record.

[IMAGE alt='RFmxTDSCDMA Configure Digital Edge Trigger' src='rfmxtdscdma_configure_digital_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Digital Edge Source specifies the source terminal for the digital edge trigger. The default of this parameter is hardware dependent. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. PXIe_DStarB (PXIe_DStarB) The trigger is received on the PXIe DStar B trigger line. |
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
| PXIe_DStarB (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. |
|  | Digital Edge specifies the trigger edge to detect. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. |
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA Disable Trigger

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='RFmxTDSCDMA Disable Trigger' src='rfmxtdscdma_disable_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_configure_uplink_scrambling_code.html language=enus -->
## TOPIC 00048: rfmxtdscdmavi/rfmxtdscdma_configure_uplink_scrambling_code.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_configure_uplink_scrambling_code.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_configure_uplink_scrambling_code.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Configure Uplink Scrambling Code (VI)

RFmxTDSCDMA Configure Uplink Scrambling Code (VI)

Owning Palette:

Configuration

Configures the scrambling code used for the uplink transmission.

[IMAGE alt='RFmxTDSCDMA Configure Uplink Scrambling Code' src='rfmxtdscdma_configure_uplink_scrambling_code.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Uplink Scrambling Code specifies the scrambling code and the basic midamble code for uplink transmission. The default value is 0. The valid range is 0 to 127. The code group of the parameter should match the code group of the Pilot Code property. For more information on code allocations, refer to the Code Allocation in Section 8.3 of 3GPP TS 25.223, v.11.0.0 Release 11. Code Group = floor (UL Scrambling Code / 4) |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_configure_user_defined_channel.html language=enus -->
## TOPIC 00049: rfmxtdscdmavi/rfmxtdscdma_configure_user_defined_channel.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_configure_user_defined_channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_configure_user_defined_channel.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Configure User Defined Channel (VI)

RFmxTDSCDMA Configure User Defined Channel (VI)

Owning Palette:

Configuration

Configures an individual user-defined channel when the channel configuration mode is set to **User Defined**.

Use "channel<n>" as the selector string to configure this VI.

A channel configuration is defined by the slot index it refers to, the channel type, and the modulation type.

[IMAGE alt='RFmxTDSCDMA Configure User Defined Channel' src='rfmxtdscdma_configure_user_defined_channel.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Slot Index specifies the index of a slot after the start of the acquisition. The default value is 0. |
|  | Channel Type specifies the TD-SCDMA channel type. The default value is Idle. Idle (0) Specifies that the user-defined channel type is an empty slot. DPCH (1) Specifies that the user-defined channel is DPCH. EDCH (2) Specifies that the user-defined channel is EDCH. HSSICH (3) Specifies that the user-defined channel is HSSICH. |
| Idle (0) | Specifies that the user-defined channel type is an empty slot. |
| DPCH (1) | Specifies that the user-defined channel is DPCH. |
| EDCH (2) | Specifies that the user-defined channel is EDCH. |
| HSSICH (3) | Specifies that the user-defined channel is HSSICH. |
|  | Slot Format specifies the spreading factor, the number of TFCI code words, the number of transmit power control bits, and the number of synchronization shift bits. Refer to the 3GPP TS 25.221 V11.0.0 standard for more information about slot format. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name and channel number. If you do not specify the signal name, the default signal instance is used. The default value is "channel0". Examples: "channel0" "signal::sig1/channel0" You can use the RFmxTDSCDMA Build Channel String VI to build the selector string. |
|  | Modulation Type specifies the modulation type of the corresponding channels. The default value is QPSK. QPSK (0) Specifies the QPSK modulation type is used. 8PSK (1) Specifies the 8-PSK modulation type is used. 16QAM (2) Specifies the 16-QAM modulation type is used. |
| QPSK (0) | Specifies the QPSK modulation type is used. |
| 8PSK (1) | Specifies the 8-PSK modulation type is used. |
| 16QAM (2) | Specifies the 16-QAM modulation type is used. |
|  | Channelization Code specifies the channelization code assigned to the channel. The default value is 1. The valid values are 1 to 16. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_configure_user_defined_channel_(array).html language=enus -->
## TOPIC 00050: rfmxtdscdmavi/rfmxtdscdma_configure_user_defined_channel_(array).html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_configure_user_defined_channel_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_configure_user_defined_channel_(array).html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Configure User Defined Channel (Array) (VI)

RFmxTDSCDMA Configure User Defined Channel (Array) (VI)

Owning Palette:

Configuration

Configures all user-defined channels when the channel configuration mode is set to **User Defined**.

Use equal-sized arrays for **Slot Index**, **Channel Type**, and **Modulation Type**. You can configure up to two channels for the same index for multi-code transmission.

[IMAGE alt='RFmxTDSCDMA Configure User Defined Channel (Array)' src='rfmxtdscdma_configure_user_defined_channel_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Slot Index specifies the slot index used for the current user defined channel configuration. The slot index is numbered according to the start time of the acquisition. For example, slot index 0 is the first slot detected in the acquired signal. Valid Values: 0 to 6 |
|  | Channel Type specifies the TD-SCDMA channel type. The default value is Idle. Idle (0) Specifies that the user-defined channel type is an empty slot. DPCH (1) Specifies that the user-defined channel is a dedicated physical channel (DPCH). EDCH (2) Specifies that the user-defined channel is an enhanced dedicated channel (EDCH). HSSICH (3) Specifies that the user-defined channel is a shared information channel for high-speed downlink. |
| Idle (0) | Specifies that the user-defined channel type is an empty slot. |
| DPCH (1) | Specifies that the user-defined channel is a dedicated physical channel (DPCH). |
| EDCH (2) | Specifies that the user-defined channel is an enhanced dedicated channel (EDCH). |
| HSSICH (3) | Specifies that the user-defined channel is a shared information channel for high-speed downlink. |
|  | Slot Format specifies the spreading factor, the number of TFCI code words, the number of transmit power control bits, and the number of synchronization shift bits. Refer to the 3GPP TS 25.221 V11.0.0 standard for more information about slot format. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | Modulation Type specifies the modulation type of the corresponding channels. The default value is QPSK. QPSK (0) Specifies the QPSK modulation type is used. 8PSK (1) Specifies the 8-PSK modulation type is used. 16QAM (2) Specifies the 16-QAM modulation type is used. |
| QPSK (0) | Specifies the QPSK modulation type is used. |
| 8PSK (1) | Specifies the 8-PSK modulation type is used. |
| 16QAM (2) | Specifies the 16-QAM modulation type is used. |
|  | Channelization Code specifies the channelization code assigned to the channel. The default value is 1. The valid values are 1 to 16. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_create_signal_configuration.html language=enus -->
## TOPIC 00051: rfmxtdscdmavi/rfmxtdscdma_create_signal_configuration.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_create_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_create_signal_configuration.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Create Signal Configuration (VI)

RFmxTDSCDMA Create Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal.

[IMAGE alt='RFmxTDSCDMA Create Signal Configuration' src='rfmxtdscdma_create_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string you can use in the Selector String input for configuration VIs, fetch VIs, or the RFmxTDSCDMA Initiate VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_delete_signal_configuration.html language=enus -->
## TOPIC 00052: rfmxtdscdmavi/rfmxtdscdma_delete_signal_configuration.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_delete_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_delete_signal_configuration.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Delete Signal Configuration (VI)

RFmxTDSCDMA Delete Signal Configuration (VI)

Owning Palette:

Advanced

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='RFmxTDSCDMA Delete Signal Configuration' src='rfmxtdscdma_delete_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_get_all_named_result_names.html language=enus -->
## TOPIC 00053: rfmxtdscdmavi/rfmxtdscdma_get_all_named_result_names.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_get_all_named_result_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_get_all_named_result_names.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Get All Named Result Names (VI)

RFmxTDSCDMA Get All Named Result Names (VI)

Owning Palette:

Utility

Returns the named result names of the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxTDSCDMA Get All Named Result Names' src='rfmxtdscdma_get_all_named_result_names.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with the option string as "AnalysisOnly=1". |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Result Names returns an array of result names. |
|  | Default Result Exists? indicates whether the default result exists. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_initiate.html language=enus -->
## TOPIC 00054: rfmxtdscdmavi/rfmxtdscdma_initiate.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_initiate.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Initiate (VI)

RFmxTDSCDMA Initiate (VI)

Owning Palette:

RFmx TDSCDMA VIs

Initiates all enabled measurements. Call this VI after configuring the signal and measurement.

This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the [fetch](fetch_pal.html) VIs or result properties in the property node. To get the status of measurements, use the [RFmxTDSCDMA Wait for Measurement Complete](rfmxtdscdma_wait_for_measurement_complete.html) VI or the [RFmxTDSCDMA Check Measurement Status](rfmxtdscdma_check_measurement_status.html) VI.

[IMAGE alt='RFmxTDSCDMA Initiate' src='rfmxtdscdma_initiate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name input. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by the Result Name input or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String input for Fetch VIs when using named signal configurations or named results. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_modacc_configure_averaging.html language=enus -->
## TOPIC 00055: rfmxtdscdmavi/rfmxtdscdma_modacc_configure_averaging.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_modacc_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_modacc_configure_averaging.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA ModAcc Configure Averaging (VI)

RFmxTDSCDMA ModAcc Configure Averaging (VI)

Owning Palette:

ModAcc

Configures averaging for the ModAcc measurement.

[IMAGE alt='RFmxTDSCDMA ModAcc Configure Averaging' src='rfmxtdscdma_modacc_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the ModAcc measurement. The default value is False. False (0) Disables averaging for the ModAcc measurement. True (1) The ModAcc measurement uses the Averaging Count parameter as the number of acquisitions over which the ModAcc measurement is averaged. |
| False (0) | Disables averaging for the ModAcc measurement. |
| True (1) | The ModAcc measurement uses the Averaging Count parameter as the number of acquisitions over which the ModAcc measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_modacc_configure_slot_type.html language=enus -->
## TOPIC 00056: rfmxtdscdmavi/rfmxtdscdma_modacc_configure_slot_type.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_modacc_configure_slot_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_modacc_configure_slot_type.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA ModAcc Configure Slot Type (VI)

RFmxTDSCDMA ModAcc Configure Slot Type (VI)

Configures the type of the Time Slot for ModAcc analysis.

[IMAGE alt='RFmxTDSCDMA ModAcc Configure Slot Type' src='rfmxtdscdma_modacc_configure_slot_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | Slot Type specifies the type of the Time Slot for ModAcc analysis. The default value is Traffic. Traffic (0) The measurement is performed on the traffic time slot. The composite, data, and midamble ModAcc results are obtained when you select this slot type. Pilot (1) The measurement is performed on the pilot time slot. The pilot ModAcc results are obtained when you select this slot type. |
| Traffic (0) | The measurement is performed on the traffic time slot. The composite, data, and midamble ModAcc results are obtained when you select this slot type. |
| Pilot (1) | The measurement is performed on the pilot time slot. The pilot ModAcc results are obtained when you select this slot type. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_modacc_configure_synchronization_mode_and_interval.html language=enus -->
## TOPIC 00057: rfmxtdscdmavi/rfmxtdscdma_modacc_configure_synchronization_mode_and_interval.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_modacc_configure_synchronization_mode_and_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_modacc_configure_synchronization_mode_and_interval.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA ModAcc Configure Synchronization Mode and Interval (VI)

RFmxTDSCDMA ModAcc Configure Synchronization Mode and Interval (VI)

Owning Palette:

ModAcc

Configures the synchronization mode, measurement offset, and measurement length for ModAcc analysis.

[IMAGE alt='RFmxTDSCDMA ModAcc Configure Synchronization Mode and Interval' src='rfmxtdscdma_modacc_configure_synchronization_mode_and_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Mode specifies the synchronization mode for the ModAcc measurement. The default value is Slot. Slot (0) The measurement uses the slot synchronization mode. The first slot boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter, starting at the offset specified by the Measurement Offset parameter. If you set the Trigger Type property to Digital Edge, you should provide the trigger at the start of the slot from which the Measurement Offset parameter should be considered. If you set the Trigger Type property to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, for this trigger type, the traffic time slot(s) in the received signal should be contiguous with the pilot time slot, if the pilot time slot is present. Subframe (1) The measurement uses the subframe synchronization mode. The first subframe boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter, starting at the offset from the boundary specified by the Measurement Offset parameter. If you set the Trigger Type property to Digital Edge, you should provide the trigger at the start of the subframe. If you set the Trigger Type property to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, the traffic time slot should be contiguous with the active pilot slot. |
| Slot (0) | The measurement uses the slot synchronization mode. The first slot boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter, starting at the offset specified by the Measurement Offset parameter. If you set the Trigger Type property to Digital Edge, you should provide the trigger at the start of the slot from which the Measurement Offset parameter should be considered. If you set the Trigger Type property to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, for this trigger type, the traffic time slot(s) in the received signal should be contiguous with the pilot time slot, if the pilot time slot is present. |
| Subframe (1) | The measurement uses the subframe synchronization mode. The first subframe boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter, starting at the offset from the boundary specified by the Measurement Offset parameter. If you set the Trigger Type property to Digital Edge, you should provide the trigger at the start of the subframe. If you set the Trigger Type property to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, the traffic time slot should be contiguous with the active pilot slot. |
|  | Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The default value is 0. |
|  | Measurement Length specifies the duration of the ModAcc measurement. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_modacc_fetch.html language=enus -->
## TOPIC 00058: rfmxtdscdmavi/rfmxtdscdma_modacc_fetch.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_modacc_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_modacc_fetch.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA ModAcc Fetch (VI)

RFmxTDSCDMA ModAcc Fetch (VI)

Owning Palette:

Fetch

Fetches the ModAcc measurement results.

#### RFmxTDSCDMA ModAcc Fetch Data EVM

Returns the EVM measurement of the data channel.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Data EVM' src='rfmxtdscdma_modacc_fetch_data_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS Data EVM returns the RMS of the data EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. |
|  | Peak Data EVM returns the peak data EVM among all active time slots and averaging iterations. This value is expressed as a percentage. |
|  | Data Rho returns the data rho value, averaged over all active time slots and all averaging iterations. |
|  | RMS Data Phase Error returns the RMS of the data phase error, averaged over all active time slots and all averaging iterations. This value is expressed in degrees. |
|  | RMS Data Magnitude Error returns the RMS of the data magnitude error, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Midamble EVM

Returns the midamble EVM measurement results.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Midamble EVM' src='rfmxtdscdma_modacc_fetch_midamble_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS Midamble EVM returns the RMS of the midamble EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. |
|  | Peak Midamble EVM returns the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage. |
|  | Midamble Rho returns the rho value of the midamble, averaged over all measured active time slots and averaging iterations. |
|  | RMS Midamble Phase Error returns the RMS of the midamble phase error, averaged over all active time slots and all averaging iterations. This value is expressed in degrees. |
|  | RMS Midamble Magnitude Error returns the RMS of the midamble magnitude error, averaged over all active time slots and averaging iterations. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Data Active CDE

Returns the peak value among the code domain errors (CDEs) of the active channels, as well as the code number, spreading factor, and branch that correspond to this peak value.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Data Active CDE' src='rfmxtdscdma_modacc_fetch_data_active_cde.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Peak Data Active CDE returns the maximum value of the peak data active CDE among all active physical channels, active time slots and averaging iterations. This value is expressed in dB. The peak data active CDE value is averaged over all averaging iterations. |
|  | Peak Data Active CDE Spreading Factor returns the spreading factor used for retrieving the peak CDE of the active physical channel corresponding to measured value of the Maximum Peak Data Active CDE property. |
|  | Peak Data Active CDE Code returns the peak channelization code of the channel corresponding to the measured value of the Maximum Peak Data Active CDE property. |
|  | Peak Data Active CDE Number of Channels returns the number of channels used to determine the peak active CDE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Data CDE

Returns the maximum value of the measured data code domain errors (CDEs), along with the spreading factor and the channelization code of the corresponding channel.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Data CDE' src='rfmxtdscdma_modacc_fetch_data_cde.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Peak Data CDE returns the maximum peak CDE among all active time slots and averaging iterations. This value is expressed in dB. |
|  | Peak Data CDE Spreading Factor returns the spreading factor used for retrieving the peak CDE of the channel corresponding to measured value of the Maximum Peak Data CDE property. |
|  | Peak Data CDE Code returns the peak channelization code of the channel corresponding to the measured value of the Maximum Peak Data CDE property. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Data RCDE

Returns the maximum value of the measured data relative code domain error (RCDE), along with the spreading factor and the channelization code of the corresponding channel.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Data RCDE' src='rfmxtdscdma_modacc_fetch_data_rcde.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Peak Data RCDE returns the maximum value of the peak RDCEs among all active time slots and averaging iterations. This value is expressed in dB. RFmx calculates the RCDEs by projecting the descrambled error vector onto the codes of each active channel. The RCDE is the ratio of the mean power of the projection onto that code to the mean power of the corresponding active channel in the reference waveform. |
|  | Peak Data RCDE Spreading Factor returns the spreading factor of the channel corresponding to the value of the ModAcc Results Pk Data RCDE property. |
|  | Peak Data RCDE Code returns the channelization code of the channel corresponding to the value of the ModAcc Results Pk Data RCDE Code property. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Pilot EVM

Fetches the EVM measurement of the pilot time slot.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Pilot EVM' src='rfmxtdscdma_modacc_fetch_pilot_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS Pilot EVM returns the RMS of the pilot EVM, averaged over all averaging iterations. This value is expressed as a percentage. |
|  | Peak Pilot EVM returns the maximum of the peak pilot EVM among the averaging iterations. This value is expressed as a percentage. |
|  | Pilot Rho returns the pilot Rho value, averaged over all averaging iterations. |
|  | RMS Pilot Phase Error returns the RMS of the pilot phase error, averaged over all averaging iterations. This value is expressed in degrees. |
|  | RMS Pilot Magnitude Error returns the RMS of the pilot magnitude error, averaged over all the averaging iterations. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch IQ Impairments

Returns the I/Q origin offset, I/Q gain imbalance, and I/Q quadrature error.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch IQ Impairments' src='rfmxtdscdma_modacc_fetch_iq_impairments.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | I/Q Origin Offset returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. |
|  | I/Q Gain Imbalance returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. |
|  | I/Q Quadrature Error returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Midamble and Data Power

Returns the power of the midamble and the data channel.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Midamble and Data Power' src='rfmxtdscdma_modacc_fetch_midamble_and_data_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Midamble Power returns the power of the midamble, averaged over all measured slots. This value is expressed in dBm. |
|  | Data Field 1 Power returns the power of the data field 1, averaged over all measured slots. This value is expressed in dBm. |
|  | Data Field 2 Power returns the power of the data field 2, averaged over all measured slots. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Number of Detected Channels

Returns the number of detected channels. If the averaging is enabled, it returns the number of detected channels of the last averaging iteration. If you set the Channel Configuration Mode property to **User Defined**, the measurement returns the number of configured channels.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Number of Detected Channels' src='rfmxtdscdma_modacc_fetch_number_of_detected_channels.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Number of Detected Channels returns the total number of the detected channels. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Composite EVM

Returns the composite EVM of all the channels in the ModAcc measurement.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Composite EVM' src='rfmxtdscdma_modacc_fetch_composite_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS Composite EVM returns the value of the RMS of the composite EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. Values close to 0 indicate a good modulation accuracy. In a loopback setup, values of approximately 0.2 to 0.4 are typical. |
|  | Peak Composite EVM returns the value of the peak composite EVM among all active time slots and averaging iterations. This value is expressed as a percentage. |
|  | Composite Rho returns the composite value of rho, averaged over all active time-slots and all averaging iterations. A value of 1 indicates a perfectly modulated signal. Typical values for real signals in a loopback setup are slightly below 1.000000. |
|  | Chip Rate Error returns the chip rate error. This value is expressed in ppm. |
|  | Frequency Error returns the frequency error averaged over all measured slots. This value is expressed in Hz. |
|  | RMS Composite Magnitude Error returns the value of the time-slot based RMS of the composite magnitude error averaged over all active time slots and averaging iterations. This value is expressed as a percentage. |
|  | RMS Composite Phase Error returns the time-slot based RMS of the composite phase error, averaged over all active time slots and averaging iterations. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Detected Channel

Returns a detected channel by its channel name.

Use "channel*<n>*" as the selector string to read results from this VI.

If the averaging is enabled, the detected channels of the last averaging operation can be retrieved.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Detected Channel' src='rfmxtdscdma_modacc_fetch_detected_channel.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and channel number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "channel0" "signal::sig1/channel0" "result::r1/channel0" "signal::sig1/result::r1/channel0" You can use the RFmxTDSCDMA Build Channel String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Detected Slot Index returns the slot index of the detected channel. |
|  | Detected Spreading Factor returns the spreading factor of the detected channel. |
|  | Detected Modulation Type returns the modulation type for the detected channel. QPSK (0) The modulation type is QPSK. 8PSK (1) The modulation type is 8-PSK. 16QAM (2) The modulation type is16-QAM. |
| QPSK (0) | The modulation type is QPSK. |
| 8PSK (1) | The modulation type is 8-PSK. |
| 16QAM (2) | The modulation type is16-QAM. |
|  | Detected Channelization Code returns the channelization code of the detected channel. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Detected Channel (Array)

Returns the detected channels. If you set the Channel Configuration Mode property to **User Defined**, the measurement returns the configured channels. If the averaging is enabled, this VI returns the array of detected channels of the last averaging iteration.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Detected Channel (Array)' src='rfmxtdscdma_modacc_fetch_detected_channel_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Detected Slot Index returns an array of slot indexes of the detected channels. |
|  | Detected Spreading Factor returns an array of spreading factors of the detected channels. |
|  | Detected Modulation Type returns an array of the modulation types for the detected channels. QPSK (0) The modulation type is QPSK. 8PSK (1) The modulation type is 8-PSK. 16QAM (2) The modulation type is 16-QAM. |
| QPSK (0) | The modulation type is QPSK. |
| 8PSK (1) | The modulation type is 8-PSK. |
| 16QAM (2) | The modulation type is 16-QAM. |
|  | Detected Channelization Code returns an array of channelization code numbers for the detected channels. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch EVM Trace

Fetches the average of the EVM traces on the chip level.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch EVM Trace' src='rfmxtdscdma_modacc_fetch_evm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | EVM returns the average of the EVM traces on the chip level. x0 returns the start time of the trace. This value is expressed in seconds. dx returns the sampling time of the trace. This value is expressed in seconds. y returns the EVM trace values as a real value array. |
|  | x0 returns the start time of the trace. This value is expressed in seconds. |
|  | dx returns the sampling time of the trace. This value is expressed in seconds. |
|  | y returns the EVM trace values as a real value array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Maximum EVM Trace

Fetches the maximum EVM trace values on the chip level.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Maximum EVM Trace' src='rfmxtdscdma_modacc_fetch_maximum_evm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum EVM returns the maximum EVM trace values on the chip level. x0 returns the start time of the trace. This value is expressed in seconds. dx returns the sampling time of the trace. This value is expressed in seconds. y returns an array of the maximum EVM trace values on the chip level. This value is expressed as a percentage. |
|  | x0 returns the start time of the trace. This value is expressed in seconds. |
|  | dx returns the sampling time of the trace. This value is expressed in seconds. |
|  | y returns an array of the maximum EVM trace values on the chip level. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Magnitude Error Trace

Fetches the average of the magnitude error trace on the chip level.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Magnitude Error Trace' src='rfmxtdscdma_modacc_fetch_magnitude_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Magnitude Error returns the data for a complex waveform including the start, delta, and actual values. x0 returns the start time of the trace. This value is expressed in seconds. dx returns the sampling time of the trace. This value is expressed in seconds. y returns the magnitude trace error values as a real value array. |
|  | x0 returns the start time of the trace. This value is expressed in seconds. |
|  | dx returns the sampling time of the trace. This value is expressed in seconds. |
|  | y returns the magnitude trace error values as a real value array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Maximum Magnitude Error Trace

Fetches the maximum magnitude error trace on the chip level.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Maximum Magnitude Error Trace' src='rfmxtdscdma_modacc_fetch_maximum_magnitude_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Magnitude Error returns the maximum magnitude error trace on the chip level. x0 returns the start time of the trace. This value is expressed in seconds. dx returns the sampling time of the trace. This value is expressed in seconds. y returns an array of maximum magnitude error trace on the chip level. This value is expressed as a percentage. |
|  | x0 returns the start time of the trace. This value is expressed in seconds. |
|  | dx returns the sampling time of the trace. This value is expressed in seconds. |
|  | y returns an array of maximum magnitude error trace on the chip level. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Phase Error Trace

Returns the average of the phase error trace on the chip level.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Phase Error Trace' src='rfmxtdscdma_modacc_fetch_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Phase Error returns the data for a complex waveform including the start, delta, and actual values. x0 returns the start time of the trace. This value is expressed in seconds. dx returns the sampling time of the trace. This value is expressed in seconds. y returns the phase error trace values as a real value array. This value is expressed in degrees. |
|  | x0 returns the start time of the trace. This value is expressed in seconds. |
|  | dx returns the sampling time of the trace. This value is expressed in seconds. |
|  | y returns the phase error trace values as a real value array. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Maximum Phase Error Trace

Fetches the maximum phase error trace on the chip level.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Maximum Phase Error Trace' src='rfmxtdscdma_modacc_fetch_maximum_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Phase Error returns the maximum phase error trace on the chip level. x0 returns the start time of the trace. This value is expressed in seconds. dx returns the sampling time of the trace. This value is expressed in seconds. y returns an array of the maximum phase error traces on the chip level. This value is expressed in degrees. |
|  | x0 returns the start time of the trace. This value is expressed in seconds. |
|  | dx returns the sampling time of the trace. This value is expressed in seconds. |
|  | y returns an array of the maximum phase error traces on the chip level. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Constellation Trace

Fetches the constellation trace of the received TD-SCDMA signal. If the averaging is enabled, this trace refers to the last averaging iteration..

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Constellation Trace' src='rfmxtdscdma_modacc_fetch_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Constellation returns an array of complex chips of the corrected signal on which the ModAcc measurements are performed. You can use these chips to obtain the constellation diagram. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Code Domain Error Trace

Fetches the value of the code domain error trace for the individual code channels in the domain of the base spreading factor. This value is averaged over all active time slots and averaging iterations.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Code Domain Error Trace' src='rfmxtdscdma_modacc_fetch_code_domain_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Code Domain Error returns an array of the code domain error traces for the individual code channels in the domain of the base spreading factor averaged over all active time slots and averaging iterations. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA ModAcc Fetch Maximum Code Domain Error Trace

Fetches the maximum code domain error trace among all active time slots and averaging iterations for the ModAcc measurement.

[IMAGE alt='RFmxTDSCDMA ModAcc Fetch Maximum Code Domain Error Trace' src='rfmxtdscdma_modacc_fetch_maximum_code_domain_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Code Domain Error returns an array of the maximum code domain error traces among all active time slots and averaging iterations. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_obw_configure_averaging.html language=enus -->
## TOPIC 00059: rfmxtdscdmavi/rfmxtdscdma_obw_configure_averaging.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_obw_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_obw_configure_averaging.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA OBW Configure Averaging (VI)

RFmxTDSCDMA OBW Configure Averaging (VI)

Owning Palette:

OBW

Configures averaging for the OBW measurement.

[IMAGE alt='RFmxTDSCDMA OBW Configure Averaging' src='rfmxtdscdma_obw_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled enables averaging for spectrum measurements. The default value is False. False (0) Disables averaging for the OBW measurement. True (1) The OBW measurement uses the value of the OBW Averaging Count property as the number of acquisitions over which the OBW measurement is averaged. |
| False (0) | Disables averaging for the OBW measurement. |
| True (1) | The OBW measurement uses the value of the OBW Averaging Count property as the number of acquisitions over which the OBW measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. Refer to the Averaging section of the Spectrum topic for more information about averaging types. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_obw_configure_rbw_filter.html language=enus -->
## TOPIC 00060: rfmxtdscdmavi/rfmxtdscdma_obw_configure_rbw_filter.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_obw_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_obw_configure_rbw_filter.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA OBW Configure RBW Filter (VI)

RFmxTDSCDMA OBW Configure RBW Filter (VI)

Owning Palette:

OBW

Configures the RBW filter.

[IMAGE alt='RFmxTDSCDMA OBW Configure RBW Filter' src='rfmxtdscdma_obw_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. The default value is True. False (0) The measurement uses the RBW you specify. True (1) RFmx TD-SCDMA automatically determines the RBW. Refer to the RBW and Sweep Time section in the Spectrum topic for more information about RBW and sweep time. |
| False (0) | The measurement uses the RBW you specify. |
| True (1) | RFmx TD-SCDMA automatically determines the RBW. |
|  | RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 5.636 kHz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is FFT Based. FFT Based (0) An RBW filter with a fast Fourier transform (FFT)-based response is applied. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_obw_configure_sweep_time.html language=enus -->
## TOPIC 00061: rfmxtdscdmavi/rfmxtdscdma_obw_configure_sweep_time.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_obw_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_obw_configure_sweep_time.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA OBW Configure Sweep Time (VI)

RFmxTDSCDMA OBW Configure Sweep Time (VI)

Owning Palette:

OBW

Configures the sweep time.

[IMAGE alt='RFmxTDSCDMA OBW Configure Sweep Time' src='rfmxtdscdma_obw_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of .00066 seconds (s). Refer to the RBW and Sweep Time section in the OBW topic for more details on RBW and sweep time. |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of .00066 seconds (s). |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 0.00066 s. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_obw_fetch.html language=enus -->
## TOPIC 00062: rfmxtdscdmavi/rfmxtdscdma_obw_fetch.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_obw_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_obw_fetch.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA OBW Fetch (VI)

RFmxTDSCDMA OBW Fetch (VI)

Owning Palette:

Fetch

Fetches the OBW measurement results.

#### RFmxTDSCDMA OBW Fetch Measurement

Returns the OBW measurement.

[IMAGE alt='RFmxTDSCDMA OBW Fetch Measurement' src='rfmxtdscdma_obw_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Occupied Bandwidth returns the OBW. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency. |
|  | Absolute Power returns the total integrated power of the averaged spectrum acquired by the OBW measurement. This value is expressed in dBm. |
|  | Stop Frequency returns the stop frequency of the OBW. This value is expressed in Hz. |
|  | Start Frequency returns the start frequency of the OBW. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA OBW Fetch Spectrum

Fetches the spectrum trace used for the OBW measurement.

[IMAGE alt='RFmxTDSCDMA OBW Fetch Spectrum' src='rfmxtdscdma_obw_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_property_node.html language=enus -->
## TOPIC 00063: rfmxtdscdmavi/rfmxtdscdma_property_node.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_property_node.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_property_node.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Property Node (VI)

RFmxTDSCDMA Property Node (VI)

Owning Palette:

RFmx TDSCDMA VIs

Gets (reads), sets (writes), or resets (sets to default value) RFmxTDSCDMA properties.

[IMAGE alt='RFmxTDSCDMA Property Node' src='rfmxtdscdma_property_node.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_pvt_configure_averaging.html language=enus -->
## TOPIC 00064: rfmxtdscdmavi/rfmxtdscdma_pvt_configure_averaging.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_pvt_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_pvt_configure_averaging.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA PVT Configure Averaging (VI)

RFmxTDSCDMA PVT Configure Averaging (VI)

Owning Palette:

PVT

Configures averaging for the power versus time (PVT) measurement.

[IMAGE alt='RFmxTDSCDMA PVT Configure Averaging' src='rfmxtdscdma_pvt_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the PVT measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The PVT measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the PVT measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The PVT measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the PVT measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the PVT measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged on a logarithmic scale. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged on a logarithmic scale. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_pvt_configure_measurement_method.html language=enus -->
## TOPIC 00065: rfmxtdscdmavi/rfmxtdscdma_pvt_configure_measurement_method.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_pvt_configure_measurement_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_pvt_configure_measurement_method.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA PVT Configure Measurement Method (VI)

RFmxTDSCDMA PVT Configure Measurement Method (VI)

Owning Palette:

PVT

Configures the measurement method for the power versus time (PVT) measurement.

[IMAGE alt='RFmxTDSCDMA PVT Configure Measurement Method' src='rfmxtdscdma_pvt_configure_measurement_method.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Method specifies the method used for performing the PVT measurement. The default value is Normal. Normal (0) The PVT measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when a higher measurement speed is preferred over a higher dynamic range. Dynamic Range (1) The PVT measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5644R/5645R/5646R/5840/5841/5842. |
| Normal (0) | The PVT measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when a higher measurement speed is preferred over a higher dynamic range. |
| Dynamic Range (1) | The PVT measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5644R/5645R/5646R/5840/5841/5842. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_pvt_fetch.html language=enus -->
## TOPIC 00066: rfmxtdscdmavi/rfmxtdscdma_pvt_fetch.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_pvt_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_pvt_fetch.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA PVT Fetch (VI)

RFmxTDSCDMA PVT Fetch (VI)

Owning Palette:

Fetch

Fetches the power versus time (PVT) measurement results.

#### RFmxTDSCDMA PVT Fetch Measurement Status

Fetches the overall status of the power versus time (PVT) measurement.

[IMAGE alt='RFmxTDSCDMA PVT Fetch Measurement Status' src='rfmxtdscdma_pvt_fetch_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the overall status of the PVT measurement. Fail (0) Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. Pass (1) Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |
| Fail (0) | Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. |
| Pass (1) | Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA PVT Fetch Powers

Fetches the values of the **Mean Absolute ON Power** and **Mean Absolute OFF Power** parameters.

[IMAGE alt='RFmxTDSCDMA PVT Fetch Powers' src='rfmxtdscdma_pvt_fetch_powers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Absolute ON Power returns the mean on power of the measured burst, or the averaged bursts. This value is expressed in dBm. |
|  | Mean Absolute OFF Power returns the mean off power of the measured burst, or the averaged bursts. This value is expressed in dBm. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA PVT Fetch Segment Measurement

Returns the status of a specific power versus time (PVT) measurement segment along with the measured segment powers.

Use "segment<*n*>" as the selector string to read this VI.

[IMAGE alt='RFmxTDSCDMA PVT Fetch Segment Measurement' src='rfmxtdscdma_pvt_fetch_segment_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxTDSCDMA Build Segment String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Segment Status returns the measurement status for an individual PVT measurement segment. Fail (0) Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. Pass (1) Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |
| Fail (0) | Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. |
| Pass (1) | Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |
|  | Segment Margin returns the power margin for an individual PVT measurement segment, which is the minimum power distance to the power limit measured within the PVT measurement segment. This value is expressed in dB. |
|  | Segment Margin Time returns the position in time corresponding to the Segment Margin parameter. This value is expressed in seconds. |
|  | Segment Mean Absolute Power returns the mean measured power corresponding to the Segment Margin parameter. This value is expressed in dBm. |
|  | Segment Maximum Absolute Power returns the maximum measured power of an individual PVT measurement segment. This value is expressed in dBm. |
|  | Segment Minimum Absolute Power returns the minimum measured power of an individual PVT measurement segment. This value is expressed in dBm. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA PVT Fetch Segment Measurement (Array)

Fetches the status and measured powers for all the power versus time (PVT) measurement segments.

[IMAGE alt='RFmxTDSCDMA PVT Fetch Segment Measurement (Array)' src='rfmxtdscdma_pvt_fetch_segment_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Segment Status returns an array of the measurement status values for an individual PVT measurement segment. Fail (0) Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. Pass (1) Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |
| Fail (0) | Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. |
| Pass (1) | Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |
|  | Segment Margin returns an array of the power margins for an individual PVT measurement segment, which is the minimum power distance to the power limit measured within the PVT measurement segment. This value is expressed in dB. |
|  | Segment Margin Time returns an array of the positions in time corresponding to the Segment Margin parameter. This value is expressed in seconds. |
|  | Segment Mean Absolute Power returns an array of the mean measured powers corresponding to the Segment Margin parameter. This value is expressed in dBm. |
|  | Segment Maximum Absolute Power returns an array of the maximum measured powers of an individual PVT measurement segment. This value is expressed in dBm. |
|  | Segment Minimum Absolute Power returns an array of the minimum measured powers of an individual PVT measurement segment. This value is expressed in dBm. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA PVT Fetch Signal Power Trace

Fetches the signal power trace and the absolute limit trace. The limit trace is defined by the transmit ON/off time mask measurement in the 3GPP TS 34.122 specification.

[IMAGE alt='RFmxTDSCDMA PVT Fetch Signal Power Trace' src='rfmxtdscdma_pvt_fetch_signal_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Signal Power returns the measured signal power over a specified period of time. x0 returns the start time of the trace relative to the start of the analyzed burst. dx returns the time difference between successive trace samples. y returns an array of values for the signal power trace. These values are expressed in dBm. |
|  | x0 returns the start time of the trace relative to the start of the analyzed burst. |
|  | dx returns the time difference between successive trace samples. |
|  | y returns an array of values for the signal power trace. These values are expressed in dBm. |
|  | Absolute Limit returns the power limit as defined by the transmit ON/OFF time mask in the 3GPP TS 34.122 specification. x0 returns the start time of the limit trace relative to the burst start. dx returns the time difference between successive trace samples. y returns an array of values for the absolute power limit trace. These values are expressed in dBm. |
|  | x0 returns the start time of the limit trace relative to the burst start. |
|  | dx returns the time difference between successive trace samples. |
|  | y returns an array of values for the absolute power limit trace. These values are expressed in dBm. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_reset_to_default.html language=enus -->
## TOPIC 00067: rfmxtdscdmavi/rfmxtdscdma_reset_to_default.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_reset_to_default.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_reset_to_default.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Reset to Default (VI)

RFmxTDSCDMA Reset to Default (VI)

Owning Palette:

Utility

Resets a signal to the default values.

[IMAGE alt='RFmxTDSCDMA Reset to Default' src='rfmxtdscdma_reset_to_default.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_select_measurement.html language=enus -->
## TOPIC 00068: rfmxtdscdmavi/rfmxtdscdma_select_measurement.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_select_measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_select_measurement.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Select Measurement (VI)

RFmxTDSCDMA Select Measurement (VI)

Owning Palette:

RFmx TDSCDMA VIs

Specifies the measurements that you want to enable. To select multiple measurements, use the **Multiple Measurements** instance. To select a single measurement, use the **Single Measurement** instance.

#### RFmxTDSCDMA Select Measurement (Multiple)

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='RFmxTDSCDMA Select Measurement (Multiple)' src='rfmxtdscdma_select_measurement_(multiple).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurements specifies the measurement to perform. ModAcc (0) Enables the ModAcc measurement. ACP (1) Enables the ACP measurement. CHP (2) Enables the CHP measurement. OBW (3) Enables the OBW measurement. SEM (4) Enables the SEM measurement. CDA (5) Enables the code domain analysis (CDA) measurement. PVT (6) Enables the power versus time (PVT) measurement. SlotPower (7) Enables the SlotPower measurement. The default is an empty array. |
| ModAcc (0) | Enables the ModAcc measurement. |
| ACP (1) | Enables the ACP measurement. |
| CHP (2) | Enables the CHP measurement. |
| OBW (3) | Enables the OBW measurement. |
| SEM (4) | Enables the SEM measurement. |
| CDA (5) | Enables the code domain analysis (CDA) measurement. |
| PVT (6) | Enables the power versus time (PVT) measurement. |
| SlotPower (7) | Enables the SlotPower measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA Select Measurement (Single)

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='RFmxTDSCDMA Select Measurement (Single)' src='rfmxtdscdma_select_measurement_(single).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement specifies the measurement to perform. ModAcc (0) Enables the ModAcc measurement. ACP (1) Enables the ACP measurement. CHP (2) Enables the CHP measurement. OBW (3) Enables the OBW measurement. SEM (4) Enables the SEM measurement. CDA (5) Enables the code domain analysis (CDA) measurement. PVT (6) Enables the power versus time (PVT) measurement. SlotPower (7) Enables the SlotPower measurement. The default value is ModAcc. |
| ModAcc (0) | Enables the ModAcc measurement. |
| ACP (1) | Enables the ACP measurement. |
| CHP (2) | Enables the CHP measurement. |
| OBW (3) | Enables the OBW measurement. |
| SEM (4) | Enables the SEM measurement. |
| CDA (5) | Enables the code domain analysis (CDA) measurement. |
| PVT (6) | Enables the power versus time (PVT) measurement. |
| SlotPower (7) | Enables the SlotPower measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_sem_configure_averaging.html language=enus -->
## TOPIC 00069: rfmxtdscdmavi/rfmxtdscdma_sem_configure_averaging.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_sem_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_sem_configure_averaging.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA SEM Configure Averaging (VI)

RFmxTDSCDMA SEM Configure Averaging (VI)

Owning Palette:

SEM

Configures averaging for the SEM measurement.

[IMAGE alt='RFmxTDSCDMA SEM Configure Averaging' src='rfmxtdscdma_sem_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled enables averaging for spectrum measurements. The default value is False. False (0) Disables averaging for the SEM measurement. True (1) The SEM measurement uses the value of the SEM Averaging Count property as the number of acquisitions over which the SEM measurement is averaged. |
| False (0) | Disables averaging for the SEM measurement. |
| True (1) | The SEM measurement uses the value of the SEM Averaging Count property as the number of acquisitions over which the SEM measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. Refer to the Averaging section of the Spectrum topic for more information about averaging types. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_sem_configure_sweep_time.html language=enus -->
## TOPIC 00070: rfmxtdscdmavi/rfmxtdscdma_sem_configure_sweep_time.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_sem_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_sem_configure_sweep_time.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA SEM Configure Sweep Time (VI)

RFmxTDSCDMA SEM Configure Sweep Time (VI)

Owning Palette:

SEM

Configures the sweep time.

[IMAGE alt='RFmxTDSCDMA SEM Configure Sweep Time' src='rfmxtdscdma_sem_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of .00066 seconds (s). |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of .00066 seconds (s). |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 0.00066 s. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_sem_fetch.html language=enus -->
## TOPIC 00071: rfmxtdscdmavi/rfmxtdscdma_sem_fetch.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_sem_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_sem_fetch.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA SEM Fetch (VI)

RFmxTDSCDMA SEM Fetch (VI)

Owning Palette:

Fetch

Fetches the SEM measurement results.

#### RFmxTDSCDMA SEM Fetch Measurement Status

Returns the SEM measurement status.

[IMAGE alt='RFmxTDSCDMA SEM Fetch Measurement Status' src='rfmxtdscdma_sem_fetch_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the status of the measurement based on measurement limits and the failure criteria specified by the standard. Fail (0) The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. Pass (1) The signal does not exceed the spectrum emission limits. |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |
| Pass (1) | The signal does not exceed the spectrum emission limits. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA SEM Fetch Carrier Absolute Integrated Power

Returns the absolute carrier integrated power of the SEM measurement.

[IMAGE alt='RFmxTDSCDMA SEM Fetch Carrier Absolute Integrated Power' src='rfmxtdscdma_sem_fetch_carrier_absolute_integrated_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Carrier Absolute Integrated Power returns the carrier power. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA SEM Fetch Lower Offset Power

Returns the lower offset segment power measurements.

Use "offset<n>" as the selector string to read results from this VI.

[IMAGE alt='RFmxTDSCDMA SEM Fetch Lower Offset Power' src='rfmxtdscdma_sem_fetch_lower_offset_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxTDSCDMA Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the lower (negative) offset segment power measured. This value is expressed in dBm. |
|  | Relative Integrated Power returns the power in the negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Absolute Peak Power returns the peak power measured in the lower (negative) offset segment. This value is expressed in dBm. |
|  | Relative Peak Power returns the peak power in the lower (negative) offset segment relative to the integrated power of the reference carrier. |
|  | Peak Frequency returns the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA SEM Fetch Lower Offset Power (Array)

Returns the arrays of lower offset segment power measurements.

[IMAGE alt='RFmxTDSCDMA SEM Fetch Lower Offset Power (Array)' src='rfmxtdscdma_sem_fetch_lower_offset_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the array of lower (negative) offset segment powers measured. This value is expressed in dBm. |
|  | Relative Integrated Power returns the array of powers in each negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Absolute Peak Power returns the array of peak powers measured in each lower (negative) offset segment. This value is expressed in dBm. |
|  | Relative Peak Power returns the array of peak powers in the lower (negative) offset segment relative to the integrated power of the reference carrier. |
|  | Peak Frequency returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA SEM Fetch Upper Offset Power

Returns the upper offset segment power measurements.

Use "offset<n>" as the selector string to read results from this VI.

[IMAGE alt='RFmxTDSCDMA SEM Fetch Upper Offset Power' src='rfmxtdscdma_sem_fetch_upper_offset_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxTDSCDMA Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the upper (positive) offset segment power measured. This value is expressed in dBm. |
|  | Relative Integrated Power returns the power in the positive offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Absolute Peak Power returns the peak power measured in the upper (positive) offset segment. This value is expressed in dBm. |
|  | Relative Peak Power returns the peak power in the upper (positive) offset segment relative to the integrated power of the reference carrier. |
|  | Peak Frequency returns the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA SEM Fetch Upper Offset Power (Array)

Returns the arrays of upper offset segment power measurements.

[IMAGE alt='RFmxTDSCDMA SEM Fetch Upper Offset Power (Array)' src='rfmxtdscdma_sem_fetch_upper_offset_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the array of upper (positive) offset segment powers measured. This value is expressed in dBm. |
|  | Relative Integrated Power returns the array of powers measured in each positive offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Absolute Peak Power returns the array of peak powers measured in each upper (positive) offset segment. This value is expressed in dBm. |
|  | Relative Peak Power returns the array of peak powers measured in each upper (positive) offset segment relative to the integrated power of the reference carrier. |
|  | Peak Frequency returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA SEM Fetch Lower Offset Margin

Returns the measurement status and margin from the limit line measured in the lower offset segment.

Use "offset<n>" as the selector string to read results from this VI.

[IMAGE alt='RFmxTDSCDMA SEM Fetch Lower Offset Margin' src='rfmxtdscdma_sem_fetch_lower_offset_margin.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxTDSCDMA Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the lower offset measurement status based on measurement limits and the failure criteria specified by the standard. Fail (0) The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. Pass (1) The signal does not exceed the spectrum emission limits. |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |
| Pass (1) | The signal does not exceed the spectrum emission limits. |
|  | Margin returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
|  | Margin Frequency returns the frequency at which the margin occurs in the negative offset. This value is expressed in Hz. |
|  | Margin Relative Power returns the power at which the margin occurs in the negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Margin Absolute Power returns the power at which the margin occurs in the negative offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA SEM Fetch Lower Offset Margin (Array)

Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments.

[IMAGE alt='RFmxTDSCDMA SEM Fetch Lower Offset Margin (Array)' src='rfmxtdscdma_sem_fetch_lower_offset_margin_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the array of lower offset measurement statuses based on measurement limits and the failure criteria specified by the standard. Fail (0) The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. Pass (1) The signal does not exceed the spectrum emission limits. |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |
| Pass (1) | The signal does not exceed the spectrum emission limits. |
|  | Margin returns the array of margins from the limit mask value specified by the standard. This value is expressed in dB. The margin is defined as the minimum distance between the spectrum and the limit mask. |
|  | Margin Frequency returns the array of frequencies at which the margin occurs in each negative offset segment. This value is expressed in Hz. |
|  | Margin Relative Power returns the array of powers at which the margin occurs in each negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Margin Absolute Power returns the array of powers at which the margin occurs in the negative offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA SEM Fetch Upper Offset Margin

Returns the measurement status and margin from the limit line measured in the upper offset segment.

Use "offset<n>" as the selector string to read results from this VI.

[IMAGE alt='RFmxTDSCDMA SEM Fetch Upper Offset Margin' src='rfmxtdscdma_sem_fetch_upper_offset_margin.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxTDSCDMA Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. Fail (0) The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. Pass (1) The signal does not exceed the spectrum emission limits. |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |
| Pass (1) | The signal does not exceed the spectrum emission limits. |
|  | Margin returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
|  | Margin Frequency returns the frequency at which the margin occurs in the positive offset. This value is expressed in Hz. |
|  | Margin Relative Power returns the power at which the margin occurs in the positive offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Margin Absolute Power returns the power at which the margin occurs in the positive offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA SEM Fetch Upper Offset Margin (Array)

Returns the measurement status and margin from the limit line measured in the upper offset segments.

[IMAGE alt='RFmxTDSCDMA SEM Fetch Upper Offset Margin (Array)' src='rfmxtdscdma_sem_fetch_upper_offset_margin_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the array of upper offset measurement statuses based on measurement limits and the failure criteria specified by the standard. Fail (0) The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. Pass (1) The signal does not exceed the spectrum emission limits. |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |
| Pass (1) | The signal does not exceed the spectrum emission limits. |
|  | Margin returns the array of margins from the limit mask value specified by the standard. This value is expressed in dB. The margin is defined as the minimum distance between the spectrum and the limit mask. |
|  | Margin Frequency returns the array of frequencies at which the margin occurs in each positive offset. This value is expressed in Hz. |
|  | Margin Relative Power returns the array of powers at which the margin occurs in each positive offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Margin Absolute Power returns the array of powers at which the margin occurs in each positive offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxTDSCDMA SEM Fetch Spectrum

Fetches the spectrum used for the SEM measurement.

[IMAGE alt='RFmxTDSCDMA SEM Fetch Spectrum' src='rfmxtdscdma_sem_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | Relative Mask returns the trace of power levels representing the relative mask in the spectral domain. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | Absolute Mask returns the data for a real waveform including the start, delta, and actual values. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_send_software_edge_trigger.html language=enus -->
## TOPIC 00072: rfmxtdscdmavi/rfmxtdscdma_send_software_edge_trigger.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_send_software_edge_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_send_software_edge_trigger.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Send Software Edge Trigger (VI)

RFmxTDSCDMA Send Software Edge Trigger (VI)

Owning Palette:

Configuration

Sends a trigger to the device when you use the [RFmxTDSCDMA Configure Trigger](rfmxtdscdma_configure_trigger.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxTDSCDMA Initiate VI.

[IMAGE alt='RFmxTDSCDMA Send Software Edge Trigger' src='rfmxtdscdma_send_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_slotpower_configure_measurement_length.html language=enus -->
## TOPIC 00073: rfmxtdscdmavi/rfmxtdscdma_slotpower_configure_measurement_length.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_slotpower_configure_measurement_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_slotpower_configure_measurement_length.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA SlotPower Configure Measurement Length (VI)

RFmxTDSCDMA SlotPower Configure Measurement Length (VI)

Owning Palette:

SlotPower

Configures the measurement length for the SlotPower measurement.

[IMAGE alt='RFmxTDSCDMA SlotPower Configure Measurement Length' src='rfmxtdscdma_slotpower_configure_measurement_length.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Length specifies the measurement length for the SlotPower measurement. This value is expressed in slots. The SlotPower measurement assumes that there is only one active traffic time slot per subframe, and that the position of this active time slot is the same in each subframe. Additionally, it assumes that there are no pilots present in the received signal. NI recommends you set a measurement length as a multiple of the number of slots per subframe, that is a multiple of 7. For example, when you set this property to 28 slots, the SlotPower measurement would report results for the 4 active time slots within the specified measurement length. In this example, 28 slots = 4 subframes. The start of the measurement is determined by the Trigger Type property. Although all the values of the Trigger Type property are supported for this measurement, it is recommended to set the Trigger Type property to Digital Edge with the following options: Digital trigger at the start of active slot, with the Trigger Delay property set to 0 seconds Digital trigger at the start of the subframe, with the Trigger Delay property configured to a value which is equal to the time offset of the active time slot from the start of the subframe The table shows the values of the Trigger Delay property, when you specify the following active slots values: Active Slot Trigger Delay (microseconds) TS0 0 TS1 950 TS2 1625 TS3 2300 TS4 2975 TS5 3650 TS6 4325 If you cannot provide a digital trigger, you can set Trigger Type property to IQ Power Edge to ensure that the measurement starts at the start of an active time slot. To ensure this trigger works properly, NI recommends you complete the following steps: Set the IQ Power Edge Level property to allow triggering for any of the power levels in the active slots Run the RFmx measurement just before generating your signal If you set the Trigger type property to None, the measurement will automatically detect the start of the first burst and measure the traffic slot in that position in every subframe. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 28. The minimum value is 1. |
| Active Slot | Trigger Delay (microseconds) |
| TS0 | 0 |
| TS1 | 950 |
| TS2 | 1625 |
| TS3 | 2300 |
| TS4 | 2975 |
| TS5 | 3650 |
| TS6 | 4325 |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_slotpower_fetch.html language=enus -->
## TOPIC 00074: rfmxtdscdmavi/rfmxtdscdma_slotpower_fetch.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_slotpower_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_slotpower_fetch.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA SlotPower Fetch (VI)

RFmxTDSCDMA SlotPower Fetch (VI)

Owning Palette:

Fetch

Fetches the SlotPower measurement results.

#### RFmxTDSCDMA SlotPower Fetch Powers

Fetches the **Slot Power** and **Slot Power Delta** values.

The SlotPower measurement assumes that there is only one active traffic time slot per subframe, and that the position of this active time slot is the same in each subframe. Additionally, it assumes that there are no pilots present in the received signal.

[IMAGE alt='RFmxTDSCDMA SlotPower Fetch Powers' src='rfmxtdscdma_slotpower_fetch_powers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Slot Power returns an array of mean powers of the active traffic time slots being measured. This value is expressed in dBm. The power of each traffic slot is measured by first excluding the gap period of 12.5 microseconds at the end of the time slot, and then excluding the transient duration of 25 microseconds at the start and the end of the remaining portion of the slot. |
|  | Slot Power Delta returns an array of the power differences between active traffic slots in adjacent subframes. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/rfmxtdscdma_wait_for_measurement_complete.html language=enus -->
## TOPIC 00075: rfmxtdscdmavi/rfmxtdscdma_wait_for_measurement_complete.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/rfmxtdscdma_wait_for_measurement_complete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/rfmxtdscdma_wait_for_measurement_complete.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Wait for Measurement Complete (VI)

RFmxTDSCDMA Wait for Measurement Complete (VI)

Owning Palette:

Utility

Waits for the specified number of seconds for all the measurements to complete.

[IMAGE alt='RFmxTDSCDMA Wait for Measurement Complete' src='rfmxtdscdma_wait_for_measurement_complete.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out returns error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/sem_pal.html language=enus -->
## TOPIC 00076: rfmxtdscdmavi/sem_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/sem_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/sem_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

SEM

SEM

Owning Palette:

Configuration

Use the VIs on this palette to configure spectral emission mask (SEM) measurements. You can use the [RFmxTDSCDMA Property Node](rfmxtdscdma_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA SEM Configure Sweep Time | Configures the sweep time. |
| RFmxTDSCDMA SEM Configure Averaging | Configures averaging for the SEM measurement. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/slotpower_pal.html language=enus -->
## TOPIC 00077: rfmxtdscdmavi/slotpower_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/slotpower_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/slotpower_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

SlotPower

SlotPower

Use the VIs on this palette to configure SlotPower measurements. You can use the [RFmxTDSCDMA Property Node](rfmxtdscdma_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA SlotPower Configure Measurement Length | Configures the measurement length for the SlotPower measurement. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/tdscdma_pal.html language=enus -->
## TOPIC 00078: rfmxtdscdmavi/tdscdma_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/tdscdma_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/tdscdma_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

RFmx TDSCDMA VIs

RFmx TDSCDMA VIs

Use the VIs on this palette to perform TD-SCDMA measurements. You can use the [RFmxTDSCDMA Property Node](rfmxtdscdma_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA Select Measurement | Specifies the measurements that you want to enable. To select multiple measurements, use the Multiple Measurements instance. To select a single measurement, use the Single Measurement instance. |
| RFmxTDSCDMA Initiate | Initiates all enabled measurements. Call this VI after configuring the signal and measurement. |
| RFmxTDSCDMA Property Node | Gets (reads), sets (writes), or resets (sets to default value) RFmxTDSCDMA properties. |

| Subpalette | Description |
| --- | --- |
| Configuration | Use the VIs on this palette to configure RFmx TD-SCDMA measurements. You can use the RFmxTDSCDMA Property Node to configure additional properties. |
| Fetch | Use the VIs on this palette to fetch measurement results and traces. |
| Utility | Use the VIs on this palette to configure RFmx TDSCDMA utilities. |
| Build String | Use the VIs on this palette to create selector strings for configurations and results that require a selector string. |
| Advanced | Use the VIs on this palette to use advanced features. |

<!--NI_TOPIC bundle=rfmx-tdscdma-vi path=rfmxtdscdmavi/utility_pal.html language=enus -->
## TOPIC 00079: rfmxtdscdmavi/utility_pal.html

- bundle_id: `rfmx-tdscdma-vi`
- source_path: `rfmxtdscdmavi/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-vi/raw/resource/enus/rfmxtdscdmavi/utility_pal.html
- document_id: `rfmx-tdscdma-vi`
- page_type: `leaf`
- content_type: ``

Utility

Utility

Owning Palette:

RFmx TDSCDMA VIs

Use the VIs on this palette to configure RFmx TDSCDMA utilities.

| Palette Object | Description |
| --- | --- |
| RFmxTDSCDMA Commit | Commits settings to the hardware. Calling this VI is optional. RFmxTDSCDMA commits settings to the hardware when you call the RFmxTDSCDMA Initiate VI. |
| RFmxTDSCDMA Reset to Default | Resets a signal to the default values. |
| RFmxTDSCDMA Wait for Measurement Complete | Waits for the specified number of seconds for all the measurements to complete. |
| RFmxTDSCDMA Check Measurement Status | Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| RFmxTDSCDMA Get All Named Result Names | Returns the named result names of the signal that you specify in the Selector String parameter. |
