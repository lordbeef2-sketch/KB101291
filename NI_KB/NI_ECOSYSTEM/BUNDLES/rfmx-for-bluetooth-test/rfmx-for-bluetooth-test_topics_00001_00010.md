# NI DOCUMENT BUNDLE: rfmx-for-bluetooth-test

<!--NI_BUNDLE_CHUNK bundle=rfmx-for-bluetooth-test start=1 end=10 -->
<!--NI_TOPIC bundle=rfmx-for-bluetooth-test path=acp.html language=enus -->
## TOPIC 00001: Adjacent Channel Power

- bundle_id: `rfmx-for-bluetooth-test`
- source_path: `acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test/raw/resource/enus/acp.html
- document_id: `rfmx-for-bluetooth-test`
- page_type: `leaf`
- content_type: `concept`
- source_description: The adjacent channel power (ACP) measurement covers three standard defined test cases: ACP, EDR In-Band Emission, and LE In-Band Emission. You can set appropriate Packet Type property values to execute the three test cases. The following table illustrates the Packet Type property values, their corre

### Adjacent Channel Power

The adjacent channel power (ACP) measurement covers three standard defined test cases: ACP, EDR In-Band Emission, and LE In-Band Emission.

You can set appropriate Packet Type property values to execute the three test cases. The following table illustrates the Packet Type property values, their corresponding test cases, and test specifications using the ACP measurement.

| Packet Type Value | Test Case | Test Specification |
| --- | --- | --- |
| DH1/DH3/DH5/DM1/DM3/DM5 | ACP | RF/TRM/CA/BV-06-C of the Bluetooth Test Specification RF.TS.p33 |
| 2-DH1/2-DH3/2-DH5/3-DH1/3-DH3/3-DH5/2-EV3/2-EV5/3-EV3/3-EV5 | EDR In-Band Emission | RF/TRM/CA/BV-13-C of the Bluetooth Test Specification RF.TS.p33 |
| LE | LE In-Band Emission | RFPHY/TRM/BV-03-C and RFPHY/TRM/BV-08-C of the Bluetooth Test Specification RFPHY.TS.p23 |

- ACP Results Meas Status
- ACP Results Reference Channel Pwr (dBm)
- ACP Results Lower Offset Abs Pwr (dBm)
- ACP Results Lower Offset Rel Pwr (dB)
- ACP Results Lower Offset Margin (dB)
- ACP Results Upper Offset Abs Pwr (dBm)
- ACP Results Upper Offset Rel Pwr (dB)
- ACP Results Upper Offset Margin (dB)

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test path=df1-and-df2.html language=enus -->
## TOPIC 00002: df1 and df2

- bundle_id: `rfmx-for-bluetooth-test`
- source_path: `df1-and-df2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test/raw/resource/enus/df1-and-df2.html
- document_id: `rfmx-for-bluetooth-test`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Bluetooth standards, Basic Rate (BR) and Low Energy (LE), the packets use Gaussian Frequency Shift Keying (GFSK) modulation scheme. Modulation accuracy of the Bluetooth transmitters that generate BR and LE packets are validated by verifying the frequency deviation values. To realize the frequency

### df1 and df2

In Bluetooth standards, Basic Rate (BR) and Low Energy (LE), the packets use Gaussian Frequency Shift Keying (GFSK) modulation scheme. Modulation accuracy of the Bluetooth transmitters that generate BR and LE packets are validated by verifying the frequency deviation values.

To realize the frequency measurement, it is required that the device under test (DUT) is set to
 generate the BR or LE packet with the maximum supported payload length and have 8-bit payload
 pattern 10101010 or 11110000 depending on the measurements type. The frequency deviation
 corresponding to the 11110000 pattern is called df1 measurement and the frequency deviation
 corresponding to the 10101010 pattern is called df2 measurement.

The Bluetooth Special Interest Group (SIG) specifies the required values of the frequency
 deviation for the two payload patterns, 10101010 and 11110000. The frequency deviation
 limits also depend on whether the packet belongs to LE standard or BR standard. For the
 frequency deviation limits on BR packet, refer to test case 07-C in the section 4.5 of the
 Bluetooth Test specification RF.TS.p33. For the frequency deviation limits on LE packet,
 refer to the test cases RFPHY/TRM/BV-05-C, RFPHY/TRM/BV-10-C and RFPHY/TRM/BV-13-C in
 section 4.6.3 of the *Bluetooth Test Specification RFPHY.TS.p23.*

#### RFmx Relevant Results

The relevant results provided by the RFmx measurements are as follows.

- ModAcc Results df1avg Mean (Hz)
- ModAcc Results df1avg Max (Hz)
- ModAcc Results df1avg Min (Hz)
- ModAcc Results Pk df1max Max (Hz)
- ModAcc Results Min df1max Min (Hz)
- ModAcc Results Percentage of Symbols above df1max Threshold (%)
- ModAcc Results df2avg Mean (Hz)
- ModAcc Results df2avg Max (Hz)
- ModAcc Results df2avg Min (Hz)
- ModAcc Results Pk df2max Max (Hz)
- ModAcc Results Min df2max Min (Hz)
- ModAcc Results Percentage of Symbols above df2max Threshold (%)

To perform df1 measurement the DUT transmits BR or LE packet with full payload and 11110000 bit pattern. The tester acquires the signal and determines the zeroth bit position (p0) for each received packet to establish the timing reference for bits in the payload. Once the p0 position of the received packet has been established, the tester calculates the average frequency for each 00001111 8-bit sequence in the payload. The frequency deviation for each bit is determined by taking an average value across these samples. For each second, third, sixth and seventh of the 8 bits, the deviation from the average frequency within bit period is calculated and recorded as df1max. The average of all the df1max deviation values is calculated and recorded as df1avg.

