# NI DOCUMENT BUNDLE: rfmx-wcdma-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-wcdma-vi start=1 end=89 -->
<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/acp_pal.html language=enus -->
## TOPIC 00001: rfmxwcdmavi/acp_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/acp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/acp_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

ACP

ACP

Owning Palette:

Configuration

Use the VIs on this palette to configure ACP measurements. You can use the RFmxWCDMA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA ACP Configure Averaging | Configures averaging for the ACP measurement. |
| RFmxWCDMA ACP Configure Sweep Time | Configures the sweep time interval. |
| RFmxWCDMA ACP Configure Number of Offsets | Configures the number of offsets for the ACP measurement. |
| RFmxWCDMA ACP Configure Offset Power Reference | Configures the power reference to use for measuring the relative power of the offset channel. |
| RFmxWCDMA ACP Configure Measurement Method | Configures the method for performing the ACP measurement. |
| RFmxWCDMA ACP Configure Noise Compensation Enabled | Configures the compensation of the channel power for the inherent noise floor of the signal analyzer. |
| RFmxWCDMA ACP Configure RBW Filter | Configures the RBW filter. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/advanced_pal.html language=enus -->
## TOPIC 00002: rfmxwcdmavi/advanced_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/advanced_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/advanced_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

Advanced

Advanced

Owning Palette:

RFmx WCDMA VIs

Use the VIs on this palette to use advanced features.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA Abort Measurements | Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxWCDMA Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error. |
| RFmxWCDMA Analyze2 | Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the Spectrum instance. |
| RFmxWCDMA Create Signal Configuration | Creates a new instance of a signal. |
| RFmxWCDMA Clone Signal Configuration | Creates a new instance of a signal by copying all the property values from an existing signal instance. |
| RFmxWCDMA Delete Signal Configuration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxWCDMA Get All Named Result Names | Returns the named result names of the signal that you specify in the Selector String parameter. |
| RFmxWCDMA Clear Named Result | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxWCDMA Clear All Named Results | Clears all results for the signal that you specify in the Selector String parameter. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/build_string_pal.html language=enus -->
## TOPIC 00003: rfmxwcdmavi/build_string_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/build_string_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/build_string_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

Build String

Build String

Owning Palette:

RFmx WCDMA VIs

Use the VIs on this palette to create strings for configurations and results that require a selector string.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA Build Signal String | Creates selector string for use with configuration or fetch properties and VIs. |
| RFmxWCDMA Build Channel String | Creates the channel string to use as the selector string with the channel configuration and results. |
| RFmxWCDMA Build Carrier String | Creates the carrier string to use as the selector string with the SEM and ACP carrier configuration or fetch VIs, properties, and results. |
| RFmxWCDMA Build Offset String | Creates the offset string to use as the selector string with the SEM and ACP offset configuration or fetch properties and VIs. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/cda_pal.html language=enus -->
## TOPIC 00004: rfmxwcdmavi/cda_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/cda_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/cda_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

CDA

CDA

Owning Palette:

Configuration

Use the VIs on this palette to configure CDA measurements. You can also use the RFmxWCDMA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA CDA Configure Synchronization Mode and Interval | Configures the synchronization mode, measurement offset, and measurement length. |
| RFmxWCDMA CDA Configure Measurement Channel | Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. |
| RFmxWCDMA CDA Configure Power Unit | Configures the power unit for all code domain power results, except Total Power (dBm). |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/chp_pal.html language=enus -->
## TOPIC 00005: rfmxwcdmavi/chp_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/chp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/chp_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

CHP

CHP

Owning Palette:

Configuration

Use the VIs on this palette to configure CHP measurements. You can also use the RFmxWCDMA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA CHP Configure Averaging | Configures averaging for the CHP measurement. |
| RFmxWCDMA CHP Configure Sweep Time | Configures the sweep time interval. |
| RFmxWCDMA CHP Configure RBW Filter | Configures the RBW filter. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/configuration_array_vis_pal.html language=enus -->
## TOPIC 00006: rfmxwcdmavi/configuration_array_vis_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/configuration_array_vis_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/configuration_array_vis_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

Array VIs

Array VIs

Owning Palette:

Configuration

