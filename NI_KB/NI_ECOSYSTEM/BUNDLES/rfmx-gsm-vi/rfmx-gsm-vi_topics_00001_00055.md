# NI DOCUMENT BUNDLE: rfmx-gsm-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-gsm-vi start=1 end=55 -->
<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/advanced_pal.html language=enus -->
## TOPIC 00001: rfmxgsmvi/advanced_pal.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/advanced_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/advanced_pal.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

Advanced

Advanced

Owning Palette:

RFmx GSM VIs

Use the VIs on this palette to use advanced features.

| Palette Object | Description |
| --- | --- |
| RFmxGSM Abort Measurements | Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. This acquisition and measurements were previously initiated by the RFmxGSM Initiate VI. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error. |
| RFmxGSM Analyze (IQ, 1 Wfm) | Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended Acquisition Type property value is IQ. |
| RFmxGSM Create Signal Configuration | Creates a new instance of a signal. |
| RFmxGSM Clone Signal Configuration | Creates a new instance of a signal by copying all the property values from an existing signal instance. |
| RFmxGSM Delete Signal Configuration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxGSM Clear Named Result | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxGSM Clear All Named Results | Clears all results for the signal that you specify in the Selector String parameter. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/build_string_pal.html language=enus -->
## TOPIC 00002: rfmxgsmvi/build_string_pal.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/build_string_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/build_string_pal.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

Build String

Build String

Owning Palette:

RFmx GSM VIs

Use the VIs on this palette to create strings for configurations that require a selector string.

| Palette Object | Description |
| --- | --- |
| RFmxGSM Build Signal String | Creates selector string for use with configuration or fetch properties and VIs. |
| RFmxGSM Build Slot String | Creates a slot string to be used as the selector string with configuration or fetch properties and VIs. |
| RFmxGSM Build Offset String | Creates an offset string to be used as the selector string with configuration or fetch properties and VIs. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/configuration_pal.html language=enus -->
## TOPIC 00003: rfmxgsmvi/configuration_pal.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/configuration_pal.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

Configuration

Configuration

Owning Palette:

RFmx GSM VIs

Use the VIs on this palette to configure measurements. You can use the RFmxGSM Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxGSM Configure RF | Configures the RF properties of the signal specified by the selector string. |
| RFmxGSM Configure Frequency | Configures the expected center frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| RFmxGSM Configure Reference Level | Configures the reference level, which represents the maximum expected power of an RF input signal. |
| RFmxGSM Auto Level | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level. |
| RFmxGSM Configure External Attenuation | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. |
| RFmxGSM Configure Trigger | Configures the Reference Trigger used to acquire the signal. |
| RFmxGSM Send Software Edge Trigger | Sends a trigger to the device when you use the RFmxGSM Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. |
| RFmxGSM Configure Link Direction | Configures the source of the signal to be measured. |
| RFmxGSM Configure Signal Type | Configures the signal type. Use "slot<n>" as the selector string to configure this VI. |
| RFmxGSM Configure Auto TSC Detection Enabled | Configures whether to auto detect the training sequence code (TSC). |
| RFmxGSM Configure TSC | Configures the training sequence code (TSC) in the burst. Use "slot<n>" as the selector string to configure this VI. |
| RFmxGSM Configure Number of Timeslots | Configures the number of time slots to be measured. |
| RFmxGSM Configure Band | Configures the band of operation. |
| RFmxGSM Configure Power Control Level | Configures the power control level corresponding to the transmitted power. Use "slot<n>" as the selector string to configure this VI. |
| RFmxGSM Configure Burst Synchronization Type | Configures the burst synchronization type. |

| Subpalette | Description |
| --- | --- |
| ModAcc | Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements. |
| ORFS | Use the VIs on this palette to configure output radio frequency spectrum (ORFS) measurements. |
| PVT | Use the VIs on this palette to configure power versus time (PVT) measurements. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/fetch_pal.html language=enus -->
## TOPIC 00004: rfmxgsmvi/fetch_pal.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/fetch_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/fetch_pal.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

Fetch

Fetch

Use the VIs on this palette to fetch measurement results and traces.

| Palette Object | Description |
| --- | --- |
| RFmxGSM ModAcc Fetch | Fetches the ModAcc measurement results. |
| RFmxGSM ORFS Fetch | Fetches the output radio frequency spectrum (ORFS) measurement results. |
| RFmxGSM PVT Fetch | Fetches the power versus time (PVT) measurement results. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/gsm_pal.html language=enus -->
## TOPIC 00005: rfmxgsmvi/gsm_pal.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/gsm_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/gsm_pal.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmx GSM VIs

RFmx GSM VIs

Use the VIs on this palette to perform GSM measurements. You can use the RFmxGSM Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxGSM Select Measurement | Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. |
| RFmxGSM Initiate | Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the RFmxGSM Wait for Measurement Complete VI or RFmxGSM Check Measurement Status VI. |
| RFmxGSM Property Node | Gets (reads), sets (writes), or resets (sets to default value) RFmxGSM properties. |

| Subpalette | Description |
| --- | --- |
| Configuration | Use the VIs on this palette to configure measurements. You can use the RFmxGSM Property Node to configure additional properties. |
| Utility | Use the VIs on this palette to configure utility measurements. You can use the RFmxGSM Property Node to configure additional properties. |
| Build String | Use the VIs on this palette to create strings for configurations that require a selector string. |
| Advanced | Use the VIs on this palette to use advanced features. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/modacc_pal.html language=enus -->
## TOPIC 00006: rfmxgsmvi/modacc_pal.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/modacc_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/modacc_pal.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

ModAcc

ModAcc

Owning Palette:

Configuration

Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements.

| Palette Object | Description |
| --- | --- |
| RFmxGSM ModAcc Configure Droop Compensation Enabled | Configures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement. |
| RFmxGSM ModAcc Configure Averaging | Configures averaging for the modulation accuracy (ModAcc) measurement. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/orfs_pal.html language=enus -->
## TOPIC 00007: rfmxgsmvi/orfs_pal.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/orfs_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/orfs_pal.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

ORFS

ORFS

Owning Palette:

Configuration

Use the VIs on this palette to configure output radio frequency spectrum (ORFS) measurements.

| Palette Object | Description |
| --- | --- |
| RFmxGSM ORFS Configure Measurement Type | Configures the type of spectral distortion to be measured. |
| RFmxGSM ORFS Configure Averaging | Configures averaging for the output radio frequency spectrum (ORFS) measurement. |
| RFmxGSM ORFS Configure Offset Frequency Mode | Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. |
| RFmxGSM ORFS Configure Evaluation Symbols | Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify the portion of the burst to measure for ORFS due to modulation. RFmx considers the measurement over evaluation symbols for a single burst as one average. |
| RFmxGSM ORFS Configure Noise Compensation Enabled | Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. |
| RFmxGSM ORFS Configure Modulation Custom Offset Frequency (Array) | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the ORFS Offset Freq Mode property to Custom. |
| RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array) | Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the ORFS Offset Freq Mode property to Custom. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/pvt_pal.html language=enus -->
## TOPIC 00008: rfmxgsmvi/pvt_pal.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/pvt_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/pvt_pal.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

PVT

PVT

Owning Palette:

Configuration

Use the VIs on this palette to configure power versus time (PVT) measurements.

| Palette Object | Description |
| --- | --- |
| RFmxGSM PVT Configure Averaging | Configures averaging for the power versus time (PVT) measurement. |
| RFmxGSM Build Slot String | Creates a slot string to be used as the selector string with configuration or fetch properties and VIs. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_abort_measurements.html language=enus -->
## TOPIC 00009: rfmxgsmvi/rfmxgsm_abort_measurements.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_abort_measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_abort_measurements.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Abort Measurements (VI)

RFmxGSM Abort Measurements (VI)

Owning Palette:

Advanced