#### df1 Measurement

To perform df1 measurement the DUT transmits the BR or LE packet with full payload and 11110000
 bit pattern. The tester acquires the signal and determines the zeroth bit position (p0) for each
 received packet to establish the timing reference for bits in the payload. Once the p0 position
 of the received packet has been established, the tester calculates the average frequency for
 each "00001111" 8-bit sequence in the payload. The frequency deviation for each bit is
 determined by taking an average value across these samples. For each second, third, sixth and
 seventh of the 8 bits, the deviation from the average frequency within bit period is calculated
 and recorded as df1max. The average of all the df1max deviation values is calculated and
 recorded as df1avg.

Figure 1.

[IMAGE alt='image' src='GUID-B6399F5C-7AA4-44B9-9685-3EFDA9A86AD6-a5.png']

#### df2 Measurement

A similar measurement procedure is performed while the DUT transmits a 10101010 bit pattern.
 However, in this case, for each bit, maximum deviation from the average frequency is found and
 recorded as df2max. The average of all the df2max deviation values is calculated and recorded as
 df2avg. As a result, the maximum frequency deviation df2max and the average frequency deviation
 df2avg are determined for the 01010101 bit pattern. Bluetooth specification requires the measurement
 to be performed over a period of at least 10 packets. In addition to the lowest operating
 frequency the modulation characteristic test should be conducted at mid operating frequency and
 the highest operating frequency of the DUT.

Figure 2.

[IMAGE alt='image' src='GUID-5B021DCF-9A4F-44D3-B22E-90F543B03BD3-a5.png']

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test path=edr-differential-evm.html language=enus -->
## TOPIC 00003: EDR Differential EVM

- bundle_id: `rfmx-for-bluetooth-test`
- source_path: `edr-differential-evm.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test/raw/resource/enus/edr-differential-evm.html
- document_id: `rfmx-for-bluetooth-test`
- page_type: `leaf`
- content_type: `concept`
- source_description: Differential Error Vector Magnitude (DEVM) quantifies the modulation signal quality of the differentially encoded modulated Bluetooth Enhanced Data Rate (EDR) packets. The EDR packet with 2Mbps data rate uses the pi/4QPSK modulation and the EDR packet with 3Mbps data rate uses the 8DPSK modulation.

### EDR Differential EVM

Differential Error Vector Magnitude (DEVM) quantifies the modulation signal quality of the
 differentially encoded modulated Bluetooth Enhanced Data Rate (EDR) packets. The EDR packet with
 2Mbps data rate uses the pi/4QPSK modulation and the EDR packet with 3Mbps data rate uses the
 8DPSK modulation.

As per the Appendix C, Part A, Volume 2 of the *Bluetooth Core Specification v6.0*
 , the differential error vector is defined as the difference between the vectors
 representing consecutive symbols of the transmitted signal. The magnitude of the
 normalized differential error vector is called the DEVM. The DEVM measurement is
 computed on 50us blocks (50 symbols) in the EDR portion of the packet after
 compensating transmitted symbols for carrier frequency error and for ideal carrier
 phase changes.

To get integral number of 50us blocks, set the Payload Length Mode property to Manual and set the spec defined payload lengths. If the number of
 symbols in the EDR portion of the packet is not an integral multiple of 50us, then
 extra symbols will be discarded from the computation. As per test case
 RF/TRM/CA/BV-11-C in section 4.5 of the *Bluetooth Test Specification
 RF.TS.p33* , the payload length requirement for EDR packets and the
 corresponding number of DEVM blocks are as given in the following table.

| # | Packet Type | Payload Length (Bytes) | Number of DEVM Blocks |
| --- | --- | --- | --- |
| 1 | 2-DH1 | 31 | 3 |
| 2 | 2-DH3 | 356 | 29 |
| 3 | 2-DH5 | 656 | 53 |
| 4 | 2-EV3 | 58 | 5 |
| 5 | 2-EV5 | 358 | 29 |
| 6 | 3-DH1 | 11 | 1 |
| 7 | 3-DH3 | 536 | 29 |
| 8 | 3-DH5 | 986 | 53 |
| 9 | 3-EV3 | 88 | 5 |
| 10 | 3-EV5 | 538 | 29 |

#### DEVM Measurement Principle

Figure 3.

[IMAGE alt='image' src='GUID-A77C9D63-7ED4-4CBD-8973-B5A3F027468A-a5.png']

To perform the DEVM measurement, the EDR packet is compensated for the initial frequency
 error ω <sub>i</sub> . In addition, a square-root raised cosine measurement filter with a
 roll-off factor, α of 0.4 and 3 dB bandwidth of ±500 kHz is applied to the EDR portion of the
 packet. The output of the measurement filter is then portioned into 50 us non-overlapping blocks
 starting from the first nominal sync symbol following the reference sync symbol. For each 50 us
 block, the tester calculates the sampling phase ε <sub>0</sub> and frequency error ω <sub>0</sub> for the RMS differential error vector magnitude (DEVM) for the block. These results are
 then used to calculate DEVM for each symbol in the block.

RMS DEVM is computed as:

[IMAGE alt='image' src='GUID-ADB6A5FF-EBFC-4BA6-9911-6C7CFD6F65E6-a5.png']

The Symbol DEVM is computed as:

[IMAGE alt='image' src='GUID-9F9839AC-0FEB-4CCA-8ADE-2C5C3FEF2B19-a5.png']

where,

Q
 <sub>k</sub> ( ε, ω ) is the compensated sequence of the k <sub>th</sub> symbol where the ideal phase changes have been removed and ε (phase)
 and ω (frequency) are chosen optimally to minimize the DEVM

E
 <sub>k</sub> ( ε, ω ) is the differential error sequence of the k <sub>th</sub> symbol and it is defined as { Q
 <sub>k</sub> ( ε, ω )— Q
 <sub>( k-1 )</sub> ( ε, ω )}

N is the number of symbols per block (50 symbols)

ε
 <sub>0</sub> is the sampling phase error used to compute symbol DEVM

ω <sub>0</sub> is the sampling frequency error used to compute symbol DEVM

The corresponding results under ModAcc measurement are Peak RMS DEVM Maximum (%) and RMS DEVM
 Mean (%).

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test path=frequency-error-measurement-basic-rate.html language=enus -->
## TOPIC 00004: Frequency Error Measurement

- bundle_id: `rfmx-for-bluetooth-test`
- source_path: `frequency-error-measurement-basic-rate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test/raw/resource/enus/frequency-error-measurement-basic-rate.html
- document_id: `rfmx-for-bluetooth-test`
- page_type: `leaf`
- content_type: `concept`
- source_description: This section provides information of the various error measurement options and scenarios. Frequency Error Measurements Basic Rate Frequency error measurements are performed on Basic Rate packets as specified in test cases RF/TRM/CA/BV-08-C and RF/TRM/CA/BV-09-C in section 4.5 of the Bluetooth Test S

