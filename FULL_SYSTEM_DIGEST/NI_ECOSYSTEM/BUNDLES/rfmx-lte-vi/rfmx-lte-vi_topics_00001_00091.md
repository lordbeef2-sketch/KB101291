# NI DOCUMENT BUNDLE: rfmx-lte-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-lte-vi start=1 end=91 -->
<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/ch_configuration_pal.html language=enus -->
## TOPIC 00001: Ch Configuration

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/ch_configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/ch_configuration_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

Ch Configuration

Owning Palette:

Configuration

Use the VIs on this palette to configure channel parameters. You can also use the [RFmxLTE Property Node](../rfmxltevi/rfmxlte_property_node.html) to configure additional properties.

| Subpalette | Description |
| --- | --- |
| Uplink | Use the VIs on this palette to configure uplink channel specific parameters. You can use the RFmxLTE Property Node to configure additional properties. |
| Downlink | Use the VIs on this palette to configure downlink channel specific parameters. You can use the RFmxLTE Property Node to configure additional properties. |
| Sidelink | Use the VIs on this palette to configure sidelink channel specific parameters. You can use the RFmxLTE Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/chp_pal.html language=enus -->
## TOPIC 00002: CHP

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/chp_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/chp_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

CHP

Owning Palette:

Configuration

Use the VIs on this palette to configure channel power (CHP) measurements. You can also use the [RFmxLTE Property Node](../rfmxltevi/rfmxlte_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxLTE CHP Configure Averaging | Configures averaging for the CHP measurement. |
| RFmxLTE CHP Configure Sweep Time | Configures the sweep time. |
| RFmxLTE CHP Configure Integration Bandwidth Type | Configures the type of integration bandwidth (IBW), which selects one of the frequency ranges over which the CHP is measured. Refer to the LTE Channel Power (CHP) topic for more information. |
| RFmxLTE CHP Configure RBW Filter | Configures the RBW filter. |
| RFmxLTE CHP Validate Noise Calibration Data | Indicates whether calibration data is valid for the configuration specified by the signal name in the Selector string parameter. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/configuration_array_vis_pal.html language=enus -->
## TOPIC 00003: Array

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/configuration_array_vis_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/configuration_array_vis_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

Array

Owning Palette:

Configuration

Use the array VI on this palette to configure the component carrier measurements. You can also use the RFmxLTE Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxLTE Configure Component Carrier (Array) | Configures an array of bandwidths, carrier offset frequencies, and cell IDs of component carriers. Use "subblock<n>" as the selector string to configure this VI. |
| RFmxLTE Configure Downlink Test Model (Array) | Configures an array of the EUTRA test model type for each component carrier within the subblock. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/configuration_pal.html language=enus -->
## TOPIC 00004: Configuration

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/configuration_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

Configuration

Owning Palette:

RFmx LTE VIs

Use the VIs on this palette to configure RFmxLTE measurements. You can use the [RFmxLTE Property Node](../rfmxltevi/rfmxlte_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxLTE Configure RF | Configures the RF properties of the signal specified by the selector string. |
| RFmxLTE Configure Frequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| RFmxLTE Configure Reference Level | Configures the reference level, which represents the maximum expected power of an RF input signal. |
| RFmxLTE Configure External Attenuation | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. |
| RFmxLTE Auto Level | Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to calculate an approximate setting for the reference level. |
| RFmxLTE Configure Trigger | Configures the Reference Trigger to use to acquire the signal. |
| RFmxLTE Send Software Edge Trigger | Sends a trigger to the device when you use the RFmxLTE Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. |
| RFmxLTE Configure Link Direction | Configures the link direction of the signal being measured. |
| RFmxLTE Configure Duplex Scheme | Configures the duplexing technique of the signal being measured. |
| RFmxLTE Configure eNodeB Category | Configures the eNodeB category of the signal being measured. |
| RFmxLTE Configure Number of DUT Antennas | Configures the number of physical antennas used for transmission by the DUT in a MIMO setup. |
| RFmxLTE Configure Transmit Antenna to Analyze | Configures the current physical antenna of the DUT in the MIMO setup being tested. |
| RFmxLTE Configure Number of Subblocks | Configures the number of subblocks. |
| RFmxLTE Configure Band | Configures the evolved universal terrestrial radio access (E-UTRA) operating frequency band of a subblock. Use "subblock<n>" as the selector string to configure this VI. |
| RFmxLTE Configure Component Carrier Spacing | Configures the Component Carrier Spacing Type and Component Carrier at Center Frequency parameters, which help to set the spacing between adjacent component carriers within a subblock. Use "subblock<n>" as the selector string to configure this VI. Refer to the Channel Spacing and Carrier Frequency Offset Definition and Reference Frequency topics for more information about carrier spacing. |
| RFmxLTE Configure Number of Component Carriers | Configures the number of component carriers within a subblock. Use "subblock<n>" as the selector string to configure this VI. |
| RFmxLTE Configure Component Carrier | Configures the Component Carrier Bandwidth, Component Carrier Frequency, and Cell ID of the component carrier. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxLTE Configure Auto Resource Block Detection Enabled | Configures whether the values of the PUSCH Mod Type, PUSCH Num RB Clusters, PUSCH RB Offset, and PUSCH Num RBs properties are automatically detected by the measurement or if you specify the values of these properties. The measurement ignores this VI, when you set the Link Direction property to Downlink. |
| RFmxLTE Configure Auto DMRS Detection Enabled | Configures whether the demodulation reference signal (DMRS) parameters are configured by a user or automatically detected by a measurement. |
| RFmxLTE Configure Downlink Test Model | Configures the EUTRA test model type. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxLTE Configure Downlink Auto Cell ID Detection Enabled | Configures whether the cell ID is configured by the user or auto-detected by the measurement. |
| RFmxLTE Configure eMTC Analysis Enabled | Configures whether the component carrier contains an enhanced machine type communications (Cat-M1 or Cat-M2) transmission. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxLTE Build Subblock String | Creates a subblock string to use as a selector string with the subblock configuration or fetch properties and VIs. |
| RFmxLTE Build Carrier String | Creates a carrier string to use as a selector string with the SEM and ACP carrier configurations or fetch properties and VIs. |
| RFmxLTE Build Cluster String | Creates a cluster string to use as a selector string with the ModAcc cluster configuration or fetch properties and VIs. |

| Subpalette | Description |
| --- | --- |
| Ch Configuration | Use the VIs on this palette to configure channel parameters. You can also use the RFmxLTE Property Node to configure additional properties. |
| NB-loT | Use the VIs on this palette to configure NB-loT measurement. You can use the RFmxLTE Property Node to configure additional properties. |
| Array | Use the array VI on this palette to configure the component carrier measurements. You can also use the RFmxLTE Property Node to configure additional properties. |
| ModAcc | Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements. You can also use the RFmxLTE Property Node to configure additional properties. |
| ACP | Use the VIs on this palette to configure ACP measurements. You can use the RFmxLTE Property Node to configure additional properties. |
| CHP | Use the VIs on this palette to configure channel power (CHP) measurements. You can also use the RFmxLTE Property Node to configure additional properties. |
| OBW | Use the VIs on this palette to configure occupied bandwidth (OBW) measurements. You can also use the RFmxLTE Property Node to configure additional properties. |
| SEM | Use the VIs on this palette to configure SEM measurements. You can also use the RFmxLTE Property Node to configure additional properties. |
| PVT | Use the VIs on this palette to configure the power versus time (PVT) measurements. You can also use the RFmxLTE Property Node to configure additional properties. |
| SlotPhase | Use the VIs on this palette to configure the SlotPhase measurements. You can also use the RFmxLTE Property Node to configure additional properties. |
| SlotPower | Use the VIs on this palette to configure the SlotPower measurements. You can also use the RFmxLTE Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/downlink_pal.html language=enus -->
## TOPIC 00005: Downlink

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/downlink_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/downlink_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

Downlink

Owning Palette:

Ch Configuration

Use the VIs on this palette to configure downlink channel specific parameters. You can use the [RFmxLTE Property Node](../rfmxltevi/rfmxlte_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxLTE Configure Downlink Channel Configuration Mode | Configures the downlink channel configuration mode. |
| RFmxLTE Configure Downlink Auto Channel Detection | Configures whether the values of physical downlink shared channel (PDSCH) parameters, control channel signal powers, and physical control format indicator channel (PCFICH) CFI are configured by a user or auto-detected by the measurement. The measurement ignores this VI, when you set the Link Direction property to Uplink. |
| RFmxLTE Configure Cell Specific Ratio | Configures the cell specific ratio parameter. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxLTE Configure Downlink Synchronization Signal | Configures the synchronization signal power relative to the cell-specific reference signal. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxLTE Configure PBCH | Configures the power of physical broadcast channel (PBCH) power relative to the cell-specific reference signal. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxLTE Configure PDCCH | Configures the physical downlink control channel (PDCCH) power relative to the cell-specific reference signal. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxLTE Configure Downlink Number of Subframes | Configures the number of unique subframes that are transmitted from the DUT. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxLTE Configure PCFICH | Configures the CFI and Power parameters of the physical control format indicator channel (PCFICH). Use "subframe<l>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subframe<l>" as the selector string to configure this VI. |
| RFmxLTE Configure PHICH | Configures the Resource, Duration, and Power parameters of the physical hybrid-ARQ indicator channel (PHICH). Use "subframe<l>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subframe<l>" as the selector string to configure this VI. |
| RFmxLTE Configure Number of PDSCH Channels | Configures the number of different physical downlink shared channel (PDSCH) allocations in a subframe. Use "subframe<l>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subframe<l>" as the selector string to configure this VI. |
| RFmxLTE Configure PDSCH | Configures the codeword0 modulation type, resource block, and relative power of a physical downlink shared channel (PDSCH) allocation. Use "PDSCH<m>" or "subframe<l>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subframe<l>/PDSCH<m>" as the selector string to configure this VI. |
| RFmxLTE Build Subblock String | Creates a subblock string to use as a selector string with the subblock configuration or fetch properties and VIs. |
| RFmxLTE Build Carrier String | Creates a carrier string to use as a selector string with the SEM and ACP carrier configurations or fetch properties and VIs. |
| RFmxLTE Build Subframe String | Creates a subframe string to use as a selector string with the configuration or fetch properties and VIs. |
| RFmxLTE Build PDSCH String | Creates a PDSCH string to use as a selector string with the configuration or fetch properties and VIs. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/fetch_pal.html language=enus -->
## TOPIC 00006: Fetch

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/fetch_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/fetch_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

Fetch

Owning Palette:

RFmx LTE VIs

Use the VIs on this palette to fetch measurement results and traces.

| Palette Object | Description |
| --- | --- |
| RFmxLTE ModAcc Fetch | Fetches the ModAcc measurement results. |
| RFmxLTE ACP Fetch | Fetches ACP measurement results. |
| RFmxLTE CHP Fetch | Fetches the CHP measurements. |
| RFmxLTE OBW Fetch | Fetches the OBW measurements. |
| RFmxLTE SEM Fetch | Fetches the SEM measurements. |
| RFmxLTE PVT Fetch | Fetches the PVT measurements. |
| RFmxLTE SlotPhase Fetch | Fetches the SlotPhase measurement results. |
| RFmxLTE SlotPower Fetch | Fetches the SlotPower measurement results. |

| Subpalette | Description |
| --- | --- |
| Build String | Use the VIs on this palette to create strings for configurations and results that require a selector string. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/lte_pal.html language=enus -->
## TOPIC 00007: RFmx LTE VIs

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/lte_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/lte_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmx LTE VIs

Use the VIs on this palette to perform LTE measurements. You can use the [RFmxLTE Property Node](../rfmxltevi/rfmxlte_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxLTE Select Measurement | Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. |
| RFmxLTE Initiate | Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the RFmxLTE Wait for Measurement Complete VI or RFmxLTE Check Measurement Status VI. |
| RFmxLTE Property Node | Gets (reads), sets (writes), or resets (sets to default value) RFmxLTE properties. |

| Subpalette | Description |
| --- | --- |
| Configuration | Use the VIs on this palette to configure RFmxLTE measurements. You can use the RFmxLTE Property Node to configure additional properties. |
| Fetch | Use the VIs on this palette to fetch measurement results and traces. |
| Utility | Use the VIs on this palette to configure RFmx LTE utilities. |
| Build String | Use the VIs on this palette to create strings for configurations and results that require a selector string. |
| Advanced | Use the VIs on this palette to use advanced features. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/modacc_pal.html language=enus -->
## TOPIC 00008: ModAcc

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/modacc_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/modacc_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

ModAcc

Owning Palette:

Configuration

Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements. You can also use the [RFmxLTE Property Node](../rfmxltevi/rfmxlte_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxLTE ModAcc Configure Averaging | Configures averaging for the ModAcc measurement. |
| RFmxLTE ModAcc Configure Synchronization Mode and Interval | Configures the Synchronization Mode, the Measurement Offset, and the Measurement Length parameters of the ModAcc measurement. Refer to the LTE Modulation Accuracy (ModAcc) topic for more information about ModAcc measurements. |
| RFmxLTE ModAcc Configure EVM Unit | Configures the units of the EVM results. |
| RFmxLTE ModAcc Configure FFT Window Offset | Configures the position of the FFT window that is used to calculate the EVM. |
| RFmxLTE ModAcc Configure Common Clock Source Enabled | Configures the Reference Clock and specifies whether same Reference Clock is used for local oscillator and D/A converter. The modacc measurement ignores this VI, when you set the Link Direction property to Downlink. |
| RFmxLTE ModAcc Configure FFT Window Position | Configures the FFT window position used for an EVM calculation. Refer to the LTE Modulation Accuracy (ModAcc) topic for more information about FFT window position. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/nb-iot_pal.html language=enus -->
## TOPIC 00009: NB-loT

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/nb-iot_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/nb-iot_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

NB-loT

Owning Palette:

Configuration

Use the VIs on this palette to configure NB-loT measurement. You can use the [RFmxLTE Property Node](../rfmxltevi/rfmxlte_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxLTE Configure NB-IoT Component Carrier | Configures the Ncell ID and Uplink Subcarrier Spacing parameters for the NB-IoT signal. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxLTE Configure NPUSCH Format | Configures the format of the narrowband physical uplink shared channel (NPUSCH). Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxLTE Configure NPUSCH Tones | Configures the values of Tone Offset, Number of Tones, and Modulation Type parameters for NPUSCH channel. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxLTE Configure Auto NPUSCH Channel Detection Enabled | Configures whether the values of the NPUSCH Tone Offset, NPUSCH Num Tones, and NPUSCH Mod Type properties for the NPUSCH channel are auto-detected by the measurement or specified by you. |
| RFmxLTE Configure NPUSCH Starting Slot | Configures the starting slot of the NPUSCH burst. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |
| RFmxLTE Configure NPUSCH DMRS | Configures the base sequence mode, base sequence index, cyclic shift, delta sequence shift of the narrowband physical uplink shared channel (NPUSCH) DMRS and specifies whether group hopping is enabled. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/obw_pal.html language=enus -->
## TOPIC 00010: OBW

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/obw_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/obw_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

OBW

Owning Palette:

Configuration

Use the VIs on this palette to configure occupied bandwidth (OBW) measurements. You can also use the [RFmxLTE Property Node](../rfmxltevi/rfmxlte_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxLTE OBW Configure Averaging | Configures averaging for the OBW measurement. |
| RFmxLTE OBW Configure Sweep Time | Configures the sweep time. |
| RFmxLTE OBW Configure RBW Filter | Configures the RBW filter. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/pvt_pal.html language=enus -->
## TOPIC 00011: PVT

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/pvt_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/pvt_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

PVT

Owning Palette:

Configuration

Use the VIs on this palette to configure the power versus time (PVT) measurements. You can also use the [RFmxLTE Property Node](../rfmxltevi/rfmxlte_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxLTE PvT Configure Averaging | Configures averaging for the power versus time (PVT) measurement. |
| RFmxLTE PvT Configure Measurement Method | Configures the method for performing the power versus time (PVT) measurement. Refer to the LTE PVT (Power Vs Time) Measurement topic for more information about measurement method. |
| RFmxLTE PVT Configure OFF Power Exclusion Periods | Configures the OFF power exclusion periods for the power versus time (PVT) measurement. Refer to the LTE PVT (Power Vs Time) Measurement topic for more information about OFF power exclusion periods. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_abort_measurements.html language=enus -->
## TOPIC 00012: RFmxLTE Abort Measurements (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_abort_measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_abort_measurements.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Abort Measurements (VI)

Owning Palette:

Advanced

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxLTE Initiate](rfmxlte_initiate.html) VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='RFmxLTE Abort Measurements' src='rfmxlte_abort_measurements.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_acp_configure_averaging.html language=enus -->
## TOPIC 00013: RFmxLTE ACP Configure Averaging (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_acp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_acp_configure_averaging.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ACP Configure Averaging (VI)

Owning Palette:

ACP

Configures averaging for the ACP measurement.

[IMAGE alt='RFmxLTE ACP Configure Averaging' src='rfmxlte_acp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_acp_configure_configurable_number_of_offsets_enabled.html language=enus -->
## TOPIC 00014: RFmxLTE ACP Configure Configurable Number of Offsets Enabled (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_acp_configure_configurable_number_of_offsets_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_acp_configure_configurable_number_of_offsets_enabled.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ACP Configure Configurable Number of Offsets Enabled (VI)

Owning Palette:

ACP

Configures whether the number of offsets will be computed by the measurement or configured by the user.

[IMAGE alt='RFmxLTE ACP Configure Configurable Number of Offsets Enabled' src='rfmxlte_acp_configure_configurable_number_of_offsets_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Configurable Number of Offsets Enabled specifies whether the number of offsets is computed by measurement or configured by you. When the carrier bandwidth is 200 kHz or the Link Direction is Downlink, the default value is False. The default value is True, otherwise. Note Incase of downlink, this property is applicable only for number of EUTRA offsets. For the number of UTRA offsets, only 3GPP specification defined values are supported. False (0) Measurement will set the number of offsets. True (1) Measurement will use the user configured value for number of offsets. |
|  | Note Incase of downlink, this property is applicable only for number of EUTRA offsets. For the number of UTRA offsets, only 3GPP specification defined values are supported. |
| False (0) | Measurement will set the number of offsets. |
| True (1) | Measurement will use the user configured value for number of offsets. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_acp_configure_measurement_method.html language=enus -->
## TOPIC 00015: RFmxLTE ACP Configure Measurement Method (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_acp_configure_measurement_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_acp_configure_measurement_method.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ACP Configure Measurement Method (VI)

Owning Palette:

ACP

Configures the method for performing the ACP measurement.

[IMAGE alt='RFmxLTE ACP Configure Measurement Method' src='rfmxlte_acp_configure_measurement_method.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Method specifies the method for performing the ACP measurement. The default value is Normal. Normal (0) The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. Dynamic Range (1) The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668 Sequential FFT (2) The ACP measurement acquires I/Q samples specified by the ACP Sweep Time property. These samples are divided into smaller chunks defined by the ACP Sequential FFT Size property, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used. Sequential FFT method should be used for the following scenarios. While performing fast ACP measurements by utilizing smaller FFT sizes. However, accuracy of the results may be reduced. When measuring signals with time-varying spectral characteristics, sequential FFT with overlap mode set to Automatic should be used. For accurate power measurements when the power characteristics of the signal vary over time averaging is allowed. The following properties have limited support when you set the ACP Measurement Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Sweep Time Auto False ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads 1 ACP Amplitude Correction Type RF Center Frequency Note For multi-span FFT, the averaging count should be 1. |
| Normal (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| Dynamic Range (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668 |
| Sequential FFT (2) | The ACP measurement acquires I/Q samples specified by the ACP Sweep Time property. These samples are divided into smaller chunks defined by the ACP Sequential FFT Size property, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used. Sequential FFT method should be used for the following scenarios. While performing fast ACP measurements by utilizing smaller FFT sizes. However, accuracy of the results may be reduced. When measuring signals with time-varying spectral characteristics, sequential FFT with overlap mode set to Automatic should be used. For accurate power measurements when the power characteristics of the signal vary over time averaging is allowed. The following properties have limited support when you set the ACP Measurement Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Sweep Time Auto False ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads 1 ACP Amplitude Correction Type RF Center Frequency Note For multi-span FFT, the averaging count should be 1. |
| Property | Supported Value |
| ACP RBW Auto | True |
| ACP RBW Filter Type | FFT Based |
| ACP Sweep Time Auto | False |
| ACP Averaging Count | >=1 |
| ACP Noise Comp Enabled | False |
| ACP Num Analysis Threads | 1 |
| ACP Amplitude Correction Type | RF Center Frequency |
|  | Note For multi-span FFT, the averaging count should be 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_acp_configure_noise_compensation_enabled.html language=enus -->
## TOPIC 00016: RFmxLTE ACP Configure Noise Compensation Enabled (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_acp_configure_noise_compensation_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_acp_configure_noise_compensation_enabled.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ACP Configure Noise Compensation Enabled (VI)

Owning Palette:

ACP

Configures compensation of the channel powers for the inherent noise floor of the signal analyzer.

[IMAGE alt='RFmxLTE ACP Configure Noise Compensation Enabled' src='rfmxlte_acp_configure_noise_compensation_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Noise Compensation Enabled specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. The default value is False. False (0) Disables compensation of the channel powers for the noise floor of the signal analyzer. True (1) Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842 |
| False (0) | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| True (1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842 |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_acp_configure_number_of_eutra_offsets.html language=enus -->
## TOPIC 00017: RFmxLTE ACP Configure Number of EUTRA Offsets (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_acp_configure_number_of_eutra_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_acp_configure_number_of_eutra_offsets.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ACP Configure Number of EUTRA Offsets (VI)

Owning Palette:

ACP

Configures the number of evolved universal terrestrial radio access adjacent channels of the subblock, when you set the [ACP Configurable Number of Offset Enabled](/csh?topicname=rfmxlteprop/attr301044.html) property to **True**.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE ACP Configure Number of EUTRA Offsets' src='rfmxlte_acp_configure_number_of_eutra_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of EUTRA Offsets specifies the number of E-UTRA adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled property to True. In case of non-contiguous carrier aggregation, the configured value will be used only for the outer offsets and the offset channels in the gap region are defined as per the 3GPP specification. Offset integration bandwidth and offset power reference for the outer E-UTRA offsets are set according to the value of ACP EUTRA Offset Definition property. The default value is 0, when carrier bandwidth is 200 kHz. The default value is 2 for downlink and 1 for uplink, otherwise. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_acp_configure_number_of_gsm_offsets.html language=enus -->
## TOPIC 00018: RFmxLTE ACP Configure Number of GSM Offsets (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_acp_configure_number_of_gsm_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_acp_configure_number_of_gsm_offsets.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ACP Configure Number of GSM Offsets (VI)

Owning Palette:

ACP

Configures the number of GSM adjacent channels of the subblock, when you set the [ACP Configurable Number of Offset Enabled](/csh?topicname=rfmxlteprop/attr301044.html) property to **True**.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE ACP Configure Number of GSM Offsets' src='rfmxlte_acp_configure_number_of_gsm_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of GSM Offsets specifies the number of GSM adjacent channel offsets to be configured when you set the CC Bandwidth to 200.0 k and when you set the ACP Configurable Number of Offset Enabled property to True. The frequency offset from the center of NB-IOT carrier to the center of the first offset is 300 kHz as defined in the 3GPP specification. The center of every other offset is placed at 200 kHz from the previous offset's center. The default value is 1, when you set the CC Bandwidth property to is 200.0 k. The default value is 0, otherwise. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_acp_configure_number_of_utra_offsets.html language=enus -->
## TOPIC 00019: RFmxLTE ACP Configure Number of UTRA Offsets (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_acp_configure_number_of_utra_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_acp_configure_number_of_utra_offsets.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ACP Configure Number of UTRA Offsets (VI)

Owning Palette:

ACP

Configures the number of universal terrestrial radio access (UTRA) adjacent channels of the subblock, when you set the [ACP Configurable Number of Offset Enabled](/csh?topicname=rfmxlteprop/attr301044.html) property to **True**.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE ACP Configure Number of UTRA Offsets' src='rfmxlte_acp_configure_number_of_utra_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of UTRA Offsets specifies the number of UTRA adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled property to True. In case of downlink, only 3GPP specification defined values are supported. In case of non-contiguous carrier aggregation, the configured value will be used only for the outer offsets and the offset channels in the gap region are defined as per the 3GPP specification. Offset power reference for the outer UTRA offsets are set according to the value of ACP EUTRA Offset Definition property. The default value is 1, when carrier bandwidth is 200 kHz. The default value is 0, when the band is 46 or when you set the Duplex Scheme property to LAA. The default value is 2 for all other configurations. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_acp_configure_power_units.html language=enus -->
## TOPIC 00020: RFmxLTE ACP Configure Power Units (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_acp_configure_power_units.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_acp_configure_power_units.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ACP Configure Power Units (VI)

Owning Palette:

ACP

Configures the units for absolute power.

[IMAGE alt='RFmxLTE ACP Configure Power Units' src='rfmxlte_acp_configure_power_units.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Power Units specifies the units for absolute power. The default value is dBm. dBm (0) The absolute powers are reported in dBm. dBm/Hz (1) The absolute powers are reported in dBm/Hz. |
| dBm (0) | The absolute powers are reported in dBm. |
| dBm/Hz (1) | The absolute powers are reported in dBm/Hz. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_acp_configure_rbw_filter.html language=enus -->
## TOPIC 00021: RFmxLTE ACP Configure RBW Filter (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_acp_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_acp_configure_rbw_filter.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ACP Configure RBW Filter (VI)

Owning Palette:

ACP

Configures the RBW filter.

[IMAGE alt='RFmxLTE ACP Configure RBW Filter' src='rfmxlte_acp_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. The default value is True. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
|  | RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 30 kHz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is FFT Based. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_acp_configure_sweep_time.html language=enus -->
## TOPIC 00022: RFmxLTE ACP Configure Sweep Time (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_acp_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_acp_configure_sweep_time.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ACP Configure Sweep Time (VI)

Owning Palette:

ACP

Configures the sweep time.

[IMAGE alt='RFmxLTE ACP Configure Sweep Time' src='rfmxlte_acp_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement uses a sweep time of 1 ms. |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement uses a sweep time of 1 ms. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_acp_fetch.html language=enus -->
## TOPIC 00023: RFmxLTE ACP Fetch (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_acp_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_acp_fetch.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ACP Fetch (VI)

Owning Palette:

Fetch

Fetches ACP measurement results.

#### RFmxLTE ACP Fetch Total Aggregated Power

Fetches the sum of powers in all the subblocks.

[IMAGE alt='RFmxLTE ACP Fetch Total Aggregated Power' src='rfmxlte_acp_fetch_total_aggregated_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Aggregated Power returns the sum of powers of all the frequency bins over the integration bandwidth of subblock. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power in the subblock gaps. When you set the ACP Pwr Units property to dBm, the parameter returns the total integrated power in dBm of all the active carriers measured. When you set the ACP Pwr Units property to dBm/Hz, the parameter returns the power spectral density in dBm/Hz based on the power in all the active carriers measured. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE ACP Fetch Subblock Measurement

Returns the power, integration bandwidth, and center frequency of the subblock.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxLTE ACP Fetch Subblock Measurement' src='rfmxlte_acp_fetch_subblock_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Subblock Power returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. When you set the ACP Pwr Units property to dBm, the parameter returns the total subblock power in dBm of all the active carriers measured over the subblock. When you set the ACP Pwr Units property to dBm/Hz, the parameter returns the power spectral density in dBm/Hz based on the power in all the active carriers measured over the subblock. |
|  | Integration Bandwidth returns the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within a subblock. This value is expressed in Hz. |
|  | Frequency returns the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE ACP Fetch Component Carrier Measurement

Fetches the ACP component carrier measurement.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxLTE ACP Fetch Component Carrier Measurement' src='rfmxlte_acp_fetch_component_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxLTE Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns the power measured over the integration bandwidth of the carrier. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | Relative Power returns the component carrier power relative to its subblock power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE ACP Fetch Component Carrier Measurement (Array)

Returns an array of the absolute and relative powers of the component carriers. The relative power is relative to the subblock power.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxLTE ACP Fetch Component Carrier Measurement (Array)' src='rfmxlte_acp_fetch_component_carrier_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Power returns the array of powers measured over the integration bandwidths of the carriers. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | Relative Power returns the array of component carrier powers relative to their subblock powers measured over the integration bandwidths of the component carriers in the subblock. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE ACP Fetch Offset Measurement

Returns the absolute and relative power of the lower and upper offset channel. The relative power is relative to subblock power.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this VI.

Refer to the *3GPP TS 36.521* specification for more information about the applicability of an offset channel. Refer to the [LTE Uplink Adjacent Channel Power](/csh?topicname=rfmxlte/lte_adjacent_channel_power.html) and [LTE Downlink Adjacent Channel Power](/csh?topicname=rfmxlte/lte_downlink_adjacent_channel_power.html) topics for more information.

[IMAGE alt='RFmxLTE ACP Fetch Offset Measurement' src='rfmxlte_acp_fetch_offset_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxLTE Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Lower Relative Power returns the power in lower (negative) offset channel relative to value returned by the ACP Results Total Aggregated Pwr property. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned. |
|  | Upper Relative Power returns the power in upper (positive) offset channel relative to the value returned by the ACP Results Total Aggregated Pwr property. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned. |
|  | Lower Absolute Power returns the lower offset channel power. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned. The offset channel power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | Upper Absolute Power returns the upper offset channel power. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned. The offset channel power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE ACP Fetch Offset Measurement (Array)

Returns an array of absolute and relative powers of the lower and upper offset channels. The relative power is relative to subblock power. The order of the offsets in the result array is universal terrestrial radio access (UTRA) (1, 2, ...m) and evolved universal terrestrial radio access (E-UTRA) (1, ..., n), where *m* and *n* are the number of UTRA offsets and the number of EUTRA offsets respectively.

Use "subblock<*n*>" as the selector string to read results from this VI.

Refer to the *3GPP TS 36.521* specification for more information about the applicability of an offset channel. Refer to the [LTE Uplink Adjacent Channel Power](/csh?topicname=rfmxlte/lte_adjacent_channel_power.html) and [LTE Downlink Adjacent Channel Power](/csh?topicname=rfmxlte/lte_downlink_adjacent_channel_power.html) topics for more information

[IMAGE alt='RFmxLTE ACP Fetch Offset Measurement (Array)' src='rfmxlte_acp_fetch_offset_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Lower Relative Power returns the array of power in lower (negative) offset channel relative to the value returned by the ACP Results Total Aggregated Pwr property. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned. |
|  | Upper Relative Power returns the array of powers in upper (positive) offset channel relative to the value returned by the ACP Results Total Aggregated Pwr property. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned. |
|  | Lower Absolute Power returns the array of lower offset channel power. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned. The offset channel power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | Upper Absolute Power returns the array of upper offset channel powers. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned. The offset channel power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE ACP Fetch Spectrum

Fetches the spectrum used for the ACP measurement.

[IMAGE alt='RFmxLTE ACP Fetch Spectrum' src='rfmxlte_acp_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the spectrum. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE ACP Fetch Relative Powers Trace

Fetches the relative powers trace for ACP measurement.

[IMAGE alt='RFmxLTE ACP Fetch Relative Powers Trace' src='rfmxlte_acp_fetch_relative_powers_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Relative Powers returns the array of traces of relative powers measured in each channel relative to total aggregated power. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the relative power measured in each channel relative to total aggregated power. This value is expressed in dB. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the relative power measured in each channel relative to total aggregated power. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE ACP Fetch Absolute Powers Trace

Fetches the absolute powers trace.

[IMAGE alt='RFmxLTE ACP Fetch Absolute Powers Trace' src='rfmxlte_acp_fetch_absolute_powers_trace.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Powers returns the trace of the measured integrated power in each channel. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the power measured in each channel. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the power measured in each channel. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_acp_validate_noise_calibration_data.html language=enus -->
## TOPIC 00024: RFmxLTE ACP Validate Noise Calibration Data (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_acp_validate_noise_calibration_data.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_acp_validate_noise_calibration_data.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ACP Validate Noise Calibration Data (VI)

Owning Palette:

ACP

Indicates whether calibration data is valid for the configuration specified by the signal name in the **Selector string** parameter.

[IMAGE alt='RFmxLTE ACP Validate Noise Calibration Data' src='rfmxlte_acp_validate_noise_calibration_data.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Noise Calibration Data Valid returns whether the calibration data is valid. False (0) Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. True (1) Returns true if the calibration data is present for the configuration specified by the signal name in the Selector string parameter. |
| False (0) | Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. |
| True (1) | Returns true if the calibration data is present for the configuration specified by the signal name in the Selector string parameter. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_analyze2.html language=enus -->
## TOPIC 00025: RFmxLTE Analyze2 (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_analyze2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_analyze2.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Analyze2 (VI)

Owning Palette:

Advanced

Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the Spectrum instance.

#### RFmxLTE Analyze (IQ, 1 Wfm)

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?topicname=rfmxinstrprop/attr27.html) property value is either **IQ** or **IQ or Spectral**.

When using the Analysis-Only mode in RFmxLTE, RFmx ignores RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmx LTE Commit VI. |
| --- | --- |

[IMAGE alt='RFmxLTE Analyze (IQ 1 Wfm)' src='rfmxlte_analyze_(iq_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". |
| --- | --- |
|  | IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 specifies the start time of the input Y array. This value is expressed in seconds. dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y specifies the array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | x0 specifies the start time of the input Y array. This value is expressed in seconds. |
|  | dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. |
|  | y specifies the array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE Analyze (Spectrum, 1 Wfm)

Performs the enabled measurements on the spectrum waveform that you specify in **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?topicname=rfmxinstrprop/attr27.html) property value is either **Spectral** or **IQ or Spectral**.

When using the Analysis-Only mode in RFmxLTE, RFmx ignores RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

|  | Note Query the Recommended Acquisition Type property from the RFmxInstr Property Node after calling the RFmx LTE Commit VI. |
| --- | --- |

[IMAGE alt='RFmxLTE Analyze (Spectrum 1 Wfm)' src='rfmxlte_analyze_(spectrum_1_wfm).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". |
| --- | --- |
|  | Spectrum specifies the data for a spectrum waveform including the start, delta, and actual values. x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx specifies the frequency interval between data points in the spectrum. y contains the real-value power spectrum. |
|  | x0 specifies the start frequency of the spectrum. This value is expressed in Hz. |
|  | dx specifies the frequency interval between data points in the spectrum. |
|  | y contains the real-value power spectrum. |
|  | Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_auto_level.html language=enus -->
## TOPIC 00026: RFmxLTE Auto Level (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_auto_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_auto_level.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Auto Level (VI)

Owning Palette:

Configuration

Examines the input signal to calculate the peak power level and sets it as the value of the [Reference Level](/csh?topicname=rfmxlteprop/attr300002.html) property. Use this VI to calculate an approximate setting for the reference level.

RFmxLTE Auto Level VI completes the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using [Auto Level Initial Ref Level](/csh?topicname=rfmxlteprop/attr30d000.html) property.

When using PXIe-5663, PXIe-5665, or PXIe-5668 devices, NI recommends that you set an appropriate value for mechanical attenuation before calling RFmxLTE Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='RFmxLTE Auto Level' src='rfmxlte_auto_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement Interval specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the signal analyzer. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Reference Level returns the estimated peak power level of the input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_build_carrier_string.html language=enus -->
## TOPIC 00027: RFmxLTE Build Carrier String (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_build_carrier_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_build_carrier_string.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Build Carrier String (VI)

Owning Palette:

Uplink

Creates a carrier string to use as a selector string with the SEM and ACP carrier configurations or fetch properties and VIs.

[IMAGE alt='RFmxLTE Build Carrier String' src='rfmxlte_build_carrier_string.gif']

|  | Carrier Number specifies the carrier number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_build_cluster_string.html language=enus -->
## TOPIC 00028: RFmxLTE Build Cluster String (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_build_cluster_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_build_cluster_string.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Build Cluster String (VI)

Owning Palette:

Uplink

Creates a cluster string to use as a selector string with the ModAcc cluster configuration or fetch properties and VIs.

[IMAGE alt='RFmxLTE Build Cluster String' src='rfmxlte_build_cluster_string.gif']

|  | Cluster Number specifies the cluster number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxLTE Build Carrier String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_build_offset_string.html language=enus -->
## TOPIC 00029: RFmxLTE Build Offset String (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_build_offset_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_build_offset_string.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Build Offset String (VI)

Owning Palette:

SEM

Creates an offset string to use as a selector string with SEM and ACP offset configuration or fetch properties and VIs.

[IMAGE alt='RFmxLTE Build Offset String' src='rfmxlte_build_offset_string.gif']

|  | Offset Number specifies the offset number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_build_pdsch_string.html language=enus -->
## TOPIC 00030: RFmxLTE Build PDSCH String (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_build_pdsch_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_build_pdsch_string.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Build PDSCH String (VI)

Owning Palette:

Downlink

Creates a PDSCH string to use as a selector string with the configuration or fetch properties and VIs.

[IMAGE alt='RFmxLTE Build PDSCH String' src='rfmxlte_build_pdsch_string.gif']

|  | PDSCH Number specifies the PDSCH channel number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, subblock number, carrier number, and subframe number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0/subframe0". Example: "subblock0/carrier0/subframe0" "signal::sig1/subblock0/carrier0/subframe0" "result::r1/subblock0/carrier0/subframe0" "signal::sig1/result::r1/subblock0/carrier0/subframe0" You can use the RFmxLTE Build Subframe String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_build_signal_string.html language=enus -->
## TOPIC 00031: RFmxLTE Build Signal String (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_build_signal_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_build_signal_string.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Build Signal String (VI)

Owning Palette:

Build String

Creates a selector string to use with configuration or fetch properties and VIs.

[IMAGE alt='RFmxLTE Build Signal String' src='rfmxlte_build_signal_string.gif']

|  | Result Name specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string). Example: "result::r1" "r1" |
| --- | --- |
|  | Signal Name specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Example: "signal::sig1" "sig1" |
|  | Selector String returns the selector string. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_build_subblock_string.html language=enus -->
## TOPIC 00032: RFmxLTE Build Subblock String (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_build_subblock_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_build_subblock_string.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Build Subblock String (VI)

Owning Palette:

Uplink

Creates a subblock string to use as a selector string with the subblock configuration or fetch properties and VIs.

[IMAGE alt='RFmxLTE Build Subblock String' src='rfmxlte_build_subblock_string.gif']

|  | Subblock Number specifies the number of subblocks that are configured in the intra-band noncontiguous carrier aggregation. Set this parameter to 1, which is the default, for single carrier and intra-band contiguous carrier aggregation. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_build_subframe_string.html language=enus -->
## TOPIC 00033: RFmxLTE Build Subframe String (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_build_subframe_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_build_subframe_string.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Build Subframe String (VI)

Owning Palette:

Downlink

Creates a subframe string to use as a selector string with the configuration or fetch properties and VIs.

[IMAGE alt='RFmxLTE Build Subframe String' src='rfmxlte_build_subframe_string.gif']

|  | Subframe Number specifies the subframe number for building the selector string. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxLTE Build Carrier String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_check_measurement_status.html language=enus -->
## TOPIC 00034: RFmxLTE Check Measurement Status (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_check_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_check_measurement_status.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Check Measurement Status (VI)

Owning Palette:

Utility

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='RFmxLTE Check Measurement Status' src='rfmxlte_check_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | done? indicates whether the measurement is complete. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_chp_configure_averaging.html language=enus -->
## TOPIC 00035: RFmxLTE CHP Configure Averaging (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_chp_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_chp_configure_averaging.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE CHP Configure Averaging (VI)

Owning Palette:

CHP

Configures averaging for the CHP measurement.

[IMAGE alt='RFmxLTE CHP Configure Averaging' src='rfmxlte_chp_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_chp_configure_integration_bandwidth_type.html language=enus -->
## TOPIC 00036: RFmxLTE CHP Configure Integration Bandwidth Type (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_chp_configure_integration_bandwidth_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_chp_configure_integration_bandwidth_type.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE CHP Configure Integration Bandwidth Type (VI)

Owning Palette:

CHP

Configures the type of integration bandwidth (IBW), which selects one of the frequency ranges over which the CHP is measured.

Refer to the [LTE Channel Power (CHP)](/csh?topicname=rfmxlte/lte_channel_power_chp.html) topic for more information.

[IMAGE alt='RFmxLTE CHP Configure Integration Bandwidth Type' src='rfmxlte_chp_configure_integration_bandwidth_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Integration Bandwidth Type specifies the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval. The default value is Signal Bandwidth. Signal Bandwidth (0) The IBW excludes the guard bands at the edges of the carrier or subblock from the power calculation. Channel Bandwidth (1) The IBW includes the guard bands at the edges of the carrier or subblock from the power calculation. |
| Signal Bandwidth (0) | The IBW excludes the guard bands at the edges of the carrier or subblock from the power calculation. |
| Channel Bandwidth (1) | The IBW includes the guard bands at the edges of the carrier or subblock from the power calculation. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_chp_configure_rbw_filter.html language=enus -->
## TOPIC 00037: RFmxLTE CHP Configure RBW Filter (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_chp_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_chp_configure_rbw_filter.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE CHP Configure RBW Filter (VI)

Owning Palette:

CHP

Configures the RBW filter.

[IMAGE alt='RFmxLTE CHP Configure RBW Filter' src='rfmxlte_chp_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. The default value is True. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
|  | RBW specifies the bandwidth of the resolution bandwidth (RBW) filter, used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is FFT Based. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_clear_noise_calibration_database.html language=enus -->
## TOPIC 00038: RFmxLTE Clear Noise Calibration Database (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_clear_noise_calibration_database.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_clear_noise_calibration_database.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Clear Noise Calibration Database (VI)

Owning Palette:

Advanced

Clears the noise calibration database used for noise compensation.

[IMAGE alt='RFmxLTE Clear Noise Calibration Database' src='rfmxlte_clear_noise_calibration_database.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_clone_signal_configuration.html language=enus -->
## TOPIC 00039: RFmxLTE Clone Signal Configuration (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_clone_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_clone_signal_configuration.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Clone Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='RFmxLTE Clone Signal Configuration' src='rfmxlte_clone_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
|  | Old Signal Name specifies the name of the existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_commit.html language=enus -->
## TOPIC 00040: RFmxLTE Commit (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_commit.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Commit (VI)

Owning Palette:

Utility

Commits settings to the hardware. Calling this VI is optional. RFmxLTE commits settings to the hardware when you call the [RFmxLTE Initiate](../rfmxltevi/rfmxlte_initiate.html) VI.

[IMAGE alt='RFmxLTE Commit' src='rfmxlte_commit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_auto_dmrs_detection_enabled.html language=enus -->
## TOPIC 00041: RFmxLTE Configure Auto DMRS Detection Enabled (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_auto_dmrs_detection_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_auto_dmrs_detection_enabled.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure Auto DMRS Detection Enabled (VI)

Owning Palette:

Configuration

Configures whether the demodulation reference signal (DMRS) parameters are configured by a user or automatically detected by a measurement.

[IMAGE alt='RFmxLTE Configure Auto DMRS Detection Enabled' src='rfmxlte_configure_auto_dmrs_detection_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Auto DMRS Detection Enabled specifies whether you need to configure the DMRS parameters, such as the values of the UL Group Hopping Enabled, UL Sequence Hopping Enabled, Cell ID, PUSCH n_DMRS_1, PUSCH n_DMRS_2, and PUSCH Delta SS properties, or if the measurement should automatically detect the values of these properties. The default value is False. False (0) The user-defined DMRS parameters are used. True (1) The DMRS parameters are automatically detected. Measurements returns an error if you set the ModAcc Sync Mode property to Frame because it is not possible to get the frame boundary when RFmx automatically detects the DMRS parameters. |
| False (0) | The user-defined DMRS parameters are used. |
| True (1) | The DMRS parameters are automatically detected. Measurements returns an error if you set the ModAcc Sync Mode property to Frame because it is not possible to get the frame boundary when RFmx automatically detects the DMRS parameters. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_auto_npusch_channel_detection_enabled.html language=enus -->
## TOPIC 00042: RFmxLTE Configure Auto NPUSCH Channel Detection Enabled (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_auto_npusch_channel_detection_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_auto_npusch_channel_detection_enabled.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure Auto NPUSCH Channel Detection Enabled (VI)

Owning Palette:

NB-loT

Configures whether the values of the [NPUSCH Tone Offset](/csh?topicname=rfmxlteprop/attr304062.html), [NPUSCH Num Tones](/csh?topicname=rfmxlteprop/attr304063.html), and [NPUSCH Mod Type](/csh?topicname=rfmxlteprop/attr304064.html) properties for the NPUSCH channel are auto-detected by the measurement or specified by you.

[IMAGE alt='RFmxLTE Configure Auto NPUSCH Channel Detection Enabled' src='rfmxlte_configure_auto_npusch_channel_detection_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Auto NPUSCH Channel Detection Enabled specifies whether the values of NPUSCH Tone Offset, NPUSCH Number of Tones, and NPUSCH Mod Type properties are auto-detected by the measurement or specified by you. The default value is True. False (0) The measurement uses the values that you specify for the NPUSCH Tone Offset, NPUSCH Number of Tones, and NPUSCH ModType properties. True (1) The measurement uses the values of the NPUSCH Tone Offset, NPUSCH Number of Tones, and NPUSCH Mod Type properties that are auto-detected. |
| False (0) | The measurement uses the values that you specify for the NPUSCH Tone Offset, NPUSCH Number of Tones, and NPUSCH ModType properties. |
| True (1) | The measurement uses the values of the NPUSCH Tone Offset, NPUSCH Number of Tones, and NPUSCH Mod Type properties that are auto-detected. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_downlink_number_of_subframes.html language=enus -->
## TOPIC 00043: RFmxLTE Configure Downlink Number of Subframes (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_downlink_number_of_subframes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_downlink_number_of_subframes.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure Downlink Number of Subframes (VI)

Owning Palette:

Downlink

Configures the number of unique subframes that are transmitted from the DUT.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE Configure Downlink Number of Subframes' src='rfmxlte_configure_downlink_number_of_subframes.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Number of Subframes specifies the number of subframes to be configured. If you set the DL Ch Configuration Mode property to Test Model, this parameter will be set to 10 for FDD and 20 for TDD by default. The default value is 10. Valid values are 10 to 20, inclusive. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" You can use the RFmxLTE Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_downlink_synchronization_signal.html language=enus -->
## TOPIC 00044: RFmxLTE Configure Downlink Synchronization Signal (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_downlink_synchronization_signal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_downlink_synchronization_signal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure Downlink Synchronization Signal (VI)

Owning Palette:

Downlink

Configures the synchronization signal power relative to the cell-specific reference signal.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE Configure Downlink Synchronization Signal' src='rfmxlte_configure_downlink_synchronization_signal.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | PSS Power specifies the power of the primary synchronization signal (PSS) relative to the power of the cell-specific reference signal. This value is expressed in dB. The default value is 0. |
|  | SSS Power specifies the power of the secondary synchronization signal (SSS) relative to the power of the cell-specific reference signal. This value is expressed in dB. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" You can use the RFmxLTE Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_downlink_test_model.html language=enus -->
## TOPIC 00045: RFmxLTE Configure Downlink Test Model (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_downlink_test_model.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_downlink_test_model.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure Downlink Test Model (VI)

Owning Palette:

Configuration

Configures the EUTRA test model type.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE Configure Downlink Test Model' src='rfmxlte_configure_downlink_test_model.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | DL Test Model specifies the EUTRA test model type when you set the DL Ch Configuration Mode property to Test Model. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. The default value is TM1.1. TM1.1 (0) Specifies an E-UTRA Test Model 1.1. TM1.2 (1) Specifies an E-UTRA Test Model 1.2. TM2 (2) Specifies an E-UTRA Test Model 2. TM2a (3) Specifies an E-UTRA Test Model 2a. TM2b (8) Specifies an E-UTRA Test Model 2b. TM3.1 (4) Specifies an E-UTRA Test Model 3.1. TM3.1a (7) Specifies an E-UTRA Test Model 3.1a. TM3.1b (9) Specifies an E-UTRA Test Model 3.1b. TM3.2 (5) Specifies an E-UTRA Test Model 3.2. TM3.3 (6) Specifies an E-UTRA Test Model 3.3. |
| TM1.1 (0) | Specifies an E-UTRA Test Model 1.1. |
| TM1.2 (1) | Specifies an E-UTRA Test Model 1.2. |
| TM2 (2) | Specifies an E-UTRA Test Model 2. |
| TM2a (3) | Specifies an E-UTRA Test Model 2a. |
| TM2b (8) | Specifies an E-UTRA Test Model 2b. |
| TM3.1 (4) | Specifies an E-UTRA Test Model 3.1. |
| TM3.1a (7) | Specifies an E-UTRA Test Model 3.1a. |
| TM3.1b (9) | Specifies an E-UTRA Test Model 3.1b. |
| TM3.2 (5) | Specifies an E-UTRA Test Model 3.2. |
| TM3.3 (6) | Specifies an E-UTRA Test Model 3.3. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" You can use the RFmxLTE Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_downlink_test_model_(array).html language=enus -->
## TOPIC 00046: RFmxLTE Configure Downlink Test Model (Array) (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_downlink_test_model_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_downlink_test_model_(array).html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure Downlink Test Model (Array) (VI)

Owning Palette:

Array

Configures an array of the EUTRA test model type for each component carrier within the subblock.

[IMAGE alt='RFmxLTE Configure Downlink Test Model (Array)' src='rfmxlte_configure_downlink_test_model_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | DL Test Model specifies the array of EUTRA test model types when you set the DL Ch Configuration Mode property to Test Model. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. The default value is TM1.1. TM1.1 (0) Specifies an E-UTRA Test Model 1.1. TM1.2 (1) Specifies an E-UTRA Test Model 1.2. TM2 (2) Specifies an E-UTRA Test Model 2. TM2a (3) Specifies an E-UTRA Test Model 2a. TM2b (8) Specifies an E-UTRA Test Model 2b. TM3.1 (4) Specifies an E-UTRA Test Model 3.1. TM3.1a (7) Specifies an E-UTRA Test Model 3.1a. TM3.1b (9) Specifies an E-UTRA Test Model 3.1b. TM3.2 (5) Specifies an E-UTRA Test Model 3.2. TM3.3 (6) Specifies an E-UTRA Test Model 3.3. |
| TM1.1 (0) | Specifies an E-UTRA Test Model 1.1. |
| TM1.2 (1) | Specifies an E-UTRA Test Model 1.2. |
| TM2 (2) | Specifies an E-UTRA Test Model 2. |
| TM2a (3) | Specifies an E-UTRA Test Model 2a. |
| TM2b (8) | Specifies an E-UTRA Test Model 2b. |
| TM3.1 (4) | Specifies an E-UTRA Test Model 3.1. |
| TM3.1a (7) | Specifies an E-UTRA Test Model 3.1a. |
| TM3.1b (9) | Specifies an E-UTRA Test Model 3.1b. |
| TM3.2 (5) | Specifies an E-UTRA Test Model 3.2. |
| TM3.3 (6) | Specifies an E-UTRA Test Model 3.3. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_duplex_scheme.html language=enus -->
## TOPIC 00047: RFmxLTE Configure Duplex Scheme (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_duplex_scheme.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_duplex_scheme.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure Duplex Scheme (VI)

Owning Palette:

Configuration

Configures the duplexing technique of the signal being measured.

[IMAGE alt='RFmxLTE Configure Duplex Scheme' src='rfmxlte_configure_duplex_scheme.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Duplex Scheme specifies the duplexing technique of the signal being measured. The default value is FDD. FDD (0) Specifies that the duplexing technique is frequency-division duplexing. TDD (1) Specifies that the duplexing technique is time-division duplexing. LAA (2) Specifies that the duplexing technique is license assisted access. |
| FDD (0) | Specifies that the duplexing technique is frequency-division duplexing. |
| TDD (1) | Specifies that the duplexing technique is time-division duplexing. |
| LAA (2) | Specifies that the duplexing technique is license assisted access. |
|  | Uplink Downlink Configuration specifies the configuration of the LTE frame structure in the time division duplex (TDD) mode. To configure the LTE frame, refer to table 4.2-2 of the 3GPP TS 36.211 specification. The default value is 0. 0 (0) The configuration of the LTE frame structure in the TDD duplex mode is 0. 1 (1) The configuration of the LTE frame structure in the TDD duplex mode is 1. 2 (2) The configuration of the LTE frame structure in the TDD duplex mode is 2. 3 (3) The configuration of the LTE frame structure in the TDD duplex mode is 3. 4 (4) The configuration of the LTE frame structure in the TDD duplex mode is 4. 5 (5) The configuration of the LTE frame structure in the TDD duplex mode is 5. 6 (6) The configuration of the LTE frame structure in the TDD duplex mode is 6. |
| 0 (0) | The configuration of the LTE frame structure in the TDD duplex mode is 0. |
| 1 (1) | The configuration of the LTE frame structure in the TDD duplex mode is 1. |
| 2 (2) | The configuration of the LTE frame structure in the TDD duplex mode is 2. |
| 3 (3) | The configuration of the LTE frame structure in the TDD duplex mode is 3. |
| 4 (4) | The configuration of the LTE frame structure in the TDD duplex mode is 4. |
| 5 (5) | The configuration of the LTE frame structure in the TDD duplex mode is 5. |
| 6 (6) | The configuration of the LTE frame structure in the TDD duplex mode is 6. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_emtc_analysis_enabled.html language=enus -->
## TOPIC 00048: RFmxLTE Configure eMTC Analysis Enabled (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_emtc_analysis_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_emtc_analysis_enabled.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure eMTC Analysis Enabled (VI)

Owning Palette:

Configuration

Configures whether the component carrier contains an enhanced machine type communications (Cat-M1 or Cat-M2) transmission.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE Configure eMTC Analysis Enabled' src='rfmxlte_configure_emtc_analysis_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | eMTC Analysis Enabled specifies whether the component carrier contains an eMTC transmission. The default value is False. False (0) The measurement considers the signal as LTE FDD/TDD transmission. True (1) Detects the eMTC half duplex pattern, narrow band hopping, and eMTC guard symbols present in the uplink transmission. |
| False (0) | The measurement considers the signal as LTE FDD/TDD transmission. |
| True (1) | Detects the eMTC half duplex pattern, narrow band hopping, and eMTC guard symbols present in the uplink transmission. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" You can use the RFmxLTE Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_enodeb_category.html language=enus -->
## TOPIC 00049: RFmxLTE Configure eNodeB Category (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_enodeb_category.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_enodeb_category.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure eNodeB Category (VI)

Owning Palette:

Configuration

Configures the eNodeB category of the signal being measured.

[IMAGE alt='RFmxLTE Configure eNodeB Category' src='rfmxlte_configure_enodeb_category.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | eNodeB Category specifies the downlink eNodeB (Base Station) category. The default value is Wide Area Base Station - Category A (0). Wide Area Base Station - Category A (0) Specifies the eNodeB is Wide Area Base Station - Category A. Wide Area Base Station - Category B Option1 (1) Specifies the eNodeB is Wide Area Base Station - Category B Option1. Wide Area Base Station - Category B Option2 (2) Specifies the eNodeB is Wide Area Base Station - Category B Option2. Local Area Base Station (3) Specifies the eNodeB is Local Area Base Station. Home Base Station (4) Specifies the eNodeB is Home Base Station. Medium Range Base Station (5) Specifies the eNodeB is Medium Range Base Station. |
| Wide Area Base Station - Category A (0) | Specifies the eNodeB is Wide Area Base Station - Category A. |
| Wide Area Base Station - Category B Option1 (1) | Specifies the eNodeB is Wide Area Base Station - Category B Option1. |
| Wide Area Base Station - Category B Option2 (2) | Specifies the eNodeB is Wide Area Base Station - Category B Option2. |
| Local Area Base Station (3) | Specifies the eNodeB is Local Area Base Station. |
| Home Base Station (4) | Specifies the eNodeB is Home Base Station. |
| Medium Range Base Station (5) | Specifies the eNodeB is Medium Range Base Station. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_external_attenuation.html language=enus -->
## TOPIC 00050: RFmxLTE Configure External Attenuation (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_external_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_external_attenuation.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure External Attenuation (VI)

Owning Palette:

Configuration

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer.

[IMAGE alt='RFmxLTE Configure External Attenuation' src='rfmxlte_configure_external_attenuation.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | External Attenuation specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_frequency.html language=enus -->
## TOPIC 00051: RFmxLTE Configure Frequency (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_frequency.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure Frequency (VI)

Owning Palette:

Configuration

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### RFmxLTE Configure Frequency (Frequency)

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

[IMAGE alt='RFmxLTE Configure Frequency (Frequency)' src='rfmxlte_configure_frequency_(frequency).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Center Frequency specifies the center frequency of the acquired RF signal for a single carrier. The parameter specifies the reference frequency of the subblock for intra-band carrier aggregation. The default value of this parameter is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE Configure Frequency (EARFCN)

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to the E-UTRA absolute radio frequency channel number (EARFCN) frequency.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE Configure Frequency (EARFCN)' src='rfmxlte_configure_frequency_(earfcn).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Link Direction specifies the link direction of the received signal. The default value is Uplink. Downlink (0) The measurement uses 3GPP LTE downlink specification to measure the received signal. Uplink (1) The measurement uses 3GPP LTE uplink specification to measure the received signal. |
| Downlink (0) | The measurement uses 3GPP LTE downlink specification to measure the received signal. |
| Uplink (1) | The measurement uses 3GPP LTE uplink specification to measure the received signal. |
|  | Band specifies the E-UTRA operating frequency band of a subblock as defined in section 5.2 of the 3GPP TS 36.521 specification. Valid values are from 1 to 256, inclusive. The default value is 1. |
|  | EARFCN specifies the evolved universal terrestrial radio access (E-UTRA) absolute radio frequency channel number. The default value is 18100. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_link_direction.html language=enus -->
## TOPIC 00052: RFmxLTE Configure Link Direction (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_link_direction.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_link_direction.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure Link Direction (VI)

Owning Palette:

Configuration

Configures the link direction of the signal being measured.

[IMAGE alt='RFmxLTE Configure Link Direction' src='rfmxlte_configure_link_direction.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Link Direction specifies the link direction of the received signal. The default value is Uplink. Downlink (0) The measurement uses 3GPP LTE downlink specification to measure the received signal. Uplink (1) The measurement uses 3GPP LTE uplink specification to measure the received signal. Sidelink (2) The measurement uses 3GPP LTE sidelink specifications to measure the received signal. |
| Downlink (0) | The measurement uses 3GPP LTE downlink specification to measure the received signal. |
| Uplink (1) | The measurement uses 3GPP LTE uplink specification to measure the received signal. |
| Sidelink (2) | The measurement uses 3GPP LTE sidelink specifications to measure the received signal. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_phich.html language=enus -->
## TOPIC 00053: RFmxLTE Configure PHICH (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_phich.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_phich.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure PHICH (VI)

Owning Palette:

Downlink

Configures the **Resource**, **Duration**, and **Power** parameters of the physical hybrid-ARQ indicator channel (PHICH).

Use "subframe<*l*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/subframe<*l*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE Configure PHICH' src='rfmxlte_configure_phich.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Resource specifies the PHICH resource value. This value is expressed in Ng. This parameter is used to calculate number of PHICH resource groups. Refer to section 6.9 of the 3GPP 36.211 specification for more information about PHICH. The default value is 1/6. 1/6 (0) Specifies that the PHICH resource value is 1/6. 1/2 (1) Specifies that the PHICH resource value is 1/2. 1 (2) Specifies that the PHICH resource value is 1. 2 (3) Specifies that the PHICH resource value is 2. |
| 1/6 (0) | Specifies that the PHICH resource value is 1/6. |
| 1/2 (1) | Specifies that the PHICH resource value is 1/2. |
| 1 (2) | Specifies that the PHICH resource value is 1. |
| 2 (3) | Specifies that the PHICH resource value is 2. |
|  | Duration specifies the PHICH duration. The default value is Normal. Normal (0) Orthogonal sequences of length 4 is used to extract PHICH. |
| Normal (0) | Orthogonal sequences of length 4 is used to extract PHICH. |
|  | Power specifies the power of all BPSK symbols in a PHICH sequence. This value is expressed in dB. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number, carrier number, and subframe number. If you do not specify the signal name, the default signal instance is used. Example: "subblock0/carrier0/subframe0" "signal::sig1/subblock0/carrier0/subframe0" You can use the RFmxLTE Build Subframe String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_pssch_modulation_type.html language=enus -->
## TOPIC 00054: RFmxLTE Configure PSSCH Modulation Type (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_pssch_modulation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_pssch_modulation_type.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure PSSCH Modulation Type (VI)

Owning Palette:

Sidelink

Configures the modulation scheme used in the physical sidelink shared channel (PSSCH) of the signal being measured.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE Configure PSSCH Modulation Type' src='rfmxlte_configure_pssch_modulation_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | PSSCH Mod Type specifies the modulation scheme used in the PSSCH channel of the signal being measured. The default value is QPSK. QPSK (0) Specifies a QPSK modulation scheme. 16 QAM (1) Specifies a 16-QAM modulation scheme. 64 QAM (2) Specifies a 64-QAM modulation scheme. |
| QPSK (0) | Specifies a QPSK modulation scheme. |
| 16 QAM (1) | Specifies a 16-QAM modulation scheme. |
| 64 QAM (2) | Specifies a 64-QAM modulation scheme. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" You can use the RFmxLTE Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_pssch_resource_blocks.html language=enus -->
## TOPIC 00055: RFmxLTE Configure PSSCH Resource Blocks (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_pssch_resource_blocks.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_pssch_resource_blocks.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure PSSCH Resource Blocks (VI)

Owning Palette:

Sidelink

Configures the start and number of resource blocks allocated for the physical sidelink shared channel (PSSCH) allocation.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE Configure PSSCH Resource Blocks' src='rfmxlte_configure_pssch_resource_blocks.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Resource Block Offset specifies the starting resource block number of the PSSCH allocation. The default value is 0. |
|  | Number of Resource Blocks specifies the number of consecutive resource blocks in the PSSCH allocation. The default value is -1. If you set this parameter to -1, all available resource blocks for the specified bandwidth are configured. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" You can use the RFmxLTE Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_pusch_modulation_type.html language=enus -->
## TOPIC 00056: RFmxLTE Configure PUSCH Modulation Type (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_pusch_modulation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_pusch_modulation_type.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure PUSCH Modulation Type (VI)

Owning Palette:

Uplink

Configures the modulation scheme used in the physical uplink shared channel (PUSCH) channel of the signal being measured.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE Configure PUSCH Modulation Type' src='rfmxlte_configure_pusch_modulation_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Modulation Type specifies the modulation scheme used in the PUSCH channel of the signal being measured. The default value is QPSK. QPSK (0) Specifies a QPSK modulation scheme. 16 QAM (1) Specifies a 16-QAM modulation scheme. 64 QAM (2) Specifies a 64-QAM modulation scheme. 256 QAM (3) Specifies a 256-QAM modulation scheme. 1024 QAM (4) Specifies a 1024-QAM modulation scheme. |
| QPSK (0) | Specifies a QPSK modulation scheme. |
| 16 QAM (1) | Specifies a 16-QAM modulation scheme. |
| 64 QAM (2) | Specifies a 64-QAM modulation scheme. |
| 256 QAM (3) | Specifies a 256-QAM modulation scheme. |
| 1024 QAM (4) | Specifies a 1024-QAM modulation scheme. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" You can use the RFmxLTE Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_pusch_resource_blocks.html language=enus -->
## TOPIC 00057: RFmxLTE Configure PUSCH Resource Blocks (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_pusch_resource_blocks.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_pusch_resource_blocks.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure PUSCH Resource Blocks (VI)

Owning Palette:

Uplink

Configures the start and number of resource blocks allocated for the physical uplink shared channel (PUSCH) cluster.

Use "cluster<*l*>" or "carrier<*k*>" or "subblock<*n*>/carrier<*k*>/cluster<*l*>" as the selector string to configure this result.

[IMAGE alt='RFmxLTE Configure PUSCH Resource Blocks' src='rfmxlte_configure_pusch_resource_blocks.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Resource Block Offset specifies the starting resource block number of a PUSCH cluster. The default value is 0. |
|  | Number of Resource Blocks specifies the number of consecutive resource blocks in a PUSCH cluster. The default value is -1. If you set this parameter to -1, all available resource blocks for the specified bandwidth are configured. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number, carrier number, and the cluster number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "subblock0/carrier0/cluster0" "signal::sig1/subblock0/carrier0/cluster0" You can use the RFmxLTE Build Cluster String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_reference_level.html language=enus -->
## TOPIC 00058: RFmxLTE Configure Reference Level (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_reference_level.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_reference_level.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure Reference Level (VI)

Owning Palette:

Configuration

Configures the reference level, which represents the maximum expected power of an RF input signal.

[IMAGE alt='RFmxLTE Configure Reference Level' src='rfmxlte_configure_reference_level.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Reference Level specifies the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_configure_trigger.html language=enus -->
## TOPIC 00059: RFmxLTE Configure Trigger (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_configure_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_configure_trigger.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Configure Trigger (VI)

Owning Palette:

Configuration

Configures the Reference Trigger to use to acquire the signal.

#### RFmxLTE Disable Trigger

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='RFmxLTE Disable Trigger' src='rfmxlte_disable_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE Configure Digital Edge Trigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

[IMAGE alt='RFmxLTE Configure Digital Edge Trigger' src='rfmxlte_configure_digital_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Digital Edge Source specifies the source terminal for the digital edge trigger. This parameter is used when you set the Trigger Type property to Digital Edge. The default value of this parameter is hardware dependent. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. PXIe_DStarB (PXIe_DStarB) The trigger is received on the PXIe DStar B trigger line. TimerEvent (TimerEvent) The trigger is received from the Timer Event. |
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
| TimerEvent (TimerEvent) | The trigger is received from the Timer Event. |
|  | Digital Edge specifies the source terminal for the digital edge trigger. This parameter is used when you set the Trigger Type property to Digital Edge. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. |
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE Configure IQ Power Edge Trigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.

To trigger on bursty signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

[IMAGE alt='RFmxLTE Configure IQ Power Edge Trigger' src='rfmxlte_configure_iq_power_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | IQ Power Edge Source specifies the channel from which the device monitors the trigger. This parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value of this parameter is hardware dependent. |
|  | IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
|  | IQ Power Edge Level specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative, and this value is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. This parameter is used only when you set the Trigger Type property to IQ Power Edge. The default value of this parameter is hardware dependent. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. The default value is 0. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
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

#### RFmxLTE Configure Software Edge Trigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

[IMAGE alt='RFmxLTE Configure Software Edge Trigger' src='rfmxlte_configure_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Trigger Delay specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. The default value is 0. |
|  | Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_delete_signal_configuration.html language=enus -->
## TOPIC 00060: RFmxLTE Delete Signal Configuration (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_delete_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_delete_signal_configuration.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Delete Signal Configuration (VI)

Owning Palette:

Advanced

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='RFmxLTE Delete Signal Configuration' src='rfmxlte_delete_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_get_all_named_result_names.html language=enus -->
## TOPIC 00061: RFmxLTE Get All Named Result Names (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_get_all_named_result_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_get_all_named_result_names.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Get All Named Result Names (VI)

Owning Palette:

Advanced

Returns the named result names of the signal that you specify in the **Selector String** parameter.

[IMAGE alt='RFmxLTE Get All Named Result Names' src='rfmxlte_get_all_named_result_names.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Result Names returns an array of result names. |
|  | Default Result Exists? indicates whether the default result exists. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_initiate.html language=enus -->
## TOPIC 00062: RFmxLTE Initiate (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_initiate.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Initiate (VI)

Owning Palette:

RFmx LTE VIs

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the [RFmxLTE Wait for Measurement Complete](../rfmxltevi/rfmxlte_wait_for_measurement_complete.html) VI or [RFmxLTE Check Measurement Status](../rfmxltevi/rfmxlte_check_measurement_status.html) VI.

[IMAGE alt='RFmxLTE Initiate' src='rfmxlte_initiate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" |
|  | Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_modacc_configure_averaging.html language=enus -->
## TOPIC 00063: RFmxLTE ModAcc Configure Averaging (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_modacc_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_modacc_configure_averaging.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ModAcc Configure Averaging (VI)

Owning Palette:

ModAcc

Configures averaging for the ModAcc measurement.

[IMAGE alt='RFmxLTE ModAcc Configure Averaging' src='rfmxlte_modacc_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_modacc_configure_common_clock_source_enabled.html language=enus -->
## TOPIC 00064: RFmxLTE ModAcc Configure Common Clock Source Enabled (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_modacc_configure_common_clock_source_enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_modacc_configure_common_clock_source_enabled.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ModAcc Configure Common Clock Source Enabled (VI)

Owning Palette:

ModAcc

Configures the Reference Clock and specifies whether same Reference Clock is used for local oscillator and D/A converter.

The modacc measurement ignores this VI, when you set the [Link Direction](/csh?topicname=rfmxlteprop/attr300029.html) property to **Downlink**.

[IMAGE alt='RFmxLTE ModAcc Configure Common Clock Source Enabled' src='rfmxlte_modacc_configure_common_clock_source_enabled.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Common Clock Source Enabled specifies whether the same Reference Clock is used for the local oscillator and the D/A converter. When the same Reference Clock is used, the carrier frequency offset is proportional to the Sample Clock error. The default value is True. False (0) The Sample Clock error is estimated independently. True (1) The Sample Clock error is estimated from carrier frequency offset. |
| False (0) | The Sample Clock error is estimated independently. |
| True (1) | The Sample Clock error is estimated from carrier frequency offset. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_modacc_configure_evm_unit.html language=enus -->
## TOPIC 00065: RFmxLTE ModAcc Configure EVM Unit (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_modacc_configure_evm_unit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_modacc_configure_evm_unit.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ModAcc Configure EVM Unit (VI)

Owning Palette:

ModAcc

Configures the units of the EVM results.

[IMAGE alt='RFmxLTE ModAcc Configure EVM Unit' src='rfmxlte_modacc_configure_evm_unit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | EVM Unit specifies the units of the EVM results. The default value is Percentage. Percentage (0) The EVM is reported in percentage. dB (1) The EVM is reported in dB. |
| Percentage (0) | The EVM is reported in percentage. |
| dB (1) | The EVM is reported in dB. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_modacc_configure_fft_window_offset.html language=enus -->
## TOPIC 00066: RFmxLTE ModAcc Configure FFT Window Offset (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_modacc_configure_fft_window_offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_modacc_configure_fft_window_offset.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ModAcc Configure FFT Window Offset (VI)

Owning Palette:

ModAcc

Configures the position of the FFT window that is used to calculate the EVM.

[IMAGE alt='RFmxLTE ModAcc Configure FFT Window Offset' src='rfmxlte_modacc_configure_fft_window_offset.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | FFT Window Offset specifies the position of the FFT window that is used to calculate the EVM. The offset is expressed as a percentage of the cyclic prefix length. If you set this parameter to 0, the EVM window starts from the end of cyclic prefix. If you set this parameter to 100, the EVM window starts from the beginning of cyclic prefix. The default value is 50. Valid values are 0 to 100, inclusive. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_modacc_configure_fft_window_position.html language=enus -->
## TOPIC 00067: RFmxLTE ModAcc Configure FFT Window Position (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_modacc_configure_fft_window_position.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_modacc_configure_fft_window_position.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ModAcc Configure FFT Window Position (VI)

Owning Palette:

ModAcc

Configures the FFT window position used for an EVM calculation.

Refer to the [LTE Modulation Accuracy (ModAcc)](/csh?topicname=rfmxlte/lte_modulation_accuracy.html) topic for more information about FFT window position.

[IMAGE alt='RFmxLTE ModAcc Configure FFT Window Position' src='rfmxlte_modacc_configure_fft_window_position.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | ModAcc FFT Window Type specifies the FFT window type used for an EVM calculation. The default value is Custom. 3GPP (0) The maximum EVM between the start window position and the end window position is returned according to the 3GPP specification. The window positions are specified by the ModAcc FFT Window Length parameter. For more information about the FFT window specification, refer to the 3GPP TS 36.521 specification, Annexe E.3.2. Custom (1) Only one FFT window position is used for the EVM calculation. The FFT window position is specified by the ModAcc FFT Window Offset parameter. |
| 3GPP (0) | The maximum EVM between the start window position and the end window position is returned according to the 3GPP specification. The window positions are specified by the ModAcc FFT Window Length parameter. For more information about the FFT window specification, refer to the 3GPP TS 36.521 specification, Annexe E.3.2. |
| Custom (1) | Only one FFT window position is used for the EVM calculation. The FFT window position is specified by the ModAcc FFT Window Offset parameter. |
|  | ModAcc FFT Window Offset specifies the position of the FFT window used to calculate the EVM. The offset is expressed as a percentage of the cyclic prefix length. If you set this parameter to 0, the EVM window starts from the end of cyclic prefix. If you set this parameter to 100, the EVM window starts from the beginning of cyclic prefix. The default value is 50. Valid values are 0 to 100, inclusive. |
|  | ModAcc FFT Window Length specifies the FFT window length. This value is expressed in a percentage of the cyclic prefix length. This parameter is used when you set the ModAcc FFT Window Type parameter to 3GPP, where you need to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. The default value is -1. Valid values are -1 to 100, inclusive. When this property is set to -1, the RFmx populates the FFT Window Length based on carrier bandwidth automatically, as given in the3GPP 36.104 specification, Annexe E.5.1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_modacc_configure_in-band_emission_mask_type.html language=enus -->
## TOPIC 00068: RFmxLTE ModAcc Configure In-Band Emission Mask Type (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_modacc_configure_in-band_emission_mask_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_modacc_configure_in-band_emission_mask_type.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ModAcc Configure In-Band Emission Mask Type (VI)

Configures the **In-Band Emission Mask Type** parameter to be used.

[IMAGE alt='RFmxLTE ModAcc Configure In-Band Emission Mask Type' src='rfmxlte_modacc_configure_in-band_emission_mask_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | In-Band Emission Mask Type specifies the in-band emissions mask type to be used for measuring in-band emission margin (dB) and subblock in-Band emission margin (dB) results. Refer to section 6.5.2.3.5 of the 3GPP 36.521-1 specification for more information. The default value is Release 8-10 for bandwidths other than 200 KHz and eMTC Analysis enabled is False. It is Release 11 Onwards, otherwise. Release 8-10 (0) Specifies the mask type to be used for UE, supporting 3GPP Release 8 to 3GPP Release 10 specification. Release 11 Onwards (1) Specifies the mask type to be used for UE, supporting 3GPP Release 11 and higher specification. |
| Release 8-10 (0) | Specifies the mask type to be used for UE, supporting 3GPP Release 8 to 3GPP Release 10 specification. |
| Release 11 Onwards (1) | Specifies the mask type to be used for UE, supporting 3GPP Release 11 and higher specification. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_modacc_configure_synchronization_mode_and_interval.html language=enus -->
## TOPIC 00069: RFmxLTE ModAcc Configure Synchronization Mode and Interval (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_modacc_configure_synchronization_mode_and_interval.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_modacc_configure_synchronization_mode_and_interval.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE ModAcc Configure Synchronization Mode and Interval (VI)

Owning Palette:

ModAcc

Configures the **Synchronization Mode**, the **Measurement Offset**, and the **Measurement Length** parameters of the ModAcc measurement.

Refer to the [LTE Modulation Accuracy (ModAcc)](/csh?topicname=rfmxlte/lte_modulation_accuracy.html) topic for more information about ModAcc measurements.

[IMAGE alt='RFmxLTE ModAcc Configure Synchronization Mode and Interval' src='rfmxlte_modacc_configure_synchronization_mode_and_interval.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Synchronization Mode specifies whether the measurement is performed from the frame or the slot boundary. The default value is Slot. When you set the Link Direction property to Downlink, the measurement supports only Frame synchronization mode. Frame (0) The frame boundary is detected, and the measurement is performed over the Measurement Length parameter, starting at the Measurement Offset parameter from the frame boundary. When you set the Trigger Type property to Digital Edge, the measurement expects a trigger at the frame boundary. Slot (1) The slot boundary is detected, and the measurement is performed over the Measurement Length parameter starting at the Measurement Offset parameter from the slot boundary. When you set the Trigger Type property to Digital Edge, the measurement expects a trigger at any slot boundary. Marker (2) The measurement expects a marker (trigger) at the frame boundary from the user. The measurement takes advantage of triggered acquisitions to reduce processing resulting in faster measurement time. Measurement is performed over the Measurement Length parameter starting at the Measurement Offset parameter from the frame boundary. |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the Measurement Length parameter, starting at the Measurement Offset parameter from the frame boundary. When you set the Trigger Type property to Digital Edge, the measurement expects a trigger at the frame boundary. |
| Slot (1) | The slot boundary is detected, and the measurement is performed over the Measurement Length parameter starting at the Measurement Offset parameter from the slot boundary. When you set the Trigger Type property to Digital Edge, the measurement expects a trigger at any slot boundary. |
| Marker (2) | The measurement expects a marker (trigger) at the frame boundary from the user. The measurement takes advantage of triggered acquisitions to reduce processing resulting in faster measurement time. Measurement is performed over the Measurement Length parameter starting at the Measurement Offset parameter from the frame boundary. |
|  | Measurement Offset specifies the measurement offset, in slots, to skip from the synchronization boundary. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. Valid values are 0 to 19, inclusive. |
|  | Measurement Length specifies the number of slots to be measured. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_obw_configure_averaging.html language=enus -->
## TOPIC 00070: RFmxLTE OBW Configure Averaging (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_obw_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_obw_configure_averaging.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE OBW Configure Averaging (VI)

Owning Palette:

OBW

Configures averaging for the OBW measurement.

[IMAGE alt='RFmxLTE OBW Configure Averaging' src='rfmxlte_obw_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_obw_configure_rbw_filter.html language=enus -->
## TOPIC 00071: RFmxLTE OBW Configure RBW Filter (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_obw_configure_rbw_filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_obw_configure_rbw_filter.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE OBW Configure RBW Filter (VI)

Owning Palette:

OBW

Configures the RBW filter.

[IMAGE alt='RFmxLTE OBW Configure RBW Filter' src='rfmxlte_obw_configure_rbw_filter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | RBW Auto specifies whether the measurement computes the RBW. The default value is True. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
|  | RBW specifies the bandwidth of the resolution bandwidth (RBW) filter, used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 10 kHz. |
|  | RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_obw_configure_sweep_time.html language=enus -->
## TOPIC 00072: RFmxLTE OBW Configure Sweep Time (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_obw_configure_sweep_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_obw_configure_sweep_time.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE OBW Configure Sweep Time (VI)

Owning Palette:

OBW

Configures the sweep time.

[IMAGE alt='RFmxLTE OBW Configure Sweep Time' src='rfmxlte_obw_configure_sweep_time.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement uses a sweep time of 1 ms. |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement uses a sweep time of 1 ms. |
|  | Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1 ms. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_obw_fetch.html language=enus -->
## TOPIC 00073: RFmxLTE OBW Fetch (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_obw_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_obw_fetch.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE OBW Fetch (VI)

Owning Palette:

Fetch

Fetches the OBW measurements.

#### RFmxLTE OBW Fetch Measurement

Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock.

Use "subblock<*n*>" as the selector string to read results from this VI.

Refer to the [LTE Occupied Bandwidth](/csh?topicname=rfmxlte/lte_occupied_bandwidth_obw.html) topic for more information about OBW measurements.

[IMAGE alt='RFmxLTE OBW Fetch Measurement' src='rfmxlte_obw_fetch_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Occupied Bandwidth returns the bandwidth that occupies 99 percentage of the total power of the signal within a carrier/subblock. |
|  | Absolute Power returns the power measured over the integration bandwidth of the carrier. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | Stop Frequency returns the stop frequency of the subblock. The occupied bandwidth of a carrier/subblock is calculated using the following equation: Stop frequency - Start frequency = Occupied bandwidth. |
|  | Start Frequency returns the start frequency of the subblock. The occupied bandwidth of a carrier/subblock is calculated using the following equation: Stop frequency - Start frequency = Occupied bandwidth. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE OBW Fetch Spectrum

Fetches the spectrum used for OBW measurements.

[IMAGE alt='RFmxLTE OBW Fetch Spectrum' src='rfmxlte_obw_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the spectrum. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_property_node.html language=enus -->
## TOPIC 00074: RFmxLTE Property Node (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_property_node.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_property_node.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Property Node (VI)

Owning Palette:

RFmx LTE VIs

Gets (reads), sets (writes), or resets (sets to default value) RFmxLTE properties.

[IMAGE alt='RFmxLTE Property Node' src='rfmxlte_property_node.gif']

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_pvt_configure_averaging.html language=enus -->
## TOPIC 00075: RFmxLTE PvT Configure Averaging (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_pvt_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_pvt_configure_averaging.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE PvT Configure Averaging (VI)

Owning Palette:

PVT

Configures averaging for the power versus time (PVT) measurement.

[IMAGE alt='RFmxLTE PvT Configure Averaging' src='rfmxlte_pvt_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_pvt_configure_measurement_method.html language=enus -->
## TOPIC 00076: RFmxLTE PvT Configure Measurement Method (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_pvt_configure_measurement_method.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_pvt_configure_measurement_method.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE PvT Configure Measurement Method (VI)

Owning Palette:

PVT

Configures the method for performing the power versus time (PVT) measurement.

Refer to the [LTE PVT (Power Vs Time) Measurement](/csh?topicname=rfmxlte/pvt.html) topic for more information about measurement method.

[IMAGE alt='RFmxLTE PvT Configure Measurement Method' src='rfmxlte_pvt_configure_measurement_method.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Meas Method specifies the method for performing the PVT measurement. The default value is Normal. Normal (0) The measurement is performed using a single acquisition. Use this method when a high dynamic range is not required. Dynamic Range (1) The measurement is performed using two acquisitions. Use this method when a higher dynamic range is desirable over the measurement speed. Supported Devices: PXIe-5644/5645/5646/5840/5841/5842 |
| Normal (0) | The measurement is performed using a single acquisition. Use this method when a high dynamic range is not required. |
| Dynamic Range (1) | The measurement is performed using two acquisitions. Use this method when a higher dynamic range is desirable over the measurement speed. Supported Devices: PXIe-5644/5645/5646/5840/5841/5842 |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_select_measurement.html language=enus -->
## TOPIC 00077: RFmxLTE Select Measurement (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_select_measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_select_measurement.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Select Measurement (VI)

Owning Palette:

RFmx LTE VIs

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

#### RFmxLTE Select Measurement (Single)

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='RFmxLTE Select Measurement (Single)' src='rfmxlte_select_measurement_(single).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurement specifies the measurement to perform. You can specify one the following measurements. The default value is ACP. ACP (0) Enables the ACP measurement. CHP (1) Enables the CHP measurement. ModAcc (2) Enables the ModAcc measurement. OBW (3) Enables the OBW measurement. SEM (4) Enables the SEM measurement. PVT (5) Enables the PVT measurement. SlotPhase (6) Enables the SlotPhase measurement. SlotPower (7) Enables the SlotPower measurement. |
| ACP (0) | Enables the ACP measurement. |
| CHP (1) | Enables the CHP measurement. |
| ModAcc (2) | Enables the ModAcc measurement. |
| OBW (3) | Enables the OBW measurement. |
| SEM (4) | Enables the SEM measurement. |
| PVT (5) | Enables the PVT measurement. |
| SlotPhase (6) | Enables the SlotPhase measurement. |
| SlotPower (7) | Enables the SlotPower measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE Select Measurement (Multiple)

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='RFmxLTE Select Measurement (Multiple)' src='rfmxlte_select_measurement_(multiple).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Measurements specifies the measurements to perform. You can specify one or more of the following measurements. The default value is an empty array. ACP (0) Enables the ACP measurement. CHP (1) Enables the CHP measurement. ModAcc (2) Enables the ModAcc measurement. OBW (3) Enables the OBW measurement. SEM (4) Enables the SEM measurement. PVT (5) Enables the PVT measurement. SlotPhase (6) Enables the SlotPhase measurement. SlotPower (7) Enables the SlotPower measurement. |
| ACP (0) | Enables the ACP measurement. |
| CHP (1) | Enables the CHP measurement. |
| ModAcc (2) | Enables the ModAcc measurement. |
| OBW (3) | Enables the OBW measurement. |
| SEM (4) | Enables the SEM measurement. |
| PVT (5) | Enables the PVT measurement. |
| SlotPhase (6) | Enables the SlotPhase measurement. |
| SlotPower (7) | Enables the SlotPower measurement. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_sem_configure_averaging.html language=enus -->
## TOPIC 00078: RFmxLTE SEM Configure Averaging (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_sem_configure_averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_sem_configure_averaging.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE SEM Configure Averaging (VI)

Owning Palette:

SEM

Configures averaging for the SEM measurement.

[IMAGE alt='RFmxLTE SEM Configure Averaging' src='rfmxlte_sem_configure_averaging.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
|  | Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
|  | Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_sem_configure_component_carrier_maximum_output_power.html language=enus -->
## TOPIC 00079: RFmxLTE SEM Configure Component Carrier Maximum Output Power (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_sem_configure_component_carrier_maximum_output_power.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_sem_configure_component_carrier_maximum_output_power.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE SEM Configure Component Carrier Maximum Output Power (VI)

Owning Palette:

SEM

Configures the maximum output power of the component carrier.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this VI.

|  | Note This VI is considered only when you set the Link Direction property to Downlink, eNodeB Category property to Medium Range Base Station, and SEM DL Mask Type property to eNodeB Category Based. |
| --- | --- |

[IMAGE alt='RFmxLTE SEM Configure Component Carrier Maximum Output Power' src='rfmxlte_sem_configure_component_carrier_maximum_output_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Component Carrier Max Output Power specifies the maximum output power per carrier, which is used only to choose the limit table for Medium Range Base Station. This value is expressed in dBm. Refer to the section 6.6.3 of the 3GPP 36.141 specification for more details. The default value is 0. Valid values are 0 to 38, inclusive. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" You can use the RFmxLTE Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_sem_configure_component_carrier_maximum_output_power_(array).html language=enus -->
## TOPIC 00080: RFmxLTE SEM Configure Component Carrier Maximum Output Power (Array) (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_sem_configure_component_carrier_maximum_output_power_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_sem_configure_component_carrier_maximum_output_power_(array).html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE SEM Configure Component Carrier Maximum Output Power (Array) (VI)

Owning Palette:

Array VIs

Configures the array of maximum output power of the component carrier.

Use "subblock<*n*>" as the selector string to configure this VI.

|  | Note This VI is considered only when you set the Link Direction property to Downlink, eNodeB Category property to Medium Range Base Station, and SEM DL Mask Type property to eNodeB Category Based. |
| --- | --- |

[IMAGE alt='RFmxLTE SEM Configure Component Carrier Maximum Output Power (Array)' src='rfmxlte_sem_configure_component_carrier_maximum_output_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Component Carrier Max Output Power specifies the array of maximum output power per carrier, which is used only to choose the limit table for Medium Range Base Station. This value is expressed in dBm. Refer to the section 6.6.3 of the 3GPP 36.141 specification for more details. The default value is 0. Valid values are 0 to 38, inclusive. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_sem_configure_downlink_mask.html language=enus -->
## TOPIC 00081: RFmxLTE SEM Configure Downlink Mask (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_sem_configure_downlink_mask.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_sem_configure_downlink_mask.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE SEM Configure Downlink Mask (VI)

Owning Palette:

SEM

Configures the **Downlink Mask Type**, **Delta F_max**, and **Aggregated Maximum Output Power** parameters for the SEM measurement in LTE downlink.

[IMAGE alt='RFmxLTE SEM Configure Downlink Mask' src='rfmxlte_sem_configure_downlink_mask.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Downlink Mask Type specifies the standard-defined spectrum emission mask used in the measurement for the downlink. You must set the mask type to CUSTOM to configure the custom offsets and the masks. Refer to section 6.6.3 of the 3GPP 36.141 specification for more information about standard-defined mask types. The default value is eNodeB Category Based. Valid values are 0, 1, and 5. eNodeB Category Based (0) Specifies limits are applied based on eNodeB Category attribute. Band 46 (1) Specifies that limits are applied based on Band 46 test requirements. Custom (5) You need to configure the SEM Num Offsets, SEM Offset Start Freq, SEM Offset Stop Freq, SEM Offset Abs Limit Start, SEM Offset Abs Limit Stop, SEM Offset Rel Limit Start , SEM Offset Rel Limit Stop, SEM Offset Sideband, SEM Offset RBW, SEM Offset RBW Filter Type, and SEM Offset BW Integral properties for each offset. |
| eNodeB Category Based (0) | Specifies limits are applied based on eNodeB Category attribute. |
| Band 46 (1) | Specifies that limits are applied based on Band 46 test requirements. |
| Custom (5) | You need to configure the SEM Num Offsets, SEM Offset Start Freq, SEM Offset Stop Freq, SEM Offset Abs Limit Start, SEM Offset Abs Limit Stop, SEM Offset Rel Limit Start , SEM Offset Rel Limit Stop, SEM Offset Sideband, SEM Offset RBW, SEM Offset RBW Filter Type, and SEM Offset BW Integral properties for each offset. |
|  | Delta F_Max specifies the stop frequency for the last offset segment to be used in the measurement. This value is expressed in Hz. The default value is 15 MHz. The minimum value is 9.5 MHz. |
|  | Aggregated Maximum Power specifies the aggregated maximum output power of all the transmit antenna connectors. This value is expressed in dBm. The default value is 0. Valid values are within 20, inclusive. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_sem_configure_number_of_offsets.html language=enus -->
## TOPIC 00082: RFmxLTE SEM Configure Number of Offsets (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_sem_configure_number_of_offsets.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_sem_configure_number_of_offsets.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE SEM Configure Number of Offsets (VI)

Owning Palette:

SEM

Configures the number of offset segments for the SEM measurement.

[IMAGE alt='RFmxLTE SEM Configure Number of Offsets' src='rfmxlte_sem_configure_number_of_offsets.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Num Offsets specifies the number of SEM offset segments. The default value is 1. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_sem_configure_offset_absolute_limit.html language=enus -->
## TOPIC 00083: RFmxLTE SEM Configure Offset Absolute Limit (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_sem_configure_offset_absolute_limit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_sem_configure_offset_absolute_limit.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE SEM Configure Offset Absolute Limit (VI)

Owning Palette:

SEM

Configures the start and the stop limit of an offset segment.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE SEM Configure Offset Absolute Limit' src='rfmxlte_sem_configure_offset_absolute_limit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset Abs Limit Start specifies the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. The default value is -16.5. |
|  | Offset Abs Limit Stop specifies the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. The default value is -16.5. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" You can use the RFmxLTE Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_sem_configure_offset_absolute_limit_(array).html language=enus -->
## TOPIC 00084: RFmxLTE SEM Configure Offset Absolute Limit (Array) (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_sem_configure_offset_absolute_limit_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_sem_configure_offset_absolute_limit_(array).html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE SEM Configure Offset Absolute Limit (Array) (VI)

Owning Palette:

Array VIs

Configures the array of the start limit and the stop limit of the offset segments.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE SEM Configure Offset Absolute Limit (Array)' src='rfmxlte_sem_configure_offset_absolute_limit_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset Abs Limit Start specifies the array of the absolute power limits corresponding to the beginning of an offset segment. This value is expressed in dBm. The default value is -16.5. |
|  | Offset Abs Limit Stop specifies the array of the absolute power limits corresponding to the end of an offset segment. This value is expressed in dBm. The default value is -16.5. |
|  | Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_sem_configure_offset_bandwidth_integral.html language=enus -->
## TOPIC 00085: RFmxLTE SEM Configure Offset Bandwidth Integral (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_sem_configure_offset_bandwidth_integral.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_sem_configure_offset_bandwidth_integral.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE SEM Configure Offset Bandwidth Integral (VI)

Owning Palette:

SEM

Configures the bandwidth integral of the offset segments.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE SEM Configure Offset Bandwidth Integral' src='rfmxlte_sem_configure_offset_bandwidth_integral.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset BW Integral specifies the resolution of the spectrum to compare with the spectral mask limits as an integer multiple of the RBW. The default value is 1. When you set this parameter to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of a bandwidth integral and a RBW. |
|  | Selector String specifies a selector string comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" You can use the RFmxLTE Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_sem_configure_offset_bandwidth_integral_(array).html language=enus -->
## TOPIC 00086: RFmxLTE SEM Configure Offset Bandwidth Integral (Array) (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_sem_configure_offset_bandwidth_integral_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_sem_configure_offset_bandwidth_integral_(array).html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE SEM Configure Offset Bandwidth Integral (Array) (VI)

Owning Palette:

Array VIs

Configures the array of the bandwidth integral of the offset segments.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxLTE SEM Configure Offset Bandwidth Integral (Array)' src='rfmxlte_sem_configure_offset_bandwidth_integral_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Offset BW Integral specifies the array of the resolution values of the spectrum to compare with the spectral mask limits as an integer multiple of the RBW. The default value is 1. When you set this parameter to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of a bandwidth integral and an RBW. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_sem_fetch.html language=enus -->
## TOPIC 00087: RFmxLTE SEM Fetch (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_sem_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_sem_fetch.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE SEM Fetch (VI)

Owning Palette:

Fetch

Fetches the SEM measurements.

#### RFmxLTE SEM Fetch Total Aggregated Power

Returns the sum of powers of all subblocks.

[IMAGE alt='RFmxLTE SEM Fetch Total Aggregated Power' src='rfmxlte_sem_fetch_total_aggregated_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Total Aggregated Power returns the sum of powers of all the frequency bins over the integration bandwidth of subblock. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power in the subblock gaps. When you set the ACP Pwr Units property to dBm, the parameter returns the total integrated power in dBm of all the active carriers measured. When you set the ACP Pwr Units property to dBm/Hz, the parameter returns the power spectral density in dBm/Hz based on the power in all the active carriers measured. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Measurement Status

Returns the overall measurement status based on the standard mask type that you configure.

[IMAGE alt='RFmxLTE SEM Fetch Measurement Status' src='rfmxlte_sem_fetch_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Subblock Measurement

Returns the power, integration bandwidth and center frequency of the subblock.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxLTE SEM Fetch Subblock Measurement' src='rfmxlte_sem_fetch_subblock_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Subblock Power returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. When you set the ACP Pwr Units property to dBm, the parameter returns the total subblock power in dBm of all the active carriers measured over the subblock. When you set the ACP Pwr Units property to dBm/Hz, the parameter returns the power spectral density in dBm/Hz based on the power in all the active carriers measured over the subblock. |
|  | Integration Bandwidth returns the integration bandwidth of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within a subblock. This value is expressed in Hz. |
|  | Frequency returns the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. This value is expressed in Hz. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Component Carrier Measurement

Returns the absolute power and relative power measured in the component carrier. The relative power is relative to subblock power.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxLTE SEM Fetch Component Carrier Measurement' src='rfmxlte_sem_fetch_component_carrier_measurement.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxLTE Build Carrier String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the power measured over the integration bandwidth of the carrier. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | Relative Integrated Power returns the component carrier power relative to its subblock power. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Lower Offset Margin

Returns the measurement status, margin, frequency at margin, and the absolute and relative powers at the margin for lower offset segments. The relative power is relative to the total aggregated power.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this VI.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information.

[IMAGE alt='RFmxLTE SEM Fetch Lower Offset Margin' src='rfmxlte_sem_fetch_lower_offset_margin.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxLTE Build Offset String VI to build the selector string. |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Margin Relative Power returns the power at which the margin occurs in the upper (positive) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr property. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Margin Absolute Power returns the power at which the margin occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Measurement Status returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |
|  | Margin returns the margin from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Margin Frequency returns the frequency at which the margin occurs in the lower (negative) offset. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Lower Offset Power

Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this VI.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information.

[IMAGE alt='RFmxLTE SEM Fetch Lower Offset Power' src='rfmxlte_sem_fetch_lower_offset_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxLTE Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the lower (negative) offset segment power. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Relative Integrated Power returns the power in the lower (negative) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr property. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Absolute Peak Power returns the peak power in the lower (negative) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Relative Peak Power returns the peak power in the upper (positive) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr property. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Peak Frequency returns the frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Upper Offset Margin

Returns the measurement status, margin, frequency at margin, and absolute and relative powers at margin for upper offset segments. The relative power is relative to total aggregated power.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this VI.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information.

[IMAGE alt='RFmxLTE SEM Fetch Upper Offset Margin' src='rfmxlte_sem_fetch_upper_offset_margin.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxLTE Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |
|  | Margin returns the margin from the standard defined absolute limit mask for upper offset. Margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Margin Frequency returns the frequency at which the margin occurs in the upper offset. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Margin Relative Power returns the power at which the margin occurs in the upper (positive) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr property. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Margin Absolute Power returns the power at which the margin occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Upper Offset Power

Returns the total absolute and relative powers, peak, absolute, and relative powers, and frequency at peak absolute power of upper offset segment. The relative power is relative to total aggregated power.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this VI.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information.

[IMAGE alt='RFmxLTE SEM Fetch Upper Offset Power' src='rfmxlte_sem_fetch_upper_offset_power.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxLTE Build Offset String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the upper offset segment power. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Relative Integrated Power returns the power in the upper offset segment relative to the value returned by the SEM Results Total Aggregated Pwr property. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Absolute Peak Power returns the peak power in the upper offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Relative Peak Power returns the peak power in the upper (positive) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr property. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Peak Frequency returns the frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Component Carrier Measurement (Array)

Returns an array of the absolute powers and relative powers measured in the component carriers. The relative power is relative to subblock power.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxLTE SEM Fetch Component Carrier Measurement (Array)' src='rfmxlte_sem_fetch_component_carrier_measurement_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the array of power measured in the subblock. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. |
|  | Relative Integrated Power returns the array of the sum of powers of all the frequency bins over the integration bandwidth of the component carrier power relative to its subblock power. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Lower Offset Margin (Array)

Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for lower offset segments. The relative power is relative to the total aggregated power.

Use "subblock<*n*>" as the selector string to read results from this VI.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information.

[IMAGE alt='RFmxLTE SEM Fetch Lower Offset Margin (Array)' src='rfmxlte_sem_fetch_lower_offset_margin_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the array of the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |
|  | Margin returns the array of margins from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Margin Frequency returns the array of frequency at which the margin occurs in the lower (negative) offset. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Margin Relative Power returns the array of powers at which the margin occurs in the upper (positive) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr property. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Margin Absolute Power returns the array of power at which the margin occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Lower Offset Power (Array)

Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power.

Use "subblock<*n*>" as the selector string to read results from this VI.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information.

[IMAGE alt='RFmxLTE SEM Fetch Lower Offset Power (Array)' src='rfmxlte_sem_fetch_lower_offset_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the array of lower (negative) offset segment powers. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Relative Integrated Power returns the array of powers in the lower (negative) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr property. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Absolute Peak Power returns the array of peak powers in the lower (negative) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Relative Peak Power returns the array of peak power in the upper (positive) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr property. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Peak Frequency returns the array of frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Upper Offset Margin (Array)

Returns an array of measurement statuses, margins, frequencies at margins, and absolute and relative powers at margins for upper offset segments. The relative power is relative to total aggregated power.

Use "subblock<*n*>" as the selector string to read results from this VI.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information.

[IMAGE alt='RFmxLTE SEM Fetch Upper Offset Margin (Array)' src='rfmxlte_sem_fetch_upper_offset_margin_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Measurement Status returns the array of the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |
|  | Margin returns the array of margins from the standard defined absolute limit mask for upper offset. The margin is defined as the minimum difference between the spectrum and the limit mask. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Margin Frequency returns the array of frequency at which the margin occurs in the upper offset. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Margin Relative Power returns the array of powers at which the margin occurs in the upper (positive) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr property. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Margin Absolute Power returns the array of power at which the margin occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the SEM results lower offset start frequency and SEM results lower offset stop frequency are updated, and the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Upper Offset Power (Array)

Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of upper offset segments. The relative power is relative to total aggregated power.

Use "subblock<*n*>" as the selector string to read results from this VI.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information.

[IMAGE alt='RFmxLTE SEM Fetch Upper Offset Power (Array)' src='rfmxlte_sem_fetch_upper_offset_power_(array).gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxLTE Build Subblock String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Absolute Integrated Power returns the array of upper offset segment powers. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Relative Integrated Power returns the array of powers in the upper offset segment relative to the value returned by the SEM Results Total Aggregated Pwr property. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Absolute Peak Power returns the array of peak powers in the upper offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Relative Peak Power returns the array of peak power in the upper (positive) offset segment relative to the value returned by the SEM Results Total Aggregated Pwr property. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | Peak Frequency returns the array of frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band noncontiguous type of carrier aggregation, the offset segment may be truncated or discarded based on offset overlap rules as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxLTE SEM Fetch Spectrum

Fetches the spectrum used for the SEM measurement.

[IMAGE alt='RFmxLTE SEM Fetch Spectrum' src='rfmxlte_sem_fetch_spectrum.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | Spectrum returns the spectrum. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
|  | Composite Mask returns the composite mask trace used for the channel. This value is expressed in dBm. x0 returns the start frequency of the channel. This value is expressed in Hz. dx returns the frequency bin spacing. This value is expressed in Hz. y returns the array of composite mask used for the channel. |
|  | x0 returns the start frequency of the channel. This value is expressed in Hz. |
|  | dx returns the frequency bin spacing. This value is expressed in Hz. |
|  | y returns the array of composite mask used for the channel. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_send_software_edge_trigger.html language=enus -->
## TOPIC 00088: RFmxLTE Send Software Edge Trigger (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_send_software_edge_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_send_software_edge_trigger.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Send Software Edge Trigger (VI)

Owning Palette:

Configuration

Sends a trigger to the device when you use the [RFmxLTE Configure Trigger](rfmxlte_configure_trigger.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxLTE Initiate VI.

[IMAGE alt='RFmxLTE Send Software Edge Trigger' src='rfmxlte_send_software_edge_trigger.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/rfmxlte_wait_for_measurement_complete.html language=enus -->
## TOPIC 00089: RFmxLTE Wait for Measurement Complete (VI)

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/rfmxlte_wait_for_measurement_complete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/rfmxlte_wait_for_measurement_complete.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

RFmxLTE Wait for Measurement Complete (VI)

Owning Palette:

Utility

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='RFmxLTE Wait for Measurement Complete' src='rfmxlte_wait_for_measurement_complete.gif']

|  | Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. |
| --- | --- |
|  | Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. |
|  | Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxLTE Build Signal String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference to your RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/sem_array_vis_pal.html language=enus -->
## TOPIC 00090: Array VIs

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/sem_array_vis_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/sem_array_vis_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

Array VIs

Owning Palette:

SEM

Use the array VIs on this palette to configure the SEM measurements. You can also use the [RFmxLTE Property Node](../rfmxltevi/rfmxlte_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxLTE SEM Configure Component Carrier Maximum Output Power (Array) | Configures the array of maximum output power of the component carrier. Use "subblock<n>" as the selector string to configure this VI. |
| RFmxLTE SEM Configure Offset Frequency (Array) | Configures the arrays of the start and stop frequencies and the sideband of an offset segment. Use "subblock<n>" as the selector string to configure this VI. |
| RFmxLTE SEM Configure Offset Bandwidth Integral (Array) | Configures the array of the bandwidth integral of the offset segments. Use "subblock<n>" as the selector string to configure this VI. |
| RFmxLTE SEM Configure Offset RBW Filter (Array) | Configures the offset RBW and the offset RBW filter type arrays. Use "subblock<n>" as the selector string to configure from this VI. |
| RFmxLTE SEM Configure Offset Limit Fail Mask (Array) | Configures the array of limit fail mask of the offset segments that specifies the criteria to determine the measurement fail status. Use "subblock<n>" as the selector string to read results from this VI. |
| RFmxLTE SEM Configure Offset Absolute Limit (Array) | Configures the array of the start limit and the stop limit of the offset segments. Use "subblock<n>" as the selector string to configure this VI. |
| RFmxLTE SEM Configure Offset Relative Limit (Array) | Configures the array of start and stop relative limits of the offset segments. Use "subblock<n>" as the selector string to read results from this VI. |

<!--NI_TOPIC bundle=rfmx-lte-vi path=rfmxltevi/utility_pal.html language=enus -->
## TOPIC 00091: Utility

- bundle_id: `rfmx-lte-vi`
- source_path: `rfmxltevi/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-vi/raw/resource/enus/rfmxltevi/utility_pal.html
- document_id: `rfmx-lte-vi`
- page_type: `leaf`
- content_type: ``

Utility

Owning Palette:

RFmx LTE VIs

Use the VIs on this palette to configure RFmx LTE utilities.

| Palette Object | Description |
| --- | --- |
| RFmxLTE Commit | Commits settings to the hardware. Calling this VI is optional. RFmxLTE commits settings to the hardware when you call the RFmxLTE Initiate VI. |
| RFmxLTE Reset to Default | Resets a signal to the default values. |
| RFmxLTE Wait for Measurement Complete | Waits for the specified number for seconds for all the measurements to complete. |
| RFmxLTE Check Measurement Status | Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