Use the VIs on this palette to configure array VIs. You can also use the [RFmxWCDMA Property Node](../rfmxwcdmavi/rfmxwcdma_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA Configure Carrier Frequency (Array) | Configures an array of the center frequencies of the carriers, relative to the RF center frequency. |
| RFmxWCDMA Configure Uplink Test Model (Array) | Configures the uplink test model for all the carriers. |
| RFmxWCDMA Configure Number of Channels (Array) | Configures the number of user-defined channels for all the carriers in the measurement. This VI is used when you set the Channel Configuration Mode property to User Defined. Call this VI before you call the RFmxWCDMA Configure User Defined Channel (Array) VI or the RFmxWCDMA Configure User Defined Channel VI. |
| RFmxWCDMA Configure User Defined Channel (Array) | Configures an array of spreading factors, spreading codes, modulation types, and branches of the user-defined channels. Before calling this VI, you must configure the Num Channels property with the appropriate number of user-defined channels. Use "carrier<n>" as the selector string to configure this VI. |
| RFmxWCDMA Configure Uplink Scrambling (Array) | Configures the scrambling code and the scrambling code type for all the carriers. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/configuration_pal.html language=enus -->
## TOPIC 00007: rfmxwcdmavi/configuration_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/configuration_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

Configuration

Configuration

Owning Palette:

RFmx WCDMA VIs

Use the VIs on this palette to configure RFmxWCDMA measurements. You can use the RFmxWCDMA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA Configure RF | Configures the RF properties of the signal specified by the selector string. |
| RFmxWCDMA Configure Frequency | Configures the RF center frequency directly or by using the UTRA absolute radio frequency channel number (UARFCN) and band. |
| RFmxWCDMA Configure Reference Level | Configures the reference level, which represents the maximum expected power of an RF input signal. |
| RFmxWCDMA Auto Level | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level. |
| RFmxWCDMA Configure External Attenuation | Configures the external attenuation. |
| RFmxWCDMA Configure Trigger | Configures the Reference Trigger you use to acquire the signal. |
| RFmxWCDMA Send Software Edge Trigger | Sends a trigger to the device when you use the RFmxWCDMA Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. |
| RFmxWCDMA Configure Number of Carriers | Configures the number of carriers for ACP, CHP, OBW, SEM, and ModAcc measurements. |
| RFmxWCDMA Configure Carrier Frequency | Configures the center frequency of the carrier, relative to the RF center frequency. Use "carrier<n>" as the selector string to configure this VI. |
| RFmxWCDMA Configure Contiguous Carriers | Configures the contiguous carriers based on the number of carriers and the carrier at the center frequency. |
| RFmxWCDMA Configure Band | Configures the Universal Mobile Telecommunications System (UMTS) operating band. |
| RFmxWCDMA Configure Channel Configuration Mode | Configures the channel configuration mode. |
| RFmxWCDMA Configure Number of Channels | Configures the number of user-defined channels for the measurement. This VI is used when you set the Channel Configuration Mode property to User Defined. Call this VI before you call the RFmxWCDMA Configure User Defined Channel (Array) VI or the RFmxWCDMA Configure User Defined Channel VI. Use "carrier<n>" as the selector string to configure this VI. |
| RFmxWCDMA Configure Uplink Scrambling | Configures the uplink scrambling type and the scrambling code. Use "carrier<n>" as the selector string to configure this VI. |
| RFmxWCDMA Configure Uplink Test Model | Configures the uplink test model. Use "carrier<n>" as the selector string to configure this VI. |
| RFmxWCDMA Configure User Defined Channel | Configures the spreading factor, spreading code, modulation type, and branch of each user-defined channel. Before calling this VI, you must configure the Num Channels property with the appropriate number of channels. Use "carrier<k>/channel<n>" as the selector string to configure this VI. |
| RFmxWCDMA Build Signal String | Creates selector string for use with configuration or fetch properties and VIs. |
| RFmxWCDMA Build Channel String | Creates the channel string to use as the selector string with the channel configuration and results. |
| RFmxWCDMA Build Carrier String | Creates the carrier string to use as the selector string with the SEM and ACP carrier configuration or fetch VIs, properties, and results. |

| Subpalette | Description |
| --- | --- |
| Array VIs | Use the VIs on this palette to configure array VIs. You can also use the RFmxWCDMA Property Node to configure additional properties. |
| ModAcc | Use the VIs on this palette to configure ModAcc measurements. You can also use the RFmxWCDMA Property Node to configure additional properties. |
| ACP | Use the VIs on this palette to configure ACP measurements. You can use the RFmxWCDMA Property Node to configure additional properties. |
| CHP | Use the VIs on this palette to configure CHP measurements. You can also use the RFmxWCDMA Property Node to configure additional properties. |
| OBW | Use the VIs on this palette to configure OBW measurements. You can also use the RFmxWCDMA Property Node to configure additional properties. |
| SEM | Use the VIs on this palette to configure spectral emission mask (SEM) measurements. You can also use the RFmxWCDMA Property Node to configure additional properties. |
| QEVM | Use the VIs on this palette to configure QEVM measurements. You can also use the RFmxWCDMA Property Node to configure additional properties. |
| SlotPhase | Use the VIs on this palette to configure SlotPhase measurements. You can also use the RFmxWCDMA Property Node to configure additional properties. |
| CDA | Use the VIs on this palette to configure CDA measurements. You can also use the RFmxWCDMA Property Node to configure additional properties. |
| SlotPower | Use the VIs on this palette to configure SlotPower measurements. You can also use the RFmxWCDMA Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/fetch_pal.html language=enus -->
## TOPIC 00008: rfmxwcdmavi/fetch_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/fetch_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/fetch_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

Fetch

Fetch

Owning Palette:

RFmx WCDMA VIs

Use the VIs on this palette to fetch measurement results and traces.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA ModAcc Fetch | Fetches results of the ModAcc measurement. |
| RFmxWCDMA ACP Fetch | Fetches the ACP measurement results. |
| RFmxWCDMA CHP Fetch | Fetches the CHP measurement results. |
| RFmxWCDMA OBW Fetch | Fetches the OBW measurement results. |
| RFmxWCDMA SEM Fetch | Fetches the SEM measurement results. |
| RFmxWCDMA QEVM Fetch | Fetches the QEVM measurement results. |
| RFmxWCDMA SlotPhase Fetch | Fetches the SlotPhase measurement results. |

| Subpalette | Description |
| --- | --- |
| Build String | Use the VIs on this palette to create strings for configurations and results that require a selector string. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/modacc_pal.html language=enus -->
## TOPIC 00009: rfmxwcdmavi/modacc_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/modacc_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/modacc_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

ModAcc

ModAcc

Owning Palette:

Configuration

Use the VIs on this palette to configure ModAcc measurements. You can also use the [RFmxWCDMA Property Node](../rfmxwcdmavi/rfmxwcdma_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA ModAcc Configure Synchronization Mode and Interval | Configures the synchronization mode, measurement offset, and measurement length of the ModAcc measurement. |
| RFmxWCDMA ModAcc Configure Reference Waveform | Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster ModAcc measurements. This VI is used only when you set the ModAcc Sync Mode property to Marker. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/obw_pal.html language=enus -->
## TOPIC 00010: rfmxwcdmavi/obw_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/obw_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/obw_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

OBW

OBW

Owning Palette:

Configuration

Use the VIs on this palette to configure OBW measurements. You can also use the RFmxWCDMA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA OBW Configure Averaging | Configures averaging for the OBW measurement. |
| RFmxWCDMA OBW Configure Sweep Time | Configures the sweep time interval. |
| RFmxWCDMA OBW Configure RBW Filter | Configures the RBW filter. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/qevm_pal.html language=enus -->
## TOPIC 00011: rfmxwcdmavi/qevm_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/qevm_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/qevm_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

QEVM

QEVM

Owning Palette:

Configuration

Use the VIs on this palette to configure QEVM measurements. You can also use the RFmxWCDMA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA QEVM Configure Averaging | Configures averaging for the QEVM measurement. |
| RFmxWCDMA QEVM Configure Measurement Length | Configures the measurement length of the QEVM measurement. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_abort_measurements.html language=enus -->
## TOPIC 00012: rfmxwcdmavi/rfmxwcdma_abort_measurements.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_abort_measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_abort_measurements.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Abort Measurements (VI)

RFmxWCDMA Abort Measurements (VI)

Owning Palette:

Advanced

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxWCDMA Initiate](rfmxwcdma_initiate.html) VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='RFmxWCDMA Abort Measurements' src='rfmxwcdma_abort_measurements.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_acp_configure_averaging.html language=enus -->
## TOPIC 00013: rfmxwcdmavi/rfmxwcdma_acp_configure_averaging.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_acp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_acp_configure_averaging.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA ACP Configure Averaging (VI)

RFmxWCDMA ACP Configure Averaging (VI)

Owning Palette:

ACP

Configures averaging for the ACP measurement.

[IMAGE alt='RFmxWCDMA ACP Configure Averaging' src='rfmxwcdma_acp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging of the spectrum for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one record to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one record to the next. |
| RMS (0) | The power spectrum is linearly averaged. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one record to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one record to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_acp_configure_measurement_method.html language=enus -->
## TOPIC 00014: rfmxwcdmavi/rfmxwcdma_acp_configure_measurement_method.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_acp_configure_measurement_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_acp_configure_measurement_method.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA ACP Configure Measurement Method (VI)

RFmxWCDMA ACP Configure Measurement Method (VI)

Owning Palette:

ACP

Configures the method for performing the ACP measurement.

[IMAGE alt='RFmxWCDMA ACP Configure Measurement Method' src='rfmxwcdma_acp_configure_measurement_method.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Method specifies the method for performing the ACP measurement. The default value is Normal. Normal (0) The ACP measurement acquires the spectrum with the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. Dynamic Range (1) The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported devices: PXIe-5665/5668R Sequential FFT (2) The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of each chunk is defined by the ACP Sequential FFT Size property, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. Accuracy of the results may be reduced when using this measurement method. For accurate power measurements, when the power characteristics of the signal vary over time, Averaging is allowed. The following properties have limited support when you set the ACP Measurement Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Sweep Time Auto False ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads 1 ACP Amplitude Correction Type RF Center Frequency Note For multi-span FFT, the averaging count should be 1. |
| Normal (0) | The ACP measurement acquires the spectrum with the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| Dynamic Range (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported devices: PXIe-5665/5668R |
| Sequential FFT (2) | The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of each chunk is defined by the ACP Sequential FFT Size property, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. Accuracy of the results may be reduced when using this measurement method. For accurate power measurements, when the power characteristics of the signal vary over time, Averaging is allowed. The following properties have limited support when you set the ACP Measurement Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Sweep Time Auto False ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads 1 ACP Amplitude Correction Type RF Center Frequency Note For multi-span FFT, the averaging count should be 1. |
| Property | Supported Value |
| ACP RBW Auto | True |
| ACP RBW Filter Type | FFT Based |
| ACP Sweep Time Auto | False |
| ACP Averaging Count | >=1 |
| ACP Noise Comp Enabled | False |
| ACP Num Analysis Threads | 1 |
| ACP Amplitude Correction Type | RF Center Frequency |
|  | Note For multi-span FFT, the averaging count should be 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_acp_configure_noise_compensation_enabled.html language=enus -->
## TOPIC 00015: rfmxwcdmavi/rfmxwcdma_acp_configure_noise_compensation_enabled.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_acp_configure_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_acp_configure_noise_compensation_enabled.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA ACP Configure Noise Compensation Enabled (VI)

RFmxWCDMA ACP Configure Noise Compensation Enabled (VI)

Owning Palette:

ACP

Configures the compensation of the channel power for the inherent noise floor of the signal analyzer.

[IMAGE alt='RFmxWCDMA ACP Configure Noise Compensation Enabled' src='rfmxwcdma_acp_configure_noise_compensation_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Noise Compensation Enabled specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. The default value is False. False (0) Disables compensation of the channel powers for the noise floor of the signal analyzer. True (1) Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842 |
| False (0) | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| True (1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842 |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_acp_configure_number_of_offsets.html language=enus -->
## TOPIC 00016: rfmxwcdmavi/rfmxwcdma_acp_configure_number_of_offsets.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_acp_configure_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_acp_configure_number_of_offsets.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA ACP Configure Number of Offsets (VI)

RFmxWCDMA ACP Configure Number of Offsets (VI)

Owning Palette:

ACP

Configures the number of offsets for the ACP measurement.

[IMAGE alt='RFmxWCDMA ACP Configure Number of Offsets' src='rfmxwcdma_acp_configure_number_of_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Offsets specifies the number of offset channels. The default value is 2. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_acp_configure_offset_power_reference.html language=enus -->
## TOPIC 00017: rfmxwcdmavi/rfmxwcdma_acp_configure_offset_power_reference.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_acp_configure_offset_power_reference.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_acp_configure_offset_power_reference.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA ACP Configure Offset Power Reference (VI)

RFmxWCDMA ACP Configure Offset Power Reference (VI)

Owning Palette:

ACP

Configures the power reference to use for measuring the relative power of the offset channel.

[IMAGE alt='RFmxWCDMA ACP Configure Offset Power Reference' src='rfmxwcdma_acp_configure_offset_power_reference.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset Power Reference Carrier specifies the carrier to use as the power reference to measure offset channel relative power. The default value is Composite. Closest (0) The measurement uses the power measured in the carrier closest to the offset channel center frequency as the power reference. Highest (1) The measurement uses the highest power measured among all the active carriers as the power reference. Composite (2) The measurement uses the sum of powers measured in all the active carriers as the power reference. Specific (3) The measurement uses the power measured in the carrier that has an index specified by the Offset Power Reference Specific parameter as the power reference. |
| Closest (0) | The measurement uses the power measured in the carrier closest to the offset channel center frequency as the power reference. |
| Highest (1) | The measurement uses the highest power measured among all the active carriers as the power reference. |
| Composite (2) | The measurement uses the sum of powers measured in all the active carriers as the power reference. |
| Specific (3) | The measurement uses the power measured in the carrier that has an index specified by the Offset Power Reference Specific parameter as the power reference. |
|  | Offset Power Reference Specific specifies the index of the carrier to be used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the Offset Power Reference Carrier parameter to Specific. The default value is 0. Valid values are 0 to (Value of the Num Carriers property - 1). |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_acp_configure_rbw_filter.html language=enus -->
## TOPIC 00018: rfmxwcdmavi/rfmxwcdma_acp_configure_rbw_filter.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_acp_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_acp_configure_rbw_filter.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA ACP Configure RBW Filter (VI)

RFmxWCDMA ACP Configure RBW Filter (VI)

Owning Palette:

ACP

Configures the RBW filter.

[IMAGE alt='RFmxWCDMA ACP Configure RBW Filter' src='rfmxwcdma_acp_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. The default value is True. This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. If you set the RBW Filter Type parameter to FFT Based, the measurement calculates the RBW regardless of the value of this parameter. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
|  | RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. This value is expressed in Hz. The default value is 38.4 kHz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_acp_configure_sweep_time.html language=enus -->
## TOPIC 00019: rfmxwcdmavi/rfmxwcdma_acp_configure_sweep_time.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_acp_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_acp_configure_sweep_time.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA ACP Configure Sweep Time (VI)

RFmxWCDMA ACP Configure Sweep Time (VI)

Owning Palette:

ACP

Configures the sweep time interval.

[IMAGE alt='RFmxWCDMA ACP Configure Sweep Time' src='rfmxwcdma_acp_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement uses a sweep time value of one slot duration. |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement uses a sweep time value of one slot duration. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 666.66666700000007 microseconds. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_acp_fetch.html language=enus -->
## TOPIC 00020: rfmxwcdmavi/rfmxwcdma_acp_fetch.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_acp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_acp_fetch.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA ACP Fetch (VI)

RFmxWCDMA ACP Fetch (VI)

Owning Palette:

Fetch

Fetches the ACP measurement results.

#### RFmxWCDMA ACP Fetch Total Carrier Power

Fetches the total carrier power for the ACP measurement.

[IMAGE alt='RFmxWCDMA ACP Fetch Total Carrier Power' src='rfmxwcdma_acp_fetch_total_carrier_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Carrier Power returns the sum of all active carrier powers, where each carrier power corresponds to the value of the ACP Results Carrier Abs Pwr property. This value is expressed in dBm. For a single-carrier measurement, total carrier power is the same as carrier absolute power. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ACP Fetch Carrier Measurement

Fetches the absolute and relative powers of the carrier. The relative power is relative to the total carrier power.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxWCDMA ACP Fetch Carrier Measurement' src='rfmxwcdma_acp_fetch_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns the carrier power. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the Center Frequency and Carrier Freq properties. This value is expressed in dBm. |
|  | Relative Power returns the carrier power relative to the total carrier power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ACP Fetch Carrier Measurement (Array)

Returns the array of absolute powers and the array of relative powers for the ACP measurement. The relative powers are relative to the ACP Results Total Carrier Pwr property.

[IMAGE alt='RFmxWCDMA ACP Fetch Carrier Measurement (Array)' src='rfmxwcdma_acp_fetch_carrier_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns an array of carrier power values. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the Center Frequency and Carrier Freq properties. This value is expressed in dBm. |
|  | Relative Power returns an array of carrier power values relative to the total active carrier power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ACP Fetch Offset Measurement

Fetches the absolute and relative powers measured in the offset channel for the ACP measurement. The relative powers are measured relative to the power reference carrier.

Use "offset<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxWCDMA ACP Fetch Offset Measurement' src='rfmxwcdma_acp_fetch_offset_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxWCDMA Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Lower Relative Power returns the offset channel power measured relative to the power of the carrier(s) that you specify in the ACP Offset Pwr Ref Carrier property. This value is expressed in dB. |
|  | Upper Relative Power returns the upper offset channel power measured relative to the power of the carrier(s) that you specify in the ACP Offset Pwr Ref Carrier property. This value is expressed in dB. |
|  | Lower Absolute Power returns the lower offset channel power. The lower offset channel power is the integrated power of the RRC-filtered signal at the lower offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. |
|  | Upper Absolute Power returns the upper offset channel power. The upper offset channel power is the integrated power of the RRC-filtered signal at the upper offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ACP Fetch Offset Measurement (Array)

Fetches an array of absolute powers and an array of relative powers measured in the offset channels for the ACP measurement. The relative powers are measured with reference to the ACP Offset Pwr Ref Carrier property.

[IMAGE alt='RFmxWCDMA ACP Fetch Offset Measurement (Array)' src='rfmxwcdma_acp_fetch_offset_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Lower Relative Power returns an array of lower offset channel power values measured relative to the power of the carrier(s) that you specify in the ACP Offset Pwr Ref Carrier property. This value is expressed in dB. |
|  | Upper Relative Power returns an array of upper offset channel power values measured relative to the power of the carrier(s) that you specify in the ACP Offset Pwr Ref Carrier property. This value is expressed in dB. |
|  | Lower Absolute Power returns an array of lower offset channel power values. The lower offset channel power is the integrated power of the RRC-filtered signal at the lower offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. |
|  | Upper Absolute Power returns an array of upper offset channel power values. The upper offset channel power is the integrated power of the RRC-filtered signal at the upper offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ACP Fetch Spectrum

Fetches the spectrum used for the ACP measurement.

[IMAGE alt='RFmxWCDMA ACP Fetch Spectrum' src='rfmxwcdma_acp_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power at each frequency bin. The value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power at each frequency bin. The value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ACP Fetch Relative Powers Trace

Fetches the relative powers trace for the ACP measurement.

[IMAGE alt='RFmxWCDMA ACP Fetch Relative Powers Trace' src='rfmxwcdma_acp_fetch_relative_powers_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Relative Powers returns the trace of relative power values measured in each channel relative to the power reference carrier. This value is expressed in dB. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the relative power with reference to the power reference carrier property. The value is expressed in dB. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the relative power with reference to the power reference carrier property. The value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ACP Fetch Absolute Powers Trace

Fetches the absolute powers trace for the ACP measurement.

[IMAGE alt='RFmxWCDMA ACP Fetch Absolute Powers Trace' src='rfmxwcdma_acp_fetch_absolute_powers_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Powers returns the trace of the measured integrated power in each channel. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power at each frequency bin. The value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power at each frequency bin. The value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_analyze2.html language=enus -->
## TOPIC 00021: rfmxwcdmavi/rfmxwcdma_analyze2.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_analyze2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_analyze2.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Analyze2 (VI)

RFmxWCDMA Analyze2 (VI)

Owning Palette:

Advanced

Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the Spectrum instance.

#### RFmxWCDMA Analyze (IQ, 1 Wfm)

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.

Use this VI only if the Recommended Acquisition Type property value is either **IQ** or **IQ or Spectral**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmx WCDMA Commit VI. |
| --- | --- |

[IMAGE alt='RFmxWCDMA Analyze (IQ 1 Wfm)' src='rfmxwcdma_analyze_(iq_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". |
| --- | --- |
|  | IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 specifies the start time of the input Y array. This value is expressed in seconds. dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input Y array. This value is expressed in seconds. |
|  | dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA Analyze (Spectrum, 1 Wfm)

Performs the enabled measurements on the spectrum waveform that you specify in the **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.

Use this VI only if the Recommended Acquisition Type property value is either **Spectral** or **IQ or Spectral**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmx WCDMA Commit VI. |
| --- | --- |

[IMAGE alt='RFmxWCDMA Analyze (Spectrum 1 Wfm)' src='rfmxwcdma_analyze_(spectrum_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". |
| --- | --- |
|  | Spectrum specifies the data for a spectrum waveform including the start, delta, and actual values. x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx specifies the frequency interval between data points in the spectrum. y contains the real-value power spectrum. |
|  | x0 specifies the start frequency of the spectrum. This value is expressed in Hz. |
|  | dx specifies the frequency interval between data points in the spectrum. |
|  | y contains the real-value power spectrum. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_auto_level.html language=enus -->
## TOPIC 00022: rfmxwcdmavi/rfmxwcdma_auto_level.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_auto_level.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Auto Level (VI)

RFmxWCDMA Auto Level (VI)

Owning Palette:

Configuration

Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxWCDMA Auto Level VI completes the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device, based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the Auto Level Initial Ref Level property.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxWCDMA Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='RFmxWCDMA Auto Level' src='rfmxwcdma_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Interval specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Reference Level returns the reference level that represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_build_carrier_string.html language=enus -->
## TOPIC 00023: rfmxwcdmavi/rfmxwcdma_build_carrier_string.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_build_carrier_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_build_carrier_string.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Build Carrier String (VI)

RFmxWCDMA Build Carrier String (VI)

Owning Palette:

Configuration

Creates the carrier string to use as the selector string with the SEM and ACP carrier configuration or fetch VIs, properties, and results.

[IMAGE alt='RFmxWCDMA Build Carrier String' src='rfmxwcdma_build_carrier_string.gif']

|  | Carrier Number specifies the carrier number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Fetch VIs. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_build_channel_string.html language=enus -->
## TOPIC 00024: rfmxwcdmavi/rfmxwcdma_build_channel_string.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_build_channel_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_build_channel_string.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Build Channel String (VI)

RFmxWCDMA Build Channel String (VI)

Owning Palette:

Configuration

Creates the channel string to use as the selector string with the channel configuration and results.

[IMAGE alt='RFmxWCDMA Build Channel String' src='rfmxwcdma_build_channel_string.gif']

|  | Channel Number specifies the channel number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Fetch VIs. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_build_offset_string.html language=enus -->
## TOPIC 00025: rfmxwcdmavi/rfmxwcdma_build_offset_string.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_build_offset_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_build_offset_string.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Build Offset String (VI)

RFmxWCDMA Build Offset String (VI)

Owning Palette:

Build String

Creates the offset string to use as the selector string with the SEM and ACP offset configuration or fetch properties and VIs.

[IMAGE alt='RFmxWCDMA Build Offset String' src='rfmxwcdma_build_offset_string.gif']

|  | Offset Number specifies the offset number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Fetch VIs. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_build_signal_string.html language=enus -->
## TOPIC 00026: rfmxwcdmavi/rfmxwcdma_build_signal_string.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_build_signal_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_build_signal_string.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Build Signal String (VI)

RFmxWCDMA Build Signal String (VI)

Owning Palette:

Configuration

Creates selector string for use with configuration or fetch properties and VIs.

[IMAGE alt='RFmxWCDMA Build Signal String' src='rfmxwcdma_build_signal_string.gif']

|  | Result Name specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string). Example: "result::r1" "r1" |
| --- | --- |
|  | Signal Name specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Example: "signal::sig1" "sig1" |
|  | Selector String returns the selector string. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_cda_configure_measurement_channel.html language=enus -->
## TOPIC 00027: rfmxwcdmavi/rfmxwcdma_cda_configure_measurement_channel.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_cda_configure_measurement_channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_cda_configure_measurement_channel.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA CDA Configure Measurement Channel (VI)

RFmxWCDMA CDA Configure Measurement Channel (VI)

Owning Palette:

CDA

Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

[IMAGE alt='RFmxWCDMA CDA Configure Measurement Channel' src='rfmxwcdma_cda_configure_measurement_channel.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Spreading Factor specifies the spreading factor of the measurement channel. This value is used to compute the symbol results of the CDA measurement. The default value is 256. Valid values are 2, 4, 8, 16, 32, 64, 128, and 256. |
|  | Spreading Code specifies the spreading code of the measurement channel. This value is used to compute the symbol results of the CDA measurement. The default value is 0. Valid values are 0 to (Spreading Factor - 1). |
|  | Modulation Type specifies the modulation type of the measurement channel. This value is used to compute the symbol results of the CDA measurement. The default value is BPSK/QPSK. BPSK/QPSK (0) The modulation type is BPSK. 4PAM/16QAM (1) The modulation type is 4-PAM. |
| BPSK/QPSK (0) | The modulation type is BPSK. |
| 4PAM/16QAM (1) | The modulation type is 4-PAM. |
|  | Branch specifies the branch of the measurement channel. This value is used to compute the symbol results of the CDA measurement. The default value is I. I (0) The signal is modulated on the in-phase branch. Q (1) The signal is modulated on the quadrature-phase branch. |
| I (0) | The signal is modulated on the in-phase branch. |
| Q (1) | The signal is modulated on the quadrature-phase branch. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_cda_configure_power_unit.html language=enus -->
## TOPIC 00028: rfmxwcdmavi/rfmxwcdma_cda_configure_power_unit.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_cda_configure_power_unit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_cda_configure_power_unit.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA CDA Configure Power Unit (VI)

RFmxWCDMA CDA Configure Power Unit (VI)

Owning Palette:

CDA

Configures the power unit for all code domain power results, except Total Power (dBm).

[IMAGE alt='RFmxWCDMA CDA Configure Power Unit' src='rfmxwcdma_cda_configure_power_unit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Power Unit specifies the measurement unit of all power results, except, CDA Results Total Pwr. The default value is dB. dB (0) Specifies the power relative to the total power. dBm (1) Specifies the absolute power measured. |
| dB (0) | Specifies the power relative to the total power. |
| dBm (1) | Specifies the absolute power measured. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_cda_configure_synchronization_mode_and_interval.html language=enus -->
## TOPIC 00029: rfmxwcdmavi/rfmxwcdma_cda_configure_synchronization_mode_and_interval.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_cda_configure_synchronization_mode_and_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_cda_configure_synchronization_mode_and_interval.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA CDA Configure Synchronization Mode and Interval (VI)

RFmxWCDMA CDA Configure Synchronization Mode and Interval (VI)

Owning Palette:

CDA

Configures the synchronization mode, measurement offset, and measurement length.

[IMAGE alt='RFmxWCDMA CDA Configure Synchronization Mode and Interval' src='rfmxwcdma_cda_configure_synchronization_mode_and_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Mode specifies whether the measurement is performed from the frame, slot, or symbol boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots expressed by Measurement Length parameter, starting at Measurement Offset slots from the slot boundary. Arbitrary (2) The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the symbol boundary. |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by Measurement Length parameter, starting at Measurement Offset slots from the slot boundary. |
| Arbitrary (2) | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the symbol boundary. |
|  | Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. The Valid values are [0, (15 - Measurement Length)]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15. |
|  | Measurement Length specifies the duration of the code domain measurement. This value is expressed in slots. The default value is 1. Valid values are [1, (15 - Measurement Offset)]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_cda_fetch.html language=enus -->
## TOPIC 00030: rfmxwcdmavi/rfmxwcdma_cda_fetch.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_cda_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_cda_fetch.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA CDA Fetch (VI)

RFmxWCDMA CDA Fetch (VI)

Fetches results of the CDA measurement.

#### RFmxWCDMA CDA Fetch Code Domain I and Q Power

Fetches the I and Q mean active powers and I and Q peak inactive powers.

[IMAGE alt='RFmxWCDMA CDA Fetch Code Domain I and Q Power' src='rfmxwcdma_cda_fetch_code_domain_i_and_q_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | I Mean Active Power returns the average code power among the set of active in-phase channels in the code domain. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. |
|  | Q Mean Active Power returns the average code power among the set of active quadrature-phase channels in the code domain. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. |
|  | I Peak Inactive Power returns the largest code power among the set of inactive in-phase channels in the code domain. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. |
|  | Q Peak Inactive Power (dB or dBm) returns the largest code power among the set of inactive quadrature-phase channels in the code domain. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA CDA Fetch Code Domain I and Q Power Trace

Fetches the code domain power trace for I and Q branches. The code domain power is obtained for all codes with a spreading factor of 256, for I and Q branches separately.

[IMAGE alt='RFmxWCDMA CDA Fetch Code Domain I and Q Power Trace' src='rfmxwcdma_cda_fetch_code_domain_i_and_q_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | I Code Domain Powers returns an array of code domain powers for the in-phase component. |
|  | Q Code Domain Powers returns an array of code domain powers for the quadrature-phase component. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA CDA Fetch Code Domain Power

Fetches the Total Power , Total Active Power , Mean and Peak Active Powers, and Mean and Peak Inactive Powers.

[IMAGE alt='RFmxWCDMA CDA Fetch Code Domain Power' src='rfmxwcdma_cda_fetch_code_domain_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Total Power returns the mean power of the received signal, sampled at ideal inter-symbol-interference free points. This value is expressed in dBm. |
|  | Total Active Power returns the sum of all the active channel powers. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. |
|  | Mean Active Power returns the average of all the active channel powers. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. |
|  | Mean Inactive Power returns the average code power among the set of inactive channels in the code domain. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. |
|  | Peak Active Power returns the largest code power among the set of active channels in the code domain. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. |
|  | Peak Inactive Power returns the largest code power among the set of inactive channels in the code domain. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA CDA Fetch Code Domain Power Trace

Fetches the code domain power trace. The code domain power is obtained for all codes with spreading factor 256 for both I and Q branches in an interleaved manner.

[IMAGE alt='RFmxWCDMA CDA Fetch Code Domain Power Trace' src='rfmxwcdma_cda_fetch_code_domain_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Code Domain Powers returns an array of code domain powers for I and Q branches in an interleaved manner. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA CDA Fetch Symbol EVM

Returns the root mean square and peak of symbol EVM, RMS of symbol magnitude error, RMS of symbol phase error, and mean symbol power, corresponding to the measurement channel.

[IMAGE alt='RFmxWCDMA CDA Fetch Symbol EVM' src='rfmxwcdma_cda_fetch_symbol_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS Symbol EVM returns the RMS EVM for the measurement channel. This value is expressed as a percentage. |
|  | Peak Symbol EVM returns the peak EVM for the measurement channel. This value is expressed as a percentage. |
|  | RMS Symbol Magnitude Error returns the RMS magnitude error for the measurement channel. This value is expressed as a percentage. |
|  | Mean Symbol Power returns the mean power of the symbols for the measurement channel. This value is expressed in dB or dBm. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. |
|  | RMS Symbol Phase Error returns the RMS phase error for the measurement channel. This value is expressed in degrees. |
|  | Chip Rate Error returns the chip rate error of the composite signal. This value is expressed in ppm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA CDA Fetch Symbol EVM Trace

Fetches the root mean square EVM trace of the measurement channel.

[IMAGE alt='RFmxWCDMA CDA Fetch Symbol EVM Trace' src='rfmxwcdma_cda_fetch_symbol_evm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Symbol EVM returns an array of RMS EVM values of the symbols of the measurement channel. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA CDA Fetch Symbol Magnitude Error Trace

Fetches the magnitude error trace of the measurement channel.

[IMAGE alt='RFmxWCDMA CDA Fetch Symbol Magnitude Error Trace' src='rfmxwcdma_cda_fetch_symbol_magnitude_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Symbol Magnitude Error returns an array of magnitude errors of the symbols of the measurement channel. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA CDA Fetch Symbol Phase Error Trace

Fetches the phase error trace of the measurement channel.

[IMAGE alt='RFmxWCDMA CDA Fetch Symbol Phase Error Trace' src='rfmxwcdma_cda_fetch_symbol_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Symbol Phase Error returns an array of phase errors of the symbols of the measurement channel. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA CDA Fetch Symbol Power Trace

Fetches the power versus time trace of the symbol corresponding to the measurement channel.

[IMAGE alt='RFmxWCDMA CDA Fetch Symbol Power Trace' src='rfmxwcdma_cda_fetch_symbol_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Symbol Powers returns the array of symbol powers of the measurement channel. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_check_measurement_status.html language=enus -->
## TOPIC 00031: rfmxwcdmavi/rfmxwcdma_check_measurement_status.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_check_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_check_measurement_status.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Check Measurement Status (VI)

RFmxWCDMA Check Measurement Status (VI)

Owning Palette:

Utility

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='RFmxWCDMA Check Measurement Status' src='rfmxwcdma_check_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | done? indicates whether the measurement is complete. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_chp_configure_averaging.html language=enus -->
## TOPIC 00032: rfmxwcdmavi/rfmxwcdma_chp_configure_averaging.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_chp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_chp_configure_averaging.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA CHP Configure Averaging (VI)

RFmxWCDMA CHP Configure Averaging (VI)

Owning Palette:

CHP

Configures averaging for the CHP measurement.

[IMAGE alt='RFmxWCDMA CHP Configure Averaging' src='rfmxwcdma_chp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging of the spectrum for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one record to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one record to the next. |
| RMS (0) | The power spectrum is linearly averaged. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one record to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one record to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_chp_configure_rbw_filter.html language=enus -->
## TOPIC 00033: rfmxwcdmavi/rfmxwcdma_chp_configure_rbw_filter.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_chp_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_chp_configure_rbw_filter.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA CHP Configure RBW Filter (VI)

RFmxWCDMA CHP Configure RBW Filter (VI)

Owning Palette:

CHP

Configures the RBW filter.

[IMAGE alt='RFmxWCDMA CHP Configure RBW Filter' src='rfmxwcdma_chp_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. The default value is True. This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. If you set the RBW Filter Type parameter to FFT Based, the measurement calculates the RBW regardless of the value of this parameter. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
|  | RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. This value is expressed in Hz. The default value is 50 kHz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_chp_configure_sweep_time.html language=enus -->
## TOPIC 00034: rfmxwcdmavi/rfmxwcdma_chp_configure_sweep_time.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_chp_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_chp_configure_sweep_time.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA CHP Configure Sweep Time (VI)

RFmxWCDMA CHP Configure Sweep Time (VI)

Owning Palette:

CHP

Configures the sweep time interval.

[IMAGE alt='RFmxWCDMA CHP Configure Sweep Time' src='rfmxwcdma_chp_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement uses a sweep time value of one slot duration. |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement uses a sweep time value of one slot duration. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 666.66666700000007 microseconds. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_chp_fetch.html language=enus -->
## TOPIC 00035: rfmxwcdmavi/rfmxwcdma_chp_fetch.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_chp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_chp_fetch.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA CHP Fetch (VI)

RFmxWCDMA CHP Fetch (VI)

Owning Palette:

Fetch

Fetches the CHP measurement results.

#### RFmxWCDMA CHP Fetch Total Carrier Power

Fetches the total carrier power for the CHP measurement.

[IMAGE alt='RFmxWCDMA CHP Fetch Total Carrier Power' src='rfmxwcdma_chp_fetch_total_carrier_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Carrier Power returns the total integrated power of all the active carriers. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA CHP Fetch Carrier Measurement

Fetches the absolute and relative powers of the carrier for the CHP measurement. The relative power is relative to the total carrier power.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxWCDMA CHP Fetch Carrier Measurement' src='rfmxwcdma_chp_fetch_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns the carrier power integrated over a bandwidth of 5 MHz. This value is expressed in dBm. |
|  | Relative Power returns the carrier power relative to the CHP Results Total Carrier Pwr property. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA CHP Fetch Carrier Measurement (Array)

Fetches an array of absolute powers and array of relative powers of the carriers for the CHP measurement. The relative power is relative to the total carrier power.

[IMAGE alt='RFmxWCDMA CHP Fetch Carrier Measurement (Array)' src='rfmxwcdma_chp_fetch_carrier_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns an array of carrier powers integrated over a bandwidth of 5 MHz. This value is expressed in dBm. |
|  | Relative Power returns an array of carrier powers relative to the CHP Results Total Carrier Pwr property. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA CHP Fetch Spectrum

Fetches the spectrum used for the CHP measurement.

[IMAGE alt='RFmxWCDMA CHP Fetch Spectrum' src='rfmxwcdma_chp_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power at each frequency bin. The value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power at each frequency bin. The value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_clear_all_named_results.html language=enus -->
## TOPIC 00036: rfmxwcdmavi/rfmxwcdma_clear_all_named_results.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_clear_all_named_results.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_clear_all_named_results.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Clear All Named Results (VI)

RFmxWCDMA Clear All Named Results (VI)

Owning Palette:

Advanced

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxWCDMA Clear All Named Results' src='rfmxwcdma_clear_all_named_results.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_clear_named_result.html language=enus -->
## TOPIC 00037: rfmxwcdmavi/rfmxwcdma_clear_named_result.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_clear_named_result.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_clear_named_result.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Clear Named Result (VI)

RFmxWCDMA Clear Named Result (VI)

Owning Palette:

Advanced

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='RFmxWCDMA Clear Named Result' src='rfmxwcdma_clear_named_result.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_clone_signal_configuration.html language=enus -->
## TOPIC 00038: rfmxwcdmavi/rfmxwcdma_clone_signal_configuration.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_clone_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_clone_signal_configuration.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Clone Signal Configuration (VI)

RFmxWCDMA Clone Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='RFmxWCDMA Clone Signal Configuration' src='rfmxwcdma_clone_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
|  | Old Signal Name specifies the name of the existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_commit.html language=enus -->
## TOPIC 00039: rfmxwcdmavi/rfmxwcdma_commit.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_commit.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Commit (VI)

RFmxWCDMA Commit (VI)

Owning Palette:

Utility

Commits settings to the hardware. Calling this VI is optional. RFmxWCDMA commits settings to the hardware when you call the [RFmxWCDMA Initiate](rfmxwcdma_initiate.html) VI.

[IMAGE alt='RFmxWCDMA Commit' src='rfmxwcdma_commit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_band.html language=enus -->
## TOPIC 00040: rfmxwcdmavi/rfmxwcdma_configure_band.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_band.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_band.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Band (VI)

RFmxWCDMA Configure Band (VI)

Owning Palette:

Configuration

Configures the Universal Mobile Telecommunications System (UMTS) operating band.

[IMAGE alt='RFmxWCDMA Configure Band' src='rfmxwcdma_configure_band.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Band specifies the UMTS operation band. The default value is 1. 1 (1) The terminal operates in UMTS Band I. 2 (2) The terminal operates in UMTS Band II. 3 (3) The terminal operates in UMTS Band III. 4 (4) The terminal operates in UMTS Band IV. 5 (5) The terminal operates in UMTS Band V. 6 (6) The terminal operates in UMTS Band VI. 7 (7) The terminal operates in UMTS Band VII. 8 (8) The terminal operates in UMTS Band VIII. 9 (9) The terminal operates in UMTS Band IX. 10 (10) The terminal operates in UMTS Band X. 11 (11) The terminal operates in UMTS Band XI. 12 (12) The terminal operates in UMTS Band XII. 13 (13) The terminal operates in UMTS Band XIII. 14 (14) The terminal operates in UMTS Band XIV. 19 (19) The terminal operates in UMTS Band XIX. 20 (20) The terminal operates in UMTS Band XX. 21 (21) The terminal operates in UMTS Band XXI. 22 (22) The terminal operates in UMTS Band XXII. 25 (25) The terminal operates in UMTS Band XXV. 26 (26) The terminal operates in UMTS Band XXVI. |
| 1 (1) | The terminal operates in UMTS Band I. |
| 2 (2) | The terminal operates in UMTS Band II. |
| 3 (3) | The terminal operates in UMTS Band III. |
| 4 (4) | The terminal operates in UMTS Band IV. |
| 5 (5) | The terminal operates in UMTS Band V. |
| 6 (6) | The terminal operates in UMTS Band VI. |
| 7 (7) | The terminal operates in UMTS Band VII. |
| 8 (8) | The terminal operates in UMTS Band VIII. |
| 9 (9) | The terminal operates in UMTS Band IX. |
| 10 (10) | The terminal operates in UMTS Band X. |
| 11 (11) | The terminal operates in UMTS Band XI. |
| 12 (12) | The terminal operates in UMTS Band XII. |
| 13 (13) | The terminal operates in UMTS Band XIII. |
| 14 (14) | The terminal operates in UMTS Band XIV. |
| 19 (19) | The terminal operates in UMTS Band XIX. |
| 20 (20) | The terminal operates in UMTS Band XX. |
| 21 (21) | The terminal operates in UMTS Band XXI. |
| 22 (22) | The terminal operates in UMTS Band XXII. |
| 25 (25) | The terminal operates in UMTS Band XXV. |
| 26 (26) | The terminal operates in UMTS Band XXVI. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_carrier_frequency.html language=enus -->
## TOPIC 00041: rfmxwcdmavi/rfmxwcdma_configure_carrier_frequency.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_carrier_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_carrier_frequency.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Carrier Frequency (VI)

RFmxWCDMA Configure Carrier Frequency (VI)

Owning Palette:

Configuration

Configures the center frequency of the carrier, relative to the RF center frequency.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxWCDMA Configure Carrier Frequency' src='rfmxwcdma_configure_carrier_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Carrier Frequency specifies the center frequency of the carrier, relative to the RF center frequency. This value is expressed in Hz. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_carrier_frequency_(array).html language=enus -->
## TOPIC 00042: rfmxwcdmavi/rfmxwcdma_configure_carrier_frequency_(array).html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_carrier_frequency_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_carrier_frequency_(array).html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Carrier Frequency (Array) (VI)

RFmxWCDMA Configure Carrier Frequency (Array) (VI)

Owning Palette:

Array VIs

Configures an array of the center frequencies of the carriers, relative to the RF center frequency.

[IMAGE alt='RFmxWCDMA Configure Carrier Frequency (Array)' src='rfmxwcdma_configure_carrier_frequency_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Carrier Frequency specifies an array of the center frequencies of the carriers, relative to the RF center frequency. This value is expressed in Hz. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_channel_configuration_mode.html language=enus -->
## TOPIC 00043: rfmxwcdmavi/rfmxwcdma_configure_channel_configuration_mode.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_channel_configuration_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_channel_configuration_mode.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Channel Configuration Mode (VI)

RFmxWCDMA Configure Channel Configuration Mode (VI)

Owning Palette:

Configuration

Configures the channel configuration mode.

[IMAGE alt='RFmxWCDMA Configure Channel Configuration Mode' src='rfmxwcdma_configure_channel_configuration_mode.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Channel Configuration Mode specifies the channel configuration mode. The default value is Auto Detect. Auto Detect (0) The measurement detects the channels. User Defined (1) Configure the channels using the Num Channels property and the RFmxWCDMA Configure User Defined Channel (Array) VI. Test Model (2) Choose from the standard-defined channel configurations using the UL Test Model property. |
| Auto Detect (0) | The measurement detects the channels. |
| User Defined (1) | Configure the channels using the Num Channels property and the RFmxWCDMA Configure User Defined Channel (Array) VI. |
| Test Model (2) | Choose from the standard-defined channel configurations using the UL Test Model property. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_contiguous_carriers.html language=enus -->
## TOPIC 00044: rfmxwcdmavi/rfmxwcdma_configure_contiguous_carriers.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_contiguous_carriers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_contiguous_carriers.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Contiguous Carriers (VI)

RFmxWCDMA Configure Contiguous Carriers (VI)

Owning Palette:

Configuration

Configures the contiguous carriers based on the number of carriers and the carrier at the center frequency.

[IMAGE alt='RFmxWCDMA Configure Contiguous Carriers' src='rfmxwcdma_configure_contiguous_carriers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Carriers specifies the number of carriers. The default value is 1. |
|  | Carrier at Center Frequency specifies the index of the carrier that is at the center frequency. Set this parameter to -1 to specify a center frequency at the center of all carriers. For example, if you set the value of the Number of Carriers parameter to 2, and set the value of the Carrier at Center Frequency parameter to 1, the center frequency is at carrier1. If you set the value of the Number of Carriers parameter to 2, and set the value of the Carrier at Center Frequency parameter to -1, the center frequency is at the center of carrier0 and carrier1. If you set the value of the Number of Carriers parameter to 3, and set the value of the Carrier at Center Frequency parameter to either -1 or 1, the center frequency is at carrier1, which is the center of all carriers. The default value is -1. Recommended values are -1 to (Number of Carriers - 1). If you set this parameter to a value greater than (Number of Carriers - 1), the value of this parameter is coerced to (Number of Carriers - 1). |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_external_attenuation.html language=enus -->
## TOPIC 00045: rfmxwcdmavi/rfmxwcdma_configure_external_attenuation.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_external_attenuation.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure External Attenuation (VI)

RFmxWCDMA Configure External Attenuation (VI)

Owning Palette:

Configuration

Configures the external attenuation.

[IMAGE alt='RFmxWCDMA Configure External Attenuation' src='rfmxwcdma_configure_external_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | External Attenuation specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. This value is expressed in dB. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_frequency.html language=enus -->
## TOPIC 00046: rfmxwcdmavi/rfmxwcdma_configure_frequency.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_frequency.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Frequency (VI)

RFmxWCDMA Configure Frequency (VI)

Owning Palette:

Configuration

Configures the RF center frequency directly or by using the UTRA absolute radio frequency channel number (UARFCN) and band.

#### RFmxWCDMA Configure Frequency (UARFCN)

Configures the center frequency in the universal mobile telecommunications system (UMTS) frequency band using the link direction, band, and UARFCN of the received signal.

[IMAGE alt='RFmxWCDMA Configure Frequency (UARFCN)' src='rfmxwcdma_configure_frequency_(uarfcn).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Link Direction specifies the link direction. Uplink (1) The link is from the user equipment to the base transceiver station. |
| Uplink (1) | The link is from the user equipment to the base transceiver station. |
|  | Band specifies the UMTS operation band. The default value is 1. 1 (1) The terminal operates in UMTS Band I. 2 (2) The terminal operates in UMTS Band II. 3 (3) The terminal operates in UMTS Band III. 4 (4) The terminal operates in UMTS Band IV. 5 (5) The terminal operates in UMTS Band V. 6 (6) The terminal operates in UMTS Band VI. 7 (7) The terminal operates in UMTS Band VII. 8 (8) The terminal operates in UMTS Band VIII. 9 (9) The terminal operates in UMTS Band IX. 10 (10) The terminal operates in UMTS Band X. 11 (11) The terminal operates in UMTS Band XI. 12 (12) The terminal operates in UMTS Band XII. 13 (13) The terminal operates in UMTS Band XIII. 14 (14) The terminal operates in UMTS Band XIV. 19 (19) The terminal operates in UMTS Band XIX. 20 (20) The terminal operates in UMTS Band XX. 21 (21) The terminal operates in UMTS Band XXI. 22 (22) The terminal operates in UMTS Band XXII. 25 (25) The terminal operates in UMTS Band XXV. 26 (26) The terminal operates in UMTS Band XXVI. |
| 1 (1) | The terminal operates in UMTS Band I. |
| 2 (2) | The terminal operates in UMTS Band II. |
| 3 (3) | The terminal operates in UMTS Band III. |
| 4 (4) | The terminal operates in UMTS Band IV. |
| 5 (5) | The terminal operates in UMTS Band V. |
| 6 (6) | The terminal operates in UMTS Band VI. |
| 7 (7) | The terminal operates in UMTS Band VII. |
| 8 (8) | The terminal operates in UMTS Band VIII. |
| 9 (9) | The terminal operates in UMTS Band IX. |
| 10 (10) | The terminal operates in UMTS Band X. |
| 11 (11) | The terminal operates in UMTS Band XI. |
| 12 (12) | The terminal operates in UMTS Band XII. |
| 13 (13) | The terminal operates in UMTS Band XIII. |
| 14 (14) | The terminal operates in UMTS Band XIV. |
| 19 (19) | The terminal operates in UMTS Band XIX. |
| 20 (20) | The terminal operates in UMTS Band XX. |
| 21 (21) | The terminal operates in UMTS Band XXI. |
| 22 (22) | The terminal operates in UMTS Band XXII. |
| 25 (25) | The terminal operates in UMTS Band XXV. |
| 26 (26) | The terminal operates in UMTS Band XXVI. |
|  | UARFCN specifies the UTRA absolute radio frequency channel number (UARFCN). UARFCN has to be updated according to the band for the uplink, as defined by the general UARFCNs in Table 4.2: UTRA Absolute Radio Frequency Channel Number in the 3GPP TS 34.121-1 specification, version 11.5.0. Otherwise, UARFCN is coerced to the top or bottom UARFCN of the selected band, depending on which is nearer. The center frequency then corresponds to this coerced UARFCN as defined by carrier frequencies in Table 4.1: UARFCN definition (general) of the 3GPP TS 34.121-1 specification, version 11.5.0. The default value is 9,750, which corresponds to the center of the UMTS Band I. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA Configure Frequency (Frequency)

Configures the RF center frequency.

[IMAGE alt='RFmxWCDMA Configure Frequency (Frequency)' src='rfmxwcdma_configure_frequency_(frequency).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the center frequency of the acquired RF signal for a single carrier. For multicarrier measurements, the Center Frequency parameter specifies the reference frequency for the values in the Carrier Freq property. This value is expressed in Hz. The default value of this parameter is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_number_of_carriers.html language=enus -->
## TOPIC 00047: rfmxwcdmavi/rfmxwcdma_configure_number_of_carriers.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_number_of_carriers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_number_of_carriers.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Number of Carriers (VI)

RFmxWCDMA Configure Number of Carriers (VI)

Owning Palette:

Configuration

Configures the number of carriers for ACP, CHP, OBW, SEM, and ModAcc measurements.

[IMAGE alt='RFmxWCDMA Configure Number of Carriers' src='rfmxwcdma_configure_number_of_carriers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Carriers specifies the number of carriers. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_number_of_channels.html language=enus -->
## TOPIC 00048: rfmxwcdmavi/rfmxwcdma_configure_number_of_channels.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_number_of_channels.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_number_of_channels.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Number of Channels (VI)

RFmxWCDMA Configure Number of Channels (VI)

Owning Palette:

Configuration

Configures the number of user-defined channels for the measurement. This VI is used when you set the Channel Configuration Mode property to **User Defined**. Call this VI before you call the [RFmxWCDMA Configure User Defined Channel (Array)](../rfmxwcdmavi/rfmxwcdma_configure_user_defined_channel_(array).html) VI or the [RFmxWCDMA Configure User Defined Channel](../rfmxwcdmavi/rfmxwcdma_configure_user_defined_channel.html) VI.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxWCDMA Configure Number of Channels' src='rfmxwcdma_configure_number_of_channels.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Channels specifies the number of user-defined channels. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_number_of_channels_(array).html language=enus -->
## TOPIC 00049: rfmxwcdmavi/rfmxwcdma_configure_number_of_channels_(array).html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_number_of_channels_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_number_of_channels_(array).html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Number of Channels (Array) (VI)

RFmxWCDMA Configure Number of Channels (Array) (VI)

Owning Palette:

Array VIs

Configures the number of user-defined channels for all the carriers in the measurement. This VI is used when you set the Channel Configuration Mode property to **User Defined**. Call this VI before you call the [RFmxWCDMA Configure User Defined Channel (Array)](../rfmxwcdmavi/rfmxwcdma_configure_user_defined_channel.html) VI or the [RFmxWCDMA Configure User Defined Channel](../rfmxwcdmavi/rfmxwcdma_configure_user_defined_channel.html) VI.

[IMAGE alt='RFmxWCDMA Configure Number of Channels (Array)' src='rfmxwcdma_configure_number_of_channels_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Channels specifies the array of number of channels. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_reference_level.html language=enus -->
## TOPIC 00050: rfmxwcdmavi/rfmxwcdma_configure_reference_level.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_reference_level.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Reference Level (VI)

RFmxWCDMA Configure Reference Level (VI)

Owning Palette:

Configuration

Configures the reference level, which represents the maximum expected power of an RF input signal.

[IMAGE alt='RFmxWCDMA Configure Reference Level' src='rfmxwcdma_configure_reference_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Level specifies the reference level, which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_rf.html language=enus -->
## TOPIC 00051: rfmxwcdmavi/rfmxwcdma_configure_rf.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_rf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_rf.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure RF (VI)

RFmxWCDMA Configure RF (VI)

Owning Palette:

Configuration

Configures the RF properties of the signal specified by the selector string.

[IMAGE alt='RFmxWCDMA Configure RF' src='rfmxwcdma_configure_rf.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the center frequency of the acquired RF signal for a single carrier. For multicarrier measurements, the Center Frequency parameter specifies the reference frequency for the values in the Carrier Freq property. This value is expressed in Hz. The default value of this parameter is hardware dependent. |
|  | Reference Level specifies the reference level that represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |
|  | External Attenuation specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. This value is expressed in dB. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_trigger.html language=enus -->
## TOPIC 00052: rfmxwcdmavi/rfmxwcdma_configure_trigger.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_trigger.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Trigger (VI)

RFmxWCDMA Configure Trigger (VI)

Owning Palette:

Configuration

Configures the Reference Trigger you use to acquire the signal.

#### RFmxWCDMA Configure IQ Power Edge Trigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.

To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

[IMAGE alt='RFmxWCDMA Configure IQ Power Edge Trigger' src='rfmxwcdma_configure_iq_power_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | IQ Power Edge Source specifies the channel from which the device monitors the trigger. The default value of this parameter is hardware dependent. |
|  | IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
|  | IQ Power Edge Level specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative; and is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default value of this parameter is hardware dependent. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | Minimum Quiet Time Mode specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Manual. Manual (0) The minimum quiet time used for triggering is the value of the Minimum Quiet Time parameter. Auto (1) The measurement computes the minimum quiet time used for triggering. |
| Manual (0) | The minimum quiet time used for triggering is the value of the Minimum Quiet Time parameter. |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |
|  | Minimum Quiet Time specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. This value is expressed in seconds. The default value of this parameter is hardware dependent. |
|  | IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. The IQ Power Edge Level Type parameter is used only when you set the Trigger Type property to IQ Power Edge. Relative (0) The IQ Power Edge Level parameter is relative to the value of the Reference Level property. Absolute (1) The IQ Power Edge Level parameter specifies the absolute power. |
| Relative (0) | The IQ Power Edge Level parameter is relative to the value of the Reference Level property. |
| Absolute (1) | The IQ Power Edge Level parameter specifies the absolute power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA Configure Software Edge Trigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

[IMAGE alt='RFmxWCDMA Configure Software Edge Trigger' src='rfmxwcdma_configure_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA Configure Digital Edge Trigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

[IMAGE alt='RFmxWCDMA Configure Digital Edge Trigger' src='rfmxwcdma_configure_digital_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Digital Edge Source specifies the source terminal for the digital edge trigger. The default value of this parameter is hardware dependent. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. PXIe_DStarB (PXIe_DStarB) The trigger is received on the PXIe DStar B trigger line. TimerEvent (TimerEvent) The trigger is received from the timer event. |
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
| TimerEvent (TimerEvent) | The trigger is received from the timer event. |
|  | Digital Edge specifies the trigger edge to detect. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. |
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA Disable Trigger

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='RFmxWCDMA Disable Trigger' src='rfmxwcdma_disable_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_uplink_scrambling.html language=enus -->
## TOPIC 00053: rfmxwcdmavi/rfmxwcdma_configure_uplink_scrambling.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_uplink_scrambling.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_uplink_scrambling.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Uplink Scrambling (VI)

RFmxWCDMA Configure Uplink Scrambling (VI)

Owning Palette:

Configuration

Configures the uplink scrambling type and the scrambling code.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxWCDMA Configure Uplink Scrambling' src='rfmxwcdma_configure_uplink_scrambling.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Uplink Scrambling Type specifies the type of scrambling to use for the measurement. The default value is Long. Long (0) A long scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. Short (1) A short scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |
| Long (0) | A long scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |
| Short (1) | A short scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |
|  | Uplink Scrambling Code specifies the scrambling code for the uplink channel. The default value is 0. Valid values are 0 to 16,777,215. |
|  | Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_uplink_scrambling_(array).html language=enus -->
## TOPIC 00054: rfmxwcdmavi/rfmxwcdma_configure_uplink_scrambling_(array).html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_uplink_scrambling_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_uplink_scrambling_(array).html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Uplink Scrambling (Array) (VI)

RFmxWCDMA Configure Uplink Scrambling (Array) (VI)

Owning Palette:

Array VIs

Configures the scrambling code and the scrambling code type for all the carriers.

[IMAGE alt='RFmxWCDMA Configure Uplink Scrambling (Array)' src='rfmxwcdma_configure_uplink_scrambling_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Uplink Scrambling Type specifies the array of types of scrambling to use for the measurement. The default value is Long. Long (0) A long scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. Short (1) A short scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |
| Long (0) | A long scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |
| Short (1) | A short scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |
|  | Uplink Scrambling Code specifies the array of scrambling codes for the uplink channel. The default value is 0. Valid values are 0 to 16,777,215. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_uplink_test_model.html language=enus -->
## TOPIC 00055: rfmxwcdmavi/rfmxwcdma_configure_uplink_test_model.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_uplink_test_model.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_uplink_test_model.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Uplink Test Model (VI)

RFmxWCDMA Configure Uplink Test Model (VI)

Owning Palette:

Configuration

Configures the uplink test model.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxWCDMA Configure Uplink Test Model' src='rfmxwcdma_configure_uplink_test_model.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | UL Test Model specifies the uplink test model when you set the Channel Configuration Mode property to Test Model. Each test model is a set of channel configurations defined by the standard. Each uplink test model is a set of channel configurations as defined by the reference measurement channels in tables C.2.1, C.2.2, C.2.3, C.2.4, C.2.5, C.10.1.4, C.11.1.3, or C.11.1.4 of the 3GPP TS 34.121-1 specification. Released specifications from version 6.3.0, release 6 to version 11.5.0, release 11 are supported. Reference measurement channels in multiple releases of the specification can be the same. Each uplink test model name starts with R<n>, where n is the oldest release number with a given set of channel configurations. The default value is R6 C.2.1. R6 C.2.1 (0) The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.2 (1) The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.3 (2) The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.4 (3) The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.5 (4) The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.10.1.4 Subtest1 (5) The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest2 (6) The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest3 (7) The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest4 (8) The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest5 (9) The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest6 (10) The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. R7 C.10.1.4 Subtest1 (11) The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. R7 C.10.1.4 Subtest2 (12) The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. R7 C.10.1.4 Subtest3 (13) The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. R7 C.10.1.4 Subtest4 (14) The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest1 (15) The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest2 (16) The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest3 (17) The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest4 (18) The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest5 (19) The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. R8 C.11.1.3 Subtest1 (20) The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest2 (21) The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest3 (22) The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest4 (23) The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest5 (24) The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.4 Subtest1 (25) The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |
| R6 C.2.1 (0) | The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.2 (1) | The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.3 (2) | The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.4 (3) | The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.5 (4) | The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.10.1.4 Subtest1 (5) | The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest2 (6) | The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest3 (7) | The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest4 (8) | The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest5 (9) | The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest6 (10) | The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. |
| R7 C.10.1.4 Subtest1 (11) | The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest2 (12) | The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest3 (13) | The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest4 (14) | The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest1 (15) | The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest2 (16) | The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest3 (17) | The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest4 (18) | The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest5 (19) | The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. |
| R8 C.11.1.3 Subtest1 (20) | The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest2 (21) | The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest3 (22) | The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest4 (23) | The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest5 (24) | The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.4 Subtest1 (25) | The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |
|  | Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_uplink_test_model_(array).html language=enus -->
## TOPIC 00056: rfmxwcdmavi/rfmxwcdma_configure_uplink_test_model_(array).html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_uplink_test_model_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_uplink_test_model_(array).html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure Uplink Test Model (Array) (VI)

RFmxWCDMA Configure Uplink Test Model (Array) (VI)

Owning Palette:

Array VIs

Configures the uplink test model for all the carriers.

[IMAGE alt='RFmxWCDMA Configure Uplink Test Model (Array)' src='rfmxwcdma_configure_uplink_test_model_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | UL Test Model specifies the array of uplink test models when you set the Channel Configuration Mode property to Test Model. Each test model is a set of channel configurations defined by the standard. Each uplink test model is a set of channel configurations as defined by the reference measurement channels in tables C.2.1, C.2.2, C.2.3, C.2.4, C.2.5, C.10.1.4, C.11.1.3, or C.11.1.4 of the 3GPP TS 34.121-1 specification. Released specifications from version 6.3.0, release 6 to version 11.5.0, release 11 are supported. Reference measurement channels in multiple releases of the specification can be the same. Each uplink test model name starts with R<n>, where n is the oldest release number with a given set of channel configurations. The default value is R6 C.2.1. R6 C.2.1 (0) The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.2 (1) The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.3 (2) The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.4 (3) The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.5 (4) The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.10.1.4 Subtest1 (5) The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest2 (6) The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest3 (7) The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest4 (8) The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest5 (9) The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest6 (10) The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. R7 C.10.1.4 Subtest1 (11) The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. R7 C.10.1.4 Subtest2 (12) The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. R7 C.10.1.4 Subtest3 (13) The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. R7 C.10.1.4 Subtest4 (14) The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest1 (15) The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest2 (16) The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest3 (17) The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest4 (18) The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest5 (19) The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. R8 C.11.1.3 Subtest1 (20) The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest2 (21) The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest3 (22) The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest4 (23) The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest5 (24) The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.4 Subtest1 (25) The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |
| R6 C.2.1 (0) | The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.2 (1) | The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.3 (2) | The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.4 (3) | The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.5 (4) | The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.10.1.4 Subtest1 (5) | The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest2 (6) | The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest3 (7) | The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest4 (8) | The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest5 (9) | The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest6 (10) | The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. |
| R7 C.10.1.4 Subtest1 (11) | The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest2 (12) | The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest3 (13) | The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest4 (14) | The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest1 (15) | The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest2 (16) | The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest3 (17) | The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest4 (18) | The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest5 (19) | The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. |
| R8 C.11.1.3 Subtest1 (20) | The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest2 (21) | The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest3 (22) | The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest4 (23) | The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest5 (24) | The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.4 Subtest1 (25) | The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_user_defined_channel.html language=enus -->
## TOPIC 00057: rfmxwcdmavi/rfmxwcdma_configure_user_defined_channel.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_user_defined_channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_user_defined_channel.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure User Defined Channel (VI)

RFmxWCDMA Configure User Defined Channel (VI)

Owning Palette:

Configuration

Configures the spreading factor, spreading code, modulation type, and branch of each user-defined channel. Before calling this VI, you must configure the Num Channels property with the appropriate number of channels.

Use "carrier<*k*>/channel<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxWCDMA Configure User Defined Channel' src='rfmxwcdma_configure_user_defined_channel.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Spreading Factor specifies the spreading factor of the channel. The default value is 256. Valid values are 2, 4, 8, 16, 32, 64, 128, and 256. |
|  | Spreading Code specifies the spreading code of the channel. The default value is 0. Valid values are 0 to (Spreading factor - 1). |
|  | Modulation Type specifies the modulation type of the channel. The default value is BPSK/QPSK. BPSK/QPSK (0) The modulation type is BPSK. 4PAM/16QAM (1) The modulation type is 4 PAM. |
| BPSK/QPSK (0) | The modulation type is BPSK. |
| 4PAM/16QAM (1) | The modulation type is 4 PAM. |
|  | Branch specifies the branch on which the data is modulated. The default value is I. I (0) The signal is modulated in the in-phase branch. Q (1) The signal is modulated in the quadrature-phase branch. |
| I (0) | The signal is modulated in the in-phase branch. |
| Q (1) | The signal is modulated in the quadrature-phase branch. |
|  | Selector String specifies a selector string comprising of the signal name, carrier number, and channel number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0/channel0". Example: "carrier0/channel0" "signal::sig1/carrier0/channel0" You can use the RFmxWCDMA Build Channel String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_configure_user_defined_channel_(array).html language=enus -->
## TOPIC 00058: rfmxwcdmavi/rfmxwcdma_configure_user_defined_channel_(array).html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_configure_user_defined_channel_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_configure_user_defined_channel_(array).html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Configure User Defined Channel (Array) (VI)

RFmxWCDMA Configure User Defined Channel (Array) (VI)

Owning Palette:

Array VIs

Configures an array of spreading factors, spreading codes, modulation types, and branches of the user-defined channels. Before calling this VI, you must configure the Num Channels property with the appropriate number of user-defined channels.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxWCDMA Configure User Defined Channel (Array)' src='rfmxwcdma_configure_user_defined_channel_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Spreading Factor specifies an array of spreading factor of the channels. The default value is 256. Valid values are 2, 4, 8,16, 32, 64, 128, and 256. |
|  | Spreading Code specifies an array of spreading code of the channels. The default value is 0. Valid values are 0 to (Spreading factor - 1). |
|  | Modulation Type specifies an array of modulation types of the channels. The default value is BPSK/QPSK. BPSK/QPSK (0) The modulation type is BPSK. 4PAM/16QAM (1) The modulation type is 4 PAM. |
| BPSK/QPSK (0) | The modulation type is BPSK. |
| 4PAM/16QAM (1) | The modulation type is 4 PAM. |
|  | Branch specifies an array of branches on which the data is modulated in the channel. The default value is I. I (0) The signal is modulated in the in-phase branch. Q (1) The signal is modulated in the quadrature-phase branch. |
| I (0) | The signal is modulated in the in-phase branch. |
| Q (1) | The signal is modulated in the quadrature-phase branch. |
|  | Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_create_signal_configuration.html language=enus -->
## TOPIC 00059: rfmxwcdmavi/rfmxwcdma_create_signal_configuration.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_create_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_create_signal_configuration.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Create Signal Configuration (VI)

RFmxWCDMA Create Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal.

[IMAGE alt='RFmxWCDMA Create Signal Configuration' src='rfmxwcdma_create_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_delete_signal_configuration.html language=enus -->
## TOPIC 00060: rfmxwcdmavi/rfmxwcdma_delete_signal_configuration.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_delete_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_delete_signal_configuration.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Delete Signal Configuration (VI)

RFmxWCDMA Delete Signal Configuration (VI)

Owning Palette:

Advanced

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='RFmxWCDMA Delete Signal Configuration' src='rfmxwcdma_delete_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_get_all_named_result_names.html language=enus -->
## TOPIC 00061: rfmxwcdmavi/rfmxwcdma_get_all_named_result_names.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_get_all_named_result_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_get_all_named_result_names.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Get All Named Result Names (VI)

RFmxWCDMA Get All Named Result Names (VI)

Owning Palette:

Advanced

Returns the named result names of the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxWCDMA Get All Named Result Names' src='rfmxwcdma_get_all_named_result_names.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Result Names returns an array of result names. |
|  | Default Result Exists? indicates whether the default result exists. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_initiate.html language=enus -->
## TOPIC 00062: rfmxwcdmavi/rfmxwcdma_initiate.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_initiate.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Initiate (VI)

RFmxWCDMA Initiate (VI)

Owning Palette:

RFmx WCDMA VIs

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the RFmxWCDMA Property Node.

To get the status of measurements, use the [RFmxWCDMA Wait for Measurement Complete](../rfmxwcdmavi/rfmxwcdma_wait_for_measurement_complete.html) VI or the [RFmxWCDMA Check Measurement Status](../rfmxwcdmavi/rfmxwcdma_check_measurement_status.html) VI.

[IMAGE alt='RFmxWCDMA Initiate' src='rfmxwcdma_initiate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_modacc_configure_reference_waveform.html language=enus -->
## TOPIC 00063: rfmxwcdmavi/rfmxwcdma_modacc_configure_reference_waveform.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_modacc_configure_reference_waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_modacc_configure_reference_waveform.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA ModAcc Configure Reference Waveform (VI)

RFmxWCDMA ModAcc Configure Reference Waveform (VI)

Owning Palette:

ModAcc

Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster

ModAcc measurements.

This VI is used only when you set the ModAcc Sync Mode property to **Marker**.

[IMAGE alt='RFmxWCDMA ModAcc Configure Reference Waveform' src='rfmxwcdma_modacc_configure_reference_waveform.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Waveform specifies the ideal complex baseband reference waveform. x0 specifies the start time. This value is expressed in seconds. dx specifies the sample duration. This value is expressed in seconds. y specifies an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
|  | x0 specifies the start time. This value is expressed in seconds. |
|  | dx specifies the sample duration. This value is expressed in seconds. |
|  | y specifies an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_modacc_configure_synchronization_mode_and_interval.html language=enus -->
## TOPIC 00064: rfmxwcdmavi/rfmxwcdma_modacc_configure_synchronization_mode_and_interval.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_modacc_configure_synchronization_mode_and_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_modacc_configure_synchronization_mode_and_interval.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA ModAcc Configure Synchronization Mode and Interval (VI)

RFmxWCDMA ModAcc Configure Synchronization Mode and Interval (VI)

Owning Palette:

ModAcc

Configures the synchronization mode, measurement offset, and measurement length of the ModAcc measurement.

[IMAGE alt='RFmxWCDMA ModAcc Configure Synchronization Mode and Interval' src='rfmxwcdma_modacc_configure_synchronization_mode_and_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Mode specifies whether the measurement is performed from the frame, slot, or symbol boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the slot boundary. Arbitrary (2) The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the symbol boundary. Marker (3) The measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the Trigger. This is the fastest way to do a ModAcc measurement. This mode requires the Trigger Type property to be set to Digital and the trigger must occur at the start of the frame. For more information about Marker mode, refer to Marker Mode. |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the slot boundary. |
| Arbitrary (2) | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the symbol boundary. |
| Marker (3) | The measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the Trigger. This is the fastest way to do a ModAcc measurement. This mode requires the Trigger Type property to be set to Digital and the trigger must occur at the start of the frame. For more information about Marker mode, refer to Marker Mode. |
|  | Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. Valid values are [0, (15 - ModAcc Measurement Length)]. The sum of the ModAcc measurement offset and ModAcc measurement length must be less than or equal to 15. |
|  | Measurement Length specifies the duration for the modulation accuracy measurement. This value is expressed in slots. The default value is 1. Valid values are [1,(15 - ModAcc Measurement Offset)]. The sum of the ModAcc measurement offset and ModAcc measurement length must be less than or equal to 15. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_modacc_fetch.html language=enus -->
## TOPIC 00065: rfmxwcdmavi/rfmxwcdma_modacc_fetch.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_modacc_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_modacc_fetch.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA ModAcc Fetch (VI)

RFmxWCDMA ModAcc Fetch (VI)

Owning Palette:

Fetch

Fetches results of the ModAcc measurement.

#### RFmxWCDMA ModAcc Fetch EVM

Fetches the chip rate error, frequency error, RMS EVM, peak EVM, Rho, RMS magnitude error, and RMS phase error of the complex chips of the corrected composite signal for a carrier in the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch EVM' src='rfmxwcdma_modacc_fetch_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS EVM returns the RMS EVM of the composite signal for a carrier. This value is expressed as a percentage. |
|  | Peak EVM returns the peak EVM of the composite signal for a carrier. This value is expressed as a percentage. |
|  | Rho returns the correlation of the received signal with the reference signal normalized by the signal power for a carrier. Valid values range from 0 to 1.0, inclusive. The maximum value of Rho is 1.0, which indicates that the received signal and reference signal are perfectly correlated. |
|  | Chip Rate Error returns the chip rate error of the composite signal for a carrier. This value is expressed in ppm. |
|  | Frequency Error returns the frequency offset of the composite signal for a carrier. This value is expressed in Hz. |
|  | RMS Magnitude Error returns the RMS magnitude error of the composite signal for a carrier. This value is expressed in percentage. |
|  | RMS Phase Error returns the RMS phase error of the composite signal for a carrier. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch IQ Impairments

Fetches the I/Q origin offset, I/Q gain imbalance and I/Q quadrature error for a carrier in the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch IQ Impairments' src='rfmxwcdma_modacc_fetch_iq_impairments.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | I/Q Origin Offset returns the I/Q origin offset of the composite signal of a carrier. This value is expressed in dB. The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured. |
|  | I/Q Gain Imbalance returns the I/Q gain imbalance of the composite signal of a carrier. This value is expressed in dB. The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured. |
|  | I/Q Quadrature Error returns the I/Q quadrature error of the composite signal of a carrier. This value is expressed in degrees. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Multicarrier IQ Impairments

Fetches the I/Q impairments for a multicarrier signal.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Multicarrier IQ Impairments' src='rfmxwcdma_modacc_fetch_multicarrier_iq_impairments.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Multicarrier IQ Origin Offset returns the estimated I/Q origin offset of the multicarrier signal when the Transmitter Architecture property is set to LO per Band. This value is expressed in dB. This result is useful when the LO is at the center of the multicarrier signal. |
|  | Multicarrier IQ Gain Imbalance returns NaN. This parameter has been added for future use. |
|  | Multicarrier IQ Quadrature Error returns NaN. This parameter has been added for future use. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Peak CDE

Fetches the peak value among the code domain errors (CDEs) obtained with a fixed spreading factor of 4, along with the code number and branch that correspond to this peak value for a carrier in the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Peak CDE' src='rfmxwcdma_modacc_fetch_peak_cde.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Peak CDE returns the maximum CDE value for a carrier in the received signal. The CDEs are computed by despreading the descrambled error vector using a specific spreading factor. A fixed spreading factor of 4 is used. The CDE for every code with the specific spreading factor is defined as the ratio of the mean power of the descrambled and despread error vector to the mean power of the composite reference waveform. The CDEs for both I and Q branches are computed for each code. This value is expressed in dB. |
|  | Peak CDE Code returns the spreading code corresponding to the value of the Peak CDE parameter for a carrier in the received signal. |
|  | Peak CDE Branch returns the branch of the channel corresponding to the value of the Peak CDE parameter for a carrier in the received signal. I (0) The signal is modulated in the in-phase branch. Q (1) The signal is modulated in the quadrature branch. |
| I (0) | The signal is modulated in the in-phase branch. |
| Q (1) | The signal is modulated in the quadrature branch. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Peak Active CDE

Fetches the peak value among the code domain errors (CDEs) of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Peak Active CDE' src='rfmxwcdma_modacc_fetch_peak_active_cde.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Peak Active CDE returns the maximum value among the active code domain errors for a carrier. This value is expressed in dB. The active CDEs are computed by despreading the descrambled error vectors corresponding to each active channel with the appropriate active channel codes. The active CDE is defined as the ratio of the mean power of this despread error vector to the mean power of the composite reference waveform. |
|  | Peak Active CDE Spreading Factor returns the spreading factor of the channel corresponding to the value of the Peak Active CDE parameter for a carrier. |
|  | Peak Active CDE Code returns the spreading code of the channel corresponding to the value of the Peak Active CDE parameter for a carrier. |
|  | Peak Active CDE Branch returns the branch of the channel corresponding to the value of the Peak Active CDE parameter for a carrier. I (0) Signal is modulated on the in-phase branch. Q (1) Signal is modulated on the quadrature branch. |
| I (0) | Signal is modulated on the in-phase branch. |
| Q (1) | Signal is modulated on the quadrature branch. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch RCDE

Returns the peak relative code domain error (RCDE) value of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch RCDE' src='rfmxwcdma_modacc_fetch_rcde.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Peak RCDE returns the maximum value among the relative code domain errors (RCDEs) for all active channels for a carrier. This value is expressed in dB. The relative CDEs are computed by despreading the descrambled error vector corresponding to each active channel with the appropriate active channel codes. The RCDE is defined as the ratio of the mean power of this despread error vector to the mean power of the corresponding reference waveform. |
|  | Peak RCDE Spreading Factor returns the spreading factor of the channel corresponding to the value of the Peak RCDE parameter for a carrier. |
|  | Peak RCDE Code returns the spreading code of the channel corresponding to the value of the Peak RCDE parameter for a carrier. |
|  | Peak RCDE Branch returns the branch of the channel corresponding to the value of the Peak RCDE parameter for a carrier. I (0) The signal is modulated in the in-phase branch. Q (1) The signal is modulated in the quadrature branch. |
| I (0) | The signal is modulated in the in-phase branch. |
| Q (1) | The signal is modulated in the quadrature branch. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Number of Detected Channels

Fetches the number of detected channels in a carrier for the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Number of Detected Channels' src='rfmxwcdma_modacc_fetch_number_of_detected_channels.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Number of Detected Channels returns the number of detected channels when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, this parameter returns the number of configured channels. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Detected Channel

Returns the spreading factor, spreading code, modulation type, and branch of the detected channel of a carrier in the ModAcc measurement.

Use "carrier<n>/channel<k>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Detected Channel' src='rfmxwcdma_modacc_fetch_detected_channel.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, carrier number, and channel number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "carrier0/channel0" "signal::sig1/carrier0/channel0" "signal::sig1/result::r1/carrier0/channel0" "result::r1/carrier0/channel0" You can use the RFmxWCDMA Build Channel String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Detected Spreading Factor returns the spreading factors of the detected channels when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, the measurement returns the spreading factor of the configured channel of a carrier. |
|  | Detected Spreading Code returns the spreading code of the detected channels when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, the measurement returns the spreading code of the configured channel of a carrier. |
|  | Detected Mod Type returns the modulation type of the detected channels when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel configuration Mode property to User Defined or Test Model, the measurement returns the modulation type of the configured channel of a carrier. BPSK/QPSK (0) The modulation type is BPSK. 4PAM/16QAM (1) The modulation type is 4-PAM. |
| BPSK/QPSK (0) | The modulation type is BPSK. |
| 4PAM/16QAM (1) | The modulation type is 4-PAM. |
|  | Detected Branch returns the branch of the detected channels when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, the measurement returns the branch of the configured channel of a carrier. I (0) The signal is modulated in the in-phase branch. Q (1) The signal is modulated in the quadrature-phase branch. |
| I (0) | The signal is modulated in the in-phase branch. |
| Q (1) | The signal is modulated in the quadrature-phase branch. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch EVM (Array)

Fetches an array of chip rate errors, an array of frequency errors, an array of RMS EVMs, an array of peak EVMs, an array of Rhos, an array of RMS magnitude errors, and an array of RMS phase errors of the complex chips of the corrected signal corresponding to all the carriers in the ModAcc measurement. The array elements represent the result of each carrier in the measurement.

[IMAGE alt='RFmxWCDMA ModAcc Fetch EVM (Array)' src='rfmxwcdma_modacc_fetch_evm_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS EVM returns the array of RMS EVM values of the composite signal corresponding to the carriers. This value is expressed as a percentage. |
|  | Peak EVM returns the array of peak EVM values of the composite signal corresponding to the carriers. This value is expressed as a percentage. |
|  | Rho returns the array of correlation values of the received signal with the reference signal normalized by the signal power corresponding to the carriers. Valid values range from 0 to 1.0, inclusive. The maximum value of Rho is 1.0, which indicates that the received signal and reference signal are perfectly correlated. |
|  | Chip Rate Error returns the array of chip rate errors of the composite signal corresponding to the carriers. This value is expressed in ppm. |
|  | Frequency Error returns the array of frequency offset values of the composite signal corresponding to the carriers. This value is expressed in Hz. |
|  | RMS Magnitude Error returns the array of RMS magnitude errors of the composite signal corresponding to the carriers. This value is expressed in percentage. |
|  | RMS Phase Error returns the array of RMS phase error values of the composite signal corresponding to the carriers. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch IQ Impairments (Array)

Fetches the array of I/Q origin offsets, an array of I/Q gain imbalances, and an array of I/Q quadrature errors corresponding to all the carriers in the ModAcc measurement. The array elements represent result of each carrier in the measurement.

[IMAGE alt='RFmxWCDMA ModAcc Fetch IQ Impairments (Array)' src='rfmxwcdma_modacc_fetch_iq_impairments_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | I/Q Origin Offset returns the array of I/Q origin offset values of the composite signal. This value is expressed in dB. The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured. |
|  | I/Q Gain Imbalance returns the array of I/Q gain imbalance values of the composite signal. This value is expressed in dB. The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured. |
|  | I/Q Quadrature Error returns the array of I/Q quadrature error values of the composite signal. This value is expressed in degrees. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Number of Detected Channels (Array)

Fetches an array of number of detected channels of all the carriers in the ModAcc measurement.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Number of Detected Channels (Array)' src='rfmxwcdma_modacc_fetch_number_of_detected_channels_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Number of Detected Channels returns the array of the number of detected channels when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, this parameter returns the array of the number of configured channels. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Peak CDE (Array)

Fetches an array of peak CDE values obtained with a fixed spreading factor of 4 for all the carriers and the corresponding code numbers and branches. Each element in these arrays corresponds to the peak value among the code domain errors in each carrier.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Peak CDE (Array)' src='rfmxwcdma_modacc_fetch_peak_cde_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Peak CDE returns the array of maximum CDE values. This value is expressed in dB. The CDEs are computed by despreading the descrambled error vector using a specific spreading factor. A fixed spreading factor of 4 is used. The CDE for every code with the specific spreading factor is defined as the ratio of the mean power of the descrambled and despread error vector to the mean power of the composite reference waveform. The CDEs for both I and Q branches are computed for each code. |
|  | Peak CDE Code returns the array of spreading codes corresponding to the value of the Peak CDE parameter. |
|  | Peak CDE Branch returns the array of branches of the channel corresponding to the value of the Peak CDE parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Peak Active CDE (Array)

Fetches arrays of peak CDE values among all the active channels of a carrier, and the corresponding code numbers, spreading factors, and branches of the carriers. Each element in these arrays corresponds to the peak value among the code domain errors of all the active channels in each carrier.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Peak Active CDE (Array)' src='rfmxwcdma_modacc_fetch_peak_active_cde_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Peak Active CDE returns array of maximum values among the active code domain errors. This value is expressed in dB. The active CDEs are computed by despreading the descrambled error vectors corresponding to each active channel with the appropriate active channel codes. The active CDE is defined as the ratio of the mean power of this despread error vector to the mean power of the composite reference waveform. |
|  | Peak Active CDE Spreading Factor returns the array of spreading factors of the channel corresponding to the value of the Peak Active CDE parameter. |
|  | Peak Active CDE Code returns the array of spreading codes of the channel corresponding to the value of the Peak Active CDE parameter. |
|  | Peak Active CDE Branch returns the array of branch values of the channel corresponding to the value of the Peak Active CDE parameter. I (0) Signal is modulated on the in-phase branch. Q (1) Signal is modulated on the quadrature branch. |
| I (0) | Signal is modulated on the in-phase branch. |
| Q (1) | Signal is modulated on the quadrature branch. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch RCDE (Array)

Fetches arrays of peak relative CDE values of the active channels, of the carriers and the corresponding code numbers, spreading factors, and branches. Each element in these arrays corresponds to the peak value among the relative code domain errors of all the active channels in each carrier.

[IMAGE alt='RFmxWCDMA ModAcc Fetch RCDE (Array)' src='rfmxwcdma_modacc_fetch_rcde_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Peak RCDE returns the array of maximum value among the relative code domain errors (RCDEs) for all active channels. This value is expressed in dB. The relative CDEs are computed by despreading the descrambled error vector corresponding to each active channel with the appropriate active channel codes. The RCDE is defined as the ratio of the mean power of this despread error vector to the mean power of the corresponding reference waveform. |
|  | Peak RCDE Spreading Factor returns the array of spreading factors of the channel corresponding to the value of the Peak RCDE parameter. |
|  | Peak RCDE Code returns the array of spreading codes of the channel corresponding to the value of the Peak RCDE parameter. |
|  | Peak RCDE Branch returns the array of branches of the channel corresponding to the value of the Peak RCDE parameter. I (0) The signal is modulated in the in-phase branch. Q (1) The signal is modulated in the quadrature branch. |
| I (0) | The signal is modulated in the in-phase branch. |
| Q (1) | The signal is modulated in the quadrature branch. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Detected Channel (Array)

Fetches an array of spreading factors, an array of spreading codes, an array of modulation types, and an array of branches of the detected channels of the carriers, when you set the Channel Configuration Mode property to **Auto Detect** for the ModAcc measurement. When you set the Channel Configuration Mode property to **User Defined** or **Test Model**, it returns the corresponding results for the configured channels of all the carriers.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Detected Channel (Array)' src='rfmxwcdma_modacc_fetch_detected_channel_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Detected Spreading Factor returns an array of spreading factors of the detected channels, when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, the measurement returns an array of spreading factors of the configured channels. |
|  | Detected Spreading Code returns an array of spreading codes of the detected channels, when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, the measurement returns an array of spreading codes of the configured channels. |
|  | Detected Mod Type returns an array of modulation types of the detected channels, when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, the measurement returns an array of modulation types of the configured channels. BPSK/QPSK (0) The modulation type is BPSK. 4PAM/16QAM (1) The modulation type is 4-PAM. |
| BPSK/QPSK (0) | The modulation type is BPSK. |
| 4PAM/16QAM (1) | The modulation type is 4-PAM. |
|  | Detected Branch returns an array of branches of the detected channels when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, the measurement returns an array of branches of the configured channels. I (0) The signal is modulated in the in-phase branch. Q (1) The signal is modulated in the quadrature-phase branch. |
| I (0) | The signal is modulated in the in-phase branch. |
| Q (1) | The signal is modulated in the quadrature-phase branch. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch EVM Trace

Fetches the EVM trace of a carrier for the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch EVM Trace' src='rfmxwcdma_modacc_fetch_evm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | EVM returns the trace of error vector magnitude of the composite corrected signal. This value is expressed as a percentage. x0 returns the start time. This value is expressed in seconds. dx returns the chip duration. This value is expressed in seconds. y returns the EVM value. This value is expressed as a percentage. |
|  | x0 returns the start time. This value is expressed in seconds. |
|  | dx returns the chip duration. This value is expressed in seconds. |
|  | y returns the EVM value. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Magnitude Error Trace

Fetches the magnitude error trace of a carrier for the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Magnitude Error Trace' src='rfmxwcdma_modacc_fetch_magnitude_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Magnitude Error returns the trace of the magnitude errors of the composite corrected signal of a carrier. x0 returns the start time. This value is expressed in seconds. dx returns the chip duration. This value is expressed in seconds. y returns the magnitude error values. This value is expressed as a percentage. |
|  | x0 returns the start time. This value is expressed in seconds. |
|  | dx returns the chip duration. This value is expressed in seconds. |
|  | y returns the magnitude error values. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Phase Error Trace

Fetches the phase error trace of a carrier for the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Phase Error Trace' src='rfmxwcdma_modacc_fetch_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Phase Error returns the trace of phase errors of the composite corrected signal of a carrier. This value is expressed in degrees. x0 returns the start time. This value is expressed in seconds. dx returns the chip duration. This value is expressed in seconds. y returns an array of phase error values. This value is expressed in degrees. |
|  | x0 returns the start time. This value is expressed in seconds. |
|  | dx returns the chip duration. This value is expressed in seconds. |
|  | y returns an array of phase error values. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch RCDE Trace

Fetches the relative code domain errors (RCDE) trace of a carrier for the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch RCDE Trace' src='rfmxwcdma_modacc_fetch_rcde_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RCDE returns an array of RCDE values of the active channels. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Constellation Trace

Fetches the complex chips of the composite corrected signal of a carrier for the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Constellation Trace' src='rfmxwcdma_modacc_fetch_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Constellation returns an array of complex chips of the corrected signal of a carrier on which the ModAcc measurements are done. You can use these chips to obtain the constellation diagram. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA ModAcc Fetch Reference Waveform

Fetches the reference waveform for the ModAcc measurement.

[IMAGE alt='RFmxWCDMA ModAcc Fetch Reference Waveform' src='rfmxwcdma_modacc_fetch_reference_waveform.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Reference Waveform returns the ideal complex baseband reference waveform. x0 returns the start time. This value is expressed in seconds. dx returns the sample duration. This value is expressed in seconds. y returns an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
|  | x0 returns the start time. This value is expressed in seconds. |
|  | dx returns the sample duration. This value is expressed in seconds. |
|  | y returns an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_obw_configure_averaging.html language=enus -->
## TOPIC 00066: rfmxwcdmavi/rfmxwcdma_obw_configure_averaging.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_obw_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_obw_configure_averaging.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA OBW Configure Averaging (VI)

RFmxWCDMA OBW Configure Averaging (VI)

Owning Palette:

OBW

Configures averaging for the OBW measurement.

[IMAGE alt='RFmxWCDMA OBW Configure Averaging' src='rfmxwcdma_obw_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging of the spectrum for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one record to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one record to the next. |
| RMS (0) | The power spectrum is linearly averaged. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one record to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one record to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_obw_configure_rbw_filter.html language=enus -->
## TOPIC 00067: rfmxwcdmavi/rfmxwcdma_obw_configure_rbw_filter.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_obw_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_obw_configure_rbw_filter.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA OBW Configure RBW Filter (VI)

RFmxWCDMA OBW Configure RBW Filter (VI)

Owning Palette:

OBW

Configures the RBW filter.

[IMAGE alt='RFmxWCDMA OBW Configure RBW Filter' src='rfmxwcdma_obw_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. The default value is True. This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. If you set the RBW Filter Type parameter to FFT Based, the measurement calculates the RBW regardless of the value of this parameter. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
|  | RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. This value is expressed in Hz. The default value is 30 kHz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_obw_configure_sweep_time.html language=enus -->
## TOPIC 00068: rfmxwcdmavi/rfmxwcdma_obw_configure_sweep_time.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_obw_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_obw_configure_sweep_time.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA OBW Configure Sweep Time (VI)

RFmxWCDMA OBW Configure Sweep Time (VI)

Owning Palette:

OBW

Configures the sweep time interval.

[IMAGE alt='RFmxWCDMA OBW Configure Sweep Time' src='rfmxwcdma_obw_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement uses a sweep time value of one slot duration. |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement uses a sweep time value of one slot duration. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 666.66666700000007 microseconds. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_obw_fetch.html language=enus -->
## TOPIC 00069: rfmxwcdmavi/rfmxwcdma_obw_fetch.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_obw_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_obw_fetch.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA OBW Fetch (VI)

RFmxWCDMA OBW Fetch (VI)

Owning Palette:

Fetch

Fetches the OBW measurement results.

#### RFmxWCDMA OBW Fetch Measurement

Fetches the absolute and relative powers of the carrier for the OBW measurement. The relative power is relative to the total carrier power.

[IMAGE alt='RFmxWCDMA OBW Fetch Measurement' src='rfmxwcdma_obw_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Occupied Bandwidth returns the bandwidth containing 99% of the total integrated power of the acquired signal, around the center of the carriers. |
|  | Absolute Power returns the carrier power integrated over a bandwidth of 5 MHz. This value is expressed in dBm. |
|  | Stop Frequency returns the stop frequency of the Occupied Bandwidth parameter. |
|  | Start Frequency returns the start frequency of the Occupied Bandwidth parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA OBW Fetch Spectrum

Fetches the spectrum used for the OBW measurement.

[IMAGE alt='RFmxWCDMA OBW Fetch Spectrum' src='rfmxwcdma_obw_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power at each frequency bin. The value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power at each frequency bin. The value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_property_node.html language=enus -->
## TOPIC 00070: rfmxwcdmavi/rfmxwcdma_property_node.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_property_node.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_property_node.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Property Node (VI)

RFmxWCDMA Property Node (VI)

Owning Palette:

RFmx WCDMA VIs

Sets (writes) or gets (reads) RFmxWCDMA properties.

[IMAGE alt='RFmxWCDMA Property Node' src='rfmxwcdma_property_node.gif']

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_qevm_configure_averaging.html language=enus -->
## TOPIC 00071: rfmxwcdmavi/rfmxwcdma_qevm_configure_averaging.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_qevm_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_qevm_configure_averaging.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA QEVM Configure Averaging (VI)

RFmxWCDMA QEVM Configure Averaging (VI)

Owning Palette:

QEVM

Configures averaging for the QEVM measurement.

[IMAGE alt='RFmxWCDMA QEVM Configure Averaging' src='rfmxwcdma_qevm_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the QEVM measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the QEVM measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the QEVM measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_qevm_configure_measurement_length.html language=enus -->
## TOPIC 00072: rfmxwcdmavi/rfmxwcdma_qevm_configure_measurement_length.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_qevm_configure_measurement_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_qevm_configure_measurement_length.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA QEVM Configure Measurement Length (VI)

RFmxWCDMA QEVM Configure Measurement Length (VI)

Owning Palette:

QEVM

Configures the measurement length of the QEVM measurement.

[IMAGE alt='RFmxWCDMA QEVM Configure Measurement Length' src='rfmxwcdma_qevm_configure_measurement_length.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Length specifies the duration of the QEVM measurement. The value is expressed in chips. The default value is 2560. NI recommends that you set this property to n * 512, where the value of n can range from 1 to 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_qevm_fetch.html language=enus -->
## TOPIC 00073: rfmxwcdmavi/rfmxwcdma_qevm_fetch.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_qevm_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_qevm_fetch.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA QEVM Fetch (VI)

RFmxWCDMA QEVM Fetch (VI)

Owning Palette:

Fetch

Fetches the QEVM measurement results.

#### RFmxWCDMA QEVM Fetch EVM

Fetches the mean chip rate error, mean frequency error, mean RMS EVM, maximum peak EVM, mean magnitude error, and mean phase error of the complex chips of the corrected signal for the QEVM measurement.

[IMAGE alt='RFmxWCDMA QEVM Fetch EVM' src='rfmxwcdma_qevm_fetch_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean RMS EVM returns the mean of the RMS EVM values for a QPSK signal. This value is obtained by averaging the RMS EVMs over all averaging iterations. The number of acquisitions is specified by the value of the QEVM Averaging Count property. This value is expressed as a percentage. The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The RMS EVM is obtained from all the chips in the measurement interval. |
|  | Maximum Peak EVM returns the maximum value of the peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The peak EVM is obtained from all the chips in the measurement interval. |
|  | Mean Frequency Error returns the mean of the frequency errors for a QPSK signal. This value is expressed in Hz. This value is obtained by the mean of frequency errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal. |
|  | Mean Phase Error returns the mean of the RMS phase error values for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS phase errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval. |
|  | Mean Magnitude Error returns the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS magnitude errors over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval. |
|  | Mean Chip Rate Error returns the mean of the chip rate errors for a QPSK signal. This value is expressed in ppm. This value is obtained by averaging the chip rate errors over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The chip rate error is the estimated error between the chip clock rate of the transmitted signal and the chip clock rate at the receiver. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA QEVM Fetch IQ Impairments

Fetches the mean and maximum I/Q origin offsets, I/Q gain imbalances, and I/Q quadrature errors for the QEVM measurement.

[IMAGE alt='RFmxWCDMA QEVM Fetch IQ Impairments' src='rfmxwcdma_qevm_fetch_iq_impairments.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean I/Q Origin Offset returns the mean of I/Q origin offsets for a QPSK signal. This value is expressed in dB. This value is obtained by averaging the I/Q origin offsets over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured. |
|  | Mean I/Q Gain Imbalance returns the mean of the I/Q gain imbalances for a QPSK signal. This value is expressed in dB. This value is obtained by the I/Q gain imbalances obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured. This result is for future use. |
|  | Mean I/Q Quadrature Error returns the mean of the I/Q quadrature errors for a QPSK signal. This value is expressed in degrees. This value is obtained by the mean of I/Q quadrature errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured. This result is for future use. |
|  | Maximum I/Q Gain Imbalance returns the maximum value of I/Q gain imbalances for a QPSK signal. This value is expressed in dB. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured. This result is for future use. |
|  | Maximum I/Q Origin Offset returns the maximum I/Q origin offset for a QPSK signal. This value is expressed in dB. |
|  | Maximum I/Q Quadrature Error returns the maximum value of I/Q quadrature errors for a QPSK signal. This value is expressed in degrees. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the QEVM Averaging Count property. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured. This result is for future use. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA QEVM Fetch EVM Trace

Fetches the EVM trace for the QEVM measurement.

[IMAGE alt='RFmxWCDMA QEVM Fetch EVM Trace' src='rfmxwcdma_qevm_fetch_evm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | EVM returns the trace of error vector magnitude of the QPSK corrected signal for the last acquisition. This value is expressed as a percentage. x0 returns the start time. This value is expressed in seconds. dx returns the chip duration. This value is expressed in seconds. y returns the EVM value. This value is expressed as a percentage. |
|  | x0 returns the start time. This value is expressed in seconds. |
|  | dx returns the chip duration. This value is expressed in seconds. |
|  | y returns the EVM value. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA QEVM Fetch Magnitude Error Trace

Fetches the magnitude error trace for the QEVM measurement.

[IMAGE alt='RFmxWCDMA QEVM Fetch Magnitude Error Trace' src='rfmxwcdma_qevm_fetch_magnitude_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Magnitude Error returns the trace of the magnitude errors of the QPSK corrected signal for the last acquisition. x0 returns the start time. This value is expressed in seconds. dx returns the chip duration. This value is expressed in seconds. y returns the magnitude error values. This value is expressed as a percentage. |
|  | x0 returns the start time. This value is expressed in seconds. |
|  | dx returns the chip duration. This value is expressed in seconds. |
|  | y returns the magnitude error values. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA QEVM Fetch Phase Error Trace

Fetches the phase error trace for the QEVM measurement.

[IMAGE alt='RFmxWCDMA QEVM Fetch Phase Error Trace' src='rfmxwcdma_qevm_fetch_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Phase Error returns the trace of phase errors of the QPSK corrected signal for the last acquisition. This value is expressed in degrees. x0 returns the start time. This value is expressed in seconds. dx returns the chip duration. This value is expressed in seconds. y returns an array of phase error values. This value is expressed in degrees. |
|  | x0 returns the start time. This value is expressed in seconds. |
|  | dx returns the chip duration. This value is expressed in seconds. |
|  | y returns an array of phase error values. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA QEVM Fetch Constellation Trace

Fetches the complex chips of the composite corrected signal for the QEVM measurement.

[IMAGE alt='RFmxWCDMA QEVM Fetch Constellation Trace' src='rfmxwcdma_qevm_fetch_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Constellation returns an array of complex chips of the QPSK corrected signal for the last acquisition. You can use these chips to obtain the constellation diagram. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_reset_to_default.html language=enus -->
## TOPIC 00074: rfmxwcdmavi/rfmxwcdma_reset_to_default.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_reset_to_default.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_reset_to_default.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Reset to Default (VI)

RFmxWCDMA Reset to Default (VI)

Owning Palette:

Utility

Resets a signal to the default values.

[IMAGE alt='RFmxWCDMA Reset to Default' src='rfmxwcdma_reset_to_default.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_select_measurement.html language=enus -->
## TOPIC 00075: rfmxwcdmavi/rfmxwcdma_select_measurement.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_select_measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_select_measurement.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Select Measurement (VI)

RFmxWCDMA Select Measurement (VI)

Owning Palette:

RFmx WCDMA VIs

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

#### RFmxWCDMA Select Measurement (Single)

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='RFmxWCDMA Select Measurement (Single)' src='rfmxwcdma_select_measurement_(single).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement specifies the measurement to perform. The default value is ModAcc. ModAcc (0) Enables the ModAcc measurement. ACP (1) Enables the ACP measurement. CHP (2) Enables the CHP measurement. OBW (3) Enables the OBW measurement. SEM (4) Enables the SEM measurement. QEVM (5) Enables the QEVM measurement. SlotPhase (6) Enables the SlotPhase measurement. CDA (7) Enables the CDA measurement. SlotPower (8) Enables the SlotPower measurement. |
| ModAcc (0) | Enables the ModAcc measurement. |
| ACP (1) | Enables the ACP measurement. |
| CHP (2) | Enables the CHP measurement. |
| OBW (3) | Enables the OBW measurement. |
| SEM (4) | Enables the SEM measurement. |
| QEVM (5) | Enables the QEVM measurement. |
| SlotPhase (6) | Enables the SlotPhase measurement. |
| CDA (7) | Enables the CDA measurement. |
| SlotPower (8) | Enables the SlotPower measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA Select Measurement (Multiple)

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='RFmxWCDMA Select Measurement (Multiple)' src='rfmxwcdma_select_measurement_(multiple).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurements specifies the measurements to perform. You can specify one or more of the following measurements. The default is an empty array. ModAcc (0) Enables the ModAcc measurement. ACP (1) Enables the ACP measurement. CHP (2) Enables the CHP measurement. OBW (3) Enables the OBW measurement. SEM (4) Enables the SEM measurement. QEVM (5) Enables the QEVM measurement. SlotPhase (6) Enables the SlotPhase measurement. CDA (7) Enables the CDA measurement. SlotPower (8) Enables the SlotPower measurement. |
| ModAcc (0) | Enables the ModAcc measurement. |
| ACP (1) | Enables the ACP measurement. |
| CHP (2) | Enables the CHP measurement. |
| OBW (3) | Enables the OBW measurement. |
| SEM (4) | Enables the SEM measurement. |
| QEVM (5) | Enables the QEVM measurement. |
| SlotPhase (6) | Enables the SlotPhase measurement. |
| CDA (7) | Enables the CDA measurement. |
| SlotPower (8) | Enables the SlotPower measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurements. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_sem_configure_averaging.html language=enus -->
## TOPIC 00076: rfmxwcdmavi/rfmxwcdma_sem_configure_averaging.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_sem_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_sem_configure_averaging.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA SEM Configure Averaging (VI)

RFmxWCDMA SEM Configure Averaging (VI)

Owning Palette:

SEM

Configures averaging for the SEM measurement.

[IMAGE alt='RFmxWCDMA SEM Configure Averaging' src='rfmxwcdma_sem_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging of the spectrum for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one record to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one record to the next. |
| RMS (0) | The power spectrum is linearly averaged. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one record to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one record to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_sem_configure_sweep_time.html language=enus -->
## TOPIC 00077: rfmxwcdmavi/rfmxwcdma_sem_configure_sweep_time.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_sem_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_sem_configure_sweep_time.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA SEM Configure Sweep Time (VI)

RFmxWCDMA SEM Configure Sweep Time (VI)

Owning Palette:

SEM

Configures the sweep time interval.

[IMAGE alt='RFmxWCDMA SEM Configure Sweep Time' src='rfmxwcdma_sem_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement uses a sweep time value of one slot duration. |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement uses a sweep time value of one slot duration. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 666.66666700000007 microseconds. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_sem_fetch.html language=enus -->
## TOPIC 00078: rfmxwcdmavi/rfmxwcdma_sem_fetch.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_sem_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_sem_fetch.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA SEM Fetch (VI)

RFmxWCDMA SEM Fetch (VI)

Owning Palette:

Fetch

Fetches the SEM measurement results.

#### RFmxWCDMA SEM Fetch Measurement Status

Fetches the overall SEM measurement status based on the measurement limits and failure criteria for each offset segment, as defined in sections 5.9 , 5.9A, 5.9B, 5.9C, and 5.9D of the *3GPP TS 34.121-1* specification, version 11.5.0, release 11.

[IMAGE alt='RFmxWCDMA SEM Fetch Measurement Status' src='rfmxwcdma_sem_fetch_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status indicates the overall SEM measurement status based on the SEM Results Lower Offset Meas Status and the SEM Results Upper Offset Meas Status properties. Fail (0) The measurement status of at least one offset segment has failed. Pass (1) The measurement status of all offset segments have passed. |
| Fail (0) | The measurement status of at least one offset segment has failed. |
| Pass (1) | The measurement status of all offset segments have passed. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SEM Fetch Total Carrier Power

Fetches the total carrier power for the SEM measurement.

[IMAGE alt='RFmxWCDMA SEM Fetch Total Carrier Power' src='rfmxwcdma_sem_fetch_total_carrier_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Carrier Power returns the sum of all active carrier powers, where each carrier power corresponds to the value of the SEM Results Carrier Abs Pwr property. This value is expressed in dBm. For a single-carrier measurement, total carrier power is the same as carrier absolute power. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SEM Fetch Carrier Measurement

Fetches the absolute integrated power and the relative integrated power of the carrier for the SEM measurement. The relative power is relative to the total carrier power.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA SEM Fetch Carrier Measurement' src='rfmxwcdma_sem_fetch_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the carrier power. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the Center Frequency and Carrier Freq properties. This value is expressed in dBm. |
|  | Relative Integrated Power returns the carrier power relative to the total carrier power property. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SEM Fetch Carrier Measurement (Array)

Fetches an array of absolute integrated powers and an array of the relative integrated powers of the carriers for the SEM measurement. The relative powers are relative to the total carrier power.

[IMAGE alt='RFmxWCDMA SEM Fetch Carrier Measurement (Array)' src='rfmxwcdma_sem_fetch_carrier_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns an array of carrier power values. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the Center Frequency and Carrier Freq properties. This value is expressed in dBm. |
|  | Relative Integrated Power returns an array of carrier power values relative to the total carrier power of all enabled carriers. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SEM Fetch Lower Offset Power

Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the lower offset segment for the SEM measurement. All relative powers are relative to the total carrier power.

Use "offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA SEM Fetch Lower Offset Power' src='rfmxwcdma_sem_fetch_lower_offset_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxWCDMA Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the power measured in the lower, or negative, offset segment. This value is expressed in dBm. |
|  | Relative Integrated Power returns the power measured in the lower, or negative, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. |
|  | Absolute Peak Power returns the peak power measured in the lower, or negative, offset segment. This value is expressed in dBm. |
|  | Relative Peak Power returns the peak power measured in the lower, or negative, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. |
|  | Peak Frequency returns the frequency corresponding to the lower offset segment peak power. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SEM Fetch Lower Offset Power (Array)

Fetches an array of the absolute integrated powers, the relative integrated powers, the absolute peak powers, the relative peak powers, and frequencies at absolute peak powers of lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.

[IMAGE alt='RFmxWCDMA SEM Fetch Lower Offset Power (Array)' src='rfmxwcdma_sem_fetch_lower_offset_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns an array of the powers measured in the lower, or negative, offset segments. This value is expressed in dBm. |
|  | Relative Integrated Power returns an array of powers measured in the lower, or negative, offset segments relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. |
|  | Absolute Peak Power returns an array of peak power values measured in the lower, or negative, offset segments. This value is expressed in dBm. |
|  | Relative Peak Power returns an array of peak power values measured in the lower, or negative, offset segments relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. |
|  | Peak Frequency returns an array of frequencies corresponding to the lower offset segment peak power values. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SEM Fetch Upper Offset Power

Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the upper offset segment for the SEM measurement. The relative power is relative to the total carrier power.

Use "offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA SEM Fetch Upper Offset Power' src='rfmxwcdma_sem_fetch_upper_offset_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxWCDMA Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the power measured in the upper, or positive, offset segment. This value is expressed in dBm. |
|  | Relative Integrated Power returns the power measured in the upper, or positive, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. |
|  | Absolute Peak Power returns an array of peak power values measured in the lower, or negative, offset segments This value is expressed in dBm. |
|  | Relative Peak Power returns the peak power measured in the upper, or positive, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. |
|  | Peak Frequency returns the frequency corresponding to the upper offset segment peak power. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SEM Fetch Upper Offset Power (Array)

Returns an array of the absolute integrated powers and an array of the relative integrated powers, an array of the absolute peak powers and an array of the relative peak powers, and an array of the frequencies corresponding to peak absolute powers for upper offset segments for the SEM measurement. All relative powers are relative to the total carrier power.

[IMAGE alt='RFmxWCDMA SEM Fetch Upper Offset Power (Array)' src='rfmxwcdma_sem_fetch_upper_offset_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns an array of the powers measured in the upper, or positive, offset segments. This value is expressed in dBm. |
|  | Relative Integrated Power returns an array of powers measured in the upper, or positive, offset segments relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. |
|  | Absolute Peak Power returns an array of peak power values measured in the upper, or positive, offset segments. This value is expressed in dBm. |
|  | Relative Peak Power returns an array of peak power values measured in the upper, or positive, offset segments relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. |
|  | Peak Frequency returns an array of frequencies at which the peak power is observed in the upper, or positive, offset segments. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SEM Fetch Lower Offset Margin

Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.

Use "offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA SEM Fetch Lower Offset Margin' src='rfmxwcdma_sem_fetch_lower_offset_margin.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxWCDMA Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status indicates the measurement status based on the SEM Results Lower Offset Margin property. |
|  | Margin returns the margin of the lower offset segment. This value is expressed in dB. In a single carrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the lower offset segment is measured. The maximum of the relative spectrum trace with reference to the standard-defined relative mask limit in the lower offset segment is also measured. The higher value is the margin. In a multicarrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the lower offset segment is the margin. |
|  | Margin Frequency returns the frequency at which the margin occurred in the lower, or negative, offset segment. This value is expressed in Hz. |
|  | Margin Relative Power returns the power at which the margin occurred in the lower, or negative, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. |
|  | Margin Absolute Power returns the power at which the margin occurred in the lower, or negative, offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SEM Fetch Lower Offset Margin (Array)

Fetches an array of measurement status values, an array of margins, an array of frequencies at the margins, an array of the absolute powers, and an array of the relative powers at the margin frequencies for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.

[IMAGE alt='RFmxWCDMA SEM Fetch Lower Offset Margin (Array)' src='rfmxwcdma_sem_fetch_lower_offset_margin_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status indicates an array of measurement status values based on the values of the SEM Results Lower Offset Margin property corresponding to each lower offset segment. |
|  | Margin returns an array of margins of the lower offset segments. This value is expressed in dB. In a single carrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the lower offset segment is measured. The maximum of the relative spectrum trace with reference to the standard-defined relative mask limit, in the lower offset segment is also measured. The higher value is the margin. In a multicarrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the lower offset segment is the margin. |
|  | Margin Frequency returns an array of frequencies at which the margins occurred in the lower, or negative, offset segments This value is expressed in Hz. |
|  | Margin Relative Power returns an array of powers at which the margins occurred in the lower, or negative, offset segments relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. |
|  | Margin Absolute Power returns an array of powers at which the margins occurred in the lower, or negative, offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SEM Fetch Upper Offset Margin

Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power.

Use "offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWCDMA SEM Fetch Upper Offset Margin' src='rfmxwcdma_sem_fetch_upper_offset_margin.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxWCDMA Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status Indicates the measurement status based on the SEM Results Upper Offset Margin property. |
|  | Margin returns the margin of the upper offset segment. In a single carrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the upper offset segment is measured. The maximum of the relative spectrum trace with reference to the standard-defined relative mask limit in the upper offset segment is also measured. The higher value is the margin. In a multicarrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the upper offset segment is the margin. This value is expressed in dB. |
|  | Margin Frequency returns the frequency at which the margin occurred in the upper, or positive, segment. This value is expressed in Hz. |
|  | Margin Relative Power returns the power at which the margin occurred in the upper, or positive, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. |
|  | Margin Absolute Power returns the power at which the margin occurred in the upper, or positive, offset segment This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SEM Fetch Upper Offset Margin (Array)

Fetches an array of measurement status values, an array of margin values, an array of frequencies at the margins, an array of the absolute power values, and an array of the relative power values at the margin frequencies for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power.

[IMAGE alt='RFmxWCDMA SEM Fetch Upper Offset Margin (Array)' src='rfmxwcdma_sem_fetch_upper_offset_margin_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns an array of measurement status values based on the values of the SEM Results Upper Offset Margin property corresponding to each upper offset segment. |
|  | Margin returns an array of margins of the upper offset segments. In a single carrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the upper offset segment is measured. The maximum of the relative spectrum trace with reference to the standard-defined relative mask limit, in the upper offset segment, is also measured. The higher value is the margin. In a multicarrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the upper offset segment is the margin. This value is expressed in dB. |
|  | Margin Frequency returns an array of frequencies corresponding to the SEM Results Upper Offset Margin property. This value is expressed in Hz. |
|  | Margin Relative Power returns an array of powers at the frequency corresponding to the SEM Results Upper Offset Margin property, relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. |
|  | Margin Absolute Power returns an array of powers at the frequency corresponding to the SEM Results Upper Offset Margin property. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SEM Fetch Spectrum

Fetches the spectrum used for the SEM measurement.

[IMAGE alt='RFmxWCDMA SEM Fetch Spectrum' src='rfmxwcdma_sem_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the trace of power levels in the spectral domain. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns an array of averaged powers measured at each frequency bin. The value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns an array of averaged powers measured at each frequency bin. The value is expressed in dBm. |
|  | Relative Mask returns the trace of power levels representing the relative mask in the spectral domain. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns an array of power levels for relative mask. The value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns an array of power levels for relative mask. The value is expressed in dBm. |
|  | Absolute Mask returns the trace of power levels representing the absolute mask in the spectral domain. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns an array of power levels for absolute mask. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns an array of power levels for absolute mask. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_send_software_edge_trigger.html language=enus -->
## TOPIC 00079: rfmxwcdmavi/rfmxwcdma_send_software_edge_trigger.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_send_software_edge_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_send_software_edge_trigger.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Send Software Edge Trigger (VI)

RFmxWCDMA Send Software Edge Trigger (VI)

Owning Palette:

Configuration

Sends a trigger to the device when you use the [RFmxWCDMA Configure Trigger](rfmxwcdma_configure_trigger.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxWCDMA Initiate VI.

[IMAGE alt='RFmxWCDMA Send Software Edge Trigger' src='rfmxwcdma_send_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_slotphase_configure_synchronization_mode_and_interval.html language=enus -->
## TOPIC 00080: rfmxwcdmavi/rfmxwcdma_slotphase_configure_synchronization_mode_and_interval.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_slotphase_configure_synchronization_mode_and_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_slotphase_configure_synchronization_mode_and_interval.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA SlotPhase Configure Synchronization Mode and Interval (VI)

RFmxWCDMA SlotPhase Configure Synchronization Mode and Interval (VI)

Owning Palette:

SlotPhase

Configures the synchronization mode, the measurement offset, and the measurement length of the SlotPhase measurement.

[IMAGE alt='RFmxWCDMA SlotPhase Configure Synchronization Mode and Interval' src='rfmxwcdma_slotphase_configure_synchronization_mode_and_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Mode specifies whether the measurement is performed from the frame or the slot boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the slot boundary. |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the slot boundary. |
|  | Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. The valid values are any value greater than or equal to 0. |
|  | Measurement Length specifies the duration of the SlotPhase measurement. This value is expressed in slots. The default value is 15. The valid values are any value greater than or equal to 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_slotphase_fetch.html language=enus -->
## TOPIC 00081: rfmxwcdmavi/rfmxwcdma_slotphase_fetch.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_slotphase_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_slotphase_fetch.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA SlotPhase Fetch (VI)

RFmxWCDMA SlotPhase Fetch (VI)

Owning Palette:

Fetch

Fetches the SlotPhase measurement results.

#### RFmxWCDMA SlotPhase Fetch Measurement

Fetches the maximum phase discontinuity, discontinuity count greater than Limit 1, discontinuity count greater than Limit 2, and discontinuity minimum distance results.

[IMAGE alt='RFmxWCDMA SlotPhase Fetch Measurement' src='rfmxwcdma_slotphase_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Maximum Phase Discontinuity returns the maximum of all the measured phase discontinuity values at the slot boundaries. This value is expressed in degrees. |
|  | Discontinuity Count > Limit 1 returns the number of times the phase discontinuity values exceed the Limit 1 value for the acquired signal. Limit 1 is fixed at 36 degrees. |
|  | Discontinuity Count > Limit 2 returns the number of times the phase discontinuity values exceed the Limit 2 value for the acquired signal. Limit 2 is fixed at 66 degrees. |
|  | Discontinuity Minimum Distance returns the minimum distance between two phase discontinuity measurements exceeding the Limit 1 value. Limit 1 is fixed at 36 degrees. This value is expressed in slots. If there are no phase discontinuity values greater than Limit 1, or if there is only one phase discontinuity value greater than Limit 1, this result is not valid. In such a case, -1 is reported as the result. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SlotPhase Fetch Phase Discontinuities

Fetches the phase discontinuity values for the slot phase measurement.

[IMAGE alt='RFmxWCDMA SlotPhase Fetch Phase Discontinuities' src='rfmxwcdma_slotphase_fetch_phase_discontinuities.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Slot Phase Discontinuity returns the difference between the first extrapolated linear chip phase of the current slot and the last extrapolated linear chip phase of the preceding slot. The extrapolation is for the exclusion period of 25us on either side of the slot boundary. If you set the SlotPhase Transient Removal Enabled property to False, this parameter returns the difference between the first and last linear chip phase, at each slot boundary. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SlotPhase Fetch Chip Phase Error Trace

Fetches the chip phase error trace for the SlotPhase measurement.

[IMAGE alt='RFmxWCDMA SlotPhase Fetch Chip Phase Error Trace' src='rfmxwcdma_slotphase_fetch_chip_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Chip Phase Error returns the chip phase error. The chip phase error is the difference in phase between the test waveform and the reference waveform for every chip. Note This trace can get affected by the LO settling time of the hardware. You can use the RfmxInstr Frequency Settling property and the RfmxInstr Frequency Settling Units property, to allow more time for the LO to settle. x0 returns the start time. This value is expressed in seconds. dx returns the chip duration. This value is expressed in seconds. y returns an array of phase error values. This value is expressed in degrees. |
|  | Note This trace can get affected by the LO settling time of the hardware. You can use the RfmxInstr Frequency Settling property and the RfmxInstr Frequency Settling Units property, to allow more time for the LO to settle. |
|  | x0 returns the start time. This value is expressed in seconds. |
|  | dx returns the chip duration. This value is expressed in seconds. |
|  | y returns an array of phase error values. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWCDMA SlotPhase Fetch Chip Phase Error Linear Fit Trace

Fetches the chip phase error linear fit trace for the SlotPhase measurement.

[IMAGE alt='RFmxWCDMA SlotPhase Fetch Chip Phase Error Linear Fit Trace' src='rfmxwcdma_slotphase_fetch_chip_phase_error_linear_fit_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Chip Phase Error Linear Fit returns the linear-fit of the chip phase error after excluding 25 micro seconds at the start and end of each slot. The linear-fit is then extrapolated to the nearest slot boundaries on either side. The exclusion and extrapolation can be disabled if you set the SlotPhase Transient Removal Enabled property to False. Note This trace can get affected by the LO settling time of the hardware. You can use the RfmxInstr Frequency Settling property and the RfmxInstr Frequency Settling Units property, to allow more time for the LO to settle. x0 returns the start time. This value is expressed in seconds. dx returns the chip duration. This value is expressed in seconds. y returns the linear-fit chip phase error values. This value is expressed in degrees. |
|  | Note This trace can get affected by the LO settling time of the hardware. You can use the RfmxInstr Frequency Settling property and the RfmxInstr Frequency Settling Units property, to allow more time for the LO to settle. |
|  | x0 returns the start time. This value is expressed in seconds. |
|  | dx returns the chip duration. This value is expressed in seconds. |
|  | y returns the linear-fit chip phase error values. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_slotpower_configure_synchronization_mode_and_interval.html language=enus -->
## TOPIC 00082: rfmxwcdmavi/rfmxwcdma_slotpower_configure_synchronization_mode_and_interval.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_slotpower_configure_synchronization_mode_and_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_slotpower_configure_synchronization_mode_and_interval.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA SlotPower Configure Synchronization Mode and Interval (VI)

RFmxWCDMA SlotPower Configure Synchronization Mode and Interval (VI)

Owning Palette:

SlotPower

Configures the synchronization mode, measurement offset, and measurement length.

[IMAGE alt='RFmxWCDMA SlotPower Configure Synchronization Mode and Interval' src='rfmxwcdma_slotpower_configure_synchronization_mode_and_interval.gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
| --- | --- |
|  | Synchronization Mode specifies whether the measurement is performed from the frame or slot boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length property starting at Measurement Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots expressed by Measurement Length parameter, starting at Measurement Offset slots from the slot boundary. |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length property starting at Measurement Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by Measurement Length parameter, starting at Measurement Offset slots from the slot boundary. |
|  | Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. The valid values are any value greater than or equal to 0. |
|  | Measurement Length specifies the duration of the SlotPower measurement. This value is expressed in slots. The default value is 15. The valid values are any value greater than or equal to 1. |
|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_slotpower_fetch.html language=enus -->
## TOPIC 00083: rfmxwcdmavi/rfmxwcdma_slotpower_fetch.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_slotpower_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_slotpower_fetch.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA SlotPower Fetch (VI)

RFmxWCDMA SlotPower Fetch (VI)

Fetches the SlotPower measurement results.

#### RFmxWCDMA SlotPower Fetch Powers

Fetches the Slot Power and Slot Power delta for all the slots in the measurement length.

[IMAGE alt='RFmxWCDMA SlotPower Fetch Powers' src='rfmxwcdma_slotpower_fetch_powers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Slot Power returns an array of slot powers. This value is expressed in dBm. |
|  | Slot Power Delta returns an array of differences in powers between the adjacent slots. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/rfmxwcdma_wait_for_measurement_complete.html language=enus -->
## TOPIC 00084: rfmxwcdmavi/rfmxwcdma_wait_for_measurement_complete.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/rfmxwcdma_wait_for_measurement_complete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/rfmxwcdma_wait_for_measurement_complete.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmxWCDMA Wait for Measurement Complete (VI)

RFmxWCDMA Wait for Measurement Complete (VI)

Owning Palette:

Utility

Waits for the specified number of seconds for all the measurements to complete.

[IMAGE alt='RFmxWCDMA Wait for Measurement Complete' src='rfmxwcdma_wait_for_measurement_complete.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/sem_pal.html language=enus -->
## TOPIC 00085: rfmxwcdmavi/sem_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/sem_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/sem_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

SEM

SEM

Owning Palette:

Configuration

Use the VIs on this palette to configure spectral emission mask (SEM) measurements. You can also use the RFmxWCDMA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA SEM Configure Averaging | Configures averaging for the SEM measurement. |
| RFmxWCDMA SEM Configure Sweep Time | Configures the sweep time interval. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/slotphase_pal.html language=enus -->
## TOPIC 00086: rfmxwcdmavi/slotphase_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/slotphase_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/slotphase_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

SlotPhase

SlotPhase

Owning Palette:

Configuration

Use the VIs on this palette to configure SlotPhase measurements. You can also use the RFmxWCDMA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA SlotPhase Configure Synchronization Mode and Interval | Configures the synchronization mode, the measurement offset, and the measurement length of the SlotPhase measurement. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/slotpower_pal.html language=enus -->
## TOPIC 00087: rfmxwcdmavi/slotpower_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/slotpower_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/slotpower_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

SlotPower

SlotPower

Owning Palette:

Configuration

Use the VIs on this palette to configure SlotPower measurements. You can also use the RFmxWCDMA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA SlotPower Configure Synchronization Mode and Interval | Configures the synchronization mode, measurement offset, and measurement length. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/utility_pal.html language=enus -->
## TOPIC 00088: rfmxwcdmavi/utility_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/utility_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

Utility

Utility

Owning Palette:

RFmx WCDMA VIs

Use the VIs on this palette to configure the RFmx WCDMA utilities.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA Commit | Commits settings to the hardware. Calling this VI is optional. RFmxWCDMA commits settings to the hardware when you call the RFmxWCDMA Initiate VI. |
| RFmxWCDMA Reset to Default | Resets a signal to the default values. |
| RFmxWCDMA Wait for Measurement Complete | Waits for the specified number of seconds for all the measurements to complete. |
| RFmxWCDMA Check Measurement Status | Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |

<!--NI_TOPIC bundle=rfmx-wcdma-vi path=rfmxwcdmavi/wcdma_pal.html language=enus -->
## TOPIC 00089: rfmxwcdmavi/wcdma_pal.html

- bundle_id: `rfmx-wcdma-vi`
- source_path: `rfmxwcdmavi/wcdma_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-vi/raw/resource/enus/rfmxwcdmavi/wcdma_pal.html
- document_id: `rfmx-wcdma-vi`
- page_type: `leaf`
- content_type: ``

RFmx WCDMA VIs

RFmx WCDMA VIs

Use the VIs on this palette to perform WCDMA measurements. You can use the RFmxWCDMA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWCDMA Select Measurement | Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. |
| RFmxWCDMA Initiate | Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the RFmxWCDMA Property Node. |
| RFmxWCDMA Property Node | Sets (writes) or gets (reads) RFmxWCDMA properties. |

| Subpalette | Description |
| --- | --- |
| Configuration | Use the VIs on this palette to configure RFmxWCDMA measurements. You can use the RFmxWCDMA Property Node to configure additional properties. |
| Fetch | Use the VIs on this palette to fetch measurement results and traces. |
| Utility | Use the VIs on this palette to configure the RFmx WCDMA utilities. |
| Build String | Use the VIs on this palette to create strings for configurations and results that require a selector string. |
| Advanced | Use the VIs on this palette to use advanced features. |