### Frequency Error Measurement

This section provides information of the various error measurement options and
 scenarios.

#### Frequency Error Measurements
 Basic Rate

Frequency error measurements are performed on Basic Rate packets as specified in
 test cases RF/TRM/CA/BV-08-C and RF/TRM/CA/BV-09-C in section 4.5 of the *Bluetooth Test Specification RF.TS.p33*.

1. For each averaging count j (one packet), the following
 operations are performed.
  1. Frequency Error is computed on Preamble. This is recorded as Initial
 Frequency Error, denoted by ƒ0 j 
 [IMAGE alt='image' src='GUID-F783480D-690F-44BB-81D2-6D3E0EAE6428-a5.png']
  2. Frequency error is computed on each 10-bit group in the payload
 starting from the 2nd bit. These frequency errors are denoted by ƒ kj with k = 1, 2, …, n is the index of the 10-bit group. The maximum difference
 between ƒ kj and ƒ 0j , for all k , is recorded as Peak Frequency Drift. [IMAGE alt='image' src='GUID-28CABBA8-E5E9-4179-BED4-9B3B245CDA44-a5.png']
  3. The maximum difference between ƒ k+5j and ƒ kj , for all k , is recorded as Peak Frequency
 Drift Rate [IMAGE alt='image' src='GUID-C3880F82-8CFD-4DC0-9443-FCB5AA3899C9-a5.png']
2. The value of the Initial Frequency Error that contains the maximum absolute
 value across all averaging counts is returned as the Initial Frequency Error
 Maximum. [IMAGE alt='image' src='GUID-E45AEF3A-1811-444E-9519-23FB0E8342C8-a5.png']
3. The value of the Peak Frequency Drift that contains the maximum absolute value
 across all averaging counts is returned as the Peak Frequency Drift Maximum. [IMAGE alt='image' src='GUID-45517989-AD5D-47AE-87DB-0E131A53D85A-a5.png']
4. The value of the Peak Frequency Drift Rate that contains the maximum absolute
 value across all averaging counts is returned as the Peak Frequency Drift Rate
 Maximum. [IMAGE alt='image' src='GUID-52829027-1054-4070-AFE7-58BEA4013C45-a5.png']

#### Frequency Error Measurements Enhanced Data Rate

Frequency error measurements are performed on Enhanced Data Rate Packets as specified in the
 test case RF/TRM/CA/BV-11-C in section 4.5 of the *Bluetooth Test Specification RF.TS.p33*.

1. For each averaging count j (one packet), the following operations are
 performed.
  1. Frequency Error is computed on the packet header. It is recorded as Header Frequency
 Error and denoted as ωi j . [IMAGE alt='image' src='GUID-31737EAB-23D9-40BA-8070-936749E3DE2E-a5.png']
  2. The Enhanced Data Rate portion of the packet is compensated for ωi j . The
 frequency error is then computed on every 50 µs block of the EDR portion (sync, payload
 Header, EDR payload, trailer and CRC) of the EDR packet. This frequency error is denoted by
 ω0 k,j , where k = 1,2,…, n is the
 index of the 50 µs block.
  3. The sum of frequency error ωi j and ω0 k,j , for all k , is recorded as Frequency Error ωi j + ω0 k,j . [IMAGE alt='image' src='GUID-77FC75E6-1CDB-42F2-9B1F-F12BEADB6527-a5.png']
  4. The maximum value of Frequency ω0 k,j , for all k , is
 recorded as Peak Frequency Error ω0 k,j . [IMAGE alt='image' src='GUID-6169428D-4D84-441C-A61D-8E19F54FD89F-a5.png']
  5. The maximum value of Frequency Error ωi j + ω0 k,j , for all
 k , is recorded as Peak Frequency Error ωi j + ω0 k,j . [IMAGE alt='image' src='GUID-7180FF39-94D0-499D-8420-707F0D337A9D-a5.png']