Stops acquisition and measurements associated with the signal instance that you specify in the **Selector String** parameter. This acquisition and measurements were previously initiated by the [RFmxGSM Initiate](rfmxgsm_initiate.html) VI. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='RFmxGSM Abort Measurements' src='rfmxgsm_abort_measurements.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_analyze_(iq_1_wfm).html language=enus -->
## TOPIC 00010: rfmxgsmvi/rfmxgsm_analyze_(iq_1_wfm).html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_analyze_(iq_1_wfm).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_analyze_(iq_1_wfm).html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Analyze (IQ, 1 Wfm) (VI)

RFmxGSM Analyze (IQ, 1 Wfm) (VI)

Owning Palette:

Advanced

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.

Use this VI only if the Recommended Acquisition Type property value is **IQ**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmx GSM Commit VI. |
| --- | --- |

[IMAGE alt='RFmxGSM Analyze (IQ 1 Wfm)' src='rfmxgsm_analyze_(iq_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". |
| --- | --- |
|  | IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 specifies the start time of the input Y array. This value is expressed in seconds. dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input Y array. This value is expressed in seconds. |
|  | dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to Selector String parameter on Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_auto_level.html language=enus -->
## TOPIC 00011: rfmxgsmvi/rfmxgsm_auto_level.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_auto_level.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Auto Level (VI)

RFmxGSM Auto Level (VI)

Owning Palette:

Configuration

Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxGSM Auto Level VI performs the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

You can also specify the starting reference level using the Auto Level Initial Reference Level property. Call this VI after configuring all signal properties.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmx GSM Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this VI, thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='RFmxGSM Auto Level' src='rfmxgsm_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Interval specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 4.6 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Reference Level returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_build_offset_string.html language=enus -->
## TOPIC 00012: rfmxgsmvi/rfmxgsm_build_offset_string.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_build_offset_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_build_offset_string.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Build Offset String (VI)

RFmxGSM Build Offset String (VI)

Owning Palette:

Build String

Creates an offset string to be used as the selector string with configuration or fetch properties and VIs.

[IMAGE alt='RFmxGSM Build Offset String' src='rfmxgsm_build_offset_string.gif']

|  | Offset Number specifies the offset number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_build_signal_string.html language=enus -->
## TOPIC 00013: rfmxgsmvi/rfmxgsm_build_signal_string.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_build_signal_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_build_signal_string.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Build Signal String (VI)

RFmxGSM Build Signal String (VI)

Owning Palette:

Build String

Creates selector string for use with configuration or fetch properties and VIs.

[IMAGE alt='RFmxGSM Build Signal String' src='rfmxgsm_build_signal_string.gif']

|  | Result Name specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. The default is "" (empty string). Example: "result::r1" "r1" |
| --- | --- |
|  | Signal Name specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default is "" (empty string). Example: "signal::sig1" "sig1" |
|  | Selector String returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_build_slot_string.html language=enus -->
## TOPIC 00014: rfmxgsmvi/rfmxgsm_build_slot_string.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_build_slot_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_build_slot_string.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Build Slot String (VI)

RFmxGSM Build Slot String (VI)

Owning Palette:

PVT

Creates a slot string to be used as the selector string with configuration or fetch properties and VIs.

[IMAGE alt='RFmxGSM Build Slot String' src='rfmxgsm_build_slot_string.gif']

|  | Slot Number specifies the slot number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_check_measurement_status.html language=enus -->
## TOPIC 00015: rfmxgsmvi/rfmxgsm_check_measurement_status.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_check_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_check_measurement_status.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Check Measurement Status (VI)

RFmxGSM Check Measurement Status (VI)

Owning Palette:

Utility

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='RFmxGSM Check Measurement Status' src='rfmxgsm_check_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | done? indicates whether the measurement is complete. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_clear_all_named_results.html language=enus -->
## TOPIC 00016: rfmxgsmvi/rfmxgsm_clear_all_named_results.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_clear_all_named_results.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_clear_all_named_results.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Clear All Named Results (VI)

RFmxGSM Clear All Named Results (VI)

Owning Palette:

Advanced

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxGSM Clear All Named Results' src='rfmxgsm_clear_all_named_results.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_clear_named_result.html language=enus -->
## TOPIC 00017: rfmxgsmvi/rfmxgsm_clear_named_result.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_clear_named_result.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_clear_named_result.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Clear Named Result (VI)

RFmxGSM Clear Named Result (VI)

Owning Palette:

Advanced

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='RFmxGSM Clear Named Result' src='rfmxgsm_clear_named_result.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_clone_signal_configuration.html language=enus -->
## TOPIC 00018: rfmxgsmvi/rfmxgsm_clone_signal_configuration.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_clone_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_clone_signal_configuration.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Clone Signal Configuration (VI)

RFmxGSM Clone Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='RFmxGSM Clone Signal Configuration' src='rfmxgsm_clone_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
|  | Old Signal Name specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of configure, initiate, and fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_commit.html language=enus -->
## TOPIC 00019: rfmxgsmvi/rfmxgsm_commit.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_commit.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Commit (VI)

RFmxGSM Commit (VI)

Owning Palette:

Utility

Commits settings to the hardware. Calling this VI is optional. RFmxGSM commits settings to the hardware when you call the [RFmxGSM Initiate](rfmxgsm_initiate.html) VI.

[IMAGE alt='RFmxGSM Commit' src='rfmxgsm_commit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_auto_tsc_detection_enabled.html language=enus -->
## TOPIC 00020: rfmxgsmvi/rfmxgsm_configure_auto_tsc_detection_enabled.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_auto_tsc_detection_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_auto_tsc_detection_enabled.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure Auto TSC Detection Enabled (VI)

RFmxGSM Configure Auto TSC Detection Enabled (VI)

Owning Palette:

Configuration

Configures whether to auto detect the training sequence code (TSC).

[IMAGE alt='RFmxGSM Configure Auto TSC Detection Enabled' src='rfmxgsm_configure_auto_tsc_detection_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Auto TSC Detection Enabled specifies whether to auto detect the TSC. The default value is True. False (0) The measurement uses the value which you configure using the TSC property. True (1) The measurement detects the TSC in the burst. |
| False (0) | The measurement uses the value which you configure using the TSC property. |
| True (1) | The measurement detects the TSC in the burst. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_band.html language=enus -->
## TOPIC 00021: rfmxgsmvi/rfmxgsm_configure_band.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_band.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_band.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure Band (VI)

RFmxGSM Configure Band (VI)

Owning Palette:

Configuration

Configures the band of operation.

[IMAGE alt='RFmxGSM Configure Band' src='rfmxgsm_configure_band.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Band specifies the band of operation. The default value is PGSM. PGSM (0) The operation band is Primary GSM in the 900 MHz band. EGSM (1) The operation band is Extended GSM in the 900 MHz band. RGSM (2) The operation band is Railway GSM in the 900 MHz band. DCS1800 (3) The operation band is GSM in the 1800 MHz band. PCS1900 (4) The operation band is GSM in the 1900 MHz band. GSM450 (5) The operation band is GSM in the 450 MHz band. GSM480 (6) The operation band is GSM in the 480 MHz band. GSM850 (7) The operation band is GSM in the 850 MHz band. GSM750 (8) The operation band is GSM in the 750 MHz band. T-GSM810 (9) The operation band is terrestrial GSM in the 810 MHz band. |
| PGSM (0) | The operation band is Primary GSM in the 900 MHz band. |
| EGSM (1) | The operation band is Extended GSM in the 900 MHz band. |
| RGSM (2) | The operation band is Railway GSM in the 900 MHz band. |
| DCS1800 (3) | The operation band is GSM in the 1800 MHz band. |
| PCS1900 (4) | The operation band is GSM in the 1900 MHz band. |
| GSM450 (5) | The operation band is GSM in the 450 MHz band. |
| GSM480 (6) | The operation band is GSM in the 480 MHz band. |
| GSM850 (7) | The operation band is GSM in the 850 MHz band. |
| GSM750 (8) | The operation band is GSM in the 750 MHz band. |
| T-GSM810 (9) | The operation band is terrestrial GSM in the 810 MHz band. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_burst_synchronization_type.html language=enus -->
## TOPIC 00022: rfmxgsmvi/rfmxgsm_configure_burst_synchronization_type.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_burst_synchronization_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_burst_synchronization_type.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure Burst Synchronization Type (VI)

RFmxGSM Configure Burst Synchronization Type (VI)

Owning Palette:

Configuration

Configures the burst synchronization type.

[IMAGE alt='RFmxGSM Configure Burst Synchronization Type' src='rfmxgsm_configure_burst_synchronization_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Burst Sync Type specifies the method used to synchronize the burst. The default value is TSC. TSC (0) Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. Amplitude (1) Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF Envelope. None (2) Sets the T0 point to 273.23 µsec after the trigger. |
| TSC (0) | Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. |
| Amplitude (1) | Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF Envelope. |
| None (2) | Sets the T0 point to 273.23 µsec after the trigger. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_external_attenuation.html language=enus -->
## TOPIC 00023: rfmxgsmvi/rfmxgsm_configure_external_attenuation.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_external_attenuation.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure External Attenuation (VI)

RFmxGSM Configure External Attenuation (VI)

Owning Palette:

Configuration

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer.

[IMAGE alt='RFmxGSM Configure External Attenuation' src='rfmxgsm_configure_external_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | External Attenuation specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the External Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_frequency.html language=enus -->
## TOPIC 00024: rfmxgsmvi/rfmxgsm_configure_frequency.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_frequency.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure Frequency (VI)

RFmxGSM Configure Frequency (VI)

Owning Palette:

Configuration

Configures the expected center frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### RFmxGSM Configure Frequency (Frequency)

Configures the center frequency of the RF signal to acquire.

[IMAGE alt='RFmxGSM Configure Frequency (Frequency)' src='rfmxgsm_configure_frequency_(frequency).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the expected center frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM Configure Frequency (ARFCN)

Configures the center frequency from the absolute RF channel number (ARFCN), band, and the link direction.

[IMAGE alt='RFmxGSM Configure Frequency (ARFCN)' src='rfmxgsm_configure_frequency_(arfcn).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Link Direction specifies the source of the signal to be measured. The default value is Uplink. Downlink (0) The source is a base transceiver station. Uplink (1) The source is a mobile station. |
| Downlink (0) | The source is a base transceiver station. |
| Uplink (1) | The source is a mobile station. |
|  | Band specifies the band of operation. The default value is PGSM. PGSM (0) The operation band is Primary GSM in the 900 MHz band. EGSM (1) The operation band is Extended GSM in the 900 MHz band. RGSM (2) The operation band is Railway GSM in the 900 MHz band. DCS1800 (3) The operation band is GSM in the 1800 MHz band. PCS1900 (4) The operation band is GSM in the 1900 MHz band. GSM450 (5) The operation band is GSM in the 450 MHz band. GSM480 (6) The operation band is GSM in the 480 MHz band. GSM850 (7) The operation band is GSM in the 850 MHz band. GSM750 (8) The operation band is GSM in the 750 MHz band. T-GSM810 (9) The operation band is terrestrial GSM in the 810 MHz band. |
| PGSM (0) | The operation band is Primary GSM in the 900 MHz band. |
| EGSM (1) | The operation band is Extended GSM in the 900 MHz band. |
| RGSM (2) | The operation band is Railway GSM in the 900 MHz band. |
| DCS1800 (3) | The operation band is GSM in the 1800 MHz band. |
| PCS1900 (4) | The operation band is GSM in the 1900 MHz band. |
| GSM450 (5) | The operation band is GSM in the 450 MHz band. |
| GSM480 (6) | The operation band is GSM in the 480 MHz band. |
| GSM850 (7) | The operation band is GSM in the 850 MHz band. |
| GSM750 (8) | The operation band is GSM in the 750 MHz band. |
| T-GSM810 (9) | The operation band is terrestrial GSM in the 810 MHz band. |
|  | ARFCN specifies the ARFCN. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_link_direction.html language=enus -->
## TOPIC 00025: rfmxgsmvi/rfmxgsm_configure_link_direction.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_link_direction.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_link_direction.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure Link Direction (VI)

RFmxGSM Configure Link Direction (VI)

Owning Palette:

Configuration

Configures the source of the signal to be measured.

[IMAGE alt='RFmxGSM Configure Link Direction' src='rfmxgsm_configure_link_direction.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Link Direction specifies the source of the signal to be measured. The default value is Uplink. Downlink (0) The source is a base transceiver station. Uplink (1) The source is a mobile station. |
| Downlink (0) | The source is a base transceiver station. |
| Uplink (1) | The source is a mobile station. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_number_of_timeslots.html language=enus -->
## TOPIC 00026: rfmxgsmvi/rfmxgsm_configure_number_of_timeslots.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_number_of_timeslots.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_number_of_timeslots.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure Number of Timeslots (VI)

RFmxGSM Configure Number of Timeslots (VI)

Owning Palette:

Configuration

Configures the number of time slots to be measured.

[IMAGE alt='RFmxGSM Configure Number of Timeslots' src='rfmxgsm_configure_number_of_timeslots.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Timeslots specifies the number of time slots to be measured. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_power_control_level.html language=enus -->
## TOPIC 00027: rfmxgsmvi/rfmxgsm_configure_power_control_level.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_power_control_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_power_control_level.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure Power Control Level (VI)

RFmxGSM Configure Power Control Level (VI)

Owning Palette:

Configuration

Configures the power control level corresponding to the transmitted power.

Use "slot<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxGSM Configure Power Control Level' src='rfmxgsm_configure_power_control_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Power Control Level specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name and slot number. If you do not specify the signal name, the default signal instance is used. The default value is "slot::all". Example: "slot0" "slot::all" "signal::sig1/slot0" You can use the RFmxGSM Build Slot String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_reference_level.html language=enus -->
## TOPIC 00028: rfmxgsmvi/rfmxgsm_configure_reference_level.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_reference_level.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure Reference Level (VI)

RFmxGSM Configure Reference Level (VI)

Owning Palette:

Configuration

Configures the reference level, which represents the maximum expected power of an RF input signal.

[IMAGE alt='RFmxGSM Configure Reference Level' src='rfmxgsm_configure_reference_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Level specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this property is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_rf.html language=enus -->
## TOPIC 00029: rfmxgsmvi/rfmxgsm_configure_rf.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_rf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_rf.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure RF (VI)

RFmxGSM Configure RF (VI)

Owning Palette:

Configuration

Configures the RF properties of the signal specified by the selector string.

[IMAGE alt='RFmxGSM Configure RF' src='rfmxgsm_configure_rf.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the expected center frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. |
|  | Reference Level specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this property is hardware dependent. |
|  | External Attenuation specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the External Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_signal_type.html language=enus -->
## TOPIC 00030: rfmxgsmvi/rfmxgsm_configure_signal_type.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_signal_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_signal_type.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure Signal Type (VI)

RFmxGSM Configure Signal Type (VI)

Owning Palette:

Configuration

Configures the signal type.

Use "slot<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxGSM Configure Signal Type' src='rfmxgsm_configure_signal_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Modulation Type specifies the modulation type of the signal. The default value is 8PSK. GMSK (0) The modulation type is Gaussian MSK. This value is valid only when you set the Burst Type parameter to NB or AB. 8PSK (1) The modulation type is 8-PSK. This value is valid only when you set theBurst Type parameter to NB. QPSK (2) The modulation type is QPSK. This value is valid only when you set the Burst Type parameter to HB. 16QAM (3) The modulation type is 16-QAM. 32QAM (4) The modulation type is 32-QAM. |
| GMSK (0) | The modulation type is Gaussian MSK. This value is valid only when you set the Burst Type parameter to NB or AB. |
| 8PSK (1) | The modulation type is 8-PSK. This value is valid only when you set theBurst Type parameter to NB. |
| QPSK (2) | The modulation type is QPSK. This value is valid only when you set the Burst Type parameter to HB. |
| 16QAM (3) | The modulation type is 16-QAM. |
| 32QAM (4) | The modulation type is 32-QAM. |
|  | Burst Type specifies the burst type. The default value is NB. NB (0) The burst type is Normal Burst. HB (1) The burst type is Higher Symbol Rate Burst. AB (2) The burst type is Access Burst. |
| NB (0) | The burst type is Normal Burst. |
| HB (1) | The burst type is Higher Symbol Rate Burst. |
| AB (2) | The burst type is Access Burst. |
|  | HB Filter Width specifies the filter width when you set the Burst Type parameter to HB. The default value is Narrow. Narrow (0) The measurement uses a narrow filter. Wide (1) The measurement uses a wide filter. |
| Narrow (0) | The measurement uses a narrow filter. |
| Wide (1) | The measurement uses a wide filter. |
|  | Selector String specifies a selector string comprising of the signal name and slot number. If you do not specify the signal name, the default signal instance is used. The default value is "slot::all". Example: "slot0" "slot::all" "signal::sig1/slot0" You can use the RFmxGSM Build Slot String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_trigger.html language=enus -->
## TOPIC 00031: rfmxgsmvi/rfmxgsm_configure_trigger.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_trigger.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure Trigger (VI)

RFmxGSM Configure Trigger (VI)

Owning Palette:

Configuration

Configures the Reference Trigger used to acquire the signal.

#### RFmxGSM Disable Trigger

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='RFmxGSM Disable Trigger' src='rfmxgsm_disable_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM Configure Digital Edge Trigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

[IMAGE alt='RFmxGSM Configure Digital Edge Trigger' src='rfmxgsm_configure_digital_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Digital Edge Source specifies the source terminal for the digital-edge trigger. The default of this property is hardware dependent. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. |
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
|  | Digital Edge specifies the active edge for the trigger. This parameter is used only when you set the Trigger Type property to Digital Edge. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. |
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |
|  | Trigger Delay specifies the trigger delay time, in seconds. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM Configure IQ Power Edge Trigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.

To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

[IMAGE alt='RFmxGSM Configure IQ Power Edge Trigger' src='rfmxgsm_configure_iq_power_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | IQ Power Edge Source specifies the channel from which the device monitors the trigger. The default of this property is hardware dependent. |
|  | IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the level that you specify in the IQ Power Edge Level parameter with the slope you specify. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
|  | IQ Power Edge Level specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative; and is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this property is hardware dependent. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Trigger Delay specifies the trigger delay time, in seconds. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | Minimum Quiet Time Mode specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Auto. Manual (0) The minimum quiet time for triggering is the value of the Minimum Quiet Time parameter. Auto (1) The measurement computes the minimum quiet time used for triggering. |
| Manual (0) | The minimum quiet time for triggering is the value of the Minimum Quiet Time parameter. |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |
|  | Minimum Quiet Time specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet above the trigger level. The default value is 582 µs. |
|  | IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. The default value is Relative. Relative (0) The value of the IQ Power Edge Level parameter is relative to the value of the Reference Level property. Absolute (1) The IQ Power Edge Level parameter specifies the absolute power. |
| Relative (0) | The value of the IQ Power Edge Level parameter is relative to the value of the Reference Level property. |
| Absolute (1) | The IQ Power Edge Level parameter specifies the absolute power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM Configure Software Edge Trigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

[IMAGE alt='RFmxGSM Configure Software Edge Trigger' src='rfmxgsm_configure_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Trigger Delay specifies the trigger delay time, in seconds. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_configure_tsc.html language=enus -->
## TOPIC 00032: rfmxgsmvi/rfmxgsm_configure_tsc.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_configure_tsc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_configure_tsc.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Configure TSC (VI)

RFmxGSM Configure TSC (VI)

Owning Palette:

Configuration

Configures the training sequence code (TSC) in the burst.

Use "slot<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxGSM Configure TSC' src='rfmxgsm_configure_tsc.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | TSC specifies the training sequence code in the burst. For access burst TSC0, TSC1, and TSC2 are applicable. The default value is TSC0. TSC0 (0) The measurement uses training sequence code 0. TSC1 (1) The measurement uses training sequence code 1. TSC2 (2) The measurement uses training sequence code 2. TSC3 (3) The measurement uses training sequence code 3. TSC4 (4) The measurement uses training sequence code 4. TSC5 (5) The measurement uses training sequence code 5. TSC6 (6) The measurement uses training sequence code 6. TSC7 (7) The measurement uses training sequence code 7. |
| TSC0 (0) | The measurement uses training sequence code 0. |
| TSC1 (1) | The measurement uses training sequence code 1. |
| TSC2 (2) | The measurement uses training sequence code 2. |
| TSC3 (3) | The measurement uses training sequence code 3. |
| TSC4 (4) | The measurement uses training sequence code 4. |
| TSC5 (5) | The measurement uses training sequence code 5. |
| TSC6 (6) | The measurement uses training sequence code 6. |
| TSC7 (7) | The measurement uses training sequence code 7. |
|  | Selector String specifies a selector string comprising of the signal name and slot number. If you do not specify the signal name, the default signal instance is used. The default value is "slot::all". Example: "slot0" "slot::all" "signal::sig1/slot0" You can use the RFmxGSM Build Slot String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_create_signal_configuration.html language=enus -->
## TOPIC 00033: rfmxgsmvi/rfmxgsm_create_signal_configuration.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_create_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_create_signal_configuration.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Create Signal Configuration (VI)

RFmxGSM Create Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal.

[IMAGE alt='RFmxGSM Create Signal Configuration' src='rfmxgsm_create_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of configure, initiate, and fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_delete_signal_configuration.html language=enus -->
## TOPIC 00034: rfmxgsmvi/rfmxgsm_delete_signal_configuration.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_delete_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_delete_signal_configuration.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Delete Signal Configuration (VI)

RFmxGSM Delete Signal Configuration (VI)

Owning Palette:

Advanced

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='RFmxGSM Delete Signal Configuration' src='rfmxgsm_delete_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_get_all_named_result_names.html language=enus -->
## TOPIC 00035: rfmxgsmvi/rfmxgsm_get_all_named_result_names.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_get_all_named_result_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_get_all_named_result_names.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Get All Named Result Names (VI)

RFmxGSM Get All Named Result Names (VI)

Returns all the named result names of the signal that you specify in the Selector String parameter.

[IMAGE alt='RFmxGSM Get All Named Result Names' src='rfmxgsm_get_all_named_result_names.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Result Names returns an array of result names. |
|  | Default Result Exists? indicates whether the default result exists. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_initiate.html language=enus -->
## TOPIC 00036: rfmxgsmvi/rfmxgsm_initiate.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_initiate.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Initiate (VI)

RFmxGSM Initiate (VI)

Owning Palette:

RFmx GSM VIs

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the [RFmxGSM Wait for Measurement Complete](rfmxgsm_wait_for_measurement_complete.html) VI or [RFmxGSM Check Measurement Status](rfmxgsm_check_measurement_status.html) VI.

[IMAGE alt='RFmxGSM Initiate' src='rfmxgsm_initiate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to Selector String parameter on Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_modacc_configure_averaging.html language=enus -->
## TOPIC 00037: rfmxgsmvi/rfmxgsm_modacc_configure_averaging.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_modacc_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_modacc_configure_averaging.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM ModAcc Configure Averaging (VI)

RFmxGSM ModAcc Configure Averaging (VI)

Owning Palette:

ModAcc

Configures averaging for the modulation accuracy (ModAcc) measurement.

[IMAGE alt='RFmxGSM ModAcc Configure Averaging' src='rfmxgsm_modacc_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_modacc_configure_droop_compensation_enabled.html language=enus -->
## TOPIC 00038: rfmxgsmvi/rfmxgsm_modacc_configure_droop_compensation_enabled.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_modacc_configure_droop_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_modacc_configure_droop_compensation_enabled.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM ModAcc Configure Droop Compensation Enabled (VI)

RFmxGSM ModAcc Configure Droop Compensation Enabled (VI)

Owning Palette:

ModAcc

Configures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement.

[IMAGE alt='RFmxGSM ModAcc Configure Droop Compensation Enabled' src='rfmxgsm_modacc_configure_droop_compensation_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Droop Compensation Enabled specifies whether to enable droop compensation for the ModAcc measurement. Droop compensation allows the ModAcc measurement to minimize the contribution of amplifier power variations to the EVM results. The default value is False. False (0) Disables the power droop compensation in the EVM measurement. True (1) Enables the power droop compensation in the EVM measurement. |
| False (0) | Disables the power droop compensation in the EVM measurement. |
| True (1) | Enables the power droop compensation in the EVM measurement. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_modacc_fetch.html language=enus -->
## TOPIC 00039: rfmxgsmvi/rfmxgsm_modacc_fetch.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_modacc_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_modacc_fetch.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM ModAcc Fetch (VI)

RFmxGSM ModAcc Fetch (VI)

Owning Palette:

Fetch

Fetches the ModAcc measurement results.

#### RFmxGSM ModAcc Fetch EVM

Fetches the EVM measurement results for EDGE/EGPRS.

[IMAGE alt='RFmxGSM ModAcc Fetch EVM' src='rfmxgsm_modacc_fetch_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean RMS EVM returns the mean of RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage. |
|  | Maximum RMS EVM returns the maximum of RMS EVM values measured over all acquisition time slots. This value is expressed as a percentage. |
|  | Mean Peak EVM returns the mean of peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. |
|  | 95th Percentile EVM returns the EVM value, at which no more than 5 percent of the symbols have an EVM exceeding this value. This value is expressed as a percentage. |
|  | Maximum Peak EVM returns the maximum of peak EVM values measured over all acquisition time slots. This value is expressed as a percentage. |
|  | Mean Frequency Error returns the mean of frequency error values measured over all acquisition time slots. This value is expressed in Hz. |
|  | Peak EVM Symbol returns the symbol number in the useful portion of the burst corresponding to Maximum Peak EVM parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ModAcc Fetch EVM Magnitude Error

Fetches the magnitude error measurement results for EDGE/EGPRS.

[IMAGE alt='RFmxGSM ModAcc Fetch EVM Magnitude Error' src='rfmxgsm_modacc_fetch_evm_magnitude_error.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Magnitude Error returns the mean of RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. |
|  | Maximum Magnitude Error returns the maximum of RMS values of magnitude error measured over all acquisition time slots. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ModAcc Fetch EVM Phase Error

Fetches the phase error measurement results for EDGE/EGPRS.

[IMAGE alt='RFmxGSM ModAcc Fetch EVM Phase Error' src='rfmxgsm_modacc_fetch_evm_phase_error.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Phase Error returns the mean of RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. |
|  | Maximum Phase Error returns the maximum of RMS values of phase error measured over all acquisition time slots. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ModAcc Fetch EVM Amplitude Droop

Fetches the amplitude droop measurement results for EDGE/EGPRS.

[IMAGE alt='RFmxGSM ModAcc Fetch EVM Amplitude Droop' src='rfmxgsm_modacc_fetch_evm_amplitude_droop.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean Amplitude Droop returns the mean of amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. |
|  | Maximum Amplitude Droop returns the maximum of amplitude droop values measured over all acquisition time slots. This value is expressed in dB/symbol. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ModAcc Fetch PFER

Fetches the phase and frequency error measurement results for GSM.

[IMAGE alt='RFmxGSM ModAcc Fetch PFER' src='rfmxgsm_modacc_fetch_pfer.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean RMS Phase Error returns the mean of RMS phase error values measured over all acquisition time slots. This value is expressed in degrees. |
|  | Maximum RMS Phase Error returns the maximum of RMS phase error values measured over all acquisition time slots. This value is expressed in degrees. |
|  | Mean Peak Phase Error returns the mean of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. |
|  | Mean Frequency Error returns the mean of frequency error values measured over all acquisition time slots. This value is expressed in Hz. |
|  | Maximum Peak Phase Error returns the maximum of peak phase error values measured over all acquisition time slots. This value is expressed in degrees. |
|  | Peak Symbol returns the symbol number in the useful portion of the burst corresponding to phase error value in the Maximum Peak Phase Error parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ModAcc Fetch IQ Impairments

Fetches the origin offset and gain imbalance measurement results for GSM/EDGE/EGPRS.

[IMAGE alt='RFmxGSM ModAcc Fetch IQ Impairments' src='rfmxgsm_modacc_fetch_iq_impairments.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Mean IQ Gain Imbalance returns the mean of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
|  | Mean IQ Origin Offset returns the mean of I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The measurement returns this result for GSM/EDGE/EGPRS. |
|  | Maximum IQ Gain Imbalance returns the maximum of I/Q gain imbalance values measured over all acquisition time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. |
|  | Maximum IQ Origin Offset returns the maximum of I/Q origin offset values measured over all acquisition time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The measurement returns this result for GSM/EDGE/EGPRS. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ModAcc Fetch Detected TSC

Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS.

Use "slot<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxGSM ModAcc Fetch Detected TSC' src='rfmxgsm_modacc_fetch_detected_tsc.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and slot number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "slot0" "signal::sig1/slot0" "result::r1/slot0" "signal::sig1/result::r1/slot0" You can use the RFmxGSM Build Slot String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Detected TSC returns the detected TSC when you set the Burst Sync Type property to TSC. Unknown (-1) Burst synchronization is not found and measurements correspond to best estimate of synchronization. TSC0 (0) The detected TSC is TSC0. TSC1 (1) The detected TSC is TSC1. TSC2 (2) The detected TSC is TSC2. TSC3 (3) The detected TSC is TSC3. TSC4 (4) The detected TSC is TSC4. TSC5 (5) The detected TSC is TSC5. TSC6 (6) The detected TSC is TSC6. TSC7 (7) The detected TSC is TSC7. |
| Unknown (-1) | Burst synchronization is not found and measurements correspond to best estimate of synchronization. |
| TSC0 (0) | The detected TSC is TSC0. |
| TSC1 (1) | The detected TSC is TSC1. |
| TSC2 (2) | The detected TSC is TSC2. |
| TSC3 (3) | The detected TSC is TSC3. |
| TSC4 (4) | The detected TSC is TSC4. |
| TSC5 (5) | The detected TSC is TSC5. |
| TSC6 (6) | The detected TSC is TSC6. |
| TSC7 (7) | The detected TSC is TSC7. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ModAcc Fetch Detected TSC (Array)

Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS.

[IMAGE alt='RFmxGSM ModAcc Fetch Detected TSC (Array)' src='rfmxgsm_modacc_fetch_detected_tsc_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Detected TSC returns an array of the detected TSCs when you set the Burst Sync Type property to TSC. Unknown (-1) The synchronization is not found and measurements correspond to best estimate of synchronization. TSC0 (0) The detected TSC is TSC0. TSC1 (1) The detected TSC is TSC1. TSC2 (2) The detected TSC is TSC2. TSC3 (3) The detected TSC is TSC3. TSC4 (4) The detected TSC is TSC4. TSC5 (5) The detected TSC is TSC5. TSC6 (6) The detected TSC is TSC6. TSC7 (7) The detected TSC is TSC7. |
| Unknown (-1) | The synchronization is not found and measurements correspond to best estimate of synchronization. |
| TSC0 (0) | The detected TSC is TSC0. |
| TSC1 (1) | The detected TSC is TSC1. |
| TSC2 (2) | The detected TSC is TSC2. |
| TSC3 (3) | The detected TSC is TSC3. |
| TSC4 (4) | The detected TSC is TSC4. |
| TSC5 (5) | The detected TSC is TSC5. |
| TSC6 (6) | The detected TSC is TSC6. |
| TSC7 (7) | The detected TSC is TSC7. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ModAcc Fetch Constellation Trace

Fetches the constellation trace concatenated over all slots for the last acquisition.

[IMAGE alt='RFmxGSM ModAcc Fetch Constellation Trace' src='rfmxgsm_modacc_fetch_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Constellation Trace returns the constellation trace concatenated over all slots for the last acquisition. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ModAcc Fetch Phase Error Trace

Fetches the phase error trace concatenated over all slots for the last acquisition.

[IMAGE alt='RFmxGSM ModAcc Fetch Phase Error Trace' src='rfmxgsm_modacc_fetch_phase_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Phase Error returns the phase error trace. x0 returns the start time, in seconds. dx returns the sample duration, in symbols. y returns an array of phase error values measured at each time instance. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in symbols. |
|  | y returns an array of phase error values measured at each time instance. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ModAcc Fetch Demodulated Bits

Fetches the array of demodulated bits concatenated over all slots for the last acquisition.

[IMAGE alt='RFmxGSM ModAcc Fetch Demodulated Bits' src='rfmxgsm_modacc_fetch_demodulated_bits.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Bits returns an array of demodulated bits concatenated over all slots for the last acquisition. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ModAcc Fetch Magnitude Error Trace

Fetches the EDGE/EGPRS magnitude error trace concatenated over all slots for the last acquisition.

[IMAGE alt='RFmxGSM ModAcc Fetch Magnitude Error Trace' src='rfmxgsm_modacc_fetch_magnitude_error_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Magnitude Error returns the magnitude error trace. This value is expressed as a percentage. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns an array of magnitude error values measured at each time instance. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns an array of magnitude error values measured at each time instance. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ModAcc Fetch EVM Trace

Fetches the EDGE/EGPRS RMS EVM trace concatenated over all slots for the last acquisition.

[IMAGE alt='RFmxGSM ModAcc Fetch EVM Trace' src='rfmxgsm_modacc_fetch_evm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | EVM returns the EVM trace. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns the EVM trace measured at each time instance. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns the EVM trace measured at each time instance. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_orfs_configure_averaging.html language=enus -->
## TOPIC 00040: rfmxgsmvi/rfmxgsm_orfs_configure_averaging.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_orfs_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_orfs_configure_averaging.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM ORFS Configure Averaging (VI)

RFmxGSM ORFS Configure Averaging (VI)

Owning Palette:

ORFS

Configures averaging for the output radio frequency spectrum (ORFS) measurement.

[IMAGE alt='RFmxGSM ORFS Configure Averaging' src='rfmxgsm_orfs_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is Log. RMS (0) The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The measurement averages the power spectrum in a logarithmic scale. |
| RMS (0) | The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The measurement averages the power spectrum in a logarithmic scale. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_orfs_configure_evaluation_symbols.html language=enus -->
## TOPIC 00041: rfmxgsmvi/rfmxgsm_orfs_configure_evaluation_symbols.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_orfs_configure_evaluation_symbols.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_orfs_configure_evaluation_symbols.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM ORFS Configure Evaluation Symbols (VI)

RFmxGSM ORFS Configure Evaluation Symbols (VI)

Owning Palette:

ORFS

Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify the portion of the burst to measure for ORFS due to modulation. RFmx considers the measurement over evaluation symbols for a single burst as one average.

[IMAGE alt='RFmxGSM ORFS Configure Evaluation Symbols' src='rfmxgsm_orfs_configure_evaluation_symbols.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Evaluation Symbols Start specifies the start position of the burst over which you perform the ORFS measurement. This value is expressed as a percentage. The default value is 50. |
|  | Evaluation Symbols Include TSC specifies whether to include the TSC portion of burst in the ORFS measurement. The default value is False. False (0) The TSC portion of the burst is excluded in the ORFS measurement. True (1) The TSC portion of the burst is included in the ORFS measurement. |
| False (0) | The TSC portion of the burst is excluded in the ORFS measurement. |
| True (1) | The TSC portion of the burst is included in the ORFS measurement. |
|  | Evaluation Symbols Stop specifies the stop position of the burst over which you perform the ORFS measurement. This value is expressed as a percentage. The default value is 90. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_orfs_configure_measurement_type.html language=enus -->
## TOPIC 00042: rfmxgsmvi/rfmxgsm_orfs_configure_measurement_type.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_orfs_configure_measurement_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_orfs_configure_measurement_type.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM ORFS Configure Measurement Type (VI)

RFmxGSM ORFS Configure Measurement Type (VI)

Owning Palette:

ORFS

Configures the type of spectral distortion to be measured.

[IMAGE alt='RFmxGSM ORFS Configure Measurement Type' src='rfmxgsm_orfs_configure_measurement_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Type specifies the type of spectral distortion to be measured. The default value is Modulation and Switching. Modulation and Switching (0) Measures the spectrum on the modulated part and switching part of the waveform. Modulation (1) Measures the spectrum on the modulated part of the waveform. Switching (2) Measures the spectrum on the switching part of the waveform. |
| Modulation and Switching (0) | Measures the spectrum on the modulated part and switching part of the waveform. |
| Modulation (1) | Measures the spectrum on the modulated part of the waveform. |
| Switching (2) | Measures the spectrum on the switching part of the waveform. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_orfs_configure_modulation_custom_offset_frequency_(array).html language=enus -->
## TOPIC 00043: rfmxgsmvi/rfmxgsm_orfs_configure_modulation_custom_offset_frequency_(array).html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_orfs_configure_modulation_custom_offset_frequency_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_orfs_configure_modulation_custom_offset_frequency_(array).html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM ORFS Configure Modulation Custom Offset Frequency (Array) (VI)

RFmxGSM ORFS Configure Modulation Custom Offset Frequency (Array) (VI)

Owning Palette:

ORFS

Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the ORFS Offset Freq Mode property to **Custom**.

[IMAGE alt='RFmxGSM ORFS Configure Modulation Custom Offset Frequency (Array)' src='rfmxgsm_orfs_configure_modulation_custom_offset_frequency_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Modulation Custom Offset Frequency specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of modulation when you set the ORFS Offset Freq Mode property to Custom. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_orfs_configure_noise_compensation_enabled.html language=enus -->
## TOPIC 00044: rfmxgsmvi/rfmxgsm_orfs_configure_noise_compensation_enabled.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_orfs_configure_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_orfs_configure_noise_compensation_enabled.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM ORFS Configure Noise Compensation Enabled (VI)

RFmxGSM ORFS Configure Noise Compensation Enabled (VI)

Owning Palette:

ORFS

Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

[IMAGE alt='RFmxGSM ORFS Configure Noise Compensation Enabled' src='rfmxgsm_orfs_configure_noise_compensation_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Noise Compensation Enabled specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. The default value is False. False (0) Disables compensation of the channel powers for the signal analyzer noise floor. True (1) Enables compensation of the channel powers for the signal analyzer noise floor. The measurement calculates the signal analyzer noise floor for the RF path used by the output radio frequency spectrum (ORFS) measurement and caches the noise floor for future use. If signal analyzer parameters or measurement parameters change, the measurement calculates noise floors again. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832 |
| False (0) | Disables compensation of the channel powers for the signal analyzer noise floor. |
| True (1) | Enables compensation of the channel powers for the signal analyzer noise floor. The measurement calculates the signal analyzer noise floor for the RF path used by the output radio frequency spectrum (ORFS) measurement and caches the noise floor for future use. If signal analyzer parameters or measurement parameters change, the measurement calculates noise floors again. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832 |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_orfs_configure_offset_frequency_mode.html language=enus -->
## TOPIC 00045: rfmxgsmvi/rfmxgsm_orfs_configure_offset_frequency_mode.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_orfs_configure_offset_frequency_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_orfs_configure_offset_frequency_mode.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM ORFS Configure Offset Frequency Mode (VI)

RFmxGSM ORFS Configure Offset Frequency Mode (VI)

Owning Palette:

ORFS

Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

[IMAGE alt='RFmxGSM ORFS Configure Offset Frequency Mode' src='rfmxgsm_orfs_configure_offset_frequency_mode.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset Frequency Mode specifies the list of frequency offsets for which you can perform the ORFS measurements. The default value is Standard. Standard (0) Uses a list of lower and upper offset frequencies of 100 kHz, 200 kHz, 250 kHz, 400 kHz, 600 kHz, 800 kHz, 1000 kHz, 1200 kHz, 1400 kHz, 1600 kHz, and 1800 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. Short (1) Uses the list of lower and upper offset frequencies of 200 kHz, 250 kHz, 400 kHz, 600 kHz, and 1200 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. Custom (2) Uses the list of frequencies that is configured using the RFmxGSM ORFS Configure Modulation Custom Offset Frequency (Array) and RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array) VIs for measurement of spectrum produced by modulation and switching measurements. |
| Standard (0) | Uses a list of lower and upper offset frequencies of 100 kHz, 200 kHz, 250 kHz, 400 kHz, 600 kHz, 800 kHz, 1000 kHz, 1200 kHz, 1400 kHz, 1600 kHz, and 1800 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |
| Short (1) | Uses the list of lower and upper offset frequencies of 200 kHz, 250 kHz, 400 kHz, 600 kHz, and 1200 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |
| Custom (2) | Uses the list of frequencies that is configured using the RFmxGSM ORFS Configure Modulation Custom Offset Frequency (Array) and RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array) VIs for measurement of spectrum produced by modulation and switching measurements. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_orfs_configure_switching_custom_offset_frequency_(array).html language=enus -->
## TOPIC 00046: rfmxgsmvi/rfmxgsm_orfs_configure_switching_custom_offset_frequency_(array).html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_orfs_configure_switching_custom_offset_frequency_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_orfs_configure_switching_custom_offset_frequency_(array).html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array) (VI)

RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array) (VI)

Owning Palette:

ORFS

Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the ORFS Offset Freq Mode property to **Custom**.

[IMAGE alt='RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array)' src='rfmxgsm_orfs_configure_switching_custom_offset_frequency_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Switching Custom Offset Frequency specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of switching when you set the ORFS Offset Freq Mode property to Custom. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_orfs_fetch.html language=enus -->
## TOPIC 00047: rfmxgsmvi/rfmxgsm_orfs_fetch.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_orfs_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_orfs_fetch.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM ORFS Fetch (VI)

RFmxGSM ORFS Fetch (VI)

Owning Palette:

Fetch

Fetches the output radio frequency spectrum (ORFS) measurement results.

#### RFmxGSM ORFS Fetch Modulation Results (Array)

Returns the modulation carrier power, absolute powers, and relative powers measured at the modulation offset frequencies. The relative powers are measured relative to the integrated modulation power of the carrier.

[IMAGE alt='RFmxGSM ORFS Fetch Modulation Results (Array)' src='rfmxgsm_orfs_fetch_modulation_results_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Modulation Carrier Power returns the modulation carrier power. This value is expressed in dBm. |
|  | Lower Relative Power returns an array of relative powers measured at the negative modulation offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated modulation power of the carrier. |
|  | Upper Relative Power returns an array of relative powers measured at the positive modulation offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated modulation power of the carrier. |
|  | Lower Absolute Power returns an array of absolute powers measured at the negative modulation offset frequencies. This value is expressed in dBm. |
|  | Upper Absolute Power returns an array of absolute powers measured at the positive modulation offset frequencies. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ORFS Fetch Switching Results (Array)

Fetches the switching carrier power, absolute powers, and relative powers measured at the switching offset frequencies. The relative powers are measured relative to the integrated switching power of the carrier.

[IMAGE alt='RFmxGSM ORFS Fetch Switching Results (Array)' src='rfmxgsm_orfs_fetch_switching_results_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Switching Carrier Power returns the switching carrier power. This value is expressed in dBm. |
|  | Lower Relative Power returns an array of relative powers measured at the negative switching offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated switching power of the carrier. |
|  | Upper Relative Power returns an array of relative powers measured at the positive switching offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated switching power of the carrier. |
|  | Lower Absolute Power returns an array of absolute powers measured at the negative switching offset frequencies. This value is expressed in dBm. |
|  | Upper Absolute Power returns an array of absolute powers measured at the positive switching offset frequencies. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ORFS Fetch Modulation Power Trace

Fetches the modulation power trace and frequency offset.

[IMAGE alt='RFmxGSM ORFS Fetch Modulation Power Trace' src='rfmxgsm_orfs_fetch_modulation_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Offset Frequency returns an array of modulation offset frequencies at which the measurement is performed in an ascending order. This value is expressed in Hz. |
|  | Absolute Power returns an array of absolute powers corresponding to the modulation offset frequency list. This value is expressed in dBm. |
|  | Relative Power returns an array of relative powers corresponding to modulation offset frequency list. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM ORFS Fetch Switching Power Trace

Fetches the switching power trace and frequency offsets.

[IMAGE alt='RFmxGSM ORFS Fetch Switching Power Trace' src='rfmxgsm_orfs_fetch_switching_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Offset Frequency returns an array of switching offset frequencies at which the measurement is performed in an ascending order. This value is expressed in Hz. |
|  | Absolute Power returns an array of absolute powers corresponding to the switching offset frequency list. This value is expressed in dBm. |
|  | Relative Power returns an array of relative powers corresponding to the switching offset frequencies. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_property_node.html language=enus -->
## TOPIC 00048: rfmxgsmvi/rfmxgsm_property_node.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_property_node.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_property_node.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Property Node (VI)

RFmxGSM Property Node (VI)

Owning Palette:

RFmx GSM VIs

Gets (reads), sets (writes), or resets (sets to default value) RFmxGSM properties.

[IMAGE alt='RFmxGSM Property Node' src='rfmxgsm_property_node.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_pvt_configure_averaging.html language=enus -->
## TOPIC 00049: rfmxgsmvi/rfmxgsm_pvt_configure_averaging.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_pvt_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_pvt_configure_averaging.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM PVT Configure Averaging (VI)

RFmxGSM PVT Configure Averaging (VI)

Owning Palette:

PVT

Configures averaging for the power versus time (PVT) measurement.

[IMAGE alt='RFmxGSM PVT Configure Averaging' src='rfmxgsm_pvt_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power at each sample interval is linearly averaged from an acquisition to the next acquisition. Log (1) The power at each sample interval is averaged on logarithmic scale from an acquisition to the next acquisition. Max (3) The peak power at each sample interval is retained from an acquisition to the next acquisition. Min (4) The lowest power at each sample interval is retained from an acquisition to the next acquisition. |
| RMS (0) | The power at each sample interval is linearly averaged from an acquisition to the next acquisition. |
| Log (1) | The power at each sample interval is averaged on logarithmic scale from an acquisition to the next acquisition. |
| Max (3) | The peak power at each sample interval is retained from an acquisition to the next acquisition. |
| Min (4) | The lowest power at each sample interval is retained from an acquisition to the next acquisition. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_pvt_fetch.html language=enus -->
## TOPIC 00050: rfmxgsmvi/rfmxgsm_pvt_fetch.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_pvt_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_pvt_fetch.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM PVT Fetch (VI)

RFmxGSM PVT Fetch (VI)

Owning Palette:

Fetch

Fetches the power versus time (PVT) measurement results.

#### RFmxGSM PVT Fetch Measurement Status

Fetches the overall PVT measurement status based on the standard defined measurement limits.

[IMAGE alt='RFmxGSM PVT Fetch Measurement Status' src='rfmxgsm_pvt_fetch_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1/result::r1" "signal::sig1" "result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status indicates the overall measurement status based on standard-defined limits. Fail (0) The measurement failed because the average power of at least one slot is outside the standard-defined limits. Pass (1) The measurement passed because the average power of all slots is within the standard-defined limits. |
| Fail (0) | The measurement failed because the average power of at least one slot is outside the standard-defined limits. |
| Pass (1) | The measurement passed because the average power of all slots is within the standard-defined limits. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM PVT Fetch Slot Measurement

Fetches the measurement results for a single-slot PVT measurement.

Use "slot<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxGSM PVT Fetch Slot Measurement' src='rfmxgsm_pvt_fetch_slot_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and slot number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "slot0" "signal::sig1/slot0" "result::r1/slot0" "signal::sig1/result::r1/slot0" You can use the RFmxGSM Build Slot String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Slot Average Power returns the mean power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
|  | Slot Burst Width returns the burst width of the slot where the -3 dB transition points occur. This value is expressed in seconds. |
|  | Slot Measurement Status indicates the PVT measurement status for a particular slot. Fail (0) The signal power is outside the standard-defined upper or lower mask Pass (1) The signal power is within the standard-defined upper and lower mask. |
| Fail (0) | The signal power is outside the standard-defined upper or lower mask |
| Pass (1) | The signal power is within the standard-defined upper and lower mask. |
|  | Slot Minimum Power returns the minimum power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
|  | Slot Maximum Power returns the maximum power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
|  | Slot Burst Threshold returns the threshold that the PVT measurement uses to determine the burst validity. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM PVT Fetch Slot Measurement (Array)

Fetches the PVT measurement results for each slot.

[IMAGE alt='RFmxGSM PVT Fetch Slot Measurement (Array)' src='rfmxgsm_pvt_fetch_slot_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Slot Average Power returns an array of mean powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
|  | Slot Burst Width returns an array of burst widths for the slots where the -3 dB transition points occur. This value is expressed in seconds. |
|  | Slot Measurement Status indicates an array of PVT measurement statuses for multiple slots. Fail (0) The signal power is outside the standard-defined upper or lower mask Pass (1) The signal power is within the standard-defined upper and lower mask. |
| Fail (0) | The signal power is outside the standard-defined upper or lower mask |
| Pass (1) | The signal power is within the standard-defined upper and lower mask. |
|  | Slot Minimum Power returns an array of minimum powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
|  | Slot Maximum Power returns an array of maximum powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. |
|  | Slot Burst Threshold returns an array of thresholds that the PVT measurement uses to determine the burst validity. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM PVT Fetch Power Trace

Fetches the upper mask, signal power, and lower mask trace.

[IMAGE alt='RFmxGSM PVT Fetch Power Trace' src='rfmxgsm_pvt_fetch_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1/result::r1" "signal::sig1" "result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Upper Mask returns the upper mask trace, in dB. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns an array of upper mask values measured at each time instance. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns an array of upper mask values measured at each time instance. |
|  | Signal Power returns the signal power trace. This value is expressed in dBm. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns an array of signal power values measured at each time instance. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns an array of signal power values measured at each time instance. |
|  | Lower Mask returns the lower mask trace. This value is expressed in dB. x0 returns the start time, in seconds. dx returns the sample duration, in seconds. y returns an array of lower mask values measured at each time instance. |
|  | x0 returns the start time, in seconds. |
|  | dx returns the sample duration, in seconds. |
|  | y returns an array of lower mask values measured at each time instance. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_reset_to_default.html language=enus -->
## TOPIC 00051: rfmxgsmvi/rfmxgsm_reset_to_default.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_reset_to_default.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_reset_to_default.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Reset to Default (VI)

RFmxGSM Reset to Default (VI)

Owning Palette:

Utility

Resets a signal to the default values.

[IMAGE alt='RFmxGSM Reset to Default' src='rfmxgsm_reset_to_default.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_select_measurement.html language=enus -->
## TOPIC 00052: rfmxgsmvi/rfmxgsm_select_measurement.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_select_measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_select_measurement.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Select Measurement (VI)

RFmxGSM Select Measurement (VI)

Owning Palette:

RFmx GSM VIs

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

#### RFmxGSM Select Measurement (Multiple)

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='RFmxGSM Select Measurement (Multiple)' src='rfmxgsm_select_measurement_(multiple).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurements specifies the measurement to perform. You can specify one or more of the following measurements. The default is an empty array. ModAcc (0) Enables the modulation accuracy (ModAcc) measurement. ORFS (1) Enables the output radio frequency spectrum (ORFS) measurement. PVT (2) Enables the power versus time (PVT) measurement. |
| ModAcc (0) | Enables the modulation accuracy (ModAcc) measurement. |
| ORFS (1) | Enables the output radio frequency spectrum (ORFS) measurement. |
| PVT (2) | Enables the power versus time (PVT) measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxGSM Select Measurement (Single)

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='RFmxGSM Select Measurement (Single)' src='rfmxgsm_select_measurement_(single).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement specifies the measurement to perform. You can specify one of the following measurements. The default value is ModAcc. ModAcc (0) Enables the modulation accuracy (ModAcc) measurement. ORFS (1) Enables the output radio frequency spectrum (ORFS) measurement. PVT (2) Enables the power versus time (PVT) measurement. |
| ModAcc (0) | Enables the modulation accuracy (ModAcc) measurement. |
| ORFS (1) | Enables the output radio frequency spectrum (ORFS) measurement. |
| PVT (2) | Enables the power versus time (PVT) measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_send_software_edge_trigger.html language=enus -->
## TOPIC 00053: rfmxgsmvi/rfmxgsm_send_software_edge_trigger.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_send_software_edge_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_send_software_edge_trigger.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Send Software Edge Trigger (VI)

RFmxGSM Send Software Edge Trigger (VI)

Owning Palette:

Configuration

Sends a trigger to the device when you use the [RFmxGSM Configure Trigger](rfmxgsm_configure_trigger.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxGSM Initiate VI.

[IMAGE alt='RFmxGSM Send Software Edge Trigger' src='rfmxgsm_send_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/rfmxgsm_wait_for_measurement_complete.html language=enus -->
## TOPIC 00054: rfmxgsmvi/rfmxgsm_wait_for_measurement_complete.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/rfmxgsm_wait_for_measurement_complete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/rfmxgsm_wait_for_measurement_complete.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

RFmxGSM Wait for Measurement Complete (VI)

RFmxGSM Wait for Measurement Complete (VI)

Owning Palette:

Utility

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='RFmxGSM Wait for Measurement Complete' src='rfmxgsm_wait_for_measurement_complete.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-gsm-vi path=rfmxgsmvi/utility_pal.html language=enus -->
## TOPIC 00055: rfmxgsmvi/utility_pal.html

- bundle_id: `rfmx-gsm-vi`
- source_path: `rfmxgsmvi/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-gsm-vi/raw/resource/enus/rfmxgsmvi/utility_pal.html
- document_id: `rfmx-gsm-vi`
- page_type: `leaf`
- content_type: ``

Utility

Utility

Owning Palette:

RFmx GSM VIs

Use the VIs on this palette to configure utility measurements. You can use the RFmxGSM Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxGSM Commit | Commits settings to the hardware. Calling this VI is optional. RFmxGSM commits settings to the hardware when you call the RFmxGSM Initiate VI. |
| RFmxGSM Reset to Default | Resets a signal to the default values. |
| RFmxGSM Wait for Measurement Complete | Waits for the specified number for seconds for all the measurements to complete. |
| RFmxGSM Check Measurement Status | Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
