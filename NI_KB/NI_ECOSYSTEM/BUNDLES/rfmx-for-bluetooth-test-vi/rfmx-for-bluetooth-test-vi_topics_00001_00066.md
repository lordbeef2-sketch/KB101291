# NI DOCUMENT BUNDLE: rfmx-for-bluetooth-test-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-for-bluetooth-test-vi start=1 end=66 -->
<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/20dbbandwidth_pal.html language=enus -->
## TOPIC 00001: 20dBBandwidth

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/20dbbandwidth_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/20dbbandwidth_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

20dBBandwidth

Owning Palette:

Configuration

Use the VIs on this palette to configure the 20dBBandwidth measurements. You can also use the RFmxBT Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxBT 20dBBandwidth Configure Averaging | Configures averaging for the 20dBBandwidth measurement. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/acp_pal.html language=enus -->
## TOPIC 00002: ACP

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/acp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/acp_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

ACP

Owning Palette:

Configuration

Use the VIs on this palette to configure ACP measurements. You can use the RFmxBT Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxBT ACP Configure Averaging | Configures averaging for the adjacent channel power (ACP) measurement. |
| RFmxBT ACP Configure Burst Synchronization Type | Configures the type of synchronization used for detecting the start of the packet in the adjacent channel power (ACP) measurement. |
| RFmxBT ACP Configure Offset Channel Mode | Configures the offset channels used for the adjacent channel power (ACP) measurement. |
| RFmxBT ACP Configure Number of Offsets | Configures the number of offsets for the adjacent channel power (ACP) measurement. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/advanced_pal.html language=enus -->
## TOPIC 00003: Advanced

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/advanced_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/advanced_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

Advanced

Owning Palette:

RFmx for Bluetooth® Test VIs

Use the VIs on this palette to use advanced features.

| Palette Object | Description |
| --- | --- |
| RFmxBT Abort Measurements | Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxBT Initiate or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error. |
| RFmxBT Analyze (IQ, 1 Wfm) | Performs the enabled measurements on the I/Q complex waveform that you specify in the IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended Acquisition Type property value is either IQ or IQ or Spectral. |
| RFmxBT Create Signal Configuration | Creates a new instance of a signal. |
| RFmxBT Clone Signal Configuration | Creates a new instance of a signal by copying all the property values from an existing signal instance. |
| RFmxBT Delete Signal Configuration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxBT Get All Named Result Names | Returns all the named result names of the signal that you specify in the Selector String parameter. |
| RFmxBT Clear Named Result | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxBT Clear All Named Results | Clears all results for the signal that you specify in the Selector String parameter. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/bt_pal.html language=enus -->
## TOPIC 00004: RFmx for Bluetooth® Test VIs

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/bt_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/bt_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmx for Bluetooth® Test VIs