2. The value of the Header Frequency Error ωi j that results into the maximum
 absolute value across all averaging counts is returned as the Header Frequency Error ωi Maximum. [IMAGE alt='image' src='GUID-E3F3C696-870B-40A9-9D85-0D7AAAD617FC-a5.png']
3. The value of the Peak Frequency Error ω0 j that results into the maximum
 absolute value across all averaging counts is returned as the Peak Frequency Error ω0 Maximum. [IMAGE alt='image' src='GUID-BAD376A7-BDF5-4C2D-80AA-D77B3B134C40-a5.png']
4. The value of the Peak Frequency Error ωi j + ω0 j that results
 into the maximum absolute value across all averaging counts is returned as the Peak Frequency
 Error ωi + ω0 Maximum. [IMAGE alt='image' src='GUID-A7B0FD55-47C9-426A-B541-5DBC0C9C6E5B-a5.png']

#### Low Energy (LE)

##### Low Energy Uncoded without Constant Tone
 Extension (CTE)

Frequency error measurement are performed on LE packets of symbol rate 1Ms/s and 2Ms/s as
 specified in section 4.6.4 of the *Bluetooth Test Specification RFPHY.TS.p23*.

1. For each averaging count j (one packet), the following operations are
 performed:
  1. Frequency Error is computed on Preamble. The result is recorded as Initial Frequency
 Error, denoted by ƒ0 j . [IMAGE alt='image' src='GUID-F783480D-690F-44BB-81D2-6D3E0EAE6428-a5.png']
  2. Frequency error is calculated from the second payload bit. LE packets use 10-bit groups at
 1 Ms/s and 20-bit groups at 2 Ms/s. These frequency errors are denoted by ƒ nj ,
 where n=1, 2, …, k is the payload group index of the LE packet.
  3. The maximum value of ƒ nj , for all n , is recorded as
 Peak Frequency Error . [IMAGE alt='image' src='GUID-890B3F0E-1120-4564-850A-6C8EB594C977-a5.png']
  4. The difference between ƒ 1j and ƒ 0j is recorded as the
 Initial Frequency Drift .
  5. The maximum difference between ƒ nj and ƒ 0j , for n=2, 3, … k , is recorded as Peak Frequency Drift. [IMAGE alt='image' src='GUID-0CEC0164-25DD-417F-B3B9-6350B95BF120-a5.png']
  6. The maximum difference between ƒ nj and ƒ n-5j , for n=6, 7,…k,
 is recorded as Peak Frequency Drift Rate. [IMAGE alt='image' src='GUID-FFE7F765-5BA5-4AA8-AF02-72428CB2F2CA-a5.png']
2. The value of the Peak Frequency Error that contains the maximum absolute value across all
 averaging counts is returned as the Peak Frequency Error Maximum . [IMAGE alt='image' src='GUID-7BC6FE89-C08D-468E-8A12-C28519698197-a5.png']
3. The value of the Initial Frequency Drift that contains the maximum absolute value across
 all averaging counts is returned as the Initial Frequency Drift Maximum . [IMAGE alt='image' src='GUID-EC2B7A87-A2AC-41C9-B87C-DD63A736BE9B-a5.png']
4. The value of the Peak Frequency Drift that contains the maximum absolute value across all
 averaging counts is returned as the Peak Frequency Drift Maximum . [IMAGE alt='image' src='GUID-5EC0C53B-6E23-4131-92FF-EBE3A6041EE9-a5.png']
5. The value of the Peak Frequency Drift Rate that contains the maximum absolute value across
 all averaging count is returned as the Peak Frequency Drift Rate Maximum . [IMAGE alt='image' src='GUID-8C502269-1118-4069-8C68-E705EBB05963-a5.png']

##### Low Energy Uncoded With Constant Tone
 Extension (CTE)

Frequency Error measurement on constant tone extension (CTE) field is performed on LE uncoded
 packets of symbol rate 1 Ms/s and 2 Ms/s as specified in section 4.6.5 of the *Bluetooth
 Test Specification RFPHY.TS.p23*.

1. For each averaging count j (one packet), the following operations
 are performed.
  1. Frequency Error is computed on the Preamble. The result is recorded as Initial
 Frequency Error, denoted by ƒ0 j 
 [IMAGE alt='image' src='GUID-F783480D-690F-44BB-81D2-6D3E0EAE6428-a5.png']
  2. For LE packet of symbol rate 1 Ms/s, Frequency error is computed on 16 bits of the
 payload. This computation starts from the (n+1) th bit of payload where
 n=((Max_Tx_Length*8)-20). For LE packet of symbol rate 2 Ms/s, Frequency Error is computed on
 32 bits of the payload. This computation starts from (n+1) th bit of payload, where
 n=((Max_Tx_Length*8)-36). The first n bits and last 4 bits are
 discarded. The remaining bits are recorded as average center frequency, denoted by ƒ pj . This recorded value is used in the computation of the Initial Frequency Drift.
 Initial Frequency Drift is the RFmx frequency error result property.
  3. The average frequency deviation is computed on each 16 us unit of CTE, starting from
 1st bit of reference period of 16 µs CTE. The average frequency deviation is denoted by ƒ3
 maxij , where i=1, 2, …, k is the index of the 16 µs unit. These frequency
 errors are denoted by ƒsi j . [IMAGE alt='image' src='GUID-6EB95A30-1A79-4020-A31F-5905089EFA3A-a5.png'] 
 For computation of dƒ1 <sub>avg</sub> , refer to the df1 and df2
 concept topic.
  4. The maximum difference between ƒ3 maxij and dƒ1 avg <sub>j</sub> , for all i , is recorded as Peak Frequency Error. [IMAGE alt='image' src='GUID-BC561487-B2B6-4A20-A69D-A6CF1DC3CDFE-a5.png']
  5. The difference between ƒs1 j and ƒ pj is recorded as Initial
 Frequency Drift. [IMAGE alt='image' src='GUID-26DB3BAB-E341-4D9D-89A8-3886514971AF-a5.png']
  6. The maximum difference between ƒsi j and ƒ0 j for all
 i , is recorded as Peak Frequency Drift. [IMAGE alt='image' src='GUID-7012E7ED-3088-4F3C-A443-FEFB841A0E1F-a5.png']
  7. The maximum difference between ƒs1 j and ƒs(i-3) j , for
 i=4,5,..k, is recorded as Peak Frequency Drift Rate. [IMAGE alt='image' src='GUID-50F1DF29-139D-4B06-9C0F-A0E140316435-a5.png']
