# NI DOCUMENT BUNDLE: rfmx-wlan-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-wlan-vi start=1 end=90 -->
<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/advanced_pal.html language=enus -->
## TOPIC 00001: Advanced

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/advanced_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/advanced_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

Advanced

Owning Palette:

RFmx WLAN VIs

Use the VIs on this palette to use advanced features.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN Abort Measurements | Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxWLAN Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error. |
| RFmxWLAN Analyze2 | Performs the enabled measurements on the specified waveform(s). For I/Q measurements you must select the IQ instance. For spectral measurements you must select the Spectrum instance. |
| RFmxWLAN Create Signal Configuration | Creates a new instance of a signal. |
| RFmxWLAN Clone Signal Configuration | Creates a new instance of a signal by copying all the property values from an existing signal instance. |
| RFmxWLAN Delete Signal Configuration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxWLAN Get All Named Result Names | Returns all the named result names of the signal that you specify in the Selector String parameter. |
| RFmxWLAN Clear Named Result | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxWLAN Clear All Named Results | Clears all results for the signal that you specify in the Selector String parameter. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/build_string_pal.html language=enus -->
## TOPIC 00002: Build String

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/build_string_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/build_string_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

Build String

Owning Palette:

RFmx WLAN VIs

Use the VIs on this palette to create strings for configurations and results that require a selector string.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN Build Signal String | Creates a selector string. |
| RFmxWLAN Build Gate String | Creates the gate string to use as the selector string. |
| RFmxWLAN Build Offset String | Creates the offset string to use as the selector string. |
| RFmxWLAN Build User String | Creates the user string to use as the selector string. |
| RFmxWLAN Build Segment String | Creates a segment string. |
| RFmxWLAN Build Stream String | Creates the stream string. |
| RFmxWLAN Build Chain String | Creates a chain string. Use "segment<n>" as the selector string to read results from this VI. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/configuration_pal.html language=enus -->
## TOPIC 00003: Configuration

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/configuration_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

Configuration

Owning Palette:

RFmx WLAN VIs

Use the VIs on this palette to configure various parameters for RFmxWLAN measurements.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN Configure Selected Ports | Configures the instrument port to acquire a signal. Use the RFmxInstr Get Available Ports VI to get the valid port names. |
| RFmxWLAN Configure Frequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. On a MIMO session, use "segment<n>" as the selector string to configure this VI. |
| RFmxWLAN Configure Reference Level | Configures the reference level, which represents the maximum expected power of an RF input signal. On a MIMO session, use "port::<deviceName>/<channelNumber>" as the selector string to configure reference level for each port. |
| RFmxWLAN Configure External Attenuation | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. On a MIMO session, use port::<deviceName>/<channelNumber> as a selector string to configure external attenuation for each port. |
| RFmxWLAN Auto Level | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level. |
| RFmxWLAN Auto Detect Signal | Automatically detects the standard, channel bandwidth, and burst length of the input signal, and writes the Detected Standard, Detected Channel Bandwidth, and Detected Burst Length properties. You must configure the Reference Level property before calling this VI. If the peak power level of the input is unknown, you can call the RFmxWLAN Auto Level VI to configure the Reference Level property after you set the Standard and Channel Bandwidth properties to values corresponding to maximum expected channel bandwidth. |
| RFmxWLAN Configure Trigger | Configures the reference trigger to use to acquire the signal. |
| RFmxWLAN Send Software Edge Trigger | Sends a trigger to the device when you use the RFmxWLAN Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. |
| RFmxWLAN Configure Standard | Configures the IEEE 802.11 standard for the signal under analysis. |
| RFmxWLAN Configure Channel Bandwidth | Configures the channel bandwidth. |

| Subpalette | Description |
| --- | --- |
| MIMO | Use the VI on this palette to configure the WLAN MIMO measurement. You can use the RFmxWLAN Property Node to configure additional properties. |
| DSSSModAcc | Use the VIs on this palette to configure DSSSModAcc measurement. You can use the RFmxWLAN Property Node to configure additional properties. |
| OFDMModAcc | Use the VIs on this palette to configure OFDMModAcc measurement. You can use the RFmxWLAN Property Node to configure additional properties. |
| SEM | Use the VIs on this palette to configure SEM measurement. You can use the RFmxWLAN Property Node to configure additional properties. |
| TXP | Use the VIs on this palette to configure TXP measurement. You can use the RFmxWLAN Property Node to configure additional properties. |
| PowerRamp | Use the VIs on this palette to configure PowerRamp measurement. You can use the RFmxWLAN Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/dsssmodacc_pal.html language=enus -->
## TOPIC 00004: DSSSModAcc

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/dsssmodacc_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/dsssmodacc_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

DSSSModAcc

Owning Palette:

Configuration

