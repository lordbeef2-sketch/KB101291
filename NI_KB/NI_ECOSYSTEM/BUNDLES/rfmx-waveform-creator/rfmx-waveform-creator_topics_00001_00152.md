# NI DOCUMENT BUNDLE: rfmx-waveform-creator

<!--NI_BUNDLE_CHUNK bundle=rfmx-waveform-creator start=1 end=152 -->
<!--NI_TOPIC bundle=rfmx-waveform-creator path=abbreviations.html language=enus -->
## TOPIC 00001: Abbreviations

- bundle_id: `rfmx-waveform-creator`
- source_path: `abbreviations.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/abbreviations.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: 3GPP 3rd Generation Partnership Project BWP Bandwidth Part CP Cyclic Prefix DFTs-OFDM DFT spread OFDM DL Downlink DMRS Demodulation Reference Symbols FDD Frequency Division Duplex FR1/FR2 Frequency Range 1 / Frequency Range 2 MIMO Multiple Input Multiple Output NR New Radio OFDM Orthogonal Frequency

### Abbreviations

| 3GPP | 3rd Generation Partnership Project |
| --- | --- |
| BWP | Bandwidth Part |
| CP | Cyclic Prefix |
| DFTs-OFDM | DFT spread OFDM |
| DL | Downlink |
| DMRS | Demodulation Reference Symbols |
| FDD | Frequency Division Duplex |
| FR1/FR2 | Frequency Range 1 / Frequency Range 2 |
| MIMO | Multiple Input Multiple Output |
| NR | New Radio |
| OFDM | Orthogonal Frequency Division Multiplexing |
| PBCH | Physical Broadcast Channel |
| PDCCH | Physical Downlink Control Channel |
| PDSCH | Physical Downlink Shared Channel |
| PRACH | Physical Uplink Random Access Channel |
| PUCCH | Physical Uplink Control Channel |
| PUSCH | Physical Uplink Shared Channel |
| RB | Resource Block |
| SISO | Single Input Single Output |
| SSB | Synchronization Signal Block |
| TDD | Time Division Duplex |
| UE | User Equipment |
| UL | Uplink |
| DL | Downlink |
| PSS | Primary Synchronization Signal |
| SSS | Secondary Synchronization Signal |
| CRB | Common Resource Block |

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=access-scheme.html language=enus -->
## TOPIC 00002: Access Scheme

- bundle_id: `rfmx-waveform-creator`
- source_path: `access-scheme.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/access-scheme.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: A multiple access scheme has been followed for the physical layer that is based on orthogonal frequency division multiplexing (OFDM) for the downlink (DL), and single carrier frequency division multiple access (SC-FDMA) for the uplink (UL). The OFDM in the DL supports high peak data rate and the SC-

### Access Scheme

A multiple access scheme has been followed for the physical layer that is based on
 orthogonal frequency division multiplexing (OFDM) for the downlink (DL), and single
 carrier frequency division multiple access (SC-FDMA) for the uplink (UL). The OFDM in
 the DL supports high peak data rate and the SC-FDMA in the UL supports relatively lower
 peak to average power ratio (PAPR), which maximizes power efficiency at the user end.
 The LTE air interface supports both frequency division duplex (FDD) and time division
 duplex (TDD) modes.

Channel bandwidths are made selectable from 1.4 MHz to 20 MHz, with a sub-carrier spacing
 of 15 kHz.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=advanced-mode.html language=enus -->
## TOPIC 00003: Advanced Mode

- bundle_id: `rfmx-waveform-creator`
- source_path: `advanced-mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/advanced-mode.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: In advanced mode of GSM/EDGE modulation, a single carrier frequency signal can be generated with the following characteristics: Slot-0 always configured as BCCH carrier Slot-1 to Slot-7 configured to carry TCH/SACCH, PDTCH, or Dummy burst You can generate the test signals for GSM/GPRS/EDGE. The Modu

### Advanced Mode

In advanced mode of GSM/EDGE modulation, a single carrier frequency signal can be
 generated with the following characteristics:

- Slot-0 always configured as BCCH carrier
- Slot-1 to Slot-7 configured to carry TCH/SACCH, PDTCH, or Dummy burst

You can generate the test signals for GSM/GPRS/EDGE.

The Modulation tab provides the same properties for number of
 frames and oversampling mode as in Basic Mode modulation.

In Frame Config tab, the following properties can be
 configured:

- Network Color Code
- Base Color Code
- Channel Type
- Data Type
- Training Sequence
- Power Control Level (PCL)
- Fast Power Control (FPC)
- Modulation and Coding Scheme (MCS)
- MAC Header
- Data Source

Multiframes, Superframes, and Hyperframes

The longest recurrent time period of the structure is called
 hyperframe. It has a duration of 3 hours 28 minutes 53 seconds
 760 miliseconds. The TDMA frames are numbered modulo this hyperframe (TDMA frame number,
 or FN, from 0 to 2,715,647). A hyperframe is subdivided in 2048 superframes which have
 duration of 6.12 seconds. The superframe is the least common multiple of the time frame
 structures. Furthermore, the superframe is subdivided in multiframes.

The following multiframes are supported by GSM/EDGE modulation in
 Advanced mode of operation:

- 51- multiframe (26 per superframe) with duration of 235.4 ms (3060/13 ms),
 comprising 51 TDMA frames. This multiframe is used to carry BCCH, CCCH.
- 
- 26- multiframe (51 per superframe) with duration of 120 ms, comprising 26 TDMA
 frames. This multiframe is used to carry TCH (and SACCH/T).
- 
- 52-multiframe (25.5 per superframe) with duration of 240 ms, comprising 52 TDMA
 frames. This multiframe is used to carry PDTCH.
- 

Logical Channels

The following logical channels are supported by GSM/EDGE modulation in the
 Advanced mode of operation:

1. Frequency correction channels (FCCH): The frequency
 correction channel carries information for frequency correction of the mobile
 station.
2. Synchronization channel (SCH): The synchronization channel
 carries information for frame synchronization of the mobile station and
 identification of a base transceiver station.
3. Broadcast control channel (BCCH): The broadcast control
 channel broadcasts general information on a base transceiver station per base
 transceiver station basis. The contents of the BCCH channel are internally
 configured by GSM/EDGE Modulation.
4. Common control channel (CCCH): Intended to carry common
 control signalling in circuit switched mode. The contents of the CCCH channel are
 internally configured by GSM/EDGE Modulation.
5. Full rate traffic channel (TCH/F): Intended to carry either
 encoded speech or user data in circuit switched mode.
6. Full rate packet data traffic channel (PDTCH/F): Intended to
 carry user data in packet switched mode.
7. Slow Associated Control Channel (SACCH/M): Provides a
 relatively slow signalling connection and is associated with traffic channel TCH/F.
 The contents of the SACCH channel are internally configured by GSM/EDGE
 Modulation.

The channels listed above are not exposed for configuration and are configured by the
 GSM/EDGE modulation based on the user settings. For example, slot-0 always carries all
 the BCCH information required for synchronization. The SCH Frame Numbers are internally
 calculated based on the number of frames to be generated and always start from 1.

For all the modulation schemes, the stealing flags as per the following table are
 inserted before burst mapping.

[IMAGE alt='image' src='GUID-21FF90C2-B123-44D4-BC20-EB2CA29459BE-a5.gif']

The following figure displays the resulting burst in the radio block after burst mapping
 (Bit swapping is not shown in the figure).

[IMAGE alt='image' src='GUID-E4F879A6-712E-4D8A-856B-9868923FE358-a5.gif']

Creating a Frame

To create an advanced frame, click Frame Config tab. This will
 present the screen shown in the following figure, which will allow you to configure the
 frame.

[IMAGE alt='image' src='GUID-EB6CBB74-C1F8-4709-AB5A-4F68BC46C698-a5.gif']

The following channel types are supported per slot.

1. BCCH: Slot-0 is set as BCCH carrier and carries all the
 information required for synchronization with the DUT in non-signaling mode of
 operation.
2. TCH/SACCH: This channel type can be set for slot-1 to slot-7.
 All the slots carry channel coded user data for transmission. When this channel type
 is selected for a slot, the user can further configure the mode of operation as
 speech or data.
3. PDTCH: This channel type can be set for slot-1 to slot-7.
 This channel type allows the user to transmit PDTCH data. When this channel type is
 selected, the user can configure the RLC/MAC Header based on the Modulation and
 Coding scheme.

The channel type can be set by selecting the appropriate value in Channel
 Type box for the slot under configuration.

By default, the parameters for BCCH will be displayed, allowing you to configure both the
 Base Color Code, and the Network Color code. The First slot within the frame is fixed to
 BCCH and cannot be changed. However, any of the other slots may be edited by clicking on
 the slot graphic at the top of the screen. The following figure shows the screen that is
 presented when the second slot, in this case a TCH-SACCH slot.

[IMAGE alt='image' src='GUID-9076D1B4-7587-43BA-8AA6-C6423AA7D96A-a5.gif']

The type of channel that is present on the given slot can be modified using the
 Channel Type control at the top of the edit panel below the
 main slot graphic. Available slot types are TCH/SACCH,
 PDTCH, and Dummy. By default, all
 configurable channels will be set to TCH/SACCH mode.

Configuring a TCH/SACCH Slot

The following controls are the main slot graphic allow you to change the configuration
 for the TCH/SACCH Slot, and are as follows.

Channel Bits

This parameter is only applicable for TCH/SACCH channel type. This control defines
 whether speech data or circuit-switched data shall be transmitted on TCH.

When the Channel Type is set to
 TCH/SACCH, the number of Data Source can be 1 or 2
 depending on Data Mode selected as listed in the following table:

[IMAGE alt='image' src='GUID-3DFEE8E7-EC8B-4408-939C-8C96A586B360-a5.gif']

The data mode can be set by selecting the appropriate value in Data
 Mode box. By default, the Data Mode is set to
 Speech.

PCL

This field is enabled only if TCH/SACCH
 Channel Type is selected for transmission. The Power Control
 Level is 5 bit field in the SACCH message. This means that a value ranging from 0
 (High Power) to 31 (Low Power) can be set.

The PCL commands the power level to be used by the mobile station.

Training Sequence

This is the standard training sequence. The training sequence is used as a timing
 reference and for equalization. There are total of eight different bit sequences
 that may be used, each 26 symbols long.

TSC0 to TSC7 can be selected and applies to the whole slot under configuration. The
 default is TS0

FPC

This field is only enabled if TCH/SACCH
 Channel Type is selected for transmission. The Fast Power
 Control is a 1 bit field in the SACCH message.

The PCL field indicates whether fast measurement reporting and power control
 mechanism is used. If the FPC checkbox is unselected,
 FPC bit is set to 0 in SACCH
 message; this indicates FPC is not in use.

By default, the FPC checkbox is selected which results in FPC
 bit set to 1 in SACCH message. By default the checkbox is selected.

Class Bits

This controls the data payload of the class bits. When the Channel Bits type is set
 to Speech, two buttons are displayed for Class 1 Bits and for Class 2 bits. When the
 Channel Bits type is set to Loop C, there will be a single data payload button
 representing the data to be transmitted on this channel.

Configuring a PDTCH Slot

The channel organization for packet data channels uses the 52-frame multiframe. Four TDMA
 slots constitute a radio block. It is basically a sequence of four normal bursts
 carrying one RLC/MAC protocol data units.

The figure below shows the constitution of radio blocks in 52-frame multiframe.

[IMAGE alt='image' src='GUID-6A7446DC-38DB-4890-BFC9-C0200B5489D8-a5.gif']

For PDTCH, the data is not coded before mapping to the bursts. The data source configured
 for generation terminates every radio block and restarts. This allows the data to wrap
 around if a multiple of 52 frames is used.

When the Channel type of a given slot is changed to PDTCH; the main configuration area
 will changed to that shown in the following figure.

[IMAGE alt='image' src='GUID-A72FFDB7-E98B-4C7A-9F7B-F8FD9E96C0FE-a5.gif']

This channel type will present similar controls to that described in the TCH/SACCH
 channel configuration above, but will also provide additional controls for MCS and MAC
 Header

MCS

GSM/EDGE Modulation supports GPRS and EGPRS DL Modulation and Coding Schemes.

Four different coding schemes, CS-1 to CS-4, are defined for the GPRS Radio Blocks
 carrying RLC data blocks. The following figure shows the supported modulation and
 coding schemes

[IMAGE alt='image' src='GUID-EC05A844-37E3-4AE4-BEDD-D50D80C96C10-a5.gif']

The modulation and coding scheme can be set by selecting the appropriate value in the
 MCS box. The selected value of MCS will changes the configuration of the MAC
 Header.

RLC/MAC block

A RLC/MAC block is the protocol data unit exchanged between RLC/MAC entities.

[IMAGE alt='image' src='GUID-8737788F-33AD-4308-8B33-C196CA599F9C-a5.gif']

A RLC/MAC header block is the part of an RLC/MAC block carrying a control message
 between RLC/MAC entities. A RLC data block is the part of a RLC/MAC block carrying
 user data or signalling data received from an upper layer.

RLC/MAC Header Include

This field sets whether the RLC/MAC header shall be included and coded for
 transmission.

There are only certain valid combinations of RLC/MAC Header and Data Encoding that
 are allowed by advanced mode of GSM/EDGE Modulation. These are shown in the
 following table.

[IMAGE alt='image' src='GUID-EF763DC9-CA6B-4479-B12C-02992CB2A1FD-a5.gif']

The RLC/MAC header inclusion can be set by selecting the appropriate value in the
 RLC/MAC Header Include checkbox.

Data Encoding

This field sets whether the Data shall be coded for transmission.

There are only certain valid combinations of RLC/MAC Header and Data Encoding that
 are allowed by advanced mode of GSM/EDGE Modulation. These are shown in the above
 table.

The data encoding can be set by setting the appropriate value in the Data
 encoding checkbox.

RLC/MAC Header

RLC/Mac header contains control information of the RLC/MAC block. Depending upon the
 MCS selected, an applicable RLC/MAC header is displayed. You are able to configure
 the parameters of RLC/MAC header. The format of RLC/MAC headers for various MCS, are
 as follows:

For MCS-1, MCS-2, MCS-3, and MCS-4, Header type 3 as per 3GPP TS
 44.060 is used. Total header size is 31 bits.

[IMAGE alt='image' src='GUID-A393377B-92BE-41D3-9523-DCBC449A46C5-a5.gif']

For MCS-5 and MCS-6, Header type 2 as per 3GPP TS 44.060 is used.
 Total header size is 28 bits.

[IMAGE alt='image' src='GUID-5669084C-2A75-4BC0-A9CE-4B6628681356-a5.gif']

For MCS-7, MCS-8 and MCS-9, Header type 1 per 3GPP TS 44.060 is used. Total header
 size is 40 bits.

[IMAGE alt='image' src='GUID-9254987B-3F24-4E76-8448-EB595BC8643D-a5.gif']

For CS-1 to CS-4, only USF bits are applicable.

[IMAGE alt='image' src='GUID-9F158888-DD9C-402D-9114-EBE7A3A5B36C-a5.gif']

The Advanced mode of GSM/EDGE generation modulation does not implement all the
 RLC/MAC Header related functionality except for CPS field which affects the way the
 coding and puncturing scheme used for the RLC/MAC data block in case the data
 encoding is set. It allows the user to set the values within the valid range.

All the RLC/MAC Header fields can be set by clicking on each bit in the MAC Header
 field. The RLC/MAC Header settings are constant across all the RLC/MAC Header data
 blocks for a configured slot.

Uplink State Flag (USF) Field

The USF field is sent in all downlink RLC/MAC blocks and indicates the owner or use
 of the next uplink radio block on the same timeslot (3GPP TS 45.002). The USF field
 is three bits in length and eight different USF values can be assigned.

EGPRS Supplementary/Polling (ES/P) Field

The ES/P field is used to indicate whether the RRBP field is valid or not valid, and
 what fields the next uplink control block shall contain.

Refer to 3GPP TS 44.060 for more information.

Relative Reserved Block Period (RRBP) Field

The RRBP value specifies a single uplink block in which the mobile station shall
 transmit either a PACKET CONTROL ACKNOWLEDGEMENT message or a PACCH block to the
 network.

Refer to 3GPP TS 44.060 for more information.

Temporary Flow Identity (TFI) Field

The TFI identifies the Temporary Block Flow (TBF) to which the RLC data block
 belongs. It is 5 bits in length.

Refer to 3GPP TS 44.060 for more information.

Power Reduction (PR) field

The Power Reduction (PR) field indicates the power level reduction of the current RLC
 block. If downlink power control is not used, the MS ignores the PR field.

[IMAGE alt='image' src='GUID-73F2291D-156A-48A9-8059-46B00D25EA96-a5.gif']

Block Sequence Number (BSN) field

This field carries the sequence absolute Block Sequence Number (BSN') modulo Sequence
 Number Space (SNS) (2 048 in EGPRS) of each RLC data block within the TBF. In EGPRS,
 the BSN is 11 bits in length and is encoded as a binary number with range 0 to 2
 047.

If two to four RLC data blocks are sent within a RLC/MAC block, BSN2 to BSN4 are
 relative to BSN1, provided the difference between the second to fourth block number
 and the first block modulo SNS is less than Window Size (WS).

Refer to 3GPP TS 44.060 for more information.

Coding and Puncturing Scheme Indicator Field (CPS)

The Coding and Puncturing Scheme indicator field indicates the kind of channel coding
 and puncturing used for data blocks. Refer to 3GPP TS 44.060
 specification for more information.

The following table shows possible Header Type 1 CPS field values

[IMAGE alt='image' src='GUID-7849B13D-3CA1-4FBD-B31C-BD9539B1E6BC-a5.gif']

The following table shows possible Header Type 2 CPS field values

[IMAGE alt='image' src='GUID-027F7097-DFDC-46B4-9DBC-28FA2CA8C64D-a5.gif']

The following table shows possible Header Type 3 CPS field values

[IMAGE alt='image' src='GUID-A7E83F79-DB5A-41BC-A89C-CB0F2FFE3D65-a5.gif']

Split Block Indicator Field (SPB)

The Split Block indicator is only used in header type 3 to indicate if some user data
 is retransmitted using 2 block re-segmentation. Refer to 3GPP TS
 44.060 for more information.

MAC Header Configuration

The MAC Header box allows you to modify the individual portions of the header
 transmitted as part of the PDTCH channel. You can either modify individual bits by
 clicking on the particular box you wish to toggle.

Alternatively, you can edit the values by clicking on the particular field you wish
 to edit and typing either 1 or 0; this will fill the field from right to left with
 the bits you type. The values you type will not carry over from one field to the
 next.

Parent topic:

GSM/EDGE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=analog-modulation.html language=enus -->
## TOPIC 00004: Analog Modulation

- bundle_id: `rfmx-waveform-creator`
- source_path: `analog-modulation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/analog-modulation.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Information about frequency modulation and amplitude modulation.

### Analog Modulation

Information about frequency modulation and amplitude modulation.

- [Introduction to Frequency Modulation](introduction-to-frequency-modulation.html#GUID-CEA1EA8A-A460-47E1-971D-7AED21DF2B4A) With frequency modulation, you vary the frequency of a carrier in order to transmit a signal.
- [Introduction to Amplitude Modulation](introduction-to-amplitude-modulation.html) With amplitude modulation (AM), you vary the amplitude of an RF carrier signal according to the amplitude of the message signal.
- [Creating an Analog Waveform](creating-an-analog-waveform.html#GUID-FF7BF605-631C-433E-B1DC-A7657B153032) Generates an analog waveform using RFmx Waveform Creator .

Parent topic:

RFmx Waveform Creator Modulation Schemes

<!--NI_TOPIC bundle=rfmx-waveform-creator path=applying-fixed-reference-channels.html language=enus -->
## TOPIC 00005: Applying Fixed Reference Channels

- bundle_id: `rfmx-waveform-creator`
- source_path: `applying-fixed-reference-channels.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/applying-fixed-reference-channels.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains information about applying fixed reference channels (FRC) for both uplink and downlink channels. You can configure the FRC for both uplink and downlink channels by clicking Apply FRC. For uplink, Apply FRC is enabled for all configurations. For downlink, Apply FRC is enabled on

### Applying Fixed Reference Channels

This section contains information about applying fixed reference channels (FRC) for both
 uplink and downlink channels.

You can configure the FRC for both uplink and downlink channels by clicking
 Apply FRC. For uplink, Apply FRC is
 enabled for all configurations. For downlink, Apply FRC is
 enabled only when you set the Channel Configuration Mode to
 User Defined.

To enable Apply FRC, you must be on the Carrier Definition tab as
 shown in the following image. FRCs are specific to individual carriers, hence, they are
 applied only to the selected carrier definition. If Carrier
 Allocated checkbox is unchecked, Apply FRC is
 disabled for that carrier definition. FRCs are available according to the selected
 frequency range.

[IMAGE alt='image' src='GUID-575F5428-81D8-4FD5-A10B-250FDC89FC5C-a5.png']

Configuring FRC

Follow the following steps to configure FRCs for selected carrier definitions:

1. Click Apply FRC , it opens a new FRC configurations
 window.
2. Configure the required parameters for FRCs.
3. Click Ok to apply changes. Note Applying FRC changes
 overwrite the carrier definition and remove any non-applicable user
 configurations from the carrier definition setup tree.

FRC Configuration Windows

Depending on the link direction, one of the following windows will appear when you click
 on Apply FRC.

Downlink FRC Configuration

This window enables the user to configure downlink FRCs (for UE receiver tests) according
 to Annex A.3 of 3GPP TS 38.521-1 and 3GPP TS
 38.521-2 specifications.

Channel Bandwidth: Specifies the overall bandwidth, comprised of
 bandwidth parts. Valid values are from 5 MHz to 400 MHz.

FRC Type: Specifies the downlink fixed reference channel table
 from the specifications.

Subcarrier Spacing: Specifies the supported values based on the
 selected channel bandwidth.

Duplex Scheme: Specifies the duplex scheme used by the downlink
 FRCs.

| FDD | Downlink FRCs are configured for FDD operation according to Annex A.3.2 of 3GPP TS 38.521-1 and 3GPP TS 38.521-2 specifications. |
| --- | --- |
| TDD | Downlink FRCs are configured for TDD operation according to Annex A.3.3 of 3GPP TS 38.521-1 and 3GPP TS 38.521-2 specifications. |

Uplink FRC Configuration

This window enables the user to configure uplink FRCs (for base station receiver tests)
 according to Annex A of 3GPP TS 38.141-1 and 3GPP TS
 38.141-2 specifications.

Channel Bandwidth: Specifies the overall bandwidth, comprised of
 bandwidth parts. Valid values are from 5 MHz to 400 MHz.

Duplex Scheme: Specifies the duplex scheme used by the uplink
 FRCs.

FRC Type: Specifies the uplink fixed reference channel table from
 the specifications.

DMRS Additional Positions: Specifies the positions of additional
 DMRS symbols.

| Frequency Range | FRC Types | DMRS Additional Positions |
| --- | --- | --- |
| Frequency Range 1 | A.3, A.4, and A.7 | 1 and 2 |
| A.3B | 0 and 1 |  |
| A.1, A.2, A.3A, A.5, A.8, A.9 and A.12 | 1 |  |
| Frequency Range 2 | A.3, A.3A, A.4, A.5, A.7, and A.10 | 0 and 1 |
| A1, A.3B, NTN A.5 and NTN A.6 | 1 |  |

Transform Precoding: Specifies whether to enable transform
 precoding. If this parameter is disabled, the signal will be CP-OFDM modulated;
 otherwise, the signal will be DFT-S-OFDM modulated.

| Frequency Range | FRC Types | Transform Precoding |
| --- | --- | --- |
| Frequency Range 1 | A.3 | Supported |
| Others | Not supported |  |
| Frequency Range 2 | A.3 | Supported |
| Others | Not supported |  |

Number of Tx Antennas: Specifies the number of transmit antennas.
 This is a read-only parameter, updated from Number of Tx Antennas in Signal
 Configuration. Other values of Number of Tx Antennas are not supported for FRC
 configuration.

| Frequency Range | FRC Types | Tx Antennas |
| --- | --- | --- |
| Frequency Range 1 | A.3, A.4, A.9, and A.12 | 1, 2, and 4 |
| Others | 1 |  |
| Frequency Range 2 | A.3, A.4, and A.7 | 1 and 2 |
| Others | 1 |  |

Reference Channel: Specifies the reference channel for the
 selected FRC table. The list of supported reference channels depends upon Channel
 Bandwidth, FRC Type, DMRS Additional Positions, Transform Precoding, and Number of Tx
 Antennas, and updated based on the selected settings. If the selected settings do not
 apply to any reference channel, the list will be empty, and an error is shown.

PUSCH Mapping Type: Allows you to choose between Type A and Type B
 mapping.

| Frequency Range | FRC Types | PUSCH Mapping Type |
| --- | --- | --- |
| Frequency Range 1 | A.3, A.3A, A.3B, NTN A.3, A.4, A.5, A.7, A.8, A.9, and A.12 | Type A and Type B |
| A.1 and A.2 | Type A |  |
| Frequency Range 2 | A.1 | Type A |
| A.3, A.3A, A.3B, A.4, A.5, NTN A.5, NTN A.6, A.7, and A.10 | Type B |  |

RB Offset: Specifies the resource block offset from where the
 resource block allocation for PUSCH should start.

FRC tables for UL FR1 conducted (specified in 3GPP 38.141-1
 specification) and UL FR1 OTA (specified in 3GPP 38.141-2
 specification) are the same. Hence, they are implemented only once for FR1.

PTRS Enabled: Specifies whether to enable adding a PTRS to the
 waveform.

| Frequency Range | FRC Types | PTRS Enabled |
| --- | --- | --- |
| Frequency Range 1 | All | Not supported |
| Frequency Range 2 | A.1, A.3, A.3A, A.3B, NTN A.5, and NTN A.6 | Not supported |
| A.4, A.5, A.7, and A.10 | Supported |  |

Note

Interlace Index: Specifies the interlace index for interlaced RB
 allocation in NR-U cases.

Parent topic:

NR

Related concepts:

- Carrier Definition

<!--NI_TOPIC bundle=rfmx-waveform-creator path=basic-mode.html language=enus -->
## TOPIC 00006: Basic Mode

- bundle_id: `rfmx-waveform-creator`
- source_path: `basic-mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/basic-mode.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Basic mode, you can select the modulation type and set the number of frames you want to generate. All the parameters are set to their nominal settings for GSM on initial entry of the modulation page (MSK modulation, 1 frame, and 6 times over sampling). In general, when using a combination of EDGE

### Basic Mode

In Basic mode, you can select the modulation type and set the number of frames you want
 to generate. All the parameters are set to their nominal settings for GSM on initial
 entry of the modulation page (MSK modulation, 1 frame, and 6 times over sampling). In
 general, when using a combination of EDGE and GSM slots, it is not possible to guarantee
 a correct phase wrap, because the modulation type has to change between GSM and EDGE
 bursts. Therefore, the default number of frames is not set to 8, as it is for EDGE only
 modulation.

Note

Creating a Frame

The Frame Config tab allows you modify the GSM frame being
 generated. Frame Config tab consists of 8 time slots each of
 which can be modified by clicking on the relevant item in the upper slot graphic.

Setting the Frame Configuration Parameters: This section describes
 the general settings available for frame configuration and how you can modify them.

Link Direction: Enables you to select the type of frame
 configuration. The default value is Up/Reverse.

Bit Encoding Method: Specifies the bit encoding method. The
 default value is GSM Differential.

Rise Time (Symbols): Specifies the duration of the rising edge
 of a burst in symbols. The valid range is between 1/Oversampling Factor and 16.0 and
 the resolution is 1/Oversampling Factor. The default value is 3.

Fall Time (Symbols): Specifies the duration of the falling
 edge of a burst in symbols. The valid range is between 1/Oversampling Factor and
 16.0 and the resolution is 1/Oversampling Factor. The default value is 3.

Rise Delay (Symbols): Specifies the offset in the start of the
 rising edge of a burst in symbols. The valid range is between -9.0 and 9.0 and the
 resolution is 1/Oversampling Factor. The default value is 0.

Fall Delay (Symbols): Specifies the offset in the start of
 falling edge of a burst in symbols. The valid range is between -9.0 and 9.0 and the
 resolution is 1/Oversampling Factor. The default value is 0.

Slot Enabled: Allows you control whether the specific slot
 will be transmitted or not. By default, only the first slot is transmitted.

Burst Type: Specifies the type of burst that can be inserted
 into the frame. The default value is GSM.

Power: Specifies the power of the slot relative to the signal
 generator's power level. This value is expressed in dB. Valid values are 0 to – 60
 dB.

Note

Configuring an Uplink Slot

On this Frame Config tab, you can examine the fields that make up
 the slot, you can change the contents of the Sync and Data fields, and you can set the
 Burst Type to GSM,
 Access, or Edge. The Slot
 Enabled checkbox allows you control if the specific slot will be
 transmitted or not. By default, only the first slot is transmitted.

[IMAGE alt='image' src='GUID-0EB0C04A-4460-4666-B4A4-099CADD9C7B2-a5.png']

There are two 58 bits long data fields in a normal burst, which are treated as a
 contiguous block of data. The data source you select for either of these is
 automatically applied to the other and if you select a PRBS sequence the data at the
 start of the second field will continue in the sequence from where the first field
 finished. These two fields combined will generate 116 data bits of the PRBS sequence,
 which will restart after the total number of frames you set on the modulation page. If
 you want a sequence longer than 116 bits, you should increase the number of frames on
 the modulation page, since the PRBS sequence is continued for every frame in the set.
 For example, to generate a sequence of at least 5,000 bits, set the number of frames to
 44, and you will get a sequence which repeats after 44 x 116 bits = 5,104 bits. The data
 source can be modified by clicking on the Data portion of the slot graphic, and then
 selecting the Source Type button.

An EDGE burst looks very similar to a normal GSM burst, except that every field has three
 times as many bits. The burst occupies the same number of symbols as a GSM burst,
 because the 8PSK modulation uses three bits per symbol.

You can change the training sequence field of a normal burst to any of the eight patterns
 TS0 to TS7 by selecting the sync portion of the slot graphic and then using the TSC
 control below. An access burst has a fixed sync field and only one data field of 36
 bits.

Configuring a Downlink Slot

You can change to a downlink frame by selecting Down/Forward on
 the Link Direction control.

To configure a slot within the downlink frame, click the slot within the main slot
 graphic at the top of the tab.

Available burst types for downlink slots are GSM,
 Sync, Dummy, Frequency
 Correction, and Edge.

The following figure shows the frequency correction burst in a downlink frame. You have
 only two choices for the frequency correction, the fixed bits can be set to represent
 either + 67.7 kHz or - 67.7 kHz. To change frequency correction, Click Freq.
 Correction in the graphic and select the correction in the
 Correction control. The guard period is either long or
 normal, depending on the slot number, the same as uplink bursts.

[IMAGE alt='image' src='GUID-9EA53A3F-51B2-4C33-9B14-6A0AF8EF2E67-a5.png']

A dummy burst has no user options, a synchronization burst has two data fields that you
 can configure, and a normal burst has two data fields and a training sequence field with
 options.

Parent topic:

GSM/EDGE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=bt.html language=enus -->
## TOPIC 00007: Bluetooth

- bundle_id: `rfmx-waveform-creator`
- source_path: `bt.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/bt.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creates a waveform that simulates a Bluetooth carrier. The following topics describe how to create Bluetooth waveforms that conform to the Bluetooth SIG specifications. You should be familiar with Bluetooth SIG specifications.

### Bluetooth

Creates a waveform that simulates a Bluetooth carrier.

The following topics describe how to create Bluetooth waveforms that conform to the
 Bluetooth SIG specifications. You should be familiar with Bluetooth SIG
 specifications.

- [Bluetooth® Packet Header Details](GUID-7C8F76F4-4426-412B-BB1D-F08004FD2F9E.html)
- [Dirty Transmitter](dirty-transmitter.html)
- [RFSG Database](GUID-40A48804-0DEC-468C-B7E3-1CD09D987F2F.html)
- [Antenna Switching for LE Direction Finding Packets](GUID-F5BC1930-9710-4EB0-9884-8D7A2CD5C26C.html)

Parent topic:

RFmx Waveform Creator Modulation Schemes

Related information:

- RFmx Bluetooth Generation LabVIEW API Reference
- RFmx Bluetooth Generation C API Reference

<!--NI_TOPIC bundle=rfmx-waveform-creator path=burst-types.html language=enus -->
## TOPIC 00008: Burst Types

- bundle_id: `rfmx-waveform-creator`
- source_path: `burst-types.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/burst-types.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: GSM EDGE Modulation supports the following types of bursts. Normal burst (NB): Used to carry information on traffic and control channels. GMSK modulated normal burst: One symbol is equivalent to a bit. A particular bit period within a timeslot is referenced by a bit number (BN), with the first bit p

### Burst Types

GSM EDGE Modulation supports the following types of bursts.

Normal burst (NB): Used to carry information on traffic and
 control channels.

GMSK modulated normal burst: One symbol is equivalent to a bit. A
 particular bit period within a timeslot is referenced by a bit number (BN), with the
 first bit period being numbered 0, and the last (1/4) bit period being numbered 156. The
 following table shows the format of GMSK modulated normal burst.

[IMAGE alt='image' src='GUID-D083AC97-98BB-4D79-870E-A93CD9CCF519-a5.gif']

8PSK modulated normal burst: One symbol is equivalent to
 three bits. A particular bit period within a timeslot is referenced by a bit number
 (BN), with the first bit being numbered 0, and the last (3/4) bit being numbered
 468. The bits are mapped to symbols in ascending order according to 3GPP TS
 45.004 specification. The following table shows the format of 8PSK
 modulated normal burst.

[IMAGE alt='image' src='GUID-A50505DE-D648-453A-ACAB-E10DEBA2B06C-a5.gif']

Frequency correction burst (FB): Used for frequency
 synchronization of the mobile. It is equivalent to an un-modulated carrier, shifted in
 frequency, with the same guard time as the normal burst. It is broadcast together with
 the BCCH.

Synchronization burst (SB): Used for time synchronization of the
 mobile. It contains a long training sequence and carries the information of the TDMA
 frame number (FN) and base station identity code (BSIC) which is 6 bit long and consists
 of 3 bits of PLMN color code with range 0 to 7 and 3 bits of BS color code with range 0
 to 7.

Access Burst (AB): Used for random access.

Dummy Burst: This burst carries dummy data. It is similar to
 normal burst and can be used for idle slots.

A collection of eight such consecutive time slots or bursts form a TDMA frame. A TDMA
 frame lasts approximately 4.615 ms and acts as a basic unit of logical channels. The
 burst structures are shown in the following figure.

[IMAGE alt='image' src='GUID-89D9F527-7E71-41F4-BADD-4A2C94529C9B-a5.gif']

Parent topic:

GSM/EDGE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=bwp-configuration-overview.html language=enus -->
## TOPIC 00009: BWP Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `bwp-configuration-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/bwp-configuration-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains the following configuration parameters. Subcarrier Spacing: Specifies the supported values on the basis of the selected channel bandwidth. In general, valid values are 15 kHz, 30 kHz, 60 kHz, and 120 kHz. Currently, only one subcarrier spacing for a single carrier bandwidth par

### BWP Configuration

This section contains the following configuration parameters.

Subcarrier Spacing: Specifies the supported values on the basis of
 the selected channel bandwidth.

In general, valid values are 15 kHz, 30 kHz, 60 kHz, and 120 kHz. Currently, only one
 subcarrier spacing for a single carrier bandwidth part per carrier is supported.

Cyclic Prefix Mode: Specifies the cyclic prefix duration and the
 number of symbols in a slot for the signal being measured. When Cyclic Prefix Mode is
 Normal, the number of symbols in a slot is 14. When Cyclic
 Prefix Mode is Extended, the number of symbols in a slot is
 12.

Grid Start: Specifies the resource block offset of a grid relative
 to the Ref Pt. A.

RB Offset: Specifies the resource block offset of a bandwidth part
 relative to the resource grid start.

Number of RBs: Specifies the number of consecutive resource blocks
 in a bandwidth part. The valid range depends on frequency range, channel bandwidth,
 subcarrier spacing, and grid settings. To automatically configure all the available RBs,
 set this parameter to -1.

Grid Size: Specifies the resource grid size when you set the
 Grid Size Mode control to Manual.

Number of User Configurations: Specifies the number of user
 configurations in a bandwidth part.

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=carrier-configuration.html language=enus -->
## TOPIC 00010: Carrier Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `carrier-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/carrier-configuration.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section allows you to configure the top level modulation parameters of the FDD Signal. It comprises the controls as described below. Link Direction: Specifies the link direction of the signal being generated. RFmx Waveform Creator supports both uplink and downlink. However in the uplink, the De

### Carrier Configuration

This section allows you to configure the top level modulation parameters of the FDD
 Signal. It comprises the controls as described below.

[IMAGE alt='image' src='GUID-5D251347-0291-4C49-8A85-A8F0A395623D-a5.png']

Link Direction: Specifies the link direction of the signal being
 generated. RFmx Waveform Creator supports both uplink and downlink. However in the
 uplink, the Dedicated Physical Channel and the Physical Random Access Channel are
 supported. The default channel is the Dedicated Physical Channel.

Number of Frames: Specifies the number of radio frames to be
 generated. The default value is 1. The duration of a 3GPP FDD waveform is given in
 frames. One frame is 10 ms (38400 chips) long, which in turn is equivalent to 15 slots.

Oversampling Factor: Specifies the oversampling factor to be used
 in the simulation. When the Auto is checked, the oversampling
 rate is adjusted automatically.

Chip Rate: Specifies the chip rate.

Short Frame Generation: Specifies the short frame generation
 settings which enables you to generate a limited number of contiguous slots instead of
 full frame. Short Frame is currently not supported for downlink channels, PRACH
 channels, sidelink channels, and DPCH Compressed mode.

Enabled: If the Enabled checkbox is
 selected, it enables short frame generation, otherwise full frame is generated. When
 short frame is enabled, Number of Frames is restricted to 1.

Offset (slots): Specifies the offset in slots from the
 beginning of the frame. Valid values are 0 to 14.

Length (slots): Specifies the number of slots to be generated.
 Valid values are 1 to 15.

Note

Offset (slots)

Length (slots)

Length(slots)

Offset
 (slots)

Parent topic:

WCDMA (3GPP FDD Release 8)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=carrier-definition-overview.html language=enus -->
## TOPIC 00011: Carrier Definition

- bundle_id: `rfmx-waveform-creator`
- source_path: `carrier-definition-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/carrier-definition-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section allows you to configure the top level modulation parameters for each carrier. Carrier Allocated: Allows the empty carrier configurations when unchecked. Helps you to configure the Multi-carrier signals with a few empty component carriers. Cell ID: Specifies the physical layer cell ident

### Carrier Definition

This section allows you to configure the top level modulation parameters for each
 carrier.

Carrier Allocated: Allows the empty carrier configurations when
 unchecked. Helps you to configure the Multi-carrier signals with a few empty component
 carriers.

Cell ID: Specifies the physical layer cell identity. The range is
 0 to 1007. The default value is 0.

Channel Bandwidth: Specifies the overall bandwidth, comprised of
 bandwidth parts. Valid values range from 5 MHz to 400 MHz.

Time Domain Windowing Duration (% Of CP): Time-domain windowing is
 not mandatory in the NR standard. The window function is employed to reduce out-of-band
 spectrum emissions.

The windowing duration specifies the time interval of the time-domain windowing. By
 default, it is set to 20 percent of the cyclic prefix length. Increasing the duration
 increases the spectrum roll-off at the cost of a decreased delay spread tolerance.

Oversampling Factor: Specifies the relation between the final
 output sample rate and the native sample rate.

For example, an oversampling factor of 4 means that the final output sample rate will be
 4 times the symbol rate.

Reference Grid Alignment Mode: Specifies whether the component
 carrier is aligned to a reference grid of a frequency range. In
 Auto mode, the reference grid is selected from the largest
 configured subcarrier spacing in a bandwidth part. In Manual
 mode, you specifies the subcarrier spacing of the reference grid manually.

Reference Grid Subcarrier Spacing: Specifies the subcarrier
 spacing for reference grid when Reference Grid Alignment Mode is
 set to Manual.

Reference Grid Start: Specifies the resource block offset of the
 reference grid relative to the Ref Pt. A when Reference Grid Alignment
 Mode is set to Manual.

Grid Size Mode: Allows you to set the grid size of all
 bandwidthparts and SSB in a component carrier. In Auto mode, the
 grid size is set equal to the maximum transmission bandwidth specified by 3GPP
 specification.

Reference Grid Size: Specifies the reference resource grid size
 when Grid Size Mode is set to Manual.

PI/2 BPSK Shaping Type: Specifies the type of PI/2 BPSK spectral
 shaping filter definition. When set to Default mode, internally
 defined spectral shaping coefficients are applied. When set to
 User mode, the spectral shaping filter coefficients given in
 the PI/2 BPSK Shaping Coefficients parameter are applied.

PI/2 BPSK Shaping Coefficients: Defines the time domain FIR filter
 coefficients of the PI/2 BPSK spectral shaping filter. The filter values are entered as
 a sequence of comma-separated, floating-point values. For example, you can enter the
 default coefficients as -0.26, 0.9268, -0.26.

Number of BWP Configurations: Specifies the number of configured
 bandwidth parts (BWP) in a carrier. Currently only a single BWP can be configured.

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=carrier-definition-setup.html language=enus -->
## TOPIC 00012: Carrier Definition Setup

- bundle_id: `rfmx-waveform-creator`
- source_path: `carrier-definition-setup.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/carrier-definition-setup.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: For more information about carrier definition setup, refer to the Carrier Definition and Carrier sets section in the RFmx Waveform Creator Help.

### Carrier Definition Setup

For more information about carrier definition setup, refer to the Carrier Definition and
 Carrier sets section in theRFmx Waveform Creator Help.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=cdma2k-3gpp2.html language=enus -->
## TOPIC 00013: CDMA2k (3GPP2)

- bundle_id: `rfmx-waveform-creator`
- source_path: `cdma2k-3gpp2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/cdma2k-3gpp2.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creates a waveform that simulates CDMA2k (3GPP2). CDMA2k is a standard for 3G wireless technology that is derived from cdmaOne (IS95). The modulation scheme is defined in the 3GPP2 specification C.S0002-C. This document assumes that you know how to package and download files to an instrument. For mo

### CDMA2k (3GPP2)

Creates a waveform that simulates CDMA2k (3GPP2). CDMA2k is a standard for 3G
 wireless technology that is derived from cdmaOne (IS95).

C.S0002-C

Note

Generating and
 Saving the Waveform File

Parent topic:

RFmx Waveform Creator Modulation Schemes

Related information:

- RFmx CDMA2k .NET Reference
- RFmx CDMA2k C API Reference

<!--NI_TOPIC bundle=rfmx-waveform-creator path=cdma2k-data-rate-to-symbol-rate-mappings.html language=enus -->
## TOPIC 00014: CDMA2k Data Rate to Symbol Rate Mappings

- bundle_id: `rfmx-waveform-creator`
- source_path: `cdma2k-data-rate-to-symbol-rate-mappings.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/cdma2k-data-rate-to-symbol-rate-mappings.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Introduction This appendix provides mappings between frame length, data rate, symbol rate, Walsh length and Walsh repeats for all channels and radio configurations supported in RFmx Waveform Creator. Note that RFmx Waveform Creator currently supports frames of 20 ms duration, thus grayed-out rows in

### CDMA2k Data Rate to Symbol Rate Mappings

Introduction

This appendix provides mappings between frame length, data rate, symbol rate, Walsh
 length and Walsh repeats for all channels and radio configurations supported in
 RFmx Waveform Creator.

Note that RFmx Waveform Creator currently supports frames of 20 ms
 duration, thus grayed-out rows in the tables below are not implemented.

Reverse/Uplink Channels

R-ACH

This is only available in spreading rate 1 for RC1 and 2.

[IMAGE alt='image' src='GUID-199004DA-980E-4444-B638-D35FC0ECBC23-a5.gif']

R-EACH

[IMAGE alt='image' src='GUID-E3C00E32-208A-4536-9C46-058D06B70586-a5.gif']

The only differences between spreading rate 1 and 3 are the number of Walsh repeats; 1
 for SR1 and 3 for SR3.

R-CCCH

[IMAGE alt='image' src='GUID-E9F7D44F-B166-4B4E-961A-92EF6A3C441C-a5.gif']

The only differences between spreading rate 1 and 3 are the number of Walsh repeats; 1
 for SR1 and 3 for SR3.

R-DCCH

RC3 and RC5

[IMAGE alt='image' src='GUID-155C7555-AB83-4A51-B9AE-2CB77E8FBD78-a5.gif']

The only differences between RC3 and RC5 are the number of Walsh repeats; 1 for RC3 and 3
 for RC5.

RC4 and RC6

[IMAGE alt='image' src='GUID-C0E175E4-84E1-4FFE-AC88-2CE74A0AE1C2-a5.gif']

The only differences between RC4 and RC6 are the number of Walsh repeats; 1 for RC4 and 3
 for RC6.

R-FCH

RC1

[IMAGE alt='image' src='GUID-3CB3268D-01BD-498C-8AE3-B4938A06E263-a5.gif']

RC2

[IMAGE alt='image' src='GUID-972475CF-AC10-48E0-ACBD-4D4A06F2BCFE-a5.gif']

RC3 and RC5

[IMAGE alt='image' src='GUID-6A247BF6-4A57-4DB0-BC32-E4B52828F506-a5.gif']

The only differences between RC3 and RC5 are the number of Walsh repeats; 1 for RC3 and 3
 for RC5.

RC4 and RC6

[IMAGE alt='image' src='GUID-9175920D-52C8-4549-AF61-3276961FA759-a5.gif']

The only differences between RC4 and RC6 are the number of Walsh repeats; 1 for RC4 and 3
 for RC6.

R-SCCH

RC1

[IMAGE alt='image' src='GUID-AD46346C-01BE-48FA-9824-28732A315C57-a5.gif']

RC2

[IMAGE alt='image' src='GUID-50BF6A44-0DBF-4508-AE2F-750C889D2892-a5.gif']

R-SCH

RC3

[IMAGE alt='image' src='GUID-D8BC6438-D71B-4CE8-BFF1-7E3C6F031C01-a5.gif']

RC4

[IMAGE alt='image' src='GUID-EB7E569C-5AA2-41B3-A181-D29BCDCE9107-a5.gif']

RC5

[IMAGE alt='image' src='GUID-82342385-CB8D-41DB-B595-E97F3580A3B0-a5.gif']

RC6

[IMAGE alt='image' src='GUID-DACA914C-5A39-43CE-908A-871081FCCF38-a5.gif']

Forward/Downlink Channels

F-SYNCH

[IMAGE alt='image' src='GUID-B3F029CB-5F8A-480A-9E76-F9399EEB037D-a5.gif']

For Spreading rate 1, the number of Walsh repeats is 4; for spreading rate 3, the number
 of Walsh repeats is 12.

F-PCH

This is only available in spreading rate 1.

[IMAGE alt='image' src='GUID-13586FAF-45AC-447B-B4EC-21F311D55283-a5.gif']

F-BCCH

Spreading Rate 1

[IMAGE alt='image' src='GUID-549286B2-C1C3-458F-8332-E8DEDFEFC6DC-a5.gif']

Spreading Rate 3

[IMAGE alt='image' src='GUID-AB649209-86A7-4BA6-AC4A-E289A7EEC61B-a5.gif']

F-QPCH

Spreading Rate 1

[IMAGE alt='image' src='GUID-5A00BC95-CE3B-4A45-9B05-D8319CA0E099-a5.gif']

Spreading Rate 3

[IMAGE alt='image' src='GUID-FC494C80-BCC2-4EF3-9E0A-8B547D6F8D4A-a5.gif']

F-CACH

Spreading Rate 1

[IMAGE alt='image' src='GUID-32CBB39C-2B35-4DD9-B2DA-CE1543D43074-a5.gif']

Spreading Rate 3

[IMAGE alt='image' src='GUID-33D5407A-CB05-4B5A-BA65-D01C82ABE8F0-a5.gif']

F-CCCH

Spreading Rate 1

[IMAGE alt='image' src='GUID-D12F3ED4-2C64-49E0-8CCC-7C6DDF074752-a5.gif']

Spreading Rate 3

[IMAGE alt='image' src='GUID-71908A9B-F036-4AEF-80E6-55BBE5701AE0-a5.gif']

F-DCCH

RC3

[IMAGE alt='image' src='GUID-9247207D-FE21-488D-8AFB-E57E02E1ACBC-a5.gif']

RC4

[IMAGE alt='image' src='GUID-D510D7D9-4BDF-45EE-BE9A-50199E7A00D3-a5.gif']

RC5

[IMAGE alt='image' src='GUID-8D374E02-0768-4F67-8D10-260AE67AB350-a5.gif']

F-FCH

RC1

[IMAGE alt='image' src='GUID-A2098523-7D91-4050-996F-10770DB5E9E1-a5.gif']

RC2

[IMAGE alt='image' src='GUID-693B122C-6BB2-4D44-87D7-1DFBA3F65ABB-a5.gif']

RC3

[IMAGE alt='image' src='GUID-59EE36B8-E2EE-4CB7-8221-90FD4215824F-a5.gif']

RC4

[IMAGE alt='image' src='GUID-655FAFD2-E548-44CB-BFE3-649DF05E2FF1-a5.gif']

RC5

[IMAGE alt='image' src='GUID-7D0D516E-F151-4575-933B-3701AB6A2744-a5.gif']

F-SCCH

RC1

[IMAGE alt='image' src='GUID-FFF62912-56DD-4051-8E02-FCAF7E255BE1-a5.gif']

RC2

[IMAGE alt='image' src='GUID-1B8960D5-331A-404A-B15C-9D6DCEDB48F0-a5.gif']

F-SCH

RC3

[IMAGE alt='image' src='GUID-79E91BF5-F3E2-4F6A-B4CD-5D7768E36748-a5.gif']

RC4

[IMAGE alt='image' src='GUID-5FE8893B-E505-4178-9663-907C7263FF3B-a5.gif']

RC5

[IMAGE alt='image' src='GUID-05B0DF81-11A1-4441-9F49-5DC3A03ADB13-a5.gif']

Parent topic:

CDMA2k (3GPP2)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=channel-spacing.html language=enus -->
## TOPIC 00015: Channel Spacing

- bundle_id: `rfmx-waveform-creator`
- source_path: `channel-spacing.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/channel-spacing.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Channel spacing is the distance between center frequencies of two adjacent component carriers for intra-band contiguous carrier aggregation. The channel spacing between the center frequencies of contiguously aggregated component carriers is a multiple of 300 KHz, in order to be compatible with the 1

### Channel Spacing

Channel spacing is the distance between center frequencies of two adjacent component
 carriers for intra-band contiguous carrier aggregation.

The channel spacing between the center frequencies of contiguously aggregated component
 carriers is a multiple of 300 KHz, in order to be compatible with the 100 KHz frequency
 raster of LTE Rel-8 and to preserve orthogonality of the subcarriers with 15 KHz
 spacing.

For more information about channel spacing, refer to section 5.4.1A of the 3GPP
 TS 36.521-1 specification.

Nominal Channel Spacing

Nominal channel spacing is the maximum allowed spacing between the center frequencies of
 two adjacent component carriers for intra-band contiguous carrier aggregation. To
 configure nominal channel spacing, set the Component Carrier Spacing Type property to
 Nominal.

Nominal channel spacing is defined using the following formula:

[IMAGE alt='image' src='GUID-5463459E-A5C7-4FB3-A886-0FF889C5177A-a5.gif']

where BW<sub>Channel(1)</sub> and
 BW<sub>Channel(2)</sub> are the channel
 bandwidths, in MHz, of the two adjacent E-UTRA component carriers.

For example, in a 20 MHz + 20 MHz intra-band contiguous carrier aggregation scenario, the
 nominal spacing is 19.8 MHz.

Refer to section 5.4.1A of the 3GPP specification for more information
 about nominal channel spacing.

The following table denotes the nominal channel spacing between adjacent carriers for
 specified channel bandwidths.

| Channel Bandwidth (MHz) | Nominal Channel Spacing Between Adjacent Carriers (MHz) |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 1.4 | 3.0 | 5 | 10 | 15 | 20 |  |
| 1.4 | 1.20 | 2.10 | 3.00 | 5.10 | 7.50 | 9.60 |
| 3 | — | 3.00 | 3.90 | 6.00 | 8.40 | 10.50 |
| 5 | — | — | 4.80 | 7.20 | 9.30 | 11.70 |
| 10 | — | — | — | 9.90 | 12.00 | 14.40 |
| 15 | — | — | — | — | 15.00 | 17.10 |
| 20 | — | — | — | — | — | 19.80 |

Minimum Channel Spacing

Minimum channel spacing is the smallest possible value of channel spacing. Minimum
 channel spacing ensures that the transmission bandwidth configurations do not overlap
 when setting the channel spacing to a multiple of 300 KHz. To configure minimum channel
 spacing, set the Component Carrier Spacing Type to Minimum.

Refer to table 5.7.1-2 of the 3GPP TS 36.808 specification for more
 information about minimum channel spacing.

The following table denotes the minimum channel spacing between adjacent carriers for
 specified channel bandwidths.

| Channel Bandwidth (MHz) | Minimum Channel Spacing between Adjacent Carriers (MHz) |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 1.4 | 3.0 | 5 | 10 | 15 | 20 |  |
| 1.4 | 1.20 | 2.10 | 3.00 | 5.10 | 7.50 | 9.60 |
| 3 | — | 3.00 | 3.90 | 6.00 | 8.40 | 10.50 |
| 5 | — | — | 4.80 | 6.90 | 9.30 | 11.40 |
| 10 | — | — | — | 9.30 | 11.40 | 13.80 |
| 15 | — | — | — | — | 13.80 | 15.90 |
| 20 | — | — | — | — | — | 18.30 |

User-Specific Channel Spacing

You can configure the spacing type between component carriers by setting the Component
 Carrier Spacing Type property to User and configuring the
 component carrier frequency for each component carrier.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=compressed-mode.html language=enus -->
## TOPIC 00016: Compressed Mode

- bundle_id: `rfmx-waveform-creator`
- source_path: `compressed-mode.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/compressed-mode.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Inter-frequency handovers are needed to pass data from one radio frequency in one cell to another radio frequency in another cell. This is more important for inter-operability between 3GPP FDD and second-generation systems such as GSM or IS-95. In order to complete inter-frequency handovers, an effi

### Compressed Mode

Inter-frequency handovers are needed to pass data from one radio frequency in one cell to
 another radio frequency in another cell. This is more important for inter-operability
 between 3GPP FDD and second-generation systems such as GSM or IS-95.

In order to complete inter-frequency handovers, an efficient method is needed for making
 measurements on other frequencies while still having the connection running on the
 current frequency. In 3GPP (FDD) this is achieved by using compressed mode, which
 effectively interrupts the signal for a short time as demonstrated in the following
 figure.

[IMAGE alt='image' src='GUID-56AEA0BD-C7F5-4D3F-B14F-1CE3407C0AF1-a5.gif']

Although a transmission gap effectively reduces the amount of transmission time
 available, the quality of service must not be affected. This is achieved by increasing
 the volume of data transmitted in the remaining time; the data is compressed. This is
 done by following methods and it depends on the link direction.

- Higher layer scheduling
- Reducing the spreading factor by 2
- Puncturing

In downlink, all the three methods are applicable; however in uplink, the puncturing
 method is not used.

Frames containing no transmission gaps are sent with the same slot format and the same
 power as in the non-compressed mode. A different slot format usually with a higher
 number of pilot bits is used in the compressed ranges.

The uplink transmit power can be increased (CM power offset mode) automatically or
 manually by defining a power offset.

Transmission Gaps

In compressed mode, slots from N<sub>first</sub> to N<sub>last</sub> are not used for
 transmission of data. This is referred as a transmission gap length (TGL). The
 transmission gap has a maximum length of 14 slots. Since at least eight active slots
 must be sent per frame, gaps comprising seven slots and more have to be distributed over
 two neighboring frames, as shown in the following figure.

[IMAGE alt='image' src='GUID-68C314BC-60A3-4BD6-9734-F8DE6455950B-a5.gif']

Frame Structures

Uplink

In compressed mode, DPCCH slot formats with TFCI fields are changed. There are two
 possible compressed slot formats for each normal slot format. The selection between them
 is dependent on the number of slots that are transmitted in each frame in compressed
 mode. The following figure represents the frame structure in uplink compressed mode
 transmission.

[IMAGE alt='image' src='GUID-2BE4EC51-951F-40B2-BA75-7265A865E29E-a5.gif']

Downlink

There are two different types of frame structures defined for downlink compressed mode.
 Type A maximizes the transmission gap length and type B is optimized for power
 control.

For type A, the pilot field of the last slot in the transmission gap is transmitted.
 Transmission is turned off for the rest of the transmission gap, as shown in the
 following figure.

For type B, the TPC field of the first slot in the transmission gap and the pilot field
 of the last slot in the transmission gap are transmitted. Transmission is turned off for
 the rest of the transmission gap.

[IMAGE alt='image' src='GUID-AF6847D1-5729-4673-8932-5FFDCE115766-a5.gif']

Transmission Gap Pattern

The transmitted signal consists of two patterns that are sent alternately and each
 pattern comprises two transmission gaps, as shown in the following figure.

[IMAGE alt='image' src='GUID-DB7F225A-8C51-4769-9EEA-E5738D55431E-a5.gif']

The preceding diagram includes all the parameters necessary to define the transmission
 gaps in the signal and are characterized as follows:

- TGSN (Transmission Gap Starting slot Number) : Slot number of
 the first missing (idle) slot in the transmission gap.
- TGL1 (Transmission Gap Length 1) : Duration of the first
 transmission gap. This value is expressed in number of slots.
- TGL2 (Transmission Gap Length 2) : Duration of the second
 transmission gap. This value is expressed in number of slots.
- TGD (Transmission Gap start Distance) : Duration between the
 two transmission gaps within a transmission gap pattern. This value is expressed in
 number of slots.
- TGPL1 (Transmission Gap Pattern Length) : Duration of the
 first transmission gap pattern. This value is expressed in number of frames.
- TGPL2 (Transmission Gap Pattern Length) : Duration of the
 second transmission gap pattern. This value is expressed in number of frames.

Parent topic:

WCDMA (3GPP FDD Release 8)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=configuring-a-td-scdma-3gpp-tdd-lcr-cell.html language=enus -->
## TOPIC 00017: Configuring a TD-SCDMA (3GPP TDD-LCR) Cell

- bundle_id: `rfmx-waveform-creator`
- source_path: `configuring-a-td-scdma-3gpp-tdd-lcr-cell.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/configuring-a-td-scdma-3gpp-tdd-lcr-cell.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The main Modulation tab consists of two parts, Cell Configuration and Frame Configuration. The Cell Configuration portion at the top of the Modulation tab allows you to change the top level parameters of the TD-SCDMA Cell. The Frame Configuration portion allows you to modify the different portions o

### Configuring a TD-SCDMA (3GPP TDD-LCR) Cell

The main Modulation tab consists of two parts, Cell
 Configuration and Frame Configuration.

The Cell Configuration portion at the top of the
 Modulation tab allows you to change the top level parameters
 of the TD-SCDMA Cell.

The Frame Configuration portion allows you to modify the different
 portions of the TD-SCDMA frame being transmitted. A graphical representation of the
 frame is shown in this portion that allows you to configure the individual slots within
 the frame.

SYNC-DL Code

This sets the SYNC-DL for the cell. The SYNC-DLcode must be in the range 0 to 31. There
 is only one SYNC-DL code per code group. When the SYNC-DL is changed, the code group is
 set to the one corresponding to the current SYNC-DL. This means that the set of SYNC-UL
 and scrambling codes that can be selected changes whenever the SYNC-DL is changed. The
 SYNC-DL code can be set using the edit box on the modulation page. The sync DL Code can
 also be modified by using the DwPTS configuration dialog. This can be selected by either
 double-clicking on the DwPTS cell with the slot graphic, or by selecting DwPTS from the
 slot graphic and clicking Configure Slot.

[IMAGE alt='image' src='GUID-BFC6C149-1E6F-4315-A614-D3B78AA861CC-a5.gif']

Fig. 6-13DwPTS dialog

In addition to being able to set the SYNC-DL code, the DwPTS configuration dialog box
 lets you set the following parameters:

State

This sets the state of the slot. When this control is selected, the slot will be
 transmitted; otherwise the slot is not transmitted. The default is on (selected). The
 DwPTS State may also be changed by right clicking on the DwPTS element in the slot
 graphic.

Power

This is the power/gain of the slot in dB (relative to the other slots). The value must be
 between 0 and –60 dB.

SYNC-UL Code

This sets SYNC-UL code for the cell. The drop-down menu lets you select any of the eight
 SYNC-UL codes belonging to the current code group. The SYNC-UL code can be set using the
 edit box on the modulation page. The sync DL Code can also be modified by using the
 UpPTS configuration dialog. This can be selected by either double clicking on the UpPTS
 cell with the slot graphic, or by selecting UpPTS from the slot graphic and clicking
 Configure Slot. This will show the dialog box as illustrated
 in the following figure.

[IMAGE alt='image' src='GUID-753B582B-B79E-461E-98F9-45936C9B3403-a5.gif']

Fig. 6-14 UpPTS dialog

In addition to being able to set the SYNC-DL code the UpPTS configuration dialog lets you
 set the following parameters:

State

This sets the state of the slot. When this control is selected, the slot will be
 transmitted, otherwise the slot is not transmitted. The default is on (selected). The
 UpPTS State may also be changed by right clicking on the UpPTS element in the slot
 graphic.

Power

This is the power/gain of the slot in dB (relative to the other slots). The value must be
 between 0 and –60 dB.

Scrambling Code

This sets the scrambling code for the cell. The scrambling can be any of the four
 scrambling codes belonging to the current code group. As the basic midamble and
 scrambling code must be the same, the midamble code is also changed whenever the
 scrambling code is changed.

Parent topic:

TD-SCDMA (3GPP TDD-LCR)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=configuring-a-td-scdma-3gpp-tdd-lcr-frame.html language=enus -->
## TOPIC 00018: Configuring a TD-SCDMA (3GPP TDD-LCR) Frame

- bundle_id: `rfmx-waveform-creator`
- source_path: `configuring-a-td-scdma-3gpp-tdd-lcr-frame.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/configuring-a-td-scdma-3gpp-tdd-lcr-frame.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Number of Sub-Frames This sets the number of sub-frames to be generated. The valid range is 1–1000. Switching Point This parameter sets the switching point position in the frame. There are five different positions. The valid switching point range is 1–5. When changing the switching point, the slot g

### Configuring a TD-SCDMA (3GPP TDD-LCR) Frame

Number of Sub-Frames

This sets the number of sub-frames to be generated. The valid range is 1–1000.

Switching Point

This parameter sets the switching point position in the frame. There are five different
 positions. The valid switching point range is 1–5. When changing the switching point,
 the slot graphic below will update it’s representation to highlight the new value.

Parent topic:

TD-SCDMA (3GPP TDD-LCR)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=configuring-a-traffic-slot.html language=enus -->
## TOPIC 00019: Configuring a Traffic Slot

- bundle_id: `rfmx-waveform-creator`
- source_path: `configuring-a-traffic-slot.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/configuring-a-traffic-slot.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: A Traffic slot (Ts0 to Ts6) can be configured by double-clicking on the timeslot graphic, or by clicking the slot graphic and selecting Configure Slot as shown in the following figure. Fig. 6-15 Traffic slot configuration dialog When configuring a traffic slot you are presented with a dialog similar

### Configuring a Traffic Slot

A Traffic slot (Ts0 to Ts6) can be configured by double-clicking on the timeslot graphic,
 or by clicking the slot graphic and selecting Configure Slot as
 shown in the following figure.

[IMAGE alt='image' src='GUID-06976772-B001-4923-B10C-7973FBCD83B1-a5.gif']

Fig. 6-15 Traffic slot configuration dialog

When configuring a traffic slot you are presented with a dialog similar to the one shown
 in the above figure. The following settings can be configured:

State

This parameter sets the state of the slot. When this control is selected, the slot will
 be transmitted, otherwise the slot is not transmitted. The default is On (selected). The
 Traffic Slot State may also be changed by right clicking on the relevant element in the
 slot graphic and using the context menu to change the current value.

Power

This is the power/gain of the slot in dB (relative to the other slots). The value must be
 between 0 and –60 dB.

Maximum Number of Users (K)

This parameter sets the maximum user ID that can be used in the slot. If you change the
 user ID to a value that is less than the user ID used by one of the channels, then you
 are asked if you want to set the user ID of the channel to 1 before continuing.

Channels

Each Traffic slot has a set of uplink channels and a set of downlink channels which are
 represented within the main table of the Traffic Slot
 Configuration dialog box. The set of channels that can be configured is
 dependent on the slot’s link direction.

You can add, edit, or remove a channel from a traffic slot using the
 Add, Edit, or
 Remove buttons at the bottom of the Traffic
 Slot dialog box. When you add a new channel to the traffic slot, a new
 row within the table will be automatically added. While you can edit most of the channel
 parameters by double-clicking on the parameter of interest within the table, you can
 also get a more detailed view of the individual channel parameters by highlighting the
 desired channel and clicking the Edit.. button at the bottom of
 the Traffic Slot Configuration dialog box. This will present the
 dialog box shown in the following figure.

[IMAGE alt='image' src='GUID-0CC3E079-5CCE-4647-B000-5B69B182B1DF-a5.gif']

Fig. 6-16 Traffic channel configuration dialog

The following channel settings can be configured;

Modulation Type

This parameter sets the type of modulation to be used when transmitting the data bursts.
 The modulation can currently be set to either QPSK or 8PSK.

Slot Format

This parameter sets the slot format used by the channel. The slot format determines the
 spreading factor, and the number of Data, TFCI, SS, and TPC bits transmitted by the
 channel. The range of slot format values is displayed to the right of the slot format
 edit box. The range of slot formats is dependent on link direction and modulation type.
 When the channel’s slot format is changed, the channel graphic is updated to show the
 number of Data, TFCI, SS, and TPC bits used with the new slot format.

Channel Code

This parameter sets the channelization code used by the channel. The range of selectable
 values is dependent on the spreading factor currently in use. If the chosen
 channelization code conflicts with channels currently transmitted in the slot, the
 specific channels that are in conflict will be highlighted red as shown in the following
 figure.

[IMAGE alt='image' src='GUID-516C187E-E2A2-4C8B-9CB9-D2078E96486C-a5.gif']

Fig. 6-17 Channel conflicts warning

Data Bits Data Source

This parameter lets you select the type of data used to produce the channel’s data bits.
 Refer to Selecting the Data Source topic for more information on data source.

TFCI Bits

This parameter lets you set the TFCI index. The TFCI index is used to produce the TFCI
 code word. The TFCI index should be between 0 and the maximum TFCI value displayed to
 the right hand side of the TFCI edit box.

SS Bits Data Source

This parameter lets you select the type of data used to produce the channel’s SS bits.
 Refer to Selecting the Data Source topic for more information on data source.

TPC Bits Data Source

This parameter lets you select the type of data used to produce the channel’s TPC bits.
 Refer to Selecting the Data Source topic for more information on data source.

Parent topic:

TD-SCDMA (3GPP TDD-LCR)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=configuring-active-channels-labview2.html language=enus -->
## TOPIC 00020: Configuring Active Channels (LabVIEW)

- bundle_id: `rfmx-waveform-creator`
- source_path: `configuring-active-channels-labview2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/configuring-active-channels-labview2.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To work with channel parameters and properties, specify an active channel using the Active Channel property or the Active Channel parameter of a VI. Such parameters and properties are channel-specific parameters and properties. An active channel is one of many entities that share the same channel-sp

### Configuring Active Channels (LabVIEW)

To work with channel parameters and properties, specify an active channel using the *Active
 Channel* property or the Active Channel parameter of a
 VI. Such parameters and properties are channel-specific parameters and properties. An
 active channel is one of many entities that share the same channel-specific parameters
 and properties. Other entities include the following:

- Segments,
- Receive channels,
- Space-time streams (or spatial streams),
- Combinations of a segment, receive channel, and a space-time stream,
- Users for a multiple-input multiple-output OFDM signal conforming to the following
 standards:
  - IEEE Standard 802.11n-2009 .
  - IEEE Standard 802.11ac-2013 .
  - IEEE P802.11ah/D1.3 .
  - IEEE Standard 802.11af-2013 .
  - IEEE P802.11ax/D8.0 .
  - IEEE P802.11be/D7.0, or IEEE P802.11bn/D0.3 .

Set the Active Channel parameter or property for channel-specific
 parameters and channel-specific properties only when you set the *Standard
 Property* to one of the following values:

- 80211N MIMOOFDM
- 80211AC MIMOOFDM
- 80211AH MIMOOFDM
- 80211AF MIMOOFDM
- 80211AX MIMOOFDM

You must specify a valid active channel string. The following table lists the various
 valid channels for different standards. The following table lists the various valid
 active channel strings for different standards.

| Standard | Valid Active Channel Strings | Comments |
| --- | --- | --- |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "channelx" | Indicates a channel with index x. |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "channelx - channely" | x < y Indicates all channels with index x to y, both inclusive. |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "channelx, channely, channelv - channelw" | Indicates channels specified by each comma-separated string. |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "streamx" | Indicates an space-time stream with index x. |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "channelx/streamy" | Indicates a space-time stream with index y in channel x. |
| 80211AC MIMOOFDM | "[segmentx]" | Indicates a segment with index x. You may use "" (empty string), if the Number of Segments property is set to 1. |
| 80211AC MIMOOFDM | "segmentx - segmenty" | x < y Indicates all segments with index x to y, both inclusive. |
| 80211AC MIMOOFDM | "segmentx, segmenty" | Indicates two segments with indices x and y, respectively. |
| 80211AC MIMOOFDM | "[segmentx/]channely" | Indicates a channel, with index y, of the segment with index x. "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AC MIMOOFDM | "[segmentx/]channely - channelz" | y < z Indicates all channels, with index y to z, both inclusive, in the segment with index x "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AC MIMOOFDM | "segmentx - segmenty/channel - channelw" | x < y, v < w Indicates all channels, with index v to w, both inclusive, in the segments with index x to y, both inclusive. |
| 80211AC MIMOOFDM | "[segmentx/]streamy" | Indicates a stream, with index y, of segment with index x. "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AC MIMOOFDM | "[segmentx/]channely/streamz" | Indicates a stream, with index z, in channel with index y of segment with index x. "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AC MIMOOFDM | "userx" | Indicates a user with index x. |
| 80211AC MIMOOFDM | "userx/[segmenty/]streamz" | Indicates a stream, with index z, of segment with index y, of user with index x. "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, or 80211G DSSSOFDM | "" | Indicates an empty string. |
| 80211AF MIMOOFDM | "[segmentx]" | Indicates a segment with index x. You may use "" (empty string), if the Number of Segments property is set to 1. |
| 80211AF MIMOOFDM | "[segmentx/]channely" | Indicates a channel, with index y, of the segment with index x. "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AF MIMOOFDM | "[segmentx/]streamy" | Indicates a stream, with index y, of segment with index x. "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AF MIMOOFDM | "[segmentx/]channely/streamz" | Indicates a stream, with index z, in channel with index y of segment with index x. "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM | "[segmentx]" | Indicates a segment with index x. You may use "" (empty string), if the Number of Segments property is set to 1. |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM | "segmentx - segmenty" | x < y Indicates all segments with index x to y, both inclusive. |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM | "segmentx, segmenty" | Indicates two segments with indices x and y, respectively. |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM | "[segmentx/]channely" | Indicates a channel, with index y, of the segment with index x. "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM | "[segmentx/]channely - channelz" | y < z Indicates all channels, with index y to z, both inclusive, in the segment with index x "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM | "segmentx - segmenty/channelv - channelw" | x < y, v < w Indicates all channels, with index v to w, both inclusive, in the segments with index x to y, both inclusive. |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM | "[segmentx/]streamy" | Indicates a stream, with index y, of segment with index x. "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM | "[segmentx/]channely/streamz" | Indicates a stream, with index z, in channel with index y of segment with index x. "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM | "userx" | Indicates a user with index x. |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM | "userx/[segmenty/]channelz" | Indicates a channel, with index z, of segment with index y, of user with index x. "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM | "userx/[segmenty/]streamz" | Indicates a stream, with index z, of segment with index y, of user with index x. "segment0/" is optional, if the Number of Segments property is set to 1. |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM | "userw/[segmentx/]channely/streamz" | Indicates a stream, with index z, in channel with index y of segment with index x, of user with index w. "segment0/" is optional, if the Number of Segments property is set to 1. |

Note

Note

Standard

80211A/G/J/P OFDM

80211B/G DSSS

80211G DSSSOFDM

#### Active Channel Syntax to Set
 Properties

Use the Active Channel property on the property node to
 configure the properties of a channel. For example, the following block diagram
 shows how you can set the spectral mask reference level to -70 dBm/Hz for
 channel1 and -71 dBm/Hz for channel2. The
 toolkit sets the spectral mask reference level for channel0 and
 channel3to the default values.

[IMAGE alt='image' src='GUID-40C25F96-2EF4-4709-93B2-C962272F16EB-a5.gif']

To set the same value on multiple channels, use an active channel to indicate
 a list of channels that you want to configure. The following block diagram shows how
 you can configure channel1 and channel2 to have a
 spectral mask reference level of -70 dBm/Hz.

[IMAGE alt='image' src='GUID-9DCD3D42-0B81-468B-A914-EE5ADC2928F9-a5.gif']

You can also use an active channel to indicate the range of channels that you
 want to configure. The following block diagram shows how you can configure
 channel0, channel1, channel2,
 and channel3 to have a spectral mask reference level of -70 dBm/Hz.

[IMAGE alt='image' src='GUID-1D94DF31-9688-4D69-A9B5-C124CE4BDD65-a5.gif']

If you set the active channel to "" (empty string) and
 configure a channel-based property, the toolkit sets this property to the configured
 value for all the channels. In the following block diagram, the toolkit sets the
 spectral mask reference level to -70 dB for all the channels.

[IMAGE alt='image' src='GUID-8C8130E5-B516-4E4C-B41B-EB9EA535727C-a5.gif']

If you specify an active channel, you can configure only channel-specific
 properties for the specified channel. The toolkit returns an error if you configure
 non-channel specific properties.

#### Active Channel Syntax to Get Properties

You can read multiple properties for an active channel on one instance of the
 property node, as shown in the following block diagram.

[IMAGE alt='image' src='GUID-7F61456B-F88E-4A38-973F-AF26E43227CB-a5.gif']

Use a stream active channel string to configure the active channel for
 stream-based properties.

[IMAGE alt='image' src='GUID-7A1D360A-E0B3-4462-82C9-125CA92324DC-a5.gif']

You must specify an active channel string for each channel to read multiple
 properties. The following block diagram shows how to specify the active channel for
 each channel to read the RMS EVM.

[IMAGE alt='image' src='GUID-A19788C9-A4EC-4DF0-9B64-085F66C21070-a5.gif']

You can also use a For Loop to read properties for multiple channels.

[IMAGE alt='image' src='GUID-4B0C9B3D-E29E-4FAE-94AE-830EE560E0ED-a5.gif']

If you specify an active channel, you can read only channel-specific
 properties for the specified channel. The toolkit returns an error if you attempt to
 read non-channel-specific properties.

Parent topic:

WLAN

<!--NI_TOPIC bundle=rfmx-waveform-creator path=configuring-active-channels-labwindows-cvi2.html language=enus -->
## TOPIC 00021: Configuring Active Channels (LabWindows™/CVI™)

- bundle_id: `rfmx-waveform-creator`
- source_path: `configuring-active-channels-labwindows-cvi2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/configuring-active-channels-labwindows-cvi2.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To set or get certain parameters and attributes you must specify an active channel using the channelString parameter. Such parameters and attributes are referred to as channel-specific parameters and attributes. An active channel is one of many entities which share the same channel-specific paramete

### Configuring Active Channels
 (LabWindows™/CVI™)

To set or get certain parameters and attributes you must specify an active channel using the
 channelString parameter. Such parameters and attributes are
 referred to as channel-specific parameters and attributes. An active channel is one of
 many entities which share the same channel-specific parameters and attributes. Other
 entities include:

Such entities are segments, receive channels, space-time streams (or spatial streams) and
 combinations of a segment, receive channel, and a space-time stream and users for a
 multiple-input multiple-output OFDM signal conforming to the following standards.

- Segments,
- Receive channels,
- Space-time streams (or spatial streams),
- Combinations of a segment, receive channel, and a space-time stream,
- Users for a multiple-input multiple-output OFDM signal conforming to the following
 standards,
  - IEEE Standard 802.11n-2009.
  - IEEE Standard 802.11ac-2013.
  - IEEE Standard P802.11ah/D1.3.
  - IEEE Standard 802.11af-2013.
  - IEEE P802.11ax/D6.0.

You must use the channelString parameter for channel-specific parameters
 and attributes only when you set the *NIWLANA_STANDARD*
 attribute to NIWLANA_VAL_STANDARD_80211N_MIMO_OFDM,
 NIWLANA_VAL_STANDARD_80211AC_MIMO_OFDM,
 NIWLANA_VAL_STANDARD_80211AH_MIMO_OFDM,
 NIWLANA_VAL_STANDARD_80211AF_MIMO_OFDM, or
 NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM.

You must specify a valid channel string. The following table lists the valid active
 channel strings for different standards:

| NIWLANA_STANDARD | Valid Active Channel Strings | Comments |
| --- | --- | --- |
| NIWLANA_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANA_VAL_STANDARD_80211AH_MIMO_OFDM | "channelx" | Indicates a channel with index x. |
| NIWLANA_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANA_VAL_STANDARD_80211AH_MIMO_OFDM | "channelx - channely" | x < y Indicates all channels with index x to y, both inclusive. |
| NIWLANA_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANA_VAL_STANDARD_80211AH_MIMO_OFDM | "channelx, channely, channelv - channelw" | Indicates channels specified by each comma-separated string. |
| NIWLANA_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANA_VAL_STANDARD_80211AH_MIMO_OFDM | "streamx" | Indicates an space-time stream with index x. |
| NIWLANA_VAL_STANDARD_80211N_MIMO_OFDM, NIWLANA_VAL_STANDARD_80211AH_MIMO_OFDM | "channelx/streamy" | Indicates a space-time stream with index y in channel x. |
| NIWLANA_VAL_STANDARD_80211AC_MIMO_OFDM | "[segmentx]" | Indicates a segment with index x. You may use "" (empty string) if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AC_MIMO_OFDM | "segmentx - segmenty" | x < y Indicates all segments with index x to y, both inclusive. |
| NIWLANA_VAL_STANDARD_80211AC_MIMO_OFDM | "segmentx, segmenty" | Indicates two segments with indices x and y, respectively. |
| NIWLANA_VAL_STANDARD_80211AC_MIMO_OFDM | "[segmentx/]channely" | Indicates a channel, with index y, of the segment with index x. "segment0/" is optional if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AC_MIMO_OFDM | "[segmentx/]channely - channelz" | y < z Indicates all channels, with index y to z, both inclusive, in the segment with index x. "segment0/" is optional if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AC_MIMO_OFDM | "segmentx - segmenty/channelv - channelw" | x < y, v < w Indicates all channels, with index v to w, both inclusive, in the segments with index x to y, both inclusive. |
| NIWLANA_VAL_STANDARD_80211AC_MIMO_OFDM | "[segmentx/]streamy" | Indicates a stream, with index y, of segment with index x. "segment0/" is optional if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AC_MIMO_OFDM | "[segmentx/]channely/streamz" | Indicates a stream, with index z, in channel with index y of segment with index x. "segment0/" is optional if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AC_MIMO_OFDM | "userx" | Indicates a user with index x. |
| NIWLANA_VAL_STANDARD_80211AC_MIMO_OFDM | "userx/[segmenty/]streamz" | Indicates a stream, with index z, of segment with index y, of user with index x. "segment0/" is optional, if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AG_OFDM or NIWLANA_VAL_STANDARD_80211J_OFDM or NIWLANA_VAL_STANDARD_80211P_OFDM or NIWLANA_VAL_STANDARD_80211BG_DSSS or NIWLANA_VAL_STANDARD_80211G_DSSS_OFDM | "" | Indicates an empty string. |
| NIWLANA_VAL_STANDARD_80211AF_MIMO_OFDM | "[segmentx]" | Indicates a segment with index x. You may use "" (empty string) if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AF_MIMO_OFDM | "[segmentx/]channely" | Indicates a channel, with index y, of the segment with index x. "segment0/" is optional if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AF_MIMO_OFDM | "[segmentx/]streamy" | Indicates a stream, with index y, of segment with index x. "segment0/" is optional if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AF_MIMO_OFDM | "[segmentx/]channely/streamz" | Indicates a stream, with index z, in channel with index y of segment with index x. "segment0/" is optional if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM | "[segmentx]" | Indicates a segment with index x. You may use "" (empty string) if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM | "segmentx - segmenty" | x < y Indicates all segments with index x to y, both inclusive. |
| NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM | "segmentx, segmenty" | Indicates two segments with indices x and y, respectively. |
| NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM | "[segmentx/]channely" | Indicates a channel, with index y, of the segment with index x. "segment0/" is optional if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM | "[segmentx/]channely - channelz" | y < z Indicates all channels, with index y to z, both inclusive, in the segment with index x. "segment0/" is optional if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM | "segmentx - segmenty/channelv - channelw" | x < y, v < w Indicates all channels, with index v to w, both inclusive, in the segments with index x to y, both inclusive. |
| NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM | "[segmentx/]streamy" | Indicates a stream, with index y, of segment with index x. "segment0/" is optional if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM | "[segmentx/]channely/streamz" | Indicates a stream, with index z, in channel with index y of segment with index x. "segment0/" is optional if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM | "userx" | Indicates a user with index x. |
| NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM | "userx/[segmenty/]channelz" | Indicates a channel, with index z, of segment with index y, of user with index x. "segment0/" is optional, if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM | "userx/[segmenty/]streamz" | Indicates a stream, with index z, of segment with index y, of user with index x. "segment0/" is optional, if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |
| NIWLANA_VAL_STANDARD_80211AX_MIMO_OFDM | "userw/[segmentx/]channely/streamz" | Indicates a stream, with index z, in channel with index y of segment with index x, of user with index w. "segment0/" is optional, if the NIWLANA_NUMBER_OF_SEGMENTS attribute is set to 1. |

Note

#### Active Channel String Syntax to Set Channel-Specific Parameters

You must
 specify the active channel for configuring channel-specific parameters and
 attributes using the channelString parameter. In the
 following example, the spectral mask reference level is set to -70 dBm/Hz for
 receive channel1 and -71 dBm/Hz for receive
 channel2. The toolkit sets the spectral mask reference level
 for receive channel0 and receive channel3 to the default
 values.

niWLANA_SetStandard (analysisSession, NULL,
 NIWLANA_VAL_STANDARD_80211N_MIMO_OFDM);

niWLANA_SetNumberOfReceiveChannels (analysisSession, NULL, 4);

niWLANA_SetScalarAttributeF64 (analysisSession, "channel1",
 NIWLANA_SPECTRAL_MASK_REFERENCE_LEVEL, -70);

niWLANA_SetScalarAttributeF64 (analysisSession, "channel2",
 NIWLANA_SPECTRAL_MASK_REFERENCE_LEVEL, -71);

To set the same parameter or attribute value on multiple channels, use the
 channelString parameter to indicate a list of channels
 that you want to configure. In the following example, receive
 channel1 and receive channel2 are configured
 to have a spectral mask reference level of -70 dBm/Hz.

niWLANA_SetScalarAttributeF64 (analysisSession, "channel1, channel2",
 NIWLANA_SPECTRAL_MASK_REFERENCE_LEVEL, -70);

You can also use the channelString parameter to indicate
 the range of channels that you want to configure. In the following example, receive
 channel0, receive channel1, receive
 channel2, and receive channel3 are configured to have a
 spectral mask reference level of -70 dBm/Hz.

niWLANA_SetScalarAttributeF64 (analysisSession, "channel0-channel3",
 NIWLANA_SPECTRAL_MASK_REFERENCE_LEVEL, -70);

If you set the channelString parameter to "" (empty
 string) or NULL and configure a channel-specific parameter, the
 toolkit sets the channel-specific parameter to the configured value for all the
 channels. In the following example, the toolkit sets the spectral mask reference
 level to -70 dBm/Hz for all the receive channels.

niWLANA_SetScalarAttributeF64 (analysisSession, "",
 NIWLANA_SPECTRAL_MASK_REFERENCE_LEVEL, -70);

or

niWLANA_SetScalarAttributeF64 (analysisSession, NULL,
 NIWLANA_SPECTRAL_MASK_REFERENCE_LEVEL, -70);

If you set the channelString parameter to values other
 than "" (empty string) or NULL, you can configure
 only channel-specific parameters or attributes for the specified channel. The
 toolkit returns an error if you configure parameters or attributes that are not
 channel-specific.

#### Active Channel String Syntax to Get Channel-Specific Parameters

You can
 specify the active channel for reading channel-based parameters using the
 channelString parameter. In the following example,
 Spectral Mask Margin is queried for a receive channel0.

niWLANA_GetSpectralMaskMargin (analysisSession, "channel0",
 &spectralMaskMargin);

You can read the parameter or attribute values for only one channel at a
 time.

For parameters or attributes which can be queried for stream-time
 stream, configure the channelString parameter as shown in the
 following example.

niWLANA_GetOFDMDemodRMSEVM (analysisSession, "stream0",
 &RMSEVM);

For parameters or attributes which can be queried for the combination of a
 receive channel and a space-time stream, configure the
 channelString parameter as shown in the following
 example.

niWLANA_GetOFDMDemodCrossPower (analysisSession, "channel0/stream1",
 &crossPower);

If you use the channelString parameter, you can read only
 channel-specific parameters or attributes for the specified channel. The toolkit
 returns an error if you read parameters or attributes that are not channel-specific.
 In the following example, the channelString parameter is set
 to channel2. The toolkit returns an error because the
 clockOffset parameter is not channel-specific.

niWLANA_GetOFDMDemodSampleClockOffset (analysisSession, "channel2",
 &clockOffset);

Parent topic:

WLAN

<!--NI_TOPIC bundle=rfmx-waveform-creator path=configuring-lo-connection-in-wlan-generation.html language=enus -->
## TOPIC 00022: Configuring LO Connection in WLAN Generation Soft Front Panel

- bundle_id: `rfmx-waveform-creator`
- source_path: `configuring-lo-connection-in-wlan-generation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/configuring-lo-connection-in-wlan-generation.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: WLAN Generation Soft Front Panel supports configuring the LO connections.The following image shows the LO Connection Configuration window in the WLAN Generation Soft Front Panel. Navigating to LO Configuration WindowComplete the following steps to configure the LO connections: Navigate to Start»All

### Configuring LO Connection in WLAN Generation Soft Front Panel

WLAN Generation Soft Front Panel supports configuring the LO connections.

The following image shows the LO Connection Configuration window in the
 WLAN Generation Soft Front Panel.

[IMAGE alt='image' src='GUID-87AC6AA2-2574-4F13-BE3E-58CEA84AD741-a5.png']

#### Navigating to LO Configuration Window

Complete the following steps
 to configure the LO connections:

1. Navigate to Start » All
 Programs » National
 Instruments» WLAN Generation
 Toolkit» WLAN Generation Soft Front Panel 
 to launch the WLAN Generation Soft Front Panel.
2. Click on the Hardware Settings tab, as illustrated in the
 following figure. [IMAGE alt='image' src='GUID-910A20AF-9E02-4849-84F0-45839C470D9B-a5.png']
3. Click the Configure LO button. [IMAGE alt='image' src='GUID-C4FEB047-ACAF-42FA-B610-32115141299A-a5.png']

#### Configuring the Local Oscillator Parameters

The following figure
 illustrates the elements of the Configure Local Oscillator
 window.

[IMAGE alt='image' src='GUID-42FD6A67-ED32-4BC9-9D42-3FA39539F402-a5.png']

1. Specify Connection : Use this button to open the
 LO Connection Configuration window and specify the
 hardware connections. For more details on how to specify the connections, refer
 to the Specifying LO Connection in LO Connection Configuration Window section of
 this topic.
2. Master LO Source : In an LO section, 'Master' is an NI RF
 Vector Signal Generator from which other NI RF Vector Signal Generators are
 connected in a daisy chain fashion. The value of this control applies to the
 Master Generator. In an LO section, when NI RF Vector Signal Generators are not
 connected in a daisy chain fashion, the value of this control applies to all the
 NI RF Vector Signal Generators. Select Onboard LO to use
 the Onboard local oscillator for the Master Generator. Select
 External LO to use external local oscillator
 device/signal as the LO Source for the Master Generator. For more details, refer
 to the Specifying LO Connection in LO Connection Configuration Window section of
 this topic.
3. External LO Configuration: Use the Control
 External LO Device(s) check box to control the selected external
 LO devices. Choose the External LO resource names in the Ext LO
 Resource drop down menu. The respective reference clock for the
 external LO devices are selected in the Ref Clock Source 
 drop down menu. Use the Clear All button to clear the
 values of the Ext LO Resource and Ref Clock
 Source columns.
4. LO Export to External Devices Enabled: Turn on this option if you are
 exporting the LO signal from an NI RF Vector Signal Generator device to an NI RF
 Vector Signal Analyzer device.
5. LO Frequency Offset Mode: Select
 Auto to automatically configure the LO Frequency
 Offset. If you want to set the LO Frequency Offset to any other value, select
 User defined from the drop down menu, and specify the
 desired value for the LO Frequency Offset in the LO Frequency
 Offset . If LO Frequency Offset Mode is
 Disabled , LO Frequency Offset will be set to
 0 Hz.

#### Specifying LO Connection in a LO Connection Configuration
 Window

Use the LO Connection Configuration window
 to specify the LO connections.

[IMAGE alt='image' src='GUID-1F36EED8-8185-499C-964B-7A91B5E93B50-a5.png']

#### Use Default from WLAN Calibration
 Utility

Select Use Default from WLAN Calibration Utility check box to
 load the default LO connection configuration saved from the WLAN Calibration
 Utility. From the default configuration, all the NI RF Vector Signal Generators, NI
 RF Vector Signal Analyzers, and External LO Devices (PXIe 5653) along with the LO
 connection topology, their respective model, chassis, and slot numbers are populated
 in the configuration tree. WLAN Generation Soft Front Panel launches with the
 default LO connection configuration, if found.

You cannot edit the configuration tree when this checkbox is selected. If you need to
 change the LO connections, deselect this checkbox, drag and drop the hardware names
 to create a tree that matches the LO connections in the system.

#### Clear and Refresh Hardware

Use Clear and Refresh Hardware button to clear the LO
 Connection configuration tree and populate all the NI RF Vector Signal Generators,
 NI RF Vector Signal Analyzers, and External LO Devices (PXIe 5653) present in the
 system, along with their respective model, chassis, and slot numbers. If
 Use Default from WLAN Calibration Utility check box is
 selected, you cannot clear and refresh the hardware.

Note

The following figures illustrate different connection configuration topologies and
 how it is depicted in the LO Connection Configuration
 window.

2x2 MIMO System with External LO shared between SAs and SGs.

[IMAGE alt='image' src='GUID-C4847085-C84C-4146-8F61-67CA340D64E9-a5.png']

[IMAGE alt='image' src='GUID-5B86E96D-0309-416F-9DE6-4289CE45FA69-a5.png']

[IMAGE alt='image' src='GUID-5E50AE06-7B6E-4437-A93A-EB7E9E491053-a5.png']

4x4 MIMO/Multi Segment System with two External LOs shared between SGs.
 The SG LOs are exported to SAs.

[IMAGE alt='image' src='GUID-310D8DA5-9FC5-470A-A1F3-D46D1589DDE3-a5.png']

[IMAGE alt='image' src='GUID-DCEFE96E-0EA0-4A9C-BF6F-614E244AA2D6-a5.png']

[IMAGE alt='image' src='GUID-6A85D2F8-0B7F-4D7F-91A2-FAECBB0B5A96-a5.png']

2x2 MIMO System with External LO daisy chained across SGs.

[IMAGE alt='image' src='GUID-1DACBF11-444C-4730-AA13-F2C3A8396900-a5.png']

[IMAGE alt='image' src='GUID-4AF4A44A-29EF-4409-A4A4-3E5B881663EB-a5.png']

[IMAGE alt='image' src='GUID-7C87A26C-3EA3-46F5-A8E1-DAA16DBBE864-a5.png']

VST1 generator is the Master generator in the preceding figure.

Parent topic:

WLAN

<!--NI_TOPIC bundle=rfmx-waveform-creator path=configuring-multicarrier.html language=enus -->
## TOPIC 00023: Configuring Multi-Carrier Modulation

- bundle_id: `rfmx-waveform-creator`
- source_path: `configuring-multicarrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/configuring-multicarrier.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: WCDMA, LTE, NR, and EV-DO modulation schemes allow you to define several carriers and combine them in arbitrary sets. This is achieved using Carrier Definitions and Carrier Sets. Carrier Definition and Carrier SetsA carrier definition is a set of parameters for the chosen modulation scheme. All thes

### Configuring Multi-Carrier Modulation

WCDMA, LTE, NR, and EV-DO modulation schemes allow you to define several carriers and
 combine them in arbitrary sets. This is achieved using Carrier Definitions and Carrier
 Sets.

#### Carrier Definition and Carrier Sets

A
 carrier definition is a set of parameters for the chosen modulation scheme. All
 these parameters are present in the Modulation tab. The
 modulation parameters of a carrier definition and the filter settings together
 completely specify the baseband signal expected from this carrier definition. The
 spectrum of such a baseband signal is a traditional single-carrier case. When
 RF-modulated, this baseband signal will be exactly centered around the carrier
 frequency.

In the multi-carrier case, there can be several sets of parameters
 that specify respective carrier definitions.

Note

Filter

To configure the
 modulation parameters for a carrier definition, perform the following steps:

1. From the Modulation tab, select a scheme. The
 New Settings File tab is prompted.
2. In the New Settings File tab, click
 OK . The selected modulation scheme window is
 prompted.
3. Under the Modulation tab, in the Carrier
 Definitions panel set the Maximum Number of Carrier
 Definitions for a link and to copy parameter values from one
 carrier definition to another. Note The copy from Carrier
 Definition tab is enabled only when value of the
 Maximum Number of Carrier Definitions is more
 than 1.

[IMAGE alt='image' src='GUID-726C6ABC-34ED-431C-8C84-7B215C5587F3-a5.png']

The parameters to configure carrier definitions are as
 follows.

Maximum Number of Carrier Definitions: The
 maximum number of carrier definitions that can be defined.

Carrier
 Definition Number: Sets the current carrier definition number of the
 definition that you want to configure.

Carrier Definition
 Name: Enables you to provide a name to the carrier definition. It
 will reflect in the choice of carrier definition to copy from.

Copy
 from Carrier Definition: Allows you to select the carrier definition
 number that you want to copy to the current one.

Note

Copy to New

#### Generating a Multi-Carrier Signal

To
 generate a multi-carrier signal, you must also configure how the baseband signals of
 various carrier definitions must be combined.

A carrier set is set of carrier
 definitions whose signals are to be combined into one baseband signal that can be
 played from a single instrument. Thus, CFR, IQ impairments and the Graphical display
 of the output apply to each carrier set.

LTE and NR multi-carrier
 configuration is slightly different from EV-DO and WCDMA. For more information on
 LTE Multi-Carrier configuration, refer to the LTE Multi-Carrier and NR Multi-Carrier
 sections of RFmx Waveform Creator Modulation Schemes. Details for
 Multi-Carrier configuration of EV-DO and WCDMA can be found in this
 topic.

Every modulation scheme that integrates multicarrier operation will
 show a Multi-Carrier tab. By default, this tab will have
 carrier set 0 with carrier definition 0 mapped to it. All other parameters
 (frequency offset, gain, phase, and delay) default to 0 as shown in the following
 image.

[IMAGE alt='image' src='GUID-D53DEFCB-9CA1-436E-AAAF-567BAF92F2CC-a5.png']

The parameters to configure each carrier set, shown in
 the lower section of the preceding figure are given
 below.

Randomize Delay Button: Randomizes the time
 delay of all carriers currently in random delay mode.

Reset Delay
 Button: Resets the random number generators used to randomize the
 time delay of each carrier in random mode. After clicking this button, the time
 delay of these files will return to the first random delay value
 generated.

Reset Delay Button: Resets the random
 number generators used to randomize the time delay of each carrier in random mode.
 After clicking this button, the time delay of these files will return to the first
 random delay value generated.

Randomize Phase Button:
 Randomizes the phase of all carriers currently in random phase
 mode.

Reset Phase Button: Resets the random number
 generators used to randomize the phases of each carrier currently in random mode.
 After clicking this button, the phase of these carriers returns to the first random
 phase value generated.

Oversampling Factor: Sets the
 oversampling factor. This allows you to increase the default sample rate, which is
 calculated internally. The default is 1. To manually change the oversampling factor,
 uncheck the Auto checkbox.

Carrier Set
 Name: You can use this field to provide a name to the carrier
 set.

Carrier Set Number: Implies the carrier set index
 to which the sampling rate and oversampling factor is applied.

Note

By clicking Add in this tab, the dialog box as
 shown in the following image appears.

[IMAGE alt='image' src='GUID-393325DA-5D6B-4DE9-8B56-954B5ADC2A44-a5.png']

The parameters in the Add Carrier
 dialog box are described in the following sections.

Carrier
 Definition: Implies the definition index. Carrier definition goes
 from 0 to N-1 where, N is the maximum number
 of carrier definitions chosen by you in the Modulation
 tab.

Carrier Set: Depicts which set the carrier number
 belongs to. For M > 0, you are not allowed to choose carrier
 set M without also choosing at least one carrier in carrier set
 (M-1).

Frequency Offset:
 Represents the frequency offset from carrier by which the signal shifts when mixed.
 The value can be from -100 MHz to +100 MHz, including 0 Hz.

Phase
 Continuous: Instructs to calculate the closest cyclic frequency
 offset to the value in the Frequency Offset control and
 update the control with the new value. This value will be recalculated each time any
 carrier is added, modified or removed.

Gain: This is
 the power level of the current carrier relative to the other carriers you have added
 or will add later. The value can be from -60 dB to 0
 dB.

Delay: Allows you to start the mixing at any
 point in the carrier and means you can emulate similar signals with different time
 references.

Random (checkbox next to Delay): In this
 field, mode automatically generates a time delay. Selecting this checkbox for each
 carrier in the table will result in a waveform with a lower crest
 factor.

Carrier Phase: Allows you to adjust the
 starting phase of the frequency mixer.

Random (checkbox next to
 Carrier Phase): Selecting this checkbox puts the file into random
 phase mode. In this mode, will automatically generate a random phase between -180
 and +180 degrees. Selecting this checkbox for each carrier in the table will result
 in a waveform with a lower crest factor.

#### Example

You can specify five different
 configurations in five carrier definitions for each of the carriers in the general
 case, but this can be repetitive because more than one carrier can have the same
 configuration. In such cases, it is sufficient to specify only the required number
 of unique carrier definitions and map them to carriers in the respective carrier
 sets. For example, carrier definition 0 is used twice in the first band and carrier
 definition 1 is used in both bands. Illustration of carrier definitions and their
 mapping to carriers in carrier sets is shown in the following figure.

[IMAGE alt='image' src='GUID-E046DD58-1320-48EA-90A7-A0D74E41CF70-a5.png']

Configuration used in the
 Multi-Carrier tab are as shown in the following
 image.

[IMAGE alt='image' src='GUID-57B37EB3-16D3-42AC-A775-35E4AE85D6D3-a5.png']

To save the outputs of all carrier definitions when there
 are more than one defined, you must configure as many carrier sets and have a
 one-to-one mapping between them and set all other multi-carrier parameters as zero.
 The center frequency of a carrier set need not correspond to that of any carrier
 within it. For example, carrier 0 at 1900 MHz and carrier 1 at 1902.5 MHz can be
 combined in one carrier set at center frequency 1901.25 MHz with carrier 0 and
 carrier 1 having frequency offsets -1.25 MHz and +1.25 MHz respectively.

Note

- IQ Impairments , CFR and
 Graphics tabs are applicable per carrier set. For
 more information, refer to the IQ Impairments, Crest Factor Reduction, and
 Plotting Graphs sections respectively.
- When you have entered a frequency offset which is not cyclic, a warning
 symbol will appear next to the frequency in the table to notify you of
 this.
- All carrier definitions must have the same duration in number of
 frames.

<!--NI_TOPIC bundle=rfmx-waveform-creator path=coreset-configuration-overview.html language=enus -->
## TOPIC 00024: CORESET Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `coreset-configuration-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/coreset-configuration-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains the following configuration parameters specific to the CORESET portion of the Downlink Signal. Symbol Offset: Configures the starting symbol of the CORESET allocation with a slot. Valid values are 0 to (14 - Number of Symbols). Number of Symbols: Configures the duration of the

### CORESET Configuration

This section contains the following configuration parameters specific to the CORESET
 portion of the Downlink Signal.

Symbol Offset: Configures the starting symbol of the CORESET
 allocation with a slot. Valid values are 0 to (14 - Number of Symbols).

Number of Symbols: Configures the duration of the CORESET
 allocation within a slot. Valid values are 1, 2, and 3.

RB Allocation: Configures the resource blocks (RBs) within the
 bandwidth part (BWP), which are a part of the CORESET allocation within a slot. The
 format is defined in the Range Format Specifiers section.

DMRS Scrambling ID Mode: If you set this parameter to
 User Defined, the DMRS scrambling sequence generator will be
 initialized with the value specified in the DMRS Scrambling ID
 field.

If you set this parameter to Cell ID, the DMRS scrambling sequence
 generator will be initialized with the value specified in the Cell
 ID field in the Carrier Definition section.

DMRS Scrambling ID: Initializes the DMRS scrambling sequence
 generator. Valid values range from 0 to 65535, inclusive. This value is only used if the
 DMRS Scrambling ID Mode is set to User
 Defined.

Precoder Granularity: If you set this parameter to Same
 As REG Bundle, the DMRS symbols are only allocated on RBs that contain
 PDCCH data.

If you set this parameter to All Contiguous RBs, the DMRS symbols
 are allocated on all RBs allocated to the CORESET.

CCE REG Mapping Type: If you set this parameter to
 Non-Interleaved, the RBs are allocated by PDCCH using
 non-interleaved CCE-to-REG mapping.

If you set this parameter to Interleaved, the RBs are allocated by
 PDCCH using interleaved CCE-to-REG mapping.

REG Bundle Size: Sets the REG bundle size in interleaved
 CCE-to-REG mapping. Valid values are 2, 3, and 6.

Interleaver Size: Sets the interleaver size in interleaved
 CCE-to-REG mapping. Valid values are 2, 3, and 6.

Shift Index: Sets the shiftIndex in interleaved CCE-to-REG
 mapping. Valid values are 0 to 274, inclusive.

Number of PDCCH Configurations: Specifies the actual PDCCH
 configuration that is visible in the user interface.

Parent topic:

NR

Related concepts:

- Range Format Specifiers
- Carrier Definition

<!--NI_TOPIC bundle=rfmx-waveform-creator path=coreset-setup.html language=enus -->
## TOPIC 00025: CORESET Setup

- bundle_id: `rfmx-waveform-creator`
- source_path: `coreset-setup.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/coreset-setup.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains the following configuration controls. Number of CORESET Configurations: Specifies the actual CORESET configuration that is visible in the user interface.

### CORESET Setup

This section contains the following configuration controls.

Number of CORESET Configurations: Specifies the actual CORESET
 configuration that is visible in the user interface.

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-a-3gpp-fdd-waveform-overview.html language=enus -->
## TOPIC 00026: Creating a 3GPP FDD Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-a-3gpp-fdd-waveform-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-a-3gpp-fdd-waveform-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a 3GPP FDD waveform, complete the following steps: Select the Modulation drop-down menu. Select WCDMA to display the generation settings window. Select either the New Default Settings or the Example Settings from the generation settings window. This opens the WCDMA window, which has tabs f

### Creating a 3GPP FDD Waveform

To create a 3GPP FDD waveform, complete the following steps:

1. Select the Modulation drop-down menu.
2. Select WCDMA to display the generation settings window.
3. Select either the New Default Settings or the
 Example Settings from the generation settings window.
 This opens the WCDMA window, which has tabs for Modulation,
 Multi-Carrier, Filter, IQ Impairments, and Graphics settings. These tabs provide the
 same functionality as other modulations.

Parent topic:

WCDMA (3GPP FDD Release 8)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-a-cdma2k-waveform.html language=enus -->
## TOPIC 00027: Creating a CDMA2k Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-a-cdma2k-waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-a-cdma2k-waveform.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a new CDMA2k waveform, Select the Modulation menu. Click CDMA2k. The New Settings File window appears. Click OK in the New Settings File window. The CDMA2k settings window appears. Note: If CDMA2k does not appear in the Modulation menu, use the Tools menu to add Registered Plugins niCdma20

### Creating a CDMA2k Waveform

To create a new CDMA2k waveform,

1. Select the Modulation menu.
2. Click CDMA2k . The New Settings File
 window appears.
3. Click OK in the New Settings File window. The
 CDMA2k settings window appears.

Note: If CDMA2k does not appear in the
 Modulation menu, use the Tools menu to
 add Registered Plugins niCdma2000GenPlugin.dll.

If example settings are available, you are offered a choice to create a New
 Default Settings and select an Example
 Settings.

[IMAGE alt='image' src='GUID-5C0AB180-AEF5-4C8C-A29B-6D6BCDEFACEF-a5.gif']

Fig. 4-12 CDMA2k settings
 window

This window has tabs for Modulation,
 Filter, IQ Impairments, and
 Graphics settings. These tabs are the same as those found in
 other modulations.

Setting the Modulation Parameters

This section describes the general settings available for CDMA2k and how you can modify
 them. The above figure shows the default settings that appear when you open a
 CDMA2k settings window. The spreading rate is direct mode.
 The chip rate is set to 1.2288 MHz when the spreading rate is x1 and 3.6864 MHz when the
 spreading rate is x3. The following parameters can be set:

Link Direction

Select the link direction you require using the Link Direction
 drop-down menu.

Spreading Rate

Select the required spreading rate using the Spreading Rate
 drop-down menu. You have the choice of x1 or x3. This selection affects the type and
 number of radio configurations that are available.

Number of Frames

You can select a value in the Number of Frames combo-box to change
 the number of frames that you want to generate. The length of the resulting waveform is
 shown in brackets.

Oversampling Factor

The default value is 4. If you want to enter a different value, unselect the
 Auto checkbox.

Radio Configuration

There is a total of nine radio configurations available.

When the Link Direction is set to
 Up/Reverse, radio configurations 1 to 4 are allowed if the
 spreading rate is x1, and radio configurations 5 to 6 are allowed with a spreading rate
 of x3.

When the Link Direction is set to
 Down/Forward, radio configurations 1 to 5 are allowed if the
 spreading rate is x1, and radio configurations 6 to 9 are allowed with a spreading rate
 of x3.

When you select a radio configuration, the types of channel available to you are
 presented in the Channel table.

Creating a Reverse Link

Once you have set the general parameters, you can define the reverse channel(s) for your
 configuration.

Radio Configurations 1 and 2 (RC1 and RC2)

If you have selected either radio configuration 1 or 2 you are only able to define either
 an Access or Traffic channel. Select the type of channel using the Select Channel combo
 box. If you select the Access channel you are presented with the settings shown in the
 following figure.

[IMAGE alt='image' src='GUID-677229FD-ED6F-4D5E-BFBB-1CAD149411C1-a5.gif']

Fig. 4-13 Settings for RC1 Access
 Channel

If you selected a Traffic channel the settings are
 as shown in the following figure. The settings are the same for both RC1 and RC2. Note that
 because RFmx Waveform Creator does not currently support data encoding, the implementations
 of RC1 and RC2 are identical.

[IMAGE alt='image' src='GUID-0EADEC75-C956-4E3B-AB1E-80E15BA3DA3B-a5.gif']

Fig. 4-14 Settings for RC1 Traffic
 Channel

You are able to set the Long Code Mask, relative power level of the channel and the data
 source. The Long Code Mask is a hex number that defines 42 bits. The default value for
 the access channel is 31E00000000. (For the FCH channel it is 30000000000).

Channel Properties

You can modify the properties of the channel by clicking on any of the editable cells in
 the table. The channel type, and symbol rate properties are not editable, and are shown
 with a shaded gray background.

Power

This controls the level of the specific channel. The range is 0 to -60 dB. The default is
 0dB

Data Source

This controls the data payload of the channel. Refer to Selecting the Data Source topic
 for more information on data source.

State

This controls whether the channel will be transmitted or not.

Radio Configurations 3 and 4 (RC3 and RC4)

If you have selected either radio configuration 3 or 4 you are only able to define an
 Enhanced Access, Common Control or Traffic channel. Select the type of channel using the
 Select Channel combo box.

If you select an Enhanced Access channel, you are presented with the settings shown in
 Fig. 4-133.

[IMAGE alt='image' src='GUID-E8FD9448-5CD8-4F26-8171-2441CB938EE4-a5.gif']

Fig. 4-15 Enhanced Access Channel settings for
 RC3

The settings for the Common Control and Traffic channels are shown in the following
 figures. Once again, because RFmx Waveform Creator does not
 currently support data encoding, the implementations of RC3 and RC4 are identical.

[IMAGE alt='image' src='GUID-8D8E53A5-13AE-409A-AF7D-0D0D0EF71FE6-a5.gif']

Fig. 4-16 Common Control Channel settings for
 RC3

[IMAGE alt='image' src='GUID-CFD0D83C-EBEB-47B1-A958-D3E68F35B4C2-a5.gif']

Fig. 4-17 Traffic Channel settings for
 RC3

For each of the channel types you are able to set the long code mask used for scrambling
 the data as indicated in the block diagram. The value is entered in hex in the Long Code
 Mask edit box.

Configuring the Enhanced Access Channel

The enhanced access channel consists of a pilot channel (PICH) and the enhanced access
 channel (EACH). You are able to set the channel state, power level and data source as
 described previously for each of the channels. Note that the data source for the pilot
 channel is PRBS Again, you are able to edit a channel by double-clicking on the cell of
 interest.

You are able to change the data source and power level. The Walsh Code and symbol rate
 are fixed and are not editable, shown with a gray background. Again, the power level is
 limited to the range of 0 to –60 dB. The data source is configured as before.

Configuring the Common Control Channel

The common control channel consists of a pilot channel (PICH) and the common control
 channel (CCCH). You are able to set the channel state, power level and data source as
 described previously for each of the channels. Note that the data source for the pilot
 channel is fixed to zeros. As with the other described channels, you can edit any
 parameters of interest by clicking on the parameter you wish to modify.

Configuring the Traffic Channel

The traffic channel consists of a pilot channel (PICH), dedicated control channel (DCCH),
 fundamental channel (FCH), and supplemental channels 1 and 2 (SCH1 and SCH2). You are
 able to set the channel state, power level and data source as described previously for
 each of the channels. For the SCH1 and SCH2 channels you are also able to set the
 spreading factor, Walsh code and symbol rate. Again, the data source is fixed to zeros
 for the pilot channel. Editing a channel is the same as before. Select the parameter of
 interest and double-click.

In addition to the power and data source parameters, you are able to set the symbol rate
 and spreading factor. The Walsh code changes to 1 if you set a spreading factor of 2.
 The relationships between symbol rate, spreading factor and Walsh code are given in
 Appendix B. Note that SCH1 and SCH2 support different data rates and can have different
 Walsh codes.

Radio Configurations 5 and 6 (RC5 and RC6)

You are only able to select the radio configurations 5 and 6 if the spreading rate has
 been set to x3. You are able to define an Enhanced Access, Common Control or Traffic
 channel. Select the type of channel using the Select Channel combo box. Once again,
 because RFmx Waveform Creator does not currently support data
 encoding, the implementations of RC5 and RC6 are identical. The method of defining and
 editing the channels is the same as that described for RC3 and RC4. Again, refer to
 Appendix B to obtain the relationships between data rates, symbol rates, Walsh codes and
 spreading factor.

Generating a Waveform

Once you have set up the reverse channel and channel filter to suit your needs, you
 generate the waveform in the same way as for other modulation schemes. Select the Save
 Waveform File menu and proceed as described in the Getting Started Manual.

Creating a Forward Link

Once you have set the general parameters to your liking, you can define the forward
 channels for your configuration. Refer to the section ‘Setting the Modulation
 Parameters’, starting on page 1-12, on how to do this.

Radio Configurations 1 and 2 (RC1 and RC2)

Selecting either radio configuration 1 or 2 presents you with the link configuration set
 up shown in Fig. 4-136. The settings page is the same for both RC1 and RC2. From here,
 you are able to set the Pilot PN Offset and configure the forward channels. The Pilot PN
 Offset is used to set the offset of the scrambling codes. Typically, each base station
 is assigned its own offset. Valid values are 0 to 511.

The default table shows the Pilot (PICH) and Sync (SYNCH) channels. In general, you would
 want to turn these channels on. To do this, move your mouse over the State and required
 channel cell and double-click the left-hand button. Select On to turn the channel on.
 The spreading factor (SF), Walsh code and symbol rate are fixed for the PICH and SYNCH
 channels. You can set the relative power level for both channels and the data source
 type for the SYNCH channel. To set the power level, double-click the left-hand mouse
 button while the cursor is over the Power and selected channel cell. You can then enter
 a value between 0 and –60 dB. To select a data source, once again double-click the
 left-hand mouse button while the cursor is over the Data Source and selected channel
 cell. On doing this, you are presented with the standard data source dialog, from which
 you can select the data source required.

[IMAGE alt='image' src='GUID-5DE9F3F2-6E81-4432-B9D4-72CF3FC9C8AF-a5.gif']

Fig. 4-18 Settings for a RC1 forward
 link

You can use the table to directly edit any of the parameters, although in some situations
 not all parameters are editable. In such situations, the background color of the table
 will be shown as light gray.

Symbol Rate

This is the symbol rate used for the particular channel. This is not editable for PICH,
 SYNC, PCH, and QPCH. As traffic channels are split into sub channels, symbol rate is not
 applicable.

Spreading Factor

This is the spreading factor for the specified channel. This is derived from the symbol
 rate of the channel and is for display purposes only.

Walsh Code

This specifies the Walsh code of the given channel. The valid range is 0 to 63. For PICH
 and SYNC channels, this value not editable. The default value is 0.

Data Source

This defines the data payload of the specific channel. This can either be All zeros, All
 ones, PRBS, Random, Repeating Pattern, or User defined. The default is a PN 9 sequence
 for editable Channels.

For PICH channels, the data source is fixed to All Zero’s.

Power

This changes the relative power of the channel within the signal. The allowed range is
 -60dB to 0dB. The default value is 0dB.

State

This changes whether the channel is transmitted. All default channels are turned off.

To edit any of the parameters; you can click on any of the items within the table.

For traffic channels, you may select the specific channel by pressing the left-hand mouse
 button when the cursor is on the required channel row. On doing so, the
 Edit… button at the bottom of the screen will be enabled
 appropriately. To edit the specific channel, press the Edit…
 button which will present the dialog shown in the following figure. This dialog will
 allow you to modify all the properties described above for the component channels within
 the traffic channel.

[IMAGE alt='image' src='GUID-995C5517-DD82-42B1-BE7E-EC5828BDFC54-a5.gif']

Fig. 4-19 Editing a traffic
 channel

You can add more channels by pressing the Add… button. On doing so, you are presented
 with the dialog box shown in the following figure. From here, you can add all the
 channels supported in RC1 and 2 as indicated in Table 4-39. Remove channels by selecting
 the channel in the table and pressing the Remove… button.

[IMAGE alt='image' src='GUID-ABB59D0C-4550-4FB3-92EE-4B705FCF6984-a5.gif']

Fig. 4-20 Add channel dialog

The default Add Channel dialog shows the settings for adding a traffic channel. For radio
 configurations 1 and 2, a traffic channel can consist of one fundamental channel and up
 to seven supplemental channels. In all cases, the spreading factor is fixed at 64. The
 Channel State combo box selects the state of the traffic channel. This lets you turn off
 a traffic channel without having to turn off channels within the traffic channel.

You are able to set the channel state, Walsh code, power level and data source type for
 each of the allowed channels within a traffic channel. This can be done by selecting the
 channel of interest and double-clicking the left-hand mouse button when the cursor is
 over the parameter cell as described to set the channel state Seen in the following
 figure. You can set the Walsh code, power level and data source type. Note that you are
 unable to define long code masks. RFmx Waveform Creator currently does not support this
 in the forward link.

[IMAGE alt='image' src='GUID-14352360-1A6E-4DBA-BA70-ECFC1AE1D82B-a5.gif']

Fig. 4-21 Edit dialog for traffic
 channels

The Walsh code for a channel is entered into the Walsh Code edit box. Allowed values are
 0 to 63. Note that if you choose a code that is either already in use or that is not
 orthogonal to another that is in use, the channels that are in conflict with each other
 will be highlighted in red, as indicated in the following figure. This warning appears
 only when the channel has been turned on.

[IMAGE alt='image' src='GUID-F250F338-69E2-4F43-BA5B-9288401D5B4A-a5.gif']

Fig. 4-22 Walsh code
 conflict

If you wish to add channels other than a traffic channel click on the combo box Select
 Channel Type. The available channels are: BCCH, CACH, CCCH, PCH, and QPCH. Add channel
 dialog. The parameters and how to change them are again straightforward. With these
 channels, you are able to change the symbol rate. For the PCH and QPCH channels the
 symbol rate is fixed and it cannot be changed.

In all cases, RFmx Waveform Creator limits the number of channels that you can add. The
 number of available Walsh codes limits the number of traffic channels.

Radio Configurations 3, 4, and 5 (RC3, RC4, and RC5)

Selecting one of radio configuration 3, 4, or 5 presents you with the link configuration
 setup shown in the following figure. The settings page is the same for all three radio
 configurations. From here, you are able to set the Pilot PN Offset, the Quasi-Orthogonal
 set, and configure the forward channels. Again, the Pilot PN Offset is used to set the
 offset of the scrambling codes. Typically, each base station is assigned its own offset.
 Valid values are 0 to 511. The Quasi-Orthogonal set defines the Walsh Rotation bits and
 QOF values that are used to modify the Walsh code. Valid values are 0 to 3.

The default channel table shows the Pilot (PICH) and Sync (SYNCH) channels. In general,
 you would want to turn these on. The channel state and other parameters that can be
 changed within the table are altered as described earlier.

[IMAGE alt='image' src='GUID-6B4C29BF-25AC-48C8-8BA9-BE464AA30547-a5.gif']

Fig. 4-23 Forward link configuration for RC3, RC4 and
 RC5

To add a channel press the Add… button beneath the table. On doing
 so, you are presented with the dialog shown in the following figure. The default channel
 is again the traffic channel. For RC3, RC4, and RC5 the traffic channel consists of up
 to two SCHs, a DCCH and a FCH. You can edit and alter parameters as for RC1 and RC2.

[IMAGE alt='image' src='GUID-01C0556B-954E-4B42-A52D-7736CC5FE477-a5.gif']

Fig. 4-24 Add channel dialog for RC3, RC4 and
 RC5

If you would like to add another type of channel, click the Select Channel
 Type combo-box. Again you are allowed to choose one of the following
 channels: BCCH, CACH, CCCH, PCH, and QPCH. You set these channels up in the same way as
 for RC1 and RC2. Walsh code conflicts. As for RC1 and RC2, RFmx Waveform Creator limits
 the number of channels that you can add. The number of available Walsh codes limits the
 number of traffic channels.

Generating a Waveform

Once you have set up the forward channel, select the filter tab to set the channel
 filter. For the forward link you would generally select either the CDMA2k. If you are
 happy with your choices, select the Save Waveform File menu and
 proceed as described in the Getting Started Manual.

Parent topic:

CDMA2k (3GPP2)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-a-ev-do-revision-0-waveform.html language=enus -->
## TOPIC 00028: Creating a EV-DO Revision 0 Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-a-ev-do-revision-0-waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-a-ev-do-revision-0-waveform.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a new EV-DO Rev 0 waveform, Select the Modulation menu. Click EV-DO. The New Settings File window appears. Click OK in the New Settings File window. The EV-DO settings window appears. Note:If EVDO does not appear in the Modulation menu, use the Tools menu to add Registered Plugins Type ni1

### Creating a EV-DO Revision 0 Waveform

To create a new EV-DO Rev 0 waveform,

1. Select the Modulation menu.
2. Click EV-DO . The New Settings File
 window appears.
3. Click OK in the New Settings File 
 window. The EV-DO settings window appears.

Note:If EVDO does not appear in the Modulation menu, use the Tools
 menu to add Registered Plugins Type ni1xEvdoGenPlugin.dll.

If example settings are available, you are offered a choice to create a New
 Default Settings or select an Example
 Settings.

[IMAGE alt='image' src='GUID-3453E62C-F1DA-4542-925E-0A1B912F4E84-a5.gif']

Fig. 5-5 EV-DO Revision 0 initial settings

Setting the Modulation Parameters

This section describes the general settings available for EV-DO and how you can modify
 them. The above figure shows the default settings that appear when you open a EV-DO
 modulation tab. The following parameters can be set:

Link Direction

Select the link direction you require using the Link Direction
 combo-box.

Number of Frames

Edit this box to change the number of frames to generate. One frame is 26.67 ms (32768
 chips) long, which in turn is equivalent to 16 slots. The number of frames is not
 editable when the Link Direction is set to
 Forward because the Forward Traffic/Control Channel
 configuration automatically sets the required number of frames.

Oversampling Factor

To over sample by a different amount to the default value of 4, disable auto mode by
 selecting the Auto checkbox and enter an oversampling factor.

Creating a Reverse Link

After setting the general parameters, you can configure the reverse channel(s). The
 default channel is the Traffic Channel.

Configuring the Access Channel

You can set the following parameters:

- Long Code Masks 
 The I and Q long-code masks are used to scramble the data. You can define the two
 codes independently. The values are entered in hex. The valid range is 0 to
 3FFFFFFFFFF. The default is 0 h.
- Number of Access Frames 
 This sets the number of access frames following the preamble, in frames, that are
 generated. The range of allowed values is 0 to 10. A value of 0 allows you to
 transmit only preamble frames. The default is 1.
- Data Power 
 This sets the data gain relative to the pilot. The value is in dB with a range of
 ?60 to 60 dB. The default is 0 dB.
- Data Source 
 This shows the type of data used by the Data Channel. The default is a PN9
 sequence. Refer to Selecting the Data Source topic for more information on data
 source.
- Number of Preambles 
 This sets the number of preambles (in frames) that are generated. The range of
 values is 1 to 10. The default is 4.

Configuring the Reverse Traffic Channel

If you wish to generate a Reverse Traffic Channel, select Traffic
 in the Select Physical Channel box. On doing so, you are
 presented with the settings shown in the following figure.

[IMAGE alt='image' src='GUID-9E8F6217-FA7D-45C5-B6B9-DADE437EF6E1-a5.gif']

Fig. 5-6 EV-DO Reverse Traffic Channel settings

RFmx Waveform Creator provides you with the facility to set the following parameters:

Long Code Masks

The I and Q long code masks are channel-independent. Their values are set in the same way
 as for the Reverse Access Channel.

Pilot and RRI Channel

The only parameter that you can set for the Pilot/RRI Channel is the channel state (On or
 Off). If the state is off, the Pilot / RRI Channel is not transmitted. The default is
 On.

Data Channel

The parameters associated with this channel are set in the Data Channel frame.

- Channel State 
 The Data Channel can be turned on or off by selecting the appropriate value in
 the Channel State check box. If the channel is unchecked, the Data Channel is
 not transmitted. The default is Off (unchecked).
- Power 
 This is the gain of the Data Channel with respect to the Pilot Channel. The value
 is in dB and has a valid range of -60 to 60 dB. The default is 0 dB.
- Data Rate 
 There are six data rates available for the Traffic Channel: 0, 9.6, 19.2, 38.4,
 76.8 and 153.6 kbps. The data rate is set using the Data Rate box. The default
 is 9.6 kbps.
- Number of Packets 
 The number of packets to transmit. The valid range of values is 1 to 100. Note
 that if you select a value that is larger than the number of frames set in the
 Number of Frames edit box, the latter takes priority. The default is 1.
- Frame Offset 
 You can offset the starting slot of the Traffic Channel transmission. This is
 done in the Frame Offset box. The valid range of values is 0 to 3. The default
 is 0.
- Data Source 
 This shows the type of data used by the Data Channel. Allowed data types are All
 Zeroes, All Ones, PRBS, User Data, and Repeating Pattern. You can configure the
 data source being used by clicking on the Data Source
 button, The default is a PN9 sequence.

DRC Channel

You can set several parameters associated with this channel. The parameters associated
 with the channel are contained within the frame DRC Channel.

- Channel State 
 The DRC Channel can be turned on or off by selecting the Channel
 State checkbox. If the Channel is
 unchecked, the DRC Channel is not transmitted. The default is
 Off.
- Power 
 This is the gain of the DRC Channel with respect to the Pilot Channel. The value
 is in dB and has a valid range of -60 to 60 dB. The default is 0 dB.
- Gating 
 Request gated DRC transmissions by selecting the Gating check box. In this case,
 only one slot of DRC is transmitted over DRC length slots. The default is not to
 use gating.
- Start Slot 
 The start slot defines the slot (there are 16 slots per frame) in which the DRC
 transmission is to start. The valid range is 0 to 7. The value is set in the
 Start Slot box. Note that DRC transmissions are offset by half a slot, so if you
 set the start slot to 0, the DRC transmission starts half way through slot 0.
 This is in accordance with the standard. The default is 0.
- Length 
 This is the length of the DRC transmission in slots. Valid range is 1 to 8. Set
 this in the Length box. The default is 1.
- DRC Value 
 The DRC value is used to request the Forward Traffic Channel data rate. The
 allowed DRC values lie between 0 and 15. The value is selected using the
 DRC Value box. The following table associates the DRC
 value with the requested data rate and packet length. 
 
 

 Table 5-2 DRC value specification 
 

 RFmx Waveform Creator lets you set DRC values 13, 14, and 15. The standard
 provides symbol values for these DRC values even though the higher-level
 protocol currently does not support them. The default is 00 h.
- DRC Cover 
 The cover value defines the selected serving sector. Valid values range from 0 to
 7. This value is set in the Cover box. The default is 0.

ACK Channel

You can configure the ACK Channel. The parameters for this channel are set in the ACK
 Channel frame.

- Channel State 
 You can turn the ACK Channel on or off by selecting or clearing the Channel State
 checkbox. If this control is unchecked, the ACK Channel is not transmitted. The
 default is Off (unchecked).
- Power 
 This is the gain of the ACK Channel with respect to the Pilot Channel. The value
 is in dB and has a valid range of -60 to 60 dB. The default is 0 dB.
- Start Slot 
 The start slot defines the slot (there are 16 slots per frame) in which the ACK
 transmission is to start. The valid range is 0 to 7. The value is set in the
 Start Slot box. The default is 0.
- ACK/NACK Gap 
 This is the spacing between ACK and/or NACK bits. The valid range is 1 to 8. The
 value is set in the ACK/NACK Gap box. The default is 0.
- ACK/NACK Pattern 
 You can select the pattern of acknowledge bits that are sent. A ‘0’ refers to an
 acknowledge (ACK) and a ‘1’ to a not acknowledge (NACK). The pattern can be set
 using the ACK(0)/NACK(1) Pattern box. A maximum of 16 bits can be entered. The
 default pattern is 01.

ACK Channel

Once you have set up the reverse channel(s) and the channel filter to suit your needs,
 you can generate the waveform in the same way as for other modulation schemes. Select
 the Save Waveform File Menu and proceed as described in the RFmx Waveform
 Creator Help document.

Creating a Forward Link

Once you have set the general parameters, you can configure the forward channels. RFmx
 Waveform Creator provides you with the facility to set parameters for each of these
 channels using the controls shown in the following figure.

[IMAGE alt='image' src='GUID-3EB3647F-9A8E-4F4A-8E1B-504CBADBAC37-a5.gif']

Fig. 5-7 EV-DO Forward Link settings

For EVDO Rev 0, set the Physical Layer Subtype to 0.

- Pilot Channel State 
 The Pilot Channel can be turned on or off by selecting or clearing the check box
 in the Pilot Channel tab. If this control is unchecked, the Pilot Channel is not
 transmitted. The default is On (checked).
- Pilot PN Offset 
 The Pilot PN Offset is used to set the offset of the scrambling codes. Typically,
 each base station is assigned its own offset. The valid range of values is 0 to
 511. The default is 0.
- Idle Noise Power 
 The Idle Noise Power can be turned on or off by clicking on the check box. If it
 is turned on, AWGN is added to the idle periods within the generated signal at
 the specified level. This level is relative to the maximum power in the signal
 (nominally the pilot channel). The default is off (unchecked).

Configuring the Traffic/Control Channel

You can configure the Forward Traffic/Control Channel via a table. You can add, edit, and
 remove a user to/from a table using the buttons underneath.

To access the traffic/control channel, select the traffic/control tab. This shows the
 table as given in Fig 1.8.

A user is an access terminal and the Forward Traffic/Control Channel can transmit one or
 more physical layer packets to up to 16 different users. The physical layer packets
 transmitted to a user are all at the same data rate and transmitted serially. Only
 physical layer packets from other users can be interleaved into the inactive slots.

A graphical representation of a frame is given to illustrate which slots are occupied and
 which slots are available. If a slot is occupied, it is color-coded according to the
 user and the modulation is given. The buttons either side of the frame graphic allows
 scrolling between frames. Clicking a row within the table will automatically select and
 highlight the relevant item within the graphic.

To add a new user to the table, click the Add… button. On doing,
 so a new user is added in the table. Configure as required by double-clicking on the
 particular parameter that you wish to change.

[IMAGE alt='image' src='GUID-A36292FF-0BE7-4143-ADDB-D401DB55CD6B-a5.gif']

Fig. 5-8 Adding a Forward Traffic/Control Channel

- MAC Index 
 The MAC Index determines the 32-ary Walsh code used to spread the preamble
 symbols. The valid range of values is 0 to 63. The default is 0.
- Data Rate 
 The available data rates are defined in Table 5-40 and one can be selected from
 this list using the Data Rate box. The default is 38.4 kbps.
- Number of Slots per Packet 
 The number of slots required to transmit one packet. Depending upon the selected
 data rate, this parameter is for information purposes only or it is set using
 the Number of Slots box.
- Number of Packets 
 The number of packets that you wish to transmit to the access terminal (user).
 The valid range of values is 1 to 100. Note that if the current number of frames
 is insufficient to transmit the selected number of packets, the number of frames
 is automatically increased. The default is 1.
- Frame Offset 
 The frame offset defines the first slot a packet is transmitted in relative to
 slot 0 of the first frame. The valid range of values is 0 to 1600. The default
 is 0.
- Data Source 
 This shows the type of data used by the Data Channel. Valid data types are All
 Zeroes, All Ones, PRBS, User Data and Repeating Pattern. You can configure the
 data source being used by clicking on the table entry, The default is a PN9
 sequence. 
 You can edit any of the parameters in the table, by double-clicking the left-hand
 mouse button on the cell. For example, double-clicking the left-hand mouse
 button on the data rate of the selected user causes a drop-down box to appear as
 shown in Fig. 5-151.
- Preamble State 
 The preamble can be turned on or off by selecting its value in the Preamble State
 box. If the preamble is not transmitted, IQ samples equal to zero are used. If
 the data is off and the preamble is on, only the preamble is transmitted. If a
 user is defined with multiple packets and only the preamble is on, the number of
 slots between the preambles is the same as when the data is transmitted. The
 default is On.
- Data State 
 The physical layer packet data can be turned on or off by selecting its value in
 the Data State box. If the data and preamble are turned off, the packets for
 this user are not transmitted. The default is On.

[IMAGE alt='image' src='GUID-2FABB71D-7B52-4B8D-9691-523715AA6AE1-a5.gif']

Fig. 5-9 Setting the user data rate

Configuring the MAC RA Channel

You can configure the MAC RA Channel using the MAC channel tab.

- MAC RA Channel State 
 The MAC RA Channel can be turned on or off by selecting or clearing the check
 box. If this control is checked, the channel will be transmitted, and the
 associated parameters will be enabled. The default is off (unchecked).
- Fig. 5-10 Configure MAC RA Channel tab
- Power 
 This is the gain of the MAC RA Channel with respect to the Pilot Channel. The
 value is in dB and has a valid range of -60 to 60 dB. The default is 0 dB.
- RAB Start Slot 
 This is the Reverse Activity Bit Offset and determines the offset in slots from
 the start of a frame when a new RA bit is transmitted. The valid range of values
 is 0 to 15. The default is 0.
- RAB Length 
 This is the Reverse Activity Bit Length and determines over how many successive
 slots the same bit is transmitted. The default is 8.
- Data Pattern 
 This is the data pattern transmitted on the MAC RA Channel and it can be up to 16
 bits long. The default pattern is 0.

Configuring the MAC RPC/DRCLock Channels

You can configure the MAC RPC and DRCLock channels in the MAC Channel frame.

- MAC RPC/DRCLock Channel State 
 This channel can be enabled by selecting the channel state check box. When this
 control is checked, the Configure button located to the right hand side will be
 enabled. The default MAC RPC/DRCLock state is off (unchecked). 
 Click on the Configure button to configure the Mac RPC/DRC Lock channels. On
 doing so, you are presented with the dialog box shown in the following figure.
 From here, you can configure the channels via a table. You can add, edit, and
 remove a RPC and DRCLock channel pair to/from the table using the buttons
 underneath. 
 
 

 Fig. 5-11 Configure MAC RPC/DRCLock Channels dialog 
 

 To add a new MAC RPC/DRCLock channel pair to the table, click the
 Add… button. On doing so, a new line is added shown
 in the following figure. From here, you can configure the parameters of both RPC
 and DRC Lock channels by clicking on the item in the table. 
 
 

 Fig. 5-12 Add MAC RPC/DRClock Channel dialog
- MAC Index 
 This is the MAC Index of both the MAC RPC and DRCLock channels. It determines
 which 64-ary Walsh code is used to spread both the RPC and DRCLock bit streams
 and whether the channel is transmitted on the I or Q branch. The valid range of
 values is 5 to 63. The default is 5. 
 Note that if you choose a MAC Index that is already in use the text for that row
 index, and the row index of the other conflict MAC channel(s) will turn red to
 warn you that the MAC Index is already in use, as indicated in the following
 figure. 
 
 

 Fig. 5-13 Forward MAC RPC/DRCLock Channel code conflict (1)
- Frame Offset 
 This determines when the DRCLock channel is transmitted with respect to the start
 of the frame and the DRCLockPeriod parameter. The valid range of values is 0 to
 15. The default is 0.

Configuring the RPC Channel

- RPC Power 
 This is the gain of the MAC RPC Channel with respect to the Pilot Channel. The
 value is in dB and has a valid range of -60 to 60 dB. The default is 0.
- RPC Data Pattern 
 This is the data pattern transmitted on the MAC RPC Channel and it can be up to
 16 bits long. The default is 0.
- RPC Channel State 
 The MAC RPC Channel is turned on or off by selecting the value in the Channel
 State box. If the channel is off, the MAC RPC Channel is not transmitted. The
 default is On.

Configuring the DRC Lock Channel

- DRC Length 
 This is the DRCLock Length parameter, which determines how many times a DRCLock
 bit is repeated. The default is 4.
- DRC Period 
 This is the DRCLock Period parameter, which determines the gap between each
 DRCLock Channel transmission. The default is 8.
- DRC Power 
 This is the gain of the MAC DRCLock Channel with respect to the Pilot Channel.
 The value is in dB and has a valid range of -60 to 60 dB. The default is 0
 dB.
- DRC Data Pattern 
 This is the data pattern transmitted on the MAC DRCLock Channel and it can be up
 to 16 bits long. The default is 0.
- DRC Channel State 
 The MAC DRCLock Channel is turned on or off by selecting the value in the Channel
 State box. If the channel is off, the MAC DRCLock Channel is not transmitted.
 The default is On. 
 To edit a MAC RPC/DRCLock Channel pair in the table, click the row in the table.
 This enables the Edit… button. Click the
 Edit… button to display the dialog box. 
 
 

 Fig- 5-14 Editing a MAC RPC.DRCLock Channel 
 

 You can edit any of the parameters directly in the parent table, by clicking the
 cell. For example, clicking the RPC Power cell lets you change the RPC Power as
 shown in the following figure. 
 
 

 Fig. 5-15 Setting the Forward MAC RPC/DRClock channel power 
 

 You can also change either channel’s state; move your mouse over the required
 State and Channel cell and double-click on the left-hand mouse button. On doing
 so, you are presented with a drop-down box as shown in the following figure. 
 
 

 Fig. 5-16 Setting the Forward MAC RPC/DRClock channel state
- 

Generating a Waveform

Once you have set up the forward channel and the channel filter, you can generate the
 waveform in the same way as for other modulation schemes. Select the Save
 Waveform File menu and proceed as described in the RFmx
 Waveform Creator Help document.

Parent topic:

EV-DO Revision 0

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-a-ev-do-revision-a-waveform.html language=enus -->
## TOPIC 00029: Creating a EV-DO Revision A Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-a-ev-do-revision-a-waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-a-ev-do-revision-a-waveform.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a new EV-DO Rev A waveform, Select the Modulation menu. Click EV-DO. The New Settings File window appears. Click OK in the New Settings File window. The EV-DO settings window appears. Note:If EVDO does not appear in the Modulation menu, use the Tools menu to add Registered Plugins Type ni1

### Creating a EV-DO Revision A Waveform

To create a new EV-DO Rev A waveform,

1. Select the Modulation menu.
2. Click EV-DO . The New Settings File
 window appears.
3. Click OK in the New Settings File 
 window. The EV-DO settings window appears.

Note:If EVDO does not appear in the Modulation menu, use the Tools
 menu to add Registered Plugins Type ni1xEvdoGenPlugin.dll.

If example settings are available, you are offered a choice to create a New
 Default Settings or select an Example
 Settings.

[IMAGE alt='image' src='GUID-E3A0A12A-7F5F-433D-81AB-3C59261FF282-a5.gif']

Fig. 5-24 EV-DO Rev A initial settings

This window has tabs for Modulation,
 Filter, IQ Impairments, and Graphics settings. These tabs are the same as those found in
 other modulations.

Setting the Modulation Parameters

This section describes settings available for EV-DO Rev A and how you can modify them.
 The above figure shows the default settings that appear when you open a EV-DO Rev A
 modulation tab. The following parameters can be set:

Link Direction

Select the link direction from the drop-down menu.

Number of Frames

Edit this box to change the number of frames that you want to generate. One frame is
 26.67 ms (32768 chips) long, which in turn is equivalent to 16 slots. The default is
 1.

Oversampling Factor

To oversample by a different amount to the default value of 4, disable auto mode by
 clearing the Auto checkbox, then enter the oversampling factor of
 your choice.

Physical Layer Subtype

This combo-box lets you choose the physical layer subtype you want to use. The default
 value is 2.

Creating a Reverse Link

Configuring the Access Channel

After you have set the general parameters, you can configure the reverse channels. The
 default channel is the Access Channel. By default, physical layer subtype 0 is selected.
 If you select physical layer subtypes 1 or 2, the parameters that you can set change.
 The following figure shows the settings available when subtype 1 or 2 is selected.

[IMAGE alt='image' src='GUID-8872435F-D9E9-44DB-9A85-C1B3B9342B69-a5.gif']

Fig. 5-25 EV-DO Rev A subtype 1 and 2 Access Channel settings

The following Access Channel parameters can be set:

Long Code Masks

The I and Q long-code masks are used to scramble the data. You can define the two codes
 independently. The values are entered in hex. The valid range is 0 to 3FFFFFFFFFF. The
 default value is 0 h.

Number of Access Frames

This sets the number of access frames that are generated following the preamble. The
 range of valid values is 0 to 10. A value of 0 allows you to transmit the preamble only.
 The default value is 1.

Data Power

This sets the data gain relative to the pilot. The value is in dB with a range of -60 to
 60 dB. The default value is 0 dB.

Data Source

This shows the type of data used by the Data Channel. The default value is a PN9
 sequence. Refer to Selecting the Data Source topic for more information on data
 source.

Number of Preamble Frames (subtype 0 only)

This sets the number of preamble frames that are generated. The range of valid values is
 1 to 10. This setting is only available when subtype 0 is selected. The default value is
 1.

Preamble Length (subtypes 1 and 2)

This lets you select the number of preamble slots that are generated. The default value
 is 16.

Data to Preamble Power (subtypes 1 and 2)

This lets you set the total signal power during the access frames relative to the power
 during the preamble. The value is in dB with a range of -20 to 20 dB. The default value
 is 0 dB.

Configuring the Traffic Channel

When subtype 0 or 1 is selected, the settings are the same as in EV-DO (Revision 0). To
 find out how to configure the traffic channel when subtype 0 or 1 is selected.

To generate a subtype 2 Reverse Traffic Channel, select Traffic in the Select Physical
 Channel box, then select subtype 2 in the Physical Layer Subtype
 box. This presents the settings shown in the following figure.

[IMAGE alt='image' src='GUID-9D61AFDC-A9B8-40D9-B588-48399AD5266B-a5.gif']

Fig. 5-26 EV-DO Rev A subtype 2 traffic settings

When subtype 2 is selected, RFmx Waveform Creator provides you with the facility to set
 the following parameters:

Long Code Masks

The I and Q long-code masks are used to scramble the data. You are able to define the two
 codes independently. The values are entered in hex. The valid range is 0 to 3FFFFFFFFFF.
 The default value is 0 h.

Pilot

To configure the Pilot channel, select the Pilot channel tab. The only setting that can
 be set on this tab is the Pilot Channel State (on or off). If the
 Pilot State checkbox is unselected, the Pilot Channel is not
 transmitted. The default is On (selected).

[IMAGE alt='image' src='GUID-93AB2B0D-0E73-4FA2-88E9-90CD8EA79E57-a5.gif']

Fig. 5-27 Pilot channel tab

Auxiliary Pilot channel

To configure the Auxiliary Pilot, select the Auxiliary Pilot
 Channel tab. This displays the screen shown in the following figure.

[IMAGE alt='image' src='GUID-C3DD6A95-BE86-4A98-B54B-5CC1BCCE1D3B-a5.gif']

Fig. 5-28 Auxiliary Pilot channel tab

Channel State

The Auxiliary Pilot Channel can be turned on or off by selecting or clearing the
 Channel State checkbox. If this control is unselected, the
 Auxiliary Pilot Channel is not transmitted. The default is On (selected).

Power

If the Auxiliary Pilot Channel is transmitted during the nth half slot, its power is
 specified relative to the maximum of the Data Channel gains during half-slots n-1 and
 n+1. The value is in dB and has a valid range of -60 to 60 dB. The default value is
 0.

Payload Threshold

The Auxiliary Pilot Channel is transmitted during the nth half slot if the transmitted
 payload (on the Data Channel) during half slots n-1 or n+1 is greater than or equal to
 the specified threshold, and the Channel State is set to On. The default is 0, the range
 is 0 to 12288.

Data Channel

To configure the Data, select the Data Channel tab. This will present the screen shown
 below in the following figure.

[IMAGE alt='image' src='GUID-A27DF047-5C83-4D16-934C-B02944F13F96-a5.gif']

Fig. 5-29 The Data channel tab.

Data/RRI Delay

The data /RRI delay edit box lets you delay the start of the first data frame (and
 therefore the start of the RRI channel) with respect to the beginning of the
 transmission. The delay is in slots and the range of valid values is from 0 to 15. The
 default value is 0.

You can configure the Data Channel via a table. Use the buttons to Add…,or Remove a
 channel.

A channel is a sequence of one or more packets that contain data from the same data
 source. In RFmx Waveform Creator, up to 16 separate channels can be configured. When
 transmitting packets on the data channel, the packets belonging to each channel are
 transmitted using 3 sub-frame interlacing. This means that packets from other channels
 can be transmitted on the intervening sub frames.

A graphical representation of a frame is given to illustrate which slots are occupied and
 which slots are available. If a slot is occupied, it is color-coded according to the
 channel, and the modulation is given. When any item in this table is selected, the
 corresponding packet within the graphic.

To add a new channel to the table, click the Add… button. This
 adds a new line as shown in the following figure. From here, you can configure a
 channel’s parameters.

[IMAGE alt='image' src='GUID-ABF86DD9-874F-4B27-A813-4B3F6B8FAA0D-a5.gif']

Fig. 5-30 EV-DO after a data channel has been added.

You can set the following parameters when adding a channel:

Channel State

The channel state checkbox sets the state for the channel. When this is set to off, the
 data channel is not transmitted during the slots occupied by the channel. The default
 value is on.

Frame Offset

The frame offset defines when the first slot in a packet is transmitted. The offset is
 relative to slot 0 of the first frame. The valid range of values is 0 to 1600. The frame
 offset must be a whole number of sub-frames (multiple of 4). If the value entered does
 not lie on a sub-frame boundary, the value is rounded down to the nearest whole
 sub-frame. The default value is 0.

Number of Packets

This specifies the number of packets to transmit. The valid range of values is 1 to 100.
 The default is 1.

Payload (Bits Per Packet)

The payload specifies the number of bits transmitted in a packet before encoding or
 repetition is applied. RFmx Waveform Creator does not implement encoding or repetition.
 This means that selecting payload only affects the data channel by changing the type of
 modulation that is used. The payload selected also determines the value transmitted on
 the RRI channel and determines if the auxiliary pilot should be transmitted. The default
 value is 128.

Number of Slots Per Packet

This combo box lets you set the number of slots per packet to 4, 8, 12, or 16 slots per
 packet. This corresponds to 1, 2, 3, or 4 sub-packets per packet. According to the
 specification, the data transmitted in a packet should be encoded or repeated so that it
 fills the required number of sub-packets. As RFmx Waveform Creator does not implement
 encoding or repetition, increasing the number of slots per sub-packet simply increases
 the amount of data produced to fill the required number of sub-packets. The default
 value is 8.

Data Source

This shows the type of data used by the Data Channel. Valid data types are All Zeroes,
 All Ones, PRBS, User Data, and Repeating Pattern. To configure the data source that is
 used, double-click the table cell. The default value is a PN9 sequence.

Power

This is the gain of the channel during slots occupied by the channel. The gain is
 relative to the Pilot Channel. The value is in dB and has a valid range of -60 to 60 dB.
 The default value is 0 dB.

Note: RFmx Waveform Creator only generates the number specified in
 the Number of Frames edit box. This means that data channel
 transmission is truncated if the channels occupy slots that do not lie within the frames
 generated.

You can edit any of the parameters directly in the table, by double-clicking the
 left-hand mouse button on the cell. For example, double-clicking the Payload column of
 the selected channel causes a drop-down menu to appear, as shown in the following
 figure.

[IMAGE alt='image' src='GUID-E9114C4F-77C8-443B-BC95-72E1C7C3F724-a5.gif']

Fig. 5-31 EV-DO editing the channel payload

ACK Channel

To configure the ACK Channel, select the ACK Channel tab as seen
 in the following figure. The ACK Channel can be turned on or off by selecting the
 appropriate value in the Channel State check box found in the ACK Channel frame. If this
 control is unselected, the ACK Channel is not transmitted. The default is Off
 (unselected).

[IMAGE alt='image' src='GUID-C03E19AD-EA33-4D92-AC5E-601B30CDBEC4-a5.gif']

Fig. 5-32 ACK configuration tab

The following ACK channel parameters can be set using the ACK
 tab.

Power

This is the gain of the ACK Channel with respect to the Pilot Channel. The value is in dB
 and has a valid range of -60 to 60 dB. The default value is 0 dB.

Start Slot

The start slot defines the slot (there are 16 slots per frame) in which the ACK
 transmission is to start. The default value is 0 dB.

ACK/NACK Gap

This is the spacing between ACK and/or NACK bits. The default value is 0.

ACK/NACK Pattern

You can select the pattern of acknowledge bits that are sent. A ‘0’ refers to an
 acknowledge (ACK) and a ‘1’ to a not acknowledge (NACK). The pattern can be set using
 the ACK(0)/NACK(1) Pattern edit box. The default is 01.

Multi-User ACK

If you select the Multi-User ACK checkbox, the ACK channel behaves as if it were
 acknowledging a multi-user packet. Otherwise, it behaves as if it is acknowledging a
 single-user packet. The default value is "off".

DSC Channel

To configure the DSC channel, click on the DSC Channel tab as shown in the following
 figure. The DSC Channel can be turned on or off by selecting or clearing the Channel
 State check box found in the DSC Channel frame. If this control is unselected, the DSC
 Channel is not transmitted. The default value is off (unselected)

[IMAGE alt='image' src='GUID-ABF78CE5-98E7-4244-9616-9A6B22F88FD6-a5.gif']

Fig. 5-33 DSC configuration tab

The following parameters can be set using the DSC configuration dialog:

Power

This is the gain of the DSC Channel with respect to the Pilot Channel. The value is in dB
 and has a valid range of -60 to 60 dB. The default value is 0 dB.

Start Slot

The start slot defines the slot (there are 16 slots per frame) in which the DSC
 transmission is to start. The default value is 0.

DSC length

This is the length of the DSC transmission in slots. The valid range is 8 to 256. The
 default value is 64.

DSC Value

The DSC value is used to indicate to the access network the selected serving cell on the
 forward link. Valid DSC values are between 0 and 7. The default value is 0.

RRI Channel

To configure the RRI Channel select the RRI Channel tab. The parameters associated with
 this channel are set in the RRI Channel frame. The following parameters can be set:

Channel State

The RRI Channel can be turned on or off by selecting the appropriate value using the
 Channel State check box. If this control is unselected, the RRI Channel is not
 transmitted. The default value is On (selected).

Power

This is the gain of the RRI Channel with respect to the Pilot Channel. The value is in dB
 and has a valid range of -60 to 60 dB. The default value is 0.

The values transmitted on the RRI channel are dependent on the payload transmitted on the
 data channel.

DRC Channel

To configure the DRC Channel, select the DRC Channel tab as shown in Fig. 5-176.The DRC
 Channel can be turned on or off by selecting or clearing the Channel State checkbox. If
 the DRC channel is off the DRC channel is not transmitted. The default value is Off
 (unselected)

[IMAGE alt='image' src='GUID-927E054E-CF81-4347-83C6-80310E0E28C2-a5.gif']

Fig. 5-34 The DRC configuration dialog

The following DRC Channel parameters can be set with the DRC configuration dialog:

Power

This is the gain of the DRC Channel with respect to the Pilot Channel. The value is in dB
 and has a valid range of -60 to 60 dB. The default value is 0 dB.

Gating

Request gated DRC transmissions by selecting the Gating check box. In this case, only one
 slot of DRC is transmitted over DRC-length slots. The default value is unselected.

Start Slot

The start slot defines the slot (there are 16 slots per frame) in which the DRC
 transmission is to start. Note that DRC transmissions are offset by half a slot, so if
 you set the start slot to 0, the DRC transmission actually starts half way through slot
 0. This is in accordance with the standard. The default value is 0.

DRC Length

This is the length of the DRC transmission in slots. Valid range is 1 to 8. The default
 value is 1.

DRC Value

The DRC value is used to request the Forward Traffic Channel data rate. The allowed DRC
 values lie between 0 and 15. The value is selected using the DRC Value box. The
 following table shows the data rate and span of the canonical transmission format
 associated with each DRC value, where the canonical transmission format is defined as
 the transmission format with the largest physical packet size. The default value is
 0.

[IMAGE alt='image' src='GUID-B39465AB-BCBF-4A8C-A134-6771E21017BB-a5.gif']

Table 5-6 Data Channel modulation formats

RFmx Waveform Creator allows you to set the DRC value to 15. The
 standard provides symbol values for this DRC value even though the higher-level protocol
 currently does not support it.

DRC Cover

The cover value is used to define the selected serving sector. Valid values range from 0
 to 7. The default value is 0.

Creating a Forward Link

Once you have set the general parameters, you can configure the forward channels.
 RFmx Waveform Creator provides the facility to set parameters
 for each of these channels using the controls shown in the following figure.

[IMAGE alt='image' src='GUID-8813EAC4-AADB-45D5-BE92-7BF228EC0FD4-a5.gif']

Fig. 5-35 EV-DO revision A Forward Link settings

Pilot PN Offset

The Pilot PN Offset is used to set the offset of the scrambling codes. Typically, each
 base station is assigned its own offset. The valid range of values is 0 to 511. The
 default value is 0.

Idle Noise Power

The Idle Noise Power can be turned on or off by clicking the checkbox. If it is turned
 on, AWGN is added to the idle periods within the generated signal at the specified
 level. This level is relative to the maximum power in the signal (nominally the pilot
 channel). The default value is off (unselected).

Pilot Channel

To configure the Pilot Channel, select the Pilot Channel tab. The Pilot Channel can be
 turned on or off by selecting or clearing the Pilot Channel check box. If this control
 is unselected, the Pilot Channel is not transmitted. The default value is On
 (selected).

Configuring the Traffic/Control Channel

To configure the Traffic/Control Channel, select the Traffic/Control Channel.

You configure the Forward Traffic/Control Channel via a table. You can add and remove a
 user to/from a table using the buttons underneath.

A user is an access terminal and the Forward Traffic/Control Channel can transmit one or
 more physical layer packets to up to 16 different users. The physical layer packets
 transmitted to a user are all at the same data rate and transmitted serially. Only
 physical layer packets from other users can be interleaved into the inactive slots.

A graphical representation of a frame is given to illustrate which slots are occupied and
 which slots are available. If a slot is occupied, it is color-coded according to the
 user and the modulation is given. The buttons either side of the frame graphic allow
 scrolling between frames.

To add a new user to the table, click on the Add… button. On doing
 so, a new line is added, shown in the following figure. From here, you can configure a
 user’s parameters.

[IMAGE alt='image' src='GUID-DE12B790-730F-40E9-A478-E163B2E57B37-a5.gif']

Fig. 5-36 Adding a Forward Traffic/Control Channel User before and
 after

MAC Index

The MAC Index is bi-orthogonally encoded to form the preamble symbols. When physical
 subtype 0 or 1 is selected the valid range of values is 0 to 63. When physical subtype 2
 is selected the valid range is 0 to 127. The default value is 0.

Data Rate

The available data rates for subtypes 0 and 1 are defined in Table 5-43. The available
 data rates for subtype 2 are defined in Table 5-44. The data rate can be selected using
 the Data Rate box. The default value is 38.4 kbps.

Number of Slots per Packet

The number of slots required to transmit one packet. Depending upon the selected data
 rate, this parameter is for information purposes only or it is set using the
 Number of Slots box.

Preamble Length

The length of the preamble in chips. Depending upon the selected data rate, this
 parameter is for information purposes only or it is set using the Preamble
 Length box.

Number of Packets

The number of packets that you wish to transmit to the access terminal (user). The valid
 range of values is 1 to 100. Note that if the current number of frames is insufficient
 to transmit the selected number of packets, the number of frames is automatically
 increased. The default value is 1.

Frame Offset

The frame offset defines the first slot a packet is transmitted in relative to slot 0 of
 the first frame. The valid range of values is 0 to 1600. The default value is 0.

Data Source

This shows the type of data used by the Data Channel. Allowed data types are All Zeroes,
 All Ones, PRBS, User Data, and Repeating Pattern. You can configure the data source
 being used by clicking on the Data source button. The default
 value is a PN9 sequence.

Preamble State

The preamble can be turned on or off by selecting or clearing the Preamble State box. If
 the preamble is not transmitted, IQ samples equal to zero are used. If the data is off
 and the preamble is on, only the preamble is transmitted. If a user is defined with
 multiple packets and only the preamble is on, the number of slots between the preambles
 is the same as when the data is transmitted. The default value is On.

Data State

The physical layer packet data can be turned on or off by selecting or clearing the Data
 State box. If the data and preamble are turned off, the packet(s) for this user are not
 transmitted. The default value is On.

You can also edit any of the parameters directly in the table, by double-clicking the
 left-hand mouse button on the appropriate cell. For example, clicking the left-hand
 mouse button on the number of Slots Per Packet of the selected user causes a drop-down
 menu to appear as shown in Fig. 5-179 .

[IMAGE alt='image' src='GUID-222FA876-6869-4726-8665-6C5B16331D49-a5.gif']

Fig. 5-37 Setting the number of slots per packet control

Configuring the MAC RA Channel

You can configure the MAC RA Channel using the MAC Channel frame. Click on the MAC
 Channel tab to configure the parameters of this channel. On doing so, you see the
 following settings shown in the following figure. From here, you can configure the
 channel’s parameters.

[IMAGE alt='image' src='GUID-40009FA8-8DC2-43F9-9C5E-4588A7DBCDE9-a5.gif']

Fig. 5-38 Configure MAC RA Channel dialog

MAC RA Channel State

The MAC RA Channel can be turned on or off by selecting or clearing the checkbox. When
 this control is unselected, no Mac RA Channel information will be transmitted. The
 default is off (unselected).

Power

This is the gain of the MAC RA Channel with respect to the Pilot Channel. The value is in
 dB and has a valid range of -60 to 60 dB. The default value is 0 dB.

RAB Start slot

This is the Reverse Activity start slot and determines the offset in slots from the start
 of a frame when the first RA bit is transmitted. The valid range of values is 0 to 15.
 The default value is 0.

RAB Length

This is the number of Reverse Activity Bits that will be transmitted. The default value
 is 8.

Data Pattern

This is the data pattern transmitted on the MAC RA Channel and it can be up to 16 bits
 long. The default pattern is 0.

Configuring the user-specific MAC channels

When physical subtype 0 or 1 is selected, you can configure the MAC RPC and DRCLock
 channels within the MAC Channel frame. When subtype 2 is selected, in addition to being
 able to configure the MAC RPC and DRCLock channels you can also configure the H/L-ARQ
 and P-ARQ channels.

When the physical subtype is changed from subtype 0 or 1 to subtype 2, the label that
 reads ‘MAC RPC/DRCLock Channel State’ changes to ‘User Specific Mac Channels
 State’.

MAC RPC/DRCLock Channel State (Subtypes 0 and 1)

The MAC RPC/DRCLock channels can be turned on or off by double-clicking the appropriate
 value in the table. The default is Off.

User-Specific Mac Channels State (Subtype 2)

The user-specific MAC channels (RPC, DRCLock and ARQ channels) can be turned on or off by
 double-clicking on the appropriate value in the table. The default is Off.

If the channels are on, the Configure… button next to the State
 box is enabled. Click on the Configure… button to configure the
 channels. On doing so, you are presented with the dialog box shown in the following
 figure if physical subtype 0 or 1 is selected, or the dialog box shown in the following
 figure if physical subtype 2 is selected.

[IMAGE alt='image' src='GUID-F077BA92-9234-4587-82B7-5612FFA2CF7F-a5.gif']

Fig. 5-39 Configure MAC RPC/DRCLock channels dialog
 (subtypes 0 and 1)

From here, you can configure the channels via a table. You can add, edit and remove
 channels to or from the table using the buttons underneath.

To add a new set of channels to the table, click on the Add…
 button. On doing so, a new MAC channel is added into the table if physical subtype 0 or
 1 is selected, or the dialog box if physical subtype 2 is selected. These dialogs will
 allow you to configure individual parameters of the User MAC Channels.

MAC Index

The MAC Index determines the Walsh code used to spread the symbols produced by the MAC
 channels. The default is 5. The valid range of values depends on the physical subtype
 selected. When subtype 0 or 1 is selected the MAC Index must be between 5 and 63. If
 subtype 2 is selected the MAC Index must be between 5 and 127.

Note that if you choose a MAC Index that is already in use, the row index, and the rows
 that share the same MAC index will turn red to warn you that the MAC Index is already in
 use shown in the following figure.

[IMAGE alt='image' src='GUID-94EAFF2B-EF81-4178-BE34-E45F5C398BCC-a5.gif']

Fig. 5-40 Forward MAC channel code conflict (1)

Frame Offset

This is used to determine when the MAC channels are transmitted with respect to the start
 of the frame. The valid range of values is 0 to 15. The default value is 0.

RPC Channel

RPC Channel configuration can be modified either through the main table, or via the User
 MAC channel edit dialog, which can be shown by selecting the relevant row on the main
 table, and clicking the Edit… button.

[IMAGE alt='image' src='GUID-2FC979B5-FC91-4B20-AAB2-6D8E24872D68-a5.gif']

Fig. 5-41 Mac RPC Channel edit parameters

RPC Power

This is the gain of the MAC RPC channel with respect to the Pilot Channel. The value is
 in dB and has a valid range of -60 to 60 dB. The default value is 0.

RPC Data Pattern

This is the data pattern transmitted on the MAC RPC channel and it can be up to 16 bits
 long. The default value is 0.

RPC Channel State

The MAC RPC channel can be turned on or off by selecting or clearing the Channel State
 check box. If the channel is off (unselected), the MAC RPC channel is not transmitted.
 The default is Off.

DRCLock Channel

DRCLock Channel configuration can be modified either through the main table, or via the
 User MAC channel edit dialog, which can be shown by selecting the relevant row on the
 main table, and clicking the Edit… button.

[IMAGE alt='image' src='GUID-E4632934-0621-4558-95AE-CF190A2B97A2-a5.gif']

Fig. 5-42 Showing the DRCLock Channel tab active

DRC Length

This is the DRCLockLength parameter, which determines how many times a DRCLock bit is
 repeated. The default value is 4.

DRC Period (Subtypes 0 and 1 only)

This is the DRCLockPeriod parameter, which determines the gap between each DRCLock
 channel transmission. The default value is 8. This field does not appear when physical
 subtype 2 is selected.

DRC Power

This is the gain of the MAC DRCLock channel with respect to the Pilot Channel. The value
 is in dB and has a valid range of -60 to 60 dB. The default value is 0 dB.

DRC Data Pattern

This is the data pattern transmitted on the MAC DRCLock channel and it can be up to 16
 bits long. The default value is 0.

DRC Channel State

The MAC DRCLock channel can be turned on or off by selecting or clearing the Channel
 State box. If the channel is off (unselected), the MAC DRCLock channel is not
 transmitted. The default is Off.

H/L-ARQ (Subtype 2 only)

H/L ARQ Channel configuration can be modified either through the main table, or via the
 User MAC channel edit dialog, which can be shown by selecting the relevant row on the
 main table, and clicking the Edit… button.

[IMAGE alt='image' src='GUID-078F755B-65DF-46FE-B72C-E0B4425AE83C-a5.gif']

Fig. 5-43 Showing H/L Arq configuration.

H/L-ARQ Power

This is the gain of the H/L-ARQ channel with respect to the Pilot Channel. The value is
 in dB and has a valid range of -60 to 60 dB. The default value is 0 dB.

H/L-ARQ Channel State

The H/L-ARQ channel can be turned on or off by selecting or clearing the Channel State
 box. If the channel is off (unselected), the H/L-ARQ channel is not transmitted. The
 default is Off.

H/L-ARQ Pattern length

H/L-ARQ pattern length sets the length of the H/L-ARQ pattern in sub-packets. The valid
 range of values is 0 to 16. The default value is 1. Changing the H/L ARQ Pattern will
 modify the available items within the H/L ARQ Pattern table.

[IMAGE alt='image' src='GUID-AF63D694-B387-41D7-98C2-3D5AF13AE220-a5.gif']

Fig. 5-44 Showing H/L Arq pattern table after changing the pattern
 length

H/L-ARQ Pattern

The H/L-ARQ pattern lets you configure the ACK/NACK pattern that is transmitted. The
 H/L-ARQ table contains one item for each sub-packet. The H/L-ARQ pattern table has three
 editable fields:

1. State : if this is true the ACK/NACK is transmitted in the
 sub-packet. Otherwise it is not.
2. ACK/NACK : is an ACK or a NACK sent in the sub-packet. The
 default value is ACK.
3. Modulation : is the type of modulation used to send the ACKS
 or NACKS. This can be BPSK, AOOK, NOOK. The default value is BPSK. BPSK or AOOK
 should be used if an H-ARQ is being sent. If an L-ARQ is being sent, NOOK should be
 used.

Repeat Pattern

If the repeat pattern check box is not selected the H/L-ARQ pattern is only transmitted
 once; otherwise the H/L-ARQ pattern is repeated until the end of the transmission. By
 default, the H/L-ARQ pattern is not repeated.

P-ARQ (Subtype 2 only)

P-ARQ Channel configuration can be modified either through the main table, or via the
 User MAC channel edit dialog, which can be shown by selecting the relevant row on the
 main table, and clicking Edit…

[IMAGE alt='image' src='GUID-D7B14ED9-8302-41F4-9E8D-571AE166CFF9-a5.gif']

Fig. 5-45 Showing P-ARQ configuration tab

P-ARQ Power

This is the gain of the P-ARQ channel with respect to the Pilot Channel. The value is in
 dB and has a valid range of -60 to 60 dB. The default is 0 dB.

P-ARQ Channel State

The P-ARQ channel can be turned on or off by selecting or clearing the Channel State box.
 If the channel is off, the P-ARQ channel is not transmitted. The default is Off.

P-ARQ Pattern Length

P-ARQ pattern length sets the length of the P-ARQ pattern in sub-packets. The valid range
 of values is 0 to 16. The default value is 1. As you change the pattern length, the
 pattern table below this control will add or remove new rows for defining the P-ARQ
 Pattern.

P-ARQ Pattern

The P-ARQ pattern lets you configure the ACK/NACK pattern that is transmitted. The P-ARQ
 table contains one item for each sub-packet. The P-ARQ pattern table has two editable
 fields:

1. State : If this is true the ACK/NACK is transmitted in the
 sub-packet. Otherwise it is not.
2. ACK/NACK : This is an ACK or a NACK sent in the sub-packet.
 The default value is ACK.

Repeat Pattern

If the Repeat Pattern checkbox is not selected, the P-ARQ pattern is transmitted once
 only; otherwise the P-ARQ pattern is repeated until the end of the transmission. By
 default, the P-ARQ pattern is not repeated.

Generating a Waveform

Once you have set up the forward channel and the channel filter to suit your needs, you
 can generate the waveform in the same way as for other modulation schemes. Select the
 Generate TDMS File! menu and proceed as described in the
 RFmx Waveform Creator Help document.

Parent topic:

EV-DO Revision A

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-a-gsmedge-waveform-overview.html language=enus -->
## TOPIC 00030: Creating a GSM/EDGE Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-a-gsmedge-waveform-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-a-gsmedge-waveform-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create an GSM waveform, complete the following steps: Select the Modulation drop-down menu. Select GSM to display the generation settings window. Select either the New Default Settings or the Example Settings from the generation settings window. This opens the GSM window, which has tabs for Modul

### Creating a GSM/EDGE Waveform

To create an GSM waveform, complete the following steps:

1. Select the Modulation drop-down menu.
2. Select GSM to display the generation settings window.
3. Select either the New Default Settings or the
 Example Settings from the generation settings window.
 This opens the GSM window, which has tabs for Modulation,
 Frame configuration, IQ Impairments, and Graphics settings. These tabs provide the
 same functionality as other modulations.

GSM/EDGE supports two modes of operation, Basic and
 Advanced. The default system mode is
 Basic.

[IMAGE alt='image' src='GUID-2CCF0035-0FF6-404B-B72E-02C1BBA9A635-a5.png']

Basic: Allows you to configure a basic signal and to create basic
 slot information.

Advanced: Allows you to create signals that can be used by
 receiver and more complex BER testing.

Parent topic:

GSM/EDGE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-a-nr-waveform-overview.html language=enus -->
## TOPIC 00031: Creating a NR Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-a-nr-waveform-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-a-nr-waveform-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a NR waveform, complete the following steps: Select the Modulation drop-down menu. Select NR to display the generation settings window. Select either the New Default Settings or the Example Settings from the generation settings window. This opens the NR window, which has tabs for Modulatio

### Creating a NR Waveform

To create a NR waveform, complete the following steps:

1. Select the Modulation drop-down menu.
2. Select NR to display the generation settings window.
3. Select either the New Default Settings or the
 Example Settings from the generation settings window.
 This opens the NR window, which has tabs for Modulation,
 Multi-Carrier, Filter, IQ Impairments, and Graphics settings. These tabs provide the
 same functionality as other modulations.

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-a-td-scdma-3gpp-tdd-lcr-waveform.html language=enus -->
## TOPIC 00032: Creating a TD-SCDMA (3GPP TDD-LCR) Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-a-td-scdma-3gpp-tdd-lcr-waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-a-td-scdma-3gpp-tdd-lcr-waveform.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a new TD-SCDMA (3GPP TDD-LCR) waveform, Select the Modulation menu. Click TD-SCDMA. The New Settings File window appears. Click OK in the New Settings File window. The TD-SCDMA settings window appears. Note: If the TD-SCDMA window does not appear in the Modulation menu, use the Tools menu

### Creating a TD-SCDMA (3GPP TDD-LCR) Waveform

To create a new TD-SCDMA (3GPP TDD-LCR) waveform,

1. Select the Modulation menu.
2. Click TD-SCDMA . The New Settings
 File window appears.
3. Click OK in the New Settings File 
 window.
4. The TD-SCDMA settings window appears.

Note: If the TD-SCDMA window does not
 appear in the Modulation menu, use the
 Tools menu to add Registered Plugins
 niTdscdmaGenPlugin.dll.

If example settings are available, you are offered a choice to create a New
 Default Setting or select an Example
 Settings.

The TD-SCDMA window has tabs for
 Modulation, Filter, IQ
 Impairments, and Graphics settings. These tabs
 are the same as those found in other modulations.

On the Modulation tab, you can set the Cell
 Configuration and Frame Configuration. In
 addition, information is given on the chip rate and oversampling factor.

[IMAGE alt='image' src='GUID-54208154-1859-4D8D-9D9B-4638C192236C-a5.gif']

Fig. 6-12 TDD-LCR modulation settings

Parent topic:

TD-SCDMA (3GPP TDD-LCR)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-a-waveform.html language=enus -->
## TOPIC 00033: Creating a Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-a-waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-a-waveform.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a waveform, select the Modulation menu, which presents you with all the modulation schemes currently supported by the application. For more information about the supported schemes, refer to the RFmx Waveform Creator Modulation Schemes. For example, from the Modulation drop-down list, selec

### Creating a Waveform

To create a waveform, select the Modulation menu, which presents
 you with all the modulation schemes currently supported by the application. For more
 information about the supported schemes, refer to the RFmx Waveform Creator
 Modulation Schemes.

For example, from the Modulation drop-down list, select
 Generic»PSK. This opens New Settings
 File window as shown in the following image.

[IMAGE alt='image' src='GUID-13297B93-0B76-44C7-ADA9-20CCA1D5317C-a5.png']

- New Default Settings : Enables you to define a new modulation
 scheme.
- Example Settings : Enables you to use example settings that
 have been provided with RFmx Waveform Creator, or those that you may have previously
 created and saved in the RFmx Waveform Creator Examples directory. Refer to RFmx Waveform Creator Examples topic for more information.

For this example, select New Default Settings and click
 OK. This opens a new window, which has tabs for Modulation,
 Multi-Carrier, Filter, IQ Impairments, and Graphics settings.

Related concepts:

- RFmx Waveform Creator Examples
- RFmx Waveform Creator Modulation Schemes

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-an-analog-waveform.html language=enus -->
## TOPIC 00034: Creating an Analog Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-an-analog-waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-an-analog-waveform.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Generates an analog waveform using RFmx Waveform Creator. To create a new analog waveform, complete the following steps. Select the Modulation menu. Point to Generic and then click Analog. The Analog settings window appears. If Analog does not appear in the Generic menu, use the Tools menu to add Re

### Creating an Analog Waveform

Generates an analog waveform using RFmx Waveform
 Creator.

To create a new analog waveform, complete the following steps.

1. Select the Modulation menu.
2. Point to Generic and then click
 Analog . The Analog settings window
 appears.

Note

Analog

Generic

Tools

niAnalogGenPlugin.dll

Create a New Default Settings

Example
 Settings

Figure 6.

[IMAGE alt='Analog Dialog Box, Modulation Tab' src='GUID-6768933A-722D-4D05-B299-36883820C552-a5.gif']

The Analog Modulation system provides tabs for Modulation,
 RDS Common parameters, RDS Group
 version type parameters, Filter, IQ
 Impairments, and Graphics. Filter, IQ Impairments
 and Graphics are used in the same way as other modulation schemes. Refer to the
 RFmx Waveform Creator Help document for more information.

Parent topic:

Analog Modulation

#### RDS Common Parameters

[IMAGE alt='image' src='GUID-B79EF308-6D73-49D2-9DCD-392C825BCF92-a5.gif']

Fig. 8-9 RDS Common Parameters tab

This tab contains common parameters for the RDS mode of operation. This tab is disabled
 if the FM Mode on the main Modulation tab is not set to
 FM RDS.

Payload Type

The payload type can either be a Bit Source or a
 Message. When the payload type is set to Bit
 Source, no encoding is applied to the bits transmitted. The bit source
 can be configured to be one of the following:

- Zeros
- Ones
- PRBS
- Random
- User Data (From a file)
- Repeating pattern

When the Payload Type is set to Message, a
 fully coded RDS message is produced. The type of message produced is dependent on the
 Message Type parameter.

PI Code

The PI (Program identification code) is a 16 bit value used to identify a Program. The PI
 code can take any value form 0 to 65535. The Program area code is currently read only
 and is calculated from the PI Area code, PI Country code, and Program reference
 number.

PI Country Code

The PI Country code forms the first 4 bits of the PI code. The Country code is entered in
 hex and can take any value from 0x1 to 0xF.

PI Area Code

The PI area code forms Bits b<sub>11</sub> to b<sub>8</sub> (where b<sub>0</sub> is the
 LSB) of the PI code. The PI area code can take one of the following values:

- Local = 0
- International = 1
- National = 2
- SupraRegion = 3
- R1 = 4
- R2 = 5
- R3 = 6
- R4 = 7
- R5 = 8
- R6 = 9
- R7 = 10
- R8 = 11
- R9 = 12
- R10 = 13
- R11 = 14
- R12 = 15

Program Reference Number

The program reference number is used to form the last 8 bits of the PI code. The program
 reference can take any value from 0 to 255.

Traffic Program

The Traffic Program (TP) is used to indicate whether the Program carries Traffic
 Announcements.

PTY Code

- Local = 0
- News = 1
- Current Affairs = 2
- Information = 3
- Sport = 4
- Education = 5
- Drama = 6
- Culture = 7
- Science = 8
- Varied = 9
- Pop Music = 10
- Rock Music = 11
- Easy Music = 12
- Light Classical = 13
- Seriously Classical = 14
- Other Music = 15
- Weather = 16
- Finance = 17
- Children = 18
- Social Affairs = 19
- Religion = 20
- Phone In = 21
- Travel = 22
- Leisure = 23
- Jazz Music = 24
- Country Music = 25
- National Music = 26
- Oldies Music = 27
- Folk Music = 28
- Documentary = 29
- Alarm Test = 30
- Alarm = 31

TMC ID

The TMC (Traffic message channel) ID. Is 12 bits long and can take any value from 0 to
 4095. The TMC ID is used to from a Program Item number and slow labeling message
 (Version A). The TMC ID will only be transmitted when the variant code for the message
 is 1 (TMC ID)

EWS Channel ID

The EWS Channel ID is 12 bits long and can take any value from 0 to 4095.

The EWS Channel ID is used to from a Program Item number and slow labeling message
 (Version A). The EWS Channel ID will only be transmitted when the variant code for the
 message is 7 (Identification of EWS channel)

Transmitter Network Group Designation

The Transmitter group designation forms the first 3 bits of the paging information
 transmitted in every Version A Program Item number and slow labeling message. The
 Transmitter group designation can take any value from 0 to 7.

Battery Saving Internal

Forms the first 5 bits of the paging information transmitted in every Version A Program
 Item number and slow labeling message. Battery saving internal can take any value from 0
 to 3.

Linking Actuator

The linking actuator is a single bit that is first bit transmitted in block 3 of every
 Version A Program Item number and slow labeling message. The value can be either 1 or
 0.

Operator Paging Code

The operator paging code is used in two different variants of the version A Program Item
 number and slow labeling message. It is transmitted with the extended country code when
 the variant code for the message is 0 (OPC/ extended country). It is also transmitted
 when the variant code is 2 (Paging identification).

Paging Area Code

The paging area code is transmitted with the operator paging code in a version A Program
 Item number and slow labeling message. The paging area code is only transmitted when the
 message variant code is 2 (Paging identification).

Extended Country Code

The extended country code is transmitted with the operator paging code in a version A
 Program Item number and slow labeling message. The extended country code is only
 transmitted when the variant code for the message is 0 (Paging/ extended country) code.
 The extended country code is entered in hex and can take any value from 0 to 0xFF.

Language Code

The Language code is 12 bits long and can take any value from 0 to 4095. The Language
 code is used to from a Program Item number and slow labeling message (Version A). The
 Language code will only be transmitted when the variant code for the message is 3
 (Language codes).

#### RDS Group Version Type Parameters

This tab contains key parameters for setting the Group Version and Type parameters of an
 RDS signal. If the Generation type in the main
 Modulation tab is not set to FM RDS,
 this tab will be disabled.

[IMAGE alt='image' src='GUID-2BDFDA5A-2245-4AF9-A622-E0547647A23D-a5.gif']

Fig. 8-2 RDS Group Version Type Parameters tab

Message Type

This specifies the type of message to transmit (when the payload type is
 Message). The Message Type can take one of the following
 values:

- Basic tuning and switching
- Radio Text
- Date and time
- PIN slow labeling code
- ODAAID
- EON
- PTYN
- Composite

When the Message Type is set to Composite,
 the Group type is ignored. Otherwise the selection of the
 Message Type is limited to the Message Type(s) transmitted
 using the specified Group type.

A composite message can be made up of any (non Composite message type). When the
 Message Type is set to Composite, the
 Composite Message Type drop-down menu appears. This can be used to configure the
 messages that make up the composite message.

Composite Message Type

A composite message can be made up of multiple messages. When the Message
 Type is set to Composite, the
 Composite Message Type drop-down menu appears. This can be
 used to configure the messages that make up the composite message. Each of the messages
 in the composite message can be included/excluded by switching the message on /off.

Group Type

The group type can take one of the following values:

- 0 :- Basic tuning and switching
- 1 :- PIN slow labeling code
- 2 :- Radio Text
- 3 :- (Version A only) ODAAID
- 4 :- (Version A only) Date and time
- 10 :- (Version A only) PTYN
- 14 :- EON

Basic Tuning and Switching

[IMAGE alt='image' src='GUID-B519F57F-AFE2-4E8B-94BA-1A8A968ACA2C-a5.gif']

Fig. 8-3 Basic Tuning and Switching Parameters

Group Version

The group version can be A or B. The group B version of the message does not transmit
 Alternative frequency information.

Decoder ID

The decoder ID transmits information about the signal to help the receiver decode it
 properly. The decoder ID is made up of the following fields.

Decoder ID0

This can be set to Stereo or Mono.

Decoder ID1

This can be set to Artificial or
 Not-Artificial.

Decoder ID2

This can be set to Compressed or
 Non-Compressed

Decoder ID3

This can be set to static PTY or dynamic PTY. This field indicates whether the PTY is
 transmitted. The PTY(s) Referenced in an eon messages can change.

Music or Speech

This can be set to Music or Speech, and
 indicates whether music or speech is being transmitted.

Traffic Announcement

This parameter is used to set the TA bit and can be set to On or
 Off. This is used in conjunction with TP bit to transmit
 information regarding traffic announcements.

PSN String

This is string of 8 characters in length. This is used to indicate the Programme service
 name.

Alternative Frequencies(Version A only)

It is possible to configure 2 alternative frequencies. For each alternative frequency the
 following fields can be set:

Frequency Type

This can be LF, MF, or VHF. This specifies the type of alternative frequency.

Carrier Frequency

The alternative carrier frequency can be between 153 kHz and 107.9 MHz

Programme Item number and slow labelling message

[IMAGE alt='image' src='GUID-D4BA7405-581B-4360-899A-E6986F7FF24F-a5.gif']

Fig. 8-4 Programme Item Number and Slow Labelling message
 screen.

Group Version

The group version can be A or B. Version B of the message does not transmit slow
 labeling.

Variant Code (Version A only)

The variant code specifies the type of information to be transmitted in the message. The
 variant code can take the following values:

- Extended Country Code
- TMC ID
- Paging ID
- Language Code
- Not Assigned
- Not Assigned 1
- Broadcaster
- EWS Channel

Radio Text

[IMAGE alt='image' src='GUID-E8DF6567-8CE7-4DAE-83BC-F074FB9073E6-a5.gif']

Fig. 8-5 Radio Text screen.

Group Version

The group version can be A or B. Version B of this message transmits text at half the
 rate of the version A.

Text A/B

This field can be set to A or B. In an RDS signal the A/B field would change from A to B
 or vice versa when the radio text string needs to be cleared.

Radio Text String

This is a string. This is contains the RDS text to transmit.

ODAAID (Open Data Application Identifier)

[IMAGE alt='image' src='GUID-EB36E11B-BAD5-42E3-B847-FD4316559A2D-a5.gif']

Fig. 8-6 ODAAID screen

Open data applications are applications that are not part of the RDS standard. An Open
 application identifier message is used to identify groups that are used to transmit data
 for an open data application.

Group Version

This message can only be transmitted using the Group version A.

Application Group Type Code

This indicates the Group type (and version) code that will be used to transmit the open
 application data. This field can take one of the following values:

- 3B
- 4A
- 4B
- 5A
- 5B
- 6A
- 6B
- 7A
- 7B
- 8A
- 8B
- 9A
- 9B
- 10A
- 10B
- 11A
- 11B
- 12A
- 12B
- 13A
- 13B
- 14A
- 14B
- 15A
- 15B
- Fault

ODA ID (Open Data Application) ID

This field is 16 bits long and can be set to any value from 0 to 65535. This field is
 used to identify the application that will transmit the data.

ODA AID Message Bits

This is a 16 bit value that contains message bits for the Open data application. This
 field can take any value from 0 to 65535.

PTYN (Programme Type Name)

[IMAGE alt='image' src='GUID-09709853-B422-408D-A1DF-03D6B600DE10-a5.gif']

Fig. 8-7 PTYN screen

Group Version

This message can only be transmitted using group version A

PTY Name

This field can be set to A or B. In an RDS signal the A/B field is changed from A to B or
 vice versa when ever the PTY name is changed

PTYN String

This is an 8 character string used to describe the programme type.

EON (Enhanced Other Networks Information)

[IMAGE alt='image' src='GUID-A0F14B36-2199-45BB-986F-E44A7D3F4EF1-a5.gif']

Fig. 8-8 EON Screen.

A Version A and A version B of this message exist. Version B of this message does not
 transmit the EON information field or the EON Variant code.

EON Information (Version A Only)

This field contains the EON information. This field is a 16 bit value and can take any
 value from 0 to 65535. The meaning of the bits transmitted in this field depends on the
 EON variant code.

EON Variant Code (Version A Only)

This specifies the type of EON information that is transmitted in this massage. The EON
 variant code can be set to any value from 0 to 15.

PI Code Other Network

This is a 16 bit value used to identify a Programme transmitted on the other network. The
 PI code can take any value form 0 to 65535. The Programme area code is currently read
 only and is calculated from the PI Area code, PI Country code, and Programme reference
 number.

PI Country Code Other Network

This is the PI country code for the other network. The PI Country code forms the first 4
 bits of a PI code. The value is entered in hex and can take any value from 0x1 to
 0xF.

PI Area Code Other Network

This is the PI area code for the other network. The PI area code forms Bits
 b<sub>11</sub> to b<sub>8</sub> (where b<sub>0</sub> is the LSB) of a PI code. The
 PI area code can take one of the following values:

- Local = 0
- International = 1
- National = 2
- SupraRegion = 3
- R1 = 4
- R2 = 5
- R3 = 6
- R4 = 7
- R5 = 8
- R6 = 9
- R7 = 10
- R8 = 11
- R9 = 12
- R10 = 13
- R11 = 14
- R12 = 15

Programme Reference Number Other Network

This is the programme reference for the other network. The programme reference number is
 used to form the last 8 bits of a PI code. The programme reference can take any value
 from 0 to 255.

TP (Traffic Programme) Other Network

The Traffic Programme (TP) is used to indicate whether the other network is transmitting
 a Programme that carries Traffic announcements.

TA (Traffic Announcements) Other Network

This is used to indicate the sate of the TA bit on the other network. The TA bit is used
 in conjunction with TP bit to transmit information regarding traffic announcements.

PTY Code Other Network

This is the PTY code for the other network. A PTY code indicates the type of programme
 that is being transmitted the programme type is a 5 bit value and can take one of the
 following values:

- None = 0
- News = 1
- Current Affairs = 2
- Information = 3
- Sport = 4
- Education = 5
- Drama = 6
- Culture = 7
- Science = 8
- Varied = 9
- Pop Music = 10
- Rock Music = 11
- Easy Music = 12
- Light Classical = 13
- Seriously Classical = 14
- Other Music = 15
- Weather = 16
- Finance = 17
- Children = 18
- Social Affairs = 19
- Religion = 20
- Phone In = 21
- Travel = 22
- Leisure = 23
- Jazz Music = 24
- Country Music = 25
- National Music = 26
- Oldies Music = 27
- Folk Music = 28
- Documentary = 29
- Alarm Test = 30
- Alarm = 31

#### FM Parameters

Input Mode

The input mode configures how the left/right channels are configured the input mode can
 take on of the following values:

Off (no audio) Left only Right only Left = Right
 Left = - Right Left and Right The input mode parameter is only applicable when a stereo
 signal is being transmitted (When the Generation Type is set to
 FM Stereo/FM RDS). If the
 Generation Type is set to FM mono, the
 Input Mode is ignored and the Modulating Signal is configured using the parameters for the
 Left channel. The following table shows how the FM stereo channels are configured for a
 given input mode. It is worth noting that when the input mode is Left = Right, or Left =
 -Right the parameters for the right channel are ignored and the signal that is transmitted
 on the Right channel is worked out from the configuration of the Left channel.

[IMAGE alt='image' src='GUID-15EB32BA-E0B6-4656-B37F-DBC2A8081527-a5.gif']

Table 8-1 how the FM stereo channels are configured for a given
 input mode

The mono component in a FM stereo signal consists of the Left channel + the Right
 channel. The stereo component in a FM stereo signal consists of the Left channel - the
 Right channel. This means that when the input mode is Left = Right no stereo component
 will get transmitted, and when the input mode is Left = - Right no mono component is
 transmitted.

Left and Right Channel Parameters

In case of FM Stereo, you can configure the FM Left and Right Channel parameters by
 selecting the FM Left Right Parameters button. This will display
 the dialog shown below.

[IMAGE alt='image' src='GUID-72B213E7-6781-4F6F-A864-372750794FA4-a5.gif']

Fig. 8-10 Left Right Channel Parameters screen

If you are configuring an FM Mono signal, this screen shows only a single set of
 Frequency, amplitude, and Phase controls.

The following parameters can be configured for both the left and the right channels.

Modulating Frequency

This specifies the frequency of the tone to be transmitted on the channel. The modulating
 frequency can be in the range 100 Hz to 15 KHz.

Amplitude

This parameter specifies the amplitude of the tone to be transmitted. This parameter is
 only useful when both the left and right channels are being transmitted. By configuring
 the amplitude of the left / right channel, it is possible to configure the balance
 between the left and right channel.

Initial Phase

This parameter specifies the starting phase of the tone. The initial phase can be between
 +/- 2π radians.

Deviation Parameters

You can specify the deviation specific parameters of an FM signal by pressing the FM
 Deviation parameters button. This will display the screen shown in the following
 figure.

[IMAGE alt='image' src='GUID-5CF639CD-D3AB-4EAE-A4E7-794E388A45C9-a5.gif']

Fig. 8-11 FM Deviation Parameters Screen

Frequency Deviation

The frequency deviation is specified in Hz and can take a value between 1Hz and 5
 MHz.

In a Mono signal, the frequency deviation is the maximum frequency deviation (The maximum
 amount the modulated signal deviates from the carrier).

In a FM Stereo or FM RDS signal, the frequency deviation parameter specifies the amount
 of deviation that is applied to the audio signal. The amount of pilot and/or RDS
 deviation can be specified separately.

In a FM stereo signal, the maximum possible total deviation = audio frequency deviation +
 pilot deviation.

In a RDS signal, the maximum possible total deviation = audio frequency deviation + pilot
 deviation + RDS deviation.

For the maximum total deviation to occur all the subcarriers of the signal have to peak
 at the same time. For example, in a RDS system the audio the pilot and the RDS carriers
 would all have to be at there peak value for the maximum possible deviation to occur. If
 the peaks of the subcarriers do not line up the total deviation may be less than the
 potential maximum.

Pilot Frequency Deviation

The pilot frequency deviation controls how much the pilot signal causes the modulated
 signal to deviate from the carrier. The value is specified in Hz and can take any value
 from 0 to 75 kHz

Pre-emphasis Filter Parameters

You can edit the Pre-emphasis parameters of an FM signal by clicking on the FM
 Pre-Emphasis Parameters button. This will show the screen shown in the
 following figure.

[IMAGE alt='image' src='GUID-7AF57333-60AB-48DA-ABE3-47C880DA175B-a5.gif']

Fig. 8-12 FM Pre Emphasis Parameters screen.

Pre Emphasis

Pre Emphasis can be set to one of the following values:

- None
- 50μs
- 75μs

When Pre Emphasis is set to None, no Pre Emphasis is applied; otherwise
 the pre-emphasis characteristic of the sound signal is identical to the
 admittance-frequency curve of a parallel resistance-capacitance circuit having a time
 constant of 50μs or 75μs

Pre Emphasis Gain Type

The Pre Emphasis Gain type can be one of the following values:

- Not Normalized
- Normalized

When the Pre Emphasis Gain type is normalized, the Gains due to
 Pre Emphasis are scaled relative to the Pre Emphasis Reference frequency. Otherwise they
 are not. If the gain is normalized all Pre Emphasis gains will be divided by the gain
 that would be applied to the Pre Emphasis Reference frequency.

In normalized mode, signals transmitted at the Pre Emphasis Reference frequency will be
 transmitted at 0 dB; Signals which require more gain than the Reference frequency
 (higher frequencies) will be transmitted with a positive gain; and Signals which require
 less gain than the Reference frequency (lower frequencies) will be transmitted with a
 negative gain.

Pre Emphasis Reference Frequency

When the Pre Emphasis Gain type is Normalized, this parameter specifies the frequency to
 use to normalize the Pre Emphasis Gain (see description of Pre Emphasis Gain type). The
 value is specified in Hz and can take a value between 100 Hz to 15 kHz.

#### AM Parameters

This section lets you configure the modulation parameters of the AM DSB Signal. It
 comprises the following controls.

[IMAGE alt='image' src='GUID-6768933A-722D-4D05-B299-36883820C552-a5.gif']

Fig. 8-13 AM Modulation Screen

Modulation Index

This parameter specifies the ratio of the unmodulated carrier amplitude to the amplitude
 deviation for which the modulated carrier wave reaches its minimum value. The Modulation
 Index can be in the range of 0 to 1.

Message Frequency

This parameter specifies the frequency of the message signal to be transmitted on the
 channel. The message frequency can be in the range of 150 Hz to 50 KHz.

Number of Samples

This parameter specifies the number of samples to generate. The minimum value that can be
 set is 100.

Sampling Rate

This is a read-only parameter which displays the sampling rate of the generated
 signal.

Number of Message Samples

This is a read-only parameter which displays the actual number of samples generated.

#### Signal Length

When the Generation Mode is Manual, you can set the Signal Length. The sampling frequency
 is specified in seconds, and can take no less than 10 ms. When in Manual mode, no
 checking is done to ensure the signal wraps.

#### Sampling Frequency

When the Generation mode is Manual, you can set the sampling frequency. The sampling
 frequency is specified in Hz. The sampling frequency does not have an upper and lower
 limit. But if the sampling frequency is set to less than 4×, the bandwidth obtained from
 Carson’s rule a conflict will be raised.

#### Generation Mode

The Generation Mode can either be Auto or
 Manual.

In Auto mode, the signal length and sampling frequency are
 automatically calculated. In Manual mode, the sampling frequency
 and signal duration are user-defined.

When in Auto mode, length of the signal is set so that the signal will always wrap. For
 an FM signal, the calculation used to automatically set the sampling frequency is based
 on Carson’s bandwidth rule. Carson’s rule states that 98% of the signal power will be
 contained in a bandwidth of 2*(f<sub>m</sub>+ΔF). Where f<sub>m</sub>= the highest
 modulating frequency, and ΔF = the frequency deviation. The sample rate is set to 4 ×
 The bandwidth obtained from Carson’s rule. If this calculation returns a value of less
 than 768kHz then the sampling rate will be set to 768kHz.

#### Generation Type

Currently the Generation Type can be set to FM
 Mono, FM Stereo, FM RDS,
 or AM DSB.

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-an-lte-fdd-waveform.html language=enus -->
## TOPIC 00035: Creating an LTE FDD Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-an-lte-fdd-waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-an-lte-fdd-waveform.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create an LTE FDD waveform, complete the following steps: Select the Modulation drop-down menu. Select LTE option and click LTE FDD to display the generation settings window. Select either the New Default Settings or the Example Settings from the generation settings window. This opens the LTE FDD

### Creating an LTE FDD Waveform

To create an LTE FDD waveform, complete the following steps:

1. Select the Modulation drop-down menu.
2. Select LTE option and click LTE FDD to
 display the generation settings window.
3. Select either the New Default Settings or the
 Example Settings from the generation settings window.
 This opens the LTE FDD window as shown in the following
 figure, which has tabs for Modulation, Multi-Carrier, Filter, CFR, IQ Impairments,
 and Graphics settings. These tabs provide the same functionality as other
 modulations.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-an-lte-laa.html language=enus -->
## TOPIC 00036: Creating an LTE LAA Waveform Overview

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-an-lte-laa.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-an-lte-laa.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create an LTE LAA waveform, complete the following steps: Select the Modulation drop-down menu. Select LTE option and click LTE LAA to display the generation settings window. Select either the New Default Settings or the Example Settings from the generation settings window. This opens the LTE LAA

### Creating an LTE LAA Waveform Overview

To create an LTE LAA waveform, complete the following steps:

1. Select the Modulation drop-down menu.
2. Select LTE option and click LTE LAA to
 display the generation settings window.
3. Select either the New Default Settings or the
 Example Settings from the generation settings window.
 This opens the LTE LAA window as shown in the following
 figure, which has tabs for Modulation, Multi-Carrier, Filter, CFR, IQ Impairments,
 and Graphics settings. These tabs provide the same functionality as other
 modulations.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-an-lte-tdd-waveform-overview.html language=enus -->
## TOPIC 00037: Creating an LTE TDD Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-an-lte-tdd-waveform-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-an-lte-tdd-waveform-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create an LTE TDD waveform, complete the following steps: Select the Modulation drop-down menu. Select LTE option and click LTE TDD to display the generation settings window. Select either the New Default Settings or the Example Settings from the generation settings window. This opens the LTE TDD

### Creating an LTE TDD Waveform

To create an LTE TDD waveform, complete the following steps:

1. Select the Modulation drop-down menu.
2. Select LTE option and click LTE TDD to
 display the generation settings window.
3. Select either the New Default Settings or the
 Example Settings from the generation settings window.
 This opens the LTE TDD window as shown in the following
 figure, which has tabs for Modulation, Multi-Carrier, Filter, CFR, IQ Impairments,
 and Graphics settings. These tabs provide the same functionality as other
 modulations.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-fixed-reference-channels-reference.html language=enus -->
## TOPIC 00038: Creating Fixed Reference Channels, Reference Measurement Channels

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-fixed-reference-channels-reference.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-fixed-reference-channels-reference.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: If your installation is accompanied by example settings files, you will be able to select RFWS files for the supported Fixed Reference Channels and Reference Measurement Channels. The name of the RFWS file specifies the reference channel that it configures. For other reference channels not supplied

### Creating Fixed Reference Channels, Reference Measurement Channels

If your installation is accompanied by example settings files, you will be able to select
 RFWS files for the supported Fixed Reference Channels and Reference Measurement
 Channels. The name of the RFWS file specifies the reference channel that it configures.
 For other reference channels not supplied as examples, you may find it helpful to modify
 the parameters of the closest available RFWS file.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=creating-pulse-waveform.html language=enus -->
## TOPIC 00039: Creating a Pulse Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `creating-pulse-waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/creating-pulse-waveform.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a Pulse waveform, you must complete the following steps: Select Modulation from the drop-down menu. Select Pulse to display the generation settings window. This opens the Pulse window, which has tabs for Modulation, Pattern, IQ Impairments, and Graphics settings. These tabs provide the sam

### Creating a Pulse Waveform

To create a Pulse waveform, you must complete the following steps:

1. Select Modulation from the drop-down menu.
2. Select Pulse to display the generation settings window. This
 opens the Pulse window, which has tabs for Modulation,
 Pattern, IQ Impairments, and Graphics settings. These tabs provide the same
 functionality as other modulations.

Parent topic:

Pulse

<!--NI_TOPIC bundle=rfmx-waveform-creator path=crest-factor-reduction.html language=enus -->
## TOPIC 00040: Applying Crest Factor Reduction

- bundle_id: `rfmx-waveform-creator`
- source_path: `crest-factor-reduction.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/crest-factor-reduction.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Crest factor reduction (CFR) is a technique to reduce the peak to average power ratio (PAPR) of a waveform to a desired value. The CFR techniques can be used in conjunction with digital predistortion to improve the overall linearization of the predistorter and power amplifier system. CFR Methods RFW

### Applying Crest Factor Reduction

Crest factor reduction (CFR) is a technique to reduce the peak to average power ratio
 (PAPR) of a waveform to a desired value. The CFR techniques can be used in conjunction
 with digital predistortion to improve the overall linearization of the predistorter and
 power amplifier system.

#### CFR Methods

RFWC supports two CFR methods namely Clipping and
 Peak Windowing.

##### Clipping by Level

- If the clipping type is Circle , the overall IQ Vector
 will be clipped to the percentage specified.
- If the clipping type is Square , the I and Q values
 will be individually clipped to the percentage specified.

##### Clipping by Target PAPR

This method hard clips the signal to
 achieve the target PAPR. The following figure shows how the PAPR of a signal can be
 reduced by using clipping by Target PAPR.[IMAGE alt='image' src='GUID-2EE1A753-9658-404E-B419-448BAD8951F9-a5.png']

Clipping
 operation can be expressed as:[IMAGE alt='image' src='GUID-80E2066F-6E69-47B2-851A-F70CB8E9BADB-a5.png']

- X[n] is the signal on which CFR is applied
- X clipping [n] is the clipped signal
- A is the threshold level determined by target PAPR

The clipping transfer function is represented by the following
 figure.[IMAGE alt='image' src='GUID-9A1955E3-B14C-4B3A-92DC-BE734842749B-a5.png']

##### Peak Windowing

1. Detect peaks above the threshold, A, determined by the target PAPR. Samples
 above the threshold, in the vicinity of the detected peaks are referred to
 as the peak region.
2. Scale all the peak regions with a weighted window function such that the
 resultant peaks are equal to the threshold level, A. The window type and
 maximum window length are user configurable.

The following figure shows the input signal, the threshold level, and
 the signal obtained after applying the Peak Windowing method of CFR.[IMAGE alt='image' src='GUID-CBFCA079-C4F4-494D-8F8F-37D03AD76BC9-a5.png']

##### CFR with Filtering

CFR is a non-linear operation that introduces
 out-of-band distortion in the signal. This distortion can be filtered out after the
 CFR operation.

CFR with filter can be applied on the waveform by enabling
 filter. The block diagram below shows one iteration of CFR operation with
 filtering.[IMAGE alt='image' src='GUID-6FE57529-6947-4168-A8BC-FD95853BF937-a5.png']

CFR applies filtering per sub Block. The diagram below shows an example of
 sub block configuration for a signal sampled at S samples per second.[IMAGE alt='image' src='GUID-7C49DA83-5677-4C08-B849-F184B4FE931F-a5.png']

##### Guidelines for Using CFR

| CFR method | Usage |
| --- | --- |
| Clipping | Faster CFR Trade-off ACP for EVM |
| Peak Windowing | Trade Off between ACP and EVM |

NI recommends the Clipping method with filter enabled
 to obtain waveform with desired PAPR.

NI also recommends to set the
 oversampling factor to 4x or more of sampling rate whenever CFR is
 enabled.

For more concept help refer to Crest Factor
 Reduction topic in RFmx SpecAn Help.

##### References

- [1] Sperlich, Roland, et al. Power amplifier linearization with
 digital pre-distortion and crest factor reduction. Microwave Symposium
 Digest, 2004 IEEE MTT-S International. Vol. 2. IEEE, 2004.
- [2] Braithwaite, R. Neil. A combined approach to digital
 predistortion and crest factor reduction for the linearization of an RF
 power amplifier. IEEE Transactions on Microwave Theory and Techniques 61.1
 (2013): 291-302.
- [3] Armstrong, Jean. Peak-to-average power reduction for OFDM by
 repeated clipping and frequency domain filtering. Electronics letters 38.5
 (2002): 246-247.

#### CFR Configurations

The following controls are available in CFR tab.

CFR Apply: Specifies whether to apply crest factor reduction
 (CFR).

Note

- CFR is applied per carrier set.

CFR Method: Specifies the method used to perform CFR when you
 select the CFR Apply checkbox. RFmx Waveform Creator supports two
 CFR methods, Clipping and Peak Windowing. The default value is
 Clipping.

##### Clipping

When the Clip
 Using control is set to Level, the I and Q
 values of a waveform are clipped.

[IMAGE alt='image' src='GUID-C7A17B30-93FC-483F-8D91-DBD0F617A486-a5.png']

With clipping enabled, the I and Q values will be clipped
 depending on the settings specified.

- If the clipping type is Circle , the overall IQ Vector
 will be clipped to the percentage specified.
- If the clipping type is Square , the I and Q values will
 be individually clipped to the percentage specified.

There is an option to apply the clipping parameters before filtering has been
 applied, or after.

Note

- Applying clip using level behavior is the same as applying the clipping
 function under IQ Impairments tab.

When the Clip Using control is set to Target
 PAPR, the signal is hard clipped such that the target PAPR is
 achieved.

[IMAGE alt='image' src='GUID-CEAF314A-EA00-40E0-A339-23231668D4C4-a5.png']

Target PAPR: Specifies the target
 peak-to-average power ratio when you select the CFR Apply
 checkbox. This value is expressed in dB. The default value is 8.00 dB. Valid values
 are 1 dB to 100 dB.

Max Iterations: Specifies the
 maximum number of iterations allowed to converge waveform PAPR to target PAPR, when
 you select the CFR Apply checkbox. The default value is 10.
 Valid values are 1 to 1000.

Filter Enabled: Specifies
 whether to enable the filtering operation when you select the CFR
 Apply checkbox. The default value is
 Disabled.

Note

When using the Multi Carrier modulation scheme, a CFR filter
 is applied to each input waveform (carrier). Frequency Offset and Bandwidth can also
 be specified for each carrier.

##### Peak
 Windowing

Peak windowing scales the peaks in the signal using weighted
 window function to get smooth peaks and achieve the target PAPR.

[IMAGE alt='image' src='GUID-CBFCA079-C4F4-494D-8F8F-37D03AD76BC9-a5.png']

Window Type: Specifies the window type to
 be used when you select the CFR Apply checkbox and set
 CFR Method control to Peak
 Windowing. The default value is Kaiser-Bessel
 Window. Select from the following options:

- Flat Top Window - Uses the flat top window function to
 scale peaks.
- Hanning Window - Uses the Hanning window function to
 scale peaks.
- Hamming Window - Uses the Hamming window function to
 scale peaks.
- Gaussian Window - Uses the Gaussian window function to
 scale peaks.
- Blackman Window - Uses the Blackman window function to
 scale peaks.
- Blackman Harris Window - Uses the Blackman-Harris window
 function to scale peaks.
- Kaiser Bessel Window - Uses the Kaiser Bessel window
 function to scale peaks.

Window Length: Specifies the maximum window length to be
 used when you select the CFR Apply checkbox and set
 CFR Method control to Peak
 Windowing. The default value is 10. Valid values are 1 to
 1024.

<!--NI_TOPIC bundle=rfmx-waveform-creator path=dedicated-physical-channel.html language=enus -->
## TOPIC 00041: Dedicated Physical Channel

- bundle_id: `rfmx-waveform-creator`
- source_path: `dedicated-physical-channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/dedicated-physical-channel.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The possible combinations of DPCHs configured simultaneously for a user equipment (UE) in addition to the DPCCH are specified in the following table. The transmission of the HS-DPCCH can be on either I or Q branches. It depends on the total number of DPDCHs to be transmitted (N[max-dpch]). Once the

### Dedicated Physical Channel

The possible combinations of DPCHs configured simultaneously for a user equipment (UE) in
 addition to the DPCCH are specified in the following table.

[IMAGE alt='image' src='GUID-3C759A1F-F986-47D5-A764-FC68384DEEFD-a5.gif']

The transmission of the HS-DPCCH can be on either I or Q branches. It depends on the
 total number of DPDCHs to be transmitted (N<sub>max-dpch</sub>). Once the channels have
 been spread with the correct spreading code and summed, the I and Q branches are
 scrambled with a UE-specific complex scrambling code, S<sub>dpch,n</sub>.

The powers of the DPCHs can be adjusted by gain factors β<sub>c</sub>, β<sub>d</sub>, and
 β<sub>hs</sub>. The channel-dependent spreading codes are the orthogonal variable
 spreading factor (OVSF) codes that preserve the orthogonality between channels of
 different rates and spreading factors. OVSFs are defined using a code tree as shown in
 the following figure. The code is given as C<sub>SF,code number</sub> where SF is
 spreading factor.

[IMAGE alt='image' src='GUID-98F4B2DA-9BC4-4FB6-8953-4FF2FA855E57-a5.gif']

Channel Code Assignments

The following conditions apply for DPCCH, DPDCHs, HS-DPCCH, E-DPCCH, and E-DPDCHs.

- The DPCCH is always spread by the code c c = C 256,0 .
- The HS-DPCCH is spread by code c hs as given in the following table.
- 
- When only one DPDCH is to be transmitted, DPDCH 1 is spread by code
 C SF,k where SF is the spreading factor of DPDCH 1 and k =
 SF/4.
- When more than one DPDCH is to be transmitted, all DPDCHs have a spreading factor
 equal to 4. DPDCH n is spread by C 4,k where
 k = 1 if n ∈ {1, 2}, k = 3 if
 n ∈ {3, 4}, and k = 2 if
 n ∈ {5, 6}.
- The E-DPCCH is always spread to chip rate with the code c c =
 C 256,1 .
- The E-DPDCH(s) is spread to chip rate by the codes c hs as given in the
 following table.

[IMAGE alt='image' src='GUID-0E21AD33-FD49-4190-B9CB-B123448F1F81-a5.gif']

Scrambling Type

There are two types of scrambling code: Long Scrambling Code and Short Scrambling
 Code.

Long Scrambling Code: This complex code is derived from a gold
 sequence that is generated by two generator polynomials of degree 25 as shown in the
 following figure. The seed value for one of the polynomials determines the code
 sequence (scrambling code number) that is to be generated. Although the code
 sequence will repeat every 2<sup>25</sup>-1 chips, the 3GPP FDD specification
 requires the sequence to repeat every frame (10 ms), which at 3.84 Mbits/sec is
 38400 chips.

[IMAGE alt='image' src='GUID-A685C4ED-27B0-49AA-8107-CAA7445E40DF-a5.gif']

Short Scrambling Code: The short scrambling code is generated
 as shown in the following figure.

[IMAGE alt='image' src='GUID-214FD070-2107-40A2-A81D-45A37C830480-a5.gif']

The mapping function, termed mapper in the preceding figure, is given in the
 following table. The generators are stalled for one chip period when the
 256<sup>th</sup> chip is generated. This means that chip 0 and 255 are equal,
 i.e. z<sub>v</sub>(255) = z<sub>v</sub>(0).

[IMAGE alt='image' src='GUID-0EC10A04-1C23-48BB-8E2E-110667FF48BC-a5.gif']

The seed values for the three generators are obtained from the user number or code
 number.

Scrambling Code: The valid range for this number is 0 to
 2<sup>24</sup>-1.

Slot Format for DPCCH: The dedicated uplink physical channel has a
 frame structure as shown in following figure. DPDCH consists of data only. Each frame is
 10 ms long and it is split into 15 slots. The DPDCH and DPCCH are always frame-aligned
 with each other.

[IMAGE alt='image' src='GUID-7A6FED24-292F-4E2F-9FE4-4C20EE4D3834-a5.gif']

The control channel consists of four fields: N<sub>pilot</sub>, N<sub>TFCI</sub>,
 N<sub>FBI</sub>, and N<sub>TPC</sub>. The spreading factor is always 256 and there
 are always 10 bits per slot. The bit values and number of bits assigned to the fields
 are dependent upon a slot format. The formats supported by are given in the following
 table.

[IMAGE alt='image' src='GUID-3F60150D-7573-44C0-A59E-CCCE73EACD8B-a5.gif']

The FBI bits are used to support feedback from mobile to base station. The TFCI
 (Transport Format Combination Indicator) field is used to obtain a 30-bit pattern. The
 pattern is calculated from a 10-bit TFCI index value. The TPC field contains the power
 control command. The bit pattern and associated power control commands are given in the
 following table.

If you select slot format 0 (or 2), when compressed mode is enabled, the choice between
 3GPP slot formats 0A and 0B (or 2A and 2B) is made based on the number of slots
 transmitted in a frame, which are derived from the transmission gap parameters.

Note

[IMAGE alt='image' src='GUID-DCB8D707-7470-4F7C-9EB0-713B6D2EA44A-a5.gif']

The FBI and TPC patterns are binary values. The edit box does not allow you to other
 numbers. The TFCI pattern is calculated from the TFCI index. This is a decimal value
 between 0 and 1023.

The pilot bit patterns are fixed in and are as defined in the following tables.

[IMAGE alt='image' src='GUID-36F6E44D-7FEE-4890-874E-F26700D4D1AB-a5.gif']

Pilot bit patterns for N<sub>pilot</sub> = 3, 4, 5, and 6

[IMAGE alt='image' src='GUID-D870F1EA-9CCB-4412-980B-15B0845DEFE3-a5.gif']

Pilot bit patterns for N<sub>pilot</sub> = 7 and 8

High Speed Dedicated Physical Control Channel (HS-DPCCH)

The HS-DPCCH carries uplink feedback signaling related to a downlink HS-DSCH
 transmission. The HS-DSCH related feedback signaling consists of hybrid-ARQ
 acknowledgement (HARQ-ACK) and channel-quality indication (CQI). The subframe structure
 of length 2 ms (3 x 2560 chips) consists of three slots, each of 2560 chips as shown in
 the following figure. The HARQ-ACK is carried in the first slot of the HS-DPCCH
 sub-frame. The CQI and in case the UE is configured in MIMO mode also the PCI, are
 carried in the second and third slot of a HS-DPCCH sub-frame. of the HS-DPCCH subframe
 according to the HS-PDSCH mode. There is at most one HS-DPCCH on each radio link, which
 can only exist together with an uplink DPCCH.

[IMAGE alt='image' src='GUID-A492C972-54BA-4590-AB01-6251B841AFD5-a5.gif']

The spreading factor of the HS-DPCCH is 256. i.e. there are 10 bits per uplink HS-DPCCH
 slot. The slot format for uplink HS-DPCCH is defined in following table.

Editing Channel Parameters

DPCCH Channel

You can select the DPCCH slot format from drop-down list. The available slot formats are
 0 to 6. The selection of slot format automatically enables or disables the TFCI and FBI
 edit boxes. The valid power range is -60 dB to 0 dB. Refer to following table for all
 other DPCCH parameters valid values/ranges.

[IMAGE alt='image' src='GUID-6115326F-EB11-4432-A67B-4155B8A8FEA2-a5.gif']

E-DPCCH Channel

This control channel is available only when the channel configuration is either Case 2 or
 Case 3.

Power: specifies the channel power level. The valid values are
 from –60 to 0 dB.

HS-DPCCH Channel

You can add HS-DPCCH channel in uplink DPCH by selecting the Channel
 State checkbox. Few settings and valid values of available parameters
 depend on the type of HS-PDSCH mode. Refer the following table for the HS-DPCCH
 parameters valid values/ranges. The sequence transmission in this table is according to
 Table 15 of section 4.7.2.1, Table 15B of section 4.7.3.1, and Table 15D of section
 4.7.3A.1 of ts_125212v080800p.

[IMAGE alt='image' src='GUID-D8762878-BB30-48C1-9ED6-232E434CA9CA-a5.gif']

Channel Configuration: Case 1

The data is transmitted exclusively on DPDCHs.

Symbol Rate: The number of DPDCH channels is dependent upon the
 total symbol rate. For example, a symbol rate of 1920 ksps results in two DPDCH
 channels. The valid symbol rates are 0, 15, 30, 60, 120, 240, 480, 960, 1920, 2880,
 3840, 4800, 5760 ksps. When the symbol rate is set to 0, neither data channel is
 displayed on the table nor transmitted.

SF: Specifies the spreading factor and cannot be edited.

Channel Code: Specifies the channel code and cannot be edited.

Power: Specifies the channel power. The valid power level rage is
 -60 to 0 dB.

Data Source: Specifies date source. The type of data source can
 also be changed.

Channel Configuration: Case 2

The data is transmitted on DPDCHs and/or E-DPDCHs.

SF: Specifies the spreading factor and cannot be edited.

Channel Code: Specifies the channel code and cannot be edited.

Power: Specifies the channel power. The valid power level rage is
 -60 to 0 dB.

Data Source: Specifies date source. Refer to Selecting the Data
 Source topic for more information on data source.

The following table shows the available symbol rates for the DPDCH and E-DPDCH(s). When
 the symbol rate for either of these channels is set to 0, all controls for the channel
 are disabled and the channel is not transmitted.

[IMAGE alt='image' src='GUID-EFD97B80-F6F2-41FF-AF99-F60BA6140936-a5.gif']

Channel Configuration: Case 3

The data is transmitted exclusively on E-DPDCHs.

Symbol Rate: The number of E-DPDCH channels is dependent upon the
 total symbol rate. For example, a symbol rate of 1920 ksps results in two E-DCH
 channels. The valid symbol rates are 0, 15, 30, 60, 120, 240, 480, 960, 1920, 3840, and
 5760 ksps. When the symbol rate is 0, neither data channel is displayed on the table nor
 transmitted.

SF: Specifies the spreading factor and cannot be edited.

Channel Code: Specifies the channel code and cannot be edited.

Power: Specifies the channel power. The valid power level rage is
 -60 to 0 dB.

Data Source: Specifies date source. Refer to Selecting the Data
 Source topic for more information on data source.

Modulation scheme: Specifies the modulation scheme used in the
 E-DPDCH channels for the rate.

Parent topic:

WCDMA (3GPP FDD Release 8)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=default-modulation-mappings.html language=enus -->
## TOPIC 00042: Default Modulation Mappings

- bundle_id: `rfmx-waveform-creator`
- source_path: `default-modulation-mappings.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/default-modulation-mappings.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Modulation mappings that are implemented by RFmx Waveform Creator and how you can modify them. In general, Gray coding is applied to the modulation mappings. 7 BPSK, DBPSK Modulation Mapping BPSK and DBPSK Modulation Mapping 8 π/2 DBPSK Modulation Mapping π/2 DBPSK Modulation Mapping 9 QPSK, DQPSK,

### Default Modulation Mappings

Modulation mappings that are implemented by RFmx Waveform Creator and how you can
 modify them.

In general, Gray coding is applied to the modulation mappings.

Figure 7.

[IMAGE alt='BPSK and DBPSK Modulation Mapping' src='GUID-F2D412E6-F516-43DD-A451-71E714E4DFBC-a5.gif']

Figure 8.

[IMAGE alt='π/2 DBPSK Modulation Mapping' src='GUID-21DE3E90-5192-4817-B328-031BF68C3684-a5.gif']

Figure 9.

[IMAGE alt='QPSK, DQPSK, π / 4 DQPSK, OQPSK Modulation Mapping' src='GUID-49486237-A725-4DA6-8923-AE9E8A052178-a5.gif']

Figure 10.

[IMAGE alt='8PSK, D8PSK Modulation Mapping' src='GUID-11E7BCBB-AECE-427F-BBC9-52FA9B424EE0-a5.gif']

Figure 11.

[IMAGE alt='π/8 D8PSK Modulation Mapping' src='GUID-3047A6CA-BA77-4495-B79E-8135AEC36037-a5.gif']

Figure 12.

[IMAGE alt='3π / 8 8PSK (EDGE) Modulation Mapping' src='GUID-616EEC8C-9F6A-47B7-BE68-7224E85B1D3A-a5.gif']

Note

Figure 13.

[IMAGE alt='16PSK Modulation Mapping' src='GUID-F5E53942-4494-4E41-AB23-8BF6541C589C-a5.gif']

Figure 14.

[IMAGE alt='2FSK Modulation Mapping' src='GUID-4B787C80-4C18-4C50-8D87-4E41C6FF4E15-a5.gif']

Figure 15.

[IMAGE alt='4FSK Modulation Mapping' src='GUID-49A6C689-C483-4270-9AA3-8B4DF83093F9-a5.gif']

Note

Figure 16.

[IMAGE alt='16-QAM Modulation Mapping' src='GUID-21A8442B-DDAC-4310-98F2-12D35041D0B0-a5.gif']

Figure 17.

[IMAGE alt='32-QAM Modulation Mapping' src='GUID-FAB3EDA8-AE24-4F05-80D4-CC43E9F8CCD6-a5.gif']

Figure 18.

[IMAGE alt='64-QAM Modulation Mapping' src='GUID-D204D361-DCF9-4B0D-B66F-AAFEA120B9C9-a5.gif']

Figure 19.

[IMAGE alt='128-QAM Modulation Mapping' src='GUID-CF0980FF-E34A-401D-8A0C-6B5631B516A4-a5.gif']

Figure 20.

[IMAGE alt='256-QAM Modulation Mapping' src='GUID-2013BAE6-DD24-4115-89DE-7174BC60540B-a5.gif']

Figure 21.

[IMAGE alt='512-QAM Modulation Mapping' src='GUID-AFCD531A-18D6-499F-A03C-828BE6E0854D-a5.gif']

Figure 22.

[IMAGE alt='1024-QAM Modulation Mapping' src='GUID-CC6AA811-5F3E-4AFF-B5AE-33AAB6ACDAF5-a5.gif']

Figure 23.

[IMAGE alt='4096-QAM Modulation Mapping' src='GUID-FC3D915F-3C19-497D-872D-E5772C16B8D4-a5.gif']

#### 16-APSK
 Modulation

The following equations apply to the 16-APSK constellation
 comprising 4 inner-ring symbols and 12 outer-ring symbols.

4

R

1

2

+

12

R

2

2

=

16

- R 1 is radii of the inner constellation ring
- R 2 is radii of the outer constellation ring

The ring ratio is defined with the following equation:

Y

=

R

2

/

R

1

Figure 24.

[IMAGE alt='Plot showing 16-APSK Constellation Mapping' src='GUID-6905B5D6-F8E1-4C2C-B5BF-6933D965A233-a5.svg']

Figure 25.

[IMAGE alt='16-APSK Modulation Symbol Mapping' src='GUID-47417C8A-AA8A-41E7-8599-C3E5ADCC08DB-a5.png']

#### 32-ASPK
 Modulation

The following equations apply to the 32-APSK constellation
 comprising 4 inner-ring symbols, 12 middle-ring symbols, and 16 outer-ring
 symbols.

4

R

1

2

+

12

R

2

2

+

16

R

3

2

=

32

- R 1 is radii of the inner constellation ring
- R 2 is radii of the moddle constellation ring
- R 3 is radii of the outer constellation ring

The ring ratio is defined with the following equations:

Y

1

=

R

2

/

R

1

Y

2

=

R

3

/

R

1

Figure 26.

[IMAGE alt='Plot showing 32-APSK Constellation Mapping' src='GUID-AFDEDEBB-3EE5-4063-A505-0521CDB60F91-a5.svg']

Figure 27.

[IMAGE alt='32-APSK Modulation Symbol Mapping' src='GUID-DC494D1B-7A92-4C4B-931B-FA87DEC297D5-a5.png']

Parent topic:

RFmx Waveform Creator Modulation Schemes

Related concepts:

- RFmx Waveform Creator 2026 Q2 Changes

<!--NI_TOPIC bundle=rfmx-waveform-creator path=dirty-transmitter.html language=enus -->
## TOPIC 00043: Dirty Transmitter

- bundle_id: `rfmx-waveform-creator`
- source_path: `dirty-transmitter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/dirty-transmitter.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Bluetooth® test specification document specifies the use of a non-ideal, or "dirty", transmitter, as a signal source for performing the receiver sensitivity tests. The dirty transmitter test parameters for basic Bluetooth packets are defined in Table 4.3 and Table 4.4 of the Bluetooth Test Speci

### Dirty Transmitter

The Bluetooth® test specification document specifies the use of a non-ideal, or "dirty",
 transmitter, as a signal source for performing the receiver sensitivity tests. The dirty
 transmitter test parameters for basic Bluetooth packets are defined in Table 4.3 and Table 4.4 of
 the Bluetooth Test Specification, RF.TS.p33 for singleslot and multislot
 packets. The dirty transmitter test parameters for enhanced data rate (EDR) packets defined in
 Table 4.8 of the Bluetooth Test Specification RF.TS.p33. The dirty transmitter
 test parameters for low energy (LE) packets are defined in the following tables:

- Table 6.2 of the
 Bluetooth Test Specification 4.0.0
- Table 4.2 of
 Bluetooth Test Specification 4.2.0/4.2.2/4.2.3
- Table 4.2, Table 4.6, Table 4.7, Table 4.10, and Table 4.11 of
 Bluetooth Test Specification 5.0.0
- Table 4.17 of Bluetooth Test Specification RFPHY.TS.p23

- The Standard mode applies all the standard dirty transmitter
 parameters.
- The User Defined mode applies only the dirty transmitter parameters
 that are specified by the user.
- The Frequency Drift mode applies only the standard-defined frequency
 drift parameters for LE HDT packets.

#### Standard Mode

Let
 c
 be the number of consecutive packets per impairment set,
 p
 be the number of impairment sets, and
 u
 be the number of unique packets. The toolkit transmits the first
 c
 packets using the first impairment set, the next
 c
 packets using the second impairment set, and so on, until it uses the
 p
 <sup>th</sup>
 impairment set. If
 u
 >=
 c
 *
 p
 , this process is repeated until
 u
 packets are generated. If
 u
 <
 c
 *
 p
 , this process is repeated until
 u
 * (ceil(
 c
 *
 p
 /
 u
 )) packets are generated. After this, the toolkit periodically repeats the generation of these packets.

Note

#### User Defined Mode

Use this mode to test the dirty transmitter for limited parameter sets. The following example is based on the number of unique packets, and the number of enabled dirty transmitter parameter sets.

Let
 x
 be the number of unique packets and
 y
 be the Dirty Tx Enabled Parameters Set [] enabled values in the array, then
 x = w * y + z
 , so each enabled parameter set is repeated
 w
 times, and the first set is repeated
 z
 times after
 w * y
 packets are generated.

Case one:
 z = 0
 , each enabled set is repeated
 w
 times, and the number of unique packets are exact multiples of the number of Dirty Tx Enabled Parameters Set [] size.

Case two:
 z â‰  0
 , each set is repeated
 w
 times and the first enabled set is repeated
 z
 (remainder) times after
 w * y
 packets are generated.

If the number of unique packets is less than the number of enabled parameter set size, x <
 y
 , the first enabled parameter set is repeated x times.

#### Frequency Drift Mode

This mode tests the dirty transmitter using standard-defined parameters related to frequency drift, such as frequency deviation and modulating frequency. It is applicable only to Low Energy HDT (LE-HDT) packets. In this mode, only frequency drift parameters are considered; all other dirty transmitter parameter settings are ignored.

#### Bluetooth Basic Rate

For singleslot packets, the dirty transmitter superimposes a synchronized sine wave frequency
 modulation (alternate packets switch phase between 0 and 180 degrees) with a deviation of Â±25
 kHz and a modulation frequency of 1.6 kHz to obtain the carrier frequency drift.

For
 multislot packets, the dirty transmitter superimposes a frequency modulation with a deviation of
 Â±40 kHz and a synchronized sine wave modulation frequency (alternate packets switch phase
 between 0 and 180 degrees) of 500 Hz for three slot packets and 300 Hz for five slot packets to
 obtain the carrier frequency drift.

(Applicable to Standard Mode only) According to the Bluetooth test
 specification RF.TS.p33, the dirty transmitter changes the carrier frequency offset, modulation
 index, and symbol timing error for each 20 ms duration. The toolkits ceils this 20 ms duration
 for each impairment set, to an integral number of consecutive packets ( c
 ). For example, for a 3-slot basic rate packet, the number of consecutive packets per impairment
 set, c , is calculated as c = 20 ms/(slot duration *
 3) = ceil (20 ms/(625 * 3 microseconds)) = 11. Thus, for 1-, 3-, or 5- slot packets, the toolkit
 uses each impairment set for 32, 11, or 7 consecutive packets ( c ). The
 test specification defines 10 impairment sets ( p ) for basic rate packets.

#### Bluetooth EDR

The dirty transmitter superimposes a frequency modulation with a deviation of Â±10 kHz and a
 synchronized sine wave modulation period of 100 microseconds onto the signal, starting at the
 beginning of the differential phase-shift keying (DPSK) synchronization word, to obtain the
 worst-case transmitter carrier frequency stability. The frequency modulation alternately
 switches phase between 0 and 180 degrees for successive packets.

(Applicable to Standard Mode only) According to the Bluetooth test
 specification RF.TS.p33, the dirty transmitter changes the carrier frequency offset, modulation
 index, and symbol timing error for every 20 packets ( c ), and it defines 3
 impairment sets ( p ) for Bluetooth EDR packets.

#### Bluetooth Low Energy

The dirty transmitter obtains a frequency drift over time by using frequency modulation with
 a deviation of Â±50 kHz and a sinusoidal signal with a modulation frequency of 1250 Hz. The
 modulating signal is synchronized with the packets so that each alternating packet starts at 0
 and 180 degrees of the modulating signal.

(Applicable to Standard Mode only) According to Bluetooth Test
 Specification RFPHY.TS.p23 , the dirty transmitter changes the carrier frequency
 offset, modulation index, and symbol timing error for every 50 packets ( c
 ), and it defines 10 impairment sets ( p ) for Bluetooth low energy
 packets. The test specification defines different sets of modulation index values for standard
 and stable modulation index types.

#### Bluetooth Low Energy - High Data Throughput

The
 dirty transmitter obtains a frequency drift over time by using frequency modulation with a
 deviation from the following table and a sinusoidal signal with a modulation frequency of 318
 Hz. The modulating signal is synchronized with the packets so that each alternating packet
 starts at 0 and 180 degrees of the modulating signal.

| Rate | Maximum Drift (kHz) |
| --- | --- |
| HDT2 | ±2 |
| HDT3 | ±2 |
| HDT4 | ±1 |
| HDT6 | ±1 |
| HDT7.5 | ±1 |

Note

| Test Run | Carrier Frequency Offset | Symbol Timing Error |
| --- | --- | --- |
| 1 | 100 kHz | -50 ppm |
| 2 | 19 kHz | -50 ppm |
| 3 | -3 kHz | +50 ppm |
| 4 | 1 kHz | +50 ppm |
| 5 | 52 kHz | +50 ppm |
| 6 | 0 kHz | -50 ppm |
| 7 | -56 kHz | -50 ppm |
| 8 | 97 kHz | -50 ppm |
| 9 | -25 kHz | -50 ppm |
| 10 | -100 kHz | +50 ppm |

Parent topic:

Bluetooth

<!--NI_TOPIC bundle=rfmx-waveform-creator path=downlink-configuration-overview.html language=enus -->
## TOPIC 00044: Downlink Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `downlink-configuration-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/downlink-configuration-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Downlink Configuration tab allows you to control the downlink signal. This tab comprises two parts: Downlink Configuration Downlink Channels The Downlink Configuration tab is disabled when the Link Direction is set to Uplink or Sidelink.

### Downlink Configuration

- Downlink Configuration
- Downlink Channels

Note

Link Direction

Uplink

Sidelink

- [Mode: LTE](mode-lte-downlink.html) Downlink configuration options for LTE (Long-Term Evolution) transmissions.
- [Mode: NB-IoT](mode-nb-iot-downlink.html) Downlink configuration options for narrow band internet of things (NB-IoT) transmissions.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=downlink-configuration.html language=enus -->
## TOPIC 00045: Downlink Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `downlink-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/downlink-configuration.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This tab allows you to configure the downlink signal. It comprises of two tabs - Downlink Configuration and Downlink Channels. Downlink Configuration is for overall configuration of the downlink signal and Downlink Channel Configuration is for modifying the transmitted downlink channels. The followi

### Downlink Configuration

This tab allows you to configure the downlink signal. It comprises of two tabs - Downlink
 Configuration and Downlink Channels.

Downlink Configuration is for overall configuration of the downlink signal and Downlink
 Channel Configuration is for modifying the transmitted downlink channels.

The following changes are needed in the Downlink Channel Configuration tab.

HS-PDSCH Mode

The HS-PDSCH mode of operation can be set to either SISIO/Diversity or MIMO. Default
 value is SISO/Diversity.

The Precoding Pattern, the Slot Format 2,
 and the Stream 2 Data Source parameters are visible only when
 HS-PDSCH Mode is MIMO and
 Select Channel Type is HS-PDSCH.

For the downlink, the spreading and scrambling operation is the same for all channels
 except for the synchronization channel (SCH). The process is shown in the following
 figure. The modulation scheme is QPSK for all channels except SCH, which consists of a
 sequence of real-valued symbols and the HS-DSCH. The HS-DSCH uses both QPSK, 16 QAM, and
 64 QAM. The symbols can take the values + 1, - 1, and 0, where 0 indicates DTX.

For channels using QPSK, each pair of two consecutive symbols is mapped to an I and a Q
 branch in a serial to parallel manner. The modulation mapper is such that even- and
 odd-numbered symbols are mapped to the I and Q branch respectively. The I and Q branches
 are then spread to the chip rate using a channelization code C<sub>ch,SF,m</sub>. The
 real-valued sequences on the I and Q branches are then treated as complex pairs and
 scrambled with a complex code S<sub>dl,n</sub>.

For physical channels using 16QAM or 64 QAM, a set of consecutive symbols is
 serial-to-parallel converted and then mapped to 16QAM or 64QAM by a modulation mapper.
 The I and Q branches are both spread to the chip rate by the same real-valued
 channelization code C<sub>ch,16,m</sub>. The sequences of real-valued chips on the I and
 Q branch are treated as a single complex-valued sequence of chips. This sequence of
 chips from all multi-codes is summed and scrambled by a complex-valued scrambling code
 S<sub>dl,n</sub>.

Spreading and scrambling for all downlink channels except for SCH is as shown in the
 following figure.

[IMAGE alt='image' src='GUID-56D9DC0A-8333-471F-BC39-BA160AF424C2-a5.gif']

The different downlink channels are combined as shown in the following figure.

[IMAGE alt='image' src='GUID-C82CE3D2-F758-49FA-87AB-3DCEA807E575-a5.gif']

Channelization Codes

The channelization codes are same as the OVSF codes used in the uplink. The
 channelization code for the primary CPICH is fixed to C<sub>ch,256,0</sub> and the
 channelization code for the primary CCPCH is fixed to C<sub>ch,256,1</sub>. You control
 the channelization codes for all other channels.

Scrambling Code

A total of 2<sup>18</sup>-1 = 262143 scrambling codes, numbered from 0 to 262142, can be
 generated. However, only a subset of this number is used. The scrambling codes are
 divided into 512 sets, each containing a primary code and 15 secondary codes. The
 primary codes consist of codes n = 16i, where i = 0, 1 … 511. The set of secondary
 scrambling codes for the i<sup>th</sup> set is defined as 16i + k, where k = 1, 2 ...
 15.

The set of primary codes is further divided into 64 scrambling code groups, each
 consisting of eight primary scrambling codes. The j<sup>th</sup> scrambling code group
 consists of primary scrambling codes 16 * 8 * j + 16k, where j = 0, 1 … 63 and k = 0, 1
 … 7.

From the above, if we are given the primary code, we can obtain the secondary code by
 requesting a value 1, 2 … 15, We can also obtain the primary scrambling code group as
 [n/128]; where [] refers to the integer part and n is the code
 number.

The scrambling code sequences are constructed by combining two real sequences into a
 complex sequence. Each of the two real sequences is constructed as the position-wise
 modulo 2 sum of 38400 chip segments of two binary m-sequences
 generated by means of two generator polynomials of degree 18. The resulting sequences
 thus constitute segments of a set of Gold sequences. The scrambling codes are repeated
 for every 10 ms radio frame.

The following figure shows the implementation of the scrambling code.

[IMAGE alt='image' src='GUID-E526DADB-5013-4486-A5EF-BBAF24914E82-a5.gif']

Note

Synchronization Codes

The synchronization codes are generated only for the first 256 chips of each slot. The
 primary SCH is same for each slot which is same for every cell in the system. However,
 this is not the same for secondary SCH. The secondary SCH consists of repeatedly
 transmitting a length 15 sequence of modulated codes of length 256 chips. The secondary
 synchronous code is denoted as c<sub>s</sub><sup>i,k</sup> in the following figure where
 i = 0, 1 … 63 is the number of the primary scrambling code group,
 and k = 0, 1 … 14 is the slot number.

[IMAGE alt='image' src='GUID-B0BCCDFB-5FCC-4E77-B493-F9AD564F0F57-a5.gif']

The actual code generated in each slot is obtained from the following table, that
 associates slot number, primary code group. Code number is used to generate the SCH
 channel.

[IMAGE alt='image' src='GUID-8105F66F-595B-4B01-A047-64302779A0AB-a5.gif']

[IMAGE alt='image' src='GUID-BC57D23F-602B-4378-9137-0422098F1107-a5.gif']

Channel Structures

This section details the structure of each downlink channel.

Dedicated Downlink Physical Channel (DPCH)

The dedicated transport channel (DCH) is transmitted in time-multiplex with control
 information. The channel can be considered as time-multiplex of a downlink DPDCH and a
 downlink DPCCH. The following figure shows the frame structure of the downlink DPCH.

[IMAGE alt='image' src='GUID-E44637BF-9439-49DB-B201-7BC0E8B7D284-a5.gif']

The number of bits in each field is dependent upon the slot format. More details are
 given in the following table.

[IMAGE alt='image' src='GUID-AE641D54-D93C-4A3C-B50C-5E84A4DB7570-a5.gif']

*If TFCI bits are not used, then DTX is used in the TFCI field

The TFCI bits are calculated from a TFCI index. The pilot bit patterns for downlink DPCCH
 are given for information in the following table.

If compressed mode is used, Waveform creator takes the user-supplied slot format,
 compares this with other compressed mode parameters set by the user, and automatically
 applies the slot format as specified in the 3GPP FDD standards.

[IMAGE alt='image' src='GUID-A6357D1A-A665-4436-B0DF-C10568703551-a5.gif']

The relationship between power control and TPC bits is given in the following table.

[IMAGE alt='image' src='GUID-48B96C49-3EE1-43D2-92F6-E023651545E8-a5.gif']

Multicode transmission may be employed in the downlink. In other words, when multiple
 DPCHs are sent to one mobile. In such cases, control information is transmitted only on
 the first downlink DPCH and DTX bits are transmitted during the corresponding time
 period for the additional downlink DPCHs as depicted in the following figure.

[IMAGE alt='image' src='GUID-84064C0D-57E0-4886-9AD3-72C7BEC4E174-a5.gif']

E-DCH Relative Grant Channel (E-RGCH)

The E-RGCH is a fixed rate (30 kbps, SF = 128) dedicated downlink physical channel
 carrying the uplink E-DCH relative grants. The following figure illustrates the
 structure of the E-RGCH. A relative grant is transmitted using 3, 12, or 15 consecutive
 slots and in each slot a sequence of 40 ternary values is transmitted.

[IMAGE alt='image' src='GUID-D54CF9CF-3930-4A79-9CC1-AE36C1F20199-a5.gif']

E-DCH Hybrid ARQ Indicator Channel (E-HICH)

The E-HICH is a fixed rate (30 kbps, SF = 128) dedicated downlink physical channel
 carrying the uplink E-DCH hybrid ARQ acknowledgement indicator. The preceding figure
 illustrates the structure of the E-HICH. A hybrid ARQ acknowledgement indicator is
 transmitted using 3 or 12 consecutive slots and in each slot a sequence of 40 ternary
 values is transmitted.

Fractional Dedicated Physical Channel (F-DPCH)

The F-PDCH is a fixed rate (3 kbps, SF = 256) downlink physical channel that carries 2
 TPC bits per slot. The slot format is depicted in the following figure.

[IMAGE alt='image' src='GUID-44871C0D-1811-4769-9B12-86F5DA75ADA2-a5.gif']

In each slot, the location of the TPC bits is given by the slot format for F-DPCH as
 detailed in the following figure.

[IMAGE alt='image' src='GUID-94EB2B8A-80A6-4FEE-8B14-5B2F6C2412DE-a5.gif']

Common Pilot Channel (CPICH)

The CPICH is a fixed rate (30 kbps, SF = 256) downlink physical channel that carries a
 predefined bit/symbol sequence 1 + j. There are primary CPICH and secondary CPICH(s).
 There can be only one primary CPICH per cell. It is scrambled with the primary
 scrambling code and is spread with C<sub>ch,0,256</sub>. The secondary CPICH may be
 scrambled by either the primary or secondary scrambling code, there may be more than one
 per cell and an arbitrary channelization code with an SF of 256 can be used.

Primary Common Control Physical Channel (P-CCPCH)

The primary CCPCH is a fixed rate (30 kbps, SF = 256) downlink channel used to carry the
 BCH transport channel. The frame structure of this channel is shown in the following
 figure.

[IMAGE alt='image' src='GUID-B6270FC5-D73D-4F65-A650-2415B1919123-a5.gif']

Secondary Common Control Physical Channel (S-CCPCH)

The structure of the S-CCPCH is shown in the following figure. The set of possible rates
 is the same as for the DPCH.

[IMAGE alt='image' src='GUID-0CF4E83B-8B46-4BF8-93F1-D653152A23BE-a5.gif']

The number of bits associated with each field depends on the slot format. The slot format
 is automatically determined by.

Physical Downlink Shared Channel (PDSCH)

The frame and slot structure of the PDSCH is shown in the following figure.

[IMAGE alt='image' src='GUID-217CAEE7-E264-464C-9776-A817873583CD-a5.gif']

The allowed data rates for the PDSCH are 15 to 960 ksps (SF = 256-4).

Paging Indicator Channel (PICH)

The Paging Indicator Channel is a fixed rate (SF= 256) physical channel that is used to
 carry the paging indicators. The structure of the paging channel is shown in the
 following figure. In this figure, it is important to note that the last 12 bits of the
 frame are not transmitted. The first 288 bits are used for paging indication. In each
 frame N<sub>p</sub> indicators are sent where N<sub>p</sub> = 18, 36, 72, 144.

[IMAGE alt='image' src='GUID-878E767A-AD3E-4E25-876F-FFC7518B924F-a5.gif']

Fig. 2-27 Structure of the PICH

The paging indicators can be represented as patterns of zeros and ones, {P<sub>0</sub>,
 …P<sub>q</sub>, …, P<sub>Np-1</sub>}. converts the paging indicators to bits
 according to the 3GPP FDD standard.

High Speed Shared Control Channel (HS-SCCH)

The HS-SCCH is a fixed rate (60 kbps, SF=128) downlink physical channel used to carry
 downlink signaling related to High Speed Downlink Shared Channel (HS-DSCH) transmission.
 The frame and slot structure of the HS-SCCH is shown in the following figure.

[IMAGE alt='image' src='GUID-35ABE930-0F23-42FA-BD09-3E838548B11F-a5.gif']

High Speed Physical Downlink Shared Channel (HS-PDSCH)

The High Speed Physical Downlink Shared Channel (HS- PDSCH) is used to carry the High
 Speed Downlink Shared Channel (HS-DSCH).

A HS-PDSCH corresponds to one channelization code of fixed spreading factor SF=16 from
 the set of channelization codes reserved for HS-DSCH transmission. The HS-PDSCH does not
 carry any Layer 1 information; this is transmitted in the associated HS-SCCH.

The subframe and slot structure of the HS-PDSCH is shown in the following figure.

[IMAGE alt='image' src='GUID-8F13EFF2-D998-4BFD-89F7-E14309C0B7F7-a5.gif']

An HS-PDSCH may use QPSK or 16QAM modulation symbols. In the above figure, M is the
 number of bits per modulation symbol; i.e. M=2 for QPSK and M=4 for 16QAM. and M=6 for
 64QAM The slot formats are shown in the following table.

[IMAGE alt='image' src='GUID-11E9D80D-8920-403A-83A5-5CAF2E97C70B-a5.gif']

E-DCH Absolute Grant Channel (E-AGCH)

The E-AGCH is a fixed rate (15 kbps, SF = 256) downlink physical channel carrying the
 uplink E-DCH absolute grant. The following figure illustrates the E-AGCH structure.

[IMAGE alt='image' src='GUID-D6CFCAE4-6D3F-48F1-B22F-6B9203587B96-a5.gif']

Channel Timing Offset

To reduce the crest factor, some channels are offset in time with respect to others. The
 offset is given as number of 256 chips. All the channels are phase-referenced to the
 primary common control channel. That is the channels that are offset in time should
 delay the multiplexed data by the equivalent of n*256 chips before
 spreading and scrambling. The allowed range is 0 to 149. For the E-AGCH, there is a
 constant frame timing offset of 20 which is relative to the P-CCPCH frame timing.

Configuring the Downlink

This section lists the parameters and methods provided by to define a 3GPP FDD
 downlink.

Scrambling Code: To set the scrambling code, enter the required
 code value in the edit box. Valid values are 0 to 8191.

Scrambling Code Group: Waveform Creator automatically calculates
 the scrambling code group depending on Scrambling Code. You can
 edit this value to override the automatic selection.

Control to Data Gain: You can set the relative power level in dB
 between the data and control parts of a channel. The allowed range is 0 to -60 dB.

Number of PI Per FrameYou can set the number of paging indicators
 per frame by choosing a value from the Number of PI per Frame combo box. Available
 values are: 18, 36, 72, and 144.

Number of Antennas: Specifies the number of antennas. Valid values
 are 1 and 2. The number of output files is equal to this number of antennas.

Transmit Diversity for Non-HS Channels: This checkbox can be
 modified only if the Number of Antennas greater than 1. If
 selected, transmit diversity will be applied on all channels other than the high-speed
 channels (HS-SCCH and HS-PDSCH). HS-SCCH diversity is controlled by its own parameter.
 HS-PDSCH diversity is applied if its mode is SISO/Tx Diversity and the number of
 antennas is greater than 1.

The second output file may contain no data if Transmit Diversity for non-HS channels is
 not enabled and if HS-PDSCH and CPICH are not configured and (a) HS-SCCH is not
 configured or (b) if HS-SCCH Tx Diversity is not selected when HS-SCCH is
 configured.

Enabling Synchronization Channels: To use synchronization channels
 select the Use SCHs check box. This lets you enter the relative
 powers of primary and secondary channels. Valid values are between 0 and -60 dB.

TFCI Bits: If you wish to generate TFCI bits, select the Use TFCI
 Bits box.

Compressed Mode: Enables compressed mode. To configure compressed
 mode, press the Configure button. This presents you with the
 dialog box as shown in the following figure.

[IMAGE alt='image' src='GUID-EB676B07-EA5F-481B-8F39-48510247427B-a5.gif']

It is possible to select three compressed mode methods and the frame structure. The
 parameters within the block diagram should be filled in with reference to compressed
 mode.

Editing, Adding, and Removing Downlink Channels

You can add, delete, and edit channels to the downlink simulation. Waveform Creator
 provides a table to define the channels. The table always shows the primary and the
 secondary common pilot channels (P-CPICH, S-CPICH), the primary and the secondary common
 control channels (P-CCPCH, S-CCPCH), the PICH, the PDSCH, the E-AGCH, the E-RGCH, and
 the E-HICH.

The following parameters can be altered:

- Power levels for all channels — Valid values are –60 to dB.
- Timing offset — Valid values are 0 to 149. The timing offset for P-CPICH, S-CPICH,
 P-CCPCH, PDSCH, and E-AGCH are constant and cannot be changed. For the first four
 channels, the timing offset is set to 0, while for the latter channel it is set to
 20.
- For the number of slots for E-RGCH and E-HICH, you are presented with a combo box.
 Select the number of slots required. The allowed numbers of slots are 3, 12, and 15.
 The latter is only applicable to E-RGCH and EAGHC.
- The Sequence Index for E-RGCH and E-HICH. The valid range is 0 to 39.
- The relative grant (R.G.) and ARQ acknowledgment indicator (ARQ A.I.) for the E_RGCH
 and E-HICH, respectively. Valid values are +1 and –1. The 0 selection is not
 supported as for a 10 ms frame this results in a frame(s) with no data. A 0
 selection is equivalent to switching the channel off.
- The data source can be changed for the P-CCPCH, S-CCPCH, PICH, and E-AGCH. This will
 show the standard data source dialog that will allow you to modify the current data
 source configuration.
- The channel state can be set to on or off for all channels.

In some situations, it is possible to configure two channels such that the channel code
 and spreading factor (determined by the current slot format) can overlap, leading to a
 conflict. When such a conflict occurs, an error graphic is shown indicating that the
 channels are in conflict, and each overlapping channel will be highlighted in red in the
 channel table as shown in the following figure.

[IMAGE alt='image' src='GUID-DA039C18-55B5-4414-A8C5-B28EAEE91771-a5.gif']

Note

Edit

Adding a Channel

To add a channel into your downlink simulation click Add
 button. The default channel is a dedicated physical channel. Select the slot format
 by clicking on the appropriate row. Enter each parameter as required. If the channel
 is a multicode channel, select the Multicode Channel check
 box. If this is selected you cannot define TPC bits. When the Add Channel
 Properties dialog box is open, the main downlink table will show the
 configured channel, allowing you to view any conflicts that occur as part of the
 channel configuration. Upon clicking OK, the current
 selection is accepted, and the channel will be permanently added to the table. Upon
 clicking Cancel, the channel will be automatically removed
 from the table.

In addition to the DPCH channel, you can also add an HS-SCCH channel, an HS-PDSCH
 channel, an OCNS and an F-DPCH channel. The OCNS channel is an orthogonal noise
 source. Furthermore, you can set the power level and channel code for all channel
 types. The slot format is used to set the symbol rate for all the available
 channels. No control bits are present in the HS-SCCH, HS-PDSCH, and OCNS
 channels.

[IMAGE alt='image' src='GUID-FAD1FC69-66A9-4AFA-85D0-CEEA613B9AE7-a5.gif']

HS-PDSCH-specific Parameters

For HS-PDSCH, refer the following figure, the following additional items are
 configurable.

[IMAGE alt='image' src='GUID-51D97D56-A545-4962-9906-C98049DBBD4D-a5.gif']

Slot Format: Valid values are 0, 1, or 2, which corresponds to
 the modulation schemes, QPSK, 16QAM, and 64QAM respectively.

Slot Format 2: This is visible only if the HS-PDSCH mode is
 selected as “MIMO”. It is the slot format for the second transport block and reuses
 the values in the slot format table for the first transport block. Thus, it can take
 the values 0, 1 and 2. The second transport block’s modulation scheme can be
 configured independent of the first transport block’s.

Tx Pattern: This controls the subframes in which HS-PDSCH and
 the corresponding HS-SCCH are transmitted. It is a sequence of 1s and 0s, where 1
 represents transmission and 0, no transmission. Default value is 1. The transmission
 pattern is applied each subframe, while wrapping around at the end of the pattern,
 to the HS-PDSCH assuming an offset of 2 slots from the start of the P-CCPCH
 frame.

Precoding Pattern: When MIMO mode is selected in HS-PDSCH Mode
 in the Downlink Channel Configuration, then the “Precoding pattern” box becomes
 visible. It corresponds to a pattern of precoding weights . It takes 0, 1, 2 and 3
 as pattern values. Default is 0. The precoding weights are applied each subframe,
 while wrapping around at the end of the pattern, to the HS-PDSCH assuming an offset
 of 2 slots from the start of the P-CCPCH frame.

Stream 2 Data Source:This is visible only if the HS-PDSCH mode
 is selected as “MIMO”. It is the source of data for the second transport block.

F-DPCH Specific Parameters:For F-DPCH, most parameters are
 similar to the DPCH. The main difference is the replacement of Ndata1 and Ndata2
 with NOFF1 and NOFF2 (refer the following figure).

[IMAGE alt='image' src='GUID-667CE0B5-93F6-466B-9D44-3BD945185B33-a5.gif']

Editing a Channel

To edit a channel, select the channel of interest and either double-click the right
 mouse button or press the Edit... button. On doing so, you
 are presented with a dialog box as shown in the following figure.

[IMAGE alt='image' src='GUID-41CCC9E7-CB1C-43A0-9C09-0358832DC432-a5.gif']

Edit the parameters of interest. Click OK when done. You
 cannot alter the type of channel.

Removing a Channel

To remove a channel, select the channel of interest and press the
 Remove button.

Note

- The slot format that you are presented with in the Edit and Add channel dialogs
 depends on whether the TFCI bits are to be used or not.
- 3GPP FDD test models are provided as example RFWC/RFWS files with. Refer to the
 RFmx Waveform Creator Help document for more details on
 using example files.
- When S-CPICH is present and HS-PDSCH is in the MIMO mode, the pilot pattern in
 CPICH for antenna 2 is the same as that of antenna 1. Otherwise, the pilot
 pattern of antenna 2 is used.

Parent topic:

WCDMA (3GPP FDD Release 8)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=downlink-dual-carrier-example.html language=enus -->
## TOPIC 00046: Downlink Dual Carrier Example

- bundle_id: `rfmx-waveform-creator`
- source_path: `downlink-dual-carrier-example.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/downlink-dual-carrier-example.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure shows an example configurations of carrier definitions and a carrier set to generate a downlink HSDPA dual carrier signal. Refer the RFmx Waveform Creator Help document for more information on Carrier Definitions and Carrier Sets. Carrier Definition 0 uses Scrambling Code 0, whi

### Downlink Dual Carrier Example

The following figure shows an example configurations of carrier definitions and a carrier
 set to generate a downlink HSDPA dual carrier signal. Refer the RFmx Waveform
 Creator Help document for more information on Carrier Definitions and
 Carrier Sets.

Carrier Definition 0 uses Scrambling Code 0, while Carrier Definition 1 uses Scrambling
 Code 1. These two definitions are configured in the Modulation
 tab and combined into Carrier Set 0 in the Multi-Carrier tab. Refer to the following
 figures to know more about Carrier Definition 0 and Carrier Definition 1.

The following figure shows the Carrier definition 0 for primary cell

[IMAGE alt='image' src='GUID-6476B531-012A-4E3E-BA63-D5D758ACD517-a5.gif']

The following figure shows the Carrier definition 1 for secondary cell

[IMAGE alt='image' src='GUID-4571BC7F-0C23-4088-96C9-A11789DFAAE9-a5.gif']

The following figure shows the Carrier set 0 for combining cells in baseband

[IMAGE alt='image' src='GUID-146316D6-3900-4869-BE28-A9390680D291-a5.gif']

The combined signal spectrum is shown in the following figure. Marker 1 shows the center
 frequency of carrier 1 which has carrier definition 0 mapped to it. Marker 2 shows the
 center frequency of carrier 2 which has carrier definition 1 mapped to it.

[IMAGE alt='image' src='GUID-28495C3E-B198-4878-8E6A-F0987C9ABF35-a5.gif']

Parent topic:

WCDMA (3GPP FDD Release 8)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=enhanced-machine-type-communication.html language=enus -->
## TOPIC 00047: Enhanced Machine Type Communication

- bundle_id: `rfmx-waveform-creator`
- source_path: `enhanced-machine-type-communication.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/enhanced-machine-type-communication.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enhanced machine type communication (eMTC) or LTE Cat-M1 is a low power wide area (LPWA) technology introduced in the Release 13 LTE 3GPP specification. eMTC supports low complexity IoT devices, which leverages the existing LTE network infrastructure. eMTC is used in IoT devices that require higher

### Enhanced Machine Type Communication

Enhanced machine type communication (eMTC) or LTE Cat-M1 is a low power wide area (LPWA)
 technology introduced in the Release 13 LTE 3GPP specification. eMTC
 supports low complexity IoT devices, which leverages the existing LTE network
 infrastructure. eMTC is used in IoT devices that require higher data rate than that
 supported by NB-IoT devices. eMTC has a reduced bandwidth compared to LTE but has an
 extended coverage.

eMTC is referred as BL/CE, where BL is bandwidth reduced low complexity and CE is
 coverage enhancement.

It supports half-duplex frequency division duplex (HD-FDD), frequency division duplex
 (FDD), and time division duplex (TDD) operations.

eMTC supports two transmission modes - Cat-M1 and Cat-M2. Cat-M1 eMTC uses 1.08 MHz of
 integration bandwidth (6 resource blocks or narrow band) for transmission and reception,
 while Cat-M2 eMTC uses 5 MHz of integration bandwidth (24 resource blocks or wideband)
 for transmission and reception.

Narrow Band Retuning or Frequency Hopping

Six consecutive non-overlapping resource blocks constitute a narrow band. Each LTE
 bandwidth is divided into a set of pre-defined narrow bands as per section 5.2.4 of
 3GPP 36.211 specification.

For channel bandwidths other than 1.4 MHz, the transmission can be retuned from one
 narrow band to another at the subframe boundary. This retuning operation called
 frequency hopping, or narrow band retuning, requires sufficient guard symbols to be
 allocated.

Narrow band hopping interval defines the periodicity of frequency hopping. The frequency
 separation between the narrow bands used before and after retuning is called narrow band
 hopping offset. Hopping offset and hopping interval is specified by higher layers.

Wide Band Retuning or Frequency Hopping

Four consecutive non-overlapping narrow bands constitute a wideband as defined in section
 5.2.4 of 3GPP 36.211 specification. For 1.4 MHz and 3 MHz, wideband
 is composed of all available narrow bands (1 and 2 respectively).

For channel bandwidths higher than 5 MHz, the transmission can be retuned from one
 wideband to another at the subframe boundary. This retuning operation called frequency
 hopping or wideband retuning, which requires sufficient guard symbols to be
 allocated.

Guard Symbols

During frequency hopping, the local oscillator (LO) of transmitter will retune to a
 different frequency. The LO requires some time to settle to the new frequency, hence
 some empty symbols are allocated. These symbols are referred to as guard symbols. In
 case of Cat-M2, guard symbols are allocated only if the hopping happens from one
 wideband to another. Number of guard symbols for different conditions are defined in
 section 5.2.5 of 3GPP 36.211 specification.

The following image shows the frequency hopping in eMTC with guard symbols, hopping
 offset, and hopping interval

[IMAGE alt='image' src='GUID-3F21758D-0D52-46EF-BFEE-F7ACA6BF4985-a5.gif']

Note

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=ev-do-revision-0-overview.html language=enus -->
## TOPIC 00048: EV-DO Revision 0

- bundle_id: `rfmx-waveform-creator`
- source_path: `ev-do-revision-0-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/ev-do-revision-0-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creates a waveform that simulates a EV-DO carrier. The modulation scheme is defined in the 3gpp2 specification C.S0024 version 4. This document assumes that you know how to package and download files to an instrument. For more information about packaging and downloading files to an instrument, refer

### EV-DO Revision 0

Creates a waveform that simulates a EV-DO carrier.

The modulation scheme is defined in the 3gpp2 specification *C.S0024 version
 4*. This document assumes that you know how to package and download files to
 an instrument.

Note

Generating and Saving the Waveform File

Parent topic:

RFmx Waveform Creator Modulation Schemes

Related information:

- RFmx EV-DO .NET Reference
- RFmx EV-DO C API Reference

<!--NI_TOPIC bundle=rfmx-waveform-creator path=ev-do-revision-a-overview.html language=enus -->
## TOPIC 00049: EV-DO Revision A

- bundle_id: `rfmx-waveform-creator`
- source_path: `ev-do-revision-a-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/ev-do-revision-a-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creates a waveform that simulates a EV-DO Revision A carrier. The modulation scheme is defined in the 3gpp2 specification C.S0024-A version 2. This document assumes that you know how to package and download files to an instrument. For more information about packaging and downloading files to an inst

### EV-DO Revision A

Creates a waveform that simulates a EV-DO Revision A carrier.

The modulation scheme is defined in the 3gpp2 specification *C.S0024-A version
 2*.

Note

Generating and Saving the Waveform
 File

Parent topic:

RFmx Waveform Creator Modulation Schemes

<!--NI_TOPIC bundle=rfmx-waveform-creator path=frame-configuration-mode-lte.html language=enus -->
## TOPIC 00050: Mode: LTE

- bundle_id: `rfmx-waveform-creator`
- source_path: `frame-configuration-mode-lte.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/frame-configuration-mode-lte.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following frame configuration options are available for a LTE transmission, when you set the Mode parameter to LTE. At the top is the subframe graphical parameter that provides a graphical representation of all the subframes in the signal. Uplink subframes are shown as blue and Downlink subframe

### Mode: LTE

The following frame configuration options are available for a LTE transmission, when you
 set the Mode parameter to LTE.

At the top is the subframe graphical parameter that provides a graphical representation of
 all the subframes in the signal. Uplink subframes are shown as blue and Downlink subframes
 are shown in green. Special subframes are shown in yellow.

Note

In Uplink mode, the graphic will also show the type of uplink subframes.

To edit the subframe parameters, click one of the items within the frame. If the parameters
 are available for this item, the panel below will change to reflect the new parameters.

Uplink Subframe Configurations

The following are the parameters that are available when you set Link
 Direction to Uplink.

Channel Type: Specifies type of the Channel that will be transmitted
 within this subframe. The valid values are PUSCH, PUCCH, DTX, or PUSCH+PUCCH.

Current Channel Type: Specifies the type of Channel whose settings
 are currently displayed. The valid values are PUSCH and PUCCH.

This parameter is available only when Channel Type is set to
 PUSCH+PUCCH.

Modulation Type: When the Channel Type is set
 to PUSCH, this specifies the modulation type. The valid values are
 QPSK, 16QAM, 64QAM, 256QAM, and 1024 QAM.

When the Modulation Mode for the PUSCH channel is User
 Defined, this property is settable. If the modulation mode is MCS
 Index, the property is read only (and is derived from the MCS index).

Power: When the Channel Type is set to
 PUSCH or PUCCH, this parameters the
 relative power of this subframe within the simulation. The valid range is -1000 to 30
 dB.

N2 DMRS: When the Channel Type is set to
 PUSCH this specifies the N2 DMRS value
 (n<sub>DMRS</sub><sup>(2)</sup> ). The valid range is between 0 and 10. The default
 value is 0. This value parameters the DMRS cyclic shift applied when transmitting a DMRS
 signal for PUSCH.

Hopping Type: This parameter is available only when the
 Channel Type is set to PUSCH. This
 parameter can be set to 0, 1, or 2. The default value is 0. This is used in conjunction
 with the hopping bits to parameter the type of hopping that is applied (see Table
 1-14).

Hopping Bits: This parameter is available only when the
 Channel Type is set to PUSCH. Valid Values
 are 0, 1, 2, and 3. The default value is 0.

The number of hopping bits is used in conjunction with hopping type to parameter the type
 of hopping that is applied. Refer to the following table for more information.

[IMAGE alt='image' src='GUID-93338E48-9691-4A84-9A26-A8C4956B560D-a5.gif']

Table 1-14 The relationship between hopping type and hopping bits

(Table 8.4-2 of 3GPP TS 36.213 V8.8.0 (2009-09))

Resource Allocation Type: This parameter is available only when
 Channel Type is set to PUSCH. You can
 choose between resource allocation types 0 and 1 (Section 8.1 of
 36.213).

[IMAGE alt='image' src='GUID-5DADBFDE-8AFF-4BF7-97FF-B784C735871F-a5.gif']

Table 1-15 : Limits for uplink Resource allocation type 1

Number of RBs: This parameter is available only when
 Channel Type is set to PUSCH and
 Resource Allocation Type is set to 0.

This defines the number of PUSCH resource blocks that have been scheduled for transmission
 in the current subframe. The value of this parameter should be set according to the
 following rules:

- It must also be a non-zero positive value. The starting RB + the number of RBs cannot
 exceed the total system bandwidth. The number of resource blocks available for specific
 bandwidths is listed in Table 1-6
- When Hopping is enabled, another level of restriction is imposed. In this
 case, M RB PUSCH cannot exceed the Hopping
 Bandwidth.

Starting RB: This parameter is available only when
 Channel Type is set to PUSCH and
 Resource Allocation Type is set to 0. This defines the starting
 position of the virtual resource block. The value of this parameter should be set following
 the rules mentioned below:

- If Hopping is disabled, the sum of Starting Virtual RB and
 M RB PUSCH should not go beyond the bandwidth.
 Table 1-6 lists the number of resource blocks available for specific bandwidths.
- If Hopping is enabled, you should ensure that the Starting Virtual RB lies within the
 hopping bandwidth.

Number of RBGs: This parameter is available only when
 Channel Type is set to PUSCH and
 Resource Allocation Type is set to 1. This defines the number of
 PUSCH resource block groups (RBGs) in the first set of RBGs that have been scheduled for
 transmission in the current subframe.

The value of this parameter should be set according to the rules mentioned at the
 description of the parameter Starting RBG Set 2.

Starting RBG: This parameter is available only when
 Channel Type is set to PUSCH and
 Resource Allocation Type is set to 1. This defines the starting
 RBG of the first set of PUSCH RBGs.

The value of this parameter should be set according to the rules mentioned at the
 description of the parameter Starting RBG Set 2.

Number of RBGs Set 2: This parameter is available only when
 Channel Type is set to PUSCH and
 Resource Allocation Type is set as 1. This defines the number of
 PUSCH RBGs in the second of RBGs that have been scheduled for transmission in the current
 subframe.

The value of this parameter should be set according to the rules mentioned at the
 description of the parameter Starting RBG Set 2.

Starting RBG Set 2: This parameter is available only when
 Channel Type is set to PUSCH and
 Resource Allocation Type is set to 1. This defines the starting
 RBG of the second set of PUSCH RBGs.

The value of this parameter, in conjunction with the above three, should be set following
 the rules below.

- Denote the number of resource block groups in the bandwidth as
 N RBG UL
- Number of RBGs must be an integer in the range 1 to
 N RBG UL -2.
- Starting RBG must be an integer between 0 and
 N RBG UL -3.
- Starting RBG Set 2 must be an integer in the range Starting RBG + Number of RBGs + 1 to
 N RBG UL -1
- Number of RBGs Set 2 must be an integer in the range 1 to
 N RBG – Starting RBG Set 2
- Number of RBGs Set 2 + Number of RBGs must follow the rules given for the parameter
 Number of RBs.

[IMAGE alt='image' src='GUID-E7E05E2E-BCAE-4B53-978B-CC03C31B1391-a5.gif']

Table 1-16 Relationship between System Bandwidth and number of PUSCH
 RBGs

DAI (Downlink Assignment Index): This parameter is available only
 when Channel Type is set to PUSCH. The valid
 range is 1, 2, 3, or 4. The default value is 1.

Code Rate: This parameter is available only when Channel
 Type is set to PUSCH and the Modulation mode is user
 defined The valid values are 1/6, 1/5, 1/3, 1/2, 2/3 3/4, or 5/6. The default value is
 1/3.

MCS Index: This parameter is available only when Channel
 Type is set to PUSCH and the Modulation mode is user
 defined. The valid range is 0 to 28.

Allow 256-QAM: If the Allow 256-QAM checkbox
 is selected, it allows higher order modulation of 256 QAM.

Current Tx NB: This parameter is available only when
 Channel Type is set to PUSCH. The valid
 values are 0, 1, 2, or 3. The default value is 0. This parameter sets the transmission
 number of data being transmitted in the selected subframe.

Starting CCE: This parameter is available only when
 Channel Type is set to PUCCH. The valid
 range is 0 to 87. The default value is 0. This specifies the starting CCE of the PDCCH
 transmission that corresponds to PUCCH being transmitted in the current subframe.

PUCCH Format: This parameter is only available when
 Channel Type is set to PUCCH and
 Auto calculate PUCCH format is set to
 False. The PUCCH format can currently be 1/1a/1b.

Downlink Subframe Configurations

The following parameters are available for any downlink subframe being configured. These
 will be available if the Link Direction is set to
 Downlink.

[IMAGE alt='image' src='GUID-F33C1370-6773-46E0-B985-5D9F86CB8ED3-a5.gif']

CFI: Specifies the Control Frame Indicator (CFI) of this subframe.
 This can be set to 1, 2, or 3. The default value is 2. The CFI controls the number of OFDM
 symbols that are used to transmit parameter information. For more information, refer to
 section 5.3.4 of TS 36.212

Channel Type

PDCCH

You can view this window by clicking the PDCCH Channel from the
 channel table and clicking the Edit button.

It comprises of three check boxes, one that specifies PDCCH channel state, one that
 contains DL Grant specific parameters, and one that contains UL Grant specific
 parameters.

[IMAGE alt='image' src='GUID-783B4524-32EC-4BDE-B6CE-2EA05324C711-a5.gif']

DL Grant State: This parameter allows you to turn off the DL
 Grant. If this checkbox is selected, the Grant will be transmitted; otherwise it will
 not be included in the signal. By default, this is selected
 (On)

DL Grant Format: The valid values are 0, 1, 2, or 3. The DL Grant
 format is used to parameter the number of CCEs used to transmit the DL Grant.

DL Grant Search Space: The valid values are UE Specific and
 Common. The Search Space controls the CCEs that are used to transmit the DL grant.

The Common Search Space contains CCEs that get read by every UE, where as the UE
 Specific Search Space contains CCEs that are only guaranteed to be read by a specific
 UE.

UL Grant State: This parameter allows you to turn off the UL
 Grant. If this is checkbox is selected, the Grant will be transmitted; otherwise it will
 not be included the signal. By default, this is selected (On)

UL Grant Search Space: The valid values are UE Specific and
 Common. The Search Space controls which CCEs are used to transmit the UL grant. The
 Common Search Space contains CCEs that get read by every UE, whereas the UE Specific
 Search Space contains CCEs that are only guaranteed to be read by a specific UE.

UL Grant Format: The valid values are 0, 1, 2, or 3. The UL Grant
 format is used to control the number of CCEs used to transmit the UL Grant.

UL Grant DMRS Cyclic Shift: The valid range is 0 to 7. The
 default value is 0. This is used to control the DMRS Cyclic Shift used on the Uplink
 transmission that is scheduled by the UL grant.

UL Grant MCS: The valid range is 0 to 28. The default value is 0.
 The MCS transmitted specifies the modulation and channel coding that should be applied
 to the Uplink transmission that is scheduled by the UL grant.

Resource Allocation Type: This parameter is available only when
 Channel Type is set to PUSCH. You can
 choose between resource allocation types 0 and 1 (Section 8.1 of
 36.213).

[IMAGE alt='image' src='GUID-5DADBFDE-8AFF-4BF7-97FF-B784C735871F-a5.gif']

Table 1-17 : Limits for downlink Resource allocation type 1

UL Grant TPC Pattern: This parameter specifies the UL grant TPC
 Pattern. It can accept a sequence of numbers including 0, 1, 2, or 3. This specifies the
 TPC pattern that is transmitted on the UL Grant.

UL Grant Hopping Flag: This parameter specifies whether the
 Hopping Flag will be set in the UL grant. If this parameter is selected,
 Hopping will be set to 1; otherwise it will be set to 0.

UL Grant Num of CSI Request Bits: This field sets the number of
 bits of CSI Request. Its value can be 1 or 2.

UL Grant SRS Request: You need to select the SRS
 Request checkbox, to include the SRS bits in DCI format 0 or DCI format
 4.

If the checkbox is selected and Number of Antennas is set to 1
 (DCI format 0), then SRS Request range is from 0 to 1.

If the checkbox is selected and Number of Antennas is set to
 2 (DCI format 4), then SRS Request range is from 0 to 3.

Description of the values is as given in the following table for DCI format 0. For DCI
 format 4, refer 36213, Table 8.1-1: SRS request value for trigger type 1 in DCI
 format 4.

[IMAGE alt='image' src='GUID-6B8733FA-4B34-4FEE-9195-006D725C1199-a5.gif']

Table 1-18 : SRS request value of trigger type 1 in DCI format 4
 Value of SRS request field

UL Grant SRS: By default the SRS Request
 checkbox is unselected. If the checkbox is selected, SRS Request will be enabled.

If the checkbox is selected and Number of Antennas is set to
 1, then range of SRS Request is from 0 to 1.

If the checkbox is selected and Number of Antennas is set to
 2, then range of SRS Request is from 0 to 3.

UL Grant CQI/CSI Request: The CQI request field is renamed to
 CQI/CSI Request. This sends a CQI Request on the UL Grant. The
 valid range is 0 and 1 if the No. Of CSI Request Bits field is
 1. Otherwise the range is between 0 to 3.

UL Grant Number Of Antennas: The valid range is 1 and 2. This
 specifies the number of UL antennas the UE is assumed to have.

If Number of Antennas is set to 2, then
 this will transmit DCI format 4 and the configuration is called Downlink
 MIMO.

PDSCH

You can view this window by clicking PDSCH Channel from the
 Channel table and then clicking the Edit button.

Multiple PDSCH channels can be configured per subframe.

It comprises the following parameters:

Transmission Mode: The Transmission mode can be Single
 Port(SISO), Tx Diversity(MIMO), Closed Loop(MIMO), Open loop(MIMO), Single-layer
 beamforming, Dual-layer beamforming, 8 layer spatial multiplexing, or 8 layer spatial
 multiplexing (Release 12). The transmission mode specifies how the signal is
 transmitted.

[IMAGE alt='image' src='GUID-1C57A83C-13BC-4699-B773-BE9B90BDDF1C-a5.gif']

Codebook Index: Codebook index is enabled for Closed loop, Eight
 layer Muxing and Eight Layer Muxing Release 12 cases.

For Closed Loop case, the valid values are 0 ,1, and 2.

For Eight Layer Muxing and Eight Layer Muxing Release 12 case, if the Rank is 1 or 2,
 then range of Codebook Index is from 0 to 15. If Rank is from 3 to 7, then range of
 Codebook Index is from 0 to 3. For Rank 8, it is disabled.

Precoding Matrix Indicator: This field is enabled when
 Transmission mode is 9 or 10 and Rank ≤ 4. It allows you to choose one of the codebooks
 used by the UE to signal precoding feedback for channel dependent codebook based
 precoding. It can take the following values:

- If Rank is 1, 2, or 3, the range is 0 to 15.
- If Rank is 4, the range is 0 to 7.

Rank: This parameter is valid only if the Transmission
 Mode is set to Closed Loop, Dual-layer
 beamforming, Eight layer spatial multiplexing, or
 Eight layer spatial multiplexing (Release 12). The valid
 values are 1 to 8.

UE ID: The valid range is 0 to 65535. The default value is 0.

Resource Allocation Type: The Resource allocation type can
 be:

- Type 0:- Controlled by a resource allocation bit mask
- Type 2:- Controlled by Starting Resource Block, Resource Block Allocation
 Length
- Full:- Allocates all possible RBs so the signal occupies the maximum bandwidth.
- Custom:- Controlled by RBs specified in Resource Block Allocation.

Resource Allocation Bit-mask: This parameter is available only if
 the Resource Allocation Type is set to Type
 0. It accepts a hexadecimal value. Each resource bit in the bit mask
 corresponds to a set of resource blocks. If the Bit is set then the corresponding set of
 resource blocks will get transmitted; otherwise it will not.

Starting Resource Block: This parameter is valid only if the
 Resource Allocation Type is set to Type
 2. This specifies the starting resource block to use in the PDSCH
 transmission. The starting RB + the RB length cannot exceed the total system
 bandwidth.

Resource Block Allocation Length: This parameter is valid only if
 the Resource Allocation Type is set to Type
 2. This specifies the number of resource blocks to use in the PDSCH
 transmission. The starting RB + the RB length cannot exceed the total system
 bandwidth.

Resource Block Allocation: This parameter is valid only if the
 Resource Allocation Type is set to
 Custom. This specifies the resource blocks to use in the PDSCH
 transmission. You can enter multiple resource block separated by commas.

Codeword 1 Data Source: Specifies the payload data of the
 Codeword 1 part of the signal. If the Transmission Mode is set to
 Closed Loop or Open Loop, then two
 codewords may be transmitted; otherwise only a signal codeword is transmitted.

Refer to Selecting the Data Source topic for more information on data source.

Codeword 2 Data Source: Specifies the payload data of the
 Codeword 2 part of the Signal. This button is enabled only if Rank is greater than
 1.

Codeword1 MCS Index: This specifies the Codeword1 MCS index for
 this subframe. The valid range is 0 to 28. If 256QAM is enabled, then MCS range is from
 0 to 27. The default value is 0. The MCS index defines the Modulation and coding scheme
 used to transmit data on the PDSCH. In a SISO system, or a MIMO system that uses TX
 diversity only one codeword is transmitted. In Open loop or Closed loop MIMO two code
 words may be transmitted.

Codeword2 MCS Index: Specifies the Codeword2 MCS index for this
 subframe. The valid range is 0 to 28. If 256QAM is enabled, then MCS range is from 0 to
 27. The default value is 0. Codeword2 is used only when the Open loop or Closed loop
 MIMO is employed.

Codeword1 Modulation Type: Specifies the Codeword1 Modulation
 Type for this subframe. The valid values are QPSK, 16QAM, 64QAM, 256QAM, and
 1024QAM.

This parameter is available only when Modulation Mode is set to
 User Defined.

Codeword2 Modulation Type: Specifies the Codeword2 Modulation
 Type for this subframe. The valid values are QPSK, 16QAM, 64QAM, 256QAM, and
 1024QAM.

This parameter is available only when Modulation Mode is set to
 User Defined.

Specify Pa/Pb: If this checkbox is selected, the UE specific
 PA/PB values will be set. Otherwise, the power specified for PDSCH in the main downlink
 channels screen is used.

The Specify Pa/Pb checkbox is enabled only for TM1 to TM6.

Pa and Pb: The value of ρ<sub>A</sub> and ρ<sub>B</sub>, that is,
 the power of PDSCH symbols in OFDM symbols not containing CS-RS, is derived from
 P<sub>A</sub> and P<sub>B</sub>.

For P<sub>B</sub>, the valid range is 0 to 3. For P<sub>A</sub>, valid values are - 6
 dB, - 4.77 dB, - 3 dB, - 1.77 dB, 0 dB, 1 dB, 2 dB, and 3 dB.

Beamforming Weight Matrix: This table is enabled for all the
 Transmission modes, but is relevant only for modes Single-layer beamforming and
 Dual-layer beamforming. The matrix is of size 2 x 8. The range of values is -65536 to
 +65535.

The following figure displays the dialog box which appears when a cell is clicked to
 update the phase value. Only entries in the first Rank rows and the first Number of
 Beamforming Antennas columns are used.

[IMAGE alt='image' src='GUID-49A8D52E-44D8-4DDD-9668-3FBF047DBDF7-a5.gif']

PHICH

[IMAGE alt='image' src='GUID-CAB40807-6065-4AAC-9B3E-5CC75639F523-a5.gif']

You can view this window by clicking the PHICH Channel from the
 Channel table and then clicking the Edit button.

PHICH State: This parameter allows you to turn off the PHICH
 within the Signal. If this is selected, the PHICH Channel will be transmitted,
 otherwise, it will not be included in the signal. By default, this parameter is selected
 (On)

ACK/NACK pattern: This parameter allows you to set a binary bit
 pattern. This pattern configures the ACK/NACK bit that is transmitted. The ACK/ NACK bit
 can be configured for each subframe, and the same bit is used for all PHICH sequences
 and PHICH groups in the subframe.

Maximum Number of Channels: Specifies number of channels in the
 selected subframe of the selected Channel Type.

Channel Index: Specifies index the channel in the selected subframe
 of the selected Channel Type.

Currently multiple PDSCH channels can be configured per subframe. You need to specify the
 appropriate channel index and then click the Edit button to edit the
 properties.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=frame-configuration-overview.html language=enus -->
## TOPIC 00051: Frame Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `frame-configuration-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/frame-configuration-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The frame configuration of modulation tab allows you to control parameters that change on a subframe basis.

### Frame Configuration

The frame configuration of modulation tab allows you to control parameters that change on
 a subframe basis.

- [Mode: LTE](mode-lte.html) Frame configuration options for LTE (Long-Term Evolution) transmissions.
- [Mode: eMTC](mode-emtc.html) Frame configuration options for eMTC (Enhanced Machine-Type Communication) transmissions.
- [Mode: NB-IoT](lte-fdd-mode-nb-iot.html#GUID-794712AE-184C-474C-8B5B-8AD4381095B2) Frame configuration options for narrow band internet of things (NB-IoT) transmissions.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=frame-configuration.html language=enus -->
## TOPIC 00052: Frame Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `frame-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/frame-configuration.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This tab allows you to control parameters that change on a subframe basis. You can click a specific subframe to configure the settings corresponding to that subframe. The parameters that can be configured for each subframe differ depending whether the signal is uplink or downlink. You can click a sp

### Frame Configuration

This tab allows you to control parameters that change on a subframe basis. You can click
 a specific subframe to configure the settings corresponding to that subframe. The
 parameters that can be configured for each subframe differ depending whether the signal
 is uplink or downlink.

You can click a specific subframe to configure the settings corresponding to that
 subframe. The parameters that can be configured for each subframe differ depending
 whether the signal is uplink, downlink, or sidelink.

Uplink Subframe Configurations

The following are the parameters that are available when you set Link
 Direction to Uplink.

Apply to all subframes: Copies the configuration from the first
 subframe to all subframes. This parameter is available only for first subframe of LTE
 FDD subframe configuration.

Channel Type: Specifies type of the Channel that will be
 transmitted within this subframe. The valid values is PUSCH.

Modulation Type: When the Channel Type is
 set to PUSCH, this specifies the modulation type. The valid
 values are QPSK, 16QAM, 64QAM, 256QAM, and 1024 QAM.

When the Modulation Mode for the PUSCH channel is User
 Defined, this property is settable. If the modulation mode is
 MCS Index, the property is read only (and is derived from the
 MCS index).

Power: When the Channel Type is set to
 PUSCH or PUCCH, this controls the
 relative power of this subframe within the simulation. The valid range is -1000 to 30
 dB.

N2 DMRS: When the Channel Type is set to
 PUSCH this specifies the N2 DMRS value
 (n<sub>DMRS</sub><sup>(2)</sup> ). The valid range is between 0 and 10. The default
 value is 0. This value controls the DMRS cyclic shift applied when transmitting a DMRS
 signal for PUSCH.

Hopping Type: This control can be set to 0, 1, or 2. The default
 value is 0. This is used in conjunction with the hopping bits to control the type of
 hopping that is applied. Refer to the following relationship between hopping type and
 hopping bits (Table 8.4-2of 3GPP TS 36.213 V8.8.0 (2009-09)) for more
 information.

[IMAGE alt='image' src='GUID-B3D23E22-11B2-4E4C-9826-D19E4D3CE906-a5.gif']

Resource Allocation Type: This control is available only when the
 Channel Type is set to
 PUSCH. You can choose between resource allocation types 0, 1
 and 3. Refer to section 8.1 of 3GPP 36.213 specification for more
 details.

Note:

- The Resource Allocation Type 2 is skipped as the value 2 is not available for
 LAA.
- The Resource Allocation Type 3 is valid when you select the Channel
 Bandwidth parameter as 10 MHz or
 20 MHz .

The following table provides information on limits for uplink Resource allocation type
 1.

[IMAGE alt='image' src='GUID-FD068E6F-4880-4A1E-BB89-ADFA6DCC0EB4-a5.gif']

Number of RBs: This control is available only when the
 Channel Type is set to PUSCH and the
 Resource Allocation Type is set as
 0.

This defines the number of PUSCH resource blocks that have been scheduled for
 transmission in the current subframe. The value of this parameter should be set
 according to the following rules:

- It must also be a non-zero positive value. The value of Starting
 RB + Number of RBs cannot exceed the total
 system bandwidth. The number of resource blocks available for specific bandwidths is
 listed in Table 1-6
- When hopping is enabled, another level of restriction is imposed. In this case,
 M RB PUSCH cannot exceed the hopping
 bandwidth.

Starting RB: This control is available only when the
 Channel Type is set to PUSCH and the
 Resource Allocation Type is set as
 0.

This defines the starting position of the virtual resource block. The value of this
 parameter should be set following the rules below:

- If hopping is disabled, the sum of Starting Virtual RB and
 M RB PUSCH should not go beyond the
 bandwidth. Table 1-6 lists the number of resource blocks available for specific
 bandwidths.
- If hopping is enabled, you should ensure that the Starting Virtual RB lies within
 the hopping bandwidth.

Number of RBGs: This control is available only when the
 Channel Type is set to PUSCH and the
 Resource Allocation Type is set as 1.

This defines the number of PUSCH resource block groups (RBGs) in the first set of RBGs
 that have been scheduled for transmission in the current subframe. The value of this
 parameter should be set according to the rules mentioned at the description of the
 parameter Starting RBG Set 2.

Starting RBG: This control is available only when the
 Channel Type is set to PUSCH and the
 Resource Allocation Type is set as 1.

This defines the starting RBG of the first set of PUSCH RBGs. The value of this parameter
 should be set according to the rules mentioned at the description of the parameter
 Starting RBG Set 2.

Number of RBGs Set 2: This control is available only when the
 Channel Type is set to PUSCH and the
 Resource Allocation Type is set as 1.

This defines the number of PUSCH RBGs in the second of RBGs that have been scheduled for
 transmission in the current subframe. The value of this parameter should be set
 according to the rules mentioned at the description of the parameter Starting
 RBG Set 2.

Starting RBG Set 2: This control is available only when the
 Channel Type is set to PUSCH and the
 Resource Allocation Type is set as 1. This defines the
 starting RBG of the second set of PUSCH RBGs. The value of this parameter, in
 conjunction with the above three, should be set following the rules below.

- Denote the number of resource block groups in the bandwidth as
 N RBG UL
- Number of RBGs must be an integer in the range 1 to
 N RBG UL -2.
- Starting RBG must be an integer between 0 and
 N RBG UL -3
- Starting RBG Set 2 must be an integer in the range Starting RBG + Number of RBGs + 1
 to N RBG UL -1.
- Number of RBGs Set 2 must be an integer in the range 1 to
 N RBG – Starting RBG Set 2.
- Number of RBGs Set 2 + Number of RBGs must follow the rules given for the parameter
 Number of RBs.

[IMAGE alt='image' src='GUID-A216B85F-BA1B-4042-A659-11CDDBCC9994-a5.gif']

Table 1-28 Relationship between System Bandwidth and number of PUSCH
 RBGs

Allocation in RB Set

Defines the value l, which is used to calculate the number of PUSCH
 resource blocks that are scheduled for transmission in the current subframe. This
 control allocates the number of PUSCH resource blocks in an interlaced pattern. The
 scheduled PUSCH resource blocks is given by the following equation:

l + iN

where,

N = [[IMAGE alt='image' src='GUID-1335877C-8A79-4904-AB38-7F6C97451669-a5.gif']/10],

i =0, 1, ....9

The Allocation in RB Set control accepts comma separated integer
 values. Valid values are:

- 0 to 4, when you select the Channel Bandwidth parameter as
 10 MHz .
- 0 to 9, when you select the Channel Bandwidth parameter as
 20 MHz .

Note: The Allocation in RB Set control is
 available when you select the Channel Type parameter as
 PUSCH, Resource Allocation Type as
 3 and Channel Bandwidth as
 10 MHz or 20 MHz. For example, for a
 signal, if you select the Channel Bandwidth as 20
 MHz and Allocation in RB Set as
 0, 2, 3, the
 scheduled PUSCH resource blocks is calculated as follows: [IMAGE alt='image' src='GUID-1335877C-8A79-4904-AB38-7F6C97451669-a5.gif'] = 100 N = [[IMAGE alt='image' src='GUID-1335877C-8A79-4904-AB38-7F6C97451669-a5.gif'] /10] = [100/10] =10 For l = 0, the calculation is as follows: l +
 iN = 0 + 10i where, i = 0, 1, ...9 PUSCH resource blocks are 0, 10, 20, 30, 40, 50, 60,
 70, 80, 90 For l = 2, the calculation is as follows: l + iN = 2 + 10i where, i = 0, 1,
 ...9 PUSCH resource blocks are 2, 12, 22, 32, 42, 52, 62, 72, 82, 92 For l = 3, the
 calculation is as follows: l + iN = 3 + 10i where, i = 0, 1, ...9 PUSCH resource blocks
 are 3, 13, 23, 33, 43, 53, 63, 73, 83, 93

Therefore, when the Allocation in RB Set = 0, 2, 3 (l = 0, 2, 3),
 the scheduled PUSCH resource blocks are: 0, 2, 3, 10, 12, 13, 20, 22, 23, 30, 32, 33,
 40, 42, 43, 50, 52, 53, 60, 62, 63, 70, 72, 73, 80, 82, 83, 90, 92, 93.

Code Rate: This control is available only when Channel
 Type is set to PUSCH and Modulation
 Mode is User Defined.

The valid values are 1/6, 1/5, 1/3, 1/2 , 2/3 3/4, or 5/6. The default value is 1/3.

MCS Index: This control is available only when Channel
 Type is set to PUSCH and Modulation
 Mode is MCS Index. The valid range is 0 to
 28.

Current Tx NB: This control is available only when
 Channel Type is set to PUSCH. The
 valid values are 0, 1, 2, or 3. The default value is 0.

This parameter sets the transmission number of data being transmitted in the selected
 subframe.

Downlink Subframe Configurations

The following parameters are available for any downlink subframe being configured. These
 are available if the Link Direction to
 Downlink.

CFI: This specifies the control frame indicator (CFI) of this
 subframe. This can be set to 1 or 2. The default value is 2. The CFI controls the number
 of OFDM symbols that are used to transmit control information. Refer to section
 5.3.4 of TS 36.212 for more information.

Channel Type

PDCCH

You can view this window by clicking the PDCCH Channel from
 the Channel Type drop-down menu and then clicking the
 Edit button.

This window comprises of two checkboxes, one that contains DL Grant specific
 parameters, and the other contains UL Grant specific parameters.

[IMAGE alt='image' src='GUID-A078C787-14E2-4BDF-96E5-2EF0AE5D9E17-a5.gif']

PDCCH DL Grant State: This control allows you to turn off the
 DL Grant. If the PDCCH DL Grant State option is selected, the
 Grant will be transmitted, otherwise, it will not be included the signal. By
 default, this option is selected (On).

Format: The valid values are 0, 1, 2, or 3. The DL Grant
 format is used to control the number of CCEs, that are used to transmit the DL
 Grant.

Search Space: The valid values are, UE
 Specific and Common. The search space
 controls which CCEs are used to transmit the DL grant. The common search space
 contains CCEs that get read by every UE, whereas the UE Specific search space
 contains CCEs that are only guaranteed to be read by a specific UE.

PDCCH UL Grant State: This control allows you to turn off the
 UL Grant. If this the PDCCH UL Grant State option is
 selected, the Grant will be transmitted, otherwise, it will not be included the
 signal. By default, this option is selected (On).

Search Space: The valid values are UE
 Specific and Common. The search space
 controls which CCEs are used to transmit the UL grant. The common search space
 contains CCEs that get read by every UE, whereas the UE Specific search space
 contains CCEs that are only guaranteed to be read by a specific UE.

Format: The valid values are 0, 1, 2, or 3. The UL Grant
 format is used to control the number of CCEs used to transmit the UL Grant.

DMRC Cyclic Shift: This parameter is used to control the DMRS
 cyclic shift used on the uplink transmission that is scheduled by the UL grant. The
 valid range is 0 to 7. The default value is 0.

MCS: The MCS transmitted specifies the modulation and channel
 coding that should be applied to the uplink transmission, that is scheduled by the
 UL grant. The valid range is 0 to 28. The default value is 0.

CQI/CSI Request. This parameter sends a CQI Request on the UL
 Grant. The valid range is 0 and 1 if the No. Of CSI Request Bits
 field is se to 1. Otherwise, the valid range is 0 to 3

TPC Pattern: This control specifies the UL grant TPC Pattern,
 it can accept a sequence of numbers including 0, 1, 2, or 3. This specifies the TPC
 pattern that is transmitted on the UL Grant.

Hopping Flag: This control specifies whether the hopping flag
 will be set in the UL grant. If this control is checked, hopping will be set to 1;
 otherwise it will be set to 0.

Num of CSI Request bits: This field will set the number of
 bits of CSI Request. The valid values are 1 or 2.

SRS Requests: You have to enable the SRS
 Request checkbox to include the SRS bits in DCI format 0 or DCI
 format 4.

- If the SRS Request option is selected and
 Number of Antennas is set to 1 
 (DCI format 0), then the SRS Request range will be from 0 to 1.
- If the SRS Request option is selected and
 Number of Antennas is set to 2 
 (DCI format 4), then the SRS Request range will be from 0 to 3.

Description of the values is as given in the following table for DCI format 0. For
 more information on DCI format 4, refer to Table 8.1-1 of 3GPP
 36.213 specification.

[IMAGE alt='image' src='GUID-391FD57C-6C7B-48ED-BFA6-FCACF0E8A2F6-a5.gif']

Table 1-10: SRS request value of trigger type 1 in DCI format 4
 Value of SRS request field

Note

- By default the SRS Request checkbox is unchecked. If the
 SRS Request checkbox is selected, the SRS Request
 spin box will be enabled.
- If the SRS Request checkbox is selected and
 Number of Antennas is set to
 1 , then range of SRS Request is 0 to 1.
- If the SRS Request checkbox is selected and
 Number of Antennas is set to
 2 , then range of SRS Request is 0 to 3.

Number Of Antennas: Specifies the number of UL antennas the UE
 is assumed to have. The valid range is 1 and 2. If Number of
 Antennas is set to 2, then this will transmit
 DCI format 4 and the configuration is called Uplink MIMO.

PDSCH

This window can be shown by clicking on the PDSCH Channel from
 the Channel table and then clicking the
 Edit button.

Multiple PDSCH channels can be configured per subframe.

[IMAGE alt='image' src='GUID-BC37A80F-7FBC-44AB-BC45-9D0007285332-a5.gif']

Transmission Mode: The transmission mode specifies how the
 signal is transmitted. The Transmission mode can be Single Port(SISO), Tx
 Diversity(MIMO), Closed Loop(MIMO), Open loop(MIMO), Single-layer beamforming,
 Dual-layer beamforming, 8 layer spatial multiplexing, or 8 layer spatial
 multiplexing (Release 12).

[IMAGE alt='image' src='GUID-1C57A83C-13BC-4699-B773-BE9B90BDDF1C-a5.gif']

Codebook Index: Codebook index is enabled for Closed loop,
 Eight layer Muxing, and Eight Layer Muxing Release 12 cases. For Closed Loop case,
 the valid values are 0, 1, and 2.

For Eight Layer Muxing and Eight Layer Muxing Release 12 case,

- If rank is 1 or 2, then range of Codebook Index is from 0 to 15.
- If rank is from 3 to 7, then range of Codebook Index is from 0 to 3.
- For rank 8, it is disabled

Precoding Matrix Indicator: This option is enabled when
 Transmission Mode is 9 or 10 and Rank = 4. It allows you to select one of the
 codebooks used by the UE to signal precoding feedback for channel dependent codebook
 based precoding. It can take the following values:

- If Rank is 1, 2, or 3, the range is 0 to 15.
- If Rank is 4, the range is 0 to 7.

Rank: This control is valid only if the
 Transmission Mode is set to Closed
 Loop, Dual-layer beamforming,
 Eight layer spatial multiplexing, or Eight
 layer spatial multiplexing (Release 12). The valid values are 1 to
 8.

UE ID: The valid range is 0 to 65535. The default value is
 0.

Resource Allocation Type: The Resource allocation type can
 be:

- Type 0:- Controlled by a Resource Allocation Bit Mask.
- Type 2:- Controlled by Starting Resource Block and Resource Block Allocation
 Length
- Full:- Allocates all possible RBs so the signal occupies the maximum
 bandwidth.
- Custom:- Controlled by RBs specified in Resource Block Allocation.

Resource Allocation Bit Mask: This option is available only if
 the Resource Allocation Type is set to Type
 0. It accepts a hexadecimal value.

Each bit in the bit mask corresponds to a set of resource blocks. If the Bit is set
 then the corresponding set of resource blocks will get transmitted; otherwise it
 will not.

Starting Resource Block: This control is valid only if the
 Resource Allocation Type is set to Type
 2. This specifies the starting resource block to use in the PDSCH
 transmission. The value of Starting RB + Number of
 RBs cannot exceed the total system bandwidth.

The number of resource blocks available for specific bandwidths is listed in Table
 1-6.

Resource Block Allocation Length: This control is valid only
 if the Resource Allocation Type is set to Type
 2. This specifies the number of resource blocks to use in the PDSCH
 transmission. The value of Starting RB + Number of
 RBs cannot exceed the total system bandwidth.

The number of resource blocks available for specific bandwidths is listed in Table
 1-6.

Resource Block Allocation: This control is only valid if the
 Resource Allocation Type is set to
 Custom. This specifies the resource blocks to use in the
 PDSCH transmission. You can enter multiple resource blocks separated by commas.

Codeword 1 Data Source: Specifies the payload data of the
 Codeword 1 part of the Signal. If the Transmission Mode is
 set to Closed Loop or Open Loop, then
 two code words may be transmitted; otherwise only a signal code word is
 transmitted.

Refer to Selecting the Data Source topic for more information on data source.

Codeword 2 Data Source: Specifies the payload data of the
 Codeword 2 part of the Signal. This button is enabled only if Rank is greater than
 1.

Codeword1 MCS Index: Specifies the Codeword1 MCS index for
 this subframe. The valid range is 0 to 28. If 256QAM is enabled, then MCS range is
 from 0 to 27. The default value is 0. The MCS index defines the modulation and
 coding scheme used to transmit data on the PDSCH. In a SISO system, or a MIMO system
 that uses TX diversity only one code word is transmitted. In open loop or closed
 loop MIMO two code words may be transmitted.

Codeword2 MCS Index: Specifies the Codeword 2 MCS Index for
 this subframe. The valid range is 0 to 28. If 256 QAM is selected, then MCS range is
 from 0 to 27. The default value is 0. Codeword 2 is only used when Open Loop or
 Closed Loop MIMO is employed.

Allow 256-QAM: If the Allow 256-QAM
 checkbox is selected, it allows higher order modulation of 256-QAM.

Specify Pa/Pb: If the Specify Pa/Pb
 checkbox is selected, the UE specific PA/PB values will be set. Otherwise, the power
 specified for PDSCH in the main downlink channels screen is used.

The Specify Pa/Pb checkbox is enabled only for TM1 to TM6.

Pa and Pb: The value of ρ<sub>A</sub> and ρ<sub>B</sub>, that
 is, the power of PDSCH symbols in OFDM symbols not containing CS-RS, is derived from
 P<sub>A</sub> and P<sub>B</sub>.

For P<sub>B</sub>, the valid range is 0 to 3. For P<sub>A</sub>, valid values are - 6
 dB, - 4.77 dB, - 3 dB, - 1.77 dB, 0 dB, 1 dB, 2 dB, and 3 dB.

Beamforming Weight Matrix: This table is enabled for all the
 Transmission modes, but is relevant only for modes Single-layer beamforming and
 Dual-layer beamforming. The matrix is of size 2 x 8. The range of values is -65536
 to +65535.

The following figure displays the dialog box which appears when a cell is clicked to
 update the phase value. Only entries in the first Rank rows and the first Number of
 Beamforming Antennas columns are used.

[IMAGE alt='image' src='GUID-49A8D52E-44D8-4DDD-9668-3FBF047DBDF7-a5.gif']

PHICH

You can view this window by clicking the PHICH Channel from
 the Channel table and then clicking the
 Edit button.

[IMAGE alt='image' src='GUID-79C93717-A1A6-49C6-9BC1-2DF5D12943A4-a5.gif']

PHICH State: This control allows you to turn off the PHICH
 within the Signal. If the PHICH State control is selected,
 the PHICH Channel will be transmitted. Otherwise, it will not be included in the
 signal. By default, the PHICH State control is selected
 (On).

ACK/NACK Pattern: This control allows you to set a binary bit
 pattern. This pattern configures the ACK/NACK bit that is transmitted. The ACK/ NACK
 bit can be configured for each subframe, and the same bit is used for all PHICH
 sequences and PHICH groups in the subframe.

Maximum Number of Channels: Specifies number of channels in the
 selected subframe of the selected Channel Type.

Channel Index: Specifies the channel index in the selected
 subframe of the selected Channel Type.

Currently, multiple PDSCH channels can be configured per subframe. You need to specify
 the appropriate channel index and then click the Edit utton to
 edit the properties.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=generating-a-mimo-signal.html language=enus -->
## TOPIC 00053: Generating a MIMO Signal

- bundle_id: `rfmx-waveform-creator`
- source_path: `generating-a-mimo-signal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/generating-a-mimo-signal.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a carrier set is configured with the carrier definition that is configured with two antennas, two waveforms are generated for the carrier set. For example, when Carrier Set 0 is configured with Carrier Definition, which is configured to have two antennas, then two waveforms are generated; Carri

### Generating a MIMO Signal

When a carrier set is configured with the carrier definition that is configured with two
 antennas, two waveforms are generated for the carrier set.

For example, when Carrier Set 0 is configured with Carrier Definition, which is
 configured to have two antennas, then two waveforms are generated; Carrier Set 0,
 Antenna0 and Carrier Set 0, Antenna1.

In case of downlink MIMO, the number of outputs of a carrier definition is decided by the
 number of antennas and the number of beamforming antennas.

The following figure illustrates a case of 2 C-RS antennas, 1 PRS antenna port and 8
 beamforming antennas with PDSCH in Transmission Mode 10, where the number of outputs is
 max(2, 8, 1) = 8.

[IMAGE alt='image' src='GUID-B8049EF3-54F5-4D7D-A9E9-5759FEAF8FE7-a5.gif']

The following figure shows a case of 2 C-RS antennas with PDSCH in Transmission Mode 4,
 and with CSI-RS enabled for 1 (beamforming) antenna so that the number of outputs is
 max(2,1,0) = 2.

Note

[IMAGE alt='image' src='GUID-67529890-9D72-4529-A59B-7CE9F90840AC-a5.gif']

In the case of uplink MIMO, the number of outputs of a carrier definition is decided by
 the number of antennas.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=generating-a-user-file.html language=enus -->
## TOPIC 00054: Generating a User File

- bundle_id: `rfmx-waveform-creator`
- source_path: `generating-a-user-file.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/generating-a-user-file.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `task`
- source_description: Generate and import custom user-defined waveform files. You can use RFmx Waveform Creator to package and modify waveform files created with third-party tools. To create a user file, complete the following steps: Select User from the Modulation menu. User Dialog Box Set the Select IQ source. The avai

### Generating a User File

Generate and import custom user-defined waveform files.

You can use RFmx Waveform
 Creator to package and modify waveform files
 created with third-party tools. To create a user file, complete the following
 steps:

1. Select User from the Modulation
 menu. 
 [IMAGE alt='User Dialog Box' src='GUID-962BAF26-F86D-4490-B46B-7F14FBE8F17F-a5.png']
2. Set the Select IQ source. The available formats are
 User IQ File and User I and Q
 File.
3. Provide the filename(s) of the file(s) you want to use in the IQ
 File or I File and Q File fields.
4. Set values for Sample Rate, Oversampling factor, and
 Signal Bandwidth controls.
5. Define Filter and IQ Impairments
 settings, as required.

Parent topic:

RFmx Waveform Creator Modulation Schemes

#### File Formats

RFmx Waveform
 Creator supports multiple IQ file data formats, allowing you to
 load a single IQ file or separate I and Q files. The
 supported file formats include:

- ASCII : The ASCII format comprises of floating-point numbers
 separated by commas, spaces or tabs, line feeds or carriage returns.
- 32-bit Float : The float format uses the IEEE single-precision
 format. This format is represented by four bytes consisting of a sign bit, an 8-bit
 excess-127 binary exponent, and a 23-bit mantissa. The mantissa represents a number
 between 1.0 and 2.0. Since the high-order bit of the mantissa is always 1, it is not
 stored in the number. This representation gives a range of approximately 3.4E-38 to
 3.4E+38.
- 14-bit Signed Integer : Refers to a 16-bit twos-complement
 representation. In the Little Endian format, this is the default for Intel-based
 machines. Each integer is interpreted as 14-bit signed with a range of -8192 to
 8191. This indicates that, the two most significant bits are masked out with the
 14-bit integer sign extended to retain the twos-complement representation.
- 14-bit Unsigned Integer : Refers to 16-bit integers. In the
 Little Endian format, this is the default for Intel-based machines. Each integer is
 interpreted as 14-bit unsigned with a range of 0 to 16383. This indicates that, the
 two most significant bits are masked out.
- 16-bit Signed Integer : Refers to a 16-bit twos-complement
 representation with a range of -32768 to 32767. In the Little Endian format, this is
 the default for Intel-based machines.
- 16-bit Unsigned Integer : Refers to values with a range of 0
 to 65535. In the Little Endian format, this is the default for Intel-based
 machines.
- 32-bit Signed Integer : Refers to a 32-bit twos-complement
 representation with a range of -2147483648 to 2147483647. In the Little Endian
 format, this is the default for Intel-based machines.
- 32-bit Unsigned Integer : Refers to values with a range of 0
 to 4294967295. In the Little Endian format, this is the default for Intel-based
 machines.

<!--NI_TOPIC bundle=rfmx-waveform-creator path=generating-a-waveform.html language=enus -->
## TOPIC 00055: Generating a Waveform

- bundle_id: `rfmx-waveform-creator`
- source_path: `generating-a-waveform.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/generating-a-waveform.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Once you have set up the forward channel and the channel filter to suit your needs, you can generate the waveform in the same way as for other modulation schemes. Select the Save Waveform File menu and proceed as described in the RFmx Waveform Creator Help document.

### Generating a Waveform

Once you have set up the forward channel and the channel filter to suit your needs, you
 can generate the waveform in the same way as for other modulation schemes. Select the
 Save Waveform File menu and proceed as described in the
 RFmx Waveform Creator Help document.

Parent topic:

TD-SCDMA (3GPP TDD-LCR)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=generating-and-saving-the-waveform-file.html language=enus -->
## TOPIC 00056: Generating and Saving the Waveform File

- bundle_id: `rfmx-waveform-creator`
- source_path: `generating-and-saving-the-waveform-file.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/generating-and-saving-the-waveform-file.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Waveform Creator provides you with two options to save your files: To save your settings, refer to Saving your Settings topic. To save the waveform, refer to Saving the Waveform File topic. Saving your Settings The parameters that you have set up to create your waveform may be saved to a file f

### Generating and Saving the Waveform File

RFmx Waveform Creator provides you with two options to save your files:

- To save your settings, refer to Saving your Settings topic.
- To save the waveform, refer to Saving the Waveform File topic.

#### Saving your Settings

The parameters that you have set up to create your waveform may be saved to a file for
 future use and reference. If you archive these settings you will be able to regenerate
 the same waveform at a later date. You can also distribute the saved settings to other
 users of RFmx Waveform Creator so that they can also regenerate the waveform.

To save your current settings, select the menu option
 File»Save or
 File»Save As. If you want to generate
 a file using these settings, keep the settings window open.

The current modulation settings can be stored in the waveform file. For more information,
 please refer to Saving Waveform File.

##### Notes on Save Behavior

- The saved settings file is termed as RFWC file and has the extension
 *.rfws .
- The updated RFmx Waveform Creator modulation schemes that appear under the
 main Modulation menu have a different format from the
 older versions. Although RFmx Waveform Creator supports loading older
 settings files ( .rfwc ), while saving these settings, the
 new file format ( .rfws ) is automatically selected.
- If you save your settings within the RFmx Waveform Creator Examples file
 directory structure, your settings file will be available in the same way as
 the provided example files.

#### Loading Your Settings

To load the modulation settings from a saved file,

- Select File -> Open (ctrl+o) from the
 drop down menu.
- Select the RFWC file (*.rfws) or the waveform file (*.tdms) you want to open.

The most recently opened waveform file appears at the bottom of the
 File tab. You can also open the recent file by clicking on
 the path of the file.

##### Notes on Settings Behavior

Store
 Configuration

- If the settings are not present in the waveform file, you will be notified
 with an error message.
- Loading the waveform file which is generated from WLAN or Bluetooth is not
 supported.

#### File Summary

The File Summary dialog box provides you the following additional information about the
 waveform that you generated.

Signal Bandwidth - Calculation of the signal bandwidth depends
 on the waveform configuration you make in the Modulation
 window.

Number of Samples - Specifies the number of samples in the
 generated signal.

Sampling Rate - Specifies the sampling rate of the generated
 signal.

PAPR (dB) - Calculation of the PAPR of the generated signal
 depends on the waveform configuration you make in the
 Modulation window.

The File Summary dialog box is depicted in the following image.

[IMAGE alt='image' src='GUID-0664EBDE-9F9A-43DB-9CCC-D76C0D877363-a5.png']

#### Download & Play

The Download & Play feature enables you to download the waveform created by the RFmx
 Waveform Creator and play it on any NI hardware.

Click Instrument and select Download &
 Play to open the dialog box as shown in the following image.

[IMAGE alt='image' src='GUID-D6B1D3BD-2CC1-46D6-BEB3-1B5A7BC27C56-a5.png']

Note

Download & Play

##### Configuring Download & Play

RFmx
 Waveform Creator provides the following controls. Enter the required parameters
 before you play the waveform on the hardware.

Device
 Name – Lists the devices which are configured in NI-MAX.

When
 you select a device, internally an RFSG session is opened for the device. This
 session automatically closes when you select another device, click No
 Device, or close the Download & Play
 window.

Center Frequency, External Attenuation, Reference Source,
 Frequency, and Markers : Values that you set on these controls are
 configured to the selected device.

- When the device name is changed, and
- When you click Create & Play

During waveform play, the values are also applied on the
 fly.

Power Level: Specifies the average power level
 of generated RF signal in dBm.

Note

pk-pk

Upconverter Frequency Offset Mode – Sets
 the upconverter frequency offset mode to NI hardware. The possible values are Auto
 and User Defined. The default value is Auto. Refer to the
 NI-RFSG help for more information.

LO Source – Sets the
 LO source to NI hardware. The possible values are Onboard, LO In, Secondary,
 SG_SA_Shared, and Automatic_SG_SA_Shared. The default value is
 Onboard. Refer to the NI-RFSG help for more information
 on LO source.

Note

Automatic_SG_SA_Shared

LO2 Source (LO in PXIe-5830/5831/5832)
 – Sets the LO2 source to NI hardware. The possible values are Onboard, LO In,
 Secondary, SG_SA_Shared, and Automatic_SG_SA_Shared. The default value is
 Onboard. This control is enabled only on selecting
 PXIe-5830/5831/5832 devices. Refer to the NI-RFSG help for more information on LO
 Source attribute.

Selected Port – Provides the list of
 available ports by reading available ports driver API and helps on setting the
 desired port. The default value is if0. This control is
 enabled only on selecting 3622 devices. Refer to the NI-RFSG help for more
 information on selected ports and available ports.

Signal
 Bandwidth – Based on the waveform configuration set in the
 Modulation window, the signal bandwidth is calculated and
 set to this control when you click Create & Play. This is
 a read-only control.

Sampling Rate – Based on the
 waveform configuration set in the Modulation window, the
 sampling rate is calculated and set to this control when you click Create
 & Play. This is a read-only control.

Runtime
 Scaling – Sets the value to runtime scaling property. The default
 value is -1.5 dB.

PAPR – Based on the waveform
 configuration from the Modulation window, PAPR is calculated
 and set to this control when you click Create & Play.
 This is a read-only control.

Create & Play –

- When you select the device, a valid session is opened and the Create
 & Play button is enabled.
- When you select No Device from the list of device names,
 the Create & Play button is disabled.
- When you configure the selected device and click the Create &
 Play button, the waveform from the active modulation window's
 configuration is generated, download to the device, and played on the
 device.

Stop – Aborts waveform generation and provides an option
 to resume the waveform generation.

Waveform generation is also aborted, if you
 close the window, change the device name, or on an error condition from the selected
 device.

Resume – Waveform generation will resume using
 the waveform already downloaded in the device memory.

Status
 Textbox – Displays status, warning, and error information about the
 current device session. The window automatically clears the resolved
 errors.

<!--NI_TOPIC bundle=rfmx-waveform-creator path=graph-types.html language=enus -->
## TOPIC 00057: Graph Types

- bundle_id: `rfmx-waveform-creator`
- source_path: `graph-types.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/graph-types.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following graph types are available in RFmx Waveform Creator: IQ FFT IQ Vector IQ vs Time Power vs Time Phase vs Time Freq vs Time IQ vs Time (Wrapped) Constellation CCDF (Complementary Cumulative Distribution Function) Code Domain The Code Domain graph type is available for CDMA modulation sche

### Graph Types

The following graph types are available in RFmx Waveform Creator:

- IQ FFT
- IQ Vector
- IQ vs Time
- Power vs Time
- Phase vs Time
- Freq vs Time
- IQ vs Time (Wrapped)
- Constellation
- CCDF (Complementary Cumulative Distribution Function)
- Code Domain

Note

#### FFT

This graph type calculates the power spectral density estimation of the waveform.

To create or open an IQ FFT plot settings,

1. Select any modulation schemes from the Modulation menu.
2. Click Graphics tab.
3. Select IQ FFT from the Measurements 
 drop-down menu.
4. Click Regenerate Plot .

The resultant plot with default settings is as shown in the following figure.

[IMAGE alt='image' src='GUID-85F13048-7F37-4CA5-87FE-6847BEF0AB70-a5.png']

The FFT measurement enables three controls under the Trace
 Controls menu:

Reset FFT

When zooming into specific time-based traces, such as IQ vs Time,
 or Frequency vs Time; the graphics page will show details of the
 zoomed region of the signal, which means that the FFT is performed only on specific
 regions of the signal. This can be seen by looking at the FFT details shown at the top
 right of the graph graticule. The Reset FFT control allows you to
 reset the FFT measurement so it applies to the entire signal.

Apply Window

This control allows you to control whether or not the incoming signal will be windowed as
 part of the FFT process. When selecting/unselecting this option, you will need to
 re-generate the signal to see the effects.

Display FFT Information

This will toggle the FFT information display is shown at the top right of the graph
 graticule.

#### IQ Vector

To create or open a settings page,

1. Select any modulation schemes from the Modulation menu.
2. Click Graphics tab.
3. Select Vector from the Measurements 
 drop-down menu.
4. Click Regenerate Plot .

The resultant plot with default settings is as shown in the following figure.

[IMAGE alt='image' src='GUID-C87AF809-CE66-47C5-AC48-0B6529FEB15F-a5.png']

The IQ Vector measurement enables three controls under the Trace
 Controls menu:

Decimate Samples

This control allows to plot only a portion of the signal up to a maximum of 1500 points
 when a new signal is generated. While this can speed up the plotting process, it may
 cause spurious points to be shown when vector lines are enabled.

Show Vector Lines

This control allows you to turn on/off the lines that join the individual vector points.
 When this control is unselected, the individual points of the vector will be
 enlarged.

Reset Samples

When zooming into specific time-based traces, such as IQ vs. Time,
 or Frequency vs. Time, the graphics page will show details of the
 zoomed region of this signal, which means that the FFT is performed only on specific
 regions of the signal. This can be seen by looking at the FFT details shown at the top
 right of the graph graticule. The Reset Samples control allows
 you to reset the IQ Vector measurement, so it applies to the entire signal.

#### IQ vs Time

The in-phase(I) and quadrature(Q) components of a signal are shown as a function of
 time.

To create or open an IQ vs Time plot settings,

1. Select any modulation schemes from the Modulation menu.
2. Click Graphics tab.
3. Select IQ vs Time from the
 Measurements drop-down menu.
4. Click Regenerate Plot .

The resultant plot with default settings is as shown in the following figure.

[IMAGE alt='image' src='GUID-DC9F0B76-A46C-44FC-8512-C489ED943F4C-a5.png']

The IQ vs Time measurement enables a few controls under the Trace
 Controls menu:

Decimate Samples

This control allows to plot only a portion of the signal up to a maximum of 1500 points
 when a new signal is generated. This can speed up the plotting process for large
 signals, but will cause some of the underlying I and Q data to be hidden.

Show I

Enables the I portion of the signal is shown on the trace.

Show Q

Enables the Q portion of the signal is shown on the trace.

#### Phase vs Time

This graph type displays the phase of the signal, as a function of time.

To create or open a settings page,

1. Select any modulation schemes from the Modulation menu.
2. Click Graphics tab.
3. Select Phase vs Time from the
 Measurements drop-down menu.
4. Click Regenerate Plot .

The resultant plot with default settings is as shown in the following figure.

[IMAGE alt='image' src='GUID-18C44180-5E06-4E2C-9C0E-2D8784011A59-a5.png']

The Phase vs Time measurement enables three controls under the Trace
 Controls menu:

Decimate Samples

This control allows to plot only a portion of the signal up to a maximum of 1500 points
 when a new signal is generated. This can speed up the plotting process for large signals
 but will cause some of the underlying I and Q data to be hidden.

#### Power vs Time

This graph type displays the magnitude of the signal, in separate graphs, as a function
 of time.

To create or open a settings page,

1. Select any modulation schemes from the Modulation menu.
2. Click Graphics tab.
3. Select Phase vs Time from the
 Measurements drop-down menu.
4. Click Regenerate Plot .

The resultant plot with default settings is as shown in the following figure.

[IMAGE alt='image' src='GUID-BDDFC10C-FDCC-448B-83A0-12DC851AA430-a5.png']

The Power vs Time measurement enables a few controls under the Trace
 Controls menu:

Decimate Samples

This control allows to plot only a portion of the signal up to a maximum of 1500 points
 when a new signal is generated. This can speed up the plotting process for large signals
 but will cause some of the underlying I and Q data to be hidden.

#### Frequency vs Time

This graph type displays the instantaneous frequency of the signal as a function of
 time.

To create or open a settings page,

1. Select any modulation schemes from the Modulation menu.
2. Click Graphics tab.
3. Select Phase vs Time from the
 Measurements drop-down menu.
4. Click Regenerate Plot .

The resultant plot with default settings is as shown in the following figure.

[IMAGE alt='image' src='GUID-60E7A71B-B803-4F32-87BA-0AF76E6573D2-a5.png']

The Frequency vs Time measurement enables Decimate Samples control under the
 Trace Controls menu:

Decimate Samples

This control allows to plot only a portion of the signal up to a maximum of 1500 points
 when a new signal is generated. This can speed up the plotting process for large signals
 but will cause some of the underlying I and Q data to be hidden.

#### IQ vs Time (Wrapped)

This plot displays the wrap-round portion of a waveform. It shows the last samples of one
 cycle of the waveform followed by the first samples of the next, when the IQ source is
 continuously output.

A maximum of 100 samples from the end of the signal and 100 samples from the start is
 displayed. Use this plot to assess whether the transition between the start and the end
 of the file is smooth and contains no discontinuity. Discontinuities will result in
 spectral smear.

To create or open a settings page,

1. Select any modulation schemes from the Modulation menu.
2. Click Graphics tab.
3. Select IQ vs Time (wrapped) Plot from the
 Measurements drop-down menu.
4. Click Regenerate Plot .

The resultant plot with default settings is as shown in the following figure.

[IMAGE alt='image' src='GUID-BEFBDE35-93C0-43FE-B4F9-96B47636184B-a5.png']

The IQ vs Time (Wrapped) measurement enables a few controls under the Trace
 Controls menu:

Show I

Enables the I portion of the signal is shown on the trace.

Show Q

Enables the Q portion of the signal is shown on the trace.

#### Constellation

To create or open a settings page,

1. Select any modulation schemes from the Modulation menu.
2. Click Graphics tab.
3. Select Constellation from the
 Measurements drop-down menu.
4. Set the scaling properties. You can either select Auto
 Scaling or define your own values.
5. Click Regenerate Plot .

The resultant plot with default settings is as shown in the following figure.

[IMAGE alt='image' src='GUID-2701B1F3-A1F3-4972-B905-C27AB71530D4-a5.png']

The Constellation measurement enables Reset Samples control under
 the Trace Controls menu:

Reset Samples

When zooming into specific time-based traces, such as IQ vs Time,
 or Frequency vs Time; the graphics page will show details of the
 zoomed region of the signal, which means that the FFT is performed only on specific
 regions of the signal. This can be seen by looking at the FFT details shown at the top
 right of the graph graticule. The Reset FFT control allows you to
 reset the FFT measurement so it applies to the entire signal.

#### CCDF

A Complementary Cumulative Distribution Function (CCDF) graph is a plot of relative power
 levels against probability. The graph shows the probability that the power is equal to
 or above a certain peak-to-average power ratio, for different probabilities and
 peak-to-average power ratios. Peak-to-average power is calculated for generated signal
 excluding OFF power period. The higher the peak-to-average power ratio, the lower the
 probability of reaching it. The x-axis represents the power level above the average
 power and the y-axis represents the percent of time the signal power is at or above the
 power specified by the x-axis. For example, at 10%, the corresponding peak-to-average
 power is 3.60 dB. This means the signal power exceeds the average by 1.88 dB for 10% of
 the time. The legend on the right-hand side identifies power levels associated with
 certain probabilities, except for Peak as this represents the crest factor of the
 curve.

Calculating CCDF

This is a 2-stage process, where the Probability Distribution Function (PDF) is used to
 compute the Cumulative Distribution Function (CDF) by computing the integral of the PDF.
 The CDF is then used to compute the CCDF by inverting the CDF result. The CCDF is
 plotted instead of CDF because a CCDF plot emphasizes peak amplitude excursions.

Create or open a settings page,

1. Select any modulation schemes from the Modulation menu.
2. Click Graphics tab.
3. Select CCDF from the Measurements 
 drop-down menu.
4. Set the scaling properties. You can either select Auto
 Scaling from the Zoom drop-down menu or
 define your own values.
5. Click Regenerate Plot .

The resultant plot with default settings is as shown in the following figure.

[IMAGE alt='image' src='GUID-33C78CD2-9CE3-4F55-B582-F02A7F67F998-a5.png']

The CCDF measurement enables few controls under the Trace Controls
 menu:

Reset Samples

When zooming into specific time-based traces, such as IQ vs Time,
 or Frequency vs Time; the graphics page will show details of the
 zoomed region of the signal, which means that the FFT is performed only on specific
 regions of the signal. This can be seen by looking at the FFT details shown at the top
 right of the graph graticule. The Reset FFT control allows you to
 reset the FFT measurement so it applies to the entire signal.

Display Annotation

This will toggle the CCDF information display shown at the top right of the graph
 graticule.

#### Code Domain

This graph type is currently only available for CDMA modulation schemes. This graph type
 shows all active channels in the code domain. The graph shows whether assigned code
 domains of different channels overlap; that is, whether a domain conflict occurs. The
 symbol rates of code channels are characterized by the color and widths of the
 corresponding bars. The information at the right of the graph indicates the colors used
 to represent symbol rates. The heights of the bars represent the channel codesâ€™ power
 level.

To create or open a Code Domain plot settings,

1. Select CDMA2k from the Modulation 
 menu.
2. Click the Graphics tab in the CDMA2k 
 settings window.
3. Select Code Domain from the
 Measurements drop-down menu.
4. Click Regenerate Plot .

Note

<!--NI_TOPIC bundle=rfmx-waveform-creator path=graphs.html language=enus -->
## TOPIC 00058: Plotting Graphs

- bundle_id: `rfmx-waveform-creator`
- source_path: `graphs.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/graphs.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Graphics tab to view and save graphical representations of the waveform that you have set up. The typical graphics setup is as shown in the following figure. The Measurements menu allows you to select different types of plots. For example, if you want to view a spectrum of the waveform you ar

### Plotting Graphs

Select Graphics tab to view and save graphical representations of
 the waveform that you have set up. The typical graphics setup is as shown in the
 following figure.

[IMAGE alt='image' src='GUID-B52997D2-0D89-4B6D-AC4F-7C5C602EF834-a5.png']

The Measurements menu allows you to select different types of
 plots. For example, if you want to view a spectrum of the waveform you are creating,
 choose the IQ FFT plot.

To generate graphics data, click Regenerate Plot on the top menu
 bar. This will generate the file and display the data in the graphics plot. After you
 have generated graphics data, you can regenerate at any time, by clicking on this
 option. You can save or print the resulting plot if required. An example vector plot of
 a 16 QAM signal is shown in the following figure. You are able to zoom and set up
 markers.

[IMAGE alt='image' src='GUID-E518C85A-5286-4FFA-8E43-33F8222A54A1-a5.png']

#### Trace Controls

This sub-menu enables you to turn on and off different traces in the graph independently.
 This option is only available if there are more than one independent trace running for
 the given graph, for example, I and Q traces.

[IMAGE alt='image' src='GUID-9E2B559C-D24B-445C-A34D-5D19038E673A-a5.png']

#### Axis Controls

The Axis Control drop-down menu allows you to change the units of
 the X or Y axis only for time or frequency.
 Depending on the type of graph, the Frequency and
 Time options are available in the Axis
 Control drop-down menu.

The Frequency menu will allow you to change the axis units to Hz,
 kHz, MHz, GHz, or THz.

The Time menu will allow you to change the axis units to s, ms,
 us, or ns.

You can select Auto to automatically select the appropriate axis
 scaling for the given graph.

#### Export

Once trace data has been created, there are several ways of exporting information about
 the trace for use outside RFmx Waveform Creator. The supported export features are as
 follows:

Print: Print the complete trace including axis marker read-out to
 any printer currently accessible to windows.

Copy Image to Clipboard: Copies the complete trace, including axis
 and marker read-out to the windows clipboard, which can then be used to paste the bitmap
 into other applications.

Export as Bitmap: Export the complete trace, including axis and
 marker read-out to a bitmap. Selecting this option will prompt you to select a file.

<!--NI_TOPIC bundle=rfmx-waveform-creator path=gsm-references.html language=enus -->
## TOPIC 00059: GSM References

- bundle_id: `rfmx-waveform-creator`
- source_path: `gsm-references.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/gsm-references.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: References 3GPP TS 45.001 Physical layer on the radio path; General description 3GPP TS 45.002 Multiplexing and multiple access on the radio path 3GPP TS 45.003 Channel coding 3GPP TS 45.004 Modulation 3GPP TS 45.010 Radio subsystem synchronization 3GPP TS 45.060 Radio Link Control/Medium Access Con

### GSM References

References

| 3GPP TS 45.001 | Physical layer on the radio path; General description |
| --- | --- |
| 3GPP TS 45.002 | Multiplexing and multiple access on the radio path |
| 3GPP TS 45.003 | Channel coding |
| 3GPP TS 45.004 | Modulation |
| 3GPP TS 45.010 | Radio subsystem synchronization |
| 3GPP TS 45.060 | Radio Link Control/Medium Access Control (RLC/MAC) protocol |

Parent topic:

GSM/EDGE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=gsmedge-overview.html language=enus -->
## TOPIC 00060: GSM/EDGE

- bundle_id: `rfmx-waveform-creator`
- source_path: `gsmedge-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/gsmedge-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creates a waveform that simulates a GSM/EDGE signal. The modulation scheme is defined in the GSM/EDGE 3GPP specifications, based on the GMSK and 8PSK modulation. The EDGE modulation facility enables you to produce a waveform that simulates an enhanced data for GSM evolution cellular mobile phone TDM

### GSM/EDGE

Creates a waveform that simulates a GSM/EDGE signal.

The modulation scheme is defined in the *GSM/EDGE 3GPP* specifications, based
 on the GMSK and 8PSK modulation.

The EDGE modulation facility enables you to produce a waveform that simulates an enhanced
 data for GSM evolution cellular mobile phone TDMA signal. You can generate test signals
 with EDGE bursts in any slot.

GSM uses time division multiple access (TDMA) and frequency division multiple access
 (FDMA) along with frequency hopping for multiple access scheme. The receiver and
 transmitter frequencies are always duplex frequencies. Frequency band is internally
 divided into set of carrier frequencies in frequency domain. Each of these carrier
 frequencies are separated by 200 kHz frequency band. Each carrier has eight basic
 physical channels.

A burst or a time slot is a basic radio resource in TDMA. The time slot or the burst
 lasts for approximately 0.577 ms and carries 156.25 symbols of information including
 guard period. The implementation adopts the method described in section 5.7 of
 3GPP TS 45.010 specification where a timeslot length of 157
 symbols is used in timeslots 0 and 4 and a timeslot length of 156 symbols is used in the
 remaining timeslots. This is achieved by having a long guard period at the end of the
 burst in slots 0 and 4, and a standard guard period for all the other slots.

[IMAGE alt='image' src='GUID-F2404C0A-2B0C-41B6-BDAC-1D91EED331D0-a5.gif']

Note

Generating and Saving the Waveform
 File

Parent topic:

RFmx Waveform Creator Modulation Schemes

Related information:

- RFmx GSM/EDGE .NET Reference
- RFmx GSM/EDGE C API Reference

<!--NI_TOPIC bundle=rfmx-waveform-creator path=GUID-40A48804-0DEC-468C-B7E3-1CD09D987F2F.html language=enus -->
## TOPIC 00061: RFSG Database

- bundle_id: `rfmx-waveform-creator`
- source_path: `GUID-40A48804-0DEC-468C-B7E3-1CD09D987F2F.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/GUID-40A48804-0DEC-468C-B7E3-1CD09D987F2F.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFSG database is a feature that allows you to store and retrieve various properties associated with a particular waveform. You can create multiple waveforms for a particular standard and download these waveforms to the arbitrary waveform generator (AWG) memory. You can then generate all these wa

### RFSG Database

The RFSG database is a feature that allows you to store and retrieve various properties associated with a particular waveform.

You can create multiple waveforms for a particular standard and download these waveforms to the arbitrary waveform generator (AWG) memory. You can then generate all these waveforms using either a single script or multiple scripts. You must set the appropriate NI-RFSG properties that correspond to the waveform being generated. Use the RFSG database to retrieve the properties for the waveform being generated.

Currently, the toolkit stores the I/Q rate and headroom properties for each waveform. The toolkit requires that the I/Q rate of all the waveforms be the same so that you can generate the waveforms using a single script. The toolkit selects the minimum headroom value and applies it to all waveforms. You can add more properties to the RFSG database to track more NI-RFSG properties per waveform.

If you want to generate a waveform from a specific standard, the toolkit configures the necessary NI-RFSG properties to do this task. These properties are global with respect to the driver. Hence, the values of the properties apply to all waveforms. However, this behavior may be an issue if you want to generate waveforms that have different values or properties associated with them. For example, assume that you want to generate waveform 1, waveform 2, and then waveform 1 again. In this case, each time a new waveform is generated, you must reconfigure the driver for that waveform, even if you have already configured it.

By using the RFSG database, you can store the required properties for each waveform in the database and then query them later while generating those waveforms.

Parent topic:

Bluetooth

<!--NI_TOPIC bundle=rfmx-waveform-creator path=GUID-7C8F76F4-4426-412B-BB1D-F08004FD2F9E.html language=enus -->
## TOPIC 00062: Bluetooth® Packet Header Details

- bundle_id: `rfmx-waveform-creator`
- source_path: `GUID-7C8F76F4-4426-412B-BB1D-F08004FD2F9E.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/GUID-7C8F76F4-4426-412B-BB1D-F08004FD2F9E.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Bluetooth® packet header for BR and EDR packets contains the link control (LC) information, which consists of the following fields: LT-ADDR: 3-bit logical transport address TYPE: 4-bit type code FLOW: 1-bit flow control ARQN: 1-bit acknowledge indication SEQN: 1-bit sequence number HEC: 8-bit he

### Bluetooth® Packet Header Details

The Bluetooth® packet header for BR and EDR packets contains the link control (LC)
 information, which consists of the following fields:

- LT-ADDR: 3-bit logical transport address
- TYPE: 4-bit type code
- FLOW: 1-bit flow control
- ARQN: 1-bit acknowledge indication
- SEQN: 1-bit sequence number
- HEC: 8-bit header error check

Parent topic:

Bluetooth

<!--NI_TOPIC bundle=rfmx-waveform-creator path=GUID-F5BC1930-9710-4EB0-9884-8D7A2CD5C26C.html language=enus -->
## TOPIC 00063: Antenna Switching for LE Direction Finding Packets

- bundle_id: `rfmx-waveform-creator`
- source_path: `GUID-F5BC1930-9710-4EB0-9884-8D7A2CD5C26C.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/GUID-F5BC1930-9710-4EB0-9884-8D7A2CD5C26C.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Antenna Switching for LE Direction Finding Packets The NI Bluetooth Generation Toolkit enables the phase and amplitude modulation on per transmit slot basis in the constant tone extension (CTE) field of LE packet resulting in the emulation of different paths taken by the CTE portion through the RF S

### Antenna Switching for LE Direction Finding Packets

Antenna Switching for LE Direction Finding Packets

The NI Bluetooth Generation
 Toolkit enables the phase and amplitude modulation on per transmit slot basis in the constant
 tone extension (CTE) field of LE packet resulting in the emulation of different paths taken by
 the CTE portion through the RF Switch and different antennas in the DUT.

[IMAGE alt='image' src='GUID-326093BD-2FBD-4AE0-9C80-9769748A47E7-a5.png']

Figure 1 - Transmission of CTE field through elements of antenna array

The IQ Samples Dynamic Range, AoD Receiver Test requires that a variable attenuation be
 applied on the line while sending a packet with a CTE field, such that the input power level to
 the receiver is set to the values for each antenna. The toolkit allows you to specify the phase
 value per slot in addition to the amplitude values.

Refer to LabVIEWÂ»ExamplesÂ»RF ToolkitÂ»BTÂ»GenerationÂ»niBT Generate LE-TP Packet Example or
 DocumentsÂ»National InstrumentsÂ»Bluetooth ToolkitÂ»ExamplesÂ»CÂ»GenerationÂ»Generate LE-TP
 Packet which shows the antenna switching capabilities in the Bluetooth Toolkit.

Configuring the Direction Finding attributes for Antenna Switching Emulation:

Antenna Switching emulation is applicable when the Direction Finding Mode property is set to
 either Angle of Arrival or Angle of Departure . To enable the antenna switching emulation, set
 the Antenna Switching Enabled property to True .

Valid Antenna Switching Patterns:

1. For example if the Number of Antennas is set to 4, there are two supported antenna switching pattern formats:
 
 
 
 Some examples of invalid patterns for the above configurations include: A0-A1A2A3, A-A1-A2-A3, A-0-A1-A2-A3.
  1. A0A1A0A0A0A2A0A0A0A3A0A0
  2. A0-A1-A2-A3
2. The only valid characters in the pattern are A, 0 to 255 and -.
3. The pattern must include all the valid Antenna Indices. For Number of Antennas set to 4, the antenna pattern must include all the antenna indices from 0 to 3.

If the antenna switching pattern is exhausted before the end of the CTE field, it shall be
 repeated from the beginning. If the pattern has not been completely used by the end of the
 Constant Tone Extension, any remaining terms shall be ignored. This is according to the
 definition present in the Section 5.1, Vol 6, Part A of the
 Bluetooth Core
 Specification Version 5.1.

Configuring Relative Amplitude and Relative Phase Values

The phase and amplitude values of the non-reference antenna are specified with respect to the
 reference antenna A0. The number of elements in these array properties must be at least
 Number of Antennas - 1
 . The first element of the Relative Phase (deg) array property
 corresponds to the phase of antenna A1, the second element of the array corresponds to phase of
 antenna A2, and so on. Similarly, the first element of the Relative Amplitude (dBm) array
 property corresponds to the amplitude of antenna A1, the second element of the array corresponds
 to amplitude of antenna A2, and so on.

Average power of the reference antenna A0 is equal to the average power of the portion of the
 LE packet before the Constant Tone Extension field. This power level is configured through the
 niRFSG Power Level property or the NIRFSG_ATTR_POWER_LEVEL attribute.

The Guard period and switching slots in the CTE field are utilized to make transitions from
 one phase value to another and from one amplitude level to another for the duration reported by
 the Antenna Switching Duration Used (s) property. The Antenna Switching Duration Used (s)
 property is derived using the Oversampling Factor and Antenna Switching Duration (s) properties.

For an antenna switching pattern of A0-A1-A0-A0-A0-A2-A0-A0-A0-A3 and CTE slot duration of
 1us, an example of a plot of amplitude transitions is as shown in the following image.

[IMAGE alt='image' src='GUID-719F4EF6-B619-4E43-A75B-B54238966B3B-a5.png']

Figure 2 - Amplitude response in the CTE field when Antenna Switching emulation is enabled

Parent topic:

Bluetooth

<!--NI_TOPIC bundle=rfmx-waveform-creator path=internet-of-things-overview.html language=enus -->
## TOPIC 00064: Internet of Things Overview

- bundle_id: `rfmx-waveform-creator`
- source_path: `internet-of-things-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/internet-of-things-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Internet of things (IoT) is a system of interconnected computing devices embedded in everyday physical objects. IoT connectivity standards enable these devices to send and receive data via existing internet infrastructure. The primary end-user requirements for these devices are low cost and reduced

### Internet of Things Overview

Internet of things (IoT) is a system of interconnected computing devices embedded in
 everyday physical objects. IoT connectivity standards enable these devices to send and
 receive data via existing internet infrastructure.

The primary end-user requirements for these devices are low cost and reduced power
 consumption. Personal Area Network (PAN) and Wireless Local Area Network (WLAN)
 technologies meet the cost and power requirements for IoT connectivity. However, these
 technologies have less coverage. Wide coverage is one of the key requirements for many
 emerging IoT use cases. The existing cellular standards have wide coverage but because
 of the complexity, results in higher cost devices and more power consumption.

To ensure IoT devices cost less, consume low power and have wide coverage; low power wide
 area (LPWA) technologies like narrowband internet of things (NB-IoT) and enhanced
 machine type communication (eMTC) were developed by 3GPP. While eMTC was developed on
 top of existing LTE infrastructure, NB-IoT was developed as a new radio interface with
 some similarities to LTE.

Note

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=introduction-to-amplitude-modulation.html language=enus -->
## TOPIC 00065: Introduction to Amplitude Modulation

- bundle_id: `rfmx-waveform-creator`
- source_path: `introduction-to-amplitude-modulation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/introduction-to-amplitude-modulation.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: With amplitude modulation (AM), you vary the amplitude of an RF carrier signal according to the amplitude of the message signal. Amplitude modulation generates discrete upper and lower sidebands, which are the sum and difference between frequencies of the message signal and the carrier signal. A ben

### Introduction to Amplitude Modulation

With amplitude modulation (AM), you vary the amplitude of an RF carrier signal
 according to the amplitude of the message signal.

Amplitude modulation generates discrete upper and lower sidebands, which are the sum and
 difference between frequencies of the message signal and the carrier signal.

A benefit of the amplitude modulation system is the ease with which the baseband message
 signal can be recovered by demodulation.

The following figure illustrates the modulation of a carrier signal with amplitude
 A<sub>C</sub> (Figure a) by a baseband message signal (Figure b). The result is the
 modulated wave (Figure c).

[IMAGE alt='image' src='GUID-940800C1-6DFD-4C69-80D3-EEB85796AA83-a5.gif']

The transmitted signal shown in Figure c is explained by the following equation:

v

(

t

)

=

A

C

[

1

+

m

(

t

)

]

⁢

cos

(

2

π

f

C

t

)

where

- m(t) is the time-varying modulation.
- t is the sampling time instant.
- A C is the amplitude of the carrier signal.
- f c is the frequency of the carrier signal.

Parent topic:

Analog Modulation

<!--NI_TOPIC bundle=rfmx-waveform-creator path=introduction-to-cdma2k.html language=enus -->
## TOPIC 00066: Introduction to CDMA2k

- bundle_id: `rfmx-waveform-creator`
- source_path: `introduction-to-cdma2k.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/introduction-to-cdma2k.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: CDMA2k is a standard for 3G wireless technology that is derived from cdmaOne (IS95). Signals are specified by radio configurations. Two chip rates are supported on the reverse link; 1.2288 Mchips/sec (spreading rate 1) and 3.6864 Mchips/sec (spreading rate 3). Currently only spreading rate 1 is supp

### Introduction to CDMA2k

CDMA2k is a standard for 3G wireless technology that is derived from cdmaOne (IS95).
 Signals are specified by radio configurations. Two chip rates are supported on the
 reverse link; 1.2288 Mchips/sec (spreading rate 1) and 3.6864 Mchips/sec (spreading rate
 3). Currently only spreading rate 1 is supported on the downlink.

CDMA2k Reverse (Uplink) Channels

1. Access Channel (ACH) 
 This is a slotted random access channel that is used for short signaling message
 exchanges with the base station. For example, call origination.
2. Reverse traffic channel 
 The reverse traffic channel is composed of up to one reverse dedicated control
 channel (DCCH) (radio configurations 3 to 4), up to one reverse fundamental
 channel (FCH), zero to two reverse supplemental channels (SCH) (only for radio
 configurations 3 and 4) and zero to seven reverse supplemental code channels
 (SCCH) (only for radio configurations 1 and 2). Note that RFmx Waveform Creator
 does not currently support reverse supplemental code channels.
3. Enhanced access channel (EACH) 
 The enhanced channel is used for transmission of short messages, such as
 signaling, response to pages and call origination. It can also be used to
 transmit moderately sized data packets (only for radio configurations 3 and
 4).
4. Reverse common control channel (CCCH) 
 This is the portion of the reverse channel that is used for the transmission of
 digital control information from one or more mobile stations to a base station.
 This is only available in radio configurations 3 and 4.
5. Reverse pilot channel (PICH) 
 This is an unmodulated, direct spread spectrum signal transmitted continuously by
 a mobile station. The reverse pilot channel provides a phase reference for
 coherent demodulation as well as a means for signal strength measurement. Note
 that the pilot channel is part of the reverse common control channel and the
 enhanced access channel. Only present in radio configurations 3 and 4.

Reverse (Uplink) Channels at Spreading Rate 1

There are four radio configurations for the reverse traffic channel at spreading rate 1.
 For completeness, these are given in the following table. These radio configurations
 define the allowed data rates and the modulation scheme.

[IMAGE alt='image' src='GUID-68E3A196-64F0-4B03-8A69-22AD6A3F46F9-a5.gif']

Table 4-1 Radio configurations for the reverse channel

The Channel types supported by RFmx Waveform Creator and that are
 allowed at spreading rate 1 are given in the following table.

[IMAGE alt='image' src='GUID-F36DEC8E-6CF8-497F-A5A8-6C6DEB2D6FE5-a5.gif']

Table 4-2 Channel types per mobile station on the reverse CDMA
 channel for spreading rate 1

The structures for the various reverse channels are given in the following tables. Refer
 to Appendix B for further information regarding symbol rate and data rate for each of
 the channels.

[IMAGE alt='image' src='GUID-9519AF66-00F0-44CD-8785-D30C332FC799-a5.gif']

Fig. 4-1 Channel structure for the access channel for spreading
 rate 1

Note that RFmx Waveform Creator does not currently implement the blocks contained within
 grayed regions shown in the following figure.

[IMAGE alt='image' src='GUID-0C378177-6514-4084-828F-22EDB9893555-a5.gif']

Fig. 4-2 Channel structure for the reverse fundamental channel and
 reverse supplemental code channels (radio configurations 1 and 2)

The long code generators use a user mask (Long code mask) to define the output sequence.
 A combination of short and long codes is used to scramble the data in radio
 configurations 3 and 4 as shown in the following figure.

[IMAGE alt='image' src='GUID-59FF957E-327D-455C-B276-FAC51508EB38-a5.gif']

Fig. 4-3 I and Q mapping for the reverse pilot channel, enhanced
 access channel, reverse common control channel and the reverse traffic channel with
 radio configuration 3 and 4

Reverse (Uplink) Channels at Spreading Rate 3

For spreading rate 3, only radio configurations 5 and 6 are allowed. This implies that
 the allowed channel types are as given in the following figure.

[IMAGE alt='image' src='GUID-78B01875-85EE-4F5A-95D7-9DB1D7C67B15-a5.gif']

Table 4-3 Channel types on the reverse channel for spreading rate 3

The I and Q mapping for the higher spreading rate is given in the following figure. Note
 that in essence this is identical to that given in the above figure. In general, the
 higher data rates are achieved by repeating the Walsh spreading three times for each
 input symbol. Note also that the long code generates data at 3.6864 Mcps as opposed to
 1.2288 Mcps.

[IMAGE alt='image' src='GUID-8E9C10DA-5B50-45E1-BB79-C4E13EBA638C-a5.gif']

Fig. 4-4 I and Q mapping for spreading rate 3

CDMA2k Forward (Downlink) Channels

The forward transmission of CDMA2k consists of several channels. These are:

1. Auxiliary pilot channel (APICH) 
 An unmodulated, direct sequence spread spectrum signal transmitted continuously
 by each CDMA base station. An auxiliary pilot channel is required for forward
 link spot beam and antenna beam forming applications, and provides a phase
 reference for coherent demodulation of those forward CDMA channels associated
 with the auxiliary pilot.
2. Auxiliary transmit diversity pilot channel (ATDPICH) 
 A transmit diversity pilot channel associated with an auxiliary pilot channel.
 These two pilot channels are used to assist with coherent demodulation when
 channels that employ transmit diversity are used. Transmit diversity is not
 supported by RFmx Waveform Creator.
3. Broadcast channel (BCCH) 
 A code channel in a forward CDMA channel used for the transmission of control
 information and pages from a base station to a mobile station. The BCCH is used
 to send control information to mobile stations that have not been assigned to a
 Traffic Channel.
4. Common assignment channel (CACH) 
 A forward common channel used by the base station to acknowledge a mobile station
 accessing the enhanced access channel.
5. Common power control channel (CPCCH) 
 A forward common channel that transmits power control bits to multiple mobile
 stations.
6. Forward common control channel (CCCH) 
 A control channel used for the transmission of digital control information from a
 base station to one or more mobile stations.
7. Forward dedicated control channel (DCCH) 
 A portion of the radio configuration 3 to 9 forward traffic channel that is used
 for the higher level data, control information and power control information
 from a base station to a mobile station.
8. Forward fundamental channel (FCH) 
 A portion of the forward traffic channel that carries a combination of
 higher-level data and power control information. It carries user data, such as
 voice, signaling and low rate data.
9. Forward pilot channel (PICH) 
 An unmodulated, direct sequence spread spectrum signal transmitted continuously
 by each CDMA base station. The PICH allows a mobile to acquire the timing of the
 forward CDMA channel.
10. Forward supplemental channel (SCH) 
 A portion of a radio configuration 3 to 9 forward traffic channel which operates
 in conjunction with a forward fundamental channel or a forward dedicated control
 channel to provide higher data rates.
11. Forward supplemental code channel (SCCH) 
 A portion of a radio configuration 1 and 2 forward traffic channel which operates
 in conjunction with a forward fundamental channel and (optionally) with other
 forward supplemental code channels to provide higher data rates.
12. Paging channel (PCH) 
 A code channel in a forward CDMA channel used for the transmission of control
 information and pages from a base station to a mobile station.
13. Quick paging channel (QPCH) 
 An uncoded, spread and on-off-keying modulated spread spectrum sent by a base
 station to inform mobile stations operating in the slotted mode during the idle
 state whether to receive the forward common control channel or the paging
 channel starting in the next forward common control channel or paging channel
 frame.
14. Sync channel (SYNCH) 
 A code channel in the forward CDMA channel that transmits the synchronization
 message to the mobile station.
15. Transmit diversity pilot channel (TDPICH) 
 An unmodulated, direct spread spectrum signal transmitted continuously by a CDMA
 base station to support forward link transmit diversity. RFmx Waveform Creator
 does not support transmit diversity.

CDMA2k Forward Channels (Downlink) at Spreading Rate 1

There are five radio configurations for the forward traffic channel at spreading rate 1.
 These are given in the following table. The radio configurations define the types of
 channel allowed as well as allowed data rates.

[IMAGE alt='image' src='GUID-39B8AE49-9365-4629-97D9-3161691A9349-a5.gif']

Table 4-4 Radio configurations for the forward channel at spreading
 rate 1

The channel types supported by RFmx Waveform Creator and that that
 are allowed at spreading rate 1 are given in the following table.

[IMAGE alt='image' src='GUID-288E3435-9FD7-4F58-9B4A-589EA740A428-a5.gif']

Table 4-5 Channel types on the forward link for spreading rate 1

The structures for these forward channels are given in Fig. 4-5 through to Fig. 4-6. RFmx
 Waveform Creator does not currently implement blocks within the gray areas shown in
 these figures.

[IMAGE alt='image' src='GUID-A6711A0E-483D-4A2D-AA14-0FCE8EB88935-a5.gif']

Fig. 4-5 Pilot channels, sync channel and paging channels for
 spreading rate 1

[IMAGE alt='image' src='GUID-7DB5D44E-692C-4C54-B837-819F8BE56EDF-a5.gif']

Fig. 4-6 Structure for the broadcast, common assignment and forward
 common control channels for spreading rate 1

Note: In RFmx Waveform Creator the common assignment channel always has a message
 present.

[IMAGE alt='image' src='GUID-62995741-9B7D-447E-8D87-D1138B074C68-a5.gif']

Fig. 4-7 Quick paging channel structure for spreading rate 1

[IMAGE alt='image' src='GUID-8E2C1768-FD0F-46FC-8E7C-6B71A11D4D00-a5.gif']

Fig. 4-8

[IMAGE alt='image' src='GUID-F94CE18B-A517-488F-A024-70EB6BD6C5E0-a5.gif']

Fig. 4-9 Forward traffic channel structure for the forward traffic
 channel with radio configurations 3, 4, and 5

[IMAGE alt='image' src='GUID-B9F49CBF-E428-4DCC-9D9E-088CA1DB841D-a5.gif']

Fig. 4-10 Demultiplexer structure for spreading rate 1

The DEMUX functions distribute input symbols sequentially from the top to the bottom of
 the output paths. The outputs are fed in the following figure.

[IMAGE alt='image' src='GUID-340E8BB2-73F7-4898-A5F8-164EC3C98539-a5.gif']

Fig. 4-11 I and Q mapping (Non-OTD Mode) for spreading rate 1

In the above figure the inputs are spread with a Walsh function that may also be modified
 by a quasi-orthogonal function termed a QOF. This in turn can be modified further by
 rotating the complex vector 90 degrees. A Walshrot value of 0 implies no rotation. A
 value of 1 implies rotate by 90 degrees. All channels are scrambled using a complex
 scrambling code. Note that radio configurations 1 and 2 use the null QOF: in other
 words, the Walsh functions are not altered.

Parent topic:

CDMA2k (3GPP2)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=introduction-to-ev-do-revision-0.html language=enus -->
## TOPIC 00067: Introduction to EV-DO Revision 0

- bundle_id: `rfmx-waveform-creator`
- source_path: `introduction-to-ev-do-revision-0.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/introduction-to-ev-do-revision-0.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: 1 x Evolution Data Optimized (EV-DO) is a packet data system associated with CDMA2k. The chip rate and filters used in this standard are identical to those used in IS-95 and CDMA2k. EV-DO Reverse (Uplink) Channels The reverse link has two physical channels: the Reverse Access Channel and the Reverse

### Introduction to EV-DO Revision 0

1 x Evolution Data Optimized (EV-DO) is a packet data system associated with CDMA2k. The
 chip rate and filters used in this standard are identical to those used in IS-95 and
 CDMA2k.

EV-DO Reverse (Uplink) Channels

The reverse link has two physical channels: the Reverse Access
 Channel and the Reverse Traffic Channel.

Reverse Access Channel

The Reverse Access Channel is used by the access terminal to initiate communication with
 the access network or to respond to an access-terminal-directed message. The Access
 Channel consists of a Pilot Channel and a Data Channel as shown in the following figure.
 RFmx Waveform Creator does not implement the encoding functions contained within gray
 areas.

An Access transmission consists of preamble frames followed by one or more physical layer
 packets. During the preamble, only the Pilot Channel is transmitted. During the access
 packet, both the Data Channel and the Pilot Channel are transmitted. The output power of
 the Pilot Channel is larger during the preamble transmission than in the access packet.
 The total power during each phase is however the same.

[IMAGE alt='image' src='GUID-26FBEB80-A61E-43F2-82BE-8F880BA0B554-a5.gif']

Fig. 5-1 Reverse Channel structure for Access Channel

Reverse Traffic Channel

The Reverse Traffic Channel is used by the access terminal to transmit user-specific data
 to the network. The Reverse Traffic Channel consists of several channels. These are:

1. Pilot/RRI Channel The Reverse Rate Indicator (RRI) Channel is used by the access
 terminal to indicate the rate at which the Data Channel is transmitted. RFmx
 Waveform Creator internally calculates the RRI symbols using the Data Channel’s
 data rate.
2. DRC Channel The Data Rate Control Channel is used by the access terminal to
 indicate to the network the selected serving sector and the requested data rate
 on the Forward Traffic Channel.
3. ACK Channel The ACK Channel is used by the access terminal to inform the access
 network whether a physical layer packet transmitted on the Forward Traffic
 Channel has been received successfully or not. A ‘0’ bit is transmitted if a
 packet has been successfully received; otherwise a ‘1’ is transmitted.
4. Data Channel The Data Channel is the channel on which data is transmitted.

The Reverse Traffic Channel structure is shown in the following figure. Again, encoding
 is not implemented, as indicated by the gray region.

[IMAGE alt='image' src='GUID-6FB265DD-219D-4390-981A-FAA4CD1D654F-a5.gif']

Fig. 5-2 Reverse Channel structure for the Reverse Traffic Channel

EV-DO Forward (Downlink) Channels

The forward link consists of three time-multiplexed channels – the Pilot Channel, the
 Traffic/Control Channel and the MAC (Medium Access Control) Channel. The overall channel
 structure is shown in the following figure. RFmx Waveform Creator does not implement the
 encoding functions contained within the gray area.

[IMAGE alt='image' src='GUID-4B05F1ED-22B7-4D8A-B8CB-7A748E066441-a5.gif']

Fig. 5-3 Forward Link Channel structure

The following figure shows how the time-multiplexing of these channels work on a
 slot-by-slot basis. Each slot has the same structure and there are 16 slots in one
 frame. If no data is transmitted, the slot is inactive and only the Pilot and MAC
 Channels are transmitted.

[IMAGE alt='image' src='GUID-4D5E5617-E785-4EEA-B4FD-9C3EB00D5CE9-a5.gif']

Fig. 5-4 Forward Link Slot structure

Forward Pilot Channel

The Forward Pilot Channel is transmitted in the Pilot Burst of each half slot and is used
 by the access terminal for initial acquisition, phase recovery and timing recovery.

Forward Traffic/Control Channel

The Traffic/Control Channel is transmitted in the two Data Bursts of each half slot. It
 is a packet-based channel with a variable data rate. The following table details these
 data rates and their modulation parameters. Each physical layer packet can be preceded
 by a preamble sequence whose length is dependent upon the data rate. An orthogonal
 32-ary Walsh code spreads the preamble sequence and uniquely identifies the destination
 access terminal. The Walsh code is determined by a MAC Index value in the range 0 to 63.
 RFmx Waveform Creator uses the term user instead of access terminal.

[IMAGE alt='image' src='GUID-042A0F5F-A740-468A-8780-1037FA638534-a5.gif']

Table 5-1 Forward Traffic/Control Channel Modulation Parameters

When a packet is transmitted in more than one slot, a three-slot spacing is used between
 each slot. Physical layer packets for other access terminals (users) can be transmitted
 in these inactive slots. When multiple packets are transmitted to the same access
 terminal (user), a three-slot spacing is used between the last slot of a packet and the
 first slot of the next packet. This gives the access terminal (user) time to acknowledge
 that the packet was successfully transmitted before the next packet is transmitted.

Forward Medium Access Control Channel

The Forward MAC Channel is transmitted in the two MAC Bursts of each half slot and
 consists of three sub-channels – the RA (Reverse Activity) Channel, the RPC (Reverse
 Power Control) Channel and the DRCLock (Data Rate Control) Channel.

Each sub-channel is BPSK modulated onto either I or Q with an orthogonal 64-ary Walsh
 code. Each Walsh code is uniquely identified by a MAC Index value in the range 0 to
 63.

Parent topic:

EV-DO Revision 0

<!--NI_TOPIC bundle=rfmx-waveform-creator path=introduction-to-ev-do-revision-a.html language=enus -->
## TOPIC 00068: Introduction to EV-DO Revision A

- bundle_id: `rfmx-waveform-creator`
- source_path: `introduction-to-ev-do-revision-a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/introduction-to-ev-do-revision-a.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: 1 x Evolution Data Optimized Revision A (EV-DO Rev A) is a revision of the EV-DO specification. Revision A of the specification defines several physical subtypes. They are: Subtype 0 Identical to the physical layer used in EV-DO Rev 0. Subtype 1 Defines an enhanced access channel. Subtype 2 The reve

### Introduction to EV-DO Revision A

1 x Evolution Data Optimized Revision A (EV-DO Rev A) is a revision of the EV-DO
 specification. Revision A of the specification defines several physical subtypes. They
 are:

Subtype 0

Identical to the physical layer used in EV-DO Rev 0.

Subtype 1

Defines an enhanced access channel.

Subtype 2

The reverse link has the enhanced access channel used in subtype 1, and defines an
 enhanced reverse traffic channel. The forward link defines a modified traffic/control
 channel and an enhanced set of MAC channels.

EV-DO Revision A Reverse (Uplink) Channels

The reverse link has two physical channels: the Reverse Access
 Channel and the Reverse Traffic Channel.

Reverse Access Channel

The Reverse Access Channel is used by the access terminal to initiate communication with
 the access network or to respond to an access-terminal-directed message. The Access
 Channel consists of a Pilot Channel and a Data Channel as shown in the following figure.
 RFmx Waveform Creator does not implement any of the encoding, interleaving or repetition
 functions contained within the gray area.

An Access transmission consists of a preamble followed by one or more physical layer
 packets. Physical subtype 0 specifies that the preamble must be an integer number of
 frames in length, whereas physical subtypes 1 and 2 allow the preamble length to be
 specified in slots.

During the preamble, only the Pilot Channel is transmitted. During the access packet,
 both the Data Channel and the Pilot Channel are transmitted. The output power of the
 Pilot Channel is larger during the preamble transmission than in the access packet.

In the original EV-DO specification, data is transmitted at a fixed rate of 9.6 kbps. The
 enhanced access channel used in subtypes 1 and 2 lets data be transmitted at a rate of
 9.6, 19.2 or 38.4 kbps. The data rate is controlled by varying the number of times the
 bits in a packet are repeated. RFmx Waveform Creator does not implement repetition and
 therefore does not provide a means of setting the data rate.

Physical subtype 0 specifies that the total power during the preamble is the same as it
 is during the data portion of the transmission. Physical subtypes 1 and 2 specify that
 the output power of the preamble is independent of the data rate and is set equal to
 that of the data portion transmitted at 9.6 kbps (as in subtype 0). If the data is not
 transmitted at 9.6 kbps, the power level during the data period may be different to the
 power level during the preamble period. When physical subtype 1 or 2 is selected, RFmx
 Waveform Creator lets you set the power during the data period relative to the power
 during the preamble period.

[IMAGE alt='image' src='GUID-C3E4B32C-E481-4B17-922C-E18C6D9FAB12-a5.gif']

Fig. 5-17 Reverse Channel structure for the Access Channel

Reverse Traffic
 Channel

The Reverse Traffic Channel is used by the access terminal to transmit user-specific data
 to the network. The Reverse Traffic Channel consists of several channels. These are:

1. Pilot Channel 
 In physical subtypes 0 and 1 the pilot symbols and reverse rate indicator (RRI)
 symbols are time domain multiplexed onto the same Walsh channel, whereas in
 physical subtype 2, pilot and RRI symbols are transmitted on two separate Walsh
 channels.
2. RRI Channel 
 The Reverse Rate Indicator is used by the access terminal to indicate the rate at
 which the Data Channel is transmitted. RFmx Waveform Creator internally
 calculates the RRI symbols using the payload transmitted on the Data Channel. In
 addition to indicating the rate at which the data is being transmitted, the
 subtype 2 RRI channel transmits a 2-bit symbol indicating the subpacket index of
 the slot being transmitted.
3. Auxiliary Pilot Channel 
 The Auxiliary Pilot Channel is only used with physical subtype 2. The purpose of
 the auxiliary pilot is to provide an additional phase reference. It is used as
 an alternative to increasing the power transmitted on the pilot (which would
 cause the power on the other channels to increase).
4. DRC Channel 
 The Data Rate Control Channel is used by the access terminal to indicate to the
 network the selected serving sector and the requested data rate on the Forward
 Traffic Channel.
5. DSC Channel 
 The Data Source Control Channel is used by the access terminal to indicate to the
 network the selected serving cell on the Forward Traffic Channel. The DSC
 channel is only used in subtype 2 and is time domain multiplexed with the ACK
 channel.
6. ACK Channel 
 The ACK Channel is used by the access terminal to inform the access network
 whether a physical layer packet transmitted on the Forward Traffic Channel has
 been received successfully or not. Subtypes 0 and 1 specify a ‘0’ bit is
 transmitted if a packet has been successfully received; otherwise a ‘1’ is
 transmitted. Subtype 2 specifies that when acknowledging a single-user packet, a
 ‘1’ is transmitted to signify an ACK and a ‘-1’ is transmitted to signify a
 NACK. When acknowledging a multi-user packet, a ‘1’ is transmitted to signify an
 ACK and a ‘0’ is transmitted to signify a NACK.
7. Data Channel 
 The Data Channel is the channel on which data is transmitted. Table 5-42 shows
 the types of modulation used to transmit data. Subtypes 0 and 1 use only B4
 modulation. Subtype 2 may use any of the defined modulation types; the type of
 modulation used is dependent on the rate at which the data is transmitted.

[IMAGE alt='image' src='GUID-1B47C774-1861-4EF9-9702-BE83BEEC43BA-a5.gif']

Table 5-3 Data Channel Modulation Formats

The Reverse Traffic Channel used by subtypes 0 and 1 is the same as is used in EV-DO
 Revision 0. The Reverse Traffic Channel structure used with physical subtype 2 is shown
 in the following figure. RFmx Waveform Creator does not perform the encoding,
 scrambling, interleaving, and repetition contained in the gray region.

[IMAGE alt='image' src='GUID-6CEA024F-45F4-4353-94DC-2882FF4C8F0D-a5.gif']

[IMAGE alt='image' src='GUID-2BCF3732-8E70-420F-B21C-F1AB81D0FF43-a5.gif']

Fig. 5-18 Reverse Channel structure for the Traffic Channel

EV-DO Revision A Forward (Downlink) Channels

The forward link consists of three time-multiplexed channels – the Pilot Channel, the
 Traffic/Control Channel and the MAC (Medium Access Control) Channel. The following
 figure shows how the time multiplexing of these channels works on a slot-by-slot basis.
 Each slot has the same structure and there are 16 slots in one frame. If no data is
 transmitted, the slot is inactive and only the Pilot and MAC Channels are transmitted.
 The slot structure in the following figure is used in all of the three physical
 subtypes.

[IMAGE alt='image' src='GUID-DA2FB75D-5685-48A4-92A6-046F4AA1E2ED-a5.gif']

Fig. 5-19 EV-DO Revision A Forward Link Slot structure

The channel structure used in physical subtype 0 and 1 is shown in the following
 figure.

[IMAGE alt='image' src='GUID-D15D8703-9D0A-44AA-BBA2-58C65EDAEE59-a5.gif']

Fig. 5-20 Subtype 0 and 1 Forward Link Channel structure

The channel structure used in physical subtype 2 is shown in the following figure. RFmx
 Waveform Creator does not implement the encoding functions contained within gray areas.
 The Traffic/Control and Pilot Channels operate in the same way in subtype 2 as they do
 in subtypes 0 and 1. The MAC channel used in subtype 2 is considerably different to the
 MAC channel used in subtypes 0 and 1.

[IMAGE alt='image' src='GUID-011AEF72-CB1E-4253-A1F3-2FC8ECC7AC40-a5.gif']

Fig. 5-21 Forward link channel structure

Forward Pilot Channel

The Forward Pilot Channel is transmitted in the Pilot Burst of each half slot and is used
 by the access terminal for initial acquisition, phase recovery and timing recovery.

Forward Traffic/Control Channel

The Traffic/Control Channel is transmitted in the two Data Bursts of each half slot. It
 is a packet-based channel with a variable data rate. The following table details the
 data rates and modulation parameters used in physical subtypes 0 and 1.

Each physical layer packet can be preceded by a preamble sequence whose length is
 dependent upon the data rate. The preamble sequence is determined by a MAC Index value.
 In subtypes 0 and 1 the Mac index is in the range 0 to 63, whereas in subtype 2 the MAC
 index is in the range 0 to 127. The preamble is a repeated bi-orthogonal sequence that
 uniquely identifies the destination access terminal. Physical subtypes 0 and 1 use a
 32-chip bi-orthogonal sequence to encode the 64 possible MAC indexes. Physical subtype 2
 uses a 64-chip bi-orthogonal sequence to encode the 128 possible MAC indexes.

[IMAGE alt='image' src='GUID-140A4370-B0FC-4265-8B6F-042ADEAF97D1-a5.gif']

Table 5-4 Subtype 0 and 1 Forward Traffic/Control Channel

Modulation Parameters

The following table details the data rates and modulation parameters used in physical
 subtype 2.

[IMAGE alt='image' src='GUID-ABF6E49A-EE63-4A2C-93AB-CBAD82C4D6F2-a5.gif']

Table 5-5 Subtype 2 Forward Traffic/Control Channel Modulation

Parameters

When a packet is transmitted in more than one slot, a three-slot spacing is used between
 each slot. Physical layer packets for other access terminals (users) can be transmitted
 in these inactive slots. When multiple packets are transmitted to the same access
 terminal (user), a three-slot spacing is used between the last slot of a packet and the
 first slot of the next packet. This gives the access terminal (user) time to acknowledge
 whether the packet was successfully transmitted or not before the next packet is
 transmitted.

Forward Medium Access Control Channel

The Forward MAC Channel is transmitted in the two MAC Bursts of each half slot. In
 physical subtypes 0 and 1, the MAC channel consists of three sub-channels — the RA
 (Reverse Activity)Channel, the RPC (Reverse Power Control) Channel and the DRCLock (Data
 Rate Control Lock)Channel. The MAC channel used in Physical subtype 2 consists of the
 three sub channels used in physical subtypes 0 and 1, and an additional sub channel, the
 ARQ (Automatic repeat request) channel.

The MAC channels’ symbols are spread by an orthogonal Walsh code and transmitted on
 either I or Q. In physical subtypes 0 and 1, 64-chip Walsh codes are used, whereas
 physical subtype 2 uses 128-chip Walsh codes. Each Walsh code corresponds to a specific
 MAC index. The following figure shows how MAC indexes are mapped to Walsh codes in
 physical subtypes 0 and 1.

[IMAGE alt='image' src='GUID-07231D6E-B75A-47E0-A524-4CD78D1E83F3-a5.gif']

Fig 5-22 Subtype 0 and 1 Walsh code to MAC index mapping

The following figure shows how MAC indexes are mapped onto Walsh codes in physical
 subtype 2.

[IMAGE alt='image' src='GUID-BE4FF9AB-7A31-4C38-B88B-B83A7908BBB9-a5.gif']

Fig 5-23 Subtype2 Walsh code to MAC index mapping

The RA channel is transmitted on a fixed Walsh code corresponding to a MAC index of 4.
 The RPC, DRCLock, and ARQ channels use the MAC index to uniquely identify the
 destination access terminal (user).

The bits produced by the RA, RPC, and DRCLock sub-channels are BPSK modulated before
 being transmitted on either I or Q. The ARQ channel consists of three parts:

The L-ARQ (Last ARQ)

The L-ARQ is sent after the final sub-packet in a packet is received. An ACK is sent if
 the packet can be decoded, or a NACK is sent if the packet needs to be retransmitted.
 The L-ARQ is sent using NOOK (NACK-Oriented On-off Keying), where an ACK = 0 and a NACK
 = -1.

The H-ARQ (Hybrid ARQ)

The H-ARQ is transmitted after a sub-packet that is not the final sub-packet of a packet
 is received. The H-ARQ sends an ACK if the packet can be decoded, or a NACK if more
 sub-packets are required. The H-ARQ can be sent using either BPSK (Bipolar shift keying)
 where an ACK = 1 and a NACK = -1, or AOOK (ACK-Oriented On-off Keying), where an ACK = 1
 and a NACK = 0

The P-ARQ (Packet ARQ)

The P-ARQ is used to acknowledge that a packet is successfully received. The P-ARQ is
 sent using NOOK.

Parent topic:

EV-DO Revision A

<!--NI_TOPIC bundle=rfmx-waveform-creator path=introduction-to-frequency-modulation.html language=enus -->
## TOPIC 00069: Introduction to Frequency Modulation

- bundle_id: `rfmx-waveform-creator`
- source_path: `introduction-to-frequency-modulation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/introduction-to-frequency-modulation.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: With frequency modulation, you vary the frequency of a carrier in order to transmit a signal. Frequency can be thought of as the rate of change of phase. In an un-modulated carrier, the phase would change at a constant rate. The unmodulated signal could be represented mathematically as illustrated b

### Introduction to Frequency Modulation

With frequency modulation, you vary the frequency of a carrier in order to transmit a
 signal.

Frequency can be thought of as the rate of change of phase. In an un-modulated carrier,
 the phase would change at a constant rate. The unmodulated signal could be represented
 mathematically as illustrated below:

[IMAGE alt='image' src='GUID-B56CFEAD-4E50-437F-9BF4-68DACFEACC01-a5.gif']

With RFmx Waveform
 Creator you can generate FM Mono, FM Stereo, and
 FM RDS signals. To reduce distortion, apply pre-emphasis to the audio components of any
 generated FM signal.

Parent topic:

Analog Modulation

#### Mono Signal

The generation of Mono signal involves Frequency modulating an audio signal to produce a
 FM signal.

#### Stereo Signal

In Stereo mode, both the left and right channels are encoded to form a Stereo signal. The
 first stage of stereo encoding is to from a Mono and Stereo components from the left and
 right channel. This is done as follows:

- Mono = left +right
- Stereo = left -right

The Stereo encoded signal consists of the flowing subcarriers:

- The Mono component
- A 19 kHz pilot tone
- A 38 kHz tone amplitude modulated by the Stereo component.

The subcarriers are summed together to form a composite stereo signal. The following
 figure shows a block diagram for the stereo coder.

[IMAGE alt='image' src='GUID-10619AD3-E3B3-479A-994A-7152E5824FB4-a5.png']

Fig. 7-1 Block Diagram for the stereo coder.

The following figure shows the baseband spectrum of the composite stereo output. The
 composite stereo output is fed to the FM modulator to produce a FM stereo signal.

[IMAGE alt='image' src='GUID-80FA1F92-E0DB-432D-B35B-6CE33ED9D2F7-a5.png']

Fig. 7-2 The baseband spectrum of the composite stereo
 output

#### RDS Signal

In the Radio Data System (RDS) mode, the left and right audio signal are encoded in the
 same way as in FM stereo. In Addition to the audio signal an Additional subcarrier is
 added to the signal.

The RDS sub carrier consists of an amplitude modulated 57 kHz tone.

The RDS subcarrier is combined with the stereo subcarriers and frequency modulated to
 form a FM RDS signal.

The RDS data is transmitted at 1187.5 bps. Before the data is used to amplitude modulate
 the sub carrier the following processes are carried out.

- Differential Encoding
- Bi-Phase Encoding
- Up sampling and Filtering (Pulse Shaping)

Differential Encoding

The RDS data is differentially encoded according to the rules mentioned in the following
 table.

[IMAGE alt='image' src='GUID-482467B1-D281-4C0B-970F-65C273D9EE7F-a5.gif']

Table 7-1 Differential encoding rules

Bi-Phase Encoding

Bi-Phase coding involves transmitting two impulses per bit. The first impulse is
 transmitted at time t, and the second impulse is transmitted at time t+t<sub>d</sub>/2
 where td = 1/1187.5*S. If the bit transmitted at time t is a 1 then a positive impulse
 is transmitted at time t, and a negative impulse is transmitted at time
 t+t<sub>d</sub>/2. If a zero is transmitted at time t then a negative impulse is
 transmitted at time t, and a positive impulse is transmitted at time t+t<sub>d</sub>/2.
 The Bi-Phase Encoding results in 2375 impulses being transmitted every second.

Up sampling and Filtering (Pulse Shaping)

After Bi-Phase coding the sample rate for the RDS data is 2375 Hz. Before the data is
 used to amplitude modulate the 57 kHz carrier the data is up sampled and filtered. The
 up sampling is done by inserting zeros between impulses. After the data has been up
 sampled a pulse shaping filter is applied. The following figures show the frequency
 response of the filter used for the RDS data.

[IMAGE alt='image' src='GUID-884FB617-60CE-4117-A3EE-0CABA19235BF-a5.gif']

Fig. 7-3 Equation of the frequency response of the filter used for the
 RDS Data

[IMAGE alt='image' src='GUID-D67F9809-ABAC-4791-9D66-23643BFD8E21-a5.gif']

Fig. 7-4 The frequency response of the filter used for the RDS
 Data

#### RDS Data Structure

The RDS data is transmitted in groups of 104 bits. Each group is divided into 4 blocks of
 26 bits. Each block consists of 16 information bits and 10 check word bits. The
 following figure shows the structure of the RDS Group.

[IMAGE alt='image' src='GUID-7054004A-0040-4699-A2DD-5E098F814AE8-a5.gif']

Fig. 7-5 The structure of an RDS
 Group

To compute the checkword, a CRC (Cyclic redundancy check) is computed. The CRC is
 remainder of the following modulo 2 calculation m(x)*x<sup>10</sup> where g(x) is the
 generator polynomial g(x)=x<sup>10</sup>+ x<sup>8</sup>+ x<sup>7</sup>+ x<sup>5</sup>+
 x<sup>4</sup>+ x<sup>3</sup>+1.

The checkword is computed by taking a modulo 2 sum of the CRC and an “offset word”. The
 offset word is different for each group in the block, the offset words A, B, C, or C'
 and D are added to the CRC computed for blocks 1, 2, 3, and 4 respectively. Where offset
 words A, B, C, C' and D are defined in the following table.

[IMAGE alt='image' src='GUID-5ACD2E2B-AF78-404F-ACFF-F52016D94DC4-a5.gif']

Table 7-2 Definition of the offset words used to
 compute the check word

The bits in an RDS group are transmitted MSB first. The first block of every group always
 contains the PI code (program identification code). In the second group; the first 4
 bits contain the Group type code; the 5th bit contains the version code; the
 6<sup>th</sup> bit is the TP bit (Traffic program code); and bits 7 to 11 contain
 the PTY (Program type code). The remaining bits of group 2 and the bits in all the other
 groups are dependent on the group type and version bit. The following figure shows the
 basic RDS message format.

[IMAGE alt='image' src='GUID-F2192DAC-ED16-4880-9478-29DC9A3EEF39-a5.gif']

Fig. 7-6 The basic RDS message
 format

When a version A group is transmitted (B<sub>0</sub>=0 ) the PI code will only be
 transmitted in block 1, and the checkword of block 3 will be formed using offset word c.
 When a version B group is transmitted (B<sub>0</sub>=1) the PI is transmitted in both
 Block 1 and Block 3. In this situation the checkword of block 3 will be formed using
 offset word c'. By using a different offset word for a version B group it is possible
 for a receiver to detect that block 3 contains the PI code without reading the version
 bit transmitted in block 1.

PI (Program identification) Code

The Program identification code is used to identify the program being transmitted. The
 use of the PI code varies from country to country, but in most countries it takes the
 following format:

Bits b<sub>15</sub> to b<sub>12</sub>= Country code.

Bits
 b<sub>11</sub> to b<sub>8</sub>= Program type in terms of area coverage.

Bits b<sub>7</sub> to b<sub>0</sub> = Program reference number.

Group Type Code / Version

The Group type code and version indicate the type of message that is transmitted in an
 RDS signal the group type is 4 bits long and the version code is 1 bit long. This
 provides 32 possible combinations of group/version codes. The following table shows the
 group types used in RDS mode. Currently RFmx Waveform Creator is only able to encode the
 messages in bold.

[IMAGE alt='image' src='GUID-20348863-EA53-44CF-9823-278B122684A3-a5.gif']

Table 7-3 group types used in
 RDS

The details of specific message types can be found in the RDS specification (IEC
 62106).

TP (Traffic Program) Code

The TP code is used to indicate that a program carries traffic announcements. The TP code
 is a single bit. A value of 1 indicates that program carries traffic announcements, and
 a value of zero indicates the program does not. The TP code is used in conjunction with
 the TA(Traffic Announcement) code. The TA code is transmitted in a Tuning and switching
 message or a Fast switching message.

EON (Enhanced Other Network) messages may be used to provide information about other
 programs that carry traffic announcements. When the TP code is set to 0 the TA code is
 used to indicate whether or not the program carries EON information for Traffic
 Announcements.

When the TP code is set to 1 the TA code is used to indicate weather a Traffic
 Announcement is currently being broadcast. In this situation the TA code no longer
 indicates the presence/absence of EON information for Traffic announcements. The
 following table shows how the TP and TA codes are interpreted.

[IMAGE alt='image' src='GUID-E8AD8D68-967D-4C2B-9E74-C184671B44E3-a5.gif']

Table 7-4 How the TP and TA codes are
 interpreted.

PTY (Program Type) Code

The PTY code indicates the type of program that is being transmitted the program type is
 a 5 bit value and can take one of the following values:

- None = 0
- News = 1
- Current Affairs = 2
- Information = 3
- Sport = 4
- Education = 5
- Drama = 6
- Culture = 7
- Science = 8
- Varied = 9
- Pop Music = 10
- Rock Music = 11
- Easy Music = 12
- Light Classical = 13
- Seriously Classical = 14
- Other Music = 15
- Weather = 16
- Finance = 17
- Children = 18
- Social Affairs = 19
- Religion = 20
- Phone In = 21
- Travel = 22
- Leisure = 23
- Jazz Music = 24
- Country Music = 25
- National Music = 26
- Oldies Music = 27
- Folk Music = 28
- Documentary = 29
- Alarm Test = 30
- Alarm = 31

<!--NI_TOPIC bundle=rfmx-waveform-creator path=introduction-to-td-scdma-3gpp-tdd-lcr.html language=enus -->
## TOPIC 00070: Introduction to TD-SCDMA (3GPP TDD-LCR)

- bundle_id: `rfmx-waveform-creator`
- source_path: `introduction-to-td-scdma-3gpp-tdd-lcr.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/introduction-to-td-scdma-3gpp-tdd-lcr.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: 3GPP TDD(Time domain duplexed) is a standard defined by the Third Generation Partnership Project. 3GPP TDD-LCR is a low chip rate (LCR) variant of the 3GPP TDD standard. More information on the 3GPP TDD-LCR standard can be found in the following 3GPP specifications: TS 25.221 Physical channels and

### Introduction to TD-SCDMA (3GPP TDD-LCR)

3GPP TDD(Time domain duplexed) is a standard defined by the Third Generation Partnership
 Project. 3GPP TDD-LCR is a low chip rate (LCR) variant of the 3GPP TDD standard. More
 information on the 3GPP TDD-LCR standard can be found in the following 3GPP
 specifications:

| TS 25.221 | Physical channels and mapping of transport channels onto physical channels (TDD) |
| --- | --- |
| TS 25.222 | Multiplexing and channel coding (TDD) |
| TS 25.223 | Spreading and modulation (TDD) |
| TS 25.224 | Physical layer procedures (TDD) |

The chip rate used by 3GPP TDD-LCR is 1.28 Mchips per second. The frame length is 10 ms,
 with each frame being made up of two 5 ms (6400 chip) sub-frames. The layout of the
 sub-frame can be seen in the following figure.

[IMAGE alt='image' src='GUID-11133BB6-B4CD-41AE-A616-B830B113F3CB-a5.gif']

Fig. 6-1 TDD-LCR sub-frame

The TDD-LCR sub-frame consists of 7 traffic time slots, a DwPts (Downlink pilot time
 slot), a guard period and a UpPts (Uplink pilot time slot). The first traffic time slot
 transmitted (Ts0) must carry downlink data. The second time slot transmitted must carry
 uplink data. The data carried in Ts2 to Ts6 is determined by the position of the
 switching point: the timeslots before the switching point carry uplink data and the
 timeslots after the switching point carry downlink data.

DwPts (Downlink Pilot Time Slot)

The DwPts consists of a 32-chip guard period (GP) followed by a 64-chip synchronization
 code (SYNC-DL). The layout of the DwPts can be seen in the following figure.

[IMAGE alt='image' src='GUID-51DA34EC-3B30-4122-937F-BA85E46C5270-a5.gif']

Fig. 6-2 DwPts

During the guard period nothing is transmitted. The SYNC-DL consists of a 64-chip complex
 sequence. The complex sequence is generated from one of the 32 basic SYNC-DL sequences
 defined in Annex AA.1 of TS 25.223. The basic SYNC-DL code is
 converted to bipolar to form a bipolar sequence S. The bipolar sequence S is then
 converted to a complex sequence S:

S<sub>i</sub>

UpPts (Uplink Pilot Time Slot)

The UpPts consists of a 128-chip SYNC-UL code followed by a 32-chip guard period. The
 layout of the UpPts can be seen in the following figure.

[IMAGE alt='image' src='GUID-F32E9482-9769-4DCB-B8BD-3898B58060EF-a5.gif']

Fig. 6-3 UpPts

The SYNC-UL consists of a 128 chip complex sequence. The complex sequence is generated
 from one of the 256 basic SYNC-UL sequences defined in Annex AA.2 of TS
 25.223. The basic SYNC-UL code is converted to bipolar form to form the
 bipolar sequence S. The bipolar sequence S is then converted to a complex sequence
 S:

S<sub>i</sub>=(j)<sup>i</sup>.S<sub>i</sub> where S<sub>i</sub> ε{1,-1},
 i=1,...,128, j=√ -1  Basic SYNC-UL
 sequence S to complex sequence S

Traffic Time Slots

The traffic slots are 864 chips long. Each traffic slot consists of a number of channels
 which are summed together to form the traffic slot’s chips. The layout of a channel is
 shown in the following figure.

[IMAGE alt='image' src='GUID-372FD8B0-DC8F-4890-B82C-DEAF915361B9-a5.gif']

Fig. 6-4 Burst layout

The data sent in a data burst is QPSK, 8PSK, or QAM modulated, multiplied by a
 channel-specific multiplier, spread by an orthogonal Walsh code and scrambled as shown
 in the following figure.

[IMAGE alt='image' src='GUID-F68406CF-03E9-4B1C-844E-2409D83E539B-a5.gif']

Fig. 6-5 Traffic channel structure

The following figure shows how the channels are combined to form the chips transmitted in
 each slot. RFmx Waveform Creator currently supports only QPSK or 8PSK modulation.

[IMAGE alt='image' src='GUID-DFBCEC51-1CBE-47CA-B102-AAEC4F055C71-a5.gif']

Fig. 6-6 Combining channel data to form slot data

Channel Weighting

The channel specific multiplier is dependent on both the channel code k and the spreading
 factor Q. The following figure shows the channel specific multipliers used in 3GPP
 TDD-LCR.

[IMAGE alt='image' src='GUID-E86B3AD3-CA97-40D0-A8A5-EE5F68582B4A-a5.gif']

Table 6-1 Channel-specific multipliers

Channel Spreading

The data in each of the traffic channels is spread by a spreading code of
 W<sub>Q</sub><sup>(k)</sup> where k is the
 channel code and q is the spreading factor. Channels in the same time slot can use
 different spreading factors (values of Q) providing the spreading code is orthogonal to
 the other channel codes used in the timeslot. The following figure shows the spreading
 tree for spreading factors 1 to 4. A channel code will be orthogonal if the specific
 code is not in use, no other code on the path from the specific code to the root of the
 tree is used, and no other code in the sub-tree below the specific code is used.

[IMAGE alt='image' src='GUID-E1B8CF41-C22D-4ACD-BB1F-9E27D9B9EF08-a5.gif']

Fig. 6-7 Code-tree for 3GPP TDD-LCR channelization

Scrambling

The complex scramble code V is 16 chips long and is generated from one of the 128 bipolar
 sequences defined in Annex A of TS 25.223. The bipolar scramble code
 V is converted to a complex scrambling code as shown below:

V<sub>i</sub>=(j)<sup>i</sup>.V<sub>i</sub> where S<sub>i</sub> ε{1,-1},
 i=1,...,16, j=√ -1  Bipolar scramble
 sequence V to complex scramble sequence V

When scrambling, the data is taken Q<sub>MAX</sub>/Q<sub>k</sub> spread words at a time
 where Q<sub>MAX</sub> = 16 (the maximum spreading factor), and Q<sub>k</sub> = The
 spreading factor used by the channel. This means the data is taken in 16-chip blocks.
 Each chip in each 16 chip block is multiplied by the corresponding chip in the scramble
 code to produce scrambled data.

Slot Formats

A Traffic channel’s data burst can be used to transmit Traffic data, TFCI (Transport
 Format Combination Indicator) bits, SS (Synchronization Shift) bits and TPC (Transmitter
 Power Control) bits. A channel’s slot format determines which spreading factor the
 channel should use and how many Traffic data, TFCI, SS, and TPC bits are transmitted in
 the channel’s data bursts. The QPSK downlink slot formats are defined in Table
 8F of TS 25.221. QPSK uplink slot formats are defined in Table 8G of TS
 25.221 and 8PSK(uplink and downlink) slot formats are defined in Table 8H of TS
 25.221. The following figure shows the positions of the TFCI, SS, and TPC
 bits in the channel’s data bursts.

[IMAGE alt='image' src='GUID-0BB07380-8687-4DAE-84FE-EFF33F19C1F9-a5.gif']

Fig. 6-8 Location of the TFCI, SS, and TPC bits

TFCI-bits

The TFCI is encoded to form a TFCI code word. The TFCI codeword is modulated and spread
 in the same was as the other data being transmitted. The TFCI codeword is transmitted
 over one frame (two sub-frames). Normally, the TFCI codeword is split into four parts
 and transmitted as shown in the following figure.

[IMAGE alt='image' src='GUID-A3C9ADD7-3119-4282-BE4F-04CE745492B5-a5.gif']

Fig. 6-9 TFCI code word location (when TFCI code word requires four
 or more chips)

When the TFCI code requires fewer than four symbols (before spreading) to transmit, the
 codeword is split into only two parts and the TFCI is transmitted as shown in the
 following figure (only transmitting in the first data burst of each sub-frame).

[IMAGE alt='image' src='GUID-FBFE9871-578E-4F7A-A084-5516075ADF74-a5.gif']

Fig. 6-10 TFCI code word location (when TFCI code word requires
 fewer than four chips)

The length of the TFCI code word is determined by the slot format. The type of coding
 used to encode the TFCI is dependent on the TFCI code word length and modulation type.
 The following table shows the TFCI coding used in 3GPP TDD-LCR.

[IMAGE alt='image' src='GUID-876D9B89-03B6-4E38-99A9-2CDD163BB9B1-a5.gif']

Table 6-2 TFCI coding

SS-bits

The SS (Synchronization Shift) bits are used to transmit uplink synchronization control.
 The SS bits are used to command a timing adjustment of (k/8) Tc every M sub-frames,
 where the values of k and M are signalled by the network and Tc is the chip period. The
 relationships between bits and synchronization Shifts are shown in the following figures
 (for QPSK and 8 PSK respectively).

[IMAGE alt='image' src='GUID-A64568C3-D90A-4B10-8511-B6FB649F3052-a5.gif']

Table 6-3 Coding of the SS for QPSK

[IMAGE alt='image' src='GUID-AD5D3BC9-F201-4D22-A154-6D6D068EC95E-a5.gif']

Table 6-4 Coding of the SS for 8PSK

TPC-bits

The TPC (Transmitter Power Control) bits are used to increase/decrease the channel power.
 The relationships between bits and power control commands are shown in the following
 figures (for QPSK and 8 PSK respectively).

[IMAGE alt='image' src='GUID-5AF0AB48-24B8-42C8-B02D-FF4890883E23-a5.gif']

Table 6-5 TPC Bits for QPSK

[IMAGE alt='image' src='GUID-6C69FC9A-BF71-4F2C-A435-B750FDE715AC-a5.gif']

Table 6-6 TPC Bits for 8PSK

Midamble Generation

The midamble sequence is determined by the basic midamble code in use, the maximum number
 of users, and the user id of the channel. The midamble sequence is generated from one of
 the 128 basic midamble codes defined in defined in Annex AA.1 of TS
 25.221. The midamble code is first converted to a bipolar to form a
 bipolar sequence (M). The bipolar sequence is converted to a complex midamble sequence
 as described in the following figure.

[IMAGE alt='image' src='GUID-49A4BB97-BB10-46B0-A09B-636AD9E91EF3-a5.gif']

Fig. 6-11 Midamble generation

Code Groups

The SYNC-DL codes, SYNC-UL codes, scrambling codes, and basic midamble codes are grouped
 into 32 groups. Each code group contains one SYNC-DL code, 8 SYNC-UL codes, and 4 basic
 midamble and scrambling codes. The following table shows the codes associated with each
 code group. The 3GPP TDD-LCR spec states that only codes from the same group can be used
 at any given time, and that the midamble code ID and scrambling code ID must be the
 same.

[IMAGE alt='image' src='GUID-032CCC84-DC78-47EE-B461-462494F4A19A-a5.gif']

Table 6-7 3GPP TDD-LCR code grouping

Parent topic:

TD-SCDMA (3GPP TDD-LCR)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=iq-impairments.html language=enus -->
## TOPIC 00071: Applying IQ Impairments

- bundle_id: `rfmx-waveform-creator`
- source_path: `iq-impairments.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/iq-impairments.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Waveform Creator allows the user to distort waveform types by adding impairments to them. If you wish to do this, select the IQ Impairments tab. This prompts the screen as shown in the following image. There are three types of impairments that can be applied to a waveform: IQ errors Noise Clipp

### Applying IQ Impairments

RFmx Waveform Creator allows the user to distort waveform types by adding impairments to
 them. If you wish to do this, select the IQ Impairments tab. This
 prompts the screen as shown in the following image.

[IMAGE alt='image' src='GUID-AE722038-3F07-4CA9-A50A-AF617CA5D284-a5.png']

There are three types of impairments that can be applied to a waveform:

- IQ errors
- Noise
- Clipping

#### Adding IQ Errors

This section of the IQ Impairments tab allows you to add errors to a waveform. Select the
 Apply IQ Errors checkbox to enable the parameters.

[IMAGE alt='image' src='GUID-85F8CE51-0790-4697-8C2D-7C0F38B4F459-a5.png']

There are four types of IQ error that you can add. These are as follows:

Skew

An ideal base band modulation scheme relies on the in phase (I) and quadrature (Q)
 components to be orthogonal. In practice this may not be the case. Skew is offset angle
 φ that forces the I and Q components of signal to become non–orthogonal. Refer to the
 following figure.

[IMAGE alt='image' src='GUID-932F48B9-F6FB-468B-BBF7-66A1A39DCEE3-a5.gif']

The in-phase component (I) axis remains unchanged while the quadrature component (Q) is
 rotated by φ degrees. Mathematically, this is described as follows:

[IMAGE alt='image' src='GUID-C13C27E2-6CB7-47EF-8409-8F3C3CFADF5F-a5.gif']

[IMAGE alt='image' src='GUID-28DC76C1-5F64-4029-9046-F30A26359EE7-a5.gif']

[IMAGE alt='image' src='GUID-26AEEDA0-6332-4405-A77A-1EE8EB8873C9-a5.gif']

where I' and Q' are the modified I and Q values with a skew of φ degrees applied. It is
 assumed that the amplitude of the axes remains unchanged.

Carrier Leak

Carrier leak after IQ modulation occurs if there is a DC component on either the I or Q
 channel. RFmx Waveform Creator allows you to add a DC value to either channel. The
 amount of DC added is defined as a percentage of the rms vector. The figure below
 depicts this, where r is the rms value voltage of the signal, k<sub>i</sub> and
 k<sub>q</sub> are the percentages of DC offsets to be added to the I and Q channels
 respectively.

[IMAGE alt='image' src='GUID-F9236CB4-B4E6-4394-A510-0B901F3CB4EA-a5.gif']

Mathematically the amount of DC added to either the I or Q channel is given by

[IMAGE alt='image' src='GUID-F52F1DB7-F39F-4738-AAF2-D96E1A41180D-a5.gif']

where

[IMAGE alt='image' src='GUID-E93CE211-34FC-410F-97FE-E98B884CC076-a5.gif']

and N is the number of IQ sample pairs. Note that it is possible to have negative DC
 offsets.

IQ Gain Imbalance

IQ gain imbalance results when the I and Q channels have a different gains applied to
 them. The result of this distortion can be seen below. This figure shows a vector plot
 of an MSK signal that has had a gain imbalance of -5 dB applied. An ideal plot would
 have been a circle. In RFmx Waveform Creator, the gain imbalance is set with reference
 to the I channel. This implies that a positive gain imbalance gives an I gain that is
 greater than the Q gain.

[IMAGE alt='image' src='GUID-1003C6A6-0B55-4C40-986E-BC58C923F45D-a5.gif']

#### Adding Noise

This section of the IQ Impairments tab provides the facility to
 inject additive white Gaussian noise (AWGN) into the waveform. To enable
 SNR, set the State to
 On.

[IMAGE alt='image' src='GUID-811AD6AA-166C-4D77-ACC3-28877195FC6E-a5.png']

You have to set the SNR parameter in dB.

#### IQ Clipping

This section of the IQ Impairments tab allows you to clip the I
 and Q of a waveform. Select the Apply Clipping checkbox to enable
 the parameters.

[IMAGE alt='image' src='GUID-A99DAD2F-8746-4BE2-B4A2-7A3B1E260212-a5.png']

With clipping enabled, the I and Q values will be clipped depending on the settings
 specified.

- If the clipping type is Circle , the overall IQ Vector will be
 clipped to the percentage specified.
- If the clipping type is Square , the I and Q values will be
 individually clipped to the percentage specified.

There is an option to apply the clipping parameters before filtering has been applied, or
 after.

|  | Note Clipping is not enabled for all modulations. For example, clipping is not enabled for the Generic modulation. For LTE, NR, and multi carrier plugin, clipping is available in CFR tab. In order to apply clipping, set CFR method to Clipping and Clip Using to Level. |
| --- | --- |

<!--NI_TOPIC bundle=rfmx-waveform-creator path=licensed-assisted-access.html language=enus -->
## TOPIC 00072: Licensed Assisted Access

- bundle_id: `rfmx-waveform-creator`
- source_path: `licensed-assisted-access.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/licensed-assisted-access.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Licensed assisted access (LAA) is introduced in release 13 of 3GPP specification to enable the operation of an LTE system in an unlicensed band. It combines an LTE carrier in the unlicensed spectrum with an LTE carrier in the licensed band using carrier aggregation. Frame structure type 3 is the new

### Licensed Assisted Access

Licensed assisted access (LAA) is introduced in release 13 of 3GPP specification to
 enable the operation of an LTE system in an unlicensed band. It combines an LTE carrier
 in the unlicensed spectrum with an LTE carrier in the licensed band using carrier
 aggregation. Frame structure type 3 is the new type of frame structure defined by 3GPP
 specification for LAA.

Frame structure Type 3

Frame structure type 3 is applicable to LAA unlicensed carrier with normal cyclic prefix
 only. Each radio frame is 10 ms long and consists of 10 subframes of length 1 ms. Any of
 these 10 subframes can be used for uplink/downlink transmission or can be empty. LAA
 transmission can start and end at any subframe and can consist of one or more
 consecutive subframes in the burst.

[IMAGE alt='image' src='GUID-90658CF4-F45F-4A5F-8570-B43D3103C577-a5.gif']

Partial Subframes

Partial subframes are introduced by 3GPP specification, as a part of frame structure type
 3, to cater to the needs of Listen Before Talk (LBT) principles and for efficient use of
 unlicensed spectrum by LAA.

Partial subframes in uplink

- LAA uplink burst gets transmitted either from the start of the 0 th symbol
 or from the start of the 1 st symbol in a subframe. The transmission can
 also start between the 0 th and the 1 st symbol, as defined in
 section 5.6 of 3GPP 36.211 specification. Thus, the
 0 th symbol in the first subframe of an LAA uplink burst can be
 partially filled, completely filled, or completely empty.
- LAA uplink transmission can end either at the 12 th or 13 th 
 OFDM symbol in a subframe as mentioned in sections 5.3.3.1.1A and 5.3.3.1.1B of
 3GPP 36.212 specification. Therefore, the last subframe in an
 LAA uplink transmission can be completely filled with 14 OFDM symbols or can be
 partially filled with 13 OFDM symbols.

[IMAGE alt='image' src='GUID-393064E1-7E19-4BB1-8257-7F22B9E67CA0-a5.gif']

Partial subframes in downlink

- LAA downlink transmission can start from 0th OFDM symbol (Subframe boundary) or from
 7 th OFDM symbol (Second Slot Starting Position) of a subframe. Refer
 to section 13A of 3GPP 36.213 specification for more
 information.
- LAA downlink transmission can either end at the subframe boundary or at any of the
 DwPTS symbols. Therefore, the last subframe can be completely occupied with 14 OFDM
 symbols or can consist of any of DwPTS duration symbols i.e. 3, 6, 9, 10, 11, or 12
 OFDM symbols. Refer to section 4.3 of 3GPP 36.211 specification
 for more information.

[IMAGE alt='image' src='GUID-AF17DDB3-BB26-4F31-9244-2D4FF3B5C898-a5.gif']

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lta-laa-carrier-configuration.html language=enus -->
## TOPIC 00073: Carrier Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `lta-laa-carrier-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lta-laa-carrier-configuration.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section allows you to configure the top level modulation parameters of the LAA Signal. It comprises the controls as described below. Link Direction: Specifies the link direction of the signal being generated. Number of Frames: Specifies the number of radio frames that will be generated. The val

### Carrier Configuration

This section allows you to configure the top level modulation parameters of the LAA Signal.
 It comprises the controls as described below.

[IMAGE alt='image' src='GUID-A896BE5C-1B88-4915-8A79-9883515C4C0E-a5.png']

Link Direction: Specifies the link direction of the signal being
 generated.

Number of Frames: Specifies the number of radio frames that will be
 generated. The valid range is 1 to 2. The number of frames is calculated based on the burst
 configuration. If the burst spans across 2 frames, number of frames is set to 2.

For example, if the starting subframe is 5 and number of subframes is 10, 2 frames will get
 generated.

Channel Bandwidth: Specifies the system bandwidth of the LTE signal.
 Valid values are 1.4 MHz, 3 MHz, 5
 MHz, 10 MHz, 15 MHz, and
 20 MHz. The default value is 10 MHz.

| System Bandwidth BWChannel [MHz] | Number of Resource Blocks |
| --- | --- |
| 1.4 | 6 |
| 3 | 15 |
| 5 | 25 |
| 10 | 50 |
| 15 | 75 |
| 20 | 100 |

Table 1-6, The relationship of bandwidth to number of resource blocks.

Cell ID: Specifies the physical layer cell identity. The range is 0
 to 503. The default value is 0. The Cell ID is automatically incremented when downlink test
 model is configured in multiple carriers.

Oversampling Factor: Specifies the oversampling factor to be used in
 the simulation. When the Auto is checked, the oversampling rate is
 adjusted automatically.

Cyclic Prefix Mode: Specifies the cyclic prefix type of the signal
 being generated. LAA supports Normal cyclic prefix. This is
 read-only.

Burst Configuration

Starting Subframe: Specifies the starting subframe of an LAA burst.
 Valid range is from 0 to 9. The default value is 0.

Number of Subframes: Specifies the number of subframes in an LAA
 burst including the starting subframe. Valid range is from 1 to 10. The default value is
 10.

Start Position (Uplink): Specifies the starting position of symbol0
 in the first subframe of an LAA uplink bursts. The default value is
 00.

| 00 | The symbol 0 in the first subframe of an LAA uplink burst is completely occupied. There is no idle duration. |
| --- | --- |
| 01 | The starting position of symbol0 in the first subframe of an LAA uplink burst is calculated as per the section 5.6 (frame structure type 3) of the 3GPP 36.211 specification. The symbol is partially occupied. |
| 10 | The starting position of symbol0 in the first subframe of an LAA uplink burst is calculated as per the section 5.6 (frame structure type 3) of the 3GPP 36.211 specification. The symbol is partially occupied. |
| 11 | The starting position of symbol0 in the first subframe of an LAA uplink burst is calculated as per the section 5.6 (frame structure type 3) of the 3GPP 36.211 specification. The symbol is partially occupied. |

Ending Symbol (Uplink): Specifies the ending symbol number in the
 last subframe of an LAA uplink burst. Refer to section 5.3.3.1.1A of the 3GPP
 36.212 specification for more information about the LAA uplink ending symbol.
 The default value is s13.

| s12 | The last subframe of an LAA uplink burst ends at symbol 12. |
| --- | --- |
| s13 | The last subframe of an LAA uplink burst ends at symbol 13. |

N<sub>TA</sub>: Specifies the timing offset between uplink and downlink radio frames at the
 UE. This attribute is expressed in units of Ts. It is used to calculate the starting
 position of symbol0 in the first subframe of an LAA uplink burst when the Start
 Position is set to 10. Valid range is from 0 to
 (N+Ncp,0)-768. Refer to section 5.3.3.1.1A of the 3GPP specification
 36.212 for more information about LAA uplink ending symbol.

Starting Symbol (Downlink): Specifies the starting symbol number in
 the first subframe of an LAA downlink burst. Refer to section 13A of the 3GPP
 36.213 specification for more information regarding LAA downlink starting
 symbol. The default value is S0.

| S0(0) | The first subframe of an LAA downlink burst starts with symbol 0. |
| --- | --- |
| S07(1) | The first subframe of an LAA downlink burst starts with symbol 7. |

Number of Ending Symbols (Downlink): Specifies the number of ending
 symbols in the last subframe of an LAA downlink burst. Refer to section 4.3 of the
 3GPP 36.211 specification for more information about LAA downlink
 number of ending symbols. The default value is 14.

| 3 | The number of ending symbols in the last subframe of an LAA downlink burst is 3. |
| --- | --- |
| 6 | The number of ending symbols in the last subframe of an LAA downlink burst is 6. |
| 9 | The number of ending symbols in the last subframe of an LAA downlink burst is 9. |
| 10 | The number of ending symbols in the last subframe of an LAA downlink burst is 10. |
| 11 | The number of ending symbols in the last subframe of an LAA downlink burst is 11. |
| 12 | The number of ending symbols in the last subframe of an LAA downlink burst is 12. |
| 14 | The number of ending symbols in the last subframe of an LAA downlink burst is 14. |

Time Domain Windowing: Time domain windowing is not mandatory in the
 LTE standard. The window function is employed to reduce out-of-band spectrum emissions.
 Time domain windowing helps in reducing the spectral sidelobes, that occurs because of the
 discontinuity at OFDM symbol boundaries, by creating an overlap between the two symbols
 (overlap duration specified by the time domain windowing duration). Larger the window
 duration, more is the overlap. This causes more samples to distort in the time domain,
 leading to a steeper reduction in sidelobe. The smaller bandwidths require larger time
 domain window.

State: Specifies whether the time domain windowing function is to be
 applied to the simulation. If the State checkbox is selected,
 windowing is to be employed. The checkbox is selected by default.

Duration: Specifies the time interval of the time domain windowing
 function. Increasing the transition time, increases the spectrum roll-off at the cost of a
 decreased delay spread tolerance. The default value of the time domain window duration is
 340 ns. This default value is optimized for a 20 MHz LTE signal.
 The transition time range is 0 to 4600 ns, inclusive.

Auto: When you select this checkbox, the value of the
 Duration parameter is set to a recommended value based on
 Channel Bandwidth. The checkbox is selected by default.

Refer to the following table for recommended values.

| Channel Bandwidth | Auto Window Duration |
| --- | --- |
| 20 MHz | 340 ns |
| 15 MHz | 350 ns |
| 10 MHz | 500 ns |
| 5 MHz | 800 ns |
| 3 MHz | 1600 ns |
| 1.4 MHz | 3200 ns |

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte-abbreviations.html language=enus -->
## TOPIC 00074: Abbreviations

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte-abbreviations.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte-abbreviations.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: 3GPP 3rd Generation Partnership Project AMC Adaptive Modulation and Coding CFI Control Format Indicator CP Cyclic Prefix DCI Downlink Control Information DMRS Demodulation Reference Symbols DTX Discontinuous Transmission DL Downlink E-UTRA Evolved UMTS Terrestrial Radio Access E-UTRAN Evolved UMTS T

### Abbreviations

| 3GPP | 3rd Generation Partnership Project |
| --- | --- |
| AMC | Adaptive Modulation and Coding |
| CFI | Control Format Indicator |
| CP | Cyclic Prefix |
| DCI | Downlink Control Information |
| DMRS | Demodulation Reference Symbols |
| DTX | Discontinuous Transmission |
| DL | Downlink |
| E-UTRA | Evolved UMTS Terrestrial Radio Access |
| E-UTRAN | Evolved UMTS Terrestrial Radio Access Network |
| FDD | Frequency Division Duplex |
| LAA | License Assisted Access |
| LTE | Long Term Evolution |
| MBSFN | Multicast/Broadcast over a Single Frequency Network |
| MIMO | Multiple Input Multiple Output |
| OFDM | Orthogonal Frequency Division Multiplexing |
| PBCH | Physical Broadcast Channel |
| PCFICH | Physical Control Format Indicator Channel |
| PDCCH | Physical Downlink Control Channel |
| PDSCH | Physical Downlink Shared Channel |
| PHICH | Physical Hybrid ARQ Indicator Channel |
| PRACH | Physical Uplink Random Access Channel |
| PSCCH | Physical Sidelink Control Channel |
| PSSCH | Physical Sidelink Shared Channel |
| PUCCH | Physical Uplink Control Channel |
| PUSCH | Physical Uplink Shared Channel |
| SC-FDMA | Single Carrier Frequency Division Multiple Access |
| RB | Resource Block |
| SISO | Single Input Single Output |
| SRS | Sounding Reference Signal |
| TDD | Time Division Duplex |
| TTI | Transmission Time Interval |
| UE | User Equipment |
| UL | Uplink |
| NPUSCH | Narrowband Physical Uplink Shared Channel |

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte-carrier-aggregation.html language=enus -->
## TOPIC 00075: LTE Carrier Aggregation

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte-carrier-aggregation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte-carrier-aggregation.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Carrier Aggregation Carrier aggregation is one of the main features in LTE-Advanced as defined by the 3GPP specification. Carrier aggregation enables multiple carriers to be combined to support wider transmission bandwidths, thereby increasing the data rate. For more information about carrier aggreg

### LTE Carrier Aggregation

Carrier Aggregation

Carrier aggregation is one of the main features in LTE-Advanced as defined by the
 3GPP specification. Carrier aggregation enables multiple carriers
 to be combined to support wider transmission bandwidths, thereby increasing the data
 rate.

For more information about carrier aggregation, refer to section 5.4.1A and 5.4.2A of the
 3GPP TS 36.521-1 specification.

You can configure multiple carrier channels by specifying the carrier offsets. You can
 configure contiguous and noncontiguous carrier aggregation by configuring the spacing
 between LTE carriers.

Carrier Bandwidths

To maintain backward compatibility, carrier aggregation is performed with release 8
 carrier bandwidths, for example, 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz, and 20 MHz. Each
 aggregated carrier is referred to as a component carrier (CC).

Types of Carrier Aggregation

- Intra-band Contiguous— Component carriers are placed side-by-side within the same
 operating frequency band. In RFmx Waveform Creator, you can configure this type by
 defining multiple carriers.
- Intra-band Noncontiguous— Component carriers are placed with some gap within the
 same operating frequency band. In RFmx Waveform Creator, you can configure this type
 by defining multiple sub blocks.
- Inter-band Noncontiguous— One or more component carriers are placed in different
 operating frequency bands. In RFmx Waveform Creator, you can configure this type by
 defining multiple carrier sets.

[IMAGE alt='image' src='GUID-DBFF665A-1923-4BFD-A8A5-58D91EBDE096-a5.gif']

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte-examples.html language=enus -->
## TOPIC 00076: LTE Examples

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte-examples.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte-examples.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Waveform Creator provides several predefined LTE example settings. You can find these examples in the following location: You can access all the installed RFmx Waveform Creator examples from the Start menu. (Windows 7) Select Start»All Programs»National Instruments»RFmx Waveform Creator»RFmx Wa

### LTE Examples

RFmx Waveform Creator provides several predefined LTE example settings. You can find
 these examples in the following location:

You can access all the installed RFmx Waveform Creator examples from the
 Start menu.

- (Windows 7) Select Start»All Programs»National Instruments»RFmx Waveform
 Creator»RFmx Waveform Creator Examples
- (Windows 10/8.1) Select Start»National Instruments»RFmx Waveform Creator
 Examples

The naming convention used for the LTE example are as follows:

- Lte_[duplexscheme]_ [Link Direction] _ [Fixed reference Channel] _ [Annexes table of
 the 36.521 specification, which defines the FRC Configurations] _
 [Bandwidth to pick from the Annexes table] _ [Type of Measurement in the
 36.521 specification, whose configurations are defined in
 Annexes]. 
 For example: LTE_FDD_DL_FRC_A321_1p4Mhz_7_6_3.rfws 
 For more information about this example, refer to the 3GPP TS 36.521-1 V
 15.1.2 (2018-04) specification.
- Lte_[duplexscheme]_ [Link Direction] _ [Fixed reference Channel] _ [Annexes table of
 the 36.521 specification, which defines the FRC
 Configurations]_[Table No (version 8.3)] _[Column No]_[Bandwidth to pick from the
 Annexes table] _ [Type of Measurement in the 36.521 
 specification, whose configurations are defined in Annexes]. 
 For example: 
 
 For more information about this examples, refer to the 3GPP TS 36.521-1
 V 8.3.0 (2009-09) specification.
  - LTE_FDD_UL_RMC_A2221_4_1_10Mhz-6_2_2.rfws
  - LTE_ FDD_UL_RMC_A2221_4_2_10Mhz-6_7.rfws
  - LTE_ FDD_UL_RMC_A2221_5__2_15Mhz-6_5_2_2.rfws
  - LTE _ FDD_UL_RMC_A2221_6__2_20Mhz-6_2_5.rfws
  - LTE _ FDD_UL_RMC_A2222_6__2_20Mhz-6_5_2_1.rfws
  - LTE _TDD_UL_RMC_A2321_4_2_20MHz_6_7.rfws
  - LTE _TDD_UL_RMC_A2321_5_2_15MHz_6_2_5.rfws

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte-fdd-carrier-configuration.html language=enus -->
## TOPIC 00077: Carrier Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte-fdd-carrier-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte-fdd-carrier-configuration.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section allows you to configure the top level modulation parameters of the FDD Signal. It comprises the controls as described below. Link Direction: Specifies the link direction of the signal being generated. Valid values are Downlink, Uplink, and Sidelink. Number of Frames: Specifies the numbe

### Carrier Configuration

This section allows you to configure the top level modulation parameters of the FDD Signal.
 It comprises the controls as described below.

[IMAGE alt='image' src='GUID-38C9C0D9-335E-4410-B50C-7C4BC44F746C-a5.png']

Link Direction: Specifies the link direction of the signal being
 generated. Valid values are Downlink,
 Uplink, and Sidelink.

Number of Frames: Specifies the number of radio frames to be
 generated. The default value is 1.

The valid ranges are:

- 1 to 8, inclusive, when Mode is LTE .
- 1 to 1000, inclusive, when Mode is eMTC 
 or NBIoT .

This parameter is valid only when you set the  Link
 Direction to Uplink or Downlink.

Number of Subframes: Specifies the transmission length to be
 generated in subframes. Valid values are 1 to 20. The default value is 20.  This parameter
 is valid only when you set the Link
 Direction to Sidelink.

Auto: The Auto checkbox is enabled only when
 Mode is eMTC or
 NBIoT. When you select the Auto checkbox,
 the value of the Number of Frames is calculated by RFmx Waveform
 Creator. The value of the Number of Frames is always an even number,
 when Mode is NBIoT.

Channel Bandwidth: Specifies the system bandwidth of the LTE signal.
 Valid values are 1.4 MHz, 3 MHz, 5
 MHz, 10 MHz, 15 MHz, and
 20 MHz. The default value is 10 MHz.
 When you set the Link Direction to Sidelink,
 channel bandwidth valid values are 10 MHz and 20
 MHz.

| System Bandwidth BWChannel [MHz] |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Number of Resource Blocks |  |  |  |  |  |
| 1.4 | 3 | 5 | 10 | 15 | 20 |
| 6 | 15 | 25 | 50 | 75 | 100 |

Table 1-6, The relationship of bandwidth to number of resource blocks.

Cell ID: Specifies the physical layer cell identity. The range is 0
 to 503. The default value is 0. The Cell ID is automatically incremented when Downlink Test
 Model is configured in multiple carriers.

Oversampling Factor: Specifies the oversampling factor to be used in
 the simulation. When the Auto is checked, the oversampling rate is
 adjusted automatically.

Cyclic Prefix Mode: Specifies the cyclic prefix (CP) type of the
 signal being generated. Normal cyclic prefix and extended cyclic prefix are supported.

Mode: Specifies the LTE carrier type. Valid values are
 LTE, eMTC, and
 NB-IoT. The default value is LTE.

Short Frame Generation: Specifies the short frame generation
 settings which allows you to generate a limited number of contiguous slots instead of
 full-frame. Short Frame is currently not supported for downlink channels, PRACH channels,
 and sidelink channels.

Enabled: If the Enabled checkbox is
 selected, it enables short frame generation, otherwise full frame is generated.

Offset (slots): Specifies the offset in slots within an LTE frame
 from where the waveform is generated. Valid values are 0 to 19, when mode is
 LTE or eMTC. Valid value is 0, when
 mode is NB-IoT.

Length (slots): Specifies the number of slots within an LTE frame
 to be generated. Valid values are 1 to 20.

Note

- Offset (slots) + Length (slots) cannot
 be greater than 20. Either Length(slots) or Offset
 (slots) is coerced to satisfy this requirement.
- When short frame is enabled, Number of Frames is restricted
 to 1. In NB-IoT mode, Number of Frames 
 varies from 1 to 4 based on Length(slots) and SC
 Spacing .

Time Domain Windowing: Time domain windowing is not mandatory in the
 LTE standard. The window function is employed to reduce out-of-band spectrum emissions.
 Time domain windowing helps in reducing the spectral sidelobes, that occurs because of the
 discontinuity at OFDM symbol boundaries, by creating an overlap between the two symbols
 (overlap duration specified by the time domain windowing duration). Larger the window
 duration, more is the overlap. This causes more samples to distort in the time domain,
 leading to a steeper reduction in sidelobe. The smaller bandwidths require larger time
 domain window.

State: Specifies whether the time domain windowing function is to
 be applied to the simulation. If the State checkbox is selected,
 windowing is to be employed. The checkbox is selected by default.

Duration: Specifies the time interval of the time domain
 windowing function. Increasing the transition time, increases the spectrum roll-off at
 the cost of a decreased delay spread tolerance. The default value of the time domain
 window duration is 500 ns. This default value is optimized for a
 10 MHz LTE signal. The transition time range is 0 to 4600 ns, inclusive.

Auto: When you select this checkbox, the value of the
 Duration parameter is set to a recommended value based on
 Channel Bandwidth. The checkbox is selected by default.

Refer to the following table for recommended values.

| Channel Bandwidth | Auto Window Duration |
| --- | --- |
| 20 MHz | 340 ns |
| 15 MHz | 350 ns |
| 10 MHz | 500 ns |
| 5 MHz | 800 ns |
| 3 MHz | 1600 ns |
| 1.4 MHz | 3200 ns |
| 200 kHz | 3200 ns |

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte-fdd-mode-nb-iot.html language=enus -->
## TOPIC 00078: Mode: NB-IoT

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte-fdd-mode-nb-iot.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte-fdd-mode-nb-iot.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frame configuration options for narrow band internet of things (NB-IoT) transmissions. Uplink Frame Configuration The following options are available for a narrow band internet of things (NB-IoT) transmission when you set the Link Direction to Uplink and Mode to NB-IoT. SC Spacing Specifies the spac

### Mode: NB-IoT

Frame configuration options for narrow band internet of things (NB-IoT)
 transmissions.

Parent topic:

Frame Configuration

#### Uplink Frame Configuration

The following options are available for a narrow band internet of things (NB-IoT)
 transmission when you set the Link Direction to
 Uplink and Mode to
 NB-IoT.

SC Spacing

NPUSCH Format

NPUSCH

1

2

Modulation

BPSK

QPSK

QPSK

Note

3GPP TS 36.211 V14.2.0 (2017-04)

[IMAGE alt='image' src='GUID-1AE3300D-8F29-4703-AB92-D2BB32971CD9-a5.gif']

Start Slot

Note

Number of Frames

Repetition

Note

3GPP TS 36.213 V14.2.0 (2017-04)

Resource Units

3GPP TS 36.213 V14.2.0 (2017-04)

Tone Offset

3GPP TS 36.213 V14.2.0 (2017-04)

[IMAGE alt='image' src='GUID-871C8121-7993-4041-96B5-F72B38A557B9-a5.gif']

Number of Tones

Slots

3GPP TS 36.211 V14.2.0 (2017-04)

[IMAGE alt='image' src='GUID-8BA079F1-4ED8-4FE1-B78C-00012E01A985-a5.gif']

Power (dB)

#### Downlink Frame Configuration

The following options are available for a narrow band internet of things (NB-IoT)
 transmission when you set the Link Direction to
 Downlink and Mode to
 NB-IoT.

##### NPDSCH

State

Modulation

Start Subframe

Note

Number of Subframe

Repetition

Data Source

data source

Selecting the Data Source

Power (dB)

##### NPDCCH

State

Start Subframe

Maximum Repetition

Repetition

Maximum Repetition

Format

NCCE

- NCCE 0 occupies subcarriers 0 through 5.
- NCCE 1 occupies subcarriers 6 through 11.

Data Source

data source

Selecting the Data Source

Power (dB)

Related concepts:

- Selecting the Data Source

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte-filter-types.html language=enus -->
## TOPIC 00079: LTE Filter Types

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte-filter-types.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte-filter-types.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Waveform Creator supports two different filter types for LTE, such as: LTE(Improved EVM): Gives better EVM performance. Preferred for ModAcc measurements. LTE(Improved ACP): Preferred for Adjacent Channel Power measurements. Default value of filter length for LTE FDD is 56, LTE TDD is 150, LTE

### LTE Filter Types

RFmx Waveform Creator supports two different filter types for LTE, such as:

- LTE(Improved EVM) : Gives better EVM performance. Preferred
 for ModAcc measurements.
- LTE(Improved ACP) : Preferred for Adjacent Channel Power
 measurements. Default value of filter length for LTE FDD is 56, LTE TDD is 150, LTE
 LAA is 150, and for NBIOT is 115.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte-frame-structure.html language=enus -->
## TOPIC 00080: LTE Frame Structure

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte-frame-structure.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte-frame-structure.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Three radio frame structures are defined in LTE: frame structure type 1, which uses both FDD and TDD duplexing, and frame structure type 2, which uses TDD duplexing. Fig. 1-1 shows frame structure type 1 as implemented in RFmx Waveform Creator. A DL/UL radio frame has a duration of 10 ms and consist

### LTE Frame Structure

Three radio frame structures are defined in LTE: frame structure type 1, which uses both
 FDD and TDD duplexing, and frame structure type 2, which uses TDD duplexing. Fig. 1-1
 shows frame structure type 1 as implemented in RFmx Waveform Creator. A DL/UL radio
 frame has a duration of 10 ms and consists of 20 slots with a slot duration of 0.5 ms.
 Two slots makes one subframe. A subframe, also known as the transmission time interval
 (TTI), has a 1 ms duration.

[IMAGE alt='image' src='GUID-61CA36D4-0561-4364-88A4-53A17576B88F-a5.gif']

Fig. 1-1 LTE Frame structure

When you use the TDD duplexing, the frame will contain the following 3 types of
 subframe:

- Downlink
- Uplink
- Special

The ratio of Uplink/Downlink subframes is controlled by the Uplink/Downlink
 configuration. The Uplink/Downlink configuration can take a value of 0 to 6. The special
 subframe consists of:

- DwPTS (Downlink Pilot time slot) :- Used for the downlink signal.
- GP: - A guard period where neither the downlink is transmitted.
- UpPTS (Uplink pilot time slot) :- Used for uplink signal.

The following figure shows the configuration of a special subframe

[IMAGE alt='image' src='GUID-EDA62D88-FF32-4D4C-BB88-653201D790C7-a5.gif']

Fig. 1-2 the configuration of a special subframe

The special subframe is transmitted in subframe 1 and may also be transmitted in subframe
 5 (depending on the Uplink/Downlink configuration).

The following table shows the possible Uplink/Downlink configurations. Where, D =
 downlink subframe, U = Uplink Subframe, and S = Special subframe.

The special subframe marks the point at which the frame stops being used for downlink and
 starts being used for uplink.

[IMAGE alt='image' src='GUID-910121B5-C8E1-4FA1-AD6B-29CDF4640E51-a5.gif']

Table 1-3 TDD Uplink/Downlink configurations (Table 4.2-2 from 3GPP TS
 36.211 V8.9.0 (2009-12))

The length of the DwPTS, GP, and UpPTS is controlled by the special subframe
 configuration.

The following table shows the possible special subframe configurations.

[IMAGE alt='image' src='GUID-39132641-1283-4733-B1CE-D7101FFBCA6A-a5.gif']

Table 1-4 Special subframe configurations (Table 4.2-1 from 3GPP TS
 36.211 V12.5.0 (2009-12))

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte-modulation-schemes.html language=enus -->
## TOPIC 00081: LTE Modulation schemes

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte-modulation-schemes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte-modulation-schemes.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Long Term Evolution (LTE) uses Adaptive Modulation and Coding (AMC) to improve data throughput. Based on the channel quality for each user, this technique varies in the downlink modulation coding scheme. When the link quality is good, the LTE system uses a higher order modulation scheme, which resul

### LTE Modulation schemes

Long Term Evolution (LTE) uses Adaptive Modulation and Coding (AMC) to improve data
 throughput. Based on the channel quality for each user, this technique varies in the
 downlink modulation coding scheme.

When the link quality is good, the LTE system uses a higher order modulation scheme,
 which results in more system capacity. On the other hand, when link quality is poor due
 to problems such as signal fading, the LTE system can change to a lower modulation
 scheme to maintain reliability and minimize error.

The allowed modulation schemes for DL and UL are shown in the following tables.

| Physical channels | Modulation scheme |
| --- | --- |
| Physical signal | Modulation scheme |
| PBCH, PCFICH, PDCCH | QPSK |
| PDSCH | QPSK, QAM16, QAM64, QAM256, QAM1024 |
| PHICH | BPSK |
| Reference | Orthogonal sequence modulated by binary random sequence |
| Primary synchronization | Cycle of three Zadoff-Chu sequence |
| Secondary synchronization | Two 31-bit BPSK M-sequence |

Table 1-1 Downlink channels and signals

| Physical channels | Modulation scheme |
| --- | --- |
| Physical signal | Modulation scheme |
| PUCCH | Based on Zadoff-Chu |
| PUSCH | QPSK, QAM16, QAM64, QAM256, QAM1024 |
| NPUSCH Format 1 | BPSK, QPSK |
| NPUSCH Format 2 | BPSK |
| PRACH1 | Based on the uth root Zadoff-Chu |
| Demodulation reference for PUCCH, PUSCH | Based on Zadoff-Chu |
| SRS | Based on Zadoff-Chu |

Table 1-2 Uplink channels and signals

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte-multi-carrier.html language=enus -->
## TOPIC 00082: LTE Multi-Carrier

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte-multi-carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte-multi-carrier.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This window allows you to configure multiple LTE carrier parameters. Click Edit to edit the carrier parameters. Parameters Number of Carrier Sets: Specifies the number of carrier sets, which is the number of waveforms to be generated. Auto Increment Cell ID Enabled: Specifies whether the Cell ID of

### LTE Multi-Carrier

This window allows you to configure multiple LTE carrier parameters. Click
 Edit to edit the carrier parameters.

[IMAGE alt='image' src='GUID-6CEB0A44-1CC0-41AC-9CE2-8F6F611ECF89-a5.png']

Parameters

Number of Carrier Sets: Specifies the number of carrier sets,
 which is the number of waveforms to be generated.

Auto Increment Cell ID Enabled: Specifies whether the Cell ID of
 component carriers is auto-calculated during waveform generation.

| Link Direction/Test Model | Auto Increment Cell ID Enabled | Cell ID for Carrier |
| --- | --- | --- |
| Uplink or Downlink-User Defined | False | Uses Cell ID specified in the Carrier Definition tab. |
| True | Cell ID of the first carrier is 0. Cell ID is incremented by 1 for each carrier. |  |
| Downlink-Test Model | N/A | Cell ID of the first carrier is 1. The Cell ID is incremented by 1 for each carrier as defined in 3GPP TS 36.141 specifications. |
| Sidelink | N/A | N/A |

Refer to Cell ID parameter in the Carrier
 Definition tab to configure Cell ID manually.

Note

Cell ID

Multi-Carrier

Carrier Set

Carrier Set Number: Specifies the index of carrier set. The
 default and minimum value is zero. The maximum value depends on the number of
 carrier sets.

Oversampling Factor: Sets the oversampling factor. This
 control enables you to increase the default sample rate. The default value is 1. To
 change the oversampling factor manually, unselect the Auto
 checkbox.

Auto: When this checkbox is unselected,
 Oversampling Factor is disabled and set to 1.

Phase Continuous: When this checkbox is selected, it coerces
 the carrier frequency offset to the closest cyclic frequency offset value such that
 the aggregated waveform is phase continuous. This parameter updates the
 CC Offset control upon clicking
 OK. Frequency offset will be recalculated each time any
 carrier is added, modified, or removed. Phase Continuous
 checkbox is selected by default.

Number of Subblocks: Specifies the number of subblocks in the
 selected carrier set.

Carrier PSD Equalization: When this checkbox is unselected,
 the component carrier signals are scaled such that they have equal average (RMS)
 power. When this checkbox is selected, the component carrier signals are scaled such
 that they have equal power spectral density (PSD). In this mode, the relative
 channel power is maintained between component carriers. Hence, if the PUSCH channel
 has a power boosting of 3 dB on one carrier, it will have 3 dB higher power spectral
 density compared to a PUSCH channel with 0 dB power boosting on the other component
 carrier. Carrier PSD Equalization checkbox is unselected by
 default.

Subblock

Subblock Number: Specifies the index of subblock. The default
 and minimum value is zero. The maximum value depends on the number of subblocks.

Subblock Offset: Specifies the frequency offset of the
 specified subblock from center frequency.

Reference CC Index: Specifies the component carrier index of
 the reference component carrier. The center of the reference component carrier is
 placed at the subblock offset. The value of Reference CC
 Index and Spacing Type is used to calculate
 the CC Offset.

Note

Spacing Type: Specifies the spacing between the two adjacent
 component carriers within a subblock.

- Nominal - Calculates the frequency spacing between
 component carriers as defined in section 5.4.1A of the 3GPP TS
 36.521 specification, and sets the CC
 offset .
- Minimum - Calculates the frequency spacing between
 component carriers as defined in section 5.4.1A of the 3GPP TS
 36.521 specification, and sets the CC
 Offset .
- User - The component carrier offset that you configure in
 the CC Offset is used.

Number of CCs: Specifies the number of component carriers of
 the selected subblocks. When you increase the value of the number of carrier sets,
 new carrier sets are added. These newly added carrier sets are preconfigured with
 the configuration of the last carrier set. When you decrease the value of the number
 of carrier sets, the carrier sets are deleted.

Note

Number of Subblocks

Number of CCs

Component Carrier

CC Index: Specifies the index component carrier. The default
 and minimum value is zero. The maximum value depends on number of CCs.

Carrier Definition Number: Specifies the carrier as defined by
 the Carrier Definition Number in the Modulation tab.

CC Offset: Specifies the offset of each carrier to subblock
 offset.

Gain, Phase, Random Phase, Delay, and Random Delay: These
 parameters are set on each component carrier.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte-references.html language=enus -->
## TOPIC 00083: References

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte-references.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte-references.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: 3GPP TS 36.201 Evolved Universal Terrestrial Radio Access (E-UTRA); Physical Layer – General Description. 3GPP TS 36.211 Evolved Universal Terrestrial Radio Access (E-UTRA); Physical Channels and Modulation. 3GPP TS 36.212 Evolved Universal Terrestrial Radio Access (E-UTRA); Multiplexing and channel

### References

| 3GPP TS 36.201 | Evolved Universal Terrestrial Radio Access (E-UTRA); Physical Layer – General Description. |
| --- | --- |
| 3GPP TS 36.211 | Evolved Universal Terrestrial Radio Access (E-UTRA); Physical Channels and Modulation. |
| 3GPP TS 36.212 | Evolved Universal Terrestrial Radio Access (E-UTRA); Multiplexing and channel coding. |
| 3GPP TS 36.213 | Evolved Universal Terrestrial Radio Access (E-UTRA); Physical layer procedures. |
| 3GPP TS 36.321 | Evolved Universal Terrestrial Radio Access (E-UTRA); Medium Access Control (MAC) protocol specification |
| 3GPP TS 36.141 | Evolved Universal Terrestrial Radio Access (E-UTRA); Base Station (BS) conformance testing |

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte-slot-structure.html language=enus -->
## TOPIC 00084: LTE Slot Structure

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte-slot-structure.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte-slot-structure.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The smallest time-frequency grid for downlink transmission is called a Resource Element, which is one symbol on one sub-carrier. A group of 12 contiguous sub-carriers in frequency and one slot in time form a Resource Block (RB) as shown in the following figure. Data is allocated to each User Equipme

### LTE Slot Structure

The smallest time-frequency grid for downlink transmission is called a Resource Element,
 which is one symbol on one sub-carrier. A group of 12 contiguous sub-carriers in
 frequency and one slot in time form a Resource Block (RB) as shown in the following
 figure. Data is allocated to each User Equipment (UE) in units of RB.

[IMAGE alt='image' src='GUID-DFE0E4E5-EBFC-449E-8763-D8497FB544C9-a5.gif']

Fig. 1-3 LTE resource grid

When using normal Cyclic Prefix (CP), a RB spans 12 consecutive sub-carriers at a
 sub-carrier spacing of 15 kHz, and seven consecutive symbols over a slot duration of 0.5
 ms as shown in Fig. 1-1.

A CP is added to each symbol as a guard period. Thus, an RB has 84 resource elements (12
 sub-carriers x 7 symbols), corresponding to one slot in the time domain and 180 kHz (12
 sub-carriers x 15 kHz spacing) in the frequency domain.

The size of an RB is the same for all bandwidths, therefore the number of available
 physical RBs depends on the transmission bandwidth. In the frequency domain, the number
 of available RBs can range from 6 (when transmission bandwidth is 1.4 MHz), to 100 (when
 transmission bandwidth is 20 MHz).

Note that the number of symbols in a slot depends on the CP length. For a normal CP,
 there are seven OFDM/SC-FDMA symbols per slot. For extended CP there are six
 OFDM/SC-FDMA symbols per slot. In a TDD special subframe the number of OFDM symbols
 allocated for Uplink/Downlink depends on the special sub frame configuration.

[IMAGE alt='image' src='GUID-9BCD3319-396A-4F3B-AE2B-D8563C855B4D-a5.gif']

Table 1-5 Number of symbols per slot and number of sub-carriers per
 resource block for different cyclic prefix type

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte-tdd-carrier-configuration.html language=enus -->
## TOPIC 00085: Carrier Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte-tdd-carrier-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte-tdd-carrier-configuration.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section allows you to configure the top level modulation parameters of the FDD Signal. It comprises the controls as described below. Link Direction: Specifies the link direction of the signal being generated. Valid values are Downlink, Uplink, and Sidelink. Number of Frames: Specifies the numbe

### Carrier Configuration

This section allows you to configure the top level modulation parameters of the FDD Signal.
 It comprises the controls as described below.

[IMAGE alt='image' src='GUID-5E6B98A1-1AF4-4C78-8383-C9E1D187A31E-a5.png']

Link Direction: Specifies the link direction of the signal being
 generated. Valid values are Downlink,
 Uplink, and Sidelink.

Number of Frames: Specifies the number of radio frames to be
 generated. The default value is 1.

The valid ranges are:

- 1 to 8, inclusive, when Mode is LTE .
- 1 to 1000, inclusive, when Mode is
 eMTC .

Auto: The Auto checkbox is enabled only when
 Mode is eMTC or
 NBIoT. When you select the Auto checkbox,
 the value of the Number of Frames is calculated by RFmx Waveform
 Creator.

UL DL Configuration: This parameter specifies the UL – DL Frame
 configuration. The valid range is 0 to 6. The default value is 0.

This controls the ratio of Uplink/Downlink subframes. Refer to Table 1-3 in LTE Frame
 Structure.

Special Subframe Configuration: This parameter specifies the
 configuration index of special subframes generated within the LTE TDD signal. The range is
 0 to 9. The default value is 0. The special subframe configuration controls the length of
 the DwPTS, GP, and UpPTS (Refer Table 1-4)

Channel Bandwidth: Specifies the system bandwidth of the LTE signal.
 Valid values are 1.4 MHz, 3 MHz, 5
 MHz, 10 MHz, 15 MHz, and
 20 MHz. The default value is 10 MHz.
 When you set the Link Direction to Sidelink,
 channel bandwidth valid values are 10 MHz and 20
 MHz.

| System Bandwidth BWChannel [MHz] | Number of Resource Blocks |
| --- | --- |
| 1.4 | 6 |
| 3 | 15 |
| 5 | 25 |
| 10 | 50 |
| 15 | 75 |
| 20 | 100 |

Table 1-6, The relationship of bandwidth to number of resource blocks.

Cell ID: Specifies the physical layer cell identity. The range is 0
 to 503. The default value is 0. The Cell ID is automatically incremented when Downlink Test
 Model is configured in multiple carriers.

Oversampling Factor: Specifies the oversampling factor to be used in
 the simulation. When the Auto is checked, the oversampling rate is
 adjusted automatically.

Cyclic Prefix Mode: Specifies the cyclic prefix (CP) type of the
 signal being generated. Normal cyclic prefix and extended cyclic prefix are supported.

Mode: Specifies the LTE carrier type. Valid values are
 LTE and eMTC. The default value is
 LTE.

Short Frame Generation: Specifies the short frame generation
 settings which enables you to generate a limited number of contiguous slots instead of full
 frame. Short Frame is currently not supported for downlink channels and PRACH channels.

Enabled: If the Enabled checkbox is selected,
 it enables short frame generation, otherwise full frame is generated. When short frame is
 enabled, Number of Frames is restricted to 1.

Offset (slots): Specifies the offset in slots within an LTE frame
 from where the waveform is generated. Valid values are 0 to 19.

Length (slots): Specifies the number of slots within an LTE frame to
 be generated. Valid values are 1 to 20.

Note

Offset (slots)

Length (slots)

Length(slots)

Offset
 (slots)

Time Domain Windowing: Time domain windowing is not mandatory in the
 LTE standard. The window function is employed to reduce out-of-band spectrum emissions.
 Time domain windowing helps in reducing the spectral sidelobes, that occurs because of the
 discontinuity at OFDM symbol boundaries, by creating an overlap between the two symbols
 (overlap duration specified by the time domain windowing duration). Larger the window
 duration, more is the overlap. This causes more samples to distort in the time domain,
 leading to a steeper reduction in sidelobe. The smaller bandwidths require larger time
 domain window.

State: Specifies whether the time domain windowing function is to be
 applied to the simulation. If the State checkbox is selected,
 windowing is to be employed. The checkbox is selected by default.

Duration: Specifies the time interval of the time domain windowing
 function. Increasing the transition time, increases the spectrum roll-off at the cost of a
 decreased delay spread tolerance. The default value of the time domain window duration is
 500 ns. This default value is optimized for a 10 MHz LTE signal.
 The transition time range is 0 to 4600 ns, inclusive.

Auto: When you select this checkbox, the value of the
 Duration parameter is set to a recommended value based on
 Channel Bandwidth. The checkbox is selected by default.

Refer to the following table for recommended values.

| Channel Bandwidth | Auto Window Duration |
| --- | --- |
| 20 MHz | 340 ns |
| 15 MHz | 350 ns |
| 10 MHz | 500 ns |
| 5 MHz | 800 ns |
| 3 MHz | 1600 ns |
| 1.4 MHz | 3200 ns |

Parent topic:

LTE

Related concepts:

- LTE Frame Structure

<!--NI_TOPIC bundle=rfmx-waveform-creator path=lte.html language=enus -->
## TOPIC 00086: LTE

- bundle_id: `rfmx-waveform-creator`
- source_path: `lte.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/lte.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creates a waveform that simulates a 3GPP LTE carrier. The modulation scheme for 3GPP LTE is defined in the 3GPP TS 36.211 and 3GPP TS 36.212 specifications. This document assumes that you know how to package and download files to an instrument. For more information about packaging and downloading fi

### LTE

Creates a waveform that simulates a 3GPP LTE carrier.

The modulation scheme for 3GPP LTE is defined in the *3GPP TS 36.211*
 and *3GPP TS 36.212* specifications.

Note

Generating and Saving the Waveform
 File

Parent topic:

RFmx Waveform Creator Modulation Schemes

Related information:

- RFmx LTE .NET Reference
- RFmx LTE C API Reference

<!--NI_TOPIC bundle=rfmx-waveform-creator path=markers.html language=enus -->
## TOPIC 00087: Markers

- bundle_id: `rfmx-waveform-creator`
- source_path: `markers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/markers.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This sub-menu lets you control how markers are displayed on the graph. You can enable up to four markers and a delta marker. Markers are available for all graph types. The markers allow individual points to be selected on the graph and tracked using the marker area underneath of the trace graticule.

### Markers

This sub-menu lets you control how markers are displayed on the graph. You can enable up
 to four markers and a delta marker.

Markers are available for all graph types. The markers allow individual points to be
 selected on the graph and tracked using the marker area underneath of the trace
 graticule. All measurements support up to 4 individual markers and a single delta.

To add a Marker,

1. Select any modulation schemes from the Modulation menu.
2. Click Graphics tab.
3. Click Markers menu or right-click on the trace.
4. Select the marker you want to add, and select Enable . This
 will turn the marker on and move the marker to the location clicked on the
 trace.

Moving a Marker

Markers can be moved in several ways.

- Left and Right Arrows — When a marker is selected, pressing
 the left and right buttons on your keyboard will move the marker a single sample
 backwards or forwards from the current marker position.
- Page Up/Down — When a marker is selected, pressing the page
 up or down buttons on your keyboard will move the marker 10 samples backwards or
 forwards from the current marker position.
- Using the Mouse — You can move a marker using the mouse, by
 clicking and dragging the marker to the desired location. For non polar plots, the
 marker will be moved to the closest sample in the X domain to the current mouse
 position. In a polar plot, the marker will be moved to the nearest sample to the
 current mouse position.
- Move Marker to Here — If you right-click on the trace
 graticule, within the marker menu for the desired marker, you can select
 Move marker to here . This will move the marker to the
 selected location.

[IMAGE alt='image' src='GUID-337A1148-7E24-4E81-B6FB-6E97D0210974-a5.png']

#### Marker Controls

As the basic marker functions, RFmx Waveform Creator supports specific marker functions
 that can be used to find particular artifacts within the trace. These are as
 follows:

- All Markers Off – Use this function to turn off all markers
 that are currently enabled.
- Enable – Use this function to turn a marker on or off. The
 first time a marker is enabled, it is automatically moved to the first location you
 right clicked.
- Track Peak – Enables a marker and automatically moves it to
 the highest Y value in the trace. When you select this option the marker
 automatically moves whenever the trace data is regenerated.
- Peak Find – Moves the marker to the highest value on the
 trace.
- Last Peak – Moves the marker to the next highest peak to the
 current marker position.
- Next Peak – Moves the marker to the next lowest peak to the
 current marker position.
- Peak Right – Moves the marker to the next peak to the right
 of the current marker position.
- Peak Left – Moves the marker to the next peak to the left of
 the current marker position.
- Delta Marker – The delta marker is manipulated in exactly the
 same way as normal markers. As the delta marker reports values relative to normal
 markers you can only display a delta marker if a normal marker is enabled.

When a delta marker is enabled, the marker table is updated with delta values.
 The following image depicts the Graphics tab with all
 markers enabled. As the delta marker does not report its own values, but instead
 the differences between its position and other markers, the Delta marker can
 only be enabled if you have one or more standard markers enabled.

[IMAGE alt='image' src='GUID-337A1148-7E24-4E81-B6FB-6E97D0210974-a5.png']

<!--NI_TOPIC bundle=rfmx-waveform-creator path=mode-emtc.html language=enus -->
## TOPIC 00088: Mode: eMTC

- bundle_id: `rfmx-waveform-creator`
- source_path: `mode-emtc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/mode-emtc.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frame configuration options for eMTC (Enhanced Machine-Type Communication) transmissions. The following configuration options are available when you set the Link Direction to Uplink and Mode to eMTC. Subframe ConfigurationThe subframe configuration parameter State is available for each eMTC Uplink s

### Mode: eMTC

Frame configuration options for eMTC (Enhanced Machine-Type Communication)
 transmissions.

The following configuration options are available when you set the Link
 Direction to Uplink and
 Mode to eMTC.

#### Subframe Configuration

The subframe configuration parameter
 State is available for each eMTC Uplink subframe that is
 being configured.

State

State

#### eMTC
 Configuration

Allows you to configure the parameters that are applicable
 for an eMTC transmission.

CE Mode

Mode A

Mode B

Mode A

NB Hopping State

Number of Retuning Symbols

CE PUSCH Maximum Bandwidth

3GPP TS 36.212 v14.6.0 (2018-07)

3GPP TS 36.213 v14.6.0 (2018-04)

- The maximum supported PUSCH channel bandwidth is
 5MHz when you set CE
 Mode to Mode A .
- The maximum supported PUSCH channel bandwidth is
 1.4MHz when you set CE
 Mode to Mode B .

1.4MHz

5MHz

1.4
 MHz

NB Hopping Interval

NB
 Hopping State

3GPP TS 36.331 V14.2.2 (2017-05)

| CE Mode | Valid Values |
| --- | --- |
| Mode A | 1, 5, 10, 20 |
| Mode B | 5, 10, 20, 40 |

NB Hopping Offset

NB Hopping
 State

3GPP TS 36.211 V14.2.2 (2017-04)

| Channel Bandwidth | Valid Values |
| --- | --- |
| 1.4 MHz | 0 |
| 3 MHz | 1 |
| 5 MHz | 1 to 3 |
| 10 MHz | 1 to 7 |
| 15 MHz | 1 to 11 |
| 20 MHz | 1 to 15 |

Content

PUSCH

Modulation

QPSK

16 QAM

64 QAM

QPSK

Start Subframe

Note

Start
 Subframe

Number of
 Frames

Repetitions

3GPP TS 36.213 V14.2.0 (2017-04)

| CE Mode | Valid Values |
| --- | --- |
| Mode A | 1, 2, 4, 8, 16, 32 |
| Mode B | 1, 4, 8, 16, 32, 64, 128, 192, 256, 384, 512, 768, 1024, 1536, 2048 |

Number of Absolute Subframes

Start NarrowBand

3GPP TS 36.211 V14.2.2 (2017-04)

| Channel Bandwidth | Valid Values |
| --- | --- |
| 1.4 MHz | 0 |
| 3 MHz | 0 to 1 |
| 5 MHz | 0 to 3 |
| 10 MHz | 0 to 7 |
| 15 MHz | 0 to 11 |
| 20 MHz | 0 to 15 |

Number of Resource Blocks

CE PUSCH Maximum Bandwidth

1.4MHz

Number of Resource
 Blocks

Resource Block Offset

Number of Resource
 Blocks

Resource Block Offset

Number of Resource Blocks

Number of Resource Block Offset

Number of Resource Block
 Offset

- When CE PUSCH Maximum Bandwidth is
 1.4 MHz , the valid value range is 1 to 6,
 inclusive. When CE PUSCH Maximum Bandwidth is
 5MHz , the valid value range is 1 to 24,
 inclusive. The default value is 1.
- If you change CE PUSCH Maximum Bandwidth from
 5MHz to 1.4MHz and
 if Number of Resource Blocks is greater than
 6, Number of Resource Blocks is coerced to 6
 and Resource Block Offset is coerced to
 0.

Resource Block Offset

CE PUSCH Maximum Bandwidth

5MHz

1.4MHz

Number of Resource Blocks

Number of Resource Blocks

Resource Block Offset

Power (dB)

Parent topic:

Frame Configuration

<!--NI_TOPIC bundle=rfmx-waveform-creator path=mode-lte-downlink.html language=enus -->
## TOPIC 00089: Mode: LTE

- bundle_id: `rfmx-waveform-creator`
- source_path: `mode-lte-downlink.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/mode-lte-downlink.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Downlink configuration options for LTE (Long-Term Evolution) transmissions. Downlink Configuration Number of Antennas Specifies the number of antennas that will be used in the signals for cell-specific reference signals, downlink control channels (PCFICH, PHICH, PDCCH,PBCH), and PDSCH configured wit

### Mode: LTE

Downlink configuration options for LTE (Long-Term Evolution)
 transmissions.

#### Downlink Configuration

Number of Antennas

Ng

UE Category

Modulation Mode

MCS Index

User Defined

MCS
 Index

Note

Modulation Mode

User Defined

PHICH Duration

Number Of Beamforming Antennas

Generating a MIMO Signal

#### Downlink Channels

This table allows you
 to edit the downlink channels configurations.

Power

State

On

Edit

Edit

PBCH

- PBCH State : Allows you to turn off the PBCH
 within the signal. If PBCH State is selected,
 the PBCH Channel will be transmitted,
 otherwise, it will not be included in the signal. By default,
 PBCH State is checked.
- Transmit SFN : Specifies whether the subframe
 number will be broadcast as part of the PBCH Channel. If the
 Transmit SFN checkbox is selected, SFN
 will be transmitted.
- Data Source : Specifies the payload data of
 the PBCH Channel. Refer to Selecting the Data Source 
 topic for more information on data source.

#### Channel State Indication Reference Signal(CSI
 RS)

CSI RS State

CSI RS Cell ID

CSI RS configuration

CSI RS Subframe Configuration

[IMAGE alt='CSI-RS sub-frame configuration' src='GUID-419C987D-D0B3-4B2B-9656-CED66BBCA333-a5.gif']

#### Positioning Reference Signal (Positioning
 RS)

Positioning reference signal is taken into consideration to determine
 the location of user equipment based on radio access network information.

Positioning RS State

Number of PRS RBs

PRS Subframe Configuration

Parent topic:

Downlink Configuration

Related concepts:

- Selecting the Data Source
- Generating a MIMO Signal

<!--NI_TOPIC bundle=rfmx-waveform-creator path=mode-lte.html language=enus -->
## TOPIC 00090: Mode: LTE

- bundle_id: `rfmx-waveform-creator`
- source_path: `mode-lte.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/mode-lte.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Frame configuration options for LTE (Long-Term Evolution) transmissions. Click a specific subframe to configure the settings corresponding to that subframe. The parameters you can configure for each subframe differ depending on whether the signal is uplink, downlink, or sidelink. Uplink Subframe Con

### Mode: LTE

Frame configuration options for LTE (Long-Term Evolution) transmissions.

Click a specific subframe to configure the settings corresponding to that subframe. The
 parameters you can configure for each subframe differ depending on whether the signal
 is uplink, downlink, or sidelink.

#### Uplink Subframe Configurations

The following are the parameters that are
 available when you set Link Direction to
 Uplink.

Apply to all subframes

Channel Type

Current Channel Type

Channel Type

PUSCH+PUCCH

Modulation Type

Channel Type

PUSCH

Modulation Mode

User Defined

MCS Index

Power

Channel Type

PUSCH

PUCCH

N2 DMRS

Channel Type

PUSCH

DMRS

(2)

Hopping Type

Channel Type

PUSCH

Hopping Bits

Channel Type

PUSCH

3GPP TS 36.213 V8.8.0 (2009-09)

[IMAGE alt='image' src='GUID-B3D23E22-11B2-4E4C-9826-D19E4D3CE906-a5.gif']

Resource Allocation Type

Channel Type

PUSCH

3GPP 36.213

[IMAGE alt='image' src='GUID-FD068E6F-4880-4A1E-BB89-ADFA6DCC0EB4-a5.gif']

Number of RBs

Channel Type

PUSCH

Resource
 Allocation Type

0

- It must also be a non-zero positive value. The value of
 Starting RB + Number of
 RBs cannot exceed the total system bandwidth. The
 number of resource blocks available for specific bandwidths is
 listed in Table 1-6
- When hopping is enabled, another level of restriction is imposed. In
 this case, M RB PUSCH cannot
 exceed the hopping bandwidth.

Starting RB

Channel Type

PUSCH

Resource
 Allocation Type

0

- If hopping is disabled, the sum of Starting Virtual RB and
 M RB PUSCH should not go
 beyond the bandwidth. Table 1-6 lists the number of resource blocks
 available for specific bandwidths.
- If hopping is enabled, you should ensure that the Starting Virtual
 RB lies within the hopping bandwidth.

Number of RBGs

Channel Type

PUSCH

Resource
 Allocation Type

Starting RBG Set
 2

Starting RBG

Channel Type

PUSCH

Resource
 Allocation Type

Starting RBG Set 2

Number of RBGs Set 2

Channel Type

PUSCH

Resource
 Allocation Type

Starting RBG Set 2

Starting RBG Set 2

Channel Type

PUSCH

Resource
 Allocation Type

- Denote the number of resource block groups in the bandwidth as
 N RBG UL
- Number of RBGs must be an integer in the range 1 to
 N RBG UL -2.
- Starting RBG must be an integer between 0 and
 N RBG UL -3
- Starting RBG Set 2 must be an integer in the range Starting RBG +
 Number of RBGs + 1 to
 N RBG UL -1.
- Number of RBGs Set 2 must be an integer in the range 1 to
 N RBG – Starting RBG Set 2.
- Number of RBGs Set 2 + Number of RBGs must follow the rules given
 for the parameter Number of RBs.

[IMAGE alt='image' src='GUID-A216B85F-BA1B-4042-A659-11CDDBCC9994-a5.gif']

Code Rate

Channel Type

PUSCH

Modulation
 Mode

User Defined

MCS Index

Channel Type

PUSCH

Modulation
 Mode

MCS Index

Allow 256-QAM

Allow 256-QAM

Current Tx NB

Channel Type

PUSCH

Starting CCE

Channel Type

PUCCH

PUCCH Format

Channel Type

PUCCH

Auto calculate
 PUCCH

False

#### Downlink Subframe Configurations

The following parameters are available
 for any downlink subframe being configured. These are available if the
 Link Direction is set to
 Downlink.

CFI

section 5.3.4

TS 36.212

Channel Type

#### PDCCH

You can view this window by clicking the
 PDCCH Channel from the Channel
 Type drop-down menu and then clicking the
 Edit button.

It comprises of three check boxes, one
 that specifies PDCCH channel state, one that contains DL Grant specific parameters,
 and one that contains UL Grant specific parameters.

[IMAGE alt='image' src='GUID-AC3C48F9-A18C-4626-A451-472D80BFC3B1-a5.png']

PDCCH DL Grant State

PDCCH DL
 Grant State

Format

Search Space

UE Specific

Common

PDCCH UL Grant State

PDCCH UL Grant State

Search Space

UE Specific

Common

Format

DMRC Cyclic Shift

CQI/CSI Request

CQI/CSI Request

No. Of CSI Request Bits

1

MCS

Resource Allocation Type

Channel Type

PUSCH

Section 8.1

36.213

TPC Pattern

Hopping Flag

Num of CSI Request bits

SRS Requests

SRS Request

- If the SRS Request option is selected and
 Number of Antennas is set to
 1 (DCI format 0), then the SRS Request
 range will be from 0 to 1.
- If the SRS Request option is selected and
 Number of Antennas is set to
 2 (DCI format 4), then the SRS Request
 range will be from 0 to 3.

Table 8.1-1: SRS request value for
 trigger type 1 in DCI format 4

3GPP
 36.213

[IMAGE alt='image' src='GUID-391FD57C-6C7B-48ED-BFA6-FCACF0E8A2F6-a5.gif']

Note

- By default the SRS Request checkbox is
 unchecked. If the SRS Request checkbox is
 selected, the SRS Request spin box will be enabled.
- If the SRS Request checkbox is selected
 and Number of Antennas is set to
 1 , then range of SRS Request is 0 to
 1.
- If the SRS Request checkbox is selected
 and Number of Antennas is set to
 2 , then range of SRS Request is 0 to
 3.

Number Of Antennas

Number of Antennas

Uplink MIMO

#### PDSCH

This window can be shown by clicking on the PDSCH
 Channel from the Channel table and then
 clicking the Edit button.

Multiple PDSCH channels can
 be configured per subframe.

[IMAGE alt='image' src='GUID-E9F24356-D741-4422-A088-88802F83EF5B-a5.png']

Transmission Mode

[IMAGE alt='image' src='GUID-1C57A83C-13BC-4699-B773-BE9B90BDDF1C-a5.gif']

Codebook Index

- If rank is 1 or 2, then range of Codebook Index is from 0 to
 15.
- If rank is from 3 to 7, then range of Codebook Index is from 0 to
 3.
- For rank 8, it is disabled.

Precoding Matrix Indicator

- If Rank is 1, 2, or 3, the range is 0 to 15.
- If Rank is 4, the range is 0 to 7.

Rank

Transmission Mode

Closed Loop

Dual-layer
 beamforming

Eight layer spatial
 multiplexing

Eight layer spatial multiplexing
 (Release 12)

UE ID

Resource Allocation Type

- Type 0:- Controlled by a Resource Allocation Bit Mask.
- Type 2:- Controlled by Starting Resource Block and Resource Block
 Allocation Length
- Full:- Allocates all possible RBs so the signal occupies the maximum
 bandwidth.
- Custom:- Controlled by RBs specified in Resource Block
 Allocation.

Resource Allocation Bit Mask

Resource Allocation
 Type

Type 0

Starting Resource Block

Resource Allocation
 Type

Type 2

Starting RB

Number of
 RBs

Resource Block Allocation Length

Resource Allocation
 Type

Type 2

Starting RB

Number of
 RBs

Resource Block Allocation

Resource Allocation
 Type

Custom

Codeword 1 Data Source

Transmission Mode

Closed
 Loop

Open Loop

Selecting the Data
 Source

Codeword 2 Data Source

Codeword1 MCS Index

Codeword2 MCS Index

Allow 256-QAM

Allow 256-QAM

Codeword 1 Modulation Type

Modulation Mode

User Defined

Codeword 2 Modulation Type

Modulation Mode

User Defined

Specify Pa/Pb

Specify Pa/Pb

Specify Pa/Pb

Pa and Pb

A

B

A

B

B

A

Beamforming Weight Matrix

[IMAGE alt='image' src='GUID-49A8D52E-44D8-4DDD-9668-3FBF047DBDF7-a5.gif']

#### PHICH

You can view this window by clicking the PHICH
 Channel from the Channel table and then
 clicking the Edit button.

[IMAGE alt='image' src='GUID-79C93717-A1A6-49C6-9BC1-2DF5D12943A4-a5.gif']

PHICH State

PHICH State

PHICH State

ACK/NACK Pattern

Maximum Number of Channels

Channel Type

Channel Index

Channel Type

Edit

#### Sidelink Subframe Configurations

The following parameters are available
 when you set Link Direction to
 Sidelink.

Frame Index

State

State

Retransmission

Hopping Offset

Hopping Offset

Apply to all subframes

#### PSSCH

Starting RB

Number of RBs

Starting
 RB

Number of RBs

Modulation Type

Power

NXID

3GPP TS 36.211
 V14.2.0

Auto Calculate NXID

#### PSCCH

State

Starting RB

Number of RBs

Starting
 RB

Number of RBs

Modulation Type

QPSK

Power

Cyclic Shift

3GPP TS 36.211
 V14.2.0

Data Source

Parent topic:

Frame Configuration

Related concepts:

- Selecting the Data Source

<!--NI_TOPIC bundle=rfmx-waveform-creator path=mode-nb-iot-downlink.html language=enus -->
## TOPIC 00091: Mode: NB-IoT

- bundle_id: `rfmx-waveform-creator`
- source_path: `mode-nb-iot-downlink.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/mode-nb-iot-downlink.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Downlink configuration options for narrow band internet of things (NB-IoT) transmissions. The following downlink configurations are available for a narrow band internet of things (NB-IoT) transmission, when you set the Link Direction to Downlink and Mode to NB-IoT. Downlink Configuration Number of A

### Mode: NB-IoT

Downlink configuration options for narrow band internet of things (NB-IoT)
 transmissions.

The following downlink configurations are available for a narrow band internet of things
 (NB-IoT) transmission, when you set the Link
 Direction to Downlink and Mode to NB-IoT.

#### Downlink Configuration

Number of Antennas

RNTI

Modulation Mode

User Defined

#### NPBCH

You can configure the following
 parameters for the NPBCH Channel.

NPBCH State

Symbol Phase Rotation

Data Source

data source

Selecting the Data Source

Power

#### NPSS

You can configure the following
 parameters for the NPSS Channel.

NPSS State

Power

#### NSSS

You can configure the following
 parameters for the NSSS Channel.

NSSS State

Power

#### NRS

You can configure the following
 parameters for the NRS Channel.

NRS State

Power

Parent topic:

Downlink Configuration

Related concepts:

- Selecting the Data Source

<!--NI_TOPIC bundle=rfmx-waveform-creator path=mode-nb-iot.html language=enus -->
## TOPIC 00092: Mode: NB-IoT

- bundle_id: `rfmx-waveform-creator`
- source_path: `mode-nb-iot.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/mode-nb-iot.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Uplink configuration options for narrow band internet of things (NB-IoT) transmissions. The following uplink configurations are available for a narrow band internet of things (NB-IoT) transmission, when you set the Link Direction to Uplink and Mode to NB-IoT. Uplink Configuration RNTI Specifies the

### Mode: NB-IoT

Uplink configuration options for narrow band internet of things (NB-IoT)
 transmissions.

The following uplink configurations are available for a narrow band internet of things
 (NB-IoT) transmission, when you set the Link Direction to
 Uplink and Mode to
 NB-IoT.

#### Uplink Configuration

RNTI

#### NPUSCH

This tab contains configuration parameters specific to the
 narrowband physical uplink shared channel (NPUSCH) portion of the NB-IoT uplink
 signal.

Data Source

NPUSCH Data Source

Selecting the Data
 Source

#### DMRS

This tab contains configuration parameters specific to the DMRS
 portion of the NB-IoT uplink signal.

Group Hopping

NPUSCH
 Format

Group Hopping

3GPP TS 36.211 V14.2.0 (2017-04)

DSS for NPUSCH

3GPP TS 36.211
 V14.2.0 (2017-04)

Group
 Hopping

Cyclic Shift

3GPP TS 36.211 V14.2.0 (2017-04)

| Tones | Cyclic Shift |
| --- | --- |
| 3 | 0-2 |
| 6 | 0-3 |
| 12 | 0 |

Auto Calculate Base Sequence

Group Hopping

NPUSCH Format

NPUSCH Number of Tones

3

6

12

Auto Calculate Base Sequence

- When you disable the Auto Calculate Base
 Sequence checkbox, the NBIoT generation uses the
 value that you specify for the NPUSCH DMRS Base Sequence
 Index parameter.
- When you enable the Auto Calculate Base
 Sequence checkbox, the NBIoT generation uses the
 value of the Cell ID property to compute the
 NPUSCH DMRS base sequence index as defined in section 10.1.4.1.2 of
 the 3GPP TS 36.211 V14.2.0 (2017-04) 
 specification.

Base Sequence Index

3GPP TS 36.211 V14.2.0 (2017-04)

Group
 Hopping

Auto Calculate Base
 Sequence

NPUSCH Number of Tones

3

6

12

| Tones | Base Sequence Index |
| --- | --- |
| 3 | 0-11 |
| 6 | 0-13 |
| 12 | 0-29 |

Parent topic:

Uplink Configuration

Related concepts:

- Selecting the Data Source

<!--NI_TOPIC bundle=rfmx-waveform-creator path=multi-carrier-configuration.html language=enus -->
## TOPIC 00093: Multi-Carrier Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `multi-carrier-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/multi-carrier-configuration.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Multi-Carrier tab enables you to aggregate multiple carriers from multiple modulations. Configuration OptionsThis section provides the following details about the configured carriers.File: Specifies the carriers that are configured for aggregation.Frequency Offset: Specifies the frequency offset

### Multi-Carrier Configuration

The Multi-Carrier tab enables you to aggregate multiple carriers from multiple
 modulations.

[IMAGE alt='image' src='GUID-9744B9A9-62EF-469E-952E-2C23E488C8F3-a5.png']

#### Configuration Options

This section
 provides the following details about the configured
 carriers.

File: Specifies the carriers that are
 configured for aggregation.

Frequency Offset: Specifies
 the frequency offset for the carrier by which the signal shifts when all the
 carriers are aggregated. The valid values are - 500 MHz to + 500 MHz,
 inclusive.

Phase Continuous: When this checkbox is
 selected, it coerces carrier frequency offset to the closest cyclic frequency offset
 value and updates Frequency Offset control. Frequency offset is recalculated each
 time any carrier is added, modified or removed. This checkbox is available when you
 add or edit a carrier.

Gain: Specifies the power level
 of the selected carrier relative to the added carriers. The valid range is -60 dB to
 0 dB, inclusive.

Bandwidth: Specifies the carrier
 bandwidth.

Delay: Initiates aggregation at any point in
 the carrier that allows you to emulate similar signals with different time
 references.

Phase: Modifies the starting phase of the
 frequency aggregation.

Configuration Controls

RFmx Waveform Creator
 provides the following controls to configure
 carriers.

Add: Adds new
 carrier(s).

Remove: Removes
 carrier(s).

Remove All: Removes all
 carriers.

Randomize Delay: Randomizes the time
 delay of all the carriers in the random delay mode.

Reset
 Delay: Resets the random number generators that are used to
 randomize the time delay of each carrier in random
 mode.

Edit: Edits the carrier
 configuration.

Randomize Phase: Randomizes the
 phase.

Reset Phase: Resets the
 phase.

Desired Sample Rate: Represents the sample
 rate of the aggregated waveform.

Auto: When this
 checkbox is selected, the desired sample rate is automatically calculated based on
 the values of Sample Rate Mode and Oversampling
 Factor. When this checkbox is unselected, you can manually enter the
 desired sample rate. If the desired sample rate to waveform sample rate ratio
 exceeds 512, the desired sample rate is coerced to 512 times the base sampling rate.

Note

Oversampling
 Factor: Sets the oversampling factor. This control enables you to
 increase the default sample rate. The default value is 1. To change the oversampling
 factor manually, unselect the Auto
 checkbox.

Auto: When this checkbox is unselected,
 Oversampling Factor is disabled and set to
 1.

Sample Rate Mode: Specifies how
 Desired Sample Rate is calculated when
 Auto checkbox is selected.

- When Sample Rate Mode is Cellular ,
 where, Base sample rate = 1.25 * max {Abs
 (Frequency Offset) + Bandwidth / 2} * 2 Maximum input sample rate = maximum
 sample rate among input waveforms
- When Sample Rate Mode is Nyquist ,
 Desired Sample Rate = 1.25 * max {Abs (Frequency
 Offset) + Bandwidth / 2} * 2

When oversampled waveforms are used, calculated desired sample rate may be
 lesser than input waveform sample rate, in which case consider increasing the
 oversampling factor.

The default value is Cellular.
 This control is disabled when Auto checkbox is
 unselected.

Note

Cellular

Parent topic:

RFmx Waveform Creator Modulation Schemes

<!--NI_TOPIC bundle=rfmx-waveform-creator path=new-features-and-changes.html language=enus -->
## TOPIC 00094: RFmx Waveform Creator New Features and Changes

- bundle_id: `rfmx-waveform-creator`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx Waveform Creator. Discover what is new in the latest releases of RFmx Waveform Creator.If you cannot find new features and changes for your version, it might not include user-facing updates. However,

### RFmx Waveform
 Creator
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx Waveform
 Creator.

RFmx Waveform
 Creator

Note

Release Notes

Related information:

- Software and Driver Downloads

#### RFmx Waveform
 Creator
 2026 Q2 Changes

RFmx Waveform
 Creator 2026 Q2 extends waveform creation
 functionality by adding support for IEEE P802.11bn/D1.3 compliant 802.11bn packet creation,
 Shaped OQPSK and 16‑APSK / 32‑APSK modulation schemes. This release also introduces Python
 support for the RFmx Bluetooth Test Generation and RFmx WLAN Generation APIs, and adds
 hardware support for the PXIe‑5841 with 200 MHz bandwidth.

##### New
 Features

RFmx Waveform
 Creator

- 802.11bn waveform creation compliant with IEEE P802.11bn/D1.3 specification
 covering salient features like Distributed RUs including 60 MHz variant, Unequal Modulation, 2x LDPC
 Encoding, New MCS indices, Enhanced long range (ELR) and Interference
 Mitigation.
- Unframed Data Modulation for UHR packets.
- Frame duration-based generation for UHR.
- Non-HT Duplicate mode waveform creation for UHR packets.
- Shaped OQPSK waveform creation.
- 16-APSK , 32-APSK waveform creation.
- Python support for RFmx Bluetooth ® Test Generation and RFmx WLAN
 Generation APIs.

##### New
 Hardware Support

This version of RFmx Waveform
 Creator
 adds support for the following hardware:

- PXIe-5841 ( 200
 MHz ) bandwidth.

Related concepts:

- Default Modulation Mappings
- Selecting the Data Source

#### RFmx Waveform Creator 2026 Q1
 Changes

Learn about new features, behavior changes, and other updates in RFmx Waveform
 Creator 2026 Q1.

- Added support for 802.11bn waveform creation compliant with IEEE P802.11bn/D1.2
 specification covering salient features like Distributed RUs including 60MHz
 variant, Unequal Modulation, 2x LDPC Encoding, New MCS indices, Enhanced long
 range (ELR) and Interference Mitigation.
- Exposed the PDU CRC Initialization seed API for Bluetooth® HDT.
- Added support for NBIoT Downlink.

#### RFmx Waveform Creator 2025 Q4
 Changes

Learn about new features, behavior changes, and other updates in RFmx Waveform
 Creator 2025 Q4.

##### New Features

- Support for 802.11bn waveform creation compliant with IEEE P802.11bn/D1.0
 specification covering salient features like Distributed RUs including 60MHz
 variant, Unequal Modulation, 2x LDPC Encoding, New MCS indices, Enhanced long
 range (ELR) and Interference Mitigation.
- Exposed granular APIs to support multi-block user configurable packet creation
 for Bluetooth LE HDT packet Format 1.
- Support for Bluetooth LE HDT packet creation with Constant Tone Extension.
- Support for NR FRCs for UL NTN.

##### Behavior Changes

- The range of Payload Length (bytes) has been changed from
 [0–510] to [0–508] when the direction-finding mode is set to Angle of
 Arrival or Angle of Departure for HDT
 Format0 packets.

#### RFmx Waveform Creator 2025 Q3
 Changes

Learn about new features, behavior changes, and other updates in RFmx Waveform
 Creator 2025 Q3.

- Support for 802.11bn waveform creation compliant with IEEE P802.11bn/D0.3
 specification covering salient features like Distributed RUs including 60MHz
 variant, Unequal Modulation, 2x LDPC Encoding, New MCS indices and Enhanced long
 range (ELR).
- Support for Bluetooth® LE HDT [High Data Throughput] Format 0 and Format 1 packet
 creation compatible with Bluetooth SIG Core_HDT_PHY_FIPD_CR_r07.
- Exposed Physical Channel Address (PCA) and Zadoff-Chu index fields for Bluetooth® LE
 HDT Waveform creation.
- Support for Dirty Tx waveform creation for Bluetooth® LE HDT [High Data Throughput]
 Format 0 and Format 1 packets.
- Support for adding Frequency Drift impairment to Bluetooth® LE HDT [High Data
 Throughput] waveforms.
- Support for continuous mode waveform creation for Bluetooth® LE HDT [High Data
 Throughput] packets.

#### RFmx Waveform Creator 2025 Q2
 Changes

Learn about new features, behavior changes, and other updates in RFmx Waveform
 Creator 2025 Q2.

- Support for early access 802.11bn waveform creation compliant with IEEE
 P802.11bn/D0.1 specification covering salient features like Distributed RUs, Unequal
 Modulation, 2x LDPC Encoding and New MCS indices.
- Support for Bluetooth® LE HDT [High Data Throughput] Format 0 and Format 1 packet
 creation compatible with Bluetooth SIG Core_HDT_PHY_FIPD_CR_06.

#### RFmx Waveform Creator 2025 Q1
 Changes

Learn about new features, behavior changes, and other updates in RFmx Waveform
 Creator 2025 Q1.

- Support for Bluetooth® LE HDT [High Data Throughput] Format 0 and Format 1 packet
 creation compatible with Bluetooth SIG Core_HDT_PHY_FIPD_CR_04.
- Support for NTN FRCs under A.1, A.2, A.3A, NTN A.3 and NTN A.5 FRC tables of 3GPP
 38.181 V18.3.0

#### RFmx Waveform Creator 2024 Q4 Changes

Learn about new features, behavior changes, and other updates in RFmx Waveform
 Creator 2024 Q4.

- Added FR1 A.3A , FR2 A.3A , FR1 A.3B, FR2 A.3B, NTN – FR2 A.5, NTN – FR2 A.6, FR1 A.9, FR1
 A.12 and updated FR1 A.3, FR2 A.3 in NR as per 3GPP Rel 18 spec.
- 802.11be standard complies with IEEE P802.11be/D7.0 specification.
- Support for Bluetooth® LE HDT [High Data Throughput] Format 0 packet creation
 compatible with Bluetooth SIG Core_HDT_PHY_FIPD_CR_r03 API.
- [API Only] Support for Bluetooth® LE HDT Format 1 packet creation compatible with Bluetooth
 SIG Core_HDT_PHY_FIPD_CR_r03.
- [API Only] Bluetooth® LE Channel Sounding standard complies with Core Specification version
 6.0 and Test Suite RFPHY.TS.p22.

#### RFmx Waveform Creator 2024 Q2 Changes

Learn about new features, behavior changes, and other updates in RFmx Waveform
 Creator 2024 Q2.

- 802.11be standard complies with IEEE P802.11be/D6.0 specification
- Support for FRCs for 3MHz
- Support FRC tables A.10 and A.11 for UL FR1 and A.12 for UL FR2-1
- Support for PXIe-5860

#### RFmx Waveform Creator 2024 Q2
 Changes

Learn about new features, behavior changes, and other updates in RFmx Waveform
 Creator 2024 Q2.

- Support for Bluetooth Channel Sounding test packet creation
- Support for BT=2.0 for Bluetooth Channel Sounding packets
- Support for LE-based hyperlength packet creation
- Support for 802.11be standard to be compliant with IEEE P802.11be/D5.0.1
 specification
- Change in default oversampling ratio for WLAN 11b waveforms

#### RFmx Waveform Creator 2024 Q1
 Changes

Learn about new features, behavior changes, and other updates in RFmx Waveform
 Creator 2024 Q1.

- Support for adding Time Delay and Clock Drift impairments for Channel Sounding
 Packets
- Updated 802.11be standard support to comply with IEEE P802.11be/D5.0
 specification
- Support for pulse generation with Pulse Repetition Interval (PRI) patterns
- Support for specifying Pulse timing parameters as 10/90/50 definition
- Support for specifying timing parameters and amplitude imperfections in
 Watts

#### RFmx Waveform Creator 2023 Q4
 Changes

Learn about new features, behavior changes, and other updates in RFmx Waveform
 Creator 2023 Q4.

- Support for Bluetooth® Channel Sounding (CS)
  - Creation of CS SYNC Packets
  - Creation of CS SYNC Packets with Sounding Sequence
  - Creation of CS Tone
  - Creation of Extended Packets
- Updated 802.11be standard support to comply with IEEE P802.11be/D4.0
 specification

#### RFmx Waveform Creator 2023 Q3
 Changes

Learn about new features, behavior changes, and other updates in RFmx Waveform
 Creator 2023 Q3.

- Support for Pulse library
  - Single pulse generation
  - Pulse Types: Trapezoidal, Raised Cosine, Custom Profile, Custom IQ
  - Modulation: BPSK, QPSK, LFM, AM/FM step, Barker code
  - Pulse Parameters
    - Rise Time, Fall Time, Pulse Width
    - Droop, Overshoot, Ripple
- Updated 802.11be standard support to comply with IEEE P802.11be/D3.2
 specification

<!--NI_TOPIC bundle=rfmx-waveform-creator path=nr-basic-signal-settings.html language=enus -->
## TOPIC 00095: NR Basic Signal Settings

- bundle_id: `rfmx-waveform-creator`
- source_path: `nr-basic-signal-settings.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/nr-basic-signal-settings.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: NR contains key attributes which encompass the most important aspects of an NR waveform, and should be set according to specification before starting the basic generation/analysis. The basic signal settings are as follows. Frequency Range (FR1/FR2) The NR standard contains different selectable optio

### NR Basic Signal Settings

NR contains key attributes which encompass the most important aspects of an NR waveform,
 and should be set according to specification before starting the basic
 generation/analysis. The basic signal settings are as follows.

Frequency Range (FR1/FR2)

The NR standard contains different selectable options based on the operating frequency.
 Select FR1 for sub-6 GHz and FR2 for mmWave carrier frequencies.

- Range 1: 450 MHz – 6000 MHz
- Range 2: 24250 MHz – 52600 MHz

Link Direction (UL/DL)

The link direction parameter sets the transmission direction to either Uplink or
 Downlink.

Bandwidth

NR signals have multiple options for carrier bandwidth along with the concept of
 bandwidth parts for mixed numerologies on the same carrier frequency. Channel bandwidth
 determines the overall bandwidth, comprised of bandwidth parts. Bandwidth parts are a
 subset of contiguous physical resource blocks within a carrier with a given
 numerology.

Valid values for channel bandwidth range from 5 MHz to 400 MHz. Options will populate
 based on the frequency range.

Subcarrier Spacing

To scale with the variable signal bandwidths, NR supports different selectable subcarrier
 spacing options.

Based on the selected channel bandwidth, this drop-down list will only show supported
 values. In general, valid values are 15 kHz, 30 kHz, 60 kHz, and 120 kHz.

Modulation Type

Supported values are QPSK, QAM16, QAM64, QAM256, and QAM1024 for CP-OFDM modulation and
 PI/2 BPSK, QPSK, QAM16, QAM64, QAM256, and QAM1024 if the Transform Precoding is
 enabled.

Transform Precoding (CP-OFDM/DFT-s-OFDM)

NR supports both CP-OFDM and DFTs-OFDM signal types. DFTs-OFDM waveforms are accomplished
 by adding transform precoding in front of the CP-OFDM mapping. Setting
 Transform Precoding to enabled will result in DFTs-OFDM
 waveforms instead of CP-OFDM waveforms.

Slot Allocation

NR leverages flexible slot capabilities between Uplink and Downlink to allow for
 switching on a per-slot basis. You can define the indices of the allocated slots using
 this parameter. The format is defined in the section Range Format
 Specifiers.

Valid values are between 0 and (Max. Slots in Frame - 1). The maximum number of slots in
 the current frame is displayed in the Max. Slots in Frame field. It depends on the
 selected Subcarrier Spacing.

To configure an FDD signal, allocate all slots within the frame. Otherwise, the signal
 will use a TDD format.

RB Allocation

Defines the range of the allocated Resource Blocks for PUSCH. The format is defined in
 the section Range Format Specifiers.

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=nr-filter-type.html language=enus -->
## TOPIC 00096: NR Filter Type

- bundle_id: `rfmx-waveform-creator`
- source_path: `nr-filter-type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/nr-filter-type.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Waveform Creator currently supports the following filter type. NR (Improved ACP) Preferred for adjacent channel power (ACP) measurements.

### NR Filter Type

RFmx Waveform Creator currently supports the following filter type.

- NR (Improved ACP) Preferred for adjacent channel power (ACP)
 measurements.

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=nr-multi-carrier.html language=enus -->
## TOPIC 00097: NR Multi-Carrier

- bundle_id: `rfmx-waveform-creator`
- source_path: `nr-multi-carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/nr-multi-carrier.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This window allows you to configure multiple NR carrier parameters. Click Edit to edit the carrier parameters. Parameters Number of Carrier Sets: Specifies the number of carrier sets, which is the number of waveforms to be generated. Carrier Set Carrier Set Number: Specifies the index of carrier set

### NR Multi-Carrier

This window allows you to configure multiple NR carrier parameters. Click
 Edit to edit the carrier parameters.

[IMAGE alt='image' src='GUID-F0B051DC-7764-488E-A531-ADC64F8975F5-a5.png']

Parameters

Number of Carrier Sets: Specifies the number of carrier sets,
 which is the number of waveforms to be generated.

Carrier Set

Carrier Set Number: Specifies the index of carrier set. The
 default and minimum value is zero. The maximum value depends on the number of
 carrier sets.

Oversampling Factor: Sets the oversampling factor. This
 control enables you to increase the default sample rate. The default value is 1. To
 change the oversampling factor manually, unselect the Auto
 checkbox.

Auto: When this checkbox is unselected,
 Oversampling Factor is disabled and set to 1.

Phase Continuous: When this checkbox is selected, it coerces
 the carrier frequency offset to the closest cyclic frequency offset value such that
 the aggregated waveform is phase continuous. This parameter updates the
 CC Offset control upon clicking
 OK. Frequency offset will be recalculated each time any
 carrier is added, modified, or removed. Phase Continuous
 checkbox is selected by default.

Phase Compensation Enabled: Specifies whether phase
 compensation is enabled. When this checkbox is not selected, no phase compensation
 is applied to the signal. When this checkbox is selected, phase compensation is
 applied to the signal using the value of Phase Compensation
 Frequency.

Number of Subblocks: Specifies the number of subblocks in the
 selected carrier set.

Carrier PSD Equalization: When this checkbox is unselected,
 the component carrier signals are scaled such that they have equal average (RMS)
 power. When this checkbox is selected, the component carrier signals are scaled such
 that they have equal power spectral density (PSD). In this mode, the relative
 channel power is maintained between component carriers. Hence, if the PUSCH channel
 has a power boosting of 3 dB on one carrier, it will have 3 dB higher power spectral
 density compared to a PUSCH channel with 0 dB power boosting on the other component
 carrier. Carrier PSD Equalization checkbox is unselected by
 default.

Subblock

Subblock Number: Specifies the index of the subblock. The
 default and minimum value is zero. The maximum value depends on the number of
 subblocks.

Subblock Offset: Specifies the frequency offset of the
 specified subblock from the center frequency.

Phase Compensation Frequency: Specifies the frequency used for
 phase compensation of the signal when you select the Phase Compensation
 Enabled checkbox. The frequency setting refers to the center
 frequency of the subblock and is applied to all carriers respectively.

Spacing Type - Specifies the spacing between the two adjacent
 component carriers within a subblock.

- Nominal - Calculates the frequency spacing between
 component carriers as defined in section 5.4.1A of 3GPP TS
 38.101-1/2 specification and section 5.4.1.2 of 3GPP TS
 38.104 specification, and sets the CC
 offset .
- User - The component carrier offset that you configure in
 the CC Offset is used.

Reference CC Index - Specifies the component carrier index of
 the reference component carrier. The center of the reference component carrier is
 placed at the subblock offset. The value of Reference CC
 Index and Spacing Type is used to calculate
 the CC Offset.

Note

Number of CCs - Specifies the number of component carriers of
 the selected subblocks. When you increase the value of the number of carrier sets,
 new carrier sets are added. These newly added carrier sets are preconfigured with
 the configuration of the last carrier set. When you decrease the value of the number
 of carrier sets, the carrier sets are deleted.

Note

Number of Subblocks

Number of CCs

Channel Raster - Specifies the subblock channel raster which
 is used for computing nominal spacing between aggregated carriers as specified in
 section 5.4A.1 of 3GPP 38.101-1/2 specification and section
 5.4.1.2 of 3GPP TS 38.104 specification.

Supported values for frequency Range 1 are 15 kHz and 100 kHz.

Supported value for frequency Range 2 is 60 kHz.

Component Carrier

CC Index: Specifies the index component carrier. The default
 and minimum value are zero. The maximum value depends on the number of CCs.

Carrier Definition Number: Specifies the carrier as defined by
 the Carrier Definition Number in the Modulation tab.

CC Offset: Specifies the offset of each carrier to subblock
 offset.

Gain, Phase, Random Phase, Delay, and Random Delay: These
 parameters are set on each component carrier.

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=nr-overview.html language=enus -->
## TOPIC 00098: NR

- bundle_id: `rfmx-waveform-creator`
- source_path: `nr-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/nr-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creates a waveform that simulates a 3GPP NR carrier. The modulation scheme for 3GPP NR is defined in the 3GPP TS 38.211 and the 3GPP TS 38.212 specifications. This document assumes that you know how to package and download files to an instrument. For more information about packaging and downloading

### NR

Creates a waveform that simulates a 3GPP NR carrier.

The modulation scheme for 3GPP NR is defined in the *3GPP TS 38.211* and the
 *3GPP TS 38.212* specifications.

Note

Generating and Saving the Waveform
 File

Parent topic:

RFmx Waveform Creator Modulation Schemes

Related information:

- RFmx NR .NET Reference
- RFmx NR C API Reference

<!--NI_TOPIC bundle=rfmx-waveform-creator path=pdcch-configuration.html language=enus -->
## TOPIC 00099: PDCCH Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `pdcch-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/pdcch-configuration.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains the following configuration parameters specific to the PDCCH portion of the downlink signal. If the Number of Tx Antennas is greater than 1, the PDCCH is configured and applied on all the antenna streams. Slot Allocation: Configures the slots that will contain a PDCCH for this

### PDCCH Configuration

This section contains the following configuration parameters specific to the PDCCH
 portion of the downlink signal.

If the Number of Tx Antennas is greater than 1, the PDCCH is
 configured and applied on all the antenna streams.

Slot Allocation: Configures the slots that will contain a PDCCH
 for this configuration. The format is defined in the Range Format Specifiers section.

CCE Offset: Sets the CCE offset within the CORESET for PDCCH.
 Valid ranges depend on the RB Allocation in the CORESET Configuration and the CCE Aggregation
 Level.

CCE Aggregation Level: Sets the CCE aggregation level of the
 PDCCH. Valid values are 1, 2, 4, 8, and 16.

RNTI: Sets the RNTI number. Valid values are 0 to 65535,
 inclusive.

Search Space Type: If you set this value to UE
 Specific, PDCCH is mapped according to the UE specific search space
 type. If you set this value to Common, PDCCH is mapped according
 to the common search space type.

Data Source: Specifies the configuration of the payload data in
 the PUSCH channel. Refer to Selecting the Data Source topic for more information on data
 source.

PDCCH Power: Specifies the factor by which the PDCCH REs are
 scaled. This value is expressed in dB.

PDCCH DMRS Power: Specifies the factor by which the PDCCH DMRS REs
 are scaled. This value is expressed in dB.

Channel Coding: Specifies whether channel coding is enabled.

Payload size: Specifies the total number of information bits in
 DCI format. Valid values are from 12 to 140. If the number of information bits in a DCI
 format is less than 12 bits, zeros shall be appended to the DCI format by user until the
 payload size equals 12.

Parent topic:

NR

Related concepts:

- Range Format Specifiers
- CORESET Configuration

<!--NI_TOPIC bundle=rfmx-waveform-creator path=pdsch-configuration.html language=enus -->
## TOPIC 00100: PDSCH Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `pdsch-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/pdsch-configuration.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: PDSCH configuration has three sections, PDSCH, PDSCH DM-RS, and PDSCH PT-RS. PDSCH The following configuration parameters specific to the PDSCH portion of the Downlink Signal. Symbol Allocation: Specifies the symbol indices which are allocated to PDSCH in the resource map. The format is defined in t

### PDSCH Configuration

PDSCH configuration has three sections, PDSCH, PDSCH DM-RS, and PDSCH PT-RS.

PDSCH

The following configuration parameters specific to the PDSCH portion of the Downlink
 Signal.

Symbol Allocation: Specifies the symbol indices which are
 allocated to PDSCH in the resource map. The format is defined in the Range Format Specifiers section. Valid values for first and last symbol
 are 0 to 13, while the last symbol must be greater than or equal to the first
 symbol. The default is 0:13.

Slot Allocation: Specifies the indices of the allocated slots.
 The format is defined in the Range Format Specifiers section.

Valid values are between 0 and (Max. Slots in Frame - 1). The maximum number of slots
 in the current frame is displayed in the Max. Slots in Frame field. It depends on
 the selected Subcarrier Spacing.

RB Allocation: Specifies the range of the allocated Resource
 Blocks for PDSCH. The format is defined in the Range Format
 Specifiers section.

For more information about RB Allocation, refer to the following figure with
 configuration - Allocated slots 2:11, RB Allocation 1:13.

[IMAGE alt='image' src='GUID-CD44E5A2-2778-4CE7-A85A-384C18DA099E-a5.gif']

Channel Coding: Specifies whether channel coding is enabled.
 If enabled, modulation type is calculated from MCS Table and
 MCS Index parameters, otherwise the user specified value
 is honoured.

MCS Table: Specifies the modulation and coding scheme table to
 be used for channel coding.

| MCS Table Value | 3GPP 38.214 Reference |
| --- | --- |
| 256QAM | Table 5.1.3.1-2: MCS index table 2 for PDSCH |
| 64QAM | Table 5.1.3.1-1: MCS index table 1 for PDSCH |
| 64QAM LowSE | Table 5.1.3.1-3: MCS index table 3 for PDSCH |
| 1024QAM | Table 5.1.3.1-4: MCS index table 4 for PDSCH |

LBRM Enabled: Specifies whether limited buffer rate matching
 is enabled.

Modulation Type/Modulation Type CW0: Specifies the modulation
 type. When channel coding is enabled, this parameter indicates the modulation type
 that is used based on the values of MCS Table and
 MCS Index.

MCS Index/MCS Index CW0: Specifies the MCS index from the
 selected table.

Redundancy Version/Redundancy Version CW0: Specifies the
 redundancy version to use for channel coding. Valid values are from 0 to 3.

The following parameters are available when the number of antennas is greater than
 4.

Modulation Type CW1: Specifies the modulation type for
 code word 1. When channel coding is enabled, this indicates the modulation type
 that is being used based on the values of MCS Table and
 MCS Index.

MCS Index CW1: Specifies the MCS index from the selected
 table for code word 1.

Redundancy Version CW1: Specifies the redundancy version
 to use for channel coding for code word 1. Valid values are from 0 to 3.

Data Scrambling ID Mode: If you set this parameter to
 User Defined, the scrambling sequence generator will be
 initialized with the value specified in the Data Scrambling
 Id parameter.

If you set this parameter to Cell ID, the scrambling sequence
 generator will be initialized with the value specified in the Cell
 ID parameter in the Carrier Definition section.

Data Scrambling Id: Initializes the scrambling sequence
 generator. Valid values are 0 to 1023. This value is used only if you set the
 Data Scrambling ID Mode to User
 Defined.

PDSCH Power: Specifies the factor by which the PDSCH REs are
 scaled. This value is expressed in dB.

Max. Slots in Frame: Specifies the maximum number of slots
 available for a PDSCH configuration in the current bandwidth part configuration.

PDSCH DMRS

The following configuration parameters specific to the DMRS portion of the Downlink
 Signal.

DMRS Power Mode: Specifies whether the configured
 DMRS Power is honored or calculated from CDM Groups for
 reference signal generation.

DMRS Power: This parameter is used to set the DMRS power in dB
 relative to the PDSCH data power. The recommended DMRS Power depends on the chosen
 Number of DM-RS CDM Groups without data:

| Number of CDM Groups | DMRS Config Type 1 | DMRS Config Type 2 |
| --- | --- | --- |
| 1 | 0 dB | 0 dB |
| 2 | 3 dB | 3 dB |
| 3 | - | 4.77 dB |

DMRS Config Type: Determines the way the DMRS is mapped to
 physical resources. Either Type 1 or Type
 2 can be selected.

DMRS Duration: Specifies the DMRS symbol length. Valid values
 are Single Symbol and Double
 Symbol.

DMRS Type A Position: Configures the position of the first
 DMRS symbol if Type A DMRS mapping is selected. Valid values are 2 and 3. This value
 is ignored in case of Type B DMRS mapping.

DMRS Additional Positions: Specifies the positions of
 additional DMRS symbols. Valid values are 0, 1, 2, and 3. If 0 is selected, no
 additional DMRS symbols are added.

PDSCH Mapping Type: Allows you to choose between
 Type A and Type B mapping.

- For Type A, the position of the first DMRS symbol can be set via the DMRS Type A
 Position field.
- For Type B, the position of the first DMRS symbol is the lowest symbol index
 specified in the Active Symbol Map.

Number of CDM Groups: Specifies the number of DM-RS CDM groups
 without data parameter. Valid values are 1,2,3 – depending on the number of transmit
 antenna ports and DMRS Config Type.

DMRS Antenna Ports: Specifies the antenna ports used for DMRS
 transmission. The antenna ports are given as a comma separated list. The number of
 specified DMRS antenna is equal to the Number of Layers.

DMRS Release Version: Specifies the 3GPP release version for
 generating the DMRS sequence. Allows you to choose between 3GPP Release
 15 and 3GPP Release 16.

- For 3GPP Release 16 , the DMRS sequence is generated as
 per section 7.4.1.1.1 of 3GPP TS 38.211 g00 specification.
- For 3GPP Release 15 , the DMRS sequence is generated as
 per section 7.4.1.1.1 of 3GPP TS 38.211 f80 specification.

DMRS Scrambling ID Mode: If you set this parameter to
 User Defined, the DMRS scrambling sequence generator will
 be initialized with the value specified in the DMRS Scrambling ID field.

If you set this parameter to Cell ID, the DMRS scrambling
 sequence generator will be initialized with the value specified in the
 Cell ID field in the Carrier Definition section.

DMRS Scrambling Id: Initializes the DMRS scrambling sequence
 generator. Valid values range from 0 to 65535. This value is only used if the
 DMRS Scrambling ID Mode is set to User
 Defined.

nSCID: The DMRS scrambling sequence generator will be
 initialized with a value that is calculated from the DMRS Scrambling ID and the
 nSCID. Valid values are 0 and 1. This value is only used if the DMRS
 Scrambling ID Mode is set to User
 Defined.

PDSCH PT-RS

The following configuration parameters specific to the phase tracking reference
 signal.

PTRS Enabled: Specifies whether to enable adding a PTRS to the
 waveform.

PTRS Power Mode: Specifies whether the PTRS power is set
 according to the 3GPP standard or as per user configuration. The default value is
 Standard.

| Standard |
| --- |
| User Defined |
| Sets the PDSCH PTRS power scaling, βPT-RS, according to the Table 4.1-2 of 3GPP TS 38.214 specification. The epre-Ratio is configured using PTRS EPRE Ratio parameter. |
| Sets the PUSCH PTRS power scaling, βPT-RS, to the value specified in the PTRS Power parameter. |

PTRS EPRE Ratio: Specifies the epre-ratio configuration
 defined in the Table 4.1-2 of 3GPP TS 38.214 specification. This
 parameter selects the power scaling of the PTRS REs relative to PDSCH data REs.
 Allowed values are 0 (results in scaling depending on number of Layers) and 1 (no
 scaling).

PTRS Power: Specifies the power of the PTRS.

PTRS RE Offset: Specifies the resource element offset. This
 parameter along with the PTRS Frequency Density is used to calculate the subcarrier
 indices to which the PTRS shall be mapped. Valid values are 0, 1, 2, and 3.

PTRS Frequency Density: This parameter along with the PTRS RE
 Offset is used to calculate the subcarrier indices to which the PTRS shall be
 mapped. This parameter is used for CP-OFDM. This parameter is not used if transform
 precoding is enabled. Valid values are 2 and 4.

PTRS Time Density: This parameter is used to calculate the set
 of time indices defined relative to the start of the PDSCH allocation. Valid values
 are 1, 2, 4.

PTRS Antenna Port: Specifies the antenna ports used for PTRS
 transmission. The antenna port should be a subset of the DMRS antenna ports.

Parent topic:

NR

Related concepts:

- Range Format Specifiers

<!--NI_TOPIC bundle=rfmx-waveform-creator path=physical-layer-channels.html language=enus -->
## TOPIC 00101: Physical Layer Channels

- bundle_id: `rfmx-waveform-creator`
- source_path: `physical-layer-channels.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/physical-layer-channels.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The long term evolution (LTE) downlink (DL) and uplink (UL) are composed of physical channels and physical signals. Physical channels carry information from higher layers and are used to carry user data, as well as user control, and information. Physical signals do not carry information from higher

### Physical Layer Channels

The long term evolution (LTE) downlink (DL) and uplink (UL) are composed of physical
 channels and physical signals. Physical channels carry information from higher layers
 and are used to carry user data, as well as user control, and information. Physical
 signals do not carry information from higher layers and are used for cell search and
 channel estimation purposes only.

The main DL physical channels are the physical broadcast channel (PBCH), physical
 downlink control channel (PDCCH), physical hybrid ARQ indicator channel (PHICH),
 physical control format indicator channel (PCFICH) and physical downlink shared channel
 (PDSCH). The main DL physical signals are the reference signal and the primary and
 secondary synchronization signals.

The UL physical channels are the physical uplink control channel (PUCCH), the physical
 uplink shared channel (PUSCH), the narrowband physical uplink shared channel (NPUSCH),
 and the physical uplink random access channel (PRACH). The UL physical signals are the
 sounding reference signal (SRS) and the demodulation reference signal for PUSCH and
 PUCCH.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=physical-random-access-channel.html language=enus -->
## TOPIC 00102: Physical Random Access Channel (PRACH)

- bundle_id: `rfmx-waveform-creator`
- source_path: `physical-random-access-channel.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/physical-random-access-channel.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The mobile can start the random access transmission at the beginning of a number of well-defined time intervals, denoted access slots. There are 15 access slots per two frames which are spaced at 5120 chips apart. The structure of the random access transmission is shown in the following figure. The

### Physical Random Access Channel (PRACH)

The mobile can start the random access transmission at the beginning of a number of
 well-defined time intervals, denoted access slots. There are 15 access slots per two
 frames which are spaced at 5120 chips apart. The structure of the random access
 transmission is shown in the following figure. The structure consists of one or more
 preambles followed by a message part that can be either 10 or 20 ms in duration. The
 minimum time between preambles and from the preamble to message part is 15360 chips. The
 PRACH preamble consists of a complex valued code that is obtained from a preamble
 scrambling code and a preamble signature.

[IMAGE alt='image' src='GUID-B447851F-91F1-44FF-9F55-A6FA1D3EDC1A-a5.gif']

PRACH Message Part

The following figure shows the principle of generating the PRACH message part. The PRACH
 message part consists of a control and a data part which are spread to the chip rate
 using spreading codes c<sub>c</sub> and c<sub>d</sub> respectively. The gains are
 adjusted by gain factors, β<sub>c</sub> and β<sub>d</sub>. The data and the control
 parts are summed as a complex pair and scrambled by the complex scrambling code
 S<sub>r-msg,n</sub>.

[IMAGE alt='image' src='GUID-96436DF5-FFA2-445F-B4DF-44A0ED596E8A-a5.gif']

Channel Codes: The channelization code for the control part is
 c<sub>c</sub> = C<sub>256,m</sub> where m = 16s+15, and s is the
 preamble signature. The channelization code for the data part is c<sub>d</sub> =
 C<sub>SF,m</sub> where SF is the spreading factor (32 to 256) and m = SF*s/16 .
 These are calculated automatically.

PRACH Message Structure

The structure of the PRACH message is shown in the following figure. The parameter
 k refers to the slot number that effectively determines the
 symbol rate.

[IMAGE alt='image' src='GUID-A259F345-1F3A-44F9-AF7F-A0FD7CE01EE5-a5.gif']

[IMAGE alt='image' src='GUID-49DB70CD-0E87-4F0B-B3C1-152BCC0F7E49-a5.gif']

The control part of the message consists of pilot bits(as shown in the following table)
 and two TFCI bits. If the message length is 20 ms, the TFCI bits are repeated for the
 second 10 ms frame. The TFCI bits are calculated from a 10-bit TFCI index.

[IMAGE alt='image' src='GUID-28119E4B-F24C-4C0F-BEA4-812ADC5FF84A-a5.gif']

Parameters

You can set the following parameters for the PRACH:

Scrambling Code: Specifies the code number used to set up the
 scrambling generator. Scrambling code is used along with the preamble signature to
 define the preamble bits. Valid range is 0 to 8191.

Number of Preambles: Specifies the number of preambles transmitted
 before the message part of the preamble. Valid range is 1 to 10.

Preamble Signature: Sets the preamble signature. Valid range is 0
 to 15.

Preamble Power: Sets the relative power of the preamble. Valid
 range is 0 to –60 dB.

Symbol Rate: Specifies the symbol rate of the message. Valid
 values are 15 ksps, 30 ksps, 60 ksps, and 120 ksps.

Data Power: Sets the relative power of the data part of the
 message. Valid range is 0 to –60 dB.

Control Power: Sets the relative power of the control part of the
 message. Valid range is 0 to –60 dB.

Message Length: Sets the message length in frames. Valid values
 are 1 and 2. One frame is 10 ms.

TFCI Index: Sets the TFCI index. Valid range is 0 to 1023. The TFI
 index is used to determine the TFCI bits.

Data Source: Specifies the data source. Refer to Selecting the
 Data Source topic for more information on data source.

Parent topic:

WCDMA (3GPP FDD Release 8)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=pulse-envelope-types.html language=enus -->
## TOPIC 00103: Pulse Envelope Types

- bundle_id: `rfmx-waveform-creator`
- source_path: `pulse-envelope-types.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/pulse-envelope-types.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The types of pulse envelope are described in detail in this section. Trapezoidal Trapezoidal pulse envelope is defined by rise time, fall time, width and amplitude reference level. The following image illustrates a trapezoidal pulse envelope with linear rise time and fall time for 0/100/100 and 10/5

### Pulse Envelope Types

The types of pulse envelope are described in detail in this section.

Trapezoidal

Trapezoidal pulse envelope is defined by rise time, fall time, width and amplitude
 reference level. The following image illustrates a trapezoidal pulse envelope with
 linear rise time and fall time for 0/100/100 and 10/50/90 Volts and Watts amplitude
 reference level.

Figure 2.

[IMAGE alt='image' src='GUID-AFDFCFB8-8E67-4DD7-97EE-E144536F283C-a5.png']

Figure 3.

[IMAGE alt='image' src='GUID-03D53E3D-B34D-4CE5-A848-7C29559D55F3-a5.png']

Raised Cosine

Raised cosine pulse offers good frequency domain response.

Raised cosine pulse envelope is defined by rise time, fall time, width, and amplitude
 reference level. Raised cosine pulse envelope is mathematically described using the
 following equation.

[IMAGE alt='image' src='GUID-90FFC1BA-8688-48C7-8C82-D1B9C715E0A1-a5.png']

where,

T ≥ (Rise Time + Fall Time + Width) for
 0/100/100 amplitude reference level

T ≥ (0.625 x (Rise Time
 + Fall Time) + Width)

T ≥ (1.119×(Rise Time+Fall Time)+ Width)
 for 10/50/90 Watts amplitude reference level

The following images illustrate a raised cosine pulse envelope with sinusoidal rise time
 and fall time for 0/100/100 and 10/50/90 amplitude reference levels, respectively.

Figure 4.

[IMAGE alt='image' src='GUID-5C120E1A-BB2E-4D74-A379-DD36CBE35380-a5.png']

Figure 5.

[IMAGE alt='image' src='GUID-D27DCF48-A310-45C0-93FE-573D409444F7-a5.png']

Custom Profile

Custom Profile is described by user-defined pulse profile data. You can provide amplitude
 levels for different points of pulse in a .txt file. The largest amplitude number in the
 .txt file is used to reference all the other amplitude data points. The Pulse RFmx
 Waveform Creator application normalizes the profile amplitude data so that the maximum
 amplitude is 1.

Modulation can be applied on pulse width. Pulse width is measured from the first point to
 the last point of the custom profile data. Pulse width can also be calculated using:
 total number of data points/sampling rate.

You can also import custom profile data using the File Name UI.

File Name: Specifies a file path which is required to create
 custom profile envelope.

The Click to select a file command button opens a dialog that
 allows you to import a .txt file containing the amplitude in Volts.

Custom IQ

Custom IQ is described by the user-defined pulse I and Q data. You can provide I and Q
 values at different points of pulse in a .txt file. The Pulse RFmx Waveform Creator
 application generates the same signal based on the IQ data in the .txt file.

You can also import custom IQ data by using the File Name UI.

File Name: Specifies a file path which is required to create
 custom IQ envelope.

The Click to select a file command button opens a dialog that
 allows you to import a .txt file containing IQ pairs.

Parent topic:

Creating a Pulse Waveform

<!--NI_TOPIC bundle=rfmx-waveform-creator path=pulse-impairments.html language=enus -->
## TOPIC 00104: Pulse Impairments

- bundle_id: `rfmx-waveform-creator`
- source_path: `pulse-impairments.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/pulse-impairments.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Droop, overshoot and ripple are defined to introduce power/amplitude deviation in the pulse. This section contains a detailed description of the pulse impairment parameters. Pulse Impairments Unit This property allows you to specify the pulse impairments unit for parameters such as droop, overshoot

### Pulse Impairments

Droop, overshoot and ripple are defined to introduce power/amplitude deviation in the pulse.
 This section contains a detailed description of the pulse impairment parameters.

Pulse Impairments Unit

This property allows you to specify the pulse impairments unit for parameters such as
 droop, overshoot and ripple either in %Volts or %Watts.

Droop

The following parameter is used to introduce droop on pulse signal.

Droop: Droop is defined as the amplitude change from the beginning to the end of the pulse on time (width (100%-100%)). A positive value decreases the amplitude. This parameter is represented in %V.

Droop is applicable only for trapezoidal pulse envelope type. Valid values are from 0 to 50.

The following image shows the droop behaviour on the trapezoidal pulse envelope.

[IMAGE alt='image' src='GUID-5653881E-E7FF-42DB-810D-A2E602DF47D3-a5.png']

Overshoot

The following parameter is used to introduce overshoot on pulse signal.

Overshoot: Overshoot is defined as the height of the local maximum after a rising edge, divided by the pulse amplitude during pulse on time Width (100%-100%). This parameter is represented in %V.

Overshoot is applicable only for the trapezoidal pulse envelope type. Valid values are from 0 to 50.

[IMAGE alt='image' src='GUID-72A0D1CA-A718-4DE3-A14B-19ADD92E249E-a5.png']

Ripple

The following parameters are used to introduce ripple on pulse signal

Ripple simulates the unwanted ringing effect, i.e., that the signal oscillates around the power level. This oscillation is defined with a ripple level and ripple frequency.

Ripple is applied on rise time (0-100%), fall time (100-0%), and width (100%-100%). Ripple Level and Ripple Frequency are applicable only for the trapezoidal pulse envelope type and defined as follows:

Ripple Level: Ripple level is defined as the difference between the maximum and minimum deviation from the pulse top reference. Ripple level is represented in %V.

Valid values are from 0 to 50.

Ripple Frequency: Ripple frequency (1/oscillation period) is defined at which ripple oscillates around power level. Ripple frequency is represented in Hz.

Valid values are from 0 to 300 MHz.

The following image shows the relationship between ripple level, ripple frequency, and time.

[IMAGE alt='image' src='GUID-2721E484-ECD6-4B61-A090-7F30C832D5F6-a5.png']

Parent topic:

Creating a Pulse Waveform

<!--NI_TOPIC bundle=rfmx-waveform-creator path=pulse-modulation-types.html language=enus -->
## TOPIC 00105: Pulse Modulation Types

- bundle_id: `rfmx-waveform-creator`
- source_path: `pulse-modulation-types.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/pulse-modulation-types.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Pulse modulation helps in achieving pulse compression, which facilitates high average transmit power and low peak power by making the pulse duration longer. In pulse0 section, Modulation Type UI allows you to specify modulation with pulse envelope type. Selecting the modulation type is supported for

### Pulse Modulation Types

Pulse modulation helps in achieving pulse compression, which facilitates high average transmit power and low peak power by making the pulse duration longer.

In pulse0 section, Modulation Type UI allows you to specify modulation with pulse envelope type. Selecting the modulation type is supported for all pulse envelope type except custom IQ.

The Pulse RFmx Waveform Creator supports the following modulation types.

| None | Generation uses this option to avoid applying modulation. |
| --- | --- |
| BPSK | Generation uses this option to apply BPSK modulation with the specified step size. |
| QPSK | Generation uses this option to apply QPSK modulation with the specified step size. |
| FM Chirp | Generation uses this option to apply FM Chirp modulation with the specified chirp deviation and chirp type. |
| FM Step | Generation uses this option to apply FM Step modulation with the user-specified step size and frequency, both of which should be entered in a table format. |
| AM Step | Generation uses this option to apply AM Step modulation with the user-specified step size and amplitude, both of which should be entered in a table format. |
| Barker | Generation uses this option to apply Barker modulation with the specified barker code length. |

All the modulation types are described in more detail in this section.

None

The 'None' modulation type does not apply any modulation on the pulse signal.

BPSK

A phase shift of 0 and 180 degrees is introduced after every specified step size during the
 pulse ON state (Width (100%-100%)).

Step Size: The step size is defined as time duration of the phase shift for each ON/OFF state. Valid values are from 0 to 1 second.

The following image shows BPSK phase changes from 0 to 180 and vice versa.

[IMAGE alt='image' src='GUID-FDFE1906-5A77-40E1-8F3E-C154502610C4-a5.png']

QPSK

Phase shift of 90 degrees is introduced after every ‘Step Size’ duration during the pulse ON state (Width (100%-100%)).

Step Size: The step size is defined as time duration of the phase shift for each I/Q state. Valid values are from 0 to 1 second.

Valid values are from 0 to 50.

The QPSK sequence supported by the Pulse RFmx Waveform Creator application is Gray code ‘00’, ‘01’, ‘11’, and ‘10’.

The following image shows QPSK phase changes.

[IMAGE alt='image' src='GUID-BA72D4DF-02D8-46BC-A2E9-80D289675E0E-a5.png']

FM Chirp

Frequency remains constant during rise time (0-100%) and fall time (100%-0) and modulated linearly over the pulse ON time (Width (100%-100%)) based on user-defined chirp deviation and chirp type parameter.

Chirp Deviation: Specifies the chirp deviation for FM Chirp modulation. The chirp deviation is defined as the maximum change in the modulation frequency that occurs over the time period of the pulse (Width (100%-100%)). Chirp deviation is represented in Hz. Valid values are from 0 to 5 GHz.

Chirp Type:Specifies the direction of chirp for FM chirp modulation.

| Up | Specifies ascending direction of chirp and indicates an increase in frequency during FM chirp. |
| --- | --- |
| Down | Specifies descending direction of chirp and indicates a decrease in frequency during FM chirp. |

The following image shows the UI selection for FM chirp modulation.

[IMAGE alt='image' src='GUID-B1E57442-46FF-497C-B2D6-81DCAE5789D4-a5.png']

In the image, the chirp deviation is 10 MHz. Chirp frequency is held at -10 MHz below the
 carrier frequency during rise time (0-100%) and chirp frequency is held at 10 MHz above
 the carrier frequency during fall time (100%-0). During the width (100%-100%), the chirp
 frequency increases from 10 MHz below the carrier to 10 MHz above the carrier.

The following image shows the FM chirp deviation with the above settings.

[IMAGE alt='image' src='GUID-85259F71-0A00-4805-941A-99126CB134F8-a5.png']

FM Step

For every user-defined step size, user-defined frequency is applied to the pulse signal during the pulse ON time (width (100%-100%)). The step size can be varied from step to step. If the sum of the step sizes is not equal to the pulse width, the FM steps will be padded (if there are insufficient steps) or truncated (if there are excessive steps).

Step Size: Step size for FM Step is defined as the time duration at each frequency step. Valid values are from 0 to 1 second.

Frequency: Specifies the frequency that is applied on the corresponding step size. Valid values are from -1 GHz to 1 GHz.

To create The FM Step table:

- Select FM Step from the Modulation Type drop-down list box.
- Click the Add button to enter step size and frequency values.
- Step size and Frequency values can be removed by clicking Remove button.

The following image shows UI selection for FM Step modulation.

[IMAGE alt='image' src='GUID-BEE75234-F826-43E0-A1CC-9062BB980905-a5.png']

The following image shows the frequency and time relationship for the table entries in UI details shown above.

[IMAGE alt='image' src='GUID-B2E21119-38A4-427F-96A3-62E00A825613-a5.png']

AM Step

For every user-defined step size, user-defined amplitude (dB) is applied to the pulse signal during the pulse ON time (width (100%-100%)). The step size can be varied from step to step. If the sum of step sizes is not equal to the pulse width, the AM steps will be padded (if there are insufficient steps) or truncated (if there are excessive steps).

Step Size: Step size for AM Step is defined as time duration at each AM step. Valid values are from 0 to 1 second.

Amplitude: Specifies the amplitude (dB) that is applied on the corresponding step size. Valid values are from -300 dB to 300 dB.

To create The AM Step table:

- Select AM Step from the Modulation Type drop-down list box.
- Click the Add button to enter step size and amplitude values.
- Step size and amplitude values can be removed by clicking Remove button.

The following image shows the UI selection for AM Step modulation.

[IMAGE alt='image' src='GUID-1E24055A-ECDE-42DB-8DED-1B73ABAD5EBB-a5.png']

The following images shows the amplitude and time relationship for the table entries in the UI details shown above.

[IMAGE alt='image' src='GUID-ADDBEFEF-564D-4DEE-8770-F5550155790E-a5.png']

Barker

Phase shift of 0 and 180 degrees is applied to the pulse based on the selected barker code length during pulse ON time (Width (100%-100%)).

The Pulse RFmx Waveform Creator application supports several barker codes which have unique auto correlation functions. When this modulation is selected, a drop-down list box, labelled Barker Code Length becomes available in the UI and displays the available barker code length.

[IMAGE alt='image' src='GUID-ABA49EDF-CFA1-4F54-99F4-B21DD5ED3D15-a5.png']

The following table shows the barker code for specified barker code length.

| Barker Code Length | Barker Code |
| --- | --- |
| 2 | 10 |
| 3 | 110 |
| 4a | 1101 |
| 4b | 1110 |
| 5 | 11101 |
| 7 | 1110010 |
| 11 | 11100010010 |
| 13 | 1111100110101 |

The following image shows barker phase shift of 0 or 180 on barker-7 coded signal.

[IMAGE alt='image' src='GUID-BDAD9BBA-C19A-402D-88BE-3400F9F50217-a5.png']

Parent topic:

Creating a Pulse Waveform

<!--NI_TOPIC bundle=rfmx-waveform-creator path=pulse-overview.html language=enus -->
## TOPIC 00106: Pulse Overview

- bundle_id: `rfmx-waveform-creator`
- source_path: `pulse-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/pulse-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can define the pulse shape using the following available parameters of the pulse0 section in the Pulse RFmx Waveform Creator. Pulse Envelope Type: Specifies pulse envelope type. You can change the pulse0 details section based on the pulse envelope type you select. Each pulse envelope type uses d

### Pulse Overview

You can define the pulse shape using the following available parameters of the pulse0 section
 in the Pulse RFmx Waveform Creator.

1. Pulse Envelope Type: Specifies pulse envelope type. You can
 change the pulse0 details section based on the pulse envelope type you select. Each
 pulse envelope type uses different pulse0 detail parameters. The following table
 shows all supported pulse envelope types. Trapezoidal
 Specifies a trapezoidal shaped envelope
 Raised Cosine
 Specifies a raised cosine-shaped envelope
 Custom Profile
 Specifies user-defined pulse profile data
 Custom IQ
 Specifies user-defined IQ pairs
2. Amplitude Reference Levels : Specifies the amplitude reference
 level. The timing parameters such as rise time, fall time, and width, are based on
 the amplitude reference level specified.
3. Rise Time: Specifies the rise time. Rise time is defined as the
 time taken for the rising edge of the pulse to increase in amplitude from 0% to 100%
 and 10% to 90% amplitude for 0/100/100 and 10/50/90 Volts, 10/50/90 Watts amplitude
 reference levels, respectively. Valid values are from 0 to 1 second.
4. Fall Time: Specifies the fall time. Fall time is defined as the
 time taken for the falling edge of the pulse to decrease in amplitude from 100% to
 0% and 90% to 10% for 0/100/100 and 10/50/90 Volts, 10/50/90 Watts amplitude
 reference levels, respectively. Valid values are from 0 to 1 second.
5. Width: Specifies the width. Width is defined as the ON time of
 the pulse specified from 100% to 100% and 50% to 50% for 0/100/100 and 10/50/90
 Volts, 10/50/90 Watts amplitude reference levels, respectively. Valid values are
 from 0 to 1 second.

Parent topic:

Creating a Pulse Waveform

<!--NI_TOPIC bundle=rfmx-waveform-creator path=pulse-references.html language=enus -->
## TOPIC 00107: References

- bundle_id: `rfmx-waveform-creator`
- source_path: `pulse-references.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/pulse-references.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: IEEE Standards for Transitions, Pulses, and Related Waveforms-181-2011

### References

IEEE Standards for Transitions, Pulses, and Related Waveforms-181-2011

Parent topic:

Pulse

<!--NI_TOPIC bundle=rfmx-waveform-creator path=pulse-repetition-interval-overview.html language=enus -->
## TOPIC 00108: Overview

- bundle_id: `rfmx-waveform-creator`
- source_path: `pulse-repetition-interval-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/pulse-repetition-interval-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: A pattern consists of a series or sequence of pulses. A pattern describes how the pulses are combined and played back by the Pulse RFmx Waveform Creator. This window allows you to configure pulse repetitions interval pattern parameters in the pattern0 section of the Pulse RFmx Waveform Creator. You

### Overview

A pattern consists of a series or sequence of pulses. A pattern describes how the pulses are
 combined and played back by the Pulse RFmx Waveform Creator.

[IMAGE alt='image' src='GUID-BE51621D-B965-48D5-8E47-0567407E8659-a5.png']

You can define the pulse pattern using the following available parameters of the pattern0
 section in the Pulse RFmx Waveform Creator.

Pulse Repetition Interval Type: Specifies pulse repetition interval
 type. This allows you to generate partial and multiple repetitions of the pattern. You
 can change the pattern0 details section based on the pulse repetition interval type you
 select. Each pulse repetition type uses different pattern0 detail parameters.

The following table shows all the supported pulse repetition interval types.

| None | Specifies a none pulse repetition interval type |
| --- | --- |
| Bursted | Specifies a bursted pulse repetition interval type |
| Linear Ramp | Specifies a linear ramp pulse repetition interval type |
| Stepped | Specifies a stepped pulse repetition interval type |
| Staggered | Specifies a staggered pulse repetition interval type |

Number of Pulse Repetitions: Specifies the total number of pulses
 generated. Valid values are from 1 to 1000.

Parent topic:

Creating a Pulse Waveform

<!--NI_TOPIC bundle=rfmx-waveform-creator path=pulse-repetition-interval-types.html language=enus -->
## TOPIC 00109: Pulse Repetition Interval Types

- bundle_id: `rfmx-waveform-creator`
- source_path: `pulse-repetition-interval-types.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/pulse-repetition-interval-types.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The types of pulse repetition interval are described in detail in this section. None The pulse repetition interval is said to be none if the pulse repetition interval is constant for all pulses generated. The following parameters are used for this type:Pulse Repetition Interval Start: It is defined

### Pulse Repetition Interval Types

The types of pulse repetition interval are described in detail in this section.

None

The pulse repetition interval is said to be none if the pulse repetition interval is constant for
 all pulses generated.

The following parameters are used for this
 type:

Pulse Repetition Interval Start: It is defined as the pulse repetition
 interval of the starting pulse in the pattern. Valid values are from 0 to 1 second.

The following image illustrates a none pattern.

[IMAGE alt='image' src='GUID-0ED61F39-7C77-4A2E-BC44-11B6D7DC4535-a5.png']

Bursted

The pulse repetition interval is said to be bursted if the pulse repetition interval is constant
 for all the pulses generated within a given burst interval. The burst interval is
 preserved in partial bursts by increasing the PRI of the last pulse in the burst.

The following parameters are used for this
 type:

Pulse Repetition Interval Start: It is defined as the pulse repetition
 interval of the starting pulse in the pattern. Valid values are from 0 to 1 second.

Burst Interval: It is defined as the total duration of the pattern. Valid
 values are from 0 to 1 second.

Number of Pulses: It is defined as the number of pulses in the pattern.
 Valid values are from 1 to 1000.

The
 following image illustrates a bursted pattern.

[IMAGE alt='image' src='GUID-3F618C6A-6921-4E2E-AF99-FCD277E94E39-a5.png']

Linear Ramp

The pulse repetition interval is said to be of linear type if the pulse repetition interval type
 creates a linearly increasing or decreasing pulse repetition interval pattern.

The
 following parameters are used for this type:

Pulse Repetition Interval Start: It is defined as the pulse repetition
 interval of the starting pulse in the pattern. Valid values are from 0 to 1 second.

Pulse Repetition Interval Stop: It is defined as the pulse repetition
 interval of the last pulse in the pattern. Valid values are from 0 to 1 second.

Number of Pulses: It is defined as the number of pulses in the pattern.
 Valid values are from 1 to 1000.

The following image illustrates a linear ramp pattern.

[IMAGE alt='image' src='GUID-DE968C22-011E-4DD6-859E-A9246538C7BA-a5.png']

Stepped

The pulse repetition interval is said to be stepped if the pulse repetition interval creates a
 stepped pulse repetition interval pattern.

The following parameters are used
 for this type:

Pulse Repetition Interval Start: It is defined as the pulse repetition
 interval of the starting step in the pattern. Valid values are from 0 to 1 second.

Pulse Repetition Interval Step: It is defined as the amount by which the
 pulse repetition interval changes from the current step to the next step in the pattern.
 Valid values are from 0 to 1 second.

Number of Steps: It is defined as the number of steps required to create a
 stepped pattern. Valid values are from 1 to 1000.

Pulses per Step: It is defined as the number of pulses present in each step
 in the pattern. Valid values are from 1 to 1000.

The following
 image illustrates a stepped pattern.

[IMAGE alt='image' src='GUID-0ACDBEA1-4314-4404-9886-C4C4C7E4200A-a5.png']

Staggered

This type creates a user defined pulse repetition interval pattern. You can provide pulse
 repetition interval values for N number of pulses in the table. The last index in the
 table will be considered as the number of pulses in the pattern.

The following parameter is used for this
 type:

Pulse Repetition Interval: Specifies the pulse repetition interval that is
 applied to each pulse. You can vary the pulse repetition interval from pulse to pulse.
 Valid values are from 0 to 1 second.

To create a staggered pulse repetition interval table:

- Select Staggered from the Pulse Repetition Interval Type
 drop-down list box.
- Click the Add button to enter the pulse repetition
 interval values.
- Pulse repetition interval values can be removed by clicking
 Remove button.

The following image shows the UI selection for the staggered pulse repetition interval type.

[IMAGE alt='image' src='GUID-A323CD8D-9E47-4826-8E7C-C4B8CCA2B304-a5.png']

The following image shows the pulse repetition interval pattern based on the table entries in the
 preceding image.

[IMAGE alt='image' src='GUID-00638C9E-509B-4D72-89A5-2CBC4B83E156-a5.png']

Parent topic:

Creating a Pulse Waveform

<!--NI_TOPIC bundle=rfmx-waveform-creator path=pulse-signal-config.html language=enus -->
## TOPIC 00110: Signal Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `pulse-signal-config.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/pulse-signal-config.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following parameters comprise generating signal: Pulse Repetition Interval: Specifies the pulse repetition interval. Pulse repetition interval is defined as the time interval between two consecutive pulses. Valid values are from 0 to 1 second. Sampling Rate: Specifies the sampling rate. Valid va

### Signal Configuration

The following parameters comprise generating signal:

Pulse Repetition Interval: Specifies the pulse repetition interval.
 Pulse repetition interval is defined as the time interval between two consecutive
 pulses. Valid values are from 0 to 1 second.

Sampling Rate: Specifies the sampling rate. Valid values are from 100 Hz to 1.25 GHz.

Signal Bandwidth: Specifies the signal bandwidth.

Auto: Specifies whether to enable auto signal bandwidth. If this parameter is disabled, user specified signal bandwidth is used for generation; otherwise, signal bandwidth is auto calculated using (0.8*sampling rate).

Parent topic:

Creating a Pulse Waveform

<!--NI_TOPIC bundle=rfmx-waveform-creator path=pulse.html language=enus -->
## TOPIC 00111: Pulse

- bundle_id: `rfmx-waveform-creator`
- source_path: `pulse.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/pulse.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creates a waveform that simulates a pulse signal. This section explains the process of generating a pulse waveform using the RFmx Waveform Creator with the assumption that the user knows how to package and download files to an instrument. This document assumes that you know how to package and downlo

### Pulse

Creates a waveform that simulates a pulse signal.

This section explains the process of generating a pulse waveform using the RFmx Waveform Creator with the assumption that the user knows how to package and download files to an instrument.

Note

Generating and Saving the Waveform
 File

Parent topic:

RFmx Waveform Creator Modulation Schemes

Related information:

- RFmx Pulse .NET Reference
- RFmx Pulse C API Reference

<!--NI_TOPIC bundle=rfmx-waveform-creator path=pusch-configuration.html language=enus -->
## TOPIC 00112: PUSCH Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `pusch-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/pusch-configuration.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: PUSCH configuration has three sections, PUSCH, PUSCH DM-RS, and PUSCH PT-RS. PUSCH The following configuration parameters specific to the PUSCH portion of the Uplink Signal. Symbol Allocation: Specifies the symbol indices which are allocated to PUSCH in the resource map. The format is defined in the

### PUSCH Configuration

PUSCH configuration has three sections, PUSCH, PUSCH DM-RS, and PUSCH PT-RS.

PUSCH

The following configuration parameters specific to the PUSCH portion of the Uplink
 Signal.

Symbol Allocation: Specifies the symbol indices which are
 allocated to PUSCH in the resource map. The format is defined in the Range Format
 Specifiers section. Valid values for first and last symbol are 0 to 13, while the
 last symbol must be greater than or equal to the first symbol. The default is
 0:13.

Slot Allocation: Specifies the indices of the allocated slots.
 The format is defined in the Range Format Specifiers section.
 Valid values are between 0 and (Max. Slots in Frame - 1). The maximum number of
 slots in the current frame is displayed in the Max. Slots in Frame field, which
 depends on the selected subcarrier spacing.

RB Allocation: Specifies the range of the allocated Resource
 Blocks for PUSCH. The format is defined in the Range Format
 Specifiers section. 3GPP 38.101-1/2 and
 3GPP 38.521-1/2 specifications describe certain
 predefined RB allocations. These strings can be used in addition to the range
 format specifiers. Supported RB allocation strings for Frequency Range 1 are
 Edge_Full_Left, Edge_Full_Right, Edge_1RB_Left, Edge_1RB_Right, Outer_Full,
 Inner_Full, Inner_1RB_Left, and Inner_1RB_Right. Supported RB allocation strings
 for Frequency Range 2 are Outer_Full, Outer_1RB_Left, Outer_1RB_Right, and
 Inner_Full. For more information about RB Allocation, refer to the following
 figure with configuration - Allocated slots 2:11, RB Allocation 1:13.

[IMAGE alt='image' src='GUID-CD44E5A2-2778-4CE7-A85A-384C18DA099E-a5.gif']

Transform Precoding (DFT-s-OFDM): Specifies whether to enable
 transform precoding. If this parameter is disabled, the signal will be CP-OFDM
 modulated; otherwise, the signal will be DFT-S-OFDM modulated.

PI/2 BPSK Spectral Shaping: Specifies whether to spectrally
 shape the signal at the generation. If this parameter is enabled, the transmitted
 signal passes through a spectral shaping filter that reduces the PAPR of the
 generated waveform. The filter coefficients are set according to PI/2
 BPSK Shaping Type and PI/2 BPSK Shaping
 Coefficients configuration. This parameter is valid only when
 you set the Modulation Type parameter to PI/2
 BPSK and Transform Precoding (DFT-s-OFDM)
 parameter is enabled.

PI/2 BPSK Enabled: When you set the MCS
 Table to 64QAM TP and MCS index is ≤ 1 or
 When you set the MCS Table to 64QAM TP
 LowSE and MCS index is ≤ 5, PI/2BPSK modulation is used if this
 checkbox is selected; otherwise QPSK is used. This checkbox is ignored for other
 combinations of MCS table and MCS index if Channel Coding
 is enabled.

Channel Coding: Specifies whether channel coding is enabled.
 If enabled, Modulation type is calculated from MCS Table
 and MCS Index parameters, otherwise the user specified
 value is honored.

MCS Table: Specifies the modulation and coding scheme table to
 be used for channel coding as defined in section 5.1.3.1 and section 6.1.4.1 of
 3GPP 38.214 specification.

| MCS Table Value | 3GPP 38.214 Reference | Applicable |
| --- | --- | --- |
| 256QAM | Table 5.1.3.1-2: MCS index table 2 for PDSCH | - |
| 64QAM | Table 5.1.3.1-1: MCS index table 1 for PDSCH | Only allowed if Transform Precoding is disabled. |
| 64QAM LowSE | Table 5.1.3.1-3: MCS index table 3 for PDSCH |  |
| 64QAM TP | Table 6.1.4.1-1: MCS index table for PUSCH with transform precoding and 64QAM | Only allowed if Transform Precoding is enabled. |
| 64QAM TP LowSE | Table 6.1.4.1-2: MCS index table 2 for PUSCH with transform precoding and 64QAM |  |

LBRM Enabled: Specifies whether Limited Buffer Rate Matching
 is enabled.

Modulation Type: Specifies the modulation type to be used.
 When channel coding is enabled, this indicates the modulation type that is being
 used based on the values of MCS Table and MCS
 Index.

MCS Index: Specifies the MCS index from the selected table.
 Modulation type and code rate are determined from the specified MCS
 Index and MCS Table.

Redundancy Version: Specifies the redundancy version to use
 for channel coding. Valid values are 0 to 3.

Data Scrambling ID Mode: If you set this parameter to
 User Defined, the scrambling sequence generator will
 be initialized with the value specified in the Data Scrambling
 Id parameter.

If you set this parameter to Cell ID, the scrambling sequence
 generator will be initialized with the value specified in the Cell
 ID parameter in the Carrier Definition section.

Data Scrambling Id: Initializes the scrambling sequence
 generator. Valid values range from 0 to 1023. This value is used only if you set
 the Data Scrambling ID Mode parameter to User
 Defined.

PUSCH Power: Specifies the factor by which the PUSCH REs are
 scaled.

Max. Slots in Frame: Specifies the maximum number of slots
 available for a PUSCH configuration in the current bandwidth part
 configuration.

PUSCH DMRS

The following configuration parameters specific to the DMRS portion of the Uplink
 Signal.

DMRS Power Mode: Specifies whether the configured
 DMRS Power is honored or calculated from CDM Groups
 for Reference Signal generation.

DMRS Power: This parameter used to set the DMRS power in dB
 relative to the PUSCH data power. The recommended DMRS Power depends on the chosen
 Number of DM-RS CDM Groups without data:

| Number of CDM Groups | DMRS Config Type 1 | DMRS Config Type 2 |
| --- | --- | --- |
| 1 | 0 dB | 0 dB |
| 2 | 3 dB | 3 dB |
| 3 | - | 4.77 dB |

DMRS Config Type: Determines the way the DMRS is mapped to
 physical resources. Either Type 1 or Type
 2 can be selected.

DMRS Duration: Specifies the DMRS symbol length. Valid values
 are Single Symbol and Double
 Symbol.

DMRS Type A Position: Configures the position of the first
 DMRS symbol if Type A DMRS mapping is selected. Valid values are 2 and 3. This
 value is ignored in case of Type B DMRS mapping.

DMRS Additional Positions: Specifies the positions of
 additional DMRS symbols. Valid values are 0, 1,2, 3. If 0 is selected, no
 additional DMRS symbols are added.

PUSCH Mapping Type: Allows you to choose between
 Type A and Type B mapping.

- For Type A, the position of the first DMRS symbol can be set via the DMRS Type
 A Position field.
- For Type B, the position of the first DMRS symbol is the lowest symbol index
 specified in the Active Symbol Map.

Number of CDM Groups: Specifies the number of DMRS CDM groups
 without data parameter. Valid values are 1, 2, and 3 - depending on the number of
 transmit antenna ports and DMRS Config Type.

DMRS Antenna Ports: Specifies the antenna ports used for DMRS
 transmission. The antenna ports are given as a comma separated list. The number of
 specified DMRS antenna is equal to the Number of Layers.

DMRS Release Version: Specifies the 3GPP release version for
 generating the DMRS sequence. Allows you to choose between 3GPP Release
 15 and 3GPP Release 16.

- For 3GPP Release 16 , the DMRS sequence is generated as
 per section 6.4.1.1.1 of 3GPP TS 38.211 g00 specification.
- For 3GPP Release 15 , the DMRS sequence is generated as
 per section 6.4.1.1.1 of 3GPP TS 38.211 f80 specification.

DMRS Scrambling ID Mode: If you set this parameter to
 User Defined, the DMRS scrambling sequence generator
 is initialized with the value specified in the DMRS Scrambling ID field.

If you set this parameter to Cell ID, the DMRS scrambling
 sequence generator is initialized with the value specified in the Cell
 ID field in the Carrier Definition section.

DMRS Scrambling Id: Initializes the DMRS scrambling sequence
 generator. Valid values range from 0 to 65535. This value is used only if the
 DMRS Scrambling ID Mode is set to User
 Defined.

nSCID: The DMRS scrambling sequence generator will be
 initialized with a value that is calculated from the DMRS Scrambling ID and the
 nSCID. Valid values are 0 and 1. This value is used only if the DMRS
 Scrambling ID Mode is set to User
 Defined.

Group Hopping: Specifies whether to enable or disable group
 hopping.

Sequence Hopping: Specifies whether to enable or disable
 sequence hopping.

PUSCH ID Mode: If you set this parameter to User
 Defined, the value in the PUSCH ID field
 will be used as the PUSH Id. If you set this parameter to Cell
 ID, the Cell ID will be used as the PUSH Id.

PUSCH ID: Specifies the PUSCH identifier. This value is used
 only if you set the PUSCH ID Mode parameter to
 User Defined.

PUSCH PT-RS

The following configuration parameters are specific to the Phase Tracking Reference
 Signal.

PTRS Enabled: Specifies whether to enable adding a PTRS to the
 waveform.

PTRS Power Mode: Specifies whether the PTRS power is set
 according to the 3GPP standard or as per user configuration. The default value is
 Standard.

| Standard |
| --- |
| User Defined |
| Sets the PUSCH PTRS power scaling, βPT-RS, according to the values when UL-PTRS-power = 01 in the Table 6.2.3.1-3 of 3GPP TS 38.214 specification. |
| Sets the PUSCH PTRS power scaling, βPT-RS, to the value specified in the PTRS Power parameter. |

PTRS Power: Specifies the power of the PTRS.

PTRS RE Offset: Specifies the resource element offset. This
 parameter along with the PTRS Frequency Density is used to
 calculate the subcarrier indices to which the PTRS shall be mapped. Valid values
 are 0, 1, 2, and 3.

PTRS Frequency Density: This parameter along with the
 PTRS RE Offset is used to calculate the subcarrier
 indices to which the PTRS shall be mapped. The parameter is used for CP-OFDM. This
 parameter is not used if transform precoding is enabled. Valid values are 2,
 4.

PTRS Time Density: This parameter is used to calculate the set
 of time indices defined relative to the start of the PUSCH allocation. Valid
 values are 1, 2, and 4.

Number of PTRS Groups: This parameter along with the PTRS RE
 Offset is used to calculate the subcarrier indices to which the PTRS shall be
 mapped. The parameter is used for CP-OFDM. This parameter is not used if transform
 precoding is enabled. Valid values are 2 and 8.

Samples Per PTRS Groups: This parameter along with the PTRS RE
 Offset is used to calculate the subcarrier indices to which the PTRS shall be
 mapped. The parameter is used for CP-OFDM. It is not used if transform precoding
 is enabled. Valid values are 2 and 4.

PTRS Antenna Ports: Specifies the antenna ports used for PTRS
 transmission. The antenna ports are given as a comma separated list. The antenna
 ports need to be a subset of the DMRS Antenna Ports. There are either 1 or 2 PTRS
 Antenna Ports allowed.

Parent topic:

NR

Related concepts:

- Range Format Specifiers

<!--NI_TOPIC bundle=rfmx-waveform-creator path=range-format-specifiers.html language=enus -->
## TOPIC 00113: Range Format Specifiers

- bundle_id: `rfmx-waveform-creator`
- source_path: `range-format-specifiers.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/range-format-specifiers.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The range format specifier is a comma separated list of entries in the following format. Single unsigned integer values or last A range of single unsigned integer values given as i[0]:i[1], where i[0] and i[1] represent the first and the last value in the range. The value of i[0] is always less than

### Range Format Specifiers

The range format specifier is a comma separated list of entries in the following format.

- Single unsigned integer values or last
- A range of single unsigned integer values given as
 i 0 : i 1 , where
 i 0 and i 1 represent
 the first and the last value in the range. The value of
 i 0 is always less than or equal to
 i 1 .

The keyword last expands to the largest allowed value, depending on
 the context of the range specification.

For example,

- 2,5 will expand to {2,5}
- 1:3,7 will expand to {1,2,3,7}

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=references.html language=enus -->
## TOPIC 00114: References

- bundle_id: `rfmx-waveform-creator`
- source_path: `references.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/references.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: 3GPP TS 36.201 Evolved Universal Terrestrial Radio Access (E-UTRA); Physical Layer – General Description. 3GPP TS 38.201 NR; Physical Layer; General Description. 3GPP TS 38.211 NR; Physical Channels and Modulation. 3GPP TS 38.212 NR; Multiplexing and channel coding. 3GPP TS 38.213 NR; Physical layer

### References

| 3GPP TS 36.201 | Evolved Universal Terrestrial Radio Access (E-UTRA); Physical Layer – General Description. |
| --- | --- |
| 3GPP TS 38.201 | NR; Physical Layer; General Description. |
| 3GPP TS 38.211 | NR; Physical Channels and Modulation. |
| 3GPP TS 38.212 | NR; Multiplexing and channel coding. |
| 3GPP TS 38.213 | NR; Physical layer procedures. |
| 3GPP TS 38.321 | NR; Medium Access Control (MAC) protocol specification |

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=rfmx-waveform-creator-examples.html language=enus -->
## TOPIC 00115: RFmx Waveform Creator Examples

- bundle_id: `rfmx-waveform-creator`
- source_path: `rfmx-waveform-creator-examples.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/rfmx-waveform-creator-examples.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Waveform Creator includes several example setting files that demonstrate the functionality of your software and can serve as an interactive tool. You can access all the installed RFmx Waveform Creator examples from the Start menu. (Windows 7) Select Start»All Programs»National Instruments»RFmx

### RFmx Waveform Creator Examples

RFmx Waveform Creator includes several example setting files that demonstrate the
 functionality of your software and can serve as an interactive tool.

You can access all the installed RFmx Waveform Creator examples from the
 Start menu.

- (Windows 7) Select Start»All Programs»National Instruments»RFmx Waveform
 Creator»RFmx Waveform Creator Examples
- (Windows 10/8.1) Select Start»National Instruments»RFmx Waveform Creator
 Examples

RFmx Waveform Creator Examples

Modulation

Note

<!--NI_TOPIC bundle=rfmx-waveform-creator path=rfmx-wc-modulation-schemes.html language=enus -->
## TOPIC 00116: RFmx Waveform Creator Modulation Schemes

- bundle_id: `rfmx-waveform-creator`
- source_path: `rfmx-wc-modulation-schemes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/rfmx-wc-modulation-schemes.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Waveform Creator provides multiple modulation schemes, including AM, FM, PM, and digital formats. Learn configuration options, key parameters, and practical use cases for generating accurate, customizable waveforms.

### RFmx Waveform Creator Modulation
 Schemes

RFmx Waveform
 Creator provides multiple modulation schemes, including
 AM, FM, PM, and digital formats. Learn configuration options, key parameters, and practical
 use cases for generating accurate, customizable waveforms.

- [Bluetooth](bt.html) Creates a waveform that simulates a Bluetooth carrier.
- [EV-DO Revision 0](ev-do-revision-0-overview.html) Creates a waveform that simulates a EV-DO carrier.
- [EV-DO Revision A](ev-do-revision-a-overview.html) Creates a waveform that simulates a EV-DO Revision A carrier.
- [CDMA2k (3GPP2)](cdma2k-3gpp2.html) Creates a waveform that simulates CDMA2k (3GPP2). CDMA2k is a standard for 3G wireless technology that is derived from cdmaOne (IS95).
- [GSM/EDGE](gsmedge-overview.html) Creates a waveform that simulates a GSM/EDGE signal.
- [LTE](lte.html) Creates a waveform that simulates a 3GPP LTE carrier.
- [NR](nr-overview.html) Creates a waveform that simulates a 3GPP NR carrier.
- [Pulse](pulse.html) Creates a waveform that simulates a pulse signal.
- [TD-SCDMA (3GPP TDD-LCR)](td-scdma-3gpp-tdd-lcr.html) Creates a waveform that simulates a 3GPP TDD-LCR carrier.
- [WCDMA (3GPP FDD Release 8)](wcdma-3gpp-fdd-release-8.html) Creates a waveform that simulates a 3GPP FDD carrier.
- [WLAN](wlan.html) Creates a waveform that simulates a WLAN carrier.
- [Multi-Carrier Configuration](multi-carrier-configuration.html)
- [Analog Modulation](analog-modulation.html) Information about frequency modulation and amplitude modulation.
- [Generating a User File](generating-a-user-file.html#GUID-A2508C03-0466-4A14-BBB7-25F5F59AEDD7) Generate and import custom user-defined waveform files.
- [Default Modulation Mappings](default-modulation-mappings.html#GUID-3A05DBA4-664B-4241-98CA-776C975FDF42) Modulation mappings that are implemented by RFmx Waveform Creator and how you can modify them.

Related concepts:

- Generating and Saving the Waveform File

<!--NI_TOPIC bundle=rfmx-waveform-creator path=rfsg-database.html language=enus -->
## TOPIC 00117: RFSG Database

- bundle_id: `rfmx-waveform-creator`
- source_path: `rfsg-database.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/rfsg-database.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFSG database is a feature that allows users to store and retrieve various properties associated with a particular waveform.You can create multiple waveforms for a particular standard and download these waveforms to the arbitrary waveform generator (arb) memory. You can then generate all these w

### RFSG Database

The RFSG database is a feature that allows users to store and retrieve various properties
 associated with a particular waveform.

You can create multiple waveforms for a particular standard and download these waveforms to the
 arbitrary waveform generator (arb) memory. You can then generate all these waveforms
 using either a single script or multiple scripts. You need to set the appropriate
 NI-RFSG properties corresponding to the waveform being generated. Use the RFSG database
 feature to retrieve the properties for the waveform being generated.

Currently, the toolkit stores the I/Q rate, headroom, burst start locations, burst stop
 locations, and waveform size properties for each waveform. The toolkit requires that the
 I/Q rate of all the waveforms be the same so that you can generate them using a single
 script. The toolkit selects the minimum headroom value and applies it to all waveforms.
 You can add more properties to the RFSG database to track more RFSG properties per
 waveform.

If you want to generate a waveform from a specific standard, the toolkit configures the
 properties of the NI-RFSG to do this task. These properties are global with respect to
 the driver. Hence, the values of the properties apply to all waveforms. However, this
 fact may be an issue if you want to generate waveforms that have different values or
 properties associated with them. For example, if you want to generate waveform 1,
 waveform 2, and then waveform 1 again, each time a new waveform is generated, you must
 reconfigure the driver for that waveform, even if you have already configured it.

By using the RFSG database, you can store the required properties for each waveform in the
 database and then query them later while generating those waveforms.

Parent topic:

WLAN

<!--NI_TOPIC bundle=rfmx-waveform-creator path=save-waveform-file.html language=enus -->
## TOPIC 00118: Save Waveform File

- bundle_id: `rfmx-waveform-creator`
- source_path: `save-waveform-file.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/save-waveform-file.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: After setting up all parameters that are required to define your waveform, you can generate and save the waveform file in .tdms format. To save the waveform file, Select the Save Waveform File menu and select Current Settings option to display the Save Waveform File dialog box as shown in the follow

### Save Waveform File

After setting up all parameters that are required to define your waveform, you can
 generate and save the waveform file in .tdms format.

To save the waveform file,

1. Select the Save Waveform File menu and select
 Current Settings option to display the Save Waveform File
 dialog box as shown in the following figure.
2. In the Save Waveform File dialog box,
  - Enter File Path .
  - Select Waveform File Version .
  - Enter Runtime Scaling .
  - Select Datatype .
  - Add Description for the waveform file.
  - Select Store Configuration checkbox to embed the
 current settings in the waveform file. The Store
 Configuration checkbox is deselected by default. This option
 does not apply to legacy plugins such as User and
 Tones which save the settings in
 .rfwc format.
  - Deselect the Show File Summary checkbox, if required. The Show
 File Summary checkbox is selected by default.
 Note Selecting the Show File Summary
 checkbox presents the File Summary dialog box.
 For more information about the File Summary
 dialog box, refer to the File Summary topic.
3. Click Save to save the waveform.

Note

.tdms

The waveform file version 2.0 contains NI_RF_RuntimeScaling and
 NI_RF_PAPR fields in dB, in the TDMS header. Waveform values saved in
 the file are scaled by NI_RF_PAPR value. The RFmx Waveform Creator computes
 peak to average power ratio (PAPR) of the waveform. The default value is 2.0.

The waveform file version 1.0 contains NI_RF_Headroom field in dB, in the TDMS
 header. The Runtime Scaling control is disabled and the value is
 ignored. Waveform values saved in the file are scaled by NI_RF_Headroom
 value. The RFmx Waveform Creator computes Headroom as ceil(PAPR + 1.5) in dB.

For more information on using your own I and Q data, refer to *Generating a User
 File*.

Related tasks:

- Generating a User File

<!--NI_TOPIC bundle=rfmx-waveform-creator path=selecting-the-channel-filter.html language=enus -->
## TOPIC 00119: Selecting the Channel Filter

- bundle_id: `rfmx-waveform-creator`
- source_path: `selecting-the-channel-filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/selecting-the-channel-filter.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: In general, the type of filter you use as your channel filter will depend upon the signal you are planning to create. For example, the TETRA standard requires you to use a Root Raised Cosine filter. RFmx Waveform Creator allows you to choose from 11 different filter types. The majority of these filt

### Selecting the Channel Filter

In general, the type of filter you use as your channel filter will depend upon the signal
 you are planning to create. For example, the TETRA standard requires you to use a Root
 Raised Cosine filter. RFmx Waveform Creator allows you to choose from 11 different
 filter types. The majority of these filter types are used in one or more digital
 modulation standards. In general, you use a filter to limit the occupied bandwidth of
 the signal or to shape the pulses as required by the modulation scheme you are
 simulating. You select the filter type by going to the Filter tab
 and selecting the Filter Type combo box. The following image
 shows a typical Filter tab.

[IMAGE alt='image' src='GUID-EA7558AE-4316-4764-8385-746C5BD765C7-a5.png']

The filter types available in RFmx Waveform Creator are given in the following list.

- Raised Cosine (Nyquist)
- Root Raised Cosine (Root Nyquist)
- Gaussian
- Gaussian EDGE
- CDMA2k Filters
- Ideal Low Pass
- Half Sine
- User

If you know the length of filter required, enter the number. But if you are unsure, then
 check the Estimate Filter Length box and click the
 Estimate button. The software calculates the filter length to
 give a filter that provides the ACP and EVM requested in the Required
 ACP and Required EVM boxes. The new estimates are
 presented. You can also estimate the expected performance of your filter by pressing the
 Estimate button for the length that you have chosen. In this
 case, do not have the Estimate Filter Length box checked.

You can also select a Window Type function as part of the filter
 setup. Essentially, the window is used to enhance the stop band capability of the
 filter. There is a trade-off between stop band and EVM. Select the window that best
 suits your needs. For more information about the window types, refer to the Selecting the window type topic. RFmx Waveform Creator recommends using the
 Parabolic window type.

You can also set the type of impulse function that RFmx Waveform Creator should use for
 filtering by selecting either the Dirac Impulse or
 Rect Impulse radio button. For more information about impulse
 types, refer to Selecting the impulse function.

For this example, select a Root Raised Cosine (Root Nyquist)
 filter. Then in Alpha, set the bandwidth of the filter. In this
 case, select a value of 0.3.

#### Raised Cosine (Nyquist) Filter

[IMAGE alt='image' src='GUID-CB17DD26-098C-4FF5-8267-7940412882BA-a5.png']

α

T

[IMAGE alt='image' src='GUID-F132338C-3548-4137-8887-260F5DDE63C3-a5.png']

[IMAGE alt='image' src='GUID-0D03D939-EF32-4BCA-8C57-9FD8F1C37AD4-a5.png']

#### Root Raised Cosine Filter

[IMAGE alt='image' src='GUID-D737D498-4F95-4B61-9842-D6D11B62A417-a5.png']

α

T

[IMAGE alt='image' src='GUID-FE5E30FF-6257-4336-97BD-857BC632E13F-a5.png']

[IMAGE alt='image' src='GUID-D1C2C9E0-24CB-49AA-A130-02E7FEBDAA95-a5.png']

#### Gaussian Filter

The Gaussian filter has a frequency response that resembles a bell shape. This filter is used
 in GSM and in GFSK modulation schemes. The frequency response is given by:

[IMAGE alt='image' src='GUID-8BD102C9-F88B-468E-BB5E-A6BE9DDB5263-a5.gif']

Where B is the 3 dB bandwidth of the filter. The impulse response is given
 by:

[IMAGE alt='image' src='GUID-2F83CB44-D24A-4512-A2D6-BFA7F622C91B-a5.gif']

where

[IMAGE alt='image' src='GUID-D8ACB9B7-BEB5-4670-BA37-A95C7E4A4892-a5.gif']

and BT is used to define a normalized bandwidth. For GSM,
 BT is 0.3. The impulse response is shown in the following image.

[IMAGE alt='image' src='GUID-1C7789BE-D460-4E16-8E8E-9A0303D60A58-a5.gif']

#### Gaussian EDGE Filter

The Gaussian EDGE filter is a fixed filter that is defined for EDGE modulation. The
 filter is described as a linearized GMSK pulse. The response is defined as follows:

[IMAGE alt='image' src='GUID-F759F57C-59B6-4893-9BAB-9A58616CDFAA-a5.gif']

where

[IMAGE alt='image' src='GUID-A8393E81-2688-4977-8701-173066759F3B-a5.gif']

[IMAGE alt='image' src='GUID-A7D49B1C-15AB-4588-AC01-75F98526ED52-a5.gif']

and

[IMAGE alt='image' src='GUID-7A2B4522-E7C3-485D-B81F-0A5B2C703B1A-a5.gif']

The impulse response of this filter is shown in the following image.

[IMAGE alt='image' src='GUID-25CE4DE8-3E14-482C-A114-588DF76E5334-a5.gif']

#### CDMA2k Filters

The RFmx Waveform Creator provides you with 6 different filters that are associated with
 CDMA2k (and IS95). The filters are as follows:

- CDMA2k 1x (Standard)
- CDMA2k 1x (Improved ACP)
- CDMA2k 1xPlusEqualization (Standard)
- CDMA2k 1xPlusEqualization (Improved ACP)
- CDMA2k 3xDS (Standard)
- CDMA2k 3xDS (Improved ACP)

CDMA2k 1x (Standard) and CDMA2k 3x DS (Standard) filters defined in the 3GPP2
 C.S0002-C specification that are used for the reverse link 1x and 3x
 spreading rates. The filter CDMA2k 1xPlusEqualization (Standard) is the filter defined
 in the specification for the forward link.

[IMAGE alt='image' src='GUID-5C20CFED-762B-4E65-9913-D805E9342F2E-a5.png']

[IMAGE alt='image' src='GUID-DA796030-9861-4EAC-8200-175A5FD7DA1D-a5.png']

#### Ideal Low Pass Filter

This filter has a frequency response of an ideal low pass filter with a frequency cut off
 that is equal to half the symbol rate.

The longer you make this filter, the sharper the cut off will be.

You can use this filter when you want to oversample without applying a shaping filter
 such as a root raised cosine. The impulse and frequency responses of this filter are
 shown in the following figures.

Note

[IMAGE alt='image' src='GUID-A0F5095C-52E7-4D95-95E9-1057290210BF-a5.gif']

[IMAGE alt='image' src='GUID-62044C25-4003-4C74-82F8-F1F85582E982-a5.gif']

#### Half Sine Filter

The impulse response of a half sine filter is given by the following equation:

[IMAGE alt='image' src='GUID-BCA5DACF-2053-4521-913D-4A7D6D4954B6-a5.gif']

Where, 2T<sub>c</sub> is the symbol period.

The impulse response of this filter is shown in the following figure.

[IMAGE alt='image' src='GUID-95119A1C-5E79-43B9-A296-B56DDC0C2F67-a5.gif']

#### User Filter Coefficients

RFmx Waveform Creator provides most of the common filter types that you are likely to
 encounter. However, there may be instances when you want to use your own special filter.
 To do this, select User from the Filter
 Type drop-down list. The User Coefficient File
 box allows you to browse the file.

You must set the over-sampling factor associated with the filter. This is generally done
 from the Modulation tab. The coefficients file must be an ASCII
 (text) file. Each coefficient is stored in floating point number format and delimited by
 commas, spaces or tabs, line feeds or carriage returns. For example, -0.025288315
 -0.034167931 -0.035752323 -0.016733702 0.021602514 0.064938487 0.091002137 0.081894974
 0.037071157 -0.021998074

Ideally, the sum of your coefficients should be equal to 1 to
 ensure unity gain through the filter. No other file format is currently
 supported.

#### Selecting the Impulse Function

Dirac Impulse

Rect Impulse

[IMAGE alt='image' src='GUID-01336705-967C-4249-9D47-F17783691047-a5.png']

[IMAGE alt='image' src='GUID-2FCE8618-3526-4595-9B48-8249B354C17A-a5.png']

In general, you would use a rectangular impulse for FSK systems, otherwise the Dirac impulse
 should be used. The default impulse function used by the RFmx Waveform Creator depends on the
 modulation scheme (or system) that you have selected. Unless you are an advanced user, keep to
 the default settings.

<!--NI_TOPIC bundle=rfmx-waveform-creator path=selecting-the-data-source.html language=enus -->
## TOPIC 00120: Selecting the Data Source

- bundle_id: `rfmx-waveform-creator`
- source_path: `selecting-the-data-source.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/selecting-the-data-source.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure the data source for a waveform with the bit sequence to modulate, bit encoding method, and PRBS type. Use the Data Source tab to configure the data source. To enable the Data Source tab, select a modulation type. For more information, refer to Selecting the Modulation Type. The following f

### Selecting the Data Source

Configure the data source for a waveform with the bit sequence to modulate, bit
 encoding method, and PRBS type.

Use the Data Source tab to configure the data source.

Note

Data Source

Selecting the Modulation Type

The following figure shows a typical, generic modulation scheme.

Figure 1.

[IMAGE alt='Data Source tab showing a typical generic modulation scheme' src='GUID-234A28A5-F05C-47E6-B707-143179F60499-a5.png']

- Data Source Type : select the bit sequence to modulate.
  - PRBS Sequences (default)
  - User Data Sequences
  - Repeating Patterns
- Bit Encoding Method : select the bit encoding method to
 apply to the bit sequence. Leave at the default None , or
 select from the following 5-bit encoding methods:
  - Differential
  - GSM Differential
  - Inverted
  - Manchester
  - NRZ Inverted
- PRBS Type : select a pre-defined PRBS sequence or select
 User Defined . To toggle the seed of the
 selected PRBS sequence, click on the required bit.

You cannot change the feedback mask or the PRBS length of a pre-defined PRBS
 sequence.

PRBS Type

User Defined

- To enter or remove a feedback path, click on the appropriate tap mask
 square.
- To change the PRBS length, enter the value into the
 Length text box. The maximum PRBS length
 is 32.

Related concepts:

- Selecting the Modulation Type
- RFmx Waveform Creator 2026 Q2 Changes

#### PRBS Sequences

In RFmx Waveform Creator, a pseudo random binary sequence (PRBS) is generated using a
 linear feedback shift register (LFSR). The following figure shows a block diagram of a
 shift register with nine registers and two taps from which the feedback is obtained.

[IMAGE alt='image' src='GUID-08FAABD5-BA82-4551-8124-97B762352D38-a5.png']

The characteristic polynomial that describes this sequence is f (x) = x<sup>9</sup> +
 x<sup>4</sup> + 1. The output is obtained by XORing the register values attached to
 the taps, feeding this back and shifting the registers by one as indicated in the
 preceding figure. An LFSR is defined by the location of feedback taps, the number of
 registers and the initial state of the registers. The output sequence will always be
 periodic because whatever the initial conditions of the shift register, after a finite
 number of shifts, the initial conditions will eventually be reproduced. The maximum
 number of different combinations is equal to 2N-1. An LFSR, whose
 output sequence has a period of 2N-1 is called a maximal length
 sequence. These sequences are also referred to pseudo random (PN) sequences.

#### Repeating Patterns

In RFmx Waveform Creator, a repeating pattern is a pattern of 1's and 0's that repeats
 until the required number of bits has been generated. You enter the pattern of your
 choice in the text box as shown in the bitmap below.

[IMAGE alt='image' src='GUID-0248696E-550E-4C6D-9AB8-39A92B1573C8-a5.png']

The example above shows a pattern of 01011. This pattern will repeat to generate a bit
 sequence of 01011010110101101011… until the required number of bits is generated. The
 maximum length of the repeating pattern is 16 bits. RFmx Waveform Creator does not allow
 you to define a longer sequence. The pattern must be entered as a binary sequence.

#### User Data Sequences

RFmx Waveform Creator allows you to input your own bit sequence as a data source. This is
 done by placing your required data into an ASCII file. The bits must be delimited by
 commas, spaces or tabs, line feeds or carriage returns. Values must be either 0 or 1.
 Any non-zero and/or non-delimited value will be set to 1 by the software.

You can select the Data Source tab and set the Source
 Type as User Data from File. you will be asked to
 enter a file name as indicated in the bitmap below.

[IMAGE alt='image' src='GUID-DDC31042-E346-4E28-9A09-655DF2ECC1D3-a5.png']

Depending on the modulation scheme that you are working with the method to select a user
 data sequence will vary.

#### Bit Encoding

RFmx Waveform Creator helps you in encoding the bit sequence (data source) before
 modulating. There are five types of encoding are available.

Differential

n

n

n

n

n

[IMAGE alt='image' src='GUID-5100216F-2AF6-4BB7-8582-D36E66FC7F94-a5.png']

where [IMAGE alt='image' src='GUID-B1C1927A-AC67-484F-9791-F6FA56C7216C-a5.png'] is an EXCLUSIVE OR operation.

GSM Differential

n

n

n

n

n

[IMAGE alt='image' src='GUID-C7A1995E-69B3-4112-8E45-F06337476690-a5.png']

where [IMAGE alt='image' src='GUID-B1C1927A-AC67-484F-9791-F6FA56C7216C-a5.png'] is an EXCLUSIVE OR operation and
 [IMAGE alt='image' src='GUID-66F47B5F-02AB-4A97-83C8-A347CAC33BFE-a5.png'] is the NOT of
 x.

Inverted

n

n

n

n

[IMAGE alt='image' src='GUID-77827FFB-E9AD-4456-92AF-1245CE0AA843-a5.png']

where [IMAGE alt='image' src='GUID-66F47B5F-02AB-4A97-83C8-A347CAC33BFE-a5.png'] is the NOT of
 x.

NRZ Inverted (Non return to zero inverted)

n

n

n

n

n

[IMAGE alt='image' src='GUID-5100216F-2AF6-4BB7-8582-D36E66FC7F94-a5.png']

where [IMAGE alt='image' src='GUID-B1C1927A-AC67-484F-9791-F6FA56C7216C-a5.png'] is an EXCLUSIVE OR operation and
 [IMAGE alt='image' src='GUID-66F47B5F-02AB-4A97-83C8-A347CAC33BFE-a5.png'] is the NOT of
 x.

Manchester

Let b<sub>n</sub> be the binary input sequence of length n and d<sub>k</sub>+1 be the
 binary output sequence of length k+1 after encoding. d<sub>k</sub>
 and d<sub>k</sub>+1 are then defined as:

d<sub>k</sub> = b<sub>n</sub>

[IMAGE alt='image' src='GUID-38147FF5-E519-48CE-A7B8-6DBD3DD4E7E1-a5.png']

where k = 2<sub>n</sub> and [IMAGE alt='image' src='GUID-66F47B5F-02AB-4A97-83C8-A347CAC33BFE-a5.png']
 is the NOT of x.

#### Auto Cyclic Data

Auto‑cyclic data maintains phase continuity.

Adding an additional number of symbols to the signal makes the signal phase continuous.

Note

#### SOQPSK Differential

Let b<sub>2i</sub> and b<sub>2i+1</sub> be the user binary input bit pairs at time index
 *i*, and δ<sub>2i</sub> and δ<sub>2i+1</sub> be the differentially encoded output
 bits.

- δ
 2
 i
 =
 b
 2
 i
 ⊕
 δ
 2
 i
 -
 1
 ¯
- δ
 2
 i
 +
 1
 =
 b
 2
 i
 +
 1
 ⊕
 δ
 2
 i

- ⊕ is an EXCLUSIVE OR operation
- is the NOT of x

<!--NI_TOPIC bundle=rfmx-waveform-creator path=selecting-the-modulation-type.html language=enus -->
## TOPIC 00121: Selecting the Modulation Type

- bundle_id: `rfmx-waveform-creator`
- source_path: `selecting-the-modulation-type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/selecting-the-modulation-type.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Modulation tab enables you to set modulation type, number of symbols, symbol rate, and oversampling factor. For example, select QPSK, keep the number of symbols as 1024 and the symbol rate as 100 kHz. For oversampling factor, the default is 4, which means that the symbol rate is oversampled by a

### Selecting the Modulation Type

The Modulation tab enables you to set modulation type, number of
 symbols, symbol rate, and oversampling factor.

[IMAGE alt='image' src='GUID-E0B7718F-6A2C-4D97-BD16-939F168B93D8-a5.png']

For example, select QPSK, keep the number of symbols as 1024 and
 the symbol rate as 100 kHz.

For oversampling factor, the default is 4, which means that the symbol rate is
 oversampled by a factor of 4 before filtering. To modify the default value, unselect the
 Auto checkbox.

To modify the IQ symbol mapping for phase modulated schemes, click Modify
 Mapping button. For more information, refer to the Appendix
 A section of RFmx Waveform Creator Modulation
 Schemes.

Each modulation scheme supported by RFmx Waveform Creator has a different
 modulation tab layout. For more information about the modulation schemes, refer to the
 *RFmx Waveform Creator Modulation Schemes*.

Note

Number of
 Symbols

Number of
 Symbols

Related concepts:

- RFmx Waveform Creator Modulation Schemes

#### Changing Symbol Mapping

Some modulations allow you to configure the symbol mapping of the signal. To edit the symbol
 mapping, click on Modify Mapping button.

##### Symbol Mapping Editor

For modulation types that have a fixed mapping
 between constellation position and symbol, a mapping plot will be presented as shown in the
 following image.

[IMAGE alt='image' src='GUID-C24F14B4-56E4-4468-AABF-AFDFDEE54E70-a5.png']

For all QAM modulations, symbols are plotted in terms of their I-Q values. For all
 non-differential PSK types, symbols are plotted in terms of their phase
 values.

##### Selecting a Symbol

You can enter a specific symbol number in the
 Symbol control and click Find. This will
 select the point within the trace that is mapped to the selected symbol value. The selected
 symbol is shown in a red color.

Note

##### Changing a Symbol Mapping

Once you have selected a symbol, you can
 enter a new mapping in the Symbol control and click
 Set. This will apply the new mapping to the currently selected
 point.

Resetting the Symbol Mapping

You can reset the symbol mapping to the
 default values by clicking the Reset To Default button.

<!--NI_TOPIC bundle=rfmx-waveform-creator path=selecting-the-window-type.html language=enus -->
## TOPIC 00122: Selecting the Window Type

- bundle_id: `rfmx-waveform-creator`
- source_path: `selecting-the-window-type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/selecting-the-window-type.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: In general, the impulse response of a filter has an infinite length. In practice, this means that the impulse is truncated to the length of the filter. The effect of this is a frequency response that is different to the ideal. Typically, the stop band tends not to be as good. For example, the blue l

### Selecting the Window Type

Root Raised Cosine (Root Nyquist)

[IMAGE alt='image' src='GUID-C7B833BE-64A4-47EB-AC06-6F3AE8937376-a5.png']

Window functions are characterized by their stop band attenuation and their main lobe
 width. The latter characteristic effects the transition width of the filter. RFmx
 Waveform Creator supports the following window types.

- Kaiser Window
- Parabolic Window
- Tapered Rectangle Window

#### Kaiser Window

The Kaiser window function allows you to control the stop band attenuation via the
 β parameter. The higher the value of β, the
 more the attenuation. The more attenuation you have the wider the main lobe and hence
 the wider the transition band. The following figure shows the frequency response of the
 window function for three different β values.

The window function is given by:

[IMAGE alt='image' src='GUID-96CDD396-C53D-45B4-82D0-6E00B29D884F-a5.gif']

where I<sub>o</sub>(x) is the zero-order modified Bessel function of
 the first kind.

#### Parabolic Window

The parabolic window is used in the design of a Tetra filter. In general, it is a good
 window type to use as it provides good stop band attenuation as well as a reasonable
 transition band. The following figure shows the response of a parabolic window that has
 a length of 81 samples.

[IMAGE alt='image' src='GUID-90E2DC4C-17FF-4404-A728-625EA1D1041B-a5.gif']

The parabolic window is given by:

[IMAGE alt='image' src='GUID-3DB684EF-B0F4-47FD-BB01-0578D0C2FEC8-a5.gif']

where N is the length of the window.

#### Tapered Rectangle Window

The tapered rectangle window type provides a means of obtaining evm results that are
 comparable to a rectangular window but with better adjacent channel performance. The
 following figure shows the response of a tapered rectangle window that has a length of
 81 samples.

[IMAGE alt='image' src='GUID-A43DB2CF-92D6-40EB-B464-9DB2B5A6E49F-a5.gif']

The tapered rectangle window is given by:

[IMAGE alt='image' src='GUID-38CE0CBD-F49C-4CE9-9F20-93E1611BE686-a5.gif']

where N is the length of the window,

[IMAGE alt='image' src='GUID-4A7A28B3-02D4-4AF0-9EDD-93F0C714C1C3-a5.gif'] and [IMAGE alt='image' src='GUID-265FC014-2196-4E2D-994D-106FE8F2A680-a5.gif'] denotes rounding to the nearest lowest integer.

<!--NI_TOPIC bundle=rfmx-waveform-creator path=setting-up-pxi-trigger-lines-for-multiple-vst.html language=enus -->
## TOPIC 00123: Setting Up PXI Trigger Lines for Multiple VSTs

- bundle_id: `rfmx-waveform-creator`
- source_path: `setting-up-pxi-trigger-lines-for-multiple-vst.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/setting-up-pxi-trigger-lines-for-multiple-vst.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you are using multiple PXIe-5644, PXIe-5645, or PXIe-5646 RF vector signal transceiver devices, you must create static routes for PXI trigger lines from the master device (source) to the slave devices (destination) using Measurement & Automation Explorer (MAX). For additional information, refer t

### Setting Up PXI Trigger Lines for Multiple VSTs

If you are using multiple PXIe-5644, PXIe-5645, or PXIe-5646 RF vector signal transceiver
 devices, you must create static routes for PXI trigger lines from the master device (source)
 to the slave devices (destination) using Measurement & Automation Explorer
 (MAX). For additional information, refer to the *How Signal Routing
 Works* topic of the RF Signal Generators Help.

To determine the possible static routes between the PXI trigger buses of your chassis, complete the following steps:

1. Launch MAX , either by navigating to Start»All Programs»National
 Instruments»Measurement&Automation or by double-clicking the MAX desktop
 icon.
2. Expand Devices and Interfaces , and then expand the
 Chassis tree.
3. Select your chassis. The attributes of your chassis are displayed on the right of the
 MAX window.
4. Click the Trigger tab below the attributes view. A table in the
 Triggers view shows the PXI trigger bus segments of your
 chassis.
5. Configure the static route that you want to make.
  - To find the bus numbers for the respective devices, verify the slot numbers in which
 the modules are installed in the chassis and the bus number associated with those slots
 in the Bus Mappings Legend of the Trigger 
 tab.
  - The table in the tab gives the routing information about the PXI trigger lines
 ( PXI_Trig0 to PXI_Trig7 ). If a route is left
 unconfigured and available for other products to perform programmatic or automated
 routes to connect devices, the route type is Dynamic .
  - To route a trigger line from the source bus to the destination, select Away
 from source bus as the route type.
6. Save the changes.

For example, assume that there are two VSTs, Dev0 and Dev1, and
 you want to use Dev0 as master device and configure trigger routing from
 Dev0 using MAX.

1. Find the bus numbers associated with the devices. Assume for Dev0 , it is bus 1;
 and for Dev1 , it is bus 3.
2. Assuming all the lines are free and you want to route PXI_Trig1 from bus 1 to
 bus3, change the state of Routing to Away from bus1.
3. Save the changes.

If you are using the *niWLANG RFSG Configure Multiple Device Synchronization VI* for
 multiple RF vector signal transceiver devices, you must configure the PXI trigger lines
 parameter with the routed PXI trigger lines.

Note

Parent topic:

WLAN

<!--NI_TOPIC bundle=rfmx-waveform-creator path=sidelink-configuration.html language=enus -->
## TOPIC 00124: Sidelink Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `sidelink-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/sidelink-configuration.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The sidelink configuration of the LTE FDD modulation tab allows you to control following parameters. This tab is disabled when the Link Direction is set to Uplink or Downlink. Number of Antennas Specifies the number of antennas. Valid value is 1.  PSSCH Data Source Specifies the data payload of the

### Sidelink Configuration

The sidelink configuration of the LTE FDD modulation tab allows you to control following
 parameters.

Note

Link Direction

Uplink

Downlink

Number of Antennas

#### PSSCH

Data Source

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=signal-configuration-overview.html language=enus -->
## TOPIC 00125: Signal Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `signal-configuration-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/signal-configuration-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Generating signal comprises of the following parameters: Link Direction: Specifies the link direction of the signal generated. Frequency Range: Specifies the operating frequency. Range 1: 450 MHz – 6000 MHz Range 2: 24250 MHz – 52600 MHz Number of Tx Antennas: Specifies the number of transmit antenn

### Signal Configuration

Generating signal comprises of the following parameters:

Link Direction: Specifies the link direction of the signal
 generated.

Frequency Range: Specifies the operating frequency.

- Range 1: 450 MHz – 6000 MHz
- Range 2: 24250 MHz – 52600 MHz

Number of Tx Antennas: Specifies the number of transmit
 antennas.

Channel Configuration Mode: Specifies the downlink channel
 configuration setup.

| Test Model | All downlink channels are configured according to the selected test model. |
| --- | --- |
| User Defined | The downlink channels are completely user configurable. |

Note

Channel Configuration Mode

Test
 Model

Number of Frames: Specifies the number of radio frames to be
 generated. Valid values are 1 to 16, inclusive. This parameter is supported only for
 downlink and when Short Frame Generation is disabled.

Number of Carrier Definitions: Specifies the actual carrier
 definition that is visible in the user interface.

For more information about carrier definition setup, refer to the Carrier Definition and
 Carrier sets section in the RFmx Waveform Creator Help.

Auto Increment Cell ID Enabled: Specifies whether Cell ID of
 component carriers is auto calculated during waveform generation.

| Auto Increment Cell ID Enabled | Link Direction/Channel Configuration Mode | Cell ID for Carrier |
| --- | --- | --- |
| False | Any non-Test Model configuration | Uses Cell ID specified in Carrier Definition tab. |
| True | Uplink or Downlink-User Defined | Cell ID of the first carrier is 0. Cell ID is incremented by 1 for each carrier. |

Refer to Cell ID parameter in Carrier
 Definition tab to configure Cell ID manually.

Note

Cell ID

Multi-Carrier

Short Frame Generation: This section enables the user to generate
 a limited number of contiguous slots instead of a full frame.

Note

Enabled: Enables creating a short frame waveform using the
 specified signal offset and signal length parameters.

Signal Length: Specifies the signal length in milliseconds. Valid
 values are 0 to 10 ms in the multiples of 0.125 ms. The shortest allowed length is one
 slot for any configured bandwidth part subcarrier spacing.

When Channel Configuration Mode is
 Test Model

Test Model: Specifies the downlink test model configuration
 according to section 4.9.2 of 3GPP TS 38.141-1 and 3GPP TS
 38.141-2 specifications.

| TM1.1 | Specifies a TM1.1 NR test model. |
| --- | --- |
| TM1.2 | Specifies a TM1.2 NR test model. |
| TM2 | Specifies a TM2 NR test model. |
| TM2a | Specifies a TM2a NR test model. |
| TM2b | Specifies a TM2b NR test model. |
| TM3.1 | Specifies a TM3.1 NR test model. |
| TM3.1a | Specifies a TM3.1a NR test model. |
| TM3.1b | Specifies a TM3.1b NR test model. |
| TM3.2 | Specifies a TM3.2 NR test model. |
| TM3.3 | Specifies a TM3.3 NR test model. |

Duplex Scheme: Specifies the downlink test model duplex mode
 according to section 4.9.2 of 3GPP TS 38.141-1 and 3GPP TS
 38.141-2 specifications.

| FDD | Test models are configured for FDD operation. |
| --- | --- |
| TDD | Test models are configured for TDD operation according to the Table 4.9.2.2-1 of 3GPP TS 38.141 specification. |

Modulation Type: Specifies the modulation type to be used with the
 selected test model. Selecting the modulation type is supported only for test models
 NR-FR2-TM3.1 and NR-FR2-TM2.

| Standard | Generation will use the standard defined modulation type for the test model as specified in 3GPP TS 38.141 (Release 16) specifications. When using this option, test models NR-FR2-TM3.1 and NR-FR2-TM2 will use 64 QAM modulation on PDSCH PRBs. |
| --- | --- |
| QPSK | Use this option to specify QPSK modulation. |
| 16 QAM | Use this option to specify 16 QAM modulation. |
| 64 QAM | Use this option to specify 64 QAM modulation. |

Cell ID Mode: Specifies whether cell ID of downlink test model
 component carriers is auto calculated.

| Auto | Cell ID of each component carriers is auto calculated as specified in the section 4.9.2.3 of 3GPP TS 38.141 specification. |
| --- | --- |
| Manual | Measurement uses the user configured cell IDs. |

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=signal-tree-view-configs.html language=enus -->
## TOPIC 00126: Signal Tree View Configurations

- bundle_id: `rfmx-waveform-creator`
- source_path: `signal-tree-view-configs.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/signal-tree-view-configs.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Pulse RFmx Waveform Creator plugin uses a tree view, displayed on the left window, to encapsulate the signal components into a corresponding hierarchy. Each level in the signal configuration will have their corresponding settings that propagate down the list into the underlying subcomponents.

### Signal Tree View Configurations

The Pulse RFmx Waveform Creator plugin uses a tree view, displayed on the left window, to encapsulate the signal components into a corresponding hierarchy. Each level in the signal configuration will have their corresponding settings that propagate down the list into the underlying subcomponents.

[IMAGE alt='image' src='GUID-17611B6D-5829-4B79-8AB9-760EDBB89C5B-a5.png']

Parent topic:

Creating a Pulse Waveform

<!--NI_TOPIC bundle=rfmx-waveform-creator path=signal-tree-view.html language=enus -->
## TOPIC 00127: Signal Tree View

- bundle_id: `rfmx-waveform-creator`
- source_path: `signal-tree-view.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/signal-tree-view.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The NR RFmx Waveform Creator plugin uses a tree view, displayed on the left window, to encapsulate the signal components into a corresponding hierarchy. Each level in the signal configuration will have their corresponding settings that propagate down the list into the underlying subcomponents. The f

### Signal Tree View

The NR RFmx Waveform Creator plugin uses a tree view, displayed on the left window, to
 encapsulate the signal components into a corresponding hierarchy. Each level in the
 signal configuration will have their corresponding settings that propagate down the list
 into the underlying subcomponents.

[IMAGE alt='image' src='GUID-61A3BD8E-6F8B-4068-B396-2145D5496A41-a5.png']

The following parameters are common across NR modulation:

[IMAGE alt='image' src='GUID-0703762E-07EB-440A-8D60-567F8818273A-a5.png']

Add — Adds a new configuration.

× — Deletes the selected configuration.

+ — Copies the selected configuration and allows you to add new
 configuration with copied configurations.

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=sspbch.html language=enus -->
## TOPIC 00128: SS/PBCH

- bundle_id: `rfmx-waveform-creator`
- source_path: `sspbch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/sspbch.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The SS/PBCH Block is enabled only when you set Link Direction to Downlink and Channel Configuration Mode to User Defined. SS/PBCH block is added to the waveform when you select SSB Enabled. The following controls are configurable only when you select the SSB Enabled check box. If the Number of Tx An

### SS/PBCH

The SS/PBCH Block is enabled only when you set Link Direction to
 Downlink and Channel Configuration
 Mode to User Defined.

SS/PBCH block is added to the waveform when you select SSB
 Enabled. The following controls are configurable only when you select the
 SSB Enabled check box.

If the Number of Tx Antennas is greater than 1, the SS/PBCH is
 configured and applied on all the antenna streams.

SSB Pattern: Specifies the candidate SS/PBCH blocks with different
 subcarrier spacing configurations as defined in the section 4.1 of *3GPP TS 38.213*
 specification.

- Case A refers to 15 kHz subcarrier spacing configuration.
- Case B and C refer to 30 kHz subcarrier spacing configuration.
- Case D refers to 120 kHz subcarrier spacing configuration.
- Case E refers to 240 kHz subcarrier spacing configuration.

Note

SSB Pattern

Case C - upto 3GHz

SSB Pattern

Case C - 3 to
 6GHz

SSB Active Blocks: Specifies the allocation of SS/PBCH blocks
 within one time period. The format is defined in the Range Format Specifiers section.
 Valid SS/PBCH blocks depend on the selected SSB Pattern.

Periodicity: Specifies the time difference with which the SS/PBCH
 block transmit pattern repeats. Valid values are 5 ms, 10 ms, 20 ms, 40 ms, 80 ms, and
 160 ms.

PSS Power: Specifies the power scaling value for the primary
 synchronization symbol in the SS/PBCH block. This value is expressed in dB.

SSS Power: Specifies the power scaling value for the secondary
 synchronization symbol in the SS/PBCH block. This value is expressed in dB.

PBCH Power: Specifies the power scaling value for the PBCH REs in
 the SS/PBCH block. This value is expressed in dB.

PBCH DMRS Power: Specifies the power scaling value for the PBCH
 DMRS symbols in the SS/PBCH block. This value is expressed in dB.

CRB Offset: Specifies the RB offset for the SS/PBCH block relative
 to the resource grid start position.

HRF Index: Specifies the half radio frame in which the SS/PBCH
 block should be allocated. The default value is 0.

| 0 | Specifies that the SS/PBCH block is allocated in the first half of radio frame. |
| --- | --- |
| 1 | Specifies that the SS/PBCH block is allocated in the second half of radio frame. |

Subcarrier Spacing Common: Specifies the basic unit for the
 Subcarrier Offset value. This value applies only for
 frequency range 2 type signals. The value refers to the MIB control element
 subCarrierSpacingCommon in 3GPP TS 38.331.

| 60 kHz | Subcarrier Offset will be in units of 60 kHz. |
| --- | --- |
| 120 kHz | Subcarrier Offset will be in units of 120 kHz. |

Subcarrier Offset: Specifies an additional subcarrier offset for
 the SS/PBCH block relative to the resource grid start position.

Data Source: Specifies the configuration of the payload data in
 the PBCH channel. Refer to Selecting the Data Source in the RFmx Waveform
 Creator Help for more information on standard data source configuration
 window.

Grid Start: Specifies the SSB resource grid start relative to
 Reference Point A in terms of resource block offset.

Grid Size: Specifies the SSB resource grid size when you set the
 Grid Size Mode control to Manual.

Disable PDSCH in SSB Slots: Allows PDSCH to be disabled in all
 those slots where SSB is already allocated.

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=subblock.html language=enus -->
## TOPIC 00129: Subblock

- bundle_id: `rfmx-waveform-creator`
- source_path: `subblock.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/subblock.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: A subblock is a collection of contiguous component carriers used for transmission and reception by the same user equipment (UE). Intra-band contiguous carrier aggregation uses one subblock. Intra-band noncontiguous and inter-band noncontiguous carrier aggregation use two or more subblocks. The follo

### Subblock

A subblock is a collection of contiguous component carriers used for transmission and
 reception by the same user equipment (UE). Intra-band contiguous carrier aggregation
 uses one subblock. Intra-band noncontiguous and inter-band noncontiguous carrier
 aggregation use two or more subblocks.

The following table lists some aggregated bandwidth combinations as defined by the 3GPP
 specification.

| Subblock Component Carriers (MHz) | Aggregated Channel Bandwidth (MHz) | Aggregated Measurement Bandwidth (MHz) |
| --- | --- | --- |
| 10 MHz + 20 MHz | 29.90 | 27.90 |
| 15 MHz + 15 MHz | 30.00 | 28.50 |
| 15 MHz + 20 MHz | 34.85 | 32.85 |
| 20 MHz + 20 MHz | 39.80 | 37.80 |
| 5 MHz + 20 MHz | 24.95 | 22.95 |

The nominal guard band on either side of aggregated carriers is defined in the following
 table,

where, a<sub>1</sub> = 0.16/1.4 for
 BW<sub>Channel(1)</sub> of 1.4 MHz
 a<sub>1</sub> = 0.05 for all other channel bandwidths.

| Maximum Number Of CCs | Nominal Guard Band (At Both Edges Of The Subblock) |
| --- | --- |
| 1 | a1 * BWChannel(1) |
| n (where n > 1) | 0.05 * max(BWChannel(1), BWChannel(2), ...BWChannel(n)) |

For more information about noncontiguous carrier aggregation, refer to Table 5.4.2A-1 in
 the 3GPP TS 36.521-1 specification.

The following image shows two subblocks, subblock A and subblock B, with guard bands
 above and below the edge component carriers to facilitate transmitter/receiver
 filtering.

[IMAGE alt='image' src='GUID-E9500980-42C2-407C-9390-EDC060FBBAA5-a5.gif']

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=supported-hw.html language=enus -->
## TOPIC 00130: Supported Hardware

- bundle_id: `rfmx-waveform-creator`
- source_path: `supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/supported-hw.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports a number of NI devices. 1 RFmx Waveform Creator Hardware RFmx Waveform Creator Hardware Earliest Driver Version Support (Windows 11) PXIe-5644 2022 Q3 PXIe-5645 2022 Q3 PXIe-5646 2022 Q3 PXIe-5673 2022 Q3 PXIe-5673E 2022 Q3 PXIe-5820 2022 Q3 PXIe-5830 2022 Q3 PXIe-5831 2022 Q3 PXIe-583

### Supported Hardware

RFmx supports a number of NI devices.

| RFmx Waveform Creator Hardware | Earliest Driver Version Support (Windows 11) |
| --- | --- |
| PXIe-5644 | 2022 Q3 |
| PXIe-5645 | 2022 Q3 |
| PXIe-5646 | 2022 Q3 |
| PXIe-5673 | 2022 Q3 |
| PXIe-5673E | 2022 Q3 |
| PXIe-5820 | 2022 Q3 |
| PXIe-5830 | 2022 Q3 |
| PXIe-5831 | 2022 Q3 |
| PXIe-5832 | 2022 Q3 |
| PXIe-5840 | 2022 Q3 |
| PXIe-5841 (1 GHz Bandwidth) | 2022 Q3 |
| PXIe-5841 (200 MHz Bandwidth) | 2026 Q2 |
| PXIe-5842 | 2022 Q4 |
| PXIe-5860 | 2022 Q3 |

Note

200 MHz

<!--NI_TOPIC bundle=rfmx-waveform-creator path=symbols.html language=enus -->
## TOPIC 00131: Symbols

- bundle_id: `rfmx-waveform-creator`
- source_path: `symbols.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/symbols.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: β[PUCCH] PUCCH Amplitude Scaling Factor β[SRS] SRS Amplitude Scaling Factor Δ[ss] Delta Sequence Shift Δ[shift]^PUCCH Delta PUCCH Shift n[DMRS]^(1) DMRS Index 1 n[DMRS]^(2) DMRS Index 2 N[CS]^(1) Number of Cyclic Shifts N[ID]^cell Physical Layer Cell Identity n[PUCCH]^(1) Resource Index for PUCCH fo

### Symbols

| βPUCCH | PUCCH Amplitude Scaling Factor |
| --- | --- |
| βSRS | SRS Amplitude Scaling Factor |
| Δss | Delta Sequence Shift |
| ΔshiftPUCCH | Delta PUCCH Shift |
| nDMRS(1) | DMRS Index 1 |
| nDMRS(2) | DMRS Index 2 |
| NCS(1) | Number of Cyclic Shifts |
| NIDcell | Physical Layer Cell Identity |
| nPUCCH(1) | Resource Index for PUCCH formats 1/1a/1b |
| nPUCCH(2) | Resource Index for PUCCH formats 2/2a/2b |
| nRNTI | Radio Network Temporary Identifier |
| NRBDL | Downlink bandwidth configuration, expressed in units of NSCRB |
| NRBUL | Uplink bandwidth configuration, expressed in units of NSCRB |
| NSCRB | Resource block size in the frequency domain, expressed as a number of subcarriers |
| NRB(2) | Number of Resource Blocks Reserved for PUCCH 2/2a/2b |
| NRBHO | PUSCH Frequency Hopping Offset |
| Nsb | Number of Sub-bands |
| MRBPUSCH | Number of PUSCH Resource Blocks |
| NRBGUL | Number of PUSCH Resource Block Groups |

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=system-requirements.html language=enus -->
## TOPIC 00132: RFmx Waveform Creator System Requirements

- bundle_id: `rfmx-waveform-creator`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/system-requirements.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Waveform Creator has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory ma

### RFmx Waveform Creator System Requirements

RFmx Waveform Creator has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-waveform-creator path=system-requirements_2.html language=enus -->
## TOPIC 00133: RFmx Waveform Creator System Requirements

- bundle_id: `rfmx-waveform-creator`
- source_path: `system-requirements_2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/system-requirements_2.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Waveform Creator has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory ma

### RFmx Waveform Creator System Requirements

RFmx Waveform Creator has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-waveform-creator path=td-scdma-3gpp-tdd-lcr.html language=enus -->
## TOPIC 00134: TD-SCDMA (3GPP TDD-LCR)

- bundle_id: `rfmx-waveform-creator`
- source_path: `td-scdma-3gpp-tdd-lcr.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/td-scdma-3gpp-tdd-lcr.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creates a waveform that simulates a 3GPP TDD-LCR carrier. This document assumes that you know how to package and download files to an instrument. For more information about packaging and downloading files to an instrument, refer to Generating and Saving the Waveform File.

### TD-SCDMA (3GPP TDD-LCR)

Creates a waveform that simulates a 3GPP TDD-LCR carrier.

Note

Generating and Saving the Waveform
 File

Parent topic:

RFmx Waveform Creator Modulation Schemes

Related information:

- RFmx TD-SCDMA .NET Reference
- RFmx TD-SCDMA C API Reference

<!--NI_TOPIC bundle=rfmx-waveform-creator path=test-models.html language=enus -->
## TOPIC 00135: Test Models

- bundle_id: `rfmx-waveform-creator`
- source_path: `test-models.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/test-models.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx Waveform Creator supports the following downlink test models. E-UTRA Test Model 1.1 (E-TM1.1) E-UTRA Test Model 1.2 (E-TM1.2) E-UTRA Test Model 2 (E-TM2) E-UTRA Test Model 2a (E-TM2a) E-UTRA Test Model 2b (E-TM2b) E-UTRA Test Model 3.1 (E-TM3.1) E-UTRA Test Model 3.1a (E-TM3.1a) E-UTRA Test Mod

### Test Models

RFmx Waveform Creator supports the following downlink test models.

- E-UTRA Test Model 1.1 (E-TM1.1)
- E-UTRA Test Model 1.2 (E-TM1.2)
- E-UTRA Test Model 2 (E-TM2)
- E-UTRA Test Model 2a (E-TM2a)
- E-UTRA Test Model 2b (E-TM2b)
- E-UTRA Test Model 3.1 (E-TM3.1)
- E-UTRA Test Model 3.1a (E-TM3.1a)
- E-UTRA Test Model 3.1b (E-TM3.1b)
- E-UTRA Test Model 3.2 (E-TM3.2)
- E-UTRA Test Model 3.3 (E-TM3.3)

If multiple carriers are configured with ETMs, the cell ID is incremented by 1 for each
 additional configured carrier. For more information about the ETM models, refer to
 section 6.1.2 of 3GPP TS 36.141 specification.

To configure test models, select an option from the Test Model
 drop-down menu. The default value is None.

RFmx Waveform Creator will configure all the necessary parameters as defined in section
 6.1 of the 3GPP TS 36141 specification.

Note

SSB Pattern

Case C - upto 3GHz

SSB Pattern

Case C - 3 to
 6GHz

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=transmission.html language=enus -->
## TOPIC 00136: Transmission

- bundle_id: `rfmx-waveform-creator`
- source_path: `transmission.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/transmission.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: GSM/EDGE modulation does not support frequency hopping, all the slots are transmitted on the same frequency, the transmission order of the slots is slot-0, slot-1 ...slot-0. The slot transmission with frequency hopping is shown in the following figure.

### Transmission

GSM/EDGE modulation does not support frequency hopping, all the slots are transmitted on
 the same frequency, the transmission order of the slots is slot-0, slot-1 ...slot-0. The
 slot transmission with frequency hopping is shown in the following figure.

[IMAGE alt='image' src='GUID-55A8C084-42E1-4AF4-82BE-B70917954DE2-a5.gif']

Parent topic:

GSM/EDGE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=trigger-frame-generation.html language=enus -->
## TOPIC 00137: Trigger Frame Generation

- bundle_id: `rfmx-waveform-creator`
- source_path: `trigger-frame-generation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/trigger-frame-generation.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The multi-user transmission (both OFDMA and MU MIMO) on uplink in 802.11ax (HE) is initiated by a trigger frame from an Access Point Station (AP STA), as shown in the following figure.As specified in standard IEEE P802.11ax/D8.0; the trigger frame contains all the user related information, and commo

### Trigger Frame Generation

The multi-user transmission (both OFDMA and MU MIMO) on uplink in 802.11ax (HE) is initiated by a trigger frame from an Access Point Station (AP STA), as shown in the following figure.

[IMAGE alt='image' src='GUID-4D99BC6F-825D-4884-9CD3-3BECA742581B-a5.gif']

As specified in standard IEEE P802.11ax/D8.0; the trigger frame contains all the user related
 information, and common information across users. The following figure depicts the
 format of the trigger frame.

[IMAGE alt='image' src='GUID-E8B2186C-2A6D-4A77-9835-8FFB2BD91F6D-a5.gif']

[IMAGE alt='image' src='GUID-286EDF9D-FEF3-4344-971A-91D0D89493F9-a5.gif']

The following list contains subfields and values of the Common Information
 Field:

Trigger Type

UL Length

/NIWLANG_L_SIG_LENGTH

More TF

CS Required

/NIWLANG_CS_REQUIRED

UL BW

/NIWLANG_CHANNEL_BANDWIDTH

GI And LTF Type

- Guard Interval Type /NIWLANG_GUARD_INTERVAL_TYPE
- HE-LTF Size /NIWLANG_HE_LTF_SIZE .

MU-MIMO LTF Mode

/NIWLANG_MU_MIMO_LTF_MODE_ENABLED

Number of HE-LTF Symbols and Midamble Periodicity

/NIWLANG_NUMBER_OF_HE_LTF_SYMBOLS

/NIWLANG_MIDAMBLE_PERIODICITY

UL STBC

/NIWLANG_STBC_ALL_STREAMS_ENABLED

LDPC Extra Symbol Segment

/NIWLANG_LDPC_EXTRA_SYMBOL_SEGMENT

AP Tx Power

/NIWLANG_TRIGGER_FRAME_AP_TXP

UL Packet Extension

- Pre-FEC Padding Factor
 property /NIWLANG_PRE_FEC_PADDING_FACTOR 
 attribute
- PE Disambiguity property /NIWLANG_PE_DISAMBIGUITY 
 attribute.

UL Spatial Reuse

Doppler

/NIWLANG_MIDAMBLE_PERIODICITY

/NIWLANG_VAL_NONE

UL HE-SIG-A2 Reserved

Reserved

The following list contains subfields and values of the User Information
 Field:

AID12

/NIWLANG_AID12

RU Allocation

/NIWLANG_RU_SIZE and
 NIWLANG_RU_OFFSET

UL FEC Coding Type

/NIWLANG_FEC_CODING_TYPE

UL MCS

/NIWLANG_MCS_INDEX

UL DCM

SS Allocation

- Number of Space Time Streams
 property /NIWLANG_NUMBER_OF_SPACE_TIME_STREAMS 
 attribute
- Space Time Stream Offset
 property /NIWLANG_SPACE_TIME_STREAM_OFFSET 
 attribute.

UL Target RSSI

/NIWLANG_TRIGGER_FRAME_TARGET_RSSI

Reserved

Trigger Dependent User Info

To generate a trigger frame using the NI WLAN Generation Toolkit APIs, you must use two
 generation toolkit sessions. One session to configure the trigger frame content and
 another one for transmit PHY. The transmit PHY could be one of the OFDM standards
 802.11a/g, 802.11n, 802.11ac, or 802.11ax.

You must complete the following steps to create the trigger frame MSDU bits.

1. Configure the first session for 802.11ax Trigger-based PPDU.
2. Enter the common settings such as bandwidth, GI, etc., directly to the session.
3. Configure the payload parameters on the session to derive the other common
 parameters such as L-SIG Length, Pre-FEC Padding factor, etc. Or configure L-SIG
 Length, Pre-FEC Padding Factor, PE Disambiguity, and LDPC Extra Symbol Segment
 directly.
4. Configure the per user information such as MCS index, RU allocation etc. with the
 “userx” active channel.
5. Call the niWLANG Create Trigger Frame MSDU Bits VI or
 niWLANG_CreateTriggerFrameMSDUBits function to create the bits.

After completing the creation steps, generate the trigger frame by completing the following
 steps.

1. Configure the second session to any one of the OFDM standards: 802.11a/g, 802.11n, 802.11ac, or 802.11ax.
2. Configure the session to generate user-defined bit pattern.
3. Input the MSDU bits created by the first session to the current session as a user-defined bit pattern.
4. Configure MAC Frame Type as Trigger Frame.
5. Configure the MAC Header settings and MAC Padding Duration (s).
6. Call the niWLANG RFSG Create and Download Waveforms VI, or niWLANG_RFSGCreateAndDownloadWaveform/niWLANG_RFSGCreateAndDownloadMIMOWaveforms functions to generate the Trigger Frame waveform.

An example demonstrating the creation and the generation of trigger frame is located at: LabVIEW\examples\RF Toolkits\WLAN\generation\Basic or Documents\National Instruments\WLAN Toolkit\Examples\C\Generation

Parent topic:

WLAN

<!--NI_TOPIC bundle=rfmx-waveform-creator path=uplink-config.html language=enus -->
## TOPIC 00138: Uplink Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `uplink-config.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/uplink-config.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Uplink Configuration tab allows you to control the uplink signal that is not configured on a subframe basis. The Uplink Configuration tab is disabled when you set the Link Direction to Downlink or Sidelink.

### Uplink Configuration

The Uplink Configuration tab allows you to control the uplink signal that is not
 configured on a subframe basis.

Note

Link Direction

Downlink

Sidelink

- [Mode: LTE](uplink-mode-lte.html) Uplink configuration options for LTE (Long-Term Evolution) transmissions.
- [Mode: eMTC](uplink-mode-emtc.html) Uplink configuration options for eMTC (Enhanced Machine-Type Communication) transmissions.
- [Mode: NB-IoT](mode-nb-iot.html) Uplink configuration options for narrow band internet of things (NB-IoT) transmissions.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=uplink-configuration-lte.html language=enus -->
## TOPIC 00139: Uplink Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `uplink-configuration-lte.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/uplink-configuration-lte.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The uplink configuration allows you to control the uplink signal that is not configured on a subframe basis. This tab is disabled when the Link Direction is set to Downlink. RNTI: Specifies the RNTI of the Uplink signal. The range is 0 to 65535. The default value is 0. Generation Mode: Specifies tha

### Uplink Configuration

The uplink configuration allows you to control the uplink signal that is not configured
 on a subframe basis.

Note

Link Direction

Downlink

RNTI: Specifies the RNTI of the Uplink signal. The range is 0
 to 65535. The default value is 0.

Generation Mode: Specifies that uplink of the frame contains
 traffic data.

Number of Antennas: When Uplink MIMO is configured,

- For PUSCH , the number of codewords/layers is equal to 2
 and the precoding index value equals zero. DTX for a single codeword is not
 supported.

Channel Coder: Selecting this checkbox enables the channel
 encoding. Channel coding is disabled when the Modulation Type
 is set to QAM 1024.

PUSCH Configuration

This tab contains the following configuration parameters specific to the PUSCH portion of
 the uplink signal.

N1 DMRS: Specifies the cell specific DMRS cyclic shift. This
 can take a value of {0,2,3,4,6,8,9,10}. The default is 0.

Delta Shift Sequence: Configures the Delta Shift sequence used
 when performing group hopping. The valid range is 0 to 29. The default value is
 0.

HARQ Offset: Used to determine the
 β<sub>offset</sub><sup>HARQ-ACK</sup> parameter. See table of 3GPP TS
 36.213 V8.8.0 (2009-09). The valid range is 0 to 14. The default value
 is 1.

Subframe Hopping: Specifies whether the hopping is inter
 subframe or intra and inter subframe.

Auto Calculate DAI: Specifies whether the Downlink Assignment
 Index should be automatically calculated or not.

Number of Sub-bands: Specifies the number of sub-bands used in
 PUSCH Hopping. The valid values are 0, 1, 2, 3, or 4. The default value is 1.

Data Source: Specifies the data payload of the PUSCH channel.
 Refer to Selecting the Data Source topic for more information on data source.

Hopping Offset: Used in PUSCH hopping. The valid range is 0 to
 98. The default value is 0.

DMRS Configuration

This tab contains configuration parameters specific to the DMRS portion of the Uplink
 Signal.

Group Hopping: Enables DMRS group hopping.

Sequence Hopping: Enables the DMRS sequence hopping.

HARQ Configuration

Codeword1 Ack/Nack Pattern: Allows you to specify the pattern
 of Ack/Nack bits used within the HARQ codeword 1. To use this control, press 1 for
 On, 0 for Off, or D for
 DTX.

Codeword2 Ack/Nack Pattern: Allows you to specify the pattern
 of Ack/Nack bits used within the HARQ codeword2. To use this control, press 1 for
 On, 0 for Off, or D for
 DTX.

Multicarrier Harq Operation: When this checkbox is selected,
 PUCCH considers Table 10.1.3.5, Table 10.1.3.6, and Table 10.1.3.7as defined in
 document 3GPP TS 36213, V12.5.0 specification.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=uplink-configuration-overview.html language=enus -->
## TOPIC 00140: Uplink Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `uplink-configuration-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/uplink-configuration-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This tab allows you to control the uplink signal that is not configured on a subframe basis. Select Physical Channel: Specifies the channel type. Channel Config: Enables you to select different channel configuration cases. Valid values are Case 1, Case 2, and Case 3. Compressed Mode: Enables the com

### Uplink Configuration

This tab allows you to control the uplink signal that is not configured on a subframe
 basis.

Select Physical Channel: Specifies the channel type.

Channel Config: Enables you to select different channel
 configuration cases. Valid values are Case 1, Case 2, and Case 3.

Compressed Mode: Enables the compressed mode. Refer to Compressed Mode for more information.

Configure: Enables you to configure the compressed mode
 values.

Scrambling Code: Specifies the scrambling code number. It is used
 to define the seed of the scrambling code generators.

Scrambling Type: Specifies the scrambling type. In the uplink, you
 can use either a long or short scrambling code.

Parent topic:

WCDMA (3GPP FDD Release 8)

Related concepts:

- Compressed Mode

<!--NI_TOPIC bundle=rfmx-waveform-creator path=uplink-frc-configuration.html language=enus -->
## TOPIC 00141: Uplink FRC Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `uplink-frc-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/uplink-frc-configuration.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enter a short description of your concept here (optional). Using this window, you can configure uplink FRCs (for base station receiver tests) according to Annex A of 3GPP TS 38.141-1, 3GPP TS 38.141-2 and 3GPP TS 38.181 specifications. TBoMS is not supported in FRC type A.3. DMRS Frequency Range FRC

### Uplink FRC Configuration

Enter a short description of your concept here (optional).

Using this window, you can configure uplink FRCs (for base station receiver tests) according to Annex A of 3GPP TS 38.141-1, 3GPP TS 38.141-2 and 3GPP TS 38.181 specifications.

Note

#### DMRS

| Frequency Range | FRC Types | DMRS Additional Position |
| --- | --- | --- |
| Frequency Range 1 | A.3, A.4 and A.7 | 1 and 2 |
|  | A.3B | 0 and 1 |
|  | A.1, A.2, A.3A, A.5, A.8, A.9, A.12 and NTN A.3 | 1 |
| Frequency Range 2 | A.3, A.3A, A.4, A.5, A.7, and A.10 | 0 and 1 |
|  | A.1, A.3B, NTN A.5 and NTN A.6 | 1 |

#### Transform Precoding

| Frequency Range | FRC Types | Transform Precoding |
| --- | --- | --- |
| Frequency Range 1 | A.3 and NTN A.3 | Supported |
|  | Others | Not supported |
| Frequency Range 2 | A.3 and NTN A.5 | Supported |
|  | Others | Not supported |

#### Number of Tx Antennas

| Frequency Range | FRC Types | Tx Antennas |
| --- | --- | --- |
| Frequency Range 1 | A.3, A.4, A.9 and A.12 | 1, 2 and 4 |
|  | Others | 1 |
| Frequency Range 2 | A.3, A.4, and A.7 | 1 and 2 |
|  | Others | 1 |

#### PUSCH Mapping Type

| Frequency Range | FRC Types | PUSCH Mapping Type |
| --- | --- | --- |
| Frequency Range 1 | A.3, A.3A, A.3B, NTN A.3, A.4, A.5, A.7, A.8, A.9 and A.12 | Type A and Type B |
|  | A.1 and A.2 | Type A |
| Frequency Range 2 | A.1 | Type A |
|  | A.3, A.3A, A.3B, NTN A.5, NTN A.6, A.4, A.5, A.7, and A.10 | Type B |

#### PTRS Enabled

| Frequency Range | FRC Types | PTRS Enabled |
| --- | --- | --- |
| Frequency Range 1 | All | Not supported |
| Frequency Range 2 | A.1, A.3, A.3A, A.3B, NTN A.5 and NTN A.6 | Not supported |
|  | A.4, A.5, A.7, and A.10 | Supported |

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=uplink-mode-emtc.html language=enus -->
## TOPIC 00142: Mode: eMTC

- bundle_id: `rfmx-waveform-creator`
- source_path: `uplink-mode-emtc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/uplink-mode-emtc.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Uplink configuration options for eMTC (Enhanced Machine-Type Communication) transmissions. The following uplink configuration options are available for a LTE transmission, when Link Direction is Uplink and Mode is eMTC. Uplink Configuration RNTI Specifies the RNTI of the Uplink signal. The range is

### Mode: eMTC

Uplink configuration options for eMTC (Enhanced Machine-Type Communication)
 transmissions.

The following uplink configuration options are available for a LTE transmission, when
 Link Direction is Uplink and
 Mode is eMTC.

#### Uplink
 Configuration

RNTI

#### PUSCH
 Configuration

This tab contains the following configuration parameters
 specific to the PUSCH portion of the uplink signal.

N1 DMRS

Delta Shift Sequence

Data Source

Selecting the Data Source

#### DMRS
 Configuration

This tab contains configuration parameters specific to the
 DMRS portion of the uplink signal.

Group Hopping

Sequence Hopping

Parent topic:

Uplink Configuration

Related concepts:

- Selecting the Data Source

<!--NI_TOPIC bundle=rfmx-waveform-creator path=uplink-mode-lte.html language=enus -->
## TOPIC 00143: Mode: LTE

- bundle_id: `rfmx-waveform-creator`
- source_path: `uplink-mode-lte.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/uplink-mode-lte.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Uplink configuration options for LTE (Long-Term Evolution) transmissions. The following uplink configuration options are available for a LTE transmission, when you set the Link Direction to Uplink and Mode to LTE. Uplink Configuration RNTI Specifies the RNTI of the Uplink signal. The range is 0 to 6

### Mode: LTE

Uplink configuration options for LTE (Long-Term Evolution) transmissions.

The following uplink configuration options are available for a LTE transmission, when you
 set the Link Direction to Uplink and
 Mode to LTE.

#### Uplink Configuration

RNTI

Generation Mode

Generation Mode

PRACH

Generation Mode

Traffic

PRACH

Traffic

Number of Antennas

- For PUSCH , the number of codewords/layers is
 equal to 2 and the precoding index value equals zero. DTX for a
 single codeword is not supported.
- For PUCCH , each antenna will carry the signal
 corresponding to its
 n PUCCH (1) value as per
 3GPP 36.213 specification. Note SRS is mapped
 only on the first antenna even if 2 antennas are configured, but
 the PUSCH/PUCCH will exclude the last SC-FDMA symbol in a
 subframe in both antennas.

Channel Coder

Modulation Type

QAM
 1024

#### PUSCH Configuration

This tab contains the following configuration
 parameters specific to the PUSCH portion of the uplink signal.

N1 DMRS

Modulation Mode

MCS Index

User Defined

MCS
 Index

Note

Modulation Mode

User Defined

Delta Sequence Shift

HARQ Offset

offset

HARQ-ACK

3GPP TS 36.213 V8.8.0 (2009-09)

Subframe Hopping

Auto Calculate DAI

Number of Sub Bands

Data Source

Hopping Offset

#### PUCCH Configuration

This tab contains
 configuration parameters specific to the PUCCH portion of the uplink signal.

N1

Delta Shift

N1SRI

SR Configuration Index

N2

Simultaneous Ack Nack and SRS

N2 Resource Blocks

Transmit Scheduling Request

Transmit Scheduling Request

Number of Cyclic Shifts

Auto Calculate Format

#### PRACH Configuration

This tab contains controls for specifying how the
 PRACH channel will be transmitted.

Configuration Index

3GPP TS 36.211 V8.9.0 (2009-12)

Cyclic Shift Configuration

N

CS

3GPP TS 36.211
 V8.9.0 (2009-12)

Format

Preamble Index

Root Sequence Number

3GPP TS 36.211 V8.9.0
 (2009-12)

Mask Index

High Speed

True

Frequency Offset

Doppler Offset

#### DMRS Configuration

This tab contains
 configuration parameters specific to the DMRS portion of the uplink signal.

Group Hopping

Sequence Hopping

#### SRS
 Configuration

This tab contains configuration parameters specific to the
 SRS portion of the uplink signal.

Enabled

Subframe Configuration

3GPP TS 36.211 V8.9.0 (2009-12)

Cell Specific B/W Config (C_SRS)

C

SRS

U/E Specific B/W (B_SRS)

B

SRS

U/E Specific B/W (B_SRS)

B

SRS

Configuration Index (I_SRS)

SRS

3GPP TS 36.213 V8.8.0 (2009-09)

Hopping Bandwidth (b_hop)

b

hop

Cyclic Shift (n_SRS_CS)

SRS

cs

Frequency Domain Position (n_RRC)

n

RRC

Transmission Comb(k_TC)

k

TC

Power

#### HARQ
 Configuration

CodeWord1 AckNackPattern

On

Off

DTX

CodeWord2 AckNackPattern

On

Off

DTX

Multicarrier Harq Operation

3GPP TS 36213,
 V12.5.0

Parent topic:

Uplink Configuration

<!--NI_TOPIC bundle=rfmx-waveform-creator path=uplink-narrowband-internet-of-things-overview.html language=enus -->
## TOPIC 00144: Uplink Narrowband Internet of Things Overview

- bundle_id: `rfmx-waveform-creator`
- source_path: `uplink-narrowband-internet-of-things-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/uplink-narrowband-internet-of-things-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Narrowband-internet of things (NB-IoT) is introduced in Release 13 of LTE 3GPP specification as a part of LTE Advanced Pro. NB-IoT is a low power wide area (LPWA) technology developed to cater to the needs of IoT devices. Its emphasis is on low cost and long battery life of the IoT devices and on le

### Uplink Narrowband Internet of Things Overview

Narrowband-internet of things (NB-IoT) is introduced in Release 13 of LTE
 3GPP specification as a part of LTE Advanced Pro. NB-IoT is a low power
 wide area (LPWA) technology developed to cater to the needs of IoT devices. Its emphasis
 is on low cost and long battery life of the IoT devices and on leveraging the existing
 LTE and GSM infrastructure. For NB-IoT, only half duplex FDD operation is supported.

Physical Structure

The bandwidth of an uplink NB-IoT carrier is fixed to 200 kHz with 180 kHz as the
 transmission bandwidth and 10 kHz as the guard-band on either side. Uplink NB-IoT uses
 single-carrier frequency-division multiple access (SC-FDMA) transmission scheme and has
 7 symbols in each slot. The subcarrier spacing can be either 15 kHz or 3.75 kHz. Per
 SC-FDMA symbol, there are 12 subcarriers with 15 kHz spacing or 48 subcarriers with 3.75
 kHz spacing (180 kHz/15 kHz or 180 kHz/3.75 kHz).

There are differences in the time domain structure of an NB-IoT uplink carrier, based on
 subcarrier spacing.

For 15 kHz subcarrier spacing, each slot is of 0.5 ms duration and has 7 SC-FDMA symbols
 in each slot as depicted in the following figure.

[IMAGE alt='image' src='GUID-1FA6AD19-4456-49DB-8515-5EE085795FF9-a5.gif']

For 3.75 kHz subcarrier spacing, each slot is 2 ms. While it still has 7 SC-FDMA symbols,
 the cyclic prefix duration of each symbol is such that there is a 2304 Ts gap at the end
 of every slot as depicted in the following figure.

[IMAGE alt='image' src='GUID-ECE93B6D-73F0-4C46-A83D-DC20BEB1DE9F-a5.gif']

Note

- Ts is the sampling time when sampling rate is 30.72 MHz.
- When the subcarrier spacing is 15 kHz, for symbol 0, the cyclic prefix duration
 is 160Ts. Therefore, the duration of symbol 0 is slightly more than the rest of
 the symbols at 71.88 us.

For uplink NB-IoT a new type of allocation, called resource unit, is defined to describe
 the mapping of the NPUSCH to resource elements.

Resource unit is the basic unit of narrowband physical uplink shared channel (NPUSCH)
 allocation in NB-IoT. A resource unit has
 N<sup>UL</sup><sub>Symb</sub>
 *
 N<sup>UL</sup><sub>Slots</sub>
 consecutive SC-FDMA symbols in the time domain and
 N<sup>RU</sup><sub>SC</sub> consecutive
 subcarriers in the frequency domain.
 N<sup>UL</sup><sub>Slots</sub>
 and N<sup>RU</sup><sub>SC</sub> are as specified
 in the following table.

| NPUSCH Format | Δf | N RU sc | N UL slots | N UL symb |
| --- | --- | --- | --- | --- |
| 1 | 3.75 kHz | 1 | 16 | 7 |
| 15 kHz | 1 | 16 |  |  |
| 3 | 8 |  |  |  |
| 6 | 4 |  |  |  |
| 12 | 2 |  |  |  |
| 2 | 3.75 kHz | 1 | 4 |  |
| 15 kHz | 1 | 4 |  |  |

Note

- N UL Symb 
 is the number of symbols in an uplink slot.
- N UL Slots 
 is the number of consecutive slots in an uplink resource unit for NB-IoT.
- N RU SC is the number
 of consecutive subcarriers in an uplink resource unit for NB-IoT.
- Δ f is the subcarrier spacing.

Narrowband Physical Uplink Shared Channel

The NPUSCH supports two formats.

- Format 1 is used to carry uplink shared channel (UL-SCH) which contains actual user
 data.
- Format 2 is used to carry uplink control information.

As seen in the preceding table, multi-tone configurations are allowed only for NPUSCH
 Format 1 with 15 kHz subcarrier spacing.

Modulation of NPUSCH

The following table specifies the modulation schemes applicable for the NPUSCH
 channel.

| NPUSCH Format | N sc RU | Modulation Scheme |
| --- | --- | --- |
| 1 | 1 | BPSK, QPSK |
| >1 | QPSK |  |
| 2 | 1 | BPSK |

Demodulation Reference Signal

Based on NPUSCH format and subcarrier spacing, demodulation reference signal (DMRS)
 symbols can be at different positions in a slot and each slot can contain multiple DMRS
 symbols. The following table specifies the DMRS locations in a slot.
 l specifies the symbol index number in an NPUSCH slot.

| NPUSCH Format | Values for l |  |
| --- | --- | --- |
| Δf = 3.75 kHz | Δf = 15 kHz |  |
| 1 | 4 | 3 |
| 2 | 0, 1, 2 | 2, 3, 4 |

The following figure depicts the DMRS symbols in a slot. DMRS symbols are
 highlighted.

[IMAGE alt='image' src='GUID-9E275BA3-213E-4507-BF4D-21652F99E62F-a5.gif']

Subcarrier Indication Field

Subcarrier indication field (I<sub>sc</sub>), in uplink DCI format N0,
 is a 6-bit unsigned integer with values ranging from 0 to 63. It determines the set of
 contiguously allocated subcarriers (n<sub>sc</sub>) in the resource unit of NB-IoT.

3.75 kHz Subcarrier Spacing

When Δf = 3.75 kHz, n<sub>sc</sub> =
 I<sub>sc</sub>. This implies only a single tone can be
 transmitted when subcarrier spacing is 3.75 kHz. Refer to the table in section.

In RFmx Waveform Creator, you cannot set the I<sub>sc</sub>; instead
 you need to set the values of the NPUSCH Tone Offset and NPUSCH Number of Tones
 properties to specify where the tone is placed.

For example, if I<sub>sc</sub> = 25, it implies a tone is transmitted
 at 25<sup>th</sup> index out of the available 48 indexed subcarrier locations starting
 from 0<sup>th</sup> index. In RFmx Waveform Creator, the equivalent configuration would
 be to set NPUSCH Tone Offset to 25 and NPUSCH Number of Tones to 1.

Note

I

sc

15 kHz Subcarrier Spacing

For 15 kHz subcarrier spacing, the subcarrier indication field
 (I<sub>sc</sub>) determines the set of contiguously allocated
 subcarriers (n<sub>sc</sub>) according to the following table.

| Subcarrier Indication Field (Isc) | Set of Allocated Subcarriers (nsc) |
| --- | --- |
| 0-11 | I sc |
| 12-15 | 3(Isc-12) + {0,1,2} |
| 16-17 | 6(Isc - 16) + {0,1,2,3,4,5} |
| 18 | {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} |
| 19-63 | Reserved |

The following table specifies the relationship of I<sub>sc</sub> with
 NPUSCH Tone Offset and NPUSCH Number of Tones.

| Subcarrier Indication Field (Isc) | NPUSCH Tone Offset | NPUSCH Number of Tones |
| --- | --- | --- |
| 0-11 | I sc | 1 |
| 12 | 0 | 3 |
| 13 | 3 | 3 |
| 14 | 6 | 3 |
| 15 | 9 | 3 |
| 16 | 0 | 6 |
| 17 | 6 | 6 |
| 18 | 0 | 12 |
| 19-63 | Undefined | Undefined |

Note

- In RFmx Waveform Creator, to select NB-IoT mode, you need to set the
 Mode control to NB_IoT .
- In RFmx Waveform Creator, carrier aggregation of more than one NB-IoT carrier is
 not supported.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=user-configuration-overview.html language=enus -->
## TOPIC 00145: User Configuration

- bundle_id: `rfmx-waveform-creator`
- source_path: `user-configuration-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/user-configuration-overview.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section contains the following configuration parameters. Uplink Number of PUSCH Configurations: Specifies the actual PUSCH configuration that is visible in the user interface. nRNTI: Specifies the radio network temporary identifier of the uplink signal. The range is 0 to 65535. The default valu

### User Configuration

This section contains the following configuration parameters.

Uplink

Number of PUSCH Configurations: Specifies the actual PUSCH
 configuration that is visible in the user interface.

nRNTI: Specifies the radio network temporary identifier of the
 uplink signal. The range is 0 to 65535. The default value is 1.

Data Source: Specifies the configuration of the payload data
 in the PUSCH channel. Refer to Selecting the Data Source topic for more information
 on data source.

Downlink

Number of PDSCH Configurations: Specifies the actual PDSCH
 configuration that is visible in the user interface.

Number of Codewords: Specifies the actual number of codewords
 configured per user and will vary based on Number of Tx
 Antennas value.

Data Source/Data Source CW0: Specifies the configuration of
 the payload data in the first Codeword of the PDSCH channel. Refer to Selecting the
 Data Source topic for more information on data source.

Data Source CW1: Specifies the configuration of the payload
 data in the second Codeword of the PDSCH channel. This parameter is available when
 number of antennas is greater than 4.

nRNTI: Specifies the radio network temporary identifier of the
 downlink signal. The range is 0 to 65535. The default value is 1.

Parent topic:

NR

<!--NI_TOPIC bundle=rfmx-waveform-creator path=user-manual-welcome.html language=enus -->
## TOPIC 00146: RFmx Waveform Creator User Manual

- bundle_id: `rfmx-waveform-creator`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx Waveform Creator User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx Waveform Creator
 User Manual

The RFmx Waveform Creator User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx Waveform Creator
- Interactive Activation Guide
- RFmx Waveform Creator Release Notes
- RFmx User Manual
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=rfmx-waveform-creator path=v2x-sidelink-communication.html language=enus -->
## TOPIC 00147: V2X Sidelink Communication

- bundle_id: `rfmx-waveform-creator`
- source_path: `v2x-sidelink-communication.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/v2x-sidelink-communication.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: LTE V2X sidelink communication is introduced as sidelink transmission mode 3 and mode 4 in the Release 14 of 3GPP specification. V2X sidelink communication is used for direct communication between vehicle to everything. V2X comprises of vehicle-to-vehicle (V2V) communications, vehicle-to-infrastruct

### V2X Sidelink Communication

LTE V2X sidelink communication is introduced as sidelink transmission mode 3 and mode 4
 in the Release 14 of 3GPP specification. V2X sidelink communication is used for direct
 communication between vehicle to everything. V2X comprises of vehicle-to-vehicle (V2V)
 communications, vehicle-to-infrastructure (V2I) communications, vehicle-to-pedestrian
 (V2P) communications.

V2X sidelink communication is used for low-latency safety services and out of coverage
 operations. It supports half duplex frequency division duplex (HD-FDD) operations as
 well as 10 MHz and 20 MHz channel bandwidths.

#### Physical Structure

Sidelink uses the single-carrier
 frequency-division multiple access (SC-FDMA) transmission scheme. It consists of 14
 symbols in each subframe.

Note

#### Guard Symbol

The last SC-FDMA symbol in a
 sidelink subframe serves as a guard period and hence not used for sidelink
 transmission.

#### Physical Channels

Physical sidelink
 shared channel (PSSCH) is used to carry sidelink data. Supported modulation schemes
 are QPSK, 16QAM, and 64QAM.

Physical sidelink control channel (PSCCH) is used
 to carry sidelink control information (SCI). SCI Format 1 consists of PSSCH
 transmission information and it is transmitted in two consecutive resource blocks
 (RBs). For more information on PSCCH, refer to section 5.4.3.1 of 3GPP
 36.212 specification.

PSSCH and PSCCH can be transmitted in
 adjacent RBs or non-adjacent RBs. For more information on allocations, refer to
 section 14.1.1.4C and section 14.2.4 of 3GPP 36.213
 specification. Both allocations types are illustrated in the following
 figure.

[IMAGE alt='image' src='GUID-D34F6F37-43B3-484F-861A-C3F0D1F2658F-a5.png']

#### Demodulation Reference Signal

PSSCH
 demodulation reference signal (DMRS) and PSCCH DMRS are transmitted in 4 symbols per
 subframe. DMRS is transmitted on symbols 2, 5, 8, and 11 of a subframe as
 highlighted in the following figure. For more information on DMRS, refer to section
 9.8 of the 3GPP 36.211 specification.

[IMAGE alt='image' src='GUID-BF8ABBF0-0991-4111-A48F-161974D0E867-a5.png']

#### Retransmission

Data and control
 information transmitted in a subframe can be retransmitted. Frequency allocation and
 subframe time gap between initial transmission and retransmission can be varied. For
 more information on retransmission, refer to section 14.1.1.4C of 3GPP
 36.213 specification.

Note

- In RFmx Waveform Creator, set the Link Direction to
 Sidelink in LTE FDD to select sidelink.
- In RFmx Waveform Creator, carrier aggregation of sidelink and other link
 direction carriers are not allowed.

Parent topic:

LTE

<!--NI_TOPIC bundle=rfmx-waveform-creator path=wcdma-3gpp-fdd-release-8.html language=enus -->
## TOPIC 00148: WCDMA (3GPP FDD Release 8)

- bundle_id: `rfmx-waveform-creator`
- source_path: `wcdma-3gpp-fdd-release-8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/wcdma-3gpp-fdd-release-8.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creates a waveform that simulates a 3GPP FDD carrier. The 3GPP has taken the Japanese and UMTS trial versions of WCDMA systems to derive the current system referred to as 3GPP WCDMA. Currently supports the frequency division duplex (FDD) mode. The modulation scheme is defined in the 3GPP TS 25.213 V

### WCDMA (3GPP FDD Release 8)

Creates a waveform that simulates a 3GPP FDD carrier.

The 3GPP has taken the Japanese and UMTS trial versions of WCDMA systems to derive the
 current system referred to as 3GPP WCDMA. Currently supports the frequency division
 duplex (FDD) mode. The modulation scheme is defined in the *3GPP TS 25.213
 V8.5.0* and *TS 25.211 V8.7.0* specifications.

The chip rate of 3GPP FDD systems is 3.84 Mchips per second. The frame length is 10 ms, with 15 slots defined per frame. The channel
 filter is a root raised cosine with an alpha of 0.22.

Note

RFmx Waveform
 Creator

2 ms

Note

Generating and Saving the Waveform
 File

Parent topic:

RFmx Waveform Creator Modulation Schemes

Related information:

- RFmx WCDMA .NET Reference
- RFmx WCDMA C API Reference

<!--NI_TOPIC bundle=rfmx-waveform-creator path=wcdma-references.html language=enus -->
## TOPIC 00149: WCDMA References

- bundle_id: `rfmx-waveform-creator`
- source_path: `wcdma-references.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/wcdma-references.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: 3GPP TS 25 211 V8.7.0 Physical channels and mapping of transport channels onto physical channels (FDD) 3GPP TS 25 212 V8.8.0 Multiplexing and channel coding 3GPP TS 25.213 V8.5.0 Spreading and modulation (FDD) 3GPP TS 25.214 V8.13.0 Physical layer procedures (FDD) 3GPP TS 25.215 V6.4.0 Measurements

### WCDMA References

| 3GPP TS 25 211 V8.7.0 | Physical channels and mapping of transport channels onto physical channels (FDD) |
| --- | --- |
| 3GPP TS 25 212 V8.8.0 | Multiplexing and channel coding |
| 3GPP TS 25.213 V8.5.0 | Spreading and modulation (FDD) |
| 3GPP TS 25.214 V8.13.0 | Physical layer procedures (FDD) |
| 3GPP TS 25.215 V6.4.0 | Measurements (FDD) |
| 3GPP TS 25.101 V8.16.0 | UE Radio transmission and Reception (FDD) |
| 3GPP TS 25.141 V8+.15.0 | Base Station (BS) Conformance Testing (FDD) |

Parent topic:

WCDMA (3GPP FDD Release 8)

<!--NI_TOPIC bundle=rfmx-waveform-creator path=windowing.html language=enus -->
## TOPIC 00150: Windowing

- bundle_id: `rfmx-waveform-creator`
- source_path: `windowing.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/windowing.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: Windowing for OFDM SignalsOFDM symbols are generated one symbol at a time. When the symbols are combined consecutively, spectral regrowth occurs because of the amplitude and phase discontinuity between the consecutive symbols. Time-domain windowing is performed on OFDM symbols to improve the spectra

### Windowing

#### Windowing for OFDM Signals

OFDM
 symbols are generated one symbol at a time. When the symbols are combined consecutively,
 spectral regrowth occurs because of the amplitude and phase discontinuity between the
 consecutive symbols. Time-domain windowing is performed on OFDM symbols to improve the
 spectral characteristics of the transmitted signal. Thus, spectral regrowth is reduced.
 Transitions between consecutive symbols are smoothed by the following methods:

- Extending the OFDM symbols cyclically based on the Windowing Method 
 property.
  - Starting at Symbol Boundary :
    - Appending the first window length (W) samples of the symbol at the end.
    - Overlapping the cyclic prefix (CP) with samples of the previous symbol and
 overlapping the cyclic suffix with the CP samples of the next symbol.
  - Centered at Symbol Boundary :
    - Appending the first W/2 samples of the symbols at the end and suffix W/2 samples
 before CP at the beginning.
    - Overlapping the extended CP with the samples of the previous symbol and
 overlapping the cyclic suffix with the samples of the CP of the next symbol.
- Applying windowing to the beginning and end of the OFDM symbol. Two windows are applied,
 with one window being the mathematical inverse of the other.
- Applying the first cosine window, which rolls over from 0 to 1, over the window length
 of samples from the beginning of the symbol after cyclic extension.
- Applying the second cosine window, which rolls over from 1 to 0, over the last window
 length of samples after cyclic extension.
- After applying windowing to all the OFDM symbols, adding the overlapped segments of the
 current symbol and the previous symbol, as well as the overlapped segments of the current
 symbol and the next symbol to maintain the required OFDM symbol length.

The windowing algorithm is controlled by the *Window Length* and
 *Windowing Method* properties. The selected window shape is a raised-cosine
 window. The shape and length of the window relative to an OFDM symbol length, along with the
 shaping procedure, are shown in the following image.

[IMAGE alt='image' src='GUID-A27865DF-720A-4DF2-BB34-B27F504DBF59-a5.gif']

1. Normal Symbol with Cyclic Prefix (CP)
2. Symbol Cyclically Extended by Window-half-length Samples from Each Side
3. Extended Symbol Shaped by Window
4. Superposition by Summation of Successive Symbols
5. Window-half-length
6. OFDM Symbol Length

#### Windowing for DSSS Signals

For direct sequence spread spectrum (DSSS)
 signals, windowing ensures power ramp up and down for the entire burst. The rising half of
 the cosine window is applied at the beginning of the burst and the falling half of the
 window is applied at the end of the burst. The length of the window is specified by the
 *Window Length* property.

The following figure represents the windowing
 for DSSS signals.

[IMAGE alt='image' src='GUID-B21E201B-B5CF-4245-A890-6923D89F5F28-a5.gif']

Parent topic:

WLAN

<!--NI_TOPIC bundle=rfmx-waveform-creator path=wlan.html language=enus -->
## TOPIC 00151: WLAN

- bundle_id: `rfmx-waveform-creator`
- source_path: `wlan.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/wlan.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a waveform that simulates a WLAN carrier. The following sections describe how to create WLAN waveforms that conform to the IEEE 802.11 specifications. This document assumes that you are familiar with the IEEE 802.11 specifications.

### WLAN

Creates a waveform that simulates a WLAN carrier.

IEEE 802.11

Note

- [Setting Up PXI Trigger Lines for Multiple VSTs](setting-up-pxi-trigger-lines-for-multiple-vst.html)
- [Configuring Active Channels (LabVIEW)](configuring-active-channels-labview2.html)
- [Configuring Active Channels (LabWindows™/CVI™)](configuring-active-channels-labwindows-cvi2.html)
- [RFSG Database](rfsg-database.html)
- [Windowing](windowing.html)
- [Trigger Frame Generation](trigger-frame-generation.html)
- [Configuring LO Connection in WLAN Generation Soft Front Panel](configuring-lo-connection-in-wlan-generation.html)

Parent topic:

RFmx Waveform Creator Modulation Schemes

Related information:

- RFmx WLAN Generation LabVIEW API Reference
- RFmx WLAN Generation C API Reference

<!--NI_TOPIC bundle=rfmx-waveform-creator path=zoom.html language=enus -->
## TOPIC 00152: Zoom

- bundle_id: `rfmx-waveform-creator`
- source_path: `zoom.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-waveform-creator/raw/resource/enus/zoom.html
- document_id: `rfmx-waveform-creator`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Zoom facility is available for all graph types. The current zoom can be operated by using the Zoom option on the sub-menu bar or by the right-clicking on the main graph graticule. The Zoom sub-menu enables you to zoom-in, zoom-out, reset zoom, and zoom into a section of the graph. Auto-scale To

### Zoom

The Zoom facility is available for all graph types. The current zoom can be operated by
 using the Zoom option on the sub-menu bar or by the
 right-clicking on the main graph graticule.

The Zoom sub-menu enables you to zoom-in, zoom-out, reset zoom,
 and zoom into a section of the graph.

[IMAGE alt='image' src='GUID-021A1CBA-1FD3-4871-B43D-ECA7FB72289D-a5.png']

#### Auto-scale

To ensure that the entire signal is visible click the Zoom menu at
 the top of the panel and select the Auto-Scale option. This will
 automatically scale the Y axis of the trace to a factor of 2, 5, or 10 in a way that
 will ensure that all trace data is retained.

#### Change Scale

To change the X and Y axis scales for a given graph, click the
 Zoom menu at the top of the panel and select the
 Change Scale option. This prompts the scaling screen as shown
 in the following image:

[IMAGE alt='image' src='GUID-C89FD8C8-43A2-4B80-957D-7C1769B44775-a5.png']

The way you specify the scale of the X and Y axes depends on the type of data that the
 active graph is displaying. The different methods are as follows:

Frequency: Center, Span

Use this to specify a scale in terms of a center point and a span.

Power: Reference, Scale/Division

Use this to specify a scale in terms of a reference, which is the maximum value of the
 display, and value for each division of the graph.

Minimum/Maximum

Use this to specify a scale in terms of a start and stop limit.

Axis Limits

There are normally limits on the scales you can enter on this screen, and these depend on
 the measurement that is being made.

#### Zooming In

To zoom in on the information displayed on the Graph display panel, click
 Zoom, then click Zoom In (x2). This
 zooms in by a factor of 2.

[IMAGE alt='image' src='GUID-0C270129-5167-4610-A70C-89647CFA1465-a5.png']

To select a region to zoom, click Zoom from the menu at the top of
 the panel and click the Selection option. Notice that the graph
 now displays the co-ordinates of the mouse cursor. To zoom in on a region of the display
 graph, click and hold the left mouse button and drag it to select the region of the
 graph you want to zoom into.

[IMAGE alt='image' src='GUID-81CB4D84-50B2-4207-AF93-112F0FA2BF77-a5.png']

After the zoom has been completed, the graph display reverts to its default selection
 mode.

#### Zooming Out

To zoom out, click the Zoom menu at the top of the panel and
 select the Zoom Out (x2) option. This causes the graph display to
 zoom out on the x-axis by a factor of 2, maintaining the current central point. If the
 graph display cannot achieve this zoom factor, as doing so exceeds the graph's maximum
 scale limits, the maximum possible scale is set instead.

#### Zoom Selection

This control lets you zoom into a section of the graph. This control provides the ability
 to select a region in both the X and Y domain. Immediately after this region is
 selected, the graph will be readjusted to the selected area.

Select the Zoom Selection control. Left click and drag the cursor
 to produce a square or rectangle. Once the required area is selected let go of cursor to
 see the changes. This can be seen in the following figure.

[IMAGE alt='image' src='GUID-8EE81FBD-C893-4966-8933-EE9CC0BF065A-a5.png']

[IMAGE alt='image' src='GUID-A2323AF1-5657-4DB5-80C8-086AF8A27508-a5.png']

#### Selection

For non-polar plots, the Zoom selection feature allows you to
 select a region of the graph in the X domain. When this option is selected, you can
 click and drag the mouse in the graph to select a region of the graph as shown in the
 following figure.

[IMAGE alt='image' src='GUID-08536CE5-E67E-4E0C-A9C3-07A7D7AB68D9-a5.png']

The region will stay selected until this option is de-selected.

When a particular region is selected, you can then right-click the selection to where you
 will be presented with a Zoom to this selection feature as shown
 figure.

When this option is selected, the trace will be zoomed to the specific selected area.

#### Reset Zoom

Resets the zoom factor of the current graph’s X and
 Y axes to their default values.
