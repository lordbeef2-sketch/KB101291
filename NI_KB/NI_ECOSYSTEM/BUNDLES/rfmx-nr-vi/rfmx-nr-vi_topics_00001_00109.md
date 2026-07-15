# NI DOCUMENT BUNDLE: rfmx-nr-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-nr-vi start=1 end=109 -->
<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/acp_pal.html language=enus -->
## TOPIC 00001: ACP

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/acp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/acp_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

ACP

Owning Palette:

Configuration

Use the VIs on this palette to configure ACP measurements. You can use the [RFmxNR Property Node](../rfmxnrvi/rfmxnr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxNR ACP Configure Averaging | Configures averaging for the ACP measurement. |
| RFmxNR ACP Configure Sweep Time | Configures the sweep time. |
| RFmxNR ACP Configure Noise Compensation Enabled | Configures compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| RFmxNR ACP Configure Measurement Method | Configures the method for performing the ACP measurement. |
| RFmxNR ACP Configure Number of EUTRA Offsets | Configures the number of E-UTRA adjacent channels of the subblock. Use "subblock<n>" as the selector string to configure this VI. |
| RFmxNR ACP Configure Number of UTRA Offsets | Configures the number of UTRA adjacent channels of the subblock. Use "subblock<n>" as the selector string to configure this VI. |
| RFmxNR ACP Configure Number of NR Offsets | Configures the number of NR adjacent channels of the subblock. Use "subblock<n>" as the selector string to configure this VI. |
| RFmxNR ACP Configure Number of ENDC Offsets | Configures the number of ENDC adjacent channels of the subblock. |
| RFmxNR ACP Configure RBW Filter | Configures the resolution bandwidth (RBW) filter. |
| RFmxNR ACP Configure Power Units | Configures the unit for absolute power. |
| RFmxNR ACP Validate Noise Calibration Data | Indicates whether the ACP noise calibration data is valid for the configuration specified by the signal name in the Selector String parameter. |
| RFmxNR Build Subblock String | Creates the subblock string. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/advanced_pal.html language=enus -->
## TOPIC 00002: Advanced

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/advanced_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/advanced_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

Advanced

Owning Palette:

RFmx NR VIs

Use the VIs on this palette to use advanced features.

| Palette Object | Description |
| --- | --- |
| RFmxNR Abort Measurements | Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxNR Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error. |
| RFmxNR Analyze2 | Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the spectrum instance. |
| RFmxNR Create Signal Configuration | Creates a new instance of a signal. |
| RFmxNR Clone Signal Configuration | Creates a new instance of a signal by copying all the property values from an existing signal instance. |
| RFmxNR Delete Signal Configuration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxNR Delete Signal Configuration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxNR Get All Named Result Names | Returns the named result names of the signal that you specify in the Selector String parameter. |
| RFmxNR Clear Named Result | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxNR Clear All Named Results | Clears all results for the signal that you specify in the Selector String parameter. |
| RFmxNR Clear Noise Calibration Database | Clears the noise calibration database used for noise compensation. |

| Subpalette | Description |
| --- | --- |
| List | Use the VIs on this palette to use list mode features. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/build_string_pal.html language=enus -->
## TOPIC 00003: Build String

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/build_string_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/build_string_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

Build String

Owning Palette:

RFmx NR VIs

Use the VIs on this palette to create strings for configurations and results that require a selector string.

| Palette Object | Description |
| --- | --- |
| RFmxNR Build Signal String | Creates selector string. |
| RFmxNR Build Subblock String | Creates the subblock string. |
| RFmxNR Build Offset String | Creates the offset string. |
| RFmxNR Build Carrier String | Creates the carrier string. |
| RFmxNR Build Bandwidth Part String | Creates the bandwidth part string. |
| RFmxNR Build User String | Creates the user number string. |
| RFmxNR Build PUSCH String | Creates the PUSCH string. |
| RFmxNR Build PUSCH Cluster String | Creates a PUSCH Cluster string. |
| RFmxNR Build PDSCH String | Creates the PDSCH string. |
| RFmxNR Build PDSCH Cluster String | Creates a PDSCH Cluster string. |
| RFmxNR Build CORESET String | Creates the coreset string. |
| RFmxNR Build CORESET Cluster String | Creates the coreset cluster string. |
| RFmxNR Build PDCCH String | Creates the PDCCH string. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/chp_pal.html language=enus -->
## TOPIC 00004: CHP

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/chp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/chp_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

CHP

Owning Palette:

Configuration

Use the VIs on this palette to configure channel power (CHP) measurements. You can also use the [RFmxNR Property Node](../rfmxnrvi/rfmxnr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxNR CHP Configure Averaging | Configures averaging for the CHP measurement. |
| RFmxNR CHP Configure Sweep Time | Configures the sweep time. |
| RFmxNR CHP Configure RBW Filter | Configures the resolution bandwidth (RBW) filter. |
| RFmxNR CHP Validate Noise Calibration Data | Indicates whether the CHP noise calibration data is valid for the configuration specified by the signal name in the Selector String parameter. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/configuration_pal.html language=enus -->
## TOPIC 00005: Configuration

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/configuration_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

Configuration

Owning Palette:

RFmx NR VIs

Use the VIs on this palette to configure RFmxNR measurements. You can use the [RFmxNR Property Node](../rfmxnrvi/rfmxnr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxNR Configure RF | Configures the RF properties of the signal specified by the selector string. |
| RFmxNR Configure Frequency (Frequency) | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| RFmxNR Configure Reference Level | Configures the reference level which represents the maximum expected power of an RF input signal. |
| RFmxNR Configure External Attenuation | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. |
| RFmxNR Auto Level | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to calculate an approximate setting for the reference level. |
| RFmxNR Configure Trigger | Configures the reference trigger to use to acquire the signal. |
| RFmxNR Send Software Edge Trigger | Sends a trigger to the device when you use the RFmxNR Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. |
| RFmxNR Configure gNodeB Category | Configures the gNodeB Category of the signal being measured. |

| Subpalette | Description |
| --- | --- |
| ACP | Use the VIs on this palette to configure ACP measurements. You can use the RFmxNR Property Node to configure additional properties. |
| CHP | Use the VIs on this palette to configure channel power (CHP) measurements. You can also use the RFmxNR Property Node to configure additional properties. |
| OBW | Use the VIs on this palette to configure occupied bandwidth (OBW) measurements. You can also use the RFmxNR Property Node to configure additional properties. |
| SEM | Use the VIs on this palette to configure SEM measurements. You can also use the RFmxNR Property Node to configure additional properties. |
| PVT | Use the VIs on this palette to configure PVT measurements. You can use the RFmxNR Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/fetch_pal.html language=enus -->
## TOPIC 00006: Fetch

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/fetch_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/fetch_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

Fetch

Owning Palette:

RFmx NR VIs

Use the VIs on this palette to fetch measurement results and traces.

| Palette Object | Description |
| --- | --- |
| RFmxNR ModAcc Fetch | Fetches the ModAcc measurements. |
| RFmxNR ACP Fetch | Fetches the ACP measurements. |
| RFmxNR CHP Fetch | Fetches the CHP measurements. |
| RFmxNR OBW Fetch | Fetches the OBW measurements. |
| RFmxNR SEM Fetch | Fetches the SEM measurements. |
| RFmxNR PVT Fetch | Fetches the PVT measurements. |

| Subpalette | Description |
| --- | --- |
| Build String | Use the VIs on this palette to create strings for configurations and results that require a selector string. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/list_pal.html language=enus -->
## TOPIC 00007: List

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/list_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/list_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

List

Owning Palette:

Advanced

Use the VIs on this palette to use list mode features.

| Palette Object | Description |
| --- | --- |
| RFmxNR Create List | Creates a new list instance. Call the RFmxNR Create List Step VI to add steps to the list. Alternatively, you can also specify the number of list steps using the Num List Steps property. Supported devices:PXIe-5840/5841/5842 |
| RFmxNR Create List Step | Creates a new list step instance in a list. Supported devices:PXIe-5840/5841/5842 |
| RFmxNR Delete List | Deletes the list instance and all the list steps that you specify in the List Name parameter. When a list step is deleted, all the instances of properties associated with the list step are also removed. Supported devices:PXIe-5840/5841 |
| RFmxNR Build List String | Creates the list string. |
| RFmxNR Build List Step String | Creates the list step string. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/modacc_pal.html language=enus -->
## TOPIC 00008: ModAcc

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/modacc_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/modacc_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

ModAcc

Use the VIs on this palette to configure ModAcc measurements. You can use the [RFmxNR Property Node](../rfmxnrvi/rfmxnr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxNR ModAcc Configure Measurement Mode | Configures the measurement mode for the ModAcc measurement. |
| RFmxNR ModAcc Configure Noise Compensation Enabled | Configures whether to enable EVM noise compensation for the ModAcc measurement. Supported devices: PXIe-5830/5831/5832/5646/5840/5841/5842. |
| RFmxNR ModAcc Clear Noise Calibration Database | Clears the noise calibration database used for EVM noise compensation. |
| RFmxNR ModAcc Validate Calibration Data | Specifies whether calibration data is valid for the configuration specified by the signal name in the Selector String parameter. |
| RFmxNR ModAcc Configure Reference Waveform | Configures the reference waveform for the creation of reference data symbols for EVM computation. |
| RFmxNR ModAcc Auto Level | Performs the user-configured ModAcc measurement at multiple reference levels relative to the user-configured Reference Level property and configures the reference level corresponding to the lowest ModAcc Results Composite RMS EVM Mean result. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/nr_pal.html language=enus -->
## TOPIC 00009: RFmx NR VIs

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/nr_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/nr_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmx NR VIs

Use the VIs on this palette to perform NR measurements. You can use the [RFmxNR Property Node](../rfmxnrvi/rfmxnr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxNR Select Measurement | Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. |
| RFmxNR Initiate | Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the RFmxNR Wait for Measurement Complete VI or RFmxNR Check Measurement Status VI. |
| RFmxNR Property Node | Gets (reads), sets (writes), or resets (sets to default value) RFmxNR properties. |

| Subpalette | Description |
| --- | --- |
| Configuration | Use the VIs on this palette to configure RFmxNR measurements. You can use the RFmxNR Property Node to configure additional properties. |
| Fetch | Use the VIs on this palette to fetch measurement results and traces. |
| Utility | Use the VIs on this palette to configure RFmx NR utilities. |
| Build String | Use the VIs on this palette to create strings for configurations and results that require a selector string. |
| Advanced | Use the VIs on this palette to use advanced features. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/obw_pal.html language=enus -->
## TOPIC 00010: OBW

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/obw_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/obw_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

OBW

Owning Palette:

Configuration

Use the VIs on this palette to configure occupied bandwidth (OBW) measurements. You can also use the [RFmxNR Property Node](../rfmxnrvi/rfmxnr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxNR OBW Configure Averaging | Configures averaging for the OBW measurement. |
| RFmxNR OBW Configure Sweep Time | Configures the sweep time. |
| RFmxNR OBW Configure RBW Filter | Configures the resolution bandwidth (RBW) filter. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/pvt_pal.html language=enus -->
## TOPIC 00011: PVT

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/pvt_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/pvt_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

PVT

Owning Palette:

Configuration

Use the VIs on this palette to configure PVT measurements. You can use the RFmxNR Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxNR PVT Configure Averaging | Configures averaging for the PVT measurement. |
| RFmxNR PVT Configure Measurement Method | Configures the measurement method for PVT measurement. |
| RFmxNR PVT Configure OFF Power Exclusion Periods | Configures the time excluded from the off region before and after the burst. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_abort_measurements.html language=enus -->
## TOPIC 00012: RFmxNR Abort Measurements (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_abort_measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_abort_measurements.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Abort Measurements (VI)

Owning Palette:

Advanced

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxNR Initiate](rfmxnr_initiate.html) VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='RFmxNR Abort Measurements' src='rfmxnr_abort_measurements.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_acp_configure_averaging.html language=enus -->
## TOPIC 00013: RFmxNR ACP Configure Averaging (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_acp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_acp_configure_averaging.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ACP Configure Averaging (VI)

Owning Palette:

ACP

Configures averaging for the ACP measurement.

[IMAGE alt='RFmxNR ACP Configure Averaging' src='rfmxnr_acp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_acp_configure_measurement_method.html language=enus -->
## TOPIC 00014: RFmxNR ACP Configure Measurement Method (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_acp_configure_measurement_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_acp_configure_measurement_method.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ACP Configure Measurement Method (VI)

Owning Palette:

ACP

Configures the method for performing the ACP measurement.

[IMAGE alt='RFmxNR ACP Configure Measurement Method' src='rfmxnr_acp_configure_measurement_method.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Method specifies the method for performing the ACP measurement. The default value is Normal. Normal (0) The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. Dynamic Range (1) The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices:PXIe-5665/5668R Sequential FFT (2) The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of each chunk is defined by the ACP Sequential FFT Size property, and the FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used for the measurement. Use this method to optimize ACP Measurement speed. The accuracy of results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following properties have limited support when you set the ACP Measurement Method to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads 1 ACP Amplitude Correction Type RF Center Frequency Note For multi-span FFT, the averaging count should be 1. |
| Normal (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| Dynamic Range (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices:PXIe-5665/5668R |
| Sequential FFT (2) | The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of each chunk is defined by the ACP Sequential FFT Size property, and the FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used for the measurement. Use this method to optimize ACP Measurement speed. The accuracy of results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following properties have limited support when you set the ACP Measurement Method to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads 1 ACP Amplitude Correction Type RF Center Frequency Note For multi-span FFT, the averaging count should be 1. |
| Property | Supported Value |
| ACP RBW Auto | True |
| ACP RBW Filter Type | FFT Based |
| ACP Averaging Count | >=1 |
| ACP Noise Comp Enabled | False |
| ACP Num Analysis Threads | 1 |
| ACP Amplitude Correction Type | RF Center Frequency |
|  | Note For multi-span FFT, the averaging count should be 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_acp_configure_noise_compensation_enabled.html language=enus -->
## TOPIC 00015: RFmxNR ACP Configure Noise Compensation Enabled (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_acp_configure_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_acp_configure_noise_compensation_enabled.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ACP Configure Noise Compensation Enabled (VI)

Owning Palette:

ACP

Configures compensation of the channel powers for the inherent noise floor of the signal analyzer.

[IMAGE alt='RFmxNR ACP Configure Noise Compensation Enabled' src='rfmxnr_acp_configure_noise_compensation_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Noise Compensation Enabled specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. The default value is False. False (0) Disables compensation of the channel powers for the noise floor of the signal analyzer. True (1) Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842 |
| False (0) | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| True (1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842 |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_acp_configure_number_of_endc_offsets.html language=enus -->
## TOPIC 00016: RFmxNR ACP Configure Number of ENDC Offsets (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_acp_configure_number_of_endc_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_acp_configure_number_of_endc_offsets.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ACP Configure Number of ENDC Offsets (VI)

Owning Palette:

ACP

Configures the number of ENDC adjacent channels of the subblock.

[IMAGE alt='RFmxNR ACP Configure Number of ENDC Offsets' src='rfmxnr_acp_configure_number_of_endc_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of ENDC Offsets specifies the number of ENDC adjacent channel offsets to be configured at offset positions. The default value is dependent on 3GPP specification. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_acp_configure_number_of_eutra_offsets.html language=enus -->
## TOPIC 00017: RFmxNR ACP Configure Number of EUTRA Offsets (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_acp_configure_number_of_eutra_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_acp_configure_number_of_eutra_offsets.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ACP Configure Number of EUTRA Offsets (VI)

Owning Palette:

ACP

Configures the number of E-UTRA adjacent channels of the subblock.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxNR ACP Configure Number of EUTRA Offsets' src='rfmxnr_acp_configure_number_of_eutra_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of EUTRA Offsets specifies the number of E-UTRA adjacent channel offsets to be configured at offset positions. For downlink ACP measurement in frequency range 2, and for uplink ACP measurement, this parameter has to be 0. The default value is dependent on 3GPP specification. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_acp_configure_number_of_nr_offsets.html language=enus -->
## TOPIC 00018: RFmxNR ACP Configure Number of NR Offsets (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_acp_configure_number_of_nr_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_acp_configure_number_of_nr_offsets.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ACP Configure Number of NR Offsets (VI)

Owning Palette:

ACP

Configures the number of NR adjacent channels of the subblock.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxNR ACP Configure Number of NR Offsets' src='rfmxnr_acp_configure_number_of_nr_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of NR Offsets specifies the number of NR adjacent channel offsets to be configured at offset positions. The default value is dependent on 3GPP specification. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_acp_configure_number_of_utra_offsets.html language=enus -->
## TOPIC 00019: RFmxNR ACP Configure Number of UTRA Offsets (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_acp_configure_number_of_utra_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_acp_configure_number_of_utra_offsets.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ACP Configure Number of UTRA Offsets (VI)

Owning Palette:

ACP

Configures the number of UTRA adjacent channels of the subblock.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxNR ACP Configure Number of UTRA Offsets' src='rfmxnr_acp_configure_number_of_utra_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of UTRA Offsets specifies the number of UTRA adjacent channel offsets to be configured at offset positions. For uplink ACP measurement in frequency range 2, and for downlink ACP measurement, this parameter has to be 0. The default value is dependent on 3GPP specification. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_acp_configure_power_units.html language=enus -->
## TOPIC 00020: RFmxNR ACP Configure Power Units (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_acp_configure_power_units.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_acp_configure_power_units.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ACP Configure Power Units (VI)

Owning Palette:

ACP

Configures the unit for absolute power.

[IMAGE alt='RFmxNR ACP Configure Power Units' src='rfmxnr_acp_configure_power_units.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Power Units specifies the unit of absolute power. The default value is dBm. dBm (0) Indicates that the absolute power is expressed in dBm. dBm/Hz (1) Indicates that the absolute power is expressed in dBm/Hz. |
| dBm (0) | Indicates that the absolute power is expressed in dBm. |
| dBm/Hz (1) | Indicates that the absolute power is expressed in dBm/Hz. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_acp_configure_rbw_filter.html language=enus -->
## TOPIC 00021: RFmxNR ACP Configure RBW Filter (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_acp_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_acp_configure_rbw_filter.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ACP Configure RBW Filter (VI)

Owning Palette:

ACP

Configures the resolution bandwidth (RBW) filter.

[IMAGE alt='RFmxNR ACP Configure RBW Filter' src='rfmxnr_acp_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. The default value is True. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
|  | RBW specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 30 kHz. |
|  | RBW Filter Type specifies the shape of the RBW filter. The default value is FFT Based. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_acp_configure_sweep_time.html language=enus -->
## TOPIC 00022: RFmxNR ACP Configure Sweep Time (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_acp_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_acp_configure_sweep_time.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ACP Configure Sweep Time (VI)

Owning Palette:

ACP

Configures the sweep time.

[IMAGE alt='RFmxNR ACP Configure Sweep Time' src='rfmxnr_acp_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement sets the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement calculates the sweep time internally. For DL, the sweep time is calculated based on the value of the OBW RBW property, and for UL, it uses a sweep time of 1 ms. |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement calculates the sweep time internally. For DL, the sweep time is calculated based on the value of the OBW RBW property, and for UL, it uses a sweep time of 1 ms. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_acp_fetch.html language=enus -->
## TOPIC 00023: RFmxNR ACP Fetch (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_acp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_acp_fetch.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ACP Fetch (VI)

Owning Palette:

Fetch

Fetches the ACP measurements.

#### RFmxNR ACP Fetch Total Aggregated Power

Returns the sum of powers in all the subblocks.

[IMAGE alt='RFmxNR ACP Fetch Total Aggregated Power' src='rfmxnr_acp_fetch_total_aggregated_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Aggregated Power returns the total power of all the subblocks. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ACP Fetch Subblock Measurement

Fetches the power, integration bandwidth, and center frequency of the subblock.

[IMAGE alt='RFmxNR ACP Fetch Subblock Measurement' src='rfmxnr_acp_fetch_subblock_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Subblock Power returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. This includes the power in inter-carrier gaps within a subblock. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | Integration Bandwidth returns the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within a subblock. This value is expressed in Hz. |
|  | Frequency returns the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ACP Fetch Component Carrier Measurement

Returns the absolute and relative powers measured in the component carriers.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ACP Fetch Component Carrier Measurement' src='rfmxnr_acp_fetch_component_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | Relative Power returns the component carrier power relative to its subblock power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ACP Fetch Component Carrier Measurement (Array)

Returns an array of the absolute and relative powers measured in the component carriers.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ACP Fetch Component Carrier Measurement (Array)' src='rfmxnr_acp_fetch_component_carrier_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns an array of the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | Relative Power returns an array of the component carrier power relative to its subblock power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ACP Fetch Offset Measurement

Returns the absolute and relative power of the lower and upper offset channel. The relative power is relative to subblock power.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ACP Fetch Offset Measurement' src='rfmxnr_acp_fetch_offset_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Lower Relative Power returns the power in lower (negative) offset channel relative to the total aggregated power. This value is expressed in dB. |
|  | Upper Relative Power returns the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. |
|  | Upper Absolute Power returns the upper offset channel power. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | Lower Absolute Power returns the lower offset channel power. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ACP Fetch Offset Measurement (Array)

Returns an array of the absolute and relative power of the lower and upper offset channel.

The relative power is relative to the subblock power. The order of the offsets in the result array is UTRA (1, 2, …k) and NR (1, 2, …n) for Uplink, and EUTRA (1, 2, …m) and NR (1, 2, …n) for Downlink, where k, m, and n are the number of UTRA offsets, number of EUTRA offsets, and number of NR offsets, respectively.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ACP Fetch Offset Measurement (Array)' src='rfmxnr_acp_fetch_offset_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Lower Relative Power returns an array of the power in lower (negative) offset channel relative to the total aggregated power. This value is expressed in dB. |
|  | Upper Relative Power returns an array of the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. |
|  | Upper Absolute Power returns an array of the upper offset channel power. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | Lower Absolute Power returns an array of the lower offset channel power. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ACP Fetch Spectrum

Fetches the spectrum used for ACP measurements.

[IMAGE alt='RFmxNR ACP Fetch Spectrum' src='rfmxnr_acp_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the spectrum. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the array of averaged power measured at each frequency bin. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the array of averaged power measured at each frequency bin. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ACP Fetch Relative Powers Trace

Fetches the relative powers trace for ACP measurement.

[IMAGE alt='RFmxNR ACP Fetch Relative Powers Trace' src='rfmxnr_acp_fetch_relative_powers_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Relative Powers returns the trace of component carrier power relative to its subblock power. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns an array of the relative power measured in each channel relative to total aggregated power. This value is expressed in dB. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns an array of the relative power measured in each channel relative to total aggregated power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ACP Fetch Absolute Powers Trace

Fetches the absolute powers trace for ACP measurement.

[IMAGE alt='RFmxNR ACP Fetch Absolute Powers Trace' src='rfmxnr_acp_fetch_absolute_powers_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Powers returns the trace of power measured over the integration bandwidth of the carrier. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns an array the power measured in each channel. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns an array the power measured in each channel. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_acp_validate_noise_calibration_data.html language=enus -->
## TOPIC 00024: RFmxNR ACP Validate Noise Calibration Data (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_acp_validate_noise_calibration_data.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_acp_validate_noise_calibration_data.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ACP Validate Noise Calibration Data (VI)

Owning Palette:

ACP

Indicates whether the ACP noise calibration data is valid for the configuration specified by the signal name in the **Selector String** parameter.

[IMAGE alt='RFmxNR ACP Validate Noise Calibration Data' src='rfmxnr_acp_validate_noise_calibration_data.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Noise Calibration Data Valid returns whether the calibration data is valid. False (0) Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. True (1) Returns true if the calibration data is present for the configuration specified by the signal name in the Selector String parameter. |
| False (0) | Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. |
| True (1) | Returns true if the calibration data is present for the configuration specified by the signal name in the Selector String parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_analyze2.html language=enus -->
## TOPIC 00025: RFmxNR Analyze2 (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_analyze2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_analyze2.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Analyze2 (VI)

Owning Palette:

Advanced

Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the spectrum instance.

#### RFmxNR Analyze (IQ, 1 Wfm)

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?topicname=rfmxinstrprop/attr27.html) property value is either **IQ** or **IQ or Spectral**.

When using the Analysis-Only mode in RFmxNR, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmxNR Commit VI. |
| --- | --- |

[IMAGE alt='RFmxNR Analyze (IQ 1 Wfm)' src='rfmxnr_analyze_(iq_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 specifies the start time of the input Y array. This value is expressed in seconds. dx specifies the frequency interval between data points in the spectrum. y specifies the array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input Y array. This value is expressed in seconds. |
|  | dx specifies the frequency interval between data points in the spectrum. |
|  | y specifies the array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR Analyze (Spectrum, 1 Wfm)

Performs the enabled measurements on the I/Q complex waveform that you specify in **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?topicname=rfmxinstrprop/attr27.html) property value is either **Spectral** or **IQ or Spectral**.

When using the Analysis-Only mode in RFmxNR, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmxNR Commit VI. |
| --- | --- |

[IMAGE alt='RFmxNR Analyze (Spectrum 1 Wfm)' src='rfmxnr_analyze_(spectrum_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Spectrum specifies the data for a spectrum waveform. x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y contains the real-value power spectrum. |
|  | x0 specifies the start frequency of the spectrum. This value is expressed in Hz. |
|  | dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y contains the real-value power spectrum. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_auto_level.html language=enus -->
## TOPIC 00026: RFmxNR Auto Level (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_auto_level.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Auto Level (VI)

Owning Palette:

Configuration

Examines the input signal to calculate the peak power level and sets it as the value of the [Reference Level](/csh?topicname=rfmxnrprop/attr900002.html) property. Use this VI to calculate an approximate setting for the reference level.

The RFmxNR Auto Level VI completes the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

When using NI-PXIe 5663, NI-PXIe 5665, or NI-PXIe 5668R device, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxNR Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='RFmxNR Auto Level' src='rfmxnr_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Interval specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the signal analyzer. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Reference Level returns the estimated peak power level of the input signal. This value is expressed in dBm. The default value of this parameter is hardware dependent. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_bandwidth_part_string.html language=enus -->
## TOPIC 00027: RFmxNR Build Bandwidth Part String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_bandwidth_part_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_bandwidth_part_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build Bandwidth Part String (VI)

Owning Palette:

Build String

Creates the bandwidth part string.

[IMAGE alt='RFmxNR Build Bandwidth Part String' src='rfmxnr_build_bandwidth_part_string.gif']

|  | Bandwidth Part Number specifies the bandwidth part number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_carrier_string.html language=enus -->
## TOPIC 00028: RFmxNR Build Carrier String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_carrier_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_carrier_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build Carrier String (VI)

Owning Palette:

Build String

Creates the carrier string.

[IMAGE alt='RFmxNR Build Carrier String' src='rfmxnr_build_carrier_string.gif']

|  | Carrier Number specifies the carrier number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_coreset_cluster_string.html language=enus -->
## TOPIC 00029: RFmxNR Build CORESET Cluster String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_coreset_cluster_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_coreset_cluster_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build CORESET Cluster String (VI)

Owning Palette:

Build String

Creates the coreset cluster string.

[IMAGE alt='RFmxNR Build CORESET Cluster String' src='rfmxnr_build_coreset_cluster_string.gif']

|  | CORESET Cluster Number specifies the CORESET cluster number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number, bandwidth part number, and coreset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/carrier0/bwp0/coreset0" "signal::sig1/subblock0/carrier0/bwp0/coreset0" "result::r1/subblock0/carrier0/bwp0/coreset0" "signal::sig1/result::r1/subblock0/carrier0/bwp0/coreset0" You can use the RFmxNR Build CORESET String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_coreset_string.html language=enus -->
## TOPIC 00030: RFmxNR Build CORESET String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_coreset_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_coreset_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build CORESET String (VI)

Owning Palette:

Build String

Creates the coreset string.

[IMAGE alt='RFmxNR Build CORESET String' src='rfmxnr_build_coreset_string.gif']

|  | CORESET Number specifies the CORESET number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and bandwidth part number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/carrier0/bwp0" "signal::sig1/subblock0/carrier0/bwp0" "result::r1/subblock0/carrier0/bwp0" "signal::sig1/result::r1/subblock0/carrier0/bwp0" You can use the RFmxNR Build Bandwidth Part String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_list_step_string.html language=enus -->
## TOPIC 00031: RFmxNR Build List Step String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_list_step_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_list_step_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build List Step String (VI)

Owning Palette:

List

Creates the list step string.

[IMAGE alt='RFmxNR Build List Step String' src='rfmxnr_build_list_step_string.gif']

|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) for the default result instance. Example: "result::r1" "r1" |
| --- | --- |
|  | Selector String specifies the list name. This input accepts the list name with or without the "list::" prefix. The default value is "" (empty string). Example: "list::samplelist1" "samplelist1" |
|  | List Step Number specifies the step number for building the selector string. The default value is 0, which corresponds to the first step. When you use -1 as the step number, all steps are considered. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_list_string.html language=enus -->
## TOPIC 00032: RFmxNR Build List String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_list_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_list_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build List String (VI)

Owning Palette:

List

Creates the list string.

[IMAGE alt='RFmxNR Build List String' src='rfmxnr_build_list_string.gif']

|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) for the default result instance. Example: "result::r1" "r1" |
| --- | --- |
|  | List Name specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. The default value is "" (empty string). Example: "list::samplelist1" "samplelist1" |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_offset_string.html language=enus -->
## TOPIC 00033: RFmxNR Build Offset String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_offset_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_offset_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build Offset String (VI)

Owning Palette:

SEM

Creates the offset string.

[IMAGE alt='RFmxNR Build Offset String' src='rfmxnr_build_offset_string.gif']

|  | Offset Number specifies the offset number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_pdcch_string.html language=enus -->
## TOPIC 00034: RFmxNR Build PDCCH String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_pdcch_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_pdcch_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build PDCCH String (VI)

Owning Palette:

Build String

Creates the PDCCH string.

[IMAGE alt='RFmxNR Build PDCCH String' src='rfmxnr_build_pdcch_string.gif']

|  | PDCCH Number specifies the PDCCH number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number, bandwidth part number, and coreset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/carrier0/bwp0/coreset0" "signal::sig1/subblock0/carrier0/bwp0/coreset0" "result::r1/subblock0/carrier0/bwp0/coreset0" "signal::sig1/result::r1/subblock0/carrier0/bwp0/coreset0" You can use the RFmxNR Build CORESET String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_pdsch_cluster_string.html language=enus -->
## TOPIC 00035: RFmxNR Build PDSCH Cluster String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_pdsch_cluster_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_pdsch_cluster_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build PDSCH Cluster String (VI)

Owning Palette:

Build String

Creates a PDSCH Cluster string.

[IMAGE alt='RFmxNR Build PDSCH Cluster String' src='rfmxnr_build_pdsch_cluster_string.gif']

|  | PDSCH Cluster Number specifies the PDSCH cluster number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, bandwidth part number, user number, and pdsch number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/carrier0/bwp0/user0/pdsch0" "signal::sig1/subblock0/carrier0/bwp0/user0/pdsch0" "signal::sig1/result::r1/subblock0/carrier0/bwp/user0/pdsch0" "result::r1/subblock0/carrier0/bwp0/user0/pdsch0" You can use the RFmxNR Build PDSCH String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_pdsch_string.html language=enus -->
## TOPIC 00036: RFmxNR Build PDSCH String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_pdsch_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_pdsch_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build PDSCH String (VI)

Owning Palette:

Build String

Creates the PDSCH string.

[IMAGE alt='RFmxNR Build PDSCH String' src='rfmxnr_build_pdsch_string.gif']

|  | PDSCH Number specifies the PDSCH number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, bandwidth part number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/carrier0/bwp0/user0" "signal::sig1/subblock0/carrier0/bwp0/user0" "signal::sig1/result::r1/subblock0/carrier0/bwp/user0" "result::r1/subblock0/carrier0/bwp0/user0" You can use the RFmxNR Build User String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_pusch_cluster_string.html language=enus -->
## TOPIC 00037: RFmxNR Build PUSCH Cluster String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_pusch_cluster_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_pusch_cluster_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build PUSCH Cluster String (VI)

Owning Palette:

Build String

Creates a PUSCH Cluster string.

[IMAGE alt='RFmxNR Build PUSCH Cluster String' src='rfmxnr_build_pusch_cluster_string.gif']

|  | PUSCH Cluster Number specifies the PUSCH cluster number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, bandwidth part number, user number, and pusch number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/carrier0/bwp0/user0/pusch0" "signal::sig1/subblock0/carrier0/bwp0/user0/pusch0" "signal::sig1/result::r1/subblock0/carrier0/bwp/user0/pusch0" "result::r1/subblock0/carrier0/bwp0/user0/pusch0" You can use the RFmxNR Build PUSCH String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_pusch_string.html language=enus -->
## TOPIC 00038: RFmxNR Build PUSCH String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_pusch_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_pusch_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build PUSCH String (VI)

Owning Palette:

Build String

Creates the PUSCH string.

[IMAGE alt='RFmxNR Build PUSCH String' src='rfmxnr_build_pusch_string.gif']

|  | PUSCH Number specifies the PUSCH number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, bandwidth part number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/carrier0/bwp0/user0" "signal::sig1/subblock0/carrier0/bwp0/user0" "signal::sig1/result::r1/subblock0/carrier0/bwp/user0" "result::r1/subblock0/carrier0/bwp0/user0" You can use the RFmxNR Build User String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_signal_string.html language=enus -->
## TOPIC 00039: RFmxNR Build Signal String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_signal_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_signal_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build Signal String (VI)

Owning Palette:

Build String

Creates selector string.

[IMAGE alt='RFmxNR Build Signal String' src='rfmxnr_build_signal_string.gif']

|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
| --- | --- |
|  | Signal Name specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Example: "signal::sig1" "sig1" |
|  | Selector String returns the selector string. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_subblock_string.html language=enus -->
## TOPIC 00040: RFmxNR Build Subblock String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_subblock_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_subblock_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build Subblock String (VI)

Owning Palette:

SEM

Creates the subblock string.

[IMAGE alt='RFmxNR Build Subblock String' src='rfmxnr_build_subblock_string.gif']

|  | Subblock Number specifies the number of subblocks that are configured in the non-contiguous carrier aggregation. Set this parameter to 1, which is the default, for single carrier and intra-band contiguous carrier aggregation. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_build_user_string.html language=enus -->
## TOPIC 00041: RFmxNR Build User String (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_build_user_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_build_user_string.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Build User String (VI)

Owning Palette:

Build String

Creates the user number string.

[IMAGE alt='RFmxNR Build User String' src='rfmxnr_build_user_string.gif']

|  | User Number specifies the user number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and bandwidth part number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/carrier0/bwp0" "signal::sig1/subblock0/carrier0/bwp0" "result::r1/subblock0/carrier0/bwp0" "signal::sig1/result::r1/subblock0/carrier0/bwp0" You can use the RFmxNR Build Bandwidth Part String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_check_measurement_status.html language=enus -->
## TOPIC 00042: RFmxNR Check Measurement Status (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_check_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_check_measurement_status.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Check Measurement Status (VI)

Owning Palette:

Utility

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='RFmxNR Check Measurement Status' src='rfmxnr_check_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | done? indicates whether the measurement is complete. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_chp_configure_averaging.html language=enus -->
## TOPIC 00043: RFmxNR CHP Configure Averaging (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_chp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_chp_configure_averaging.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR CHP Configure Averaging (VI)

Owning Palette:

CHP

Configures averaging for the CHP measurement.

[IMAGE alt='RFmxNR CHP Configure Averaging' src='rfmxnr_chp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_chp_configure_rbw_filter.html language=enus -->
## TOPIC 00044: RFmxNR CHP Configure RBW Filter (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_chp_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_chp_configure_rbw_filter.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR CHP Configure RBW Filter (VI)

Owning Palette:

CHP

Configures the resolution bandwidth (RBW) filter.

[IMAGE alt='RFmxNR CHP Configure RBW Filter' src='rfmxnr_chp_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. The default value is True. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
|  | RBW specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 30 kHz. |
|  | RBW Filter Type specifies the shape of the RBW filter. The default value is FFT Based. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_chp_configure_sweep_time.html language=enus -->
## TOPIC 00045: RFmxNR CHP Configure Sweep Time (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_chp_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_chp_configure_sweep_time.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR CHP Configure Sweep Time (VI)

Owning Palette:

CHP

Configures the sweep time.

[IMAGE alt='RFmxNR CHP Configure Sweep Time' src='rfmxnr_chp_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement sets the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement calculates the sweep time internally. For DL, the sweep time is calculated based on the value of the OBW RBW property, and for UL, it uses a sweep time of 1 ms. |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement calculates the sweep time internally. For DL, the sweep time is calculated based on the value of the OBW RBW property, and for UL, it uses a sweep time of 1 ms. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_chp_fetch.html language=enus -->
## TOPIC 00046: RFmxNR CHP Fetch (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_chp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_chp_fetch.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR CHP Fetch (VI)

Owning Palette:

Fetch

Fetches the CHP measurements.

#### RFmxNR CHP Fetch Total Aggregated Power

Returns the sum of powers in all the subblocks.

[IMAGE alt='RFmxNR CHP Fetch Total Aggregated Power' src='rfmxnr_chp_fetch_total_aggregated_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Aggregated Power returns the total power of all the subblocks. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR CHP Fetch Subblock Power

Returns the power of subblock.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR CHP Fetch Subblock Power' src='rfmxnr_chp_fetch_subblock_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Subblock Power returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. This includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR CHP Fetch Component Carrier Measurement

Returns the absolute and relative powers measured in the component carriers.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR CHP Fetch Component Carrier Measurement' src='rfmxnr_chp_fetch_component_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. |
|  | Relative Power returns the component carrier power relative to its subblock power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR CHP Fetch Component Carrier Measurement (Array)

Returns an array of the absolute and relative powers measured in the component carriers.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR CHP Fetch Component Carrier Measurement (Array)' src='rfmxnr_chp_fetch_component_carrier_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns an array of the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. |
|  | Relative Power returns an array of the component carrier power relative to its subblock power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR CHP Fetch Spectrum

Fetches the spectrum used for CHP measurements.

[IMAGE alt='RFmxNR CHP Fetch Spectrum' src='rfmxnr_chp_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the spectrum. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_chp_validate_noise_calibration_data.html language=enus -->
## TOPIC 00047: RFmxNR CHP Validate Noise Calibration Data (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_chp_validate_noise_calibration_data.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_chp_validate_noise_calibration_data.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR CHP Validate Noise Calibration Data (VI)

Owning Palette:

CHP

Indicates whether the CHP noise calibration data is valid for the configuration specified by the signal name in the **Selector String** parameter.

[IMAGE alt='RFmxNR CHP Validate Noise Calibration Data' src='rfmxnr_chp_validate_noise_calibration_data.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Noise Calibration Data Valid returns whether the calibration data is valid. False (0) Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. True (1) Returns true if the calibration data is present for the configuration specified by the signal name in the Selector String parameter. |
| False (0) | Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. |
| True (1) | Returns true if the calibration data is present for the configuration specified by the signal name in the Selector String parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_clear_all_named_results.html language=enus -->
## TOPIC 00048: RFmxNR Clear All Named Results (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_clear_all_named_results.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_clear_all_named_results.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Clear All Named Results (VI)

Owning Palette:

Advanced

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxNR Clear All Named Results' src='rfmxnr_clear_all_named_results.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_clear_named_result.html language=enus -->
## TOPIC 00049: RFmxNR Clear Named Result (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_clear_named_result.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_clear_named_result.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Clear Named Result (VI)

Owning Palette:

Advanced

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='RFmxNR Clear Named Result' src='rfmxnr_clear_named_result.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_clear_noise_calibration_database.html language=enus -->
## TOPIC 00050: RFmxNR Clear Noise Calibration Database (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_clear_noise_calibration_database.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_clear_noise_calibration_database.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Clear Noise Calibration Database (VI)

Owning Palette:

Advanced

Clears the noise calibration database used for noise compensation.

[IMAGE alt='RFmxNR Clear Noise Calibration Database' src='rfmxnr_clear_noise_calibration_database.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_clone_signal_configuration.html language=enus -->
## TOPIC 00051: RFmxNR Clone Signal Configuration (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_clone_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_clone_signal_configuration.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Clone Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='RFmxNR Clone Signal Configuration' src='rfmxnr_clone_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
|  | Old Signal Name specifies the name of the existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_commit.html language=enus -->
## TOPIC 00052: RFmxNR Commit (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_commit.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Commit (VI)

Owning Palette:

Utility

Commits settings to the hardware. Calling this VI is optional. RFmxNR commits settings to the hardware when you call the [RFmxNR Initiate](..//rfmxnrvi/rfmxnr_initiate.html) VI.

[IMAGE alt='RFmxNR Commit' src='rfmxnr_commit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_configure_external_attenuation.html language=enus -->
## TOPIC 00053: RFmxNR Configure External Attenuation (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_configure_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_configure_external_attenuation.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Configure External Attenuation (VI)

Owning Palette:

Configuration

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer.

[IMAGE alt='RFmxNR Configure External Attenuation' src='rfmxnr_configure_external_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | External Attenuation specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_configure_frequency_(frequency).html language=enus -->
## TOPIC 00054: RFmxNR Configure Frequency (Frequency) (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_configure_frequency_(frequency).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_configure_frequency_(frequency).html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Configure Frequency (Frequency) (VI)

Owning Palette:

Configuration

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

[IMAGE alt='RFmxNR Configure Frequency (Frequency)' src='rfmxnr_configure_frequency_(frequency).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_configure_gnodeb_category.html language=enus -->
## TOPIC 00055: RFmxNR Configure gNodeB Category (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_configure_gnodeb_category.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_configure_gnodeb_category.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Configure gNodeB Category (VI)

Owning Palette:

Configuration

Configures the gNodeB Category of the signal being measured.

[IMAGE alt='RFmxNR Configure gNodeB Category' src='rfmxnr_configure_gnodeb_category.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | gNodeB Category specifies the downlink gNodeB (Base station) category. Refer to 3GPP 38.104 specification for more information about gNodeB Category. The default value is Wide Area Base Station - Category A. Wide Area Base Station - Category A (0) Specifies that gNodeB is of type Wide Area Base Station - Category A. Wide Area Base Station - Category B Option1 (1) Specifies that gNodeB is of type Wide Area Base Station - Category B Option1. Wide Area Base Station - Category B Option2 (2) Specifies that gNodeB is of type Wide Area Base Station - Category B Option2. Local Area Base Station (3) Specifies that gNodeB is of type Local Area Base Station. Medium Range Base Station (5) Specifies that gNodeB is of type Medium Range Base Station. FR2 Category A (6) Specifies that gNodeB is of type FR2 Category A. FR2 Category B (7) Specifies that gNodeB is of type FR2 Category B. |
| Wide Area Base Station - Category A (0) | Specifies that gNodeB is of type Wide Area Base Station - Category A. |
| Wide Area Base Station - Category B Option1 (1) | Specifies that gNodeB is of type Wide Area Base Station - Category B Option1. |
| Wide Area Base Station - Category B Option2 (2) | Specifies that gNodeB is of type Wide Area Base Station - Category B Option2. |
| Local Area Base Station (3) | Specifies that gNodeB is of type Local Area Base Station. |
| Medium Range Base Station (5) | Specifies that gNodeB is of type Medium Range Base Station. |
| FR2 Category A (6) | Specifies that gNodeB is of type FR2 Category A. |
| FR2 Category B (7) | Specifies that gNodeB is of type FR2 Category B. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_configure_reference_level.html language=enus -->
## TOPIC 00056: RFmxNR Configure Reference Level (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_configure_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_configure_reference_level.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Configure Reference Level (VI)

Owning Palette:

Configuration

Configures the reference level which represents the maximum expected power of an RF input signal.

[IMAGE alt='RFmxNR Configure Reference Level' src='rfmxnr_configure_reference_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Level specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_configure_rf.html language=enus -->
## TOPIC 00057: RFmxNR Configure RF (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_configure_rf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_configure_rf.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Configure RF (VI)

Owning Palette:

Configuration

Configures the RF properties of the signal specified by the selector string.

[IMAGE alt='RFmxNR Configure RF' src='rfmxnr_configure_rf.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. |
|  | Reference Level specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |
|  | External Attenuation specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_configure_trigger.html language=enus -->
## TOPIC 00058: RFmxNR Configure Trigger (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_configure_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_configure_trigger.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Configure Trigger (VI)

Owning Palette:

Configuration

Configures the reference trigger to use to acquire the signal.

#### RFmxNR Disable Trigger

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='RFmxNR Disable Trigger' src='rfmxnr_disable_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR Configure Digital Edge Trigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

Spectral measurements are sometimes implemented with multiple acquisitions and therefore will require that digital triggers are sent for each acquisition. Multiple factors, including the desired span versus the realtime bandwidth of the hardware, affect the number of acquisitions. NI recommends repeating the generation until the measurement is completed in order to ensure that all the acquisitions are triggered.

[IMAGE alt='RFmxNR Configure Digital Edge Trigger' src='rfmxnr_configure_digital_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Digital Edge Source specifies the source terminal for the digital edge trigger. This parameter is used when you set the Trigger Type property to Digital Edge. The default value of this parameter is hardware dependent. PFI0 (0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. PXIe_DStarB (PXIe_DStarB) The trigger is received on the PXIe DStar B trigger line. TimerEvent (TimerEvent) The trigger is received from the timer event. |
| PFI0 (0) | The trigger is received on PFI 0. |
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
|  | Digital Edge specifies the source terminal for the digital edge trigger. This parameter is used when you set the Trigger Type property to Digital Edge. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. |
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR Configure IQ Power Edge Trigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.

To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

[IMAGE alt='RFmxNR Configure IQ Power Edge Trigger' src='rfmxnr_configure_iq_power_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | IQ Power Edge Source specifies the channel from which the device monitors the trigger. This parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value of this parameter is hardware dependent. |
|  | IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value is Rising Slope. |
|  | IQ Power Edge Level specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative, and this value is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. This parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value of this parameter is hardware dependent. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | Min Quiet Time Mode specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Auto. Manual (0) The minimum quiet time for triggering is the value of the Min Quiet Time parameter. Auto (1) The measurement computes the minimum quiet time used for triggering. |
| Manual (0) | The minimum quiet time for triggering is the value of the Min Quiet Time parameter. |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |
|  | Min Quiet Time specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet above the trigger level. The default value of this parameter is hardware dependent. |
|  | IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. The IQ Power Edge Level Type parameter is used only when you set the Trigger Type property to IQ Power Edge. Relative (0) The IQ Power Edge Level property is relative to the value of the Reference Level property. Absolute (1) The IQ Power Edge Level property specifies the absolute power. |
| Relative (0) | The IQ Power Edge Level property is relative to the value of the Reference Level property. |
| Absolute (1) | The IQ Power Edge Level property specifies the absolute power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR Configure Software Edge Trigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

[IMAGE alt='RFmxNR Configure Software Edge Trigger' src='rfmxnr_configure_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_create_list.html language=enus -->
## TOPIC 00059: RFmxNR Create List (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_create_list.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_create_list.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Create List (VI)

Owning Palette:

List

Creates a new list instance. Call the [RFmxNR Create List Step](../rfmxnrvi/rfmxnr_create_list_step.html) VI to add steps to the list. Alternatively, you can also specify the number of list steps using the [Num List Steps](/csh?topicname=rfmxnrprop/attr900ff8.html) property.

**Supported devices:**PXIe-5840/5841/5842

[IMAGE alt='RFmxNR Create List' src='rfmxnr_create_list.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | List Name specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. Example: "list::samplelist1" "samplelist1" You can use the RFmxNR Build List String VI to build the list name. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of the RFmxNR Commit, RFmxNR Initiate, and RFmxNR Create List Step VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_create_list_step.html language=enus -->
## TOPIC 00060: RFmxNR Create List Step (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_create_list_step.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_create_list_step.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Create List Step (VI)

Owning Palette:

List

Creates a new list step instance in a list.

**Supported devices:**PXIe-5840/5841/5842

[IMAGE alt='RFmxNR Create List Step' src='rfmxnr_create_list_step.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. Example: "list::samplelist1" "samplelist1" You can use the RFmxNR Build List String VI to build the selector string or use the Selector String Out parameter from the RFmxNR Create List VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of the configure and fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_create_signal_configuration.html language=enus -->
## TOPIC 00061: RFmxNR Create Signal Configuration (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_create_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_create_signal_configuration.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Create Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal.

[IMAGE alt='RFmxNR Create Signal Configuration' src='rfmxnr_create_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_delete_list.html language=enus -->
## TOPIC 00062: RFmxNR Delete List (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_delete_list.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_delete_list.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Delete List (VI)

Owning Palette:

List

Deletes the list instance and all the list steps that you specify in the **List Name** parameter. When a list step is deleted, all the instances of properties associated with the list step are also removed.

**Supported devices:**PXIe-5840/5841

[IMAGE alt='RFmxNR Delete List' src='rfmxnr_delete_list.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | List Name specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. Example: "list::samplelist1" "samplelist1" You can use the RFmxNR Build List String VI to build the list name. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_delete_signal_configuration.html language=enus -->
## TOPIC 00063: RFmxNR Delete Signal Configuration (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_delete_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_delete_signal_configuration.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Delete Signal Configuration (VI)

Owning Palette:

Advanced

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='RFmxNR Delete Signal Configuration' src='rfmxnr_delete_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_get_all_named_result_names.html language=enus -->
## TOPIC 00064: RFmxNR Get All Named Result Names (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_get_all_named_result_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_get_all_named_result_names.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Get All Named Result Names (VI)

Owning Palette:

Advanced

Returns the named result names of the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxNR Get All Named Result Names' src='rfmxnr_get_all_named_result_names.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Result Names returns an array of result names. |
|  | Default Result Exists? indicates whether the default result exists. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_initiate.html language=enus -->
## TOPIC 00065: RFmxNR Initiate (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_initiate.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Initiate (VI)

Owning Palette:

RFmx NR VIs

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the [RFmxNR Wait for Measurement Complete](../rfmxnrvi/rfmxnr_wait_for_measurement_complete.html) VI or [RFmxNR Check Measurement Status](../rfmxnrvi/rfmxnr_check_measurement_status.html) VI.

[IMAGE alt='RFmxNR Initiate' src='rfmxnr_initiate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_load_from_generation_configuration_file.html language=enus -->
## TOPIC 00066: RFmxNR Load from Generation Configuration File (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_load_from_generation_configuration_file.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_load_from_generation_configuration_file.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Load from Generation Configuration File (VI)

Loads the attributes saved in an RFWS/TDMS file onto the RFmx session. This file can be saved using the NR Modulation Scheme in RFmx Waveform Creator. Make sure to select the 'store configuration' option while saving the TDMS file.

[IMAGE alt='RFmxNR Load from Generation Configuration File' src='rfmxnr_load_from_generation_configuration_file.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | File Path specifies the complete path to the RFWS/TDMS file from which the configurations are to be loaded. |
|  | Configuration Index specifies the index of the carrier set to be loaded from the RFWS/TDMS file. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_modacc_auto_level.html language=enus -->
## TOPIC 00067: RFmxNR ModAcc Auto Level (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_modacc_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_modacc_auto_level.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ModAcc Auto Level (VI)

Owning Palette:

ModAcc

Performs the user-configured ModAcc measurement at multiple reference levels relative to the user-configured [Reference Level](/csh?topicname=rfmxnrprop/attr900002.html) property and configures the reference level corresponding to the lowest [ModAcc Results Composite RMS EVM Mean](/csh?topicname=rfmxnrprop/attr904016.html) result.

This VI only measures at the reference levels that do not result in an ADC or DSP overflow when you set the [ModAcc Auto Level Allow Overflow](/csh?topicname=rfmxnrprop/attr904097.html) property to **False**. If you set the ModAcc Auto Level Allow Overflow property to **True**, this VI measures at a few reference levels beyond the overflow. After calling the ModAcc Auto Level VI, you need to call the ModAcc measurement.

|  | Note Calling this VI will also set the Reference Level Headroom property to 0. |
| --- | --- |

This VI expects:

- A valid ModAcc measurement configuration
- Reference Level property set to peak power of the signal
- Repetitive signals at the analyzer's input along with trigger settings that measure the same portion of the waveform every time the measurement is performed
- No other measurements are running in parallel

Auto level needs to be performed again if the input signal or RFmx configuration changes.

For repeatable results, you must make sure that the ModAcc measurement is repeatable.

This VI measures EVM at reference levels starting at an integer at least 1 dB above the value you configure for the Reference Level property, extending upto 12 dB lower when you set the ModAcc Auto Level Allow Overflow property to **False**, and up to 17 dB lower when you set the ModAcc Auto Level Allow Overflow property to **True** with a step size of 0.5 dB.

When you use this VI with the [ModAcc Noise Comp Enabled](/csh?topicname=rfmxnrprop/attr904092.html) property set to **True**, you need to make sure that valid noise calibration data is available for the above measurements.

[IMAGE alt='RFmxNR ModAcc Auto Level' src='rfmxnr_modacc_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the EVM results. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_modacc_clear_noise_calibration_database.html language=enus -->
## TOPIC 00068: RFmxNR ModAcc Clear Noise Calibration Database (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_modacc_clear_noise_calibration_database.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_modacc_clear_noise_calibration_database.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ModAcc Clear Noise Calibration Database (VI)

Owning Palette:

ModAcc

Clears the noise calibration database used for EVM noise compensation.

[IMAGE alt='RFmxNR ModAcc Clear Noise Calibration Database' src='rfmxnr_modacc_clear_noise_calibration_database.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_modacc_configure_measurement_mode.html language=enus -->
## TOPIC 00069: RFmxNR ModAcc Configure Measurement Mode (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_modacc_configure_measurement_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_modacc_configure_measurement_mode.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ModAcc Configure Measurement Mode (VI)

Owning Palette:

ModAcc

Configures the measurement mode for the ModAcc measurement.

[IMAGE alt='RFmxNR ModAcc Configure Measurement Mode' src='rfmxnr_modacc_configure_measurement_mode.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Mode specifies whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. The default value is Measure. Measure (0) The ModAcc measurement is performed on the acquired signal. Calibrate Noise Floor (1) The ModAcc measurement measures the noise floor of the instrument across the frequency range of interest determined by the carrier frequency and channel bandwidth. In this mode, the measurement expects that the signal generator to be turned off and checks whether no signal power is detected at the RF In port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is previously calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |
| Measure (0) | The ModAcc measurement is performed on the acquired signal. |
| Calibrate Noise Floor (1) | The ModAcc measurement measures the noise floor of the instrument across the frequency range of interest determined by the carrier frequency and channel bandwidth. In this mode, the measurement expects that the signal generator to be turned off and checks whether no signal power is detected at the RF In port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is previously calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_modacc_configure_noise_compensation_enabled.html language=enus -->
## TOPIC 00070: RFmxNR ModAcc Configure Noise Compensation Enabled (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_modacc_configure_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_modacc_configure_noise_compensation_enabled.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ModAcc Configure Noise Compensation Enabled (VI)

Owning Palette:

ModAcc

Configures whether to enable EVM noise compensation for the ModAcc measurement.

**Supported devices:**PXIe-5830/5831/5832/5646/5840/5841/5842.

[IMAGE alt='RFmxNR ModAcc Configure Noise Compensation Enabled' src='rfmxnr_modacc_configure_noise_compensation_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Noise Compensation Enabled specifies whether the contribution of the instrument noise is compensated for EVM computation. The default value is False. False (0) Disables instrument noise compensation for EVM results. True (1) Enables instrument noise compensation for EVM results. |
| False (0) | Disables instrument noise compensation for EVM results. |
| True (1) | Enables instrument noise compensation for EVM results. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_modacc_configure_reference_waveform.html language=enus -->
## TOPIC 00071: RFmxNR ModAcc Configure Reference Waveform (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_modacc_configure_reference_waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_modacc_configure_reference_waveform.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ModAcc Configure Reference Waveform (VI)

Owning Palette:

ModAcc

Configures the reference waveform for the creation of reference data symbols for EVM computation.

[IMAGE alt='RFmxNR ModAcc Configure Reference Waveform' src='rfmxnr_modacc_configure_reference_waveform.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Waveform specifies the reference waveform for the creation of reference data symbols for EVM computation. x0 specifies the start time, in seconds. dx specifies the sample duration, in seconds. y specifies the complex baseband samples, in volts. |
|  | x0 specifies the start time, in seconds. |
|  | dx specifies the sample duration, in seconds. |
|  | y specifies the complex baseband samples, in volts. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_modacc_fetch.html language=enus -->
## TOPIC 00072: RFmxNR ModAcc Fetch (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_modacc_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_modacc_fetch.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ModAcc Fetch (VI)

Owning Palette:

Fetch

Fetches the ModAcc measurements.

#### RFmxNR ModAcc Fetch Composite EVM

Fetches the composite EVM for ModAcc measurements.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch Composite EVM' src='rfmxnr_modacc_fetch_composite_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Composite RMS EVM Mean returns the mean value of the RMS EVMs calculated on all configured channels over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage.When you set the ModAcc EVM Unit property to dB, the measurement returns this result in dB. |
|  | Composite Peak EVM Max returns the maximum value of the peak EVMs calculated on all configured channels over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage.When you set the ModAcc EVM Unit property to dB, the measurement returns this result in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch Frequency Error Mean

Fetches the estimated carrier frequency offset averaged over measurement length. This value is expressed in Hz.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

[IMAGE alt='RFmxNR ModAcc Fetch Frequency Error Mean' src='rfmxnr_modacc_fetch_frequency_error_mean.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Frequency Error Mean returns the estimated carrier frequency offset averaged over measurement length. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch Frequency Error per Slot Maximum Trace

Fetches an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

[IMAGE alt='RFmxNR ModAcc Fetch Frequency Error per Slot Maximum Trace' src='rfmxnr_modacc_fetch_frequency_error_per_slot_maximum_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Frequency Error per Slot Maximum returns an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz. x0 returns the index of the first active slot. dx returns the increment value. This is always set to one slot. y returns an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. |
|  | x0 returns the index of the first active slot. |
|  | dx returns the increment value. This is always set to one slot. |
|  | y returns an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch RMS EVM per Subcarrier Mean Trace

Fetches the EVM of each allocated subcarrier averaged across all the symbols within the measurement length.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch RMS EVM per Subcarrier Mean Trace' src='rfmxnr_modacc_fetch_rms_evm_per_subcarrier_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS EVM per Subcarrier Mean returns the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch Peak EVM per Subcarrier Maximum Trace

Fetches the peak value of EVM for each allocated subcarrier computed across all the symbols within the measurement length.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch Peak EVM per Subcarrier Maximum Trace' src='rfmxnr_modacc_fetch_peak_evm_per_subcarrier_maximum_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Peak EVM per Subcarrier Maximum returns the peak value of EVM for each allocated subcarrier computed across all the symbols within the measurement length. . x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array the peak value of EVM for each allocated subcarrier computed across all the symbols within the measurement length. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array the peak value of EVM for each allocated subcarrier computed across all the symbols within the measurement length. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch RMS EVM per Slot Mean Trace

Fetches the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch RMS EVM per Slot Mean Trace' src='rfmxnr_modacc_fetch_rms_evm_per_slot_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS EVM per Slot Mean returns the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot. x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch Peak EVM per Slot Maximum Trace

Fetches the peak value of EVM for each slot computed across all the symbols and all the allocated subcarriers.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch Peak EVM per Slot Maximum Trace' src='rfmxnr_modacc_fetch_peak_evm_per_slot_maximum_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Peak EVM per Slot Maximum returns the peak value of EVM for each slot computed across all the symbols and all the allocated subcarriers. x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array the peak value of EVM for each slot computed across all the symbols and all the allocated subcarriers. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array the peak value of EVM for each slot computed across all the symbols and all the allocated subcarriers. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch RMS EVM per Symbol Mean Trace

Fetches the EVM on each symbol within the measurement length averaged across all the allocated subcarriers.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch RMS EVM per Symbol Mean Trace' src='rfmxnr_modacc_fetch_rms_evm_per_symbol_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS EVM per Symbol Mean returns the EVM on each symbol within the measurement length averaged across all the allocated subcarriers. x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array the EVM on each symbol within the measurement length averaged across all the allocated subcarriers. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array the EVM on each symbol within the measurement length averaged across all the allocated subcarriers. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch Peak EVM per Symbol Maximum Trace

Fetches the peak value of EVM for each symbol computed across all the allocated subcarriers.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch Peak EVM per Symbol Maximum Trace' src='rfmxnr_modacc_fetch_peak_evm_per_symbol_maximum_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Peak EVM per Symbol Maximum returns the peak value of EVM for each symbol computed across all the allocated subcarriers. x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array the the peak value of EVM for each symbol computed across all the allocated subcarriers. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array the the peak value of EVM for each symbol computed across all the allocated subcarriers. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch RMS EVM-High per Symbol Mean Trace

Fetches the EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C+W/2.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch RMS EVM-High per Symbol Mean Trace' src='rfmxnr_modacc_fetch_rms_evm-high_per_symbol_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS EVM-High per Symbol Mean returns the EVM per symbol trace for all confgured slots. x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array of the EVM per symbol for all confgured slots. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array of the EVM per symbol for all confgured slots. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch RMS EVM-Low per Symbol Mean Trace

Fetches the EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C-W/2.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch RMS EVM-Low per Symbol Mean Trace' src='rfmxnr_modacc_fetch_rms_evm-low_per_symbol_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS EVM-Low per Symbol Mean returns the EVM per symbol trace for all confgured slots. x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array of the EVM per symbol for all confgured slots. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array of the EVM per symbol for all confgured slots. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch Transient Period Locations Trace

Returns the symbol indices that were identified to have a transient period.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

The length of the trace is equal to the number of symbols within the measurement length.

The trace returns a 1 for the symbol index that was identified to have a transient period; otherwise returns a 0.

The trace is intended to be used as additional context information for the following traces:

- RMS EVM per Symbol Mean Trace
- RMS EVM-High per Symbol Mean Trace
- RMS EVM-Low per Symbol Mean Trace

[IMAGE alt='RFmxNR ModAcc Fetch Transient Period Locations Trace' src='rfmxnr_modacc_fetch_transient_period_locations_trace.gif']

|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
| --- | --- |
|  | error out contains error information. This output provides standard error out functionality. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Transient Period Locations returns the symbol indices that were identified to have a transient period. x0 returns the start symbol index from the frame start. dx returns the width in terms of symbols. y returns a 1 for the symbol index that was identified to have a transient period; otherwise returns a 0. |
|  | x0 returns the start symbol index from the frame start. |
|  | dx returns the width in terms of symbols. |
|  | y returns a 1 for the symbol index that was identified to have a transient period; otherwise returns a 0. |
|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |

#### RFmxNR ModAcc Fetch Spectral Flatness Trace

Returns the spectral flatness, upper mask, and lower mask traces. Spectral flatness is the magnitude of equalizer coefficients at each allocated subcarrier. Lower and upper masks are derived from section 6.5.2.4.5 of *3GPP TS 38.521-1* specification.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch Spectral Flatness Trace' src='rfmxnr_modacc_fetch_spectral_flatness_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectral Flatness returns the spectral flatness. x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array of the spectral flatness values at each allocated subcarrier. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array of the spectral flatness values at each allocated subcarrier. |
|  | Spectral Flatness Lower Mask returns the lower mask of the spectral flatness. x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array of the lower mask values for the spectral flatness. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array of the lower mask values for the spectral flatness. |
|  | Spectral Flatness Upper Mask returns the upper mask of the spectral flatness. x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array of the upper mask values for the spectral flatness. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array of the upper mask values for the spectral flatness. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch Subblock In-Band Emission Trace

Returns the in-band emission trace and limit trace for the the subblocks aggregated bandwidth. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier leakage, and I/Q Image) are obtained and concatenated to form a composite trace and the limits are defined in section 6.4A.2.2.2 of *3GPP 38.101-1*, and section 6.4A.2.3 of *3GPP 38.101-2*. The trace is not returned when there is clustered PUSCH allocation, or when there is more than one active carrier, or when there is full allocation of resource blocks, or when carriers with different sub-carrier spacing are aggregated, or when the number of carriers is greater than 2.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch Subblock In-Band Emission Trace' src='rfmxnr_modacc_fetch_subblock_in-band_emission_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Subblock In-Band Emission returns the array of subblock in-band emission measurement trace. |
|  | Subblock In-Band Emission Mask returns the array of subblock in-band emission mask trace. |
|  | Subblock In-Band Emission RB Indices returns the array of resource block indices for the subblock in-band emission trace. It can have non integer values depending upon the spacing between carriers. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch In-Band Emission Trace

Fetches the in-band emission trace and limits trace for the component carrier. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier leakage, and I/Q Image) are obtained and concatenated to form a composite trace and the limits are defined in section 6.4.2.3 of *3GPP 38.101-1*, and section 6.4.2.3 of *3GPP 38.101-2*. The trace is not returned when there is full allocation of bandwidth, or there is clustered PUSCH or there is more than one active component carrier.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch In-Band Emission Trace' src='rfmxnr_modacc_fetch_in-band_emission_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | In Band Emission returns the in-band emission margin. x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array of the in-band emission value as an array for each of the resource blocks. In-band emission is the interference falling into non-allocated resource blocks. This value is expressed in dB. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array of the in-band emission value as an array for each of the resource blocks. In-band emission is the interference falling into non-allocated resource blocks. This value is expressed in dB. |
|  | In Band Emission Mask returns the in-band emission mask. x0 returns the start point of the of the resource block. dx returns the subcarrier spacing. y returns an array of the in-band emission limit value as an array for each of the resource blocks. The in-band emission limit for regions such as general, carrier leakage and IQ image, are evaluated according to the method defined in the 3GPP specification and concatenated to form a composite limit trace. |
|  | x0 returns the start point of the of the resource block. |
|  | dx returns the subcarrier spacing. |
|  | y returns an array of the in-band emission limit value as an array for each of the resource blocks. The in-band emission limit for regions such as general, carrier leakage and IQ image, are evaluated according to the method defined in the 3GPP specification and concatenated to form a composite limit trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch IQ Gain Imbalance per Subcarrier Mean Trace

Fetches mean value of IQ Gain Imbalance.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch IQ Gain Imbalance per Subcarrier Mean Trace' src='rfmxnr_modacc_fetch_iq_gain_imbalance_per_subcarrier_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | IQ Gain Imbalance per Subcarrier Mean returns the mean value of IQ Gain Imbalance. This value is expressed in dB. x0 returns the start point of the of the resource grid. dx returns the sampling duration of the analyzed signal. y returns the mean value of IQ Gain Imbalance. This value is expressed in dB. |
|  | x0 returns the start point of the of the resource grid. |
|  | dx returns the sampling duration of the analyzed signal. |
|  | y returns the mean value of IQ Gain Imbalance. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch IQ Quadrature Error per Subcarrier Mean Trace

Fetches the mean value of IQ Quadrature Error.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch IQ Quadrature Error per Subcarrier Mean Trace' src='rfmxnr_modacc_fetch_iq_quadrature_error_per_subcarrier_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | IQ Quadrature Error per Subcarrier Mean returns the mean value of IQ Quadrature Error. This value is expressed in degrees. x0 returns the start point of the of the resource grid. dx returns the sampling duration of the analyzed signal. y returns the mean value of IQ Quadrature Error. This value is expressed in degrees. |
|  | x0 returns the start point of the of the resource grid. |
|  | dx returns the sampling duration of the analyzed signal. |
|  | y returns the mean value of IQ Quadrature Error. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PUSCH Data Constellation Trace

Fetches PUSCH Data Constellation trace. The constellation points of different slots in the measurement length is concatenated.

Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PUSCH Data Constellation Trace' src='rfmxnr_modacc_fetch_pusch_data_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0". Example: "subblock0/carrier0/user0" "signal::sig1/subblock0/carrier0/user0" "result::r1/subblock0/carrier0/user0" "signal::sig1/result::r1/subblock0/carrier0/user0" You can use the RFmxNR Build User String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PUSCH Data Constellation returns the PUSCH data constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PUSCH DMRS Constellation Trace

Fetches PUSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.

Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PUSCH DMRS Constellation Trace' src='rfmxnr_modacc_fetch_pusch_dmrs_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0". Example: "subblock0/carrier0/user0" "signal::sig1/subblock0/carrier0/user0" "result::r1/subblock0/carrier0/user0" "signal::sig1/result::r1/subblock0/carrier0/user0" You can use the RFmxNR Build User String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PUSCH DMRS Constellation returns the PDSCH DMRS constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PUSCH PTRS Constellation Trace

Fetches PUSCH PTRS trace. The constellation points of different slots in the measurement length is concatenated.

Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PUSCH PTRS Constellation Trace' src='rfmxnr_modacc_fetch_pusch_ptrs_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0". Example: "subblock0/carrier0/user0" "signal::sig1/subblock0/carrier0/user0" "result::r1/subblock0/carrier0/user0" "signal::sig1/result::r1/subblock0/carrier0/user0" You can use the RFmxNR Build User String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PUSCH PTRS Constellation returns the PUSCH PTRS constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PUSCH Phase Offset Trace

Returns the phase offset for the slots with respect to the reference slot.

Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this VI.

The length of the trace is equal to the number of slots within the measurement length.

For each burst of continuously allocated slots, the first active slot in the burst is used as the reference slot.

The reference slot is reset at frame boundary.

The phase offset is calculated for slots that are contiguous to the reference slot and have overlapping subcarrier allocations. For all other slots, NaN is provided.

[IMAGE alt='RFmxNR ModAcc Fetch PUSCH Phase Offset Trace' src='rfmxnr_modacc_fetch_pusch_phase_offset_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0". Example: "subblock0/carrier0/user0" "signal::sig1/subblock0/carrier0/user0" "result::r1/subblock0/carrier0/user0" "signal::sig1/result::r1/subblock0/carrier0/user0" You can use the RFmxNR Build User String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PUSCH Peak Phase Offset (deg) returns the phase offset for the slots with respect to the reference slot. x0 returns the index of the first active slot. dx returns the increment value. This is always set to one slot. y returns an array of the maximum value across averaging counts of the phase error per slot for all slots within the measurement length. |
|  | x0 returns the index of the first active slot. |
|  | dx returns the increment value. This is always set to one slot. |
|  | y returns an array of the maximum value across averaging counts of the phase error per slot for all slots within the measurement length. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PUSCH Demodulated Bits

Fetches the recovered bits during EVM calculation. The bits of different slots in the measurement length are concatenated.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PUSCH Demodulated Bits' src='rfmxnr_modacc_fetch_pusch_demodulated_bits.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Bits returns an array of the recovered bits during EVM calculation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PDSCH Data Constellation Trace

Fetches the recovered PDSCH data constellation points. The constellation points of different slots in the measurement length is concatenated.

Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PDSCH Data Constellation Trace' src='rfmxnr_modacc_fetch_pdsch_data_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0". Example: "subblock0/carrier0/user0" "signal::sig1/subblock0/carrier0/user0" "result::r1/subblock0/carrier0/user0" "signal::sig1/result::r1/subblock0/carrier0/user0" You can use the RFmxNR Build User String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PDSCH Data Constellation returns the PDSCH data constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PDSCH DMRS Constellation Trace

Fetches PDSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.

Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PDSCH DMRS Constellation Trace' src='rfmxnr_modacc_fetch_pdsch_dmrs_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0". Example: "subblock0/carrier0/user0" "signal::sig1/subblock0/carrier0/user0" "result::r1/subblock0/carrier0/user0" "signal::sig1/result::r1/subblock0/carrier0/user0" You can use the RFmxNR Build User String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PDSCH DMRS Constellation returns the PDSCH DMRS constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PDSCH PTRS Constellation Trace

Fetches PDSCH PTRS trace.

Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PDSCH PTRS Constellation Trace' src='rfmxnr_modacc_fetch_pdsch_ptrs_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0". Example: "subblock0/carrier0/user0" "signal::sig1/subblock0/carrier0/user0" "result::r1/subblock0/carrier0/user0" "signal::sig1/result::r1/subblock0/carrier0/user0" You can use the RFmxNR Build User String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PDSCH PTRS Constellation returns the PDSCH PTRS constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PDSCH QPSK Constellation Trace

Fetches PDSCH QPSK trace.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PDSCH QPSK Constellation Trace' src='rfmxnr_modacc_fetch_pdsch_qpsk_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | QPSK Constellation returns the QPSK constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PDSCH 16QAM Constellation Trace

Fetches PDSCH 16 QAM trace.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PDSCH 16QAM Constellation Trace' src='rfmxnr_modacc_fetch_pdsch_16qam_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | 16 QAM Constellation returns the 16 QAM constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PDSCH 64QAM Constellation Trace

Fetches PDSCH 64 QAM trace.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PDSCH 64QAM Constellation Trace' src='rfmxnr_modacc_fetch_pdsch_64qam_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | 64 QAM Constellation returns the 64 QAM constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PDSCH 256QAM Constellation Trace

Fetches PDSCH 256 QAM trace.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PDSCH 256QAM Constellation Trace' src='rfmxnr_modacc_fetch_pdsch_256qam_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | 256 QAM Constellation returns the 256 QAM constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PDSCH 1024QAM Constellation Trace

Fetches the PDSCH 1024 QAM constellation trace.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PDSCH 1024QAM Constellation Trace' src='rfmxnr_modacc_fetch_pdsch_1024qam_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | 1024 QAM Constellation returns the 1024 QAM constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PDSCH 8PSK Constellation Trace

Fetches PDSCH 8 PSK constellation trace.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PDSCH 8PSK Constellation Trace' src='rfmxnr_modacc_fetch_pdsch_8psk_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | 8 PSK Constellation returns the PDSCH 8 PSK constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PDSCH Demodulated Bits

Fetches the recovered bits during EVM calculation. The bits of different slots in the measurement length are concatenated.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PDSCH Demodulated Bits' src='rfmxnr_modacc_fetch_pdsch_demodulated_bits.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Bits returns an array of the recovered bits during EVM calculation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PSS RMS EVM per Subcarrier Mean Trace

Fetches the mean PSS RMS EVM of each subcarrier.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PSS RMS EVM per Subcarrier Mean Trace' src='rfmxnr_modacc_fetch_pss_rms_evm_per_subcarrier_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PSS RMS EVM per Subcarrier Mean returns the RMS EVM of each subcarrier averaged across all the OFDM symbols allocated with PSS within the Meas Length. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 returns the start point of the of the resource grid. dx returns the subcarrier spacing of SSB. y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with PSS within the measurement length. |
|  | x0 returns the start point of the of the resource grid. |
|  | dx returns the subcarrier spacing of SSB. |
|  | y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with PSS within the measurement length. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch SSS RMS EVM per Subcarrier Mean Trace

Fetches the mean SSS RMS EVM of each subcarrier.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch SSS RMS EVM per Subcarrier Mean Trace' src='rfmxnr_modacc_fetch_sss_rms_evm_per_subcarrier_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | SSS RMS EVM per Subcarrier Mean returns the RMS EVM of each subcarrier averaged across all the OFDM symbols allocated with SSS within the Meas Length. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 returns the start point of the of the resource grid. dx returns the subcarrier spacing of SSB. y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with SSS within the measurement length. |
|  | x0 returns the start point of the of the resource grid. |
|  | dx returns the subcarrier spacing of SSB. |
|  | y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with SSS within the measurement length. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PBCH Data RMS EVM per Subcarrier Mean Trace

Fetches the mean PBCH data RMS EVM of each subcarrier.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PBCH Data RMS EVM per Subcarrier Mean Trace' src='rfmxnr_modacc_fetch_pbch_data_rms_evm_per_subcarrier_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PBCH Data RMS EVM per Subcarrier Mean returns the RMS EVM of each subcarrier averaged across all the OFDM symbols allocated with PBCH data within the Meas Length property. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 returns the start point of the of the resource grid. dx returns the subcarrier spacing of SSB. y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with PBCH data within the measurement length. |
|  | x0 returns the start point of the of the resource grid. |
|  | dx returns the subcarrier spacing of SSB. |
|  | y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with PBCH data within the measurement length. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PBCH DMRS RMS EVM per Subcarrier Mean Trace

Fetches the mean PBCH DMRS RMS EVM for each subcarrier.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PBCH DMRS RMS EVM per Subcarrier Mean Trace' src='rfmxnr_modacc_fetch_pbch_dmrs_rms_evm_per_subcarrier_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PBCH DMRS RMS EVM per Subcarrier Mean returns the RMS EVM of each subcarrier averaged across all the OFDM symbols allocated with PBCH DMRS within the Meas Length. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 returns the start point of the of the resource grid. dx returns the subcarrier spacing of SSB. y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with PBCH DMRS within the measurement length. |
|  | x0 returns the start point of the of the resource grid. |
|  | dx returns the subcarrier spacing of SSB. |
|  | y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with PBCH DMRS within the measurement length. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PSS RMS EVM per Symbol Mean Trace

Fetches the mean PSS RMS EVM of each symbol.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PSS RMS EVM per Symbol Mean Trace' src='rfmxnr_modacc_fetch_pss_rms_evm_per_symbol_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PSS RMS EVM per Symbol Mean returns the RMS EVM on each OFDM symbol averaged across all the defined subcarriers allocated with PSS within the Meas Length. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 returns the start symbol index from the frame start in terms of SSB numerology. dx returns the width in terms of symbols. y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PSS within symbol. |
|  | x0 returns the start symbol index from the frame start in terms of SSB numerology. |
|  | dx returns the width in terms of symbols. |
|  | y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PSS within symbol. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch SSS RMS EVM per Symbol Mean Trace

Fetches the mean SSS RMS EVM of each symbol.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch SSS RMS EVM per Symbol Mean Trace' src='rfmxnr_modacc_fetch_sss_rms_evm_per_symbol_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | SSS RMS EVM per Symbol Mean returns the RMS EVM on each OFDM symbol averaged across all the defined subcarriers allocated with SSS within the Meas Length. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 returns the start symbol index from the frame start in terms of SSB numerology. dx returns the width in terms of symbols. y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with SSS within symbol. |
|  | x0 returns the start symbol index from the frame start in terms of SSB numerology. |
|  | dx returns the width in terms of symbols. |
|  | y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with SSS within symbol. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PBCH Data RMS EVM per Symbol Mean Trace

Fetches the mean PBCH data RMS EVM for each symbol.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PBCH Data RMS EVM per Symbol Mean Trace' src='rfmxnr_modacc_fetch_pbch_data_rms_evm_per_symbol_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PBCH Data RMS EVM per Symbol Mean returns the RMS EVM on each OFDM symbol averaged across all the allocated subcarriers allocated with PBCH data within the Meas Length. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 returns the start symbol index from the frame start in terms of SSB numerology. dx returns the width in terms of symbols. y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PBCH data within symbol. |
|  | x0 returns the start symbol index from the frame start in terms of SSB numerology. |
|  | dx returns the width in terms of symbols. |
|  | y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PBCH data within symbol. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PBCH DMRS RMS EVM per Symbol Mean Trace

Fetches the mean PBCH DMRS RMS EVM for each symbol.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PBCH DMRS RMS EVM per Symbol Mean Trace' src='rfmxnr_modacc_fetch_pbch_dmrs_rms_evm_per_symbol_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PBCH DMRS RMS EVM per Symbol Mean returns the RMS EVM on each OFDM symbol averaged across all the allocated subcarriers allocated with PBCH DMRS within the Meas Length. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 returns the start symbol index from the frame start in terms of SSB numerology. dx returns the width in terms of symbols. y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PBCH DMRS within symbol. |
|  | x0 returns the start symbol index from the frame start in terms of SSB numerology. |
|  | dx returns the width in terms of symbols. |
|  | y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PBCH DMRS within symbol. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PSS Constellation Trace

Fetches the PSS constellation trace. The constellation points of different slots in the measurement length is concatenated.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PSS Constellation Trace' src='rfmxnr_modacc_fetch_pss_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PSS Constellation returns the PSS constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch SSS Constellation Trace

Fetches the SSS constellation trace. The constellation points of different slots in the measurement length is concatenated.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch SSS Constellation Trace' src='rfmxnr_modacc_fetch_sss_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | SSS Constellation returns the SSS constellation trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PBCH Data Constellation Trace

Fetches the PBCH data trace. The constellation points of different slots in the measurement length is concatenated.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PBCH Data Constellation Trace' src='rfmxnr_modacc_fetch_pbch_data_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PBCH Data Constellation returns the PBCH data trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR ModAcc Fetch PBCH DMRS Constellation Trace

Fetches the PBCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR ModAcc Fetch PBCH DMRS Constellation Trace' src='rfmxnr_modacc_fetch_pbch_dmrs_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | PBCH DMRS Constellation returns the PBCH DMRS trace. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_modacc_validate_calibration_data.html language=enus -->
## TOPIC 00073: RFmxNR ModAcc Validate Calibration Data (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_modacc_validate_calibration_data.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_modacc_validate_calibration_data.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR ModAcc Validate Calibration Data (VI)

Owning Palette:

ModAcc

Specifies whether calibration data is valid for the configuration specified by the signal name in the **Selector String** parameter.

[IMAGE alt='RFmxNR ModAcc Validate Calibration Data' src='rfmxnr_modacc_validate_calibration_data.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Calibration Data Valid returns whether the calibration data is valid. False (0) Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. True (1) Returns true if the calibration data is present for the configuration specified by the signal name in the Selector String parameter. |
| False (0) | Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. |
| True (1) | Returns true if the calibration data is present for the configuration specified by the signal name in the Selector String parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_obw_configure_averaging.html language=enus -->
## TOPIC 00074: RFmxNR OBW Configure Averaging (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_obw_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_obw_configure_averaging.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR OBW Configure Averaging (VI)

Owning Palette:

OBW

Configures averaging for the OBW measurement.

[IMAGE alt='RFmxNR OBW Configure Averaging' src='rfmxnr_obw_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_obw_configure_rbw_filter.html language=enus -->
## TOPIC 00075: RFmxNR OBW Configure RBW Filter (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_obw_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_obw_configure_rbw_filter.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR OBW Configure RBW Filter (VI)

Owning Palette:

OBW

Configures the resolution bandwidth (RBW) filter.

[IMAGE alt='RFmxNR OBW Configure RBW Filter' src='rfmxnr_obw_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. The default value is True. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
|  | RBW specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 10 kHz. |
|  | RBW Filter Type specifies the shape of the RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_obw_configure_sweep_time.html language=enus -->
## TOPIC 00076: RFmxNR OBW Configure Sweep Time (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_obw_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_obw_configure_sweep_time.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR OBW Configure Sweep Time (VI)

Owning Palette:

OBW

Configures the sweep time.

[IMAGE alt='RFmxNR OBW Configure Sweep Time' src='rfmxnr_obw_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement sets the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement calculates the sweep time internally. For DL, the sweep time is calculated based on the value of the OBW RBW property, and for UL, it uses a sweep time of 1 ms. |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement calculates the sweep time internally. For DL, the sweep time is calculated based on the value of the OBW RBW property, and for UL, it uses a sweep time of 1 ms. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_obw_fetch.html language=enus -->
## TOPIC 00077: RFmxNR OBW Fetch (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_obw_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_obw_fetch.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR OBW Fetch (VI)

Owning Palette:

Fetch

Fetches the OBW measurements.

#### RFmxNR OBW Fetch Measurement

Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR OBW Fetch Measurement' src='rfmxnr_obw_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Occupied Bandwidth returns the bandwidth that occupies the specified percentage of the total power of the signal. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation: Occupied bandwidth = Stop frequency - Start frequency |
|  | Absolute Power returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. |
|  | Stop Frequency returns the stop frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. |
|  | Start Frequency returns the start frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR OBW Fetch Spectrum

Fetches the spectrum used for OBW measurements.

[IMAGE alt='RFmxNR OBW Fetch Spectrum' src='rfmxnr_obw_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the spectrum. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_property_node.html language=enus -->
## TOPIC 00078: RFmxNR Property Node (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_property_node.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_property_node.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Property Node (VI)

Owning Palette:

RFmx NR VIs

Gets (reads), sets (writes), or resets (sets to default value) RFmxNR properties.

[IMAGE alt='RFmxNR Property Node' src='rfmxnr_property_node.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_pvt_configure_averaging.html language=enus -->
## TOPIC 00079: RFmxNR PVT Configure Averaging (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_pvt_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_pvt_configure_averaging.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR PVT Configure Averaging (VI)

Owning Palette:

PVT

Configures averaging for the PVT measurement.

[IMAGE alt='RFmxNR PVT Configure Averaging' src='rfmxnr_pvt_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_pvt_configure_measurement_method.html language=enus -->
## TOPIC 00080: RFmxNR PVT Configure Measurement Method (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_pvt_configure_measurement_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_pvt_configure_measurement_method.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR PVT Configure Measurement Method (VI)

Owning Palette:

PVT

Configures the measurement method for PVT measurement.

[IMAGE alt='RFmxNR PVT Configure Measurement Method' src='rfmxnr_pvt_configure_measurement_method.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Method specifies the method for performing the PVT measurement. The default value is Normal. Normal (0) The measurement is performed using a single acquisition. Use this method when a high dynamic range is not required. Dynamic Range (1) The measurement is performed using two acquisitions. Use this method when a higher dynamic range is desirable over the measurement speed. Supported Devices: PXIe-5644R/5645R/5646R, PXIe-5840/5841/5842. |
| Normal (0) | The measurement is performed using a single acquisition. Use this method when a high dynamic range is not required. |
| Dynamic Range (1) | The measurement is performed using two acquisitions. Use this method when a higher dynamic range is desirable over the measurement speed. Supported Devices: PXIe-5644R/5645R/5646R, PXIe-5840/5841/5842. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_pvt_configure_off_power_exclusion_periods.html language=enus -->
## TOPIC 00081: RFmxNR PVT Configure OFF Power Exclusion Periods (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_pvt_configure_off_power_exclusion_periods.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_pvt_configure_off_power_exclusion_periods.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR PVT Configure OFF Power Exclusion Periods (VI)

Owning Palette:

PVT

Configures the time excluded from the off region before and after the burst.

[IMAGE alt='RFmxNR PVT Configure OFF Power Exclusion Periods' src='rfmxnr_pvt_configure_off_power_exclusion_periods.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | OFF Power Exclusion Before specifies the time excluded from the Off region before the burst. This value is expressed in seconds. The default value is 0. |
|  | OFF Power Exclusion After specifies the time excluded from the Off region after the burst. This value is expressed in seconds. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_pvt_fetch.html language=enus -->
## TOPIC 00082: RFmxNR PVT Fetch (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_pvt_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_pvt_fetch.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR PVT Fetch (VI)

Owning Palette:

Fetch

Fetches the PVT measurements.

#### RFmxNR PVT Fetch Measurement

Fetches PVT ON and OFF powers along with measurement status and burst width.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read from this VI.

[IMAGE alt='RFmxNR PVT Fetch Measurement' src='rfmxnr_pvt_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the measurement status indicating whether the off power before and after is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |
|  | Absolute OFF Power Before returns the OFF power in the segment before the captured burst. The segment is defined as one slot prior to a short transient segment and the burst. This value is expressed in dBm. |
|  | Absolute OFF Power After returns the OFF power in the segment after the captured burst. The segment is defined as one slot after the burst and a short transient segment. This value is expressed in dBm. |
|  | Absolute ON Power returns the power of the subframes within the captured burst. This value is expressed in dBm. |
|  | Burst Width returns the width of the captured burst. This value is expressed in seconds. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR PVT Fetch Measurement (Array)

Fetches an array of PVT ON and OFF powers along with measurement status and burst width.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR PVT Fetch Measurement (Array)' src='rfmxnr_pvt_fetch_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the measurement status indicating whether the off power before and after is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |
|  | Absolute OFF Power Before returns the OFF power in the segment before the captured burst. The segment is defined as one slot prior to a short transient segment and the burst. This value is expressed in dBm. |
|  | Absolute OFF Power After returns the OFF power in the segment after the captured burst. The segment is defined as one slot after the burst and a short transient segment. This value is expressed in dBm. |
|  | Absolute ON Power returns the power of the subframes within the captured burst. This value is expressed in dBm. |
|  | Burst Width returns the width of the captured burst. This value is expressed in seconds. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR PVT Fetch Signal Power Trace

Fetches an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

[IMAGE alt='RFmxNR PVT Fetch Signal Power Trace' src='rfmxnr_pvt_fetch_signal_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Signal Power returns an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz. x0 returns start time of the signal. This value is expressed in seconds. dx returns the time bin spacing. This value is expressed in seconds. y returns the instantaneous signal power trace. This value is expressed in dBm. |
|  | x0 returns start time of the signal. This value is expressed in seconds. |
|  | dx returns the time bin spacing. This value is expressed in seconds. |
|  | y returns the instantaneous signal power trace. This value is expressed in dBm. |
|  | Absolute Limit returns absolute limit for each segment in the trace as specified in section 6.5.2.4.5 of the 3GPP 36.521 specification. This value is expressed in dBm or dBm/MHz. x0 returns start time of the signal. This value is expressed in seconds. dx returns the time bin spacing. This value is expressed in seconds. y returns an array of the absolute limit for each segment in the trace. |
|  | x0 returns start time of the signal. This value is expressed in seconds. |
|  | dx returns the time bin spacing. This value is expressed in seconds. |
|  | y returns an array of the absolute limit for each segment in the trace. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR PVT Fetch Windowed Signal Power Trace

Fetches the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

[IMAGE alt='RFmxNR PVT Fetch Windowed Signal Power Trace' src='rfmxnr_pvt_fetch_windowed_signal_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Windowed Signal Power returns the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. x0 returns start time of the signal. This value is expressed in seconds. dx returns the time bin spacing. This value is expressed in seconds. y returns the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. |
|  | x0 returns start time of the signal. This value is expressed in seconds. |
|  | dx returns the time bin spacing. This value is expressed in seconds. |
|  | y returns the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_reset_to_default.html language=enus -->
## TOPIC 00083: RFmxNR Reset to Default (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_reset_to_default.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_reset_to_default.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Reset to Default (VI)

Owning Palette:

Utility

Resets a signal to the default values.

[IMAGE alt='RFmxNR Reset to Default' src='rfmxnr_reset_to_default.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_select_measurement.html language=enus -->
## TOPIC 00084: RFmxNR Select Measurement (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_select_measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_select_measurement.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Select Measurement (VI)

Owning Palette:

RFmx NR VIs

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

#### RFmxNR Select Measurement (Single)

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='RFmxNR Select Measurement (Single)' src='rfmxnr_select_measurement_(single).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement specifies the measurement to perform. You can specify one of the following measurements. The default value is ModAcc. ModAcc (0) Enables the ModAcc measurement. SEM (1) Enables the SEM measurement. ACP (2) Enables the ACP measurement. CHP (3) Enables the CHP measurement. OBW (4) Enables the OBW measurement. PVT (5) Enables the PVT measurement. TXP (6) Enables the TXP measurement. |
| ModAcc (0) | Enables the ModAcc measurement. |
| SEM (1) | Enables the SEM measurement. |
| ACP (2) | Enables the ACP measurement. |
| CHP (3) | Enables the CHP measurement. |
| OBW (4) | Enables the OBW measurement. |
| PVT (5) | Enables the PVT measurement. |
| TXP (6) | Enables the TXP measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR Select Measurement (Multiple)

Enables all the measurements that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='RFmxNR Select Measurement (Multiple)' src='rfmxnr_select_measurement_(multiple).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurements specifies the measurements to perform. You can specify one or more of the following measurements. The default value is an empty array. ModAcc (0) Enables the ModAcc measurement. SEM (1) Enables the SEM measurement. ACP (2) Enables the ACP measurement. CHP (3) Enables the CHP measurement. OBW (4) Enables the OBW measurement. PVT (5) Enables the PVT measurement. TXP (6) Enables the TXP measurement. |
| ModAcc (0) | Enables the ModAcc measurement. |
| SEM (1) | Enables the SEM measurement. |
| ACP (2) | Enables the ACP measurement. |
| CHP (3) | Enables the CHP measurement. |
| OBW (4) | Enables the OBW measurement. |
| PVT (5) | Enables the PVT measurement. |
| TXP (6) | Enables the TXP measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_averaging.html language=enus -->
## TOPIC 00085: RFmxNR SEM Configure Averaging (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_averaging.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Averaging (VI)

Owning Palette:

SEM

Configures averaging for the SEM measurement.

[IMAGE alt='RFmxNR SEM Configure Averaging' src='rfmxnr_sem_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_component_carrier_rated_output_power.html language=enus -->
## TOPIC 00086: RFmxNR SEM Configure Component Carrier Rated Output Power (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_component_carrier_rated_output_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_component_carrier_rated_output_power.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Component Carrier Rated Output Power (VI)

Owning Palette:

SEM

Configures the rated output power (P<sub>rated</sub>, x) of the component carrier.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this VI.

|  | Note This VI is valid when you set the Link Direction property to Downlink, SEM DL Mask Type property to Standard, and gNodeB Category property to Medium Range Base Station. For more details please refer to section 6.6.4 of 3GPP 38.104 specification. |
| --- | --- |

[IMAGE alt='RFmxNR SEM Configure Component Carrier Rated Output Power' src='rfmxnr_sem_configure_component_carrier_rated_output_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Component Carrier Rated Output Power specifies the rated output power (Prated, x), which is used only to choose the limit table for medium range base station, FR2 Category A and FR2 Category B. This value is expressed in dBm. This parameter will be considered when you set the Link Direction property to Downlink, SEM DL Mask Type property to Standard, and gNodeB Category property to Medium Range Base Station or FR2 Category A or FR2 Category B. For more details please refer to section 6.6.4 and section 9.7.4 of 3GPP 38.104 specification. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_component_carrier_rated_output_power_(array).html language=enus -->
## TOPIC 00087: RFmxNR SEM Configure Component Carrier Rated Output Power (Array) (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_component_carrier_rated_output_power_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_component_carrier_rated_output_power_(array).html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Component Carrier Rated Output Power (Array) (VI)

Owning Palette:

Array VIs

Configures an array of the rated output power (P<sub>rated</sub>, x) of the component carrier.

Use "subblock<*n*>" as the selector string to read results from this VI.

|  | Note This VI is valid when you set the Link Direction property to Downlink, SEM DL Mask Type property to Standard, and gNodeB Category property to Medium Range Base Station. For more details please refer to section 6.6.4 of 3GPP 38.104 specification. |
| --- | --- |

[IMAGE alt='RFmxNR SEM Configure Component Carrier Rated Output Power (Array)' src='rfmxnr_sem_configure_component_carrier_rated_output_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Component Carrier Rated Output Power specifies an array of the rated output power (Prated, x), which is used only to choose the limit table for medium range base station, FR2 Category A and FR2 Category B. This value is expressed in dBm. This parameter will be considered when you set the Link Direction property to Downlink, SEM DL Mask Type property to Standard, and gNodeB Category property to Medium Range Base Station or FR2 Category A or FR2 Category B. For more details please refer to section 6.6.4 of 3GPP 38.104 specification. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_number_of_offsets.html language=enus -->
## TOPIC 00088: RFmxNR SEM Configure Number of Offsets (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_number_of_offsets.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Number of Offsets (VI)

Owning Palette:

SEM

Configures the number of offset segments for the SEM measurement.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR SEM Configure Number of Offsets' src='rfmxnr_sem_configure_number_of_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Offsets specifies the number of SEM offset segments. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_offset_absolute_limit.html language=enus -->
## TOPIC 00089: RFmxNR SEM Configure Offset Absolute Limit (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_offset_absolute_limit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_offset_absolute_limit.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Offset Absolute Limit (VI)

Owning Palette:

SEM

Configures the start and the stop limit of an offset segment.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxNR SEM Configure Offset Absolute Limit' src='rfmxnr_sem_configure_offset_absolute_limit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Absolute Limit Start specifies the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. The default value is -21. |
|  | Absolute Limit Stop specifies the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. The default value is -21. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_offset_absolute_limit_(array).html language=enus -->
## TOPIC 00090: RFmxNR SEM Configure Offset Absolute Limit (Array) (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_offset_absolute_limit_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_offset_absolute_limit_(array).html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Offset Absolute Limit (Array) (VI)

Owning Palette:

Array VIs

Configures an array of the start limit and the stop limit of the offset segments.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxNR SEM Configure Offset Absolute Limit (Array)' src='rfmxnr_sem_configure_offset_absolute_limit_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Absolute Limit Start specifies an array of the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. The default value is -21. |
|  | Absolute Limit Stop specifies an array of the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. The default value is -21. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_offset_bandwidth_integral.html language=enus -->
## TOPIC 00091: RFmxNR SEM Configure Offset Bandwidth Integral (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_offset_bandwidth_integral.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_offset_bandwidth_integral.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Offset Bandwidth Integral (VI)

Owning Palette:

SEM

Configures the bandwidth integral of the offset segments.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the selector string to configure or read this VI.

[IMAGE alt='RFmxNR SEM Configure Offset Bandwidth Integral' src='rfmxnr_sem_configure_offset_bandwidth_integral.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Bandwidth Integral specifies the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. When you set this parameter to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of a bandwidth integral and a RBW. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_offset_bandwidth_integral_(array).html language=enus -->
## TOPIC 00092: RFmxNR SEM Configure Offset Bandwidth Integral (Array) (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_offset_bandwidth_integral_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_offset_bandwidth_integral_(array).html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Offset Bandwidth Integral (Array) (VI)

Owning Palette:

Array VIs

Configures an array of the bandwidth integral of the offset segments.

Use "subblock<*n*>" as the selector string to configure or read this property.

[IMAGE alt='RFmxNR SEM Configure Offset Bandwidth Integral (Array)' src='rfmxnr_sem_configure_offset_bandwidth_integral_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Bandwidth Integral specifies an array of the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. When you set this parameter to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of a bandwidth integral and a RBW. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_offset_frequency.html language=enus -->
## TOPIC 00093: RFmxNR SEM Configure Offset Frequency (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_offset_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_offset_frequency.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Offset Frequency (VI)

Owning Palette:

SEM

Configures the start and stop frequencies and the sideband of an offset segment.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the selector string to configure or read this VI.

[IMAGE alt='RFmxNR SEM Configure Offset Frequency' src='rfmxnr_sem_configure_offset_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset Start Frequency specifies the start frequency of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. The default value is 0. |
|  | Offset Stop Frequency specifies the stop frequency of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. The default value is 1 MHz. |
|  | Offset Sideband specifies whether the offset segment is present either on one side or on both sides of a carrier. The default value is Both. Neg (0) Configures a lower offset segment to the left of the leftmost carrier. Pos (1) Configures an upper offset segment to the right of the rightmost carrier. Both (2) Configures both the negative and the positive offset segments. |
| Neg (0) | Configures a lower offset segment to the left of the leftmost carrier. |
| Pos (1) | Configures an upper offset segment to the right of the rightmost carrier. |
| Both (2) | Configures both the negative and the positive offset segments. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_offset_frequency_(array).html language=enus -->
## TOPIC 00094: RFmxNR SEM Configure Offset Frequency (Array) (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_offset_frequency_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_offset_frequency_(array).html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Offset Frequency (Array) (VI)

Owning Palette:

Array VIs

Configures an array of the start and stop frequencies and the sideband of an offset segment.

Use "subblock<*n*>" as the selector string to configure or read this VI.

[IMAGE alt='RFmxNR SEM Configure Offset Frequency (Array)' src='rfmxnr_sem_configure_offset_frequency_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset Start Frequency specifies an array of the start frequencies of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. The default value is 0. |
|  | Offset Stop Frequency specifies an array of the stop frequencies of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. The default value is 1 MHz. |
|  | Offset Sideband specifies an array of whether the offset segment is present either on one side or on both sides of a carrier. The default value is Both. Neg (0) Configures a lower offset segment to the left of the leftmost carrier. Pos (1) Configures an upper offset segment to the right of the rightmost carrier. Both (2) Configures both the negative and the positive offset segments. |
| Neg (0) | Configures a lower offset segment to the left of the leftmost carrier. |
| Pos (1) | Configures an upper offset segment to the right of the rightmost carrier. |
| Both (2) | Configures both the negative and the positive offset segments. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_offset_limit_fail_mask.html language=enus -->
## TOPIC 00095: RFmxNR SEM Configure Offset Limit Fail Mask (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_offset_limit_fail_mask.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_offset_limit_fail_mask.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Offset Limit Fail Mask (VI)

Owning Palette:

SEM

Configures the limit fail mask of the offset segments that specify the criteria to determine the measurement fail status.

Use "offset<*n*>" or "subblock<*n*>/"offset<*n*>" as the selector string to configure or read this VI.

[IMAGE alt='RFmxNR SEM Configure Offset Limit Fail Mask' src='rfmxnr_sem_configure_offset_limit_fail_mask.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Limit Fail Mask specifies the criteria to determine the measurement fail status. The default value is Absolute. Abs AND Rel (0) Specifies that the measurement fails if the power in the segment exceeds both the absolute and relative masks. Abs OR Rel (1) Specifies that the measurement fails if the power in the segment exceeds either the absolute or relative mask. Absolute (2) Specifies that the measurement fails if the power in the segment exceeds the absolute mask. Relative (3) Specifies that the measurement fails if the power in the segment exceeds the relative mask. |
| Abs AND Rel (0) | Specifies that the measurement fails if the power in the segment exceeds both the absolute and relative masks. |
| Abs OR Rel (1) | Specifies that the measurement fails if the power in the segment exceeds either the absolute or relative mask. |
| Absolute (2) | Specifies that the measurement fails if the power in the segment exceeds the absolute mask. |
| Relative (3) | Specifies that the measurement fails if the power in the segment exceeds the relative mask. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_offset_limit_fail_mask_(array).html language=enus -->
## TOPIC 00096: RFmxNR SEM Configure Offset Limit Fail Mask (Array) (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_offset_limit_fail_mask_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_offset_limit_fail_mask_(array).html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Offset Limit Fail Mask (Array) (VI)

Owning Palette:

Array VIs

Configures an array of the limit fail mask of the offset segments that specifies the criteria to determine the measurement fail status.

Use "subblock<*n*>" as the selector string to configure or read this VI.

[IMAGE alt='RFmxNR SEM Configure Offset Limit Fail Mask (Array)' src='rfmxnr_sem_configure_offset_limit_fail_mask_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Limit Fail Mask specifies an array of the criteria to determine the measurement fail status. The default value is Absolute. Abs AND Rel (0) Specifies that the measurement fails if the power in the segment exceeds both the absolute and relative masks. Abs OR Rel (1) Specifies that the measurement fails if the power in the segment exceeds either the absolute or relative mask. Absolute (2) Specifies that the measurement fails if the power in the segment exceeds the absolute mask. Relative (3) Specifies that the measurement fails if the power in the segment exceeds the relative mask. |
| Abs AND Rel (0) | Specifies that the measurement fails if the power in the segment exceeds both the absolute and relative masks. |
| Abs OR Rel (1) | Specifies that the measurement fails if the power in the segment exceeds either the absolute or relative mask. |
| Absolute (2) | Specifies that the measurement fails if the power in the segment exceeds the absolute mask. |
| Relative (3) | Specifies that the measurement fails if the power in the segment exceeds the relative mask. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_offset_rbw_filter.html language=enus -->
## TOPIC 00097: RFmxNR SEM Configure Offset RBW Filter (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_offset_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_offset_rbw_filter.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Offset RBW Filter (VI)

Owning Palette:

SEM

Configures the offset RBW and the offset RBW filter type.

Use "offset<*n*>" or "subblock<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxNR SEM Configure Offset RBW Filter' src='rfmxnr_sem_configure_offset_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset RBW specifies the bandwidth of an RBW filter used to sweep an acquired offset segment. This value is expressed in Hz. The default value is 30 kHz. |
|  | Offset RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) The RBW filter has a Gaussian response. Flat (2) The RBW filter has a flat response. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | The RBW filter has a Gaussian response. |
| Flat (2) | The RBW filter has a flat response. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_offset_rbw_filter_(array).html language=enus -->
## TOPIC 00098: RFmxNR SEM Configure Offset RBW Filter (Array) (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_offset_rbw_filter_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_offset_rbw_filter_(array).html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Offset RBW Filter (Array) (VI)

Owning Palette:

Array VIs

Configures the offset RBW and the offset RBW filter type array.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxNR SEM Configure Offset RBW Filter (Array)' src='rfmxnr_sem_configure_offset_rbw_filter_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset RBW specifies an array of the bandwidth of an RBW filter used to sweep an acquired offset segment. This value is expressed in Hz. The default value is 30 kHz. |
|  | Offset RBW Filter Type specifies an array of the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) The RBW filter has a Gaussian response. Flat (2) The RBW filter has a flat response. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | The RBW filter has a Gaussian response. |
| Flat (2) | The RBW filter has a flat response. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_offset_relative_limit.html language=enus -->
## TOPIC 00099: RFmxNR SEM Configure Offset Relative Limit (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_offset_relative_limit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_offset_relative_limit.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Offset Relative Limit (VI)

Owning Palette:

SEM

Configures the start and stop relative limit of the offset segment.

Use "offset<*n*>" or "subblock<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to configure this VI.

|  | Note This VI is considered only when you set the Link Direction property to Downlink and SEM DL Mask Type property to Custom. |
| --- | --- |

[IMAGE alt='RFmxNR SEM Configure Offset Relative Limit' src='rfmxnr_sem_configure_offset_relative_limit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Relative Limit Start specifies the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. The default value is -53. |
|  | Relative Limit Stop specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. The default value is -60. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_offset_relative_limit_(array).html language=enus -->
## TOPIC 00100: RFmxNR SEM Configure Offset Relative Limit (Array) (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_offset_relative_limit_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_offset_relative_limit_(array).html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Offset Relative Limit (Array) (VI)

Owning Palette:

Array VIs

Configures an array of the start and stop relative limit of the offset segment.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxNR SEM Configure Offset Relative Limit (Array)' src='rfmxnr_sem_configure_offset_relative_limit_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Relative Limit Start specifies an array of the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. The default value is -53. |
|  | Relative Limit Stop specifies an array of the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. The default value is -60. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_sweep_time.html language=enus -->
## TOPIC 00101: RFmxNR SEM Configure Sweep Time (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_sweep_time.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Sweep Time (VI)

Owning Palette:

SEM

Configures the sweep time.

[IMAGE alt='RFmxNR SEM Configure Sweep Time' src='rfmxnr_sem_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement sets the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement calculates the sweep time internally. For DL, the sweep time is calculated based on the value of the OBW RBW property, and for UL, it uses a sweep time of 1 ms. |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement calculates the sweep time internally. For DL, the sweep time is calculated based on the value of the OBW RBW property, and for UL, it uses a sweep time of 1 ms. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_configure_uplink_mask_type.html language=enus -->
## TOPIC 00102: RFmxNR SEM Configure Uplink Mask Type (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_configure_uplink_mask_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_configure_uplink_mask_type.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Configure Uplink Mask Type (VI)

Owning Palette:

SEM

Configures the standard defined mask type that has to be used in the measurement for uplink.

[IMAGE alt='RFmxNR SEM Configure Uplink Mask Type' src='rfmxnr_sem_configure_uplink_mask_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Uplink Mask Type specifies the spectrum emission mask used in the measurement for uplink. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.5.2 of the 3GPP 38.101 specification for more information about standard-defined mask types. The default value is General. General (0) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.2-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification, Table 6.5.2.1-1 and 6.5A.2.1-1 in section 6.5.2 of the 3GPP TS 38.101-2 specification and Table 6.5B.2.1.1-1 in section 6.5B of the 3GPP TS 38.101-3 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.1.5-1, 6.6.2.1.5-2, 6.6.2.1A.1.5-1, and 6.6.2.1A.1.5-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. NS_35 (1) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.1-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification and Table 6.5B.2.1.2.1-1 in section 6.5B of the 3GPP TS 38.101-3 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.5-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. Custom (2) You need to configure the SEM Num Offsets, SEM Offset Start Freq, SEM Offset Stop Freq, SEM Offset Abs Limit Start, SEM Offset Abs Limit Stop, SEM Offset Sideband, SEM Offset RBW, SEM Offset RBW Filter Type, and SEM Offset BW Integral properties for each offset. NS_03 (3) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. NS_04 (4) The measurement selects the offset frequencies and limits for the SEM as defined in Table 6.5.2.3.2-3 in section 6.5.2 of the 3GPP TS 38.101-1 specification. Subcarrier spacing can be configured through BWP Subcarrier Spacing property. Subcarrier spacing corresponding to first bandwidth part is used for computing mask. Transform precoding can be configured through PUSCH Transform Precoding Enabled property. Transform precoding corresponding to first bandwidth part is used for computing mask. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.3.2-3 in section 6.6.2 of the 3GPP TS 36.521-1 specification. NS_06 (5) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.4-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.3-1 and 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. NS_21 (6) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. NS_27 (7) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.8-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of intra-band contiguous CA consisting of at least one subblock with all NR carriers, for the NR subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.2A.2.3.2.1-1 in section 6.5A.2.3 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.3.4-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. NS_07 (8) The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.4-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.3-1 and Table 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| General (0) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.2-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification, Table 6.5.2.1-1 and 6.5A.2.1-1 in section 6.5.2 of the 3GPP TS 38.101-2 specification and Table 6.5B.2.1.1-1 in section 6.5B of the 3GPP TS 38.101-3 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.1.5-1, 6.6.2.1.5-2, 6.6.2.1A.1.5-1, and 6.6.2.1A.1.5-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS_35 (1) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.1-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification and Table 6.5B.2.1.2.1-1 in section 6.5B of the 3GPP TS 38.101-3 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.5-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| Custom (2) | You need to configure the SEM Num Offsets, SEM Offset Start Freq, SEM Offset Stop Freq, SEM Offset Abs Limit Start, SEM Offset Abs Limit Stop, SEM Offset Sideband, SEM Offset RBW, SEM Offset RBW Filter Type, and SEM Offset BW Integral properties for each offset. |
| NS_03 (3) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS_04 (4) | The measurement selects the offset frequencies and limits for the SEM as defined in Table 6.5.2.3.2-3 in section 6.5.2 of the 3GPP TS 38.101-1 specification. Subcarrier spacing can be configured through BWP Subcarrier Spacing property. Subcarrier spacing corresponding to first bandwidth part is used for computing mask. Transform precoding can be configured through PUSCH Transform Precoding Enabled property. Transform precoding corresponding to first bandwidth part is used for computing mask. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.3.2-3 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS_06 (5) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.4-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.3-1 and 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS_21 (6) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS_27 (7) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.8-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of intra-band contiguous CA consisting of at least one subblock with all NR carriers, for the NR subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.2A.2.3.2.1-1 in section 6.5A.2.3 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.3.4-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS_07 (8) | The measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.5.2.3.4-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.3-1 and Table 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_sem_fetch.html language=enus -->
## TOPIC 00103: RFmxNR SEM Fetch (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_sem_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_sem_fetch.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR SEM Fetch (VI)

Owning Palette:

Fetch

Fetches the SEM measurements.

#### RFmxNR SEM Fetch Total Aggregated Power

Returns the sum of powers in all the subblocks.

[IMAGE alt='RFmxNR SEM Fetch Total Aggregated Power' src='rfmxnr_sem_fetch_total_aggregated_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Aggregated Power returns the total power of all the subblocks. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Measurement Status

Returns the overall measurement status based on the standard mask type that you configure.

[IMAGE alt='RFmxNR SEM Fetch Measurement Status' src='rfmxnr_sem_fetch_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Subblock Measurement

Fetches the power, integration bandwidth, and center frequency of the subblock.

[IMAGE alt='RFmxNR SEM Fetch Subblock Measurement' src='rfmxnr_sem_fetch_subblock_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Subblock Power returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. This includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. |
|  | Integration Bandwidth returns the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within a subblock. This value is expressed in Hz. |
|  | Frequency returns the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Component Carrier Measurement

Returns the absolute and relative powers measured in the component carriers.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR SEM Fetch Component Carrier Measurement' src='rfmxnr_sem_fetch_component_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. |
|  | Peak Absolute Power returns the peak power in the component carrier. This value is expressed in dBm. |
|  | Peak Frequency returns the frequency at which peak power occurs in the component carrier. This value is expressed in Hz. |
|  | Relative Power returns the component carrier power relative to its subblock power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Lower Offset Margin

Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for lower offset segments. The relative power is relative to the total aggregated power.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR SEM Fetch Lower Offset Margin' src='rfmxnr_sem_fetch_lower_offset_margin.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |
|  | Margin returns the margin from the absolute limit mask for lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
|  | Margin Frequency returns the frequency at which the margin occurs in the lower offset. This value is expressed in Hz. |
|  | Margin Relative Power returns the power at which the margin occurs in the lower offset segment. This value is expressed in dB. |
|  | Margin Absolute Power returns the power at which the margin occurs in the lower offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Lower Offset Power

Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR SEM Fetch Lower Offset Power' src='rfmxnr_sem_fetch_lower_offset_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Absolute Power returns the lower (negative) offset segment power. This value is expressed in dBm. |
|  | Total Relative Power returns the power in the lower offset segment relative to total aggregated power. This value is expressed in dB. |
|  | Peak Absolute Power returns the peak power in the lower offset segment. This value is expressed in dBm. |
|  | Peak Relative Power returns the peak power in the lower offset segment relative to total aggregated power. This value is expressed in dB. |
|  | Peak Frequency returns the frequency at which the peak power occurs in the lower offset segment. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Upper Offset Margin

Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for upper offset segments. The relative power is relative to the total aggregated power.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR SEM Fetch Upper Offset Margin' src='rfmxnr_sem_fetch_upper_offset_margin.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |
|  | Margin returns the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
|  | Margin Frequency returns the frequency at which the margin occurs in the upper offset. This value is expressed in Hz. |
|  | Margin Relative Power returns the power at which the margin occurs in the upper offset segment. This value is expressed in dB. |
|  | Margin Absolute Power returns the power at which the margin occurs in the upper offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Upper Offset Power

Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the upper offset segment. The relative power is relative to the total aggregated power.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR SEM Fetch Upper Offset Power' src='rfmxnr_sem_fetch_upper_offset_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Absolute Power returns the upper (positive) offset segment power. This value is expressed in dBm. |
|  | Total Relative Power returns the power in the upper offset segment relative to total aggregated power. This value is expressed in dB. |
|  | Peak Absolute Power returns the peak power in the upper offset segment. This value is expressed in dBm. |
|  | Peak Relative Power returns the peak power in the upper offset segment relative to total aggregated power. This value is expressed in dB. |
|  | Peak Frequency returns the frequency at which the peak power occurs in the upper offset segment. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Component Carrier Measurement (Array)

Returns an array of the absolute and relative powers measured in the component carriers.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR SEM Fetch Component Carrier Measurement (Array)' src='rfmxnr_sem_fetch_component_carrier_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns an array of the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. |
|  | Peak Absolute Power returns an array of the peak power in the component carrier. This value is expressed in dBm. |
|  | Peak Frequency returns an array of the frequency at which peak power occurs in the component carrier. This value is expressed in Hz. |
|  | Relative Power returns an array of the component carrier power relative to its subblock power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Lower Offset Margin (Array)

Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for lower offset segments. The relative power is relative to the total aggregated power.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR SEM Fetch Lower Offset Margin (Array)' src='rfmxnr_sem_fetch_lower_offset_margin_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns an array of the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |
|  | Margin returns an array of the margin from the absolute limit mask for lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
|  | Margin Frequency returns an array of the frequency at which the margin occurs in the lower offset. This value is expressed in Hz. |
|  | Margin Relative Power returns an array of the power at which the margin occurs in the lower offset segment. This value is expressed in dB. |
|  | Margin Absolute Power returns an array of the power at which the margin occurs in the lower offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Lower Offset Power (Array)

Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR SEM Fetch Lower Offset Power (Array)' src='rfmxnr_sem_fetch_lower_offset_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Absolute Power returns an array of the lower (negative) segment power. This value is expressed in dBm. |
|  | Total Relative Power returns an array of the power in the lower offset segment relative to total aggregated power. This value is expressed in dB. |
|  | Peak Absolute Power returns an array of the peak power in the lower offset segment. This value is expressed in dBm. |
|  | Peak Frequency returns an array of the frequency at which the peak power occurs in the lower offset segment. This value is expressed in Hz. |
|  | Peak Relative Power returns an array of the peak power in the lower offset segment relative to total aggregated power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Upper Offset Margin (Array)

Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for upper offset segments. The relative power is relative to the total aggregated power.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR SEM Fetch Upper Offset Margin (Array)' src='rfmxnr_sem_fetch_upper_offset_margin_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns an array of the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |
|  | Margin returns an array of the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. |
|  | Margin Frequency returns an array of the frequency at which the margin occurs in the upper offset. This value is expressed in Hz. |
|  | Margin Relative Power returns an array of the power at which the margin occurs in the upper (positive) offset segment. This value is expressed in dB. |
|  | Margin Absolute Power returns an array of the power at which the margin occurs in the upper offset segment. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Upper Offset Power (Array)

Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of upper offset segments. The relative power is relative to total aggregated power.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxNR SEM Fetch Upper Offset Power (Array)' src='rfmxnr_sem_fetch_upper_offset_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Absolute Power returns an array of the upper segment power. This value is expressed in dBm. |
|  | Total Relative Power returns an array of the power in the upper offset segment relative to total aggregated power. This value is expressed in dB. |
|  | Peak Absolute Power returns an array of the peak power in the upper offset segment. This value is expressed in dBm. |
|  | Peak Frequency returns an array of the frequency at which the peak power occurs in the upper offset segment. This value is expressed in Hz. |
|  | Peak Relative Power returns an array of the peak power in the upper offset segment relative to total aggregated power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR SEM Fetch Spectrum

Fetches the spectrum used for SEM measurements.

[IMAGE alt='RFmxNR SEM Fetch Spectrum' src='rfmxnr_sem_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the spectrum. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | Composite Mask returns the composite mask trace used for the channel. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the array of composite mask used for the channel. This value is expressed in dBm. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the array of composite mask used for the channel. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_send_software_edge_trigger.html language=enus -->
## TOPIC 00104: RFmxNR Send Software Edge Trigger (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_send_software_edge_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_send_software_edge_trigger.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Send Software Edge Trigger (VI)

Owning Palette:

Configuration

Sends a trigger to the device when you use the [RFmxNR Configure Trigger](rfmxnr_configure_trigger.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxNR Initiate VI.

[IMAGE alt='RFmxNR Send Software Edge Trigger' src='rfmxnr_send_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_txp_fetch.html language=enus -->
## TOPIC 00105: RFmxNR TXP Fetch (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_txp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_txp_fetch.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR TXP Fetch (VI)

Fetches the TXP measurements.

#### RFmxNR TXP Fetch Measurement

Fetches the average power and peak power of the the signal over which power measurments are performed.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

[IMAGE alt='RFmxNR TXP Fetch Measurement' src='rfmxnr_txp_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Average Power Mean returns the average power of the the signal over which power measurments are performed. This value is expressed in dBm. |
|  | Peak Power Maximum returns the peak power of the the signal over which power measurments are performed. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxNR TXP Fetch Power Trace

Fetches power versus time trace.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

[IMAGE alt='RFmxNR TXP Fetch Power Trace' src='rfmxnr_txp_fetch_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Power returns power versus time trace. This value is expressed in dBm. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the measured average power at each time instance, in dBm. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the measured average power at each time instance, in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/rfmxnr_wait_for_measurement_complete.html language=enus -->
## TOPIC 00106: RFmxNR Wait for Measurement Complete (VI)

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/rfmxnr_wait_for_measurement_complete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/rfmxnr_wait_for_measurement_complete.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

RFmxNR Wait for Measurement Complete (VI)

Owning Palette:

Utility

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='RFmxNR Wait for Measurement Complete' src='rfmxnr_wait_for_measurement_complete.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/sem_array_vis_pal.html language=enus -->
## TOPIC 00107: Array VIs

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/sem_array_vis_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/sem_array_vis_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

Array VIs

Owning Palette:

SEM

Use the array VIs on this palette to configure the SEM measurements. You can also use the [RFmxNR Property Node](../rfmxnrvi/rfmxnr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxNR SEM Configure Component Carrier Rated Output Power (Array) | Configures an array of the rated output power (Prated, x) of the component carrier. Use "subblock<n>" as the selector string to read results from this VI. |
| RFmxNR SEM Configure Offset Frequency (Array) | Configures an array of the start and stop frequencies and the sideband of an offset segment. Use "subblock<n>" as the selector string to configure or read this VI. |
| RFmxNR SEM Configure Offset Bandwidth Integral (Array) | Configures an array of the bandwidth integral of the offset segments. Use "subblock<n>" as the selector string to configure or read this property. |
| RFmxNR SEM Configure Offset RBW Filter (Array) | Configures the offset RBW and the offset RBW filter type array. Use "subblock<n>" as the selector string to configure this VI. |
| RFmxNR SEM Configure Offset Limit Fail Mask (Array) | Configures an array of the limit fail mask of the offset segments that specifies the criteria to determine the measurement fail status. Use "subblock<n>" as the selector string to configure or read this VI. |
| RFmxNR SEM Configure Offset Absolute Limit (Array) | Configures an array of the start limit and the stop limit of the offset segments. Use "subblock<n>" as the selector string to configure this VI. |
| RFmxNR SEM Configure Offset Relative Limit (Array) | Configures an array of the start and stop relative limit of the offset segment. Use "subblock<n>" as the selector string to configure this VI. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/sem_pal.html language=enus -->
## TOPIC 00108: SEM

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/sem_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/sem_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

SEM

Owning Palette:

Configuration

Use the VIs on this palette to configure SEM measurements. You can also use the [RFmxNR Property Node](../rfmxnrvi/rfmxnr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxNR SEM Configure Averaging | Configures averaging for the SEM measurement. |
| RFmxNR SEM Configure Sweep Time | Configures the sweep time. |
| RFmxNR SEM Configure Uplink Mask Type | Configures the standard defined mask type that has to be used in the measurement for uplink. |
| RFmxNR SEM Configure Component Carrier Rated Output Power | Configures the rated output power (Prated, x) of the component carrier. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxNR SEM Configure Number of Offsets | Configures the number of offset segments for the SEM measurement. Use "subblock<n>" as the selector string to read results from this VI. |
| RFmxNR SEM Configure Offset Frequency | Configures the start and stop frequencies and the sideband of an offset segment. Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the selector string to configure or read this VI. |
| RFmxNR SEM Configure Offset Bandwidth Integral | Configures the bandwidth integral of the offset segments. Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the selector string to configure or read this VI. |
| RFmxNR SEM Configure Offset RBW Filter | Configures the offset RBW and the offset RBW filter type. Use "offset<n>" or "subblock<n>" or "subblock<n>/offset<n>" as the selector string to configure this VI. |
| RFmxNR SEM Configure Offset Limit Fail Mask | Configures the limit fail mask of the offset segments that specify the criteria to determine the measurement fail status. Use "offset<n>" or "subblock<n>/"offset<n>" as the selector string to configure or read this VI. |
| RFmxNR SEM Configure Offset Absolute Limit | Configures the start and the stop limit of an offset segment. Use "offset<n>" or "subblock<n>/offset<n>" as the selector string to configure this VI. |
| RFmxNR SEM Configure Offset Relative Limit | Configures the start and stop relative limit of the offset segment. Use "offset<n>" or "subblock<n>" or "subblock<n>/offset<n>" as the selector string to configure this VI. |
| RFmxNR Build Subblock String | Creates the subblock string. |
| RFmxNR Build Offset String | Creates the offset string. |

| Subpalette | Description |
| --- | --- |
| Array VIs | Use the array VIs on this palette to configure the SEM measurements. You can also use the RFmxNR Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-nr-vi path=rfmxnrvi/utility_pal.html language=enus -->
## TOPIC 00109: Utility

- bundle_id: `rfmx-nr-vi`
- source_path: `rfmxnrvi/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-vi/raw/resource/enus/rfmxnrvi/utility_pal.html
- document_id: `rfmx-nr-vi`
- page_type: `leaf`
- content_type: ``

Utility

Owning Palette:

RFmx NR VIs

Use the VIs on this palette to configure RFmx NR utilities.

| Palette Object | Description |
| --- | --- |
| RFmxNR Commit | Commits settings to the hardware. Calling this VI is optional. RFmxNR commits settings to the hardware when you call the RFmxNR Initiate VI. |
| RFmxNR Reset to Default | Resets a signal to the default values. |
| RFmxNR Wait for Measurement Complete | Waits for the specified number for seconds for all the measurements to complete. |
| RFmxNR Check Measurement Status | Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