Use the VIs on this palette to configure DSSSModAcc measurement. You can use the [RFmxWLAN Property Node](rfmxwlan_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN DSSSModAcc Configure Averaging | Configures averaging for the measurement. |
| RFmxWLAN DSSSModAcc Configure EVM Unit | Configures EVM unit for the measurement. |
| RFmxWLAN DSSSModAcc Configure Acquisition Length | Configures the Acquisition Length parameter and the Acquisition Length Mode parameter of the acquired waveform for the measurement. |
| RFmxWLAN DSSSModAcc Configure Measurement Length | Configures the measurement offset and the maximum measurement length for the DSSSModAcc measurement. |
| RFmxWLAN DSSSModAcc Configure Power Measurement Enabled | Configures whether power measurement is enabled for the DSSSModAcc measurement. |
| RFmxWLAN DSSSModAcc Configure Power Measurement Number of Custom Gates | Configures the number of custom gates for power measurement. |
| RFmxWLAN DSSSModAcc Configure Power Measurement Custom Gate (Array) | Configures the custom gate start and stop times for power measurement. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/fetch_pal.html language=enus -->
## TOPIC 00005: Fetch

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/fetch_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/fetch_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

Fetch

Owning Palette:

RFmx WLAN VIs

Use the VIs on this palette to fetch WLAN measurement results and traces. You can use the [RFmxWLAN Property Node](rfmxwlan_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN DSSSModAcc Fetch | Fetches the DSSSModAcc measurement results. |
| RFmxWLAN OFDMModAcc Fetch | Fetches the OFDMModAcc measurement results. |
| RFmxWLAN SEM Fetch | Fetches spectral emission mask (SEM) measurement results. |
| RFmxWLAN TXP Fetch | Fetches the TXP measurement results. |
| RFmxWLAN PowerRamp Fetch | Fetches the PowerRamp measurement results. |

| Subpalette | Description |
| --- | --- |
| Build String | Use the VIs on this palette to create strings for configurations and results that require a selector string. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/mimo_pal.html language=enus -->
## TOPIC 00006: MIMO

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/mimo_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/mimo_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

MIMO

Owning Palette:

Configuration

Use the VI on this palette to configure the WLAN MIMO measurement. You can use the [RFmxWLAN Property Node](rfmxwlan_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN Configure Number of Frequency Segments and Receive Chains | Configures the number of frequency segments and receive chains. |
| RFmxWLAN Configure Frequency (Array) | Configures a list of expected carrier frequencies of the RF signal to acquire. The signal analyzers tune to these frequencies based on the value you configure for the Num Freq Segments property. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/ofdmmodacc_pal.html language=enus -->
## TOPIC 00007: OFDMModAcc

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/ofdmmodacc_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/ofdmmodacc_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

OFDMModAcc

Owning Palette:

Configuration

Use the VIs on this palette to configure OFDMModAcc measurement. You can use the [RFmxWLAN Property Node](rfmxwlan_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN OFDMModAcc Configure Averaging | Configures averaging for the measurement. |
| RFmxWLAN OFDMModAcc Configure Measurement Mode | Configures the measurement mode for the OFDMModAcc measurement. |
| RFmxWLAN OFDMModAcc Configure EVM Unit | Configures EVM unit for the measurement. |
| RFmxWLAN OFDMModAcc Configure Acquisition Length | Configures the Acquisition Length parameter and the Acquisition Length Mode parameter of the acquired waveform for the measurement. |
| RFmxWLAN OFDMModAcc Configure Measurement Length | Configures the measurement offset and maximum measurement length for the OFDMModAcc EVM measurements. |
| RFmxWLAN OFDMModAcc Configure Frequency Error Estimation Method | Configures the frequency error estimation method for the OFDMModAcc measurement. |
| RFmxWLAN OFDMModAcc Configure Common Clock Source Enabled | Configures whether the transmitter uses the same reference clock signal for generating the RF carrier and for the symbol clock. |
| RFmxWLAN OFDMModAcc Configure Amplitude Tracking Enabled | Configures whether to enable pilot-based mean amplitude tracking per OFDM data symbol. |
| RFmxWLAN OFDMModAcc Configure Phase Tracking Enabled | Configures whether to enable pilot-based common phase error correction per OFDM data symbol. |
| RFmxWLAN OFDMModAcc Configure Symbol Clock Error Correction Enabled | Configures whether to enable symbol clock error correction. |
| RFmxWLAN OFDMModAcc Configure Channel Estimation Type | Configures the fields in the PPDU used to estimate the channel frequency response. |
| RFmxWLAN OFDMModAcc Configure Optimize Dynamic Range for EVM | Specifies whether to optimize analyzer’s dynamic range for the EVM measurement. Supported devices: PXIe-5646/5840/5841/5842. |
| RFmxWLAN OFDMModAcc Configure Noise Compensation Enabled | Configures whether to enable EVM noise compensation for the OFDMModAcc measurement. Supported devices: PXIe-5830/5831/5832/5646/5840/5841/5842. |
| RFmxWLAN OFDMModAcc Clear Noise Calibration Database | Clears the noise calibration database used for EVM noise compensation. |
| RFmxWLAN OFDMModAcc Validate Calibration Data | Indicates whether calibration data is valid for the configuration specified by the signal name in the Selector string parameter. |
| RFmxWLAN OFDMModAcc Configure Reference Waveform (1 Wfm) | Configures the reference waveform for a SISO measurement when you set the OFDMModAcc EVM Ref Data Symbols Mode property to Reference Waveform. |
| RFmxWLAN OFDMModAcc Configure Reference Waveform (N Wfms) | Configures the reference waveform array for a MIMO measurement when you set the OFDMModAcc EVM Ref Data Symbols Mode property to Reference Waveform. |
| RFmxWLAN OFDMModAcc Auto Level | Performs the user-configured ModAcc measurement on all initialized devices at multiple reference levels relative to the user-configured Reference Level property and configures the reference level corresponding to the lowest OFDMModAcc Results Chain RMS EVM Mean result on each device. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/powerramp_pal.html language=enus -->
## TOPIC 00008: PowerRamp

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/powerramp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/powerramp_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

PowerRamp

Owning Palette:

Configuration

Use the VIs on this palette to configure PowerRamp measurement. You can use the [RFmxWLAN Property Node](rfmxwlan_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN PowerRamp Configure Averaging | Configures averaging for the measurement. |
| RFmxWLAN PowerRamp Configure Acquisition Length | Configures the waveform acquisition length for the measurement. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_abort_measurements.html language=enus -->
## TOPIC 00009: RFmxWLAN Abort Measurements (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_abort_measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_abort_measurements.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Abort Measurements (VI)

Owning Palette:

Advanced

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxWLAN Initiate](rfmxwlan_initiate.html) VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='RFmxWLAN Abort Measurements' src='rfmxwlan_abort_measurements.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_analyze2.html language=enus -->
## TOPIC 00010: RFmxWLAN Analyze2 (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_analyze2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_analyze2.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Analyze2 (VI)

Owning Palette:

Advanced

Performs the enabled measurements on the specified waveform(s). For I/Q measurements you must select the IQ instance. For spectral measurements you must select the Spectrum instance.

#### RFmxWLAN Analyze (IQ, 1 Wfm)

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?topicname=rfmxinstrprop/attr27.html) property value is either **IQ** or **IQ or Spectral**.

When using the Analysis-Only mode in RFmxWLAN, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmx WLAN Commit VI. |
| --- | --- |

[IMAGE alt='RFmxWLAN Analyze (IQ 1 Wfm)' src='rfmxwlan_analyze_(iq_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 specifies the start time of the input y array. This value is expressed in seconds. dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input y array. This value is expressed in seconds. |
|  | dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN Analyze (Spectrum, 1 Wfm)

Performs the enabled measurements on the spectrum that you specify in the **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?topicname=rfmxinstrprop/attr27.html) property value is either **Spectral** or **IQ or Spectral**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmxWLAN Commit VI. |
| --- | --- |

[IMAGE alt='RFmxWLAN Analyze (Spectrum 1 Wfm)' src='rfmxwlan_analyze_(spectrum_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Spectrum specifies the data for a spectrum waveform including the start, delta, and actual values. x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx specifies the frequency interval between data points in the spectrum. y specifies the array of real-value power spectrum. |
|  | x0 specifies the start frequency of the spectrum. This value is expressed in Hz. |
|  | dx specifies the frequency interval between data points in the spectrum. |
|  | y specifies the array of real-value power spectrum. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN Analyze N Wfms (IQ)

Performs the enabled measurements on the I/Q complex waveform(s) that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?topicname=rfmxinstrprop/attr27.html) property value is either **IQ** or **IQ or Spectral**.

When using the Analysis-Only mode in RFmxWLAN, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmx WLAN Commit VI. |
| --- | --- |

[IMAGE alt='RFmxWLAN Analyze N Wfms (IQ)' src='rfmxwlan_analyze_n_wfms_(iq).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | IQ specifies the waveform array where each element contains data for a complex waveform including start, delta, and actual values. x0 specifies the start time of the input y array. This value is expressed in seconds. dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input y array. This value is expressed in seconds. |
|  | dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN Analyze N Wfms (Spectrum)

Performs the enabled measurements on the spectrum(s) that you specify in the **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?topicname=rfmxinstrprop/attr27.html) property value is either **Spectral** or **IQ or Spectral**.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmxWLAN Commit VI. |
| --- | --- |

[IMAGE alt='RFmxWLAN Analyze N Wfms (Spectrum)' src='rfmxwlan_analyze_n_wfms_(spectrum).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Spectrum specifies the waveform array where each element contains data for a spectrum waveform including start, delta, and actual values. x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx specifies the frequency interval between data points in the spectrum. y specifies the array of real-value power spectrum. |
|  | x0 specifies the start frequency of the spectrum. This value is expressed in Hz. |
|  | dx specifies the frequency interval between data points in the spectrum. |
|  | y specifies the array of real-value power spectrum. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_auto_detect_signal.html language=enus -->
## TOPIC 00011: RFmxWLAN Auto Detect Signal (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_auto_detect_signal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_auto_detect_signal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Auto Detect Signal (VI)

Owning Palette:

Configuration

Automatically detects the standard, channel bandwidth, and burst length of the input signal, and writes the [Detected Standard](/csh?topicname=rfmxwlanprop/attra00011.html), [Detected Channel Bandwidth](/csh?topicname=rfmxwlanprop/attra00012.html), and [Detected Burst Length](/csh?topicname=rfmxwlanprop/attra00013.html) properties.

You must configure the [Reference Level](/csh?topicname=rfmxwlanprop/attra00002.html) property before calling this VI. If the peak power level of the input is unknown, you can call the [RFmxWLAN Auto Level](../rfmxwlanvi/rfmxwlan_auto_level.html) VI to configure the Reference Level property after you set the [Standard](/csh?topicname=rfmxwlanprop/attra0000d.html) and [Channel Bandwidth](/csh?topicname=rfmxwlanprop/attra0000e.html) properties to values corresponding to maximum expected channel bandwidth.

[IMAGE alt='RFmxWLAN Auto Detect Signal' src='rfmxwlan_auto_detect_signal.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_auto_detect_signal_(analysisonly).html language=enus -->
## TOPIC 00012: RFmxWLAN Auto Detect Signal (AnalysisOnly) (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_auto_detect_signal_(analysisonly).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_auto_detect_signal_(analysisonly).html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Auto Detect Signal (AnalysisOnly) (VI)

Automatically detects the standard, channel bandwidth, and burst length on the I/Q complex waveform that you specify in **IQ** parameter, and writes the [Detected Standard](/csh?topicname=rfmxwlanprop/attra00011.html), [Detected Channel Bandwidth](/csh?topicname=rfmxwlanprop/attra00012.html), and [Detected Burst Length](/csh?topicname=rfmxwlanprop/attra00013.html) properties.

[IMAGE alt='RFmxWLAN Auto Detect Signal (AnalysisOnly)' src='rfmxwlan_auto_detect_signal_(analysisonly).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 specifies the start time of the input y array. This value is expressed in seconds. dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input y array. This value is expressed in seconds. |
|  | dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_auto_level.html language=enus -->
## TOPIC 00013: RFmxWLAN Auto Level (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_auto_level.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Auto Level (VI)

Owning Palette:

Configuration

Examines the input signal to calculate the peak power level and sets it as the value of the [Reference Level](/csh?topicname=rfmxwlanprop/attra00002.html) property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxWLAN Auto Level VI does the following:

1. Resets the mixer level, mixer level offset and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

You can also specify the starting reference level using the [Auto Level Initial Ref Level](/csh?topicname=rfmxwlanprop/attra00024.html) property.

When using NI-PXie 5663, NI-PXie 5665, or NI-PXie 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxWLAN Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this VI, thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='RFmxWLAN Auto Level' src='rfmxwlan_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Measurement Interval specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_build_chain_string.html language=enus -->
## TOPIC 00014: RFmxWLAN Build Chain String (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_build_chain_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_build_chain_string.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Build Chain String (VI)

Owning Palette:

Build String

Creates a chain string.

Use "segment<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN Build Chain String' src='rfmxwlan_build_chain_string.gif']

|  | Chain Number specifies the chain number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. You can also pass Selector String Out from the RFmxWLAN Build Segment String VI as an input to this VI. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxWLAN Build Segment String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_build_gate_string.html language=enus -->
## TOPIC 00015: RFmxWLAN Build Gate String (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_build_gate_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_build_gate_string.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Build Gate String (VI)

Owning Palette:

Build String

Creates the gate string to use as the selector string.

[IMAGE alt='RFmxWLAN Build Gate String' src='rfmxwlan_build_gate_string.gif']

|  | Gate Number specifies the gate number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_build_offset_string.html language=enus -->
## TOPIC 00016: RFmxWLAN Build Offset String (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_build_offset_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_build_offset_string.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Build Offset String (VI)

Owning Palette:

Build String

Creates the offset string to use as the selector string.

[IMAGE alt='RFmxWLAN Build Offset String' src='rfmxwlan_build_offset_string.gif']

|  | Offset Number specifies the offset number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_build_segment_string.html language=enus -->
## TOPIC 00017: RFmxWLAN Build Segment String (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_build_segment_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_build_segment_string.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Build Segment String (VI)

Owning Palette:

Build String

Creates a segment string.

[IMAGE alt='RFmxWLAN Build Segment String' src='rfmxwlan_build_segment_string.gif']

|  | Segment Number specifies the segment number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_build_signal_string.html language=enus -->
## TOPIC 00018: RFmxWLAN Build Signal String (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_build_signal_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_build_signal_string.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Build Signal String (VI)

Owning Palette:

Build String

Creates a selector string.

[IMAGE alt='RFmxWLAN Build Signal String' src='rfmxwlan_build_signal_string.gif']

|  | Result Name specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string). Example: "" "result::r1" "r1" |
| --- | --- |
|  | Signal Name specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Example: "" "signal::sig1" "sig1" |
|  | Selector String returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_build_stream_string.html language=enus -->
## TOPIC 00019: RFmxWLAN Build Stream String (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_build_stream_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_build_stream_string.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Build Stream String (VI)

Owning Palette:

Build String

Creates the stream string.

[IMAGE alt='RFmxWLAN Build Stream String' src='rfmxwlan_build_stream_string.gif']

|  | Stream Number specifies the stream number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_build_user_string.html language=enus -->
## TOPIC 00020: RFmxWLAN Build User String (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_build_user_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_build_user_string.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Build User String (VI)

Owning Palette:

Build String

Creates the user string to use as the selector string.

[IMAGE alt='RFmxWLAN Build User String' src='rfmxwlan_build_user_string.gif']

|  | User Number specifies the user number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_check_measurement_status.html language=enus -->
## TOPIC 00021: RFmxWLAN Check Measurement Status (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_check_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_check_measurement_status.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Check Measurement Status (VI)

Owning Palette:

Utility

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='RFmxWLAN Check Measurement Status' src='rfmxwlan_check_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | done? indicates whether the measurement is complete. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_clear_all_named_results.html language=enus -->
## TOPIC 00022: RFmxWLAN Clear All Named Results (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_clear_all_named_results.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_clear_all_named_results.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Clear All Named Results (VI)

Owning Palette:

Advanced

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxWLAN Clear All Named Results' src='rfmxwlan_clear_all_named_results.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_clear_named_result.html language=enus -->
## TOPIC 00023: RFmxWLAN Clear Named Result (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_clear_named_result.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_clear_named_result.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Clear Named Result (VI)

Owning Palette:

Advanced

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='RFmxWLAN Clear Named Result' src='rfmxwlan_clear_named_result.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_clone_signal_configuration.html language=enus -->
## TOPIC 00024: RFmxWLAN Clone Signal Configuration (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_clone_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_clone_signal_configuration.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Clone Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='RFmxWLAN Clone Signal Configuration' src='rfmxwlan_clone_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
|  | Old Signal Name specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_commit.html language=enus -->
## TOPIC 00025: RFmxWLAN Commit (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_commit.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Commit (VI)

Owning Palette:

Utility

Commits settings to the hardware. Calling this VI is optional. RFmxWLAN commits settings to the hardware when you call the [RFmxWLAN Initiate](rfmxwlan_initiate.html) VI.

[IMAGE alt='RFmxWLAN Commit' src='rfmxwlan_commit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_configure_channel_bandwidth.html language=enus -->
## TOPIC 00026: RFmxWLAN Configure Channel Bandwidth (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_configure_channel_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_configure_channel_bandwidth.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Configure Channel Bandwidth (VI)

Owning Palette:

Configuration

Configures the channel bandwidth.

[IMAGE alt='RFmxWLAN Configure Channel Bandwidth' src='rfmxwlan_configure_channel_bandwidth.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Channel Bandwidth specifies the channel spacing as defined in section 3.1 of IEEE Standard 802.11-2016 (pp. 130). This value is expressed in Hz. The default value is 20M. 5M (5e6) This bandwidth corresponds to IEEE Standard 802.11p. 10M (10e6) This bandwidth corresponds to IEEE Standard 802.11j and IEEE Standard 802.11p. 20M (20e6) This bandwidth corresponds to IEEE Standard 802.11a/g, IEEE Standard 802.11j, IEEE Standard 802.11p, IEEE Standard 802.11n, IEEE Standard 802.11ac, IEEE Standard 802.11ax, and IEEE Standard 802.11be. 40M (40e6) This bandwidth corresponds to IEEE Standard 802.11n, IEEE Standard 802.11ac, IEEE Standard 802.11ax, and IEEE Standard 802.11be. 80M (80e6) This bandwidth corresponds to IEEE Standard 802.11ac, IEEE Standard 802.11ax, and IEEE Standard 802.11be. 160M (160e6) This bandwidth corresponds to IEEE Standard 802.11ac, IEEE Standard 802.11ax, and IEEE Standard 802.11be. 320M (320e6) This bandwidth corresponds to IEEE Standard 802.11be. |
| 5M (5e6) | This bandwidth corresponds to IEEE Standard 802.11p. |
| 10M (10e6) | This bandwidth corresponds to IEEE Standard 802.11j and IEEE Standard 802.11p. |
| 20M (20e6) | This bandwidth corresponds to IEEE Standard 802.11a/g, IEEE Standard 802.11j, IEEE Standard 802.11p, IEEE Standard 802.11n, IEEE Standard 802.11ac, IEEE Standard 802.11ax, and IEEE Standard 802.11be. |
| 40M (40e6) | This bandwidth corresponds to IEEE Standard 802.11n, IEEE Standard 802.11ac, IEEE Standard 802.11ax, and IEEE Standard 802.11be. |
| 80M (80e6) | This bandwidth corresponds to IEEE Standard 802.11ac, IEEE Standard 802.11ax, and IEEE Standard 802.11be. |
| 160M (160e6) | This bandwidth corresponds to IEEE Standard 802.11ac, IEEE Standard 802.11ax, and IEEE Standard 802.11be. |
| 320M (320e6) | This bandwidth corresponds to IEEE Standard 802.11be. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_configure_external_attenuation.html language=enus -->
## TOPIC 00027: RFmxWLAN Configure External Attenuation (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_configure_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_configure_external_attenuation.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Configure External Attenuation (VI)

Owning Palette:

Configuration

Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. On a MIMO session, use port::<deviceName>/<channelNumber> as a selector string to configure external attenuation for each port.

[IMAGE alt='RFmxWLAN Configure External Attenuation' src='rfmxwlan_configure_external_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | External Attenuation specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name and port string. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). On a MIMO session, an empty string corresponds to all the initialized ports. Example: "" "signal::sig1" "port::myrfsa1/0" "signal::sig1/port::myrfsa1/0" You can use the RFmxWLAN Build Signal String VI to build the selector string. On a MIMO session, you can use the RFmxInstr Build Port String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_configure_frequency.html language=enus -->
## TOPIC 00028: RFmxWLAN Configure Frequency (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_configure_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_configure_frequency.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Configure Frequency (VI)

Owning Palette:

Configuration

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. On a MIMO session, use "segment<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxWLAN Configure Frequency' src='rfmxwlan_configure_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Center Frequency specifies the center frequency. This value is expressed in Hz. The default of this property is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" You can use the RFmxWLAN Build Chain String VI to build the selector string. If number of segments is greater than 1, you can use the RFmxWLAN Build Segment String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_configure_frequency_(array).html language=enus -->
## TOPIC 00029: RFmxWLAN Configure Frequency (Array) (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_configure_frequency_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_configure_frequency_(array).html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Configure Frequency (Array) (VI)

Owning Palette:

MIMO

Configures a list of expected carrier frequencies of the RF signal to acquire. The signal analyzers tune to these frequencies based on the value you configure for the [Num Freq Segments](/csh?topicname=rfmxwlanprop/attra0000f.html) property.

[IMAGE alt='RFmxWLAN Configure Frequency (Array)' src='rfmxwlan_configure_frequency_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Center Frequency specifies the list of center frequencies to be configured for the given number of frequency segments. This value is expressed in Hz. The default value is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_configure_number_of_frequency_segments_and_receive_chains.html language=enus -->
## TOPIC 00030: RFmxWLAN Configure Number of Frequency Segments and Receive Chains (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_configure_number_of_frequency_segments_and_receive_chains.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_configure_number_of_frequency_segments_and_receive_chains.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Configure Number of Frequency Segments and Receive Chains (VI)

Owning Palette:

MIMO

Configures the number of frequency segments and receive chains.

[IMAGE alt='RFmxWLAN Configure Number of Frequency Segments and Receive Chains' src='rfmxwlan_configure_number_of_frequency_segments_and_receive_chains.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Number of Frequency Segments specifies the number of frequency segments. The default value is 1. |
|  | Number of Receive Chains specifies the number of receive chains. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_configure_reference_level.html language=enus -->
## TOPIC 00031: RFmxWLAN Configure Reference Level (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_configure_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_configure_reference_level.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Configure Reference Level (VI)

Owning Palette:

Configuration

Configures the reference level, which represents the maximum expected power of an RF input signal. On a MIMO session, use "port::<deviceName>/<channelNumber>" as the selector string to configure reference level for each port.

[IMAGE alt='RFmxWLAN Configure Reference Level' src='rfmxwlan_configure_reference_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Reference Level specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this property is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name and port string. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). On a MIMO session, an empty string corresponds to all the initialized ports. Example: "" "signal::sig1" "port::myrfsa1/0" "signal::sig1/port::myrfsa1/0" You can use the RFmxWLAN Build Signal String VI to build the selector string. On a MIMO session, you can use the RFmxInstr Build Port String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_configure_selected_ports.html language=enus -->
## TOPIC 00032: RFmxWLAN Configure Selected Ports (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_configure_selected_ports.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_configure_selected_ports.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Configure Selected Ports (VI)

Owning Palette:

Configuration

Configures the instrument port to acquire a signal. Use the [RFmxInstr Get Available Ports](/csh?topicname=rfmxinstrvi/rfmxinstr_get_available_ports.html) VI to get the valid port names.

#### RFmxWLAN Configure Selected Ports (Single)

Configures the selected ports.

You do not need to use the **Selector String** parameter to configure this VI for the default signal instance if the session is initialized with [RFmxInstr Initialize NIRFSA](/csh?topicname=rfmxinstrvi/rfmxinstr_initialize_nirfsa.html) VI.

On a MIMO session, use "segment<*n*>/chain<*k*>" as the selector string. To perform a MIMO measurement, you must configure the [Selected Ports](/csh?topicname=rfmxwlanprop/attra00ffd.html) property for the configured number of segments and chains.

[IMAGE alt='RFmxWLAN Configure Selected Ports (Single)' src='rfmxwlan_configure_selected_ports_(single).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selected Ports specifies the instrument port to be configured to acquire a signal. On a MIMO session, this value specifies one of the initialized devices. Use "port::<deviceName>/<channelNumber>" as the format for the selected port. For PXIe-5830/5831/5832 devices on a MIMO session, the selected port includes the instrument port in the format "port::<deviceName>/<channelNumber>/<instrPort>". Example: port::myrfsa1/0/if1 You can use the RFmxInstr Build Port String VI to build the selected port. |
|  | Selector String specifies a selector string comprising of the signal name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN Configure Selected Ports (Multiple)

Configures the selected ports to each segment/chain based on the values you set in [Num Freq Segments](/csh?topicname=rfmxwlanprop/attra0000f.html) and [Num Rx Chains](/csh?topicname=rfmxwlanprop/attra00010.html) properties.

[IMAGE alt='RFmxWLAN Configure Selected Ports (Multiple)' src='rfmxwlan_configure_selected_ports_(multiple).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selected Ports specifies the list of MIMO ports to be configured. Use "port::<deviceName>/<channelNumber>" as the format for the selected port. For PXIe-5830/5831/5832 devices on a MIMO session, the selected port includes the instrument port in the format "port::<deviceName>/<channelNumber>/<instrPort>". Example: port::myrfsa1/0/if1 You can use the RFmxInstr Build Port String VI to build the selected port. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_configure_standard.html language=enus -->
## TOPIC 00033: RFmxWLAN Configure Standard (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_configure_standard.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_configure_standard.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Configure Standard (VI)

Owning Palette:

Configuration

Configures the IEEE 802.11 standard for the signal under analysis.

[IMAGE alt='RFmxWLAN Configure Standard' src='rfmxwlan_configure_standard.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Standard specifies the signal under analysis as defined under IEEE Standard 802.11. The default value is 802.11a/g. Note On a MIMO session, the supported standards are 802.11n, 802.11ac, 802.11ax, and 802.11be. 802.11a/g (0) Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11a-1999 and IEEE Standard 802.11g-2003. 802.11b (1) Corresponds to the DSSS based PPDU formats as defined in IEEE Standard 802.11b-1999. 802.11j (2) Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11j-2004. 802.11p (3) Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11p-2010. 802.11n (4) Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11n-2009. 802.11ac (5) Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11ac-2013. 802.11ax (6) Corresponds to the OFDM based PPDU formats as defined in IEEE Standard P802.11ax/D8.0. 802.11be (7) Corresponds to the OFDM based PPDU formats as defined in IEEE Standard P802.11be/D5.0.1. |
|  | Note On a MIMO session, the supported standards are 802.11n, 802.11ac, 802.11ax, and 802.11be. |
| 802.11a/g (0) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11a-1999 and IEEE Standard 802.11g-2003. |
| 802.11b (1) | Corresponds to the DSSS based PPDU formats as defined in IEEE Standard 802.11b-1999. |
| 802.11j (2) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11j-2004. |
| 802.11p (3) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11p-2010. |
| 802.11n (4) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11n-2009. |
| 802.11ac (5) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard 802.11ac-2013. |
| 802.11ax (6) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard P802.11ax/D8.0. |
| 802.11be (7) | Corresponds to the OFDM based PPDU formats as defined in IEEE Standard P802.11be/D5.0.1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_configure_trigger.html language=enus -->
## TOPIC 00034: RFmxWLAN Configure Trigger (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_configure_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_configure_trigger.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Configure Trigger (VI)

Owning Palette:

Configuration

Configures the reference trigger to use to acquire the signal.

#### RFmxWLAN Configure Digital Edge Trigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

On a MIMO session, this VI configures the digital edge trigger on the master port. By default, the [Selected Ports](/csh?topicname=rfmxwlanprop/attra00ffd.html) property is configured to "segment0/chain0" and is considered as the master port.

Spectral measurements are sometimes implemented with multiple acquisitions and therefore will require that digital triggers are sent for each acquisition. Multiple factors, including the desired span versus the realtime bandwidth of the hardware, affect the number of acquisitions. RFmx recommends repeating the generation until the measurement is completed in order to ensure that all the acquisitions are triggered.

[IMAGE alt='RFmxWLAN Configure Digital Edge Trigger' src='rfmxwlan_configure_digital_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Digital Edge Source specifies the source terminal for the digital edge trigger. This parameter is used only when you set the Trigger Type property to Digital Edge. The default value of this property is hardware dependent. To make a specific MIMO port as the trigger master, you must use the port specifier format "port::<device_name>/<source_terminal>". Example: "port::myrfsa1/PFI0" PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. PXIe_DStarB (PXIe_DStarB) The trigger is received on the PXIe DStar B trigger line. TimerEvent (TimerEvent) The trigger is received from the timer event. |
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
|  | Digital Edge specifies the active edge for the trigger. This parameter is used only when you set the Trigger Type property to Digital Edge. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. |
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN Configure IQ Power Edge Trigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.

On a MIMO session, this VI configures the IQ Power edge trigger on the master port. By default, the [Selected Ports](/csh?topicname=rfmxwlanprop/attra00ffd.html) property is configured to "segment0/chain0" and is considered as the master port.

To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

[IMAGE alt='RFmxWLAN Configure IQ Power Edge Trigger' src='rfmxwlan_configure_iq_power_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | IQ Power Edge Source specifies the channel from which the device monitors the trigger. This parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value is hardware dependent. To make a specific MIMO port as the trigger master, use the port specifier format "port::<deviceName>/<source_terminal>". Example: port::myrfsa1/0 |
|  | IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the Trigger Type property to IQ Power Edge. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
|  | IQ Power Edge Level specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative and is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The default value is hardware dependent. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the Trigger Type property to IQ Power Edge |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "port::myrfsa1/0" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | Minimum Quiet Time Mode specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Auto. Manual (0) The minimum quiet time used for triggering is the value of the Min Quiet Time parameter. Auto (1) The measurement computes the minimum quiet time used for triggering. |
| Manual (0) | The minimum quiet time used for triggering is the value of the Min Quiet Time parameter. |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |
|  | Minimum Quiet Time specifies the duration for which the signal must be quiet before the signal analyzer arms the I/Q Power Edge trigger. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default of this property is hardware dependent. This value is expressed in seconds. |
|  | IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. The IQ Power Edge Level parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value is Relative. Relative (0) The IQ Power Edge Level property is relative to the value of the Reference Level property. Absolute (1) The IQ Power Edge Level property specifies the absolute power. |
| Relative (0) | The IQ Power Edge Level property is relative to the value of the Reference Level property. |
| Absolute (1) | The IQ Power Edge Level property specifies the absolute power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN Configure Software Edge Trigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

[IMAGE alt='RFmxWLAN Configure Software Edge Trigger' src='rfmxwlan_configure_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN Disable Trigger

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='RFmxWLAN Disable Trigger' src='rfmxwlan_disable_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_create_signal_configuration.html language=enus -->
## TOPIC 00035: RFmxWLAN Create Signal Configuration (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_create_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_create_signal_configuration.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Create Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal.

[IMAGE alt='RFmxWLAN Create Signal Configuration' src='rfmxwlan_create_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_delete_signal_configuration.html language=enus -->
## TOPIC 00036: RFmxWLAN Delete Signal Configuration (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_delete_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_delete_signal_configuration.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Delete Signal Configuration (VI)

Owning Palette:

Advanced

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='RFmxWLAN Delete Signal Configuration' src='rfmxwlan_delete_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_dsssmodacc_configure_acquisition_length.html language=enus -->
## TOPIC 00037: RFmxWLAN DSSSModAcc Configure Acquisition Length (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_dsssmodacc_configure_acquisition_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_dsssmodacc_configure_acquisition_length.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN DSSSModAcc Configure Acquisition Length (VI)

Owning Palette:

DSSSModAcc

Configures the **Acquisition Length** parameter and the **Acquisition Length Mode** parameter of the acquired waveform for the measurement.

[IMAGE alt='RFmxWLAN DSSSModAcc Configure Acquisition Length' src='rfmxwlan_dsssmodacc_configure_acquisition_length.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Acquisition Length Mode specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties. The default value is Auto. Manual (0) Uses the acquisition length specified by the Acquisition Length parameter. Auto (1) Computes the acquisition length based on the DSSSModAcc Meas Offset property and the DSSSModAcc Max Meas Length property. |
| Manual (0) | Uses the acquisition length specified by the Acquisition Length parameter. |
| Auto (1) | Computes the acquisition length based on the DSSSModAcc Meas Offset property and the DSSSModAcc Max Meas Length property. |
|  | Acquisition Length specifies the length of the waveform to be acquired for the DSSSModAcc measurement when you set the Acquisition Length Mode parameter to Manual. This value is expressed in seconds. The default value is 0.001. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_dsssmodacc_configure_averaging.html language=enus -->
## TOPIC 00038: RFmxWLAN DSSSModAcc Configure Averaging (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_dsssmodacc_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_dsssmodacc_configure_averaging.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN DSSSModAcc Configure Averaging (VI)

Owning Palette:

DSSSModAcc

Configures averaging for the measurement.

[IMAGE alt='RFmxWLAN DSSSModAcc Configure Averaging' src='rfmxwlan_dsssmodacc_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for DSSSModAcc measurements. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_dsssmodacc_configure_evm_unit.html language=enus -->
## TOPIC 00039: RFmxWLAN DSSSModAcc Configure EVM Unit (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_dsssmodacc_configure_evm_unit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_dsssmodacc_configure_evm_unit.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN DSSSModAcc Configure EVM Unit (VI)

Owning Palette:

DSSSModAcc

Configures EVM unit for the measurement.

[IMAGE alt='RFmxWLAN DSSSModAcc Configure EVM Unit' src='rfmxwlan_dsssmodacc_configure_evm_unit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | EVM Unit specifies the unit for the EVM results. The default value is Percentage. dB (0) EVM results are returned in dB. Percentage (1) EVM results are returned as a percentage. |
| dB (0) | EVM results are returned in dB. |
| Percentage (1) | EVM results are returned as a percentage. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_dsssmodacc_configure_measurement_length.html language=enus -->
## TOPIC 00040: RFmxWLAN DSSSModAcc Configure Measurement Length (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_dsssmodacc_configure_measurement_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_dsssmodacc_configure_measurement_length.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN DSSSModAcc Configure Measurement Length (VI)

Owning Palette:

DSSSModAcc

Configures the measurement offset and the maximum measurement length for the DSSSModAcc measurement.

[IMAGE alt='RFmxWLAN DSSSModAcc Configure Measurement Length' src='rfmxwlan_dsssmodacc_configure_measurement_length.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Measurement Offset specifies the number of data chips to be ignored from the start of the data field for the EVM computation. This value is expressed in chips. The default value is 0. |
|  | Maximum Measurement Length specifies the maximum number of data chips that the measurement uses to compute EVM. This value is expressed in chips. The default value is 1000. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_dsssmodacc_configure_power_measurement_custom_gate_(array).html language=enus -->
## TOPIC 00041: RFmxWLAN DSSSModAcc Configure Power Measurement Custom Gate (Array) (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_dsssmodacc_configure_power_measurement_custom_gate_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_dsssmodacc_configure_power_measurement_custom_gate_(array).html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN DSSSModAcc Configure Power Measurement Custom Gate (Array) (VI)

Owning Palette:

DSSSModAcc

Configures the custom gate start and stop times for power measurement.

[IMAGE alt='RFmxWLAN DSSSModAcc Configure Power Measurement Custom Gate (Array)' src='rfmxwlan_dsssmodacc_configure_power_measurement_custom_gate_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Start Time specifies the array of start time of the custom power gates. This value is expressed in seconds. A value of 0 indicates that the start time is the start of the PPDU. The default value is an empty array. |
|  | Stop Time specifies the array of stop time of the custom power gates. This value is expressed in seconds. The default value is an empty array. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_dsssmodacc_configure_power_measurement_enabled.html language=enus -->
## TOPIC 00042: RFmxWLAN DSSSModAcc Configure Power Measurement Enabled (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_dsssmodacc_configure_power_measurement_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_dsssmodacc_configure_power_measurement_enabled.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN DSSSModAcc Configure Power Measurement Enabled (VI)

Owning Palette:

DSSSModAcc

Configures whether power measurement is enabled for the DSSSModAcc measurement.

[IMAGE alt='RFmxWLAN DSSSModAcc Configure Power Measurement Enabled' src='rfmxwlan_dsssmodacc_configure_power_measurement_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Power Measurement Enabled specifies if power measurement is performed. This parameter computes power of various fields in the PPDU. Additionally, this measurement computes power over the custom gates that you can configure using the DSSSModAcc Pwr Num Custom Gates, the DSSSModAcc Pwr Custom Gate Start Time and the DSSSModAcc Pwr Custom Gate Stop Time properties. The default value is False. False (0) Disables power measurement. True (1) Enables power measurement. |
| False (0) | Disables power measurement. |
| True (1) | Enables power measurement. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_dsssmodacc_configure_power_measurement_number_of_custom_gates.html language=enus -->
## TOPIC 00043: RFmxWLAN DSSSModAcc Configure Power Measurement Number of Custom Gates (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_dsssmodacc_configure_power_measurement_number_of_custom_gates.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_dsssmodacc_configure_power_measurement_number_of_custom_gates.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN DSSSModAcc Configure Power Measurement Number of Custom Gates (VI)

Owning Palette:

DSSSModAcc

Configures the number of custom gates for power measurement.

[IMAGE alt='RFmxWLAN DSSSModAcc Configure Power Measurement Number of Custom Gates' src='rfmxwlan_dsssmodacc_configure_power_measurement_number_of_custom_gates.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Number of Gates specifies the number of custom gates used for power measurement. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_dsssmodacc_fetch.html language=enus -->
## TOPIC 00044: RFmxWLAN DSSSModAcc Fetch (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_dsssmodacc_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_dsssmodacc_fetch.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN DSSSModAcc Fetch (VI)

Owning Palette:

Fetch

Fetches the DSSSModAcc measurement results.

#### RFmxWLAN DSSSModAcc Fetch EVM

Fetches the EVM results for the DSSSModAcc measurement.

[IMAGE alt='RFmxWLAN DSSSModAcc Fetch EVM' src='rfmxwlan_dsssmodacc_fetch_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | RMS EVM Mean returns the RMS EVM results of the burst. When you set the DSSSModAcc Averaging Enabled property to True, this result returns the mean of the RMS EVM computed for each averaging count. When you set the DSSSModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the DSSSModAcc EVM Unit property to dB, the measurement returns this result in dB. |
|  | Peak EVM (802.11-2016) Maximum returns the peak EVM results of the burst. When you set the DSSSModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the DSSSModAcc EVM Unit property to dB, the measurement returns this result in dB. This measurement is performed in accordance with section 16.3.7.9 of IEEE Standard 802.11-2016. When you set the DSSSModAcc Averaging Enabled property to True, this result returns the maximum of the peak EVM computed for each averaging count. |
|  | Peak EVM (802.11-2007) Maximum returns the peak EVM results of the burst. When you set the DSSSModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the DSSSModAcc EVM Unit property to dB, the measurement returns this result in dB. This measurement is performed in accordance with section 18.4.7.8 of IEEE Standard 802.11-2007. When you set the DSSSModAcc Averaging Enabled property to True, this result returns the maximum of the peak EVM computed for each averaging count. |
|  | Frequency Error Mean returns the carrier frequency error of the transmitter. This value is expressed in Hz. When you set the DSSSModAcc Averaging Enabled property to True, this result returns the mean of the carrier frequency error results computed for each averaging count. |
|  | Peak EVM (802.11-1999) Maximum returns the peak EVM results of the burst. When you set the DSSSModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the DSSSModAcc EVM Unit property to dB, the measurement returns this result in dB. This measurement is performed in accordance with section 18.4.7.8 of IEEE Standard 802.11b-1999. When you set the DSSSModAcc Averaging Enabled property to True, this result returns the maximum of the peak EVM computed for each averaging count. |
|  | Chip Clock Error Mean returns the chip clock error result of the transmitter. This value is expressed in parts per million (ppm). When you set the DSSSModAcc Averaging Enabled property to True, this result returns the mean of the chip clock error computed for each averaging count. |
|  | Number of Chips Used returns the number of chips used for the DSSSModAcc measurement. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN DSSSModAcc Fetch IQ Impairments

Fetches the I/Q Impairment results for the DSSSModAcc measurement.

[IMAGE alt='RFmxWLAN DSSSModAcc Fetch IQ Impairments' src='rfmxwlan_dsssmodacc_fetch_iq_impairments.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | I/Q Origin Offset Mean returns the I/Q origin offset. This value is expressed in dB. I/Q origin offset is the ratio of the mean value of the signal to the RMS value of the signal. When you set the DSSSModAcc Averaging Enabled property to True, this parameter returns the mean of the I/Q origin offset results computed for each averaging count. |
|  | I/Q Gain Imbalance Mean returns the I/Q gain imbalance results. This value is expressed in dB. I/Q gain imbalance is the ratio of the mean amplitude of the in-phase (I) signal to the mean amplitude of the quadrature-phase (Q) signal. When you set the DSSSModAcc Averaging Enabled property to True, this parameter returns the mean of the I/Q gain imbalance results computed for each averaging count. |
|  | I/Q Quadrature Error Mean returns the I/Q quadrature error. This value is expressed in degrees. Quadrature error is the deviation in angle from 90 degrees between the in-phase (I) and quadrature-phase (Q) signals. When the DSSSModAcc Averaging Enabled property is set to True, this parameter returns the mean of the I/Q quadrature error results computed for each averaging count. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN DSSSModAcc Fetch PPDU Information

Fetches the PPDU information.

[IMAGE alt='RFmxWLAN DSSSModAcc Fetch PPDU Information' src='rfmxwlan_dsssmodacc_fetch_ppdu_information.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Data Modulation Format returns the data modulation format results of the analyzed waveform. DSSS 1 Mbps (0) Indicates that the modulation format is DSSS and the data rate is 1 Mbps. DSSS 2 Mbps (1) Indicates that the modulation format is DSSS and the data rate is 2 Mbps. CCK 5.5 Mbps (2) Indicates that the modulation format is CCK and the data rate is 5.5 Mbps. CCK 11 Mbps (3) Indicates that the modulation format is CCK and the data rate is 11 Mbps. PBCC 5.5 Mbps (4) Indicates that the modulation format is PBCC and the data rate is 5.5 Mbps. PBCC 11 Mbps (5) Indicates that the modulation format is PBCC and the data rate is 11 Mbps. PBCC 22 Mbps (6) Indicates that the modulation format is PBCC and the data rate is 22 Mbps. PBCC 33 Mbps (7) Indicates that the modulation format is PBCC and the data rate is 33 Mbps. |
| DSSS 1 Mbps (0) | Indicates that the modulation format is DSSS and the data rate is 1 Mbps. |
| DSSS 2 Mbps (1) | Indicates that the modulation format is DSSS and the data rate is 2 Mbps. |
| CCK 5.5 Mbps (2) | Indicates that the modulation format is CCK and the data rate is 5.5 Mbps. |
| CCK 11 Mbps (3) | Indicates that the modulation format is CCK and the data rate is 11 Mbps. |
| PBCC 5.5 Mbps (4) | Indicates that the modulation format is PBCC and the data rate is 5.5 Mbps. |
| PBCC 11 Mbps (5) | Indicates that the modulation format is PBCC and the data rate is 11 Mbps. |
| PBCC 22 Mbps (6) | Indicates that the modulation format is PBCC and the data rate is 22 Mbps. |
| PBCC 33 Mbps (7) | Indicates that the modulation format is PBCC and the data rate is 33 Mbps. |
|  | Payload length returns the payload length of the acquired burst. This value is expressed in bytes. |
|  | Preamble Type returns the detected preamble type. Long (0) Indicates that the PPDU has a long PHY preamble and header. Short (1) Indicates that the PPDU has a short PHY preamble and header. |
| Long (0) | Indicates that the PPDU has a long PHY preamble and header. |
| Short (1) | Indicates that the PPDU has a short PHY preamble and header. |
|  | Header CRC Status returns whether the header CRC is successfully passed, as defined under section 16.2.3.7 of IEEE Standard 802.11 2016. Fail (0) Indicates that the header CRC failed. Pass (1) Indicates that the header CRC passed. |
| Fail (0) | Indicates that the header CRC failed. |
| Pass (1) | Indicates that the header CRC passed. |
|  | Locked Clocks Bit returns the value of the locked clocks bit in the Long PHY SERVICE field. A value of 1 indicates that the transmit frequency and the symbol clock are derived from the same oscillator. A value of 0 indicates that the transmit frequency and the symbol clock are derived from independent oscillators. |
|  | PSDU CRC Status returns whether the PLCP service data unit (PSDU) cyclic redundancy check (CRC) has successfully passed. Fail (0) Indicates that the PSDU CRC failed. Pass (1) Indicates that the PSDU CRC passed. |
| Fail (0) | Indicates that the PSDU CRC failed. |
| Pass (1) | Indicates that the PSDU CRC passed. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN DSSSModAcc Fetch Average Powers

Fetches the average power of various fields in the PPDU.

[IMAGE alt='RFmxWLAN DSSSModAcc Fetch Average Powers' src='rfmxwlan_dsssmodacc_fetch_average_powers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Preamble Average Power Mean returns the average power of the preamble field of the PPDU. When you set the DSSSModAcc Averaging Enabled property to True, this result returns the mean of the average preamble field power computed for each averaging count. This value is expressed in dBm. |
|  | Header Average Power Mean returns the average power of the header field of the PPDU. When you set the DSSSModAcc Averaging Enabled property to True, this result returns the mean of the average header field power computed for each averaging count. This value is expressed in dBm. |
|  | Data Average Power Mean returns the average power of the data field of the PPDU. When you set the DSSSModAcc Averaging Enabled property to True, this property returns the mean of the data field average power results computed for each averaging count. This value is expressed in dBm. |
|  | PPDU Average Power Mean returns the average power of the PPDU. When you set the DSSSModAcc Averaging Enabled property to True, this parameter returns the mean of the average PPDU power results computed for each averaging count. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN DSSSModAcc Fetch Peak Powers

Fetches the peak power of various fields in the PPDU.

[IMAGE alt='RFmxWLAN DSSSModAcc Fetch Peak Powers' src='rfmxwlan_dsssmodacc_fetch_peak_powers.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Preamble Peak Power Maximum returns the peak power of the preamble field of the PPDU. When you set the DSSSModAcc Averaging Enabled property to True, this result returns the maximum of the peak preamble field power results computed for each averaging count. This value is expressed in dBm. |
|  | Header Peak Power Maximum returns the peak power of the header field of the PPDU. When you set the DSSSModAcc Averaging Enabled property to True, this result returns the maximum of the peak header field power results computed for each averaging count. This value is expressed in dBm. |
|  | Data Peak Power Maximum returns the peak power of the data field of the PPDU. When you set the DSSSModAcc Averaging Enabled property to True, this result returns the maximum of the peak data field power results computed for each averaging count. This value is expressed in dBm. |
|  | PPDU Peak Power Maximum returns the peak power of the PPDU. When you set the DSSSModAcc Averaging Enabled property to True, this parameter returns the maximum of the peak PPDU power results computed for each averaging count. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN DSSSModAcc Fetch Custom Gate Powers (Array)

Fetches the average and peak power of custom gates.

[IMAGE alt='RFmxWLAN DSSSModAcc Fetch Custom Gate Powers (Array)' src='rfmxwlan_dsssmodacc_fetch_custom_gate_powers_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Average Power Mean returns an array of average powers of the custom gates. This value is expressed in dBm. When you set the DSSSModAcc Averaging Enabled property to True, this parameter returns an array of the mean of the average custom gate power results computed for each averaging count. |
|  | Peak Power Maximum returns an array of peak powers of the custom gates. This value is expressed in dBm. When you set the DSSSModAcc Averaging Enabled property to True, this parameter returns an array of the maximum of the peak custom gate power results computed for each averaging count. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN DSSSModAcc Fetch Constellation Trace

Fetches the constellation trace for the data field.

[IMAGE alt='RFmxWLAN DSSSModAcc Fetch Constellation Trace' src='rfmxwlan_dsssmodacc_fetch_constellation_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Constellation returns the constellation of the received symbols. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN DSSSModAcc Fetch EVM per Chip Mean Trace

Fetches the EVM per chip in the data field. When you set the [DSSSModAcc Averaging Enabled](/csh?topicname=rfmxwlanprop/attra0302f.html) property to **True**, this VI returns the mean of the EVM per chip computed for each averaging count.

[IMAGE alt='RFmxWLAN DSSSModAcc Fetch EVM per Chip Mean Trace' src='rfmxwlan_dsssmodacc_fetch_evm_per_chip_mean_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | EVM Per Chip Mean returns the EVM per chip trace for the data field. x0 returns the index of the first chip. dx returns the trace increment interval in number of chips. This value is always equal to 1. y returns an array of EVM per chip. When you set the DSSSModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the DSSSModAcc EVM Unit property to dB, the measurement returns this result in dB. |
|  | x0 returns the index of the first chip. |
|  | dx returns the trace increment interval in number of chips. This value is always equal to 1. |
|  | y returns an array of EVM per chip. When you set the DSSSModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the DSSSModAcc EVM Unit property to dB, the measurement returns this result in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN DSSSModAcc Fetch Decoded Header Bits Trace

Fetches the decoded Header bits.

[IMAGE alt='RFmxWLAN DSSSModAcc Fetch Decoded Header Bits Trace' src='rfmxwlan_dsssmodacc_fetch_decoded_header_bits_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Decoded Header Bits returns an array of bits in the Header field. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN DSSSModAcc Fetch Decoded PSDU Bits Trace

Fetches the decoded PLCP service data unit (PSDU) bits.

[IMAGE alt='RFmxWLAN DSSSModAcc Fetch Decoded PSDU Bits Trace' src='rfmxwlan_dsssmodacc_fetch_decoded_psdu_bits_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Decoded PSDU Bits returns an array of PSDU bits obtained after demodulation and decoding. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_get_all_named_result_names.html language=enus -->
## TOPIC 00045: RFmxWLAN Get All Named Result Names (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_get_all_named_result_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_get_all_named_result_names.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Get All Named Result Names (VI)

Owning Palette:

Advanced

Returns all the named result names of the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxWLAN Get All Named Result Names' src='rfmxwlan_get_all_named_result_names.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Result Names returns an array of result names. |
|  | Default Result Exists? indicates whether the default result exists. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_initiate.html language=enus -->
## TOPIC 00046: RFmxWLAN Initiate (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_initiate.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Initiate (VI)

Owning Palette:

RFmx WLAN VIs

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the [RFmxWLAN Wait for Measurement Complete](rfmxwlan_wait_for_measurement_complete.html) VI or [RFmxWLAN Check Measurement Status](rfmxwlan_check_measurement_status.html) VI.

[IMAGE alt='RFmxWLAN Initiate' src='rfmxwlan_initiate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" |
|  | Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_auto_level.html language=enus -->
## TOPIC 00047: RFmxWLAN OFDMModAcc Auto Level (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_auto_level.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Auto Level (VI)

Owning Palette:

OFDMModAcc

Performs the user-configured ModAcc measurement on all initialized devices at multiple reference levels relative to the user-configured [Reference Level](/csh?topicname=rfmxwlanprop/attra00002.html) property and configures the reference level corresponding to the lowest [OFDMModAcc Results Chain RMS EVM Mean](/csh?topicname=rfmxwlanprop/attra04071.html) result on each device.

This VI only measures at the reference levels that do not result in an ADC or OSP overflow when you set the [OFDMModAcc Auto Level Allow Overflow](/csh?topicname=rfmxwlanprop/attra040b1.html) property to **False**. If you set the OFDMModAcc Auto Level Allow Overflow property to **True**, this VI measures at a few reference levels beyond the overflow.

After calling this VI, you need to perform the ModAcc measurement.

|  | Note Calling this VI will also set the Reference Level Headroom property to 0. |
| --- | --- |

This VI expects:

- A valid OFDMModAcc measurement configuration
- Reference Level property set to peak power of the signal
- Repetitive signals at the analyzer's input along with trigger settings that measure the same portion of the waveform every time the measurement is performed
- No other measurements are running in parallel

Auto level needs to be performed again if the input signal or RFmx configuration changes.

For repeatable results, you must make sure that the OFDMModAcc measurement is repeatable.

This VI measures EVM at reference levels starting at an integer at least 1 dB above the value you configure for the Reference Level property, extending upto 12 dB lower when you set the OFDMModAcc Auto Level Allow Overflow property to **False**, and up to 17 dB lower when you set the OFDMModAcc Auto Level Allow Overflow property to **True** with a step size of 0.5 dB.

When you use this VI with the [OFDMModAcc Noise Comp Enabled](/csh?topicname=rfmxwlanprop/attra04067.html) property set to **True**, you need to make sure that valid noise calibration data is available for the above measurements.

[IMAGE alt='RFmxWLAN OFDMModAcc Auto Level' src='rfmxwlan_ofdmmodacc_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout (s) specifies the timeout for fetching the EVM results. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_clear_noise_calibration_database.html language=enus -->
## TOPIC 00048: RFmxWLAN OFDMModAcc Clear Noise Calibration Database (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_clear_noise_calibration_database.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_clear_noise_calibration_database.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Clear Noise Calibration Database (VI)

Owning Palette:

OFDMModAcc

Clears the noise calibration database used for EVM noise compensation.

[IMAGE alt='RFmxWLAN OFDMModAcc Clear Noise Calibration Database' src='rfmxwlan_ofdmmodacc_clear_noise_calibration_database.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_acquisition_length.html language=enus -->
## TOPIC 00049: RFmxWLAN OFDMModAcc Configure Acquisition Length (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_acquisition_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_acquisition_length.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Acquisition Length (VI)

Owning Palette:

OFDMModAcc

Configures the **Acquisition Length** parameter and the **Acquisition Length Mode** parameter of the acquired waveform for the measurement.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Acquisition Length' src='rfmxwlan_ofdmmodacc_configure_acquisition_length.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Acquisition Length Mode specifies whether the measurement automatically computes the acquisition length of the waveform based on other OFDMModAcc properties. The default value is Auto. Manual (0) Uses the acquisition length specified by the OFDMModAcc Acquisition Length property. Auto (1) Computes the acquisition length based on the OFDMModAcc Meas Offset and the OFDMModAcc Max Meas Length properties. |
| Manual (0) | Uses the acquisition length specified by the OFDMModAcc Acquisition Length property. |
| Auto (1) | Computes the acquisition length based on the OFDMModAcc Meas Offset and the OFDMModAcc Max Meas Length properties. |
|  | Acquisition Length specifies the length of the waveform to be acquired for the OFDMModAcc measurement when you set the Acquisition Length Mode parameter to Manual. This value is expressed in seconds. The default value is 0.001. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_amplitude_tracking_enabled.html language=enus -->
## TOPIC 00050: RFmxWLAN OFDMModAcc Configure Amplitude Tracking Enabled (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_amplitude_tracking_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_amplitude_tracking_enabled.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Amplitude Tracking Enabled (VI)

Owning Palette:

OFDMModAcc

Configures whether to enable pilot-based mean amplitude tracking per OFDM data symbol.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Amplitude Tracking Enabled' src='rfmxwlan_ofdmmodacc_configure_amplitude_tracking_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Amplitude Tracking Enabled specifies whether to enable pilot-based mean amplitude tracking per OFDM data symbol. Amplitude tracking is useful if the mean amplitude of the OFDM symbols in a PPDU varies over time. However, enabling tracking may degrade EVM because of attempts to track random amplitude distortions caused by additive noise and other distortions. The default value is False. False (0) Amplitude tracking is disabled. True (1) Amplitude tracking is enabled. |
| False (0) | Amplitude tracking is disabled. |
| True (1) | Amplitude tracking is enabled. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_averaging.html language=enus -->
## TOPIC 00051: RFmxWLAN OFDMModAcc Configure Averaging (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_averaging.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Averaging (VI)

Owning Palette:

OFDMModAcc

Configures averaging for the measurement.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Averaging' src='rfmxwlan_ofdmmodacc_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for OFDMModAcc measurements. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the results are averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the results are averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_channel_estimation_type.html language=enus -->
## TOPIC 00052: RFmxWLAN OFDMModAcc Configure Channel Estimation Type (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_channel_estimation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_channel_estimation_type.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Channel Estimation Type (VI)

Owning Palette:

OFDMModAcc

Configures the fields in the PPDU used to estimate the channel frequency response.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Channel Estimation Type' src='rfmxwlan_ofdmmodacc_configure_channel_estimation_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Channel Estimation Type specifies the fields in the PPDU used to estimate the channel frequency response. The default value is Reference. Reference (0) The channel is estimated using long training fields (LTFs) in the preamble and the most recently received midamble, if present. Reference and Data (1) The channel is estimated using long training fields (LTFs) in the preamble, the midamble (if present), and the data field. |
| Reference (0) | The channel is estimated using long training fields (LTFs) in the preamble and the most recently received midamble, if present. |
| Reference and Data (1) | The channel is estimated using long training fields (LTFs) in the preamble, the midamble (if present), and the data field. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_common_clock_source_enabled.html language=enus -->
## TOPIC 00053: RFmxWLAN OFDMModAcc Configure Common Clock Source Enabled (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_common_clock_source_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_common_clock_source_enabled.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Common Clock Source Enabled (VI)

Owning Palette:

OFDMModAcc

Configures whether the transmitter uses the same reference clock signal for generating the RF carrier and for the symbol clock.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Common Clock Source Enabled' src='rfmxwlan_ofdmmodacc_configure_common_clock_source_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Common Clock Source Enabled specifies if the transmitter uses the same reference clock signal for generating the RF carrier and the symbol clock. The default value is True. False (0) Specifies that the transmitter does not use a common reference clock. The OFDMModAcc measurement computes the symbol clock error and carrier frequency error independently. True (1) Specifies that the transmitter uses a common reference clock. The OFDMModAcc measurement derives the symbol clock error from the configured center frequency and carrier frequency error. |
| False (0) | Specifies that the transmitter does not use a common reference clock. The OFDMModAcc measurement computes the symbol clock error and carrier frequency error independently. |
| True (1) | Specifies that the transmitter uses a common reference clock. The OFDMModAcc measurement derives the symbol clock error from the configured center frequency and carrier frequency error. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_evm_unit.html language=enus -->
## TOPIC 00054: RFmxWLAN OFDMModAcc Configure EVM Unit (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_evm_unit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_evm_unit.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure EVM Unit (VI)

Owning Palette:

OFDMModAcc

Configures EVM unit for the measurement.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure EVM Unit' src='rfmxwlan_ofdmmodacc_configure_evm_unit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | EVM Unit specifies the unit for the EVM results. The default value is dB. dB (0) EVM results are returned in dB. Percentage (1) EVM results are returned as a percentage. |
| dB (0) | EVM results are returned in dB. |
| Percentage (1) | EVM results are returned as a percentage. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_frequency_error_estimation_method.html language=enus -->
## TOPIC 00055: RFmxWLAN OFDMModAcc Configure Frequency Error Estimation Method (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_frequency_error_estimation_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_frequency_error_estimation_method.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Frequency Error Estimation Method (VI)

Owning Palette:

OFDMModAcc

Configures the frequency error estimation method for the OFDMModAcc measurement.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Frequency Error Estimation Method' src='rfmxwlan_ofdmmodacc_configure_frequency_error_estimation_method.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Frequency Error Estimation Method specifies the PPDU fields that the measurement uses to estimate the carrier frequency error in the acquired signal. The default value is Preamble and Pilots. Disabled (0) Carrier frequency error is not computed and the corresponding result is returned as NaN. Initial Preamble (1) Initial short and long training fields in the PPDU are used. Preamble (2) Initial short and long training fields along with the SIGnal fields are used. Preamble and Pilots (3) The initial short and long training fields, SIGnal fields, and the pilot subcarriers in the DATA field are used. Preamble, Pilots and Data (4) The initial short and long training fields, SIGnal fields, and all the subcarriers in the DATA field are used. |
| Disabled (0) | Carrier frequency error is not computed and the corresponding result is returned as NaN. |
| Initial Preamble (1) | Initial short and long training fields in the PPDU are used. |
| Preamble (2) | Initial short and long training fields along with the SIGnal fields are used. |
| Preamble and Pilots (3) | The initial short and long training fields, SIGnal fields, and the pilot subcarriers in the DATA field are used. |
| Preamble, Pilots and Data (4) | The initial short and long training fields, SIGnal fields, and all the subcarriers in the DATA field are used. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_measurement_length.html language=enus -->
## TOPIC 00056: RFmxWLAN OFDMModAcc Configure Measurement Length (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_measurement_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_measurement_length.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Measurement Length (VI)

Owning Palette:

OFDMModAcc

Configures the measurement offset and maximum measurement length for the OFDMModAcc EVM measurements.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Measurement Length' src='rfmxwlan_ofdmmodacc_configure_measurement_length.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Measurement Offset specifies the number of data OFDM symbols to be ignored from the start of the data field for EVM computation. The default value is 0. |
|  | Maximum Measurement Length specifies the maximum number of data OFDM symbols that the measurement uses to compute EVM. The default value is 16. If the number of available data symbols (n) is greater than the value that you specify (m), the measurement ignores (n-m) symbols from the end of the data field. If you set this parameter to -1, all symbols in the data field are used to compute the EVM. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_measurement_mode.html language=enus -->
## TOPIC 00057: RFmxWLAN OFDMModAcc Configure Measurement Mode (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_measurement_mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_measurement_mode.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Measurement Mode (VI)

Owning Palette:

OFDMModAcc

Configures the measurement mode for the OFDMModAcc measurement.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Measurement Mode' src='rfmxwlan_ofdmmodacc_configure_measurement_mode.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Measurement Mode specifies whether the measurement should calibrate the noise floor of the analyzer or perform the OFDMModAcc measurement. The default value is Measure. Measure (0) The OFDMModAcc measurement is performed on the acquired signal. Calibrate Noise Floor (1) The OFDMModAcc measurement measures the noise floor of the instrument across the frequency range of interest determined by the carrier frequency and channel bandwidth. In this mode, the measurement expects that the signal generator to be turned off and checks whether no signal power is detected at the RF In port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is previously calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |
| Measure (0) | The OFDMModAcc measurement is performed on the acquired signal. |
| Calibrate Noise Floor (1) | The OFDMModAcc measurement measures the noise floor of the instrument across the frequency range of interest determined by the carrier frequency and channel bandwidth. In this mode, the measurement expects that the signal generator to be turned off and checks whether no signal power is detected at the RF In port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is previously calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_noise_compensation_enabled.html language=enus -->
## TOPIC 00058: RFmxWLAN OFDMModAcc Configure Noise Compensation Enabled (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_noise_compensation_enabled.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Noise Compensation Enabled (VI)

Owning Palette:

OFDMModAcc

Configures whether to enable EVM noise compensation for the OFDMModAcc measurement.

**Supported devices:**PXIe-5830/5831/5832/5646/5840/5841/5842.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Noise Compensation Enabled' src='rfmxwlan_ofdmmodacc_configure_noise_compensation_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Noise Compensation Enabled specifies whether the contribution of the instrument noise is compensated for EVM computation. The default value is False. False (0) Disables instrument noise compensation for EVM results. True (1) Enables instrument noise compensation for EVM results. |
| False (0) | Disables instrument noise compensation for EVM results. |
| True (1) | Enables instrument noise compensation for EVM results. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_optimize_dynamic_range_for_evm.html language=enus -->
## TOPIC 00059: RFmxWLAN OFDMModAcc Configure Optimize Dynamic Range for EVM (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_optimize_dynamic_range_for_evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_optimize_dynamic_range_for_evm.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Optimize Dynamic Range for EVM (VI)

Owning Palette:

OFDMModAcc

Specifies whether to optimize analyzer’s dynamic range for the EVM measurement.

**Supported devices:**PXIe-5646/5840/5841/5842.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Optimize Dynamic Range for EVM' src='rfmxwlan_ofdmmodacc_configure_optimize_dynamic_range_for_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Optimize Dynamic Range for EVM Enabled specifies whether to optimize the analyzer's dynamic range for the EVM measurement. This parameter computes optimum attenuation settings for the analyzer based on the reference level you specify while still avoiding ADC or onboard signal processing (OSP) overflow. When you specify the reference level and you notice an overflow error, you can increase the reference level or specify a margin above the reference level by configuring the Optimize Dynamic Range for EVM Margin parameter. The default value is False. False (0) Specifies that the dynamic range is not optimized for EVM measurement. True (1) Specifies that the dynamic range is optimized for EVM measurement. |
| False (0) | Specifies that the dynamic range is not optimized for EVM measurement. |
| True (1) | Specifies that the dynamic range is optimized for EVM measurement. |
|  | Optimize Dynamic Range for EVM Margin (dB) specifies the margin above the reference level you specify when you set the Optimize Dynamic Range for EVM Enabled parameter to True. This value is expressed in dB. When the parameter's value is 0, the dynamic range is optimized. When you set a positive value to the parameter, the dynamic range reduces from the optimized dynamic range. You can use this parameter to avoid ADC and onboard signal processing (OSP) overflows. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_phase_tracking_enabled.html language=enus -->
## TOPIC 00060: RFmxWLAN OFDMModAcc Configure Phase Tracking Enabled (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_phase_tracking_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_phase_tracking_enabled.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Phase Tracking Enabled (VI)

Owning Palette:

OFDMModAcc

Configures whether to enable pilot-based common phase error correction per OFDM data symbol.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Phase Tracking Enabled' src='rfmxwlan_ofdmmodacc_configure_phase_tracking_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Phase Tracking Enabled specifies whether to enable pilot-based common phase error correction per OFDM data symbol. Phase tracking is useful for tracking the phase variation over the modulation symbol caused by the residual frequency offset and phase noise. The default value is True. False (0) Phase tracking is disabled. True (1) Phase tracking is enabled. |
| False (0) | Phase tracking is disabled. |
| True (1) | Phase tracking is enabled. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_reference_waveform_(1_wfm).html language=enus -->
## TOPIC 00061: RFmxWLAN OFDMModAcc Configure Reference Waveform (1 Wfm) (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_reference_waveform_(1_wfm).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_reference_waveform_(1_wfm).html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Reference Waveform (1 Wfm) (VI)

Owning Palette:

OFDMModAcc

Configures the reference waveform for a SISO measurement when you set the [OFDMModAcc EVM Ref Data Symbols Mode](/csh?topicname=rfmxwlanprop/attra04093.html) property to **Reference Waveform**.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Reference Waveform (1 Wfm)' src='rfmxwlan_ofdmmodacc_configure_reference_waveform_(1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Reference Waveform specifies the reference waveform used for deriving the reference data symbols for an EVM computation. The default value is an empty waveform. x0 specifies the starting time of the reference waveform. This value is expressed in seconds. dx specifies the sampling interval of the reference waveform. This value is expressed in seconds. y specifies an array of waveform samples of the reference waveform. |
|  | x0 specifies the starting time of the reference waveform. This value is expressed in seconds. |
|  | dx specifies the sampling interval of the reference waveform. This value is expressed in seconds. |
|  | y specifies an array of waveform samples of the reference waveform. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_reference_waveform_(n_wfms).html language=enus -->
## TOPIC 00062: RFmxWLAN OFDMModAcc Configure Reference Waveform (N Wfms) (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_reference_waveform_(n_wfms).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_reference_waveform_(n_wfms).html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Reference Waveform (N Wfms) (VI)

Owning Palette:

OFDMModAcc

Configures the reference waveform array for a MIMO measurement when you set the [OFDMModAcc EVM Ref Data Symbols Mode](/csh?topicname=rfmxwlanprop/attra04093.html) property to **Reference Waveform**.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Reference Waveform (N Wfms)' src='rfmxwlan_ofdmmodacc_configure_reference_waveform_(n_wfms).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Reference Waveform specifies the reference waveform array used for deriving the reference data symbols for an EVM computation. The default value is an empty waveform. x0 specifies the starting time of the reference waveform. This value is expressed in seconds. dx specifies the sampling interval of the reference waveform. This value is expressed in seconds. y specifies an array of waveform samples of the reference waveform. |
|  | x0 specifies the starting time of the reference waveform. This value is expressed in seconds. |
|  | dx specifies the sampling interval of the reference waveform. This value is expressed in seconds. |
|  | y specifies an array of waveform samples of the reference waveform. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_symbol_clock_error_correction_enabled.html language=enus -->
## TOPIC 00063: RFmxWLAN OFDMModAcc Configure Symbol Clock Error Correction Enabled (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_symbol_clock_error_correction_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_configure_symbol_clock_error_correction_enabled.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Configure Symbol Clock Error Correction Enabled (VI)

Owning Palette:

OFDMModAcc

Configures whether to enable symbol clock error correction.

[IMAGE alt='RFmxWLAN OFDMModAcc Configure Symbol Clock Error Correction Enabled' src='rfmxwlan_ofdmmodacc_configure_symbol_clock_error_correction_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Symbol Clock Error Correction Enabled specifies whether to enable symbol clock error correction. The default value is True. False (0) Symbol clock error correction is disabled. True (1) Symbol clock error correction is enabled. |
| False (0) | Symbol clock error correction is disabled. |
| True (1) | Symbol clock error correction is enabled. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_fetch.html language=enus -->
## TOPIC 00064: RFmxWLAN OFDMModAcc Fetch (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_fetch.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Fetch (VI)

Owning Palette:

Fetch

Fetches the OFDMModAcc measurement results.

#### RFmxWLAN OFDMModAcc Fetch Composite RMS EVM

Fetches the composite RMS EVM results.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Composite RMS EVM' src='rfmxwlan_ofdmmodacc_fetch_composite_rms_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Composite RMS EVM Mean returns the RMS EVM of all subcarriers in all OFDM symbols. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the composite RMS EVM results computed for each averaging count. |
|  | Composite Data RMS EVM Mean returns the RMS EVM of data-subcarriers in all OFDM symbols. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the composite data RMS EVM results computed for each averaging count. |
|  | Composite Pilot RMS EVM Mean returns the RMS EVM of pilot-subcarriers in all OFDM symbols. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the composite pilot RMS EVM results computed for each averaging count. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Stream RMS EVM

Fetches the stream RMS EVM results.

Use "segment<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Stream RMS EVM' src='rfmxwlan_ofdmmodacc_fetch_stream_rms_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0". Example: "segment0/stream0" "signal::sig1/segment0/stream0" "signal::sig1/result::r1/segment0/stream0" "result::r1/segment0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Stream RMS EVM Mean returns the stream RMS EVM of all subcarriers in all OFDM symbols. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of stream RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB. |
|  | Stream Data RMS EVM Mean returns the stream RMS EVM of data subcarriers in all OFDM symbols. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of data stream RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB. |
|  | Stream Pilot RMS EVM Mean returns the stream RMS EVM of pilot subcarriers in all OFDM symbols. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of pilot stream RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Chain RMS EVM

Fetches the chain RMS EVM results.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Chain RMS EVM' src='rfmxwlan_ofdmmodacc_fetch_chain_rms_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Chain RMS EVM Mean returns the chain RMS EVM of all subcarriers in all OFDM symbols. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of chain RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB. |
|  | Chain Data RMS EVM Mean returns the chain RMS EVM of data subcarriers in all OFDM symbols. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of data chain RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB. |
|  | Chain Pilot RMS EVM Mean returns the chain RMS EVM of pilot subcarriers in all OFDM symbols. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of pilot chain RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch User Stream RMS EVM

Fetches the stream RMS EVM results for the specified user.

Use "user<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch User Stream RMS EVM' src='rfmxwlan_ofdmmodacc_fetch_user_stream_rms_evm.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, user number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0/stream0". Example: "user0/stream0" "signal::sig1/user0/stream0" "signal::sig1/result::r1/user0/stream0" "result::r1/user0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | User Stream RMS EVM Mean returns the RMS EVM of all subcarriers in all OFDM symbols for the specified user. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the user stream RMS EVM computed for each averaging count. |
|  | User Stream Data RMS EVM Mean returns the RMS EVM of data-subcarriers in all OFDM symbols for the specified user. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the user stream data RMS EVM computed for each averaging count. |
|  | User Stream Pilot RMS EVM Mean returns the RMS EVM of pilot-subcarriers in all OFDM symbols for the specified user. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the user stream pilot RMS EVM computed for each averaging count. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Frequency Error Mean

Fetches the carrier frequency error of the transmitter.

Use "segment<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Frequency Error Mean' src='rfmxwlan_ofdmmodacc_fetch_frequency_error_mean.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxWLAN Build Segment String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Frequency Error Mean returns the carrier frequency error of the transmitter. This value is expressed in Hz. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the carrier frequency error results computed for each averaging count. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Frequency Error CCDF 10 Percent

Fetches the 10% point of the complementary cumulative distribution function (CCDF) of frequency error across the number of iterations.

Use "segment<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Frequency Error CCDF 10 Percent' src='rfmxwlan_ofdmmodacc_fetch_frequency_error_ccdf_10_percent.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxWLAN Build Segment String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Frequency Error CCDF 10% returns the 10% point of the CCDF of absolute frequency error. When you set the OFDMModAcc Averaging Enabled property to True, the CCDF is computed over each averaging count. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Symbol Clock Error Mean

Fetches the symbol clock error of the transmitter.

Use "segment<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Symbol Clock Error Mean' src='rfmxwlan_ofdmmodacc_fetch_symbol_clock_error_mean.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxWLAN Build Segment String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Symbol Clock Error Mean returns the symbol clock error of the transmitter. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the symbol clock error results computed for each averaging count. This value is expressed in parts per million (ppm). |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch IQ Impairments

Fetches the I/Q Impairment results for the OFDMModAcc measurement.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch IQ Impairments' src='rfmxwlan_ofdmmodacc_fetch_iq_impairments.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Relative I/Q Origin Offset Mean returns the relative I/Q origin offset, which is the ratio of the power of the DC subcarrier to the total power of all the subcarriers. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the relative I/Q origin offset computed for each averaging count. This value is expressed in dB. |
|  | I/Q Gain Imbalance Mean returns the I/Q gain imbalance, which is the ratio of the RMS amplitude of the in-phase (I) component of the signal to the RMS amplitude of the quadrature-phase (Q) component of the signal. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the I/Q gain imbalance computed for each averaging count. This value is expressed in dB. |
|  | I/Q Quadrature Error Mean returns the I/Q quadrature error, which is a measure of deviation of the phase difference between the quadrature-phase (Q) and the in-phase (I) component of the signal from 90 degrees. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the I/Q quadrature error computed for each averaging count. This value is expressed in degrees. |
|  | I/Q Timing Skew Mean returns the I/Q timing skew, which is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the I/Q timing skew computed for each averaging count. This value is expressed in seconds. |
|  | Absolute I/Q Origin Offset Mean returns the absolute I/Q origin offset, which is the power of the DC subcarrier. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the absolute I/Q origin offset computed for each averaging count. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Spectral Flatness

Fetches the spectral flatness margin results.

Use "segment<*n*>/chain<*k*>/stream<*l*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Spectral Flatness' src='rfmxwlan_ofdmmodacc_fetch_spectral_flatness.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, and stream number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/stream0". Example: "segment0/chain0/stream0" "signal::sig1/segment0/chain0/stream0" "signal::sig1/result::r1/segment0/chain0/stream0" "result::r1/segment0/chain0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Spectral Flatness Margin returns the spectral flatness margin, which is the minimum of the upper and lower spectral flatness margins. The upper spectral flatness margin is the minimum difference between the upper mask and the spectral flatness across subcarriers. The lower spectral flatness margin is the minimum difference between the spectral flatness and the lower mask across subcarriers. When you set the OFDMModAcc Averaging Enabled property to True, the spectral flatness is computed using the mean of the channel frequency response magnitude computed for each averaging count. This value is expressed in dB. |
|  | Spectral Flatness Margin Subcarrier Index returns the subcarrier index corresponding to the Spectral Flatness Margin parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Number of Symbols Used

Fetches the number of OFDM symbols used for EVM measurement.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Number of Symbols Used' src='rfmxwlan_ofdmmodacc_fetch_number_of_symbols_used.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Number of Symbols Used returns the number of OFDM symbols used by the measurement. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Number of Space Time Streams

Fetches the number of space time streams.

Use "user<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Number of Space Time Streams' src='rfmxwlan_ofdmmodacc_fetch_number_of_space_time_streams.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0". Example: "user0" "signal::sig1/user0" "signal::sig1/result::r1/user0" "result::r1/user0" You can use the RFmxWLAN Build User String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Number of Space Time Streams returns the number of space time streams. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch PPDU Type

Fetches the PPDU type.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch PPDU Type' src='rfmxwlan_ofdmmodacc_fetch_ppdu_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | PPDU Type returns the PPDU type. Non-HT (0) Applicable to 802.11a, 802.11j, and 802.11p signals or for 802.11n, 802.11ac, and 802.11ax signals that operate in the Non-HT mode. Mixed (1) Applicable to 802.11n mixed PPDU signals. Greenfield (2) Applicable to 802.11n greenfield PPDU signals. SU (3) Applicable to 802.11ac and 802.11ax SU PPDU signals. MU (4) Applicable to 802.11ax and 802.11be MU PPDU signals. Extended Range SU (5) Applicable to 802.11ax extended range SU PPDU signals. Trigger-based (6) Applicable to 802.11ax and 802.11be TB PPDU signals. |
| Non-HT (0) | Applicable to 802.11a, 802.11j, and 802.11p signals or for 802.11n, 802.11ac, and 802.11ax signals that operate in the Non-HT mode. |
| Mixed (1) | Applicable to 802.11n mixed PPDU signals. |
| Greenfield (2) | Applicable to 802.11n greenfield PPDU signals. |
| SU (3) | Applicable to 802.11ac and 802.11ax SU PPDU signals. |
| MU (4) | Applicable to 802.11ax and 802.11be MU PPDU signals. |
| Extended Range SU (5) | Applicable to 802.11ax extended range SU PPDU signals. |
| Trigger-based (6) | Applicable to 802.11ax and 802.11be TB PPDU signals. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch MCS Index

Fetches the MCS index.

Use "user<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch MCS Index' src='rfmxwlan_ofdmmodacc_fetch_mcs_index.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0". Example: "user0" "signal::sig1/user0" "signal::sig1/result::r1/user0" "result::r1/user0" You can use the RFmxWLAN Build User String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | MCS Index returns the MCS index or the data rate. The MCS index or data rate for various standard signals are decoded as follows: Standard Field 802.11a, 802.11j, 802.11p The data rate is decoded from the SIGNAL field. 802.11n The MCS index is decoded from the HT-SIG field. 802.11ac The MCS index is decoded from the VHT-SIG-A field. 802.11ax SU and Extended Range SU PPDU The MCS index is decoded from the HE-SIG-A field. 802.11ax MU PPDU The MCS index is decoded from the HE-SIG-B field. 802.11be MU PPDU The MCS index is decoded from the EHT-SIG field. For 802.11a, 802.11j, and 802.11p signals, the following MCS indices corresponds to their data rates: MCS Data Rate 0 1.5 Mbps, 3 Mbps, and 6 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 1 2.25 Mbps, 4.5 Mbps, and 9 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 2 3 Mbps, 6 Mbps, and 12 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 3 4.5 Mbps, 9 Mbps, and 18 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 4 6 Mbps, 12 Mbps, and 24 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 5 9 Mbps, 18 Mbps, and 36 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 6 12 Mbps, 24 Mbps, and 48 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 7 13.5 Mbps, 27 Mbps, and 54 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| Standard | Field |
| 802.11a, 802.11j, 802.11p | The data rate is decoded from the SIGNAL field. |
| 802.11n | The MCS index is decoded from the HT-SIG field. |
| 802.11ac | The MCS index is decoded from the VHT-SIG-A field. |
| 802.11ax SU and Extended Range SU PPDU | The MCS index is decoded from the HE-SIG-A field. |
| 802.11ax MU PPDU | The MCS index is decoded from the HE-SIG-B field. |
| 802.11be MU PPDU | The MCS index is decoded from the EHT-SIG field. |
| MCS | Data Rate |
| 0 | 1.5 Mbps, 3 Mbps, and 6 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 1 | 2.25 Mbps, 4.5 Mbps, and 9 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 2 | 3 Mbps, 6 Mbps, and 12 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 3 | 4.5 Mbps, 9 Mbps, and 18 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 4 | 6 Mbps, 12 Mbps, and 24 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 5 | 9 Mbps, 18 Mbps, and 36 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 6 | 12 Mbps, 24 Mbps, and 48 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 7 | 13.5 Mbps, 27 Mbps, and 54 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch RU Offset and Size

Fetches the RU offset and the RU size of the specified user.

Use "user<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch RU Offset and Size' src='rfmxwlan_ofdmmodacc_fetch_ru_offset_and_size.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0". Example: "user0" "signal::sig1/user0" "signal::sig1/result::r1/user0" "result::r1/user0" You can use the RFmxWLAN Build User String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | RU Offset returns the location of RU for the specified user in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. |
|  | RU Size returns the RU size for the specified user. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Number of Users

Fetches the number of users.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Number of Users' src='rfmxwlan_ofdmmodacc_fetch_number_of_users.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Number of Users returns the number of users which is derived for the following standards. Standard Derivation 802.11ac Derived from the VHT-SIG-A for VHT MU PPDU. 802.11ax Derived from the HE-SIG-B for HE MU PPDU. 802.11be Derived from the EHT-SIG for EHT MU PPDU. For all other PPDUs, this property returns 1. |
| Standard | Derivation |
| 802.11ac | Derived from the VHT-SIG-A for VHT MU PPDU. |
| 802.11ax | Derived from the HE-SIG-B for HE MU PPDU. |
| 802.11be | Derived from the EHT-SIG for EHT MU PPDU. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Number of HE-SIG-B Symbols

Fetches the number of HE-SIG-B symbols.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Number of HE-SIG-B Symbols' src='rfmxwlan_ofdmmodacc_fetch_number_of_he-sig-b_symbols.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Number of HE-SIG-B Symbols returns the number of HE-SIG-B symbols. This result is applicable for 802.11ax MU PPDU signals, and is decoded from the HE-SIG-A field. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Guard Interval Type

Fetches the guard interval type.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Guard Interval Type' src='rfmxwlan_ofdmmodacc_fetch_guard_interval_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Guard Interval Type returns the size of the guard interval of OFDM symbols. 1/4 (0) Indicates the guard interval is 1/4th of the IFFT duration. 1/8 (1) Indicates the guard interval is 1/8th of the IFFT duration. 1/16 (2) Indicates the guard interval is 1/16th of the IFFT duration. |
| 1/4 (0) | Indicates the guard interval is 1/4th of the IFFT duration. |
| 1/8 (1) | Indicates the guard interval is 1/8th of the IFFT duration. |
| 1/16 (2) | Indicates the guard interval is 1/16th of the IFFT duration. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch LTF Size

Fetches the HE-LTF or EHT-LTF size for 802.11ax or 802.11be, respectively.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch LTF Size' src='rfmxwlan_ofdmmodacc_fetch_ltf_size.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | LTF Size returns the HE-LTF or EHT-LTF size. This result is applicable only to 802.11ax and 802.11be signals. Not Applicable (-1) Result is not applicable. 4x (0) The HE-LTF or EHT-LTF size is 4x. 2x (1) The HE-LTF or EHT-LTF size is 2x. 1x (2) The HE-LTF or EHT-LTF size is 1x. |
| Not Applicable (-1) | Result is not applicable. |
| 4x (0) | The HE-LTF or EHT-LTF size is 4x. |
| 2x (1) | The HE-LTF or EHT-LTF size is 2x. |
| 1x (2) | The HE-LTF or EHT-LTF size is 1x. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch L-SIG Parity Check Status

Fetches the L-SIG parity check status.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch L-SIG Parity Check Status' src='rfmxwlan_ofdmmodacc_fetch_l-sig_parity_check_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | L-SIG Parity Check Status returns whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be waveforms. Not Applicable (-1) Returns that the parity check is invalid for the current waveform. Fail (0) Returns that the parity check failed. Pass (1) Returns that the parity check passed. |
| Not Applicable (-1) | Returns that the parity check is invalid for the current waveform. |
| Fail (0) | Returns that the parity check failed. |
| Pass (1) | Returns that the parity check passed. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch SIG CRC Status

Fetches the SIG CRC Status.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch SIG CRC Status' src='rfmxwlan_ofdmmodacc_fetch_sig_crc_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | SIG CRC Status returns whether the cyclic redundancy check (CRC) has passed either for the HT-SIG field of the 802.11n waveform, for the VHT-SIG-A field of the 802.11ac waveform, or for the HE-SIG-A field of the 802.11ax waveform. Not Applicable (-1) Returns that the SIG CRC is invalid for the current waveform. Fail (0) Returns that the SIG CRC failed. Pass (1) Returns that the SIG CRC passed. |
| Not Applicable (-1) | Returns that the SIG CRC is invalid for the current waveform. |
| Fail (0) | Returns that the SIG CRC failed. |
| Pass (1) | Returns that the SIG CRC passed. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch SIG-B CRC Status

Fetches the SIG-B CRC Status.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch SIG-B CRC Status' src='rfmxwlan_ofdmmodacc_fetch_sig-b_crc_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | SIG-B CRC Status returns whether the cyclic redundancy check (CRC) has passed for the HE-SIG-B field of the 802.11ax MU PPDU waveform. Not Applicable (-1) Returns that the SIG-B CRC is invalid for the current waveform. Fail (0) Returns that the SIG-B CRC failed. Pass (1) Returns that the SIG-B CRC passed. |
| Not Applicable (-1) | Returns that the SIG-B CRC is invalid for the current waveform. |
| Fail (0) | Returns that the SIG-B CRC failed. |
| Pass (1) | Returns that the SIG-B CRC passed. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch PSDU CRC Status

Fetches the PLCP service data unit (PSDU) CRC status.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch PSDU CRC Status' src='rfmxwlan_ofdmmodacc_fetch_psdu_crc_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | PSDU CRC Status returns the PSDU CRC status. Fail (0) Indicates that the PSDU CRC failed. Pass (1) Indicates that the PSDU CRC passed. |
| Fail (0) | Indicates that the PSDU CRC failed. |
| Pass (1) | Indicates that the PSDU CRC passed. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch PE Duration

Fetches the duration of the packet extension field.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch PE Duration' src='rfmxwlan_ofdmmodacc_fetch_pe_duration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | PE Duration returns the duration of the packet extension field for the 802.11ax and 802.11be signals. This parameter is applicable only when you set the OFDM Header Decoding Enabled property to True. This value is expressed in seconds. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Data Average Power

Fetches the average power of the data field.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Data Average Power' src='rfmxwlan_ofdmmodacc_fetch_data_average_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Data Average Power Mean returns the average power of the data field. This value is expressed in dBm. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the data average power results computed for each averaging count. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Data Peak Power

Fetches the peak power of the data field.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Data Peak Power' src='rfmxwlan_ofdmmodacc_fetch_data_peak_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Data Peak Power Maximum returns the peak power of the data field. This value is expressed in dBm. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns an array of the maximum of the data peak power results computed for each averaging count. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch PPDU Average Power

Fetches the average power of the PPDU.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch PPDU Average Power' src='rfmxwlan_ofdmmodacc_fetch_ppdu_average_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | PPDU Average Power Mean returns the average power of the PPDU. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the PPDU average power results computed for each averaging count. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch PPDU Peak Power

Fetches the peak power of the PPDU.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch PPDU Peak Power' src='rfmxwlan_ofdmmodacc_fetch_ppdu_peak_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | PPDU Peak Power Maximum returns the peak power of the PPDU. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the PPDU peak power results computed for each averaging count. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch PE Average Power

Fetches the average power of the packet extension field.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch PE Average Power' src='rfmxwlan_ofdmmodacc_fetch_pe_average_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | PE Average Power Mean returns the average power of the packet extension field. This parameter is applicable for 802.11ax signals. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the packet extension field average power results computed for each averaging count. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch PE Peak Power

Fetches the peak power of the packet extension field.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch PE Peak Power' src='rfmxwlan_ofdmmodacc_fetch_pe_peak_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | PE Peak Power Maximum returns the peak power of the packet extension field. This parameter is applicable for 802.11ax signals. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the PE field peak power results computed for each averaging count. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (Common)

Fetches the average power of the preamble fields.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (Common)' src='rfmxwlan_ofdmmodacc_fetch_preamble_average_powers_(common).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_ofdmmodacc_validate_calibration_data.html language=enus -->
## TOPIC 00065: RFmxWLAN OFDMModAcc Validate Calibration Data (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_ofdmmodacc_validate_calibration_data.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_ofdmmodacc_validate_calibration_data.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN OFDMModAcc Validate Calibration Data (VI)

Owning Palette:

OFDMModAcc

Indicates whether calibration data is valid for the configuration specified by the signal name in the **Selector string** parameter.

[IMAGE alt='RFmxWLAN OFDMModAcc Validate Calibration Data' src='rfmxwlan_ofdmmodacc_validate_calibration_data.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Calibration Data Valid returns whether the calibration data is valid. False (0) Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. True (1) Returns true if the calibration data is present for the configuration specified by the signal name in the Selector string parameter. |
| False (0) | Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. |
| True (1) | Returns true if the calibration data is present for the configuration specified by the signal name in the Selector string parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_powerramp_configure_acquisition_length.html language=enus -->
## TOPIC 00066: RFmxWLAN PowerRamp Configure Acquisition Length (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_powerramp_configure_acquisition_length.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_powerramp_configure_acquisition_length.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN PowerRamp Configure Acquisition Length (VI)

Owning Palette:

PowerRamp

Configures the waveform acquisition length for the measurement.

[IMAGE alt='RFmxWLAN PowerRamp Configure Acquisition Length' src='rfmxwlan_powerramp_configure_acquisition_length.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | Acquisition Length specifies the duration of the signal to be acquired for the PowerRamp measurement. This value is expressed in seconds. You must set this parameter to a value that is greater than or equal to the duration of the PPDU under analysis, so that the acquired signal contains both rising and falling power ramp transitions. The default value is 1 ms. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_powerramp_configure_averaging.html language=enus -->
## TOPIC 00067: RFmxWLAN PowerRamp Configure Averaging (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_powerramp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_powerramp_configure_averaging.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN PowerRamp Configure Averaging (VI)

Owning Palette:

PowerRamp

Configures averaging for the measurement.

[IMAGE alt='RFmxWLAN PowerRamp Configure Averaging' src='rfmxwlan_powerramp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the PowerRamp measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_powerramp_fetch.html language=enus -->
## TOPIC 00068: RFmxWLAN PowerRamp Fetch (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_powerramp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_powerramp_fetch.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN PowerRamp Fetch (VI)

Owning Palette:

Fetch

Fetches the PowerRamp measurement results.

#### RFmxWLAN PowerRamp Fetch Measurement

Returns the PowerRamp rise time and fall time.

[IMAGE alt='RFmxWLAN PowerRamp Fetch Measurement' src='rfmxwlan_powerramp_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Rise Time Mean returns the rise time of the acquired signal that is the amount of time taken for the power envelope to rise from a level of 10 percent to 90 percent. This value is expressed in seconds. When you set the PowerRamp Averaging Enabled property to True, this parameter returns the mean of the rise time computed for each averaging count. This value is expressed in seconds. |
|  | Fall Time Mean returns the fall time of the acquired signal that is the amount of time taken for the power envelope to fall from a level of 90 percent to 10 percent. This value is expressed in seconds. When you set the PowerRamp Averaging Enabled property to True, this parameter returns the mean of the fall time computed for each averaging count. This value is expressed in seconds. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN PowerRamp Fetch Rise Trace

Returns the raw, processed, threshold and power-reference traces at the beginning of a burst.

[IMAGE alt='RFmxWLAN PowerRamp Fetch Rise Trace' src='rfmxwlan_powerramp_fetch_rise_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Raw Waveform returns the power versus time trace of the acquired waveform at the beginning of the burst. x0 returns the trace start time. This value is expressed in seconds. dx returns the sampling interval. This value is expressed in seconds. y returns an array of measured signal power. This value is expressed as a percentage. |
|  | x0 returns the trace start time. This value is expressed in seconds. |
|  | dx returns the sampling interval. This value is expressed in seconds. |
|  | y returns an array of measured signal power. This value is expressed as a percentage. |
|  | Processed Waveform returns the power versus time trace of the power envelope of the acquired waveform at the beginning of the burst. x0 returns the trace start time. This value is expressed in seconds. dx returns the sampling interval. This value is expressed in seconds. y returns an array of measured envelope power. This value is expressed as a percentage. |
|  | x0 returns the trace start time. This value is expressed in seconds. |
|  | dx returns the sampling interval. This value is expressed in seconds. |
|  | y returns an array of measured envelope power. This value is expressed as a percentage. |
|  | Threshold returns the threshold trace indicating the 10 percent and the 90 percent power levels. x0 returns the trace start time. This value is expressed in seconds. dx returns the sampling interval. This value is expressed in seconds. y returns an array of threshold values. This value is expressed as a percentage. |
|  | x0 returns the trace start time. This value is expressed in seconds. |
|  | dx returns the sampling interval. This value is expressed in seconds. |
|  | y returns an array of threshold values. This value is expressed as a percentage. |
|  | Power Reference returns the power reference trace which indicates the 100% power level, corresponding to the steady state average power level of the initial portion of the burst. x0 returns the trace start time. This value is expressed in seconds. dx returns the sampling interval. This value is expressed in seconds. y returns an array of power reference values. This value is expressed as a percentage. |
|  | x0 returns the trace start time. This value is expressed in seconds. |
|  | dx returns the sampling interval. This value is expressed in seconds. |
|  | y returns an array of power reference values. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN PowerRamp Fetch Fall Trace

Returns the raw, processed, thresholding and power reference waveforms at the end of a burst.

[IMAGE alt='RFmxWLAN PowerRamp Fetch Fall Trace' src='rfmxwlan_powerramp_fetch_fall_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Raw Waveform returns the power versus time trace of the acquired waveform at the end of the burst. x0 returns the trace start time. This value is expressed in seconds. dx returns the sampling interval. This value is expressed in seconds. y returns an array of measured signal power. This value is expressed as a percentage. |
|  | x0 returns the trace start time. This value is expressed in seconds. |
|  | dx returns the sampling interval. This value is expressed in seconds. |
|  | y returns an array of measured signal power. This value is expressed as a percentage. |
|  | Processed Waveform returns the power versus time trace of the power envelope of the acquired waveform at the end of the burst. x0 returns the trace start time. This value is expressed in seconds. dx returns the sampling interval. This value is expressed in seconds. y returns an array of measured envelope power. This value is expressed as a percentage. |
|  | x0 returns the trace start time. This value is expressed in seconds. |
|  | dx returns the sampling interval. This value is expressed in seconds. |
|  | y returns an array of measured envelope power. This value is expressed as a percentage. |
|  | Threshold returns the threshold trace indicating the 10 percent and the 90 percent power levels. x0 returns the trace start time. This value is expressed in seconds. dx returns the sampling interval. This value is expressed in seconds. y returns an array of threshold values. This value is expressed as a percentage. |
|  | x0 returns the trace start time. This value is expressed in seconds. |
|  | dx returns the sampling interval. This value is expressed in seconds. |
|  | y returns an array of threshold values. This value is expressed as a percentage. |
|  | Power Reference returns the power reference trace which indicates the 100% power level, corresponding to the steady state average power level of the final portion of the burst. x0 returns the trace start time. This value is expressed in seconds. dx returns the sampling interval. This value is expressed in seconds. y returns an array of power reference values. This value is expressed as a percentage. |
|  | x0 returns the trace start time. This value is expressed in seconds. |
|  | dx returns the sampling interval. This value is expressed in seconds. |
|  | y returns an array of power reference values. This value is expressed as a percentage. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_property_node.html language=enus -->
## TOPIC 00069: RFmxWLAN Property Node (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_property_node.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_property_node.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Property Node (VI)

Owning Palette:

RFmx WLAN VIs

Gets (reads), sets (writes), or resets (sets to default value) [RFmxWLAN properties](/csh?topicname=rfmxwlanprop/crfmxwlan.html).

[IMAGE alt='RFmxWLAN Property Node' src='rfmxwlan_property_node.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_reset_to_default.html language=enus -->
## TOPIC 00070: RFmxWLAN Reset to Default (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_reset_to_default.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_reset_to_default.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Reset to Default (VI)

Owning Palette:

Utility

Resets a signal to the default values.

[IMAGE alt='RFmxWLAN Reset to Default' src='rfmxwlan_reset_to_default.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_select_measurement.html language=enus -->
## TOPIC 00071: RFmxWLAN Select Measurement (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_select_measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_select_measurement.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Select Measurement (VI)

Owning Palette:

RFmx WLAN VIs

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

#### RFmxWLAN Select Measurement (Single)

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='RFmxWLAN Select Measurement (Single)' src='rfmxwlan_select_measurement_(single).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Measurement specifies the measurement to perform. You can specify one of the following measurements. The default value is TXP. TXP (0) Enables TXP measurement. PowerRamp (1) Enables PowerRamp measurement. DSSSModAcc (2) Enables DSSSModAcc measurement. OFDMModAcc (3) Enables OFDMModAcc measurement. SEM (4) Enables SEM measurement. |
| TXP (0) | Enables TXP measurement. |
| PowerRamp (1) | Enables PowerRamp measurement. |
| DSSSModAcc (2) | Enables DSSSModAcc measurement. |
| OFDMModAcc (3) | Enables OFDMModAcc measurement. |
| SEM (4) | Enables SEM measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN Select Measurement (Multiple)

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='RFmxWLAN Select Measurement (Multiple)' src='rfmxwlan_select_measurement_(multiple).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Measurements specifies the measurement to perform. You can specify one or more of the following measurements. The default is an empty array. TXP (0) Enables TXP measurement. PowerRamp (1) Enables PowerRamp measurement. DSSSModAcc (2) Enables DSSSModAcc measurement. OFDMModAcc (3) Enables OFDMModAcc measurement. SEM (4) Enables SEM measurement. |
| TXP (0) | Enables TXP measurement. |
| PowerRamp (1) | Enables PowerRamp measurement. |
| DSSSModAcc (2) | Enables DSSSModAcc measurement. |
| OFDMModAcc (3) | Enables OFDMModAcc measurement. |
| SEM (4) | Enables SEM measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_sem_configure_averaging.html language=enus -->
## TOPIC 00072: RFmxWLAN SEM Configure Averaging (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_sem_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_sem_configure_averaging.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN SEM Configure Averaging (VI)

Owning Palette:

SEM

Configures averaging for the measurement.

[IMAGE alt='RFmxWLAN SEM Configure Averaging' src='rfmxwlan_sem_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the SEM. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one record to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one record to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one record to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one record to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_sem_configure_mask_type.html language=enus -->
## TOPIC 00073: RFmxWLAN SEM Configure Mask Type (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_sem_configure_mask_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_sem_configure_mask_type.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN SEM Configure Mask Type (VI)

Owning Palette:

SEM

Configures the mask type for the SEM measurement.

[IMAGE alt='RFmxWLAN SEM Configure Mask Type' src='rfmxwlan_sem_configure_mask_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Mask Type specifies whether the mask used for the SEM measurement is as per the 3GPP standard or specified by you. The default value is Standard. Standard (0) Mask limits are configured as per the standard. Custom (1) Mask limits are configured by you. |
| Standard (0) | Mask limits are configured as per the standard. |
| Custom (1) | Mask limits are configured by you. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_sem_configure_number_of_offsets.html language=enus -->
## TOPIC 00074: RFmxWLAN SEM Configure Number of Offsets (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_sem_configure_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_sem_configure_number_of_offsets.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN SEM Configure Number of Offsets (VI)

Owning Palette:

SEM

Configures the number of offset segments for the SEM measurement when you set the [SEM Mask Type](/csh?topicname=rfmxwlanprop/attra05002.html) property to **Custom**.

[IMAGE alt='RFmxWLAN SEM Configure Number of Offsets' src='rfmxwlan_sem_configure_number_of_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Number of Offsets specifies the number of SEM offset segments. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_sem_configure_offset_frequency_(array).html language=enus -->
## TOPIC 00075: RFmxWLAN SEM Configure Offset Frequency (Array) (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_sem_configure_offset_frequency_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_sem_configure_offset_frequency_(array).html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN SEM Configure Offset Frequency (Array) (VI)

Owning Palette:

SEM Array VIs

Configures the array of offset start and stop frequencies and specifies whether the offsets are present on one side, or on both the sides of the carrier when you set the [SEM Mask Type](/csh?topicname=rfmxwlanprop/attra05002.html) property to **Custom**.

[IMAGE alt='RFmxWLAN SEM Configure Offset Frequency (Array)' src='rfmxwlan_sem_configure_offset_frequency_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Offset Start Frequency specifies the array of offset start frequencies, relative to the carrier frequency. This value is expressed in Hz. The default value is an empty array. |
|  | Offset Stop Frequency specifies the array of offset stop frequencies, relative to the carrier frequency. This value is expressed in Hz. The default value is an empty array. |
|  | Offset Sideband specifies whether the offset segments present on one or both sides of the carrier. The default value is Both. Neg (0) Configures a lower offset segment to the left of the carrier. Pos (1) Configures an upper offset segment to the right of the carrier. Both (2) Configures both negative and positive offset segments. |
| Neg (0) | Configures a lower offset segment to the left of the carrier. |
| Pos (1) | Configures an upper offset segment to the right of the carrier. |
| Both (2) | Configures both negative and positive offset segments. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_sem_configure_offset_relative_limit_(array).html language=enus -->
## TOPIC 00076: RFmxWLAN SEM Configure Offset Relative Limit (Array) (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_sem_configure_offset_relative_limit_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_sem_configure_offset_relative_limit_(array).html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN SEM Configure Offset Relative Limit (Array) (VI)

Owning Palette:

SEM Array VIs

Configures an array of relative mask limits corresponding the start and stop frequencies of the offsets when you set the [SEM Mask Type](/csh?topicname=rfmxwlanprop/attra05002.html) property to **Custom**. The relative limits are relative to the peak power of the carrier.

[IMAGE alt='RFmxWLAN SEM Configure Offset Relative Limit (Array)' src='rfmxwlan_sem_configure_offset_relative_limit_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Relative Limit Start specifies the array of relative power limits corresponding to the start frequencies of the offsets. The relative limits are relative to the peak power of the carrier. This value is expressed in dB. The default value is an empty array. |
|  | Relative Limit Stop specifies the array of relative power limits corresponding to the stop frequencies of the offsets. The relative limits are relative to the peak power of the carrier. This value is expressed in dB. The default value is an empty array. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_sem_configure_span.html language=enus -->
## TOPIC 00077: RFmxWLAN SEM Configure Span (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_sem_configure_span.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_sem_configure_span.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN SEM Configure Span (VI)

Owning Palette:

SEM

Configures the frequency range around the center frequency to be acquired for the SEM measurement.

[IMAGE alt='RFmxWLAN SEM Configure Span' src='rfmxwlan_sem_configure_span.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Span Auto specifies whether the frequency range of the spectrum used for the SEM measurement is computed automatically by the measurement or is configured by you. This parameter is applicable when you set the SEM Mask Type property to Standard. The default value is True. False (0) The span you configure is used as the frequency range for the SEM measurement. True (1) The span is automatically computed based on the configured standard and bandwidth. |
| False (0) | The span you configure is used as the frequency range for the SEM measurement. |
| True (1) | The span is automatically computed based on the configured standard and bandwidth. |
|  | Span specifies the frequency range of the spectrum that is used for the SEM measurement. This value is expressed in Hz. This parameter is applicable only when you set the Span Auto parameter to False, and the SEM Mask Type property to Standard. The default value is 66 MHz. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_sem_configure_sweep_time.html language=enus -->
## TOPIC 00078: RFmxWLAN SEM Configure Sweep Time (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_sem_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_sem_configure_sweep_time.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN SEM Configure Sweep Time (VI)

Owning Palette:

SEM

Configures the sweep time.

[IMAGE alt='RFmxWLAN SEM Configure Sweep Time' src='rfmxwlan_sem_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the sweep time for the SEM measurement is computed automatically by the measurement or is configured by you. The default value is True. False (0) The sweep time you configure using the Sweep Time parameter is used as the sweep time for the SEM measurement. True (1) The sweep time is computed automatically based on the configured standard. |
| False (0) | The sweep time you configure using the Sweep Time parameter is used as the sweep time for the SEM measurement. |
| True (1) | The sweep time is computed automatically based on the configured standard. |
|  | Sweep Time specifies the sweep time for the SEM measurement. This value is expressed in seconds. This parameter is ignored when you set the SEM Sweep Time Auto parameter to False. The default value is 1 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_sem_fetch.html language=enus -->
## TOPIC 00079: RFmxWLAN SEM Fetch (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_sem_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_sem_fetch.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN SEM Fetch (VI)

Owning Palette:

Fetch

Fetches spectral emission mask (SEM) measurement results.

#### RFmxWLAN SEM Fetch Measurement Status

Fetches the overall measurement status.

[IMAGE alt='RFmxWLAN SEM Fetch Measurement Status' src='rfmxwlan_sem_fetch_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Measurement Status returns the overall measurement status indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments. Fail (0) The spectrum exceeds the SEM measurement mask limits for at least one of the offset segments. Pass (1) The spectrum does not exceed the SEM measurement mask limits for any offset segment. |
| Fail (0) | The spectrum exceeds the SEM measurement mask limits for at least one of the offset segments. |
| Pass (1) | The spectrum does not exceed the SEM measurement mask limits for any offset segment. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN SEM Fetch Carrier Measurement

Returns the absolute and relative carrier power measurements. The relative power is relative to the peak power of the carrier.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN SEM Fetch Carrier Measurement' src='rfmxwlan_sem_fetch_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Absolute Power returns the average power of the carrier channel over the bandwidth indicated by the SEM Carrier IBW property. This value is expressed in dBm. |
|  | Relative Power returns the average power of the carrier channel, relative to the peak power of the carrier channel, over the bandwidth indicated by the SEM Carrier IBW property. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN SEM Fetch Lower Offset Margin

Returns the measurement status, margin, margin-frequency, and absolute and relative power corresponding to the margin-frequency for lower offset segment. The relative power is relative to the peak power in the carrier.

Use "segment<*n*>/chain<*k*>/offset<*l*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN SEM Fetch Lower Offset Margin' src='rfmxwlan_sem_fetch_lower_offset_margin.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/offset0". Example: "segment0/chain0/offset0" "signal::sig1/segment0/chain0/offset0" "signal::sig1/result::r1/segment0/chain0/offset0" "result::r1/segment0/chain0/offset0" You can use the RFmxWLAN Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Measurement Status returns the lower offset (negative) segment measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in the lower offset segment. Fail (0) The spectrum exceeds the SEM measurement mask limits the lower offset segment. Pass (1) The spectrum does not exceed the SEM measurement mask limits for the lower offset segment. |
| Fail (0) | The spectrum exceeds the SEM measurement mask limits the lower offset segment. |
| Pass (1) | The spectrum does not exceed the SEM measurement mask limits for the lower offset segment. |
|  | Margin returns the margin from the SEM measurement mask for the lower offset. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the mask. |
|  | Margin Frequency returns the frequency corresponding to the margin for the lower offset. This value is expressed in Hz. |
|  | Margin Relative Power returns the relative power corresponding to the margin for the lower offset. The relative power is relative to the peak power of the carrier channel. This value is expressed in dB. |
|  | Margin Absolute Power returns the absolute power corresponding to the margin for the lower offset. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN SEM Fetch Lower Offset Power

Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of lower offset segment. The relative power is relative to the peak power of the carrier.

Use "segment<*n*>/chain<*k*>/offset<*l*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN SEM Fetch Lower Offset Power' src='rfmxwlan_sem_fetch_lower_offset_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/offset0". Example: "segment0/chain0/offset0" "signal::sig1/segment0/chain0/offset0" "signal::sig1/result::r1/segment0/chain0/offset0" "result::r1/segment0/chain0/offset0" You can use the RFmxWLAN Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Total Absolute Power returns the average power of the lower offset over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm. |
|  | Total Relative Power returns the average power of the lower offset relative to the peak power of the carrier channel. This value is expressed in dB. |
|  | Peak Absolute Power returns the peak power of the lower offset. This value is expressed in dBm. |
|  | Peak Relative Power returns the peak power of the lower offset, relative to the peak power of the carrier channel. This value is expressed in dBm. |
|  | Peak Frequency returns the frequency at which the peak power occurs in the lower offset. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN SEM Fetch Upper Offset Margin

Returns the measurement status, margin, margin-frequency, absolute and relative power corresponding to the margin-frequency for upper offset segment. The relative power is relative to the peak power in the carrier.

Use "segment<*n*>/chain<*k*>/offset<*l*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN SEM Fetch Upper Offset Margin' src='rfmxwlan_sem_fetch_upper_offset_margin.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/offset0". Example: "segment0/chain0/offset0" "signal::sig1/segment0/chain0/offset0" "signal::sig1/result::r1/segment0/chain0/offset0" "result::r1/segment0/chain0/offset0" You can use the RFmxWLAN Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Measurement Status returns the upper (positive) offset segment measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in the upper offset segment. Fail (0) The spectrum exceeds the SEM measurement mask limits the upper offset segment. Pass (1) The spectrum does not exceed the SEM measurement mask limits for the upper offset segment. |
| Fail (0) | The spectrum exceeds the SEM measurement mask limits the upper offset segment. |
| Pass (1) | The spectrum does not exceed the SEM measurement mask limits for the upper offset segment. |
|  | Margin returns the margin from the SEM measurement mask for the upper offset. Margin is defined as the maximum difference between the spectrum and the mask. This value is expressed in dB. |
|  | Margin Frequency returns the frequency corresponding to the margin for the upper offset. This value is expressed in Hz. |
|  | Margin Relative Power returns the power level of the spectrum, corresponding to the SEM Results Upper Offset Margin result. The power level is returned relative to the peak power of the carrier channel. This value is expressed in dB. |
|  | Margin Absolute Power returns the power level of the spectrum, corresponding to the SEM Results Upper Offset Margin result. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN SEM Fetch Upper Offset Power

Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of upper offset segment. The relative power is relative to the peak power of the carrier.

Use "segment<*n*>/chain<*k*>/offset<*l*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN SEM Fetch Upper Offset Power' src='rfmxwlan_sem_fetch_upper_offset_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/offset0". Example: "segment0/chain0/offset0" "signal::sig1/segment0/chain0/offset0" "signal::sig1/result::r1/segment0/chain0/offset0" "result::r1/segment0/chain0/offset0" You can use the RFmxWLAN Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Total Absolute Power returns the average power of the upper (positive) offset over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm. |
|  | Total Relative Power returns the average power of the upper offset relative to the peak power of the carrier channel. This value is expressed in dB. |
|  | Peak Absolute Power returns the peak power of the upper offset. This value is expressed in dBm. |
|  | Peak Relative Power returns the peak power of the upper offset, relative to the peak power of the carrier channel. This value is expressed in dBm. |
|  | Peak Frequency returns the frequency at which the peak power occurs in the upper offset. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN SEM Fetch Lower Offset Margin (Array)

Returns an array of measurement status, margins, margin-frequencies, and absolute and relative powers corresponding to the margin-frequencies for lower offset segments. The relative powers are relative to the peak power in the carrier.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN SEM Fetch Lower Offset Margin (Array)' src='rfmxwlan_sem_fetch_lower_offset_margin_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Measurement Status returns an array of lower (negative) offset segment measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in the lower offset segments. Fail (0) The spectrum exceeds the SEM measurement mask limits the lower offset segment. Pass (1) The spectrum does not exceed the SEM measurement mask limits for the lower offset segment. |
| Fail (0) | The spectrum exceeds the SEM measurement mask limits the lower offset segment. |
| Pass (1) | The spectrum does not exceed the SEM measurement mask limits for the lower offset segment. |
|  | Margin returns an array of margins from the SEM measurement mask for the lower offset. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the mask. |
|  | Margin Frequency returns an array of frequencies corresponding to the margins for the lower (negative) offsets. This value is expressed in dB. |
|  | Margin Relative Power returns an array of relative powers corresponding to the margins for the lower offsets. The relative powers are relative to the peak power of the carrier channel. This value is expressed in dB. |
|  | Margin Absolute Power returns an array of absolute powers corresponding to the margins for the lower offsets. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN SEM Fetch Lower Offset Power (Array)

Returns an array of total absolute and relative powers, peak absolute and relative powers and frequencies corresponding to the peak absolute powers of lower offset segments. The relative powers are relative to peak power of the carrier.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN SEM Fetch Lower Offset Power (Array)' src='rfmxwlan_sem_fetch_lower_offset_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Total Absolute Power returns an array of average powers of the lower offsets over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm. |
|  | Total Relative Power returns an array of average powers of the lower offsets relative to the peak power of the carrier channel. This value is expressed in dB. |
|  | Peak Absolute Power returns an array of peak powers of the lower offsets. This value is expressed in dBm. |
|  | Peak Relative Power returns an array of peak powers of the lower offsets, relative to the peak power of the carrier channel. This value is expressed in dBm. |
|  | Peak Frequency returns an array of frequencies at which the peak power occurs in the lower offsets. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN SEM Fetch Upper Offset Margin (Array)

Returns an array of measurement status, margins, margin frequencies, absolute and relative powers corresponding to the margin-frequencies for upper offset segments. The relative powers are relative to the peak power in the carrier.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN SEM Fetch Upper Offset Margin (Array)' src='rfmxwlan_sem_fetch_upper_offset_margin_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Measurement Status returns an array of upper offset (positive) segment measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in the upper offset segments. Fail (0) The spectrum exceeds the SEM measurement mask limits the upper offset segment. Pass (1) The spectrum does not exceed the SEM measurement mask limits for the upper offset segment. |
| Fail (0) | The spectrum exceeds the SEM measurement mask limits the upper offset segment. |
| Pass (1) | The spectrum does not exceed the SEM measurement mask limits for the upper offset segment. |
|  | Margin returns an array of margins from the SEM measurement mask for the upper offset. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the mask. |
|  | Margin Frequency returns an array of frequencies corresponding to the margins for the upper offsets. This value is expressed in Hz. |
|  | Margin Relative Power returns an array of relative powers corresponding to the margins for the upper (positive) offsets. The relative powers are relative to the peak power of the carrier channel. This value is expressed in dB. |
|  | Margin Absolute Power returns an array of absolute powers corresponding to the margins for the upper (positive) offsets. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN SEM Fetch Upper Offset Power (Array)

Fetches an array of total absolute and relative powers, peak absolute and relative powers, and frequencies corresponding to the peak absolute powers of upper offset segments. The relative powers are relative to peak power of the carrier.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN SEM Fetch Upper Offset Power (Array)' src='rfmxwlan_sem_fetch_upper_offset_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Total Absolute Power returns an array of average powers of the upper offsets over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm. |
|  | Total Relative Power returns an array of average powers of the upper offsets relative to the peak power of the carrier channel. This value is expressed in dB. |
|  | Peak Absolute Power returns an array of peak powers of the upper offsets. This value is expressed in dBm. |
|  | Peak Relative Power returns an array of peak powers of the upper offsets, relative to the peak power of the carrier channel. This value is expressed in dBm. |
|  | Peak Frequency returns an array of frequencies at which the peak power occurs in the upper offsets. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN SEM Fetch Spectrum

Fetches the spectrum and mask traces.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN SEM Fetch Spectrum' src='rfmxwlan_sem_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Spectrum returns the spectrum trace. x0 returns the start frequency. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns an array of power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns an array of power measured at each frequency bin. This value is expressed in dBm. |
|  | Composite Mask returns the SEM measurement mask trace. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns an array of mask level values for each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns an array of mask level values for each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_send_software_edge_trigger.html language=enus -->
## TOPIC 00080: RFmxWLAN Send Software Edge Trigger (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_send_software_edge_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_send_software_edge_trigger.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Send Software Edge Trigger (VI)

Owning Palette:

Configuration

Sends a trigger to the device when you use the [RFmxWLAN Configure Trigger](rfmxwlan_configure_trigger.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxWLAN Initiate VI.

[IMAGE alt='RFmxWLAN Send Software Edge Trigger' src='rfmxwlan_send_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_txp_configure_averaging.html language=enus -->
## TOPIC 00081: RFmxWLAN TXP Configure Averaging (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_txp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_txp_configure_averaging.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN TXP Configure Averaging (VI)

Owning Palette:

TXP

Configures averaging for the measurement.

[IMAGE alt='RFmxWLAN TXP Configure Averaging' src='rfmxwlan_txp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the TXP measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_txp_configure_burst_detection_enabled.html language=enus -->
## TOPIC 00082: RFmxWLAN TXP Configure Burst Detection Enabled (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_txp_configure_burst_detection_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_txp_configure_burst_detection_enabled.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN TXP Configure Burst Detection Enabled (VI)

Owning Palette:

TXP

Configures burst detection for the TXP measurement.

[IMAGE alt='RFmxWLAN TXP Configure Burst Detection Enabled' src='rfmxwlan_txp_configure_burst_detection_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Burst Detection Enabled specifies whether the measurement detects the start and the end of a WLAN packet automatically. The default value is True. False (0) Disables burst detection. True (1) Enables burst detection. |
| False (0) | Disables burst detection. |
| True (1) | Enables burst detection. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_txp_configure_maximum_measurement_interval.html language=enus -->
## TOPIC 00083: RFmxWLAN TXP Configure Maximum Measurement Interval (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_txp_configure_maximum_measurement_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_txp_configure_maximum_measurement_interval.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN TXP Configure Maximum Measurement Interval (VI)

Owning Palette:

TXP

Configures the maximum measurement interval for the TXP measurement.

[IMAGE alt='RFmxWLAN TXP Configure Maximum Measurement Interval' src='rfmxwlan_txp_configure_maximum_measurement_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Maximum Measurement Interval specifies the maximum measurement interval. This value is expressed in seconds. When you set the TXP Burst Detection Enabled property to True, the measurement interval used is equal to the smaller of the duration of the WLAN packet under analysis or the value you set for this parameter. The default value is 0.001. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_txp_fetch.html language=enus -->
## TOPIC 00084: RFmxWLAN TXP Fetch (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_txp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_txp_fetch.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN TXP Fetch (VI)

Owning Palette:

Fetch

Fetches the TXP measurement results.

#### RFmxWLAN TXP Fetch Measurement

Returns the average power and the peak power of the signal over which power measurements are performed.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN TXP Fetch Measurement' src='rfmxwlan_txp_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Average Power Mean returns the average power of the acquired signal. This value is expressed in dBm. When you set the TXP Averaging Enabled property to True, this parameter returns the mean of the average power computed for each averaging count. |
|  | Peak Power Maximum returns the peak power of the acquired signal. This value is expressed in dBm. When you set the TXP Averaging Enabled property to True, this parameter returns the maximum of the peak power computed for each averaging count. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxWLAN TXP Fetch Power Trace

Returns the power versus time trace.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxWLAN TXP Fetch Power Trace' src='rfmxwlan_txp_fetch_power_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. |
|  | Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Power returns the power versus time trace. x0 returns the trace start time. This value is expressed in seconds. dx returns the sampling interval. This value is expressed in seconds. y returns an array of measured signal power. This value is expressed in dBm. |
|  | x0 returns the trace start time. This value is expressed in seconds. |
|  | dx returns the sampling interval. This value is expressed in seconds. |
|  | y returns an array of measured signal power. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/rfmxwlan_wait_for_measurement_complete.html language=enus -->
## TOPIC 00085: RFmxWLAN Wait for Measurement Complete (VI)

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/rfmxwlan_wait_for_measurement_complete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/rfmxwlan_wait_for_measurement_complete.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmxWLAN Wait for Measurement Complete (VI)

Owning Palette:

Utility

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='RFmxWLAN Wait for Measurement Complete' src='rfmxwlan_wait_for_measurement_complete.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/sem_array_pal.html language=enus -->
## TOPIC 00086: SEM Array VIs

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/sem_array_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/sem_array_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

SEM Array VIs

Owning Palette:

SEM

Use the array VIs on this palette to configure adjacent channel power (SEM) measurements. You can use the RFmxWLAN Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN SEM Configure Offset Frequency (Array) | Configures the array of offset start and stop frequencies and specifies whether the offsets are present on one side, or on both the sides of the carrier when you set the SEM Mask Type property to Custom. |
| RFmxWLAN SEM Configure Offset Relative Limit (Array) | Configures an array of relative mask limits corresponding the start and stop frequencies of the offsets when you set the SEM Mask Type property to Custom. The relative limits are relative to the peak power of the carrier. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/sem_pal.html language=enus -->
## TOPIC 00087: SEM

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/sem_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/sem_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

SEM

Owning Palette:

Configuration

Use the VIs on this palette to configure SEM measurement. You can use the [RFmxWLAN Property Node](rfmxwlan_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN SEM Configure Averaging | Configures averaging for the measurement. |
| RFmxWLAN SEM Configure Sweep Time | Configures the sweep time. |
| RFmxWLAN SEM Configure Span | Configures the frequency range around the center frequency to be acquired for the SEM measurement. |
| RFmxWLAN SEM Configure Mask Type | Configures the mask type for the SEM measurement. |
| RFmxWLAN SEM Configure Number of Offsets | Configures the number of offset segments for the SEM measurement when you set the SEM Mask Type property to Custom. |

| Subpalette | Description |
| --- | --- |
| SEM Array VIs | Use the array VIs on this palette to configure adjacent channel power (SEM) measurements. You can use the RFmxWLAN Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/txp_pal.html language=enus -->
## TOPIC 00088: TXP

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/txp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/txp_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

TXP

Owning Palette:

Configuration

Use the VIs on this palette to configure TXP measurement. You can use the [RFmxWLAN Property Node](rfmxwlan_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN TXP Configure Averaging | Configures averaging for the measurement. |
| RFmxWLAN TXP Configure Maximum Measurement Interval | Configures the maximum measurement interval for the TXP measurement. |
| RFmxWLAN TXP Configure Burst Detection Enabled | Configures burst detection for the TXP measurement. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/utility_pal.html language=enus -->
## TOPIC 00089: Utility

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/utility_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

Utility

Owning Palette:

RFmx WLAN VIs

Use the VIs on this palette to configure RFmxWLAN utilities.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN Commit | Commits settings to the hardware. Calling this VI is optional. RFmxWLAN commits settings to the hardware when you call the RFmxWLAN Initiate VI. |
| RFmxWLAN Reset to Default | Resets a signal to the default values. |
| RFmxWLAN Wait for Measurement Complete | Waits for the specified number for seconds for all the measurements to complete. |
| RFmxWLAN Wait for Measurement Complete | Waits for the specified number for seconds for all the measurements to complete. |
| RFmxWLAN Check Measurement Status | Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |

<!--NI_TOPIC bundle=rfmx-wlan-vi path=rfmxwlanvi/wlan_pal.html language=enus -->
## TOPIC 00090: RFmx WLAN VIs

- bundle_id: `rfmx-wlan-vi`
- source_path: `rfmxwlanvi/wlan_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-vi/raw/resource/enus/rfmxwlanvi/wlan_pal.html
- document_id: `rfmx-wlan-vi`
- page_type: `leaf`
- content_type: ``

RFmx WLAN VIs

Use the VIs on this palette to perform WLAN measurements. You can use the [RFmxWLAN Property Node](../rfmxwlanvi/rfmxwlan_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxWLAN Select Measurement | Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. |
| RFmxWLAN Initiate | Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the RFmxWLAN Wait for Measurement Complete VI or RFmxWLAN Check Measurement Status VI. |
| RFmxWLAN Property Node | Gets (reads), sets (writes), or resets (sets to default value) RFmxWLAN properties. |

| Subpalette | Description |
| --- | --- |
| Configuration | Use the VIs on this palette to configure various parameters for RFmxWLAN measurements. |
| Fetch | Use the VIs on this palette to fetch WLAN measurement results and traces. You can use the RFmxWLAN Property Node to configure additional properties. |
| Utility | Use the VIs on this palette to configure RFmxWLAN utilities. |
| Build String | Use the VIs on this palette to create strings for configurations and results that require a selector string. |
| Advanced | Use the VIs on this palette to use advanced features. |