Use the VIs on this palette to perform Bluetooth measurements. You can use the [RFmxBT Property Node](../rfmxbtvi/rfmxbt_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxBT Select Measurement | Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. |
| RFmxBT Initiate | Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the RFmxBT Wait for Measurement Complete VI or RFmxBT Check Measurement Status VI. |
| RFmxBT Property Node | Gets (reads), sets (writes), or resets (sets to default value) RFmxBluetooth properties. |

| Subpalette | Description |
| --- | --- |
| Configuration | Use the VIs on this palette to configure various parameters for RFmxBT measurements. |
| Fetch | Use the VIs on this palette to fetch Bluetooth measurement results and traces. |
| Utility | Use the VIs on this palette to configure utility VIs. |
| Build String | Use the VIs on this palette to create strings for configurations and results that require a selector string. |
| Advanced | Use the VIs on this palette to use advanced features. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/build_string_pal.html language=enus -->
## TOPIC 00005: Build String

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/build_string_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/build_string_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

Build String

Owning Palette:

RFmx for Bluetooth® Test VIs

Use the VIs on this palette to create strings for configurations and results that require a selector string.

| Palette Object | Description |
| --- | --- |
| RFmxBT Build Signal String | Creates a selector string. |
| RFmxBT Build Offset String | Creates the offset string. |
| RFmxBT Build Slot String | Creates the slot string for use with the TXP configuration or fetch properties and VIs. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/configuration_pal.html language=enus -->
## TOPIC 00006: Configuration

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/configuration_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

Configuration

Owning Palette:

RFmx for Bluetooth® Test VIs

Use the VIs on this palette to configure various parameters for RFmxBT measurements.

| Palette Object | Description |
| --- | --- |
| RFmxBT Configure RF | Configures the RF properties of the signal specified by the selector string. |
| RFmxBT Configure Frequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| RFmxBT Configure Reference Level | Configures the reference level which represents the maximum expected power of an RF input signal. |
| RFmxBT Configure External Attenuation | Configures the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. |
| RFmxBT Auto Level | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level. |
| RFmxBT Configure Trigger | Configures the reference trigger to use to acquire the signal. |
| RFmxBT Send Software Edge Trigger | Sends a trigger to the device when you use the RFmxBT Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. |
| RFmxBT Configure Packet Type | Configures the type of Bluetooth packet to be measured. |
| RFmxBT Configure Data Rate | Configures the data rate of low energy (LE) or low energy - channel sounding (LE-CS) packets to be measured. |
| RFmxBT Configure Payload Bit Pattern | Configures the bit pattern present in the payload of the packet. |
| RFmxBT Configure Payload Length | Configures the Payload Length Mode and Payload Length parameters that decide the length of the payload to be used for the measurement. |
| RFmxBT Configure LE Direction Finding | Configures the mode of direction finding, length of the constant tone extension field, and the duration of the switching slot in the generated signal. |

| Subpalette | Description |
| --- | --- |
| ModAcc | Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements. You can also use the RFmxBT Property Node to configure additional properties. |
| ACP | Use the VIs on this palette to configure ACP measurements. You can use the RFmxBT Property Node to configure additional properties. |
| 20dBBandwidth | Use the VIs on this palette to configure the 20dBBandwidth measurements. You can also use the RFmxBT Property Node to configure additional properties. |
| Frequency Range | Use the VIs on this palette to configure the Frequency Range measurements. You can also use the RFmxBT Property Node to configure additional properties. |
| TXP | Use the VIs on this palette to configure transmit power (TXP) measurements. You can also use the RFmxBT Property Node to configure additional properties. |
| PowerRamp | Use the VIs on this palette to configure PowerRamp measurements. You can use the RFmxBT Property Node to configure additional properties. |
| ModSpectrum | Use the VIs on this palette to configure ModSpectrum measurements. You can use the RFmxBT Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/fetch_pal.html language=enus -->
## TOPIC 00007: Fetch

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/fetch_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/fetch_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

Fetch

Owning Palette:

RFmx for Bluetooth® Test VIs

Use the VIs on this palette to fetch Bluetooth measurement results and traces.

| Palette Object | Description |
| --- | --- |
| RFmxBT ModAcc Fetch | Fetches the ModAcc measurement results. |
| RFmxBT ACP Fetch | Fetches the ACP measurement results. |
| RFmxBT 20dBBandwidth Fetch | Fetches the 20dBBandwidth measurement results. |
| RFmxBT FrequencyRange Fetch | Fetches the FrequencyRange measurement results. |
| RFmxBT TXP Fetch | Fetches the TXP measurement results. |
| RFmxBT ModSpectrum Fetch Spectrum | Fetches the ModSpectrum spectrum trace. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/frequency_range_pal.html language=enus -->
## TOPIC 00008: Frequency Range

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/frequency_range_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/frequency_range_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

Frequency Range

Owning Palette:

Configuration

Use the VIs on this palette to configure the Frequency Range measurements. You can also use the RFmxBT Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxBT FrequencyRange Configure Averaging | Configures averaging for the FrequencyRange measurement. |
| RFmxBT FrequencyRange Configure Span | Configures the span for the FrequencyRange measurement. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/modacc_pal.html language=enus -->
## TOPIC 00009: ModAcc

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/modacc_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/modacc_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

ModAcc

Owning Palette:

Configuration

Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements. You can also use the RFmxBT Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxBT ModAcc Configure Averaging | Configures averaging for the ModAcc measurement. |
| RFmxBT ModAcc Configure Burst Synchronization Type | Configures the burst synchronization type for ModAcc measurement. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/modspectrum_pal.html language=enus -->
## TOPIC 00010: ModSpectrum

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/modspectrum_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/modspectrum_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

ModSpectrum

Owning Palette:

Configuration

Use the VIs on this palette to configure ModSpectrum measurements. You can use the RFmxBT Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxBT ModSpectrum Configure Averaging | Configures averaging for the ModSpectrum measurement. |
| RFmxBT ModSpectrum Configure Burst Synchronization Type | Configures the burst synchronization type for ModSpectrum measurement. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/powerramp_pal.html language=enus -->
## TOPIC 00011: PowerRamp

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/powerramp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/powerramp_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

PowerRamp

Owning Palette:

Configuration

Use the VIs on this palette to configure PowerRamp measurements. You can use the RFmxBT Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxBT PowerRamp Configure Averaging | Configures averaging for the PowerRamp measurement. |
| RFmxBT PowerRamp Configure Burst Synchronization Type | Configures the burst synchronization type for PowerRamp measurement. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_20dbbandwidth_configure_averaging.html language=enus -->
## TOPIC 00012: RFmxBT 20dBBandwidth Configure Averaging (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_20dbbandwidth_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_20dbbandwidth_configure_averaging.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT 20dBBandwidth Configure Averaging (VI)

Owning Palette:

20dBBandwidth

Configures averaging for the 20dBBandwidth measurement.

[IMAGE alt='RFmxBT 20dBBandwidth Configure Averaging' src='rfmxbt_20dbbandwidth_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for 20dBBandwidth measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the 20dBBandwidth measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the 20dBBandwidth measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_20dbbandwidth_fetch.html language=enus -->
## TOPIC 00013: RFmxBT 20dBBandwidth Fetch (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_20dbbandwidth_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_20dbbandwidth_fetch.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT 20dBBandwidth Fetch (VI)

Owning Palette:

Fetch

Fetches the 20dBBandwidth measurement results.

#### RFmxBT 20dBBandwidth Fetch Measurement

Fetches the 20dBBandwidth measurement results.

[IMAGE alt='RFmxBT 20dBBandwidth Fetch Measurement' src='rfmxbt_20dbbandwidth_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Peak Power returns the peak power of the measured spectrum. This value is expressed in dBm. |
|  | Bandwidth returns the 20dB bandwidth of the received signal. It is computed as the difference between High Frequency and Low Frequency parameters. This value is expressed in Hz. |
|  | High Frequency returns the highest frequency above the center frequency at which transmit power drops 20 dB below the peak power. This value is expressed in Hz. |
|  | Low Frequency returns the lowest frequency below the center frequency at which transmit power drops 20 dB below the peak power. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT 20dBBandwidth Fetch Spectrum

Fetches the 20dBBandwidth spectrum trace.

[IMAGE alt='RFmxBT 20dBBandwidth Fetch Spectrum' src='rfmxbt_20dbbandwidth_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the 20dBBandwidth spectrum trace. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_abort_measurements.html language=enus -->
## TOPIC 00014: RFmxBT Abort Measurements (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_abort_measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_abort_measurements.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Abort Measurements (VI)

Owning Palette:

Advanced

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxBT Initiate](../rfmxbtvi/rfmxbt_initiate.html) or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='RFmxBT Abort Measurements' src='rfmxbt_abort_measurements.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_acp_configure_averaging.html language=enus -->
## TOPIC 00015: RFmxBT ACP Configure Averaging (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_acp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_acp_configure_averaging.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT ACP Configure Averaging (VI)

Owning Palette:

ACP

Configures averaging for the adjacent channel power (ACP) measurement.

[IMAGE alt='RFmxBT ACP Configure Averaging' src='rfmxbt_acp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the ACP measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the ACP measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the ACP measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_acp_configure_burst_synchronization_type.html language=enus -->
## TOPIC 00016: RFmxBT ACP Configure Burst Synchronization Type (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_acp_configure_burst_synchronization_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_acp_configure_burst_synchronization_type.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT ACP Configure Burst Synchronization Type (VI)

Owning Palette:

ACP

Configures the type of synchronization used for detecting the start of the packet in the adjacent channel power (ACP) measurement.

[IMAGE alt='RFmxBT ACP Configure Burst Synchronization Type' src='rfmxbt_acp_configure_burst_synchronization_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Burst Sync Type specifies the type of synchronization used for detecting the start of packet in the measurement. The default value is Preamble. None (0) Specifies that the measurement does not perform synchronization to detect the start of the packet. Preamble (1) Specifies that the measurement uses the preamble field bits to detect the start of the packet. Sync Word (2) Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the BD Address LAP property. |
| None (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| Preamble (1) | Specifies that the measurement uses the preamble field bits to detect the start of the packet. |
| Sync Word (2) | Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the BD Address LAP property. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_acp_configure_number_of_offsets.html language=enus -->
## TOPIC 00017: RFmxBT ACP Configure Number of Offsets (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_acp_configure_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_acp_configure_number_of_offsets.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT ACP Configure Number of Offsets (VI)

Owning Palette:

ACP

Configures the number of offsets for the adjacent channel power (ACP) measurement.

[IMAGE alt='RFmxBT ACP Configure Number of Offsets' src='rfmxbt_acp_configure_number_of_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Offsets specifies the number of offset channels used on either side of the reference channel for the ACP measurement when you set the ACP Offset Channel Mode property to Symmetric. This parameter returns the actual number of offsets used in the ACP measurement when you set the ACP Offset Channel Mode property to In-band. The default value is 5. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_acp_configure_offset_channel_mode.html language=enus -->
## TOPIC 00018: RFmxBT ACP Configure Offset Channel Mode (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_acp_configure_offset_channel_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_acp_configure_offset_channel_mode.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT ACP Configure Offset Channel Mode (VI)

Owning Palette:

ACP

Configures the offset channels used for the adjacent channel power (ACP) measurement.

[IMAGE alt='RFmxBT ACP Configure Offset Channel Mode' src='rfmxbt_acp_configure_offset_channel_mode.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset Channel Mode specifies which offset channels are used for the measurement. The default value is Symmetric. Symmetric (0) Specifies that the offset channels are symmetrically located around the reference channel. The number of offsets on either side of the reference channel is specified by the ACP Num Offsets property. In symmetric mode, the Center Frequency property specifies the frequency of the reference channel, expressed in Hz. In-band (1) Specifies that the measurement is performed over all the channels as specified by the standard. For BR and EDR packets, 79 channels starting from 2.402GHz to 2.48GHz are used for the measurement. For LE packets, 81 channels starting from 2.401GHz to 2.481GHz are used for the measurement. In In-band mode, the Center Frequency property specifies the frequency of acquisition which must be equal to 2.441GHz. Configure the Channel Number property to specify the frequency of the reference channel. |
| Symmetric (0) | Specifies that the offset channels are symmetrically located around the reference channel. The number of offsets on either side of the reference channel is specified by the ACP Num Offsets property. In symmetric mode, the Center Frequency property specifies the frequency of the reference channel, expressed in Hz. |
| In-band (1) | Specifies that the measurement is performed over all the channels as specified by the standard. For BR and EDR packets, 79 channels starting from 2.402GHz to 2.48GHz are used for the measurement. For LE packets, 81 channels starting from 2.401GHz to 2.481GHz are used for the measurement. In In-band mode, the Center Frequency property specifies the frequency of acquisition which must be equal to 2.441GHz. Configure the Channel Number property to specify the frequency of the reference channel. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_acp_fetch.html language=enus -->
## TOPIC 00019: RFmxBT ACP Fetch (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_acp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_acp_fetch.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT ACP Fetch (VI)

Owning Palette:

Fetch

Fetches the ACP measurement results.

#### RFmxBT ACP Fetch Absolute Power Trace

Fetches the absolute power trace for ACP measurement.

[IMAGE alt='RFmxBT ACP Fetch Absolute Power Trace' src='rfmxbt_acp_fetch_absolute_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns the absolute power trace. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the power measured in the carrier and offset channels. This value is expressed in Hz. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the power measured in the carrier and offset channels. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ACP Fetch Mask Trace

Fetches the limit with exception mask and limit without exception mask traces for ACP measurement. This VI returns a valid trace only if you set the [ACP Offset Channel Mode](/csh?topicname=rfmxbtprop/attrb05002.html) property to **In-band**.

[IMAGE alt='RFmxBT ACP Fetch Mask Trace' src='rfmxbt_acp_fetch_mask_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Limit With Exception Mask returns the limit with exception mask trace used for the measurement. x0 returns the start frequency, which is the center frequency of the lowest offset. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the limit with exception mask used for the measurement. This value is expressed in dBm. |
|  | x0 returns the start frequency, which is the center frequency of the lowest offset. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the limit with exception mask used for the measurement. This value is expressed in dBm. |
|  | Limit Without Exception Mask returns the limit without exception mask trace used for the measurement. x0 returns the start frequency, which is the center frequency of the lowest offset. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the limit without exception mask used for the measurement. This value is expressed in dBm. |
|  | x0 returns the start frequency, which is the center frequency of the lowest offset. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the limit without exception mask used for the measurement. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ACP Fetch Measurement Status

Fetches the overall ACP measurement status based on the measurement limits as defined by the standard if you set the [ACP Offset Channel Mode](/csh?topicname=rfmxbtprop/attrb05002.html) property to **In-Band**. This VI is not valid if you set the ACP Offset Channel Mode property to **Symmetric**.

[IMAGE alt='RFmxBT ACP Fetch Measurement Status' src='rfmxbt_acp_fetch_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the overall measurement status based on the measurement limits specified by the standard when you set the ACP Offset Channel Mode property to In-Band. Refer to ACP Results Meas Status property for more information about measurement status. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ACP Fetch Offset Measurement

Fetches the absolute powers, relative powers and margins measured in the offset channel.

Use "offset<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxBT ACP Fetch Offset Measurement' src='rfmxbt_acp_fetch_offset_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, offset number, and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "signal::sig1/result::r1/offset0" "result::r1/offset0" You can use the RFmxBT Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Lower Absolute Power returns the absolute power measured in the lower offset channel. This value is expressed in dBm. |
|  | Upper Absolute Power returns the absolute power measured in the upper offset channel. This value is expressed in dBm. |
|  | Lower Relative Power returns the relative power in the lower offset channel measured with respect to the reference channel power. This value is expressed in dB. |
|  | Upper Relative Power returns the relative power in the upper offset channel measured with respect to the reference channel power. This value is expressed in dB. |
|  | Lower Margin returns the margin from the limit specified by the mask with exception for lower offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This parameter is valid only if you set the ACP Offset Channel Mode property to In-band. This parameter returns NaN if you set the ACP Offset Channel Mode property to Symmetric. |
|  | Upper Margin returns the margin from the limit specified by the mask with exception for upper offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This parameter is valid only if you set the ACP Offset Channel Mode property to In-band. This parameter returns NaN if you set the ACP Offset Channel Mode property to Symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ACP Fetch Offset Measurement (Array)

Fetches the array of absolute powers, relative powers and margins measured in the offset channels.

[IMAGE alt='RFmxBT ACP Fetch Offset Measurement (Array)' src='rfmxbt_acp_fetch_offset_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Lower Absolute Power returns the array of absolute power measured in the lower offset channel. This value is expressed in dBm. |
|  | Upper Absolute Power returns the array of absolute power measured in the upper offset channel. This value is expressed in dBm. |
|  | Lower Relative Power returns the array of relative power in the lower offset channel measured with respect to the reference channel power. This value is expressed in dB. |
|  | Upper Relative Power returns array of the relative power in the upper offset channel measured with respect to the reference channel power. This value is expressed in dB. |
|  | Lower Margin returns the array of margin from the limit specified by the mask with Exception for lower offset channel. This value is expressed in dB. Margin is defined as the difference between the Offset Absolute Power and Mask with Exception. This parameter is valid only if you set the ACP Offset Channel Mode property to In-band. This parameter returns NaN if you set the ACP Offset Channel Mode property to Symmetric. |
|  | Upper Margin returns the array of the margin from the limit specified by the mask with Exception for upper offset channel. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This parameter is valid only if you set the ACP Offset Channel Mode property to In-band. This parameter returns NaN if you set the ACP Offset Channel Mode property to Symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ACP Fetch Reference Channel Power

Returns the measured power of the reference channel.

[IMAGE alt='RFmxBT ACP Fetch Reference Channel Power' src='rfmxbt_acp_fetch_reference_channel_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Reference Channel Power returns the measured power of the reference channel. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ACP Fetch Spectrum

Fetches the spectrum used for ACP measurement.

[IMAGE alt='RFmxBT ACP Fetch Spectrum' src='rfmxbt_acp_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the ACP spectrum trace. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_analyze_(iq_1_wfm).html language=enus -->
## TOPIC 00020: RFmxBT Analyze (IQ, 1 Wfm) (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_analyze_(iq_1_wfm).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_analyze_(iq_1_wfm).html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Analyze (IQ, 1 Wfm) (VI)

Owning Palette:

Advanced

Performs the enabled measurements on the I/Q complex waveform that you specify in the **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?topicname=rfmxinstrprop/attr27.html) property value is either **IQ** or **IQ or Spectral**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmxBT Commit VI. |
| --- | --- |

[IMAGE alt='RFmxBT Analyze (IQ 1 Wfm)' src='rfmxbt_analyze_(iq_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | IQ specifies the data for a complex I/Q waveform including the start, delta, and actual values. x0 specifies the start time of the input y array. This value is expressed in seconds. dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input y array. This value is expressed in seconds. |
|  | dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_auto_detect_signal.html language=enus -->
## TOPIC 00021: RFmxBT Auto Detect Signal (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_auto_detect_signal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_auto_detect_signal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Auto Detect Signal (VI)

Detects the Bluetooth packet and returns the detected packet type, data rate, and payload length.

[IMAGE alt='RFmxBT Auto Detect Signal' src='rfmxbt_auto_detect_signal.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_auto_level.html language=enus -->
## TOPIC 00022: RFmxBT Auto Level (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_auto_level.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Auto Level (VI)

Owning Palette:

Configuration

Examines the input signal to calculate the peak power level and sets it as the value of the [Reference Level](/csh?topicname=rfmxbtprop/attrb00002.html) property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxBT Auto Level VI does the following:

1. Resets the mixer level, mixer level offset and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

You can also specify the starting reference level using the [Auto Level Initial Reference Level](/csh?topicname=rfmxbtprop/attrb0d001.html) property.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxBT Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this VI, thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='RFmxBT Auto Level' src='rfmxbt_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Interval specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Reference Level returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_build_offset_string.html language=enus -->
## TOPIC 00023: RFmxBT Build Offset String (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_build_offset_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_build_offset_string.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Build Offset String (VI)

Owning Palette:

Build String

Creates the offset string.

[IMAGE alt='RFmxBT Build Offset String' src='rfmxbt_build_offset_string.gif']

|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
| --- | --- |
|  | Offset Number specifies the offset number for building the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_build_signal_string.html language=enus -->
## TOPIC 00024: RFmxBT Build Signal String (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_build_signal_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_build_signal_string.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Build Signal String (VI)

Owning Palette:

Build String

Creates a selector string.

[IMAGE alt='RFmxBT Build Signal String' src='rfmxbt_build_signal_string.gif']

|  | Result Name specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string). Example: "result::r1" "r1" |
| --- | --- |
|  | Signal Name specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Example: "signal::sig1" "sig1" |
|  | Selector String returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_build_slot_string.html language=enus -->
## TOPIC 00025: RFmxBT Build Slot String (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_build_slot_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_build_slot_string.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Build Slot String (VI)

Owning Palette:

Build String

Creates the slot string for use with the TXP configuration or fetch properties and VIs.

[IMAGE alt='RFmxBT Build Slot String' src='rfmxbt_build_slot_string.gif']

|  | Slot Number specifies the slot number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_check_measurement_status.html language=enus -->
## TOPIC 00026: RFmxBT Check Measurement Status (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_check_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_check_measurement_status.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Check Measurement Status (VI)

Owning Palette:

Utility

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='RFmxBT Check Measurement Status' src='rfmxbt_check_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | done? indicates whether the measurement is complete. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_clear_all_named_results.html language=enus -->
## TOPIC 00027: RFmxBT Clear All Named Results (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_clear_all_named_results.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_clear_all_named_results.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Clear All Named Results (VI)

Owning Palette:

Advanced

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxBT Clear All Named Results' src='rfmxbt_clear_all_named_results.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_clear_named_result.html language=enus -->
## TOPIC 00028: RFmxBT Clear Named Result (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_clear_named_result.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_clear_named_result.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Clear Named Result (VI)

Owning Palette:

Advanced

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='RFmxBT Clear Named Result' src='rfmxbt_clear_named_result.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_clone_signal_configuration.html language=enus -->
## TOPIC 00029: RFmxBT Clone Signal Configuration (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_clone_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_clone_signal_configuration.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Clone Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='RFmxBT Clone Signal Configuration' src='rfmxbt_clone_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
|  | Old Signal Name specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_commit.html language=enus -->
## TOPIC 00030: RFmxBT Commit (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_commit.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Commit (VI)

Owning Palette:

Utility

Commits settings to the hardware. Calling this VI is optional. RFmxBT commits settings to the hardware when you call the [RFmxBT Initiate](../rfmxbtvi/rfmxbt_initiate.html) VI or any of the measurement Read VIs.

[IMAGE alt='RFmxBT Commit' src='rfmxbt_commit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_configure_channel_number.html language=enus -->
## TOPIC 00031: RFmxBT Configure Channel Number (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_configure_channel_number.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_configure_channel_number.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Configure Channel Number (VI)

Configures the RF channel number of the signal generated by the device under test (DUT), as defined in the Bluetooth specification.

[IMAGE alt='RFmxBT Configure Channel Number' src='rfmxbt_configure_channel_number.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Channel Number specifies the RF channel number of the signal generated by the device under test (DUT), as defined in the Bluetooth specification. This parameter is applicable when you enable the ACP measurement and when you set the ACP Offset Channel Mode property to In-band. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_configure_data_rate.html language=enus -->
## TOPIC 00032: RFmxBT Configure Data Rate (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_configure_data_rate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_configure_data_rate.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Configure Data Rate (VI)

Owning Palette:

Configuration

Configures the data rate of low energy (LE) or low energy - channel sounding (LE-CS) packets to be measured.

[IMAGE alt='RFmxBT Configure Data Rate' src='rfmxbt_configure_data_rate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Data Rate specifies the data rate of the LE packet transmitted by the device under test (DUT). This value is expressed in bps. This parameter is applicable only to the LE/LE-CS packet types. The default value is 1M. 125K (125000) The date rate is 125 Kbps. 500K (500000) The date rate is 500 Kbps. 1M (1000000) The date rate is 1 Mbps. 2M (2000000) The date rate is 2 Mbps. |
| 125K (125000) | The date rate is 125 Kbps. |
| 500K (500000) | The date rate is 500 Kbps. |
| 1M (1000000) | The date rate is 1 Mbps. |
| 2M (2000000) | The date rate is 2 Mbps. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_configure_external_attenuation.html language=enus -->
## TOPIC 00033: RFmxBT Configure External Attenuation (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_configure_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_configure_external_attenuation.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Configure External Attenuation (VI)

Owning Palette:

Configuration

Configures the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer.

[IMAGE alt='RFmxBT Configure External Attenuation' src='rfmxbt_configure_external_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | External Attenuation specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The value is expressed in dB. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_configure_frequency.html language=enus -->
## TOPIC 00034: RFmxBT Configure Frequency (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_configure_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_configure_frequency.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Configure Frequency (VI)

Owning Palette:

Configuration

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### RFmxBT Configure Frequency (Frequency)

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

[IMAGE alt='RFmxBT Configure Frequency (Frequency)' src='rfmxbt_configure_frequency_(frequency).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. The default value of this parameter is hardware dependent. The default value for the devices PXIe-5645/5820 is 0 Hz. The default value for devices PXIe-5644/5646/5840/5663/5663E/5665/5668 is 2.402 GHz. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT Configure Frequency (Channel Number)

Configures the expected carrier frequency of the RF signal to be acquired using **Channel Number** and 
 **Standard** parameters.

[IMAGE alt='RFmxBT Configure Frequency (Channel Number)' src='rfmxbt_configure_frequency_(channel_number).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Standard specifies the signal to which the Bluetooth physical layer belongs. The default value is BR/EDR. BR/EDR (0) Specifies that the signal belongs to Basic Rate (BR) or Enhanced Data Rate (EDR) PHY. LE (1) Specifies that the signal belongs to Low Energy (LE) PHY. LE-CS (2) Specifies that the signal belongs to Low Energy - Channel Sounding (LE-CS) PHY. |
| BR/EDR (0) | Specifies that the signal belongs to Basic Rate (BR) or Enhanced Data Rate (EDR) PHY. |
| LE (1) | Specifies that the signal belongs to Low Energy (LE) PHY. |
| LE-CS (2) | Specifies that the signal belongs to Low Energy - Channel Sounding (LE-CS) PHY. |
|  | Channel Number specifies the RF channel number of the signal generated by the device under test (DUT), as defined in the Bluetooth specification. This parameter is applicable when you enable the ACP measurement and when you set the ACP Offset Channel Mode property to In-band. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_configure_le_direction_finding.html language=enus -->
## TOPIC 00035: RFmxBT Configure LE Direction Finding (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_configure_le_direction_finding.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_configure_le_direction_finding.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Configure LE Direction Finding (VI)

Owning Palette:

Configuration

Configures the mode of direction finding, length of the constant tone extension field, and the duration of the switching slot in the generated signal.

[IMAGE alt='RFmxBT Configure LE Direction Finding' src='rfmxbt_configure_le_direction_finding.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Direction Finding Mode specifies the mode of direction finding. The default value is Disabled. Disabled (0) Specifies that the LE packet does not have fields required for direction finding. Angle of Arrival (1) Specifies the LE packets uses the Angle of Arrival method of direction finding. Angle of Departure (2) Specifies the LE packets uses the angle of departure method of direction finding. |
| Disabled (0) | Specifies that the LE packet does not have fields required for direction finding. |
| Angle of Arrival (1) | Specifies the LE packets uses the Angle of Arrival method of direction finding. |
| Angle of Departure (2) | Specifies the LE packets uses the angle of departure method of direction finding. |
|  | CTE Length specifies the length of the constant tone extension field in the generated signal. This value is expressed in seconds. This parameter is applicable only when you set the Direction Finding Mode parameter to either Angle of Arrival or Angle of Departure. The default value is 160 microseconds. |
|  | CTE Slot Duration specifies the length of the switching slots and transmit slots in the constant tone extension field in the generated signal. This property is applicable only when you set the Direction Finding Mode parameter to Angle of Arrival or Angle of Departure The default value is 1u. 1u (0.000001) Specifies that the length of the transmit slot and sampling slot is 0.000001. 2u (0.000002) Specifies that the length of the transmit slot and sampling slot is 0.000002. |
| 1u (0.000001) | Specifies that the length of the transmit slot and sampling slot is 0.000001. |
| 2u (0.000002) | Specifies that the length of the transmit slot and sampling slot is 0.000002. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_configure_packet_type.html language=enus -->
## TOPIC 00036: RFmxBT Configure Packet Type (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_configure_packet_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_configure_packet_type.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Configure Packet Type (VI)

Owning Palette:

Configuration

Configures the type of Bluetooth packet to be measured.

[IMAGE alt='RFmxBT Configure Packet Type' src='rfmxbt_configure_packet_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Packet Type specifies the type of Bluetooth packet to be measured. In this document, packet type is sometimes referred to by the Bluetooth physical layer (PHY) it belongs to. Supported Bluetooth physical layers are basic rate (BR), enhanced data rate (EDR), low energy (LE) and low energy - channel sounding (LE-CS). The default value is DH1. DH1 (0) Specifies that the packet type is DH1. The packet belongs to BR PHY. Refer to sections 6.5.1.5 and 6.5.4.2, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. DH3 (1) Specifies that the packet type is DH3. The packet belongs to BR PHY. Refer to section 6.5.4.4, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. DH5 (2) Specifies that the packet type is DH5. The packet belongs to BR PHY. Refer to section 6.5.4.6, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. DM1 (3) Specifies that the packet type is DM1. The packet belongs to BR PHY. Refer to sections 6.5.1.5 and 6.5.4.1, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. DM3 (4) Specifies that the packet type is DM3. The packet belongs to BR PHY. Refer to section 6.5.4.3, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. DM5 (5) Specifies that the packet type is DM5. The packet belongs to BR PHY. Refer to section 6.5.4.5, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. 2-DH1 (6) Specifies that the packet type is 2-DH1. The packet belongs to EDR PHY. Refer to section 6.5.4.8, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. 2-DH3 (7) Specifies that the packet type is 2-DH3. The packet belongs to EDR PHY. Refer to section 6.5.4.9, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. 2-DH5 (8) Specifies that the packet type is 2-DH5. The packet belongs to EDR PHY. Refer to section 6.5.4.10, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. 3-DH1 (9) Specifies that the packet type is 3-DH1. The packet belongs to EDR PHY. Refer to section 6.5.4.11, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. 3-DH3 (10) Specifies that the packet type is 3-DH3. The packet belongs to EDR PHY. Refer to section 6.5.4.12, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. 3-DH5 (11) Specifies that the packet type is 3-DH5. The packet belongs to EDR PHY. Refer to section 6.5.4.13, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. 2-EV3 (12) Specifies that the packet type is 2-EV3. The packet belongs to EDR PHY. Refer to section 6.5.3.4, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. 2-EV5 (13) Specifies that the packet type is 2-EV5. The packet belongs to EDR PHY. Refer to section 6.5.3.5, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. 3-EV3 (14) Specifies that the packet type is 3-EV3. The packet belongs to EDR PHY. Refer to section 6.5.3.6, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. 3-EV5 (15) Specifies that the packet type is 3-EV5. The packet belongs to EDR PHY. Refer to section 6.5.3.7, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. LE (16) Specifies that the packet belongs to LE PHY. Refer to sections 2.1 and 2.2, Part B, Volume 6 of the Bluetooth Core Specification v5.1 for more information about this packet. LE-CS (17) Specifies that the packet type is LE-CS. The packet belongs to LE-CS PHY. |
| DH1 (0) | Specifies that the packet type is DH1. The packet belongs to BR PHY. Refer to sections 6.5.1.5 and 6.5.4.2, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DH3 (1) | Specifies that the packet type is DH3. The packet belongs to BR PHY. Refer to section 6.5.4.4, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DH5 (2) | Specifies that the packet type is DH5. The packet belongs to BR PHY. Refer to section 6.5.4.6, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DM1 (3) | Specifies that the packet type is DM1. The packet belongs to BR PHY. Refer to sections 6.5.1.5 and 6.5.4.1, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DM3 (4) | Specifies that the packet type is DM3. The packet belongs to BR PHY. Refer to section 6.5.4.3, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DM5 (5) | Specifies that the packet type is DM5. The packet belongs to BR PHY. Refer to section 6.5.4.5, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-DH1 (6) | Specifies that the packet type is 2-DH1. The packet belongs to EDR PHY. Refer to section 6.5.4.8, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-DH3 (7) | Specifies that the packet type is 2-DH3. The packet belongs to EDR PHY. Refer to section 6.5.4.9, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-DH5 (8) | Specifies that the packet type is 2-DH5. The packet belongs to EDR PHY. Refer to section 6.5.4.10, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-DH1 (9) | Specifies that the packet type is 3-DH1. The packet belongs to EDR PHY. Refer to section 6.5.4.11, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-DH3 (10) | Specifies that the packet type is 3-DH3. The packet belongs to EDR PHY. Refer to section 6.5.4.12, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-DH5 (11) | Specifies that the packet type is 3-DH5. The packet belongs to EDR PHY. Refer to section 6.5.4.13, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-EV3 (12) | Specifies that the packet type is 2-EV3. The packet belongs to EDR PHY. Refer to section 6.5.3.4, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-EV5 (13) | Specifies that the packet type is 2-EV5. The packet belongs to EDR PHY. Refer to section 6.5.3.5, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-EV3 (14) | Specifies that the packet type is 3-EV3. The packet belongs to EDR PHY. Refer to section 6.5.3.6, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-EV5 (15) | Specifies that the packet type is 3-EV5. The packet belongs to EDR PHY. Refer to section 6.5.3.7, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| LE (16) | Specifies that the packet belongs to LE PHY. Refer to sections 2.1 and 2.2, Part B, Volume 6 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| LE-CS (17) | Specifies that the packet type is LE-CS. The packet belongs to LE-CS PHY. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_configure_payload_bit_pattern.html language=enus -->
## TOPIC 00037: RFmxBT Configure Payload Bit Pattern (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_configure_payload_bit_pattern.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_configure_payload_bit_pattern.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Configure Payload Bit Pattern (VI)

Owning Palette:

Configuration

Configures the bit pattern present in the payload of the packet.

[IMAGE alt='RFmxBT Configure Payload Bit Pattern' src='rfmxbt_configure_payload_bit_pattern.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |  |  |  |
| --- | --- | --- | --- | --- |
|  | Payload Bit Pattern specifies the bit pattern present in the payload of the packet. This value is used to determine the set of ModAcc measurements to be performed. The following table shows the measurements applicable for different payload bit patterns: Bluetooth PHY Data Rate Standard 11110000 10101010 BR NA Error df1 df2 and BR frequency error EDR NA DEVM (The measurement considers PN9 as payload pattern) Error Error LE 1 Mbps Error df1 and LE frequency errors on the constant tone extension (CTE) field within the direction finding packets. df2 and LE frequency error LE 2 Mbps Error df1 and LE frequency errors on the constant tone extension (CTE) field within the direction finding packets. df2 and LE frequency error LE 125 kbps df1 and LE frequency errors (The measurement considers 11111111 as payload pattern) Error Error LE 500 kbps df2 and LE frequency errors (The measurement considers 11111111 as payload pattern) Error Error The default value is Standard Defined. Standard Defined (0) Specifies that the payload bit pattern is Standard Defined. 11110000 (1) Specifies that the payload bit pattern is 11110000. 10101010 (2) Specifies that the payload bit pattern is 10101010. |  |  |  |
| Bluetooth PHY | Data Rate | Standard | 11110000 | 10101010 |
| BR | NA | Error | df1 | df2 and BR frequency error |
| EDR | NA | DEVM (The measurement considers PN9 as payload pattern) | Error | Error |
| LE | 1 Mbps | Error | df1 and LE frequency errors on the constant tone extension (CTE) field within the direction finding packets. | df2 and LE frequency error |
| LE | 2 Mbps | Error | df1 and LE frequency errors on the constant tone extension (CTE) field within the direction finding packets. | df2 and LE frequency error |
| LE | 125 kbps | df1 and LE frequency errors (The measurement considers 11111111 as payload pattern) | Error | Error |
| LE | 500 kbps | df2 and LE frequency errors (The measurement considers 11111111 as payload pattern) | Error | Error |
| Standard Defined (0) | Specifies that the payload bit pattern is Standard Defined. |  |  |  |
| 11110000 (1) | Specifies that the payload bit pattern is 11110000. |  |  |  |
| 10101010 (2) | Specifies that the payload bit pattern is 10101010. |  |  |  |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |  |  |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |  |  |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |  |  |  |
|  | error out contains error information. This output provides standard error out functionality. |  |  |  |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_configure_payload_length.html language=enus -->
## TOPIC 00038: RFmxBT Configure Payload Length (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_configure_payload_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_configure_payload_length.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Configure Payload Length (VI)

Owning Palette:

Configuration

Configures the **Payload Length Mode** and **Payload Length** parameters that decide the length of the payload to be used for the measurement.

[IMAGE alt='RFmxBT Configure Payload Length' src='rfmxbt_configure_payload_length.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Payload Length Mode specifies the payload length mode of the signal to be measured. The Payload Length Mode and Payload Length parameters decide the length of the payload to be used for measurement. The default value is Auto. Manual (0) Enables the value specified by the Payload Length parameter. The acquisition and measurement durations will be decided based on this value. Auto (1) Enables the standard defined maximum payload length for the selected packet type. If this parameter is set to Auto, the maximum standard defined payload length for the selected packet type is chosen. For LE, the maximum payload length that a device under test(DUT) can generate varies from 37 to 255 bytes. When you set the payload length mode for the LE packet type to Auto, RFmx chooses 37 bytes as the payload length. |
| Manual (0) | Enables the value specified by the Payload Length parameter. The acquisition and measurement durations will be decided based on this value. |
| Auto (1) | Enables the standard defined maximum payload length for the selected packet type. If this parameter is set to Auto, the maximum standard defined payload length for the selected packet type is chosen. For LE, the maximum payload length that a device under test(DUT) can generate varies from 37 to 255 bytes. When you set the payload length mode for the LE packet type to Auto, RFmx chooses 37 bytes as the payload length. |
|  | Payload Length specifies the payload length of the signal in bytes. The parameter is applicable only when you set the Payload Length Mode parameter to Manual. This parameter returns the payload length used for measurement if you set the Payload Length Mode parameter to Auto. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_configure_reference_level.html language=enus -->
## TOPIC 00039: RFmxBT Configure Reference Level (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_configure_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_configure_reference_level.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Configure Reference Level (VI)

Owning Palette:

Configuration

Configures the reference level which represents the maximum expected power of an RF input signal.

[IMAGE alt='RFmxBT Configure Reference Level' src='rfmxbt_configure_reference_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Level specifies the reference level which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_configure_rf.html language=enus -->
## TOPIC 00040: RFmxBT Configure RF (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_configure_rf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_configure_rf.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Configure RF (VI)

Owning Palette:

Configuration

Configures the RF properties of the signal specified by the selector string.

[IMAGE alt='RFmxBT Configure RF' src='rfmxbt_configure_rf.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. The value is expressed in Hz. The default of this property is hardware dependent. |
|  | Reference Level specifies the reference level which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent. |
|  | External Attenuation specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The value is expressed in dB. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_configure_trigger.html language=enus -->
## TOPIC 00041: RFmxBT Configure Trigger (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_configure_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_configure_trigger.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Configure Trigger (VI)

Owning Palette:

Configuration

Configures the reference trigger to use to acquire the signal.

#### RFmxBT Configure IQ Power Edge Trigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.

To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

[IMAGE alt='RFmxBT Configure IQ Power Edge Trigger' src='rfmxbt_configure_iq_power_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | IQ Power Edge Source specifies the channel from which the device monitors the trigger. The default of this property is hardware dependent. |
|  | IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
|  | IQ Power Edge Level specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative; and is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this property is hardware dependent. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Trigger Delay specifies the trigger delay time, in seconds. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | Minimum Quiet Time Mode specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Auto. Manual (0) The minimum quiet time used for triggering is the value of the Min Quiet Time parameter. Auto (1) The measurement computes the minimum quiet time used for triggering. |
| Manual (0) | The minimum quiet time used for triggering is the value of the Min Quiet Time parameter. |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |
|  | Minimum Quiet Time specifies the duration, in seconds, for which the signal must be quiet before the signal analyzer arms the I/Q Power Edge trigger. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default of this property is hardware dependent. |
|  | IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. The default value is Relative. Relative (0) The IQ Power Edge Level parameter is relative to the value of the Reference Level property. Absolute (1) The IQ Power Edge Level parameter specifies the absolute power. |
| Relative (0) | The IQ Power Edge Level parameter is relative to the value of the Reference Level property. |
| Absolute (1) | The IQ Power Edge Level parameter specifies the absolute power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT Configure Software Edge Trigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

[IMAGE alt='RFmxBT Configure Software Edge Trigger' src='rfmxbt_configure_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Trigger Delay specifies the trigger delay time, in seconds. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT Configure Digital Edge Trigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

[IMAGE alt='RFmxBT Configure Digital Edge Trigger' src='rfmxbt_configure_digital_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Digital Edge Source specifies the source terminal for the digital edge trigger. The default of this property is hardware dependent. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. PXIe_DStarB (PXIe_DStarB) The trigger is received on the PXIe DStar B trigger line. TimerEvent (TimerEvent) The trigger is received from the timer event. |
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
|  | Trigger Delay specifies the trigger delay time, in seconds. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT Disable Trigger

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='RFmxBT Disable Trigger' src='rfmxbt_disable_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_create_signal_configuration.html language=enus -->
## TOPIC 00042: RFmxBT Create Signal Configuration (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_create_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_create_signal_configuration.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Create Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal.

[IMAGE alt='RFmxBT Create Signal Configuration' src='rfmxbt_create_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_delete_signal_configuration.html language=enus -->
## TOPIC 00043: RFmxBT Delete Signal Configuration (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_delete_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_delete_signal_configuration.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Delete Signal Configuration (VI)

Owning Palette:

Advanced

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='RFmxBT Delete Signal Configuration' src='rfmxbt_delete_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_frequencyrange_configure_averaging.html language=enus -->
## TOPIC 00044: RFmxBT FrequencyRange Configure Averaging (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_frequencyrange_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_frequencyrange_configure_averaging.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT FrequencyRange Configure Averaging (VI)

Owning Palette:

Frequency Range

Configures averaging for the FrequencyRange measurement.

[IMAGE alt='RFmxBT FrequencyRange Configure Averaging' src='rfmxbt_frequencyrange_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the FrequencyRange measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the FrequencyRange measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the FrequencyRange measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_frequencyrange_configure_span.html language=enus -->
## TOPIC 00045: RFmxBT FrequencyRange Configure Span (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_frequencyrange_configure_span.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_frequencyrange_configure_span.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT FrequencyRange Configure Span (VI)

Owning Palette:

Frequency Range

Configures the span for the FrequencyRange measurement.

[IMAGE alt='RFmxBT FrequencyRange Configure Span' src='rfmxbt_frequencyrange_configure_span.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Span specifies the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the Bluetooth Test Specification v5.1.0.. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz. The default value is 10 MHz. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_frequencyrange_fetch.html language=enus -->
## TOPIC 00046: RFmxBT FrequencyRange Fetch (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_frequencyrange_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_frequencyrange_fetch.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT FrequencyRange Fetch (VI)

Owning Palette:

Fetch

Fetches the FrequencyRange measurement results.

#### RFmxBT FrequencyRange Fetch Measurement

Fetches the FrequencyRange measurement results.

[IMAGE alt='RFmxBT FrequencyRange Fetch Measurement' src='rfmxbt_frequencyrange_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | High Frequency returns the highest frequency above the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz. |
|  | Low Frequency returns the lowest frequency below the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT FrequencyRange Fetch Spectrum

Fetches the FrequencyRange spectrum trace.

[IMAGE alt='RFmxBT FrequencyRange Fetch Spectrum' src='rfmxbt_frequencyrange_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the FrequencyRange spectrum trace. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_get_all_named_result_names.html language=enus -->
## TOPIC 00047: RFmxBT Get All Named Result Names (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_get_all_named_result_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_get_all_named_result_names.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Get All Named Result Names (VI)

Owning Palette:

Advanced

Returns all the named result names of the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxBT Get All Named Result Names' src='rfmxbt_get_all_named_result_names.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Result Names returns an array of result names. |
|  | Default Result Exists? indicates whether the default result exists. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_initiate.html language=enus -->
## TOPIC 00048: RFmxBT Initiate (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_initiate.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Initiate (VI)

Owning Palette:

RFmx for Bluetooth® Test VIs

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the [RFmxBT Wait for Measurement Complete](rfmxbt_wait_for_measurement_complete.html) VI or [RFmxBT Check Measurement Status](rfmxbt_check_measurement_status.html) VI.

[IMAGE alt='RFmxBT Initiate' src='rfmxbt_initiate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter on Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_modacc_configure_averaging.html language=enus -->
## TOPIC 00049: RFmxBT ModAcc Configure Averaging (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_modacc_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_modacc_configure_averaging.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT ModAcc Configure Averaging (VI)

Owning Palette:

ModAcc

Configures averaging for the ModAcc measurement.

[IMAGE alt='RFmxBT ModAcc Configure Averaging' src='rfmxbt_modacc_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the ModAcc measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the ModAcc measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the ModAcc measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_modacc_configure_burst_synchronization_type.html language=enus -->
## TOPIC 00050: RFmxBT ModAcc Configure Burst Synchronization Type (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_modacc_configure_burst_synchronization_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_modacc_configure_burst_synchronization_type.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT ModAcc Configure Burst Synchronization Type (VI)

Owning Palette:

ModAcc

Configures the burst synchronization type for ModAcc measurement.

[IMAGE alt='RFmxBT ModAcc Configure Burst Synchronization Type' src='rfmxbt_modacc_configure_burst_synchronization_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Burst Sync Type specifies the type of synchronization used for detecting the start of packet in the measurement. The default value is Preamble. None (0) Specifies that the measurement does not perform synchronization to detect the start of the packet. Preamble (1) Specifies that the measurement uses the preamble field bits to detect the start of the packet. Sync Word (2) Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the BD Address LAP property. |
| None (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| Preamble (1) | Specifies that the measurement uses the preamble field bits to detect the start of the packet. |
| Sync Word (2) | Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the BD Address LAP property. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_modacc_fetch.html language=enus -->
## TOPIC 00051: RFmxBT ModAcc Fetch (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_modacc_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_modacc_fetch.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT ModAcc Fetch (VI)

Owning Palette:

Fetch

Fetches the ModAcc measurement results.

#### RFmxBT ModAcc Fetch Constellation Trace

Fetches the demodulated symbols from the enhanced data rate (EDR) portion of the EDR packet. This VI is valid only for EDR packets.

[IMAGE alt='RFmxBT ModAcc Fetch Constellation Trace' src='rfmxbt_modacc_fetch_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Constellation returns the array of demodulated symbols from over the EDR portion of the EDR packet. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch DEVM

Fetches ModAcc differential EVM (DEVM) measurement results. These results are valid only for enhanced data rate (EDR) packets.

[IMAGE alt='RFmxBT ModAcc Fetch DEVM' src='rfmxbt_modacc_fetch_devm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Peak RMS DEVM Maximum returns the peak of the RMS DEVM values computed on each 50us block of the EDR portion of the EDR packet. When you set ModAcc Averaging Enabled property to True, it returns the maximum of the peak RMS DEVM values computed for each averaging count. This value is expressed in percentage. |
|  | Peak DEVM Maximum returns the peak of the DEVM values computed on symbols in the EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled property to True, it returns the maximum of the peak symbol DEVM values computed for each averaging count. This value is expressed in percentage. |
|  | 99% DEVM returns the 99th percentile of the DEVM values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed in percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch DEVM Per Symbol Trace

Fetches the DEVM values for symbols from the enhanced data rate (EDR) portion of the EDR packet. This VI is valid only for EDR packets.

[IMAGE alt='RFmxBT ModAcc Fetch DEVM Per Symbol Trace' src='rfmxbt_modacc_fetch_devm_per_symbol_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | DEVM Per Symbol returns the array of DEVM values computed over the symbols in the EDR portion of EDR packet. This value is expressed in percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch df1

Fetches the ModAcc df1 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets.

[IMAGE alt='RFmxBT ModAcc Fetch df1' src='rfmxbt_modacc_fetch_df1.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | df1avg Maximum returns the df1avg value computed on the signal. This value is expressed in Hz. When you set the ModAcc Averaging Enabled property to True, it returns the maximum of the df1avg results computed for each averaging count. |
|  | df1avg Minimum returns the df1avg value computed on the signal. This value is expressed in Hz. When you set the ModAcc Averaging Enabled property to True, it returns the minimum of the df1avg results computed for each averaging count. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch df1max Trace

Fetches the df1max versus the time trace. This VI is applicable only for basic rate (BR) and low energy (LE) packets.

[IMAGE alt='RFmxBT ModAcc Fetch df1max Trace' src='rfmxbt_modacc_fetch_df1max_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Time returns the array of time instances at which the df1max values are computed. This value is expressed in seconds. |
|  | df1max returns the array of df1max values computed over the packet at each time instance. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch df2

Fetches the ModAcc df2 measurement results. These results are valid only for basic rate (BR) and low energy (LE) packets.

[IMAGE alt='RFmxBT ModAcc Fetch df2' src='rfmxbt_modacc_fetch_df2.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | df2avg Minimum returns the df2avg value computed on the signal. When you set the ModAcc Averaging Enabled property to True, it returns the minimum of the df2avg results computed for each averaging count. This value is expressed in Hz. |
|  | Percentage of Symbols above df2max Threshold returns the percentage of symbols with df2max values that are greater than the df2max threshold defined by the standard. When you set the ModAcc Averaging Enabled property to True, it computes this result using the df2max values from all averaging counts. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch df2max Trace

Fetches the df2max versus the time trace. This VI is valid only for basic rate (BR) and low energy (LE) packets.

[IMAGE alt='RFmxBT ModAcc Fetch df2max Trace' src='rfmxbt_modacc_fetch_df2max_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Time returns the array of time instances at which the df2max values are computed. This value is expressed in seconds. |
|  | df2max returns the array of df2max values computed over the packet at each time instance. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch df4avg Trace

Fetches the df4avg versus the time trace. This VI is valid only for LE-CS Packets.

[IMAGE alt='RFmxBT ModAcc Fetch df4avg Trace' src='rfmxbt_modacc_fetch_df4avg_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Time returns the array of time instances at which the df4avg values are computed. This value is expressed in seconds. |
|  | df4avg (Hz)returns the array of df4avg values computed over the packet at each time instance. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch Frequency Error (BR)

Fetches the ModAcc frequency error trace for basic rate (BR) packets.

[IMAGE alt='RFmxBT ModAcc Fetch Frequency Error (BR)' src='rfmxbt_modacc_fetch_frequency_error_(br).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Initial Frequency Error Maximum returns the initial frequency error value computed on the preamble of the BR packet. When you set the ModAcc Averaging Enabled property to True, it returns a value corresponding to the maximum of absolute initial frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | Peak Frequency Drift Maximum returns the peak frequency drift value computed on the BR packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
|  | Peak Frequency Drift Rate Maximum returns the peak frequency drift rate value computed on the BR packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch Frequency Error (EDR)

Fetches ModAcc frequency error measurement results for enhanced data rate (EDR) packets.

[IMAGE alt='RFmxBT ModAcc Fetch Frequency Error (EDR)' src='rfmxbt_modacc_fetch_frequency_error_(edr).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Header Frequency Error wi Maximum returns the frequency error value computed on the header of the EDR packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute header frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | Peak Frequency Error wi+w0 Maximum returns the peak frequency error value computed on the EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | Peak Frequency Error w0 Maximum returns the peak frequency error value computed on the EDR portion of the EDR packet, relative to the header frequency error. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch Frequency Error (LE)

Fetches ModAcc frequency error measurement results for low energy (LE) or low energy - channel sounding (LE-CS) packets.

[IMAGE alt='RFmxBT ModAcc Fetch Frequency Error (LE)' src='rfmxbt_modacc_fetch_frequency_error_(le).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Peak Frequency Error Maximum when you set the Direction Finding Mode property to Disabled, it returns the peak frequency error value computed on the preamble and payload portion of the LE packet. When you set the Direction Finding Mode property to Angle of Arrival, it returns the peak frequency error value computed on the Constant tone extension field of the LE packet. When you set the ModAcc Averaging Enabled property to True, , it returns the value corresponding to the maximum of absolute peak frequency error values computed for each averaging count. This value is expressed in Hz. |
|  | Initial Frequency Drift Maximum returns the initial frequency drift value computed on the LE packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute initial frequency drift values computed for each averaging count. This value is expressed in Hz. |
|  | Peak Frequency Drift Maximum returns the peak frequency drift value computed on the LE packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz. |
|  | Peak Frequency Drift Rate Maximum returns the peak frequency drift rate value computed on the LE packet. When you set the ModAcc Averaging Enabled property to True, it returns the value corresponding to the maximum of absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch Frequency Error Trace (BR)

Fetches the ModAcc frequency error trace for basic rate (BR) packets.

[IMAGE alt='RFmxBT ModAcc Fetch Frequency Error Trace (BR)' src='rfmxbt_modacc_fetch_frequency_error_trace_(br).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Time returns an array of time instances corresponding to the start of the bit blocks at which the frequency error values are computed. This value is expressed in seconds. |
|  | BR Frequency Error returns an array of frequency errors computed over the packet. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch Frequency Error Trace (LE)

Fetches the ModAcc frequency error trace for low energy (LE) or low energy - channel sounding (LE-CS) packets.

[IMAGE alt='RFmxBT ModAcc Fetch Frequency Error Trace (LE)' src='rfmxbt_modacc_fetch_frequency_error_trace_(le).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Time returns an array of time instances corresponding to the start of the bit blocks at which the frequency error values are computed. This value is expressed in seconds. |
|  | LE Frequency Error returns the array of frequency errors computed over the packet. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch Frequency Error wi+w0 Trace (EDR)

Fetches the ModAcc frequency error trace for enhanced data rate (EDR) packets.

[IMAGE alt='RFmxBT ModAcc Fetch Frequency Error wi+w0 Trace (EDR)' src='rfmxbt_modacc_fetch_frequency_error_wi+w0_trace_(edr).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Time returns an array of time instances corresponding to the start of the 50us blocks of the EDR portion of EDR packet at which the frequency error values are computed. This value is expressed in seconds. |
|  | EDR Frequency Error wi+w0 returns the array of frequency errors wi+w0 computed over the packet. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch Frequency Trace

Fetches the frequency versus time trace. This trace is valid for basic rate (BR), low energy (LE) and low energy - channel sounding (LE-CS) packets.

[IMAGE alt='RFmxBT ModAcc Fetch Frequency Trace' src='rfmxbt_modacc_fetch_frequency_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Frequency returns the frequency versus time trace. x0 returns the start time. This value is expressed in seconds. dx returns the sample duration. This value is expressed in seconds. y returns the frequency at each time instance. This value is expressed in Hz. |
|  | x0 returns the start time. This value is expressed in seconds. |
|  | dx returns the sample duration. This value is expressed in seconds. |
|  | y returns the frequency at each time instance. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch RMS DEVM Trace

Fetches the RMS DEVM values from each 50us block of EDR portion of EDR packet. This VI is valid only for enhanced data rate (EDR) packets.

[IMAGE alt='RFmxBT ModAcc Fetch RMS DEVM Trace' src='rfmxbt_modacc_fetch_rms_devm_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | RMS DEVM returns the array of RMS DEVM values computed on each 50us block of the EDR portion of the EDR packet. This value is expressed in percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch Demodulated Bit Trace

Fetches the ModAcc demodulated bit trace.

[IMAGE alt='RFmxBT ModAcc Fetch Demodulated Bit Trace' src='rfmxbt_modacc_fetch_demodulated_bit_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Demodulated Bits returns an array of demodulated bits of the packet. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch DEVM Magnitude Error

Fetches ModAcc RMS magnitude error results. These results are valid only for enhanced data rate (EDR) packets.

[IMAGE alt='RFmxBT ModAcc Fetch DEVM Magnitude Error' src='rfmxbt_modacc_fetch_devm_magnitude_error.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Average RMS Magnitude Error Mean returns the average of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled property to True, it returns the mean of the average RMS magnitude error values computed for each averaging count. This value is expressed as a percentage. |
|  | Peak RMS Magnitude Error Maximum returns the peak of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled property to True, it returns the maximum of the peak RMS magnitude error values computed for each averaging count. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch DEVM Phase Error

Fetches ModAcc RMS phase error results. These results are valid only for enhanced data rate (EDR) packets.

[IMAGE alt='RFmxBT ModAcc Fetch DEVM Phase Error' src='rfmxbt_modacc_fetch_devm_phase_error.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Average RMS Phase Error Mean returns the average of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled property to True, it returns the mean of the average RMS phase error values computed for each averaging count. This value is expressed in degrees. |
|  | Peak RMS Phase Error Maximum returns the peak of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the ModAcc Averaging Enabled property to True, it returns the maximum of the peak RMS phase error values computed for each averaging count. This value is expressed in degrees. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch CS Tone Trace

Fetches the CS Tone Amplitude (dBm) versus time and CS Tone Phase (deg) versus time traces. This VI is valid only for low energy CS (LE-CS) packets.

[IMAGE alt='RFmxBT ModAcc Fetch CS Tone Trace' src='rfmxbt_modacc_fetch_cs_tone_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | CS Tone Amplitude (dBm) returns the CS Tone Amplitude (dBm) versus time trace |
|  | CS Tone Phase (deg) returns the CS Tone Phase (deg) versus time trace |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT ModAcc Fetch CS Detrended Phase Trace

Fetches the zero-mean Detrended Phase (deg) versus time trace. This VI is valid only for low energy CS (LE-CS) packets.

[IMAGE alt='RFmxBT ModAcc Fetch CS Detrended Phase Trace' src='rfmxbt_modacc_fetch_cs_detrended_phase_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | CS Detrended Phase (deg) returns the zero-mean detrended phase versus time trace. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_modspectrum_configure_averaging.html language=enus -->
## TOPIC 00052: RFmxBT ModSpectrum Configure Averaging (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_modspectrum_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_modspectrum_configure_averaging.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT ModSpectrum Configure Averaging (VI)

Owning Palette:

ModSpectrum

Configures averaging for the ModSpectrum measurement.

[IMAGE alt='RFmxBT ModSpectrum Configure Averaging' src='rfmxbt_modspectrum_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the ModSpectrum measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the ModSpectrum measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the ModSpectrum measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_modspectrum_configure_burst_synchronization_type.html language=enus -->
## TOPIC 00053: RFmxBT ModSpectrum Configure Burst Synchronization Type (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_modspectrum_configure_burst_synchronization_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_modspectrum_configure_burst_synchronization_type.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT ModSpectrum Configure Burst Synchronization Type (VI)

Owning Palette:

ModSpectrum

Configures the burst synchronization type for ModSpectrum measurement.

[IMAGE alt='RFmxBT ModSpectrum Configure Burst Synchronization Type' src='rfmxbt_modspectrum_configure_burst_synchronization_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Burst Sync Type Specifies the type of synchronization used for detecting the start of packet in the ModSpectrum measurement. The default value is Preamble. None (0) Specifies that the measurement does not perform synchronization to detect the start of the packet. Preamble (1) Specifies that the measurement uses the preamble field bits to detect the start of the packet. Sync Word (2) Specifies that the measurement uses the Access Address for LE-CS packets to detect the start of the packet. |
| None (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| Preamble (1) | Specifies that the measurement uses the preamble field bits to detect the start of the packet. |
| Sync Word (2) | Specifies that the measurement uses the Access Address for LE-CS packets to detect the start of the packet. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_modspectrum_fetch_spectrum.html language=enus -->
## TOPIC 00054: RFmxBT ModSpectrum Fetch Spectrum (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_modspectrum_fetch_spectrum.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_modspectrum_fetch_spectrum.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT ModSpectrum Fetch Spectrum (VI)

Owning Palette:

Fetch

Fetches the ModSpectrum spectrum trace.

[IMAGE alt='RFmxBT ModSpectrum Fetch Spectrum' src='rfmxbt_modspectrum_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, offset number, and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "signal::sig1/result::r1/offset0" "result::r1/offset0" You can use the RFmxBT Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum Returns the ModSpectrum spectrum trace. x0Returns the start frequency. This value is expressed in Hz. dxReturns the frequency bin spacing. This value is expressed in Hz. yReturns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0Returns the start frequency. This value is expressed in Hz. |
|  | dxReturns the frequency bin spacing. This value is expressed in Hz. |
|  | yReturns the averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_powerramp_configure_averaging.html language=enus -->
## TOPIC 00055: RFmxBT PowerRamp Configure Averaging (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_powerramp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_powerramp_configure_averaging.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT PowerRamp Configure Averaging (VI)

Owning Palette:

PowerRamp

Configures averaging for the PowerRamp measurement.

[IMAGE alt='RFmxBT PowerRamp Configure Averaging' src='rfmxbt_powerramp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the PowerRamp measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the PowerRamp measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the PowerRamp measurement is averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_powerramp_configure_burst_synchronization_type.html language=enus -->
## TOPIC 00056: RFmxBT PowerRamp Configure Burst Synchronization Type (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_powerramp_configure_burst_synchronization_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_powerramp_configure_burst_synchronization_type.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT PowerRamp Configure Burst Synchronization Type (VI)

Owning Palette:

PowerRamp

Configures the burst synchronization type for PowerRamp measurement.

[IMAGE alt='RFmxBT PowerRamp Configure Burst Synchronization Type' src='rfmxbt_powerramp_configure_burst_synchronization_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Burst Sync Type Specifies the type of synchronization used for detecting the start of packet in the PowerRamp measurement. The default value is Preamble. None (0) Specifies that the measurement does not perform synchronization to detect the start of the packet. Preamble (1) Specifies that the measurement uses the preamble field bits to detect the start of the packet. Sync Word (2) Specifies that the measurement uses the Access Address for LE-CS packets to detect the start of the packet. |
| None (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| Preamble (1) | Specifies that the measurement uses the preamble field bits to detect the start of the packet. |
| Sync Word (2) | Specifies that the measurement uses the Access Address for LE-CS packets to detect the start of the packet. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_property_node.html language=enus -->
## TOPIC 00057: RFmxBT Property Node (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_property_node.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_property_node.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Property Node (VI)

Owning Palette:

RFmx for Bluetooth® Test VIs

Gets (reads), sets (writes), or resets (sets to default value) RFmxBluetooth properties.

[IMAGE alt='RFmxBT Property Node' src='rfmxbt_property_node.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_reset_to_default.html language=enus -->
## TOPIC 00058: RFmxBT Reset to Default (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_reset_to_default.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_reset_to_default.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Reset to Default (VI)

Owning Palette:

Utility

Resets a signal to the default values.

[IMAGE alt='RFmxBT Reset to Default' src='rfmxbt_reset_to_default.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_select_measurement.html language=enus -->
## TOPIC 00059: RFmxBT Select Measurement (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_select_measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_select_measurement.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Select Measurement (VI)

Owning Palette:

RFmx for Bluetooth® Test VIs

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

#### RFmxBT Select Measurement (Single)

Enables the single measurement that you specify in the **Measurement** parameter and disables all other measurements in the selected signal configuration.

[IMAGE alt='RFmxBT Select Measurement (Single)' src='rfmxbt_select_measurement_(single).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement specifies the measurement to perform. You can specify one of the following measurements. The default value is TXP. TXP (0) Enables TXP measurement. ModAcc (1) Enables ModAcc measurement. 20dB Bandwidth (2) Enables 20dB Bandwidth measurement. FrequencyRange (3) Enables FrequencyRange measurement. ACP (4) Enables ACP measurement. |
| TXP (0) | Enables TXP measurement. |
| ModAcc (1) | Enables ModAcc measurement. |
| 20dB Bandwidth (2) | Enables 20dB Bandwidth measurement. |
| FrequencyRange (3) | Enables FrequencyRange measurement. |
| ACP (4) | Enables ACP measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT Select Measurement (Multiple)

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='RFmxBT Select Measurement (Multiple)' src='rfmxbt_select_measurement_(multiple).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurements specifies the measurement to perform. You can specify one or more of the following measurements. The default is an empty array. TXP (0) Enables TXP measurement. ModAcc (1) Enables ModAcc measurement. 20dB Bandwidth (2) Enables 20dB Bandwidth measurement. FrequencyRange (3) Enables FrequencyRange measurement. ACP (4) Enables ACP measurement. |
| TXP (0) | Enables TXP measurement. |
| ModAcc (1) | Enables ModAcc measurement. |
| 20dB Bandwidth (2) | Enables 20dB Bandwidth measurement. |
| FrequencyRange (3) | Enables FrequencyRange measurement. |
| ACP (4) | Enables ACP measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_send_software_edge_trigger.html language=enus -->
## TOPIC 00060: RFmxBT Send Software Edge Trigger (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_send_software_edge_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_send_software_edge_trigger.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Send Software Edge Trigger (VI)

Owning Palette:

Configuration

Sends a trigger to the device when you use the [RFmxBT Configure Trigger](rfmxbt_configure_trigger.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxBT Initiate VI.

[IMAGE alt='RFmxBT Send Software Edge Trigger' src='rfmxbt_send_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_txp_configure_averaging.html language=enus -->
## TOPIC 00061: RFmxBT TXP Configure Averaging (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_txp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_txp_configure_averaging.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT TXP Configure Averaging (VI)

Owning Palette:

TXP

Configures averaging for the transmit power (TXP) measurement.

[IMAGE alt='RFmxBT TXP Configure Averaging' src='rfmxbt_txp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | TXP Averaging Enabled specifies whether to enable averaging for TXP measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the TXP Averaging Count parameter as the number of acquisitions over which the TXP measurement is averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the TXP Averaging Count parameter as the number of acquisitions over which the TXP measurement is averaged. |
|  | TXP Averaging Count specifies the number of acquisitions used for averaging when you set the TXP Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_txp_configure_burst_synchronization_type.html language=enus -->
## TOPIC 00062: RFmxBT TXP Configure Burst Synchronization Type (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_txp_configure_burst_synchronization_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_txp_configure_burst_synchronization_type.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT TXP Configure Burst Synchronization Type (VI)

Owning Palette:

TXP

Configures the type of synchronization used for detecting the start of the packet in the transmit power (TXP) measurement.

[IMAGE alt='RFmxBT TXP Configure Burst Synchronization Type' src='rfmxbt_txp_configure_burst_synchronization_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Burst Sync Type specifies the type of synchronization used for detecting the start of packet in the measurement. The default value is Preamble. None (0) Specifies that the measurement does not perform synchronization to detect the start of the packet. Preamble (1) Specifies that the measurement uses the preamble field bits to detect the start of the packet. Sync Word (2) Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the BD Address LAP property. |
| None (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| Preamble (1) | Specifies that the measurement uses the preamble field bits to detect the start of the packet. |
| Sync Word (2) | Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the BD Address LAP property. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_txp_fetch.html language=enus -->
## TOPIC 00063: RFmxBT TXP Fetch (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_txp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_txp_fetch.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT TXP Fetch (VI)

Owning Palette:

Fetch

Fetches the TXP measurement results.

#### RFmxBT TXP Fetch Powers

Fetches TXP measurement results. These results are valid for all packets.

[IMAGE alt='RFmxBT TXP Fetch Powers' src='rfmxbt_txp_fetch_powers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Average Power Mean returns the average power computed over the measurement interval. When you set the Direction Finding Mode property to Angle of Departure for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled property to True, it returns the mean of the average power results computed for each averaging count. This value is expressed in dBm. |
|  | Average Power Maximum returns the average power computed over the measurement interval. When you set the Direction Finding Mode property to Angle of Departure for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled property to True, it returns the maximum of the average power results computed for each averaging count. This value is expressed in dBm. |
|  | Average Power Minimum returns the average power computed over the measurement interval. When you set the Direction Finding Mode property to Angle of Departure for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the TXP Averaging Enabled property to True, it returns the minimum of the average power results computed for each averaging count. This value is expressed in dBm. |
|  | Peak to Average Power Ratio Maximum returns the peak to average power ratio computed over the measurement interval. When you set the Direction Finding Mode property to Angle of Departure for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computation. When you set the TXP Averaging Enabled property to True, it returns the maximum of the peak to average power ratio results computed for each averaging count. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT TXP Fetch LE CTE Reference Period Powers

Fetches the transmit power (TXP) measurement results over the reference period of the constant tone extension (CTE) portion for low energy (LE) packets when you set the [Direction Finding Mode](/csh?topicname=rfmxbtprop/attrb0002c.html) property to **Angle of Departure**.

[IMAGE alt='RFmxBT TXP Fetch LE CTE Reference Period Powers' src='rfmxbt_txp_fetch_le_cte_reference_period_powers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Reference Period Average Power Mean returns the average power computed over the reference period in the CTE portion of the LE packet. When you set the TXPï¿½Averagingï¿½Enabled property to True, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm. |
|  | Reference Period Peak Absolute Power Deviation Maximum returns the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. When you set the TXPï¿½Averagingï¿½Enabled property to True, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT TXP Fetch LE CTE Transmit Slot Powers

Fetches the transmit power (TXP) measurement results over each transmit slot of the constant tone extension (CTE) portion for low energy (LE) packets when you set the [Direction Finding Mode](/csh?topicname=rfmxbtprop/attrb0002c.html) property to **Angle of Departure**.

[IMAGE alt='RFmxBT TXP Fetch LE CTE Transmit Slot Powers' src='rfmxbt_txp_fetch_le_cte_transmit_slot_powers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and slot number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "slot0" "signal::sig1/slot0" "signal::sig1/result::r1/slot0" "result::r1/slot0" You can use the RFmxBT Build Slot String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Transmit Slot Average Power Mean returns the average power computed over each transmit slot in CTE portion of the LE packet. When you set the TXPï¿½Averagingï¿½Enabled property to True, it returns the mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm. |
|  | Transmit Slot Peak Absolute Power Deviation Maximum returns the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. When you set the TXPï¿½Averagingï¿½Enabled property to True, it returns the maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT TXP Fetch LE CTE Transmit Slot Powers (Array)

Fetches an array of transmit power (TXP) measurement results over all the transmit slots of constant tone extension (CTE) portion for low energy (LE) packets when you set the [Direction Finding Mode](/csh?topicname=rfmxbtprop/attrb0002c.html) property to **Angle of Departure**.

[IMAGE alt='RFmxBT TXP Fetch LE CTE Transmit Slot Powers (Array)' src='rfmxbt_txp_fetch_le_cte_transmit_slot_powers_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Transmit Slot Average Power Mean returns an array of average powers computed over every transmit slot in CTE portion of the LE packet. When you set the TXP Averaging Enabled property to True, it returns an array of mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm. |
|  | Transmit Slot Peak Absolute Power Deviation Maximum returns an array of peak absolute power deviations computed over every transmit slot in CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. When you set the TXPï¿½Averagingï¿½Enabled property to True, it returns an array of maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT TXP Fetch EDR Powers

Fetches TXP measurement results for enhanced data rate (EDR) packets.

[IMAGE alt='RFmxBT TXP Fetch EDR Powers' src='rfmxbt_txp_fetch_edr_powers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | EDR GFSK Average Power Mean returns the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled property to True, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm. |
|  | EDR DPSK Average Power Mean returns the average power of the DPSK portion of the EDR packet. When you set the TXP Averaging Enabled property to True, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm. |
|  | EDR DPSK GFSK Average Power Ratio Mean returns the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the TXP Averaging Enabled property to True, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxBT TXP Fetch Power Trace

Fetches the power versus time trace.

[IMAGE alt='RFmxBT TXP Fetch Power Trace' src='rfmxbt_txp_fetch_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Power returns the power versus time trace. x0 returns the start time. This value is expressed in seconds. dx returns the sample duration. This value is expressed in seconds. y returns the averaged power at each time instance. This value is expressed in dBm. |
|  | x0 returns the start time. This value is expressed in seconds. |
|  | dx returns the sample duration. This value is expressed in seconds. |
|  | y returns the averaged power at each time instance. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/rfmxbt_wait_for_measurement_complete.html language=enus -->
## TOPIC 00064: RFmxBT Wait for Measurement Complete (VI)

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/rfmxbt_wait_for_measurement_complete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/rfmxbt_wait_for_measurement_complete.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

RFmxBT Wait for Measurement Complete (VI)

Owning Palette:

Utility

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='RFmxBT Wait for Measurement Complete' src='rfmxbt_wait_for_measurement_complete.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxBT Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/txp_pal.html language=enus -->
## TOPIC 00065: TXP

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/txp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/txp_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

TXP

Owning Palette:

Configuration

Use the VIs on this palette to configure transmit power (TXP) measurements. You can also use the RFmxBT Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxBT TXP Configure Averaging | Configures averaging for the transmit power (TXP) measurement. |
| RFmxBT TXP Configure Burst Synchronization Type | Configures the type of synchronization used for detecting the start of the packet in the transmit power (TXP) measurement. |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-vi path=rfmxbtvi/utility_pal.html language=enus -->
## TOPIC 00066: Utility

- bundle_id: `rfmx-for-bluetooth-test-vi`
- source_path: `rfmxbtvi/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-vi/raw/resource/enus/rfmxbtvi/utility_pal.html
- document_id: `rfmx-for-bluetooth-test-vi`
- page_type: `leaf`
- content_type: ``

Utility

Owning Palette:

RFmx for Bluetooth® Test VIs

Use the VIs on this palette to configure utility VIs.

| Palette Object | Description |
| --- | --- |
| RFmxBT Commit | Commits settings to the hardware. Calling this VI is optional. RFmxBT commits settings to the hardware when you call the RFmxBT Initiate VI or any of the measurement Read VIs. |
| RFmxBT Reset to Default | Resets a signal to the default values. |
| RFmxBT Wait for Measurement Complete | Waits for the specified number for seconds for all the measurements to complete. |
| RFmxBT Check Measurement Status | Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