2. The value of the Peak Frequency Error that contains the maximum absolute value across all
 averaging counts is returned as the Peak Frequency Error Maximum . [IMAGE alt='image' src='GUID-58BE0D92-161E-473F-8A80-6BC7396F9688-a5.png']
3. The value of the Initial Frequency Drift that contains the maximum absolute value across
 all averaging counts is returned as the Initial Frequency Drift Maximum . [IMAGE alt='image' src='GUID-F03FE0FC-4AB7-447E-A622-59AC08FFDD20-a5.png']
4. The value of the Peak Frequency Drift that contains the maximum absolute value across all
 averaging counts is returned as the Peak Frequency Drift Maximum . [IMAGE alt='image' src='GUID-6A916626-D78C-462C-BCF1-F0E84AB21B60-a5.png']
5. The value of the Peak Frequency Drift Rate that contains the maximum absolute value
 across all averaging count is returned as the Peak Frequency Drift Rate
 Maximum . [IMAGE alt='image' src='GUID-60C75A7F-1B47-45DE-86C0-16E552AC1E69-a5.png']

##### Low Energy Coded (S=8)

Frequency error measurement are performed on Low Energy Coded (S=8) packets of symbol rate
 125Kbps as specified in section 4.6.4 of the *Bluetooth Test Specification
 RFPHY.TS.p23*.

1. For each averaging count j (one packet), the following operations are performed.
  1. Frequency Error is computed on each group of 16 symbols in the preamble field starting
 at the third symbol. The last 14 symbols of the preamble are discarded. These frequency
 errors are recorded as ƒ0 j , ƒ1 j , ƒ2 j , and ƒ3
 j , with ƒ0 j being the Initial Frequency Error. [IMAGE alt='image' src='GUID-F783480D-690F-44BB-81D2-6D3E0EAE6428-a5.png']
  2. The computation skips the first 26 symbols of the payload, then starts computing
 frequency error on each remaining 16-symbol group of the payload. This computation starts
 starting at the 27th symbol in the payload. These frequency errors are denoted by ƒ nj , where n=4,5,…,k is the index of the 16-symbol group.
  3. The maximum value of ƒ nj , for all n , is recorded
 as Peak Frequency Error. [IMAGE alt='image' src='GUID-94033810-4DC1-4FD6-8945-2D48F5FD9DEE-a5.png']
  4. The maximum difference between ƒ nj and ƒ 0j , for all
 n , is recorded as Peak Frequency Drift. [IMAGE alt='image' src='GUID-DBE8B334-7D08-4B99-8CB7-AF01591A0B41-a5.png']
  5. The maximum difference between ƒ nj and ƒ n-3j for n=3 &
 7,8,…,k, is recorded as the Peak Frequency Drift Rate. [IMAGE alt='image' src='GUID-85027621-C80D-4236-B0E4-7361FA7FE4B5-a5.png']
2. The value of the Peak Frequency Error that contains the maximum absolute value across all
 averaging counts is returned as the Peak Frequency Error Maximum. [IMAGE alt='image' src='GUID-F022FB4A-2304-48C3-9D85-7B3872C76B0C-a5.png']
3. The value of the Peak Frequency Drift that contains the maximum absolute value across all
 averaging counts is returned as the Peak Frequency Drift Maximum. [IMAGE alt='image' src='GUID-E4F98DE3-E995-44CE-91B7-EDCB428603F7-a5.png']
4. The value of the Peak Frequency Drift Rate that contains the maximum absolute value
 across all averaging counts is returned as the Peak Frequency Drift Rate Maximum. [IMAGE alt='image' src='GUID-3987E7C7-3E44-4E41-ADBD-C7F40AE41F9B-a5.png']

##### Low Energy High Data Throughput
 (LE-HDT)

Frequency error measurement are performed on format0 and
 format1 packet format for all data rate configurations.

1. For each averaging count j (one packet), the following operations
 are performed:
  - Frequency error is computed across all preamble samples and is recorded as
 Preamble Frequency Error ω<sub>0,j</sub> . All packet samples are
 compensated for ω<sub>0,j</sub> . [IMAGE alt='image' src='GUID-A7AD0B9C-878C-4D2B-BC45-AAD476D185EE-a5.png']
  - After compensating for ω<sub>0,j</sub> , frequency error is computed
 over the payload samples and is recorded as Payload Frequency Error
 ω<sub>1,j</sub> . Payload samples of the packet are compensated for
 ω<sub>1,j</sub> . [IMAGE alt='image' src='GUID-D6A681C8-6A2E-41D9-AC20-737C17DE2DC1-a5.png']
  - The sum of frequency error ω<sub>0,j</sub> and
 ω<sub>1,j</sub> is recorded as Frequency Error
 ω<sub>0,j</sub> + ω<sub>1,j</sub> . [IMAGE alt='image' src='GUID-26C17182-12DD-4E5F-BF7E-7DB6A74021A0-a5.png']
