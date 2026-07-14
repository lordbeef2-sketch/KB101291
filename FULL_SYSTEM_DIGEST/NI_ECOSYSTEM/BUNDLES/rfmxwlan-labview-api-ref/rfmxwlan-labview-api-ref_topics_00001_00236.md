# NI DOCUMENT BUNDLE: rfmxwlan-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxwlan-labview-api-ref start=1 end=236 -->
<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan-p.html language=enus -->
## TOPIC 00001: RFmxWLAN Properties

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan-p.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan-p.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RFmxWLAN properties to access options for configuring and fetching measurements. © 2019–2026 National Instruments Corporation. All rights reserved.

### RFmxWLAN Properties

Use the RFmxWLAN properties to access options for configuring and fetching measurements.

© 2019–2026 National Instruments Corporation. All rights reserved.

- [Advanced: Sample Clock Rate Factor](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00036.html) Specifies the factor by which the sample clock rate is multiplied at the transmitter to generate a signal compressed in the frequency domain and expanded in the time domain.
- [Advanced:Auto Level Initial Reference Level (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00024.html) Specifies the initial reference level which the RFmxWLAN Auto Level VI uses to estimate the peak power of the input signal. This value is expressed in dBm.
- [Advanced:Limited Configuration Change](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00025.html) Specifies the set of properties that are considered by RFmx in the locked signal configuration state.
- [Auto Detect Signal:Detected Burst Length (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00013.html) Returns the duration of the packet detected by the RFmxWLAN Auto Detect Signal VI. The value is expressed in seconds.
- [Auto Detect Signal:Detected Channel Bandwidth (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00012.html) Returns the channel bandwidth detected by the RFmxWLAN Auto Detect Signal . The value is expressed in Hz.
- [Auto Detect Signal:Detected Standard](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00011.html) Returns the standard detected by the RFmxWLAN Auto Detect Signal VI.
- [Center Frequency (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00001.html) Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency.
- [DSSSModAcc:Acquisition Length (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300c.html) Specifies the length of the waveform to be acquired for the DSSSModAcc measurement when you set the DSSSModAcc Acquisition Length Mode property to Manual . This value is expressed in seconds.
- [DSSSModAcc:Acquisition Length Mode](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300b.html) Specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties.
- [DSSSModAcc:All Traces Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03031.html) Specifies whether to enable all the traces computed by DSSSModAcc measurement.
- [DSSSModAcc:Averaging:Count](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03030.html) Specifies the number of acquisitions used for averaging when you set the DSSSModAcc Averaging Enabled property to True .
- [DSSSModAcc:Averaging:Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0302f.html) Specifies whether to enable averaging for DSSSModAcc measurement.
- [DSSSModAcc:Burst Start Detection Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0307a.html) Specifies whether the measurement detects the rising edge of a burst in the acquired waveform.
- [DSSSModAcc:Chip Clock Error Correction Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0302d.html) Specifies whether to enable chip clock error correction.
- [DSSSModAcc:Data Decoding Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0307c.html) Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC).
- [DSSSModAcc:EVM Unit](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03012.html) Specifies the unit for the EVM results.
- [DSSSModAcc:Equalization Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03011.html) Specifies whether to enable equalization. The IEEE Standard 802.11-2016 does not allow equalization for computing EVM. If you enable equalization, the measurement does not support I/Q impairment estimation.
- [DSSSModAcc:Frequency Error Correction Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0302c.html) Specifies whether to enable frequency error correction.
- [DSSSModAcc:I/Q Origin Offset Correction Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0302e.html) Specifies whether to enable I/Q origin offset correction.
- [DSSSModAcc:Maximum Measurement Length (chips)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300e.html) Specifies the maximum number of data chips that the measurement uses to compute EVM. This value is expressed in chips.
- [DSSSModAcc:Measurement Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300a.html) Specifies whether to enable the DSSSModAcc measurement, which is a measurement of the modulation accuracy on signals conforming to the DSSS PHY defined in section 15 and the High Rate DSSS PHY defined in section 16 of IEEE Standard 802.11-2016 .
- [DSSSModAcc:Measurement Offset (chips)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300d.html) Specifies the number of data chips to be ignored from the start of the data field for the EVM computation. This value is expressed in chips.
- [DSSSModAcc:Number of Analysis Threads](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03071.html) Specifies the maximum number of threads used for parallelism for DSSSModAcc measurement.
- [DSSSModAcc:Power:Custom Gate Start Time (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03015.html) Specifies the start time of the custom power gate. This value is expressed in seconds.
- [DSSSModAcc:Power:Custom Gate Stop Time (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03016.html) Specifies the stop time for the custom power gate. This value is expressed in seconds.
- [DSSSModAcc:Power:Measurement Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03013.html) Specifies whether power measurement is performed. This measurement computes power of various fields in the PPDU.
- [DSSSModAcc:Power:Number of Custom Gates](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03014.html) Specifies the number of custom gates used for power measurement.
- [DSSSModAcc:Pulse Shaping Filter Parameter](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03010.html) Specifies the value of the filter roll-off when you set the Pulse Shaping Filter Type property to Raised Cosine or Root Raised Cosine . This property is ignored if you set the Pulse Shaping Filter Type property to Rectangular .
- [DSSSModAcc:Pulse Shaping Filter Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300f.html) Specifies the type of pulse shaping filter used at the transmitter. This property is ignored when you set the DSSSModAcc Equalization Enabled property to True .
- [DSSSModAcc:Results:Chip Clock Error Mean (ppm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03052.html) Returns the chip clock error of the transmitter. This value is expressed in parts per million (ppm).
- [DSSSModAcc:Results:Frequency Error Mean (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0304e.html) Returns the carrier frequency error of the transmitter. This value is expressed in Hz.
- [DSSSModAcc:Results:I/Q Gain Imbalance Mean (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03053.html) Returns the I/Q gain imbalance. This value is expressed in dB.
- [DSSSModAcc:Results:I/Q Origin Offset Mean (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0305b.html) Returns the I/Q origin offset. This value is expressed in dB.
- [DSSSModAcc:Results:I/Q Quadrature Error Mean (deg)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03057.html) Returns the I/Q quadrature error. This value is expressed in degrees.
- [DSSSModAcc:Results:Number of Chips Used](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0304d.html) Returns the number of chips used for the DSSSModAcc measurement.
- [DSSSModAcc:Results:PPDU Info:Data Modulation Format](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03068.html) Returns the data modulation format results of the analyzed waveform.
- [DSSSModAcc:Results:PPDU Info:Header CRC Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0306d.html) Returns whether the header cyclic redundancy check (CRC) is successfully passed, as defined in section 16.2.3.7 of IEEE Standard 802.11 2016 .
- [DSSSModAcc:Results:PPDU Info:Locked Clocks Bit](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0306c.html) Returns the value of the locked clocks bit in the Long PHY SERVICE field.
- [DSSSModAcc:Results:PPDU Info:PSDU CRC Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0306e.html) Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed.
- [DSSSModAcc:Results:PPDU Info:Payload Length (bytes)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03069.html) Returns the payload length of the acquired burst. This value is expressed in bytes.
- [DSSSModAcc:Results:PPDU Info:Preamble Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0306a.html) Returns the detected preamble type of the acquired burst.
- [DSSSModAcc:Results:Peak EVM (802.11-1999):Maximum (% or dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03034.html) Returns the peak EVM of the burst. This value is expressed as percentage or in dB.
- [DSSSModAcc:Results:Peak EVM (802.11-1999):Mean (% or dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03033.html) Returns the peak EVM of the burst. This value is expressed as a percentage or in dB.
- [DSSSModAcc:Results:Peak EVM (802.11-2007):Maximum (% or dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03036.html) Returns the peak EVM of the burst. This value is expressed as a percentage or in dB.
- [DSSSModAcc:Results:Peak EVM (802.11-2007):Mean (% or dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03035.html) Returns the peak EVM of the burst. This value is expressed as a percentage or in dB.
- [DSSSModAcc:Results:Peak EVM (802.11-2016):Maximum (% or dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0303d.html) Returns the peak EVM of the burst. This value is expressed as a percentage or in dB.
- [DSSSModAcc:Results:Peak EVM (802.11-2016):Mean (% or dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0303c.html) Returns the peak EVM of the burst. This value is expressed as a percentage or in dB.
- [DSSSModAcc:Results:Power:Custom Gate Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0303e.html) Returns the average power of the custom gate. This value is expressed in dBm.
- [DSSSModAcc:Results:Power:Custom Gate Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0303f.html) Returns the peak power of the custom gate. This value is expressed in dBm.
- [DSSSModAcc:Results:Power:Data Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03076.html) Returns the average power of the data field of the PPDU. This value is expressed in dBm.
- [DSSSModAcc:Results:Power:Data Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03077.html) Returns the peak power of the data field of the PPDU. This value is expressed in dBm.
- [DSSSModAcc:Results:Power:Header Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03074.html) Returns the average power of the header field of the PPDU. This value is expressed in dBm.
- [DSSSModAcc:Results:Power:Header Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03075.html) Returns the peak power of the header field of the PPDU. This value is expressed in dBm.
- [DSSSModAcc:Results:Power:PPDU Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03078.html) Returns the average power of the PPDU. This value is expressed in dBm.
- [DSSSModAcc:Results:Power:PPDU Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03079.html) Returns the peak power of the PPDU. This value is expressed in dBm.
- [DSSSModAcc:Results:Power:Preamble Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03072.html) Returns the average power of the preamble field of the PPDU. This value is expressed in dBm.
- [DSSSModAcc:Results:Power:Preamble Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03073.html) Returns the peak power of the preamble field of the PPDU. This value is expressed in dBm.
- [DSSSModAcc:Results:RMS EVM Mean (% or dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03032.html) Returns the RMS EVM of the burst. This value is expressed as a percentage or in dB.
- [DSSSModAcc:Results:RMS Magnitude Error Mean (%)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03062.html) Returns the RMS magnitude error of the received constellation, which is the RMS level of the one minus the magnitude error of the received constellation symbols. This value is expressed as a percentage.
- [DSSSModAcc:Results:RMS Phase Error Mean (deg)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra03063.html) Returns the RMS phase error of the received constellation, which is the RMS level of difference between the ideal and the actual values of the phase of the received constellation symbols. This value is expressed in degrees.
- [DSSSModAcc:Spectrum Inverted](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0307b.html) Specifies whether the spectrum of the measured signal is inverted.
- [External Attenuation (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00003.html) Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help .
- [OFDM:Advanced:2xLDPC Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00041.html) Specifies whether to enable 2xLDPC for 802.11bn MU PPDU and 802.11bn TB PPDU signals.
- [OFDM:Advanced:Auto PPDU Type Detection Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00027.html) Specifies whether to enable auto detection of the PPDU type when performing the OFDMModAcc measurement.
- [OFDM:Advanced:DCM Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00021.html) Specifies whether the dual carrier modulation (DCM) is applied to the data field of the 802.11ax TB PPDU signals.
- [OFDM:Advanced:Distribution Bandwidth (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00040.html) Specifies the bandwidth across which RU subcarriers are distributed, when you set >OFDM RU Type property to dRU .
- [OFDM:Advanced:FEC Coding Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00032.html) Specifies the type of forward error correction (FEC) coding used.
- [OFDM:Advanced:Guard Interval Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0001c.html) Specifies the size of the guard interval of OFDM symbols.
- [OFDM:Advanced:Header Decoding Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00028.html) Specifies whether to enable the decoding of the header fields in the PPDU.
- [OFDM:Advanced:IM Pilots Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00042.html) Specifies whether inteference mitigating pilots are present in 802.11bn MU PPDU signals.
- [OFDM:Advanced:LDPC Extra Symbol Segment](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00034.html) Specifies the presence of an extra OFDM symbol segment for LDPC in the 802.11ax TB PPDU, 802.11be TB PPDU, and 802.11bn TB PPDU.
- [OFDM:Advanced:LTF Size](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0001d.html) Specifies the LTF symbol size. This property is applicable only for 802.11ax, 802.11be, and 802.11bn signals.
- [OFDM:Advanced:MCS Index](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00019.html) Specifies the modulation and coding scheme (MCS) index or the data rate when you set the OFDM Header Decoding Enabled property to False .
- [OFDM:Advanced:MU-MIMO LTF Mode Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00029.html) Specifies whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code.
- [OFDM:Advanced:Number of HE-SIG-B Symbols](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00020.html) Specifies the number of HE-SIG-B symbols.
- [OFDM:Advanced:Number of LTF Symbols](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00022.html) Specifies the number of HE-LTF, EHT-LTF, or UHR-LTF symbols in the 802.11ax TB PPDU, 802.11be or 802.11bn TB PPDU, respectively.
- [OFDM:Advanced:Number of SIG Symbols](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0003b.html) Specifies the number of SIG symbols. This property is applicable for 802.11be and 802.11bn MU PPDU signals.
- [OFDM:Advanced:Number of Space Time Streams](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0001e.html) Specifies the number of space time streams.
- [OFDM:Advanced:Number of Users](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00018.html) Specifies the number of users in a multi-user (MU) PPDU.
- [OFDM:Advanced:PE Disambiguity](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00031.html) Specifies the packet extension disambiguity information.
- [OFDM:Advanced:PPDU Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00017.html) Specifies the PPDU type when you set the OFDM Auto PPDU Type Detection Enabled property to False .
- [OFDM:Advanced:Phase Rotation:Auto Detection Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0003c.html) Specifies whether to enable auto detection of phase rotation coefficients.
- [OFDM:Advanced:Phase Rotation:Coefficient 1](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00037.html) Specifies the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D7.0 .
- [OFDM:Advanced:Phase Rotation:Coefficient 2](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00038.html) Specifies the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D7.0 .
- [OFDM:Advanced:Phase Rotation:Coefficient 3](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00039.html) Specifies the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D7.0 .
- [OFDM:Advanced:Pre-FEC Padding Factor](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00033.html) Specifies the pre-FEC padding factor used in 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU for decoding PLCP service data unit (PSDU) bits.
- [OFDM:Advanced:Preamble Puncturing:Bitmap](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00030.html) Specifies the punctured 20 MHz sub-channels in the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal when preamble puncturing is enabled.
- [OFDM:Advanced:Preamble Puncturing:Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0002f.html) Specifies whether the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal is preamble punctured.
- [OFDM:Advanced:RU Offset/MRU Index](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0001b.html) Specifies the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of IEEE P802.11be/D7.0 . If a dRU is configured, the RU Offset represents dRU Index as defined in the Table 38-4 to Table 38-6 and the Equation 38-1 of IEEE P802.11bn/D1.3 .
- [OFDM:Advanced:RU Size](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0001a.html) Specifies the size of the resource unit (RU) or the multiple resource unit (MRU) in terms of number of subcarriers for 802.11ax, 802.11be, and 802.11bn signals.
- [OFDM:Advanced:RU Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0003f.html) Specifies whether contiguous subcarriers form the resource unit (rRU) or non-contiguous subcarriers form the resource unit (dRU).
- [OFDM:Advanced:SIG Compression Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0003a.html) Specifies whether to enable SIG compression. This property is applicable only for 802.11be MU PPDU and 802.11bn MU PPDU signals.
- [OFDM:Advanced:STBC Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00035.html) Specifies whether space-time block coding is enabled. This property is applicable only for 802.11ax TB PPDU.
- [OFDM:Advanced:Scrambler Seed](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0003d.html) Specifies the scrambler seed for combined signal demodulation. This is applicable only if OFDMModAcc Combined Signal Demodulation Enabled is set to True .
- [OFDM:Advanced:Space Time Stream Offset](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0001f.html) Specifies the space time stream offset.
- [OFDM:Advanced:Unequal Modulation:Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00043.html) Specifies whether to enable unequal modulation in different spatial streams for 802.11bn MU PPDU signals.
- [OFDM:Advanced:Unequal Modulation:Pattern Index](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00044.html) Specifies the unequal modulation pattern for the user. Valid values are between 0 and number of space time streams-1.
- [OFDM:Channel Bandwidth (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0000e.html) Specifies the channel spacing as defined under section 3.1 of IEEE Standard 802.11-2016 (pp. 130) . This value is specified in Hz.
- [OFDM:Frequency Band](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00016.html) Specifies the ISM frequency band. The SEM measurement uses this information to select an appropriate mask as defined in IEEE Standard 802.11n - 2009 and IEEE Standard P802.11be/D7.0 .
- [OFDM:Frequency Segment Index](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00014.html) Specifies the frequency segment index to be analyzed in an 80+80 MHz 802.11ax signal. You must set this property to either of the valid values when you want to analyze one of the two segments.
- [OFDM:Number of Frequency Segments](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0000f.html) Specifies the number of frequency segments for 802.11ac and 802.11ax signals.
- [OFDM:Number of Receive Chains](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00010.html) Specifies the number of receive chains for OFDM standards.
- [OFDM:Transmit Power Class](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00015.html) Specifies the STA transmit power classification as defined in annexure D.2.2 of IEEE Standard 802.11-2016 , if you set the Standard property to 802.11p .
- [OFDMModAcc:Acquisition Length (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0400a.html) Specifies the length of the waveform to be acquired for the OFDMModAcc measurement, when you set the OFDMModAcc Acquisition Length Mode property to Manual . This value is expressed in seconds.
- [OFDMModAcc:Acquisition Length Mode](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04009.html) Specifies whether the measurement automatically computes the acquisition length of the waveform based on other OFDMModAcc properties.
- [OFDMModAcc:All Traces Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04005.html) Specifies whether to enable all the traces computed by the OFDMModAcc measurement.
- [OFDMModAcc:Amplitude Tracking Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0400e.html) Specifies whether to enable pilot-based mean amplitude tracking per OFDM data symbol.
- [OFDMModAcc:Auto Level:Allow Overflow](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040b1.html) Specifies whether the RFmxWLAN OFDMModAcc Auto Level VI should search for the optimum reference levels while allowing ADC overflow.
- [OFDMModAcc:Averaging:Count](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04003.html) Specifies the number of acquisitions used for averaging when you set the OFDMModAcc Averaging Enabled property to True .
- [OFDMModAcc:Averaging:Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04002.html) Specifies whether to enable averaging for OFDMModAcc measurements.
- [OFDMModAcc:Averaging:Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ac.html) Specifies the averaging type for the OFDMModAcc measurement.
- [OFDMModAcc:Averaging:Vector Averaging:Phase Alignment Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ae.html) Specifies whether to enable phase alignment for the acquired I/Q data across multiple acquisitions.
- [OFDMModAcc:Averaging:Vector Averaging:Time Alignment Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ad.html) Specifies whether to enable time alignment for the acquired I/Q data across multiple acquisitions.
- [OFDMModAcc:Burst Start Detection Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04085.html) Specifies whether the measurement detects a rising edge of a burst in the acquired waveform.
- [OFDMModAcc:Channel Estimation:Interpolation Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0406a.html) Specifies the interpolation type and/or smoothing type used on the channel estimates.
- [OFDMModAcc:Channel Estimation:L-LTF Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04087.html) Specifies whether to use the legacy channel estimation field for combining with the reference channel frequency response.
- [OFDMModAcc:Channel Estimation:LTF Averaging Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e0.html) Specifies whether to average multiple Long Training Field (LTF) symbols to improve channel estimation. This property is only applicable for 11ax, 11be and 11bn standards.
- [OFDMModAcc:Channel Estimation:Relative Delay Spread](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040b7.html) Specifies the expected channel delay spread relative to the OFDM symbol length.
- [OFDMModAcc:Channel Estimation:Smoothing Length](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0406b.html) Specifies the length of the triangular-weighted moving window across subcarriers that is used for averaging the channel estimate.
- [OFDMModAcc:Channel Estimation:Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04011.html) Specifies the fields in the PPDU used to estimate the channel frequency response.
- [OFDMModAcc:Channel Matrix Power Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408d.html) Specifies whether the channel frequency response matrix power measurements are enabled. This enables cross-power measurements for MIMO signals and user-power measurements for MU signals.
- [OFDMModAcc:Combined Signal Demodulation Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ca.html) Specifies whether to enable demodulation of the signal that is formed by combining signals from multiple transmitter chains.
- [OFDMModAcc:Common Clock Source Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0400d.html) Specifies whether the transmitter uses the same reference clock signal for generating the RF carrier and the symbol clock.
- [OFDMModAcc:Common Pilot Error Scaling Reference](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d1.html) Specifies whether common pilot error is computed relative to only LTF or scaling by average CPE.
- [OFDMModAcc:Data Decoding Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408b.html) Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC).
- [OFDMModAcc:EVM Reference Data Symbols Mode](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04093.html) Specifies whether to use an acquired waveform or a reference waveform to create reference data symbols (ideal constellation points) for an EVM computation.
- [OFDMModAcc:EVM Unit](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04008.html) Specifies the unit for EVM results.
- [OFDMModAcc:Frequency Error Estimation Method](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0407e.html) Specifies the PPDU fields that the measurement uses to estimate the carrier frequency error in the acquired signal.
- [OFDMModAcc:I/Q Impairments:Estimation Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0407b.html) Specifies whether to enable the estimation of I/Q gain imbalance, I/Q quadrature error, and I/Q timing skew impairments.
- [OFDMModAcc:I/Q Impairments:I/Q Gain Imbalance Correction Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401c.html) Specifies whether to enable I/Q gain imbalance correction.
- [OFDMModAcc:I/Q Impairments:I/Q Impairments Per Subcarrier Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0407f.html) Specifies whether to estimate I/Q impairments independently for each subcarrier.
- [OFDMModAcc:I/Q Impairments:I/Q Quadrature Error Correction Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401d.html) Specifies whether to enable I/Q quadrature error correction.
- [OFDMModAcc:I/Q Impairments:I/Q Timing Skew Correction Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401e.html) Specifies whether to enable I/Q timing skew correction.
- [OFDMModAcc:I/Q Impairments:Model](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401b.html) Specifies the I/Q impairments model used by the measurement for estimating I/Q impairments.
- [OFDMModAcc:Maximum Measurement Length (symbols)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0400c.html) Specifies the maximum number of OFDM symbols that the measurement uses to compute EVM. This value is expressed in symbols.
- [OFDMModAcc:Measurement Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04000.html) Specifies whether to enable OFDMModAcc measurement for OFDM based standards.
- [OFDMModAcc:Measurement Mode](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04066.html) Specifies whether the measurement calibrates the noise floor of analyzer or performs the ModAcc measurement.
- [OFDMModAcc:Measurement Offset (symbols)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0400b.html) Specifies the number of data symbols to be ignored from the start of the data field for EVM computation. This value is expressed in symbols.
- [OFDMModAcc:Noise Compensation:Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04067.html) Specifies whether the contribution of the instrument noise is compensated for EVM computation.
- [OFDMModAcc:Noise Compensation:Input Power Check Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04068.html) Specifies whether the measurement checks if any high power signal is present at the RFIn port of the instrument while performing noise floor calibration.
- [OFDMModAcc:Noise Compensation:Reference Level Coercion Limit (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04069.html) Specifies the reference level coercion limit for noise compensation. This value is expressed in dB.
- [OFDMModAcc:Number of Analysis Threads](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04004.html) Specifies the maximum number of threads used for parallelism for the OFDMModAcc measurement.
- [OFDMModAcc:Optimize Dynamic Range for EVM:Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0407c.html) Specifies whether to optimize the analyzer's dynamic range for the EVM measurement.
- [OFDMModAcc:Optimize Dynamic Range for EVM:Margin (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0407d.html) Specifies the margin above the reference level you specify when you set the OFDMModAcc Optimize Dynamic Range for EVM Enabled property to True . This value is expressed in dB.
- [OFDMModAcc:Phase Tracking Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0400f.html) Specifies whether to enable pilot-based common phase error correction per OFDM data symbol.
- [OFDMModAcc:Power:Custom Gate Start Time (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04019.html) Specifies the start time of the custom power gate. This value is expressed in seconds.
- [OFDMModAcc:Power:Custom Gate Stop Time (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401a.html) Specifies the stop time of the custom power gate, and must be greater than the corresponding OFDMModAcc Pwr Custom Gate Start Time property. This value is expressed in seconds.
- [OFDMModAcc:Power:Measurement Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04017.html) Specifies whether power measurements are performed.
- [OFDMModAcc:Power:Number of Custom Gates](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04018.html) Specifies the number of custom gates for power measurement.
- [OFDMModAcc:Reference Data Constellation Identifier](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040cb.html) Identifies the reference files used for combined signal demodulation. The value of this property must be same as the value of the Reference Data Identifier string specified while creating the reference files. This is applicable only if OFDMModAcc Combined Signal Demodulation Enabled is set to True .
- [OFDMModAcc:Results:Absolute I/Q Origin Offset Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0402c.html) Returns the absolute I/Q origin offset, which is the power of the DC subcarrier. This value is expressed in dBm.
- [OFDMModAcc:Results:Burst Start Time Mean (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040b0.html) Returns the absolute time corresponding to the detected start of the analyzed burst. The start time is computed with respect to the initial time value of the acquired waveform. This value is expressed in seconds.
- [OFDMModAcc:Results:Chain Data RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04072.html) Returns the chain RMS EVM of data subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:Chain Pilot RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04073.html) Returns the chain RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:Chain RMS EVM Maximum (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04098.html)
- [OFDMModAcc:Results:Chain RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04071.html) Returns the chain RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:Chain RMS EVM Minimum (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04099.html)
- [OFDMModAcc:Results:Channel Matrix Power:Chain Stream Cross Power Mean (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e8.html) Returns the stream cross power. The cross power for chain k stream m is the power contribution of stream m in chain k . This value is expressed in dB.
- [OFDMModAcc:Results:Channel Matrix Power:Cross Power Mean (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408e.html) Returns the cross power. The cross power for chain x is the power contribution from streams other than stream x in the chain. This value is expressed in dB.
- [OFDMModAcc:Results:Channel Matrix Power:User Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409c.html)
- [OFDMModAcc:Results:Channel Matrix Power:User Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408f.html) Returns the user power. User power is the frequency domain power measured over subcarriers occupied by a given user. This value is expressed in dBm.
- [OFDMModAcc:Results:Channel Matrix Power:User Power Minimum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409d.html)
- [OFDMModAcc:Results:Composite Data RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0406f.html) Returns the RMS EVM of data-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:Composite Pilot RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04070.html) Returns the RMS EVM of pilot-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:Composite RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0406e.html) Returns the RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:EHT-SIG RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040bf.html) Returns the RMS EVM of subcarriers in the EHT-SIG symbol. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:ELR-SIG RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d4.html) Returns the RMS EVM of subcarriers in the ELR-SIG symbol. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:Frequency Error CCDF 10% (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04029.html) Returns the 10% point of Complementary Cumulative Distribution Function (CCDF) of the absolute frequency error. This value is expressed in Hz.
- [OFDMModAcc:Results:Frequency Error Maximum (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a0.html)
- [OFDMModAcc:Results:Frequency Error Mean (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04028.html) Returns the carrier frequency error of the transmitter. This value is expressed in Hz.
- [OFDMModAcc:Results:Frequency Error Minimum (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a1.html)
- [OFDMModAcc:Results:I/Q Gain Imbalance Maximum (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a6.html)
- [OFDMModAcc:Results:I/Q Gain Imbalance Mean (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0402d.html) Returns the I/Q gain imbalance, which is the ratio of the RMS amplitude of the in-phase (I) component of the signal to the RMS amplitude of the quadrature-phase (Q) component of the signal. This value is expressed in dB.
- [OFDMModAcc:Results:I/Q Gain Imbalance Minimum (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a7.html)
- [OFDMModAcc:Results:I/Q Quadrature Error Maximum (deg)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a8.html)
- [OFDMModAcc:Results:I/Q Quadrature Error Mean (deg)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0402e.html) Returns the I/Q quadrature error, which is a measure of deviation of the phase difference between the quadrature-phase (Q) and the in-phase (I) component of the signal from 90 degrees. This value is expressed in degrees.
- [OFDMModAcc:Results:I/Q Quadrature Error Minimum (deg)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a9.html)
- [OFDMModAcc:Results:I/Q Timing Skew Mean (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0402f.html) Returns the I/Q timing skew, which is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. This value is expressed in seconds.
- [OFDMModAcc:Results:L-SIG RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040bb.html) Returns the RMS EVM of subcarriers in the L-SIG symbol. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:Noise Compensation Applied](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04027.html) Returns whether the noise compensation is applied.
- [OFDMModAcc:Results:Number of Symbols Used](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04016.html) Returns the number of OFDM symbols used by the measurement.
- [OFDMModAcc:Results:PPDU Info:2xLDPC Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e3.html) Returns whether 2xLDPC is enabled for a specified user.
- [OFDMModAcc:Results:PPDU Info:Aggregation](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c9.html) Returns the value of the Aggregation field as decoded from the high-throughput signal (HT-SIG) field of 802.11n signal.
- [OFDMModAcc:Results:PPDU Info:DCM Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ab.html) Returns whether DCM is enabled for a specified user.
- [OFDMModAcc:Results:PPDU Info:Distribution Bandwidth (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e2.html) Returns the bandwidth across which RU Subcarriers are distributed for a user.
- [OFDMModAcc:Results:PPDU Info:EHT-SIG CRC Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04092.html) Returns whether the cyclic redundancy check (CRC) has passed for the EHT-SIG field of the 802.11be waveform.
- [OFDMModAcc:Results:PPDU Info:ELR-SIG CRC Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d5.html) Returns whether the cyclic redundancy check (CRC) has passed for the ELR-SIG field of the 802.11bn waveform.
- [OFDMModAcc:Results:PPDU Info:FEC Coding Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040aa.html) Returns the FEC coding type for a specified user.
- [OFDMModAcc:Results:PPDU Info:Guard Interval Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04037.html) Returns the size of the guard interval of OFDM symbols.
- [OFDMModAcc:Results:PPDU Info:IM Pilots Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e4.html) Returns whether interference mitigating pilots are present.
- [OFDMModAcc:Results:PPDU Info:L-SIG Parity Check Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04088.html) Returns whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be/802.11bn waveforms.
- [OFDMModAcc:Results:PPDU Info:LTF Size](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04038.html) Returns the HE-LTF size, EHT-LTF or UHR-LTF size when you set the Standard property to 802.11ax , 802.11be , or 802.11bn , respectively.
- [OFDMModAcc:Results:PPDU Info:MCS Index](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04032.html) Returns the MCS index or the data rate of the measured signal.
- [OFDMModAcc:Results:PPDU Info:Number of HE-SIG-B Symbols](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04036.html) Returns the number of HE-SIG-B symbols.
- [OFDMModAcc:Results:PPDU Info:Number of SIG Symbols](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e7.html)
- [OFDMModAcc:Results:PPDU Info:Number of Space Time Streams](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04039.html) Returns the number of space time streams.
- [OFDMModAcc:Results:PPDU Info:Number of Users](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04035.html) Returns the number of users.
- [OFDMModAcc:Results:PPDU Info:PE Duration (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04095.html) Returns the duration of the packet extension field for the 802.11ax, 802.11be and 802.11bn signals. This value is expressed in seconds.
- [OFDMModAcc:Results:PPDU Info:PPDU Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04031.html) Returns the PPDU type of the measured signal.
- [OFDMModAcc:Results:PPDU Info:PSDU CRC Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408c.html) Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed.
- [OFDMModAcc:Results:PPDU Info:RU Offset/MRU Index](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04034.html) Returns the location of RU or MRU for a user. If an RU is detected, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is detected, the MRU Index is as defined in the Table 36-8 to Table 36-15 of IEEE P802.11be/D7.0 .
- [OFDMModAcc:Results:PPDU Info:RU Size](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04033.html) Returns the RU or the MRU size.
- [OFDMModAcc:Results:PPDU Info:RU Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e1.html) Returns the type of RU for a user.
- [OFDMModAcc:Results:PPDU Info:SIG CRC Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04089.html) Returns whether the cyclic redundancy check (CRC) has passed either for the HT-SIG field of the 802.11n waveform, for the VHT-SIG-A field of the 802.11ac waveform, or for the HE-SIG-A field of the 802.11ax waveform.
- [OFDMModAcc:Results:PPDU Info:SIG-B CRC Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408a.html) Returns whether the cyclic redundancy check (CRC) has passed for the HE-SIG-B field of the 802.11ax MU PPDU waveform.
- [OFDMModAcc:Results:PPDU Info:Scrambler Seed](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c8.html) Returns the detected initial state of the scrambler, which is used to scramble the data bits in the device under test (DUT). RFmx uses the same seed to descramble the received bit-sequence.
- [OFDMModAcc:Results:PPDU Info:Space Time Stream Offset](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04090.html) Returns the space time stream offset. This property is applicable only to 802.11ac, 802.11ax, 802.11be, and 802.11bn signals.
- [OFDMModAcc:Results:PPDU Info:U-SIG CRC Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04091.html) Returns whether the cyclic redundancy check (CRC) has passed for the U-SIG field of the 802.11be or the 802.11bn waveform.
- [OFDMModAcc:Results:PPDU Info:UHR-SIG CRC Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d3.html) Returns whether the cyclic redundancy check (CRC) has passed for the UHR-SIG field of the 802.11bn waveform.
- [OFDMModAcc:Results:PPDU Info:Unequal Modulation:Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e5.html) Returns whether unequal modulation is enabled for a specified user.
- [OFDMModAcc:Results:PPDU Info:Unequal Modulation:Pattern Index](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e6.html) Returns unequal modulation pattern for a specified user.
- [OFDMModAcc:Results:Phase Rotation:Coefficient 1](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040b8.html) Specifies the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D7.0 .
- [OFDMModAcc:Results:Phase Rotation:Coefficient 2](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040b9.html) Specifies the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D7.0 .
- [OFDMModAcc:Results:Phase Rotation:Coefficient 3](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ba.html) Specifies the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D7.0 .
- [OFDMModAcc:Results:Power:Custom Gate Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04062.html) Returns the average power of the custom gate. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:Custom Gate Peak Power Max (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04063.html) Returns the peak power of the custom gate. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:Data Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0405c.html) Returns the average power of the data field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:Data Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0405d.html) Returns the peak power of the data field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:EHT-LTF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c6.html) Returns the average power of the EHT-LTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:EHT-LTF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c7.html) Returns the peak power of the EHT-LTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:EHT-SIG Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c2.html) Returns the average power of the EHT-SIG field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:EHT-SIG Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c3.html) Returns the peak power of the EHT-SIG field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:EHT-STF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c4.html) Returns the average power of the EHT-STF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:EHT-STF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c5.html) Returns the peak power of the EHT-STF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:ELR-MARK Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040de.html) Returns the average power of the ELR-MARK field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:ELR-MARK Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040df.html) Returns the peak power of the ELR-MARK field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:ELR-SIG Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040dc.html) Returns the average power of the ELR-SIG field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:ELR-SIG Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040dd.html) Returns the peak power of the ELR-SIG field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HE-LTF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0405a.html) Returns the average power of the HE-LTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HE-LTF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0405b.html) Returns the peak power of the HE-LTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HE-SIG-A Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04046.html) Returns the average power of the HE-SIG-A field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HE-SIG-A Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04047.html) Returns the peak power of the HE-SIG-A field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HE-SIG-B Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404a.html) Returns the average power of the HE-SIG-B field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HE-SIG-B Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404b.html) Returns the peak power of the HE-SIG-B field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HE-STF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04052.html) Returns the average power of the HE-STF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HE-STF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04053.html) Returns the peak power of the HE-STF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HT-DLTF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04054.html) Returns the average power of the HT-DLTF. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HT-DLTF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04055.html) Returns the peak power of the HT-DLTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HT-ELTF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04056.html) Returns the average power of the HT-ELTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HT-ELTF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04057.html) Returns the peak power of the HT-ELTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HT-GF-STF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404e.html) Returns the average power of the HT-GF-STF. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HT-GF-STF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404f.html) Returns the peak power of the HT-GF-STF. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HT-SIG Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04042.html) Returns the average power of the HT-SIG field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HT-SIG Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04043.html) Returns the peak power of the HT-SIG field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HT-STF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404c.html) Returns the average power of the HT-STF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:HT-STF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404d.html) Returns the peak power of the HT-STF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:L-LTF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0403c.html) Returns the average power of the L-LTF or LTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:L-LTF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0403d.html) Returns the peak power of the L-LTF or LTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:L-SIG Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0403e.html) Returns the average power of the L-SIG or SIGNAL field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:L-SIG Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0403f.html) Returns the peak power of the L-SIG or SIGNAL field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:L-STF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0403a.html) Returns the average power of the L-STF or STF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:L-STF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0403b.html) Returns the peak power of the L-STF or STF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:PE Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0405e.html) Returns the average power of the packet extension field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:PE Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0405f.html) Returns the peak power of the packet extension field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:PPDU Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04060.html) Returns the average power of the PPDU. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:PPDU Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04061.html) Returns the peak power of the PPDU. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:RL-SIG Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04040.html) Returns the average power of the RL-SIG field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:RL-SIG Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04041.html) Returns the peak power of the RL-SIG field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:U-SIG Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c0.html) Returns the average power of the U-SIG field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:U-SIG Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c1.html) Returns the peak power of the U-SIG field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:UHR-LTF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d8.html) Returns the average power of the UHR-LTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:UHR-LTF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d9.html) Returns the peak power of the UHR-LTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:UHR-SIG Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040da.html) Returns the average power of the UHR-SIG field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:UHR-SIG Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040db.html) Returns the peak power of the UHR-SIG field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:UHR-STF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d6.html) Returns the average power of the UHR-STF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:UHR-STF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d7.html) Returns the peak power of the UHR-STF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:VHT-LTF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04058.html) Returns the average power of the VHT-LTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:VHT-LTF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04059.html) Returns the peak power of the VHT-LTF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:VHT-SIG-A Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04044.html) Returns the average power of the VHT-SIG-A field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:VHT-SIG-A Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04045.html) Returns the peak power of the VHT-SIG-A field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:VHT-SIG-B Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04048.html) Returns the average power of the VHT-SIG-B field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:VHT-SIG-B Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04049.html) Returns the peak power of the VHT-SIG-B field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:VHT-STF Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04050.html) Returns the average power of the VHT-STF field. This value is expressed in dBm.
- [OFDMModAcc:Results:Power:VHT-STF Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04051.html) Returns the peak power of the VHT-STF field. This value is expressed in dBm.
- [OFDMModAcc:Results:RMS Common Phase Error Mean (deg)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04030.html) Returns the RMS common phase error.
- [OFDMModAcc:Results:RMS Common Pilot Error Mean (%)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0406d.html) Returns the RMS common pilot error. This value is expressed as a percentage.
- [OFDMModAcc:Results:Relative I/Q Origin Offset Maximum (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a4.html)
- [OFDMModAcc:Results:Relative I/Q Origin Offset Mean (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0402b.html) Returns the relative I/Q origin offset, which is the ratio of the power of the DC subcarrier to the total power of all the subcarriers. This value is expressed in dB.
- [OFDMModAcc:Results:Relative I/Q Origin Offset Minimum (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a5.html)
- [OFDMModAcc:Results:SIG RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040bc.html) Returns the RMS EVM of subcarriers in the SIG symbol. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:SIG-B RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040bd.html) Returns the RMS EVM of subcarriers in the SIG-B symbol. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:Spectral Flatness Margin (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04023.html) Returns the spectral flatness margin, which is the minimum of the upper and lower spectral flatness margins. This value is expressed in dB.
- [OFDMModAcc:Results:Spectral Flatness Margin Maximum (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409e.html)
- [OFDMModAcc:Results:Spectral Flatness Margin Minimum (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409f.html)
- [OFDMModAcc:Results:Spectral Flatness Margin Subcarrier Index](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04024.html) Returns the subcarrier index corresponding to the OFDMModAcc Results Spectral Flatness Margin result.
- [OFDMModAcc:Results:Stream Data RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04075.html) Returns the stream RMS EVM of data subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:Stream Pilot RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04076.html) Returns the stream RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:Stream Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040cc.html) Returns average stream power across iterations for combined signal demodulation. This is applicable only if OFDMModAcc Combined Signal Demodulation Enabled is set to True .
- [OFDMModAcc:Results:Stream RMS EVM Maximum (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04096.html)
- [OFDMModAcc:Results:Stream RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04074.html) Returns the stream RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:Stream RMS EVM Minimum (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04097.html)
- [OFDMModAcc:Results:Symbol Clock Error Maximum (ppm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a2.html)
- [OFDMModAcc:Results:Symbol Clock Error Mean (ppm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0402a.html) Returns the symbol clock error of the transmitter.
- [OFDMModAcc:Results:Symbol Clock Error Minimum (ppm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a3.html)
- [OFDMModAcc:Results:U-SIG RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040be.html) Returns the RMS EVM of subcarriers in the U-SIG symbol. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:UHR-SIG RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d2.html) Returns the RMS EVM of subcarriers in the UHR-SIG symbol. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:Unused Tone Error:Margin (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04025.html) Returns the unused tone error margin, which is the minimum difference between the unused tone error mask and the unused tone error across 26-tone RUs. This value is expressed in dB.
- [OFDMModAcc:Results:Unused Tone Error:Margin RU Index](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04026.html) Returns the 26-tone RU index corresponding to the OFDMModAcc Results Unused Tone Error Margin result.
- [OFDMModAcc:Results:User Stream Data RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04078.html) Returns the RMS EVM of data-subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:User Stream Pilot RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04079.html) Returns the RMS EVM of pilot-subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:User Stream RMS EVM Maximum (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409a.html)
- [OFDMModAcc:Results:User Stream RMS EVM Mean (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04077.html) Returns the RMS EVM of all subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB.
- [OFDMModAcc:Results:User Stream RMS EVM Minimum (dB or %)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409b.html)
- [OFDMModAcc:Spectrum Inverted](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0407a.html) Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped.
- [OFDMModAcc:Symbol Clock Error Correction Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04010.html) Specifies whether to enable symbol clock error correction.
- [OFDMModAcc:Unused Tone Error Mask Reference](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0406c.html) Specifies the reference used to create the unused tone error mask for the 802.11ax, 802.11be or 802.11bn TB PPDU signals.
- [PowerRamp:Acquisition Length (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0200c.html) Specifies the duration of the signal to be acquired for the PowerRamp measurement. This value is expressed in seconds.
- [PowerRamp:All Traces Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra02016.html) Specifies whether to enable all the traces computed by the PowerRamp measurement.
- [PowerRamp:Averaging:Count](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra02015.html) Specifies the number of acquisitions used for averaging when you set the PowerRamp Averaging Enabled property to True .
- [PowerRamp:Averaging:Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra02014.html) Specifies if averaging is enabled for PowerRamp measurements.
- [PowerRamp:Measurement Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0200a.html) Specifies whether to enable PowerRamp measurement.
- [PowerRamp:Number of Analysis Threads](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra02017.html) Specifies the maximum number of threads used for parallelism for PowerRamp measurement.
- [PowerRamp:Results:Fall Time Mean (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra02019.html) Returns the power-ramp fall time of the burst. This value is expressed in seconds.
- [PowerRamp:Results:Rise Time Mean (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra02018.html) Returns the power-ramp rise time of the burst. This value is expressed in seconds.
- [Reference Level](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00002.html) Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.
- [Reference Level Headroom](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00ffc.html) Specifies the margin RFmx adds to the Reference Level property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.
- [Result Fetch Timeout (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0c000.html) Specifies the time, in seconds, to wait before results are available in the RFmxWLAN Property Node . Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxWLAN Property Node waits until the measurement is complete.
- [SEM:All Traces Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05017.html) Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement.
- [SEM:Amplitude Correction Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05016.html) Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table VI to configure the external attenuation table.
- [SEM:Averaging:Count](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05014.html) Specifies the number of acquisitions used for averaging when you set the SEM Averaging Enabled property to True .
- [SEM:Averaging:Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05013.html) Specifies whether to enable averaging for the SEM measurement.
- [SEM:Averaging:Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05015.html) Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement.
- [SEM:Carrier:Integration Bandwidth (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05005.html) Returns the integration bandwidth of the carrier as per the standard and channel bandwidth. This value is expressed in Hz.
- [SEM:Mask Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05002.html) Specifies whether the mask used for the SEM measurement is defined either as per the standard or as specified by you.
- [SEM:Measurement Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05000.html) Specifies whether to enable the spectral emission mask (SEM) measurement.
- [SEM:Number of Analysis Threads](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05018.html) Specifies the maximum number of threads used for parallelism for SEM measurement.
- [SEM:Offset:Number of Offsets](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05006.html) Specifies the number of offset segments for the SEM measurement when you set the SEM Mask Type property to Custom .
- [SEM:Offset:Relative Limit:Start (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500a.html) Specifies the relative power limit corresponding to the start of the offset segment. This value is expressed in dB.
- [SEM:Offset:Relative Limit:Stop (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500b.html) Specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB.
- [SEM:Offset:Sideband](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05009.html) Specifies whether the offset segment is present on one side or on both sides of the carrier.
- [SEM:Offset:Start Frequency (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05007.html) Specifies the start frequency of the offset segment relative to the carrier frequency. This value is expressed in Hz.
- [SEM:Offset:Stop Frequency (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05008.html) Specifies the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz.
- [SEM:Results:Carrier:Absolute Integrated Power (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0501c.html) Returns the average power of the carrier channel over the bandwidth indicated by the SEM Carrier IBW property. This value is expressed in dBm.
- [SEM:Results:Carrier:Absolute Peak Power (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0501e.html) Returns the peak power in the carrier channel over the bandwidth indicated by the SEM Carrier IBW property. This value is expressed in dBm. SEM mask level is determined by this result.
- [SEM:Results:Carrier:Peak Frequency (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0501f.html) Returns the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz.
- [SEM:Results:Lower Offset:Absolute Integrated Power (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05022.html) Returns the average power of the lower (negative) offset channel over the bandwidth obtained by the start and stop frequencies of the offset channel. This value is expressed in dBm.
- [SEM:Results:Lower Offset:Absolute Peak Power (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05024.html) Returns the peak power measured in the lower (negative) offset segment. This value is expressed in dBm.
- [SEM:Results:Lower Offset:Margin (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05027.html) Returns the margin from the SEM measurement mask for the lower (negative) offset. This value is expressed in dB.
- [SEM:Results:Lower Offset:Margin Absolute Power (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05028.html) Returns the power level of the spectrum corresponding to the result of the SEM Results Lower Offset Margin property. This value is expressed in dBm.
- [SEM:Results:Lower Offset:Margin Frequency (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0502a.html) Returns the frequency of the spectrum corresponding to the result of the SEM Results Lower Offset Margin property. This value is expressed in Hz.
- [SEM:Results:Lower Offset:Margin Relative Power (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05029.html) Returns the power level of the spectrum corresponding to the result of the SEM Results Lower Offset Margin property. This value is expressed in dB.
- [SEM:Results:Lower Offset:Measurement Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05021.html) Returns the lower offset segment measurement status indicating whether the spectrum exceeds the SEM measurement mask limits in the lower offset segment.
- [SEM:Results:Lower Offset:Peak Frequency (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05026.html) Returns the frequency at which the peak power occurs in the lower (negative) offset channel. This value is expressed in Hz.
- [SEM:Results:Lower Offset:Relative Integrated Power (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05023.html) Returns the average power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB.
- [SEM:Results:Lower Offset:Relative Peak Power (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05025.html) Returns the peak power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB.
- [SEM:Results:Measurement Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0501b.html) Returns the overall measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments.
- [SEM:Results:Upper Offset:Absolute Integrated Power (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0502c.html) Returns the average power of the offset (positive) offset channel over the bandwidth determined by the start and stop frequencies of the offset channel. This value is expressed in dBm.
- [SEM:Results:Upper Offset:Absolute Peak Power (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0502e.html) Returns the peak power of the offset (positive) offset segment. This value is expressed in dBm.
- [SEM:Results:Upper Offset:Margin (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05031.html) Returns the margin from the SEM measurement mask for the offset (positive). This value is expressed in dB.
- [SEM:Results:Upper Offset:Margin Absolute Power (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05032.html) Returns the power level of the spectrum corresponding to the result of the SEM Results Upper Offset Margin property. This value is expressed in dBm.
- [SEM:Results:Upper Offset:Margin Frequency (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05034.html) Returns the frequency of the spectrum corresponding to the result of the SEM Results Upper Offset Margin property. This value is expressed in Hz.
- [SEM:Results:Upper Offset:Margin Relative Power (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05033.html) Returns the power level of the spectrum corresponding to the result of the SEM Results Upper Offset Margin property. This value is expressed in dB.
- [SEM:Results:Upper Offset:Measurement Status](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0502b.html) Returns the upper offset (positive) segment measurement status indicating if the spectrum exceeds the SEM measurement mask limits in the upper offset segment.
- [SEM:Results:Upper Offset:Peak Frequency (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05030.html) Returns the frequency at which the peak power occurs in the offset (positive) channel. This value is expressed in Hz.
- [SEM:Results:Upper Offset:Relative Integrated Power (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0502d.html) Returns the average power of the offset (positive) offset segment relative to the peak power of the carrier channel. This value is expressed in dB.
- [SEM:Results:Upper Offset:Relative Peak Power (dB)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0502f.html) Returns the peak power of the offset (positive) segment relative to the peak power of the carrier channel. This value is expressed in dB.
- [SEM:Span:Auto](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500c.html) Specifies whether the frequency range of the spectrum used for SEM measurement is computed automatically by the measurement or is configured by you.
- [SEM:Span:Span (Hz)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500d.html) Specifies the frequency range of the spectrum used for the SEM measurement. This value is expressed in Hz.
- [SEM:Sweep Time:Auto](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05011.html) Specifies whether the sweep time for the SEM measurement is computed automatically or is configured by you.
- [SEM:Sweep Time:Interval (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05012.html) Specifies the sweep time for the SEM measurement. This value is expressed in seconds.
- [Selected Ports](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00ffd.html) Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names.
- [Selector String](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00000.html) Specifies the selector string used to access all subsequent channel-based properties in this instance of the property node.
- [Standard](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0000d.html) Specifies the signal under analysis as defined in IEEE Standard 802.11 .
- [TXP:All Traces Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01006.html) Specifies whether to enable the traces to be stored and retrieved after performing the TXP measurement.
- [TXP:Averaging:Count](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01005.html) Specifies the number of acquisitions used for averaging when you set the TXP Averaging Enabled property to True .
- [TXP:Averaging:Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01004.html) Specifies whether to enable averaging for the TXP measurement.
- [TXP:Burst Detection Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01003.html) Specifies whether the measurement detects the start and the end of a WLAN packet automatically.
- [TXP:Maximum Measurement Interval (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01002.html) Specifies the maximum measurement interval. This value is expressed in seconds.
- [TXP:Measurement Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01000.html) Specifies whether to enable the transmit power (TXP) measurement.
- [TXP:Number of Analysis Threads](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01007.html) Specifies the maximum number of threads used for parallelism for TXP measurement.
- [TXP:Results:Average Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01015.html)
- [TXP:Results:Average Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01009.html) Returns the average power of the acquired signal. This value is expressed in dBm.
- [TXP:Results:Average Power Minimum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01016.html)
- [TXP:Results:Peak Power Maximum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01011.html) Returns the peak power of the acquired signal. This value is expressed in dBm.
- [TXP:Results:Peak Power Mean (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01017.html)
- [TXP:Results:Peak Power Minimum (dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01018.html)
- [Trigger:Delay (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0000a.html) Specifies the trigger delay time. This value is expressed in seconds.
- [Trigger:Digital Edge:Edge](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00006.html) Specifies the active edge for the trigger. This property is used only when you set the Trigger Type property to Digital Edge .
- [Trigger:Digital Edge:Source](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00005.html) Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge .
- [Trigger:Gating:Enabled](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0002a.html) Enables time-domain gating of the acquired signal for SEM measurement.
- [Trigger:Gating:Length (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0002b.html) Specifies the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the Gate Enabled property to True .
- [Trigger:IQ Power Edge:Level (dB or dBm)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00008.html) Specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type property to Relative and in dBm when you set the IQ Power Edge Level Type property to Absolute .
- [Trigger:IQ Power Edge:Level Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00fff.html) Specifies the reference for the IQ Power Edge Level property. The IQ Power Edge Level Type property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Slope](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00009.html) Specifies whether the device asserts the trigger when the signal power is rising or falling.
- [Trigger:IQ Power Edge:Source](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00007.html) Specifies the channel from which the device monitors the trigger. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:Minimum Quiet Time:Duration (s)](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0000c.html) Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.
- [Trigger:Minimum Quiet Time:Mode](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0000b.html) Specifies whether the measurement computes the minimum quiet time used for triggering.
- [Trigger:Type](../../../resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00004.html) Specifies the trigger type.

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0001a.html language=enus -->
## TOPIC 00002: OFDM:Advanced:RU Size

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0001a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0001a.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the size of the resource unit (RU) or the multiple resource unit (MRU) in terms of number of subcarriers for 802.11ax, 802.11be, and 802.11bn signals. You must always configure this property for 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU. For 802.11ax Extended Range SU, MU, 80

### OFDM:Advanced:RU Size

Specifies the size of the resource unit (RU) or the multiple resource unit (MRU) in terms of number of subcarriers for 802.11ax, 802.11be, and 802.11bn signals.

You must always configure this property for 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU. For 802.11ax Extended Range SU, MU, 802.11be MU and 802.11bn MU PPDUs, you must configure this property if the [OFDM Header Decoding Enabled](attra00028.html) property is set to **False**.

Use "user<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for 802.11ax MU PPDU, 802.11ax TB PPDU, 802.11be MU PPDU, 802.11be TB PPDU, 802.11bn MU PPDU, and 802.11bn TB PPDU.

The default value is **26**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM RU Size |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| 26 | 26 | The RU size is 26. |
| --- | --- | --- |
| 52 | 52 | The RU size is 52. |
| 106 | 106 | The RU size is 106. |
| 242 | 242 | The RU size is 242. |
| 484 | 484 | The RU size is 484. |
| 996 | 996 | The RU size is 996. |
| 2x996 | 1992 | The RU size is 2 x 996. |
| 4x996 | 3984 | The RU size is 4 x 996. |
| 52+26 | 78 | The RU size is 52 + 26. |
| 106+26 | 132 | The RU size is 106 + 26. |
| 484+242 | 726 | The RU size is 484 + 242. |
| 996+484 | 1480 | The RU size is 996 + 484. |
| 996+484+242 | 1722 | The RU size is 996 + 484 + 242. |
| 2x996+484 | 2476 | The RU size is 2 x 996 + 484. |
| 3x996 | 2988 | The RU size is 3 x 996. |
| 3x996+484 | 3472 | The RU size is 3 x 996 + 484 |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0001b.html language=enus -->
## TOPIC 00003: OFDM:Advanced:RU Offset/MRU Index

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0001b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0001b.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of IEEE P802.11be/D7.0. If a

### OFDM:Advanced:RU Offset/MRU Index

Specifies the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of
 *IEEE P802.11be/D7.0*. If a dRU is configured, the RU Offset represents dRU Index as defined in the Table 38-4 to Table 38-6 and the Equation 38-1 of *IEEE P802.11bn/D1.3*.

This property is applicable for 802.11ax MU and TB PPDU, 802.11be MU and TB PPDU, and 802.11bn MU and TB PPDU signals. For 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU you must always configure this property. For 802.11ax MU PPDU, 802.11be MU PPDU and 802.11bn MU PPDU, you must configure this property if [OFDM Header Decoding Enabled](attra00028.html) is set to **False**.

Use "user<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for 802.11ax MU PPDU, 802.11ax TB PPDU, 802.11be MU PPDU, 802.11be TB PPDU, 802.11bn MU PPDU, and 802.11bn TB PPDU.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM RU Offset/MRU Index |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00022.html language=enus -->
## TOPIC 00004: OFDM:Advanced:Number of LTF Symbols

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00022.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00022.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of HE-LTF, EHT-LTF, or UHR-LTF symbols in the 802.11ax TB PPDU, 802.11be or 802.11bn TB PPDU, respectively. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the

### OFDM:Advanced:Number of LTF Symbols

Specifies the number of HE-LTF, EHT-LTF, or UHR-LTF symbols in the 802.11ax TB PPDU, 802.11be or 802.11bn TB PPDU, respectively.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The valid values are 1, 2, 4, 6, and 8. The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM Num LTF Symbols |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0002b.html language=enus -->
## TOPIC 00005: Trigger:Gating:Length (s)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0002b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0002b.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the Gate Enabled property to True. If the measurement interval required to perform the measurement exceeds the gate length, the measurement acquires as m

### Trigger:Gating:Length (s)

Specifies the maximum duration of time for each record used for computing the spectrum when you are performing an SEM measurement and when you set the [Gate Enabled](/csh?topicname=attra0002a.html) property to **True**.

If the measurement interval required to perform the measurement exceeds the gate length, the measurement acquires as many additional records as necessary to honor the required measurement interval. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1 millisecond.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Gate Length (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00030.html language=enus -->
## TOPIC 00006: OFDM:Advanced:Preamble Puncturing:Bitmap

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00030.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00030.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the punctured 20 MHz sub-channels in the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal when preamble puncturing is enabled. The binary representation of the signed integer is interpreted as the bitmap, where a '0' bit indicates that the corresponding sub-channel is

### OFDM:Advanced:Preamble Puncturing:Bitmap

Specifies the punctured 20 MHz sub-channels in the 802.11ax MU PPDU, the 802.11be MU PPDU or the 802.11bn MU PPDU signal when preamble puncturing is enabled.

The binary representation of the signed integer is interpreted as the bitmap, where a '0' bit indicates that the corresponding sub-channel is punctured. In the binary representation, the least significant bit (LSB) maps to the 20 MHz sub-channel lower in frequency, and the most significant bit (MSB) maps to the 20 MHz sub-channel higher in frequency. For a 80+80 MHz PPDU, the LSB represents the lowest sub-channel in the lower frequency segment. The puncturing information for the 20 MHz sub-channels of a 80 MHz PPDU are encoded in the least significant four bits. The puncturing information for the 20 MHz sub-channels of a 80+80 MHz PPDU or a 160 MHz PPDU is encoded in the least significant eight bits. The puncturing information for the 20 MHz sub-channels of a 320 MHz PPDU is encoded in the least significant sixteen bits.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **0xFFF FFFF FFFF FFFF**, indicating that none of the eight 20 MHz sub-channels of a 160 MHz PPDU are punctured. The most significant 52 bits are reserved for future use.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM Preamble Puncturing Bitmap |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00031.html language=enus -->
## TOPIC 00007: OFDM:Advanced:PE Disambiguity

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00031.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00031.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the packet extension disambiguity information. This property is applicable only for 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for

### OFDM:Advanced:PE Disambiguity

Specifies the packet extension disambiguity information.

This property is applicable only for 802.11ax TB PPDU, 802.11be TB PPDU and 802.11bn TB PPDU.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM PE Disambiguity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0003f.html language=enus -->
## TOPIC 00008: OFDM:Advanced:RU Type

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0003f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0003f.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether contiguous subcarriers form the resource unit (rRU) or non-contiguous subcarriers form the resource unit (dRU). This property is only applicable for 802.11bn TB PPDU signals. You must configure this property if OFDM Header Decoding Enabled is set to False. Use "user<n>" as the sele

### OFDM:Advanced:RU Type

Specifies whether contiguous subcarriers form the resource unit (rRU) or non-contiguous subcarriers form the resource unit (dRU).

This property is only applicable for 802.11bn TB PPDU signals. You must configure this property if [OFDM Header Decoding Enabled](attra00028.html) is set to **False**.

Use "user<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **rRU**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM RU Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| rRU | 0 | Contiguous subcarriers are present in the RU. |
| --- | --- | --- |
| dRU | 1 | Non-contiguous subcarriers are present in the RU. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00040.html language=enus -->
## TOPIC 00009: OFDM:Advanced:Distribution Bandwidth (Hz)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00040.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00040.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth across which RU subcarriers are distributed, when you set >OFDM RU Type property to dRU. This property is only applicable for 802.11bn TB PPDU signals. You must configure this property if OFDM Header Decoding Enabled is set to False. Use "user<n>" as the selector string to co

### OFDM:Advanced:Distribution Bandwidth (Hz)

Specifies the bandwidth across which RU subcarriers are distributed, when you set [>OFDM RU Type](/csh?topicname=attra0003f.html) property to **dRU**.

This property is only applicable for 802.11bn TB PPDU signals. You must configure this property if [OFDM Header Decoding Enabled](attra00028.html) is set to **False**.

Use "user<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **20M**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM DBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| 20M | 20000000 | DBW is 20 MHz. |
| --- | --- | --- |
| 40M | 40000000 | DBW is 40 MHz. |
| 60M | 60000000 | DBW is 60 MHz. |
| 80M | 80000000 | DBW is 80 MHz. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00041.html language=enus -->
## TOPIC 00010: OFDM:Advanced:2xLDPC Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00041.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00041.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable 2xLDPC for 802.11bn MU PPDU and 802.11bn TB PPDU signals. Use "user<n>" as the selector string to configure or read this property. The default value is False. Remarks The following table lists the characteristics of this property. Short Name OFDM 2xLDPC Enabled Data type

### OFDM:Advanced:2xLDPC Enabled

Specifies whether to enable 2xLDPC for 802.11bn MU PPDU and 802.11bn TB PPDU signals.

Use "user<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM 2xLDPC Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Specifies that 2xLDPC is disabled. |
| --- | --- | --- |
| True | 1 | Specifies that 2xLDPC is enabled. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00042.html language=enus -->
## TOPIC 00011: OFDM:Advanced:IM Pilots Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00042.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00042.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether inteference mitigating pilots are present in 802.11bn MU PPDU signals. This property is applicable only to 802.11bn MU PPDU signals. You must configure this property if the OFDM Header Decoding Enabled property is set to False. You do not need to use a selector string to configure

### OFDM:Advanced:IM Pilots Enabled

Specifies whether inteference mitigating pilots are present in 802.11bn MU PPDU signals.

This property is applicable only to 802.11bn MU PPDU signals. You must configure this property if the [OFDM Header Decoding Enabled](attra00028.html) property is set to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM IM Pilots Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Specifies that Interference Mitigating Pilots are absent. |
| --- | --- | --- |
| True | 1 | Specifies that Interference Mitigating Pilots are present. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00043.html language=enus -->
## TOPIC 00012: OFDM:Advanced:Unequal Modulation:Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00043.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00043.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable unequal modulation in different spatial streams for 802.11bn MU PPDU signals. This property is applicable only to 802.11bn MU PPDU signals. You must configure this property if the OFDM Header Decoding Enabled property is set to False. You do not need to use a selector str

### OFDM:Advanced:Unequal Modulation:Enabled

Specifies whether to enable unequal modulation in different spatial streams for 802.11bn MU PPDU signals.

This property is applicable only to 802.11bn MU PPDU signals. You must configure this property if the [OFDM Header Decoding Enabled](attra00028.html) property is set to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM Unequal Modulation Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Specifies that Unequal Modulation is disabled. |
| --- | --- | --- |
| True | 1 | Specifies that Unequal Modulation is enabled. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00044.html language=enus -->
## TOPIC 00013: OFDM:Advanced:Unequal Modulation:Pattern Index

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00044.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra00044.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unequal modulation pattern for the user. Valid values are between 0 and number of space time streams-1. This property is applicable only to 802.11bn MU PPDU signals. You must configure this property if the OFDM Header Decoding Enabled property is set to False. You do not need to use a

### OFDM:Advanced:Unequal Modulation:Pattern Index

Specifies the unequal modulation pattern for the user. Valid values are between 0 and number of space time streams-1.

This property is applicable only to 802.11bn MU PPDU signals. You must configure this property if the [OFDM Header Decoding Enabled](attra00028.html) property is set to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM Unequal Modulation Pattern Index |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01002.html language=enus -->
## TOPIC 00014: TXP:Maximum Measurement Interval (s)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01002.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum measurement interval. This value is expressed in seconds. When you set the TXP Burst Detection Enabled property to True, the measurement interval used is equal to the smaller of the duration of the WLAN packet under analysis or the value you set for this property. You do not ne

### TXP:Maximum Measurement Interval (s)

Specifies the maximum measurement interval. This value is expressed in seconds.

When you set the [TXP Burst Detection Enabled](attra01003.html) property to **True**, the measurement interval used is equal to the smaller of the duration of the WLAN packet under analysis or the value you set for this property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1 millisecond.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TXP Max Meas Interval (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01003.html language=enus -->
## TOPIC 00015: TXP:Burst Detection Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra01003.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement detects the start and the end of a WLAN packet automatically. When you set this property to True, the measurement interval used is equal to the smaller of the duration of the WLAN packet under analysis or the value you set for the TXP Max Meas Interval property. You

### TXP:Burst Detection Enabled

Specifies whether the measurement detects the start and the end of a WLAN packet automatically.

When you set this property to **True**, the measurement interval used is equal to the smaller of the duration of the WLAN packet under analysis or the value you set for the [TXP Max Meas Interval](attra01002.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TXP Burst Detection Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Disables burst detection. |
| --- | --- | --- |
| True | 1 | Enables burst detection. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra02014.html language=enus -->
## TOPIC 00016: PowerRamp:Averaging:Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra02014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra02014.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if averaging is enabled for PowerRamp measurements. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remark

### PowerRamp:Averaging:Enabled

Specifies if averaging is enabled for PowerRamp measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PowerRamp Averaging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The measurement uses the PowerRamp Averaging Count property as the number of acquisitions using which the results are averaged. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300a.html language=enus -->
## TOPIC 00017: DSSSModAcc:Measurement Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300a.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the DSSSModAcc measurement, which is a measurement of the modulation accuracy on signals conforming to the DSSS PHY defined in section 15 and the High Rate DSSS PHY defined in section 16 of IEEE Standard 802.11-2016. You do not need to use a selector string to configure o

### DSSSModAcc:Measurement Enabled

Specifies whether to enable the DSSSModAcc measurement, which is a measurement of the modulation accuracy on signals conforming to the DSSS PHY defined in section 15 and the High Rate DSSS PHY defined in section 16 of *IEEE Standard 802.11-2016*.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DSSSModAcc Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300b.html language=enus -->
## TOPIC 00018: DSSSModAcc:Acquisition Length Mode

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300b.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the s

### DSSSModAcc:Acquisition Length Mode

Specifies whether the measurement automatically computes the acquisition length of the waveform based on DSSSModAcc properties.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Auto**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DSSSModAcc Acquisition Length Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Manual | 0 | Uses the acquisition length specified by the DSSSModAcc Acquisition Length property. |
| --- | --- | --- |
| Auto | 1 | Computes the acquisition length based on the DSSSModAcc Meas Offset property and the DSSSModAcc Max Meas Length property. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300c.html language=enus -->
## TOPIC 00019: DSSSModAcc:Acquisition Length (s)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0300c.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the waveform to be acquired for the DSSSModAcc measurement when you set the DSSSModAcc Acquisition Length Mode property to Manual. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default signal instance.

### DSSSModAcc:Acquisition Length (s)

Specifies the length of the waveform to be acquired for the DSSSModAcc measurement when you set the [DSSSModAcc Acquisition Length Mode](/csh?topicname=attra0300b.html) property to **Manual**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1 millisecond.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DSSSModAcc Acquisition Length (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0400b.html language=enus -->
## TOPIC 00020: OFDMModAcc:Measurement Offset (symbols)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0400b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0400b.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of data symbols to be ignored from the start of the data field for EVM computation. This value is expressed in symbols. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for informatio

### OFDMModAcc:Measurement Offset (symbols)

Specifies the number of data symbols to be ignored from the start of the data field for EVM computation. This value is expressed in symbols.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Meas Offset (symbols) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401a.html language=enus -->
## TOPIC 00021: OFDMModAcc:Power:Custom Gate Stop Time (s)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401a.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the stop time of the custom power gate, and must be greater than the corresponding OFDMModAcc Pwr Custom Gate Start Time property. This value is expressed in seconds. Use "gate<n>" as the selector string to configure this property. The default value is 10 microseconds. Remarks The followin

### OFDMModAcc:Power:Custom Gate Stop Time (s)

Specifies the stop time of the custom power gate, and must be greater than the corresponding [OFDMModAcc Pwr Custom Gate Start Time](/csh?topicname=attra04019.html) property. This value is expressed in seconds.

Use "gate<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure this property.

The default value is 10 microseconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Pwr Custom Gate Stop Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401c.html language=enus -->
## TOPIC 00022: OFDMModAcc:I/Q Impairments:I/Q Gain Imbalance Correction Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401c.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable I/Q gain imbalance correction. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remarks T

### OFDMModAcc:I/Q Impairments:I/Q Gain Imbalance Correction Enabled

Specifies whether to enable I/Q gain imbalance correction.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc I/Q Gain Imbalance Correction Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | I/Q gain imbalance correction is disabled. |
| --- | --- | --- |
| True | 1 | I/Q gain imbalance correction is enabled. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401d.html language=enus -->
## TOPIC 00023: OFDMModAcc:I/Q Impairments:I/Q Quadrature Error Correction Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0401d.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable I/Q quadrature error correction. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remarks

### OFDMModAcc:I/Q Impairments:I/Q Quadrature Error Correction Enabled

Specifies whether to enable I/Q quadrature error correction.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc I/Q Quadrature Error Correction Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | I/Q quadrature error correction is disabled. |
| --- | --- | --- |
| True | 1 | I/Q quadrature error correction is enabled. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04023.html language=enus -->
## TOPIC 00024: OFDMModAcc:Results:Spectral Flatness Margin (dB)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04023.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04023.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spectral flatness margin, which is the minimum of the upper and lower spectral flatness margins. This value is expressed in dB. The upper spectral flatness margin is the minimum difference between the upper mask and the spectral flatness across subcarriers. The lower spectral flatness ma

### OFDMModAcc:Results:Spectral Flatness Margin (dB)

Returns the spectral flatness margin, which is the minimum of the upper and lower spectral flatness margins. This value is expressed in dB.

The upper spectral flatness margin is the minimum difference between the upper mask and the spectral flatness across subcarriers. The lower spectral flatness margin is the minimum difference between the spectral flatness and the lower mask across subcarriers. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, the spectral flatness is computed using the mean of the channel frequency response magnitude computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Spectral Flatness Margin (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04024.html language=enus -->
## TOPIC 00025: OFDMModAcc:Results:Spectral Flatness Margin Subcarrier Index

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04024.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04024.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the subcarrier index corresponding to the OFDMModAcc Results Spectral Flatness Margin result. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and

### OFDMModAcc:Results:Spectral Flatness Margin Subcarrier Index

Returns the subcarrier index corresponding to the [OFDMModAcc Results Spectral Flatness Margin](/csh?topicname=attra04023.html) result.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Spectral Flatness Margin Subcarrier Index |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04026.html language=enus -->
## TOPIC 00026: OFDMModAcc:Results:Unused Tone Error:Margin RU Index

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04026.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04026.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the 26-tone RU index corresponding to the OFDMModAcc Results Unused Tone Error Margin result. This result is applicable for 802.11ax, 802.11be and 802.11bn TB PPDU signals. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selec

### OFDMModAcc:Results:Unused Tone Error:Margin RU Index

Returns the 26-tone RU index corresponding to the [OFDMModAcc Results Unused Tone Error Margin](/csh?topicname=attra04025.html) result.

This result is applicable for 802.11ax, 802.11be and 802.11bn TB PPDU signals.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Unused Tone Error Margin RU Index |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0402e.html language=enus -->
## TOPIC 00027: OFDMModAcc:Results:I/Q Quadrature Error Mean (deg)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0402e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0402e.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q quadrature error, which is a measure of deviation of the phase difference between the quadrature-phase (Q) and the in-phase (I) component of the signal from 90 degrees. This value is expressed in degrees. When you set the OFDMModAcc Averaging Enabled property to True, this property r

### OFDMModAcc:Results:I/Q Quadrature Error Mean (deg)

Returns the I/Q quadrature error, which is a measure of deviation of the phase difference between the quadrature-phase (Q) and the in-phase (I) component of the signal from 90 degrees. This value is expressed in degrees.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the I/Q quadrature error results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results I/Q Quadrature Error Mean (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04033.html language=enus -->
## TOPIC 00028: OFDMModAcc:Results:PPDU Info:RU Size

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04033.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04033.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RU or the MRU size. This result is applicable for 802.11ax MU, extended range SU, and TB PPDU signals, 802.11be MU and TB PPDU signals, and 802.11bn MU and TB PPDU signals. For 802.11ax MU PPDU signals, this value is decoded from the HE-SIG-B field. For 802.11ax extended range SU PPDU si

### OFDMModAcc:Results:PPDU Info:RU Size

Returns the RU or the MRU size.

This result is applicable for 802.11ax MU, extended range SU, and TB PPDU signals, 802.11be MU and TB PPDU signals, and 802.11bn MU and TB PPDU signals. For 802.11ax MU PPDU signals, this value is decoded from the HE-SIG-B field. For 802.11ax extended range SU PPDU signals, this value is decoded from the HE-SIG-A field. For 802.11be MU PPDU signals, this value is decoded from the EHT-SIG field. For 802.11bn MU PPDU signals, this value is decoded from the UHR-SIG field. For 802.11ax, 802.11be or 802.11bn TB PPDU signals, this property returns the same value as the [OFDM RU Size](attra0001a.html) property.

Use "user<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results RU Size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| 26 | 26 | The RU size is 26. |
| --- | --- | --- |
| 52 | 52 | The RU size is 52. |
| 106 | 106 | The RU size is 106. |
| 242 | 242 | The RU size is 242. |
| 484 | 484 | The RU size is 484. |
| 996 | 996 | The RU size is 996. |
| 2x996 | 1992 | The RU size is 2 x 996. |
| 4x996 | 3984 | The RU size is 4 x 996. |
| 52+26 | 78 | The RU size is 52 + 26. |
| 106+26 | 132 | The RU size is 106 + 26. |
| 484+242 | 726 | The RU size is 484 + 242. |
| 996+484 | 1480 | The RU size is 996 + 484. |
| 996+484+242 | 1722 | The RU size is 996 + 484 + 242. |
| 2x996+484 | 2476 | The RU size is 2 x 996 + 484. |
| 3x996 | 2988 | The RU size is 3 x 996. |
| 3x996+484 | 3472 | The RU size is 3 x 996 + 484 |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04037.html language=enus -->
## TOPIC 00029: OFDMModAcc:Results:PPDU Info:Guard Interval Type

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04037.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04037.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size of the guard interval of OFDM symbols. This result is always 1/4 for 802.11a, 802.11j, and 802.11p signals. The value is decoded for various standards as follows: Standards Fields 802.11n The guard interval type is decoded from HT-SIG field. 802.11ac The guard interval type is decod

### OFDMModAcc:Results:PPDU Info:Guard Interval Type

Returns the size of the guard interval of OFDM symbols.

This result is always **1/4** for 802.11a, 802.11j, and 802.11p signals. The value is decoded for various standards as follows:

| Standards | Fields |
| --- | --- |
| 802.11n | The guard interval type is decoded from HT-SIG field. |
| 802.11ac | The guard interval type is decoded from VHT-SIG-A field. |
| 802.11ax | The guard interval type is decoded from HE-SIG-A field. |
| 802.11be | The guard interval type is decoded from EHT-SIG field. |
| 802.11bn | The guard interval type is decoded from UHR-SIG field. |

For 802.11ax, 802.11be, or 802.11bn TB PPDU signals, the property returns the same value as the [OFDM Guard Interval Type](attra0001c.html) property.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Guard Interval Type |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| 1/4 | 0 | The Guard interval is 1/4th of the IFFT duration. |
| --- | --- | --- |
| 1/8 | 1 | The Guard interval is 1/8th of the IFFT duration. |
| 1/16 | 2 | The Guard interval is 1/16th of the IFFT duration. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0403e.html language=enus -->
## TOPIC 00030: OFDMModAcc:Results:Power:L-SIG Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0403e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0403e.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the L-SIG or SIGNAL field. This value is expressed in dBm. This result is not applicable for 802.11n Greenfield PPDU signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the L-SIG or SIGNAL field average power results

### OFDMModAcc:Results:Power:L-SIG Average Power Mean (dBm)

Returns the average power of the L-SIG or SIGNAL field. This value is expressed in dBm.

This result is not applicable for 802.11n Greenfield PPDU signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the L-SIG or SIGNAL field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr L-SIG Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04042.html language=enus -->
## TOPIC 00031: OFDMModAcc:Results:Power:HT-SIG Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04042.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04042.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the HT-SIG field. This value is expressed in dBm. This result is applicable only to 802.11n signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the HT-SIG field average power results computed for each averaging count

### OFDMModAcc:Results:Power:HT-SIG Average Power Mean (dBm)

Returns the average power of the HT-SIG field. This value is expressed in dBm.

This result is applicable only to 802.11n signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the HT-SIG field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr HT-SIG Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04046.html language=enus -->
## TOPIC 00032: OFDMModAcc:Results:Power:HE-SIG-A Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04046.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04046.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the HE-SIG-A field. This value is expressed in dBm. This result is applicable only to 802.11ax signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the HE-SIG-A field average power results computed for each averaging

### OFDMModAcc:Results:Power:HE-SIG-A Average Power Mean (dBm)

Returns the average power of the HE-SIG-A field. This value is expressed in dBm.

This result is applicable only to 802.11ax signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the HE-SIG-A field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr HE-SIG-A Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404a.html language=enus -->
## TOPIC 00033: OFDMModAcc:Results:Power:HE-SIG-B Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404a.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the HE-SIG-B field. This value is expressed in dBm. This result is applicable only to 802.11ax signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the HE-SIG-B field average power results computed for each averaging

### OFDMModAcc:Results:Power:HE-SIG-B Average Power Mean (dBm)

Returns the average power of the HE-SIG-B field. This value is expressed in dBm.

This result is applicable only to 802.11ax signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the HE-SIG-B field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr HE-SIG-B Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404b.html language=enus -->
## TOPIC 00034: OFDMModAcc:Results:Power:HE-SIG-B Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404b.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the HE-SIG-B field. This value is expressed in dBm. This result is applicable only to 802.11ax signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the HE-SIG-B field peak power results computed for each averaging cou

### OFDMModAcc:Results:Power:HE-SIG-B Peak Power Maximum (dBm)

Returns the peak power of the HE-SIG-B field. This value is expressed in dBm.

This result is applicable only to 802.11ax signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the HE-SIG-B field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr HE-SIG-B Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404c.html language=enus -->
## TOPIC 00035: OFDMModAcc:Results:Power:HT-STF Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404c.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the HT-STF field. This value is expressed in dBm. This result is applicable only to 802.11n signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the HT-STF average power results computed for each averaging count. You

### OFDMModAcc:Results:Power:HT-STF Average Power Mean (dBm)

Returns the average power of the HT-STF field. This value is expressed in dBm.

This result is applicable only to 802.11n signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the HT-STF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr HT-STF Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404d.html language=enus -->
## TOPIC 00036: OFDMModAcc:Results:Power:HT-STF Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404d.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the HT-STF field. This value is expressed in dBm. This result is applicable only to 802.11n signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the HT-STF peak power results computed for each averaging count. You do

### OFDMModAcc:Results:Power:HT-STF Peak Power Maximum (dBm)

Returns the peak power of the HT-STF field. This value is expressed in dBm.

This result is applicable only to 802.11n signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the HT-STF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr HT-STF Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404e.html language=enus -->
## TOPIC 00037: OFDMModAcc:Results:Power:HT-GF-STF Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0404e.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the HT-GF-STF. This value is expressed in dBm. This result is applicable only to 802.11n greenfield PPDU signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the HT-GF-STF average power results computed for each avera

### OFDMModAcc:Results:Power:HT-GF-STF Average Power Mean (dBm)

Returns the average power of the HT-GF-STF. This value is expressed in dBm.

This result is applicable only to 802.11n greenfield PPDU signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the HT-GF-STF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr HT-GF-STF Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04051.html language=enus -->
## TOPIC 00038: OFDMModAcc:Results:Power:VHT-STF Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04051.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04051.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the VHT-STF field. This value is expressed in dBm. This result is applicable only to 802.11ac signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the VHT-STF peak power results computed for each averaging count. You

### OFDMModAcc:Results:Power:VHT-STF Peak Power Maximum (dBm)

Returns the peak power of the VHT-STF field. This value is expressed in dBm.

This result is applicable only to 802.11ac signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the VHT-STF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr VHT-STF Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04054.html language=enus -->
## TOPIC 00039: OFDMModAcc:Results:Power:HT-DLTF Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04054.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04054.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the HT-DLTF. This value is expressed in dBm. This result is applicable only to 802.11n signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the HT-DLTF average power results computed for each averaging count. You do n

### OFDMModAcc:Results:Power:HT-DLTF Average Power Mean (dBm)

Returns the average power of the HT-DLTF. This value is expressed in dBm.

This result is applicable only to 802.11n signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the HT-DLTF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr HT-DLTF Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04057.html language=enus -->
## TOPIC 00040: OFDMModAcc:Results:Power:HT-ELTF Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04057.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04057.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the HT-ELTF field. This value is expressed in dBm. This result is applicable only to 802.11n signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the HT-ELTF peak power results computed for each averaging count. You d

### OFDMModAcc:Results:Power:HT-ELTF Peak Power Maximum (dBm)

Returns the peak power of the HT-ELTF field. This value is expressed in dBm.

This result is applicable only to 802.11n signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the HT-ELTF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr HT-ELTF Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04059.html language=enus -->
## TOPIC 00041: OFDMModAcc:Results:Power:VHT-LTF Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04059.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04059.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the VHT-LTF field. This value is expressed in dBm. This result is applicable only to 802.11ac signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the VHT-LTF peak power results computed for each averaging count. You

### OFDMModAcc:Results:Power:VHT-LTF Peak Power Maximum (dBm)

Returns the peak power of the VHT-LTF field. This value is expressed in dBm.

This result is applicable only to 802.11ac signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the VHT-LTF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr VHT-LTF Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0405d.html language=enus -->
## TOPIC 00042: OFDMModAcc:Results:Power:Data Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0405d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0405d.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the data field. This value is expressed in dBm. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the data field peak power results computed for each averaging count. You do not need to use a selector string to read this re

### OFDMModAcc:Results:Power:Data Peak Power Maximum (dBm)

Returns the peak power of the data field. This value is expressed in dBm.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the data field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr Data Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04061.html language=enus -->
## TOPIC 00043: OFDMModAcc:Results:Power:PPDU Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04061.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04061.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the PPDU. This value is expressed in dBm. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the PPDU peak power results computed for each averaging count. You do not need to use a selector string to read this result for def

### OFDMModAcc:Results:Power:PPDU Peak Power Maximum (dBm)

Returns the peak power of the PPDU. This value is expressed in dBm.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the PPDU peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr PPDU Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0406f.html language=enus -->
## TOPIC 00044: OFDMModAcc:Results:Composite Data RMS EVM Mean (dB or %)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0406f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0406f.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS EVM of data-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of data RMS EVM results computed for each averaging count. You do not need to use a selector s

### OFDMModAcc:Results:Composite Data RMS EVM Mean (dB or %)

Returns the RMS EVM of data-subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of data RMS EVM results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Composite Data RMS EVM Mean |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408a.html language=enus -->
## TOPIC 00045: OFDMModAcc:Results:PPDU Info:SIG-B CRC Status

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408a.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the cyclic redundancy check (CRC) has passed for the HE-SIG-B field of the 802.11ax MU PPDU waveform. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string synt

### OFDMModAcc:Results:PPDU Info:SIG-B CRC Status

Returns whether the cyclic redundancy check (CRC) has passed for the HE-SIG-B field of the 802.11ax MU PPDU waveform.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results SIG-B CRC Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| Not Applicable | -1 | Returns that the SIG-B CRC is invalid for the current waveform. |
| --- | --- | --- |
| Fail | 0 | Returns that the SIG-B CRC failed. |
| Pass | 1 | Returns that the SIG-B CRC passed. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408b.html language=enus -->
## TOPIC 00046: OFDMModAcc:Data Decoding Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408b.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC). This further enables the check for the validity of SIG-B cyclic redundancy check (CRC) of the 802.11ac PPDU. Set the Maximum Measurement Length (symbols) property to -1 to decode all symbols. You d

### OFDMModAcc:Data Decoding Enabled

Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC).

This further enables the check for the validity of SIG-B cyclic redundancy check (CRC) of the 802.11ac PPDU.

Note

Maximum Measurement Length (symbols)

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Data Decoding Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Disables data decoding. |
| --- | --- | --- |
| True | 1 | Enables data decoding. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408c.html language=enus -->
## TOPIC 00047: OFDMModAcc:Results:PPDU Info:PSDU CRC Status

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408c.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed. The measurement calculates the CRC over the decoded bits, excluding the last 32 bits of each MAC Protocol Data Unit (MPDU). The measurement first compares this value with the CRC val

### OFDMModAcc:Results:PPDU Info:PSDU CRC Status

Indicates whether the cyclic redundancy check (CRC) of the received decoded PLCP service data unit (PSDU) has passed.

The measurement calculates the CRC over the decoded bits, excluding the last 32 bits of each MAC Protocol Data Unit (MPDU). The measurement first compares this value with the CRC value in the received payload, which is represented by the last 32 bits of the MPDU and then aggregates the values.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results PSDU CRC Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| Fail | 0 | Indicates that the PSDU CRC failed. |
| --- | --- | --- |
| Pass | 1 | Indicates that the PSDU CRC passed. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408d.html language=enus -->
## TOPIC 00048: OFDMModAcc:Channel Matrix Power Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0408d.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the channel frequency response matrix power measurements are enabled. This enables cross-power measurements for MIMO signals and user-power measurements for MU signals. You do not need to use a selector string to configure or read this property for the default signal instance. Refe

### OFDMModAcc:Channel Matrix Power Enabled

Specifies whether the channel frequency response matrix power measurements are enabled. This enables cross-power measurements for MIMO signals and user-power measurements for MU signals.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Ch Matrix Pwr Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Channel frequency response matrix power measurements are disabled. |
| --- | --- | --- |
| True | 1 | Channel frequency response matrix power measurements are enabled. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04092.html language=enus -->
## TOPIC 00049: OFDMModAcc:Results:PPDU Info:EHT-SIG CRC Status

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04092.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04092.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the cyclic redundancy check (CRC) has passed for the EHT-SIG field of the 802.11be waveform. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named sign

### OFDMModAcc:Results:PPDU Info:EHT-SIG CRC Status

Returns whether the cyclic redundancy check (CRC) has passed for the EHT-SIG field of the 802.11be waveform.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results EHT-SIG CRC Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| Not Applicable | -1 | Returns that the EHT-SIG CRC is invalid for the current waveform. |
| --- | --- | --- |
| Fail | 0 | Returns that the EHT-SIG CRC failed. |
| Pass | 1 | Returns that the EHT-SIG CRC passed. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04095.html language=enus -->
## TOPIC 00050: OFDMModAcc:Results:PPDU Info:PE Duration (s)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04095.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra04095.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the duration of the packet extension field for the 802.11ax, 802.11be and 802.11bn signals. This value is expressed in seconds. This result is applicable only when you set the OFDM Header Decoding Enabled property to True. You do not need to use a selector string to read this result for defa

### OFDMModAcc:Results:PPDU Info:PE Duration (s)

Returns the duration of the packet extension field for the 802.11ax, 802.11be and 802.11bn signals. This value is expressed in seconds.

This result is applicable only when you set the [OFDM Header Decoding Enabled](attra00028.html) property to **True**.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results PE Duration (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409a.html language=enus -->
## TOPIC 00051: OFDMModAcc:Results:User Stream RMS EVM Maximum (dB or %)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409a.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remarks The following table lists the characteristics of this property. Short Name OFDMModAcc Results User Stream RMS EVM Max Data type cdbl.png Permissions Read Only High-level VIs N/A Resettable No

### OFDMModAcc:Results:User Stream RMS EVM Maximum (dB or %)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results User Stream RMS EVM Max |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409b.html language=enus -->
## TOPIC 00052: OFDMModAcc:Results:User Stream RMS EVM Minimum (dB or %)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409b.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remarks The following table lists the characteristics of this property. Short Name OFDMModAcc Results User Stream RMS EVM Min Data type cdbl.png Permissions Read Only High-level VIs N/A Resettable No

### OFDMModAcc:Results:User Stream RMS EVM Minimum (dB or %)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results User Stream RMS EVM Min |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409e.html language=enus -->
## TOPIC 00053: OFDMModAcc:Results:Spectral Flatness Margin Maximum (dB)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0409e.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remarks The following table lists the characteristics of this property. Short Name OFDMModAcc Results Spectral Flatness Margin Max (dB) Data type cdbl.png Permissions Read Only High-level VIs N/A Resettable No

### OFDMModAcc:Results:Spectral Flatness Margin Maximum (dB)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Spectral Flatness Margin Max (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a0.html language=enus -->
## TOPIC 00054: OFDMModAcc:Results:Frequency Error Maximum (Hz)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a0.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remarks The following table lists the characteristics of this property. Short Name OFDMModAcc Results Freq Error Max (Hz) Data type cdbl.png Permissions Read Only High-level VIs N/A Resettable No

### OFDMModAcc:Results:Frequency Error Maximum (Hz)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Freq Error Max (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a3.html language=enus -->
## TOPIC 00055: OFDMModAcc:Results:Symbol Clock Error Minimum (ppm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040a3.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remarks The following table lists the characteristics of this property. Short Name OFDMModAcc Results Symbol Clock Error Min (ppm) Data type cdbl.png Permissions Read Only High-level VIs N/A Resettable No

### OFDMModAcc:Results:Symbol Clock Error Minimum (ppm)

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Symbol Clock Error Min (ppm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ad.html language=enus -->
## TOPIC 00056: OFDMModAcc:Averaging:Vector Averaging:Time Alignment Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ad.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable time alignment for the acquired I/Q data across multiple acquisitions. This property is considered only when you set the OFDMModAcc Averaging Enabled property to True, when you set the OFDMModAcc Averaging Count property to a value greater than 1, and when you set the OFD

### OFDMModAcc:Averaging:Vector Averaging:Time Alignment Enabled

Specifies whether to enable time alignment for the acquired I/Q data across multiple acquisitions.

This property is considered only when you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, when you set the [OFDMModAcc Averaging Count](attra04003.html) property to a value greater than 1, and when you set the [OFDMModAcc Averaging Type](attra040ac.html) property to **Vector**. You can set this property to **False** when there is no time offset between the acquired I/Q data of all averaging counts. Refer to the [Vector Averaging](/csh?context=rfmxwlan_rfmxwlan_ofdmmodacc_vector_averaging) concept topic for more information.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Vector Averaging Time Alignment Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Disables time alignment for the acquired I/Q data across multiple acquisitions. |
| --- | --- | --- |
| True | 1 | Enables time alignment for the acquired I/Q data across multiple acquisitions. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ae.html language=enus -->
## TOPIC 00057: OFDMModAcc:Averaging:Vector Averaging:Phase Alignment Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ae.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ae.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable phase alignment for the acquired I/Q data across multiple acquisitions. This property is considered only when you set the OFDMModAcc Averaging Enabled property to True, when you set the OFDMModAcc Averaging Count property to a value greater than 1, and when you set the OF

### OFDMModAcc:Averaging:Vector Averaging:Phase Alignment Enabled

Specifies whether to enable phase alignment for the acquired I/Q data across multiple acquisitions.

This property is considered only when you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, when you set the [OFDMModAcc Averaging Count](attra04003.html) property to a value greater than 1, and when you set the [OFDMModAcc Averaging Type](attra040ac.html) property to **Vector**. You can set this property to **False** when there is no phase offset between the acquired I/Q data of all averaging counts. Refer to the [Vector Averaging](/csh?context=rfmxwlan_rfmxwlan_ofdmmodacc_vector_averaging) concept topic for more information.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Vector Averaging Phase Alignment Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Disables phase alignment for the acquired I/Q data across multiple acquisitions. |
| --- | --- | --- |
| True | 1 | Enables phase alignment for the acquired I/Q data across multiple acquisitions. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ba.html language=enus -->
## TOPIC 00058: OFDMModAcc:Results:Phase Rotation:Coefficient 3

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ba.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040ba.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the phase rotation coefficient 3 as defined in IEEE Standard P802.11be/D7.0. This property returns detected value when you set the OFDM Auto Phase Rotation Detection Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal

### OFDMModAcc:Results:Phase Rotation:Coefficient 3

Specifies the phase rotation coefficient 3 as defined in *IEEE Standard P802.11be/D7.0*.

This property returns detected value when you set the [OFDM Auto Phase Rotation Detection Enabled](/csh?context=rfmxwlan_rfmxwlanprop_attra0003c) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Phase Rotation Coefficient 3 |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| +1 | 0 | Specifies that phase rotation coefficient 3 is +1. |
| --- | --- | --- |
| -1 | 1 | Specifies that phase rotation coefficient 3 is –1. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040bb.html language=enus -->
## TOPIC 00059: OFDMModAcc:Results:L-SIG RMS EVM Mean (dB or %)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040bb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040bb.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS EVM of subcarriers in the L-SIG symbol. This value is expressed as a percentage or in dB. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of RMS EVM results computed for each averaging count. You do not need to use a selector string to r

### OFDMModAcc:Results:L-SIG RMS EVM Mean (dB or %)

Returns the RMS EVM of subcarriers in the L-SIG symbol. This value is expressed as a percentage or in dB.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of RMS EVM results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results L-SIG RMS EVM Mean |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c6.html language=enus -->
## TOPIC 00060: OFDMModAcc:Results:Power:EHT-LTF Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c6.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the EHT-LTF field. This value is expressed in dBm. This result is applicable only to 802.11be signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the EHT-LTF average power results computed for each averaging count. Y

### OFDMModAcc:Results:Power:EHT-LTF Average Power Mean (dBm)

Returns the average power of the EHT-LTF field. This value is expressed in dBm.

This result is applicable only to 802.11be signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the EHT-LTF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr EHT-LTF Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c7.html language=enus -->
## TOPIC 00061: OFDMModAcc:Results:Power:EHT-LTF Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040c7.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the EHT-LTF field. This value is expressed in dBm. This result is applicable only to 802.11be signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the EHT-LTF peak power results computed for each averaging count. You

### OFDMModAcc:Results:Power:EHT-LTF Peak Power Maximum (dBm)

Returns the peak power of the EHT-LTF field. This value is expressed in dBm.

This result is applicable only to 802.11be signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the EHT-LTF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr EHT-LTF Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d2.html language=enus -->
## TOPIC 00062: OFDMModAcc:Results:UHR-SIG RMS EVM Mean (dB or %)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d2.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS EVM of subcarriers in the UHR-SIG symbol. This value is expressed as a percentage or in dB. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of RMS EVM results computed for each averaging count. You do not need to use a selector string to

### OFDMModAcc:Results:UHR-SIG RMS EVM Mean (dB or %)

Returns the RMS EVM of subcarriers in the UHR-SIG symbol. This value is expressed as a percentage or in dB.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of RMS EVM results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results UHR-SIG RMS EVM Mean |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d3.html language=enus -->
## TOPIC 00063: OFDMModAcc:Results:PPDU Info:UHR-SIG CRC Status

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d3.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the cyclic redundancy check (CRC) has passed for the UHR-SIG field of the 802.11bn waveform. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named sign

### OFDMModAcc:Results:PPDU Info:UHR-SIG CRC Status

Returns whether the cyclic redundancy check (CRC) has passed for the UHR-SIG field of the 802.11bn waveform.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results UHR-SIG CRC Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| Not Applicable | -1 | Returns that the UHR-SIG CRC is invalid for the current waveform. |
| --- | --- | --- |
| Fail | 0 | Returns that the UHR-SIG CRC failed. |
| Pass | 1 | Returns that the UHR-SIG CRC passed. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d4.html language=enus -->
## TOPIC 00064: OFDMModAcc:Results:ELR-SIG RMS EVM Mean (dB or %)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d4.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS EVM of subcarriers in the ELR-SIG symbol. This value is expressed as a percentage or in dB. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of RMS EVM results computed for each averaging count. You do not need to use a selector string to

### OFDMModAcc:Results:ELR-SIG RMS EVM Mean (dB or %)

Returns the RMS EVM of subcarriers in the ELR-SIG symbol. This value is expressed as a percentage or in dB.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of RMS EVM results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results ELR-SIG RMS EVM Mean |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d5.html language=enus -->
## TOPIC 00065: OFDMModAcc:Results:PPDU Info:ELR-SIG CRC Status

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d5.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the cyclic redundancy check (CRC) has passed for the ELR-SIG field of the 802.11bn waveform. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named sign

### OFDMModAcc:Results:PPDU Info:ELR-SIG CRC Status

Returns whether the cyclic redundancy check (CRC) has passed for the ELR-SIG field of the 802.11bn waveform.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results ELR-SIG CRC Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| Not Applicable | -1 | Returns that the ELR-SIG CRC is invalid for the current waveform. |
| --- | --- | --- |
| Fail | 0 | Returns that the ELR-SIG CRC failed. |
| Pass | 1 | Returns that the ELR-SIG CRC passed. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d6.html language=enus -->
## TOPIC 00066: OFDMModAcc:Results:Power:UHR-STF Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d6.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the UHR-STF field. This value is expressed in dBm. This result is applicable only to 802.11bn signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the UHR-STF average power results computed for each averaging count. Y

### OFDMModAcc:Results:Power:UHR-STF Average Power Mean (dBm)

Returns the average power of the UHR-STF field. This value is expressed in dBm.

This result is applicable only to 802.11bn signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the UHR-STF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr UHR-STF Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d7.html language=enus -->
## TOPIC 00067: OFDMModAcc:Results:Power:UHR-STF Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d7.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the UHR-STF field. This value is expressed in dBm. This result is applicable only to 802.11bn signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the UHR-STF peak power results computed for each averaging count. You

### OFDMModAcc:Results:Power:UHR-STF Peak Power Maximum (dBm)

Returns the peak power of the UHR-STF field. This value is expressed in dBm.

This result is applicable only to 802.11bn signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the UHR-STF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr UHR-STF Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d8.html language=enus -->
## TOPIC 00068: OFDMModAcc:Results:Power:UHR-LTF Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d8.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the UHR-LTF field. This value is expressed in dBm. This result is applicable only to 802.11bn signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the UHR-LTF average power results computed for each averaging count. Y

### OFDMModAcc:Results:Power:UHR-LTF Average Power Mean (dBm)

Returns the average power of the UHR-LTF field. This value is expressed in dBm.

This result is applicable only to 802.11bn signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the UHR-LTF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr UHR-LTF Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d9.html language=enus -->
## TOPIC 00069: OFDMModAcc:Results:Power:UHR-LTF Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040d9.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the UHR-LTF field. This value is expressed in dBm. This result is applicable only to 802.11bn signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the UHR-LTF peak power results computed for each averaging count. You

### OFDMModAcc:Results:Power:UHR-LTF Peak Power Maximum (dBm)

Returns the peak power of the UHR-LTF field. This value is expressed in dBm.

This result is applicable only to 802.11bn signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the UHR-LTF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr UHR-LTF Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040da.html language=enus -->
## TOPIC 00070: OFDMModAcc:Results:Power:UHR-SIG Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040da.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040da.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the UHR-SIG field. This value is expressed in dBm. This result is applicable only to 802.11bn signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the UHR-SIG field average power results computed for each averaging co

### OFDMModAcc:Results:Power:UHR-SIG Average Power Mean (dBm)

Returns the average power of the UHR-SIG field. This value is expressed in dBm.

This result is applicable only to 802.11bn signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the UHR-SIG field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr UHR-SIG Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040db.html language=enus -->
## TOPIC 00071: OFDMModAcc:Results:Power:UHR-SIG Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040db.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040db.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the UHR-SIG field. This value is expressed in dBm. This result is applicable only to 802.11bn signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the UHR-SIG field peak power results computed for each averaging count

### OFDMModAcc:Results:Power:UHR-SIG Peak Power Maximum (dBm)

Returns the peak power of the UHR-SIG field. This value is expressed in dBm.

This result is applicable only to 802.11bn signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the UHR-SIG field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr UHR-SIG Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040dc.html language=enus -->
## TOPIC 00072: OFDMModAcc:Results:Power:ELR-SIG Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040dc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040dc.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the ELR-SIG field. This value is expressed in dBm. This result is applicable only to 802.11bn signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the ELR-SIG field average power results computed for each averaging co

### OFDMModAcc:Results:Power:ELR-SIG Average Power Mean (dBm)

Returns the average power of the ELR-SIG field. This value is expressed in dBm.

This result is applicable only to 802.11bn signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the ELR-SIG field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr ELR-SIG Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040dd.html language=enus -->
## TOPIC 00073: OFDMModAcc:Results:Power:ELR-SIG Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040dd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040dd.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the ELR-SIG field. This value is expressed in dBm. This result is applicable only to 802.11bn signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the ELR-SIG field peak power results computed for each averaging count

### OFDMModAcc:Results:Power:ELR-SIG Peak Power Maximum (dBm)

Returns the peak power of the ELR-SIG field. This value is expressed in dBm.

This result is applicable only to 802.11bn signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the ELR-SIG field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr ELR-SIG Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040de.html language=enus -->
## TOPIC 00074: OFDMModAcc:Results:Power:ELR-MARK Average Power Mean (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040de.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040de.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the ELR-MARK field. This value is expressed in dBm. This result is applicable only to 802.11bn signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the ELR-MARK field average power results computed for each averaging

### OFDMModAcc:Results:Power:ELR-MARK Average Power Mean (dBm)

Returns the average power of the ELR-MARK field. This value is expressed in dBm.

This result is applicable only to 802.11bn signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the ELR-MARK field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr ELR-MARK Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040df.html language=enus -->
## TOPIC 00075: OFDMModAcc:Results:Power:ELR-MARK Peak Power Maximum (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040df.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040df.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power of the ELR-MARK field. This value is expressed in dBm. This result is applicable only to 802.11bn signals. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the ELR-MARK field peak power results computed for each averaging cou

### OFDMModAcc:Results:Power:ELR-MARK Peak Power Maximum (dBm)

Returns the peak power of the ELR-MARK field. This value is expressed in dBm.

This result is applicable only to 802.11bn signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the ELR-MARK field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Pwr ELR-MARK Pk Pwr Max (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e0.html language=enus -->
## TOPIC 00076: OFDMModAcc:Channel Estimation:LTF Averaging Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e0.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to average multiple Long Training Field (LTF) symbols to improve channel estimation. This property is only applicable for 11ax, 11be and 11bn standards. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selecto

### OFDMModAcc:Channel Estimation:LTF Averaging Enabled

Specifies whether to average multiple Long Training Field (LTF) symbols to improve channel estimation. This property is only applicable for 11ax, 11be and 11bn standards.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Ch Estimation LTF Averaging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Channel estimation with LTF averaging is disabled. |
| --- | --- | --- |
| True | 1 | Channel estimation with LTF averaging is enabled. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e1.html language=enus -->
## TOPIC 00077: OFDMModAcc:Results:PPDU Info:RU Type

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e1.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the type of RU for a user. This result is applicable for 802.11bn TB PPDU signals. For 802.11bn TB PPDU signals, this property returns the same value as the OFDM RU Type property. Use "user<n>" as the selector string to read this result. Remarks The following table lists the characteristics

### OFDMModAcc:Results:PPDU Info:RU Type

Returns the type of RU for a user.

This result is applicable for 802.11bn TB PPDU signals. For 802.11bn TB PPDU signals, this property returns the same value as the [OFDM RU Type](attra0003f.html) property.

Use "user<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results RU Type |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| rRU | 0 | The RU type is rRU. |
| --- | --- | --- |
| dRU | 1 | The RU type is dRU. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e2.html language=enus -->
## TOPIC 00078: OFDMModAcc:Results:PPDU Info:Distribution Bandwidth (Hz)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e2.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth across which RU Subcarriers are distributed for a user. This result is applicable for 802.11bn TB PPDU signals when RU Type is dRU. For 802.11bn TB PPDU signals, this property returns the same value as the OFDM RU Type property. Use "user<n>" as the selector string to read this

### OFDMModAcc:Results:PPDU Info:Distribution Bandwidth (Hz)

Returns the bandwidth across which RU Subcarriers are distributed for a user.

This result is applicable for 802.11bn TB PPDU signals when RU Type is dRU. For 802.11bn TB PPDU signals, this property returns the same value as the [OFDM RU Type](attra00040.html) property.

Use "user<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results DBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| 20M | 20000000 | DBW is 20 MHz. |
| --- | --- | --- |
| 40M | 40000000 | DBW is 40 MHz. |
| 60M | 60000000 | DBW is 60 MHz. |
| 80M | 80000000 | DBW is 80 MHz. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e3.html language=enus -->
## TOPIC 00079: OFDMModAcc:Results:PPDU Info:2xLDPC Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e3.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether 2xLDPC is enabled for a specified user. Use "user<n>" as the selector string to read this result for 802.11bn MU and TB PPDU signals. Remarks The following table lists the characteristics of this property. Short Name OFDMModAcc Results 2xLDPC Enabled Data type ci32.png Permissions Re

### OFDMModAcc:Results:PPDU Info:2xLDPC Enabled

Returns whether 2xLDPC is enabled for a specified user.

Use "user<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for 802.11bn MU and TB PPDU signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results 2xLDPC Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Indicates that 2xLDPC is disabled for the specified user. |
| --- | --- | --- |
| True | 1 | Indicates that 2xLDPC is enabled for the specified user. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e4.html language=enus -->
## TOPIC 00080: OFDMModAcc:Results:PPDU Info:IM Pilots Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e4.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether interference mitigating pilots are present. This result is applicable only to 802.11bn MU PPDU signals. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for

### OFDMModAcc:Results:PPDU Info:IM Pilots Enabled

Returns whether interference mitigating pilots are present.

This result is applicable only to 802.11bn MU PPDU signals.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results IM Pilots Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Indicates that interference mitigating pilots are absent. |
| --- | --- | --- |
| True | 1 | Indicates that interference mitigating pilots are present. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e5.html language=enus -->
## TOPIC 00081: OFDMModAcc:Results:PPDU Info:Unequal Modulation:Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e5.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether unequal modulation is enabled for a specified user. Use "user<n>" as the selector string to read this result for 802.11bn MU PPDU signals. Remarks The following table lists the characteristics of this property. Short Name OFDMModAcc Results Unequal Modulation Enabled Data type ci32.p

### OFDMModAcc:Results:PPDU Info:Unequal Modulation:Enabled

Returns whether unequal modulation is enabled for a specified user.

Use "user<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for 802.11bn MU PPDU signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Unequal Modulation Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Indicates that unequal modulation is disabled for the specified user. |
| --- | --- | --- |
| True | 1 | Indicates that unequal modulation is enabled for the specified user. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e6.html language=enus -->
## TOPIC 00082: OFDMModAcc:Results:PPDU Info:Unequal Modulation:Pattern Index

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e6.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns unequal modulation pattern for a specified user. Use "user<n>" as the selector string to read this result for 802.11bn MU PPDU signals. Remarks The following table lists the characteristics of this property. Short Name OFDMModAcc Results Unequal Modulation Pattern Index Data type ci32.png Pe

### OFDMModAcc:Results:PPDU Info:Unequal Modulation:Pattern Index

Returns unequal modulation pattern for a specified user.

Use "user<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for 802.11bn MU PPDU signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Unequal Modulation Pattern Index |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e7.html language=enus -->
## TOPIC 00083: OFDMModAcc:Results:PPDU Info:Number of SIG Symbols

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra040e7.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remarks The following table lists the characteristics of this property. Short Name OFDMModAcc Results Num SIG Symbols Data type ci32.png Permissions Read Only High-level VIs N/A Resettable No

### OFDMModAcc:Results:PPDU Info:Number of SIG Symbols

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDMModAcc Results Num SIG Symbols |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05000.html language=enus -->
## TOPIC 00084: SEM:Measurement Enabled

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05000.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the spectral emission mask (SEM) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is F

### SEM:Measurement Enabled

Specifies whether to enable the spectral emission mask (SEM) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05005.html language=enus -->
## TOPIC 00085: SEM:Carrier:Integration Bandwidth (Hz)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05005.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the integration bandwidth of the carrier as per the standard and channel bandwidth. This value is expressed in Hz. You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for n

### SEM:Carrier:Integration Bandwidth (Hz)

Returns the integration bandwidth of the carrier as per the standard and channel bandwidth. This value is expressed in Hz.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 18 M.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Carrier IBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05006.html language=enus -->
## TOPIC 00086: SEM:Offset:Number of Offsets

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05006.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of offset segments for the SEM measurement when you set the SEM Mask Type property to Custom. You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named sig

### SEM:Offset:Number of Offsets

Specifies the number of offset segments for the SEM measurement when you set the [SEM Mask Type](/csh?topicname=attra05002.html) property to **Custom**.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Num Offsets |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05008.html language=enus -->
## TOPIC 00087: SEM:Offset:Stop Frequency (Hz)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05008.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05008.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz. Use "offset<n>" as the selector string to configure this property. The default value is 11 MHz. Remarks The following table lists the characteristics of this property. Short Name SEM Offs

### SEM:Offset:Stop Frequency (Hz)

Specifies the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz.

Use "offset<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure this property.

The default value is 11 MHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset Stop Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500a.html language=enus -->
## TOPIC 00088: SEM:Offset:Relative Limit:Start (dB)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500a.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the relative power limit corresponding to the start of the offset segment. This value is expressed in dB. Use "offset<n>" as the selector string to configure this property. The default value is 0. Remarks The following table lists the characteristics of this property. Short Name SEM Offset

### SEM:Offset:Relative Limit:Start (dB)

Specifies the relative power limit corresponding to the start of the offset segment. This value is expressed in dB.

Use "offset<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset Rel Limit Start (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500b.html language=enus -->
## TOPIC 00089: SEM:Offset:Relative Limit:Stop (dB)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500b.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. Use "offset<n>" as the selector string to configure this property. The default value is -20. Remarks The following table lists the characteristics of this property. Short Name SEM Offset

### SEM:Offset:Relative Limit:Stop (dB)

Specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB.

Use "offset<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure this property.

The default value is -20.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset Rel Limit Stop (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500c.html language=enus -->
## TOPIC 00090: SEM:Span:Auto

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0500c.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the frequency range of the spectrum used for SEM measurement is computed automatically by the measurement or is configured by you. This property is applicable when you set the SEM Mask Type property to Standard. You do not need to use a selector string to read this property for the

### SEM:Span:Auto

Specifies whether the frequency range of the spectrum used for SEM measurement is computed automatically by the measurement or is configured by you.

This property is applicable when you set the [SEM Mask Type](attra05002.html)
 property to **Standard**.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Span Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The span you configure is used as the frequency range for the SEM measurement. |
| --- | --- | --- |
| True | 1 | The span is automatically computed based on the configured standard and channel bandwidth. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05016.html language=enus -->
## TOPIC 00091: SEM:Amplitude Correction Type

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05016.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table VI to configure the external attenuation table. You do not nee

### SEM:Amplitude Correction Type

Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_configure_external_attenuation_table) VI to configure the external attenuation table.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Amplitude Correction Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| RF Center Frequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| --- | --- | --- |
| Spectrum Frequency Bin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0501b.html language=enus -->
## TOPIC 00092: SEM:Results:Measurement Status

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0501b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0501b.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the overall measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information abou

### SEM:Results:Measurement Status

Returns the overall measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Meas Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| Fail | 0 | The spectrum exceeds the SEM measurement mask limits for at least one of the offset segments. |
| --- | --- | --- |
| Pass | 1 | The spectrum does not exceed the SEM measurement mask limits for any offset segment. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05023.html language=enus -->
## TOPIC 00093: SEM:Results:Lower Offset:Relative Integrated Power (dB)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05023.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05023.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Result

### SEM:Results:Lower Offset:Relative Integrated Power (dB)

Returns the average power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB.

Use "offset<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Rel Integrated Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0502b.html language=enus -->
## TOPIC 00094: SEM:Results:Upper Offset:Measurement Status

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0502b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0502b.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the upper offset (positive) segment measurement status indicating if the spectrum exceeds the SEM measurement mask limits in the upper offset segment. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Nam

### SEM:Results:Upper Offset:Measurement Status

Returns the upper offset (positive) segment measurement status indicating if the spectrum exceeds the SEM measurement mask limits in the upper offset segment.

Use "offset<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Meas Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| Fail | 0 | The spectrum exceeds the SEM measurement mask and limits for the upper offset segment. |
| --- | --- | --- |
| Pass | 1 | The spectrum does not exceed the SEM measurement mask and limits for the upper offset segment. |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05031.html language=enus -->
## TOPIC 00095: SEM:Results:Upper Offset:Margin (dB)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05031.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05031.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the margin from the SEM measurement mask for the offset (positive). This value is expressed in dB. Margin is computed as Margin(dB) = Max(Spectrum[] - Mask[]) Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. S

### SEM:Results:Upper Offset:Margin (dB)

Returns the margin from the SEM measurement mask for the offset (positive). This value is expressed in dB.

Margin is computed as

Margin(dB) = Max(Spectrum[] - Mask[])

Use "offset<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Margin (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05032.html language=enus -->
## TOPIC 00096: SEM:Results:Upper Offset:Margin Absolute Power (dBm)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05032.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05032.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power level of the spectrum corresponding to the result of the SEM Results Upper Offset Margin property. This value is expressed in dBm. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Resu

### SEM:Results:Upper Offset:Margin Absolute Power (dBm)

Returns the power level of the spectrum corresponding to the result of the [SEM Results Upper Offset Margin](/csh?topicname=attra05031.html) property. This value is expressed in dBm.

Use "offset<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Margin Abs Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05033.html language=enus -->
## TOPIC 00097: SEM:Results:Upper Offset:Margin Relative Power (dB)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05033.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05033.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power level of the spectrum corresponding to the result of the SEM Results Upper Offset Margin property. This value is expressed in dB. The power level is returned relative to the peak power of the carrier channel. Use "offset<n>" as the selector string to read this result. Remarks The f

### SEM:Results:Upper Offset:Margin Relative Power (dB)

Returns the power level of the spectrum corresponding to the result of the [SEM Results Upper Offset Margin](/csh?topicname=attra05031.html) property. This value is expressed in dB.

The power level is returned relative to the peak power of the carrier channel.

Use "offset<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Margin Rel Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05034.html language=enus -->
## TOPIC 00098: SEM:Results:Upper Offset:Margin Frequency (Hz)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05034.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra05034.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency of the spectrum corresponding to the result of the SEM Results Upper Offset Margin property. This value is expressed in Hz. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results

### SEM:Results:Upper Offset:Margin Frequency (Hz)

Returns the frequency of the spectrum corresponding to the result of the [SEM Results Upper Offset Margin](/csh?topicname=attra05031.html) property. This value is expressed in Hz.

Use "offset<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Margin Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0c000.html language=enus -->
## TOPIC 00099: Result Fetch Timeout (s)

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0c000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwlan-rc/rfmxwlan/attra0c000.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time, in seconds, to wait before results are available in the RFmxWLAN Property Node. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxWLAN Property Node waits until the measurement is complete. You do not need to use a se

### Result Fetch Timeout (s)

Specifies the time, in seconds, to wait before results are available in the [RFmxWLAN Property Node](/csh?context=rfmxwlan_rfmxwlanvi_rfmxwlan_property_node). Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxWLAN Property Node waits until the measurement is complete.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Result Fetch Timeout (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWLAN Properties

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-abort-measurements-vi.html language=enus -->
## TOPIC 00100: RFmxWLAN Abort Measurements VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-abort-measurements-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-abort-measurements-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxWLAN Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI

### RFmxWLAN Abort Measurements VI

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxWLAN Initiate](/csh?topicname=rfmxwlan-initiate-vi.html) VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='icon' src='rfmxwlan-abort-measurements-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-analyze-iq-1-wfm-vi.html language=enus -->
## TOPIC 00101: RFmxWLAN Analyze (IQ, 1 Wfm) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-analyze-iq-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-analyze-iq-1-wfm-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended

### RFmxWLAN Analyze (IQ, 1 Wfm) VI

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **IQ** or **IQ or Spectral**.

When using the Analysis-Only mode in RFmxWLAN, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

Note

RFmxInstr Property Node

RFmx WLAN Commit

[IMAGE alt='icon' src='rfmxwlan-analyze-iq-1-wfm-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. IQ — IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 — x0 specifies the start time of the input y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start time of the input y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

RFmxWLAN Analyze2 VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-analyze-n-wfms-iq-vi.html language=enus -->
## TOPIC 00102: RFmxWLAN Analyze N Wfms (IQ) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-analyze-n-wfms-iq-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-analyze-n-wfms-iq-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform(s) that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommen

### RFmxWLAN Analyze N Wfms (IQ) VI

Performs the enabled measurements on the I/Q complex waveform(s) that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **IQ** or **IQ or Spectral**.

When using the Analysis-Only mode in RFmxWLAN, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

Note

RFmxInstr Property Node

RFmx WLAN Commit

[IMAGE alt='icon' src='rfmxwlan-analyze-n-wfms-iq-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. IQ — IQ specifies the waveform array where each element contains data for a complex waveform including start, delta, and actual values. x0 — x0 specifies the start time of the input y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start time of the input y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

RFmxWLAN Analyze2 VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-analyze-n-wfms-spectrum-vi.html language=enus -->
## TOPIC 00103: RFmxWLAN Analyze N Wfms (Spectrum) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-analyze-n-wfms-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-analyze-n-wfms-spectrum-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum(s) that you specify in the Spectrum parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommende

### RFmxWLAN Analyze N Wfms (Spectrum) VI

Performs the enabled measurements on the spectrum(s) that you specify in the **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **Spectral** or **IQ or Spectral**.

Note

RFmxInstr Property Node

RFmxWLAN Commit

[IMAGE alt='icon' src='rfmxwlan-analyze-n-wfms-spectrum-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Spectrum — Spectrum specifies the waveform array where each element contains data for a spectrum waveform including start, delta, and actual values. x0 — x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx — dx specifies the frequency interval between data points in the spectrum. y — y specifies the array of real-value power spectrum. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx — dx specifies the frequency interval between data points in the spectrum. y — y specifies the array of real-value power spectrum. |

Parent topic:

RFmxWLAN Analyze2 VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-analyze-spectrum-1-wfm-vi.html language=enus -->
## TOPIC 00104: RFmxWLAN Analyze (Spectrum, 1 Wfm) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-analyze-spectrum-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-analyze-spectrum-1-wfm-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum that you specify in the Spectrum parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended A

### RFmxWLAN Analyze (Spectrum, 1 Wfm) VI

Performs the enabled measurements on the spectrum that you specify in the **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **Spectral** or **IQ or Spectral**.

Note

RFmxInstr Property Node

RFmxWLAN Commit

[IMAGE alt='icon' src='rfmxwlan-analyze-spectrum-1-wfm-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Spectrum — Spectrum specifies the data for a spectrum waveform including the start, delta, and actual values. x0 — x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx — dx specifies the frequency interval between data points in the spectrum. y — y specifies the array of real-value power spectrum. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx — dx specifies the frequency interval between data points in the spectrum. y — y specifies the array of real-value power spectrum. |

Parent topic:

RFmxWLAN Analyze2 VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-auto-detect-signal-analysisonly-vi.html language=enus -->
## TOPIC 00105: RFmxWLAN Auto Detect Signal (AnalysisOnly) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-auto-detect-signal-analysisonly-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-auto-detect-signal-analysisonly-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automatically detects the standard, channel bandwidth, and burst length on the I/Q complex waveform that you specify in IQ parameter, and writes the Detected Standard, Detected Channel Bandwidth, and Detected Burst Length properties. icon Inputs/Outputs cstr.png Selector String Selector String speci

### RFmxWLAN Auto Detect Signal (AnalysisOnly) VI

Automatically detects the standard, channel bandwidth, and burst length on the I/Q complex waveform that you specify in **IQ** parameter, and writes the [Detected Standard](/csh?context=rfmxwlan_rfmxwlanprop_attra00011), [Detected Channel Bandwidth](/csh?context=rfmxwlan_rfmxwlanprop_attra00012), and [Detected Burst Length](/csh?context=rfmxwlan_rfmxwlanprop_attra00013) properties.

[IMAGE alt='icon' src='rfmxwlan-auto-detect-signal-analysisonly-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. IQ — IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 — x0 specifies the start time of the input y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start time of the input y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-auto-detect-signal-vi.html language=enus -->
## TOPIC 00106: RFmxWLAN Auto Detect Signal VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-auto-detect-signal-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-auto-detect-signal-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automatically detects the standard, channel bandwidth, and burst length of the input signal, and writes the Detected Standard, Detected Channel Bandwidth, and Detected Burst Length properties. You must configure the Reference Level property before calling this VI. If the peak power level of the inpu

### RFmxWLAN Auto Detect Signal VI

Automatically detects the standard, channel bandwidth, and burst length of the input signal, and writes the [Detected Standard](/csh?context=rfmxwlan_rfmxwlanprop_attra00011), [Detected Channel Bandwidth](/csh?context=rfmxwlan_rfmxwlanprop_attra00012), and [Detected Burst Length](/csh?context=rfmxwlan_rfmxwlanprop_attra00013) properties.

You must configure the [Reference Level](/csh?context=rfmxwlan_rfmxwlanprop_attra00002) property before calling this VI. If the peak power level of the input is unknown, you can call the [RFmxWLAN Auto Level](/csh?context=rfmxwlan_rfmxwlanvi_rfmxwlan_auto_level) VI to configure the Reference Level property after you set the [Standard](/csh?context=rfmxwlan_rfmxwlanprop_attra0000d) and [Channel Bandwidth](/csh?context=rfmxwlan_rfmxwlanprop_attra0000e) properties to values corresponding to maximum expected channel bandwidth.

[IMAGE alt='icon' src='rfmxwlan-auto-detect-signal-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-auto-level-vi.html language=enus -->
## TOPIC 00107: RFmxWLAN Auto Level VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-auto-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-auto-level-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level. The RFmxWLAN Auto Level VI does the following: Resets the mixer level, mixer level offset and IF output

### RFmxWLAN Auto Level VI

Examines the input signal to calculate the peak power level and sets it as the value of the [Reference Level](/csh?context=rfmxwlan_rfmxwlanprop_attra00002) property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxWLAN Auto Level VI does the following:

1. Resets the mixer level, mixer level offset and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation and preamp enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after completing execution.

You can also specify the starting reference level using the [Auto Level Initial Ref Level](/csh?context=rfmxwlan_rfmxwlanprop_attra00024) property.

When using NI-PXie 5663, NI-PXie 5665, or NI-PXie 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxWLAN Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this VI, thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='icon' src='rfmxwlan-auto-level-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Measurement Interval (s) — Measurement Interval specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-build-chain-string-vi.html language=enus -->
## TOPIC 00108: RFmxWLAN Build Chain String VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-build-chain-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-build-chain-string-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a chain string. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. You can also pass Selector String Out from the

### RFmxWLAN Build Chain String VI

Creates a chain string.

[IMAGE alt='icon' src='rfmxwlan-build-chain-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. You can also pass Selector String Out from the RFmxWLAN Build Segment String VI as an input to this VI. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxWLAN Build Segment String VI to build the selector string. Chain Number — Chain Number specifies the chain number for building the selector string. Selector String Out — Selector String Out returns the selector string created by this VI. |
| --- |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-build-gate-string-vi.html language=enus -->
## TOPIC 00109: RFmxWLAN Build Gate String VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-build-gate-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-build-gate-string-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the gate string to use as the selector string. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result

### RFmxWLAN Build Gate String VI

Creates the gate string to use as the selector string.

[IMAGE alt='icon' src='rfmxwlan-build-gate-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Gate Number — Gate Number specifies the gate number for building the selector string. Selector String Out — Selector String Out returns the selector string created by this VI. |
| --- |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-clear-all-named-results-vi.html language=enus -->
## TOPIC 00110: RFmxWLAN Clear All Named Results VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-clear-all-named-results-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-clear-all-named-results-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value i

### RFmxWLAN Clear All Named Results VI

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxwlan-clear-all-named-results-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-clear-named-result-vi.html language=enus -->
## TOPIC 00111: RFmxWLAN Clear Named Result VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-clear-named-result-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-clear-named-result-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result

### RFmxWLAN Clear Named Result VI

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxwlan-clear-named-result-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-clone-signal-configuration-vi.html language=enus -->
## TOPIC 00112: RFmxWLAN Clone Signal Configuration VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-clone-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-clone-signal-configuration-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the property values from an existing signal instance. icon Inputs/Outputs cstr.png Old Signal Name Old Signal Name specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signa

### RFmxWLAN Clone Signal Configuration VI

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='icon' src='rfmxwlan-clone-signal-configuration-vi.png']

#### Inputs/Outputs

| Old Signal Name — Old Signal Name specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. New Signal Name — New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-configure-selected-ports-vi.html language=enus -->
## TOPIC 00113: RFmxWLAN Configure Selected Ports VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-configure-selected-ports-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-configure-selected-ports-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the instrument port to acquire a signal. Use the RFmxInstr Get Available Ports VI to get the valid port names. icon

### RFmxWLAN Configure Selected Ports VI

Configures the instrument port to acquire a signal. Use the [RFmxInstr Get Available Ports](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_get_available_ports) VI to get the valid port names.

[IMAGE alt='icon' src='rfmxwlan-configure-selected-ports-vi.png']

- [RFmxWLAN Configure Selected Ports (Single) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-configure-selected-ports-single-vi.html) Configures the selected ports.
- [RFmxWLAN Configure Selected Ports (Multiple) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-configure-selected-ports-multiple-vi.html) Configures the selected ports to each segment/chain based on the values you set in Num Freq Segments and Num Rx Chains properties.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-create-signal-configuration-vi.html language=enus -->
## TOPIC 00114: RFmxWLAN Create Signal Configuration VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-create-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-create-signal-configuration-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. icon Inputs/Outputs cstr.png Signal Name Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" cgenclassrntag.png Instrument Handle In Instrument Handle In specifies

### RFmxWLAN Create Signal Configuration VI

Creates a new instance of a signal.

[IMAGE alt='icon' src='rfmxwlan-create-signal-configuration-vi.png']

#### Inputs/Outputs

| Signal Name — Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-delete-signal-configuration-vi.html language=enus -->
## TOPIC 00115: RFmxWLAN Delete Signal Configuration VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-delete-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-delete-signal-configuration-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal that you specify in the Signal Name parameter. icon Inputs/Outputs cstr.png Signal Name Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" cgenclassrntag.png Instrume

### RFmxWLAN Delete Signal Configuration VI

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='icon' src='rfmxwlan-delete-signal-configuration-vi.png']

#### Inputs/Outputs

| Signal Name — Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::s1" "sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-disable-trigger-vi.html language=enus -->
## TOPIC 00116: RFmxWLAN Disable Trigger VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-disable-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-disable-trigger-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name

### RFmxWLAN Disable Trigger VI

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='icon' src='rfmxwlan-disable-trigger-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN Configure Trigger VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-dsssmodacc-configure-evm-unit-vi.html language=enus -->
## TOPIC 00117: RFmxWLAN DSSSModAcc Configure EVM Unit VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-dsssmodacc-configure-evm-unit-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-dsssmodacc-configure-evm-unit-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures EVM unit for the measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::si

### RFmxWLAN DSSSModAcc Configure EVM Unit VI

Configures EVM unit for the measurement.

[IMAGE alt='icon' src='rfmxwlan-dsssmodacc-configure-evm-unit-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. EVM Unit — EVM Unit specifies the unit for the EVM results. The default value is Percentage. dB (0) EVM results are returned in dB. Percentage (1) EVM results are returned as a percentage. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| dB (0) | EVM results are returned in dB. |
| Percentage (1) | EVM results are returned as a percentage. |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-dsssmodacc-configure-power-measurement-enabled-vi.html language=enus -->
## TOPIC 00118: RFmxWLAN DSSSModAcc Configure Power Measurement Enabled VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-dsssmodacc-configure-power-measurement-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-dsssmodacc-configure-power-measurement-enabled-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether power measurement is enabled for the DSSSModAcc measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is ""

### RFmxWLAN DSSSModAcc Configure Power Measurement Enabled VI

Configures whether power measurement is enabled for the DSSSModAcc measurement.

[IMAGE alt='icon' src='rfmxwlan-dsssmodacc-configure-power-measurement-enabled-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Power Measurement Enabled — Power Measurement Enabled specifies if power measurement is performed. This parameter computes power of various fields in the PPDU. Additionally, this measurement computes power over the custom gates that you can configure using the DSSSModAcc Pwr Num Custom Gates, the DSSSModAcc Pwr Custom Gate Start Time and the DSSSModAcc Pwr Custom Gate Stop Time properties. The default value is False. False (0) Disables power measurement. True (1) Enables power measurement. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Disables power measurement. |
| True (1) | Enables power measurement. |

Parent topic:

DSSSModAcc

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-dsssmodacc-fetch-decoded-psdu-bits-trace-vi.html language=enus -->
## TOPIC 00119: RFmxWLAN DSSSModAcc Fetch Decoded PSDU Bits Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-dsssmodacc-fetch-decoded-psdu-bits-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-dsssmodacc-fetch-decoded-psdu-bits-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded PLCP service data unit (PSDU) bits. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result

### RFmxWLAN DSSSModAcc Fetch Decoded PSDU Bits Trace VI

Fetches the decoded PLCP service data unit (PSDU) bits.

[IMAGE alt='icon' src='rfmxwlan-dsssmodacc-fetch-decoded-psdu-bits-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Decoded PSDU Bits — Decoded PSDU Bits returns an array of PSDU bits obtained after demodulation and decoding. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN DSSSModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-configure-phase-tracking-enabled-vi.html language=enus -->
## TOPIC 00120: RFmxWLAN OFDMModAcc Configure Phase Tracking Enabled VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-configure-phase-tracking-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-configure-phase-tracking-enabled-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to enable pilot-based common phase error correction per OFDM data symbol. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default

### RFmxWLAN OFDMModAcc Configure Phase Tracking Enabled VI

Configures whether to enable pilot-based common phase error correction per OFDM data symbol.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-configure-phase-tracking-enabled-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Phase Tracking Enabled — Phase Tracking Enabled specifies whether to enable pilot-based common phase error correction per OFDM data symbol. Phase tracking is useful for tracking the phase variation over the modulation symbol caused by the residual frequency offset and phase noise. The default value is True. False (0) Phase tracking is disabled. True (1) Phase tracking is enabled. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Phase tracking is disabled. |
| True (1) | Phase tracking is enabled. |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-common-pilot-error-trace-vi.html language=enus -->
## TOPIC 00121: RFmxWLAN OFDMModAcc Fetch Common Pilot Error Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-common-pilot-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-common-pilot-error-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the common pilot error magnitude and phase traces. Use "segment<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not spec

### RFmxWLAN OFDMModAcc Fetch Common Pilot Error Trace VI

Fetches the common pilot error magnitude and phase traces.

Use "segment<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-common-pilot-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxWLAN Build Segment String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Common Pilot Error Magnitude — Common Pilot Error Magnitude returns the common pilot error magnitude trace. Common pilot error for an OFDM symbol is the correlation of the received pilot subcarrier BPSK symbols with their ideal values. This trace represents the magnitude of the common pilot error for each OFDM symbol. x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns an array of magnitude of the common pilot error for each OFDM symbol. Common Pilot Error Phase (deg) — Common Pilot Error Phase returns the common pilot error phase trace. Common pilot error for an OFDM symbol is the correlation of the received pilot subcarrier BPSK symbols with their ideal values. This trace represents the phase of the common pilot error for each OFDM symbol. x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns an array of phase of the common pilot error for each OFDM symbol. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns an array of magnitude of the common pilot error for each OFDM symbol. |
| x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns an array of phase of the common pilot error for each OFDM symbol. This value is expressed in degrees. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-composite-rms-evm-vi.html language=enus -->
## TOPIC 00122: RFmxWLAN OFDMModAcc Fetch Composite RMS EVM VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-composite-rms-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-composite-rms-evm-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the composite RMS EVM results. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the defaul

### RFmxWLAN OFDMModAcc Fetch Composite RMS EVM VI

Fetches the composite RMS EVM results.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-composite-rms-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Composite RMS EVM Mean (dB or %) — Composite RMS EVM Mean returns the RMS EVM of all subcarriers in all OFDM symbols. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the composite RMS EVM results computed for each averaging count. Composite Data RMS EVM Mean (dB or %) — Composite Data RMS EVM Mean returns the RMS EVM of data-subcarriers in all OFDM symbols. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the composite data RMS EVM results computed for each averaging count. Composite Pilot RMS EVM Mean (dB or %) — Composite Pilot RMS EVM Mean returns the RMS EVM of pilot-subcarriers in all OFDM symbols. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the composite pilot RMS EVM results computed for each averaging count. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-cross-power-vi.html language=enus -->
## TOPIC 00123: RFmxWLAN OFDMModAcc Fetch Cross Power VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-cross-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-cross-power-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the cross power. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the sig

### RFmxWLAN OFDMModAcc Fetch Cross Power VI

Fetches the cross power.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-cross-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Cross Power Mean (dB) — Cross Power Mean returns the cross power. The cross power for chain x is the power contribution from streams other than stream x in the chain. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the cross power results computed for each averaging count. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-data-constellation-trace-vi.html language=enus -->
## TOPIC 00124: RFmxWLAN OFDMModAcc Fetch Data Constellation Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-data-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-data-constellation-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace for the data-subcarriers. Use "segment<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream nu

### RFmxWLAN OFDMModAcc Fetch Data Constellation Trace VI

Fetches the constellation trace for the data-subcarriers.

Use "segment<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-data-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0". Example: "segment0/stream0" "signal::sig1/segment0/stream0" "signal::sig1/result::r1/segment0/stream0" "result::r1/segment0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Data — Data Constellation returns the demodulated QAM symbols from all the data-subcarriers in all the OFDM symbols. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-data-peak-power-vi.html language=enus -->
## TOPIC 00125: RFmxWLAN OFDMModAcc Fetch Data Peak Power VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-data-peak-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-data-peak-power-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the data field. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do no

### RFmxWLAN OFDMModAcc Fetch Data Peak Power VI

Fetches the peak power of the data field.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-data-peak-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Data Peak Power Maximum (dBm) — Data Peak Power Maximum returns the peak power of the data field. This value is expressed in dBm. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns an array of the maximum of the data peak power results computed for each averaging count. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-eht-sig-bits-trace-vi.html language=enus -->
## TOPIC 00126: RFmxWLAN OFDMModAcc Fetch Decoded EHT-SIG Bits Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-eht-sig-bits-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-eht-sig-bits-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded EHT-SIG bits trace. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the defau

### RFmxWLAN OFDMModAcc Fetch Decoded EHT-SIG Bits Trace VI

Fetches the decoded EHT-SIG bits trace.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-decoded-eht-sig-bits-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Decoded EHT-SIG Bits — Decoded EHT-SIG Bits returns the array of bits in the EHT-SIG field of the 802.11be waveform for all 80 MHz subblocks. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-l-sig-bits-trace-vi.html language=enus -->
## TOPIC 00127: RFmxWLAN OFDMModAcc Fetch Decoded L-SIG Bits Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-l-sig-bits-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-l-sig-bits-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded L-SIG bits trace. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default

### RFmxWLAN OFDMModAcc Fetch Decoded L-SIG Bits Trace VI

Fetches the decoded L-SIG bits trace.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-decoded-l-sig-bits-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Decoded L-SIG Bits — Decoded L-SIG Bits returns the array of bits in the SIGNAL field of the 802.11a/g waveform or the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be/802.11bn waveforms. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-psdu-bits-trace-vi.html language=enus -->
## TOPIC 00128: RFmxWLAN OFDMModAcc Fetch Decoded PSDU Bits Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-psdu-bits-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-psdu-bits-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded PLCP service data unit (PSDU) bits. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not spec

### RFmxWLAN OFDMModAcc Fetch Decoded PSDU Bits Trace VI

Fetches the decoded PLCP service data unit (PSDU) bits.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-decoded-psdu-bits-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0". Example: "user0" "signal::sig1/user0" "signal::sig1/result::r1/user0" "result::r1/user0" You can use the RFmxWLAN Build User String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Decoded PSDU Bits — Decoded PSDU Bits returns an array of PSDU bits obtained after demodulation and decoding. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-service-bits-trace-vi.html language=enus -->
## TOPIC 00129: RFmxWLAN OFDMModAcc Fetch Decoded Service Bits Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-service-bits-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-service-bits-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded Service bits. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, t

### RFmxWLAN OFDMModAcc Fetch Decoded Service Bits Trace VI

Fetches the decoded Service bits.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-decoded-service-bits-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0". Example: "user0" "signal::sig1/user0" "signal::sig1/result::r1/user0" "result::r1/user0" You can use the RFmxWLAN Build User String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Decoded Service Bits — Decoded Service Bits returns an array of Service bits obtained after demodulation and decoding. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-sig-b-bits-trace-vi.html language=enus -->
## TOPIC 00130: RFmxWLAN OFDMModAcc Fetch Decoded SIG-B Bits Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-sig-b-bits-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-sig-b-bits-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded SIG-B bits. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default resul

### RFmxWLAN OFDMModAcc Fetch Decoded SIG-B Bits Trace VI

Fetches the decoded SIG-B bits.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-decoded-sig-b-bits-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Decoded SIG-B Bits — Decoded SIG-B Bits returns an array of bits in the VHT-SIG-B field of the 802.11ac waveform or the HE-SIG-B field of the 802.11ax waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-sig-bits-trace-vi.html language=enus -->
## TOPIC 00131: RFmxWLAN OFDMModAcc Fetch Decoded SIG Bits Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-sig-bits-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-sig-bits-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded SIG bits. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result

### RFmxWLAN OFDMModAcc Fetch Decoded SIG Bits Trace VI

Fetches the decoded SIG bits.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-decoded-sig-bits-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Decoded SIG Bits — Decoded SIG Bits returns an array of bits in the HT-SIG field of the 802.11n waveform, the VHT-SIG-A field of the 802.11ac waveform, or the HE-SIG-A field of the 802.11ax waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-u-sig-bits-trace-vi.html language=enus -->
## TOPIC 00132: RFmxWLAN OFDMModAcc Fetch Decoded U-SIG Bits Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-u-sig-bits-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-u-sig-bits-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the decoded U-SIG bits trace. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default

### RFmxWLAN OFDMModAcc Fetch Decoded U-SIG Bits Trace VI

Fetches the decoded U-SIG bits trace.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-decoded-u-sig-bits-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Decoded U-SIG Bits — Decoded U-SIG Bits returns the array of bits in the U-SIG field of the 802.11be/802.11bn waveform for all 80 MHz subblocks. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-evm-subcarrier-indices-vi.html language=enus -->
## TOPIC 00133: RFmxWLAN OFDMModAcc Fetch EVM Subcarrier Indices VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-evm-subcarrier-indices-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-evm-subcarrier-indices-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of subcarrier indices for which the EVM results are computed. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you d

### RFmxWLAN OFDMModAcc Fetch EVM Subcarrier Indices VI

Fetches the array of subcarrier indices for which the EVM results are computed.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-evm-subcarrier-indices-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Subcarrier Indices — Subcarrier Indices returns an array of subcarrier indices for which the EVM results are computed. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-frequency-error-ccdf-10-percent-vi.html language=enus -->
## TOPIC 00134: RFmxWLAN OFDMModAcc Fetch Frequency Error CCDF 10 Percent VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-frequency-error-ccdf-10-percent-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-frequency-error-ccdf-10-percent-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the 10% point of the complementary cumulative distribution function (CCDF) of frequency error across the number of iterations. Use "segment<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string compri

### RFmxWLAN OFDMModAcc Fetch Frequency Error CCDF 10 Percent VI

Fetches the 10% point of the complementary cumulative distribution function (CCDF) of frequency error across the number of iterations.

Use "segment<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-frequency-error-ccdf-10-percent-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxWLAN Build Segment String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Frequency Error CCDF 10% (Hz) — Frequency Error CCDF 10% returns the 10% point of the CCDF of absolute frequency error. When you set the OFDMModAcc Averaging Enabled property to True, the CCDF is computed over each averaging count. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-frequency-error-mean-vi.html language=enus -->
## TOPIC 00135: RFmxWLAN OFDMModAcc Fetch Frequency Error Mean VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-frequency-error-mean-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-frequency-error-mean-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the carrier frequency error of the transmitter. Use "segment<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify

### RFmxWLAN OFDMModAcc Fetch Frequency Error Mean VI

Fetches the carrier frequency error of the transmitter.

Use "segment<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-frequency-error-mean-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxWLAN Build Segment String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Frequency Error Mean (Hz) — Frequency Error Mean returns the carrier frequency error of the transmitter. This value is expressed in Hz. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the carrier frequency error results computed for each averaging count. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-group-delay-mean-trace-vi.html language=enus -->
## TOPIC 00136: RFmxWLAN OFDMModAcc Fetch Group Delay Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-group-delay-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-group-delay-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the group delay trace. Group delay is computed from the channel frequency response. When you set the OFDMModAcc Averaging Enabled property to True, this VI returns the mean of the group delay trace computed for each averaging count. Use "segment<n>/chain<k>/stream<l>" as the selector string

### RFmxWLAN OFDMModAcc Fetch Group Delay Mean Trace VI

Fetches the group delay trace. Group delay is computed from the channel frequency response. When you set the [OFDMModAcc Averaging Enabled](/csh?context=rfmxwlan_rfmxwlanprop_attra04002) property to **True**, this VI returns the mean of the group delay trace computed for each averaging count.

Use "segment<*n*>/chain<*k*>/stream<*l*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-group-delay-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, and stream number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/stream0". Example: "segment0/chain0/stream0" "signal::sig1/segment0/chain0/stream0" "signal::sig1/result::r1/segment0/chain0/stream0" "result::r1/segment0/chain0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Group Delay Mean (s) — Group Delay Mean (s) returns the group delay mean trace. x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of group delay responses. This value is expressed in seconds. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of group delay responses. This value is expressed in seconds. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-guard-interval-type-vi.html language=enus -->
## TOPIC 00137: RFmxWLAN OFDMModAcc Fetch Guard Interval Type VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-guard-interval-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-guard-interval-type-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the guard interval type. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default resu

### RFmxWLAN OFDMModAcc Fetch Guard Interval Type VI

Fetches the guard interval type.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-guard-interval-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Guard Interval Type — Guard Interval Type returns the size of the guard interval of OFDM symbols. 1/4 (0) Indicates the guard interval is 1/4th of the IFFT duration. 1/8 (1) Indicates the guard interval is 1/8th of the IFFT duration. 1/16 (2) Indicates the guard interval is 1/16th of the IFFT duration. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 1/4 (0) | Indicates the guard interval is 1/4th of the IFFT duration. |
| 1/8 (1) | Indicates the guard interval is 1/8th of the IFFT duration. |
| 1/16 (2) | Indicates the guard interval is 1/16th of the IFFT duration. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-iq-gain-imbalance-per-subcarrier-mean-trace-vi.html language=enus -->
## TOPIC 00138: RFmxWLAN OFDMModAcc Fetch IQ Gain Imbalance per Subcarrier Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-iq-gain-imbalance-per-subcarrier-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-iq-gain-imbalance-per-subcarrier-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q gain imbalance per subcarrier trace. When you set the OFDMModAcc Averaging Enabled property to True, this VI returns the mean of the I/Q gain imbalance computed for each averaging count. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Output

### RFmxWLAN OFDMModAcc Fetch IQ Gain Imbalance per Subcarrier Mean Trace VI

Fetches the I/Q gain imbalance per subcarrier trace. When you set the [OFDMModAcc Averaging Enabled](/csh?context=rfmxwlan_rfmxwlanprop_attra04002) property to **True**, this VI returns the mean of the I/Q gain imbalance computed for each averaging count.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-iq-gain-imbalance-per-subcarrier-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. I/Q Gain Imbalance per Subcarrier Mean (dB) — I/Q Gain Imbalance per Subcarrier Mean returns the I/Q gain imbalance per subcarrier trace. x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of I/Q gain imbalance for each subcarrier. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of I/Q gain imbalance for each subcarrier. This value is expressed in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-iq-impairments-vi.html language=enus -->
## TOPIC 00139: RFmxWLAN OFDMModAcc Fetch IQ Impairments VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-iq-impairments-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-iq-impairments-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q Impairment results for the OFDMModAcc measurement. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and c

### RFmxWLAN OFDMModAcc Fetch IQ Impairments VI

Fetches the I/Q Impairment results for the OFDMModAcc measurement.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-iq-impairments-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. I/Q Timing Skew Mean (s) — I/Q Timing Skew Mean returns the I/Q timing skew, which is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the I/Q timing skew computed for each averaging count. This value is expressed in seconds. Absolute I/Q Origin Offset Mean (dBm) — Absolute I/Q Origin Offset Mean returns the absolute I/Q origin offset, which is the power of the DC subcarrier. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the absolute I/Q origin offset computed for each averaging count. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Relative I/Q Origin Offset Mean (dB) — Relative I/Q Origin Offset Mean returns the relative I/Q origin offset, which is the ratio of the power of the DC subcarrier to the total power of all the subcarriers. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the relative I/Q origin offset computed for each averaging count. This value is expressed in dB. I/Q Gain Imbalance Mean (dB) — I/Q Gain Imbalance Mean returns the I/Q gain imbalance, which is the ratio of the RMS amplitude of the in-phase (I) component of the signal to the RMS amplitude of the quadrature-phase (Q) component of the signal. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the mean of the I/Q gain imbalance computed for each averaging count. This value is expressed in dB. I/Q Quadrature Error Mean (deg) — I/Q Quadrature Error Mean returns the I/Q quadrature error, which is a measure of deviation of the phase difference between the quadrature-phase (Q) and the in-phase (I) component of the signal from 90 degrees. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the I/Q quadrature error computed for each averaging count. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-iq-quadrature-error-per-subcarrier-mean-trace-vi.html language=enus -->
## TOPIC 00140: RFmxWLAN OFDMModAcc Fetch IQ Quadrature Error per Subcarrier Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-iq-quadrature-error-per-subcarrier-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-iq-quadrature-error-per-subcarrier-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q quadrature error per subcarrier trace. When you set the OFDMModAcc Averaging Enabled property to True, this VI returns the mean of the I/Q quadrature error computed for each averaging count. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Ou

### RFmxWLAN OFDMModAcc Fetch IQ Quadrature Error per Subcarrier Mean Trace VI

Fetches the I/Q quadrature error per subcarrier trace. When you set the [OFDMModAcc Averaging Enabled](/csh?context=rfmxwlan_rfmxwlanprop_attra04002) property to **True**, this VI returns the mean of the I/Q quadrature error computed for each averaging count.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-iq-quadrature-error-per-subcarrier-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. I/Q Quadrature Error per Subcarrier Mean (deg) — I/Q Quadrature Error per Subcarrier Mean returns the I/Q quadrature error per subcarrier trace. x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of I/Q quadrature errors for each subcarrier. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of I/Q quadrature errors for each subcarrier. This value is expressed in degrees. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-l-sig-parity-check-status-vi.html language=enus -->
## TOPIC 00141: RFmxWLAN OFDMModAcc Fetch L-SIG Parity Check Status VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-l-sig-parity-check-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-l-sig-parity-check-status-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the L-SIG parity check status. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the defaul

### RFmxWLAN OFDMModAcc Fetch L-SIG Parity Check Status VI

Fetches the L-SIG parity check status.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-l-sig-parity-check-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. L-SIG Parity Check Status — L-SIG Parity Check Status returns whether the parity check has passed either for the SIGNAL field of the 802.11a/g waveform or for the L-SIG field of the 802.11n/802.11ac/802.11ax/802.11be/802.11bn waveforms. Not Applicable (-1) Returns that the parity check is invalid for the current waveform. Fail (0) Returns that the parity check failed. Pass (1) Returns that the parity check passed. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Not Applicable (-1) | Returns that the parity check is invalid for the current waveform. |
| Fail (0) | Returns that the parity check failed. |
| Pass (1) | Returns that the parity check passed. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ltf-size-vi.html language=enus -->
## TOPIC 00142: RFmxWLAN OFDMModAcc Fetch LTF Size VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ltf-size-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ltf-size-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the HE-LTF or EHT-LTF size for 802.11ax or 802.11be, respectively. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not

### RFmxWLAN OFDMModAcc Fetch LTF Size VI

Fetches the HE-LTF or EHT-LTF size for 802.11ax or 802.11be, respectively.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-ltf-size-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. LTF Size — LTF Size returns the HE-LTF or EHT-LTF size. This result is applicable only to 802.11ax and 802.11be signals. Not Applicable (-1) Result is not applicable. 4x (0) The HE-LTF or EHT-LTF size is 4x. 2x (1) The HE-LTF or EHT-LTF size is 2x. 1x (2) The HE-LTF or EHT-LTF size is 1x. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Not Applicable (-1) | Result is not applicable. |
| 4x (0) | The HE-LTF or EHT-LTF size is 4x. |
| 2x (1) | The HE-LTF or EHT-LTF size is 2x. |
| 1x (2) | The HE-LTF or EHT-LTF size is 1x. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-mcs-index-vi.html language=enus -->
## TOPIC 00143: RFmxWLAN OFDMModAcc Fetch MCS Index VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-mcs-index-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-mcs-index-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the MCS index. Use "user<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal in

### RFmxWLAN OFDMModAcc Fetch MCS Index VI

Fetches the MCS index.

Use "user<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-mcs-index-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0". Example: "user0" "signal::sig1/user0" "signal::sig1/result::r1/user0" "result::r1/user0" You can use the RFmxWLAN Build User String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. MCS Index — MCS Index returns the MCS index or the data rate. The MCS index or data rate for various standard signals are decoded as follows: Standard Field 802.11a, 802.11j, 802.11p The data rate is decoded from the SIGNAL field. 802.11n The MCS index is decoded from the HT-SIG field. 802.11ac The MCS index is decoded from the VHT-SIG-A field. 802.11ax SU and Extended Range SU PPDU The MCS index is decoded from the HE-SIG-A field. 802.11ax MU PPDU The MCS index is decoded from the HE-SIG-B field. 802.11be MU PPDU The MCS index is decoded from the EHT-SIG field. 802.11bn MU PPDU The MCS index is decoded from the UHR-SIG field. 802.11bn ELR PPDU The MCS index is decoded from the ELR-SIG field. For 802.11a, 802.11j, and 802.11p signals, the following MCS indices corresponds to their data rates: MCS Data Rate 0 1.5 Mbps, 3 Mbps, and 6 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 1 2.25 Mbps, 4.5 Mbps, and 9 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 2 3 Mbps, 6 Mbps, and 12 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 3 4.5 Mbps, 9 Mbps, and 18 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 4 6 Mbps, 12 Mbps, and 24 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 5 9 Mbps, 18 Mbps, and 36 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 6 12 Mbps, 24 Mbps, and 48 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. 7 13.5 Mbps, 27 Mbps, and 54 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Standard | Field |
| 802.11a, 802.11j, 802.11p | The data rate is decoded from the SIGNAL field. |
| 802.11n | The MCS index is decoded from the HT-SIG field. |
| 802.11ac | The MCS index is decoded from the VHT-SIG-A field. |
| 802.11ax SU and Extended Range SU PPDU | The MCS index is decoded from the HE-SIG-A field. |
| 802.11ax MU PPDU | The MCS index is decoded from the HE-SIG-B field. |
| 802.11be MU PPDU | The MCS index is decoded from the EHT-SIG field. |
| 802.11bn MU PPDU | The MCS index is decoded from the UHR-SIG field. |
| 802.11bn ELR PPDU | The MCS index is decoded from the ELR-SIG field. |
| MCS | Data Rate |
| 0 | 1.5 Mbps, 3 Mbps, and 6 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 1 | 2.25 Mbps, 4.5 Mbps, and 9 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 2 | 3 Mbps, 6 Mbps, and 12 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 3 | 4.5 Mbps, 9 Mbps, and 18 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 4 | 6 Mbps, 12 Mbps, and 24 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 5 | 9 Mbps, 18 Mbps, and 36 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 6 | 12 Mbps, 24 Mbps, and 48 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 7 | 13.5 Mbps, 27 Mbps, and 54 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-he-sig-b-symbols-vi.html language=enus -->
## TOPIC 00144: RFmxWLAN OFDMModAcc Fetch Number of HE-SIG-B Symbols VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-he-sig-b-symbols-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-he-sig-b-symbols-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the number of HE-SIG-B symbols. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the defau

### RFmxWLAN OFDMModAcc Fetch Number of HE-SIG-B Symbols VI

Fetches the number of HE-SIG-B symbols.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-number-of-he-sig-b-symbols-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Number of HE-SIG-B Symbols — Number of HE-SIG-B Symbols returns the number of HE-SIG-B symbols. This result is applicable for 802.11ax MU PPDU signals, and is decoded from the HE-SIG-A field. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-space-time-streams-vi.html language=enus -->
## TOPIC 00145: RFmxWLAN OFDMModAcc Fetch Number of Space Time Streams VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-space-time-streams-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-space-time-streams-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the number of space time streams. Use "user<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, th

### RFmxWLAN OFDMModAcc Fetch Number of Space Time Streams VI

Fetches the number of space time streams.

Use "user<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-number-of-space-time-streams-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0". Example: "user0" "signal::sig1/user0" "signal::sig1/result::r1/user0" "result::r1/user0" You can use the RFmxWLAN Build User String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Number of Space Time Streams — Number of Space Time Streams returns the number of space time streams. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-symbols-used-vi.html language=enus -->
## TOPIC 00146: RFmxWLAN OFDMModAcc Fetch Number of Symbols Used VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-symbols-used-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-symbols-used-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the number of OFDM symbols used for EVM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the r

### RFmxWLAN OFDMModAcc Fetch Number of Symbols Used VI

Fetches the number of OFDM symbols used for EVM measurement.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-number-of-symbols-used-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Number of Symbols Used — Number of Symbols Used returns the number of OFDM symbols used by the measurement. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-users-vi.html language=enus -->
## TOPIC 00147: RFmxWLAN OFDMModAcc Fetch Number of Users VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-users-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-users-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the number of users. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result i

### RFmxWLAN OFDMModAcc Fetch Number of Users VI

Fetches the number of users.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-number-of-users-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Number of Users — Number of Users returns the number of users which is derived for the following standards. Standard Derivation 802.11ac Derived from the VHT-SIG-A for VHT MU PPDU. 802.11ax Derived from the HE-SIG-B for HE MU PPDU. 802.11be Derived from the EHT-SIG for EHT MU PPDU. 802.11bn Derived from the UHR-SIG for UHR MU PPDU. For all other PPDUs, this property returns 1. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Standard | Derivation |
| 802.11ac | Derived from the VHT-SIG-A for VHT MU PPDU. |
| 802.11ax | Derived from the HE-SIG-B for HE MU PPDU. |
| 802.11be | Derived from the EHT-SIG for EHT MU PPDU. |
| 802.11bn | Derived from the UHR-SIG for UHR MU PPDU. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pe-average-power-vi.html language=enus -->
## TOPIC 00148: RFmxWLAN OFDMModAcc Fetch PE Average Power VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pe-average-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pe-average-power-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power of the packet extension field. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain numbe

### RFmxWLAN OFDMModAcc Fetch PE Average Power VI

Fetches the average power of the packet extension field.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-pe-average-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PE Average Power Mean (dBm) — PE Average Power Mean returns the average power of the packet extension field. This parameter is applicable for 802.11ax signals. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the packet extension field average power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pe-duration-vi.html language=enus -->
## TOPIC 00149: RFmxWLAN OFDMModAcc Fetch PE Duration VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pe-duration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pe-duration-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the duration of the packet extension field. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result nam

### RFmxWLAN OFDMModAcc Fetch PE Duration VI

Fetches the duration of the packet extension field.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-pe-duration-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PE Duration (s) — PE Duration (s) returns the duration of the packet extension field for the 802.11ax and 802.11be signals. This parameter is applicable only when you set the OFDM Header Decoding Enabled property to True. This value is expressed in seconds. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pe-peak-power-vi.html language=enus -->
## TOPIC 00150: RFmxWLAN OFDMModAcc Fetch PE Peak Power VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pe-peak-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pe-peak-power-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the packet extension field. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number.

### RFmxWLAN OFDMModAcc Fetch PE Peak Power VI

Fetches the peak power of the packet extension field.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-pe-peak-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PE Peak Power Maximum (dBm) — PE Peak Power Maximum returns the peak power of the packet extension field. This parameter is applicable for 802.11ax signals. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the PE field peak power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-phase-noise-psd-mean-trace-vi.html language=enus -->
## TOPIC 00151: RFmxWLAN OFDMModAcc Fetch Phase Noise PSD Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-phase-noise-psd-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-phase-noise-psd-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase noise power spectral density (PSD) trace for signals containing an OFDM payload. Phase noise estimates are derived from the common pilot error estimates. When you set the OFDMModAcc Averaging Enabled property to True, this VI returns the mean of the phase noise PSD computed for eac

### RFmxWLAN OFDMModAcc Fetch Phase Noise PSD Mean Trace VI

Fetches the phase noise power spectral density (PSD) trace for signals containing an OFDM payload.

Phase noise estimates are derived from the common pilot error estimates. When you set the [OFDMModAcc Averaging Enabled](/csh?context=rfmxwlan_rfmxwlanprop_attra04002) property to **True**, this VI returns the mean of the phase noise PSD computed for each averaging count.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-phase-noise-psd-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxWLAN Build Segment String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Phase Noise PSD Mean (dBc/Hz) — Phase Noise PSD Mean returns the mean of the phase noise PSD trace. x0 — x0 returns the start frequency of the phase noise PSD mean trace. This value is expressed in Hz. dx — dx returns the frequency intervals between data points in the phase noise PSD mean trace. This value is expressed in Hz. y — y returns an array of the mean of phase noise PSD. This value is expressed in dBc/Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency of the phase noise PSD mean trace. This value is expressed in Hz. dx — dx returns the frequency intervals between data points in the phase noise PSD mean trace. This value is expressed in Hz. y — y returns an array of the mean of phase noise PSD. This value is expressed in dBc/Hz. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pilot-constellation-trace-vi.html language=enus -->
## TOPIC 00152: RFmxWLAN OFDMModAcc Fetch Pilot Constellation Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pilot-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pilot-constellation-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace for the pilot-subcarriers. Use "segment<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream n

### RFmxWLAN OFDMModAcc Fetch Pilot Constellation Trace VI

Fetches the constellation trace for the pilot-subcarriers.

Use "segment<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-pilot-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0". Example: "segment0/stream0" "signal::sig1/segment0/stream0" "signal::sig1/result::r1/segment0/stream0" "result::r1/segment0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Data — Pilot Constellation returns the demodulated QAM symbols from all the pilot-subcarriers in all OFDM symbols. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ppdu-average-power-vi.html language=enus -->
## TOPIC 00153: RFmxWLAN OFDMModAcc Fetch PPDU Average Power VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ppdu-average-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ppdu-average-power-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power of the PPDU. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not s

### RFmxWLAN OFDMModAcc Fetch PPDU Average Power VI

Fetches the average power of the PPDU.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-ppdu-average-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PPDU Average Power Mean (dBm) — PPDU Average Power Mean returns the average power of the PPDU. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the PPDU average power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ppdu-peak-power-vi.html language=enus -->
## TOPIC 00154: RFmxWLAN OFDMModAcc Fetch PPDU Peak Power VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ppdu-peak-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ppdu-peak-power-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the PPDU. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not spec

### RFmxWLAN OFDMModAcc Fetch PPDU Peak Power VI

Fetches the peak power of the PPDU.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-ppdu-peak-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PPDU Peak Power Maximum (dBm) — PPDU Peak Power Maximum returns the peak power of the PPDU. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the PPDU peak power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ppdu-type-vi.html language=enus -->
## TOPIC 00155: RFmxWLAN OFDMModAcc Fetch PPDU Type VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ppdu-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ppdu-type-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PPDU type. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instanc

### RFmxWLAN OFDMModAcc Fetch PPDU Type VI

Fetches the PPDU type.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-ppdu-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PPDU Type — PPDU Type returns the PPDU type. Non-HT (0) Applicable to 802.11a, 802.11j, and 802.11p signals or for 802.11n, 802.11ac, and 802.11ax signals that operate in the Non-HT mode. Mixed (1) Applicable to 802.11n mixed PPDU signals. Greenfield (2) Applicable to 802.11n greenfield PPDU signals. SU (3) Applicable to 802.11ac and 802.11ax SU PPDU signals. MU (4) Applicable to 802.11ax, 802.11be, and 802.11bn MU PPDU signals. Extended Range SU (5) Applicable to 802.11ax extended range SU PPDU signals. Trigger-based (6) Applicable to 802.11ax, 802.11be, and 802.11bn TB PPDU signals. ELR (7) Applicable to 802.11bn ELR PPDU signals. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Non-HT (0) | Applicable to 802.11a, 802.11j, and 802.11p signals or for 802.11n, 802.11ac, and 802.11ax signals that operate in the Non-HT mode. |
| Mixed (1) | Applicable to 802.11n mixed PPDU signals. |
| Greenfield (2) | Applicable to 802.11n greenfield PPDU signals. |
| SU (3) | Applicable to 802.11ac and 802.11ax SU PPDU signals. |
| MU (4) | Applicable to 802.11ax, 802.11be, and 802.11bn MU PPDU signals. |
| Extended Range SU (5) | Applicable to 802.11ax extended range SU PPDU signals. |
| Trigger-based (6) | Applicable to 802.11ax, 802.11be, and 802.11bn TB PPDU signals. |
| ELR (7) | Applicable to 802.11bn ELR PPDU signals. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11ac-vi.html language=enus -->
## TOPIC 00156: RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (802.11ac) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11ac-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11ac-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power of the 802.11ac specific preamble fields. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and

### RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (802.11ac) VI

Fetches the average power of the 802.11ac specific preamble fields.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11ac-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VHT-SIG-B Average Power Mean (dBm) — VHT-SIG-B Average Power Mean returns the average power of the VHT-SIG-B field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the VHT-SIG-B field average power results computed for each averaging count. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. VHT-SIG-A Average Power Mean (dBm) — VHT-SIG-A Average Power Mean returns the average power of the VHT-SIG-A field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the VHT-SIG-A field average power results computed for each averaging count. This value is expressed in dBm. VHT-STF Average Power Mean (dBm) — VHT-STF Average Power Mean returns the average power of the VHT-STF field. When you set the OFDMModAcc Averaging Enabled property to True, this paramter returns the mean of the VHT-STF average power results computed for each averaging count. This value is expressed in dBm. VHT-LTF Average Power Mean (dBm) — VHT-LTF Average Power Mean returns the average power of the VHT-LTF field. When you set the OFDMModAcc Averaging Enabled property to True, this paramter returns the mean of the VHT-LTF average power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11ax-vi.html language=enus -->
## TOPIC 00157: RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (802.11ax) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11ax-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11ax-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power of the 802.11ax specific preamble fields. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and

### RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (802.11ax) VI

Fetches the average power of the 802.11ax specific preamble fields.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11ax-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. HE-LTF Average Power Mean (dBm) — HE-LTF Average Power Mean returns the average power of the HE-LTF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the HE-LTF average power results computed for each averaging count. This value is expressed in dBm. HE-STF Average Power Mean (dBm) — HE-STF Average Power Mean returns the average power of the HE-STF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the HE-STF average power results computed for each averaging count. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. RL-SIG Average Power Mean (dBm) — RL-SIG Average Power Mean returns the average power of the RL-SIG field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the RL-SIG field average power results computed for each averaging count. This value is expressed in dBm. HE-SIG-A Average Power Mean (dBm) — HE-SIG-A Average Power Mean returns the average power of the HE-SIG-A field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the HE-SIG-A field average power results computed for each averaging count. This value is expressed in dBm. HE-SIG-B Average Power Mean (dBm) — HE-SIG-B Average Power Mean returns the average power of the HE-SIG-B field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the HE-SIG-B field average power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11be-vi.html language=enus -->
## TOPIC 00158: RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (802.11be) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11be-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11be-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power of the 802.11be specific preamble fields. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and

### RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (802.11be) VI

Fetches the average power of the 802.11be specific preamble fields.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11be-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. EHT-LTF Average Power Mean (dBm) — EHT-LTF Average Power Mean returns the average power of the EHT-LTF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the EHT-LTF average power results computed for each averaging count. This value is expressed in dBm. EHT-STF Average Power Mean (dBm) — EHT-STF Average Power Mean returns the average power of the EHT-STF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the EHT-STF average power results computed for each averaging count. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. RL-SIG Average Power Mean (dBm) — RL-SIG Average Power Mean returns the average power of the RL-SIG field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the RL-SIG field average power results computed for each averaging count. This value is expressed in dBm. U-SIG Average Power Mean (dBm) — U-SIG Average Power Mean returns the average power of the U-SIG field. When you set the OFDMModAcc Averaging Enabled property to True, this paramter returns the mean of the U-SIG average power results computed for each averaging count. This value is expressed in dBm. EHT-SIG Average Power Mean (dBm) — EHT-SIG Average Power Mean returns the average power of the EHT-SIG field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the EHT-SIG average power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11n-vi.html language=enus -->
## TOPIC 00159: RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (802.11n) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11n-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11n-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power of the 802.11n specific preamble fields. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and c

### RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (802.11n) VI

Fetches the average power of the 802.11n specific preamble fields.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11n-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. HT-ELTF Average Power Mean (dBm) — HT-ELTF Average Power Mean returns the average power of the HT-ELTF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the HT-ELTF average power results computed for each averaging count. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. HT-SIG Average Power Mean (dBm) — HT-SIG Average Power Mean returns the average power of the HT-SIG field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the HT-SIG field average power results computed for each averaging count. This value is expressed in dBm. HT-STF Average Power Mean (dBm) — HT-STF Average Power Mean returns the average power of the HT-STF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the HT-STF average power results computed for each averaging count. This value is expressed in dBm. HT-DLTF Average Power Mean (dBm) — HT-DLTF Average Power Mean returns the average power of the HT-DLTF. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the HT-DLTF average power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-common-vi.html language=enus -->
## TOPIC 00160: RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (Common) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-common-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-common-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power of the preamble fields. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If y

### RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (Common) VI

Fetches the average power of the preamble fields.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-common-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. L-STF Average Power Mean (dBm) — L-STF Average Power Mean returns the average power of the L-STF or STF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the L-STF or STF average power results computed for each averaging count. This value is expressed in dBm. L-LTF Average Power Mean (dBm) — L-LTF Average Power Mean returns the average power of the L-LTF or LTF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the L-LTF or LTF average power results computed for each averaging count. This value is expressed in dBm. L-SIG Average Power Mean (dBm) — L-SIG Average Power Mean returns the average power of the L-SIG or SIGNAL field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the L-SIG or SIGNAL field average power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-frequency-error-trace-vi.html language=enus -->
## TOPIC 00161: RFmxWLAN OFDMModAcc Fetch Preamble Frequency Error Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-frequency-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-frequency-error-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the preamble frequency error trace for signals containing an OFDM payload. Preamble frequency error computes the variations, across time, of the frequency error over initial 16us which comprises of the short training field (STF) and long training field (LTF) symbols. icon Inputs/Outputs cstr

### RFmxWLAN OFDMModAcc Fetch Preamble Frequency Error Trace VI

Fetches the preamble frequency error trace for signals containing an OFDM payload. Preamble frequency error computes the variations, across time, of the frequency error over initial 16us which comprises of the short training field (STF) and long training field (LTF) symbols.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-preamble-frequency-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Preamble Frequency Error (Hz) — Preamble Frequency Error (Hz) returns the preamble frequency error trace for signals containing an OFDM payload. Preamble frequency error computes the variations, across time, of the frequency error over initial 16us which comprises of the short training field (STF) and long training field (LTF) symbols. x0 — x0 returns the start time in seconds. dx — dx returns the time increment value. This value is the reciprocal of OFDM ModAcc processing rate. y — y returns the preamble frequency error at every sampling time. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time in seconds. dx — dx returns the time increment value. This value is the reciprocal of OFDM ModAcc processing rate. y — y returns the preamble frequency error at every sampling time. This value is expressed in Hz. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11ac-vi.html language=enus -->
## TOPIC 00162: RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (802.11ac) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11ac-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11ac-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the 802.11ac specific preamble fields. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and cha

### RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (802.11ac) VI

Fetches the peak power of the 802.11ac specific preamble fields.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11ac-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. VHT-SIG-B Peak Power Maximum (dBm) — VHT-SIG-B Peak Power Maximum returns the peak power of the VHT-SIG-B field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the VHT-SIG-B field peak power results computed for each averaging count. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. VHT-SIG-A Peak Power Maximum (dBm) — VHT-SIG-A Peak Power Maximum returns the peak power of the VHT-SIG-A field. When you set the OFDMModAcc Averaging Enabled property to True, this property returns the maximum of the VHT-SIG-A field peak power results computed for each averaging count. This value is expressed in dBm. VHT-STF Peak Power Maximum (dBm) — VHT-STF Peak Power Maximum returns the peak power of the VHT-STF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the VHT-STF peak power results computed for each averaging count. This value is expressed in dBm. VHT-LTF Peak Power Maximum (dBm) — VHT-LTF Peak Power Maximum returns the peak power of the VHT-LTF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the VHT-LTF peak power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11ax-vi.html language=enus -->
## TOPIC 00163: RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (802.11ax) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11ax-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11ax-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the 802.11ax specific preamble fields. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and cha

### RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (802.11ax) VI

Fetches the peak power of the 802.11ax specific preamble fields.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11ax-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. HE-LTF Peak Power Maximum (dBm) — HE-LTF Peak Power Maximum returns the peak power of the HE-LTF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the HE-LTF peak power results computed for each averaging count. This value is expressed in dBm. HE-STF Peak Power Maximum (dBm) — HE-STF Peak Power Maximum returns the peak power of the HE-STF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the HE-STF peak power results computed for each averaging count. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. RL-SIG Peak Power Maximum (dBm) — RL-SIG Peak Power Maximum returns the peak power of the RL-SIG field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the RL-SIG field peak power results computed for each averaging count. This value is expressed in dBm. HE-SIG-A Peak Power Maximum (dBm) — HE-SIG-A Peak Power Maximum (dBm) returns the peak power of the HE-SIG-A field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the HE-SIG-A field peak power results computed for each averaging count. This value is expressed in dBm. HE-SIG-B Peak Power Maximum (dBm) — HE-SIG-B Peak Power Maximum returns the peak power of the HE-SIG-B field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the HE-SIG-B field peak power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11be-vi.html language=enus -->
## TOPIC 00164: RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (802.11be) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11be-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11be-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the 802.11be specific preamble fields. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and cha

### RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (802.11be) VI

Fetches the peak power of the 802.11be specific preamble fields.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11be-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. EHT-LTF Peak Power Maximum (dBm) — EHT-LTF Peak Power Maximum returns the peak power of the EHT-LTF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the EHT-LTF peak power results computed for each averaging count. This value is expressed in dBm. EHT-STF Peak Power Maximum (dBm) — EHT-STF Peak Power Maximum returns the peak power of the EHT-STF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the EHT-STF peak power results computed for each averaging count. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. RL-SIG Peak Power Maximum (dBm) — RL-SIG Peak Power Maximum returns the peak power of the RL-SIG field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the RL-SIG field peak power results computed for each averaging count. This value is expressed in dBm. U-SIG Peak Power Maximum (dBm) — U-SIG Peak Power Maximum returns the peak power of the U-SIG field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the U-SIG peak power results computed for each averaging count. This value is expressed in dBm. EHT-SIG Peak Power Maximum (dBm) — EHT-SIG Peak Power Maximum returns the peak power of the EHT-SIG field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the EHT-SIG peak power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11n-vi.html language=enus -->
## TOPIC 00165: RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (802.11n) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11n-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11n-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the 802.11n specific preamble fields. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and chai

### RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (802.11n) VI

Fetches the peak power of the 802.11n specific preamble fields.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11n-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. HT-ELTF Peak Power Maximum (dBm) — HT-ELTF Peak Power Maximum returns the peak power of the HT-ELTF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the HT-ELTF peak power results computed for each averaging count. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. HT-SIG Peak Power Maximum (dBm) — HT-SIG Peak Power Maximum returns the peak power of the HT-SIG field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the HT-SIG field peak power results computed for each averaging count. This value is expressed in dBm. HT-STF Peak Power Maximum (dBm) — HT-STF Peak Power Maximum returns the peak power of the HT-STF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the HT-STF peak power results computed for each averaging count. This value is expressed in dBm. HT-DLTF Peak Power Maximum (dBm) — HT-DLTF Peak Power Maximum returns the peak power of the HT-DLTF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the HT-DLTF peak power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-common-vi.html language=enus -->
## TOPIC 00166: RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (Common) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-common-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-common-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak power of the preamble fields. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you

### RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (Common) VI

Fetches the peak power of the preamble fields.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-common-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. L-STF Peak Power Maximum (dBm) — L-STF Peak Power Maximum returns the peak power of the L-STF or STF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the L-STF or STF peak power results computed for each averaging count. This value is expressed in dBm. L-LTF Peak Power Maximum (dBm) — L-LTF Peak Power Maximum returns the peak power of the L-LTF or LTF field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the L-LTF or LTF peak power results computed for each averaging count. This value is expressed in dBm. L-SIG Peak Power Maximum (dBm) — L-SIG Peak Power Maximum returns the peak power of the L-SIG or SIGNAL field. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the maximum of the L-SIG or SIGNAL field peak power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-psdu-crc-status-vi.html language=enus -->
## TOPIC 00167: RFmxWLAN OFDMModAcc Fetch PSDU CRC Status VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-psdu-crc-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-psdu-crc-status-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PLCP service data unit (PSDU) CRC status. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result n

### RFmxWLAN OFDMModAcc Fetch PSDU CRC Status VI

Fetches the PLCP service data unit (PSDU) CRC status.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-psdu-crc-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PSDU CRC Status — PSDU CRC Status returns the PSDU CRC status. Fail (0) Indicates that the PSDU CRC failed. Pass (1) Indicates that the PSDU CRC passed. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | Indicates that the PSDU CRC failed. |
| Pass (1) | Indicates that the PSDU CRC passed. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-reference-data-constellation-trace-vi.html language=enus -->
## TOPIC 00168: RFmxWLAN OFDMModAcc Fetch Reference Data Constellation Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-reference-data-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-reference-data-constellation-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the reference constellation trace for the data-subcarriers. Use "segment<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and

### RFmxWLAN OFDMModAcc Fetch Reference Data Constellation Trace VI

Fetches the reference constellation trace for the data-subcarriers.

Use "segment<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-reference-data-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0". Example: "segment0/stream0" "signal::sig1/segment0/stream0" "signal::sig1/result::r1/segment0/stream0" "result::r1/segment0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Reference Data — Reference Data Constellation returns the reference QAM symbols for all the data-subcarriers in all the OFDM symbols. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ru-offset-and-size-vi.html language=enus -->
## TOPIC 00169: RFmxWLAN OFDMModAcc Fetch RU Offset and Size VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ru-offset-and-size-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ru-offset-and-size-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the RU offset and the RU size of the specified user. Use "user<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify

### RFmxWLAN OFDMModAcc Fetch RU Offset and Size VI

Fetches the RU offset and the RU size of the specified user.

Use "user<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-ru-offset-and-size-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0". Example: "user0" "signal::sig1/user0" "signal::sig1/result::r1/user0" "result::r1/user0" You can use the RFmxWLAN Build User String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. RU Offset — RU Offset returns the location of RU for the specified user in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. RU Size — RU Size returns the RU size for the specified user. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-sig-b-crc-status-vi.html language=enus -->
## TOPIC 00170: RFmxWLAN OFDMModAcc Fetch SIG-B CRC Status VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-sig-b-crc-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-sig-b-crc-status-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SIG-B CRC Status. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result

### RFmxWLAN OFDMModAcc Fetch SIG-B CRC Status VI

Fetches the SIG-B CRC Status.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-sig-b-crc-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. SIG-B CRC Status — SIG-B CRC Status returns whether the cyclic redundancy check (CRC) has passed for the HE-SIG-B field of the 802.11ax MU PPDU waveform. Not Applicable (-1) Returns that the SIG-B CRC is invalid for the current waveform. Fail (0) Returns that the SIG-B CRC failed. Pass (1) Returns that the SIG-B CRC passed. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Not Applicable (-1) | Returns that the SIG-B CRC is invalid for the current waveform. |
| Fail (0) | Returns that the SIG-B CRC failed. |
| Pass (1) | Returns that the SIG-B CRC passed. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-sig-crc-status-vi.html language=enus -->
## TOPIC 00171: RFmxWLAN OFDMModAcc Fetch SIG CRC Status VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-sig-crc-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-sig-crc-status-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SIG CRC Status. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result in

### RFmxWLAN OFDMModAcc Fetch SIG CRC Status VI

Fetches the SIG CRC Status.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-sig-crc-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. SIG CRC Status — SIG CRC Status returns whether the cyclic redundancy check (CRC) has passed either for the HT-SIG field of the 802.11n waveform, for the VHT-SIG-A field of the 802.11ac waveform, or for the HE-SIG-A field of the 802.11ax waveform. Not Applicable (-1) Returns that the SIG CRC is invalid for the current waveform. Fail (0) Returns that the SIG CRC failed. Pass (1) Returns that the SIG CRC passed. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Not Applicable (-1) | Returns that the SIG CRC is invalid for the current waveform. |
| Fail (0) | Returns that the SIG CRC failed. |
| Pass (1) | Returns that the SIG CRC passed. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-spectral-flatness-mean-trace-vi.html language=enus -->
## TOPIC 00172: RFmxWLAN OFDMModAcc Fetch Spectral Flatness Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-spectral-flatness-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-spectral-flatness-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectral flatness trace, and the lower and upper spectral flatness mask traces. When you set the OFDMModAcc Averaging Enabled property to True, this VI returns the spectral flatness trace computed on the mean of the channel estimates computed for each averaging count. Use "segment<n>/cha

### RFmxWLAN OFDMModAcc Fetch Spectral Flatness Mean Trace VI

Fetches the spectral flatness trace, and the lower and upper spectral flatness mask traces. When you set the [OFDMModAcc Averaging Enabled](/csh?context=rfmxwlan_rfmxwlanprop_attra04002) property to **True**, this VI returns the spectral flatness trace computed on the mean of the channel estimates computed for each averaging count.

Use "segment<*n*>/chain<*k*>/stream<*l*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-spectral-flatness-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, and stream number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/stream0". Example: "segment0/chain0/stream0" "signal::sig1/segment0/chain0/stream0" "signal::sig1/result::r1/segment0/chain0/stream0" "result::r1/segment0/chain0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Spectral Flatness Mean (dB) — Spectral Flatness Mean returns the spectral flatness trace. x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of spectral flatness for each subcarrier. This value is expressed in dB. Spectral Flatness Lower Mask (dB) — Spectral Flatness Lower Mask returns the lower spectral flatness mask trace. x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of spectral flatness lower mask for each subcarrier. This value is expressed in dB. Spectral Flatness Upper Mask (dB) — Spectral Flatness Upper Mask returns the upper spectral flatness mask trace. x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of spectral flatness upper mask for each subcarrier. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of spectral flatness for each subcarrier. This value is expressed in dB. |
| x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of spectral flatness lower mask for each subcarrier. This value is expressed in dB. |
| x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of spectral flatness upper mask for each subcarrier. This value is expressed in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-spectral-flatness-vi.html language=enus -->
## TOPIC 00173: RFmxWLAN OFDMModAcc Fetch Spectral Flatness VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-spectral-flatness-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-spectral-flatness-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectral flatness margin results. Use "segment<n>/chain<k>/stream<l>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, an

### RFmxWLAN OFDMModAcc Fetch Spectral Flatness VI

Fetches the spectral flatness margin results.

Use "segment<*n*>/chain<*k*>/stream<*l*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-spectral-flatness-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, and stream number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/stream0". Example: "segment0/chain0/stream0" "signal::sig1/segment0/chain0/stream0" "signal::sig1/result::r1/segment0/chain0/stream0" "result::r1/segment0/chain0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Spectral Flatness Margin (dB) — Spectral Flatness Margin returns the spectral flatness margin, which is the minimum of the upper and lower spectral flatness margins. The upper spectral flatness margin is the minimum difference between the upper mask and the spectral flatness across subcarriers. The lower spectral flatness margin is the minimum difference between the spectral flatness and the lower mask across subcarriers. When you set the OFDMModAcc Averaging Enabled property to True, the spectral flatness is computed using the mean of the channel frequency response magnitude computed for each averaging count. This value is expressed in dB. Spectral Flatness Margin Subcarrier Index — Spectral Flatness Margin Subcarrier Index returns the subcarrier index corresponding to the Spectral Flatness Margin parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-data-rms-evm-per-symbol-mean-trace-vi.html language=enus -->
## TOPIC 00174: RFmxWLAN OFDMModAcc Fetch Stream Data RMS EVM per Symbol Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-data-rms-evm-per-symbol-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-data-rms-evm-per-symbol-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream data subcarriers RMS EVM per symbol trace. Use "segment<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and strea

### RFmxWLAN OFDMModAcc Fetch Stream Data RMS EVM per Symbol Mean Trace VI

Fetches the stream data subcarriers RMS EVM per symbol trace.

Use "segment<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-stream-data-rms-evm-per-symbol-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0". Example: "segment0/stream0" "signal::sig1/segment0/stream0" "signal::sig1/result::r1/segment0/stream0" "result::r1/segment0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Stream Data RMS EVM per Symbol Mean (dB or %) — Stream Data RMS EVM per Symbol Mean returns the stream data subcarriers RMS EVM per symbol trace. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the stream data RMS EVM per symbol computed for each averaging count. x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream data subcarriers RMS EVM of each OFDM symbol. This value is expressed as a percentage or in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream data subcarriers RMS EVM of each OFDM symbol. This value is expressed as a percentage or in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-pilot-rms-evm-per-symbol-mean-trace-vi.html language=enus -->
## TOPIC 00175: RFmxWLAN OFDMModAcc Fetch Stream Pilot RMS EVM per Symbol Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-pilot-rms-evm-per-symbol-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-pilot-rms-evm-per-symbol-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream pilot subcarriers RMS EVM per symbol trace. Use "segment<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and stre

### RFmxWLAN OFDMModAcc Fetch Stream Pilot RMS EVM per Symbol Mean Trace VI

Fetches the stream pilot subcarriers RMS EVM per symbol trace.

Use "segment<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-stream-pilot-rms-evm-per-symbol-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0". Example: "segment0/stream0" "signal::sig1/segment0/stream0" "signal::sig1/result::r1/segment0/stream0" "result::r1/segment0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Stream Pilot RMS EVM per Symbol Mean (dB or %) — Stream Pilot RMS EVM per Symbol Mean returns the stream pilot subcarriers RMS EVM per symbol trace. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the stream pilot RMS EVM per symbol computed for each averaging count. x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream pilot subcarriers RMS EVM of each OFDM symbol. This value is expressed as a percentage or in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream pilot subcarriers RMS EVM of each OFDM symbol. This value is expressed as a percentage or in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-per-subcarrier-mean-trace-vi.html language=enus -->
## TOPIC 00176: RFmxWLAN OFDMModAcc Fetch Stream RMS EVM per Subcarrier Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-per-subcarrier-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-per-subcarrier-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream RMS EVM per subcarrier trace. Use "segment<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If

### RFmxWLAN OFDMModAcc Fetch Stream RMS EVM per Subcarrier Mean Trace VI

Fetches the stream RMS EVM per subcarrier trace.

Use "segment<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-per-subcarrier-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0". Example: "segment0/stream0" "signal::sig1/segment0/stream0" "signal::sig1/result::r1/segment0/stream0" "result::r1/segment0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Stream RMS EVM per Subcarrier Mean (dB or %) — Stream RMS EVM per Subcarrier Mean returns the stream RMS EVM per subcarrier trace. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the stream RMS EVM per subcarrier computed for each averaging count. x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns the stream RMS EVM for each subcarrier. This value is expressed as a percentage or in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns the stream RMS EVM for each subcarrier. This value is expressed as a percentage or in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-per-symbol-mean-trace-vi.html language=enus -->
## TOPIC 00177: RFmxWLAN OFDMModAcc Fetch Stream RMS EVM per Symbol Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-per-symbol-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-per-symbol-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream RMS EVM per symbol trace. Use "segment<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you

### RFmxWLAN OFDMModAcc Fetch Stream RMS EVM per Symbol Mean Trace VI

Fetches the stream RMS EVM per symbol trace.

Use "segment<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-per-symbol-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0". Example: "segment0/stream0" "signal::sig1/segment0/stream0" "signal::sig1/result::r1/segment0/stream0" "result::r1/segment0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Stream RMS EVM per Symbol Mean (dB or %) — Stream RMS EVM per Symbol Mean returns the stream RMS EVM per symbol trace. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the stream RMS EVM per symbol computed for each averaging count. x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream RMS EVM of each OFDM symbol. This value is expressed as a percentage or in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream RMS EVM of each OFDM symbol. This value is expressed as a percentage or in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-vi.html language=enus -->
## TOPIC 00178: RFmxWLAN OFDMModAcc Fetch Stream RMS EVM VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream RMS EVM results. Use "segment<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not sp

### RFmxWLAN OFDMModAcc Fetch Stream RMS EVM VI

Fetches the stream RMS EVM results.

Use "segment<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0". Example: "segment0/stream0" "signal::sig1/segment0/stream0" "signal::sig1/result::r1/segment0/stream0" "result::r1/segment0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Stream RMS EVM Mean (dB or %) — Stream RMS EVM Mean returns the stream RMS EVM of all subcarriers in all OFDM symbols. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of stream RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB. Stream Data RMS EVM Mean (dB or %) — Stream Data RMS EVM Mean returns the stream RMS EVM of data subcarriers in all OFDM symbols. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of data stream RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB. Stream Pilot RMS EVM Mean (dB or %) — Stream Pilot RMS EVM Mean returns the stream RMS EVM of pilot subcarriers in all OFDM symbols. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of pilot stream RMS EVM results computed for each averaging count. This value is expressed as a percentage or in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-subcarrier-chain-evm-per-symbol-trace-vi.html language=enus -->
## TOPIC 00179: RFmxWLAN OFDMModAcc Fetch Subcarrier Chain EVM per Symbol Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-subcarrier-chain-evm-per-symbol-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-subcarrier-chain-evm-per-symbol-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chain EVM per symbol trace for a subcarrier. For unoccupied subcarriers, the trace value is NaN. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signa

### RFmxWLAN OFDMModAcc Fetch Subcarrier Chain EVM per Symbol Trace VI

Fetches the chain EVM per symbol trace for a subcarrier. For unoccupied subcarriers, the trace value is NaN.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-subcarrier-chain-evm-per-symbol-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. Subcarrier Index — Subcarrier Index specifies the subcarrier index for which the trace is fetched. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Subcarrier Chain EVM per Symbol (dB or %) — Subcarrier Chain EVM per Symbol returns the chain EVM per symbol trace for a subcarrier. x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns an array of chain EVM of each OFDM symbol for the specified subcarrier index. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns an array of chain EVM of each OFDM symbol for the specified subcarrier index. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-subcarrier-stream-evm-per-symbol-trace-vi.html language=enus -->
## TOPIC 00180: RFmxWLAN OFDMModAcc Fetch Subcarrier Stream EVM per Symbol Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-subcarrier-stream-evm-per-symbol-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-subcarrier-stream-evm-per-symbol-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream EVM per symbol trace for a subcarrier. Use "segment<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream nu

### RFmxWLAN OFDMModAcc Fetch Subcarrier Stream EVM per Symbol Trace VI

Fetches the stream EVM per symbol trace for a subcarrier.

Use "segment<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-subcarrier-stream-evm-per-symbol-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0". Example: "segment0/stream0" "signal::sig1/segment0/stream0" "signal::sig1/result::r1/segment0/stream0" "result::r1/segment0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. Subcarrier Index — Subcarrier Index specifies the subcarrier index for which to fetch the trace. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Subcarrier Stream EVM per Symbol (dB or %) — Subcarrier Stream EVM per Symbol returns the stream EVM per symbol trace for a subcarrier. For unoccupied subcarriers, the trace value is NaN. x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream EVM of each OFDM symbol for the specified subcarrier index. This value is expressed as a percentage or in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream EVM of each OFDM symbol for the specified subcarrier index. This value is expressed as a percentage or in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-symbol-chain-evm-per-subcarrier-trace-vi.html language=enus -->
## TOPIC 00181: RFmxWLAN OFDMModAcc Fetch Symbol Chain EVM per Subcarrier Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-symbol-chain-evm-per-subcarrier-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-symbol-chain-evm-per-subcarrier-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chain EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector strin

### RFmxWLAN OFDMModAcc Fetch Symbol Chain EVM per Subcarrier Trace VI

Fetches the chain EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-symbol-chain-evm-per-subcarrier-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. Symbol Index — Symbol Index specifies the symbol index for which to fetch the trace. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Symbol Chain EVM per Subcarrier (dB or %) — Symbol Chain EVM per Subcarrier fetches the chain EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN. x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of chain EVM for each subcarrier for the specified symbol index. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns an array of chain EVM for each subcarrier for the specified symbol index. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-symbol-clock-error-mean-vi.html language=enus -->
## TOPIC 00182: RFmxWLAN OFDMModAcc Fetch Symbol Clock Error Mean VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-symbol-clock-error-mean-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-symbol-clock-error-mean-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the symbol clock error of the transmitter. Use "segment<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the

### RFmxWLAN OFDMModAcc Fetch Symbol Clock Error Mean VI

Fetches the symbol clock error of the transmitter.

Use "segment<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-symbol-clock-error-mean-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0". Example: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxWLAN Build Segment String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Symbol Clock Error Mean (ppm) — Symbol Clock Error Mean returns the symbol clock error of the transmitter. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the symbol clock error results computed for each averaging count. This value is expressed in parts per million (ppm). error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-symbol-stream-evm-per-subcarrier-trace-vi.html language=enus -->
## TOPIC 00183: RFmxWLAN OFDMModAcc Fetch Symbol Stream EVM per Subcarrier Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-symbol-stream-evm-per-subcarrier-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-symbol-stream-evm-per-subcarrier-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream EVM per subcarrier trace for a symbol. Use "segment<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream nu

### RFmxWLAN OFDMModAcc Fetch Symbol Stream EVM per Subcarrier Trace VI

Fetches the stream EVM per subcarrier trace for a symbol.

Use "segment<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-symbol-stream-evm-per-subcarrier-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/stream0". Example: "segment0/stream0" "signal::sig1/segment0/stream0" "signal::sig1/result::r1/segment0/stream0" "result::r1/segment0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. Symbol Index — Symbol Index specifies the symbol index for which to fetch the trace. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Symbol Stream EVM per Subcarrier (dB or %) — Symbol Stream EVM per Subcarrier returns the stream EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN. x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns the stream EVM for each subcarrier for the specified symbol index. This value is expressed as a percentage or in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns the stream EVM for each subcarrier for the specified symbol index. This value is expressed as a percentage or in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-unused-tone-error-margin-per-ru-vi.html language=enus -->
## TOPIC 00184: RFmxWLAN OFDMModAcc Fetch Unused Tone Error Margin per RU VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-unused-tone-error-margin-per-ru-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-unused-tone-error-margin-per-ru-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the unused tone error margin result per RU. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If

### RFmxWLAN OFDMModAcc Fetch Unused Tone Error Margin per RU VI

Fetches the unused tone error margin result per RU.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-unused-tone-error-margin-per-ru-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Unused Tone Error Margin per RU (dB) — Unused Tone Error Margin per RU returns an array of unused tone error margin per RU, which is the difference between the unused tone error mask and the unused tone error for each RU. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-unused-tone-error-mean-trace-vi.html language=enus -->
## TOPIC 00185: RFmxWLAN OFDMModAcc Fetch Unused Tone Error Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-unused-tone-error-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-unused-tone-error-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the unused tone error trace and the unused tone error mask trace. When you set the OFDMModAcc Averaging Enabled property to True, this VI returns the mean of the unused tone error computed for each averaging count. Use "segment<n>/chain<k>" as the selector string to read results from this VI

### RFmxWLAN OFDMModAcc Fetch Unused Tone Error Mean Trace VI

Fetches the unused tone error trace and the unused tone error mask trace. When you set the [OFDMModAcc Averaging Enabled](/csh?context=rfmxwlan_rfmxwlanprop_attra04002) property to **True**, this VI returns the mean of the unused tone error computed for each averaging count.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-unused-tone-error-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Unused Tone Error (dB) — Unused Tone Error returns the unused tone error trace. x0 — x0 returns the starting RU index. This value is always 0. dx — dx returns the RU increment value. This value is always 1. y — y returns an array of unused tone error for each RU. This value is expressed in dB. Unused Tone Error Mask (dB) — Unused Tone Error Mask returns the unused tone error mask trace. x0 — x0 returns the starting RU index. This value is always 0. dx — dx returns the RU increment value. This value is always 1. y — y returns an array of unused tone error mask for each RU. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting RU index. This value is always 0. dx — dx returns the RU increment value. This value is always 1. y — y returns an array of unused tone error for each RU. This value is expressed in dB. |
| x0 — x0 returns the starting RU index. This value is always 0. dx — dx returns the RU increment value. This value is always 1. y — y returns an array of unused tone error mask for each RU. This value is expressed in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-unused-tone-error-vi.html language=enus -->
## TOPIC 00186: RFmxWLAN OFDMModAcc Fetch Unused Tone Error VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-unused-tone-error-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-unused-tone-error-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the unused tone error margin results. Refer to Unused Tone Error Measurement for more information. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal

### RFmxWLAN OFDMModAcc Fetch Unused Tone Error VI

Fetches the unused tone error margin results.

Refer to [Unused Tone Error Measurement](/csh?context=rfmxwlan_rfmxwlan_unused_tone_error_mx) for more information.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-unused-tone-error-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Unused Tone Error Margin (dB) — Unused Tone Error Margin returns the unused tone error margin, which is the minimum difference between the unused tone error mask and the unused tone error across 26-tone RUs. This value is expressed in dB. Unused Tone Error Margin RU Index — Unused Tone Error Margin RU Index returns the 26-tone RU index corresponding to the Unused Tone Error Margin parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-data-constellation-trace-vi.html language=enus -->
## TOPIC 00187: RFmxWLAN OFDMModAcc Fetch User Data Constellation Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-data-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-data-constellation-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace for the data-subcarriers of each user. Use "user<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, user number, and st

### RFmxWLAN OFDMModAcc Fetch User Data Constellation Trace VI

Fetches the constellation trace for the data-subcarriers of each user.

Use "user<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-user-data-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, user number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0/stream0". Example: "user0/stream0" "signal::sig1/user0/stream0" "signal::sig1/result::r1/user0/stream0" "result::r1/user0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. User Data Constellation — User Data Constellation returns the demodulated QAM symbols from all the data-subcarriers in all of the OFDM symbols for each user. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-pilot-constellation-trace-vi.html language=enus -->
## TOPIC 00188: RFmxWLAN OFDMModAcc Fetch User Pilot Constellation Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-pilot-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-pilot-constellation-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the constellation trace for the pilot-subcarriers of each user. Use "user<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, user number, and s

### RFmxWLAN OFDMModAcc Fetch User Pilot Constellation Trace VI

Fetches the constellation trace for the pilot-subcarriers of each user.

Use "user<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-user-pilot-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, user number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0/stream0". Example: "user0/stream0" "signal::sig1/user0/stream0" "signal::sig1/result::r1/user0/stream0" "result::r1/user0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. User Pilot Constellation — User Pilot Constellation returns the demodulated QAM symbols from all the pilot-subcarriers in all of the OFDM symbols for each user. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-power-vi.html language=enus -->
## TOPIC 00189: RFmxWLAN OFDMModAcc Fetch User Power VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-power-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the user power. Use "user<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal i

### RFmxWLAN OFDMModAcc Fetch User Power VI

Fetches the user power.

Use "user<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-user-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0". Example: "user0" "signal::sig1/user0" "signal::sig1/result::r1/user0" "result::r1/user0" You can use the RFmxWLAN Build User String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. User Power Mean (dBm) — User Power Mean returns the user power. User power is the frequency domain power measured over subcarriers occupied by a given user. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the user power results computed for each averaging count. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-data-rms-evm-per-symbol-mean-trace-vi.html language=enus -->
## TOPIC 00190: RFmxWLAN OFDMModAcc Fetch User Stream Data RMS EVM per Symbol Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-data-rms-evm-per-symbol-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-data-rms-evm-per-symbol-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream data-subcarriers RMS EVM per symbol trace for each user. When you set the OFDMModAcc Averaging Enabled property to True, this VI returns the mean of the user stream data RMS EVM per symbol computed for each averaging count. Use "user<n>/stream<k>" as the selector string to read re

### RFmxWLAN OFDMModAcc Fetch User Stream Data RMS EVM per Symbol Mean Trace VI

Fetches the stream data-subcarriers RMS EVM per symbol trace for each user. When you set the [OFDMModAcc Averaging Enabled](/csh?context=rfmxwlan_rfmxwlanprop_attra04002) property to **True**, this VI returns the mean of the user stream data RMS EVM per symbol computed for each averaging count.

Use "user<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-user-stream-data-rms-evm-per-symbol-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, user number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0/stream0". Example: "user0/stream0" "signal::sig1/user0/stream0" "signal::sig1/result::r1/user0/stream0" "result::r1/user0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. User Stream Data RMS EVM per Symbol Mean (dB or %) — User Stream Data RMS EVM per Symbol Mean (dB or %) returns the stream data-subcarriers RMS EVM per symbol trace for each user. When you set the Averaging Enabled property to True, this parameter returns the mean of the user stream data RMS EVM per symbol computed for each averaging count. x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream data subcarriers RMS EVM of each OFDM symbol for each user. This value is expressed as a percentage or in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream data subcarriers RMS EVM of each OFDM symbol for each user. This value is expressed as a percentage or in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-pilot-rms-evm-per-symbol-mean-trace-vi.html language=enus -->
## TOPIC 00191: RFmxWLAN OFDMModAcc Fetch User Stream Pilot RMS EVM per Symbol Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-pilot-rms-evm-per-symbol-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-pilot-rms-evm-per-symbol-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream pilot-subcarriers RMS EVM per symbol trace for each user. Use "user<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, user number,

### RFmxWLAN OFDMModAcc Fetch User Stream Pilot RMS EVM per Symbol Mean Trace VI

Fetches the stream pilot-subcarriers RMS EVM per symbol trace for each user.

Use "user<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-user-stream-pilot-rms-evm-per-symbol-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, user number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0/stream0". Example: "user0/stream0" "signal::sig1/user0/stream0" "signal::sig1/result::r1/user0/stream0" "result::r1/user0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. User Stream Pilot RMS EVM per Symbol Mean (dB or %) — User Stream Pilot RMS EVM per Symbol Mean (dB or %) returns the stream pilot-subcarriers RMS EVM per symbol trace for each user. When you set the Averaging Enabled property to True, this parameter returns the mean of the user stream pilot RMS EVM per symbol computed for each averaging count. x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream pilot subcarriers RMS EVM of each OFDM symbol for each user. This value is expressed as a percentage or in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream pilot subcarriers RMS EVM of each OFDM symbol for each user. This value is expressed as a percentage or in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-per-subcarrier-mean-trace-vi.html language=enus -->
## TOPIC 00192: RFmxWLAN OFDMModAcc Fetch User Stream RMS EVM per Subcarrier Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-per-subcarrier-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-per-subcarrier-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream RMS EVM per subcarrier trace for each user. When you set the OFDMModAcc Averaging Enabled property to True, this VI returns the mean of the user stream RMS EVM per subcarrier computed for each averaging count. Use "user<n>/stream<k>" as the selector string to read results from thi

### RFmxWLAN OFDMModAcc Fetch User Stream RMS EVM per Subcarrier Mean Trace VI

Fetches the stream RMS EVM per subcarrier trace for each user. When you set the [OFDMModAcc Averaging Enabled](/csh?context=rfmxwlan_rfmxwlanprop_attra04002) property to **True**, this VI returns the mean of the user stream RMS EVM per subcarrier computed for each averaging count.

Use "user<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-per-subcarrier-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, user number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0/stream0". Example: "user0/stream0" "signal::sig1/user0/stream0" "signal::sig1/result::r1/user0/stream0" "result::r1/user0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. User Stream RMS EVM per Subcarrier Mean (dB or %) — User Stream RMS EVM per Subcarrier Mean (dB or %) returns the stream RMS EVM per subcarrier trace for each user. When you set the Averaging Enabled property to True, this parameter returns the mean of the user stream RMS EVM per subcarrier computed for each averaging count. x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns the user stream RMS EVM for each subcarrier. This value is expressed as a percentage or in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting subcarrier index. dx — dx returns the subcarrier increment value. This value is always 1. y — y returns the user stream RMS EVM for each subcarrier. This value is expressed as a percentage or in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-per-symbol-mean-trace-vi.html language=enus -->
## TOPIC 00193: RFmxWLAN OFDMModAcc Fetch User Stream RMS EVM per Symbol Mean Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-per-symbol-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-per-symbol-mean-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream RMS EVM per symbol trace for each user. When you set the OFDMModAcc Averaging Enabled property to True, this VI returns the mean of the user stream RMS EVM per symbol computed for each averaging count. Use "user<n>/stream<k>" as the selector string to read results from this VI. ic

### RFmxWLAN OFDMModAcc Fetch User Stream RMS EVM per Symbol Mean Trace VI

Fetches the stream RMS EVM per symbol trace for each user. When you set the [OFDMModAcc Averaging Enabled](/csh?context=rfmxwlan_rfmxwlanprop_attra04002) property to **True**, this VI returns the mean of the user stream RMS EVM per symbol computed for each averaging count.

Use "user<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-per-symbol-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, user number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0/stream0". Example: "user0/stream0" "signal::sig1/user0/stream0" "signal::sig1/result::r1/user0/stream0" "result::r1/user0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. User Stream RMS EVM per Symbol Mean (dB or %) — User Stream RMS EVM per Symbol Mean (dB or %) returns the stream RMS EVM per symbol trace for each user. When you set the Averaging Enabled property to True, this parameter returns the mean of the user stream RMS EVM per symbol computed for each averaging count. x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream RMS EVM of each OFDM symbol for each user. This value is expressed as a percentage or in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting OFDM symbol index corresponding to the value of OFDMModAcc Meas Offset property. dx — dx returns the OFDM symbol increment value. This value is always equal to 1. y — y returns the stream RMS EVM of each OFDM symbol for each user. This value is expressed as a percentage or in dB. |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-vi.html language=enus -->
## TOPIC 00194: RFmxWLAN OFDMModAcc Fetch User Stream RMS EVM VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the stream RMS EVM results for the specified user. Use "user<n>/stream<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, user number, and stream number.

### RFmxWLAN OFDMModAcc Fetch User Stream RMS EVM VI

Fetches the stream RMS EVM results for the specified user.

Use "user<*n*>/stream<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, user number, and stream number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "user0/stream0". Example: "user0/stream0" "signal::sig1/user0/stream0" "signal::sig1/result::r1/user0/stream0" "result::r1/user0/stream0" You can use the RFmxWLAN Build Stream String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. User Stream RMS EVM Mean (dB or %) — User Stream RMS EVM Mean returns the RMS EVM of all subcarriers in all OFDM symbols for the specified user. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the user stream RMS EVM computed for each averaging count. User Stream Data RMS EVM Mean (dB or %) — User Stream Data RMS EVM Mean returns the RMS EVM of data-subcarriers in all OFDM symbols for the specified user. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the user stream data RMS EVM computed for each averaging count. User Stream Pilot RMS EVM Mean (dB or %) — User Stream Pilot RMS EVM Mean returns the RMS EVM of pilot-subcarriers in all OFDM symbols for the specified user. When you set the OFDMModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the OFDMModAcc EVM Unit property to dB, the measurement returns this result in dB. When you set the OFDMModAcc Averaging Enabled property to True, this parameter returns the mean of the user stream pilot RMS EVM computed for each averaging count. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN OFDMModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-vi.html language=enus -->
## TOPIC 00195: RFmxWLAN OFDMModAcc Fetch VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the OFDMModAcc measurement results. icon

### RFmxWLAN OFDMModAcc Fetch VI

Fetches the OFDMModAcc measurement results.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-fetch-vi.png']

- [RFmxWLAN OFDMModAcc Fetch Composite RMS EVM VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-composite-rms-evm-vi.html) Fetches the composite RMS EVM results.
- [RFmxWLAN OFDMModAcc Fetch Stream RMS EVM VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-vi.html) Fetches the stream RMS EVM results.
- [RFmxWLAN OFDMModAcc Fetch Chain RMS EVM VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-chain-rms-evm-vi.html) Fetches the chain RMS EVM results.
- [RFmxWLAN OFDMModAcc Fetch User Stream RMS EVM VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-vi.html) Fetches the stream RMS EVM results for the specified user.
- [RFmxWLAN OFDMModAcc Fetch Frequency Error Mean VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-frequency-error-mean-vi.html) Fetches the carrier frequency error of the transmitter.
- [RFmxWLAN OFDMModAcc Fetch Frequency Error CCDF 10 Percent VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-frequency-error-ccdf-10-percent-vi.html) Fetches the 10% point of the complementary cumulative distribution function (CCDF) of frequency error across the number of iterations.
- [RFmxWLAN OFDMModAcc Fetch Symbol Clock Error Mean VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-symbol-clock-error-mean-vi.html) Fetches the symbol clock error of the transmitter.
- [RFmxWLAN OFDMModAcc Fetch IQ Impairments VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-iq-impairments-vi.html) Fetches the I/Q Impairment results for the OFDMModAcc measurement.
- [RFmxWLAN OFDMModAcc Fetch Spectral Flatness VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-spectral-flatness-vi.html) Fetches the spectral flatness margin results.
- [RFmxWLAN OFDMModAcc Fetch Number of Symbols Used VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-symbols-used-vi.html) Fetches the number of OFDM symbols used for EVM measurement.
- [RFmxWLAN OFDMModAcc Fetch Number of Space Time Streams VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-space-time-streams-vi.html) Fetches the number of space time streams.
- [RFmxWLAN OFDMModAcc Fetch PPDU Type VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ppdu-type-vi.html) Fetches the PPDU type.
- [RFmxWLAN OFDMModAcc Fetch MCS Index VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-mcs-index-vi.html) Fetches the MCS index.
- [RFmxWLAN OFDMModAcc Fetch RU Offset and Size VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ru-offset-and-size-vi.html) Fetches the RU offset and the RU size of the specified user.
- [RFmxWLAN OFDMModAcc Fetch Number of Users VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-users-vi.html) Fetches the number of users.
- [RFmxWLAN OFDMModAcc Fetch Number of HE-SIG-B Symbols VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-number-of-he-sig-b-symbols-vi.html) Fetches the number of HE-SIG-B symbols.
- [RFmxWLAN OFDMModAcc Fetch Guard Interval Type VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-guard-interval-type-vi.html) Fetches the guard interval type.
- [RFmxWLAN OFDMModAcc Fetch LTF Size VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ltf-size-vi.html) Fetches the HE-LTF or EHT-LTF size for 802.11ax or 802.11be, respectively.
- [RFmxWLAN OFDMModAcc Fetch L-SIG Parity Check Status VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-l-sig-parity-check-status-vi.html) Fetches the L-SIG parity check status.
- [RFmxWLAN OFDMModAcc Fetch SIG CRC Status VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-sig-crc-status-vi.html) Fetches the SIG CRC Status.
- [RFmxWLAN OFDMModAcc Fetch SIG-B CRC Status VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-sig-b-crc-status-vi.html) Fetches the SIG-B CRC Status.
- [RFmxWLAN OFDMModAcc Fetch PSDU CRC Status VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-psdu-crc-status-vi.html) Fetches the PLCP service data unit (PSDU) CRC status.
- [RFmxWLAN OFDMModAcc Fetch PE Duration VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pe-duration-vi.html) Fetches the duration of the packet extension field.
- [RFmxWLAN OFDMModAcc Fetch Data Average Power VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-data-average-power-vi.html) Fetches the average power of the data field.
- [RFmxWLAN OFDMModAcc Fetch Data Peak Power VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-data-peak-power-vi.html) Fetches the peak power of the data field.
- [RFmxWLAN OFDMModAcc Fetch PPDU Average Power VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ppdu-average-power-vi.html) Fetches the average power of the PPDU.
- [RFmxWLAN OFDMModAcc Fetch PPDU Peak Power VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-ppdu-peak-power-vi.html) Fetches the peak power of the PPDU.
- [RFmxWLAN OFDMModAcc Fetch PE Average Power VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pe-average-power-vi.html) Fetches the average power of the packet extension field.
- [RFmxWLAN OFDMModAcc Fetch PE Peak Power VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pe-peak-power-vi.html) Fetches the peak power of the packet extension field.
- [RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (Common) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-common-vi.html) Fetches the average power of the preamble fields.
- [RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (Common) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-common-vi.html) Fetches the peak power of the preamble fields.
- [RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (802.11n) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11n-vi.html) Fetches the average power of the 802.11n specific preamble fields.
- [RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (802.11n) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11n-vi.html) Fetches the peak power of the 802.11n specific preamble fields.
- [RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (802.11ac) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11ac-vi.html) Fetches the average power of the 802.11ac specific preamble fields.
- [RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (802.11ac) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11ac-vi.html) Fetches the peak power of the 802.11ac specific preamble fields.
- [RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (802.11ax) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11ax-vi.html) Fetches the average power of the 802.11ax specific preamble fields.
- [RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (802.11ax) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11ax-vi.html) Fetches the peak power of the 802.11ax specific preamble fields.
- [RFmxWLAN OFDMModAcc Fetch Preamble Average Powers (802.11be) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-average-powers-802-11be-vi.html) Fetches the average power of the 802.11be specific preamble fields.
- [RFmxWLAN OFDMModAcc Fetch Preamble Peak Powers (802.11be) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-peak-powers-802-11be-vi.html) Fetches the peak power of the 802.11be specific preamble fields.
- [RFmxWLAN OFDMModAcc Fetch Custom Gate Powers (Array) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-custom-gate-powers-array-vi.html) Fetches the average and peak power of the custom gates.
- [RFmxWLAN OFDMModAcc Fetch Cross Power VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-cross-power-vi.html) Fetches the cross power.
- [RFmxWLAN OFDMModAcc Fetch User Power VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-power-vi.html) Fetches the user power.
- [RFmxWLAN OFDMModAcc Fetch Unused Tone Error VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-unused-tone-error-vi.html) Fetches the unused tone error margin results.
- [RFmxWLAN OFDMModAcc Fetch Unused Tone Error Margin per RU VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-unused-tone-error-margin-per-ru-vi.html) Fetches the unused tone error margin result per RU.
- [RFmxWLAN OFDMModAcc Fetch EVM Subcarrier Indices VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-evm-subcarrier-indices-vi.html) Fetches the array of subcarrier indices for which the EVM results are computed.
- [RFmxWLAN OFDMModAcc Fetch Data Constellation Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-data-constellation-trace-vi.html) Fetches the constellation trace for the data-subcarriers.
- [RFmxWLAN OFDMModAcc Fetch Reference Data Constellation Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-reference-data-constellation-trace-vi.html) Fetches the reference constellation trace for the data-subcarriers.
- [RFmxWLAN OFDMModAcc Fetch Pilot Constellation Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-pilot-constellation-trace-vi.html) Fetches the constellation trace for the pilot-subcarriers.
- [RFmxWLAN OFDMModAcc Fetch User Data Constellation Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-data-constellation-trace-vi.html) Fetches the constellation trace for the data-subcarriers of each user.
- [RFmxWLAN OFDMModAcc Fetch User Pilot Constellation Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-pilot-constellation-trace-vi.html) Fetches the constellation trace for the pilot-subcarriers of each user.
- [RFmxWLAN OFDMModAcc Fetch Stream RMS EVM per Subcarrier Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-per-subcarrier-mean-trace-vi.html) Fetches the stream RMS EVM per subcarrier trace.
- [RFmxWLAN OFDMModAcc Fetch Stream RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-rms-evm-per-symbol-mean-trace-vi.html) Fetches the stream RMS EVM per symbol trace.
- [RFmxWLAN OFDMModAcc Fetch Stream Data RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-data-rms-evm-per-symbol-mean-trace-vi.html) Fetches the stream data subcarriers RMS EVM per symbol trace.
- [RFmxWLAN OFDMModAcc Fetch Stream Pilot RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-stream-pilot-rms-evm-per-symbol-mean-trace-vi.html) Fetches the stream pilot subcarriers RMS EVM per symbol trace.
- [RFmxWLAN OFDMModAcc Fetch Chain RMS EVM per Subcarrier Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-chain-rms-evm-per-subcarrier-mean-trace-vi.html) Fetches the chain RMS EVM per subcarrier trace. When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the mean of the chain RMS EVM per subcarrier computed for each averaging count.
- [RFmxWLAN OFDMModAcc Fetch Chain RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-chain-rms-evm-per-symbol-mean-trace-vi.html) Fetches the chain RMS EVM per symbol trace. When you set the When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the mean of the chain RMS EVM per symbol computed for each averaging count.
- [RFmxWLAN OFDMModAcc Fetch Chain Data RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-chain-data-rms-evm-per-symbol-mean-trace-vi.html) Fetches the chain data-subcarriers RMS EVM per symbol trace. When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the mean of the chain data RMS EVM per symbol computed for each averaging count.
- [RFmxWLAN OFDMModAcc Fetch Chain Pilot RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-chain-pilot-rms-evm-per-symbol-mean-trace-vi.html) Fetches the chain pilot-subcarriers RMS EVM per symbol trace. When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the mean of the chain pilot RMS EVM per symbol computed for each averaging count.
- [RFmxWLAN OFDMModAcc Fetch User Stream RMS EVM per Subcarrier Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-per-subcarrier-mean-trace-vi.html) Fetches the stream RMS EVM per subcarrier trace for each user. When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the mean of the user stream RMS EVM per subcarrier computed for each averaging count.
- [RFmxWLAN OFDMModAcc Fetch User Stream RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-rms-evm-per-symbol-mean-trace-vi.html) Fetches the stream RMS EVM per symbol trace for each user. When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the mean of the user stream RMS EVM per symbol computed for each averaging count.
- [RFmxWLAN OFDMModAcc Fetch User Stream Data RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-data-rms-evm-per-symbol-mean-trace-vi.html) Fetches the stream data-subcarriers RMS EVM per symbol trace for each user. When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the mean of the user stream data RMS EVM per symbol computed for each averaging count.
- [RFmxWLAN OFDMModAcc Fetch User Stream Pilot RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-user-stream-pilot-rms-evm-per-symbol-mean-trace-vi.html) Fetches the stream pilot-subcarriers RMS EVM per symbol trace for each user.
- [RFmxWLAN OFDMModAcc Fetch Subcarrier Stream EVM per Symbol Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-subcarrier-stream-evm-per-symbol-trace-vi.html) Fetches the stream EVM per symbol trace for a subcarrier.
- [RFmxWLAN OFDMModAcc Fetch Subcarrier Chain EVM per Symbol Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-subcarrier-chain-evm-per-symbol-trace-vi.html) Fetches the chain EVM per symbol trace for a subcarrier. For unoccupied subcarriers, the trace value is NaN.
- [RFmxWLAN OFDMModAcc Fetch Symbol Stream EVM per Subcarrier Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-symbol-stream-evm-per-subcarrier-trace-vi.html) Fetches the stream EVM per subcarrier trace for a symbol.
- [RFmxWLAN OFDMModAcc Fetch Symbol Chain EVM per Subcarrier Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-symbol-chain-evm-per-subcarrier-trace-vi.html) Fetches the chain EVM per subcarrier trace for a symbol. For symbol indices outside the measurement interval, the trace value is NaN.
- [RFmxWLAN OFDMModAcc Fetch Spectral Flatness Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-spectral-flatness-mean-trace-vi.html) Fetches the spectral flatness trace, and the lower and upper spectral flatness mask traces. When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the spectral flatness trace computed on the mean of the channel estimates computed for each averaging count.
- [RFmxWLAN OFDMModAcc Fetch Common Pilot Error Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-common-pilot-error-trace-vi.html) Fetches the common pilot error magnitude and phase traces.
- [RFmxWLAN OFDMModAcc Fetch Phase Noise PSD Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-phase-noise-psd-mean-trace-vi.html) Fetches the phase noise power spectral density (PSD) trace for signals containing an OFDM payload.
- [RFmxWLAN OFDMModAcc Fetch Preamble Frequency Error Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-preamble-frequency-error-trace-vi.html) Fetches the preamble frequency error trace for signals containing an OFDM payload. Preamble frequency error computes the variations, across time, of the frequency error over initial 16us which comprises of the short training field (STF) and long training field (LTF) symbols.
- [RFmxWLAN OFDMModAcc Fetch Channel Frequency Response Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-channel-frequency-response-mean-trace-vi.html) Fetches the channel frequency response trace. When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the mean of the channel frequency response trace computed for each averaging count.
- [RFmxWLAN OFDMModAcc Fetch IQ Gain Imbalance per Subcarrier Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-iq-gain-imbalance-per-subcarrier-mean-trace-vi.html) Fetches the I/Q gain imbalance per subcarrier trace. When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the mean of the I/Q gain imbalance computed for each averaging count.
- [RFmxWLAN OFDMModAcc Fetch IQ Quadrature Error per Subcarrier Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-iq-quadrature-error-per-subcarrier-mean-trace-vi.html) Fetches the I/Q quadrature error per subcarrier trace. When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the mean of the I/Q quadrature error computed for each averaging count.
- [RFmxWLAN OFDMModAcc Fetch Unused Tone Error Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-unused-tone-error-mean-trace-vi.html) Fetches the unused tone error trace and the unused tone error mask trace. When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the mean of the unused tone error computed for each averaging count.
- [RFmxWLAN OFDMModAcc Fetch Decoded L-SIG Bits Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-l-sig-bits-trace-vi.html) Fetches the decoded L-SIG bits trace.
- [RFmxWLAN OFDMModAcc Fetch Decoded SIG Bits Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-sig-bits-trace-vi.html) Fetches the decoded SIG bits.
- [RFmxWLAN OFDMModAcc Fetch Decoded SIG-B Bits Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-sig-b-bits-trace-vi.html) Fetches the decoded SIG-B bits.
- [RFmxWLAN OFDMModAcc Fetch Decoded U-SIG Bits Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-u-sig-bits-trace-vi.html) Fetches the decoded U-SIG bits trace.
- [RFmxWLAN OFDMModAcc Fetch Decoded EHT-SIG Bits Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-eht-sig-bits-trace-vi.html) Fetches the decoded EHT-SIG bits trace.
- [RFmxWLAN OFDMModAcc Fetch Decoded PSDU Bits Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-psdu-bits-trace-vi.html) Fetches the decoded PLCP service data unit (PSDU) bits.
- [RFmxWLAN OFDMModAcc Fetch Decoded Service Bits Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-decoded-service-bits-trace-vi.html) Fetches the decoded Service bits.
- [RFmxWLAN OFDMModAcc Fetch Group Delay Mean Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-fetch-group-delay-mean-trace-vi.html) Fetches the group delay trace. Group delay is computed from the channel frequency response. When you set the OFDMModAcc Averaging Enabled property to True , this VI returns the mean of the group delay trace computed for each averaging count.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-validate-calibration-data-vi.html language=enus -->
## TOPIC 00196: RFmxWLAN OFDMModAcc Validate Calibration Data VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-validate-calibration-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-ofdmmodacc-validate-calibration-data-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether calibration data is valid for the configuration specified by the signal name in the Selector string parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default

### RFmxWLAN OFDMModAcc Validate Calibration Data VI

Indicates whether calibration data is valid for the configuration specified by the signal name in the **Selector string** parameter.

[IMAGE alt='icon' src='rfmxwlan-ofdmmodacc-validate-calibration-data-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Calibration Data Valid — Calibration Data Valid returns whether the calibration data is valid. False (0) Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. True (1) Returns true if the calibration data is present for the configuration specified by the signal name in the Selector string parameter. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Returns false if the calibration data is not present for the specified configuration or if the difference between the current device temperature and the calibration temperature exceeds the [-5 °C, 5 °C] range. |
| True (1) | Returns true if the calibration data is present for the configuration specified by the signal name in the Selector string parameter. |

Parent topic:

OFDMModAcc

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-configure-acquisition-length-vi.html language=enus -->
## TOPIC 00197: RFmxWLAN PowerRamp Configure Acquisition Length VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-configure-acquisition-length-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-configure-acquisition-length-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the waveform acquisition length for the measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).

### RFmxWLAN PowerRamp Configure Acquisition Length VI

Configures the waveform acquisition length for the measurement.

[IMAGE alt='icon' src='rfmxwlan-powerramp-configure-acquisition-length-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Acquisition Length (s) — Acquisition Length specifies the duration of the signal to be acquired for the PowerRamp measurement. This value is expressed in seconds. You must set this parameter to a value that is greater than or equal to the duration of the PPDU under analysis, so that the acquired signal contains both rising and falling power ramp transitions. The default value is 1 ms. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PowerRamp

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-configure-averaging-vi.html language=enus -->
## TOPIC 00198: RFmxWLAN PowerRamp Configure Averaging VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-configure-averaging-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::s

### RFmxWLAN PowerRamp Configure Averaging VI

Configures averaging for the measurement.

[IMAGE alt='icon' src='rfmxwlan-powerramp-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the PowerRamp measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. |

Parent topic:

PowerRamp

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-fall-trace-vi.html language=enus -->
## TOPIC 00199: RFmxWLAN PowerRamp Fetch Fall Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-fall-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-fall-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the raw, processed, thresholding and power reference waveforms at the end of a burst. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is

### RFmxWLAN PowerRamp Fetch Fall Trace VI

Returns the raw, processed, thresholding and power reference waveforms at the end of a burst.

[IMAGE alt='icon' src='rfmxwlan-powerramp-fetch-fall-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Power Reference (%) — Power Reference returns the power reference trace which indicates the 100% power level, corresponding to the steady state average power level of the final portion of the burst. x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of power reference values. This value is expressed as a percentage. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Raw Waveform (%) — Raw Waveform returns the power versus time trace of the acquired waveform at the end of the burst. x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of measured signal power. This value is expressed as a percentage. Processed Waveform (%) — Processed Waveform returns the power versus time trace of the power envelope of the acquired waveform at the end of the burst. x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of measured envelope power. This value is expressed as a percentage. Threshold (%) — Threshold returns the threshold trace indicating the 10 percent and the 90 percent power levels. x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of threshold values. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of power reference values. This value is expressed as a percentage. |
| x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of measured signal power. This value is expressed as a percentage. |
| x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of measured envelope power. This value is expressed as a percentage. |
| x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of threshold values. This value is expressed as a percentage. |

Parent topic:

RFmxWLAN PowerRamp Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-measurement-vi.html language=enus -->
## TOPIC 00200: RFmxWLAN PowerRamp Fetch Measurement VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-measurement-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the PowerRamp rise time and fall time. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, th

### RFmxWLAN PowerRamp Fetch Measurement VI

Returns the PowerRamp rise time and fall time.

[IMAGE alt='icon' src='rfmxwlan-powerramp-fetch-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Rise Time Mean (s) — Rise Time Mean returns the rise time of the acquired signal that is the amount of time taken for the power envelope to rise from a level of 10 percent to 90 percent. This value is expressed in seconds. When you set the PowerRamp Averaging Enabled property to True, this parameter returns the mean of the rise time computed for each averaging count. This value is expressed in seconds. Fall Time Mean (s) — Fall Time Mean returns the fall time of the acquired signal that is the amount of time taken for the power envelope to fall from a level of 90 percent to 10 percent. This value is expressed in seconds. When you set the PowerRamp Averaging Enabled property to True, this parameter returns the mean of the fall time computed for each averaging count. This value is expressed in seconds. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN PowerRamp Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-rise-trace-vi.html language=enus -->
## TOPIC 00201: RFmxWLAN PowerRamp Fetch Rise Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-rise-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-rise-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the raw, processed, threshold and power-reference traces at the beginning of a burst. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is

### RFmxWLAN PowerRamp Fetch Rise Trace VI

Returns the raw, processed, threshold and power-reference traces at the beginning of a burst.

[IMAGE alt='icon' src='rfmxwlan-powerramp-fetch-rise-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Power Reference (%) — Power Reference returns the power reference trace which indicates the 100% power level, corresponding to the steady state average power level of the initial portion of the burst. x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of power reference values. This value is expressed as a percentage. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Raw Waveform (%) — Raw Waveform returns the power versus time trace of the acquired waveform at the beginning of the burst. x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of measured signal power. This value is expressed as a percentage. Processed Waveform (%) — Processed Waveform returns the power versus time trace of the power envelope of the acquired waveform at the beginning of the burst. x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of measured envelope power. This value is expressed as a percentage. Threshold (%) — Threshold returns the threshold trace indicating the 10 percent and the 90 percent power levels. x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of threshold values. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of power reference values. This value is expressed as a percentage. |
| x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of measured signal power. This value is expressed as a percentage. |
| x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of measured envelope power. This value is expressed as a percentage. |
| x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of threshold values. This value is expressed as a percentage. |

Parent topic:

RFmxWLAN PowerRamp Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-vi.html language=enus -->
## TOPIC 00202: RFmxWLAN PowerRamp Fetch VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PowerRamp measurement results. icon

### RFmxWLAN PowerRamp Fetch VI

Fetches the PowerRamp measurement results.

[IMAGE alt='icon' src='rfmxwlan-powerramp-fetch-vi.png']

- [RFmxWLAN PowerRamp Fetch Measurement VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-measurement-vi.html) Returns the PowerRamp rise time and fall time.
- [RFmxWLAN PowerRamp Fetch Rise Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-rise-trace-vi.html) Returns the raw, processed, threshold and power-reference traces at the beginning of a burst.
- [RFmxWLAN PowerRamp Fetch Fall Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-powerramp-fetch-fall-trace-vi.html) Returns the raw, processed, thresholding and power reference waveforms at the end of a burst.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-property-node-vi.html language=enus -->
## TOPIC 00203: RFmxWLAN Property Node VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-property-node-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads), sets (writes), or resets (sets to default value) RFmxWLAN properties. icon Inputs/Outputs cgenclassrntag.png niRFmx Instrument Handle Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. cerrcodeclst.png error

### RFmxWLAN Property Node VI

Gets (reads), sets (writes), or resets (sets to default value) RFmxWLAN properties.

[IMAGE alt='icon' src='rfmxwlan-property-node-vi.png']

#### Inputs/Outputs

| niRFmx Instrument Handle — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Property — RFmx WLAN Property Node is used to get (read), set (write), or reset (set to default value) RFmx WLAN properties. niRFmx Instrument Handle — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

WLAN

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-reset-to-default-vi.html language=enus -->
## TOPIC 00204: RFmxWLAN Reset to Default VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-reset-to-default-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-reset-to-default-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1

### RFmxWLAN Reset to Default VI

Resets a signal to the default values.

[IMAGE alt='icon' src='rfmxwlan-reset-to-default-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-select-measurement-multiple-vi.html language=enus -->
## TOPIC 00205: RFmxWLAN Select Measurement (Multiple) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-select-measurement-multiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-select-measurement-multiple-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance

### RFmxWLAN Select Measurement (Multiple) VI

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxwlan-select-measurement-multiple-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Measurements — Measurements specifies the measurement to perform. You can specify one or more of the following measurements. The default is an empty array. TXP (0) Enables TXP measurement. PowerRamp (1) Enables PowerRamp measurement. DSSSModAcc (2) Enables DSSSModAcc measurement. OFDMModAcc (3) Enables OFDMModAcc measurement. SEM (4) Enables SEM measurement. Enable All Traces — Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TXP (0) | Enables TXP measurement. |
| PowerRamp (1) | Enables PowerRamp measurement. |
| DSSSModAcc (2) | Enables DSSSModAcc measurement. |
| OFDMModAcc (3) | Enables OFDMModAcc measurement. |
| SEM (4) | Enables SEM measurement. |

Parent topic:

RFmxWLAN Select Measurement VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-select-measurement-single-vi.html language=enus -->
## TOPIC 00206: RFmxWLAN Select Measurement (Single) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-select-measurement-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-select-measurement-single-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the measurement that you specify in the Measurement parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is use

### RFmxWLAN Select Measurement (Single) VI

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxwlan-select-measurement-single-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Measurement — Measurement specifies the measurement to perform. You can specify one of the following measurements. The default value is TXP. TXP (0) Enables TXP measurement. PowerRamp (1) Enables PowerRamp measurement. DSSSModAcc (2) Enables DSSSModAcc measurement. OFDMModAcc (3) Enables OFDMModAcc measurement. SEM (4) Enables SEM measurement. Enable All Traces — Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TXP (0) | Enables TXP measurement. |
| PowerRamp (1) | Enables PowerRamp measurement. |
| DSSSModAcc (2) | Enables DSSSModAcc measurement. |
| OFDMModAcc (3) | Enables OFDMModAcc measurement. |
| SEM (4) | Enables SEM measurement. |

Parent topic:

RFmxWLAN Select Measurement VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-select-measurement-vi.html language=enus -->
## TOPIC 00207: RFmxWLAN Select Measurement VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-select-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-select-measurement-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. icon

### RFmxWLAN Select Measurement VI

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

[IMAGE alt='icon' src='rfmxwlan-select-measurement-vi.png']

- [RFmxWLAN Select Measurement (Single) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-select-measurement-single-vi.html) Enables the measurement that you specify in the Measurement parameter and disables all other measurements.
- [RFmxWLAN Select Measurement (Multiple) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-select-measurement-multiple-vi.html) Enables all the measurements that you specify in the Measurements parameter and disables all other measurements.

Parent topic:

WLAN

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-averaging-vi.html language=enus -->
## TOPIC 00208: RFmxWLAN SEM Configure Averaging VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-averaging-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::s

### RFmxWLAN SEM Configure Averaging VI

Configures averaging for the measurement.

[IMAGE alt='icon' src='rfmxwlan-sem-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the SEM. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one record to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one record to the next. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one record to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one record to the next. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-mask-type-vi.html language=enus -->
## TOPIC 00209: RFmxWLAN SEM Configure Mask Type VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-mask-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-mask-type-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the mask type for the SEM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "s

### RFmxWLAN SEM Configure Mask Type VI

Configures the mask type for the SEM measurement.

[IMAGE alt='icon' src='rfmxwlan-sem-configure-mask-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Mask Type — Mask Type specifies whether the mask used for the SEM measurement is as per the 3GPP standard or specified by you. The default value is Standard. Standard (0) Mask limits are configured as per the standard. Custom (1) Mask limits are configured by you. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Standard (0) | Mask limits are configured as per the standard. |
| Custom (1) | Mask limits are configured by you. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-number-of-offsets-vi.html language=enus -->
## TOPIC 00210: RFmxWLAN SEM Configure Number of Offsets VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-number-of-offsets-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-number-of-offsets-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of offset segments for the SEM measurement when you set the SEM Mask Type property to Custom. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instan

### RFmxWLAN SEM Configure Number of Offsets VI

Configures the number of offset segments for the SEM measurement when you set the [SEM Mask Type](/csh?context=rfmxwlan_rfmxwlanprop_attra05002) property to **Custom**.

[IMAGE alt='icon' src='rfmxwlan-sem-configure-number-of-offsets-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Number of Offsets — Number of Offsets specifies the number of SEM offset segments. The default value is 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-offset-frequency-array-vi.html language=enus -->
## TOPIC 00211: RFmxWLAN SEM Configure Offset Frequency (Array) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-offset-frequency-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-offset-frequency-array-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the array of offset start and stop frequencies and specifies whether the offsets are present on one side, or on both the sides of the carrier when you set the SEM Mask Type property to Custom. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string compris

### RFmxWLAN SEM Configure Offset Frequency (Array) VI

Configures the array of offset start and stop frequencies and specifies whether the offsets are present on one side, or on both the sides of the carrier when you set the [SEM Mask Type](/csh?context=rfmxwlan_rfmxwlanprop_attra05002) property to **Custom**.

[IMAGE alt='icon' src='rfmxwlan-sem-configure-offset-frequency-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Offset Start Frequency (Hz) — Offset Start Frequency specifies the array of offset start frequencies, relative to the carrier frequency. This value is expressed in Hz. The default value is an empty array. Offset Stop Frequency (Hz) — Offset Stop Frequency specifies the array of offset stop frequencies, relative to the carrier frequency. This value is expressed in Hz. The default value is an empty array. Offset Sideband — Offset Sideband specifies whether the offset segments present on one or both sides of the carrier. The default value is Both. Neg (0) Configures a lower offset segment to the left of the carrier. Pos (1) Configures an upper offset segment to the right of the carrier. Both (2) Configures both negative and positive offset segments. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Neg (0) | Configures a lower offset segment to the left of the carrier. |
| Pos (1) | Configures an upper offset segment to the right of the carrier. |
| Both (2) | Configures both negative and positive offset segments. |

Parent topic:

SEM Array VIs

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-offset-relative-limit-array-vi.html language=enus -->
## TOPIC 00212: RFmxWLAN SEM Configure Offset Relative Limit (Array) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-offset-relative-limit-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-offset-relative-limit-array-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of relative mask limits corresponding the start and stop frequencies of the offsets when you set the SEM Mask Type property to Custom. The relative limits are relative to the peak power of the carrier. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selec

### RFmxWLAN SEM Configure Offset Relative Limit (Array) VI

Configures an array of relative mask limits corresponding the start and stop frequencies of the offsets when you set the [SEM Mask Type](/csh?context=rfmxwlan_rfmxwlanprop_attra05002) property to **Custom**. The relative limits are relative to the peak power of the carrier.

[IMAGE alt='icon' src='rfmxwlan-sem-configure-offset-relative-limit-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Relative Limit Start (dB) — Relative Limit Start specifies the array of relative power limits corresponding to the start frequencies of the offsets. The relative limits are relative to the peak power of the carrier. This value is expressed in dB. The default value is an empty array. Relative Limit Stop (dB) — Relative Limit Stop specifies the array of relative power limits corresponding to the stop frequencies of the offsets. The relative limits are relative to the peak power of the carrier. This value is expressed in dB. The default value is an empty array. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

SEM Array VIs

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-span-vi.html language=enus -->
## TOPIC 00213: RFmxWLAN SEM Configure Span VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-span-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-span-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency range around the center frequency to be acquired for the SEM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The d

### RFmxWLAN SEM Configure Span VI

Configures the frequency range around the center frequency to be acquired for the SEM measurement.

[IMAGE alt='icon' src='rfmxwlan-sem-configure-span-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Span Auto — Span Auto specifies whether the frequency range of the spectrum used for the SEM measurement is computed automatically by the measurement or is configured by you. This parameter is applicable when you set the SEM Mask Type property to Standard. The default value is True. False (0) The span you configure is used as the frequency range for the SEM measurement. True (1) The span is automatically computed based on the configured standard and bandwidth. Span (Hz) — Span specifies the frequency range of the spectrum that is used for the SEM measurement. This value is expressed in Hz. This parameter is applicable only when you set the Span Auto parameter to False, and the SEM Mask Type property to Standard. The default value is 66 MHz. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The span you configure is used as the frequency range for the SEM measurement. |
| True (1) | The span is automatically computed based on the configured standard and bandwidth. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-sweep-time-vi.html language=enus -->
## TOPIC 00214: RFmxWLAN SEM Configure Sweep Time VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-sweep-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-configure-sweep-time-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can us

### RFmxWLAN SEM Configure Sweep Time VI

Configures the sweep time.

[IMAGE alt='icon' src='rfmxwlan-sem-configure-sweep-time-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Sweep Time Auto — Sweep Time Auto specifies whether the sweep time for the SEM measurement is computed automatically by the measurement or is configured by you. The default value is True. False (0) The sweep time you configure using the Sweep Time parameter is used as the sweep time for the SEM measurement. True (1) The sweep time is computed automatically based on the configured standard. Sweep Time Interval (s) — Sweep Time Interval (s) specifies the sweep time for the SEM measurement. This value is expressed in seconds. This parameter is ignored when you set the SEM Sweep Time Auto parameter to False. The default value is 1 ms. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The sweep time you configure using the Sweep Time parameter is used as the sweep time for the SEM measurement. |
| True (1) | The sweep time is computed automatically based on the configured standard. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-carrier-measurement-vi.html language=enus -->
## TOPIC 00215: RFmxWLAN SEM Fetch Carrier Measurement VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-carrier-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-carrier-measurement-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative carrier power measurements. The relative power is relative to the peak power of the carrier. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string compr

### RFmxWLAN SEM Fetch Carrier Measurement VI

Returns the absolute and relative carrier power measurements. The relative power is relative to the peak power of the carrier.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-sem-fetch-carrier-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Absolute Power (dBm) — Absolute Power returns the average power of the carrier channel over the bandwidth indicated by the SEM Carrier IBW property. This value is expressed in dBm. Relative Power (dB) — Relative Power returns the average power of the carrier channel, relative to the peak power of the carrier channel, over the bandwidth indicated by the SEM Carrier IBW property. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-margin-array-vi.html language=enus -->
## TOPIC 00216: RFmxWLAN SEM Fetch Lower Offset Margin (Array) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-margin-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-margin-array-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of measurement status, margins, margin-frequencies, and absolute and relative powers corresponding to the margin-frequencies for lower offset segments. The relative powers are relative to the peak power in the carrier. Use "segment<n>/chain<k>" as the selector string to read results

### RFmxWLAN SEM Fetch Lower Offset Margin (Array) VI

Returns an array of measurement status, margins, margin-frequencies, and absolute and relative powers corresponding to the margin-frequencies for lower offset segments. The relative powers are relative to the peak power in the carrier.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-sem-fetch-lower-offset-margin-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns an array of relative powers corresponding to the margins for the lower offsets. The relative powers are relative to the peak power of the carrier channel. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns an array of absolute powers corresponding to the margins for the lower offsets. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Measurement Status — Measurement Status returns an array of lower (negative) offset segment measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in the lower offset segments. Fail (0) The spectrum exceeds the SEM measurement mask limits the lower offset segment. Pass (1) The spectrum does not exceed the SEM measurement mask limits for the lower offset segment. Margin (dB) — Margin returns an array of margins from the SEM measurement mask for the lower offset. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the mask. Margin Frequency (Hz) — Margin Frequency returns an array of frequencies corresponding to the margins for the lower (negative) offsets. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The spectrum exceeds the SEM measurement mask limits the lower offset segment. |
| Pass (1) | The spectrum does not exceed the SEM measurement mask limits for the lower offset segment. |

Parent topic:

RFmxWLAN SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-margin-vi.html language=enus -->
## TOPIC 00217: RFmxWLAN SEM Fetch Lower Offset Margin VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-margin-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-margin-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status, margin, margin-frequency, and absolute and relative power corresponding to the margin-frequency for lower offset segment. The relative power is relative to the peak power in the carrier. Use "segment<n>/chain<k>/offset<l>" as the selector string to read results from t

### RFmxWLAN SEM Fetch Lower Offset Margin VI

Returns the measurement status, margin, margin-frequency, and absolute and relative power corresponding to the margin-frequency for lower offset segment. The relative power is relative to the peak power in the carrier.

Use "segment<*n*>/chain<*k*>/offset<*l*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-sem-fetch-lower-offset-margin-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/offset0". Example: "segment0/chain0/offset0" "signal::sig1/segment0/chain0/offset0" "signal::sig1/result::r1/segment0/chain0/offset0" "result::r1/segment0/chain0/offset0" You can use the RFmxWLAN Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns the relative power corresponding to the margin for the lower offset. The relative power is relative to the peak power of the carrier channel. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns the absolute power corresponding to the margin for the lower offset. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Measurement Status — Measurement Status returns the lower offset (negative) segment measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in the lower offset segment. Fail (0) The spectrum exceeds the SEM measurement mask limits the lower offset segment. Pass (1) The spectrum does not exceed the SEM measurement mask limits for the lower offset segment. Margin (dB) — Margin returns the margin from the SEM measurement mask for the lower offset. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the mask. Margin Frequency (Hz) — Margin Frequency returns the frequency corresponding to the margin for the lower offset. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The spectrum exceeds the SEM measurement mask limits the lower offset segment. |
| Pass (1) | The spectrum does not exceed the SEM measurement mask limits for the lower offset segment. |

Parent topic:

RFmxWLAN SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-power-array-vi.html language=enus -->
## TOPIC 00218: RFmxWLAN SEM Fetch Lower Offset Power (Array) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-power-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-power-array-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of total absolute and relative powers, peak absolute and relative powers and frequencies corresponding to the peak absolute powers of lower offset segments. The relative powers are relative to peak power of the carrier. Use "segment<n>/chain<k>" as the selector string to read result

### RFmxWLAN SEM Fetch Lower Offset Power (Array) VI

Returns an array of total absolute and relative powers, peak absolute and relative powers and frequencies corresponding to the peak absolute powers of lower offset segments. The relative powers are relative to peak power of the carrier.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-sem-fetch-lower-offset-power-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Peak Relative Power (dB) — Peak Relative Power returns an array of peak powers of the lower offsets, relative to the peak power of the carrier channel. This value is expressed in dBm. Peak Frequency (Hz) — Peak Frequency returns an array of frequencies at which the peak power occurs in the lower offsets. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Total Absolute Power (dBm) — Total Absolute Power returns an array of average powers of the lower offsets over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm. Total Relative Power (dB) — Total Relative Power returns an array of average powers of the lower offsets relative to the peak power of the carrier channel. This value is expressed in dB. Peak Absolute Power (dBm) — Peak Absolute Power returns an array of peak powers of the lower offsets. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-power-vi.html language=enus -->
## TOPIC 00219: RFmxWLAN SEM Fetch Lower Offset Power VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-power-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of lower offset segment. The relative power is relative to the peak power of the carrier. Use "segment<n>/chain<k>/offset<l>" as the selector string to read results from this VI. ic

### RFmxWLAN SEM Fetch Lower Offset Power VI

Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of lower offset segment. The relative power is relative to the peak power of the carrier.

Use "segment<*n*>/chain<*k*>/offset<*l*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-sem-fetch-lower-offset-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/offset0". Example: "segment0/chain0/offset0" "signal::sig1/segment0/chain0/offset0" "signal::sig1/result::r1/segment0/chain0/offset0" "result::r1/segment0/chain0/offset0" You can use the RFmxWLAN Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Peak Relative Power (dB) — Peak Relative Power returns the peak power of the lower offset, relative to the peak power of the carrier channel. This value is expressed in dBm. Peak Frequency (Hz) — Peak Frequency returns the frequency at which the peak power occurs in the lower offset. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Total Absolute Power (dBm) — Total Absolute Power returns the average power of the lower offset over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm. Total Relative Power (dB) — Total Relative Power returns the average power of the lower offset relative to the peak power of the carrier channel. This value is expressed in dB. Peak Absolute Power (dBm) — Peak Absolute Power returns the peak power of the lower offset. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-measurement-status-vi.html language=enus -->
## TOPIC 00220: RFmxWLAN SEM Fetch Measurement Status VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-measurement-status-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the overall measurement status. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the defau

### RFmxWLAN SEM Fetch Measurement Status VI

Fetches the overall measurement status.

[IMAGE alt='icon' src='rfmxwlan-sem-fetch-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Measurement Status — Measurement Status returns the overall measurement status indicating whether the spectrum exceeds the SEM measurement mask limits in any of the offset segments. Fail (0) The spectrum exceeds the SEM measurement mask limits for at least one of the offset segments. Pass (1) The spectrum does not exceed the SEM measurement mask limits for any offset segment. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The spectrum exceeds the SEM measurement mask limits for at least one of the offset segments. |
| Pass (1) | The spectrum does not exceed the SEM measurement mask limits for any offset segment. |

Parent topic:

RFmxWLAN SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-spectrum-vi.html language=enus -->
## TOPIC 00221: RFmxWLAN SEM Fetch Spectrum VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-spectrum-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum and mask traces. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not sp

### RFmxWLAN SEM Fetch Spectrum VI

Fetches the spectrum and mask traces.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-sem-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the spectrum trace. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns an array of power measured at each frequency bin. This value is expressed in dBm. Composite Mask (dBm) — Composite Mask returns the SEM measurement mask trace. x0 — x0 returns the start frequency of the channel. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns an array of mask level values for each frequency bin. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns an array of power measured at each frequency bin. This value is expressed in dBm. |
| x0 — x0 returns the start frequency of the channel. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns an array of mask level values for each frequency bin. This value is expressed in dBm. |

Parent topic:

RFmxWLAN SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-margin-array-vi.html language=enus -->
## TOPIC 00222: RFmxWLAN SEM Fetch Upper Offset Margin (Array) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-margin-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-margin-array-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of measurement status, margins, margin frequencies, absolute and relative powers corresponding to the margin-frequencies for upper offset segments. The relative powers are relative to the peak power in the carrier. Use "segment<n>/chain<k>" as the selector string to read results fro

### RFmxWLAN SEM Fetch Upper Offset Margin (Array) VI

Returns an array of measurement status, margins, margin frequencies, absolute and relative powers corresponding to the margin-frequencies for upper offset segments. The relative powers are relative to the peak power in the carrier.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-sem-fetch-upper-offset-margin-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns an array of relative powers corresponding to the margins for the upper (positive) offsets. The relative powers are relative to the peak power of the carrier channel. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns an array of absolute powers corresponding to the margins for the upper (positive) offsets. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Measurement Status — Measurement Status returns an array of upper offset (positive) segment measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in the upper offset segments. Fail (0) The spectrum exceeds the SEM measurement mask limits the upper offset segment. Pass (1) The spectrum does not exceed the SEM measurement mask limits for the upper offset segment. Margin (dB) — Margin returns an array of margins from the SEM measurement mask for the upper offset. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the mask. Margin Frequency (Hz) — Margin Frequency returns an array of frequencies corresponding to the margins for the upper offsets. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The spectrum exceeds the SEM measurement mask limits the upper offset segment. |
| Pass (1) | The spectrum does not exceed the SEM measurement mask limits for the upper offset segment. |

Parent topic:

RFmxWLAN SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-margin-vi.html language=enus -->
## TOPIC 00223: RFmxWLAN SEM Fetch Upper Offset Margin VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-margin-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-margin-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status, margin, margin-frequency, absolute and relative power corresponding to the margin-frequency for upper offset segment. The relative power is relative to the peak power in the carrier. Use "segment<n>/chain<k>/offset<l>" as the selector string to read results from this

### RFmxWLAN SEM Fetch Upper Offset Margin VI

Returns the measurement status, margin, margin-frequency, absolute and relative power corresponding to the margin-frequency for upper offset segment. The relative power is relative to the peak power in the carrier.

Use "segment<*n*>/chain<*k*>/offset<*l*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-sem-fetch-upper-offset-margin-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/offset0". Example: "segment0/chain0/offset0" "signal::sig1/segment0/chain0/offset0" "signal::sig1/result::r1/segment0/chain0/offset0" "result::r1/segment0/chain0/offset0" You can use the RFmxWLAN Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns the power level of the spectrum, corresponding to the SEM Results Upper Offset Margin result. The power level is returned relative to the peak power of the carrier channel. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns the power level of the spectrum, corresponding to the SEM Results Upper Offset Margin result. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Measurement Status — Measurement Status returns the upper (positive) offset segment measurement status, indicating whether the spectrum exceeds the SEM measurement mask limits in the upper offset segment. Fail (0) The spectrum exceeds the SEM measurement mask limits the upper offset segment. Pass (1) The spectrum does not exceed the SEM measurement mask limits for the upper offset segment. Margin (dB) — Margin returns the margin from the SEM measurement mask for the upper offset. Margin is defined as the maximum difference between the spectrum and the mask. This value is expressed in dB. Margin Frequency (Hz) — Margin Frequency returns the frequency corresponding to the margin for the upper offset. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The spectrum exceeds the SEM measurement mask limits the upper offset segment. |
| Pass (1) | The spectrum does not exceed the SEM measurement mask limits for the upper offset segment. |

Parent topic:

RFmxWLAN SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-power-array-vi.html language=enus -->
## TOPIC 00224: RFmxWLAN SEM Fetch Upper Offset Power (Array) VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-power-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-power-array-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of total absolute and relative powers, peak absolute and relative powers, and frequencies corresponding to the peak absolute powers of upper offset segments. The relative powers are relative to peak power of the carrier. Use "segment<n>/chain<k>" as the selector string to read resul

### RFmxWLAN SEM Fetch Upper Offset Power (Array) VI

Fetches an array of total absolute and relative powers, peak absolute and relative powers, and frequencies corresponding to the peak absolute powers of upper offset segments. The relative powers are relative to peak power of the carrier.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-sem-fetch-upper-offset-power-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Peak Relative Power (dB) — Peak Relative Power returns an array of peak powers of the upper offsets, relative to the peak power of the carrier channel. This value is expressed in dBm. Peak Frequency (Hz) — Peak Frequency returns an array of frequencies at which the peak power occurs in the upper offsets. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Total Absolute Power (dBm) — Total Absolute Power returns an array of average powers of the upper offsets over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm. Total Relative Power (dB) — Total Relative Power returns an array of average powers of the upper offsets relative to the peak power of the carrier channel. This value is expressed in dB. Peak Absolute Power (dBm) — Peak Absolute Power returns an array of peak powers of the upper offsets. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-power-vi.html language=enus -->
## TOPIC 00225: RFmxWLAN SEM Fetch Upper Offset Power VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-power-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of upper offset segment. The relative power is relative to the peak power of the carrier. Use "segment<n>/chain<k>/offset<l>" as the selector string to read results from this VI. ic

### RFmxWLAN SEM Fetch Upper Offset Power VI

Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of upper offset segment. The relative power is relative to the peak power of the carrier.

Use "segment<*n*>/chain<*k*>/offset<*l*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-sem-fetch-upper-offset-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, chain number, and offset number. If you do not specify the signal name, the default signal instance is used. The default value is "segment0/chain0/offset0". Example: "segment0/chain0/offset0" "signal::sig1/segment0/chain0/offset0" "signal::sig1/result::r1/segment0/chain0/offset0" "result::r1/segment0/chain0/offset0" You can use the RFmxWLAN Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Peak Relative Power (dB) — Peak Relative Power returns the peak power of the upper offset, relative to the peak power of the carrier channel. This value is expressed in dBm. Peak Frequency (Hz) — Peak Frequency returns the frequency at which the peak power occurs in the upper offset. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Total Absolute Power (dBm) — Total Absolute Power returns the average power of the upper (positive) offset over the bandwidth determined by the offset start and stop frequencies. This value is expressed in dBm. Total Relative Power (dB) — Total Relative Power returns the average power of the upper offset relative to the peak power of the carrier channel. This value is expressed in dB. Peak Absolute Power (dBm) — Peak Absolute Power returns the peak power of the upper offset. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-vi.html language=enus -->
## TOPIC 00226: RFmxWLAN SEM Fetch VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches spectral emission mask (SEM) measurement results. icon

### RFmxWLAN SEM Fetch VI

Fetches spectral emission mask (SEM) measurement results.

[IMAGE alt='icon' src='rfmxwlan-sem-fetch-vi.png']

- [RFmxWLAN SEM Fetch Measurement Status VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-measurement-status-vi.html) Fetches the overall measurement status.
- [RFmxWLAN SEM Fetch Carrier Measurement VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-carrier-measurement-vi.html) Returns the absolute and relative carrier power measurements. The relative power is relative to the peak power of the carrier.
- [RFmxWLAN SEM Fetch Lower Offset Margin VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-margin-vi.html) Returns the measurement status, margin, margin-frequency, and absolute and relative power corresponding to the margin-frequency for lower offset segment. The relative power is relative to the peak power in the carrier.
- [RFmxWLAN SEM Fetch Lower Offset Power VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-power-vi.html) Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of lower offset segment. The relative power is relative to the peak power of the carrier.
- [RFmxWLAN SEM Fetch Upper Offset Margin VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-margin-vi.html) Returns the measurement status, margin, margin-frequency, absolute and relative power corresponding to the margin-frequency for upper offset segment. The relative power is relative to the peak power in the carrier.
- [RFmxWLAN SEM Fetch Upper Offset Power VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-power-vi.html) Returns the total absolute and relative powers, peak absolute and relative powers and frequency at peak absolute power of upper offset segment. The relative power is relative to the peak power of the carrier.
- [RFmxWLAN SEM Fetch Lower Offset Margin (Array) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-margin-array-vi.html) Returns an array of measurement status, margins, margin-frequencies, and absolute and relative powers corresponding to the margin-frequencies for lower offset segments. The relative powers are relative to the peak power in the carrier.
- [RFmxWLAN SEM Fetch Lower Offset Power (Array) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-lower-offset-power-array-vi.html) Returns an array of total absolute and relative powers, peak absolute and relative powers and frequencies corresponding to the peak absolute powers of lower offset segments. The relative powers are relative to peak power of the carrier.
- [RFmxWLAN SEM Fetch Upper Offset Margin (Array) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-margin-array-vi.html) Returns an array of measurement status, margins, margin frequencies, absolute and relative powers corresponding to the margin-frequencies for upper offset segments. The relative powers are relative to the peak power in the carrier.
- [RFmxWLAN SEM Fetch Upper Offset Power (Array) VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-upper-offset-power-array-vi.html) Fetches an array of total absolute and relative powers, peak absolute and relative powers, and frequencies corresponding to the peak absolute powers of upper offset segments. The relative powers are relative to peak power of the carrier.
- [RFmxWLAN SEM Fetch Spectrum VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-sem-fetch-spectrum-vi.html) Fetches the spectrum and mask traces.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-send-software-edge-trigger-vi.html language=enus -->
## TOPIC 00227: RFmxWLAN Send Software Edge Trigger VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-send-software-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-send-software-edge-trigger-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxWLAN Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. This VI returns an error in the following situations: You configure an

### RFmxWLAN Send Software Edge Trigger VI

Sends a trigger to the device when you use the [RFmxWLAN Configure Trigger](/csh?topicname=rfmxwlan-configure-trigger-vi.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxWLAN Initiate VI.

[IMAGE alt='icon' src='rfmxwlan-send-software-edge-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-configure-averaging-vi.html language=enus -->
## TOPIC 00228: RFmxWLAN TXP Configure Averaging VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-configure-averaging-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::s

### RFmxWLAN TXP Configure Averaging VI

Configures averaging for the measurement.

[IMAGE alt='icon' src='rfmxwlan-txp-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the TXP measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter as the number of acquisitions over which the results are averaged. |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-configure-burst-detection-enabled-vi.html language=enus -->
## TOPIC 00229: RFmxWLAN TXP Configure Burst Detection Enabled VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-configure-burst-detection-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-configure-burst-detection-enabled-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures burst detection for the TXP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: ""

### RFmxWLAN TXP Configure Burst Detection Enabled VI

Configures burst detection for the TXP measurement.

[IMAGE alt='icon' src='rfmxwlan-txp-configure-burst-detection-enabled-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Burst Detection Enabled — Burst Detection Enabled specifies whether the measurement detects the start and the end of a WLAN packet automatically. The default value is True. False (0) Disables burst detection. True (1) Enables burst detection. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Disables burst detection. |
| True (1) | Enables burst detection. |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-configure-maximum-measurement-interval-vi.html language=enus -->
## TOPIC 00230: RFmxWLAN TXP Configure Maximum Measurement Interval VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-configure-maximum-measurement-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-configure-maximum-measurement-interval-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the maximum measurement interval for the TXP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty stri

### RFmxWLAN TXP Configure Maximum Measurement Interval VI

Configures the maximum measurement interval for the TXP measurement.

[IMAGE alt='icon' src='rfmxwlan-txp-configure-maximum-measurement-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Maximum Measurement Interval (s) — Maximum Measurement Interval specifies the maximum measurement interval. This value is expressed in seconds. When you set the TXP Burst Detection Enabled property to True, the measurement interval used is equal to the smaller of the duration of the WLAN packet under analysis or the value you set for this parameter. The default value is 0.001. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

TXP

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-fetch-measurement-vi.html language=enus -->
## TOPIC 00231: RFmxWLAN TXP Fetch Measurement VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-fetch-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-fetch-measurement-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power and the peak power of the signal over which power measurements are performed. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal nam

### RFmxWLAN TXP Fetch Measurement VI

Returns the average power and the peak power of the signal over which power measurements are performed.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-txp-fetch-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Average Power Mean (dBm) — Average Power Mean returns the average power of the acquired signal. This value is expressed in dBm. When you set the TXP Averaging Enabled property to True, this parameter returns the mean of the average power computed for each averaging count. Peak Power Maximum (dBm) — Peak Power Maximum returns the peak power of the acquired signal. This value is expressed in dBm. When you set the TXP Averaging Enabled property to True, this parameter returns the maximum of the peak power computed for each averaging count. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWLAN TXP Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-fetch-power-trace-vi.html language=enus -->
## TOPIC 00232: RFmxWLAN TXP Fetch Power Trace VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-fetch-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-fetch-power-trace-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power versus time trace. Use "segment<n>/chain<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not spe

### RFmxWLAN TXP Fetch Power Trace VI

Returns the power versus time trace.

Use "segment<*n*>/chain<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwlan-txp-fetch-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, segment number, and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "segment0/chain0". Example: "segment0/chain0" "signal::sig1/segment0/chain0" "signal::sig1/result::r1/segment0/chain0" "result::r1/segment0/chain0" You can use the RFmxWLAN Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Power (dBm) — Power returns the power versus time trace. x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of measured signal power. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the trace start time. This value is expressed in seconds. dx — dx returns the sampling interval. This value is expressed in seconds. y — y returns an array of measured signal power. This value is expressed in dBm. |

Parent topic:

RFmxWLAN TXP Fetch VI

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-fetch-vi.html language=enus -->
## TOPIC 00233: RFmxWLAN TXP Fetch VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-fetch-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the TXP measurement results. icon

### RFmxWLAN TXP Fetch VI

Fetches the TXP measurement results.

[IMAGE alt='icon' src='rfmxwlan-txp-fetch-vi.png']

- [RFmxWLAN TXP Fetch Measurement VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-fetch-measurement-vi.html) Returns the average power and the peak power of the signal over which power measurements are performed.
- [RFmxWLAN TXP Fetch Power Trace VI](../../../../../vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-txp-fetch-power-trace-vi.html) Returns the power versus time trace.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-wait-for-measurement-complete-vi.html language=enus -->
## TOPIC 00234: RFmxWLAN Wait for Measurement Complete VI

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-wait-for-measurement-complete-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/rfmxwlan-wait-for-measurement-complete-vi.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you

### RFmxWLAN Wait for Measurement Complete VI

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='icon' src='rfmxwlan-wait-for-measurement-complete-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWLAN Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00235: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxwlan-labview-api-ref`
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

<!--NI_TOPIC bundle=rfmxwlan-labview-api-ref path=vi-lib/rfmx/wlan/mx/rfmxwlan-llb/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00236: Using the Standard Functionality for error out Parameters

- bundle_id: `rfmxwlan-labview-api-ref`
- source_path: `vi-lib/rfmx/wlan/mx/rfmxwlan-llb/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlan-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wlan/mx/rfmxwlan-llb/standard-functionality-for-error-out-parameters.html
- document_id: `rfmxwlan-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard err

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard error out functionality is as follows:

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

error out contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |
