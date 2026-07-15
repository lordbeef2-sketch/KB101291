# NI DOCUMENT BUNDLE: rfmx-evdo-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-evdo-vi start=1 end=83 -->
<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/acp_pal.html language=enus -->
## TOPIC 00001: rfmxevdovi/acp_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/acp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/acp_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

ACP

ACP

Owning Palette:

Configuration

Use the VIs on this palette to configure adjacent channel power (ACP) measurements. You can use the [RFmxEVDO Property Node](rfmxevdo_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO ACP Configure Averaging | Configures averaging for the adjacent channel power (ACP) measurement. |
| RFmxEVDO ACP Configure Sweep Time | Configures the sweep time. |
| RFmxEVDO ACP Configure Number of Offsets | Configures the number of offset channel pairs for the adjacent channel power (ACP) measurement. Channel pairs consist of upper and lower offset channels. |
| RFmxEVDO ACP Configure Offset Power Reference | Configures the power reference of the offset channels in multi-carrier setups. |
| RFmxEVDO ACP Configure Measurement Method | Configures the method for performing the adjacent channel power (ACP) measurement. |
| RFmxEVDO ACP Configure Noise Compensation Enabled | Configures compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| RFmxEVDO ACP Configure RBW Filter | Configures the resolution bandwidth (RBW) filter. |
| RFmxEVDO Build Offset String | Creates the offset string to use as the selector string with adjacent channel power (ACP) and spectral emission mask (SEM) offset configuration or fetch properties and VIs. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/advanced_pal.html language=enus -->
## TOPIC 00002: rfmxevdovi/advanced_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/advanced_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/advanced_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

Advanced

Advanced

Owning Palette:

RFmx EV-DO VIs

Use the VIs on this palette to use advanced features.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO Abort Measurements | Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. These measurements were previously initiated by the RFmxEVDO Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error. |
| RFmxEVDO Analyze2 | Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the Spectrum instance. |
| RFmxEVDO Create Signal Configuration | Creates a new instance of a signal. |
| RFmxEVDO Clone Signal Configuration | Creates a new instance of a signal by copying all the property values from an existing signal instance. |
| RFmxEVDO Delete Signal Configuration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxEVDO Clear Named Result | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxEVDO Clear All Named Results | Clears all results for the signal that you specify in the Selector String parameter. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/build_string_pal.html language=enus -->
## TOPIC 00003: rfmxevdovi/build_string_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/build_string_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/build_string_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

Build String

Build String

Owning Palette:

Fetch

Use the VIs on this palette to create selector strings for configurations and results that require a selector string.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO Build Signal String | Creates a selector string for use with configuration or fetch properties and VIs. |
| RFmxEVDO Build Channel String | Creates the channel string to use as the selector string with the modulation accuracy (ModAcc) channel configuration or fetch properties and VIs. |
| RFmxEVDO Build Carrier String | Creates the carrier string to use as the selector string with the adjacent channel power (ACP), channel power (CHP), and spectral emission mask (SEM) carrier configuration or fetch properties and VIs. |
| RFmxEVDO Build Offset String | Creates the offset string to use as the selector string with adjacent channel power (ACP) and spectral emission mask (SEM) offset configuration or fetch properties and VIs. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/cda_pal.html language=enus -->
## TOPIC 00004: rfmxevdovi/cda_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/cda_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/cda_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

CDA

CDA

Use the VIs on this palette to configure CDA measurement. You can use the RFmxEVDO Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO CDA Configure Synchronization Mode and Interval | Configures the synchronization mode, measurement offset, and measurement length. |
| RFmxEVDO CDA Configure Uplink Measurement Channel | Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. |
| RFmxEVDO CDA Configure Power Unit | Configures the power unit for the code domain power results, except total power. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/chp_pal.html language=enus -->
## TOPIC 00005: rfmxevdovi/chp_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/chp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/chp_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

CHP

CHP

Owning Palette:

Configuration

Use the VIs on this palette to configure channel power (CHP) measurements. You can also use the [RFmxEVDO Property Node](rfmxevdo_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO CHP Configure Averaging | Configures averaging for the channel power (CHP) measurement. |
| RFmxEVDO CHP Configure Sweep Time | Configures the sweep time. |
| RFmxEVDO CHP Configure RBW Filter | Configures the resolution bandwidth (RBW) filter. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/configuration_array_vis_pal.html language=enus -->
## TOPIC 00006: rfmxevdovi/configuration_array_vis_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/configuration_array_vis_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/configuration_array_vis_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

Array VIs

Array VIs

Owning Palette:

Configuration

Use the VIs on this palette to configure measurements requiring an array of properties. You can use the [RFmxEVDO Property Node](rfmxevdo_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO Configure Carrier Frequency (Array) | Configures the carrier frequency of the selected carriers as an offset frequency relative to the center frequency. |
| RFmxEVDO Configure Uplink User Defined Channel (Array) | Configures the array of user defined channels in the EV-DO uplink. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/configuration_pal.html language=enus -->
## TOPIC 00007: rfmxevdovi/configuration_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/configuration_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

Configuration

Configuration

Owning Palette:

RFmx EV-DO VIs

Use the VIs on this palette to configure RFmxEVDO measurements. You can use the [RFmxEVDO Property Node](rfmxevdo_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO Configure RF | Configures the RF properties of the signal specified by the Selector String parameter. |
| RFmxEVDO Configure Frequency | Configures the expected carrier frequency of the RF signal to acquire according to the Center Frequency value in Hz or according to the Channel Number and Band parameters. The signal analyzer tunes to this frequency. |
| RFmxEVDO Configure Reference Level | Configures the reference level. The reference level represents the maximum expected power of an input RF signal. |
| RFmxEVDO Auto Level | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level. |
| RFmxEVDO Configure External Attenuation | Specifies external attenuation to be considered by RFmx EV-DO measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector. |
| RFmxEVDO Configure Trigger | Configures the Reference Trigger to use to acquire the signal. |
| RFmxEVDO Send Software Edge Trigger | Sends a trigger to the device when you use the RFmxEVDO Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. |
| RFmxEVDO Configure Number of Carriers | Configures the number of carriers for the analysis of the EV-DO signal. |
| RFmxEVDO Configure Carrier Frequency | Configures the carrier frequency of the selected carrier as an offset frequency relative to the center frequency. Use "carrier<n>" as the selector string to configure this VI. |
| RFmxEVDO Configure Contiguous Carriers | Configures a number of contiguous carriers in a given band. |
| RFmxEVDO Configure Band Class | Configures the band class to be used for the measurement. |
| RFmxEVDO Configure Physical Layer Subtype | Configures the subtype of the EV-DO signal. |
| RFmxEVDO Configure Uplink Spreading | Configures the spreading of the EV-DO uplink. |
| RFmxEVDO Configure Channel Configuration Mode | Configures RFmx EV-DO to detect the channels automatically or to use a specified channel configuration. |
| RFmxEVDO Configure Uplink Data Modulation Type | Configures RFmx EV-DO to detect the channels automatically or to use a specified data modulation type. |
| RFmxEVDO Configure Uplink Number of Channels | Configures the number of channels in the EV-DO uplink. |
| RFmxEVDO Configure Uplink User Defined Channel | Configures a user defined channel in the EV-DO uplink specified by the selector string. Use "channel<n>" as the selector string to configure this VI. |
| RFmxEVDO Build Carrier String | Creates the carrier string to use as the selector string with the adjacent channel power (ACP), channel power (CHP), and spectral emission mask (SEM) carrier configuration or fetch properties and VIs. |
| RFmxEVDO Build Channel String | Creates the channel string to use as the selector string with the modulation accuracy (ModAcc) channel configuration or fetch properties and VIs. |

| Subpalette | Description |
| --- | --- |
| Array VIs | Use the VIs on this palette to configure measurements requiring an array of properties. You can use the RFmxEVDO Property Node to configure additional properties. |
| ModAcc | Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements. You can use the RFmxEVDO Property Node to configure additional properties. |
| ACP | Use the VIs on this palette to configure adjacent channel power (ACP) measurements. You can use the RFmxEVDO Property Node to configure additional properties. |
| CHP | Use the VIs on this palette to configure channel power (CHP) measurements. You can also use the RFmxEVDO Property Node to configure additional properties. |
| OBW | Use the VIs on this palette to configure occupied bandwidth (OBW) measurements. You can also use the RFmxEVDO Property Node to configure additional properties. |
| SEM | Use the VIs on this palette to configure spectral emission mask (SEM) measurements. You can also use the RFmxEVDO Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/evdo_pal.html language=enus -->
## TOPIC 00008: rfmxevdovi/evdo_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/evdo_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/evdo_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmx EV-DO VIs

RFmx EV-DO VIs

Use the VIs on this palette to perform EV-DO measurements. You can use the [RFmxEVDO Property Node](rfmxevdo_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO Select Measurement | Specifies the measurements that you want to enable. To select a single measurement, use the Measurement instance. To select multiple measurements, use the Multiple Measurements instance. |
| RFmxEVDO Initiate | Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the RFmxEVDO Property Node. To get the status of measurements, use the RFmxEVDO Wait for Measurement Complete VI or Check Measurement Status VI. |
| RFmxEVDO Property Node | Gets (reads), sets (writes), or resets (sets to default value) RFmxEVDO properties. |

| Subpalette | Description |
| --- | --- |
| Configuration | Use the VIs on this palette to configure RFmxEVDO measurements. You can use the RFmxEVDO Property Node to configure additional properties. |
| Fetch | Use the VIs on this palette to fetch measurement results and traces. |
| Utility | Use the VIs on this palette to configure RFmxEVDO utilities. |
| Build String | Use the VIs on this palette to create selector strings for configurations and results that require a selector string. |
| Advanced | Use the VIs on this palette to use advanced features. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/fetch_pal.html language=enus -->
## TOPIC 00009: rfmxevdovi/fetch_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/fetch_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/fetch_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

Fetch

Fetch

Owning Palette:

RFmx EV-DO VIs

Use the VIs on this palette to fetch measurement results and traces.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO ModAcc Fetch | Fetches Modulation Accuracy (ModAcc) measurement results. |
| RFmxEVDO ACP Fetch | Fetches adjacent channel power (ACP) measurement results. |
| RFmxEVDO CHP Fetch | Fetches the channel power (CHP) measurement results. |
| RFmxEVDO OBW Fetch | Fetches occupied bandwidth (OBW) measurement results. |
| RFmxEVDO SEM Fetch | Fetches the spectral emission mask (SEM) measurement results. |

| Subpalette | Description |
| --- | --- |
| Build String | Use the VIs on this palette to create selector strings for configurations and results that require a selector string. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/modacc_pal.html language=enus -->
## TOPIC 00010: rfmxevdovi/modacc_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/modacc_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/modacc_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

ModAcc

ModAcc

Owning Palette:

Configuration

Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements. You can use the [RFmxEVDO Property Node](rfmxevdo_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO ModAcc Configure Multi Carrier Filter Enabled | Enables or disables the multicarrier filter. In multicarrier setups, EVM values are higher than in single carrier setups. The multicarrier filter attempts to minimize interferences from neighboring carriers by applying sharp edges. |
| RFmxEVDO ModAcc Configure Synchronization Mode and Interval | Configures how the modulation accuracy (ModAcc) measurement synchronizes to the signal and the synchronization interval length. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/obw_pal.html language=enus -->
## TOPIC 00011: rfmxevdovi/obw_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/obw_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/obw_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

OBW

OBW

Owning Palette:

Configuration

Use the VIs on this palette to configure occupied bandwidth (OBW) measurements. You can also use the [RFmxEVDO Property Node](rfmxevdo_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO OBW Configure Averaging | Configures averaging for the occupied bandwidth (OBW) measurement. |
| RFmxEVDO OBW Configure Sweep Time | Configures sweep time. |
| RFmxEVDO OBW Configure RBW Filter | Configures the resolution bandwidth (RBW) filter. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_abort_measurements.html language=enus -->
## TOPIC 00012: rfmxevdovi/rfmxevdo_abort_measurements.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_abort_measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_abort_measurements.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Abort Measurements (VI)

RFmxEVDO Abort Measurements (VI)

Owning Palette:

Advanced

Stops acquisition and measurements associated with the signal instance that you specify in the **Selector String** parameter. These measurements were previously initiated by the [RFmxEVDO Initiate](rfmxevdo_initiate.html) VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='RFmxEVDO Abort Measurements' src='rfmxevdo_abort_measurements.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_acp_configure_averaging.html language=enus -->
## TOPIC 00013: rfmxevdovi/rfmxevdo_acp_configure_averaging.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_acp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_acp_configure_averaging.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO ACP Configure Averaging (VI)

RFmxEVDO ACP Configure Averaging (VI)

Owning Palette:

ACP

Configures averaging for the adjacent channel power (ACP) measurement.

[IMAGE alt='RFmxEVDO ACP Configure Averaging' src='rfmxevdo_acp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging of the spectrum for the measurement. The default value is False. False (0) Averaging is not enabled. True (1) Averaging is enabled. |
| False (0) | Averaging is not enabled. |
| True (1) | Averaging is enabled. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_acp_configure_measurement_method.html language=enus -->
## TOPIC 00014: rfmxevdovi/rfmxevdo_acp_configure_measurement_method.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_acp_configure_measurement_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_acp_configure_measurement_method.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO ACP Configure Measurement Method (VI)

RFmxEVDO ACP Configure Measurement Method (VI)

Owning Palette:

ACP

Configures the method for performing the adjacent channel power (ACP) measurement.

[IMAGE alt='RFmxEVDO ACP Configure Measurement Method' src='rfmxevdo_acp_configure_measurement_method.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Method specifies the method for performing the ACP measurement. The default value is Normal. Normal (0) The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. Dynamic Range (1) The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. Sequential FFT (2) The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of each chunk is defined by the defined by the ACP Sequential FFT Size property, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. The accuracy of the results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following properties have limited support when you set the ACP Meas Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads 1 Note For multi-span FFT, the averaging count should be 1. |
| Normal (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| Dynamic Range (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. |
| Sequential FFT (2) | The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of each chunk is defined by the defined by the ACP Sequential FFT Size property, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. The accuracy of the results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following properties have limited support when you set the ACP Meas Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads 1 |
| Property | Supported Value |
| ACP RBW Auto | True |
| ACP RBW Filter Type | FFT Based |
| ACP Averaging Count | >=1 |
| ACP Noise Comp Enabled | False |
| ACP Num Analysis Threads | 1 |
|  | Note For multi-span FFT, the averaging count should be 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_acp_configure_noise_compensation_enabled.html language=enus -->
## TOPIC 00015: rfmxevdovi/rfmxevdo_acp_configure_noise_compensation_enabled.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_acp_configure_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_acp_configure_noise_compensation_enabled.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO ACP Configure Noise Compensation Enabled (VI)

RFmxEVDO ACP Configure Noise Compensation Enabled (VI)

Owning Palette:

ACP

Configures compensation of the channel powers for the inherent noise floor of the signal analyzer.

[IMAGE alt='RFmxEVDO ACP Configure Noise Compensation Enabled' src='rfmxevdo_acp_configure_noise_compensation_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Noise Compensation Enabled specifies whether to enable compensation of the channel powers for the inherent noise floor of the RF signal analyzer. The default value is False. False (0) Disables compensation of the channel powers for the noise floor of the signal analyzer. True (1) Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842 |
| False (0) | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| True (1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842 |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_acp_configure_number_of_offsets.html language=enus -->
## TOPIC 00016: rfmxevdovi/rfmxevdo_acp_configure_number_of_offsets.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_acp_configure_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_acp_configure_number_of_offsets.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO ACP Configure Number of Offsets (VI)

RFmxEVDO ACP Configure Number of Offsets (VI)

Owning Palette:

ACP

Configures the number of offset channel pairs for the adjacent channel power (ACP) measurement. Channel pairs consist of upper and lower offset channels.

[IMAGE alt='RFmxEVDO ACP Configure Number of Offsets' src='rfmxevdo_acp_configure_number_of_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Offsets specifies the number of offset channel pairs. The default value is 2, which consists of 2 upper and 2 lower offset channels. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_acp_configure_offset_power_reference.html language=enus -->
## TOPIC 00017: rfmxevdovi/rfmxevdo_acp_configure_offset_power_reference.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_acp_configure_offset_power_reference.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_acp_configure_offset_power_reference.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO ACP Configure Offset Power Reference (VI)

RFmxEVDO ACP Configure Offset Power Reference (VI)

Owning Palette:

ACP

Configures the power reference of the offset channels in multi-carrier setups.

[IMAGE alt='RFmxEVDO ACP Configure Offset Power Reference' src='rfmxevdo_acp_configure_offset_power_reference.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset Power Reference Carrier specifies how the reference power is selected. The default value is Composite. Closest (0) The measurement uses the carrier power closest to the center frequency of the offset channel as the power reference. Highest (1) The measurement uses the highest measured active carrier power as the power reference. Composite (2) The measurement uses total measured active carrier power as the power reference. Specific (3) The measurement uses the power measured in the carrier with index specified by the Offset Power Reference Specific property as the power reference. For single-carrier configurations, all options have the same behavior. |
| Closest (0) | The measurement uses the carrier power closest to the center frequency of the offset channel as the power reference. |
| Highest (1) | The measurement uses the highest measured active carrier power as the power reference. |
| Composite (2) | The measurement uses total measured active carrier power as the power reference. |
| Specific (3) | The measurement uses the power measured in the carrier with index specified by the Offset Power Reference Specific property as the power reference. |
|  | Offset Power Reference Specific specifies the carrier number that is used as power reference. This parameter only applies if you set the Offset Power Reference Carrier parameter to Specific. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_acp_configure_rbw_filter.html language=enus -->
## TOPIC 00018: rfmxevdovi/rfmxevdo_acp_configure_rbw_filter.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_acp_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_acp_configure_rbw_filter.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO ACP Configure RBW Filter (VI)

RFmxEVDO ACP Configure RBW Filter (VI)

Owning Palette:

ACP

Configures the resolution bandwidth (RBW) filter.

[IMAGE alt='RFmxEVDO ACP Configure RBW Filter' src='rfmxevdo_acp_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement calculates the RBW. The default value is True. True (1) RFmx EV-DO automatically computes the RBW. False (0) The measurement uses the RBW you specify. Refer to the RBW and Sweep Time section in the ACP topic for more details on RBW and sweep time. |
| True (1) | RFmx EV-DO automatically computes the RBW. |
| False (0) | The measurement uses the RBW you specify. |
|  | RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 30 kHz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_acp_configure_sweep_time.html language=enus -->
## TOPIC 00019: rfmxevdovi/rfmxevdo_acp_configure_sweep_time.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_acp_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_acp_configure_sweep_time.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO ACP Configure Sweep Time (VI)

RFmxEVDO ACP Configure Sweep Time (VI)

Owning Palette:

ACP

Configures the sweep time.

[IMAGE alt='RFmxEVDO ACP Configure Sweep Time' src='rfmxevdo_acp_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement calculates the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of 1.67 ms. |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of 1.67 ms. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1.67 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_acp_fetch.html language=enus -->
## TOPIC 00020: rfmxevdovi/rfmxevdo_acp_fetch.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_acp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_acp_fetch.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO ACP Fetch (VI)

RFmxEVDO ACP Fetch (VI)

Owning Palette:

Fetch

Fetches adjacent channel power (ACP) measurement results.

#### RFmxEVDO ACP Fetch Total Carrier Power

Fetches the total carrier power measured by the adjacent channel power (ACP) measurement.

[IMAGE alt='RFmxEVDO ACP Fetch Total Carrier Power' src='rfmxevdo_acp_fetch_total_carrier_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Carrier Power returns the total carrier power. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ACP Fetch Carrier Measurement

Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. 



Use "carrier<n>" as the selector string to read results from this VI.

[IMAGE alt='RFmxEVDO ACP Fetch Carrier Measurement' src='rfmxevdo_acp_fetch_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxEVDO Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns the absolute carrier power. This value is expressed in dBm. |
|  | Relative Power returns the relative carrier power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ACP Fetch Offset Measurement

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier.



Use "offset<n>" as the selector string to read results from this VI.

[IMAGE alt='RFmxEVDO ACP Fetch Offset Measurement' src='rfmxevdo_acp_fetch_offset_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxEVDO Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Lower Relative Power returns the lower offset channel power measured relative to the power of the carrier specified by the ACP Offset Pwr Ref Carrier property. This value is expressed in dB. |
|  | Upper Relative Power returns the upper offset channel power measured relative to the power of the carrier specified by the ACP Offset Pwr Ref Carrier property. This value is expressed in dB. |
|  | Lower Absolute Power returns the lower offset channel power. This value is expressed in dBm. |
|  | Upper Absolute Power returns the upper offset channel power. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ACP Fetch Carrier Measurement (Array)

Returns the absolute and relative powers measured in the carrier channels. The relative powers are measured relative to the integrated power of the power reference carrier.

[IMAGE alt='RFmxEVDO ACP Fetch Carrier Measurement (Array)' src='rfmxevdo_acp_fetch_carrier_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns the array of absolute carrier powers. This value is expressed in dBm. |
|  | Relative Power returns the array of relative carrier powers. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ACP Fetch Offset Measurement (Array)

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier.

[IMAGE alt='RFmxEVDO ACP Fetch Offset Measurement (Array)' src='rfmxevdo_acp_fetch_offset_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Lower Relative Power returns the array of lower offset channel powers measured relative to the power of the carrier specified by the ACP Offset Pwr Ref Carrier property. This value is expressed in dB. |
|  | Upper Relative Power returns the array of upper offset channel powers measured relative to the power of the carrier specified by the ACP Offset Pwr Ref Carrier property. This value is expressed in dB. |
|  | Lower Absolute Power returns the array of lower offset channel powers. |
|  | Upper Absolute Power returns the array of upper offset channel powers. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ACP Fetch Spectrum

Fetches the spectrum used for the adjacent channel power (ACP) measurement.

[IMAGE alt='RFmxEVDO ACP Fetch Spectrum' src='rfmxevdo_acp_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the trace of power levels in the spectral domain. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ACP Fetch Relative Powers Trace

Fetches the relative powers trace for adjacent channel power (ACP) measurement.

[IMAGE alt='RFmxEVDO ACP Fetch Relative Powers Trace' src='rfmxevdo_acp_fetch_relative_powers_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Relative Powers returns the trace of relative powers measured in each channel relative to the power reference carrier. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the relative power measured in each channel relative to power reference carrier. This value is expressed in dB. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the relative power measured in each channel relative to power reference carrier. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ACP Fetch Absolute Powers Trace

Fetches the absolute powers trace for the adjacent channel power (ACP) measurement.

[IMAGE alt='RFmxEVDO ACP Fetch Absolute Powers Trace' src='rfmxevdo_acp_fetch_absolute_powers_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Powers returns the trace of measured integrated power. This value is expressed in dBm. x0 is the start parameter. dx is the delta parameter. y returns the real signal values stored in an array. |
|  | x0 is the start parameter. |
|  | dx is the delta parameter. |
|  | y returns the real signal values stored in an array. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_analyze2.html language=enus -->
## TOPIC 00021: rfmxevdovi/rfmxevdo_analyze2.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_analyze2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_analyze2.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Analyze2 (VI)

RFmxEVDO Analyze2 (VI)

Owning Palette:

Advanced

Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the Spectrum instance.

#### RFmxEVDO Analyze (IQ, 1 Wfm)

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.

Use this VI only if the Recommended Acquisition Type property value is either **IQ** or **IQ or Spectral**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmx EVDO Commit VI. |
| --- | --- |

[IMAGE alt='RFmxEVDO Analyze (IQ 1 Wfm)' src='rfmxevdo_analyze_(iq_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". |
| --- | --- |
|  | IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 specifies the start time of the input Y array. This value is expressed in seconds. dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input Y array. This value is expressed in seconds. |
|  | dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String input parameter for Fetch VIs when using named signal configurations or named results. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO Analyze (Spectrum, 1 Wfm)

Performs the enabled measurements on the spectrum waveform that you specify in the **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.

Use this VI only if the Recommended Acquisition Type property value is either **Spectral** or **IQ or Spectral**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmx EVDO Commit VI. |
| --- | --- |

[IMAGE alt='RFmxEVDO Analyze (Spectrum 1 Wfm)' src='rfmxevdo_analyze_(spectrum_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". |
| --- | --- |
|  | Spectrum specifies the data for a spectrum waveform including the start, delta, and actual values. x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx specifies the frequency interval between data points in the spectrum. y contains the real-value power spectrum. |
|  | x0 specifies the start frequency of the spectrum. This value is expressed in Hz. |
|  | dx specifies the frequency interval between data points in the spectrum. |
|  | y contains the real-value power spectrum. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String input parameter for Fetch VIs when using named signal configurations or named results. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_auto_level.html language=enus -->
## TOPIC 00022: rfmxevdovi/rfmxevdo_auto_level.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_auto_level.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Auto Level (VI)

RFmxEVDO Auto Level (VI)

Owning Palette:

Configuration

Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxEVDO Auto Level VI completes the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device, based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the Auto Level Initial Ref Level property.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxEVDO Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='RFmxEVDO Auto Level' src='rfmxevdo_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Interval specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the RF signal analyzer. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Reference Level returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_build_carrier_string.html language=enus -->
## TOPIC 00023: rfmxevdovi/rfmxevdo_build_carrier_string.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_build_carrier_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_build_carrier_string.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Build Carrier String (VI)

RFmxEVDO Build Carrier String (VI)

Owning Palette:

Configuration

Creates the carrier string to use as the selector string with the adjacent channel power (ACP), channel power (CHP), and spectral emission mask (SEM) carrier configuration or fetch properties and VIs.

Refer to the Selector String topic for information about the string syntax for named signals.

[IMAGE alt='RFmxEVDO Build Carrier String' src='rfmxevdo_build_carrier_string.gif']

|  | Carrier Number specifies the carrier number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string you can use in the Selector String input parameter for Configuration VIs, Fetch VIs, or the RFmxEVDO Initiate VI. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_build_channel_string.html language=enus -->
## TOPIC 00024: rfmxevdovi/rfmxevdo_build_channel_string.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_build_channel_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_build_channel_string.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Build Channel String (VI)

RFmxEVDO Build Channel String (VI)

Owning Palette:

Configuration

Creates the channel string to use as the selector string with the modulation accuracy (ModAcc) channel configuration or fetch properties and VIs.

Refer to the Selector String topic for information about the string syntax for named signals.

[IMAGE alt='RFmxEVDO Build Channel String' src='rfmxevdo_build_channel_string.gif']

|  | Channel Number specifies the channel number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string you can use in the Selector String input parameter for Configuration VIs, Fetch VIs, or the RFmxEVDO Initiate VI. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_build_offset_string.html language=enus -->
## TOPIC 00025: rfmxevdovi/rfmxevdo_build_offset_string.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_build_offset_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_build_offset_string.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Build Offset String (VI)

RFmxEVDO Build Offset String (VI)

Owning Palette:

Build String

Creates the offset string to use as the selector string with adjacent channel power (ACP) and spectral emission mask (SEM) offset configuration or fetch properties and VIs.

Refer to the Selector String topic for information about the string syntax for named signals.

[IMAGE alt='RFmxEVDO Build Offset String' src='rfmxevdo_build_offset_string.gif']

|  | Offset Number specifies the offset number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string you can use in the Selector String input parameter for Configuration VIs, Fetch VIs, or the RFmxEVDO Initiate VI. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_build_signal_string.html language=enus -->
## TOPIC 00026: rfmxevdovi/rfmxevdo_build_signal_string.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_build_signal_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_build_signal_string.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Build Signal String (VI)

RFmxEVDO Build Signal String (VI)

Owning Palette:

Build String

Creates a selector string for use with configuration or fetch properties and VIs.

Refer to the Selector String topic for information about the string syntax for named signals.

[IMAGE alt='RFmxEVDO Build Signal String' src='rfmxevdo_build_signal_string.gif']

|  | Result Name specifies the name of the result when performing overlapped measurements. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string). Examples: "" "result::r1" "r1" |
| --- | --- |
|  | Signal Name specifies the name of the signal when using named signal configurations. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Examples: "" "signal::sig1" "sig1" |
|  | Selector String returns the selector string you can use in the Selector String input parameter for Configuration VIs, Fetch VIs, or other VIs that build selector strings. This string contains the signal and/or result names with their appropriate prefixes. Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_cda_configure_power_unit.html language=enus -->
## TOPIC 00027: rfmxevdovi/rfmxevdo_cda_configure_power_unit.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_cda_configure_power_unit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_cda_configure_power_unit.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO CDA Configure Power Unit (VI)

RFmxEVDO CDA Configure Power Unit (VI)

Owning Palette:

CDA

Configures the power unit for the code domain power results, except total power.

[IMAGE alt='RFmxEVDO CDA Configure Power Unit' src='rfmxevdo_cda_configure_power_unit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Power Unit specifies the measurement unit of the code domain power results. The default value is dB. dB (0) Specifies that the measurement unit is dB. dBm (1) Specifies that the measurement unit is dBm. |
| dB (0) | Specifies that the measurement unit is dB. |
| dBm (1) | Specifies that the measurement unit is dBm. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_cda_configure_synchronization_mode_and_interval.html language=enus -->
## TOPIC 00028: rfmxevdovi/rfmxevdo_cda_configure_synchronization_mode_and_interval.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_cda_configure_synchronization_mode_and_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_cda_configure_synchronization_mode_and_interval.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO CDA Configure Synchronization Mode and Interval (VI)

RFmxEVDO CDA Configure Synchronization Mode and Interval (VI)

Owning Palette:

CDA

Configures the synchronization mode, measurement offset, and measurement length.

[IMAGE alt='RFmxEVDO CDA Configure Synchronization Mode and Interval' src='rfmxevdo_cda_configure_synchronization_mode_and_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Mode specifies whether the measurement is performed from the frame, slot, or symbol boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots specified by the CDA Meas Length property starting at CDA Meas Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots specified by CDA Meas Length number of slots, starting at CDA Meas Offset slots from the slot boundary. Arbitrary (2) The symbol boundary is detected and the measurement is performed over the number of slots specified by the CDA Meas Length property, starting at CDA Meas Offset slots from the symbol boundary. |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the CDA Meas Length property starting at CDA Meas Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots specified by CDA Meas Length number of slots, starting at CDA Meas Offset slots from the slot boundary. |
| Arbitrary (2) | The symbol boundary is detected and the measurement is performed over the number of slots specified by the CDA Meas Length property, starting at CDA Meas Offset slots from the symbol boundary. |
|  | Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. Valid values are [0,15]. The sum of CDA Meas Offset and CDA Meas Length is less than or equal to 16. |
|  | Measurement Length specifies the duration of the CDA measurement. This value is expressed in slots. The default value is 1. Valid values are [1, 16]. The sum of the CDA Meas Offset and CDA Meas Length is less than or equal to 16. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_cda_configure_uplink_measurement_channel.html language=enus -->
## TOPIC 00029: rfmxevdovi/rfmxevdo_cda_configure_uplink_measurement_channel.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_cda_configure_uplink_measurement_channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_cda_configure_uplink_measurement_channel.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO CDA Configure Uplink Measurement Channel (VI)

RFmxEVDO CDA Configure Uplink Measurement Channel (VI)

Owning Palette:

CDA

Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

[IMAGE alt='RFmxEVDO CDA Configure Uplink Measurement Channel' src='rfmxevdo_cda_configure_uplink_measurement_channel.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Walsh Code Length specifies the Walsh code length of the channel, subject to channel-specific analysis. The default value is 16. Valid values are 2, 4, 8, 16, and 32. |
|  | Walsh Code Number specifies the Walsh code number of the channel, subject to channel-specific analysis. The default value is 0. The maximum value is 31. |
|  | Branch specifies the Walsh branch of the channel, subject to channel-specific analysis. The default value is I. I (0) Specifies the in-phase branch. Q (1) Specifies the quadrature branch. I and Q (2) Specifies the in-phase and quadrature branch. |
| I (0) | Specifies the in-phase branch. |
| Q (1) | Specifies the quadrature branch. |
| I and Q (2) | Specifies the in-phase and quadrature branch. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_cda_fetch.html language=enus -->
## TOPIC 00030: rfmxevdovi/rfmxevdo_cda_fetch.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_cda_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_cda_fetch.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO CDA Fetch (VI)

RFmxEVDO CDA Fetch (VI)

Fetches CDA measurement results.

#### RFmxEVDO CDA Fetch IQ Impairments

Fetches the measured I/Q impairments.

[IMAGE alt='RFmxEVDO CDA Fetch IQ Impairments' src='rfmxevdo_cda_fetch_iq_impairments.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | I/Q Origin Offset returns the I/Q origin offset. This value is expressed in dB. |
|  | I/Q Gain Imbalance returns the I/Q gain imbalance. This value is expressed in dB. |
|  | I/Q Quadrature Error returns the I/Q quadrature error. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO CDA Fetch Uplink Symbol EVM

Fetches the modulation accuracy related measures for the configured measurement channel.

[IMAGE alt='RFmxEVDO CDA Fetch Uplink Symbol EVM' src='rfmxevdo_cda_fetch_uplink_symbol_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS Symbol EVM returns the RMS ymbol EVM of the configured measurement channel. This value is expressed as a percentage. |
|  | Peak Symbol EVM returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. |
|  | RMS Symbol Magnitude Error returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. |
|  | RMS Symbol Phase Error returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. |
|  | Mean Symbol Power returns the mean symbol power of the configured measurement channel. This value is expressed in dB or dBm. |
|  | Frequency Error returns the frequency error. This value is expressed in Hz. |
|  | Chip Rate Error returns the chip rate error. This value is expressed in ppm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO CDA Fetch Uplink Code Domain Power

Fetches the scalar code domain power results.

[IMAGE alt='RFmxEVDO CDA Fetch Uplink Code Domain Power' src='rfmxevdo_cda_fetch_uplink_code_domain_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Power returns the mean power of the received signal. This value is expressed in dBm. |
|  | Total Active Power returns the sum of the powers of all active code channels. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
|  | Mean Inactive Power returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. The default value is 0. |
|  | Mean Active Power returns the average power of all active code channels. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
|  | Peak Active Power returns the maximum power among all active code channels. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
|  | Peak Inactive Power returns the largest measured code power among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO CDA Fetch Uplink Code Domain I and Q Power

Fetches the I and Q mean active powers and the I and Q peak inactive powers.

[IMAGE alt='RFmxEVDO CDA Fetch Uplink Code Domain I and Q Power' src='rfmxevdo_cda_fetch_uplink_code_domain_i_and_q_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | I Mean Active Power returns the average power of all active code channels measured on the I-branch. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
|  | Q Mean Active Power returns the average power of all active code channels measured on the Q-branch. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
|  | I Peak Inactive Power returns the largest measured code power among the set of inactive channels on the I-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
|  | Q Peak Inactive Power returns the largest measured code power among the set of inactive channels on the Q-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO CDA Fetch Uplink Symbol EVM Trace

Returns the symbol EVM trace of the configured measurement channel.

[IMAGE alt='RFmxEVDO CDA Fetch Uplink Symbol EVM Trace' src='rfmxevdo_cda_fetch_uplink_symbol_evm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Symbol EVM Symbol EVM returns the trace of symbol EVM. This value is expressed as a percentage. x0 is the start parameter. dx is the delta parameter. y returns the real signal values stored in an array. |
|  | x0 is the start parameter. |
|  | dx is the delta parameter. |
|  | y returns the real signal values stored in an array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO CDA Fetch Uplink Symbol Magnitude Error Trace

Returns the symbol magnitude error trace of the configured measurement channel.

[IMAGE alt='RFmxEVDO CDA Fetch Uplink Symbol Magnitude Error Trace' src='rfmxevdo_cda_fetch_uplink_symbol_magnitude_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Symbol Magnitude Error returns the trace of symbol magnitude error.. This value is expressed as a percentage. x0 is the start parameter. dx is the delta parameter. y returns the real signal values stored in an array. |
|  | x0 is the start parameter. |
|  | dx is the delta parameter. |
|  | y returns the real signal values stored in an array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO CDA Fetch Uplink Symbol Phase Error Trace

Fetches the symbol phase error trace of the configured measurement channel.

[IMAGE alt='RFmxEVDO CDA Fetch Uplink Symbol Phase Error Trace' src='rfmxevdo_cda_fetch_uplink_symbol_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Symbol Phase Error returns the array of RMS symbol phase errors of the configured measurement channel. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO CDA Fetch Uplink Code Domain I and Q Power Trace

Fetches the I and Q code power traces measured in the code domain of the base spreading factor.

[IMAGE alt='RFmxEVDO CDA Fetch Uplink Code Domain I and Q Power Trace' src='rfmxevdo_cda_fetch_uplink_code_domain_i_and_q_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | I Code Domain Powers returns the I code domain power traces. This value is expressed in dB or dBm. |
|  | Q Code Domain Powers returns the Q code domain power traces. This value is expressed in dB or dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO CDA Fetch Uplink Symbol Power Trace

Returns the symbol power trace of the configured measurement channel.

[IMAGE alt='RFmxEVDO CDA Fetch Uplink Symbol Power Trace' src='rfmxevdo_cda_fetch_uplink_symbol_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Symbol Powers returns the trace of measured symbol powers. This value is expressed in dBm. x0 is the start parameter. dx is the delta parameter. y returns the real signal values stored in an array. |
|  | x0 is the start parameter. |
|  | dx is the delta parameter. |
|  | y returns the real signal values stored in an array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO CDA Fetch Uplink Symbol Constellation Trace

Fetches the symbol constellation trace of the configured measurement channel.

[IMAGE alt='RFmxEVDO CDA Fetch Uplink Symbol Constellation Trace' src='rfmxevdo_cda_fetch_uplink_symbol_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Symbol Constellation returns the complex signal values stored in an array. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_check_measurement_status.html language=enus -->
## TOPIC 00031: rfmxevdovi/rfmxevdo_check_measurement_status.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_check_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_check_measurement_status.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Check Measurement Status (VI)

RFmxEVDO Check Measurement Status (VI)

Owning Palette:

Utility

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='RFmxEVDO Check Measurement Status' src='rfmxevdo_check_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | done? indicates whether the measurement is complete. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_chp_configure_averaging.html language=enus -->
## TOPIC 00032: rfmxevdovi/rfmxevdo_chp_configure_averaging.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_chp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_chp_configure_averaging.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO CHP Configure Averaging (VI)

RFmxEVDO CHP Configure Averaging (VI)

Owning Palette:

CHP

Configures averaging for the channel power (CHP) measurement.

[IMAGE alt='RFmxEVDO CHP Configure Averaging' src='rfmxevdo_chp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) Averaging is not enabled. True (1) Averaging is enabled. |
| False (0) | Averaging is not enabled. |
| True (1) | Averaging is enabled. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_chp_configure_rbw_filter.html language=enus -->
## TOPIC 00033: rfmxevdovi/rfmxevdo_chp_configure_rbw_filter.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_chp_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_chp_configure_rbw_filter.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO CHP Configure RBW Filter (VI)

RFmxEVDO CHP Configure RBW Filter (VI)

Owning Palette:

CHP

Configures the resolution bandwidth (RBW) filter.

[IMAGE alt='RFmxEVDO CHP Configure RBW Filter' src='rfmxevdo_chp_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement calculates the RBW. The default value is True True (1) RFmx EV-DO automatically computes the RBW. False (0) The measurement uses the RBW you specify. Refer to the RBW and Sweep Time section in the CHP topic for more details on RBW and sweep time. |
| True (1) | RFmx EV-DO automatically computes the RBW. |
| False (0) | The measurement uses the RBW you specify. |
|  | RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 30 kHz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_chp_configure_sweep_time.html language=enus -->
## TOPIC 00034: rfmxevdovi/rfmxevdo_chp_configure_sweep_time.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_chp_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_chp_configure_sweep_time.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO CHP Configure Sweep Time (VI)

RFmxEVDO CHP Configure Sweep Time (VI)

Owning Palette:

CHP

Configures the sweep time.

[IMAGE alt='RFmxEVDO CHP Configure Sweep Time' src='rfmxevdo_chp_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement calculates the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of 1.67 ms. |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of 1.67 ms. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1.67 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_chp_fetch.html language=enus -->
## TOPIC 00035: rfmxevdovi/rfmxevdo_chp_fetch.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_chp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_chp_fetch.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO CHP Fetch (VI)

RFmxEVDO CHP Fetch (VI)

Owning Palette:

Fetch

Fetches the channel power (CHP) measurement results.

#### RFmxEVDO CHP Fetch Total Carrier Power

Fetches the total carrier power measured by the channel power (CHP) measurement.

[IMAGE alt='RFmxEVDO CHP Fetch Total Carrier Power' src='rfmxevdo_chp_fetch_total_carrier_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Carrier Power returns the total carrier power. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO CHP Fetch Carrier Measurement

Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. Use "carrier<n>" as the selector string to read results from this VI.

[IMAGE alt='RFmxEVDO CHP Fetch Carrier Measurement' src='rfmxevdo_chp_fetch_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxEVDO Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Carrier Absolute Power returns the absolute carrier power of the selected carrier. This value is expressed in dBm. |
|  | Carrier Relative Power returns the relative carrier power of the selected carrier. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO CHP Fetch Carrier Measurement (Array)

Returns the array of carrier measurements of the channel power (CHP) measurement.

[IMAGE alt='RFmxEVDO CHP Fetch Carrier Measurement (Array)' src='rfmxevdo_chp_fetch_carrier_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Carrier Absolute Power returns the array of absolute carrier powers. This value is expressed in dBm. |
|  | Carrier Relative Power returns the array of relative carrier powers. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO CHP Fetch Spectrum

Fetches the spectrum used for the channel power (CHP) measurement.

[IMAGE alt='RFmxEVDO CHP Fetch Spectrum' src='rfmxevdo_chp_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the trace of power levels in the spectral domain. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_clear_all_named_results.html language=enus -->
## TOPIC 00036: rfmxevdovi/rfmxevdo_clear_all_named_results.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_clear_all_named_results.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_clear_all_named_results.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Clear All Named Results (VI)

RFmxEVDO Clear All Named Results (VI)

Owning Palette:

Advanced

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxEVDO Clear All Named Results' src='rfmxevdo_clear_all_named_results.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_clear_named_result.html language=enus -->
## TOPIC 00037: rfmxevdovi/rfmxevdo_clear_named_result.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_clear_named_result.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_clear_named_result.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Clear Named Result (VI)

RFmxEVDO Clear Named Result (VI)

Owning Palette:

Advanced

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='RFmxEVDO Clear Named Result' src='rfmxevdo_clear_named_result.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_clone_signal_configuration.html language=enus -->
## TOPIC 00038: rfmxevdovi/rfmxevdo_clone_signal_configuration.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_clone_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_clone_signal_configuration.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Clone Signal Configuration (VI)

RFmxEVDO Clone Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='RFmxEVDO Clone Signal Configuration' src='rfmxevdo_clone_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | New Signal Name specifies the name of the new signal. This input accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
|  | Old Signal Name specifies the name of the existing signal. This input accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string you can use in the Selector String input parameter for Configuration VIs, Fetch VIs, or the RFmxEVDO Initiate VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_commit.html language=enus -->
## TOPIC 00039: rfmxevdovi/rfmxevdo_commit.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_commit.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Commit (VI)

RFmxEVDO Commit (VI)

Owning Palette:

Utility

Commits settings to the hardware. Calling this VI is optional. RFmxEVDO commits settings to the hardware when you call the [RFmxEVDO Initiate](rfmxevdo_initiate.html) VI.

[IMAGE alt='RFmxEVDO Commit' src='rfmxevdo_commit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_band_class.html language=enus -->
## TOPIC 00040: rfmxevdovi/rfmxevdo_configure_band_class.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_band_class.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_band_class.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Band Class (VI)

RFmxEVDO Configure Band Class (VI)

Owning Palette:

Configuration

Configures the band class to be used for the measurement.

[IMAGE alt='RFmxEVDO Configure Band Class' src='rfmxevdo_configure_band_class.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Band Class specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. Valid values range between 0 and 15, inclusive. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_carrier_frequency.html language=enus -->
## TOPIC 00041: rfmxevdovi/rfmxevdo_configure_carrier_frequency.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_carrier_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_carrier_frequency.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Carrier Frequency (VI)

RFmxEVDO Configure Carrier Frequency (VI)

Owning Palette:

Configuration

Configures the carrier frequency of the selected carrier as an offset frequency relative to the center frequency. Use "carrier<n>" as the selector string to configure this VI.

Configure the center frequency by using the [RFmxEVDO Configure Frequency](rfmxevdo_configure_frequency.html) VI. If the number of carriers is greater than 1, configure the number of carriers using the [RFmxEVDO Configure Number of Carriers](rfmxevdo_configure_number_of_carriers.html) VI.

[IMAGE alt='RFmxEVDO Configure Carrier Frequency' src='rfmxevdo_configure_carrier_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Carrier Frequency specifies the carrier frequency. This value is expressed in Hz. |
|  | Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0" (empty string). Examples: "carrier0" "signal::sig1/carrier0" You can use the RFmxEVDO Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_carrier_frequency_(array).html language=enus -->
## TOPIC 00042: rfmxevdovi/rfmxevdo_configure_carrier_frequency_(array).html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_carrier_frequency_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_carrier_frequency_(array).html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Carrier Frequency (Array) (VI)

RFmxEVDO Configure Carrier Frequency (Array) (VI)

Owning Palette:

Array VIs

Configures the carrier frequency of the selected carriers as an offset frequency relative to the center frequency.

Configure the center frequency by using the [RFmxEVDO Configure Frequency](rfmxevdo_configure_frequency.html) VI. Configure the number of carriers using the [RFmxEVDO Configure Number of Carriers](rfmxevdo_configure_number_of_carriers.html) VI.

[IMAGE alt='RFmxEVDO Configure Carrier Frequency (Array)' src='rfmxevdo_configure_carrier_frequency_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Carrier Frequency specifies the carrier frequency. This value is expressed in Hz. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_channel_configuration_mode.html language=enus -->
## TOPIC 00043: rfmxevdovi/rfmxevdo_configure_channel_configuration_mode.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_channel_configuration_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_channel_configuration_mode.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Channel Configuration Mode (VI)

RFmxEVDO Configure Channel Configuration Mode (VI)

Owning Palette:

Configuration

Configures RFmx EV-DO to detect the channels automatically or to use a specified channel configuration.

[IMAGE alt='RFmxEVDO Configure Channel Configuration Mode' src='rfmxevdo_configure_channel_configuration_mode.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | The Channel Configuration Mode specifies how the channel configuration is derived. Auto Detect (0) RFmx EV-DO detects the channels automatically. User Defined (1) Channel configuration is defined manually. This mode increases measurement speed because no time is spent on channel detection. |
| Auto Detect (0) | RFmx EV-DO detects the channels automatically. |
| User Defined (1) | Channel configuration is defined manually. This mode increases measurement speed because no time is spent on channel detection. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_contiguous_carriers.html language=enus -->
## TOPIC 00044: rfmxevdovi/rfmxevdo_configure_contiguous_carriers.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_contiguous_carriers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_contiguous_carriers.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Contiguous Carriers (VI)

RFmxEVDO Configure Contiguous Carriers (VI)

Owning Palette:

Configuration

Configures a number of contiguous carriers in a given band.

[IMAGE alt='RFmxEVDO Configure Contiguous Carriers' src='rfmxevdo_configure_contiguous_carriers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Carriers specifies the number of carriers in the signal. The default value is 1. |
|  | Carrier at Center Frequency specifies the carrier at the center frequency. |
|  | Band Class specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. Valid values range between 0 and 15, inclusive. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_external_attenuation.html language=enus -->
## TOPIC 00045: rfmxevdovi/rfmxevdo_configure_external_attenuation.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_external_attenuation.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure External Attenuation (VI)

RFmxEVDO Configure External Attenuation (VI)

Owning Palette:

Configuration

Specifies external attenuation to be considered by RFmx EV-DO measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector.

[IMAGE alt='RFmxEVDO Configure External Attenuation' src='rfmxevdo_configure_external_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | External Attenuation specifies external attenuation to be considered by RFmx EV-DO measurements, such as the attenuation of a switch or cable connected to the RF signal analyzer RF IN connector. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_frequency.html language=enus -->
## TOPIC 00046: rfmxevdovi/rfmxevdo_configure_frequency.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_frequency.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Frequency (VI)

RFmxEVDO Configure Frequency (VI)

Owning Palette:

Configuration

Configures the expected carrier frequency of the RF signal to acquire according to the **Center Frequency** value in Hz or according to the **Channel Number** and **Band** parameters. The signal analyzer tunes to this frequency.

#### RFmxEVDO Configure Frequency (Channel Number)

Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency.

[IMAGE alt='RFmxEVDO Configure Frequency (Channel Number)' src='rfmxevdo_configure_frequency_(channel_number).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Link Direction specifies which direction the frequency is calculated. Currently, only Uplink is supported. Uplink (1) The frequency is calculated in the reverse link direction, also know as the uplink direction. |
| Uplink (1) | The frequency is calculated in the reverse link direction, also know as the uplink direction. |
|  | Band Class specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. Valid values range between 0 and 15, inclusive. |
|  | Channel Number is the absolute RF channel number. The valid range for this parameter depends on the value you specify for the Band parameter. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO Configure Frequency (Frequency)

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

[IMAGE alt='RFmxEVDO Configure Frequency (Frequency)' src='rfmxevdo_configure_frequency_(frequency).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the expected carrier frequency of the RF signal to acquire. This value is expressed in Hz. The RF signal analyzer tunes to this frequency. The default of this parameter is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_number_of_carriers.html language=enus -->
## TOPIC 00047: rfmxevdovi/rfmxevdo_configure_number_of_carriers.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_number_of_carriers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_number_of_carriers.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Number of Carriers (VI)

RFmxEVDO Configure Number of Carriers (VI)

Owning Palette:

Configuration

Configures the number of carriers for the analysis of the EV-DO signal.

[IMAGE alt='RFmxEVDO Configure Number of Carriers' src='rfmxevdo_configure_number_of_carriers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Carriers specifies the number of carriers in the signal. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_physical_layer_subtype.html language=enus -->
## TOPIC 00048: rfmxevdovi/rfmxevdo_configure_physical_layer_subtype.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_physical_layer_subtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_physical_layer_subtype.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Physical Layer Subtype (VI)

RFmxEVDO Configure Physical Layer Subtype (VI)

Owning Palette:

Configuration

Configures the subtype of the EV-DO signal.

[IMAGE alt='RFmxEVDO Configure Physical Layer Subtype' src='rfmxevdo_configure_physical_layer_subtype.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Physical Layer Subtype specifies the EV-DO physical layer subtype. The default value is 0, 1. 0,1 (0) Specifies subtype 0, 1. 3GPP2 C.S0024-B v3.0 defines this subtype in 10 DEFAULT (SUBTYPE 0) AND SUBTYPE 1 PHYSICAL LAYER PROTOCOL. 2 (1) Specifies subtype 2. 3GPP2 C.S0024-B v3.0 defines this subtype in 11 SUBTYPE 2 PHYSICAL LAYER. 3 (2) Specifies subtype 3. 3GPP2 C.S0024-B v3.0 defines this subtype in 12 SUBTYPE 3 PHYSICAL LAYER. |
| 0,1 (0) | Specifies subtype 0, 1. 3GPP2 C.S0024-B v3.0 defines this subtype in 10 DEFAULT (SUBTYPE 0) AND SUBTYPE 1 PHYSICAL LAYER PROTOCOL. |
| 2 (1) | Specifies subtype 2. 3GPP2 C.S0024-B v3.0 defines this subtype in 11 SUBTYPE 2 PHYSICAL LAYER. |
| 3 (2) | Specifies subtype 3. 3GPP2 C.S0024-B v3.0 defines this subtype in 12 SUBTYPE 3 PHYSICAL LAYER. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_reference_level.html language=enus -->
## TOPIC 00049: rfmxevdovi/rfmxevdo_configure_reference_level.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_reference_level.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Reference Level (VI)

RFmxEVDO Configure Reference Level (VI)

Owning Palette:

Configuration

Configures the reference level. The reference level represents the maximum expected power of an input RF signal.

[IMAGE alt='RFmxEVDO Configure Reference Level' src='rfmxevdo_configure_reference_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Level specifies the reference level which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_rf.html language=enus -->
## TOPIC 00050: rfmxevdovi/rfmxevdo_configure_rf.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_rf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_rf.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure RF (VI)

RFmxEVDO Configure RF (VI)

Owning Palette:

Configuration

Configures the RF properties of the signal specified by the **Selector String** parameter.

[IMAGE alt='RFmxEVDO Configure RF' src='rfmxevdo_configure_rf.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the expected carrier frequency of the RF signal to acquire. This value is expressed in Hz. The RF signal analyzer tunes to this frequency. The default of this parameter is hardware dependent. |
|  | Reference Level specifies the reference level which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent. |
|  | External Attenuation specifies external attenuation to be considered by RFmx EV-DO measurements, such as the attenuation of a switch or cable connected to the RF signal analyzer RF IN connector. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_trigger.html language=enus -->
## TOPIC 00051: rfmxevdovi/rfmxevdo_configure_trigger.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_trigger.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Trigger (VI)

RFmxEVDO Configure Trigger (VI)

Owning Palette:

Configuration

Configures the Reference Trigger to use to acquire the signal.

#### RFmxEVDO Configure IQ Power Edge Trigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

To trigger on burst signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts but large enough to ignore power changes within a burst.

[IMAGE alt='RFmxEVDO Configure IQ Power Edge Trigger' src='rfmxevdo_configure_iq_power_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | IQ Power Edge Source specifies the channel from which the device monitors the trigger. The default of this parameter is hardware dependent. |
|  | IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
|  | IQ Power Edge Level specifies the threshold above or below which the RF signal analyzer triggers. The value is expressed in dB if IQ Power Edge Level Type is set to Relative; and is expressed in dBm if IQ Power Edge Level Type is set to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this parameter is hardware dependent. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Minimum Quiet Time Mode specifies whether the measurement calculates the minimum quiet time used for triggering. The default value is Auto. Manual (0) The measurement uses the minimum quiet time value you specify. Auto (1) The measurement calculates the minimum quiet time used for triggering. |
| Manual (0) | The measurement uses the minimum quiet time value you specify. |
| Auto (1) | The measurement calculates the minimum quiet time used for triggering. |
|  | Minimum Quiet Time specifies the duration for which the signal must be quiet before the RF signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default of this parameter is hardware dependent. |
|  | IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. The IQ Power Edge Level Type parameter is used only when you set the Trigger Type property to IQ Power Edge. Relative (0) The IQ Power Edge Level is relative to the reference level. Absolute (1) The IQ Power Edge Level specifies the absolute power. |
| Relative (0) | The IQ Power Edge Level is relative to the reference level. |
| Absolute (1) | The IQ Power Edge Level specifies the absolute power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |

#### RFmxEVDO Configure Software Edge Trigger

Configures the device to wait for a software trigger to mark a reference point within the record.

[IMAGE alt='RFmxEVDO Configure Software Edge Trigger' src='rfmxevdo_configure_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO Configure Digital Edge Trigger

Configures the device to wait for a software trigger to mark a reference point within the record.

[IMAGE alt='RFmxEVDO Configure Digital Edge Trigger' src='rfmxevdo_configure_digital_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Digital Edge Source specifies the source terminal for the digital edge trigger. The default of this parameter is hardware dependent. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. |
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
|  | Digital Edge specifies the trigger edge to detect. The default value is Rising Edge. Rising Edge (0) RFmx EV-DO detects a rising edge. Falling Edge (1) RFmx EV-DO detects a falling edge. |
| Rising Edge (0) | RFmx EV-DO detects a rising edge. |
| Falling Edge (1) | RFmx EV-DO detects a falling edge. |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO Disable Trigger

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='RFmxEVDO Disable Trigger' src='rfmxevdo_disable_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_uplink_data_modulation_type.html language=enus -->
## TOPIC 00052: rfmxevdovi/rfmxevdo_configure_uplink_data_modulation_type.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_uplink_data_modulation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_uplink_data_modulation_type.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Uplink Data Modulation Type (VI)

RFmxEVDO Configure Uplink Data Modulation Type (VI)

Owning Palette:

Configuration

Configures RFmx EV-DO to detect the channels automatically or to use a specified data modulation type.

[IMAGE alt='RFmxEVDO Configure Uplink Data Modulation Type' src='rfmxevdo_configure_uplink_data_modulation_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Uplink Data Modulation Type specifies the modulation type of the uplink data channel. The default value is Auto. Auto (0) RFmx EV-DO automatically determines the modulation type. Data Channel Absent (1) The specified uplink data channel is absent. B4 (2) The specified uplink data channel uses binary phase shift keying (BPSK) with the Walsh function W(4,2). Q4 (3) The specified uplink data channel uses quadrature phase shift keying (QPSK) with the Walsh function W(4,2). Q2 (4) The specified uplink data channel uses QPSK with the Walsh function W(2,1). Q4Q2 (5) The specified uplink data channel uses QPSK with the Walsh functions W(4,2) and W(2,1). E4E2 (6) The specified uplink data channel uses 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |
| Auto (0) | RFmx EV-DO automatically determines the modulation type. |
| Data Channel Absent (1) | The specified uplink data channel is absent. |
| B4 (2) | The specified uplink data channel uses binary phase shift keying (BPSK) with the Walsh function W(4,2). |
| Q4 (3) | The specified uplink data channel uses quadrature phase shift keying (QPSK) with the Walsh function W(4,2). |
| Q2 (4) | The specified uplink data channel uses QPSK with the Walsh function W(2,1). |
| Q4Q2 (5) | The specified uplink data channel uses QPSK with the Walsh functions W(4,2) and W(2,1). |
| E4E2 (6) | The specified uplink data channel uses 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_uplink_number_of_channels.html language=enus -->
## TOPIC 00053: rfmxevdovi/rfmxevdo_configure_uplink_number_of_channels.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_uplink_number_of_channels.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_uplink_number_of_channels.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Uplink Number of Channels (VI)

RFmxEVDO Configure Uplink Number of Channels (VI)

Owning Palette:

Configuration

Configures the number of channels in the EV-DO uplink.

[IMAGE alt='RFmxEVDO Configure Uplink Number of Channels' src='rfmxevdo_configure_uplink_number_of_channels.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Uplink Number of Channels specifies the number of user-defined channels. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_uplink_spreading.html language=enus -->
## TOPIC 00054: rfmxevdovi/rfmxevdo_configure_uplink_spreading.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_uplink_spreading.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_uplink_spreading.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Uplink Spreading (VI)

RFmxEVDO Configure Uplink Spreading (VI)

Owning Palette:

Configuration

Configures the spreading of the EV-DO uplink.

[IMAGE alt='RFmxEVDO Configure Uplink Spreading' src='rfmxevdo_configure_uplink_spreading.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Uplink Spreading I mask specifies the long code mask of the in-phase (I) channel. The default value is 0x0. |
|  | Uplink Spreading Q mask specifies the long code mask of the quadrature (Q) channel. The default value is 0x0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_uplink_user_defined_channel.html language=enus -->
## TOPIC 00055: rfmxevdovi/rfmxevdo_configure_uplink_user_defined_channel.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_uplink_user_defined_channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_uplink_user_defined_channel.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Uplink User Defined Channel (VI)

RFmxEVDO Configure Uplink User Defined Channel (VI)

Owning Palette:

Configuration

Configures a user defined channel in the EV-DO uplink specified by the selector string. Use "channel<n>" as the selector string to configure this VI.

[IMAGE alt='RFmxEVDO Configure Uplink User Defined Channel' src='rfmxevdo_configure_uplink_user_defined_channel.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Uplink Walsh Code Length specifies the Walsh code length of a specific user-defined channel. The default value is 64. |
|  | Uplink Walsh Code Number specifies the Walsh code number of a specific user-defined channel. The default value is 0. |
|  | Uplink Branch specifies the quadrature branch on which a specific user-defined channel is mapped. The default value is I. I (0) Specifies the in-phase component. Q (1) Specifies the quadrature component. I and Q (2) Specifies both the in-phase component and the quadrature component. |
| I (0) | Specifies the in-phase component. |
| Q (1) | Specifies the quadrature component. |
| I and Q (2) | Specifies both the in-phase component and the quadrature component. |
|  | Selector String specifies a selector string comprising of the signal name and channel number. If you do not specify the signal name, the default signal instance is used. The default value is "channel0". Examples: "channel0" "signal::sig1/channel0" You can use the RFmxEVDO Build Channel String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_configure_uplink_user_defined_channel_(array).html language=enus -->
## TOPIC 00056: rfmxevdovi/rfmxevdo_configure_uplink_user_defined_channel_(array).html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_configure_uplink_user_defined_channel_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_configure_uplink_user_defined_channel_(array).html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Configure Uplink User Defined Channel (Array) (VI)

RFmxEVDO Configure Uplink User Defined Channel (Array) (VI)

Owning Palette:

Array VIs

Configures the array of user defined channels in the EV-DO uplink.

[IMAGE alt='RFmxEVDO Configure Uplink User Defined Channel (Array)' src='rfmxevdo_configure_uplink_user_defined_channel_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Uplink Walsh Code Length specifies the Walsh code length of a specific user-defined channel. The default value is 64. |
|  | Uplink Walsh Code Number specifies the Walsh code number of a specific user-defined channel. The default value is 0. |
|  | Uplink Branch specifies the quadrature branch on which a specific user-defined channel is mapped. The default value is I. I (0) Specifies the in-phase component. Q (1) Specifies the quadrature component. I and Q (2) Specifies both the in-phase component and the quadrature component. |
| I (0) | Specifies the in-phase component. |
| Q (1) | Specifies the quadrature component. |
| I and Q (2) | Specifies both the in-phase component and the quadrature component. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_create_signal_configuration.html language=enus -->
## TOPIC 00057: rfmxevdovi/rfmxevdo_create_signal_configuration.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_create_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_create_signal_configuration.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Create Signal Configuration (VI)

RFmxEVDO Create Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal.

[IMAGE alt='RFmxEVDO Create Signal Configuration' src='rfmxevdo_create_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string you can use in the Selector String input parameter for Configuration VIs, Fetch VIs, or the RFmxEVDO Initiate VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_delete_signal_configuration.html language=enus -->
## TOPIC 00058: rfmxevdovi/rfmxevdo_delete_signal_configuration.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_delete_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_delete_signal_configuration.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Delete Signal Configuration (VI)

RFmxEVDO Delete Signal Configuration (VI)

Owning Palette:

Advanced

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='RFmxEVDO Delete Signal Configuration' src='rfmxevdo_delete_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_get_all_named_result_names.html language=enus -->
## TOPIC 00059: rfmxevdovi/rfmxevdo_get_all_named_result_names.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_get_all_named_result_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_get_all_named_result_names.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Get All Named Result Names (VI)

RFmxEVDO Get All Named Result Names (VI)

Returns the named result names of the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxEVDO Get All Named Result Names' src='rfmxevdo_get_all_named_result_names.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Result Names returns an array of result names. |
|  | Default Result Exists? indicates whether the default result exists. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_initiate.html language=enus -->
## TOPIC 00060: rfmxevdovi/rfmxevdo_initiate.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_initiate.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Initiate (VI)

RFmxEVDO Initiate (VI)

Owning Palette:

RFmx EV-DO VIs

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the [RFmxEVDO Property Node](rfmxevdo_property_node.html). To get the status of measurements, use the [RFmxEVDO Wait for Measurement Complete](rfmxevdo_wait_for_measurement_complete.html) VI or [Check Measurement Status](rfmxevdo_check_measurement_status.html) VI.

[IMAGE alt='RFmxEVDO Initiate' src='rfmxevdo_initiate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String input parameter for Fetch VIs when using named signal configurations or named results. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_modacc_configure_multi_carrier_filter_enabled.html language=enus -->
## TOPIC 00061: rfmxevdovi/rfmxevdo_modacc_configure_multi_carrier_filter_enabled.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_modacc_configure_multi_carrier_filter_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_modacc_configure_multi_carrier_filter_enabled.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO ModAcc Configure Multi Carrier Filter Enabled (VI)

RFmxEVDO ModAcc Configure Multi Carrier Filter Enabled (VI)

Owning Palette:

ModAcc

Enables or disables the multicarrier filter. In multicarrier setups, EVM values are higher than in single carrier setups. The multicarrier filter attempts to minimize interferences from neighboring carriers by applying sharp edges.

To save time, do not use this filter in single-carrier setups.

[IMAGE alt='RFmxEVDO ModAcc Configure Multi Carrier Filter Enabled' src='rfmxevdo_modacc_configure_multi_carrier_filter_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Multi Carrier Filter Enabled enables or disables the multicarrier filter. The default value is False. False (0) The multicarrier filter is disabled. True (1) The multicarrier filter is enabled. |
| False (0) | The multicarrier filter is disabled. |
| True (1) | The multicarrier filter is enabled. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_modacc_configure_synchronization_mode_and_interval.html language=enus -->
## TOPIC 00062: rfmxevdovi/rfmxevdo_modacc_configure_synchronization_mode_and_interval.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_modacc_configure_synchronization_mode_and_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_modacc_configure_synchronization_mode_and_interval.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO ModAcc Configure Synchronization Mode and Interval (VI)

RFmxEVDO ModAcc Configure Synchronization Mode and Interval (VI)

Owning Palette:

ModAcc

Configures how the modulation accuracy (ModAcc) measurement synchronizes to the signal and the synchronization interval length.

[IMAGE alt='RFmxEVDO ModAcc Configure Synchronization Mode and Interval' src='rfmxevdo_modacc_configure_synchronization_mode_and_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Mode specifies whether the measurement is performed from frame, slot, or symbol boundary. Frame (0) The frame boundary is detected and measurement is performed over the Measurement Length parameter value, starting at the offset from the frame boundary specified in the Measurement Offset parameter. Slot (1) The slot boundary is detected and measurement is performed over the Measurement Length parameter value, starting at the offset from the frame boundary specified in the Measurement Offset parameter. Arbitrary (2) The symbol boundary is detected and measurement is performed over the Measurement Length parameter value, starting at the offset from the frame boundary specified in the Measurement Offset parameter. The default value is Slot. |
| Frame (0) | The frame boundary is detected and measurement is performed over the Measurement Length parameter value, starting at the offset from the frame boundary specified in the Measurement Offset parameter. |
| Slot (1) | The slot boundary is detected and measurement is performed over the Measurement Length parameter value, starting at the offset from the frame boundary specified in the Measurement Offset parameter. |
| Arbitrary (2) | The symbol boundary is detected and measurement is performed over the Measurement Length parameter value, starting at the offset from the frame boundary specified in the Measurement Offset parameter. |
|  | Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. For example, if the Synchronization Mode is set to Frame, ModAcc synchronizes to the first frame it finds. The measurement offset in slots is added after the boundary of this frame. The analysis is then started. |
|  | Measurement Length specifies the duration of the ModAcc measurement. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_modacc_fetch.html language=enus -->
## TOPIC 00063: rfmxevdovi/rfmxevdo_modacc_fetch.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_modacc_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_modacc_fetch.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO ModAcc Fetch (VI)

RFmxEVDO ModAcc Fetch (VI)

Owning Palette:

Fetch

Fetches Modulation Accuracy (ModAcc) measurement results.

#### RFmxEVDO ModAcc Fetch Uplink EVM

Returns the EVM and related values of the EV-DO uplink.

[IMAGE alt='RFmxEVDO ModAcc Fetch Uplink EVM' src='rfmxevdo_modacc_fetch_uplink_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Uplink RMS EVM (%) returns the RMS of the EVM, as a percentage. |
|  | Uplink Peak EVM (%) returns the peak value of the uplink EVM, as a percentage. |
|  | Uplink Rho returns the Rho value. |
|  | Chip Rate Error returns the chip rate error in parts per million (ppm). |
|  | Frequency Error returns the detected frequency error in Hz. |
|  | Uplink RMS Magnitude Error (%) returns the RMS of the magnitude error, as a percentage. |
|  | Uplink RMS Phase Error returns the RMS of the phase error in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ModAcc Fetch IQ Impairments

Returns the origin offset, gain imbalance, and quadrature error.

[IMAGE alt='RFmxEVDO ModAcc Fetch IQ Impairments' src='rfmxevdo_modacc_fetch_iq_impairments.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | I/Q Origin Offset returns the I/Q origin offset of the composite signal. This value is expressed in dB. |
|  | I/Q Gain Imbalance returns the I/Q gain imbalance of the composite signal. This value is expressed in dB. |
|  | I/Q Quadrature Error returns the I/Q quadrature error of the composite signal. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ModAcc Fetch Uplink Peak CDE

Returns the maximum value among the code domain errors (CDEs), in dB.

The CDEs are calculated by projecting the descrambled error vector onto the code domain at a specific spreading factor.

The CDE for every code with a specific spreading factor is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform.

A fixed spreading factor of 16 is used.

The CDEs are calculated separately for I and Q branches.

[IMAGE alt='RFmxEVDO ModAcc Fetch Uplink Peak CDE' src='rfmxevdo_modacc_fetch_uplink_peak_cde.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Uplink Peak CDE returns the maximum value among the CDEs. This value is expressed in dB. |
|  | Uplink Peak CDE Walsh Code Number returns the code number of the channel corresponding to the Uplink Peak CDE (dB) result. |
|  | Uplink Peak CDE Branch returns the quadrature branch of the peak CDE. I (0) Returns the channel with peak CDE detected on the in-phase branch. Q (1) Returns the channel with peak CDE detected on the quadrature branch. |
| I (0) | Returns the channel with peak CDE detected on the in-phase branch. |
| Q (1) | Returns the channel with peak CDE detected on the quadrature branch. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ModAcc Fetch Uplink Number of Detected Channels

Returns the number of channels detected by the modulation accuracy (ModAcc) measurement.

[IMAGE alt='RFmxEVDO ModAcc Fetch Uplink Number of Detected Channels' src='rfmxevdo_modacc_fetch_uplink_number_of_detected_channels.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Uplink Number of Detected Channels returns the number of channels detected by the ModAcc. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ModAcc Fetch Uplink Peak Active CDE

Returns the peak value among the code domain errors of the active channels, along with the code number and the code length.

[IMAGE alt='RFmxEVDO ModAcc Fetch Uplink Peak Active CDE' src='rfmxevdo_modacc_fetch_uplink_peak_active_cde.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Uplink Peak Active CDE returns the peak value of all CDEs of the active channels. This value is expressed in dB. |
|  | Uplink Peak Active CDE Walsh Code Length returns the Walsh code length of the channel corresponding to the Uplink Peak Active CDE (dB) result. |
|  | Uplink Peak Active CDE Walsh Code Number returns the Walsh code number of the channel corresponding to the Uplink Peak Active CDE (dB) result. |
|  | Uplink Peak Active CDE Branch returns the branch of the channel corresponding to the Peak Active CDE (dB) result. I (0) The peak active CDE corresponds to the in-phase branch. Q (1) The peak active CDE corresponds to the quadrature branch. I and Q (2) The peak active CDE corresponds to the in-phase branch and the quadrature branch. |
| I (0) | The peak active CDE corresponds to the in-phase branch. |
| Q (1) | The peak active CDE corresponds to the quadrature branch. |
| I and Q (2) | The peak active CDE corresponds to the in-phase branch and the quadrature branch. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ModAcc Fetch Uplink Detected Data Modulation Type

Returns the modulation type of the uplink data channel.

[IMAGE alt='RFmxEVDO ModAcc Fetch Uplink Detected Data Modulation Type' src='rfmxevdo_modacc_fetch_uplink_detected_data_modulation_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Uplink Detected Data Modulation Type returns the detected modulation type of the uplink data channel. Data Channel Absent (1) The uplink data channel is absent. B4 (2) The uplink data channel uses binary phase shift keying (BPSK) with the Walsh function W(4,2). Q4 (3) The uplink data channel uses quadrature phase shift keying (QPSK) with the Walsh function W(4,2). Q2 (4) The uplink data channel uses QPSK with the Walsh function W(2,1). Q4Q2 (5) The uplink data channel uses QPSK with the Walsh functions W(4,2) and W(2,1). E4E2 (6) The uplink data channel uses 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |
| Data Channel Absent (1) | The uplink data channel is absent. |
| B4 (2) | The uplink data channel uses binary phase shift keying (BPSK) with the Walsh function W(4,2). |
| Q4 (3) | The uplink data channel uses quadrature phase shift keying (QPSK) with the Walsh function W(4,2). |
| Q2 (4) | The uplink data channel uses QPSK with the Walsh function W(2,1). |
| Q4Q2 (5) | The uplink data channel uses QPSK with the Walsh functions W(4,2) and W(2,1). |
| E4E2 (6) | The uplink data channel uses 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ModAcc Fetch Uplink Detected Channel

Returns the detected channel selected by the selector string.

Use "channel<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxEVDO ModAcc Fetch Uplink Detected Channel' src='rfmxevdo_modacc_fetch_uplink_detected_channel.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and channel number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "channel0" "signal::sig1/channel0" "result::r1/channel0" "signal::sig1/result::r1/channel0" You can use the RFmxEVDO Build Channel String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Uplink Detected Walsh Code Length returns the detected Walsh code length. |
|  | Uplink Detected Walsh Code Number returns the detected Walsh code number. |
|  | Uplink Detected Branch returns the detected branch. I (0) The detected channel occupies the in-phase branch. Q (1) The detected channel occupies the quadrature branch. I and Q (2) The detected channel occupies the in-phase branch and the quadrature branch. |
| I (0) | The detected channel occupies the in-phase branch. |
| Q (1) | The detected channel occupies the quadrature branch. |
| I and Q (2) | The detected channel occupies the in-phase branch and the quadrature branch. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ModAcc Fetch Uplink Detected Channel (Array)

Returns the array of detected channels in the EV-DO uplink.

[IMAGE alt='RFmxEVDO ModAcc Fetch Uplink Detected Channel (Array)' src='rfmxevdo_modacc_fetch_uplink_detected_channel_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Uplink Detected Walsh Code Length returns an array of detected Walsh code length values. |
|  | Uplink Detected Walsh Code Number returns an array of detected Walsh code number values. |
|  | Uplink Detected Branch returns an array of detected branch values. I (0) The detected channel occupies the in-phase branch. Q (1) The detected channel occupies the quadrature branch. I and Q (2) The detected channel occupies the in-phase branch and the quadrature branch. |
| I (0) | The detected channel occupies the in-phase branch. |
| Q (1) | The detected channel occupies the quadrature branch. |
| I and Q (2) | The detected channel occupies the in-phase branch and the quadrature branch. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ModAcc Fetch EVM Trace

Returns the EVM trace of the ModAcc measurement.

[IMAGE alt='RFmxEVDO ModAcc Fetch EVM Trace' src='rfmxevdo_modacc_fetch_evm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | EVM returns the trace of error vector magnitude of the composite corrected signal. x0 is the start parameter. dx is the delta parameter. y returns the real signal values stored in an array. |
|  | x0 is the start parameter. |
|  | dx is the delta parameter. |
|  | y returns the real signal values stored in an array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ModAcc Fetch Magnitude Error Trace

Returns the magnitude error trace for the modulation accuracy (ModAcc) measurement.

[IMAGE alt='RFmxEVDO ModAcc Fetch Magnitude Error Trace' src='rfmxevdo_modacc_fetch_magnitude_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Magnitude Error specifies the data for a real waveform including the start, delta, and actual values. x0 is the start parameter. dx is the delta parameter. y returns the real signal values stored in an array. |
|  | x0 is the start parameter. |
|  | dx is the delta parameter. |
|  | y returns the real signal values stored in an array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ModAcc Fetch Phase Error Trace

Returns the phase error trace of the ModAcc measurement.

[IMAGE alt='RFmxEVDO ModAcc Fetch Phase Error Trace' src='rfmxevdo_modacc_fetch_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Phase Error specifies the data for a real waveform including the start, delta, and actual values. x0 is the start parameter. dx is the delta parameter. y returns the real signal values stored in an array. |
|  | x0 is the start parameter. |
|  | dx is the delta parameter. |
|  | y returns the real signal values stored in an array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO ModAcc Fetch Constellation Trace

Returns the constellation trace of the EV-DO measurement.

[IMAGE alt='RFmxEVDO ModAcc Fetch Constellation Trace' src='rfmxevdo_modacc_fetch_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Constellation returns an array of complex chips of the corrected signal on which the ModAcc measurements are done. These chips can be used to obtain the constellation diagram. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_obw_configure_averaging.html language=enus -->
## TOPIC 00064: rfmxevdovi/rfmxevdo_obw_configure_averaging.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_obw_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_obw_configure_averaging.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO OBW Configure Averaging (VI)

RFmxEVDO OBW Configure Averaging (VI)

Owning Palette:

OBW

Configures averaging for the occupied bandwidth (OBW) measurement.

[IMAGE alt='RFmxEVDO OBW Configure Averaging' src='rfmxevdo_obw_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) Averaging is not enabled. True (1) Averaging is enabled. |
| False (0) | Averaging is not enabled. |
| True (1) | Averaging is enabled. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_obw_configure_rbw_filter.html language=enus -->
## TOPIC 00065: rfmxevdovi/rfmxevdo_obw_configure_rbw_filter.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_obw_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_obw_configure_rbw_filter.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO OBW Configure RBW Filter (VI)

RFmxEVDO OBW Configure RBW Filter (VI)

Owning Palette:

OBW

Configures the resolution bandwidth (RBW) filter.

[IMAGE alt='RFmxEVDO OBW Configure RBW Filter' src='rfmxevdo_obw_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement calculates the RBW. The default value is True. True (1) RFmx EV-DO automatically computes the RBW. False (0) The measurement uses the RBW you specify. Refer to the RBW and Sweep Time section in the Spectrum topic for more details on RBW and sweep time. |
| True (1) | RFmx EV-DO automatically computes the RBW. |
| False (0) | The measurement uses the RBW you specify. |
|  | RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 30 kHz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_obw_configure_sweep_time.html language=enus -->
## TOPIC 00066: rfmxevdovi/rfmxevdo_obw_configure_sweep_time.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_obw_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_obw_configure_sweep_time.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO OBW Configure Sweep Time (VI)

RFmxEVDO OBW Configure Sweep Time (VI)

Owning Palette:

OBW

Configures sweep time.

[IMAGE alt='RFmxEVDO OBW Configure Sweep Time' src='rfmxevdo_obw_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement calculates the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of 1.67 ms. |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of 1.67 ms. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1.67 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_obw_fetch.html language=enus -->
## TOPIC 00067: rfmxevdovi/rfmxevdo_obw_fetch.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_obw_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_obw_fetch.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO OBW Fetch (VI)

RFmxEVDO OBW Fetch (VI)

Owning Palette:

Fetch

Fetches occupied bandwidth (OBW) measurement results.

#### RFmxEVDO OBW Fetch Measurement

Returns the occupied bandwidth (OBW) measurement.

[IMAGE alt='RFmxEVDO OBW Fetch Measurement' src='rfmxevdo_obw_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Occupied Bandwidth returns the occupied bandwidth. This value is expressed in Hz. |
|  | Absolute Power returns the total integrated power of the averaged spectrum acquired by the OBW measurement. This value is expressed in dBm. |
|  | Stop Frequency returns the stop frequency of the OBW. This value is expressed in Hz. |
|  | Start Frequency returns the start frequency of the OBW. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = stop frequency - start frequency |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO OBW Fetch Spectrum

Fetches the spectrum trace used for the OBW measurement.

[IMAGE alt='RFmxEVDO OBW Fetch Spectrum' src='rfmxevdo_obw_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_property_node.html language=enus -->
## TOPIC 00068: rfmxevdovi/rfmxevdo_property_node.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_property_node.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_property_node.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Property Node (VI)

RFmxEVDO Property Node (VI)

Owning Palette:

RFmx EV-DO VIs

Gets (reads), sets (writes), or resets (sets to default value) RFmxEVDO properties.

[IMAGE alt='RFmxEVDO Property Node' src='rfmxevdo_property_node.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_reset_to_default.html language=enus -->
## TOPIC 00069: rfmxevdovi/rfmxevdo_reset_to_default.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_reset_to_default.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_reset_to_default.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Reset to Default (VI)

RFmxEVDO Reset to Default (VI)

Owning Palette:

Utility

Resets a signal to the default values.

[IMAGE alt='RFmxEVDO Reset to Default' src='rfmxevdo_reset_to_default.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_select_measurement.html language=enus -->
## TOPIC 00070: rfmxevdovi/rfmxevdo_select_measurement.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_select_measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_select_measurement.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Select Measurement (VI)

RFmxEVDO Select Measurement (VI)

Owning Palette:

RFmx EV-DO VIs

Specifies the measurements that you want to enable. To select a single measurement, use the **Measurement** instance. To select multiple measurements, use the **Multiple Measurements** instance.

#### RFmxEVDO Select Measurement (Multiple)

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='RFmxEVDO Select Measurement (Multiple)' src='rfmxevdo_select_measurement_(multiple).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurements specifies the measurements to perform. ModAcc (0) Enables the ModAcc measurement. ACP (1) Enables the ACP measurement. CHP (2) Enables the CHP measurement. OBW (3) Enables the OBW measurement. SEM (4) Enables the SEM measurement. CDA (5) Enables the CDA measurement. SlotPhase (6) Enables the SlotPhase measurement. SlotPower (7) Enables the SlotPower measurement. The default is an empty array. |
| ModAcc (0) | Enables the ModAcc measurement. |
| ACP (1) | Enables the ACP measurement. |
| CHP (2) | Enables the CHP measurement. |
| OBW (3) | Enables the OBW measurement. |
| SEM (4) | Enables the SEM measurement. |
| CDA (5) | Enables the CDA measurement. |
| SlotPhase (6) | Enables the SlotPhase measurement. |
| SlotPower (7) | Enables the SlotPower measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO Select Measurement (Single)

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='RFmxEVDO Select Measurement (Single)' src='rfmxevdo_select_measurement_(single).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement specifies the measurement to perform. ModAcc (0) Enables the ModAcc measurement. ACP (1) Enables the ACP measurement. CHP (2) Enables the CHP measurement. OBW (3) Enables the OBW measurement. SEM (4) Enables the SEM measurement. CDA (5) Enables the CDA measurement. SlotPhase (6) Enables the SlotPhase measurement. SlotPower (7) Enables the SlotPower measurement. The default value is ModAcc. |
| ModAcc (0) | Enables the ModAcc measurement. |
| ACP (1) | Enables the ACP measurement. |
| CHP (2) | Enables the CHP measurement. |
| OBW (3) | Enables the OBW measurement. |
| SEM (4) | Enables the SEM measurement. |
| CDA (5) | Enables the CDA measurement. |
| SlotPhase (6) | Enables the SlotPhase measurement. |
| SlotPower (7) | Enables the SlotPower measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_sem_configure_averaging.html language=enus -->
## TOPIC 00071: rfmxevdovi/rfmxevdo_sem_configure_averaging.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_sem_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_sem_configure_averaging.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO SEM Configure Averaging (VI)

RFmxEVDO SEM Configure Averaging (VI)

Owning Palette:

SEM

Configures averaging for the spectral emission mask (SEM) measurement.

[IMAGE alt='RFmxEVDO SEM Configure Averaging' src='rfmxevdo_sem_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) Averaging is not enabled. True (1) Averaging is enabled. |
| False (0) | Averaging is not enabled. |
| True (1) | Averaging is enabled. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_sem_configure_sweep_time.html language=enus -->
## TOPIC 00072: rfmxevdovi/rfmxevdo_sem_configure_sweep_time.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_sem_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_sem_configure_sweep_time.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO SEM Configure Sweep Time (VI)

RFmxEVDO SEM Configure Sweep Time (VI)

Owning Palette:

SEM

Configures the sweep time.

[IMAGE alt='RFmxEVDO SEM Configure Sweep Time' src='rfmxevdo_sem_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement calculates the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of 1.67 ms. |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of 1.67 ms. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1.67 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_sem_fetch.html language=enus -->
## TOPIC 00073: rfmxevdovi/rfmxevdo_sem_fetch.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_sem_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_sem_fetch.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO SEM Fetch (VI)

RFmxEVDO SEM Fetch (VI)

Owning Palette:

Fetch

Fetches the spectral emission mask (SEM) measurement results.

#### RFmxEVDO SEM Fetch Measurement Status

Fetches the SEM measurement status.

[IMAGE alt='RFmxEVDO SEM Fetch Measurement Status' src='rfmxevdo_sem_fetch_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the status of the measurement. Fail (0) the signal exceeds the limits given by 3GPP2 C.S0033-D v2.0 tables 4.4.1.3-1 ff. Pass (1) The signal did not exceed the spectrum emission limits. |
| Fail (0) | the signal exceeds the limits given by 3GPP2 C.S0033-D v2.0 tables 4.4.1.3-1 ff. |
| Pass (1) | The signal did not exceed the spectrum emission limits. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SEM Fetch Total Carrier Power

Returns the total carrier power of the selected carrier.

[IMAGE alt='RFmxEVDO SEM Fetch Total Carrier Power' src='rfmxevdo_sem_fetch_total_carrier_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Carrier Power returns the total carrier power of the selected carrier. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SEM Fetch Carrier Measurement

Returns the carrier measurements for the carrier selected by the selector string. Use "carrier<n>" as the selector string to read parameters from this VI.

[IMAGE alt='RFmxEVDO SEM Fetch Carrier Measurement' src='rfmxevdo_sem_fetch_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxEVDO Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns absolute power of the selected carrier. This value is expressed in dBm. |
|  | Relative Integrated Power returns the relative power of the selected carrier. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SEM Fetch Carrier Measurement (Array)

Returns the array of carrier measurements.

[IMAGE alt='RFmxEVDO SEM Fetch Carrier Measurement (Array)' src='rfmxevdo_sem_fetch_carrier_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the array of absolute carrier powers. This value is expressed in dBm. |
|  | Relative Integrated Power returns the array of relative carrier powers. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SEM Fetch Lower Offset Power

Returns the lower offset segment power measurements. Use "offset<n>" as the selector string to read parameters from this VI.

[IMAGE alt='RFmxEVDO SEM Fetch Lower Offset Power' src='rfmxevdo_sem_fetch_lower_offset_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxEVDO Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the lower (negative) offset segment power measured. This value is expressed in dBm. |
|  | Relative Integrated Power returns the power in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Absolute Peak Power returns the peak power measured in the lower (negative) offset segment. The power is measured in dBm. |
|  | Relative Peak Power returns the peak power in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Peak Frequency returns the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SEM Fetch Lower Offset Power (Array)

Returns the arrays of lower offset segment power measurements.

[IMAGE alt='RFmxEVDO SEM Fetch Lower Offset Power (Array)' src='rfmxevdo_sem_fetch_lower_offset_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the array of lower (negative) offset segment powers measured. This value is expressed in dBm. |
|  | Relative Integrated Power returns the array of powers in each lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Absolute Peak Power returns the array of peak powers measured in each lower (negative) offset segment. |
|  | Relative Peak Power returns the array of peak powers in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Peak Frequency returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SEM Fetch Upper Offset Power

Returns the upper offset segment power measurements.



Use "offset<n>" as the selector string to read parameters from this VI.

[IMAGE alt='RFmxEVDO SEM Fetch Upper Offset Power' src='rfmxevdo_sem_fetch_upper_offset_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxEVDO Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the upper (positive) offset segment power measured. This value is expressed in dBm. |
|  | Relative Integrated Power returns the power in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Absolute Peak Power returns the peak power measured in the upper (positive) offset segment. The power is measured in dBm. |
|  | Relative Peak Power returns the peak power in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Peak Frequency returns the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SEM Fetch Upper Offset Power (Array)

Returns the arrays of upper offset segment power measurements.

[IMAGE alt='RFmxEVDO SEM Fetch Upper Offset Power (Array)' src='rfmxevdo_sem_fetch_upper_offset_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the array of upper (positive) offset segment powers measured. This value is expressed in dBm. |
|  | Relative Integrated Power returns the array of powers measured in each upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Absolute Peak Power returns the array of peak powers measured in each upper (positive) offset segment. The power is measured in dBm. |
|  | Relative Peak Power returns the array of peak powers measured in each upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Peak Frequency returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SEM Fetch Lower Offset Margin

Returns the measurement status and margin from the limit line measured in the lower offset segment.



Use "offset<n>" as the selector string to read parameters from this VI.

[IMAGE alt='RFmxEVDO SEM Fetch Lower Offset Margin' src='rfmxevdo_sem_fetch_lower_offset_margin.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxEVDO Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status indicates the lower offset measurement status. Fail (0) the signal exceeds the limits given by 3GPP2 C.S0033-D v2.0 tables 4.4.1.3-1 ff. Pass (1) The signal did not exceed the spectrum emission limits. |
| Fail (0) | the signal exceeds the limits given by 3GPP2 C.S0033-D v2.0 tables 4.4.1.3-1 ff. |
| Pass (1) | The signal did not exceed the spectrum emission limits. |
|  | Margin returns the margin. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
|  | Margin Frequency returns the frequency at which the margin occurred in the lower (negative) offset. This value is expressed in Hz. |
|  | Margin Relative Power returns the power at which the margin occurred in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Margin Absolute Power returns the power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SEM Fetch Lower Offset Margin (Array)

Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments.

[IMAGE alt='RFmxEVDO SEM Fetch Lower Offset Margin (Array)' src='rfmxevdo_sem_fetch_lower_offset_margin_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the array of lower offset measurement statuses. Fail (0) the signal exceeds the limits given by 3GPP2 C.S0033-D v2.0 tables 4.4.1.3-1 ff. Pass (1) The signal did not exceed the spectrum emission limits. |
| Fail (0) | the signal exceeds the limits given by 3GPP2 C.S0033-D v2.0 tables 4.4.1.3-1 ff. |
| Pass (1) | The signal did not exceed the spectrum emission limits. |
|  | Margin returns the array of margins. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
|  | Margin Frequency returns the array of frequencies at which the margin occurred in each lower (negative) offset segment. This value is expressed in Hz. |
|  | Margin Relative Power returns the array of powers at which the margin occurred in each lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Margin Absolute Power returns the array of powers at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SEM Fetch Upper Offset Margin

Returns the measurement status and margin from the limit line measured in the upper offset segment.



Use "offset<n>" as the selector string to read parameters from this VI.

[IMAGE alt='RFmxEVDO SEM Fetch Upper Offset Margin' src='rfmxevdo_sem_fetch_upper_offset_margin.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxEVDO Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status indicates the upper offset measurement status. |
|  | Margin returns the margin from the limit mask value. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
|  | Margin Frequency returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. |
|  | Margin Relative Power returns the power at which the margin occurred in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Margin Absolute Power returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SEM Fetch Upper Offset Margin (Array)

Returns the measurement status and margin from the limit line measured in the upper offset segments.

[IMAGE alt='RFmxEVDO SEM Fetch Upper Offset Margin (Array)' src='rfmxevdo_sem_fetch_upper_offset_margin_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the array of upper offset measurement statuses. Fail (0) the signal exceeds the limits given by 3GPP2 C.S0033-D v2.0 tables 4.4.1.3-1 ff. Pass (1) The signal did not exceed the spectrum emission limits. |
| Fail (0) | the signal exceeds the limits given by 3GPP2 C.S0033-D v2.0 tables 4.4.1.3-1 ff. |
| Pass (1) | The signal did not exceed the spectrum emission limits. |
|  | Margin returns the array of margins. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. |
|  | Margin Frequency returns the array of frequencies at which the margin occurred in each upper (positive) offset. This value is expressed in Hz. |
|  | Margin Relative Power returns the array of powers at which the margin occurred in each upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. |
|  | Margin Absolute Power returns the array of powers at which the margin occurred in each upper (positive) offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SEM Fetch Spectrum

Fetches the spectrum used for the spectral emission mask (SEM) measurement.

[IMAGE alt='RFmxEVDO SEM Fetch Spectrum' src='rfmxevdo_sem_fetch_spectrum.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Relative Mask returns the trace of power levels representing the relative mask in the spectral domain. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Absolute Mask returns the trace of power levels representing the absolute mask in the spectral domain. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_send_software_edge_trigger.html language=enus -->
## TOPIC 00074: rfmxevdovi/rfmxevdo_send_software_edge_trigger.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_send_software_edge_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_send_software_edge_trigger.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Send Software Edge Trigger (VI)

RFmxEVDO Send Software Edge Trigger (VI)

Owning Palette:

Configuration

Sends a trigger to the device when you use the [RFmxEVDO Configure Trigger](rfmxevdo_configure_trigger.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxEVDO Initiate VI.

[IMAGE alt='RFmxEVDO Send Software Edge Trigger' src='rfmxevdo_send_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_slotphase_configure_synchronization_mode_and_interval.html language=enus -->
## TOPIC 00075: rfmxevdovi/rfmxevdo_slotphase_configure_synchronization_mode_and_interval.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_slotphase_configure_synchronization_mode_and_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_slotphase_configure_synchronization_mode_and_interval.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO SlotPhase Configure Synchronization Mode and Interval (VI)

RFmxEVDO SlotPhase Configure Synchronization Mode and Interval (VI)

Owning Palette:

SlotPhase

Configures the synchronization mode, measurement offset, and measurement length.

[IMAGE alt='RFmxEVDO SlotPhase Configure Synchronization Mode and Interval' src='rfmxevdo_slotphase_configure_synchronization_mode_and_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Mode specifies whether the measurement is performed from the frame or the slot boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots specified by the SlotPhase Meas Length property starting at SlotPhase Meas Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots specified by SlotPhase Measurement Length number of slots, starting at SlotPhase Measurement Offset slots from the slot boundary. |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SlotPhase Meas Length property starting at SlotPhase Meas Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots specified by SlotPhase Measurement Length number of slots, starting at SlotPhase Measurement Offset slots from the slot boundary. |
|  | Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPhase Sync Mode property. The default value is 0. |
|  | Measurement Length specifies the duration of the SlotPhase measurement. This value is expressed in slots. The default value is 16. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_slotphase_fetch.html language=enus -->
## TOPIC 00076: rfmxevdovi/rfmxevdo_slotphase_fetch.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_slotphase_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_slotphase_fetch.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO SlotPhase Fetch (VI)

RFmxEVDO SlotPhase Fetch (VI)

Fetches SlotPhase measurement results.

#### RFmxEVDO SlotPhase Fetch Phase Discontinuities

Fetches the phase discontinuity value for the half-slot boundaries in the measurement interval.

[IMAGE alt='RFmxEVDO SlotPhase Fetch Phase Discontinuities' src='rfmxevdo_slotphase_fetch_phase_discontinuities.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Half Slot Phase Discontinuity returns the array of slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SlotPhase Fetch Maximum Half Slot Phase Discontinuity

Fetches the maximum phase discontinuity observed at half-slot boundaries in the measurement interval.

[IMAGE alt='RFmxEVDO SlotPhase Fetch Maximum Half Slot Phase Discontinuity' src='rfmxevdo_slotphase_fetch_maximum_half_slot_phase_discontinuity.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Half Slot Phase Discontinuity returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SlotPhase Fetch Chip Phase Error Trace

Fetches the chip phase error trace for the SlotPhase Measurement.

The chip phase error is the phase error between the actually received waveform and the reference waveform.

[IMAGE alt='RFmxEVDO SlotPhase Fetch Chip Phase Error Trace' src='rfmxevdo_slotphase_fetch_chip_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Chip Phase Error returns the data for a real waveform including the start, delta, and actual values. x0 is the start parameter. dx is the delta parameter. y returns the real signal values stored in an array. |
|  | x0 is the start parameter. |
|  | dx is the delta parameter. |
|  | y returns the real signal values stored in an array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxEVDO SlotPhase Fetch Chip Phase Error Linear Fit Trace

Fetches the chip phase error trace linear fit trace for the SlotPhase measurement.

The linear fit is obtained from the chip phase error on a half-slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side of the half-slot boundary and extrapolates the phase error to the half-slot boundaries.

[IMAGE alt='RFmxEVDO SlotPhase Fetch Chip Phase Error Linear Fit Trace' src='rfmxevdo_slotphase_fetch_chip_phase_error_linear_fit_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Chip Phase Error Linear Fit returns the data for a real waveform including the start, delta, and actual values. x0 is the start parameter. dx is the delta parameter. y returns the real signal values stored in an array. |
|  | x0 is the start parameter. |
|  | dx is the delta parameter. |
|  | y returns the real signal values stored in an array. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_slotpower_configure_synchronization_mode_and_interval.html language=enus -->
## TOPIC 00077: rfmxevdovi/rfmxevdo_slotpower_configure_synchronization_mode_and_interval.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_slotpower_configure_synchronization_mode_and_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_slotpower_configure_synchronization_mode_and_interval.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO SlotPower Configure Synchronization Mode and Interval (VI)

RFmxEVDO SlotPower Configure Synchronization Mode and Interval (VI)

Owning Palette:

SlotPower

Configures the synchronization mode, measurement offset, and measurement length.

[IMAGE alt='RFmxEVDO SlotPower Configure Synchronization Mode and Interval' src='rfmxevdo_slotpower_configure_synchronization_mode_and_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Mode specifies whether the measurement is performed from the frame or the slot boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots specified by the SlotPower Meas Length property starting at SlotPower Meas Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots specified by SlotPower Measurement Length number of slots, starting at SlotPower Measurement Offset slots from the slot boundary. |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SlotPower Meas Length property starting at SlotPower Meas Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots specified by SlotPower Measurement Length number of slots, starting at SlotPower Measurement Offset slots from the slot boundary. |
|  | Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPower Sync Mode property. The default value is 0. |
|  | Measurement Length specifies the duration of the SlotPower measurement. This value is expressed in slots. The default value is 16. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_slotpower_fetch.html language=enus -->
## TOPIC 00078: rfmxevdovi/rfmxevdo_slotpower_fetch.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_slotpower_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_slotpower_fetch.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO SlotPower Fetch (VI)

RFmxEVDO SlotPower Fetch (VI)

Fetches SlotPower measurement results.

#### RFmxEVDO SlotPower Fetch Powers

Fetches the slot power and slot power delta for all half-slots in the measurement length. The slot power delta is the difference in power between adjacent half-slots.

[IMAGE alt='RFmxEVDO SlotPower Fetch Powers' src='rfmxevdo_slotpower_fetch_powers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Half Slot Power returns the array of half slot powers. This value is expressed in dBm. |
|  | Half Slot Power Delta returns the array of half slot power delta powers. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/rfmxevdo_wait_for_measurement_complete.html language=enus -->
## TOPIC 00079: rfmxevdovi/rfmxevdo_wait_for_measurement_complete.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/rfmxevdo_wait_for_measurement_complete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/rfmxevdo_wait_for_measurement_complete.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Wait for Measurement Complete (VI)

RFmxEVDO Wait for Measurement Complete (VI)

Owning Palette:

Utility

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='RFmxEVDO Wait for Measurement Complete' src='rfmxevdo_wait_for_measurement_complete.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/sem_pal.html language=enus -->
## TOPIC 00080: rfmxevdovi/sem_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/sem_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/sem_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

SEM

SEM

Owning Palette:

Configuration

Use the VIs on this palette to configure spectral emission mask (SEM) measurements. You can also use the [RFmxEVDO Property Node](rfmxevdo_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO SEM Configure Averaging | Configures averaging for the spectral emission mask (SEM) measurement. |
| RFmxEVDO SEM Configure Sweep Time | Configures the sweep time. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/slotphase_pal.html language=enus -->
## TOPIC 00081: rfmxevdovi/slotphase_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/slotphase_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/slotphase_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

SlotPhase

SlotPhase

Use the VIs on this palette to configure SlotPhase measurement. You can use the RFmxEVDO Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO SlotPhase Configure Synchronization Mode and Interval | Configures the synchronization mode, measurement offset, and measurement length. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/slotpower_pal.html language=enus -->
## TOPIC 00082: rfmxevdovi/slotpower_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/slotpower_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/slotpower_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

SlotPower

SlotPower

Use the VIs on this palette to configure SlotPower measurement. You can use the RFmxEVDO Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO SlotPower Configure Synchronization Mode and Interval | Configures the synchronization mode, measurement offset, and measurement length. |

<!--NI_TOPIC bundle=rfmx-evdo-vi path=rfmxevdovi/utility_pal.html language=enus -->
## TOPIC 00083: rfmxevdovi/utility_pal.html

- bundle_id: `rfmx-evdo-vi`
- source_path: `rfmxevdovi/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-vi/raw/resource/enus/rfmxevdovi/utility_pal.html
- document_id: `rfmx-evdo-vi`
- page_type: `leaf`
- content_type: ``

Utility

Utility

Owning Palette:

RFmx EV-DO VIs

Use the VIs on this palette to configure RFmxEVDO utilities.

| Palette Object | Description |
| --- | --- |
| RFmxEVDO Commit | Commits settings to the hardware. Calling this VI is optional. RFmxEVDO commits settings to the hardware when you call the RFmxEVDO Initiate VI. |
| RFmxEVDO Reset to Default | Resets a signal to the default values. |
| RFmxEVDO Wait for Measurement Complete | Waits for the specified number for seconds for all the measurements to complete. |
| RFmxEVDO Check Measurement Status | Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