2. The value of the Preamble Frequency Error ω<sub>0,j</sub> that contains
 the maximum absolute value across all averaging counts is returned as the Preamble
 Frequency Error ω<sub>0</sub> Maximum . [IMAGE alt='image' src='GUID-C67C0C9F-5C18-49BB-8D5D-25598CF6B86C-a5.png']
3. The value of the Payload Frequency Error ω<sub>1,j</sub> that contains
 the maximum absolute value across all averaging counts is returned as the Payload
 Frequency Error ω<sub>1</sub> Maximum . [IMAGE alt='image' src='GUID-61703F29-F93C-42F6-BB54-46C7D9488024-a5.png']
4. The value of the Frequency Error ω<sub>0,j</sub> + ω<sub>1,j</sub> that
 contains the maximum absolute value across all averaging counts is returned as the
 Frequency Error ω<sub>0</sub> + ω<sub>1</sub> Maximum . [IMAGE alt='image' src='GUID-8FDEE098-6A4E-4BD0-98DE-64149E5C8881-a5.png']

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test path=new-features-and-changes.html language=enus -->
## TOPIC 00005: RFmx for Bluetooth Test New Features and Changes

- bundle_id: `rfmx-for-bluetooth-test`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test/raw/resource/enus/new-features-and-changes.html
- document_id: `rfmx-for-bluetooth-test`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of RFmx for Bluetooth Test. Discover what is new in the latest releases of RFmx for Bluetooth Test.If you cannot find new features and changes for your version, it might not include user-facing updates. Howe

### RFmx for Bluetooth Test
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of RFmx for Bluetooth Test.

RFmx for Bluetooth Test

Note

Release Notes

Related information:

- Software and Driver Downloads

#### RFmx for Bluetooth Test
 2026 Q2 Changes

RFmx for Bluetooth Test 2026 Q2 adds Bluetooth LE HDT ModAcc, TxP, and ACP
 measurements that align with the *HDT RFPHY_Test_CR r08* specification, along
 with automatic detection of standard, packet format, and preamble format (ZC index). This
 release also adds support for the PXIe-5841 with 200 MHz bandwidth

##### New
 Features

This version of RFmx for Bluetooth Test adds
 support for the following features:

- Bluetooth LE HDT ModAcc, TxP and ACP measurements compatible with HDT
 RFPHY_Test_CR r08 test specification.
- Autodetection of Standard for Bluetooth HDT.
- Autodetection of Packet Format as part of Autodetection of Standard.
- Autodetection of Preamble Format (ZC index) for Bluetooth HDT.

##### Behavior Changes

This version of RFmx for Bluetooth Test updates support for the following feature:

- The Zadoff-Chu Index is automatically detected, and the configured property
 value is ignored by default.

##### New
 Hardware Support

This version of RFmx for Bluetooth Test
 adds support for the following hardware:

- PXIe-5841 ( 200 MHz ) bandwidth

#### RFmx for Bluethtooth Test 2026 Q1
 Changes

Learn about new features, behavior changes, and other updates in RFmx for Bluetooth Test 2026 Q1.

- Added support for Bluetooth LE HDT ModAcc, TxP and ACP measurements compatible
 with HDT RFPHY_Test_CR r08 test specification.
- Added support for Tx IQ Origin Offset Correction in ModAcc measurement for
 Bluetooth HDT.
- Added support for Tx IQ Mismatch Correction in ModAcc measurement for Bluetooth
 HDT.
- Added support for Frequency tracking in ModAcc measurement for Bluetooth
 HDT.

#### RFmx for Bluetooth Test 2025 Q4
 Changes

Learn about new features, behavior changes, and other updates in RFmx for Bluetooth Test 2025 Q4.

- Added support for Frequency Error measurement of Bluetooth LE HDT Packets.
- Added support for TxP measurement of Bluetooth LE HDT Format 0 packets with Constant
 Tone Extension.
- Added Python API support.

##### Behavior Changes

- The Payload Length (bytes) for LE HDT packets was updated
 to be the payload zone length including CRC bits.
- The valid range for Payload Length (bytes) was updated as
 follows:
  - For Format0 , 0 - 514 (previously 0 – 510).
  - For Format1 , 0–33020 (previously 0–8191).
- When Payload Length Mode is set to
 Auto , the default value of the Payload Length
 (bytes) parameter was updated to 514 for both
 Format0 and Format1 (previously
 510 for Format0 and 8191 for Format1)

#### RFmx for Bluetooth Test 2025 Q3
 Changes

Learn about new features, behavior changes, and other updates in RFmx for Bluetooth Test 2025 Q3.

- Added support for Self-Cal Validity Check for PXIe-5860.
- Added support for Bluetooth LE HDT ModAcc, TxP and ACP measurements compatible with
 HDT RFPHY_Test_CR r06test specification.
- Added support for varying Zadoff-Chu index in Bluetooth LE HDT ModAcc and TxP
 measurement.

#### RFmx for Bluetooth Test 2025 Q2
 Changes

Learn about new features, behavior changes, and other updates in RFmx for Bluetooth Test 2025 Q2.

- Added support for Bluetooth LE HDT [High Data Throughput] ModAcc measurement for
 Format 1 packets .
- Added support for Bluetooth LE HDT ModAcc, TxP and ACP measurements compatible with
 HDT RFPHY_Test_FIPD_r06 test specification.

#### RFmx for Bluetooth Test 2025 Q1
 Changes

Learn about new features, behavior changes, and other updates in RFmx for Bluetooth Test 2025 Q1.

- Added support for Bluetooth® LE HDT [High Data Throughput] ModAcc measurement for
 Format 0 packets.

#### RFmx for Bluetooth Test 2024 Q4
 Changes

Learn about new features, behavior changes, and other updates in RFmx for Bluetooth Test 2024 Q4.

- Bluetooth LE Channel Sounding standard complies with Core Specification version
 6.0 and Test Suite RFPHY.TS.p22.
- Added support for Bluetooth LE HDT [High Data Throughput] ACP Measurement.
- Added support for Bluetooth LE HDT TxP measurement.

##### Behavior Changes

- Uninstalling RFmx Bluetooth Test software also removes any previous versions of RFmx
 Bluetooth® Test .NET runtimes that were leaked in .NET Global Assembly Cache
 directory.

#### RFmx for Bluetooth Test 2024 Q3
 Changes

Learn about new features, behavior changes, and other updates in RFmx for Bluetooth Test 2024 Q3.

##### New Hardware Support

- Added support for PXIe-5860.

#### RFmx for Bluetooth Test 2024 Q2
 Changes

Learn about new features, behavior changes, and other updates in RFmx for Bluetooth Test 2024 Q2.

- Added support for Modulation spectrum measurement for Bluetooth Channel Sounding
- Added support for df1/df2 measurement for Bluetooth Channel Sounding
- Added support for Transmit Antenna Switching Integrity for Bluetooth Channel
 Sounding
- Added support for measurement updates for Bluetooth Channel Sounding BT=2.0.
- Added support for measurement updates for Bluetooth LE based Hyperlength.

##### Behavior Changes

- Obsoleted the RFmxInstr Load All Configurations VI. Use the
 RFmxInstr Load Configurations VI along with the
 appropriate RFmxInstr Load Options property, instead.

#### RFmx for Bluetooth Test 2024 Q1
 Changes

Learn about new features, behavior changes, and other updates in RFmx for Bluetooth Test 2024 Q1.

- Added support for PowerRamp measurements for channel sounding packets.
- Implemented clock drift estimate improvements for channel sounding packets.

#### RFmx for Bluetooth Test 2023 Q4
 Changes

Learn about new features, behavior changes, and other updates in RFmx for Bluetooth Test 2023 Q4.

- Added support for Channel Sounding version of Bluetooth physical layer conforming to the
 Bluetooth Core Channel Sounding CR (July 2023), and the Bluetooth Channel Sounding
 Test spec r04 (April 2023).
  - Support for Frequency Error, Clock Drift, and Preamble start time as part of
 Demodulation for Channel Sounding packets.
  - Support for Detrended Phase trace and CS Tone Amplitude/Phase trace as part
 of Channel Sounding Phase measurements.
  - Support for TxP for Channel Sounding packets.
- Added support for obtaining unprocessed I/Q data utilized for RFmx measurements.

#### RFmx for Bluetooth Test 2023 Q3
 Changes

Learn about new features, behavior changes, and other updates in RFmx for Bluetooth Test 2023 Q3.

- Added support for saving and loading RFmx configurations into/from rfmxconfig files.
  - Load from TDMS is supported.
  - Save into TDMS files is discontinued.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test path=packet-type-support-for-bluetooth-measurements.html language=enus -->
## TOPIC 00006: Packet Type Support for Bluetooth Measurements

- bundle_id: `rfmx-for-bluetooth-test`
- source_path: `packet-type-support-for-bluetooth-measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test/raw/resource/enus/packet-type-support-for-bluetooth-measurements.html
- document_id: `rfmx-for-bluetooth-test`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists various Bluetooth measurements and the supported packet types corresponding to each measurement. Packet Type TxP ACP 20dB Bandwidth Frequency Range CS Demod and Phase CS ModSpectrum CS Power Ramp ModAcc df1 df2 DEVM Frequency Error df3 df4 HDT EVM DH1 Y Y Y Y - - - Y Y - Y

### Packet Type Support for Bluetooth Measurements

The following table lists various Bluetooth measurements and the supported packet types corresponding to each measurement.

| Packet Type | TxP | ACP | 20dB Bandwidth | Frequency Range | CS Demod and Phase | CS ModSpectrum | CS Power Ramp | ModAcc |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | df1 | df2 | DEVM | Frequency Error | df3 | df4 | HDT EVM |
| DH1 | Y | Y | Y | Y | - | - | - | Y | Y | - | Y | - | - | - |
| DH3 | Y | Y | Y | Y | - | - | - | Y | Y | - | Y | - | - | - |
| DH5 | Y | Y | Y | Y | - | - | - | Y | Y | - | Y | - | - | - |
| DM1 | Y | Y | Y | Y | - | - | - | Y | Y | - | Y | - | - | - |
| DM3 | Y | Y | Y | Y | - | - | - | Y | Y | - | Y | - | - | - |
| DM5 | Y | Y | Y | Y | - | - | - | Y | Y | - | Y | - | - | - |
| 2-DH1 | Y | Y | - | - | - | - | - | - | - | Y | Y | - | - | - |
| 2-DH3 | Y | Y | - | - | - | - | - | - | - | Y | Y | - | - | - |
| 2-DH5 | Y | Y | - | - | - | - | - | - | - | Y | Y | - | - | - |
| 3-DH1 | Y | Y | - | - | - | - | - | - | - | Y | Y | - | - | - |
| 3-DH3 | Y | Y | - | - | - | - | - | - | - | Y | Y | - | - | - |
| 3-DH5 | Y | Y | - | - | - | - | - | - | - | Y | Y | - | - | - |
| 2-EV3 | Y | Y | - | - | - | - | - | - | - | Y | Y | - | - | - |
| 2-EV5 | Y | Y | - | - | - | - | - | - | - | Y | Y | - | - | - |
| 3-EV3 | Y | Y | - | - | - | - | - | - | - | Y | Y | - | - | - |
| 3-EV5 | Y | Y | - | - | - | - | - | - | - | Y | Y | - | - | - |
| LE 1Mbps | Y | Y | - | - | - | - | - | Y | Y | - | Y | - | - | - |
| LE 2Mpbs | Y | Y | - | - | - | - | - | Y | Y | - | Y | - | - | - |
| LE 125kbps | Y | Y | - | - | - | - | - | Y | - | - | Y | - | - | - |
| LE 500kbps | Y | Y | - | - | - | - | - | - | - | - | - | - | - | - |
| LE-CS-1M | Y | - | - | - | Y | Y | Y | Y | Y | - | Y | Y | Y | - |
| LE-CS-2M | Y | - | - | - | Y | Y | Y | Y | Y | - | Y | Y | Y | - |
| LE-HDT | Y | Y | - | - | - | - | - | - | - | - | - | - | - | Y |

Note

- Y denotes supported by RFmx for Bluetooth® Test
- - denotes measurement is not applicable to this packet

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test path=rfmx-for-bluetooth-test-overview.html language=enus -->
## TOPIC 00007: RFmx for Bluetooth Test Overview

- bundle_id: `rfmx-for-bluetooth-test`
- source_path: `rfmx-for-bluetooth-test-overview.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test/raw/resource/enus/rfmx-for-bluetooth-test-overview.html
- document_id: `rfmx-for-bluetooth-test`
- page_type: `leaf`
- content_type: `concept`
- source_description: This user manual introduces RFmx for Bluetooth Test measurement concepts.

### RFmx for Bluetooth Test Overview

This user manual introduces RFmx for Bluetooth Test measurement
 concepts.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test path=supported-hw.html language=enus -->
## TOPIC 00008: Supported Hardware

- bundle_id: `rfmx-for-bluetooth-test`
- source_path: `supported-hw.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test/raw/resource/enus/supported-hw.html
- document_id: `rfmx-for-bluetooth-test`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx supports a number of NI devices. 1 RFmx for Bluetooth Test Supported Hardware RFmx for Bluetooth Test Hardware Earliest Driver Version Support (Windows 11) PXIe-5646 2022 Q3 PXIe-5668 with PXIe-5698 2022 Q3 PXIe-5820 2022 Q3 PXIe-5840 2022 Q3 PXIe-5841 (1 GHz Bandwidth) 2022 Q3 PXIe-5841 (200 M

### Supported Hardware

RFmx supports a number of NI devices.

| RFmx for Bluetooth Test Hardware | Earliest Driver Version Support (Windows 11) |
| --- | --- |
| PXIe-5646 | 2022 Q3 |
| PXIe-5668 with PXIe-5698 | 2022 Q3 |
| PXIe-5820 | 2022 Q3 |
| PXIe-5840 | 2022 Q3 |
| PXIe-5841 (1 GHz Bandwidth) | 2022 Q3 |
| PXIe-5841 (200 MHz Bandwidth) | 2026 Q2 |
| PXIe-5842 | 2022 Q4 |
| PXIe-5860 | 2024 Q3 |

Note

RFmx for Bluetooth Test

NI-RFSA Properties

NI-RFSA LabVIEW VI Reference

For more information about your hardware and functionality, refer to the *NI-RFSA User
 Manual*.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test path=system-requirements.html language=enus -->
## TOPIC 00009: RFmx for Bluetooth Test System Requirements

- bundle_id: `rfmx-for-bluetooth-test`
- source_path: `system-requirements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test/raw/resource/enus/system-requirements.html
- document_id: `rfmx-for-bluetooth-test`
- page_type: `leaf`
- content_type: `concept`
- source_description: RFmx for Bluetooth Test has the following requirements: Processor—1 GHz 64-bit (x64) processor 4 GB RAM * A screen resolution of 1,024 x 768 Any supported OS, with all available critical updates and service packs * Depending on the amount of data acquired and/or processed, a larger amount of memory

### RFmx for Bluetooth Test System Requirements

RFmx for Bluetooth Test has the following requirements:

- Processor—1 GHz 64-bit (x64) processor
- 4 GB RAM *
- A screen resolution of 1,024 x 768
- Any supported OS, with all available critical updates and service packs

* Depending on the amount of data acquired and/or processed, a larger amount of memory
 may be required.

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test path=user-manual-welcome.html language=enus -->
## TOPIC 00010: RFmx for Bluetooth Test User Manual

- bundle_id: `rfmx-for-bluetooth-test`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test/raw/resource/enus/user-manual-welcome.html
- document_id: `rfmx-for-bluetooth-test`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RFmx for Bluetooth Test User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### RFmx for Bluetooth Test
 User Manual

The RFmx for Bluetooth Test User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download RFmx for Bluetooth Test
- Interactive Activation Guide
- RFmx for Bluetooth Test Release Notes
- Getting Started with RFmx
- RFmx for Bluetooth Test LabVIEW Reference
- RFmx for Bluetooth Test .NET Reference
- RFmx for Bluetooth Test C Reference
- RFmx Instr LabVIEW Reference
- RFmx Instr .NET Reference
- RFmx Instr C Reference
