# NI DOCUMENT BUNDLE: rfmxevdo-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxevdo-labview-api-ref start=1 end=95 -->
<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo-p.html language=enus -->
## TOPIC 00001: RFmxEVDO Properties

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo-p.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo-p.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RFmxEVDO properties to access options for configuring and fetching measurements. © 2015–2026 National Instruments Corporation. All rights reserved.

### RFmxEVDO Properties

Use the RFmxEVDO properties to access options for configuring and fetching measurements.

© 2015–2026 National Instruments Corporation. All rights reserved.

- [ACP:Advanced:Far IF Output Power Offset (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801036.html) Specifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the ACP Meas Method property to Dynamic Range and set the ACP IF Output Power Offset Auto property to False .
- [ACP:Advanced:IF Output Power Offset Auto](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801034.html) Specifies whether the measurement calculates an IF output power level offset for the offset channels to improve the dynamic range of the adjacent channel power (ACP) measurement. This property is used only if you set the ACP Meas Method property to Dynamic Range .
- [ACP:Advanced:Near IF Output Power Offset (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801035.html) Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the ACP Meas Method property to Dynamic Range and set the ACP IF Output Power Offset Auto property to False .
- [ACP:Advanced:Sequential FFT Size](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801038.html) Specifies the number of bins to use for FFT computation when the ACP Meas Method property is set to Sequential FFT .
- [ACP:All Traces Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801021.html) Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement.
- [ACP:Averaging:Count](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801015.html) Specifies the number of acquisitions used for averaging when you set the ACP Averaging Enabled property to True .
- [ACP:Averaging:Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801016.html) Specifies whether to enable averaging for the ACP measurement.
- [ACP:Averaging:Type](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801018.html) Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.
- [ACP:Carrier:Integration Bandwidth (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801005.html) Returns the ACP carrier integration bandwidth. This value is expressed in Hz.
- [ACP:FFT:Overlap (%)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80103a.html) Returns the number of samples to overlap between consecutive chunks while performing FFT.
- [ACP:FFT:Overlap Mode](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801039.html) Specifies how the FFT overlap is applied to the acquired samples.
- [ACP:Measurement Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801000.html) Specifies whether to enable the ACP measurement.
- [ACP:Measurement Method](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801012.html) Specifies the method for performing the adjacent channel power (ACP) measurement.
- [ACP:Noise Compensation Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801020.html) Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.
- [ACP:Number of Analysis Threads](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801014.html) Specifies the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement.
- [ACP:Offset:Frequency (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80100a.html) Returns the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz.
- [ACP:Offset:Integration Bandwidth (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80100e.html) Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz.
- [ACP:Offset:Number of Offsets](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801008.html) Specifies the number of offset channels for the adjacent channel power (ACP) measurement.
- [ACP:Offset:Power Reference:Carrier](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80100c.html) Specifies the carrier number that is used as the power reference to measure the offset channel relative power.
- [ACP:Offset:Power Reference:Specific](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80100d.html) Specifies the index of the carrier used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the ACP Offset Pwr Ref Carrier property to Specific .
- [ACP:RBW Filter:Auto Bandwidth](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80101b.html) Specifies whether the measurement computes the RBW.
- [ACP:RBW Filter:Bandwidth (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80101c.html) Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the ACP RBW Auto property to False . This value is expressed in Hz.
- [ACP:RBW Filter:Type](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80101d.html) Specifies the shape of the digital RBW filter.
- [ACP:Results:Carrier:Absolute Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801026.html) Returns the absolute measured carrier power. This value is expressed in dBm.
- [ACP:Results:Carrier:Relative Power (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801027.html) Returns the relative measured carrier power. This value is expressed in dB.
- [ACP:Results:Lower Offset:Absolute Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80102c.html) Returns the absolute measured lower offset channel power. This value is expressed in dBm.
- [ACP:Results:Lower Offset:Relative Power (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80102d.html) Returns the lower offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB.
- [ACP:Results:Total Carrier Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801022.html) Returns the total carrier power measured by the adjacent channel power (ACP) measurement. This value is expressed in dBm.
- [ACP:Results:Upper Offset:Absolute Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801032.html) Returns the absolute measured upper offset channel power. This value is expressed in dBm.
- [ACP:Results:Upper Offset:Relative Power (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801033.html) Returns the upper offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB.
- [ACP:Sweep Time:Auto](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80101e.html) Specifies whether the measurement computes the sweep time.
- [ACP:Sweep Time:Interval (s)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80101f.html) Specifies the sweep time when you set the ACP Sweep Time Auto property to False . This value is expressed in seconds.
- [Advanced:Auto Level Initial Reference Level (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80d000.html) Specifies the reference level at which the auto leveling process starts finding the optimal reference level. This value is expressed in dBm.
- [Advanced:Limited Configuration Change](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80d003.html) Specifies the set of properties that are considered by RFmx in the locked signal configuration state.
- [Band Class](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800010.html) Specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5- Band Class List, of the 3GPP2 C.S0057-F specification v1.0.
- [CDA:All Traces Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81300e.html) Specifies whether to enable the traces after performing the CDA measurement.
- [CDA:IQ Gain Imbalance Removal Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81300b.html) Specifies whether to remove the I/Q gain imbalance before the CDA measurement.
- [CDA:IQ Offset Removal Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81300a.html) Specifies whether to remove the I/Q offset before the CDA measurement.
- [CDA:IQ Quadrature Error Removal Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81300c.html) Specifies whether to remove the I/Q quadrature error before the CDA measurement.
- [CDA:Measurement Channel:Uplink:Branch](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813007.html) Specifies the Walsh branch of the channel, subject to channel-specific analysis.
- [CDA:Measurement Channel:Uplink:Walsh Code Length](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813005.html) Specifies the Walsh code length of the channel, subject to channel-specific analysis.
- [CDA:Measurement Channel:Uplink:Walsh Code Number](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813006.html) Specifies the Walsh code number of the channel, subject to channel-specific analysis.
- [CDA:Measurement Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813000.html) Specifies whether to enable the CDA measurement.
- [CDA:Measurement Length (slots)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813004.html) Specifies the duration of the CDA measurement. This value is expressed in slots.
- [CDA:Measurement Offset (slots)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813003.html) Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the CDA Sync Mode property.
- [CDA:Power Unit](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813008.html) Specifies the measurement unit of the code domain power results.
- [CDA:Receive Filter Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81300d.html) Specifies whether to enable receive filtering.
- [CDA:Results:Chip Rate Error (ppm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813012.html) Returns the chip rate error. This value is expressed in ppm.
- [CDA:Results:Frequency Error (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813011.html) Returns the frequency error. This value is expressed in Hz.
- [CDA:Results:I/Q Gain Imbalance (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813014.html) Returns the I/Q gain imbalance. This value is expressed in dB.
- [CDA:Results:I/Q Origin Offset (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813013.html) Returns the I/Q origin offset. This value is expressed in dB.
- [CDA:Results:I/Q Quadrature Error (deg)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813015.html) Returns the I/Q quadrature error. This value is expressed in degrees.
- [CDA:Results:Uplink:I Mean Active Power (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813021.html) Returns the average power of all active code channels measured on the I-branch. If you set the CDA Power Unit property to dBm , the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.
- [CDA:Results:Uplink:I Peak Inactive Power (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813022.html) Returns the largest measured code power among the set of inactive channels on the I-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm , the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.
- [CDA:Results:Uplink:Mean Active Power (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81301d.html) Returns the average power of all active code channels. If you set the CDA Power Unit property to dBm , the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.
- [CDA:Results:Uplink:Mean Auxiliary Pilot Power (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813026.html) Returns the mean power of the Reverse Auxiliary Pilot Channel (R-APICH). This value is expressed in dB or dBm.
- [CDA:Results:Uplink:Mean Inactive Power (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81301f.html) Returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm , the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.
- [CDA:Results:Uplink:Mean Pilot Power (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813025.html) Returns the mean power of the Reverse Pilot channel (R-PICH). This value is expressed in dB or dBm.
- [CDA:Results:Uplink:Mean Symbol Power (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81301a.html) Returns the mean symbol power of the configured measurement channel. This value is expressed in dB or dBm.
- [CDA:Results:Uplink:Peak Active Power (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81301e.html) Returns the maximum power among all the active code channels. If you set the CDA Power Unit property to dBm , the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.
- [CDA:Results:Uplink:Peak Inactive Power (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813020.html) Returns the largest measured code power among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm , the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.
- [CDA:Results:Uplink:Peak Symbol EVM (%)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813017.html) Returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage.
- [CDA:Results:Uplink:Q Mean Active Power (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813023.html) Returns the average power of all active code channels measured on the Q-branch. If you set the CDA Power Unit property to dBm , the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.
- [CDA:Results:Uplink:Q Peak Inactive Power (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813024.html) Returns the largest measured code power among the set of inactive channels on the Q-branch, and in the code domain of the base spreading factor. This value is expressed in dB or dBm. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1, and 32 otherwise.
- [CDA:Results:Uplink:RMS Symbol EVM (%)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813016.html) Returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage.
- [CDA:Results:Uplink:RMS Symbol Magnitude Error (%)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813018.html) Returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage.
- [CDA:Results:Uplink:RMS Symbol Phase Error (deg)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813019.html) Returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees.
- [CDA:Results:Uplink:Total Active Power (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81301c.html) Returns the sum of the powers of all active code channels. If you set the CDA Power Unit property to dBm , the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.
- [CDA:Results:Uplink:Total Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81301b.html) Returns the mean power of the received signal. This value is expressed in dBm.
- [CDA:Spectrum Inverted](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813009.html) Specifies whether the signal spectrum is inverted.
- [CDA:Synchronization Mode](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813002.html) Specifies whether the measurement is performed from the frame, slot, or symbol boundary.
- [CHP:All Traces Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr803014.html) Specifies whether to enable the traces to be stored and retrieved after performing the channel power (CHP) measurement.
- [CHP:Averaging:Count](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr803006.html) Specifies the number of acquisitions used for averaging when you set the CHP Averaging Enabled property to True .
- [CHP:Averaging:Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr803007.html) Specifies whether to enable averaging for the channel power (CHP) measurement.
- [CHP:Averaging:Type](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr803009.html) Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the channel power (CHP) measurement.
- [CHP:Carrier Integration Bandwidth (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr803002.html) Returns the CHP carrier integration bandwidth. This value is expressed in Hz.
- [CHP:Measurement Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr803000.html) Specifies whether to enable the channel power (CHP) measurement.
- [CHP:Number of Analysis Threads](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr803003.html) Specifies the maximum number of threads used for parallelism for the channel power (CHP) measurement.
- [CHP:RBW Filter:Auto Bandwidth](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80300c.html) Specifies whether the measurement computes the RBW.
- [CHP:RBW Filter:Bandwidth (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80300d.html) Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the CHP RBW Auto property to False . This value is expressed in Hz.
- [CHP:RBW Filter:Type](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80300e.html) Specifies the shape of the digital RBW filter.
- [CHP:Results:Carrier:Absolute Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr803015.html) Returns the absolute averaged channel power (CHP) for a specific carrier. This value is expressed in dBm.
- [CHP:Results:Carrier:Relative Power (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr803019.html) Returns the relative averaged channel power (CHP) for a specific carrier. This value is expressed in dB.
- [CHP:Results:Total Carrier Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr803018.html) Returns the sum of all the active carrier powers. This value is expressed in dBm.
- [CHP:Sweep Time:Auto](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr803011.html) Specifies whether the measurement computes the sweep time.
- [CHP:Sweep Time:Interval (s)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr803012.html) Specifies the sweep time when you set the CHP Sweep Time Auto property to False . This value is expressed in seconds.
- [Carrier:Channel:Configuration Mode](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800012.html) Specifies whether to detect the channels automatically or to use a specified channel configuration.
- [Carrier:Channel:User Defined:Uplink:Branch](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80001c.html) Specifies the quadrature branch on which a specific user defined-channel is mapped. This property is used only when you set the Channel Configuration Mode property to User Defined .
- [Carrier:Channel:User Defined:Uplink:Data Modulation Type](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800019.html) Defines the modulation of the data channel. This property is used only when you set the Channel Configuration Mode property to User Defined .
- [Carrier:Channel:User Defined:Uplink:Number of Channels](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800018.html) Specifies the number of user-defined channels. This property is used only when you set the Channel Configuration Mode property to User Defined .
- [Carrier:Channel:User Defined:Uplink:Walsh Code Length](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80001a.html) Specifies the Walsh Code Length of a specific user-defined channel. This property is used only when you set the Channel Configuration Mode property to User Defined .
- [Carrier:Channel:User Defined:Uplink:Walsh Code Number](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80001b.html) Specifies the Walsh Code Number of a specific user-defined channel. This property is used only when you set the Channel Configuration Mode property to User Defined .
- [Carrier:Frequency (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80000f.html) Specifies the carrier frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency.
- [Carrier:Number of Carriers](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80000e.html) Specifies the number of carriers in the signal.
- [Carrier:Physical Layer Subtype](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800011.html) Selects the EV-DO physical layer subtype.
- [Carrier:Spreading:Uplink:I mask](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800029.html) Specifies the long code mask of the in-phase (I) channel.
- [Carrier:Spreading:Uplink:Q mask](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80002a.html) Specifies the long code mask of the quadrature (Q) channel.
- [Center Frequency (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800001.html) Specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz.
- [External Attenuation (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800003.html) Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB.
- [ModAcc:All Traces Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81100c.html) Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement.
- [ModAcc:IQ Gain Imbalance Removal Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr8110a1.html) Specifies whether to remove the I/Q gain imbalance before the EVM measurement.
- [ModAcc:IQ Offset Removal Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811007.html) Specifies whether to remove the I/Q offset before the EVM measurement.
- [ModAcc:IQ Quadrature Error Removal Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr8110a2.html) Specifies whether to remove the I/Q quadrature error before the EVM measurement.
- [ModAcc:Measurement Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811000.html) Specifies whether to enable the ModAcc measurement.
- [ModAcc:Measurement Length (slots)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811005.html) Specifies the duration of the modulation accuracy measurement.
- [ModAcc:Measurement Offset (slots)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811004.html) Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the ModAcc Sync Mode property.
- [ModAcc:Multi Carrier Filter:Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811008.html) Enables the multi-carrier filter that can increase the multi-carrier interference suppression to improve ModAcc measurement quality in the presence of neighboring carriers.
- [ModAcc:Receive Filter Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr8110a3.html) Specifies whether to enable receive filtering.
- [ModAcc:Results:Chip Rate Error (ppm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811010.html) Returns the chip rate error averaged over all measured slots. This value is expressed in parts per million (ppm).
- [ModAcc:Results:Frequency Error (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81100f.html) Returns the frequency error averaged over all measured slots. This value is expressed in Hz.
- [ModAcc:Results:I/Q Gain Imbalance (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811012.html) Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB.
- [ModAcc:Results:I/Q Origin Offset (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811011.html) Returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB.
- [ModAcc:Results:I/Q Quadrature Error (deg)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811013.html) Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees.
- [ModAcc:Results:Uplink:Detected Channels:Branch](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811023.html) Returns the quadrature branch of a particular detected channel.
- [ModAcc:Results:Uplink:Detected Channels:Code Length](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811021.html) Returns the Walsh Code length of a detected channel.
- [ModAcc:Results:Uplink:Detected Channels:Code Number](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811022.html) Returns the Walsh Code number of a detected channel.
- [ModAcc:Results:Uplink:Detected Data Modulation Type](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101f.html) Returns the modulation type of the uplink data channel.
- [ModAcc:Results:Uplink:Number of Detected Channels](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811020.html) Returns the total number of detected channels.
- [ModAcc:Results:Uplink:Peak Active CDE (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101c.html) Returns the peak code domain error (CDE) value among the active Walsh channels. This value is expressed in dB.
- [ModAcc:Results:Uplink:Peak Active CDE Branch](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81104e.html) Returns the quadrature branch of the channel corresponding to the Peak Active CDE (dB) result.
- [ModAcc:Results:Uplink:Peak Active CDE Walsh Code Length](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101d.html) The Walsh code length of the active Walsh channel for which the peak CDE has been observed.
- [ModAcc:Results:Uplink:Peak Active CDE Walsh Code Number](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101e.html) Returns the Walsh code number of the channel corresponding to the ModAcc:Uplink:Peak Active CDE (dB) result.
- [ModAcc:Results:Uplink:Peak CDE (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811019.html) Returns the peak uplink code domain error (CDE), expressed in dB.
- [ModAcc:Results:Uplink:Peak CDE Branch](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81104d.html) Returns the branch of the channel corresponding to the Peak Active CDE (dB) property result.
- [ModAcc:Results:Uplink:Peak CDE Walsh Code Number](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101b.html) Returns the Walsh code number of the channel corresponding to the ModAcc:Uplink:Peak CDE (db) result.
- [ModAcc:Results:Uplink:Peak EVM (%)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811015.html) Returns the peak value of the uplink error vector magnitude (EVM), averaged over all measured slots. This value is expressed as a percentage.
- [ModAcc:Results:Uplink:RMS EVM (%)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811014.html) Returns the RMS of the uplink error vector magnitude (EVM), averaged over all measured slots. This value is expressed as a percentage.
- [ModAcc:Results:Uplink:RMS Magnitude Error (%)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811016.html) Returns the RMS of the magnitude error. This value is expressed as a percentage.
- [ModAcc:Results:Uplink:RMS Phase Error (Deg)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811017.html) Returns the RMS of the phase error. This value is expressed in degrees.
- [ModAcc:Results:Uplink:Rho](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811018.html) Returns the measured Rho value of the analyzed signal.
- [ModAcc:Spectrum Inverted](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811006.html) Specifies whether the measured spectrum is inverted.
- [ModAcc:Synchronization Mode](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811002.html) Specifies whether the measurement is performed from frame, slot, or symbol boundary.
- [OBW:All Traces Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr806012.html) Specifies whether to enable the traces to be stored and retrieved after performing the occupied bandwidth (OBW) measurement.
- [OBW:Averaging:Count](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr806006.html) Specifies the number of acquisitions used for averaging when you set the OBW Averaging Enabled property to True .
- [OBW:Averaging:Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr806007.html) Specifies whether to enable averaging for the occupied bandwidth (OBW) measurement.
- [OBW:Averaging:Type](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr806009.html) Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for occupied bandwidth (OBW) measurement.
- [OBW:Measurement Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr806000.html) Specifies whether to enable the occupied bandwidth (OBW) measurement.
- [OBW:Number of Analysis Threads](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr806003.html) Specifies the maximum number of threads used for parallelism for the occupied bandwidth (OBW) measurement.
- [OBW:RBW Filter:Auto Bandwidth](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600c.html) Specifies whether the measurement computes the RBW.
- [OBW:RBW Filter:Bandwidth (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600d.html) Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the OBW RBW Auto property to False . This value is expressed in Hz.
- [OBW:RBW Filter:Type](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600e.html) Specifies the shape of the digital RBW filter.
- [OBW:Results:Absolute Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr806014.html) Returns the absolute power measured in the occupied bandwidth (OBW). This value is expressed in dBm.
- [OBW:Results:Occupied Bandwidth (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr806013.html) Returns the bandwidth that occupies 99 percent of the total power of the signal. This value is expressed in Hz.
- [OBW:Results:Start Frequency (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr806015.html) Returns the start frequency of the occupied bandwidth (OBW). This value is expressed in Hz.
- [OBW:Results:Stop Frequency (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr806016.html) Returns the stop frequency of the occupied bandwidth (OBW). This value is expressed in Hz.
- [OBW:Span (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr806004.html) Returns the frequency span of the OBW measurement. This value is expressed in Hz.
- [OBW:Sweep Time:Auto](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600f.html) Specifies whether the measurement computes the sweep time.
- [OBW:Sweep Time:Interval (s)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr806010.html) Specifies the sweep time when you set the OBW Sweep Time Auto property to False . This value is expressed in seconds.
- [Reference Level](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800002.html) Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.
- [Reference Level Headroom](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800ffc.html) Specifies the margin RFmx adds to the Reference Level property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.
- [Result Fetch Timeout (s)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80c000.html) Specifies the time to wait before results are available in the RFmxEVDO Property Node . This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxEVDO Property Node waits until the measurement is complete.
- [SEM:All Traces Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808027.html) Specifies whether to enable the traces to be stored and retrieved after performing the spectral emissions mask (SEM) measurement.
- [SEM:Averaging:Count](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80801e.html) Specifies the number of acquisitions used for averaging when you set the SEM Averaging Enabled property to True .
- [SEM:Averaging:Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80801f.html) Specifies whether to enable averaging for the spectral emissions mask (SEM) measurement.
- [SEM:Averaging:Type](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808021.html) Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the spectral emissions mask (SEM) measurement.
- [SEM:Carrier:Integration Bandwidth (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808005.html) Returns the SEM carrier integration bandwidth. This value is expressed in Hz.
- [SEM:Measurement Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808000.html) Specifies whether to enable the spectral emissions mask (SEM) measurement.
- [SEM:Number of Analysis Threads](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80801d.html) Specifies the maximum number of threads used for parallelism for the spectral emissions mask (SEM) measurement.
- [SEM:Offset:Bandwidth Integral](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80800c.html) Returns the bandwidth integral for a specific offset segment.
- [SEM:Offset:Number of Offsets](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80800b.html) Returns the number of SEM offset segments.
- [SEM:Offset:RBW Filter:Bandwidth (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808017.html) Returns the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz.
- [SEM:Offset:RBW Filter:Type](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808018.html) Returns the type of RBW filter used to sweep the offset segment.
- [SEM:Offset:Start Frequency (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808014.html) Returns the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.
- [SEM:Offset:Stop Frequency (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808015.html) Returns the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.
- [SEM:Results:Carrier:Absolute Integrated Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80802d.html) Returns the absolute carrier power measurement. This value is expressed in dBm.
- [SEM:Results:Carrier:Absolute Peak Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80802f.html) Returns the peak absolute carrier power. This value is expressed in dBm.
- [SEM:Results:Carrier:Peak Frequency (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808030.html) Returns the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz.
- [SEM:Results:Carrier:Relative Integrated Power (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80802e.html) Returns the relative carrier power measurement. This value is expressed in dB.
- [SEM:Results:Composite Measurement Status](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808029.html) Indicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment.
- [SEM:Results:Lower Offset:Absolute Integrated Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808034.html) Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.
- [SEM:Results:Lower Offset:Absolute Peak Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808036.html) Returns the peak absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.
- [SEM:Results:Lower Offset:Margin (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808039.html) Returns the margin from the limit mask value specified by the standard. This value is expressed in dB.
- [SEM:Results:Lower Offset:Margin Absolute Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80803a.html) Returns the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm.
- [SEM:Results:Lower Offset:Margin Frequency (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80803c.html) Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz.
- [SEM:Results:Lower Offset:Margin Relative Power (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80803b.html) Returns the power at which the margin occurred in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB.
- [SEM:Results:Lower Offset:Measurement Status](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80803d.html) Indicates the lower offset segment measurement status based on measurement limits and the failure criteria specified by the standard.
- [SEM:Results:Lower Offset:Peak Frequency (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808038.html) Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz.
- [SEM:Results:Lower Offset:Relative Integrated Power (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808035.html) Returns the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier.
- [SEM:Results:Lower Offset:Relative Peak Power (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808037.html) Returns the peak power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB.
- [SEM:Results:Total Carrier Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808028.html) Returns the total carrier power of the selected carrier. This value is expressed in dBm.
- [SEM:Results:Upper Offset:Absolute Integrated Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808041.html) Returns the absolute power measured in the upper (positive) offset segment. This value is expressed in dBm.
- [SEM:Results:Upper Offset:Absolute Peak Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808043.html) Returns the peak absolute power measured in the upper (positive) offset segment. This value is expressed in dBm.
- [SEM:Results:Upper Offset:Margin (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808046.html) Returns the margin from the limit mask value specified by the standard. This value is expressed in dB.
- [SEM:Results:Upper Offset:Margin Absolute Power (dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808047.html) Returns the power at which the margin occurred in the upper (positive) offset segment, relative to the integrated power of the reference carrier. This value is expressed in dBm.
- [SEM:Results:Upper Offset:Margin Frequency (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808049.html) Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.
- [SEM:Results:Upper Offset:Margin Relative Power (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808048.html) Returns the power at which the margin occurred in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB.
- [SEM:Results:Upper Offset:Measurement Status](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80804a.html) Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard.
- [SEM:Results:Upper Offset:Peak Frequency (Hz)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808045.html) Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz.
- [SEM:Results:Upper Offset:Relative Integrated Power (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808042.html) Returns the power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB.
- [SEM:Results:Upper Offset:Relative Peak Power (dB)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808044.html) Returns the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB.
- [SEM:Sweep Time:Auto](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808025.html) Specifies whether the measurement computes the sweep time.
- [SEM:Sweep Time:Interval (s)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr808026.html) Specifies the sweep time when you set the SEM Sweep Time Auto property to False . This value is expressed in seconds.
- [Selected Ports](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800ffd.html) Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names.
- [Selector String](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800000.html) Specifies the selector string used to access all subsequent channel-based properties in this instance of the property node.
- [SlotPhase:All Traces Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr815008.html) Specifies whether to enable the traces after performing the SlotPhase measurement.
- [SlotPhase:Measurement Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr815000.html) Specifies whether to enable the SlotPhase measurement.
- [SlotPhase:Measurement Length (slots)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr815004.html) Specifies the duration of the SlotPhase measurement. This value is expressed in slots.
- [SlotPhase:Measurement Offset (slots)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr815003.html) Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPhase Sync Mode property.
- [SlotPhase:Receive Filter Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr815006.html) Specifies whether to enable receive filtering.
- [SlotPhase:Results:Maximum Half Slot Phase Discontinuity (deg)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81500b.html) Returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees.
- [SlotPhase:Spectrum Inverted](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr815005.html) Specifies whether the signal spectrum is inverted.
- [SlotPhase:Synchronization Mode](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr815002.html) Specifies whether the measurement is performed from the frame or the slot boundary.
- [SlotPhase:Transient Duration (s)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr815007.html) Specifies the transient duration for the SlotPhase measurement. This value is expressed in seconds.
- [SlotPower:Measurement Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr814000.html) Specifies whether to enable the SlotPower measurement.
- [SlotPower:Measurement Length (slots)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr814004.html) Specifies the duration of the SlotPower measurement. This value is expressed in slots.
- [SlotPower:Measurement Offset (slots)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr814003.html) Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPower Sync Mode property.
- [SlotPower:Receive Filter Enabled](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr814006.html) Specifies whether to enable receive filtering.
- [SlotPower:Spectrum Inverted](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr814005.html) Specifies whether the signal spectrum is inverted.
- [SlotPower:Synchronization Mode](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr814002.html) Specifies whether the measurement is performed from the frame or the slot boundary.
- [Trigger:Delay (s)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80000a.html) Specifies the trigger delay time. This value is expressed in seconds.
- [Trigger:Digital Edge:Edge](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800006.html) Specifies the active edge for the trigger. This property is used only when you set the Trigger Type property to Digital Edge .
- [Trigger:Digital Edge:Source](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800005.html) Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge .
- [Trigger:IQ Power Edge:Level (dB or dBm)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800008.html) Specifies the power level at which the device triggers. This value is expressed in dB when the IQ Power Edge Level Type property is set to Relative and in dBm when the IQ Power Edge Level Type property is set to Absolute . The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Level Type](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800fff.html) Specifies the reference for the IQ Power Edge Level property. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Slope](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800009.html) Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Source](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800007.html) Specifies the channel from which the device monitors the trigger. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:Minimum Quiet Time:Duration (s)](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80000c.html) Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope property to Rising Slope , the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to Falling Slope , the signal is quiet above the trigger level.
- [Trigger:Minimum Quiet Time:Mode](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80000b.html) Specifies whether the measurement computes the minimum quiet time used for triggering.
- [Trigger:Type](../../../resource/objmgr/rfmxevdo-rc/rfmxevdo/attr800004.html) Specifies the trigger type.

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80100e.html language=enus -->
## TOPIC 00002: ACP:Offset:Integration Bandwidth (Hz)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80100e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80100e.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name ACP Offset IBW (Hz) Data type cdbl.png Permissions Read Only High-

### ACP:Offset:Integration Bandwidth (Hz)

Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Offset IBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801016.html language=enus -->
## TOPIC 00003: ACP:Averaging:Enabled

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801016.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the ACP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remar

### ACP:Averaging:Enabled

Specifies whether to enable averaging for the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Averaging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO ACP Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The ACP measurement uses the Averaging Count property as the number of acquisitions over which the ACP measurement is averaged. |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801020.html language=enus -->
## TOPIC 00004: ACP:Noise Compensation Enabled

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801020.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801020.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax

### ACP:Noise Compensation Enabled

Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Noise Comp Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO ACP Configure Noise Compensation Enabled |
| Resettable | Yes |

| False | 0 | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| --- | --- | --- |
| True | 1 | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842/5860 |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801021.html language=enus -->
## TOPIC 00005: ACP:All Traces Enabled

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801021.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801021.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named s

### ACP:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80102c.html language=enus -->
## TOPIC 00006: ACP:Results:Lower Offset:Absolute Power (dBm)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80102c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80102c.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute measured lower offset channel power. This value is expressed in dBm. Use "offset<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ACP Results Lower Offset Abs Pwr Data type cdbl.png Permissions R

### ACP:Results:Lower Offset:Absolute Power (dBm)

Returns the absolute measured lower offset channel power. This value is expressed in dBm.

Use "offset*<n>*" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Results Lower Offset Abs Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ACP Fetch |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80102d.html language=enus -->
## TOPIC 00007: ACP:Results:Lower Offset:Relative Power (dB)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80102d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80102d.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lower offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ACP Results

### ACP:Results:Lower Offset:Relative Power (dB)

Returns the lower offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB.

Use "offset*<n>*" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Results Lower Offset Rel Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ACP Fetch |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801035.html language=enus -->
## TOPIC 00008: ACP:Advanced:Near IF Output Power Offset (dB)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801035.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr801035.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the ACP Meas Method property to Dynamic Range and set the ACP IF Output Power Off

### ACP:Advanced:Near IF Output Power Offset (dB)

Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the [ACP Meas Method](/csh?topicname=attr801012.html) property to **Dynamic Range** and set the [ACP IF Output Power Offset Auto](/csh?topicname=attr801034.html) property to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Near IF Output Power Offset (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600d.html language=enus -->
## TOPIC 00009: OBW:RBW Filter:Bandwidth (Hz)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600d.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the OBW RBW Auto property to False. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings top

### OBW:RBW Filter:Bandwidth (Hz)

Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the [OBW RBW Auto](/csh?topicname=attr80600c.html) property to **False**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 30 kHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW RBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO OBW Configure RBW Filter |
| Resettable | Yes |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600e.html language=enus -->
## TOPIC 00010: OBW:RBW Filter:Type

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600e.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Gaussian. Remarks The follow

### OBW:RBW Filter:Type

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Gaussian**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW RBW Filter Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO OBW Configure RBW Filter |
| Resettable | Yes |

| FFT Based | 0 | An RBW filter with an FFT-Based response is applied. |
| --- | --- | --- |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600f.html language=enus -->
## TOPIC 00011: OBW:Sweep Time:Auto

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr80600f.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is True. Remarks Th

### OBW:Sweep Time:Auto

Specifies whether the measurement computes the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Sweep Time Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO OBW Configure Sweep Time |
| Resettable | Yes |

| False | 0 | The measurement uses the sweep time that you specify in the OBW Sweep Time property. |
| --- | --- | --- |
| True | 1 | The measurement uses the default sweep time of 1.67 ms. |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811012.html language=enus -->
## TOPIC 00012: ModAcc:Results:I/Q Gain Imbalance (dB)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811012.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about

### ModAcc:Results:I/Q Gain Imbalance (dB)

Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results I/Q Gain Imbalance (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811013.html language=enus -->
## TOPIC 00013: ModAcc:Results:I/Q Quadrature Error (deg)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811013.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information

### ModAcc:Results:I/Q Quadrature Error (deg)

Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in
 degrees.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results I/Q Quadrature Error (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811014.html language=enus -->
## TOPIC 00014: ModAcc:Results:Uplink:RMS EVM (%)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811014.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS of the uplink error vector magnitude (EVM), averaged over all measured slots. This value is expressed as a percentage. You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for info

### ModAcc:Results:Uplink:RMS EVM (%)

Returns the RMS of the uplink error vector magnitude (EVM), averaged over all measured slots. This
 value is expressed as a percentage.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results UL RMS EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811016.html language=enus -->
## TOPIC 00015: ModAcc:Results:Uplink:RMS Magnitude Error (%)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811016.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS of the magnitude error. This value is expressed as a percentage. You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Rem

### ModAcc:Results:Uplink:RMS Magnitude Error (%)

Returns the RMS of the magnitude error. This value is expressed as a percentage.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results UL RMS Magnitude Error (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811017.html language=enus -->
## TOPIC 00016: ModAcc:Results:Uplink:RMS Phase Error (Deg)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811017.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811017.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS of the phase error. This value is expressed in degrees. You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. Remarks The

### ModAcc:Results:Uplink:RMS Phase Error (Deg)

Returns the RMS of the phase error. This value is expressed in degrees.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results UL RMS Phase Error (Deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101c.html language=enus -->
## TOPIC 00017: ModAcc:Results:Uplink:Peak Active CDE (dB)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101c.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak code domain error (CDE) value among the active Walsh channels. This value is expressed in dB. You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string

### ModAcc:Results:Uplink:Peak Active CDE (dB)

Returns the peak code domain error (CDE) value among the active Walsh channels. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results UL Pk Active CDE (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101d.html language=enus -->
## TOPIC 00018: ModAcc:Results:Uplink:Peak Active CDE Walsh Code Length

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101d.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Walsh code length of the active Walsh channel for which the peak CDE has been observed. You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named s

### ModAcc:Results:Uplink:Peak Active CDE Walsh Code Length

The Walsh code length of the active Walsh channel for which the peak CDE has been observed.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results UL Pk Active CDE Walsh Code Length |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101e.html language=enus -->
## TOPIC 00019: ModAcc:Results:Uplink:Peak Active CDE Walsh Code Number

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101e.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Walsh code number of the channel corresponding to the ModAcc:Uplink:Peak Active CDE (dB) result. You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string s

### ModAcc:Results:Uplink:Peak Active CDE Walsh Code Number

Returns the Walsh code number of the channel corresponding to the [ModAcc:Uplink:Peak Active CDE (dB)](/csh?topicname=attr81101c.html) result.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results UL Pk Active CDE Walsh Code Number |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101f.html language=enus -->
## TOPIC 00020: ModAcc:Results:Uplink:Detected Data Modulation Type

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81101f.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the modulation type of the uplink data channel. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Remarks The following table lists the ch

### ModAcc:Results:Uplink:Detected Data Modulation Type

Returns the modulation type of the uplink data channel.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results UL Detected Data Mod Type |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

| Data Channel Absent | 1 | The specified uplink data channel is absent. |
| --- | --- | --- |
| B4 | 2 | The specified uplink data channel uses binary phase shift keying (BPSK) with the Walsh function W(4,2). |
| Q4 | 3 | The specified uplink data channel uses quadrature phase shift keying (QPSK) with the Walsh function W(4,2). |
| Q2 | 4 | The specified uplink data channel uses QPSK with the Walsh function W(2,1). |
| Q4Q2 | 5 | The specified uplink data channel uses QPSK with the Walsh functions W(4,2) and W(2,1). |
| E4E2 | 6 | The specified uplink data channel 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811023.html language=enus -->
## TOPIC 00021: ModAcc:Results:Uplink:Detected Channels:Branch

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811023.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr811023.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the quadrature branch of a particular detected channel. Use "channel<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ModAcc Results UL Detected Branch Data type ci32.png Permissions Read Only High-level VIs

### ModAcc:Results:Uplink:Detected Channels:Branch

Returns the quadrature branch of a particular detected channel.

Use "channel*<n>*" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results UL Detected Branch |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

| I | 0 | The detected channel occupies the in-phase branch. |
| --- | --- | --- |
| Q | 1 | The detected channel occupies the quadrature branch. |
| I and Q | 2 | The detected channel occupies the in-phase branch and the quadrature branch. |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81104e.html language=enus -->
## TOPIC 00022: ModAcc:Results:Uplink:Peak Active CDE Branch

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81104e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81104e.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the quadrature branch of the channel corresponding to the Peak Active CDE (dB) result. You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for name

### ModAcc:Results:Uplink:Peak Active CDE Branch

Returns the quadrature branch of the channel corresponding to the Peak Active CDE (dB) result.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results UL Pk Active CDE Branch |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

| I | 0 | The peak active CDE corresponds to the in-phase branch. |
| --- | --- | --- |
| Q | 1 | The peak active CDE corresponds to the quadrature branch. |
| I and Q | 2 | The peak active CDE corresponds to the in-phase branch and the quadrature branch. |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr8110a1.html language=enus -->
## TOPIC 00023: ModAcc:IQ Gain Imbalance Removal Enabled

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr8110a1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr8110a1.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q gain imbalance before the EVM measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value

### ModAcc:IQ Gain Imbalance Removal Enabled

Specifies whether to remove the I/Q gain imbalance before the EVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc IQ Gain Imbalance Removal Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The I/Q gain imbalance is not removed before the EVM measurement. |
| --- | --- | --- |
| True | 1 | The I/Q gain imbalance is removed before the EVM measurement. |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813002.html language=enus -->
## TOPIC 00024: CDA:Synchronization Mode

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813002.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame, slot, or symbol boundary. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The def

### CDA:Synchronization Mode

Specifies whether the measurement is performed from the frame, slot, or symbol boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Slot**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Sync Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots specified by the CDA Meas Length property starting at CDA Meas Offset slots from the frame boundary. |
| --- | --- | --- |
| Slot | 1 | The slot boundary is detected and the measurement is performed over the number of slots specified by CDA Meas Length number of slots, starting at CDA Meas Offset slots from the slot boundary. |
| Arbitrary | 2 | The symbol boundary is detected and the measurement is performed over the number of slots specified by the CDA Meas Length property, starting at CDA Meas Offset slots from the symbol boundary. |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813008.html language=enus -->
## TOPIC 00025: CDA:Power Unit

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813008.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813008.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement unit of the code domain power results. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is dB. Remark

### CDA:Power Unit

Specifies the measurement unit of the code domain power results.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **dB**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Pwr Unit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| dB | 0 | Specifies that the measurement unit is dB. |
| --- | --- | --- |
| dBm | 1 | Specifies that the measurement unit is dBm. |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81300a.html language=enus -->
## TOPIC 00026: CDA:IQ Offset Removal Enabled

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81300a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81300a.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q offset before the CDA measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Fals

### CDA:IQ Offset Removal Enabled

Specifies whether to remove the I/Q offset before the CDA measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA IQ Offset Removal Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The I/Q offset is not removed before the CDA measurement. |
| --- | --- | --- |
| True | 1 | The I/Q offset is removed before the CDA measurement. |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813016.html language=enus -->
## TOPIC 00027: CDA:Results:Uplink:RMS Symbol EVM (%)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr813016.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named s

### CDA:Results:Uplink:RMS Symbol EVM (%)

Returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results UL RMS Symbol EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81301e.html language=enus -->
## TOPIC 00028: CDA:Results:Uplink:Peak Active Power (dB or dBm)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81301e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81301e.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum power among all the active code channels. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. You do not need to use a selector string to read th

### CDA:Results:Uplink:Peak Active Power (dB or dBm)

Returns the maximum power among all the active code channels. If you set the [CDA Power Unit](/csh?topicname=attr813008.html) property to **dBm**, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results UL Pk Active Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81301f.html language=enus -->
## TOPIC 00029: CDA:Results:Uplink:Mean Inactive Power (dB or dBm)

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81301f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr81301f.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm, the measureme

### CDA:Results:Uplink:Mean Inactive Power (dB or dBm)

Returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise.
 If you set the [CDA Power Unit](/csh?topicname=attr813008.html) property to **dBm**, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results UL Mean Inactive Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr814000.html language=enus -->
## TOPIC 00030: SlotPower:Measurement Enabled

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr814000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr814000.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the SlotPower measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FALSE. Remarks The f

### SlotPower:Measurement Enabled

Specifies whether to enable the SlotPower measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPower Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=resource/objmgr/rfmxevdo-rc/rfmxevdo/attr815008.html language=enus -->
## TOPIC 00031: SlotPhase:All Traces Enabled

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `resource/objmgr/rfmxevdo-rc/rfmxevdo/attr815008.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxevdo-rc/rfmxevdo/attr815008.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces after performing the SlotPhase measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default v

### SlotPhase:All Traces Enabled

Specifies whether to enable the traces after performing the SlotPhase measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPhase All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxEVDO Properties

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-abort-measurements-vi.html language=enus -->
## TOPIC 00032: RFmxEVDO Abort Measurements VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-abort-measurements-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-abort-measurements-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. These measurements were previously initiated by the RFmxEVDO Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is

### RFmxEVDO Abort Measurements VI

Stops acquisition and measurements associated with the signal instance that you specify in the **Selector String** parameter. These measurements were previously initiated by the [RFmxEVDO Initiate](/csh?topicname=rfmxevdo-initiate-vi.html) VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='icon' src='rfmxevdo-abort-measurements-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-configure-number-of-offsets-vi.html language=enus -->
## TOPIC 00033: RFmxEVDO ACP Configure Number of Offsets VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-configure-number-of-offsets-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-configure-number-of-offsets-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of offset channel pairs for the adjacent channel power (ACP) measurement. Channel pairs consist of upper and lower offset channels. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the

### RFmxEVDO ACP Configure Number of Offsets VI

Configures the number of offset channel pairs for the adjacent channel power (ACP) measurement. Channel pairs consist of upper and lower offset channels.

[IMAGE alt='icon' src='rfmxevdo-acp-configure-number-of-offsets-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Offsets — Number of Offsets specifies the number of offset channel pairs. The default value is 2, which consists of 2 upper and 2 lower offset channels. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-configure-offset-power-reference-vi.html language=enus -->
## TOPIC 00034: RFmxEVDO ACP Configure Offset Power Reference VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-configure-offset-power-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-configure-offset-power-reference-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power reference of the offset channels in multi-carrier setups. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (

### RFmxEVDO ACP Configure Offset Power Reference VI

Configures the power reference of the offset channels in multi-carrier setups.

[IMAGE alt='icon' src='rfmxevdo-acp-configure-offset-power-reference-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Offset Power Reference Carrier — Offset Power Reference Carrier specifies how the reference power is selected. The default value is Composite. Closest (0) The measurement uses the carrier power closest to the center frequency of the offset channel as the power reference. Highest (1) The measurement uses the highest measured active carrier power as the power reference. Composite (2) The measurement uses total measured active carrier power as the power reference. Specific (3) The measurement uses the power measured in the carrier with index specified by the Offset Power Reference Specific property as the power reference. For single-carrier configurations, all options have the same behavior. Offset Power Reference Specific — Offset Power Reference Specific specifies the carrier number that is used as power reference. This parameter only applies if you set the Offset Power Reference Carrier parameter to Specific. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Closest (0) | The measurement uses the carrier power closest to the center frequency of the offset channel as the power reference. |
| Highest (1) | The measurement uses the highest measured active carrier power as the power reference. |
| Composite (2) | The measurement uses total measured active carrier power as the power reference. |
| Specific (3) | The measurement uses the power measured in the carrier with index specified by the Offset Power Reference Specific property as the power reference. |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-configure-rbw-filter-vi.html language=enus -->
## TOPIC 00035: RFmxEVDO ACP Configure RBW Filter VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-configure-rbw-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-configure-rbw-filter-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "

### RFmxEVDO ACP Configure RBW Filter VI

Configures the resolution bandwidth (RBW) filter.

[IMAGE alt='icon' src='rfmxevdo-acp-configure-rbw-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. RBW Auto — RBW Auto specifies whether the measurement calculates the RBW. The default value is True. True (1) RFmx EV-DO automatically computes the RBW. False (0) The measurement uses the RBW you specify. Refer to the RBW and Sweep Time section in the ACP topic for more details on RBW and sweep time. RBW (Hz) — RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 30 kHz. RBW Filter Type — RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| True (1) | RFmx EV-DO automatically computes the RBW. |
| False (0) | The measurement uses the RBW you specify. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-configure-sweep-time-vi.html language=enus -->
## TOPIC 00036: RFmxEVDO ACP Configure Sweep Time VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-configure-sweep-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-configure-sweep-time-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can u

### RFmxEVDO ACP Configure Sweep Time VI

Configures the sweep time.

[IMAGE alt='icon' src='rfmxevdo-acp-configure-sweep-time-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Sweep Time Auto — Sweep Time Auto specifies whether the measurement calculates the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of 1.67 ms. Sweep Time Interval (s) — Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1.67 ms. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of 1.67 ms. |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-fetch-absolute-powers-trace-vi.html language=enus -->
## TOPIC 00037: RFmxEVDO ACP Fetch Absolute Powers Trace VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-fetch-absolute-powers-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-fetch-absolute-powers-trace-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute powers trace for the adjacent channel power (ACP) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If y

### RFmxEVDO ACP Fetch Absolute Powers Trace VI

Fetches the absolute powers trace for the adjacent channel power (ACP) measurement.

[IMAGE alt='icon' src='rfmxevdo-acp-fetch-absolute-powers-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Powers (dBm) — Absolute Powers returns the trace of measured integrated power. This value is expressed in dBm. x0 — x0 is the start parameter. dx — dx is the delta parameter. y — y returns the real signal values stored in an array. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 is the start parameter. dx — dx is the delta parameter. y — y returns the real signal values stored in an array. |

Parent topic:

RFmxEVDO ACP Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-fetch-spectrum-vi.html language=enus -->
## TOPIC 00038: RFmxEVDO ACP Fetch Spectrum VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-acp-fetch-spectrum-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the adjacent channel power (ACP) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do no

### RFmxEVDO ACP Fetch Spectrum VI

Fetches the spectrum used for the adjacent channel power (ACP) measurement.

[IMAGE alt='icon' src='rfmxevdo-acp-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |

Parent topic:

RFmxEVDO ACP Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-analyze-iq-1-wfm-vi.html language=enus -->
## TOPIC 00039: RFmxEVDO Analyze (IQ, 1 Wfm) VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-analyze-iq-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-analyze-iq-1-wfm-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended

### RFmxEVDO Analyze (IQ, 1 Wfm) VI

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **IQ** or **IQ or Spectral**.

Note

RFmxInstr Property Node

RFmx EVDO Commit

[IMAGE alt='icon' src='rfmxevdo-analyze-iq-1-wfm-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance. Example: "" "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". IQ — IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 — x0 specifies the start time of the input Y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String input parameter for Fetch VIs when using named signal configurations or named results. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start time of the input Y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

RFmxEVDO Analyze2 VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-analyze-spectrum-1-wfm-vi.html language=enus -->
## TOPIC 00040: RFmxEVDO Analyze (Spectrum, 1 Wfm) VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-analyze-spectrum-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-analyze-spectrum-1-wfm-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum waveform that you specify in the Spectrum parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Reco

### RFmxEVDO Analyze (Spectrum, 1 Wfm) VI

Performs the enabled measurements on the spectrum waveform that you specify in the **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **Spectral** or **IQ or Spectral**.

Note

RFmxInstr Property Node

RFmx EVDO Commit

[IMAGE alt='icon' src='rfmxevdo-analyze-spectrum-1-wfm-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance. Example: "" "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". Spectrum — Spectrum specifies the data for a spectrum waveform including the start, delta, and actual values. x0 — x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx — dx specifies the frequency interval between data points in the spectrum. y — y contains the real-value power spectrum. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String input parameter for Fetch VIs when using named signal configurations or named results. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx — dx specifies the frequency interval between data points in the spectrum. y — y contains the real-value power spectrum. |

Parent topic:

RFmxEVDO Analyze2 VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-auto-level-vi.html language=enus -->
## TOPIC 00041: RFmxEVDO Auto Level VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-auto-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-auto-level-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level. The RFmxEVDO Auto Level VI completes the following tasks: Resets the mixer level, mixer level offset, an

### RFmxEVDO Auto Level VI

Examines the input signal to calculate the peak power level and sets it as the value of the [Reference Level](/csh?context=rfmxevdo_rfmxevdoprop_attr800002) property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxEVDO Auto Level VI completes the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device, based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the [Auto Level Initial Ref Level](/csh?context=rfmxevdo_rfmxevdoprop_attr80d000) property.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxEVDO Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='icon' src='rfmxevdo-auto-level-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Interval (s) — Measurement Interval specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the RF signal analyzer. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Reference Level — Reference Level returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-build-carrier-string-vi.html language=enus -->
## TOPIC 00042: RFmxEVDO Build Carrier String VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-build-carrier-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-build-carrier-string-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the carrier string to use as the selector string with the adjacent channel power (ACP), channel power (CHP), and spectral emission mask (SEM) carrier configuration or fetch properties and VIs. Refer to the Selector String topic for information about the string syntax for named signals. icon

### RFmxEVDO Build Carrier String VI

Creates the carrier string to use as the selector string with the adjacent channel power (ACP), channel power (CHP), and spectral emission mask (SEM) carrier configuration or fetch properties and VIs.

Refer to the [Selector String](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

[IMAGE alt='icon' src='rfmxevdo-build-carrier-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Carrier Number — Carrier Number specifies the carrier number for building the selector string. Selector String Out — Selector String Out returns the selector string you can use in the Selector String input parameter for Configuration VIs, Fetch VIs, or the RFmxEVDO Initiate VI. |
| --- |

Parent topic:

Configuration

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-build-channel-string-vi.html language=enus -->
## TOPIC 00043: RFmxEVDO Build Channel String VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-build-channel-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-build-channel-string-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the channel string to use as the selector string with the modulation accuracy (ModAcc) channel configuration or fetch properties and VIs. Refer to the Selector String topic for information about the string syntax for named signals. icon Inputs/Outputs cstr.png Selector String Selector String

### RFmxEVDO Build Channel String VI

Creates the channel string to use as the selector string with the modulation accuracy (ModAcc) channel configuration or fetch properties and VIs.

Refer to the [Selector String](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

[IMAGE alt='icon' src='rfmxevdo-build-channel-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Channel Number — Channel Number specifies the channel number for building the selector string. Selector String Out — Selector String Out returns the selector string you can use in the Selector String input parameter for Configuration VIs, Fetch VIs, or the RFmxEVDO Initiate VI. |
| --- |

Parent topic:

Configuration

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-build-offset-string-vi.html language=enus -->
## TOPIC 00044: RFmxEVDO Build Offset String VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-build-offset-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-build-offset-string-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the offset string to use as the selector string with adjacent channel power (ACP) and spectral emission mask (SEM) offset configuration or fetch properties and VIs. Refer to the Selector String topic for information about the string syntax for named signals. icon Inputs/Outputs cstr.png Sele

### RFmxEVDO Build Offset String VI

Creates the offset string to use as the selector string with adjacent channel power (ACP) and spectral emission mask (SEM) offset configuration or fetch properties and VIs.

Refer to the [Selector String](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

[IMAGE alt='icon' src='rfmxevdo-build-offset-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Offset Number — Offset Number specifies the offset number for building the selector string. Selector String Out — Selector String Out returns the selector string you can use in the Selector String input parameter for Configuration VIs, Fetch VIs, or the RFmxEVDO Initiate VI. |
| --- |

Parent topic:

ACP

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-build-signal-string-vi.html language=enus -->
## TOPIC 00045: RFmxEVDO Build Signal String VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-build-signal-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-build-signal-string-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string for use with configuration or fetch properties and VIs. Refer to the Selector String topic for information about the string syntax for named signals. icon Inputs/Outputs cstr.png Result Name Result Name specifies the name of the result when performing overlapped measurement

### RFmxEVDO Build Signal String VI

Creates a selector string for use with configuration or fetch properties and VIs.

Refer to the [Selector String](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

[IMAGE alt='icon' src='rfmxevdo-build-signal-string-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name of the result when performing overlapped measurements. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string). Examples: "" "result::r1" "r1" Signal Name — Signal Name specifies the name of the signal when using named signal configurations. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Examples: "" "signal::sig1" "sig1" Selector String — Selector String returns the selector string you can use in the Selector String input parameter for Configuration VIs, Fetch VIs, or other VIs that build selector strings. This string contains the signal and/or result names with their appropriate prefixes. Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" |
| --- |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-configure-power-unit-vi.html language=enus -->
## TOPIC 00046: RFmxEVDO CDA Configure Power Unit VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-configure-power-unit-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-configure-power-unit-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power unit for the code domain power results, except total power. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is ""

### RFmxEVDO CDA Configure Power Unit VI

Configures the power unit for the code domain power results, except total power.

[IMAGE alt='icon' src='rfmxevdo-cda-configure-power-unit-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Power Unit — Power Unit specifies the measurement unit of the code domain power results. The default value is dB. dB (0) Specifies that the measurement unit is dB. dBm (1) Specifies that the measurement unit is dBm. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| dB (0) | Specifies that the measurement unit is dB. |
| dBm (1) | Specifies that the measurement unit is dBm. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-configure-synchronization-mode-and-interval-vi.html language=enus -->
## TOPIC 00047: RFmxEVDO CDA Configure Synchronization Mode and Interval VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-configure-synchronization-mode-and-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-configure-synchronization-mode-and-interval-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is ""

### RFmxEVDO CDA Configure Synchronization Mode and Interval VI

Configures the synchronization mode, measurement offset, and measurement length.

[IMAGE alt='icon' src='rfmxevdo-cda-configure-synchronization-mode-and-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Synchronization Mode — Synchronization Mode specifies whether the measurement is performed from the frame, slot, or symbol boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots specified by the CDA Meas Length property starting at CDA Meas Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots specified by CDA Meas Length number of slots, starting at CDA Meas Offset slots from the slot boundary. Arbitrary (2) The symbol boundary is detected and the measurement is performed over the number of slots specified by the CDA Meas Length property, starting at CDA Meas Offset slots from the symbol boundary. Measurement Offset (slots) — Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. Valid values are [0,15]. The sum of CDA Meas Offset and CDA Meas Length is less than or equal to 16. Measurement Length (slots) — Measurement Length specifies the duration of the CDA measurement. This value is expressed in slots. The default value is 1. Valid values are [1, 16]. The sum of the CDA Meas Offset and CDA Meas Length is less than or equal to 16. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the CDA Meas Length property starting at CDA Meas Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots specified by CDA Meas Length number of slots, starting at CDA Meas Offset slots from the slot boundary. |
| Arbitrary (2) | The symbol boundary is detected and the measurement is performed over the number of slots specified by the CDA Meas Length property, starting at CDA Meas Offset slots from the symbol boundary. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-configure-uplink-measurement-channel-vi.html language=enus -->
## TOPIC 00048: RFmxEVDO CDA Configure Uplink Measurement Channel VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-configure-uplink-measurement-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-configure-uplink-measurement-channel-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is us

### RFmxEVDO CDA Configure Uplink Measurement Channel VI

Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

[IMAGE alt='icon' src='rfmxevdo-cda-configure-uplink-measurement-channel-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Walsh Code Length — Walsh Code Length specifies the Walsh code length of the channel, subject to channel-specific analysis. The default value is 16. Valid values are 2, 4, 8, 16, and 32. Walsh Code Number — Walsh Code Number specifies the Walsh code number of the channel, subject to channel-specific analysis. The default value is 0. The maximum value is 31. Branch — Branch specifies the Walsh branch of the channel, subject to channel-specific analysis. The default value is I. I (0) Specifies the in-phase branch. Q (1) Specifies the quadrature branch. I and Q (2) Specifies the in-phase and quadrature branch. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| I (0) | Specifies the in-phase branch. |
| Q (1) | Specifies the quadrature branch. |
| I and Q (2) | Specifies the in-phase and quadrature branch. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-iq-impairments-vi.html language=enus -->
## TOPIC 00049: RFmxEVDO CDA Fetch IQ Impairments VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-iq-impairments-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-iq-impairments-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measured I/Q impairments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default

### RFmxEVDO CDA Fetch IQ Impairments VI

Fetches the measured I/Q impairments.

[IMAGE alt='icon' src='rfmxevdo-cda-fetch-iq-impairments-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. I/Q Origin Offset (dB) — I/Q Origin Offset returns the I/Q origin offset. This value is expressed in dB. I/Q Gain Imbalance (dB) — I/Q Gain Imbalance returns the I/Q gain imbalance. This value is expressed in dB. I/Q Quadrature Error (deg) — I/Q Quadrature Error returns the I/Q quadrature error. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO CDA Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-code-domain-i-and-q-power-trace-vi.html language=enus -->
## TOPIC 00050: RFmxEVDO CDA Fetch Uplink Code Domain I and Q Power Trace VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-code-domain-i-and-q-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-code-domain-i-and-q-power-trace-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I and Q code power traces measured in the code domain of the base spreading factor. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance i

### RFmxEVDO CDA Fetch Uplink Code Domain I and Q Power Trace VI

Fetches the I and Q code power traces measured in the code domain of the base spreading factor.

[IMAGE alt='icon' src='rfmxevdo-cda-fetch-uplink-code-domain-i-and-q-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. I Code Domain Powers (dB or dBm) — I Code Domain Powers returns the I code domain power traces. This value is expressed in dB or dBm. Q Code Domain Powers (dB or dBm) — Q Code Domain Powers returns the Q code domain power traces. This value is expressed in dB or dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO CDA Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-code-domain-i-and-q-power-vi.html language=enus -->
## TOPIC 00051: RFmxEVDO CDA Fetch Uplink Code Domain I and Q Power VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-code-domain-i-and-q-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-code-domain-i-and-q-power-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I and Q mean active powers and the I and Q peak inactive powers. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do n

### RFmxEVDO CDA Fetch Uplink Code Domain I and Q Power VI

Fetches the I and Q mean active powers and the I and Q peak inactive powers.

[IMAGE alt='icon' src='rfmxevdo-cda-fetch-uplink-code-domain-i-and-q-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Q Peak Inactive Power (dB or dBm) — Q Peak Inactive Power returns the largest measured code power among the set of inactive channels on the Q-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. I Mean Active Power (dB or dBm) — I Mean Active Power returns the average power of all active code channels measured on the I-branch. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. Q Mean Active Power (dB or dBm) — Q Mean Active Power returns the average power of all active code channels measured on the Q-branch. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. I Peak Inactive Power (dB or dBm) — I Peak Inactive Power returns the largest measured code power among the set of inactive channels on the I-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO CDA Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-code-domain-power-vi.html language=enus -->
## TOPIC 00052: RFmxEVDO CDA Fetch Uplink Code Domain Power VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-code-domain-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-code-domain-power-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the scalar code domain power results. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the

### RFmxEVDO CDA Fetch Uplink Code Domain Power VI

Fetches the scalar code domain power results.

[IMAGE alt='icon' src='rfmxevdo-cda-fetch-uplink-code-domain-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Inactive Power (dB or dBm) — Mean Inactive Power returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. The default value is 0. Peak Active Power (dB or dBm) — Peak Active Power returns the maximum power among all active code channels. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Total Power (dBm) — Total Power returns the mean power of the received signal. This value is expressed in dBm. Total Active Power (dB or dBm) — Total Active Power returns the sum of the powers of all active code channels. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. Mean Active Power (dB or dBm) — Mean Active Power returns the average power of all active code channels. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. error out — error out contains error information. This output provides standard error out functionality. Peak Inactive Power (dB or dBm) — Peak Inactive Power returns the largest measured code power among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. |
| --- |

Parent topic:

RFmxEVDO CDA Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-constellation-trace-vi.html language=enus -->
## TOPIC 00053: RFmxEVDO CDA Fetch Uplink Symbol Constellation Trace VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-constellation-trace-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the symbol constellation trace of the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do

### RFmxEVDO CDA Fetch Uplink Symbol Constellation Trace VI

Fetches the symbol constellation trace of the configured measurement channel.

[IMAGE alt='icon' src='rfmxevdo-cda-fetch-uplink-symbol-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Symbol Constellation — Symbol Constellation returns the complex signal values stored in an array. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO CDA Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-evm-trace-vi.html language=enus -->
## TOPIC 00054: RFmxEVDO CDA Fetch Uplink Symbol EVM Trace VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-evm-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-evm-trace-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol EVM trace of the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specif

### RFmxEVDO CDA Fetch Uplink Symbol EVM Trace VI

Returns the symbol EVM trace of the configured measurement channel.

[IMAGE alt='icon' src='rfmxevdo-cda-fetch-uplink-symbol-evm-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Symbol EVM (%) — Symbol EVM Symbol EVM returns the trace of symbol EVM. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO CDA Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-evm-vi.html language=enus -->
## TOPIC 00055: RFmxEVDO CDA Fetch Uplink Symbol EVM VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-evm-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the modulation accuracy related measures for the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used.

### RFmxEVDO CDA Fetch Uplink Symbol EVM VI

Fetches the modulation accuracy related measures for the configured measurement channel.

[IMAGE alt='icon' src='rfmxevdo-cda-fetch-uplink-symbol-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Symbol Power (dB or dBm) — Mean Symbol Power returns the mean symbol power of the configured measurement channel. This value is expressed in dB or dBm. RMS Symbol Phase Error (deg) — RMS Symbol Phase Error returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. RMS Symbol EVM (%) — RMS Symbol EVM returns the RMS ymbol EVM of the configured measurement channel. This value is expressed as a percentage. Peak Symbol EVM (%) — Peak Symbol EVM returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. RMS Symbol Magnitude Error (%) — RMS Symbol Magnitude Error returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. Frequency Error (Hz) — Frequency Error returns the frequency error. This value is expressed in Hz. Chip Rate Error (ppm) — Chip Rate Error returns the chip rate error. This value is expressed in ppm. |
| --- |

Parent topic:

RFmxEVDO CDA Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-magnitude-error-trace-vi.html language=enus -->
## TOPIC 00056: RFmxEVDO CDA Fetch Uplink Symbol Magnitude Error Trace VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-magnitude-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-magnitude-error-trace-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol magnitude error trace of the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you d

### RFmxEVDO CDA Fetch Uplink Symbol Magnitude Error Trace VI

Returns the symbol magnitude error trace of the configured measurement channel.

[IMAGE alt='icon' src='rfmxevdo-cda-fetch-uplink-symbol-magnitude-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Symbol Magnitude Error (%) — Symbol Magnitude Error returns the trace of symbol magnitude error.. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO CDA Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-phase-error-trace-vi.html language=enus -->
## TOPIC 00057: RFmxEVDO CDA Fetch Uplink Symbol Phase Error Trace VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-phase-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-phase-error-trace-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the symbol phase error trace of the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do no

### RFmxEVDO CDA Fetch Uplink Symbol Phase Error Trace VI

Fetches the symbol phase error trace of the configured measurement channel.

[IMAGE alt='icon' src='rfmxevdo-cda-fetch-uplink-symbol-phase-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Symbol Phase Error (deg) — Symbol Phase Error returns the array of RMS symbol phase errors of the configured measurement channel. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO CDA Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-power-trace-vi.html language=enus -->
## TOPIC 00058: RFmxEVDO CDA Fetch Uplink Symbol Power Trace VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-power-trace-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol power trace of the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not spec

### RFmxEVDO CDA Fetch Uplink Symbol Power Trace VI

Returns the symbol power trace of the configured measurement channel.

[IMAGE alt='icon' src='rfmxevdo-cda-fetch-uplink-symbol-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Symbol Powers (dBm) — Symbol Powers returns the trace of measured symbol powers. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO CDA Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-vi.html language=enus -->
## TOPIC 00059: RFmxEVDO CDA Fetch VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches CDA measurement results. icon

### RFmxEVDO CDA Fetch VI

Fetches CDA measurement results.

[IMAGE alt='icon' src='rfmxevdo-cda-fetch-vi.png']

- [RFmxEVDO CDA Fetch IQ Impairments VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-iq-impairments-vi.html) Fetches the measured I/Q impairments.
- [RFmxEVDO CDA Fetch Uplink Symbol EVM VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-evm-vi.html) Fetches the modulation accuracy related measures for the configured measurement channel.
- [RFmxEVDO CDA Fetch Uplink Code Domain Power VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-code-domain-power-vi.html) Fetches the scalar code domain power results.
- [RFmxEVDO CDA Fetch Uplink Code Domain I and Q Power VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-code-domain-i-and-q-power-vi.html) Fetches the I and Q mean active powers and the I and Q peak inactive powers.
- [RFmxEVDO CDA Fetch Uplink Symbol EVM Trace VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-evm-trace-vi.html) Returns the symbol EVM trace of the configured measurement channel.
- [RFmxEVDO CDA Fetch Uplink Symbol Magnitude Error Trace VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-magnitude-error-trace-vi.html) Returns the symbol magnitude error trace of the configured measurement channel.
- [RFmxEVDO CDA Fetch Uplink Symbol Phase Error Trace VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-phase-error-trace-vi.html) Fetches the symbol phase error trace of the configured measurement channel.
- [RFmxEVDO CDA Fetch Uplink Code Domain I and Q Power Trace VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-code-domain-i-and-q-power-trace-vi.html) Fetches the I and Q code power traces measured in the code domain of the base spreading factor.
- [RFmxEVDO CDA Fetch Uplink Symbol Power Trace VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-power-trace-vi.html) Returns the symbol power trace of the configured measurement channel.
- [RFmxEVDO CDA Fetch Uplink Symbol Constellation Trace VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-cda-fetch-uplink-symbol-constellation-trace-vi.html) Fetches the symbol constellation trace of the configured measurement channel.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-check-measurement-status-vi.html language=enus -->
## TOPIC 00060: RFmxEVDO Check Measurement Status VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-check-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-check-measurement-status-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal nam

### RFmxEVDO Check Measurement Status VI

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='icon' src='rfmxevdo-check-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. done? — done? indicates whether the measurement is complete. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-configure-averaging-vi.html language=enus -->
## TOPIC 00061: RFmxEVDO CHP Configure Averaging VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-configure-averaging-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the channel power (CHP) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Ex

### RFmxEVDO CHP Configure Averaging VI

Configures averaging for the channel power (CHP) measurement.

[IMAGE alt='icon' src='rfmxevdo-chp-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) Averaging is not enabled. True (1) Averaging is enabled. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. Refer to the Averaging section of the Spectrum topic for more information about averaging types. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Averaging is not enabled. |
| True (1) | Averaging is enabled. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-configure-rbw-filter-vi.html language=enus -->
## TOPIC 00062: RFmxEVDO CHP Configure RBW Filter VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-configure-rbw-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-configure-rbw-filter-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "

### RFmxEVDO CHP Configure RBW Filter VI

Configures the resolution bandwidth (RBW) filter.

[IMAGE alt='icon' src='rfmxevdo-chp-configure-rbw-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. RBW Auto — RBW Auto specifies whether the measurement calculates the RBW. The default value is True True (1) RFmx EV-DO automatically computes the RBW. False (0) The measurement uses the RBW you specify. Refer to the RBW and Sweep Time section in the CHP topic for more details on RBW and sweep time. RBW (Hz) — RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 30 kHz. RBW Filter Type — RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| True (1) | RFmx EV-DO automatically computes the RBW. |
| False (0) | The measurement uses the RBW you specify. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-configure-sweep-time-vi.html language=enus -->
## TOPIC 00063: RFmxEVDO CHP Configure Sweep Time VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-configure-sweep-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-configure-sweep-time-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can u

### RFmxEVDO CHP Configure Sweep Time VI

Configures the sweep time.

[IMAGE alt='icon' src='rfmxevdo-chp-configure-sweep-time-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Sweep Time Auto — Sweep Time Auto specifies whether the measurement calculates the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of 1.67 ms. Sweep Time Interval (s) — Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1.67 ms. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of 1.67 ms. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-carrier-measurement-array-vi.html language=enus -->
## TOPIC 00064: RFmxEVDO CHP Fetch Carrier Measurement (Array) VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-carrier-measurement-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-carrier-measurement-array-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of carrier measurements of the channel power (CHP) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you

### RFmxEVDO CHP Fetch Carrier Measurement (Array) VI

Returns the array of carrier measurements of the channel power (CHP) measurement.

[IMAGE alt='icon' src='rfmxevdo-chp-fetch-carrier-measurement-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Carrier Absolute Power (dBm) — Carrier Absolute Power returns the array of absolute carrier powers. This value is expressed in dBm. Carrier Relative Power (dB) — Carrier Relative Power returns the array of relative carrier powers. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO CHP Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-carrier-measurement-vi.html language=enus -->
## TOPIC 00065: RFmxEVDO CHP Fetch Carrier Measurement VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-carrier-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-carrier-measurement-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. Use "carrier<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String spec

### RFmxEVDO CHP Fetch Carrier Measurement VI

Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. Use "carrier<n>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxevdo-chp-fetch-carrier-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxEVDO Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Carrier Absolute Power (dBm) — Carrier Absolute Power returns the absolute carrier power of the selected carrier. This value is expressed in dBm. Carrier Relative Power (dB) — Carrier Relative Power returns the relative carrier power of the selected carrier. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO CHP Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-spectrum-vi.html language=enus -->
## TOPIC 00066: RFmxEVDO CHP Fetch Spectrum VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-spectrum-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the channel power (CHP) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify

### RFmxEVDO CHP Fetch Spectrum VI

Fetches the spectrum used for the channel power (CHP) measurement.

[IMAGE alt='icon' src='rfmxevdo-chp-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |

Parent topic:

RFmxEVDO CHP Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-total-carrier-power-vi.html language=enus -->
## TOPIC 00067: RFmxEVDO CHP Fetch Total Carrier Power VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-total-carrier-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-total-carrier-power-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the total carrier power measured by the channel power (CHP) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you

### RFmxEVDO CHP Fetch Total Carrier Power VI

Fetches the total carrier power measured by the channel power (CHP) measurement.

[IMAGE alt='icon' src='rfmxevdo-chp-fetch-total-carrier-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Total Carrier Power (dBm) — Total Carrier Power returns the total carrier power. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO CHP Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-vi.html language=enus -->
## TOPIC 00068: RFmxEVDO CHP Fetch VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the channel power (CHP) measurement results. icon

### RFmxEVDO CHP Fetch VI

Fetches the channel power (CHP) measurement results.

[IMAGE alt='icon' src='rfmxevdo-chp-fetch-vi.png']

- [RFmxEVDO CHP Fetch Total Carrier Power VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-total-carrier-power-vi.html) Fetches the total carrier power measured by the channel power (CHP) measurement.
- [RFmxEVDO CHP Fetch Carrier Measurement VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-carrier-measurement-vi.html) Returns the absolute and relative powers measured in the carriers. The relative powers are measured relative to the integrated power of the power reference carrier. Use "carrier<n>" as the selector string to read results from this VI.
- [RFmxEVDO CHP Fetch Carrier Measurement (Array) VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-carrier-measurement-array-vi.html) Returns the array of carrier measurements of the channel power (CHP) measurement.
- [RFmxEVDO CHP Fetch Spectrum VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-chp-fetch-spectrum-vi.html) Fetches the spectrum used for the channel power (CHP) measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-clear-all-named-results-vi.html language=enus -->
## TOPIC 00069: RFmxEVDO Clear All Named Results VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-clear-all-named-results-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-clear-all-named-results-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value i

### RFmxEVDO Clear All Named Results VI

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxevdo-clear-all-named-results-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-clear-named-result-vi.html language=enus -->
## TOPIC 00070: RFmxEVDO Clear Named Result VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-clear-named-result-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-clear-named-result-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used.

### RFmxEVDO Clear Named Result VI

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxevdo-clear-named-result-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-clone-signal-configuration-vi.html language=enus -->
## TOPIC 00071: RFmxEVDO Clone Signal Configuration VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-clone-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-clone-signal-configuration-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the property values from an existing signal instance. icon Inputs/Outputs cstr.png Old Signal Name Old Signal Name specifies the name of the existing signal. This input accepts the signal name with or without the "signal::" prefix. Example: "signal::

### RFmxEVDO Clone Signal Configuration VI

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='icon' src='rfmxevdo-clone-signal-configuration-vi.png']

#### Inputs/Outputs

| Old Signal Name — Old Signal Name specifies the name of the existing signal. This input accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. New Signal Name — New Signal Name specifies the name of the new signal. This input accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string you can use in the Selector String input parameter for Configuration VIs, Fetch VIs, or the RFmxEVDO Initiate VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-commit-vi.html language=enus -->
## TOPIC 00072: RFmxEVDO Commit VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-commit-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-commit-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this VI is optional. RFmxEVDO commits settings to the hardware when you call the RFmxEVDO Initiate VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal na

### RFmxEVDO Commit VI

Commits settings to the hardware. Calling this VI is optional. RFmxEVDO commits settings to the hardware when you call the [RFmxEVDO Initiate](/csh?topicname=rfmxevdo-initiate-vi.html) VI.

[IMAGE alt='icon' src='rfmxevdo-commit-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-band-class-vi.html language=enus -->
## TOPIC 00073: RFmxEVDO Configure Band Class VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-band-class-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-band-class-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the band class to be used for the measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Exampl

### RFmxEVDO Configure Band Class VI

Configures the band class to be used for the measurement.

[IMAGE alt='icon' src='rfmxevdo-configure-band-class-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Band Class — Band Class specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. Valid values range between 0 and 15, inclusive. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-carrier-frequency-array-vi.html language=enus -->
## TOPIC 00074: RFmxEVDO Configure Carrier Frequency (Array) VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-carrier-frequency-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-carrier-frequency-array-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the carrier frequency of the selected carriers as an offset frequency relative to the center frequency. Configure the center frequency by using the RFmxEVDO Configure Frequency VI. Configure the number of carriers using the RFmxEVDO Configure Number of Carriers VI. icon Inputs/Outputs cst

### RFmxEVDO Configure Carrier Frequency (Array) VI

Configures the carrier frequency of the selected carriers as an offset frequency relative to the center frequency.

Configure the center frequency by using the [RFmxEVDO Configure Frequency](rfmxevdo-configure-frequency-vi.html) VI. Configure the number of carriers using the [RFmxEVDO Configure Number of Carriers](rfmxevdo-configure-number-of-carriers-vi.html) VI.

[IMAGE alt='icon' src='rfmxevdo-configure-carrier-frequency-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Carrier Frequency (Hz) — Carrier Frequency specifies the carrier frequency. This value is expressed in Hz. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Array VIs

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-carrier-frequency-vi.html language=enus -->
## TOPIC 00075: RFmxEVDO Configure Carrier Frequency VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-carrier-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-carrier-frequency-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the carrier frequency of the selected carrier as an offset frequency relative to the center frequency. Use "carrier <n> " as the selector string to configure this VI. Configure the center frequency by using the RFmxEVDO Configure Frequency VI. If the number of carriers is greater than 1,

### RFmxEVDO Configure Carrier Frequency VI

Configures the carrier frequency of the selected carrier as an offset frequency relative to the center frequency. Use "carrier
*<n>*
" as the selector string to configure this VI.

Configure the center frequency by using the [RFmxEVDO Configure Frequency](rfmxevdo-configure-frequency-vi.html) VI. If the number of carriers is greater than 1, configure the number of carriers using the [RFmxEVDO Configure Number of Carriers](rfmxevdo-configure-number-of-carriers-vi.html) VI.

[IMAGE alt='icon' src='rfmxevdo-configure-carrier-frequency-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0" (empty string). Examples: "carrier0" "signal::sig1/carrier0" You can use the RFmxEVDO Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Carrier Frequency (Hz) — Carrier Frequency specifies the carrier frequency. This value is expressed in Hz. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-channel-configuration-mode-vi.html language=enus -->
## TOPIC 00076: RFmxEVDO Configure Channel Configuration Mode VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-channel-configuration-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-channel-configuration-mode-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures RFmx EV-DO to detect the channels automatically or to use a specified channel configuration. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used.

### RFmxEVDO Configure Channel Configuration Mode VI

Configures RFmx EV-DO to detect the channels automatically or to use a specified channel configuration.

[IMAGE alt='icon' src='rfmxevdo-configure-channel-configuration-mode-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Channel Configuration Mode — The Channel Configuration Mode specifies how the channel configuration is derived. Auto Detect (0) RFmx EV-DO detects the channels automatically. User Defined (1) Channel configuration is defined manually. This mode increases measurement speed because no time is spent on channel detection. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Auto Detect (0) | RFmx EV-DO detects the channels automatically. |
| User Defined (1) | Channel configuration is defined manually. This mode increases measurement speed because no time is spent on channel detection. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-contiguous-carriers-vi.html language=enus -->
## TOPIC 00077: RFmxEVDO Configure Contiguous Carriers VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-contiguous-carriers-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-contiguous-carriers-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a number of contiguous carriers in a given band. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Exam

### RFmxEVDO Configure Contiguous Carriers VI

Configures a number of contiguous carriers in a given band.

[IMAGE alt='icon' src='rfmxevdo-configure-contiguous-carriers-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Carriers — Number of Carriers specifies the number of carriers in the signal. The default value is 1. Carrier at Center Frequency — Carrier at Center Frequency specifies the carrier at the center frequency. Band Class — Band Class specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. Valid values range between 0 and 15, inclusive. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-digital-edge-trigger-vi.html language=enus -->
## TOPIC 00078: RFmxEVDO Configure Digital Edge Trigger VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-digital-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-digital-edge-trigger-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger to mark a reference point within the record. icon Inputs/Outputs cbool.png Enable Trigger? Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. cstr.png Selector String Selector String specifies a selector string com

### RFmxEVDO Configure Digital Edge Trigger VI

Configures the device to wait for a software trigger to mark a reference point within the record.

[IMAGE alt='icon' src='rfmxevdo-configure-digital-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Digital Edge Source — Digital Edge Source specifies the source terminal for the digital edge trigger. The default of this parameter is hardware dependent. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. Digital Edge — Digital Edge specifies the trigger edge to detect. The default value is Rising Edge. Rising Edge (0) RFmx EV-DO detects a rising edge. Falling Edge (1) RFmx EV-DO detects a falling edge. Trigger Delay (s) — Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
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
| Rising Edge (0) | RFmx EV-DO detects a rising edge. |
| Falling Edge (1) | RFmx EV-DO detects a falling edge. |

Parent topic:

RFmxEVDO Configure Trigger VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-external-attenuation-vi.html language=enus -->
## TOPIC 00079: RFmxEVDO Configure External Attenuation VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-external-attenuation-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-external-attenuation-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies external attenuation to be considered by RFmx EV-DO measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do

### RFmxEVDO Configure External Attenuation VI

Specifies external attenuation to be considered by RFmx EV-DO measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector.

[IMAGE alt='icon' src='rfmxevdo-configure-external-attenuation-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. External Attenuation (dB) — External Attenuation specifies external attenuation to be considered by RFmx EV-DO measurements, such as the attenuation of a switch or cable connected to the RF signal analyzer RF IN connector. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-frequency-channel-number-vi.html language=enus -->
## TOPIC 00080: RFmxEVDO Configure Frequency (Channel Number) VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-frequency-channel-number-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-frequency-channel-number-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the

### RFmxEVDO Configure Frequency (Channel Number) VI

Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency.

[IMAGE alt='icon' src='rfmxevdo-configure-frequency-channel-number-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Link Direction — Link Direction specifies which direction the frequency is calculated. Currently, only Uplink is supported. Uplink (1) The frequency is calculated in the reverse link direction, also know as the uplink direction. Band Class — Band Class specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. Valid values range between 0 and 15, inclusive. Channel Number — Channel Number is the absolute RF channel number. The valid range for this parameter depends on the value you specify for the Band parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Uplink (1) | The frequency is calculated in the reverse link direction, also know as the uplink direction. |

Parent topic:

RFmxEVDO Configure Frequency VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-frequency-frequency-vi.html language=enus -->
## TOPIC 00081: RFmxEVDO Configure Frequency (Frequency) VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-frequency-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-frequency-frequency-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instan

### RFmxEVDO Configure Frequency (Frequency) VI

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

[IMAGE alt='icon' src='rfmxevdo-configure-frequency-frequency-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Center Frequency (Hz) — Center Frequency specifies the expected carrier frequency of the RF signal to acquire. This value is expressed in Hz. The RF signal analyzer tunes to this frequency. The default of this parameter is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO Configure Frequency VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-frequency-vi.html language=enus -->
## TOPIC 00082: RFmxEVDO Configure Frequency VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-frequency-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire according to the Center Frequency value in Hz or according to the Channel Number and Band parameters. The signal analyzer tunes to this frequency. icon

### RFmxEVDO Configure Frequency VI

Configures the expected carrier frequency of the RF signal to acquire according to the **Center Frequency** value in Hz or according to the **Channel Number** and **Band** parameters. The signal analyzer tunes to this frequency.

[IMAGE alt='icon' src='rfmxevdo-configure-frequency-vi.png']

- [RFmxEVDO Configure Frequency (Frequency) VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-frequency-frequency-vi.html) Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.
- [RFmxEVDO Configure Frequency (Channel Number) VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-frequency-channel-number-vi.html) Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-iq-power-edge-trigger-vi.html language=enus -->
## TOPIC 00083: RFmxEVDO Configure IQ Power Edge Trigger VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-iq-power-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-iq-power-edge-trigger-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. To trigger on burst signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time

### RFmxEVDO Configure IQ Power Edge Trigger VI

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

To trigger on burst signals, specify a minimum quiet time, which ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts but large enough to ignore power changes within a burst.

[IMAGE alt='icon' src='rfmxevdo-configure-iq-power-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. Trigger Delay (s) — Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. IQ Power Edge Source — IQ Power Edge Source specifies the channel from which the device monitors the trigger. The default of this parameter is hardware dependent. IQ Power Edge Slope — IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. IQ Power Edge Level (dB or dBm) — IQ Power Edge Level specifies the threshold above or below which the RF signal analyzer triggers. The value is expressed in dB if IQ Power Edge Level Type is set to Relative; and is expressed in dBm if IQ Power Edge Level Type is set to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this parameter is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Minimum Quiet Time Mode — Minimum Quiet Time Mode specifies whether the measurement calculates the minimum quiet time used for triggering. The default value is Auto. Manual (0) The measurement uses the minimum quiet time value you specify. Auto (1) The measurement calculates the minimum quiet time used for triggering. Minimum Quiet Time (s) — Minimum Quiet Time specifies the duration for which the signal must be quiet before the RF signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet when it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default of this parameter is hardware dependent. IQ Power Edge Level Type — IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. The IQ Power Edge Level Type parameter is used only when you set the Trigger Type property to IQ Power Edge. Relative (0) The IQ Power Edge Level is relative to the reference level. Absolute (1) The IQ Power Edge Level specifies the absolute power. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
| Manual (0) | The measurement uses the minimum quiet time value you specify. |
| Auto (1) | The measurement calculates the minimum quiet time used for triggering. |
| Relative (0) | The IQ Power Edge Level is relative to the reference level. |
| Absolute (1) | The IQ Power Edge Level specifies the absolute power. |

Parent topic:

RFmxEVDO Configure Trigger VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-number-of-carriers-vi.html language=enus -->
## TOPIC 00084: RFmxEVDO Configure Number of Carriers VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-number-of-carriers-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-number-of-carriers-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of carriers for the analysis of the EV-DO signal. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty s

### RFmxEVDO Configure Number of Carriers VI

Configures the number of carriers for the analysis of the EV-DO signal.

[IMAGE alt='icon' src='rfmxevdo-configure-number-of-carriers-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Carriers — Number of Carriers specifies the number of carriers in the signal. The default value is 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-physical-layer-subtype-vi.html language=enus -->
## TOPIC 00085: RFmxEVDO Configure Physical Layer Subtype VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-physical-layer-subtype-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-configure-physical-layer-subtype-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the subtype of the EV-DO signal. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal

### RFmxEVDO Configure Physical Layer Subtype VI

Configures the subtype of the EV-DO signal.

[IMAGE alt='icon' src='rfmxevdo-configure-physical-layer-subtype-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Physical Layer Subtype — Physical Layer Subtype specifies the EV-DO physical layer subtype. The default value is 0, 1. 0,1(0) Specifies subtype 0, 1. 3GPP2 C.S0024-B v3.0 defines this subtype in 10 DEFAULT (SUBTYPE 0) AND SUBTYPE 1 PHYSICAL LAYER PROTOCOL. 2(1) Specifies subtype 2. 3GPP2 C.S0024-B v3.0 defines this subtype in 11 SUBTYPE 2 PHYSICAL LAYER. 3(2) Specifies subtype 3. 3GPP2 C.S0024-B v3.0 defines this subtype in 12 SUBTYPE 3 PHYSICAL LAYER. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0,1(0) | Specifies subtype 0, 1. 3GPP2 C.S0024-B v3.0 defines this subtype in 10 DEFAULT (SUBTYPE 0) AND SUBTYPE 1 PHYSICAL LAYER PROTOCOL. |
| 2(1) | Specifies subtype 2. 3GPP2 C.S0024-B v3.0 defines this subtype in 11 SUBTYPE 2 PHYSICAL LAYER. |
| 3(2) | Specifies subtype 3. 3GPP2 C.S0024-B v3.0 defines this subtype in 12 SUBTYPE 3 PHYSICAL LAYER. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-obw-fetch-vi.html language=enus -->
## TOPIC 00086: RFmxEVDO OBW Fetch VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-obw-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-obw-fetch-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches occupied bandwidth (OBW) measurement results. icon

### RFmxEVDO OBW Fetch VI

Fetches occupied bandwidth (OBW) measurement results.

[IMAGE alt='icon' src='rfmxevdo-obw-fetch-vi.png']

- [RFmxEVDO OBW Fetch Measurement VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-obw-fetch-measurement-vi.html) Returns the occupied bandwidth (OBW) measurement.
- [RFmxEVDO OBW Fetch Spectrum VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-obw-fetch-spectrum-vi.html) Fetches the spectrum trace used for the OBW measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-select-measurement-vi.html language=enus -->
## TOPIC 00087: RFmxEVDO Select Measurement VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-select-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-select-measurement-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurements that you want to enable. To select a single measurement, use the Measurement instance. To select multiple measurements, use the Multiple Measurements instance. icon

### RFmxEVDO Select Measurement VI

Specifies the measurements that you want to enable. To select a single measurement, use the **Measurement** instance. To select multiple measurements, use the **Multiple Measurements** instance.

[IMAGE alt='icon' src='rfmxevdo-select-measurement-vi.png']

- [RFmxEVDO Select Measurement (Single) VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-select-measurement-single-vi.html) Enables the measurement that you specify in the Measurement parameter and disables all other measurements.
- [RFmxEVDO Select Measurement (Multiple) VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-select-measurement-multiple-vi.html) Enables all the measurements that you specify in the Measurements parameter and disables all other measurements.

Parent topic:

EVDO

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-lower-offset-power-array-vi.html language=enus -->
## TOPIC 00088: RFmxEVDO SEM Fetch Lower Offset Power (Array) VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-lower-offset-power-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-lower-offset-power-array-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of lower offset segment power measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the

### RFmxEVDO SEM Fetch Lower Offset Power (Array) VI

Returns the arrays of lower offset segment power measurements.

[IMAGE alt='icon' src='rfmxevdo-sem-fetch-lower-offset-power-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Relative Peak Power (dB) — Relative Peak Power returns the array of peak powers in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Peak Frequency (Hz) — Peak Frequency returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns the array of lower (negative) offset segment powers measured. This value is expressed in dBm. Relative Integrated Power (dB) — Relative Integrated Power returns the array of powers in each lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Absolute Peak Power (dBm) — Absolute Peak Power returns the array of peak powers measured in each lower (negative) offset segment. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO SEM Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-vi.html language=enus -->
## TOPIC 00089: RFmxEVDO SEM Fetch VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectral emission mask (SEM) measurement results. icon

### RFmxEVDO SEM Fetch VI

Fetches the spectral emission mask (SEM) measurement results.

[IMAGE alt='icon' src='rfmxevdo-sem-fetch-vi.png']

- [RFmxEVDO SEM Fetch Measurement Status VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-measurement-status-vi.html) Fetches the SEM measurement status.
- [RFmxEVDO SEM Fetch Total Carrier Power VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-total-carrier-power-vi.html) Returns the total carrier power of the selected carrier.
- [RFmxEVDO SEM Fetch Carrier Measurement VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-carrier-measurement-vi.html) Returns the carrier measurements for the carrier selected by the selector string. Use "carrier<n>" as the selector string to read parameters from this VI.
- [RFmxEVDO SEM Fetch Carrier Measurement (Array) VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-carrier-measurement-array-vi.html) Returns the array of carrier measurements.
- [RFmxEVDO SEM Fetch Lower Offset Power VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-lower-offset-power-vi.html) Returns the lower offset segment power measurements. Use "offset<n>" as the selector string to read parameters from this VI.
- [RFmxEVDO SEM Fetch Lower Offset Power (Array) VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-lower-offset-power-array-vi.html) Returns the arrays of lower offset segment power measurements.
- [RFmxEVDO SEM Fetch Upper Offset Power VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-upper-offset-power-vi.html) Returns the upper offset segment power measurements. Use "offset<n>" as the selector string to read parameters from this VI.
- [RFmxEVDO SEM Fetch Upper Offset Power (Array) VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-upper-offset-power-array-vi.html) Returns the arrays of upper offset segment power measurements.
- [RFmxEVDO SEM Fetch Lower Offset Margin VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-lower-offset-margin-vi.html) Returns the measurement status and margin from the limit line measured in the lower offset segment. Use "offset<n>" as the selector string to read parameters from this VI.
- [RFmxEVDO SEM Fetch Lower Offset Margin (Array) VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-lower-offset-margin-array-vi.html) Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments.
- [RFmxEVDO SEM Fetch Upper Offset Margin VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-upper-offset-margin-vi.html) Returns the measurement status and margin from the limit line measured in the upper offset segment. Use "offset<n>" as the selector string to read parameters from this VI.
- [RFmxEVDO SEM Fetch Upper Offset Margin (Array) VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-upper-offset-margin-array-vi.html) Returns the measurement status and margin from the limit line measured in the upper offset segments.
- [RFmxEVDO SEM Fetch Spectrum VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-sem-fetch-spectrum-vi.html) Fetches the spectrum used for the spectral emission mask (SEM) measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-send-software-edge-trigger-vi.html language=enus -->
## TOPIC 00090: RFmxEVDO Send Software Edge Trigger VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-send-software-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-send-software-edge-trigger-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxEVDO Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. This VI returns an error in the following situations: You configure an

### RFmxEVDO Send Software Edge Trigger VI

Sends a trigger to the device when you use the [RFmxEVDO Configure Trigger](/csh?topicname=rfmxevdo-configure-trigger-vi.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxEVDO Initiate VI.

[IMAGE alt='icon' src='rfmxevdo-send-software-edge-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-slotphase-fetch-maximum-half-slot-phase-discontinuity-vi.html language=enus -->
## TOPIC 00091: RFmxEVDO SlotPhase Fetch Maximum Half Slot Phase Discontinuity VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-slotphase-fetch-maximum-half-slot-phase-discontinuity-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-slotphase-fetch-maximum-half-slot-phase-discontinuity-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum phase discontinuity observed at half-slot boundaries in the measurement interval. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal inst

### RFmxEVDO SlotPhase Fetch Maximum Half Slot Phase Discontinuity VI

Fetches the maximum phase discontinuity observed at half-slot boundaries in the measurement interval.

[IMAGE alt='icon' src='rfmxevdo-slotphase-fetch-maximum-half-slot-phase-discontinuity-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Maximum Half Slot Phase Discontinuity (deg) — Maximum Half Slot Phase Discontinuity returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxEVDO SlotPhase Fetch VI

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-slotpower-configure-synchronization-mode-and-interval-vi.html language=enus -->
## TOPIC 00092: RFmxEVDO SlotPower Configure Synchronization Mode and Interval VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-slotpower-configure-synchronization-mode-and-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-slotpower-configure-synchronization-mode-and-interval-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is ""

### RFmxEVDO SlotPower Configure Synchronization Mode and Interval VI

Configures the synchronization mode, measurement offset, and measurement length.

[IMAGE alt='icon' src='rfmxevdo-slotpower-configure-synchronization-mode-and-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Synchronization Mode — Synchronization Mode specifies whether the measurement is performed from the frame or the slot boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots specified by the SlotPower Meas Length property starting at SlotPower Meas Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots specified by SlotPower Measurement Length number of slots, starting at SlotPower Measurement Offset slots from the slot boundary. Measurement Offset (slots) — Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPower Sync Mode property. The default value is 0. Measurement Length (slots) — Measurement Length specifies the duration of the SlotPower measurement. This value is expressed in slots. The default value is 16. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SlotPower Meas Length property starting at SlotPower Meas Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots specified by SlotPower Measurement Length number of slots, starting at SlotPower Measurement Offset slots from the slot boundary. |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-slotpower-fetch-vi.html language=enus -->
## TOPIC 00093: RFmxEVDO SlotPower Fetch VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-slotpower-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-slotpower-fetch-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches SlotPower measurement results. icon

### RFmxEVDO SlotPower Fetch VI

Fetches SlotPower measurement results.

[IMAGE alt='icon' src='rfmxevdo-slotpower-fetch-vi.png']

- [RFmxEVDO SlotPower Fetch Powers VI](../../../../../vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-slotpower-fetch-powers-vi.html) Fetches the slot power and slot power delta for all half-slots in the measurement length. The slot power delta is the difference in power between adjacent half-slots.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-wait-for-measurement-complete-vi.html language=enus -->
## TOPIC 00094: RFmxEVDO Wait for Measurement Complete VI

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-wait-for-measurement-complete-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/rfmxevdo-wait-for-measurement-complete-vi.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you

### RFmxEVDO Wait for Measurement Complete VI

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='icon' src='rfmxevdo-wait-for-measurement-complete-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxEVDO Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxevdo-labview-api-ref path=vi-lib/rfmx/evdo/mx/rfmxevdo-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00095: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxevdo-labview-api-ref`
- source_path: `vi-lib/rfmx/evdo/mx/rfmxevdo-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxevdo-labview-api-ref/raw/resource/enus/vi-lib/rfmx/evdo/mx/rfmxevdo-llb/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxevdo-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error

### Using the Standard Functionality for error in Parameters

Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error in behavior is as follows

Note

error in

error in

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |
